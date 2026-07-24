# -*- coding: utf-8 -*-
"""
Módulo Principal (Main) de CyberSwipe-AI.
Punto de entrada de la lógica de aplicación. Coordina los argumentos de la línea de comandos,
inicializa el registro y arranca el pipeline de generación individual de cápsulas.
"""

import argparse
import sys
from app.config import Config
from app.logger import setup_logger
from app.generator import QuestionsGenerator

logger = setup_logger("Main")

def parse_arguments() -> argparse.Namespace:
    """
    Parsea los argumentos de la línea de comandos.
    
    Returns:
        argparse.Namespace: Los argumentos parseados.
    """
    parser = argparse.ArgumentParser(
        description="CyberSwipe-AI: Generador automático de cápsulas pedagógicas de ciberseguridad utilizando Ollama."
    )
    parser.add_argument(
        "-c", "--capsule",
        type=int,
        default=None,
        help="ID numérico de una cápsula específica a generar (ej. 1, 2, 3)."
    )
    parser.add_argument(
        "-n", "--count",
        type=int,
        default=None,
        help="Cantidad de cápsulas del programa a generar de forma secuencial."
    )
    return parser.parse_args()

def main() -> int:
    """
    Punto de entrada principal para el pipeline.
    
    Returns:
        int: Código de salida (0 para éxito, 1 para error).
    """
    logger.info("=== Iniciando Ejecución de CyberSwipe-AI ===")
    
    if not Config.validate():
        logger.error("Error al validar las configuraciones de entorno.")
        return 1

    args = parse_arguments()

    try:
        generator = QuestionsGenerator()

        if args.capsule is not None:
            logger.info(f"Modo de generación individual solicitado para la Cápsula #{args.capsule}")
            capsules_info = generator.prompt_builder.parse_capsules_info()
            match_info = next((c for c in capsules_info if c["id"] == args.capsule), None)
            topic_text = match_info["topic_text"] if match_info else ""
            topic_title = match_info["topic_title"] if match_info else ""

            ok, data, errors = generator.generate_single_capsule(capsule_id=args.capsule, topic_text=topic_text, topic_title=topic_title)
            if ok:
                logger.info(f"=== Cápsula #{args.capsule} generada exitosamente en output/capsules/capsule_{args.capsule:03d}.json ===")
                return 0
            else:
                logger.error(f"=== Falló la generación de la Cápsula #{args.capsule}: {errors} ===")
                return 1
        else:
            success = generator.run_pipeline(capsules_count=args.count)
            if success:
                logger.info("=== Pipeline finalizado exitosamente. Cápsulas guardadas en output/capsules/ ===")
                return 0
            else:
                logger.error("=== El pipeline finalizó con errores. Revisa los logs en logs/cyberswipe_ai.log ===")
                return 1

    except Exception as e:
        logger.critical(f"Excepción no controlada en la ejecución principal: {e}", exc_info=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())
