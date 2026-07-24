# -*- coding: utf-8 -*-

"""
CyberSwipe - Publish Content

Publica automáticamente las cápsulas cifradas
en el repositorio CyberSwipe-Content.

Flujo:
1. Compara los archivos .lsg.
2. Copia únicamente los modificados.
3. Ejecuta git add.
4. Ejecuta git commit.
5. Ejecuta git push.
"""

import hashlib
import shutil
import subprocess
from pathlib import Path


# ==========================================================
# CONFIGURACIÓN
# ==========================================================

ROOT = Path(__file__).resolve().parent

SOURCE_DIR = ROOT / "output" / "encrypted"

CONTENT_REPO = Path(r"D:\GitHub\CyberSwipe-Content")

DESTINATION_DIR = CONTENT_REPO / "content"

COMMIT_MESSAGE = "Update encrypted capsules"


# ==========================================================
# SHA256
# ==========================================================

def sha256(path: Path) -> str:
    """Calcula el SHA-256 de un archivo."""

    h = hashlib.sha256()

    with open(path, "rb") as f:

        while True:

            chunk = f.read(8192)

            if not chunk:
                break

            h.update(chunk)

    return h.hexdigest()


# ==========================================================
# GIT
# ==========================================================

def git(command):

    result = subprocess.run(
        command,
        cwd=CONTENT_REPO,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception(result.stderr)

    return result.stdout


# ==========================================================
# COPIAR ARCHIVOS
# ==========================================================

def sync_capsules():

    DESTINATION_DIR.mkdir(parents=True, exist_ok=True)

    copied = 0
    skipped = 0

    for source in sorted(SOURCE_DIR.glob("*.lsg")):

        destination = DESTINATION_DIR / source.name

        # Archivo nuevo
        if not destination.exists():

            shutil.copy2(source, destination)

            copied += 1

            print(f"[NEW] {source.name}")

            continue

        # Comparar hash
        if sha256(source) != sha256(destination):

            shutil.copy2(source, destination)

            copied += 1

            print(f"[UPDATE] {source.name}")

        else:

            skipped += 1

            print(f"[SKIP] {source.name}")

    return copied, skipped


# ==========================================================
# PUBLICAR
# ==========================================================

def publish():

    git(["git", "add", "."])

    status = git(["git", "status", "--porcelain"])

    if not status.strip():

        print("\nNo existen cambios para publicar.")

        return False

    git([

        "git",

        "commit",

        "-m",

        COMMIT_MESSAGE

    ])

    git([

        "git",

        "push",

        "origin",

        "main"

    ])

    return True


# ==========================================================
# MAIN
# ==========================================================

def main():

    print("=" * 55)
    print(" CyberSwipe - Publish Content")
    print("=" * 55)

    if not SOURCE_DIR.exists():

        print("No existe la carpeta de cápsulas cifradas.")

        return

    if not CONTENT_REPO.exists():

        print("No existe el repositorio CyberSwipe-Content.")

        return

    copied, skipped = sync_capsules()

    print("\nResumen")
    print("----------------------------")
    print(f"Actualizados : {copied}")
    print(f"Sin cambios  : {skipped}")

    if publish():

        print("\nContenido publicado correctamente.")

    print("\nProceso finalizado.")


if __name__ == "__main__":
    main()