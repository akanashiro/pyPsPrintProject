# ============================================================================
# Project:          pyPSPrintProject
# Description:      GUI Tkinter para pyPSPrintProject
# File:             ui_tkinter.py
# Author:           akanashiro@gmail.com
# License:          MIT - read LICENSE in repo
# ============================================================================
"""
ui_tkinter.py
-------------
Interfaz gráfica basada en tkinter para pyPSPrintProject.
Compatible con Windows, Linux y macOS.

Requisitos:
    pip install tkinter  (incluido en Python estándar)
"""

import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import sys
import io
import threading
from pathlib import Path


# ── Redireccionamiento de stdout/stderr → Log console ──────────────────────

class _TextRedirector(io.TextIOBase):
    """Redirige print() y sys.stderr hacia el widget de log."""

    def __init__(self, text_widget: scrolledtext.ScrolledText, tag: str = "info"):
        self._widget = text_widget
        self._tag = tag

    def write(self, s: str) -> int:
        if s:
            self._widget.configure(state="normal")
            self._widget.insert(tk.END, s, self._tag)
            self._widget.see(tk.END)
            self._widget.configure(state="disabled")
        return len(s)

    def flush(self):
        pass


# ── Ventana principal ───────────────────────────────────────────────────────

class AppWindow(tk.Tk):

    # Paleta de colores
    BG          = "#1e1e2e"   # fondo general
    PANEL       = "#2a2a3e"   # fondo de paneles
    ACCENT      = "#7c6af7"   # morado principal
    ACCENT2     = "#56d4b5"   # verde-agua secundario
    FG          = "#e0dff5"   # texto normal
    FG_DIM      = "#888899"   # texto apagado
    ENTRY_BG    = "#13131f"   # fondo de campos de texto
    ENTRY_FG    = "#c9c7e8"   # texto de campos
    LOG_BG      = "#0d0d18"   # fondo de la consola
    ERROR_FG    = "#ff6b6b"
    WARN_FG     = "#ffc36b"
    SUCCESS_FG  = "#56d4b5"
    BTN_BG      = "#7c6af7"
    BTN_FG      = "#ffffff"
    BTN_ACT     = "#5e50d4"
    BTN2_BG     = "#2e3250"
    BTN2_FG     = "#a0a8d0"

    FONT_LABEL  = ("Consolas", 9)
    FONT_ENTRY  = ("Consolas", 9)
    FONT_BTN    = ("Consolas", 9, "bold")
    FONT_LOG    = ("Consolas", 9)
    FONT_TITLE  = ("Consolas", 11, "bold")

    def __init__(self):
        super().__init__()

        self.title("pyPSPrintProject")
        self.resizable(True, True)
        self.minsize(700, 520)
        self.configure(bg=self.BG)

        # Centrar ventana
        self.update_idletasks()
        w, h = 760, 560
        x = (self.winfo_screenwidth()  - w) // 2
        y = (self.winfo_screenheight() - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")

        # Variables de control
        self.xml_path_var    = tk.StringVar()
        self.output_name_var = tk.StringVar()
        self.format_var      = tk.StringVar(value="md")
        self.template_var    = tk.StringVar()

        self._build_ui()
        self._redirect_output()

    # ── Construcción de la UI ────────────────────────────────────────────────

    def _build_ui(self):
        """Arma todos los widgets."""

        outer = tk.Frame(self, bg=self.BG, padx=18, pady=14)
        outer.pack(fill=tk.BOTH, expand=True)

        # Título
        title_lbl = tk.Label(
            outer,
            text="⬡  PeopleSoft Project Doc Generator",
            bg=self.BG, fg=self.ACCENT,
            font=self.FONT_TITLE, anchor="w"
        )
        title_lbl.pack(fill=tk.X, pady=(0, 12))

        # ── Panel de parámetros ──────────────────────────────────────────────
        params_frame = tk.LabelFrame(
            outer,
            text=" Parameters ",
            bg=self.PANEL, fg=self.FG_DIM,
            font=self.FONT_LABEL,
            bd=1, relief=tk.FLAT,
            labelanchor="nw",
            padx=12, pady=10
        )
        params_frame.pack(fill=tk.X, pady=(0, 10))

        # Grid interno
        params_frame.columnconfigure(1, weight=1)

        # Fila 0 – XML Project File
        self._make_label(params_frame, "XML Project File", 0)
        self.xml_entry = self._make_entry(params_frame, self.xml_path_var, 0)
        self._make_browse_btn(
            params_frame, row=0, col=2,
            command=self._browse_xml,
            filetypes=[("XML files", "*.xml"), ("All files", "*.*")]
        )

        # Fila 1 – Output file name
        self._make_label(params_frame, "Output file name", 1)
        self._make_entry(params_frame, self.output_name_var, 1)
        # Botón placeholder invisible para mantener alineación
        tk.Label(params_frame, bg=self.PANEL, width=11).grid(row=1, column=2, padx=(6, 0))

        # Fila 2 – Output format
        self._make_label(params_frame, "Output format", 2)
        fmt_combo = ttk.Combobox(
            params_frame,
            textvariable=self.format_var,
            values=["md", "docx"],
            state="readonly",
            width=10,
            font=self.FONT_ENTRY
        )
        fmt_combo.grid(row=2, column=1, sticky="w", pady=4)
        self._style_combobox(fmt_combo)
        fmt_combo.bind("<<ComboboxSelected>>", self._on_format_change)

        # Fila 3 – Template
        self._make_label(params_frame, "Template (.docx)", 3)
        self.template_entry = self._make_entry(params_frame, self.template_var, 3)
        self._make_browse_btn(
            params_frame, row=3, col=2,
            command=self._browse_template,
            filetypes=[("Word documents", "*.docx"), ("All files", "*.*")]
        )

        # Estado inicial del campo Template
        self._on_format_change()

        # ── Botón Process ────────────────────────────────────────────────────
        btn_row = tk.Frame(outer, bg=self.BG)
        btn_row.pack(fill=tk.X, pady=(0, 8))

        self.process_btn = tk.Button(
            btn_row,
            text="▶  Process files",
            bg=self.BTN_BG, fg=self.BTN_FG,
            activebackground=self.BTN_ACT, activeforeground=self.BTN_FG,
            font=self.FONT_BTN,
            relief=tk.FLAT, bd=0,
            padx=16, pady=6,
            cursor="hand2",
            command=self._run_process
        )
        self.process_btn.pack(side=tk.RIGHT)

        self.clear_btn = tk.Button(
            btn_row,
            text="✕  Clear log",
            bg=self.BTN2_BG, fg=self.BTN2_FG,
            activebackground="#404060", activeforeground=self.FG,
            font=self.FONT_BTN,
            relief=tk.FLAT, bd=0,
            padx=12, pady=6,
            cursor="hand2",
            command=self._clear_log
        )
        self.clear_btn.pack(side=tk.RIGHT, padx=(0, 8))

        # ── Log console ──────────────────────────────────────────────────────
        log_frame = tk.LabelFrame(
            outer,
            text=" Log console ",
            bg=self.PANEL, fg=self.FG_DIM,
            font=self.FONT_LABEL,
            bd=1, relief=tk.FLAT,
            labelanchor="nw",
            padx=8, pady=8
        )
        log_frame.pack(fill=tk.BOTH, expand=True)

        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            bg=self.LOG_BG, fg=self.FG,
            insertbackground=self.ACCENT,
            font=self.FONT_LOG,
            relief=tk.FLAT, bd=0,
            state="disabled",
            wrap=tk.WORD
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)

        # Tags de color para el log
        self.log_text.tag_config("info",    foreground=self.FG)
        self.log_text.tag_config("error",   foreground=self.ERROR_FG)
        self.log_text.tag_config("warning", foreground=self.WARN_FG)
        self.log_text.tag_config("success", foreground=self.SUCCESS_FG)
        self.log_text.tag_config("dim",     foreground=self.FG_DIM)

    # ── Helpers de construcción de widgets ───────────────────────────────────

    def _make_label(self, parent, text: str, row: int):
        tk.Label(
            parent, text=text,
            bg=self.PANEL, fg=self.FG_DIM,
            font=self.FONT_LABEL, anchor="w", width=18
        ).grid(row=row, column=0, sticky="w", pady=4)

    def _make_entry(self, parent, textvariable, row: int):
        entry = tk.Entry(
            parent,
            textvariable=textvariable,
            bg=self.ENTRY_BG, fg=self.ENTRY_FG,
            insertbackground=self.ACCENT,
            relief=tk.FLAT, bd=0,
            font=self.FONT_ENTRY,
            highlightthickness=1,
            highlightbackground=self.BTN2_BG,
            highlightcolor=self.ACCENT
        )
        entry.grid(row=row, column=1, sticky="ew", padx=(6, 6), pady=4)
        return entry

    def _make_browse_btn(self, parent, row: int, col: int, command, filetypes=None):
        btn = tk.Button(
            parent,
            text="Browse…",
            bg=self.BTN2_BG, fg=self.BTN2_FG,
            activebackground="#404060", activeforeground=self.FG,
            font=self.FONT_BTN,
            relief=tk.FLAT, bd=0,
            padx=8, pady=3,
            cursor="hand2",
            command=command
        )
        btn.grid(row=row, column=col, sticky="e", padx=(0, 0), pady=4)
        btn._filetypes = filetypes
        return btn

    def _style_combobox(self, combo: ttk.Combobox):
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "TCombobox",
            fieldbackground=self.ENTRY_BG,
            background=self.BTN2_BG,
            foreground=self.ENTRY_FG,
            selectbackground=self.ACCENT,
            selectforeground="#ffffff",
            arrowcolor=self.ACCENT,
            borderwidth=0
        )

    # ── Redireccionamiento de output ─────────────────────────────────────────

    def _redirect_output(self):
        """Conecta stdout y stderr al widget de log."""
        sys.stdout = _TextRedirector(self.log_text, "info")
        sys.stderr = _TextRedirector(self.log_text, "error")

    # ── Callbacks ────────────────────────────────────────────────────────────

    def _browse_xml(self):
        path = filedialog.askopenfilename(
            title="Select XML Project File",
            filetypes=[("XML files", "*.xml"), ("All files", "*.*")]
        )
        if path:
            self.xml_path_var.set(path)
            # Sugerir nombre de salida automáticamente
            if not self.output_name_var.get():
                self.output_name_var.set(Path(path).stem)

    def _browse_template(self):
        path = filedialog.askopenfilename(
            title="Select .docx Template",
            filetypes=[("Word documents", "*.docx"), ("All files", "*.*")]
        )
        if path:
            self.template_var.set(path)

    def _on_format_change(self, event=None):
        """Habilita/deshabilita el campo Template según el formato seleccionado."""
        fmt = self.format_var.get()
        if fmt == "docx":
            self.template_entry.configure(state="normal")
        else:
            self.template_entry.configure(state="disabled")
            self.template_var.set("")

    def _clear_log(self):
        self.log_text.configure(state="normal")
        self.log_text.delete("1.0", tk.END)
        self.log_text.configure(state="disabled")

    def _log(self, msg: str, tag: str = "info"):
        """Escribe directamente en el log con el tag indicado."""
        self.log_text.configure(state="normal")
        self.log_text.insert(tk.END, msg + "\n", tag)
        self.log_text.see(tk.END)
        self.log_text.configure(state="disabled")

    def _run_process(self):
        """Valida inputs y lanza el procesamiento en un hilo separado."""

        xml_path     = self.xml_path_var.get().strip()
        output_name  = self.output_name_var.get().strip()
        fmt          = self.format_var.get()
        template     = self.template_var.get().strip()

        # ── Validaciones básicas ─────────────────────────────────────────────
        if not xml_path:
            self._log("❌ Error: Please select an XML Project File.", "error")
            return

        if not Path(xml_path).exists():
            self._log(f"❌ Error: File not found: {xml_path}", "error")
            return

        if fmt == "docx" and not template:
            self._log("❌ Error: A .docx template is required for DOCX output.", "error")
            return

        if fmt == "docx" and not Path(template).exists():
            self._log(f"❌ Error: Template not found: {template}", "error")
            return

        # Deshabilitar botón mientras procesa
        self.process_btn.configure(state="disabled", text="⏳  Processing…")
        self._clear_log()

        # Lanzar en hilo para no bloquear la UI
        threading.Thread(
            target=self._worker,
            args=(xml_path, output_name, fmt, template),
            daemon=True
        ).start()

    def _worker(self, xml_path: str, output_name: str, fmt: str, template: str):
        """Ejecuta el procesamiento real (en hilo separado)."""
        try:
            from pathlib import Path
            import helpFunctions as helpers
            from projectParser import PSProjectParser
            from projectDocGen import DocGenerator

            xml_path_obj = Path(xml_path)
            salida_base  = output_name or xml_path_obj.stem

            # Corregir root XML
            fixed = helpers.fixRootTag(xml_path)
            if fixed:
                print("⚠️  XML fixed: <root> tag automatically added.")

            # Parseo
            print(f"🔍 Parsing: {xml_path_obj.name} …")
            parser  = PSProjectParser(xml_path)
            project = parser.parse()
            print(f"✅ Project parsed: {project.project_name}")

            # Generación
            gen = DocGenerator(project, output_format=fmt, template_path=template or None)

            if fmt == "md":
                md_path = salida_base if salida_base.endswith(".md") else f"{salida_base}.md"
                gen.to_markdown(md_path)
                print(f"✅ Markdown generated: {md_path}", )
                self._log(f"✅ Done → {md_path}", "success")

            elif fmt == "docx":
                docx_path = salida_base if salida_base.endswith(".docx") else f"{salida_base}.docx"
                gen.to_docx(docx_path)
                print(f"✅ DOCX generated: {docx_path}")
                self._log(f"✅ Done → {docx_path}", "success")

        except Exception as exc:
            import traceback
            print(f"❌ Error: {exc}", file=sys.stderr)
            traceback.print_exc()

        finally:
            # Restaurar botón en el hilo principal
            self.after(0, lambda: self.process_btn.configure(
                state="normal", text="▶  Process files"
            ))


# ── Entrada ─────────────────────────────────────────────────────────────────

def main():
    app = AppWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
