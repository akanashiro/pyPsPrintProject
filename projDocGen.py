# ============================================================================
# Project:          pyPSPrintProject
# Description:      Print Project de proyecto de proyecto exportado a XML
# Nombre Archivo:  projDocGen.py
# Author:           akanashiro@gmail.com
# License:          MIT - read LICENSE in repo
# Changelog:
# Date             Author       Ref.     Description
# 2026/03/22       AKF          #001     Document render engine.
# ============================================================================


"""
projDocGen.py
-------------------
Genera documentación de un proyecto PeopleSoft en formato DOCX (via
python-docx-template con Jinja2) o Markdown.

Requisites:
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
from docxtpl import RichText

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

    for sql in projectObj_.sql_objects:
        sql.getSQLInfo()
        if contaNbr < len(projectObj_.sql_objects):
            print ("--------------------------------")
        contaNbr += 1

    print ("=================================")
    contaNbr = 1

    for pcode in projectObj_.ap_peoplecode:
        pcode.getPeopleCodeInfo()
        if contaNbr < len(projectObj_.ap_peoplecode):
            print ("--------------------------------")
        contaNbr += 1

    print ("=================================")


# ---------------------------------------------------------------------------
# Construcción del contexto Jinja2
# ---------------------------------------------------------------------------

def build_context(project: "PSProject", output_format: str) -> dict:
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
        if rf.is_key == True:            flags.append("Key")
        if rf.is_duplicate_key == True:  flags.append("Duplicate Key")
        if rf.is_alternate_key == True:  flags.append("Alternate Key")
        if rf.is_search_key == True:     flags.append("Search Key")
        if rf.is_list_box == True:       flags.append("List Box")
        if rf.is_from_search == True:    flags.append("From Search")
        if rf.is_required == True:       flags.append("Required")
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

    """ 
    def pc_to_dict(pc):
        return {
            "record_name": pc.record_name,
            "field_name": pc.field_name,
            "event_type": pc.event_type,
            "full_name": f"{pc.record_name}.{pc.field_name}.{pc.event_type}" if pc.field_name
                         else f"{pc.record_name}.{pc.event_type}",
            "source_code": pc.source_code,
            #"functions": pc.functions,
            #"has_functions": bool(pc.functions),
        }

    def appPackage_pc_to_dict(pc):
        return {
            "app_package": pc.app_package,
            "code_type": pc.code_type,
            "event": pc.event,
            "source_code": pc.source_code,
        }    
    """
    def pc_to_dict(pc, outStr: str):

        match outStr:
            case "md":
                return {
                    "component":    pc.component,
                    "market":       pc.market,                    
                    "record_name":  pc.record_name,
                    "field_name":   pc.field_name,
                    "event_type":   pc.event_type,
                    "full_name": f"{pc.record_name}.{pc.field_name}.{pc.event_type}" if pc.field_name else f"{pc.record_name}.{pc.event_type}",
                    "code_type":    pc.code_type,
                    "source_code": pc.source_code
                    #"functions": pc.functions,
                    #"has_functions": bool(pc.functions),
                }
            case "docx":
                # Convertir source_code a RichText para manejar saltos de línea
                rt = RichText()
                lines = (pc.source_code or "").split("\n")
                for i, line in enumerate(lines):
                    rt.add(line, font="Courier New", size=18, color="#595959")
                    if i < len(lines) - 1:
                        rt.add("\a")   # \a = salto de línea en docxtpl (w:br)
                return {
                    "component":    pc.component,
                    "market":       pc.market,                    
                    "record_name":  pc.record_name,
                    "field_name":   pc.field_name,
                    "event_type":   pc.event_type,
                    "full_name":    f"{pc.record_name}.{pc.field_name}.{pc.event_type}" if pc.field_name else f"{pc.record_name}.{pc.event_type}",
                    "code_type":    pc.code_type,
                    "source_code":  rt,
                }

    def appPackage_pc_to_dict(pc, output: str):

        match output:
            case "md":
                return {
                    "app_package": pc.app_package,
                    "code_type": pc.code_type,
                    "event": pc.event,
                    "source_code": pc.source_code,
                }   
            case "docx":
                rt = RichText()
                lines = (pc.source_code or "").split("\n")
                for i, line in enumerate(lines):
                    rt.add(line, font="Courier New", size=18, color="#595959")
                    if i < len(lines) - 1:
                        rt.add("\a")
                return {
                    "app_package":  pc.app_package,
                    "code_type":    pc.code_type,
                    "event":        pc.event,
                    "source_code":  rt,
                } 

    def convertPc(pc: str, output: str) -> str:

        match output:
            case "md":
                return pc.source_code
            case "docx":
                rt = RichText()
                lines = pc.split("\n")
                for i, line in enumerate(lines):
                    rt.add(line, font="Courier New", size=18, color="#595959")
                    if i < len(lines) - 1:
                        rt.add("\a")
                return  rt


    def ae_step_actions(action):
        #print(f"Action type: {action.action_type}")
        #print(f"PeopleCode: {action.peoplecode}")
        # print(f"call: {action.call}")
        return {
            "action_type": action.action_type or "",
            "peoplecode":  convertPc(action.peoplecode.source_code, output_format) if action.peoplecode else None,
            "sql": action.sql.sql_text if action.sql else None,
            "call": action.call or "prueba"
        }

    def ae_step_to_dict(step):
        # print(f"Step name: {step.step_name}")
        return {
            "step_name": step.step_name, #step.get("step_name", "")
            "step_actions": [ae_step_actions(a) for a in step.step_actions],
        }

    def ae_section_to_dict(sect):
        # debug print(f"tiene steps {bool(sect.steps)}")
        return {
            "section_name": sect.section_name,
            "program_name": sect.program_name,
            #"section_type": sect.section_type,
            "steps": [ae_step_to_dict(s) for s in sect.steps],
            #"steps": sect.steps,
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

    # --- SQL Objects ---
    sql_objects = [
        {
            "name": s.name,
            "sql_type": s.sql_type,
            "description": s.description or "",
            "sql_text": s.sql_text,
        }
        for s in project.sql_objects
    ]


    # --- Pages ---
    pages = [
        {
            "name": p.name,
            "page_type": p.page_type,
            "description": p.description or "",
            #
            #"controls": [
            #    {
            #        "control_type": c.control_type,
            #        "record_name": c.record_name or "",
            #        "field_name": c.field_name or "",
            #        "label": c.label or "",
            #    }
            #    for c in p.controls
            #]
            #"control_count": len(p.controls),

        }
        for p in project.pages
    ]

    # --- File Layouts ---
    file_layouts = [
        {
            "name": fl.name,
            "file_type": fl.file_type,
            "description": fl.description or "",
            "delimiter": fl.delimiter or "",
            "records": fl.records,
        }
        for fl in project.file_layouts
    ]

    # --- Menus ---
    menus = [
        {
            "name": m.name,
            #"menu_type": m.menu_type,
            "description": m.description or "",
            #"menu_items": m.menu_items,
        }
        for m in project.menus
    ]

    # --- App Engine ---
    app_engines = [
        {
            "name": ae.name,
            "aeType": ae.aeType,
            "description": ae.description or "",
            "disRestart": ae.disRestart,
            "aetRecords": ae.aetRecords,
            "sections": [ae_section_to_dict(s) for s in ae.sections],
            #"sections": ae.sections,
            "section_count": len(ae.sections),
            #"peoplecode": [pc_to_dict(p) for p in ae.peoplecode],
            #"has_peoplecode": bool(ae.peoplecode),
        }
        for ae in project.app_engines
    ]    

    # --- Processes ---
    processes = [
        {
            "name": p.name,
            "process_type": p.process_type,
            "description": p.description or "",
            "run_location": p.run_location or "",
            "parameters": p.parameters or "",
            "components": p.components or [],
            "procGroups": p.procGroups or []
        }
        for p in project.processes
    ]

    # --- Jobs ---
    jobs = [
        {
            "jobName": p.jobName,
            "jobDescr": p.jobDescr,
            "processList": p.processList
        }
        for p in project.jobs
    ]

    # --- PeopleCode (agrupado por record) ---
    pc_by_record: dict[str, list] = {}
    for pc in project.peoplecode:
        # debug print (f"{pc.record_name}.{pc.field_name}.{pc.event_type}")
        key = pc.record_name
        
        if pc.code_type == "Record":
            pc_by_record.setdefault(key, []).append(pc_to_dict(pc, output_format))
        
    peoplecode_groups = [
        {"record_name": rec, "events": evts}            
        for rec, evts in sorted(pc_by_record.items())
    ]

    # --- PeopleCode (agrupado por componente) ---
    
    pc_by_comp: dict[str, list] = {}
    for pc in project.peoplecode:
        # debug print (f"{pc.record_name}.{pc.field_name}.{pc.event_type}")
        key = pc.component

        if pc.code_type == "Component":
            pc_by_comp.setdefault(key, []).append(pc_to_dict(pc, output_format))
        
    pc_comp_groups = [
        {"component": comp, "events": evts}            
        for comp, evts in sorted(pc_by_comp.items())
    ]    

    pc_by_crf: dict[str, list] = {}
    for pc in project.peoplecode:
        # debug print (f"{pc.record_name}.{pc.field_name}.{pc.event_type}")
        key = pc.component

        if pc.code_type == "Component Record Field":
            pc_by_crf.setdefault(key, []).append(pc_to_dict(pc, output_format))
        
    pc_crf_groups = [
        {"component": comp, "events": evts}            
        for comp, evts in sorted(pc_by_crf.items())
    ]    


    # --- Application Package PeopleCode (agrupado por App Package) ---
    pc_by_app_package: dict[str, list] = {}
    for pc in project.ap_peoplecode:
        key = pc.app_package
        pc_by_app_package.setdefault(key, []).append(appPackage_pc_to_dict(pc, output_format))

    ap_peoplecode_grp = [
        {"app_package": app_pkg, "events": evts}
        for app_pkg, evts in sorted(pc_by_app_package.items())
    ]    


    # Service Operation
    service_operations = [
        {
            "name": p.name,
            "restMethod": p.restMethod,
            "description": p.description,
            "comments": p.comments,
            "restBaseUrl": p.restBaseUrl,
            "uriTemplates": p.uriTemplates
        }
        for p in project.service_operations
    ]

    # --- Message Catalog ---
    msg_catalog = [
        {
            "message_set": m.message_set,
            "message_number": m.message_number,
            "severity": m.severity,
            "message_text": m.message_text,
            "explanation": m.explanation or "",
        }
        for m in sorted(project.msg_catalog, key=lambda x: (x.message_set, x.message_number))
    ]    


    # --- Resumen / Stats ---
    summary = {
        "records":           len(records),
        "fields":            len(fields),   
        "pages":             len(project.pages),
        "sql_objects":       len(sql_objects),             
        "menus":             len(menus),        
        "processes":         len(processes),
        "jobs":              len(jobs),
        "peoplecode_events": len(project.peoplecode),
        "ap_peoplecode":     len(ap_peoplecode_grp),
        "app_engines":       len(app_engines),
        "service_operations":len(service_operations),
        "msg_catalog":       len(msg_catalog),
        "file_layouts":      len(file_layouts),        
        "total":             sum([
            len(records), len(fields),len(project.pages), len(sql_objects), len(processes), len(jobs), len(project.peoplecode), len(ap_peoplecode_grp), \
            len(service_operations), len(app_engines), len(msg_catalog), len(file_layouts), len(menus)]
        )
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
        "pages":              pages,
        "sql_objects":        sql_objects,
        "menus":              menus,
        "processes":          processes,
        "app_engines":        app_engines,
        "jobs":               jobs,
        "peoplecode_groups":  peoplecode_groups,
        "pc_comp_groups":     pc_comp_groups,
        "pc_crf_groups":      pc_crf_groups,
        "ap_peoplecode_grp":  ap_peoplecode_grp,
        "service_operations": service_operations,
        "msg_catalog":        msg_catalog,
        "file_layouts":       file_layouts        
    }


# ---------------------------------------------------------------------------
# Generador DOCX (python-docx-template)
# ---------------------------------------------------------------------------

class DocxGenerator:

    def __init__(self, template_path: str):
        try:
            from docxtpl import DocxTemplate
        except ImportError:
            raise ImportError("Install python-docx-template: pip install docxtpl")

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
            ("PeopleCode Events",   "peoplecode_events"),
            ("App Package PeopleCode",  "ap_peoplecode"),
            ("SQL Objects",        "sql_objects"),
            ("App Engine Programs","app_engines"),
            ("App Packages",       "app_packages"),
            ("Messages",           "messages"),
            ("Process Definitions","processes"),
            ("Job Definitions",     "jobs"),
            ("Service Operations", "service_operations"),
            ("Queries",            "queries"),
            ("Style Sheets",       "style_sheets"),
            ("Roles",              "roles"),
            ("File Layouts",       "file_layouts"),
            ("Portal Definitions", "portals"),
        ]:
            if s.get(key, 0) > 0:
                a(f"| {label} | {s[key]} |")
        
        a(f"| **TOTAL** | **{s['total']}** |")
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

        # Pages
        if ctx["has"]["pages"]:
            a("---")
            a("## Pages")
            a("")
            for pg in ctx["pages"]:
                a(f"### {pg['name']}")
                a("")
                a(f"**Tipo:** {pg['page_type']}  ")
                if pg["description"]:
                    a(f"**Descripción:** {pg['description']}  ")
                """
                a(f"**Controles:** {pg['control_count']}  ")
                a("")
                
                if pg["controls"]:
                    a("| Control | Record | Campo | Label |")
                    a("|---------|--------|-------|-------|")
                    for ctrl in pg["controls"]:
                        a(f"| {ctrl['control_type']} | {ctrl['record_name']} | {ctrl['field_name']} | {ctrl['label']} |")
                    a("")
                """


        # SQL Objects
        if ctx["has"]["sql_objects"]:
            a("---")
            a("## SQL Objects")
            a("")
            for sql in ctx["sql_objects"]:
                a(f"### {sql['name']}")
                a("")
                if sql["description"]:
                    a(f"**Descripción:** {sql['description']}  ")
                a("")
                a("```sql")
                a(sql["sql_text"])
                a("```")
                a("")


        # Record PeopleCode
        if ctx["peoplecode_groups"]:
            a("---")
            a("## Record PeopleCode")
            a("")
            for group in ctx["peoplecode_groups"]:
                a(f"### Record: {group['record_name']}")
                a("")
                for evt in group["events"]:
                    a(f"#### {evt['full_name']}")
                    a("")
                    #if evt["has_functions"]:
                    #    a(f"**Funciones definidas:** {', '.join(evt['functions'])}  ")
                    #    a("")
                    a("```peoplecode")
                    a(evt["source_code"])
                    a("```")
                    a("")

        # Component PeopleCode
        if ctx["pc_comp_groups"]:
            a("---")
            a("## Record PeopleCode")
            a("")
            for group in ctx["pc_comp_groups"]:
                a(f"### Component: {group['component']}")
                a("")
                for evt in group["events"]:
                    a(f"#### {evt['full_name']}")
                    a(f"#### {evt['market']}")
                    a("")
                    #if evt["has_functions"]:
                    #    a(f"**Funciones definidas:** {', '.join(evt['functions'])}  ")
                    #    a("")
                    a("```peoplecode")
                    a(evt["source_code"])
                    a("```")
                    a("")

        # Component Record Field PeopleCode
        if ctx["pc_crf_groups"]:
            a("---")
            a("## Record PeopleCode")
            a("")
            for group in ctx["pc_crf_groups"]:
                a(f"### Component: {group['component']}")
                a("")
                for evt in group["events"]:
                    a(f"#### {evt['full_name']}")
                    a("")
                    #if evt["has_functions"]:
                    #    a(f"**Funciones definidas:** {', '.join(evt['functions'])}  ")
                    #    a("")
                    a("```peoplecode")
                    a(evt["source_code"])
                    a("```")
                    a("")


        # App Package PeopleCode
        if ctx["ap_peoplecode_grp"]:
            a("---")
            a("## App Package PeopleCode")
            a("")
            for group in ctx["ap_peoplecode_grp"]:
                a(f"### Application Package: {group['app_package']}")
                a("")
                for evt in group["events"]:
                    a(f"#### {evt['event']}")
                    a("")                    
                    a("```peoplecode")
                    a(evt["source_code"])
                    a("```")
                    a("")

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

    def __init__(self, project: "PSProject", output_format: str, template_path: str = None):
        self.project = project
        self.template_path = template_path
        self.context = build_context(project, output_format)

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