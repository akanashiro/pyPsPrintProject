# ============================================================================
# Project:          pyPSPrintProject
# Description:      Print Project de proyecto de proyecto exportado a XML
# File:             helperFunctions.py
# Author:           akanashiro@gmail.com
# License:          MIT - read LICENSE in repo
# Changelog:
# Date             Author       Ref.     Description
# 2026/03/22       AKF          #001     Additional functions needed
# ============================================================================
"""
helperFunctions.py
-------------------
Funciones auxiliares para el proyecto pyPSPrintProject, incluyendo:
- getFieldTypeDescription: Convierte el código de tipo de campo a una descripción legible
- getRecordTypeDescription: Convierte el código de tipo de registro a una descripción legible
- getPageTypeDescription: Convierte el código de tipo de página a una descripción legible
- decodeFieldFlags: Decodifica los bit del campo fUseEdit del XML para saber qué tipo de campo es

Requisitos:
    N/A

"""

# Begin 001
def getFieldTypeDescription(fieldTypeStr_: str) -> str:
    """
    Convierte el código de tipo de campo (fieldTypeStr_) a una descripción legible.

    :param fieldTypeStr_: Código de tipo de campo (string)
    :return: Descripción legible del tipo de campo
    """

    match fieldTypeStr_:
        case "0":
            return "Character"
        case "1":
            return "Long Character"
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

def getRecordTypeDescription(recTypeStr_: str) -> str:

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

def getPageTypeDescription(pageTypeStr_: str) -> str:
    """
    Convierte el código de tipo de página (pageTypeStr_) a una descripción legible.
    :param pageTypeStr_: Código de tipo de página (string)
    :return: Descripción legible del tipo de página
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
    Decodifica los bit del campo fUseEdit del XML para saber qué tipo de campo es.

    Args:
        useEditValueNbr_: valor numérico de la columna USEEDIT

    Returns:
        dict con:
          - 'value':       el valor original
          - 'bits':        lista de bit values que componen el valor
          - 'flags':       lista de descripciones de cada flag activo
          - 'description': string legible con todos los flags unidos por ' + '
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

    active_bits  = []
    active_flags = []

    # Recorre cada bit de mayor a menor para descomponer el valor
    for bit_value in sorted(USEEDIT_FLAGS.keys(), reverse=True):
        if valueNbr >= bit_value:
            valueNbr -= bit_value
            active_bits.append(bit_value)
            active_flags.append(USEEDIT_FLAGS[bit_value])

    # Si sobra algo, hay bits no mapeados
    if valueNbr > 0:
        active_bits.append(valueNbr)
        active_flags.append(f"Unknown (valor residual: {valueNbr})")

    # Ordenar de menor a mayor para presentación
    combined = sorted(zip(active_bits, active_flags), key=lambda x: x[0])
    active_bits  = [b for b, _ in combined]
    active_flags = [f for _, f in combined]

    return {
        "value":       useEditValueNbr_,
        "bits":        active_bits,
        "flags":       active_flags,
        "description": " + ".join(active_flags) if active_flags else "Sin flags activos",
    }

# End 001