# ============================================================================
# Proyecto:        pyPSPrintProject
# Descripción:     Print Project de proyecto de proyecto exportado a XML
# Nombre Archivo:  projectParser.py
# Autor:           akanashiro@gmail.com
# Historial de Modificaciones:
# Fecha            Autor        Ref.     Descripción
# 2026/03/22       AKF          #001     Parseador de XML.
# ============================================================================

# Begin 001

import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import Optional
import helperFunctions as helpers


@dataclass
class FieldDefinition:
    name: str
    field_type: str
    length: Optional[int] = None
    decimals: Optional[int] = None
    long_name: Optional[str] = None
    short_name: Optional[str] = None
    #translate_values: list[TranslateValue] = field(default_factory=list)
    description: Optional[str] = None

    def getFieldInfo(self):
        print (f"  🗂️  Field: {self.name}\n  📄 Description: {self.description}\n  📄 Field Type: {self.field_type}\n  📄 Length: {self.length}\n  📄 Decimals: {self.decimals}")

@dataclass
class RecordField:
    name: str
    field_type: str          # CHAR, LONG CHAR, NUMBER, DATE, TIME, DATETIME, IMAGE, etc.
    length: Optional[int] = 0
    decimals: Optional[int] = 0
    is_key: bool = False
    is_duplicate_key: bool = False
    is_alternate_key: bool = False
    is_search_key: bool = False
    is_list_box: bool = False
    is_from_search: bool = False
    is_required: bool = False
    is_audit: bool = False
    is_regular: bool = False
    default_value: Optional[str] = None
    label: Optional[str] = None
   # translate_values: list[TranslateValue] = field(default_factory=list)
   

@dataclass
class RecordDefinition:
    name: str
    record_type: str          # TABLE, VIEW, DERIVED/WORK, SUBRECORD, DYNAMIC VIEW, QUERY VIEW
    fields: list[RecordField] = field(default_factory=list)
    sql_view_text: Optional[str] = None
    description: Optional[str] = None
    parent_record: Optional[str] = None

    def getRecordInfo(self):
        print (f"  🗂️  Record: {self.name}\n  📄 Description: {self.description}\n  📄 Type: {self.record_type}")
        print (f"  🗂️  Fields: {len(self.fields)}")
        conta = 1
        for recField in self.fields:
            print(f"       Field {conta}. {recField.name} | Type: {helpers.getFieldTypeDescription(recField.field_type)} | Length: {recField.length} | Decimals: {recField.decimals} | Is Key: {recField.is_key}")
            conta += 1

@dataclass
class SQLDefinition:
    name: str
    sql_type: str             # SQL Object, View, etc.
    sql_text: str = ""
    description: Optional[str] = None
    
    def getSQLInfo(self):
        if self.sql_type == "SQL Object":
            print (f"  🗂️  SQL Object: {self.name}\n  📄 Description: {self.description}\n  📄 Type: {self.sql_type}\n  📄 SQL Text: {self.sql_text}")


@dataclass
class PageControl:
    control_type: str         # EditBox, DropDown, CheckBox, RadioButton, Grid, SubPage, etc.
    record_name: Optional[str] = None
    field_name: Optional[str] = None
    label: Optional[str] = None
    occurrence: Optional[int] = None

@dataclass
class PeopleCodeEvent:
    record_name: str
    field_name: str
    event_type: str           # FieldDefault, FieldFormula, RowInit, RowInsert, RowDelete,
                              # SavePreChange, SavePostChange, FieldEdit, FieldChange,
                              # PrePopup, Activate, ItemSelected, etc.
    source_code: str = ""
    # functions: list[str] = field(default_factory=list)


@dataclass
class PageDefinition:
    name: str
    page_type: str            # Standard, Secondary, Popup, etc.
    #controls: list[PageControl] = field(default_factory=list)
    description: Optional[str] = None

@dataclass
class AppPackagePCode:
    app_package: str = ""
    code_type: str  ="Application Package PeopleCode"  
    event: str =""          
    source_code: str = ""
    #functions: list[str] = field(default_factory=list)

    def getPeopleCodeInfo(self):
       print (f"  🗂️  📄 Code Type: {self.code_type}\n PeopleCode Event: {self.app_package} {self.event}\n    📄 Source Code: {self.source_code}")


@dataclass
class ProcessDefinition:
    name: str
    process_type: str         # SQR, COBOL, Application Engine, Crystal, etc.
    description: Optional[str] = None
    run_location: Optional[str] = None

    def getProcessInfo(self):
        print (f"  🗂️  Process: {self.name}\n  📄 Description: {self.description}\n  📄 Type: {self.process_type}\n  📄 Run Location: {self.run_location}")


@dataclass
class PSProject:

    """
    Clase que contiene toda la información del proyecto parseada desde el XML exportado por PeopleSoft Application Designer.
    """

    project_name: str
    description: Optional[str] = None
    
    # Definiciones por tipo
    records: list[RecordDefinition] = field(default_factory=list)    
    fields: list[FieldDefinition] = field(default_factory=list)
    sql_objects: list[SQLDefinition] = field(default_factory=list)
    pages: list[PageDefinition] = field(default_factory=list)    
    processes: list[ProcessDefinition] = field(default_factory=list)
    peoplecode: list[PeopleCodeEvent] = field(default_factory=list)    
    ap_peoplecode: list[AppPackagePCode] = field(default_factory=list)    
    """    
    components: list[ComponentDefinition] = field(default_factory=list)
    menus: list[MenuDefinition] = field(default_factory=list)
    app_engines: list[AppEngineProgram] = field(default_factory=list)
    app_packages: list[AppPackageDefinition] = field(default_factory=list)
    messages: list[MessageDefinition] = field(default_factory=list)
    service_operations: list[ServiceOperation] = field(default_factory=list)
    queries: list[QueryDefinition] = field(default_factory=list)
    style_sheets: list[StyleSheetDefinition] = field(default_factory=list)
    roles: list[RoleDefinition] = field(default_factory=list)
    file_layouts: list[FileLayoutDefinition] = field(default_factory=list)
    portals: list[PortalDefinition] = field(default_factory=list)
    others: list[GenericDefinition] = field(default_factory=list)
    """


    def _getRecFieldDefinition(self, recordNameStr_: str, row_) -> list[RecordField]:
        recFieldNode = row_.find(".//rowset[@name='RecField']")
        
        fieldObjs = []
        if recFieldNode is not None:
            for fieldRow in recFieldNode.findall("row"):
                # Process each field row
                atmFieldNameStr = fieldRow.findtext("atmFieldName", default="").strip()
                eFieldTypeStr = fieldRow.findtext("eFieldType", default="").strip()
                nLengthStr = fieldRow.findtext("nLength", default="").strip()
                nDecimalPosStr = fieldRow.findtext("nDecimalPos", default="").strip()
                fUseEditNbr = int(fieldRow.findtext("fUseEdit", default="0").strip())
                decodeResultArray = helpers.decodeFieldFlags(fUseEditNbr)

                # Output esperado:
                # Valor:       8390657
                # Bits:        [1, 2048, 8388608]
                # Descripción: Key Value + Search key + Regular field (sub-record)

                isKeyBool = False
                isDuplicateBool = False
                isAuditBool = False
                isAlternateBool = False
                isLitBoxBool = False
                isReqBool = False
                isSearchKeyBool = False
                isFromSrchBool = False

                if 0 in decodeResultArray['bits']:
                    isKeyBool = True

                if 2 in decodeResultArray['bits']:
                    isDuplicateBool = True

                if 8 in decodeResultArray['bits']:
                    isAuditBool = True
                
                if 16 in decodeResultArray['bits']:
                    isAlternateBool = True

                if 3 in decodeResultArray['bits']:
                    isLitBoxBool = True

                if 256 in decodeResultArray['bits']:
                    isReqBool = True

                if 2048 in decodeResultArray['bits']:
                    isSearchKeyBool = True

                if 262144 in decodeResultArray['bits']:
                    isFromSrchBool = True


                recordFieldObj = RecordField(
                    name = atmFieldNameStr,
                    field_type = eFieldTypeStr,
                    length = int(nLengthStr),
                    decimals = int(nDecimalPosStr),
                    is_key = isKeyBool,
                    is_duplicate_key = isDuplicateBool,
                    is_alternate_key = isAlternateBool,
                    is_search_key = isSearchKeyBool,
                    is_list_box = isLitBoxBool,
                    is_required = isReqBool,
                    is_from_search = isFromSrchBool,
                    is_audit = isAuditBool,
                ) 
                            

                fieldObjs.append(recordFieldObj)

            return fieldObjs

    def _getRecordDefinition(self, recordNameStr_: str, rootNode_) -> RecordDefinition | None:

        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "RDM":         
                recDefnNode = instance.find(".//rowset[@name='RecDefn']")

                if recDefnNode is not None:
                    for row in recDefnNode.findall("row"):
                        szRecNameStr = row.findtext("szRecName", default="").strip()
                                                    
                        if szRecNameStr == recordNameStr_:
                            eRecTypeStr = row.findtext("eRecType", default="").strip()

                            recTypeDescrStr = helpers.getRecordTypeDescription(eRecTypeStr)

                            szRecDescrStr = row.findtext("szRecDescr", default="").strip() 
                            szParentRecNameStr = row.findtext("szParentRecName", default="").strip() 

                            # Debo obtener los campos asociados a este record
                            recordFields = []
                            for field in self._getRecFieldDefinition(recordNameStr_, row):
                                recordFields.append(field)

                            recordObj = RecordDefinition(
                                name=recordNameStr_,
                                record_type=recTypeDescrStr,
                                fields=recordFields,
                                description=szRecDescrStr,
                                parent_record=szParentRecNameStr
                            )
                            return recordObj
        return None

    def _getFieldDefinition(self, fieldNameStr_: str, rootNode_) -> FieldDefinition | None:

        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "FIELD":         
                fieldNode = instance.find(".//rowset[@name='Field']")

                if fieldNode is not None:
                    for row in fieldNode.findall("row"):
                        szFieldNameStr = row.findtext("szFieldName", default="").strip()
                                                    
                        if szFieldNameStr == fieldNameStr_:
                            eFieldTypeStr = row.findtext("eFieldType", default="").strip()
                            fieldTypeDescrStr = helpers.getFieldTypeDescription(eFieldTypeStr)
                            atmShortNameStr = row.findtext("atmShortName", default="").strip() 
                            atmLongNameStr = row.findtext("atmLongName", default="").strip() 
                            nLengthStr = row.findtext("nLength", default="").strip()
                            nDecimalPosStr = row.findtext("nDecimalPos", default="").strip()

                            fieldObj = FieldDefinition(
                                name=fieldNameStr_,
                                field_type=fieldTypeDescrStr,
                                length=nLengthStr,
                                decimals=nDecimalPosStr,
                                long_name=atmLongNameStr,
                                short_name=atmShortNameStr,
                                description=atmShortNameStr,
                            )

                            return fieldObj
        return None

    def _getProcessDefinition(self, processTypeStr_: str, processNameStr_: str, rootNode_) -> ProcessDefinition | None:

        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "PSD":         
                procDefnNode = instance.find(".//rowset[@name='PsdDefn']")

                if procDefnNode is not None:
                    for procRow in procDefnNode.findall("row"):
                        szPrcsNameStr = procRow.findtext("szPrcsName", default="").strip()
                        szPrcsTypeStr = procRow.findtext("szPrcsType", default="").strip()
                        if szPrcsNameStr == processNameStr_ and szPrcsTypeStr == processTypeStr_:                            
                            szDescrStr = procRow.findtext("szDescr", default="").strip()
                            szRunLocationStr = procRow.findtext("szRunLocation", default="").strip()

                            procDefnObj = ProcessDefinition(
                                name=szPrcsNameStr,
                                process_type=szPrcsTypeStr,
                                description=szDescrStr,
                                run_location=szRunLocationStr
                            )

                            return procDefnObj
        return None

    def _getSQLDefinition(self, sqlNameStr_: str, objectValue1_: str, rootNode_) -> SQLDefinition | None:
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "SRM":         
                sqlNode = instance.find(".//rowset[@name='SrmDefn']")

                if sqlNode is not None:
                    for sqlRow in sqlNode.findall("row"):
                        szSqlIdStr = sqlRow.findtext("szSqlId", default="").strip()
                        szSqlTypeStr = sqlRow.findtext("szSqlType", default="").strip()  
                        
                        # Degub print(f"Debug SQL: szSqlId={szSqlIdStr}, szSqlType={szSqlTypeStr}, objectValue1={objectValue1_}")

                        if szSqlIdStr == sqlNameStr_ and szSqlTypeStr == objectValue1_ and objectValue1_ == "0":

                            szDescrStr = sqlRow.find(
                                "lpStmtT"
                                "/rowset[@name='SrmStmt']/row"
                                "/szDescr"
                            ).text

                            # Debug print (f"Debug SQL: szDescr={szDescrStr}")


                            szSQLTextStr = sqlRow.find(
                                "lpStmtT"
                                "/rowset[@name='SrmStmt']/row"
                                "/lpszSqlText"
                                "/rowset[@name='char']/row"
                                "/lpszSqlText"
                            ).text

                            # debug print (f"Debug SQL: szSQLText={szSQLTextStr}")

                            sqlDefnObj = SQLDefinition(
                                name=szSqlIdStr,
                                sql_type="SQL Object",
                                description=szDescrStr,
                                sql_text=szSQLTextStr
                            )

                            return sqlDefnObj
        return None

    def _getRecordPeopleCode(self, objectValue0_: str, objectValue1_: str, objectValue2_: str, rootNode_) -> PeopleCodeEvent | None:
        for instance in rootNode_.iter("instance"):
            if instance.get("class") == "PCM":
                pcNode = instance.find(".//rowset[@name='PcmProg']")
                if pcNode is not None:
                    for pcRow in pcNode.findall("row"):
                        szObjectValue_0Str = pcRow.findtext("szObjectValue_0", default="").strip() # Record
                        szObjectValue_1Str = pcRow.findtext("szObjectValue_1", default="").strip() # Field
                        szObjectValue_2Str = pcRow.findtext("szObjectValue_2", default="").strip() # Event
                        

                        if szObjectValue_0Str == objectValue0_ and szObjectValue_1Str == objectValue1_ and szObjectValue_2Str == objectValue2_ :

                            peopleCodeText = instance.find(".//peoplecode_text")    

                            pcEventObj = PeopleCodeEvent(
                                    record_name = objectValue0_,
                                    field_name = objectValue1_,
                                    event_type =  objectValue2_,          # FieldDefault, FieldFormula, RowInit, RowInsert, RowDelete,
                                                              # SavePreChange, SavePostChange, FieldEdit, FieldChange,
                                                              # PrePopup, Activate, ItemSelected, etc.
                                    source_code = peopleCodeText.text.strip()
                            )
                            
                            return pcEventObj
        return None

    def _getAppPackagePeopleCode(self, packageNameStr_: str, objectValue1_: str, objectValue2_: str, objectValue3_: str, rootNode_) -> AppPackagePCode | None:
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "PCM":         
                pcNode = instance.find(".//rowset[@name='PcmProg']")

                if pcNode is not None:
                    for pcRow in pcNode.findall("row"):
                        szObjectValue_0Str = pcRow.findtext("szObjectValue_0", default="").strip()
                        szObjectValue_1Str = pcRow.findtext("szObjectValue_1", default="").strip()
                        szObjectValue_2Str = pcRow.findtext("szObjectValue_2", default="").strip()
                        szObjectValue_3Str = pcRow.findtext("szObjectValue_3", default="").strip()

                        if szObjectValue_0Str == packageNameStr_ and szObjectValue_1Str == objectValue1_ and szObjectValue_2Str == objectValue2_ and szObjectValue_3Str == objectValue3_:

                            peopleCodeText = instance.find(".//peoplecode_text")       

                            eventTypeStr = f"{packageNameStr_}:{objectValue1_}"
                            if objectValue2_ != " ":
                                eventTypeStr=f"{packageNameStr_}:{objectValue1_}:{objectValue2_}"
                                if objectValue3_ != " ":
                                    eventTypeStr=f"{packageNameStr_}:{objectValue1_}:{objectValue2_}:{objectValue3_}"

                            pcEventObj = AppPackagePCode(
                                app_package=packageNameStr_,
                                event=eventTypeStr,
                                code_type="Application Package PeopleCode",
                                source_code=peopleCodeText.text.strip()
                            )

                            return pcEventObj
        return None

    def _getPageDefinition(self, pageNameStr_: str, rootNode_) -> PageDefinition | None:
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "PDM":         
                pageNode = instance.find(".//rowset[@name='PdmDefn']")

                if pageNode is not None:
                    for pageRow in pageNode.findall("row"):
                        szPnlNameStr = pageRow.findtext("szPnlName", default="").strip()
                                                    
                        if szPnlNameStr == pageNameStr_:
                            ePnlTypeStr = pageRow.findtext("ePnlType", default="").strip()
                            pageTypeDescrStr = helpers.getPageTypeDescription(ePnlTypeStr)
                            szDescrStr = pageRow.findtext("szDescr", default="").strip() 

                            pageObj = PageDefinition(
                                name=pageNameStr_,
                                page_type=pageTypeDescrStr,
                                description=szDescrStr
                            )

                            return pageObj
        return None

    def _describeItems(self, objectTypeNode_, objectValue0_, objectValue1_, objectValue2_, objectValue3_, rootNode_):

        """
        Parsea el archivo XML exportado desde PeopleSoft Application Designer
        y retorna una estructura de datos normalizada con todas las definiciones
        del proyecto (equivalente a PSPROJECTITEMS).

        Tipos soportados (OBJECTTYPE en PSPROJECTITEMS):
        0  - Record
        1  - Field
        2  - Index
        4  - Page
        5  - Component
        6  - Menu
        7  - Component Interface (CI)
        8  - File Layout
        9  - Application Engine Program
        10 - Application Engine Section
        14 - Message Catalog
        23 - SQL Object
        25 - Roles
        26 - Process Definition
        29 - Application Package
        30 - Application Class (PeopleCode)
        40 - Service Operation
        43 - IScript
        46 - Portal Registry Structure
        54 - Activity Guide
        58 - Analytic Model
        66 - Style Sheet
        104 - Query
        116 - Integration Broker
        """

        match objectTypeNode_:
            case "0":
                # Definición de Record. Se debe obtener toda la información del record, incluyendo sus campos asociados.
                resultObj = self._getRecordDefinition(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.records.append(resultObj)                
            case "2":
                # Definición de Field.
                resultObj = self._getFieldDefinition(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.fields.append(resultObj)
            #case "4":
            #    print(f"📄 Page: {objectValue_}")
            case "5":
                # Definición de Página   
                resultObj = self._getPageDefinition(objectValue0_, rootNode_)       
                if resultObj is not None:
                    self.pages.append(resultObj)
            case "6":
                # Definición de Menú
                print(f"🔸 Menu: {objectValue0_}")
            case "7":
                # Definición de Componente
                print(f"🔹 Component: {objectValue0_}")
            case "8":
                # Definición de Record PeopleCode
                resultObj = self._getRecordPeopleCode(objectValue0_, objectValue1_, objectValue2_, rootNode_)
                if resultObj is not None:
                    self.peoplecode.append(resultObj)
            case "14":
                print(f"📄 Message Catalog: {objectValue0_}" )                
            case "20":
                # Definición de Proceso
                resultObj = self._getProcessDefinition(objectValue0_, objectValue1_, rootNode_)
                if resultObj is not None:
                    self.processes.append(resultObj)
            case "23":
                # Definición de Job
                print(f"📄 Job Definition: {objectValue0_}")                
            case "25":
                # Definición de Catálogo de Mensajes
                print(f"📄 Message Catalog:: {objectValue0_}")
            case "26":
                print(f"📄 Process Definition: {objectValue0_}") 
            case "29":
                print(f"📄 Application Package: {objectValue0_}")
            case "30":
                # Definición de Objeto SQL
                match objectValue1_:
                    case "0":
                        resultObj = self._getSQLDefinition(objectValue0_, objectValue1_, rootNode_)
                        if resultObj is not None:
                            self.sql_objects.append(resultObj)
                    case "1":
                        print(f"📄 Application Engine SQL: {objectValue0_}")
                    case _:
                        print(f"SQL no reconocido: {objectValue0_} con tipo {objectValue1_}")
            case "31":
                print(f"📄 File Layout: {objectValue0_}")                
            case "33":
                print(f"📄 Application Engine Program: {objectValue0_}")                
            case "34":
                print(f"📄 Application Engine Section: {objectValue0_}")
            case "43":
                print(f"📄 Application Engine Step: {objectValue0_}")                   
            case "40":
                print(f"📄 Service Operation: {objectValue0_}")
            case "46":
                print(f"📄 Portal Registry Structure: {objectValue0_}")
            case "54":
                print(f"📄 Activity Guide: {objectValue0_}")
            case "58":                
                if objectValue3_ =="":
                    #print(f"📄 Application Package PeopleCode: {objectValue0_}:{objectValue1_}:{objectValue2_}:{objectValue3_}")
                    print ("pendiente escribir código")
                elif objectValue3_ != "":
                    resultObj = self._getAppPackagePeopleCode(objectValue0_, objectValue1_, objectValue2_, objectValue3_, rootNode_)
                    if resultObj is not None:
                        self.ap_peoplecode.append(resultObj)
            case "66":
                print(f"📄 Style Sheet: {objectValue0_}")
            case "104":
                print(f"📄 Query: {objectValue0_}")
            case "116":
                print(f"📄 Integration Broker: {objectValue0_}")
        return None



def getProject(xml_path: str)  -> PSProject  | None:

    """
    Parsea el archivo XML exportado desde PeopleSoft Application Designer
    y retorna una estructura de datos normalizada con todas las definiciones
    """

    # PeopleSoft a veces exporta con encoding no estándar
    with open(xml_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    root = ET.fromstring(content)

    # .// busca en cualquier nivel del árbol, por si hay nodos wrapper
    for instance in root.iter("instance"):
        if instance.get("class") == "PJM":
            projectNameStr = instance.find(".//rowset[@name='PjmDefn']/row/szProjectName")
            if projectNameStr is not None and projectNameStr.text:

                projectObj = PSProject(project_name=projectNameStr.text.strip())

                projectDescrStr = instance.find(".//rowset[@name='PjmDefn']/row/szProjectDescr")
                projectObj.description = projectDescrStr.text.strip()

                if projectNameStr is None or not projectNameStr.text:
                    print("⚠️  No se encontró nombre del proyecto en el XML.")
                    return None

                for lpPit in instance.iter("lpPit"):
                    
                    if lpPit is None:
                        print("⚠️  No se encontró nodo lpPit en el XML.")
                        continue

                    pjmPitNode = lpPit.find(".//rowset[@name='PjmPit']")

                    if pjmPitNode is not None:
                        print(f"Total de rows: {pjmPitNode.get('count')}")
                        
                        for row in pjmPitNode.findall("row"):
                            objectTypeNode = row.findtext("eObjectType", default="").strip()
                            objectValue0 = row.findtext("szObjectValue_0", default="").strip()
                            objectValue1 = row.findtext("szObjectValue_1", default="").strip()
                            objectValue2 = row.findtext("szObjectValue_2", default="").strip()
                            objectValue3 = row.findtext("szObjectValue_3", default="").strip()

                            # Debug print(f"Procesando item: ObjectType={objectTypeNode}, ObjectValue0={objectValue0}, ObjectValue1={objectValue1}, ObjectValue2={objectValue2}, ObjectValue3={objectValue3}")

                            projectObj._describeItems(objectTypeNode, objectValue0, objectValue1, objectValue2, objectValue3, root)

                    return projectObj

            if projectNameStr is None or not projectNameStr.text:
                print("⚠️  No se encontró nombre del proyecto en el XML.")
                return None

    return None    

class PSProjectParser:
    """
    Clase para parsear el XML exportado desde Application Designer y extraer la información del proyecto.
    """

    def __init__(self, xml_path):
        self.xml_path = xml_path

    def parse(self) -> PSProject:
        project = getProject(self.xml_path)

        if project is None:
            raise ValueError("No se pudo extraer el nombre del proyecto desde el XML.")
        
        return project
# End 001