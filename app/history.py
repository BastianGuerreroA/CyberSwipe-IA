# -*- coding: utf-8 -*-
"""
Módulo de Historial de CyberSwipe-AI.
Responsable de registrar y archivar cada ejecución del pipeline de generación,
creando carpetas numeradas secuencialmente para auditoría y reproducibilidad.
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from app.config import Config
from app.file_manager import FileManager
from app.logger import setup_logger
from app.utils import get_current_timestamp

logger = setup_logger("History")

class HistoryManager:
    """Clase encargada de mantener el registro histórico de las generaciones."""

    def __init__(self, history_dir: Path = Config.HISTORY_DIR):
        self.history_dir = history_dir
        self.history_dir.mkdir(parents=True, exist_ok=True)

    def _get_next_generation_dir(self) -> Path:
        """
        Escanea el directorio de historial y calcula la siguiente ruta secuencial
        (ej: generation_0001, generation_0002).
        """
        existing_dirs = [
            d for d in self.history_dir.iterdir() 
            if d.is_dir() and d.name.startswith("generation_")
        ]
        
        if not existing_dirs:
            next_num = 1
        else:
            numbers = []
            for d in existing_dirs:
                try:
                    num = int(d.name.split("_")[1])
                    numbers.append(num)
                except (ValueError, IndexError):
                    continue
            next_num = max(numbers) + 1 if numbers else 1

        folder_name = f"generation_{next_num:04d}"
        return self.history_dir / folder_name

    def save_generation(
        self,
        prompt: str,
        response_raw: str,
        questions_json: Optional[Dict[str, Any]],
        metadata: Dict[str, Any]
    ) -> Path:
        """
        Crea una nueva carpeta en el historial y guarda todos los artefactos de la generación.
        
        Args:
            prompt (str): Prompt final completo enviado a Ollama.
            response_raw (str): Respuesta cruda obtenida de Ollama.
            questions_json (dict, opcional): El JSON validado resultante (si fue válido).
            metadata (dict): Metadatos del intento (modelo, éxito, errores, tiempos).
            
        Returns:
            Path: Ruta de la carpeta del historial creada.
        """
        gen_dir = self._get_next_generation_dir()
        gen_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Guardando registro histórico de generación en: {gen_dir.name}")

        # 1. Guardar prompt
        FileManager.write_text_file(gen_dir / "prompt.md", prompt)

        # 2. Guardar respuesta cruda
        FileManager.write_text_file(gen_dir / "response.txt", response_raw)

        # 3. Guardar JSON de preguntas si existe (aunque sea inválido, sirve para depurar)
        if questions_json is not None:
            FileManager.write_json_file(gen_dir / "questions.json", questions_json)

        # 4. Guardar metadatos
        FileManager.write_json_file(gen_dir / "metadata.json", metadata)

        return gen_dir
