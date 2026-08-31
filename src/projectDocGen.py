# ============================================================================
# Project:          pyPSPrintProject
# Description:      Print Project de proyecto de proyecto exportado a XML
# Nombre Archivo:   projectDocGen.py
# Author:           akanashiro at gmail dot com
# License:          MIT - read LICENSE in repo
# ============================================================================


"""
projectDocGen.py
-------------------
Genera documentación de un proyecto PeopleSoft en formato DOCX (via
python-docx-template con Jinja2).

Requisites:
    pip install docxtpl python-docx

Uso:
    from ps_docprojDocGen_generator import DocGenerator
    gen = DocGenerator(project, template_path="plantilla.docx")
    gen.to_docx("output.docx")
"""

from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING
import re
from docxtpl import RichText

if TYPE_CHECKING:
    from ps_project_parser import PSProject

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

    def formatSQL(sql) -> str:
        rt = RichText()
        lines = sql.split("\n")
        for i, line in enumerate(lines):
            rt.add(line, font="Courier New", size=18, color="#595959")
            if i < len(lines) - 1:
                rt.add("\a")
        return  rt

    def pc_to_dict(pc):

        # Convertir source_code a RichText para manejar saltos de línea
        rt = RichText()
        lines = (pc.source_code or "").split("\n")
        for i, line in enumerate(lines):
            rt.add(line, font="Courier New", size=18, color="#595959")
            if i < len(lines) - 1:
                rt.add("\a")   # \a = salto de línea en docxtpl (w:br)

        partesLst = [pc.component, pc.record_name, pc.field_name, pc.event_type]
        #print(f"Debug pc_to_dict: partesLst={partesLst}, full_name={'.'.join(parte for parte in partesLst if parte)}")
        return {
            "component":    pc.component,
            "market":       pc.market,                    
            "record_name":  pc.record_name,
            "field_name":   pc.field_name,
            "event_type":   pc.event_type,
            # "full_name":    f"{pc.component}.{pc.market}.{pc.record_name}.{pc.field_name}.{pc.event_type}" 
            #                 if pc.component and pc.market and pc.record_name and pc.field_name and pc.event_type
            #                   else f"{pc.record_name}.{pc.field_name}.{pc.event_type}",
            "full_name":    ".".join(parte for parte in partesLst if parte),
            "code_type":    pc.code_type,
            "source_code":  rt,
        }

    def appPackage_pc_to_dict(pc):
        rt = RichText()
        lines = (pc.source_code or "").split("\n")
        
        for i, line in enumerate(lines):
            rt.add(line)
            if i < len(lines) - 1:
                rt.add("\a")
        return {
            "app_package":  pc.app_package,
            "code_type":    pc.code_type,
            "event":        pc.event,
            "source_code":  rt,
        } 

    def convertPc(pc, output: str) -> str:

        match output:
            case "md":
                return pc
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
            "log_message": action.log_message or "",
            "call": action.call or "prueba",
            "description": action.description or ""
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
            "description": r.description or "-",
            "parent_record": r.parent_record or "-",
            "fields": [rf_to_dict(f) for f in r.fields],
            "field_count": len(r.fields),
            #"has_sql_view": bool(r.sql_view_text),
            "sql_view_text": r.sql_view_text if bool(r.sql_view_text) else "-",
            "is_view": bool(r.record_type in ("View", "Dynamic View", "Query View")),
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
            #"description": f.description or ""
            "translate_values": [xv_to_dict(x) for x in f.translate_values] if f.translate_values else [],
            "has_xlat": bool(f.translate_values) if f.translate_values else [],
            "xlat_count": len(f.translate_values) if f.translate_values else "0",
        })

    # --- SQL Objects ---
    sql_objects = [
        {
            "name": s.name,
            "sql_type": s.sql_type,
            "description": s.description or "-",
            "sql_text": s.sql_text if bool(s.sql_text) else "-",
        }
        for s in project.sql_objects
    ]

    # --- Permission lists ---
    permission_lists = [
        {
            "name": pl.name,
            "description": pl.description or "-",
            "menu_items": pl.menu_items,
        }
        for pl in project.permission_lists
    ]

    # --- Roles ---
    roles = [
        {
            "name": r.name,
            "description": r.description or "-",
            "permissions": r.permissions,
            "permission_count": len(r.permissions),
        }
        for r in project.roles
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

    # --- BI Publisher Reports ---
    bi_reports = [
        {
            "name": r.name,
            "description": r.description,
            "data_source": r.data_source,
            "template_type": r.template_type,
            "template_id": r.template_id,
            "output_format": r.output_format,
        }
        for r in project.bi_reports
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

    # --- Portals ---
    portals = [
        {
            "name": p.name,
            "label": p.label or "",
            "object_name": p.object_name,
            "portal_type": p.portal_type,
            "url": p.url or "",
            "description": p.description or "",
        }
        for p in project.portals
    ]

    # --- Queries ---
    queries = [
        {
            "name": q.name,
            "query_type": q.query_type,
            "description": q.description or "",
            "sql_text": q.sql_text,
        }
        for q in project.queries
    ]

    # --- Menus ---
    menus = [
        {
            "name": m.name,
            "menu_type": m.menu_type,
            "description": m.description or "-",
            #"menu_items": m.menu_items,
        }
        for m in project.menus
    ]

    # --- App Engine ---
    app_engines = [
        {
            "name": ae.name,
            "ae_type": ae.ae_type,
            "description": ae.description or "-",
            "disable_restart": ae.disable_restart,
            "aet_records": ae.aet_records,
            "temp_records": ae.temp_records,
            "sections": [ae_section_to_dict(s) for s in ae.sections],
            #"sections": ae.sections,
            "section_count": len(ae.sections),
            #"peoplecode": [pc_to_dict(p) for p in ae.peoplecode],
            #"has_peoplecode": bool(ae.peoplecode),
        }
        for ae in project.app_engines
    ]    

    # --- Components ---
    components = [
        {
            "name": c.name,
            "market": c.market,
            "description": c.description or "",
            "search_record": c.search_record or "",
            "add_search_record": c.add_search_record or "",
            "pages": c.pages,
            #"records": [comp_rec_to_dict(r) for r in c.records],
            #"peoplecode": [pc_to_dict(p) for p in c.peoplecode],
            #"has_peoplecode": bool(c.peoplecode),
        }
        for c in project.components
    ]

    # --- Component Interfaces ---
    component_interfaces = [
        {
            "name": ci.name,
            "display_name": ci.display_name or "",
            "description": ci.description or "",
            "panel_group": ci.panel_group or "",
            "search_record": ci.search_record or "",
            "add_search_record": ci.add_search_record or "",
        }
        for ci in project.component_interfaces
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
            "process_groups": p.process_groups or []
        }
        for p in project.processes
    ]

    # --- Jobs ---
    jobs = [
        {
            "job_name": p.job_name,
            "job_descr": p.job_descr,
            "process_list": p.process_list
        }
        for p in project.jobs
    ]

    # --- PeopleCode (agrupado por record) ---
    pc_by_record: dict[str, list] = {}
    for pc in project.peoplecode:
        # debug print (f"{pc.record_name}.{pc.field_name}.{pc.event_type}")
        key = pc.record_name
        
        if pc.code_type == "Record":
            pc_by_record.setdefault(key, []).append(pc_to_dict(pc))
        
    peoplecode_groups = [
        {"record_name": rec, "events": evts}            
        for rec, evts in sorted(pc_by_record.items())
    ]

    # --- Page PeopleCode (agrupado por page) ---
    pc_by_page: dict[str, list] = {}
    for pc in project.peoplecode:
        # debug print (f"{pc.record_name}.{pc.field_name}.{pc.event_type}")
        key = pc.record_name
        
        if pc.code_type == "Page":
            pc_by_page.setdefault(key, []).append(pc_to_dict(pc))
    
    page_peoplecode_groups = [
        {"record_name": rec, "events": evts}
        for rec, evts in sorted(pc_by_page.items())
    ]

    # --- PeopleCode (agrupado por componente) ---
    
    pc_by_comp: dict[str, list] = {}
    for pc in project.peoplecode:
        # debug print (f"{pc.record_name}.{pc.field_name}.{pc.event_type}")
        key = pc.component

        if pc.code_type == "Component":
            pc_by_comp.setdefault(key, []).append(pc_to_dict(pc))
        
    pc_comp_groups = [
        {"component": comp, "events": evts}            
        for comp, evts in sorted(pc_by_comp.items())
    ]    

    pc_by_cr: dict[str, list] = {}
    for pc in project.peoplecode:
        key = pc.component

        if pc.code_type == "Component Record":
            pc_by_cr.setdefault(key, []).append(pc_to_dict(pc))
        
    pc_cr_groups = [
        {"component": comp, "events": evts}            
        for comp, evts in sorted(pc_by_cr.items())
    ]  

    pc_by_crf: dict[str, list] = {}
    for pc in project.peoplecode:
        # debug print (f"{pc.record_name}.{pc.field_name}.{pc.event_type}")
        key = pc.component

        if pc.code_type == "Component Record Field":
            pc_by_crf.setdefault(key, []).append(pc_to_dict(pc))
        
    pc_crf_groups = [
        {"component": comp, "events": evts}            
        for comp, evts in sorted(pc_by_crf.items())
    ]    


    # --- Application Package PeopleCode (agrupado por App Package) ---
    pc_by_app_package: dict[str, list] = {}

    for pc in project.ap_peoplecode:
        key = pc.app_package
        pc_by_app_package.setdefault(key, []).append(appPackage_pc_to_dict(pc))

    ap_peoplecode_grp = [
        {"app_package": app_pkg, "events": evts}
        for app_pkg, evts in sorted(pc_by_app_package.items())
    ]    

    # Documents
    documents = [
        {
            "package": doc.package,
            "name": doc.name,
            "version": doc.version,
            "label": doc.label or "",
            "elements": doc.elements or [],
            "physical_schemas": doc.physical_schemas or [],
            "xsd": doc.xsd or ""
        }
        for doc in project.documents
    ]

    # Message
    messages =[
        {
            "name" : msg.name,
            "message_type" : msg.getMessageType(),
            "message_type_code" : msg.message_type,
            "message_version" : msg.message_version,
            "package_id" : msg.package_id or "",
            "schema_name" : msg.schema_name or "",
            "package_ver" : msg.package_ver or ""
        }
        for msg in project.messages
    ]

    # Service Operation
    service_operations = [
        {
            "name": p.name,
            "rest_method": p.rest_method,
            "description": p.description,
            "comments": p.comments,
            "rest_base_url": p.rest_base_url,
            "uri_templates": p.uri_templates
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

    # --- App Packages ---
    app_packages = [
        {
            "name": pkg.name,
            "description": pkg.description or "",
            "classes": [
                {
                    "class_name": cls.class_name,
                    "package_path": cls.package_path,
                    "source_code": cls.source_code,
                    "methods": cls.methods,
                    "properties": cls.properties,
                    "has_methods": bool(cls.methods),
                    "has_properties": bool(cls.properties),
                }
                for cls in pkg.classes
            ],
            "class_count": len(pkg.classes),
            "sub_packages": pkg.sub_packages,
            "has_sub_packages": bool(pkg.sub_packages),
        }
        for pkg in project.app_packages
    ]


    # --- Resumen / Stats ---
    summary = {
        "components":        len(components),
        "component_interfaces": len(component_interfaces),
        "records":           len(records),
        "fields":            len(fields),   
        "pages":             len(project.pages),
        "sql_objects":       len(sql_objects),             
        "menus":             len(menus),        
        "processes":         len(processes),
        "jobs":              len(jobs),
        #"peoplecode_events": len(project.peoplecode),
        "record_pcode": len(peoplecode_groups),
        "component_pcode":      len(pc_comp_groups),
        "component_record_pcode": len(pc_cr_groups),
        "component_record_field_pcode": len(pc_crf_groups),
        "page_peoplecode":   len(page_peoplecode_groups),
        "ap_peoplecode":     len(project.ap_peoplecode),
        "app_engines":       len(app_engines),
        "app_packages":      len(app_packages),
        "documents":         len(documents),
        "messages":          len(messages),
        "service_operations":len(service_operations),
        "msg_catalog":       len(msg_catalog),
        "file_layouts":      len(file_layouts),
        "permission_lists":  len(permission_lists),
        "roles":             len(roles),
        "queries":           len(queries),
        "bi_reports":        len(bi_reports),
        "portals":           len(portals),        
        "total":             sum([
            len(components), len(component_interfaces), len(records), len(fields),len(project.pages), len(sql_objects), len(processes), len(jobs),\
            len(peoplecode_groups), len(pc_comp_groups), len(pc_cr_groups), len(pc_crf_groups), len(page_peoplecode_groups), len(project.ap_peoplecode),\
            len(messages), len(documents), len(service_operations), len(app_engines), len(msg_catalog),\
            len(file_layouts), len(menus), len(permission_lists), len(queries), len(bi_reports), len(roles), len(portals),\
            len(app_packages)]
        )
    }

    # Flags de presencia (para mostrar/ocultar secciones en la plantilla)
    has = {k: v > 0 for k, v in summary.items()}

    return {
        "project_name":       project.project_name,
        "description":        project.description or "",
        "longdescription":    project.longdescription or "",
        "summary":            summary,
        "has":                has,
        "components":         components,
        "component_interfaces": component_interfaces,
        "records":            records,
        "fields":             fields,
        "pages":              pages,
        "sql_objects":        sql_objects,
        "menus":              menus,
        "processes":          processes,
        "app_engines":        app_engines,
        "app_packages":       app_packages,        
        "jobs":               jobs,
        "peoplecode_groups":  peoplecode_groups,
        "page_peoplecode_groups": page_peoplecode_groups,
        "pc_comp_groups":     pc_comp_groups,
        "pc_cr_groups":       pc_cr_groups,
        "pc_crf_groups":      pc_crf_groups,
        "ap_peoplecode_grp":  ap_peoplecode_grp,
        "service_operations": service_operations,
        "msg_catalog":        msg_catalog,
        "file_layouts":       file_layouts,
        "permission_lists":   permission_lists,
        "queries":            queries,
        "bi_reports":         bi_reports,
        "roles":              roles,
        "portals":            portals,
        "messages":           messages,
        "documents":          documents
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
        print(f"✅ DOCX created: {output_path}")


# ---------------------------------------------------------------------------
# Clase principal
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

    def get_context(self) -> dict:
        """Retorna el contexto para inspección o plantillas personalizadas."""
        return self.context