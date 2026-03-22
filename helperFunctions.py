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


Requisitos:
    N/A


"""

# Begin 001
def getFieldTypeDescription(eFieldTypeStr_: str) -> str:
    """
    Convierte el código de tipo de campo (eFieldTypeStr_) a una descripción legible.

    :param eFieldTypeStr_: Código de tipo de campo (string)
    :return: Descripción legible del tipo de campo
    """

    match eFieldTypeStr_:
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

    return f"Unknown ({eFieldTypeStr_})"

def getRecordTypeDescription(eRecTypeStr_: str) -> str:

    """
    Convierte el código de tipo de registro (eRecTypeStr_) a una descripción legible.
    :param eRecTypeStr_: Código de tipo de registro (string)
    :return: Descripción legible del tipo de registro
    """

    match eRecTypeStr_:
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
    
    return f"Unknown ({eRecTypeStr_})" 


# End 001