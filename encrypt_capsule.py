# -*- coding: utf-8 -*-

"""
CyberSwipe - Encrypt Capsules

Convierte todas las cápsulas JSON en archivos .lsg
utilizando AES-256-CBC.

También genera un index.json (desarrollo)
y un index.lsg (producción).
"""

import os
import json
import hashlib
from pathlib import Path

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

ROOT = Path(__file__).resolve().parent

INPUT_DIR = ROOT / "output" / "capsules"
OUTPUT_DIR = ROOT / "output" / "encrypted"
KEY_FILE = ROOT / "output" / "keys" / "aes.key"

SAVE_DEBUG_JSON = True


# ==========================================================
# CLAVE AES
# ==========================================================




def load_key():

    KEY_FILE.parent.mkdir(parents=True, exist_ok=True)

    if KEY_FILE.exists():

        key = KEY_FILE.read_bytes()

        if len(key) == 32:
            print(list(key))
            return key

    key = os.urandom(32)

    KEY_FILE.write_bytes(key)

    print("[+] Nueva clave AES creada")
    print(list(key))

    return key


# ==========================================================
# CIFRADO
# ==========================================================

def encrypt_bytes(data: bytes, key: bytes):

    iv = os.urandom(16)

    padder = padding.PKCS7(128).padder()

    padded = padder.update(data)

    padded += padder.finalize()

    cipher = Cipher(

        algorithms.AES(key),

        modes.CBC(iv)

    )

    encryptor = cipher.encryptor()

    encrypted = encryptor.update(padded)

    encrypted += encryptor.finalize()

    return iv + encrypted


# ==========================================================
# GENERAR CAPSULA
# ==========================================================

def encrypt_capsule(json_file: Path, key):

    with open(json_file, "r", encoding="utf-8") as f:

        capsule = json.load(f)

    raw = json.dumps(

        capsule,

        ensure_ascii=False,

        separators=(",", ":")

    ).encode("utf-8")

    payload = encrypt_bytes(raw, key)

    output = OUTPUT_DIR / (json_file.stem + ".lsg")

    output.parent.mkdir(parents=True, exist_ok=True)

    output.write_bytes(payload)

    sha = hashlib.sha256(payload).hexdigest()

    print(f"[OK] {json_file.name}")

    metadata = {

        "id": capsule.get("id"),

        "titulo": capsule.get("titulo"),

        "subtitulo": capsule.get("subtitulo"),

        "mini_descripcion": capsule.get("mini_descripcion"),

        "filename": output.name,

        "sha256": sha,

        "estado": capsule.get("estado", "Disponible")

    }

    return metadata


# ==========================================================
# INDEX
# ==========================================================

def generate_index(metadata, key):

    index = {

        "capsulas": metadata

    }

    if SAVE_DEBUG_JSON:

        with open(

            OUTPUT_DIR / "index.json",

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                index,

                f,

                indent=4,

                ensure_ascii=False

            )

    raw = json.dumps(

        index,

        ensure_ascii=False,

        separators=(",", ":")

    ).encode("utf-8")

    encrypted = encrypt_bytes(raw, key)

    (OUTPUT_DIR / "index.lsg").write_bytes(encrypted)

    print("[OK] index.lsg generado")


# ==========================================================
# MAIN
# ==========================================================

def main():

    print("=== CyberSwipe Encrypt ===")

    key = load_key()

    if not INPUT_DIR.exists():

        print("No existe la carpeta de cápsulas.")

        return

    metadata = []

    for file in sorted(INPUT_DIR.glob("*.json")):

        try:

            metadata.append(

                encrypt_capsule(file, key)

            )

        except Exception as e:

            print(f"[ERROR] {file.name}: {e}")

    generate_index(metadata, key)

    print("\nProceso terminado.")


if __name__ == "__main__":

    main()