# ============================================================================
# Project:          pyPSPrintProject
# Description:      UI Tkinter para pyPSPrintProject
# File:             mainTk.py
# Author:           akanashiro@gmail.com
# License:          MIT - read LICENSE in repo
# ============================================================================
"""
ui_tkinter.py
-------------
Interfaz gráfica multiplataforma (Windows / Linux / macOS) construida con
Tkinter + ttk.

Selección de tema:
  - Windows : usa el tema nativo "vista" (ttk built-in)
  - macOS   : usa el tema nativo "aqua"  (ttk built-in)
  - Linux   : si está instalado ttkthemes, intenta "arc" o "breeze";
              de lo contrario usa "clam" (ttk built-in)

Instalar temas extra (opcional, solo mejora apariencia en Linux):
    pip install ttkthemes

Uso:
    python ui_tkinter.py
"""

import sys
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path

# ── ttkthemes (opcional) ───────────────────────────────────────────────────
try:
    from ttkthemes import ThemedTk
    _HAS_THEMED = True
except ImportError:
    _HAS_THEMED = False

# ── Módulos del proyecto (opcionales: la UI funciona en modo demo sin ellos) ─
try:
    from projectParser import PSProjectParser
    from projectDocGen import DocGenerator
    import helpFunctions as helpers
    _HAS_PROJECT = True
except ImportError:
    _HAS_PROJECT = False

# ── Some constants ───────────────────────────────────────────────────
ABOUT_COLOR = "#1a73e8"
ABOUT_HOVER = "#4285f4"


# ══════════════════════════════════════════════════════════════════════════════
# Redireccionador de stdout / stderr → widget Text
# ══════════════════════════════════════════════════════════════════════════════

class _TextRedirector:
    """Redirige print() y sys.stderr al cuadro de log de la UI."""

    def __init__(self, widget: tk.Text, tag: str = "normal"):
        self._widget = widget
        self._tag    = tag

    def write(self, msg: str):
        # Siempre actualizar desde el hilo principal de Tkinter
        self._widget.after(0, self._append, msg)

    def _append(self, msg: str):
        self._widget.configure(state="normal")
        self._widget.insert(tk.END, msg, self._tag)
        self._widget.see(tk.END)
        self._widget.configure(state="disabled")

    def flush(self):
        pass


# ══════════════════════════════════════════════════════════════════════════════
# Ventana principal
# ══════════════════════════════════════════════════════════════════════════════

class App:
    """Ventana principal de pyPSPrintProject."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("pyPSPrintProject")
        self.root.resizable(True, True)
        self.root.minsize(700, 480)

        self._build_ui()
        self._redirect_streams()
        self._toggle_template()   # deshabilita Template si el formato es "md"

    # --------------------------------------------------------
    # About hyperlink hover effects
    # --------------------------------------------------------
    def _aboutHoverIn(self, event):
        self.about_label.config(fg=ABOUT_HOVER)

    def _aboutHoverOut(self, event):
        self.about_label.config(fg=ABOUT_COLOR)

    # --------------------------------------------------------
    # About pop-up window
    # --------------------------------------------------------
    def _showAbout(self):
        about = tk.Toplevel(self.root)
        about.title("About")
        
        about.geometry("420x300")
        about.resizable(False, False)
        
        about.transient(self.root)
        about.wait_visibility()
        about.grab_set()
        
        frame = ttk.Frame(about, padding=20)
        frame.pack(fill="both", expand=True)
        
        text = (
            "pyPSPrintProject 1.1.0\n\n"
            "PeopleSoft Project technical document generator.\n\n"
            "This UI was built with Tkinter.\n"
            "Agustín Kanashiro.\n"
            "2026\n\n"
            "https://github.com/akanashiro/pyPsPrintProject"
        )

        ttk.Label(frame, text=text, justify="center").pack(expand=True)
        ttk.Button(frame, text="Close", command=about.destroy).pack(pady=(15, 0))
        

    # ── Construcción de la UI ──────────────────────────────────────────────

    def _build_ui(self):
        root = self.root

        main = ttk.Frame(root, padding="12 12 12 8")
        main.grid(row=0, column=0, sticky="nsew")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main.columnconfigure(1, weight=1)
        main.rowconfigure(5, weight=1)   # la consola se expande verticalmente

        pad = {"padx": 5, "pady": 4}

        # ── Fila 0 · XML Project File ──────────────────────────────────────
        ttk.Label(main, text="XML Project File:").grid(
            row=0, column=0, sticky="w", **pad)
        self._xml_var = tk.StringVar()
        ttk.Entry(main, textvariable=self._xml_var).grid(
            row=0, column=1, sticky="ew", **pad)
        ttk.Button(main, text="Browse…",
                   command=self._browse_xml).grid(row=0, column=2, **pad)

        # ── Fila 1 · Output file name ──────────────────────────────────────
        ttk.Label(main, text="Output file name:").grid(
            row=1, column=0, sticky="w", **pad)
        self._out_var = tk.StringVar()
        ttk.Entry(main, textvariable=self._out_var).grid(
            row=1, column=1, sticky="ew", **pad)
        ttk.Button(main, text="Browse…",
                   command=self._browse_output).grid(row=1, column=2, **pad)

        # ── Fila 2 · Output format ─────────────────────────────────────────
        ttk.Label(main, text="Output format:").grid(
            row=2, column=0, sticky="w", **pad)
        self._fmt_var = tk.StringVar(value="md")
        fmt_combo = ttk.Combobox(
            main,
            textvariable=self._fmt_var,
            values=["md", "docx"],
            state="readonly",
            width=12,
        )
        fmt_combo.grid(row=2, column=1, sticky="w", **pad)
        fmt_combo.bind("<<ComboboxSelected>>",
                       lambda _e: self._toggle_template())

        # ── Fila 3 · Template (.docx) ──────────────────────────────────────
        self._tpl_label = ttk.Label(main, text="Template (.docx):")
        self._tpl_label.grid(row=3, column=0, sticky="w", **pad)
        self._tpl_var = tk.StringVar()
        self._tpl_entry = ttk.Entry(main, textvariable=self._tpl_var)
        self._tpl_entry.grid(row=3, column=1, sticky="ew", **pad)
        self._tpl_btn = ttk.Button(
            main, text="Browse…", command=self._browse_template)
        self._tpl_btn.grid(row=3, column=2, **pad)

        # ── Fila 4 · Botón Process ─────────────────────────────────────────
        btn_frame = ttk.Frame(main)
        #btn_frame.grid(row=4, column=0, columnspan=3, sticky="e", pady=8)
        btn_frame.grid(row=4, column=0, columnspan=3, sticky="e", **pad)
        self._run_btn = ttk.Button(
            btn_frame, text="Process files", command=self._run)
        self._run_btn.pack()

        # ── Fila 5 · Log console ───────────────────────────────────────────
        ttk.Label(main, text="Log console:").grid(
            row=5, column=0, columnspan=3, sticky="w", padx=5, pady=(4, 0))

        log_frame = ttk.Frame(main)
        log_frame.grid(row=6, column=0, columnspan=3, sticky="nsew",
                       padx=5, pady=(2, 4))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        main.rowconfigure(6, weight=1)

        mono_font = ("Consolas", 9) if sys.platform == "win32" \
            else ("Menlo", 10)      if sys.platform == "darwin" \
            else ("Monospace", 9)

        self._log = tk.Text(
            log_frame,
            state="disabled",
            wrap="word",
            height=10,
            font=mono_font,
        )
        self._log.grid(row=0, column=0, sticky="nsew")

        vsb = ttk.Scrollbar(log_frame, orient="vertical",
                            command=self._log.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        self._log.configure(yscrollcommand=vsb.set)

        # Colores semánticos en el log (se ajustan a fondo claro u oscuro)
        self._log.tag_configure("warning", foreground="#B8860B")
        self._log.tag_configure("error",   foreground="#CC0000")
        self._log.tag_configure("ok",      foreground="#2E7D32")

        # ── About ────────────────────────────────────────────────────
        self.about_label = tk.Label(main, text="About", fg="blue", cursor="hand2")
        self.about_label.grid(row=7, column=2, columnspan=3, sticky="e", padx=2, pady=(8, 4))

        self.about_label.bind("<Enter>", self._aboutHoverIn)
        self.about_label.bind("<Leave>", self._aboutHoverOut)
        self.about_label.bind("<Button-1>", lambda e: self._showAbout())       


    # ── Habilitación/deshabilitación del campo Template ────────────────────

    def _toggle_template(self):
        is_docx = self._fmt_var.get() == "docx"
        state = "normal" if is_docx else "disabled"
        self._tpl_entry.configure(state=state)
        self._tpl_btn.configure(state=state)

    # ── Diálogos de archivos ───────────────────────────────────────────────

    def _browse_xml(self):
        path = filedialog.askopenfilename(
            title="Select XML project file",
            filetypes=[("XML files", "*.xml *.XML"), ("All files", "*.*")],
        )
        if path:
            self._xml_var.set(path)
            if not self._out_var.get():          # sugerir nombre de salida
                self._out_var.set(str(Path(path).stem))

    def _browse_output(self):
        fmt = self._fmt_var.get()
        path = filedialog.asksaveasfilename(
            title="Select output file",
            defaultextension=f".{fmt}",
            filetypes=[(f"{fmt.upper()} files", f"*.{fmt}"),
                       ("All files", "*.*")],
        )
        if path:
            self._out_var.set(path)

    def _browse_template(self):
        path = filedialog.askopenfilename(
            title="Select DOCX template",
            filetypes=[("Word documents", "*.docx"), ("All files", "*.*")],
        )
        if path:
            self._tpl_var.set(path)

    # ── Redirección de streams ─────────────────────────────────────────────

    def _redirect_streams(self):
        sys.stdout = _TextRedirector(self._log, "normal")
        sys.stderr = _TextRedirector(self._log, "error")

    # ── Validación de inputs ───────────────────────────────────────────────

    def _validate(self) -> bool:
        xml  = self._xml_var.get().strip()
        out  = self._out_var.get().strip()
        fmt  = self._fmt_var.get()
        tpl  = self._tpl_var.get().strip()

        if not xml:
            messagebox.showerror("Validation error",
                                 "Please select the XML project file.")
            return False
        if not Path(xml).exists():
            messagebox.showerror("Validation error",
                                 f"File not found:\n{xml}")
            return False
        if not out:
            messagebox.showerror("Validation error",
                                 "Please specify the output file name.")
            return False
        if fmt == "docx" and not tpl:
            messagebox.showerror("Validation error",
                "A template (.docx) is required for DOCX output.")
            return False
        if fmt == "docx" and not Path(tpl).exists():
            messagebox.showerror("Validation error",
                                 f"Template not found:\n{tpl}")
            return False
        return True

    # ── Ejecución en hilo secundario ───────────────────────────────────────

    def _run(self):
        if not self._validate():
            return
        self._run_btn.configure(state="disabled")
        threading.Thread(target=self._process, daemon=True).start()

    def _process(self):
        xml  = self._xml_var.get().strip()
        out  = self._out_var.get().strip()
        fmt  = self._fmt_var.get()
        tpl  = self._tpl_var.get().strip() or None

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
            self.root.after(0,
                lambda: self._run_btn.configure(state="normal"))


# ══════════════════════════════════════════════════════════════════════════════
# Selección de tema
# ══════════════════════════════════════════════════════════════════════════════

def _setup_theme(root: tk.Tk):
    """Aplica el mejor tema disponible según la plataforma."""
    style = ttk.Style(root)
    platform = sys.platform

    if platform == "win32":
        style.theme_use("vista")
    elif platform == "darwin":
        style.theme_use("aqua")
    else:
        # Linux: intentar arc / breeze vía ttkthemes, si no → clam
        if _HAS_THEMED:
            available = root.get_themes() if hasattr(root, "get_themes") else []
            for candidate in ("arc", "breeze", "clearlooks"):
                if candidate in available:
                    root.set_theme(candidate)
                    return
        for t in ("clam", "alt", "default"):
            if t in style.theme_names():
                style.theme_use(t)
                return


# ══════════════════════════════════════════════════════════════════════════════
# Entry point
# ══════════════════════════════════════════════════════════════════════════════

def main():
    if _HAS_THEMED and sys.platform not in ("win32", "darwin"):
        root = ThemedTk()
    else:
        root = tk.Tk()

    _setup_theme(root)
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
