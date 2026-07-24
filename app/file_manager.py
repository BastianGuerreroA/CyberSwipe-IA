# -*- coding: utf-8 -*-
"""
Módulo de Gestión de Archivos (File Manager) de CyberSwipe-AI.
Responsable de realizar lecturas y escrituras físicas en el sistema de archivos de forma segura.
"""

import json
from pathlib import Path
from typing import Dict, Any, List

class FileManager:
    """Clase encargada de interactuar con el sistema de archivos del proyecto."""

    @staticmethod
    def read_text_file(path: Path) -> str:
        """
        Lee el contenido de un archivo de texto con codificación UTF-8.
        
        Args:
            path (Path): Ruta del archivo.
            
        Returns:
            str: Contenido del archivo.
        """
        if not path.exists():
            raise FileNotFoundError(f"Archivo no encontrado en la ruta: {path}")
        
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def write_text_file(path: Path, content: str) -> None:
        """
        Escribe contenido de texto en un archivo con codificación UTF-8.
        
        Args:
            path (Path): Ruta del archivo.
            content (str): Texto a escribir.
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    @classmethod
    def read_json_file(cls, path: Path) -> Dict[str, Any]:
        """
        Lee un archivo JSON y lo retorna como un diccionario.
        
        Args:
            path (Path): Ruta del archivo.
            
        Returns:
            dict: Datos cargados desde el JSON.
        """
        content = cls.read_text_file(path)
        return json.loads(content)

    @classmethod
    def write_json_file(cls, path: Path, data: Any, indent: int = 4) -> None:
        """
        Escribe datos a un archivo JSON con formato legible.
        
        Args:
            path (Path): Ruta del archivo.
            data (Any): Datos serializables a escribir.
            indent (int): Sangría del JSON resultante.
        """
        content = json.dumps(data, indent=indent, ensure_ascii=False)
        cls.write_text_file(path, content)

    @classmethod
    def list_markdown_files(cls, directory: Path) -> List[Path]:
        """
        Lista todos los archivos con extensión .md dentro de un directorio.
        
        Args:
            directory (Path): Ruta del directorio a escanear.
            
        Returns:
            List[Path]: Lista de rutas de archivos Markdown encontrados.
        """
        if not directory.exists() or not directory.is_dir():
            return []
        return list(directory.glob("*.md"))
