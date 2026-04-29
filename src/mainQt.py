# ============================================================================
# Project:          pyPSPrintProject
# Description:      UI PySide6 for pyPSPrintProject
# File:             mainQt.py
# Author:           akanashiro@gmail.com
# License:          MIT - read LICENSE in repo
# ============================================================================
"""
ui_pyside.py
------------
Interfaz gráfica multiplataforma (Windows / Linux / macOS) construida con
PySide6.

Selección de tema / estilo:
  - Windows : usa el estilo nativo "windowsvista" (QStyleFactory)
  - macOS   : usa el estilo nativo "macOS"
  - Linux   : intenta cargar el tema Breeze vía qt-material o QStyleFactory;
              si no está disponible usa "Fusion" (built-in, limpio y portable)

Instalar dependencias:
    pip install PySide6

Uso:
    python ui_pyside.py
"""

import sys
import threading
from pathlib import Path

from PySide6.QtCore    import Qt, QObject, Signal, Slot
from PySide6.QtGui     import QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QLineEdit, QPushButton, QComboBox,
    QTextEdit, QFileDialog, QMessageBox,
    QGridLayout, QHBoxLayout, QVBoxLayout,
    QFrame, QSizePolicy, QStyleFactory
)
from PySide6.QtGui import QTextCursor, QColor, QFont

# ── Módulos del proyecto (opcionales: la UI funciona en modo demo sin ellos) ─
try:
    from projectParser import PSProjectParser
    from projectDocGen import DocGenerator
    import helpFunctions as helpers
    _HAS_PROJECT = True
except ImportError:
    _HAS_PROJECT = False


# ══════════════════════════════════════════════════════════════════════════════
# Señal para escribir en el log desde hilos secundarios (thread-safe)
# ══════════════════════════════════════════════════════════════════════════════

class _LogSignals(QObject):
    append = Signal(str, str)   # (text, tag)


# ══════════════════════════════════════════════════════════════════════════════
# Redireccionador de stdout / stderr → QTextEdit
# ══════════════════════════════════════════════════════════════════════════════

class _StreamRedirector:
    """Redirige print() / sys.stderr al widget de log de forma thread-safe."""

    _COLOR = {
        "normal":  None,
        "warning": QColor("#B8600A"),
        "error":   QColor("#CC0000"),
        "ok":      QColor("#2E7D32"),
    }

    def __init__(self, signals: _LogSignals, tag: str = "normal"):
        self._signals = signals
        self._tag     = tag

    def write(self, msg: str):
        if msg:
            self._signals.append.emit(msg, self._tag)

    def flush(self):
        pass


# ══════════════════════════════════════════════════════════════════════════════
# Clickable text label (para el botón "About" en la esquina inferior derecha)
# ══════════════════════════════════════════════════════════════════════════════

class ClickableLabel(QLabel):
    # Define a custom signal
    clicked = Signal()

    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    def mousePressEvent(self, event):
        # Only emit signal if left mouse button is clicked
        if event.button() == Qt.LeftButton:
            self.clicked.emit()


# ══════════════════════════════════════════════════════════════════════════════
# Ventana principal
# ══════════════════════════════════════════════════════════════════════════════

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("pyPSPrintProject")
        self.setMinimumSize(720, 500)

        # Uso de la función
        icon = get_app_icon("img/ps_icon.svg", "img/ps_icon.png")
        self.setWindowIcon(icon)

        self._signals = _LogSignals()
        self._signals.append.connect(self._log_append)

        self._build_ui()
        self._redirect_streams()
        self._toggle_template()


    def _showAbout(self):
        aboutDialogBox = QMessageBox()
        aboutDialogBox.setWindowTitle("About pyPSPrintProject")
        informationStr = "<h2 align='center'>pyPSPrintProject 1.1.0</h2><br>" +\
                            "<p align='center'>PeopleSoft Project technical document generator.<br>" +\
                            "This UI was built with PySide6.<br><br>" + "<b>Agustín Kanashiro</b><br>2026<br>"+\
                            "<a href='https://github.com/akanashiro/pyPsPrintProject'>https://github.com/akanashiro/pyPsPrintProject</a></p>"
        aboutDialogBox.setText(informationStr)
        aboutDialogBox.setIcon(QMessageBox.Information)

        aboutDialogBox.exec()

    # ── Construcción de la UI ──────────────────────────────────────────────

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        root_layout = QVBoxLayout(central)
        root_layout.setContentsMargins(12, 12, 12, 8)
        root_layout.setSpacing(6)

        # ── Grid de parámetros ─────────────────────────────────────────────
        grid = QGridLayout()
        grid.setColumnStretch(1, 1)
        grid.setSpacing(6)

        # Fila 0 · XML Project File
        self._xml_edit = QLineEdit()
        self._xml_edit.setPlaceholderText("Path to exported XML…")
        xml_btn = QPushButton("Browse…")
        xml_btn.clicked.connect(self._browse_xml)
        grid.addWidget(QLabel("XML Project File:"), 0, 0, Qt.AlignRight)
        grid.addWidget(self._xml_edit,              0, 1)
        grid.addWidget(xml_btn,                     0, 2)

        # Fila 1 · Output file name
        self._out_edit = QLineEdit()
        self._out_edit.setPlaceholderText("Output file name (without extension)…")
        out_btn = QPushButton("Browse…")
        out_btn.clicked.connect(self._browse_output)
        grid.addWidget(QLabel("Output file name:"), 1, 0, Qt.AlignRight)
        grid.addWidget(self._out_edit,              1, 1)
        grid.addWidget(out_btn,                     1, 2)

        # Fila 2 · Output format
        self._fmt_combo = QComboBox()
        self._fmt_combo.addItems(["docx", "md"])
        self._fmt_combo.currentTextChanged.connect(
            lambda _: self._toggle_template())
        grid.addWidget(QLabel("Output format:"), 2, 0, Qt.AlignRight)
        grid.addWidget(self._fmt_combo,          2, 1, Qt.AlignLeft)

        # Fila 3 · Template
        self._tpl_label = QLabel("Template (.docx):")
        self._tpl_edit  = QLineEdit()
        self._tpl_edit.setPlaceholderText("Required only for DOCX output…")
        self._tpl_btn   = QPushButton("Browse…")
        self._tpl_btn.clicked.connect(self._browse_template)
        grid.addWidget(self._tpl_label, 3, 0, Qt.AlignRight)
        grid.addWidget(self._tpl_edit,  3, 1)
        grid.addWidget(self._tpl_btn,   3, 2)

        root_layout.addLayout(grid)

        # ── Botón Process ──────────────────────────────────────────────────
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        self._run_btn = QPushButton("Process files")
        self._run_btn.setMinimumWidth(140)
        self._run_btn.clicked.connect(self._run)
        btn_row.addWidget(self._run_btn)
        root_layout.addLayout(btn_row)

        # ── Separador ─────────────────────────────────────────────────────
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        root_layout.addWidget(line)

        # ── Log console ────────────────────────────────────────────────────
        root_layout.addWidget(QLabel("Log console:"))

        self._log = QTextEdit()
        self._log.setReadOnly(True)
        self._log.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Fuente monoespaciada por plataforma
        if sys.platform == "win32":
            mono = QFont("Consolas", 9)
        elif sys.platform == "darwin":
            mono = QFont("Menlo", 10)
        else:
            mono = QFont("Monospace", 9)
        self._log.setFont(mono)

        root_layout.addWidget(self._log)

        # ── About ────────────────────────────────────────────────────
        about_btn = ClickableLabel("About")
        about_btn.setStyleSheet("QLabel {color: blue; text-decoration: underline;}")
        about_btn.clicked.connect(self._showAbout)

        hboxBottomRight = QHBoxLayout()
        hboxBottomRight.addStretch(1)
        hboxBottomRight.addWidget(about_btn)
        # hboxBottomRight.addWidget(self.btnClose)
        root_layout.addLayout(hboxBottomRight)
        # root_layout.addWidget(about_btn)

    # ── Habilitación del campo Template ───────────────────────────────────

    def _toggle_template(self):
        is_docx = self._fmt_combo.currentText() == "docx"
        self._tpl_edit.setEnabled(is_docx)
        self._tpl_btn.setEnabled(is_docx)
        self._tpl_label.setEnabled(is_docx)

    # ── Diálogos de archivos ───────────────────────────────────────────────

    def _browse_xml(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Select XML project file", "",
            "XML files (*.XML *.xml);;All files (*.*)")
        if path:
            self._xml_edit.setText(path)
            if not self._out_edit.text():
                self._out_edit.setText(str(Path(path).stem))

    def _browse_output(self):
        fmt = self._fmt_combo.currentText()
        path, _ = QFileDialog.getSaveFileName(
            self, "Select output file", "",
            f"{fmt.upper()} files (*.{fmt});;All files (*.*)")
        if path:
            self._out_edit.setText(path)

    def _browse_template(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Select DOCX template", "",
            "Word documents (*.docx *.DOCX);;All files (*.*)")
        if path:
            self._tpl_edit.setText(path)

    # ── Redirección de streams ─────────────────────────────────────────────

    def _redirect_streams(self):
        sys.stdout = _StreamRedirector(self._signals, "normal")
        sys.stderr = _StreamRedirector(self._signals, "error")

    # ── Slot para escribir en el log (desde el hilo principal) ────────────

    @Slot(str, str)
    def _log_append(self, text: str, tag: str):
        colors = {
            "warning": QColor("#B8600A"),
            "error":   QColor("#CC0000"),
            "ok":      QColor("#2E7D32"),
        }
        cursor = self._log.textCursor()
        cursor.movePosition(QTextCursor.End)

        fmt = cursor.charFormat()
        if tag in colors:
            fmt.setForeground(colors[tag])
        else:
            fmt.clearForeground()
        cursor.setCharFormat(fmt)
        cursor.insertText(text)
        self._log.setTextCursor(cursor)
        self._log.ensureCursorVisible()

    # ── Validación ────────────────────────────────────────────────────────

    def _validate(self) -> bool:
        xml = self._xml_edit.text().strip()
        out = self._out_edit.text().strip()
        fmt = self._fmt_combo.currentText()
        tpl = self._tpl_edit.text().strip()

        if not xml:
            QMessageBox.critical(self, "Validation error",
                                 "Please select the XML project file.")
            return False
        if not Path(xml).exists():
            QMessageBox.critical(self, "Validation error",
                                 f"File not found:\n{xml}")
            return False
        if not out:
            QMessageBox.critical(self, "Validation error",
                                 "Please specify the output file name.")
            return False
        if fmt == "docx" and not tpl:
            QMessageBox.critical(self, "Validation error",
                "A template (.docx) is required for DOCX output.")
            return False
        if fmt == "docx" and not Path(tpl).exists():
            QMessageBox.critical(self, "Validation error",
                                 f"Template not found:\n{tpl}")
            return False
        return True

    # ── Ejecución en hilo secundario ───────────────────────────────────────

    def _run(self):
        if not self._validate():
            return
        self._run_btn.setEnabled(False)
        threading.Thread(target=self._process, daemon=True).start()

    def _process(self):
        xml = self._xml_edit.text().strip()
        out = self._out_edit.text().strip()
        fmt = self._fmt_combo.currentText()
        tpl = self._tpl_edit.text().strip() or None

        try:
            if not _HAS_PROJECT:
                print("⚠️  Project modules not found — running in demo mode.")
                print(f"   XML      : {xml}")
                print(f"   Output   : {out}")
                print(f"   Format   : {fmt}")
                print(f"   Template : {tpl or 'N/A'}")
                print("✅ (Demo) Finished.")
                return

            fixed = helpers.fixRootTag(xml)
            if fixed:
                print("⚠️  XML fixed: <root> tag automatically added.")

            print(f"🔍 Parsing: {Path(xml).name} …")
            project = PSProjectParser(xml).parse()

            gen = DocGenerator(project, output_format=fmt, template_path=tpl)

            if fmt == "md":
                dest = out if out.endswith(".md") else f"{out}.md"
                gen.to_markdown(dest)
            else:
                dest = out if out.endswith(".docx") else f"{out}.docx"
                gen.to_docx(dest)

        except Exception as exc:
            sys.stderr.write(f"❌ Error: {exc}\n")
        finally:
            # Volver al hilo principal para re-habilitar el botón
            self._signals.append.emit("", "_reenable_btn_")

    @Slot(str, str)
    def _handle_internal_signal(self, text: str, tag: str):
        if tag == "_reenable_btn_":
            self._run_btn.setEnabled(True)

    def closeEvent(self, event):
        # Restaurar streams al cerrar
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        super().closeEvent(event)


# ══════════════════════════════════════════════════════════════════════════════
# Selección de estilo / tema
# ══════════════════════════════════════════════════════════════════════════════

def _setup_style(app: QApplication):
    """
    Aplica el estilo más apropiado según la plataforma:
      - Windows : windowsvista (nativo)
      - macOS   : macOS (nativo)
      - Linux   : Fusion (limpio y portable; se puede personalizar con QPalette)
    """
    available = [s.lower() for s in QStyleFactory.keys()]
    platform  = sys.platform

    if platform == "win32":
        for s in ("windowsvista", "windows"):
            if s in available:
                app.setStyle(QStyleFactory.create(s))
                return
    elif platform == "darwin":
        if "macos" in available:
            app.setStyle(QStyleFactory.create("macOS"))
            return
    else:
        # Linux: Fusion es el más limpio sin dependencias extra
        if "fusion" in available:
            app.setStyle(QStyleFactory.create("Fusion"))
            return

    # Fallback genérico
    app.setStyle(QStyleFactory.create("Fusion"))

def get_app_icon(svg_path, png_fallback):
    # Verifica si el SVG existe
    if Path(svg_path).exists():
        return QIcon(svg_path)
    # Si no, intenta cargar el PNG
    elif Path(png_fallback).exists():
        print(f"Advertencia: No se encontró {svg_path}, usando fallback PNG.")
        return QIcon(png_fallback)
    # Si ninguno existe, devuelve un icono vacío o uno del sistema
    return QIcon()

# ══════════════════════════════════════════════════════════════════════════════
# Entry point
# ══════════════════════════════════════════════════════════════════════════════

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("pyPSPrintProject")

    _setup_style(app)

    window = MainWindow()

    # Conectar la señal interna para re-habilitar el botón
    window._signals.append.connect(window._handle_internal_signal)

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
