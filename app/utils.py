# -*- coding: utf-8 -*-
"""
Módulo de Utilidades de CyberSwipe-AI.
Contiene funciones auxiliares y utilitarias comunes para todo el proyecto.
"""

from datetime import datetime
import json
import uuid
from typing import Any, Dict

def get_current_timestamp() -> str:
    """
    Retorna la marca de tiempo actual en formato ISO 8601.
    
    Returns:
        str: Marca de tiempo formateada.
    """
    return datetime.utcnow().isoformat() + "Z"

def generate_unique_id(prefix: str = "") -> str:
    """
    Genera un identificador único seguro.
    
    Args:
        prefix (str): Prefijo opcional para el ID.
        
    Returns:
        str: ID único generado.
    """
    uid = str(uuid.uuid4())[:8]  # Tomar los primeros 8 caracteres
    return f"{prefix}_{uid}" if prefix else uid

def pretty_print_json(data: Dict[str, Any]) -> str:
    """
    Formatea un diccionario a formato JSON con sangría.
    
    Args:
        data (dict): Diccionario a formatear.
        
    Returns:
        str: Cadena JSON formateada con sangría.
    """
    return json.dumps(data, indent=4, ensure_ascii=False)

import re

def convert_markdown_to_bbcode(text: str) -> str:
    """
    Convierte formato Markdown (**negrita**, * viñeta) a formato BBCode de Godot ([b]negrita[/b], • viñeta).
    """
    if not isinstance(text, str):
        return text
    # Convertir **negrita** a [b]negrita[/b]
    text = re.sub(r"\*\*(.*?)\*\*", r"[b]\1[/b]", text)
    # Convertir viñetas markdown (* o -) al inicio de línea a viñeta unicode •
    text = re.sub(r"(?m)^(\s*)[\*\-]\s+", r"\1• ", text)
    text = re.sub(r"(\\n|\n)\s*[\*\-]\s+", r"\1• ", text)
    return text

def fix_card_correcto_coherence(capsule_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Verifica y corrige la coherencia matemática del campo 'correcto' (-1.0 vs 1.0) en cada carta
    basándose en la comparación del impacto en las estadísticas de efecto_izquierda vs efecto_derecha.
    """
    if not isinstance(capsule_data, dict):
        return capsule_data

    cartas = capsule_data.get("cartas", [])
    if isinstance(cartas, list):
        for carta in cartas:
            if isinstance(carta, dict):
                ef_izq = carta.get("efecto_izquierda", {})
                ef_der = carta.get("efecto_derecha", {})

                # Sumar beneficios de seguridad y gestión (presupuesto + confidencialidad + integridad + disponibilidad)
                score_izq = ef_izq.get("presupuesto", 0) + ef_izq.get("confidencialidad", 0) + ef_izq.get("integridad", 0) + ef_izq.get("disponibilidad", 0)
                score_der = ef_der.get("presupuesto", 0) + ef_der.get("confidencialidad", 0) + ef_der.get("integridad", 0) + ef_der.get("disponibilidad", 0)

                expected_correcto = 1.0 if score_der > score_izq else -1.0
                carta["correcto"] = expected_correcto

    return capsule_data

def format_capsule_bbcode(capsule_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recorre los campos de texto de una cápsula (contenido_estudio, explicacion)
    y asegura que usen BBCode compatible con Godot RichTextLabel y la coherencia del campo 'correcto'.
    """
    if not isinstance(capsule_data, dict):
        return capsule_data

    if "contenido_estudio" in capsule_data:
        capsule_data["contenido_estudio"] = convert_markdown_to_bbcode(capsule_data["contenido_estudio"])

    if "cartas" in capsule_data and isinstance(capsule_data["cartas"], list):
        for carta in capsule_data["cartas"]:
            if isinstance(carta, dict) and "explicacion" in carta:
                carta["explicacion"] = convert_markdown_to_bbcode(carta["explicacion"])

    # Corregir la coherencia de 'correcto' basada en estadísticas
    capsule_data = fix_card_correcto_coherence(capsule_data)

    return capsule_data
