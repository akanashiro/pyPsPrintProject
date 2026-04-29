# ============================================================================
# Proyecto:        pyPSPrintProject
# Descripción:     Print Project de proyecto de proyecto exportado a XML
# Nombre Archivo:  main.py
# Autor:           akanashiro@gmail.com
# ============================================================================

import argparse
import sys
from pathlib import Path
from projectParser import PSProjectParser, PSProject
from projectDocGen import DocGenerator, printToConsole
import helpFunctions as helpers


def main():
    """
    Función principal del generador de documentación.
    """

    parserObj = argparse.ArgumentParser(description="PeopleSoft Project technical document generator",
    formatter_class=argparse.RawDescriptionHelpFormatter,epilog="""
    Examples: 
    python main.py MyProject.xml --format md --output docs/MyProject.md
    python main.py MyProject.xml --format docx --template template_file.docx
    """)

    parserObj.add_argument("xml_path",
        help="Path to exported XML from Application Designer")
    parserObj.add_argument("--format", "-f",
        choices=["docx", "md"],
        default="md",
        help="Output format: docx or md (default: md)")
    parserObj.add_argument("--template", "-t",
        help="Path to .docx template with Jinja2 placeholders (required for --format docx)")
    parserObj.add_argument("--output", "-o",
        help="Output path without extension (extension added automatically)")

    args = parserObj.parse_args()

    # Validaciones
    xml_path = Path(args.xml_path)
    if not xml_path.exists():
        print(f"❌ Error: File not found: {xml_path}", file=sys.stderr)
        sys.exit(1)

    if args.format in ("docx") and not args.template:
        print("❌ Error: --template is required to generate DOCX.", file=sys.stderr)
        sys.exit(1)

    if args.template and not Path(args.template).exists():
        print(f"❌ Error: Template not found: {args.template}", file=sys.stderr)
        sys.exit(1)


    # Corregir root automáticamente si hace falta
    try:
        fixed = helpers.fixRootTag(args.xml_path)
        if fixed:
            print(f"⚠️  XML fixed: <root> tag automatically added.")
    except (FileNotFoundError, ValueError) as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Salida base
    salida_base = args.output or xml_path.stem

    # Parseo
    print(f"🔍 Parsing: {xml_path.name} ...")
    try:
        parserObj = PSProjectParser(str(xml_path))
        projectObj = parserObj.parse()
        # printToConsole(projectObj)        

    except Exception as e:
        print(f"❌ Error parsing XML: {e}", file=sys.stderr)
        sys.exit(1)

    # Generación
    
    gen = DocGenerator(projectObj, output_format = args.format, template_path=args.template)

    if args.format in ("md"):
        md_path = salida_base if salida_base.endswith(".md") else f"{salida_base}.md"
        gen.to_markdown(md_path)

    if args.format in ("docx"):
        docx_path = salida_base if salida_base.endswith(".docx") else f"{salida_base}.docx"
        gen.to_docx(docx_path)
    

if __name__ == "__main__":
    main()