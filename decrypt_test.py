# -*- coding: utf-8 -*-

"""
CyberSwipe - Decrypt Test

Valida que los archivos .lsg puedan ser
descifrados correctamente antes de ser
consumidos por Godot.
"""

import json
import hashlib
from pathlib import Path

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

ROOT = Path(__file__).resolve().parent

KEY_FILE = ROOT / "output" / "keys" / "aes.key"

INPUT_DIR = ROOT / "output" / "encrypted"

OUTPUT_DIR = ROOT / "output" / "decrypted_test"


# ==========================================================
# DESCIFRAR
# ==========================================================

def decrypt_bytes(data: bytes, key: bytes) -> bytes:

    iv = data[:16]

    ciphertext = data[16:]

    cipher = Cipher(

        algorithms.AES(key),

        modes.CBC(iv)

    )

    decryptor = cipher.decryptor()

    padded = decryptor.update(ciphertext)

    padded += decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()

    plain = unpadder.update(padded)

    plain += unpadder.finalize()

    return plain


# ==========================================================
# DESCIFRAR ARCHIVO
# ==========================================================

def decrypt_file(lsg_file: Path, key: bytes, expected_hash=None):

    payload = lsg_file.read_bytes()

    if len(payload) < 17:

        raise Exception("Archivo inválido.")

    if expected_hash:

        current = hashlib.sha256(payload).hexdigest()

        if current != expected_hash:

            raise Exception("SHA-256 inválido.")

    decrypted = decrypt_bytes(payload, key)

    json_data = json.loads(

        decrypted.decode("utf-8")

    )

    OUTPUT_DIR.mkdir(

        parents=True,

        exist_ok=True

    )

    output = OUTPUT_DIR / f"{lsg_file.stem}.json"

    with open(

        output,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            json_data,

            f,

            indent=4,

            ensure_ascii=False

        )

    print(f"[OK] {lsg_file.name}")


# ==========================================================
# MAIN
# ==========================================================

def main():

    print("=== CyberSwipe Decrypt Test ===")

    if not KEY_FILE.exists():

        print("No existe la clave AES.")

        return

    key = KEY_FILE.read_bytes()

    hashes = {}

    index_json = INPUT_DIR / "index.json"

    if index_json.exists():

        with open(

            index_json,

            "r",

            encoding="utf-8"

        ) as f:

            index = json.load(f)

        for capsule in index["capsulas"]:

            hashes[capsule["filename"]] = capsule["sha256"]

    for file in sorted(INPUT_DIR.glob("*.lsg")):

        try:

            decrypt_file(

                file,

                key,

                hashes.get(file.name)

            )

        except Exception as e:

            print(f"[ERROR] {file.name}: {e}")

    print("Proceso terminado.")


if __name__ == "__main__":

    main()