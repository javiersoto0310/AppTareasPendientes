# App Tareas(AppTareasPendientes)

App Tareas es una aplicación sencilla desarrollada en Python con PySide6 que permite a los usuarios organizar sus tareas diarias. Esta herramienta es perfecta para quienes buscan gestionar actividades de forma rápida y visual. El proyecto sigue principios de desarrollo basado en pruebas (TDD) para garantizar su calidad.

## Características
- Agregar nuevas tareas.
- Marcar tareas como completadas.
- Alternar tareas entre completadas y no completadas.
- Eliminar tareas completadas.

## Tecnologías utilizadas
- Python 3.9+ (gestionado con pyenv).
- PySide6 para la interfaz gráfica.
- pip-tools para la gestión de dependencias.
- TDD (Desarrollo basado en pruebas).

## Requisitos previos
1. **Instalar pyenv para crear un entorno virtual:**
   [Guía oficial de pyenv](https://github.com/pyenv/pyenv.git).

2. **Crear un entorno con venv:**
   Ejecuta los siguientes comandos:
   - En Linux/MacOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - En Windows:
     ```bash
     python3 -m venv .venv
     .venv\Scripts\activate
     ```

3. **Instalar pip-tools en el entorno virtual:**
   ```bash
   pip install pip-tools
   ```
   
4. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
    ```
   
5. **Clona el repositorio en tu máquina local:**
https://github.com/javiersoto0310/AppTareasPendientes.git

6. **Ejecuta la aplicación desde la terminal:**
   ```bash
   python src/main.py
    ```
