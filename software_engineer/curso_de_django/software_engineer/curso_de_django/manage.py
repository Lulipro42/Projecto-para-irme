#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# Importa el módulo 'os' para interactuar con el sistema operativo (rutas, variables de entorno)
import os
# Importa el módulo 'sys' para acceder a parámetros y funciones específicos del sistema (como argumentos de consola)
import sys


def main():
    """Run administrative tasks."""
    # Establece la variable de entorno por defecto para los ajustes de Django apuntando a 'mysite.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        # Intenta importar la función necesaria para ejecutar comandos de Django desde la terminal
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si Django no está instalado o el entorno virtual no está activo, lanza un error descriptivo
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Ejecuta el comando que el usuario escribió en la terminal (ej: runserver, migrate)
    execute_from_command_line(sys.argv)


# Punto de entrada estándar de Python: si este archivo se ejecuta directamente, llama a la función main()
if __name__ == '__main__':
    main()

# EL PRIMERO ARRIBSA DE TODO ES EL NORMAL Y EL SEGUNDO ES EL NTR