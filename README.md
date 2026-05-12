Multi-Agent Translation & Simplification API
Esta API proporciona servicios avanzados de procesamiento de lenguaje natural (NLP), permitiendo la traducción automática con detección de idioma y la simplificación de textos mediante Modelos de Lenguaje de Gran Escala (LLM) a través de Ollama.

El sistema utiliza técnicas de smart chunking para procesar textos largos de manera eficiente y mantiene una arquitectura modular para facilitar la escalabilidad.

🚀 Características
Traducción Inteligente: Traducción de textos (individuales o listas) con detección automática del idioma de entrada.

Simplificación de Textos: Generación de versiones simplificadas de textos complejos mediante prompts optimizados (RAG/LLM).

Smart Chunking: Segmentación inteligente de párrafos para evitar límites de tokens y mejorar la coherencia.

Soporte CORS: Configurado para aceptar peticiones desde entornos locales (por defecto localhost:3000).

🛠️ Tecnologías Utilizadas
FastAPI: Framework web de alto rendimiento.

Pydantic: Validación de datos y esquemas de petición.

Ollama: Ejecución de LLMs locales para la simplificación.

NLP Custom Modules: Módulos internos para traducción (Translator), gestión de prompts y procesamiento de texto.

📦 Instalación y Configuración
Clonar el repositorio:

Bash
git clone https://github.com/tu-usuario/tu-proyecto.git
cd tu-proyecto
Configurar el entorno:
Se recomienda el uso de un entorno virtual:

Bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instalar dependencias:

Bash
pip install -r requirements.txt
Configuración de Ollama:
Asegúrate de tener Ollama instalado y el modelo correspondiente descargado para que el módulo Executor pueda realizar las peticiones.

🖥️ Uso
Para iniciar el servidor de desarrollo:

Bash
uvicorn main:app --reload
La API estará disponible en http://localhost:8000. Puedes acceder a la documentación interactiva en /docs.

Endpoints Principales
1. Traductor (POST /translator)
Traduce uno o varios textos al idioma objetivo.

Cuerpo de la petición:

JSON
{
  "text": "Hola mundo",
  "languageOutput": "en"
}
2. Simplificador (POST /simplifier)
Simplifica la complejidad de un texto manteniendo su significado.

Cuerpo de la petición:

JSON
{
  "text": "El texto técnico complejo que deseas reducir...",
  "languageInput": "es"
}
📁 Estructura del Proyecto
Plaintext
.
├── Agent/
│   └── TranslatorModule.py   # Lógica del motor de traducción
├── LLMMaganer/
│   ├── Executor.py           # Integración con Ollama
│   └── RAGmodule.py          # Generación de prompts para el LLM
├── NLPModule.py              # Funciones de procesamiento (smart_chunking)
├── main.py                   # Punto de entrada de FastAPI
└── README.md
⚠️ Notas Técnicas
Detección de duplicados KMP: El script incluye os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE" para evitar conflictos con librerías de procesamiento matemático (OpenMP) en ciertos entornos de desarrollo.

Chunking: El sistema divide automáticamente los textos en fragmentos de 500 caracteres para asegurar la estabilidad del traductor.
