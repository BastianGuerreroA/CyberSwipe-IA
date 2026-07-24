# -*- coding: utf-8 -*-
"""
Módulo Ollama Client de CyberSwipe-AI.
Responsable de realizar las llamadas HTTP al servicio local de Ollama para la generación de contenido.
"""

import requests
from typing import Dict, Any, Optional
from app.config import Config
from app.logger import setup_logger

logger = setup_logger("OllamaClient")

class OllamaClient:
    """Cliente para comunicarse con la API de Ollama ejecutándose localmente."""

    def __init__(self, host: str = Config.OLLAMA_HOST, model: str = Config.OLLAMA_MODEL):
        self.host = host.rstrip('/')
        self.model = model
        self.generate_url = f"{self.host}/api/generate"

    def generate_response(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None,
        format_schema: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Envía el prompt a la API de Ollama y retorna la respuesta de texto generada.
        
        Args:
            prompt (str): El prompt de usuario con las reglas e información de RAG.
            system_prompt (str, opcional): El prompt del sistema para configurar el comportamiento.
            format_schema (dict, opcional): Esquema opcional.
            
        Returns:
            str: Respuesta cruda del modelo.
        """
        options: Dict[str, Any] = {
            "temperature": Config.OLLAMA_TEMPERATURE,
            "num_ctx": Config.OLLAMA_NUM_CTX,
            "num_gpu": Config.OLLAMA_NUM_GPU
        }
        if Config.OLLAMA_NUM_PREDICT > 0:
            options["num_predict"] = Config.OLLAMA_NUM_PREDICT

        payload: Dict[str, Any] = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": options
        }
        
        if system_prompt:
            payload["system"] = system_prompt

        if format_schema:
            payload["format"] = format_schema
        else:
            payload["format"] = "json"

        try:
            logger.info(f"Enviando solicitud a Ollama ({self.model}) en {self.generate_url}...")
            response = requests.post(self.generate_url, json=payload, timeout=3600)
            response.raise_for_status()
            
            result_json = response.json()
            response_text = result_json.get("response", "")
            return response_text

        except requests.exceptions.RequestException as e:
            logger.error(f"Error de conexión con Ollama en {self.generate_url}: {e}")
            raise ConnectionError(f"No se pudo establecer comunicación con Ollama: {e}")
        except ValueError as e:
            logger.error(f"Error al decodificar la respuesta JSON de Ollama: {e}")
            raise ValueError(f"Respuesta inválida de Ollama: {e}")
