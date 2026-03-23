# ============================================================================
# Proyecto:        pyPSPrintProject
# Descripción:     Print Project de proyecto de proyecto exportado a XML
# Nombre Archivo:  helperFunctions.py
# Autor:           akanashiro@gmail.com
# Historial de Modificaciones:
# Fecha            Autor        Ref.     Descripción
# 2026/03/22       AKF          #001     Funciones de ayuda.
# ============================================================================

"""
helperFunctions.py
-------------------
Funciones auxiliares para el proyecto pyPSPrintProject, incluyendo:
- getFieldTypeDescription: Convierte el código de tipo de campo a una descripción legible
- getRecordTypeDescription: Convierte el código de tipo de registro a una descripción legible
- getPageTypeDescription: Convierte el código de tipo de página a una descripción legible

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

# End 001