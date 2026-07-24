# CyberSwipe-AI 🤖🔒

Subproyecto de Inteligencia Artificial para **CyberSwipe**, un videojuego serio de ciberseguridad desarrollado en Godot 4 como parte de una Tesis de Ingeniería Civil en Informática.

El objetivo de **CyberSwipe-AI** es generar cápsulas educativas dinámicas basadas en modelos de lenguaje locales (LLM) que luego son revisadas por expertos, cifradas y publicadas en un repositorio público para su consumo desde el juego.

---

## 🔄 Flujo de Trabajo del Sistema

```text
[ Ollama (LLM Local) ]
        │
        ▼ (Genera JSONs individuales)
[ output/capsules/capsule_00X.json ]
        │
        ▼ (Revisión y Aprobación del Experto Humano)
[ encrypt_capsule.py ]
        │
        ▼ (Cifra a archivos binarios protegidos)
[ Archivos .lsg + index.lsg ]
        │
        ▼
[ publish_content.py ]
        │
        ▼ (Publicación remota)
[ Repositorio CyberSwipe-Content en GitHub ]
        │
        ▼ (Descarga dinámica)
[ Videojuego CyberSwipe en Godot 4 ]
```

---

## 🛠️ Tecnologías y Requisitos Previos

* **Lenguaje:** Python 3.10+
* **Motor LLM Local:** [Ollama](https://ollama.com/) con el modelo `gemma4:e2b` (o compatible).
* **Marcos de Referencia:**
  * **CIS Controls v8 - Implementation Group 1 (IG1)**
  * **CAPEC** (Common Attack Pattern Enumeration and Classification)
  * **Ley 21.719** (Protección de Datos Personales en Chile)
* **Librerías de Python principales:**
  * `requests` (Conexión HTTP con la API local de Ollama)
  * `jsonschema` (Validación estructural y de negocio estricta del JSON)
  * `cryptography` / `pycryptodome` (Cifrado simétrico AES-256)
  * `rich` (Reportes visuales formateados en terminal)
  * `python-dotenv` (Gestión de variables de entorno)

---

## 📁 Estructura del Proyecto

```text
CyberSwipe-IA/
├── app/                        # Módulos del backend generador
│   ├── config.py               # Configuración centralizada y variables .env
│   ├── file_manager.py        # Lectura y escritura segura de archivos JSON/MD
│   ├── generator.py           # Orquestador del ciclo de generación y reintentos
│   ├── history.py             # Registro histórico de ejecuciones
│   ├── logger.py              # Logging formateado y coloreado
│   ├── main.py                # Punto de entrada CLI (--capsule X)
│   ├── ollama_client.py       # Cliente HTTP hacia la API de Ollama
│   ├── prompt_builder.py      # Construcción del prompt y contexto anti-repetición
│   ├── utils.py               # Utilidades, formateo a BBCode y validación de signos
│   └── validator.py           # Validador de JSON Schema y reglas de negocio
├── prompts/                    # Definición de reglas instruccionales
│   ├── aprendizaje.md         # Programa pedagógico y objetivos por cápsula
│   ├── generation_rules.md    # Reglas pedagógicas de diseño no-binario
│   ├── output_rules.md        # Especificación de formato de salida JSON
│   ├── style_rules.md         # Tono de redacción (Español laboral chileno)
│   └── system_prompt.md       # Definición de rol del Diseñador Instruccional
├── references/                 # Guías de conocimiento técnico y pedagógico
│   ├── capec_social_engineering.md  # Taxonomía de patrones de ataque
│   ├── cis_controls_ig1.md          # Salvaguardas de ciberhigiene básica
│   └── pedagogy.md                  # Filosofía de decisiones y no-binariedad
├── schema/
│   └── questions_schema.json  # JSON Schema para validación estricta de Ollama
├── templates/
│   └── questions_template.json # Plantilla JSON de referencia pedagógica
├── output/
│   ├── capsules/              # Cápsulas JSON individuales generadas (capsule_00X.json)
│   ├── history/               # Historial guardado de ejecuciones pasadas
│   └── latest/                # questions.json compilado más reciente
├── encrypt_capsule.py         # Script para cifrar cápsulas JSON a formato .lsg (AES-256)
├── decrypt_test.py            # Script para verificar la integridad del descifrado
├── publish_content.py         # Script para sincronizar y publicar .lsg a GitHub
├── run.py                     # Script de ejecución rápida del pipeline completo
├── .env.example               # Plantilla de variables de entorno
├── .gitignore                 # Filtro de archivos no rastreados por Git
└── requirements.txt           # Lista de dependencias de Python
```

---

## ⚙️ Configuración e Instalación

### 1. Clonar el repositorio e instalar dependencias
```bash
# Clonar el proyecto
git clone https://github.com/TU_USUARIO/CyberSwipe-IA.git
cd CyberSwipe-IA

# Crear y activar entorno virtual (opcional pero recomendado)
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar variables de entorno
Copia la plantilla `.env.example` a `.env`:
```bash
cp .env.example .env
```

Contenido por defecto de `.env`:
```env
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma4:e2b
OLLAMA_NUM_CTX=16384
OLLAMA_NUM_PREDICT=-1
OLLAMA_TEMPERATURE=0.1
OLLAMA_NUM_GPU=0
OUTPUT_DIR=output
LOG_LEVEL=INFO
```

> 💡 **Nota sobre Hardware / Laptops:**  
> Si ejecutas en un equipo con GPU dedicada limitada (ej. 2 GB VRAM), mantén `OLLAMA_NUM_GPU=0` para forzar el procesamiento en CPU pura y evitar crashes por desbordamiento de memoria de vídeo (`0xc0000409`).

---

## 🚀 Guía de Uso

### 1. Iniciar el servidor local de Ollama
Asegúrate de tener corriendo Ollama en segundo plano con el modelo descargado:
```bash
ollama run gemma4:e2b
```

### 2. Generar Cápsulas Educativas

* **Generación Completa (todas las cápsulas definidas en `aprendizaje.md`):**
  ```bash
  python run.py
  ```

* **Generación Individual de una Cápsula Específica (ej. Cápsula #1):**
  ```bash
  python -m app.main --capsule 1
  ```

Las cápsulas generadas se guardarán en la carpeta `output/capsules/capsule_00X.json`.

---

### 3. Flujo Manual de Cifrado y Publicación (Experto en el Loop)

Una vez que las cápsulas `.json` hayan sido revisadas y aprobadas por el experto pedagógico:

1. **Cifrar las cápsulas a binarios `.lsg` (AES-256):**
   ```bash
   python encrypt_capsule.py
   ```
   *Genera los archivos `.lsg` cifrados y el índice `index.lsg`.*

2. **Probar el descifrado (Verificación de integridad):**
   ```bash
   python decrypt_test.py
   ```

3. **Publicar contenido cifrado al repositorio GitHub de CyberSwipe:**
   ```bash
   python publish_content.py
   ```
   *Subirá los archivos `.lsg` al repositorio remoto para que Godot los descargue dinámicamente.*

---

## 🎯 Principios de Diseño Instruccional

1. **No-Binariedad:** Ambas opciones de decisión (izquierda y derecha) deben ser frases completas, plausibles y defendibles en el contexto laboral diario. Se prohíben respuestas caricaturescas u obvias (ej: *"Dar clave"* vs *"No dar clave"*).
2. **Aislamiento Temático:** Cada cápsula trata **únicamente** sobre sus objetivos temáticos sin contaminación (ej: la Cápsula 1 aborda solo credenciales/MFA sin adelantarse a Phishing).
3. **Mapeo 1-a-1:** El contenido de estudio enseña 5 conceptos clave únicos que se evalúan secuencialmente en las 5 cartas asociadas.
4. **Diversidad de Canales y Entornos:** Escenarios ambientados en teletrabajo, cafeterías, aeropuertos, WhatsApp, Teams, Google Drive/OneDrive, códigos QR, SMS y vishing.
5. **Formato Nativo Godot:** Formateo automático de negritas `[b]` y viñetas `• ` para nodos `RichTextLabel` en Godot.

---

## 📄 Licencia

Este proyecto fue desarrollado como parte de una tesis de grado para la carrera de Ingeniería Civil en Informática.
