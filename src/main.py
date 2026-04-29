# ============================================================================
# Project:          pyPSPrintProject
# Description:      Launcher principal — selecciona la UI disponible
# File:             main.py
# Author:           akanashiro@gmail.com
# License:          MIT - read LICENSE in repo
# ============================================================================
"""
main.py
-------
Punto de entrada de pyPSPrintProject.

Prioridad de UI:
  1. PySide6   → ui_pyside.py
  2. Tkinter   → ui_tkinter.py
  3. Ninguno   → mensaje de error y salida con código 1
"""

import sys


def _try_pyside6() -> bool:
    try:
        import importlib
        importlib.import_module("PySide6")
        return True
    except ImportError:
        return False


def _try_tkinter() -> bool:
    try:
        import importlib
        importlib.import_module("tkinter")
        return True
    except ImportError:
        return False


def main():
    if _try_pyside6():
        from mainQt import main as run
        run()

    elif _try_tkinter():
        from mainTk import main as run
        run()

    else:
        print(
            "❌  No se encontró ninguna biblioteca de UI compatible.\n"
            "\n"
            "   Para instalar PySide6 (recomendado):\n"
            "       pip install PySide6\n"
            "\n"
            "   Tkinter suele venir incluido con Python.\n"
            "   Si no está disponible, instalalo según tu sistema:\n"
            "       Windows / macOS : reinstalá Python desde python.org\n"
            "       Debian / Ubuntu : sudo apt install python3-tk\n"
            "       Fedora          : sudo dnf install python3-tkinter\n"
            "       Arch            : sudo pacman -S tk\n",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
