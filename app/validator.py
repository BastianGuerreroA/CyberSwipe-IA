# -*- coding: utf-8 -*-
"""
Módulo de Validación de CyberSwipe-AI.
Responsable de verificar la sintaxis JSON, el cumplimiento del JSON Schema y
las reglas lógicas/semánticas de negocio para la generación individual de cápsulas.
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional
import jsonschema
from app.config import Config
from app.file_manager import FileManager
from app.logger import setup_logger

logger = setup_logger("Validator")

class JSONValidator:
    """Clase encargada de validar la salida JSON del LLM contra el esquema y reglas del negocio."""

    def __init__(self, schema_path: Path = Config.SCHEMA_DIR / "questions_schema.json"):
        self.schema_path = schema_path
        self._schema: Dict[str, Any] = {}

    def get_schema(self) -> Dict[str, Any]:
        """Retorna el esquema JSON cargado."""
        return self._load_schema()

    def _load_schema(self) -> Dict[str, Any]:
        """Carga el JSON Schema desde la ruta configurada."""
        if not self._schema:
            try:
                self._schema = FileManager.read_json_file(self.schema_path)
            except Exception as e:
                logger.error(f"No se pudo cargar el JSON Schema desde {self.schema_path}: {e}")
                raise
        return self._schema

    def _escape_literal_newlines(self, text: str) -> str:
        """Escape saltos de línea reales dentro de valores entre comillas."""
        res = []
        in_str = False
        esc = False
        for ch in text:
            if ch == '"' and not esc:
                in_str = not in_str
                res.append(ch)
            elif ch == '\n' and in_str:
                res.append('\\n')
            elif ch == '\r' and in_str:
                pass
            else:
                res.append(ch)
                esc = (ch == '\\' and not esc)
        return "".join(res)

    def clean_markdown_json(self, raw_text: str) -> str:
        """
        Limpia bloques de código markdown (por ejemplo, ```json ... ```) 
        y extrae únicamente el contenido del objeto JSON principal (desde la primera '{' hasta la última '}').
        """
        text = raw_text.strip()
        
        # Eliminar marcadores markdown de bloque de código
        text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE).strip()
        text = re.sub(r"\s*```$", "", text).strip()
        
        # Extraer el fragmento delimitado por la primera '{' y la última '}'
        first_brace = text.find("{")
        last_brace = text.rfind("}")
        
        if first_brace != -1 and last_brace != -1 and last_brace > first_brace:
            text = text[first_brace:last_brace + 1]
        
        return self._escape_literal_newlines(text)

    def validate_syntax(self, json_str: str) -> Tuple[bool, Optional[Dict[str, Any]], Optional[str]]:
        """
        Intenta parsear el JSON y valida la sintaxis básica.
        
        Returns:
            Tuple: (es_valido, diccionario_datos, mensaje_error)
        """
        try:
            cleaned_str = self.clean_markdown_json(json_str)
            data = json.loads(cleaned_str, strict=False)
            return True, data, None
        except json.JSONDecodeError as e:
            err_msg = f"Error de sintaxis JSON: {e}"
            logger.error(err_msg)
            return False, None, err_msg

    def validate_schema(self, data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Valida los datos JSON contra el JSON Schema de la cápsula individual.
        
        Returns:
            Tuple: (es_valido, lista_de_errores)
        """
        try:
            schema = self._load_schema()
            jsonschema.validate(instance=data, schema=schema)
            return True, []
        except jsonschema.exceptions.ValidationError as e:
            err_msg = f"Fallo en esquema JSON (Ruta: {list(e.path)}): {e.message}"
            logger.warning(err_msg)
            return False, [err_msg]
        except Exception as e:
            err_msg = f"Error inesperado durante validación de esquema: {e}"
            logger.error(err_msg)
            return False, [err_msg]

    def validate_business_rules(self, data: Dict[str, Any], expected_id: Optional[int] = None) -> Tuple[bool, List[str]]:
        """
        Valida reglas semánticas y de negocio personalizadas para una cápsula individual:
        - No existen valores nulos o vacíos en textos clave.
        - ID coincidente si se especifica expected_id.
        - La cápsula contiene al menos una carta.
        - Cada carta posee todas las propiedades requeridas y efectos válidos.
        
        Returns:
            Tuple: (es_valido, lista_de_errores)
        """
        errors = []
        
        # Si por error el LLM envolvió la cápsula en {"capsulas": [...]}, extraer la primera cápsula
        capsula = data
        if "capsulas" in data and isinstance(data["capsulas"], list) and len(data["capsulas"]) > 0:
            capsula = data["capsulas"][0]

        c_id = capsula.get("id")
        c_titulo = capsula.get("titulo", "")
        c_subtitulo = capsula.get("subtitulo", "")
        c_mini = capsula.get("mini_descripcion", "")
        c_contenido = capsula.get("contenido_estudio", "")
        c_estado = capsula.get("estado", "")
        
        # 1. Validar ID
        if c_id is None:
            errors.append("La cápsula no posee ID.")
        elif not isinstance(c_id, int):
            errors.append(f"El ID de la cápsula debe ser entero (recibido: {c_id}).")
        elif expected_id is not None and c_id != expected_id:
            errors.append(f"Se esperaba la cápsula ID {expected_id}, pero se recibió ID {c_id}.")

        # 2. Validar campos de texto principales
        if not isinstance(c_titulo, str) or not c_titulo.strip():
            errors.append("El título de la cápsula está vacío.")
        if not isinstance(c_subtitulo, str) or not c_subtitulo.strip():
            errors.append("El subtítulo de la cápsula está vacío.")
        if not isinstance(c_mini, str) or not c_mini.strip():
            errors.append("La mini descripción de la cápsula está vacía.")
        if not isinstance(c_contenido, str) or not c_contenido.strip():
            errors.append("El contenido de estudio de la cápsula está vacío.")
        if c_estado not in ["Disponible", "Bloqueado"]:
            errors.append(f"Estado de cápsula inválido: {c_estado}. Debe ser 'Disponible' o 'Bloqueado'.")

        # 3. Validar cartas
        cartas = capsula.get("cartas", [])
        if not cartas or not isinstance(cartas, list):
            errors.append("La cápsula no contiene ninguna carta válida.")
        elif len(cartas) != 5:
            errors.append(f"La cápsula debe contener exactamente 5 cartas (recibidas: {len(cartas)}).")
        
        if isinstance(cartas, list):
            for card_idx, carta in enumerate(cartas):
                c_imagen = carta.get("imagen")
                c_contexto = carta.get("contexto", "")
                c_izq = carta.get("texto_izquierda", "")
                c_der = carta.get("texto_derecha", "")
                c_correcto = carta.get("correcto")
                c_explicacion = carta.get("explicacion", "")

                if c_imagen is None or not isinstance(c_imagen, int):
                    errors.append(f"La carta {card_idx} tiene un valor de imagen inválido.")
                if c_correcto is None or c_correcto not in [-1.0, 1.0]:
                    errors.append(f"La carta {card_idx} tiene un valor 'correcto' inválido: {c_correcto}. Debe ser -1.0 o 1.0.")

                if not isinstance(c_contexto, str) or not c_contexto.strip():
                    errors.append(f"La carta {card_idx} tiene un contexto vacío.")
                if not isinstance(c_izq, str) or not c_izq.strip():
                    errors.append(f"La carta {card_idx} tiene un texto izquierdo vacío.")
                if not isinstance(c_der, str) or not c_der.strip():
                    errors.append(f"La carta {card_idx} tiene un texto derecho vacío.")
                if not isinstance(c_explicacion, str) or not c_explicacion.strip():
                    errors.append(f"La carta {card_idx} tiene una explicación vacía.")

                for key, val in carta.items():
                    if val is None:
                        errors.append(f"La propiedad '{key}' en la carta {card_idx} es nula.")

        return len(errors) == 0, errors
