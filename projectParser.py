# ============================================================================
# Project:          pyPSPrintProject
# Description:      Print Project de proyecto de proyecto exportado a XML
# File:             projectParser.py
# Author:           akanashiro@gmail.com
# License:          MIT - read LICENSE in repo
# Changelog:
# Date             Author       Ref.     Description
# 2026/03/22       AKF          #001     XML parser.
# ============================================================================

"""
projectParser.py
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

import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import Optional
import helperFunctions as helpers


@dataclass
class FieldDefinition:

    """
    FieldDefinition class:
    This class stores Basic Field definition.
    To-do: xlat values.
    """

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

    """
    RecordField class:
    This class stores Record Field definition.
    """

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

    """
    RecordDefinition class:
    This class stores Record definition.
    getRecordInfo: prints Record definition to console. For debug purposes.
    """

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
    component: str
    market: str
    record_name: str
    field_name: str
    event_type: str           # FieldDefault, FieldFormula, RowInit, RowInsert, RowDelete,
                              # SavePreChange, SavePostChange, FieldEdit, FieldChange,
                              # PrePopup, Activate, ItemSelected, etc.
    code_type: str           # Record, Component, Component Record, Component Record Field
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
class MsgCatalog:
    message_set: int
    message_number: int
    severity: str             # Message, Warning, Error
    message_text: str = ""
    explanation: Optional[str] = None


# ============================================================================
# Application Engine Classes
# ============================================================================

@dataclass
class aetRecord:
    name: str
    defRecord: str

@dataclass
class AppEngineSteps:
    section_name: str
    program_name: str
    # section_type: str         # Prepare, Process, etc.
    stepName: str
    #stepActions: list[dict] = field(default_factory=list)   # step → action (SQL, PeopleCode, CallSection, etc.)
    stepActions: str


@dataclass
class AppEngineSection:
    section_name: str
    program_name: str
    steps: list[AppEngineSteps] = field(default_factory=list)
    

@dataclass
class AppEngineProgram:
    name: str
    aeType: str      # Standard, Daemon, etc.
    disRestart: str
    aetRecords: list[aetRecord] = field(default_factory=list)
    sections: list[AppEngineSection] = field(default_factory=list)
    peoplecode: list[PeopleCodeEvent] = field(default_factory=list)
    description: Optional[str] = None    

# ============================================================================
# Process Classes
# ============================================================================
@dataclass
class ProcSecComp:
    component: str = ""

@dataclass
class ProcSecGroups:
    processGroup: str =""

@dataclass
class ProcessDefinition:
    name: str
    process_type: str         # SQR, COBOL, Application Engine, Crystal, etc.
    description: Optional[str] = None
    run_location: Optional[str] = None
    parameters: Optional[str] = None
    components: [ProcSecComp] = None
    procGroups: [ProcSecGroups] = None

    def getProcessInfo(self):
        print (f"  🗂️  Process: {self.name}\n  📄 Description: {self.description}\n  📄 Type: {self.process_type}\n  📄 Run Location: {self.run_location}")

# ============================================================================
# Job Classes
# ============================================================================
@dataclass
class JobProcessDefinition:
    jobSeqNbr: str
    procType: str
    procName: str

@dataclass
class JobDefinition:
    jobName: str
    jobDescr: str
    processCat: str
    processList: [JobProcessDefinition] = None

# ============================================================================
# Service Operation Classes
# ============================================================================
@dataclass
class uriTemplateDefinition:
    uriSeq: str
    uriTemplate: str

@dataclass
class serviceOperationDefinition:
    name: str
    restMethod: str
    description: str
    restBaseUrl: str
    comments: Optional[str] = None    
    uriTemplates: [uriTemplateDefinition] = None

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
    jobs: list[JobDefinition] = field(default_factory=list)
    peoplecode: list[PeopleCodeEvent] = field(default_factory=list)    
    ap_peoplecode: list[AppPackagePCode] = field(default_factory=list)   
    service_operations: list[serviceOperationDefinition] = field(default_factory=list)
    app_engines: list[AppEngineProgram] = field(default_factory=list)
    msg_catalog: list[MsgCatalog] = field(default_factory=list)
    """    
    components: list[ComponentDefinition] = field(default_factory=list)
    menus: list[MenuDefinition] = field(default_factory=list)

    app_packages: list[AppPackageDefinition] = field(default_factory=list)

    queries: list[QueryDefinition] = field(default_factory=list)
    style_sheets: list[StyleSheetDefinition] = field(default_factory=list)
    roles: list[RoleDefinition] = field(default_factory=list)
    file_layouts: list[FileLayoutDefinition] = field(default_factory=list)
    portals: list[PortalDefinition] = field(default_factory=list)
    others: list[GenericDefinition] = field(default_factory=list)
    """


    def _getRecFieldDefinition(self, recordNameStr_: str, row_) -> list[RecordField]:

        """
        Gets Record.Field definition from XML

        :param recordNameStr_: Record Name
        :param row_: where cursor is positioned
        :return: a list of RecordField object
        """

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


        """
        Gets Record from XML

        :param recordNameStr_: Record Name as an objectvalue
        :param rootNode_: where cursor is positioned
        :return: a list of RecordDefinition object
        """

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

                            szParmListStr = procRow.findtext("szParmList", default="").strip() # trace

                            # Browse Process Security
                            componentNode = procDefnNode.find(".//lpPnlGrpList/rowset[@name='PsdPnlGrp']")

                            componentDict = []
                            procGrpDict = []

                            if componentNode is not None:
                                for compRow in componentNode.findall("row"):
                                    szPnlGrpNameStr = compRow.findtext("szPnlGrpName", default="").strip() # Component
                                    componentObj = ProcSecComp(
                                        component = szPnlGrpNameStr
                                    )
                                    # print(f"{szPnlGrpNameStr}")
                                    componentDict.append(componentObj)

                            procGroupNode = procDefnNode.find(".//lpPrcsGrpList/rowset[@name='PsdPrcsGrp']")
                            if procGroupNode is not None:
                                for procGrouprow in procGroupNode.findall("row"):
                                    szPrcsGrpStr = procGrouprow.findtext("szPrcsGrp", default="").strip() # Process Groups
                                    procGrpObj = ProcSecGroups(
                                        processGroup = szPrcsGrpStr
                                    )
                                    # print(f"{szPrcsGrpStr}")
                                    procGrpDict.append(procGrpObj)                                    

                            procDefnObj = ProcessDefinition(
                                name = szPrcsNameStr,
                                process_type = szPrcsTypeStr,
                                description = szDescrStr,
                                run_location = szRunLocationStr,
                                parameters = szParmListStr,
                                components = componentDict,
                                procGroups = procGrpDict
                            )

                            return procDefnObj
        return None

    def _getJobDefinition(self, jobNameStr_: str, rootNode_) -> JobDefinition | None:
        for instance in rootNode_.iter("instance"):
            if instance.get("class") == "PSJ":
                jobDefnNode = instance.find(".//rowset[@name='PsjDefn']")
                
                if jobDefnNode is not None:
                    jobProcArray=[]
                    for jobRow in jobDefnNode.findall("row"):
                        szJobNameStr = jobRow.findtext("szJobName", default="").strip()
                        szPrcsTypeStr = jobRow.findtext("szPrcsType", default="").strip()
                                              
                        if jobNameStr_ == szJobNameStr and szPrcsTypeStr == "PSJob":
                            szDescrStr =  jobRow.findtext("szDescr", default="").strip()
                            szPrcsCategoryStr = jobRow.findtext("szPrcsCategory", default="").strip()
                            jobProcNode = jobDefnNode.find(".//lpItemList/rowset[@name='PsjItem']")
                            
                            if jobProcNode is not None:
                                for procRow in jobProcNode.findall("row"):
                                    nJobSeqStr = procRow.findtext("nJobSeq", default="").strip()
                                    szPrcsTypeStr = procRow.findtext("szPrcsType", default="").strip()
                                    szPrcsNameStr = procRow.findtext("szPrcsName", default="").strip()                                    

                                    jobProcObj = JobProcessDefinition(
                                        jobSeqNbr = nJobSeqStr,
                                        procType = szPrcsTypeStr,
                                        procName = szPrcsNameStr
                                    )
                                    jobProcArray.append(jobProcObj)
                            
                            jobDefnObj = JobDefinition(
                                jobName = jobNameStr_,
                                jobDescr = szDescrStr,
                                processCat = szPrcsCategoryStr,
                                processList = jobProcArray
                            )
                            return jobDefnObj
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

    def _getEventPeopleCode(self, objectValue0_: str, objectValue1_: str, objectValue2_: str, objectValue3_: str, objectValue4_:str, eventTypeStr_: str, rootNode_) -> PeopleCodeEvent | None:

        # Inicialización de variables
        recordNameStr = ""
        componentStr = ""
        marketStr = ""


        for instance in rootNode_.iter("instance"):
            if instance.get("class") == "PCM":
                pcNode = instance.find(".//rowset[@name='PcmProg']")
                if pcNode is not None:
                    for pcRow in pcNode.findall("row"):
                        match eventTypeStr_:
                            case "REC" | "CMP":
                                szObjectValue_0Str = pcRow.findtext("szObjectValue_0", default="").strip() # Record | Component
                                szObjectValue_1Str = pcRow.findtext("szObjectValue_1", default="").strip() # Field | Market
                                szObjectValue_2Str = pcRow.findtext("szObjectValue_2", default="").strip() # Event | Event
                                if szObjectValue_0Str == objectValue0_ and szObjectValue_1Str == objectValue1_ and szObjectValue_2Str == objectValue2_ :

                                    if eventTypeStr_ == "REC":
                                        peopleCodeTypeStr = "Record"
                                        recordNameStr = objectValue0_
                                    
                                    if eventTypeStr_ == "CMP":
                                        peopleCodeTypeStr = "Component"
                                        componentStr = objectValue0_
                                        marketStr = szObjectValue_1Str

                                    peopleCodeText = instance.find(".//peoplecode_text")    

                                    pcEventObj = PeopleCodeEvent(
                                            component = componentStr,
                                            market = marketStr,
                                            record_name = recordNameStr,                                            
                                            field_name = objectValue1_,
                                            event_type =  objectValue2_,          # FieldDefault, FieldFormula, RowInit, RowInsert, RowDelete,
                                                                    # SavePreChange, SavePostChange, FieldEdit, FieldChange,
                                                                    # PrePopup, Activate, ItemSelected, etc.
                                            code_type = peopleCodeTypeStr,                                                            
                                            source_code = peopleCodeText.text.strip()
                                    )
                                    return pcEventObj
                                    
                            case "CRF":
                                szObjectValue_0Str = pcRow.findtext("szObjectValue_0", default="").strip() # Component
                                szObjectValue_1Str = pcRow.findtext("szObjectValue_1", default="").strip() # Market
                                szObjectValue_2Str = pcRow.findtext("szObjectValue_2", default="").strip() # Record
                                szObjectValue_3Str = pcRow.findtext("szObjectValue_3", default="").strip() # Field
                                szObjectValue_4Str = pcRow.findtext("szObjectValue_4", default="").strip() # Event

                                peopleCodeTypeStr = "Component Record Field"

                                if szObjectValue_0Str == objectValue0_ and szObjectValue_1Str == objectValue1_ and szObjectValue_2Str == objectValue2_ and szObjectValue_3Str == objectValue3_  and  szObjectValue_4Str == objectValue4_ :

                                    peopleCodeText = instance.find(".//peoplecode_text")    
                                    print(f"{szObjectValue_0Str}.{szObjectValue_1Str}.{szObjectValue_2Str}.{szObjectValue_3Str}.{szObjectValue_4Str}")
                                    pcEventObj = PeopleCodeEvent(
                                        component = szObjectValue_0Str,
                                        market = szObjectValue_1Str,                                        
                                        record_name = szObjectValue_2Str,
                                        field_name = szObjectValue_3Str,
                                        event_type =  szObjectValue_4Str,          # FieldDefault, FieldFormula, RowInit, RowInsert, RowDelete,
                                                                    # SavePreChange, SavePostChange, FieldEdit, FieldChange,
                                                                    # PrePopup, Activate, ItemSelected, etc.
                                        code_type = peopleCodeTypeStr,                                                            
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

    def _getServiceOpDef(self, serviceOpDefStr_: str, rootNode_) -> serviceOperationDefinition | None:
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "OPRM":         
                soNode = instance.find(".//rowset[@name='Operation']")

                if soNode is not None:
                    uriTemplateArray = []
                    for servOpRow in soNode.findall("row"):
                        szOperationnameStr = servOpRow.findtext("szOperationname", default="").strip()
                                                    
                        if szOperationnameStr == serviceOpDefStr_:
                            versionStr = servOpRow.findtext("szDefaultversion", default="").strip()
                            restMethodStr = servOpRow.findtext("szRestmethod", default="").strip()
                            szDescrStr = servOpRow.findtext("szDescr", default="").strip() 
                            operDescrStr =  servOpRow.findtext("lpszDescrlong", default="").strip()
                            restBaseUrlStr = servOpRow.findtext("szRestBaseurl", default="").strip()

                            uriTemplateNode = soNode.find(".//rowset[@name='Operationuritemplate']")

                            if uriTemplateNode is not None:                               
                                for uriTemplRow in uriTemplateNode.findall("row"):
                                    uriSeqStr = uriTemplRow.findtext("nURISeq", default="").strip()
                                    uriTemplateStr = uriTemplRow.find("lpszURITemplate/rowset/row/lpszURITemplate").text
                                    uriTemplateObj = uriTemplateDefinition(
                                        uriSeq  = uriSeqStr,
                                        uriTemplate = uriTemplateStr
                                    )
                                    uriTemplateArray.append(uriTemplateObj)
                                    # print(f"{uriTemplateStr}")

                        serviceOperObj = serviceOperationDefinition(
                            name = serviceOpDefStr_,
                            restMethod = restMethodStr,
                            description = szDescrStr,
                            comments = operDescrStr,
                            restBaseUrl = restBaseUrlStr,
                            uriTemplates = uriTemplateArray
                        )
                        
                        return serviceOperObj
        return None


    def _getAppEngine(self, appEngineStr_: str, rootNode_) -> AppEngineProgram | None:

        # Default values
        aeSectionDict = []
        returnObjectBool = False
        aeTypeStr = ""
        disableRestartStr = ""
        aeDescrStr = ""
        aetDict = []
        for instance in rootNode_.iter("instance"):
            
            if instance.get("class") == "AEM":
                aeDefNode = instance.find(".//rowset[@name='AemDefn']")
                
                if aeDefNode is not None:
                    for aeDefRow in aeDefNode.findall("row"):
                        aeNameStr = aeDefRow.findtext("szApplId", default="").strip()
                        if aeNameStr == appEngineStr_:
                            aeDescrStr = aeDefRow.findtext("szDescr", default="").strip()
                            
                            if aeDefRow.findtext("cApplLibrary", default="").strip() == "N":
                                aeTypeStr = "App Engine"
                            else:
                                aeTypeStr = "App Library"

                            disableRestartStr = aeDefRow.findtext("cDisableRestart", default="").strip() # Y/N

                            
                            aetNode = aeDefNode.find(".//lpStateT/rowset[@name='AeState']")

                            if aetNode is not None:
                                for aetRow in aetNode.findall("row"):
                                    aetRecStr = aetRow.findtext("szStateRecName", default="").strip()
                                    aetDefStr = aetRow.findtext("cDefaultState", default="").strip()

                                    aetObj=aetRecord(
                                        name = aetRecStr,                    
                                        defRecord = aetDefStr
                                    )
                                aetDict.append(aetObj)

                            # Faltan obtener los Temporary Tables                            

                returnObjectBool = True
            
        for instance in rootNode_.iter("instance"):
            if instance.get("class") == "AES":         
                aeNode = instance.find(".//rowset[@name='AesDefn']")
                
                if aeNode is not None:
                    
                    for aeRow in aeNode.findall("row"):
                        szApplIdStr = aeRow.findtext("szApplId", default="").strip()
                                                    
                        if szApplIdStr == appEngineStr_:

                            sectionNameStr =  aeRow.findtext("szSection", default="").strip() # MAIN

                            aeSectionNode = aeNode.find(".//lpSectT/rowset[@name='AeSect']")
                            if aeSectionNode is not None:
                                aeSectionsDict = []
                                for sectionRow in aeSectionNode.findall("row"):
                                    aeStepNode = aeSectionNode.find(".//lpStepT/rowset[@name='AeStep']")
                                    
                                    if aeStepNode is not None:
                                        aeStepsDict = []
                                        
                                        for aeStepRow in aeStepNode.findall("row"):
                                            stepsDict = []
                                            stepsStr = ""
                                            aeStepNameStr = aeStepRow.findtext("szStep", default="").strip()

                                            # Do Actions Step (Do While, Do When, Do Select, Do Until).
                                            if aeStepRow.find("lpAeStmtWhen/rowset[@name='AeStmtWhen']") is not None:
                                                stepsDict.append( "Do When")
                                                if len(stepsStr) > 0:
                                                    stepsStr = stepsStr + " - Do When"
                                                else:
                                                    stepsStr = "Do When"

                                            if aeStepRow.find("lpAeStmtSelect/rowset[@name='AeStmtWhen']") is not None:
                                                stepsDict.append("Do Select")
                                                if len(stepsStr) > 0:
                                                    stepsStr = stepsStr + " - Do Select"
                                                else:
                                                    stepsStr = "Do Select"

                                            # PeopleCode Step
                                            if aeStepRow.find("lpAePcode/rowset[@name='AePcode']") is not None:
                                                stepsDict.append( "PeopleCode")
                                                if len(stepsStr) > 0:
                                                    stepsStr = stepsStr + " - PeopleCode"
                                                else:
                                                    stepsStr = "PeopleCode"

                                            # SQL
                                            if aeStepRow.find("lpAeStmtSql/rowset[@name='AeStmtWhen']") is not None:
                                                stepsDict.append("SQL")
                                                if len(stepsStr) > 0:
                                                    stepsStr = stepsStr + " - SQL"
                                                else:
                                                    stepsStr = "SQL"

                                            # Call Section
                                            if aeStepRow.find("lpAeDoSect/rowset[@name='AeDoSect']") is not None:
                                                callAppStr = aeStepRow.find("lpAeDoSect/rowset[@name='AeDoSect']/row/szDoApplId").text
                                                callAppSectStr = aeStepRow.find("lpAeDoSect/rowset[@name='AeDoSect']/row/szDoSection").text
                                                stepsDict.append(f"Call Section {callAppStr}.{callAppSectStr}")
                                                if len(stepsStr) > 0:
                                                    stepsStr = stepsStr + " - Call Section " + callAppStr + "." + callAppSectStr
                                                else:
                                                    stepsStr = "Call Section " + callAppStr + "." + callAppSectStr
                               
                                            aStepsObj = AppEngineSteps(
                                                section_name = sectionNameStr,
                                                program_name = appEngineStr_,
                                                stepName = aeStepNameStr,
                                                stepActions = stepsStr #stepsDict
                                            )

                                            aeStepsDict.append(aStepsObj)

                                    aeSectionObj = AppEngineSection(
                                        section_name = sectionNameStr,
                                        program_name = appEngineStr_,
                                        steps = aeStepsDict
                                    )
                                    aeSectionDict.append(aeSectionObj)
        if returnObjectBool == True:
            
            aeObj = AppEngineProgram(
                name = appEngineStr_,
                aeType = aeTypeStr,
                aetRecords = aetDict,
                sections =  aeSectionDict,
                disRestart = disableRestartStr,
                description = aeDescrStr,
                # peoplecode: list[PeopleCodeEvent] = field(default_factory=list)
            )
            return aeObj
        else:
            return None


    def _getMsgCatalog(self, msgSetStr_: str, msgNumberstr_: str, rootNode_) -> MsgCatalog | None:
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "MSG":         
                msgCatNode = instance.find(".//rowset[@name='MsgSet']")

                if msgCatNode is not None:
                    for msgCatRow in msgCatNode.findall("row"):
                        msgSetStr = msgCatRow.findtext("lMsgSet", default="").strip()

                        msgNumberNode =  msgCatRow.find(".//hMvt/rowset[@name='MsgNum']")
                        
                        if msgNumberNode is not None:
                            
                            # severityCodeStr=""
                            for msgNumberRow in msgNumberNode.findall("row"):
                                msgNumberStr = msgNumberRow.findtext("lMsgNum", default="").strip()
                                print (f"mensaje {msgNumberStr} = {msgNumberstr_}")
                                if msgNumberStr == msgNumberstr_:
                                    
                                    match msgNumberRow.findtext("cMsgSeverity", default="").strip():
                                        case "M":
                                            severityCodeStr = "Message"
                                        case "E":
                                            severityCodeStr = "Error"
                                        case _:
                                            severityCodeStr = "Unknown"

                                    pszMsgText = msgNumberRow.find(".//pszMsgText/rowset/row/pszMsgText").text

                                    msgCatObj = MsgCatalog(
                                        message_set = msgSetStr_,
                                        message_number = msgNumberstr_,
                                        severity = severityCodeStr,
                                        message_text = pszMsgText
                                    )
                                    
                                    return msgCatObj
        return None


    def _describeItems(self, objectTypeNode_, objectValue0_, objectValue1_, objectValue2_, objectValue3_, objectValue4_, rootNode_):

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
                resultObj = self._getEventPeopleCode(objectValue0_, objectValue1_, objectValue2_, objectValue3_, objectValue4_, "REC", rootNode_)
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
                resultObj = self._getJobDefinition(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.jobs.append(resultObj)                
                #print(f"📄 Job Definition: {objectValue0_}")                
            case "25":
                # Message Catalog
                resultObj = self._getMsgCatalog(objectValue0_, objectValue1_, rootNode_)
                if resultObj is not None:
                    self.msg_catalog.append(resultObj)                 
                #print(f"📄 Message Catalog:: {objectValue0_}.{objectValue1_}")
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
                # Application Engine
                resultObj = self._getAppEngine(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.app_engines.append(resultObj)            
                # print(f"📄 Application Engine Program: {objectValue0_}")                
            case "34":
                print(f"📄 Application Engine Section: {objectValue0_}")
            case "43":
                print(f"📄 Application Engine Step: {objectValue0_}")                   
            case "40":
                print(f"📄 Service Operation: {objectValue0_}")
            case "46":
                # Definición de Component PeopleCode
                resultObj = self._getEventPeopleCode(objectValue0_, objectValue1_, objectValue2_, objectValue3_, objectValue4_, "CMP", rootNode_)
                if resultObj is not None:
                    self.peoplecode.append(resultObj)
            case "48":
                # Definición de Component Record Field PeopleCode
                objectValue3Str_, objectValue4Str_ = objectValue3_.split()
                resultObj = self._getEventPeopleCode(objectValue0_, objectValue1_, objectValue2_, objectValue3Str_, objectValue4Str_, "CRF", rootNode_)
                if resultObj is not None:
                    self.peoplecode.append(resultObj)            
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
            case "80":
                # Definición de Service Operation
                resultObj = self._getServiceOpDef(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.service_operations.append(resultObj)            
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
                            objectValue4 = row.findtext("szObjectValue_3", default="").strip()                            

                            # Debug print(f"Procesando item: ObjectType={objectTypeNode}, ObjectValue0={objectValue0}, ObjectValue1={objectValue1}, ObjectValue2={objectValue2}, ObjectValue3={objectValue3}")

                            projectObj._describeItems(objectTypeNode, objectValue0, objectValue1, objectValue2, objectValue3, objectValue4, root)

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