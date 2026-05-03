

## Instalación

Instalar dependencias con el siguiente comando:

pip install -r requirements.txt

## Ejecución del programa

Este proyecto utiliza una estructura modular basada en la carpeta src. Por esta razón no debe ejecutarse directamente con el botón de ejecución del editor.

Forma incorrecta de ejecución:

python src/main.py

Esto puede generar errores de importación.

Forma correcta de ejecución desde la raíz del proyecto:

python -m src.main

## Explicación técnica

El proyecto está organizado como un paquete llamado src y utiliza imports absolutos como:

from src.service import ...

Para que Python reconozca correctamente esta estructura, el programa debe ejecutarse en modo módulo usando la opción -m.

## Ejecución de pruebas

Para ejecutar las pruebas automatizadas:

python -m pytest


