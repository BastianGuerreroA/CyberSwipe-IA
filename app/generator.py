# -*- coding: utf-8 -*-
"""
Módulo Generador de CyberSwipe-AI.
Coordinador del flujo principal del pipeline de generación individual por cápsula.
Ejecuta la construcción de prompts enfocados, llamadas a Ollama, validaciones
y almacenamiento independiente en output/capsules/capsule_XXX.json.
"""

import time
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
from app.config import Config
from app.prompt_builder import PromptBuilder
from app.ollama_client import OllamaClient
from app.validator import JSONValidator
from app.history import HistoryManager
from app.file_manager import FileManager
from app.logger import setup_logger
from app.utils import get_current_timestamp, generate_unique_id, format_capsule_bbcode

logger = setup_logger("Generator")

class QuestionsGenerator:
    """Clase principal que orquesta el ciclo de vida de generación individual de cápsulas."""

    def __init__(self):
        self.config = Config()
        self.prompt_builder = PromptBuilder()
        self.ollama_client = OllamaClient()
        self.validator = JSONValidator()
        self.history_manager = HistoryManager()

    def generate_single_capsule(self, capsule_id: int, topic_text: str = "", topic_title: str = "") -> Tuple[bool, Optional[Dict[str, Any]], List[str]]:
        """
        Genera y valida una ÚNICA cápsula por su ID.
        Reintenta hasta Config.MAX_RETRIES veces si ocurre un fallo.
        Guarda el resultado en output/capsules/capsule_{capsule_id:03d}.json.

        Args:
            capsule_id (int): El ID numérico de la cápsula.
            topic_text (str): Texto del tema y objetivos pedagógicos.
            topic_title (str): Título del tema asignado.

        Returns:
            Tuple[bool, Optional[Dict[str, Any]], List[str]]: (éxito, datos_capsula, lista_errores)
        """
        system_prompt = self.prompt_builder.build_system_prompt()
        prompt = self.prompt_builder.build_single_capsule_prompt(capsule_id=capsule_id, capsule_topic=topic_text, topic_title=topic_title)

        try:
            format_schema = self.validator.get_schema()
        except Exception as e:
            logger.warning(f"No se pudo cargar el esquema para generación estructurada: {e}")
            format_schema = None

        max_retries = Config.MAX_RETRIES
        last_errors = []
        parsed_data = None

        for attempt in range(1, max_retries + 1):
            logger.info(f"--- Generando Cápsula #{capsule_id} (Intento {attempt}/{max_retries}) ---")
            errors = []
            
            try:
                response_raw = self.ollama_client.generate_response(
                    prompt=prompt,
                    system_prompt=system_prompt,
                    format_schema=format_schema
                )

                # 1. Sintaxis
                syntax_ok, parsed_data, syntax_err = self.validator.validate_syntax(response_raw)
                if not syntax_ok:
                    logger.error(f"Respuesta cruda de Ollama (Intento {attempt}):\n{response_raw}\n--- FIN RESPUESTA CRUDA ---")
                    errors.append(syntax_err or "Error al parsear el JSON de salida.")
                else:
                    # Desenvolver en caso de que esté dentro de {"capsulas": [...]}
                    if isinstance(parsed_data, dict) and "capsulas" in parsed_data and isinstance(parsed_data["capsulas"], list) and len(parsed_data["capsulas"]) > 0:
                        parsed_data = parsed_data["capsulas"][0]

                    # 2. Esquema JSON
                    schema_ok, schema_errors = self.validator.validate_schema(parsed_data)
                    if not schema_ok:
                        errors.extend(schema_errors)

                    # 3. Reglas de Negocio
                    business_ok, business_errors = self.validator.validate_business_rules(parsed_data, expected_id=capsule_id)
                    if not business_ok:
                        errors.extend(business_errors)

                if not errors and parsed_data is not None:
                    # Forzar id correcto si no venía en int y formatear a BBCode de Godot
                    parsed_data["id"] = capsule_id
                    parsed_data = format_capsule_bbcode(parsed_data)
                    
                    # Guardar en output/capsules/capsule_00X.json
                    capsule_filename = f"capsule_{capsule_id:03d}.json"
                    capsule_path = Config.CAPSULES_DIR / capsule_filename
                    FileManager.write_json_file(capsule_path, parsed_data)
                    logger.info(f"Cápsula #{capsule_id} guardada exitosamente en {capsule_path}")

                    return True, parsed_data, []
                else:
                    logger.warning(f"Intento {attempt} para Cápsula #{capsule_id} falló con errores: {errors}")
                    last_errors = errors

            except Exception as e:
                err_msg = f"Excepción en la generación de Cápsula #{capsule_id} (Intento {attempt}): {e}"
                logger.error(err_msg)
                last_errors.append(err_msg)

        return False, None, last_errors

    def run_pipeline(self, capsules_count: Optional[int] = None) -> bool:
        """
        Ejecuta el pipeline de generación individual para todas las cápsulas del programa.

        Args:
            capsules_count (int, opcional): Cantidad de cápsulas que se desea generar.
            
        Returns:
            bool: True si todas las cápsulas fueron generadas y guardadas exitosamente.
        """
        self.config.validate()
        generation_id = generate_unique_id("gen")
        start_time = time.time()

        capsules_info = self.prompt_builder.parse_capsules_info()
        if capsules_count is not None and capsules_count > 0:
            capsules_info = capsules_info[:capsules_count]

        total_capsules = len(capsules_info)
        logger.info(f"Iniciando pipeline de generación individual [ID: {generation_id}] para {total_capsules} cápsulas.")

        generated_capsules: List[Dict[str, Any]] = []
        overall_errors: List[str] = []
        success_count = 0

        for idx, info in enumerate(capsules_info):
            c_id = info["id"]
            topic_text = info.get("topic_text", "")
            topic_title = info.get("topic_title", "")
            
            if idx > 0:
                time.sleep(2)
                
            ok, capsule_data, errors = self.generate_single_capsule(capsule_id=c_id, topic_text=topic_text, topic_title=topic_title)
            
            if ok and capsule_data is not None:
                generated_capsules.append(capsule_data)
                success_count += 1
            else:
                err_summary = f"Fallo al generar Cápsula #{c_id}: " + "; ".join(errors)
                logger.error(err_summary)
                overall_errors.append(err_summary)

        duration = time.time() - start_time
        status = "success" if success_count == total_capsules else "partial" if success_count > 0 else "failed"

        # Guardar en latest/questions.json (compilación completa para retrocompatibilidad)
        if generated_capsules:
            compiled_data = {"capsulas": generated_capsules}
            latest_path = Config.LATEST_DIR / "questions.json"
            try:
                FileManager.write_json_file(latest_path, compiled_data)
                logger.info(f"Compilación questions.json actualizada en {latest_path}")
            except Exception as e:
                logger.error(f"No se pudo guardar la compilación latest/questions.json: {e}")

        # Guardar metadatos de auditoría
        metadata = {
            "generation_id": generation_id,
            "timestamp": get_current_timestamp(),
            "model_used": Config.OLLAMA_MODEL,
            "status": status,
            "errors": overall_errors if overall_errors else None,
            "capsules_requested": total_capsules,
            "capsules_generated": success_count,
            "duration_seconds": round(duration, 2)
        }

        self.history_manager.save_generation(
            prompt=f"Generación individual de {total_capsules} cápsulas",
            response_raw=f"Generadas {success_count}/{total_capsules} cápsulas exitosamente",
            questions_json={"capsulas": generated_capsules},
            metadata=metadata
        )

        logger.info(f"=== Pipeline finalizado. Estado: {status} ({success_count}/{total_capsules} cápsulas exitosas en {round(duration, 2)}s) ===")
        return status == "success"
