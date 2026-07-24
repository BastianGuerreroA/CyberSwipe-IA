"""
Script de prueba interactivo para validar la integración con Ollama (Gemma 4).
Ejecuta una generación simple de 1 cápsula y muestra los resultados y logs detallados.
"""

import sys
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from app.config import Config
from app.generator import QuestionsGenerator

console = Console()

def check_ollama_status() -> bool:
    #Verifica si Ollama está corriendo localmente y si tiene el modelo cargado.
    console.print("[yellow]Verificando estado del servidor local de Ollama...[/yellow]")
    
    # 1. Comprobar host
    try:
        response = requests.get(Config.OLLAMA_HOST, timeout=5)
        if response.status_code != 200:
            console.print(Panel(
                f"[red]Ollama respondió con código de estado inesperado: {response.status_code}[/red]\n"
                f"Asegúrate de que Ollama está activo en: {Config.OLLAMA_HOST}",
                title="Error de Ollama"
            ))
            return False
    except requests.exceptions.RequestException as e:
        console.print(Panel(
            f"[red]No se pudo conectar al servidor Ollama en {Config.OLLAMA_HOST}.[/red]\n\n"
            f"[bold]Detalle del error:[/bold]\n{e}\n\n"
            "¿Está Ollama encendido? Puedes iniciarlo abriendo la aplicación de Ollama o ejecutando `ollama serve`.",
            title="Ollama Desconectado"
        ))
        return False

    # 2. Comprobar si el modelo está disponible
    tags_url = f"{Config.OLLAMA_HOST.rstrip('/')}/api/tags"
    try:
        response = requests.get(tags_url, timeout=5)
        if response.status_code == 200:
            models_data = response.json()
            models_list = [m.get("name") for m in models_data.get("models", [])]
            
            # Buscar coincidencia exacta o parcial del modelo configurado
            model_target = Config.OLLAMA_MODEL
            model_found = False
            for model_name in models_list:
                if model_target in model_name or model_name in model_target:
                    model_found = True
                    model_target = model_name
                    break

            if model_found:
                console.print(f"[green][OK] Ollama está activo y el modelo '{model_target}' está disponible.[/green]")
                return True
            else:
                console.print(Panel(
                    f"[warning]Advertencia: El modelo '{model_target}' no parece estar descargado en Ollama.[/warning]\n\n"
                    f"[bold]Modelos disponibles en tu sistema:[/bold]\n" + "\n".join(f"- {m}" for m in models_list) + "\n\n"
                    f"Puedes intentar descargarlo ejecutando:\n[bold cyan]ollama pull {model_target}[/bold cyan]",
                    title="Modelo no encontrado"
                ))
                # Retornamos True de todas formas por si es un alias no listado, pero advertimos
                return True
    except Exception as e:
        console.print(f"[yellow]Advertencia al comprobar modelos: {e}. Procediendo con la generación...[/yellow]")
    
    return True

def run_test_generation():
    #Ejecuta una generación de prueba corta de 1 cápsula.
    console.print("\n[bold blue]=== TEST DE GENERACIÓN ESTRUCTURADA CYBERSWIPE-AI ===[/bold blue]\n")
    
    if not check_ollama_status():
        console.print("[red]Cancelando prueba debido a problemas con Ollama.[/red]")
        sys.exit(1)

    console.print("\n[yellow]Iniciando generación corta de prueba (1 cápsula) basada en prompts/aprendizaje.md...[/yellow]\n")
    
    generator = QuestionsGenerator()
    
    # Ejecutamos con 1 cápsula para acelerar la respuesta del LLM local
    success = generator.run_pipeline(capsules_count=1)
    
    if success:
        console.print("\n[bold green]¡Generación completada exitosamente![/bold green]")
        latest_file = Config.CAPSULES_DIR / "capsule_001.json"
        console.print(f"[green]La cápsula individual fue guardada y validada en: [bold]{latest_file}[/bold][/green]")
        
        # Mostrar metadatos de la generación
        # Buscar el último directorio en history
        history_dirs = sorted([d for d in Config.HISTORY_DIR.iterdir() if d.is_dir()])
        if history_dirs:
            latest_history = history_dirs[-1]
            try:
                import json
                with open(latest_history / "metadata.json", "r", encoding="utf-8") as f:
                    meta = json.load(f)
                
                table = Table(title="Detalle de la Generación (Historial)")
                table.add_column("Métrica", style="cyan")
                table.add_column("Valor", style="magenta")
                table.add_row("ID Generación", meta.get("generation_id"))
                table.add_row("Duración", f"{meta.get('duration_seconds')} seg")
                table.add_row("Estado", meta.get("status"))
                table.add_row("Modelo Utilizado", meta.get("model_used"))
                
                console.print(table)
            except Exception as e:
                console.print(f"[yellow]No se pudieron leer los metadatos de historial: {e}[/yellow]")
    else:
        console.print("\n[bold red][ERROR] La generación de prueba falló.[/bold red]")
        console.print("[red]Revisa la carpeta de historial o el archivo 'logs/cyberswipe_ai.log' para más información.[/red]")
        sys.exit(1)

if __name__ == "__main__":
    run_test_generation()
