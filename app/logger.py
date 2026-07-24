"""
Sistema de logging para CyberSwipe-AI.

Permite registrar mensajes tanto en consola como en un archivo de log.
"""

from pathlib import Path
import logging

from rich.console import Console
from rich.logging import RichHandler

from app.config import Config

console = Console()

Config.LOGS_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = Config.LOGS_DIR / "cyberswipe.log"


def get_logger(name: str = "CyberSwipe") -> logging.Logger:

    #Retorna una instancia configurada del logger.
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s - %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )

    # Consola
    console_handler = RichHandler(console=console, show_path=False)
    console_handler.setFormatter(formatter)

    # Archivo
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# Alias para compatibilidad con otros módulos
setup_logger = get_logger