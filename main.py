# ============================================================================
# Proyecto:        pyPSPrintProject
# Descripción:     Print Project de proyecto de proyecto exportado a XML
# Nombre Archivo:  main.py
# Autor:           akanashiro@gmail.com
# Historial de Modificaciones:
# Fecha            Autor        Ref.     Descripción
# 2026/03/22       AKF          #001     CLI para generación de documento
# ============================================================================

# Begin 001
import argparse
import sys
from pathlib import Path
from projectParser import PSProjectParser, PSProject
from projDocGen import DocGenerator, printToConsole



def main():
    """
    Función principal del generador de documentación.
    """

    parserObj = argparse.ArgumentParser(description="Generador de documentación para proyectos PeopleSoft",
    formatter_class=argparse.RawDescriptionHelpFormatter,epilog="""
    Ejemplos: 
    python main.py MiProyecto.xml --format md --output docs/MiProyecto.md
    python main.py MiProyecto.xml --format docx --template plantilla.docx
    python main.py MiProyecto.xml --format both --template plantilla.docx --output docs/MiProyecto""")

    parserObj.add_argument("xml_path",
        help="Ruta al archivo XML exportado desde Application Designer")
    parserObj.add_argument("--format", "-f",
        choices=["docx", "md", "both"],
        default="md",
        help="Formato de salida: docx, md, o ambos (default: md)")
    parserObj.add_argument("--template", "-t",
        help="Ruta a la plantilla .docx con marcadores Jinja2 (requerido para --formato docx/ambos)")
    parserObj.add_argument("--output", "-o",
        help="Ruta de salida sin extensión (se agrega automáticamente) o con extensión si es un formato único")

    args = parserObj.parse_args()

    # Validaciones
    xml_path = Path(args.xml_path)
    if not xml_path.exists():
        print(f"❌ Error: No se encontró el archivo: {xml_path}", file=sys.stderr)
        sys.exit(1)

    if args.format in ("docx", "both") and not args.template:
        print("❌ Error: --plantilla es requerido para generar DOCX.", file=sys.stderr)
        sys.exit(1)

    if args.template and not Path(args.plantilla).exists():
        print(f"❌ Error: No se encontró la plantilla: {args.plantilla}", file=sys.stderr)
        sys.exit(1)

    # Salida base
    salida_base = args.output or xml_path.stem

    # Parseo
    print(f"🔍 Parseando: {xml_path.name} ...")
    try:
        parserObj = PSProjectParser(str(xml_path))
        projectObj = parserObj.parse()
        # printToConsole(projectObj)        

    except Exception as e:
        print(f"❌ Error al parsear el XML: {e}", file=sys.stderr)
        sys.exit(1)

    # Generación
    
    gen = DocGenerator(projectObj, template_path=args.template)

    if args.format in ("md", "both"):
        md_path = salida_base if salida_base.endswith(".md") else f"{salida_base}.md"
        gen.to_markdown(md_path)

    #if args.format in ("docx", "both"):
    #    docx_path = salida_base if salida_base.endswith(".docx") else f"{salida_base}.docx"
    #    gen.to_docx(docx_path)
    

if __name__ == "__main__":
    main()
# End 001