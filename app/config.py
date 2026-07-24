"""
Configuración general del proyecto CyberSwipe-AI.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Config:

    ROOT_DIR = Path(__file__).resolve().parent.parent

    APP_DIR = ROOT_DIR / "app"

    PROMPTS_DIR = ROOT_DIR / "prompts"

    SCHEMA_DIR = ROOT_DIR / "schema"

    TEMPLATE_DIR = ROOT_DIR / "templates"

    REFERENCES_DIR = ROOT_DIR / "references"

    OUTPUT_DIR = ROOT_DIR / "output"

    LOGS_DIR = ROOT_DIR / "logs"

    # Ollama y Modelo
    MODEL_NAME = os.getenv("OLLAMA_MODEL", "gemma4:e2b")
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

    # Parámetros del LLM
    OLLAMA_NUM_CTX = int(os.getenv("OLLAMA_NUM_CTX", "8192"))
    OLLAMA_NUM_PREDICT = int(os.getenv("OLLAMA_NUM_PREDICT", "4096"))
    OLLAMA_TEMPERATURE = float(os.getenv("OLLAMA_TEMPERATURE", "0.1"))
    OLLAMA_NUM_GPU = int(os.getenv("OLLAMA_NUM_GPU", "0"))

    # Valores por defecto para generación
    DEFAULT_CAPSULES = 5
    TEMPERATURE = OLLAMA_TEMPERATURE
    TOP_P = 0.9
    MAX_RETRIES = 3

    # Mapeos de compatibilidad
    TEMPLATES_DIR = TEMPLATE_DIR
    HISTORY_DIR = OUTPUT_DIR / "history"
    LATEST_DIR = OUTPUT_DIR / "latest"
    CAPSULES_DIR = OUTPUT_DIR / "capsules"
    OLLAMA_MODEL = MODEL_NAME
    LOG_LEVEL = "INFO"

    @classmethod
    def validate(cls):

        folders = [
            cls.PROMPTS_DIR,
            cls.SCHEMA_DIR,
            cls.TEMPLATE_DIR,
            cls.OUTPUT_DIR,
            cls.CAPSULES_DIR,
            cls.HISTORY_DIR,
            cls.LATEST_DIR,
            cls.LOGS_DIR,
            cls.REFERENCES_DIR,
        ]

        for folder in folders:
            folder.mkdir(parents=True, exist_ok=True)

        return True