# Servidor y Cliente TCP en Python

Este repositorio contiene un servidor y un cliente TCP implementados en Python 3.12. El servidor escucha en el puerto 5000 y maneja conexiones de clientes. La interacción entre el cliente y el servidor se realiza mediante el protocolo TCP.

## Requisitos

- **Python 3.12**: Asegúrate de tener Python 3.12 instalado en tu sistema.
- **pip**: Python viene con `pip`, que es el gestor de paquetes necesario para instalar dependencias.

## Instalación

### 1. Instalar Python 3.12

Si no tienes Python 3.12 instalado, puedes descargarlo desde la [página oficial de Python](https://www.python.org/downloads/release/python-3120/). Durante la instalación, asegúrate de seleccionar la opción **"Add Python to PATH"**.

Para verificar que Python 3.12 y `pip` están correctamente instalados, abre la terminal o línea de comandos y ejecuta:

Checa que los tengas instalados correctamente con:

python --version
pip --version

### 2. Crear un entorno virtual (venv)

Navega a la carpeta donde quieres almacenar tu proyecto.

Crea el entorno virtual ejecutando el siguiente comando:

python -m venv venv

Activa el entorno virtual:

En Windows:
venv\Scripts\activate

En macOS o Linux:
source venv/bin/activate

### 3. Instalar dependencias

Corre el comando para instalar las librerias: 

pip install -r requirements.txt

### 4. Ejecutar el servidor

Con las dependencias instaladas, puedes ejecutar el servidor TCP. Asegúrate de estar en el directorio donde se encuentra el archivo server.py y ejecuta:

python server.py


### 5. Ejecutar el cliente

Para ejecutar el cliente, abre otra terminal (con el entorno virtual activado si es necesario) y ejecuta el archivo client.py:

python client.py

puedes crear los clientes que desees