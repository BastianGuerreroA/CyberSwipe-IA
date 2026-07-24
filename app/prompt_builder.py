# -*- coding: utf-8 -*-
"""
Módulo Prompt Builder de CyberSwipe-AI.
Responsable de leer las plantillas de prompts, las reglas y construir el prompt final
unificado para la generación individual de cápsulas con Ollama.
"""

import re
from pathlib import Path
from typing import Dict, Any, List, Optional
from app.config import Config
from app.file_manager import FileManager
from app.logger import setup_logger

logger = setup_logger("PromptBuilder")

class PromptBuilder:
    """Clase encargada de construir y estructurar los prompts para el modelo LLM."""

    def __init__(self, prompts_dir: Path = Config.PROMPTS_DIR):
        self.prompts_dir = prompts_dir

    def _load_prompts_file(self, filename: str) -> str:
        """Carga el archivo de prompt si existe."""
        path = self.prompts_dir / filename
        try:
            return FileManager.read_text_file(path)
        except FileNotFoundError:
            logger.warning(f"Archivo de prompt {filename} no encontrado.")
            return ""

    def _load_references_context(self) -> str:
        """
        Lee de forma incondicional todos los archivos Markdown de la carpeta de referencias
        y los concatena como contexto estructurado para guiar el contenido.
        """
        ref_files = FileManager.list_markdown_files(Config.REFERENCES_DIR)
        if not ref_files:
            logger.info("No se encontraron documentos en el directorio de referencias.")
            return "No hay marcos de referencia o guías externas cargados."

        context_parts = []
        for file_path in ref_files:
            try:
                content = FileManager.read_text_file(file_path)
                context_parts.append(f"### Fuente (Guía de Referencia): {file_path.name}\n\n{content}\n")
                logger.info(f"Referencia Cargada: {file_path.name}")
            except Exception as e:
                logger.error(f"Error al leer la guía de referencia {file_path.name}: {e}")
        
        return "\n---\n".join(context_parts)

    def _load_template_json(self) -> str:
        """Carga la plantilla JSON para incluirla en las reglas de salida."""
        template_path = Config.TEMPLATES_DIR / "questions_template.json"
        try:
            return FileManager.read_text_file(template_path)
        except FileNotFoundError:
            logger.warning("Plantilla questions_template.json no encontrada.")
            return "{}"

    def get_capsules_count(self) -> int:
        """
        Lee el archivo aprendizaje.md y extrae dinámicamente la cantidad de cápsulas a generar.
        
        Returns:
            int: Cantidad de cápsulas requeridas.
        """
        content = self._load_prompts_file("aprendizaje.md")
        match = re.search(r"Numero_capsulas:\s*(\d+)", content)
        if match:
            try:
                count = int(match.group(1))
                logger.info(f"Auto-detectado Numero_capsulas de aprendizaje.md: {count}")
                return count
            except ValueError:
                logger.warning("Error al convertir la cantidad de cápsulas a entero.")
        
        # Si no hay Numero_capsulas pero hay bloques "Cápsula X:", contarlos
        capsules_blocks = re.findall(r"Cápsula\s+(\d+):", content, re.IGNORECASE)
        if capsules_blocks:
            count = len(capsules_blocks)
            logger.info(f"Auto-detectado {count} bloques de cápsulas en aprendizaje.md")
            return count

        logger.warning("No se encontró 'Numero_capsulas' en aprendizaje.md. Usando valor por defecto de 1.")
        return 1

    def parse_capsules_info(self) -> List[Dict[str, Any]]:
        """
        Parsea aprendizaje.md y retorna una lista de información estructurada por cápsula.
        
        Returns:
            List[Dict[str, Any]]: Lista de diccionarios con 'id' y 'topic_text'.
        """
        content = self._load_prompts_file("aprendizaje.md")
        total_count = self.get_capsules_count()
        
        # Buscar bloques delimitados por "Cápsula N:"
        parts = re.split(r"(?=Cápsula\s+\d+:)", content, flags=re.IGNORECASE)
        header_context = parts[0].strip() if parts else ""
        
        result = []
        capsule_pattern = re.compile(r"Cápsula\s+(\d+):", re.IGNORECASE)

        for part in parts[1:]:
            match = capsule_pattern.search(part)
            if match:
                c_id = int(match.group(1))
                title_match = re.search(r"Tema:\s*([^\n\r]+)", part, re.IGNORECASE)
                topic_title = title_match.group(1).strip() if title_match else f"Cápsula {c_id}"
                topic_text = f"{header_context}\n\n{part.strip()}"
                result.append({"id": c_id, "topic_text": topic_text, "topic_title": topic_title})

        # Si no se encontraron bloques explícitos pero se requiere N cápsulas, generar entradas por defecto
        if not result:
            for i in range(1, total_count + 1):
                result.append({"id": i, "topic_text": content, "topic_title": f"Cápsula {i}"})

        return result

    def _build_previous_capsules_context(self, current_capsule_id: int) -> str:
        """
        Lee los archivos de cápsulas generadas anteriormente (< current_capsule_id)
        y construye una lista concisa de temas y conceptos PROHIBIDOS para evitar que el LLM los copie o repita.
        """
        if current_capsule_id <= 1:
            return ""

        previous_info = []
        for c_id in range(1, current_capsule_id):
            capsule_file = Config.CAPSULES_DIR / f"capsule_{c_id:03d}.json"
            if capsule_file.exists():
                try:
                    data = FileManager.read_json_file(capsule_file)
                    c_title = data.get("titulo", f"Cápsula {c_id}")
                    previous_info.append(f"- Cápsula #{c_id} [{c_title}] (TEMAS YA CUBIERTOS - PROHIBIDO REPETIR)")
                except Exception as e:
                    logger.warning(f"No se pudo leer la cápsula previa {capsule_file}: {e}")

        if not previous_info:
            return ""

        summary_str = "\n".join(previous_info)
        return (
            f"## TEMAS DE CÁPSULAS ANTERIORES YA CUBIERTOS (ESTRICTAMENTE PROHIBIDO REPETIR O ADELANTAR):\n"
            f"{summary_str}\n\n"
            f"REGLA DE AISLAMIENTO TEMÁTICO:\n"
            f"Genera los contenidos y las 5 cartas enfocándote ÚNICAMENTE en los objetivos pedagógicos de la Cápsula #{current_capsule_id}.\n"
            f"Está prohibido usar escenarios, vectores o conceptos pertenecientes a las cápsulas anteriores listadas arriba.\n\n"
        )

    def build_system_prompt(self) -> str:
        """Construye el System Prompt completo."""
        return self._load_prompts_file("system_prompt.md")

    def build_single_capsule_prompt(self, capsule_id: int, capsule_topic: str = "", topic_title: str = "") -> str:
        """
        Construye el User Prompt para generar una ÚNICA cápsula específica.
        
        Args:
            capsule_id (int): El ID de la cápsula a generar.
            capsule_topic (str): El contenido específico de tema y objetivos de la cápsula.
            topic_title (str): Título del tema específico para mayor prominencia.
            
        Returns:
            str: El prompt estructurado listo para Ollama.
        """
        generation_rules = self._load_prompts_file("generation_rules.md")
        style_rules = self._load_prompts_file("style_rules.md")
        output_rules = self._load_prompts_file("output_rules.md")
        references_context = self._load_references_context()
        json_template = self._load_template_json()
        previous_capsules_context = self._build_previous_capsules_context(capsule_id)

        title_str = topic_title if topic_title else f"Cápsula #{capsule_id}"

        topic_instruction = f"\n### TEMA Y OBJETIVOS ESPECÍFICOS DE LA CÁPSULA {capsule_id}:\n{capsule_topic}\n" if capsule_topic else ""

        instruction = (
            f"====================================================\n"
            f"GENERACIÓN DE CÁPSULA INDIVIDUAL #{capsule_id}\n"
            f"TEMA OBLIGATORIO DE ESTA CÁPSULA: {title_str}\n"
            f"CANTIDAD DE CARTAS OBLIGATORIA: EXACTAMENTE 5 CARTAS\n"
            f"====================================================\n\n"
            f"REGLAS CRÍTICAS:\n"
            f"1. El campo 'id' DEBE SER EXACTAMENTE {capsule_id}.\n"
            f"2. El campo 'titulo', 'subtitulo', 'mini_descripcion', 'contenido_estudio' y las 5 'cartas' DEBEN tratar EXCLUSIVAMENTE sobre el tema: '{title_str}'.\n"
            f"   PROHIBIDO GENERAR SOBRE TEMAS DE OTRAS CÁPSULAS (por ejemplo: si el tema es 'Identidad Digital y Contraseñas', NO generes nada sobre Phishing, correos falsos ni vishing).\n"
            f"3. PROHIBIDO GENERAR CARTAS BINARIAS U OBVIAS (ej: 'Dar clave' vs 'No dar clave'). Ambas opciones de cada carta deben ser frases completas, plausibles y razonables para un trabajador.\n"
            f"4. DEBES GENERAR UN ARREGLO 'cartas' CON EXACTAMENTE 5 ELEMENTOS INTERACTIVOS, evaluando 5 conceptos clave distintos explicados en el 'contenido_estudio'.\n\n"
        )

        full_prompt = (
            f"{instruction}"
            f"{topic_instruction}\n"
            f"{previous_capsules_context}"
            f"## REGLAS DE GENERACIÓN\n{generation_rules}\n\n"
            f"## REGLAS DE ESTILO\n{style_rules}\n\n"
            f"## GUÍAS Y MARCOS DE REFERENCIA\n{references_context}\n\n"
            f"## REGLAS DE SALIDA Y ESTRUCTURA DE CÁPSULA ÚNICA\n{output_rules}\n\n"
            f"### PLANTILLA DE REFERENCIA JSON (CÁPSULA ÚNICA)\n```json\n{json_template}\n```\n"
        )
        
        return full_prompt

    def build_generation_prompt(self, capsules_count: Optional[int] = None) -> str:
        """
        Método de compatibilidad. Construye el prompt para la cápsula 1.
        """
        return self.build_single_capsule_prompt(capsule_id=1)
