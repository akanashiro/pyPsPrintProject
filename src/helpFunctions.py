# ============================================================================
# Project:          pyPSPrintProject
# Description:      Print Project de proyecto de proyecto exportado a XML
# File:             helpFunctions.py
# Author:           akanashiro at gmail dot com
# License:          MIT - read LICENSE in repo
# ============================================================================
"""
helpFunctions.py
-------------------
Funciones auxiliares para el proyecto pyPSPrintProject, incluyendo:
- decodeFieldType: Convierte el código de tipo de campo a una descripción legible
- decodRecordType: Convierte el código de tipo de registro a una descripción legible
- decodePageType: Decodes the code of the page type (pageTypeStr_) to a readable description.
- decodeFieldFlags: Decode the bits of the fUseEdit field from the XML to determine what type of field is.
- fixRootTag: Add <root> tag that wraps the entire XML if it doesn't exist.

Requisites:
    N/A

"""

import re
import os

# ============================================================================
# Project Parse helper functions from HERE
# ============================================================================

def decodeFieldType(fieldTypeStr_: str) -> str:
    """
    Convierte el código de tipo de campo (fieldTypeStr_) a una descripción legible.

    :param fieldTypeStr_: Código de tipo de campo (string)
    :return: Descripción legible del tipo de campo
    """

    match fieldTypeStr_:
        case "0":
            return "Char"
        case "1":
            return "Long Char"
        case "2":
            return "Number"
        case "3":
            return "Signed Number"
        case "4":
            return "Date"
        case "5":
            return "Time"
        case "6":
            return "DateTime"
        case "8":
            return "Image / Attachment"
        case "9":
            return "Image Reference"

    return f"Unknown ({fieldTypeStr_})"

def decodeRecordType(recTypeStr_: str) -> str:
    """
    Convierte el código de tipo de registro (recTypeStr_) a una descripción legible.
    :param recTypeStr_: Código de tipo de registro (string)
    :return: Descripción legible del tipo de registro
    """

    match recTypeStr_:
        case "0":
            return "Table"
        case "1":
            return "View"
        case "2":
            return "Derived/Work"
        case "3":
            return "Subrecord"
        case "4":
            return "Dynamic View"
        case "5":
            return "Query View"
        case "7":
            return "Temporary Table"
            
    return f"Unknown ({recTypeStr_})" 

def decodePageType(pageTypeStr_: str) -> str:
    """
    Decodes the code of the page type (pageTypeStr_) to a readable description.
    :param pageTypeStr_: Code of the page type (string)
    :return: Readable description of the page type
    """

    match pageTypeStr_:
        case "0":
            return "Standard"
        case "1":
            return "Subpage"
        case "2":
            return "Popup"
        case "3":
            return "System"
    
    return f"Unknown ({pageTypeStr_})"

def decodeFieldFlags(useEditValueNbr_ : int) -> dict:
    """
    Decode the bits of the fUseEdit field from the XML to determine what type of field is.

    :param useEditValueNbr_: numeric value of the USEEDIT column
    :return: dict with the decoded field flags, including:
          - 'value':       the original value
          - 'bits':        list of bit values that compose the value
          - 'flags':       list of descriptions for each active flag
          - 'description': readable string with all flags joined by ' + '
    """


    # Mapeo completo de USEEDIT extraído de https://www2.go-faster.co.uk/static/useedit.htm
    USEEDIT_FLAGS = {
        1:          "Key Value",
        2:          "Duplicate (unique) key",
        4:          "System Maintained Field",
        8:          "Audit field - add",
        16:         "Alternate search key",
        32:         "List box item",
        64:         "Ascending (descending) key field",
        128:        "Audit field - change",
        256:        "Required field",
        512:        "X/Lat (Translate Table)",
        1024:       "Audit field - delete",
        2048:       "Search key",
        4096:       "Edits - Reasonable Date",
        8192:       "Edits - Yes/No",
        16384:      "Prompt table edit enabled",
        32768:      "Auto Update",
        65536:      "Unknown (bit 16)",
        131072:     "Unknown (bit 17)",
        262144:     "From search field",
        524288:     "To search field",
        1048576:    "1/0 Table Edit",
        2097152:    "Disable advanced search options",
        4194304:    "Unknown (bit 22)",
        8388608:    "Regular field (sub-record)",
        16777216:   "Default search field",
        33554432:   "Unknown (bit 25)",
        67108864:   "Unknown (bit 26)",
        134217728:  "Keys - Allow Search Events for Prompt Dialogs",
        268435456:  "Keys - Search Edit",
        536870912:  "Edits - Display in Autocomplete Window",
        1073741824: "Autocomplete - Enable Autocomplete when used in Search Record",
        2147483648: "Menu - Persist in Menu",
    }

    valueNbr = useEditValueNbr_

    if valueNbr < 0:
        raise ValueError(f"El valor debe ser un entero positivo. Recibido: {valueNbr}")

    activeBitsArray  = []
    activeFlagsArray = []

    # Recorre cada bit de mayor a menor para descomponer el valor
    for bitValueNbr in sorted(USEEDIT_FLAGS.keys(), reverse=True):
        if valueNbr >= bitValueNbr:
            valueNbr -= bitValueNbr
            activeBitsArray.append(bitValueNbr)
            activeFlagsArray.append(USEEDIT_FLAGS[bitValueNbr])

    # Si sobra algo, hay bits no mapeados
    if valueNbr > 0:
        activeBitsArray.append(valueNbr)
        activeFlagsArray.append(f"Unknown (valor residual: {valueNbr})")

    # Ordenar de menor a mayor para presentación
    combined = sorted(zip(activeBitsArray, activeFlagsArray), key=lambda x: x[0])
    activeBitsArray  = [b for b, _ in combined]
    activeFlagsArray = [f for _, f in combined]

    return {
        "value":       useEditValueNbr_,
        "bits":        activeBitsArray,
        "flags":       activeFlagsArray,
        "description": " + ".join(activeFlagsArray) if activeFlagsArray else "Sin flags activos",
    }

def fixRootTag(filepath: str,hasBackupBool: bool = True) -> bool:
    """
    Add <root> tag that wraps the entire XML if it doesn't exist.
    :param filepath: path to the XML file.
    :param hasBackupBool: If True, saves a backup copy with a .bak extension before modifying.
    :return: True if the file was modified, False if it was already valid.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError:        If the file is empty or does not appear to be XML.
    """

    # rootTagStr:  Nombre del tag raíz a insertar (default: "root").
    rootTagStr = "root"
    

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Archivo no encontrado: {filepath}")

    with open(filepath, encoding="utf-8", errors="replace") as f:
        content = f.read()

    if not content.strip():
        raise ValueError(f"El archivo está vacío: {filepath}")

    # Detectar si ya tiene un único elemento raíz válido
    # Estrategia: buscar si el primer tag de apertura tiene su cierre al final
    stripped = content.strip()

    # Extraer declaración XML si existe (<?xml ... ?>)
    xmlDeclareStr = ""
    body = stripped
    decl_match = re.match(r"^(<\?xml[^?]*\?>)\s*", stripped, re.IGNORECASE)
    if decl_match:
        xmlDeclareStr = decl_match.group(1)
        body = stripped[decl_match.end():]

    # Detectar si el body ya tiene UN solo elemento raíz
    # (empieza con <tag y termina con </tag>)
    single_root_match = re.match(r"^<([a-zA-Z_][\w\-.]*)[\s>]", body)
    if single_root_match:
        first_tag = single_root_match.group(1)
        closing_tag = f"</{first_tag}>"
        if body.rstrip().endswith(closing_tag):
            # Ya tiene un root válido, no tocar
            return False

    # Necesita root: construir el nuevo contenido
    if hasBackupBool:
        backupPathStr = filepath + ".bak"
        with open(backupPathStr, "w", encoding="utf-8") as f:
            f.write(content)

    newContentStr = ""
    if xmlDeclareStr:
        newContentStr += xmlDeclareStr + "\n"

    newContentStr += f"<{rootTagStr}>\n"
    newContentStr += body.strip() + "\n"
    newContentStr += f"</{rootTagStr}>\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(newContentStr)

    return True

# ============================================================================
# Project Doc Generator helper functions from HERE
# ============================================================================
def formatPeopleCode(pc) -> str:
    rt = RichText()
    lines = pc.split("\n")
    for i, line in enumerate(lines):
        rt.add(line, font="Courier New", size=18, color="#595959")
        if i < len(lines) - 1:
            rt.add("\a")
    return  rt


def formatSQL(sql) -> str:
    rt = RichText()
    lines = sql.split("\n")
    for i, line in enumerate(lines):
        rt.add(line, font="Courier New", size=18, color="#595959")
        if i < len(lines) - 1:
            rt.add("\a")
    return  rt