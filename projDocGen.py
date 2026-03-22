# ============================================================================
# Proyecto:        pyPSPrintProject
# Descripción:     Print Project de proyecto de proyecto exportado a XML
# Nombre Archivo:  projDocGen.py
# Autor:           akanashiro@gmail.com
# Historial de Modificaciones:
# Fecha            Autor        Ref.     Descripción
# 2026/03/22       AKF          #001     CLI para generación de documento
# ============================================================================


"""
projDocGen.py
-------------------
Genera documentación de un proyecto PeopleSoft en formato DOCX (via
python-docx-template con Jinja2) o Markdown.

Requisitos:
    pip install docxtpl python-docx

Uso:
    from ps_docprojDocGen_generator import DocGenerator
    gen = DocGenerator(project, template_path="plantilla.docx")
    gen.to_docx("output.docx")
    gen.to_markdown("output.md")
"""
# Begin 001
from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING
import re

if TYPE_CHECKING:
    from ps_project_parser import PSProject


# ---------------------------------------------------------------------------
# Construcción por consola
# ---------------------------------------------------------------------------

def printToConsole(projectObj_: PSProject):
    """
    Función de ayuda para imprimir la información del proyecto en consola.
    :param projectObj_: Objeto del proyecto con la información parseada
    """
    print(f"✅ Proyecto: {projectObj_.project_name}")
    print(f"✅ Descripción: {projectObj_.description}")

    print ("=================================")

    contaNbr = 1
    for record in projectObj_.records:
        record.getRecordInfo()
        if contaNbr < len(projectObj_.records):
            print ("--------------------------------")
        contaNbr += 1

    print ("=================================")
    
    contaNbr = 1
    for field in projectObj_.fields:
        field.getFieldInfo()
        if contaNbr < len(projectObj_.fields):
            print ("--------------------------------")
        contaNbr += 1
    
    print ("=================================")

    contaNbr = 1
    for process in projectObj_.processes:
        process.getProcessInfo()
        if contaNbr < len(projectObj_.processes):
            print ("--------------------------------")
        contaNbr += 1

    print ("=================================")
    contaNbr = 1

# ---------------------------------------------------------------------------
# Construcción del contexto Jinja2
# ---------------------------------------------------------------------------

def build_context(project: "PSProject") -> dict:
    """
    Convierte el objeto PSProject en un diccionario plano apto para Jinja2.
    Todas las listas y objetos se serializan como dicts para que la plantilla
    pueda iterar con {% for %} y acceder con {{ }}.
    """

    def xv_to_dict(xv):
        return {
            "value": xv.value,
            "long_name": xv.long_name,
            "short_name": xv.short_name,
            "effective_date": xv.effective_date or "",
            "status": xv.status or "",
        }

    def rf_to_dict(rf):
        flags = []
        if rf.is_key:            flags.append("Key")
        if rf.is_duplicate_key:  flags.append("Duplicate Key")
        if rf.is_alternate_key:  flags.append("Alternate Key")
        if rf.is_search_key:     flags.append("Search Key")
        if rf.is_list_box:       flags.append("List Box")
        if rf.is_from_search:    flags.append("From Search")
        if rf.is_required:       flags.append("Required")
        return {
            "name": rf.name,
            "field_type": rf.field_type,
            "length": rf.length or "",
            "decimals": rf.decimals or "",
            "flags": ", ".join(flags) if flags else "—",
            "default_value": rf.default_value or "",
            "label": rf.label or "",
            # "translate_values": [xv_to_dict(x) for x in rf.translate_values],
            # "has_xlat": bool(rf.translate_values),
        }

    def pc_to_dict(pc):
        return {
            "record_name": pc.record_name,
            "field_name": pc.field_name,
            "event_type": pc.event_type,
            "full_name": f"{pc.record_name}.{pc.field_name}.{pc.event_type}" if pc.field_name
                         else f"{pc.record_name}.{pc.event_type}",
            "source_code": pc.source_code,
            "functions": pc.functions,
            "has_functions": bool(pc.functions),
        }

    def ae_step_to_dict(step):
        return {
            "step_name": step.get("step_name", ""),
            "actions": step.get("actions", []),
        }

    def ae_section_to_dict(sect):
        return {
            "section_name": sect.section_name,
            "section_type": sect.section_type,
            "steps": [ae_step_to_dict(s) for s in sect.steps],
            "has_steps": bool(sect.steps),
        }

    def comp_rec_to_dict(cr):
        return {
            "record_name": cr.record_name,
            "record_type": cr.record_type,
            "scroll_level": cr.scroll_level,
        }

    # --- Records ---
    records = []
    for r in project.records:
        rec_dict = {
            "name": r.name,
            "record_type": r.record_type,
            "description": r.description or "",
            "parent_record": r.parent_record or "",
            "fields": [rf_to_dict(f) for f in r.fields],
            "field_count": len(r.fields),
            "has_sql_view": bool(r.sql_view_text),
            "sql_view_text": r.sql_view_text or "",
            "is_view": r.record_type in ("SQL View", "Dynamic View", "Query View"),
            "is_derived": r.record_type == "Derived/Work",
        }
        records.append(rec_dict)

    # --- Fields con Translate Values ---
    fields = []
    for f in project.fields:
        fields.append({
            "name": f.name,
            "field_type": f.field_type,
            "length": f.length or "",
            "decimals": f.decimals or "",
            "long_name": f.long_name or "",
            "short_name": f.short_name or "",
            "description": f.description or ""
            #"translate_values": [xv_to_dict(x) for x in f.translate_values],
            #"has_xlat": bool(f.translate_values),
            #"xlat_count": len(f.translate_values),
        })

    # --- Processes ---
    processes = [
        {
            "name": p.name,
            "process_type": p.process_type,
            "description": p.description or "",
            "run_location": p.run_location or "",
        }
        for p in project.processes
    ]

    # --- Resumen / Stats ---
    summary = {
        "records":           len(records),
        "fields":            len(fields),        
        "processes":         len(processes),
        "total":             sum([
            len(records), len(fields), len(processes)])

    }

    # Flags de presencia (para mostrar/ocultar secciones en la plantilla)
    has = {k: v > 0 for k, v in summary.items()}

    return {
        "project_name":       project.project_name,
        "description":        project.description or "",
        "summary":            summary,
        "has":                has,
        "records":            records,
        "fields":             fields,
        "processes":         processes
    }


# ---------------------------------------------------------------------------
# Generador DOCX (python-docx-template)
# ---------------------------------------------------------------------------

class DocxGenerator:

    def __init__(self, template_path: str):
        try:
            from docxtpl import DocxTemplate
        except ImportError:
            raise ImportError("Instalá python-docx-template: pip install docxtpl")

        self.DocxTemplate = DocxTemplate
        self.template_path = template_path

    def generate(self, context: dict, output_path: str):
        doc = self.DocxTemplate(self.template_path)
        doc.render(context)
        doc.save(output_path)
        print(f"✅ DOCX generado: {output_path}")


# ---------------------------------------------------------------------------
# Generador Markdown
# ---------------------------------------------------------------------------

class MarkdownGenerator:

    def generate(self, context: dict, output_path: str):
        lines = []
        self._write(lines, context)
        Path(output_path).write_text("\n".join(lines), encoding="utf-8")
        print(f"✅ Markdown generado: {output_path}")

    def _write(self, lines: list, ctx: dict):
        a = lines.append

        a(f"# Proyecto PeopleSoft: {ctx['project_name']}")
        a("")
        if ctx["description"]:
            a(ctx["description"])
            a("")

        # Resumen
        a("## Resumen del Proyecto")
        a("")
        a("| Tipo de Objeto | Cantidad |")
        a("|----------------|----------|")
        s = ctx["summary"]
        for label, key in [
            ("Records",            "records"),
            ("Fields",             "fields"),
            ("Pages",              "pages"),
            ("Components",         "components"),
            ("Menus",              "menus"),
            ("PeopleCode Events",  "peoplecode_events"),
            ("SQL Objects",        "sql_objects"),
            ("App Engine Programs","app_engines"),
            ("App Packages",       "app_packages"),
            ("Messages",           "messages"),
            ("Process Definitions","processes"),
            ("Service Operations", "service_operations"),
            ("Queries",            "queries"),
            ("Style Sheets",       "style_sheets"),
            ("Roles",              "roles"),
            ("File Layouts",       "file_layouts"),
            ("Portal Definitions", "portals"),
        ]:
            if s.get(key, 0) > 0:
                a(f"| {label} | {s[key]} |")
        #a(f"| **TOTAL** | **{s['total']}** |")
        a("")

        # Records
        if ctx["has"]["records"]:
            a("---")
            a("## Records")
            a("")
            for rec in ctx["records"]:
                a(f"### {rec['name']}")
                a("")
                a(f"**Tipo:** {rec['record_type']}  ")
                if rec["description"]:
                    a(f"**Descripción:** {rec['description']}  ")
                if rec["parent_record"]:
                    a(f"**Parent Record:** {rec['parent_record']}  ")
                a("")

                if rec["fields"]:
                    a("#### Campos")
                    a("")
                    a("| Campo | Tipo | Long. | Flags | Label |")
                    a("|-------|------|-------|-------|-------|")
                    for f in rec["fields"]:
                        length = str(f["length"]) if f["length"] else ""
                        a(f"| {f['name']} | {f['field_type']} | {length} | {f['flags']} | {f['label']} |")
                    a("")

                if rec["is_view"] and rec["sql_view_text"]:
                    a("#### SQL del View")
                    a("")
                    a("```sql")
                    a(rec["sql_view_text"])
                    a("```")
                    a("")

        # Fields standalone (con Translate Values)
        if ctx["has"]["fields"]:
            a("---")
            a("## Fields")
            a("")
            for fld in ctx["fields"]:
                a(f"### {fld['name']}")
                a("")
                a(f"**Tipo:** {fld['field_type']}  ")
                if fld["length"]:
                    a(f"**Longitud:** {fld['length']}  ")
                if fld["long_name"]:
                    a(f"**Nombre Largo:** {fld['long_name']}  ")
                if fld["short_name"]:
                    a(f"**Nombre Corto:** {fld['short_name']}  ")
                if fld["description"]:
                    a(f"**Descripción:** {fld['description']}  ")
                a("")

                """
                if fld["has_xlat"]:
                    a(f"#### Translate Values ({fld['xlat_count']} valores)")
                    a("")
                    a("| Valor | Nombre Largo | Nombre Corto | F. Efectiva | Estado |")
                    a("|-------|-------------|--------------|-------------|--------|")
                    for xv in fld["translate_values"]:
                        a(f"| {xv['value']} | {xv['long_name']} | {xv['short_name']} | {xv['effective_date']} | {xv['status']} |")
                    a("")                    
                """
        # Processes
        if ctx["has"]["processes"]:
            a("---")
            a("## Process Definitions")
            a("")
            for proc in ctx["processes"]:
                a(f"### {proc['name']}")
                a("")
                a(f"**Tipo:** {proc['process_type']}  ")
                if proc["run_location"]:
                    a(f"**Run Location:** {proc['run_location']}  ")
                if proc["description"]:
                    a(f"**Descripción:** {proc['description']}  ")
                a("")

# ---------------------------------------------------------------------------
# Clase principal (fachada)
# ---------------------------------------------------------------------------

class DocGenerator:

    def __init__(self, project: "PSProject", template_path: str = None):
        self.project = project
        self.template_path = template_path
        self.context = build_context(project)

    def to_docx(self, output_path: str):
        if not self.template_path:
            raise ValueError("Se requiere template_path para generar DOCX.")
        gen = DocxGenerator(self.template_path)
        gen.generate(self.context, output_path)

    def to_markdown(self, output_path: str):
        gen = MarkdownGenerator()
        gen.generate(self.context, output_path)

    def get_context(self) -> dict:
        """Retorna el contexto para inspección o plantillas personalizadas."""
        return self.context
# End 001