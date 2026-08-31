# ============================================================================
# Project:          pyPSPrintProject
# Description:      Print Project de proyecto de proyecto exportado a XML
# File:             projectParser.py
# Author:           akanashiro at gmail dot com
# License:          MIT - read LICENSE in repo
# ============================================================================

"""
projectParser.py
-------------------

Requisites:
    N/A

"""
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import Optional
import helpFunctions as helpers


@dataclass
class SQLDefinition:

    """
    This class represents SQL object definition.  
    """

    name: str
    sql_type: str             # SQL Object, View, etc.
    sql_text: str = ""
    description: Optional[str] = None
    
    def getSQLInfo(self):
        if self.sql_type == "SQL Object":
            print (f"  🗂️  SQL Object: {self.name}\n  📄 Description: {self.description}\n  📄 Type: {self.sql_type}\n  📄 SQL Text: {self.sql_text}")

# ============================================================================
# Field Related Definitions
# ============================================================================

@dataclass
class TranslateValue:

    """
    This class represents xlats.
    """

    value: str
    long_name: str
    short_name: str
    effective_date: Optional[str] = None
    status: Optional[str] = None


@dataclass
class FieldDefinition:

    """
    This class represents Basic Field definition.
    getFieldInfo: prints Field definition to console. For debug purposes.
    """

    name: str
    field_type: str
    length: Optional[int] = None
    decimals: Optional[int] = None
    long_name: Optional[str] = None
    short_name: Optional[str] = None
    translate_values: list[TranslateValue] = None
    # description: Optional[str] = None

    def getFieldInfo(self):
        print (f"  🗂️  Field: {self.name}\n  📄 Description: {self.description}\n  📄 Field Type: {self.field_type}\n  📄 Length: {self.length}\n  📄 Decimals: {self.decimals}")

@dataclass
class RecordField:

    """
    This class represents Record Field definition.
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
   
# ============================================================================
# Record Definition
# ============================================================================

@dataclass
class RecordDefinition:

    """
    This class represents Record definition.
    getRecordInfo: prints Record definition to console. For debug purposes.
    """

    name: str
    record_type: str          # TABLE, VIEW, DERIVED/WORK, SUBRECORD, DYNAMIC VIEW, QUERY VIEW
    object_property: str
    field_count: int = 0
    fields: list[RecordField] = field(default_factory=list)
    sql_view_text: SQLDefinition = None
    description: Optional[str] = None
    parent_record: Optional[str] = None

# ============================================================================
# Component related Definitions
# ============================================================================

@dataclass
class ComponentRecord:
    record_name: str
    record_type: str          # Primary, Derived, Related
    scroll_level: int = 0


@dataclass
class ComponentDefinition:
    name: str
    market: str = "GBL"
    pages: list[str] = field(default_factory=list)
    #records: list[ComponentRecord] = field(default_factory=list)
    #peoplecode: list[PeopleCodeEvent] = field(default_factory=list)
    description: Optional[str] = None
    search_record: Optional[str] = None
    add_search_record: Optional[str] = None

@dataclass 
class ComponentInterfaceDefinition:
    name: str
    display_name: str
    panel_group: str    
    description: Optional[str] = None
    search_record: Optional[str] = None
    add_search_record: Optional[str] = None

@dataclass
class MenuDefinition:
    """
    This class represents Menu definition.    
    """

    name: str
    menu_type: str
    menu_items: list[dict] = field(default_factory=list)
    description: Optional[str] = None

@dataclass
class MenuDefinitionSec:
    """
    This class represents Menu definition security.
    """
    name : str
    bar_name : str
    bar_item_name : str
    pnl_item_name : str
    display_only : str
    auth_flags : str

@dataclass
class PermissionListDefinition:
    """
    This class represents Permission List definition.
    """    
    name: str
    description: Optional[str] = None
    menu_items: list[MenuDefinitionSec] = field(default_factory=list)

@dataclass
class RoleDefinition:
    name: str
    description: Optional[str] = None
    permissions: list[str] = field(default_factory=list)

@dataclass
class PortalDefinition:
    name: str
    portal_type: str
    object_name: str
    label: str
    url: Optional[str] = None
    description: Optional[str] = None

@dataclass
class PageControl:
    control_type: str         # EditBox, DropDown, CheckBox, RadioButton, Grid, SubPage, etc.
    record_name: Optional[str] = None
    field_name: Optional[str] = None
    label: Optional[str] = None
    occurrence: Optional[int] = None

@dataclass
class PeopleCodeEvent:

    """
    This class represents PeopleCode event.
    It may be associated to a Record Field, a Record, a Component, or a Component Record.
    """ 

    component: str
    market: str
    record_name: str
    field_name: str
    event_type: str           # FieldDefault, FieldFormula, RowInit, RowInsert, RowDelete,
                              # SavePreChange, SavePostChange, FieldEdit, FieldChange,
                              # PrePopup, Activate, ItemSelected, etc.
    code_type: str           # Record, Component, Component Record, Component Record Field
    source_code: str = ""
    
@dataclass
class PageDefinition:

    """
    This class represents Page definition.
    """ 

    name: str
    page_type: str            # Standard, Secondary, Popup, etc.
    #controls: list[PageControl] = field(default_factory=list)
    description: Optional[str] = None

@dataclass
class AppPackagePCode:

    """
    This class represents Application Package PeopleCode.
    """ 

    app_package: str = ""
    code_type: str  ="Application Package PeopleCode"  
    event: str =""          
    source_code: str = ""
    #functions: list[str] = field(default_factory=list)


@dataclass
class AppPackageClass:
    class_name: str
    package_path: str
    source_code: str = ""
    methods: list[str] = field(default_factory=list)
    properties: list[str] = field(default_factory=list)


@dataclass
class AppPackageDefinition:
    name: str
    classes: list[AppPackageClass] = field(default_factory=list)
    sub_packages: list[str] = field(default_factory=list)
    description: Optional[str] = None


@dataclass
class MsgCatalog:

    """
    This class represents Message Catalog.
    """ 

    message_set: int
    message_number: int
    severity: str             # Message, Warning, Error
    message_text: str = ""
    explanation: Optional[str] = None


@dataclass
class QueryDefinition:

    """
    This class represents Query definition.
    """ 

    name: str
    query_type: str           # Public, Private, Process, Role
    sql_text: str = ""
    description: Optional[str] = None


# ============================================================================
# File Layout
# ============================================================================
@dataclass
class FLSegment:
    record_name: str
    segment_name: str
    field_name: str

@dataclass
class FileLayoutDefinition:
    name: str
    file_type: str            # CSV, Fixed, XML, etc.
    description: Optional[str] = None
    delimiter: Optional[str] = None
    records: list[FLSegment] = field(default_factory=list)


# ============================================================================
# Application Engine Classes
# ============================================================================

@dataclass
class AEPeopleCode:
    name: str =""
    section: str = ""
    market: str = ""
    step: str = ""
    action: str = ""
    #event: str = ""
    source_code: str = ""

@dataclass
class aetRecord:
    name: str
    defRecord: str

@dataclass
class AeStepAction:
    action_type: str         # SQL, PeopleCode, CallSection, etc.
    description: Optional[str] = None
    log_message: Optional[str] = None
    # log_message_text: Optional[str] = None
    peoplecode: AEPeopleCode = None
    sql: SQLDefinition = None
    call: Optional[str] = None

@dataclass
class AppEngineSteps:
    section_name: str
    program_name: str
    # section_type: str         # Prepare, Process, etc.
    step_name: str
    #step_actions: list[dict] = field(default_factory=list)   # step → action (SQL, PeopleCode, CallSection, etc.)
    step_actions: list[AeStepAction] = field(default_factory=list)

@dataclass
class AppEngineSection:
    section_name: str
    program_name: str
    steps: list[AppEngineSteps] = field(default_factory=list)
    

@dataclass
class AppEngineProgram:
    name: str
    ae_type: str      # Standard, Daemon, etc.
    disable_restart: str
    aet_records: list[aetRecord] = field(default_factory=list)
    temp_records: list[str] = field(default_factory=list)
    sections: list[AppEngineSection] = field(default_factory=list)
    #peoplecode: list[PeopleCodeEvent] = field(default_factory=list)
    #sql: list[SQLDefinition] = field(default_factory=list)
    description: Optional[str] = None    

# ============================================================================
# Process Classes
# ============================================================================
@dataclass
class ProcSecComp:
    component: str = ""

@dataclass
class ProcSecGroups:
    process_group: str =""

@dataclass
class ProcessDefinition:
    name: str
    process_type: str         # SQR, COBOL, Application Engine, Crystal, etc.
    description: Optional[str] = None
    run_location: Optional[str] = None
    parameters: Optional[str] = None
    components: [ProcSecComp] = None
    process_groups: [ProcSecGroups] = None

    def getProcessInfo(self):
        print (f"  🗂️  Process: {self.name}\n  📄 Description: {self.description}\n  📄 Type: {self.process_type}\n  📄 Run Location: {self.run_location}")

# ============================================================================
# Job Classes
# ============================================================================
@dataclass
class JobProcessDefinition:
    job_seq_nbr: str
    process_type: str
    process_name: str

@dataclass
class JobDefinition:
    job_name: str
    job_descr: str
    process_category: str
    process_list: [JobProcessDefinition] = None

# ============================================================================
# All related objects to Integration Broker
# ============================================================================
@dataclass
class uriTemplateDefinition:
    uri_sequence: str
    uri_template: str

@dataclass
class serviceOperationDefinition:
    name: str
    rest_method: str
    description: str
    rest_base_url: str
    comments: Optional[str] = None    
    uri_templates: [uriTemplateDefinition] = None

@dataclass
class messageDefinition:
    name: str
    message_type: str
    message_version: str
    package_id: Optional[str] = None
    schema_name: Optional[str] = None
    package_ver: Optional[str] = None

    def getMessageType(self) -> str:
        match self.message_type:
            case "6":
                return "Documento"
            case _:
                return "Unknown"


@dataclass
class DocumentElement:
    name: str
    sequence: int = 0
    element_type: str = ""    # Primitive, Compound, Collection
    label: str = ""
    is_required: bool = False

@dataclass
class DocumentDefinition:

    """
    NUEVO - Document de Integration Broker: package + nombre + version.
    Un mismo Document se proyecta en varios tipos de item (92 logico,
    93 XML, 96 schema, 110 JSON, 120 HTML); aca se consolidan en un objeto.
    """

    package: str
    name: str
    version: str
    label: str = ""
    elements: list[DocumentElement] = field(default_factory=list)
    physical_schemas: list[str] = field(default_factory=list)
    xsd: str = ""

    @property
    def full_name(self) -> str:
        return f"{self.package}.{self.name}.{self.version}"


# ============================================================================
# BI Publisher
# ============================================================================
@dataclass
class BIReportDefinition:
    name: str
    description: str = ""
    data_source: str = ""
    template_type: str  = ""
    template_id: str = ""
    output_format: str = ""

# ============================================================================
# Main Project Class
# ============================================================================
@dataclass
class PSProject:

    """
    Clase que contiene toda la información del proyecto parseada desde el XML exportado por PeopleSoft Application Designer.
    """

    project_name: str
    description: Optional[str] = None
    longdescription: Optional[str] = None
    
    # Definiciones por tipo
    records: list[RecordDefinition] = field(default_factory=list)    
    fields: list[FieldDefinition] = field(default_factory=list)
    sql_objects: list[SQLDefinition] = field(default_factory=list)
    pages: list[PageDefinition] = field(default_factory=list)    
    processes: list[ProcessDefinition] = field(default_factory=list)
    jobs: list[JobDefinition] = field(default_factory=list)
    peoplecode: list[PeopleCodeEvent] = field(default_factory=list)    
    ap_peoplecode: list[AppPackagePCode] = field(default_factory=list)   
    messages: list[messageDefinition] = field(default_factory=list)
    documents: list[DocumentDefinition] = field(default_factory=list)
    service_operations: list[serviceOperationDefinition] = field(default_factory=list)
    app_engines: list[AppEngineProgram] = field(default_factory=list)
    msg_catalog: list[MsgCatalog] = field(default_factory=list)
    file_layouts: list[FileLayoutDefinition] = field(default_factory=list)
    menus: list[MenuDefinition] = field(default_factory=list)
    permission_lists: list[PermissionListDefinition] = field(default_factory=list)
    queries: list[QueryDefinition] = field(default_factory=list)
    bi_reports: list[BIReportDefinition] = field(default_factory=list)
    components: list[ComponentDefinition] = field(default_factory=list)
    component_interfaces: list[ComponentInterfaceDefinition] = field(default_factory=list)
    roles: list[RoleDefinition] = field(default_factory=list)
    portals: list[PortalDefinition] = field(default_factory=list)    
    app_packages: list[AppPackageDefinition] = field(default_factory=list)
    """    

    style_sheets: list[StyleSheetDefinition] = field(default_factory=list)


    others: list[GenericDefinition] = field(default_factory=list)
    """

    def _find_instance_rows(self, rootNode_, class_name: str, rowset_name: str):
        """
        Busca dentro del XML el nodo <instance class=class_name> y retorna
        las rows del rowset indicado.

        :param rootNode_:    Nodo raíz del XML (ET.Element)
        :param class_name:   Valor del atributo 'class' del nodo <instance>
        :param rowset_name:  Valor del atributo 'name' del rowset a buscar
        :return:             Lista de elementos <row>, o lista vacía si no encuentra nada
        """
        for instance in rootNode_.iter("instance"):
            if instance.get("class") == class_name:
                rowset_node = instance.find(f".//rowset[@name='{rowset_name}']")
                if rowset_node is not None:
                    return rowset_node.findall("row")
        return []


    def _getRecFieldDefinition(self, recordNameStr_: str, row_) -> list[RecordField]| None:

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
                fieldTypeStr = helpers.decodeFieldType(eFieldTypeStr)
                nLengthStr = fieldRow.findtext("nLength", default="").strip()
                nDecimalPosStr = fieldRow.findtext("nDecimalPos", default="").strip()
                fUseEditNbr = int(fieldRow.findtext("fUseEdit", default="0").strip())

                # Get default Field Label        
                defaultLabelStr = ""                   
                labelNode = fieldRow.find(".//hDBFldLabel/rowset[@name='DBFldLabel']")
                if labelNode is not None:
                    for labelRow in labelNode.findall("row"):
                        if labelRow.findtext("bIsDefault", default="0").strip() == "1":
                            defaultLabelStr = labelRow.findtext("atmLabelID", default="").strip()
                            break

                # Obtain field flags by decoding fUseEditNbr
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

                if 1 in decodeResultArray['bits']:
                    isKeyBool = True

                if 2 in decodeResultArray['bits']:
                    isDuplicateBool = True

                if 8 in decodeResultArray['bits']:
                    isAuditBool = True
                
                if 16 in decodeResultArray['bits']:
                    isAlternateBool = True

                if 32 in decodeResultArray['bits']:
                    isLitBoxBool = True

                if 256 in decodeResultArray['bits']:
                    isReqBool = True

                if 2048 in decodeResultArray['bits']:
                    isSearchKeyBool = True

                if 262144 in decodeResultArray['bits']:
                    isFromSrchBool = True


                recordFieldObj = RecordField(
                    name = atmFieldNameStr,
                    field_type = fieldTypeStr,
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
                    label = defaultLabelStr
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
                    for recordRow in recDefnNode.findall("row"):

                        szRecNameStr = recordRow.findtext("szRecName", default="").strip()
                        nFieldCountStr = recordRow.findtext("nFieldCount", default="").strip()
                        
                                                    
                        if szRecNameStr == recordNameStr_:
                            eRecTypeStr = recordRow.findtext("eRecType", default="").strip()

                            recTypeDescrStr = helpers.decodeRecordType(eRecTypeStr)

                            szRecDescrStr = recordRow.findtext("szRecDescr", default="").strip() 

                            """
                            descrLongNode = recordRow.findall(".//hDescrLong/rowset[@name='hDescrLong']/row")

                            if descrLongNode is not None:
                                hDescrLongStr = descrLongNode.findtext("hDescrLong", default="").strip()
                            else:
                                hDescrLongStr = ""
                            """
                            szParentRecNameStr = recordRow.findtext("szParentRecName", default="").strip() 

                            # Debo obtener los campos asociados a este record
                            recordFields = []
                            for field in self._getRecFieldDefinition(recordNameStr_, recordRow):
                                recordFields.append(field)

                            resultObj = None
                            if eRecTypeStr == "1" or eRecTypeStr == "4": # Solo obtengo definición SQL para Record Type View y Dynamic View
                                resultObj = self._getSQLDefinition(recordNameStr_, "2", rootNode_)
                                

                            recordObj = RecordDefinition(
                                name = recordNameStr_,
                                object_property = " ", # hDescrLongStr pending
                                record_type = recTypeDescrStr,
                                field_count = nFieldCountStr,
                                fields = recordFields,
                                description = szRecDescrStr,
                                parent_record = szParentRecNameStr,
                                sql_view_text = resultObj
                            )
                            return recordObj
        return None

    def _getTranslateValues(self, fieldNameStr_: str, rootNode_) -> list[TranslateValue] | None:

        """
        Gets Translate Values from a field

        :param fieldNameStr_: Field Name
        :param rootNode_: where cursor is positioned
        :return: a list of TranslateValue object
        """

        translateValues = []

        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "XTM":
                xlatNode = instance.find(".//rowset[@name='XtmDefn']")
                if xlatNode is not None:
                    for xlatRow in xlatNode.findall("row"):
                        fieldNameStr = xlatRow.findtext("szFieldName", default="").strip()
                        if fieldNameStr == fieldNameStr_:
                            xlatNodeValues = xlatRow.find(".//hFvt/rowset[@name='XtmValue']")
                            if xlatNodeValues is not None:
                                for xlatValueRow in xlatNodeValues.findall("row"):
                                    fieldValueStr = xlatValueRow.findtext("szFieldValue", default="").strip()
                                    longNameStr = xlatValueRow.findtext("szLongName", default="").strip()
                                    shortNameStr = xlatValueRow.findtext("szShortName", default="").strip()
                                    effDateStr = xlatValueRow.findtext("szEffDt", default="").strip()
                                    effStatusStr = xlatValueRow.findtext("cEffStatus", default="").strip()

                                    translateValueObj = TranslateValue(
                                        value = fieldValueStr,
                                        long_name = longNameStr,
                                        short_name = shortNameStr,
                                        effective_date = effDateStr,
                                        status = effStatusStr
                                    )
                                    translateValues.append(translateValueObj)
                                return translateValues
        return None

    def _getFieldDefinition(self, fieldNameStr_: str, rootNode_) -> FieldDefinition | None:

        """
        Gets Field definition

        :param fieldNameStr_: Field Name
        :param rootNode_: where cursor is positioned
        :return: a Field Definition object
        """

        xlatDict = []
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "FIELD":         
                fieldNode = instance.find(".//rowset[@name='Field']")
                if fieldNode is not None:
                    for fieldRow in fieldNode.findall("row"):

                        szFieldNameStr = fieldRow.findtext("szFieldName", default="").strip()
                        # print(f"{szFieldNameStr}")
                        #print(f"{fieldNameStr_}")                     
                        if szFieldNameStr == fieldNameStr_:
                            eFieldTypeStr = fieldRow.findtext("eFieldType", default="").strip()
                            fieldTypeDescrStr = helpers.decodeFieldType(eFieldTypeStr)
                            nLengthStr = fieldRow.findtext("nLength", default="").strip()
                            nDecimalPosStr = fieldRow.findtext("nDecimalPos", default="").strip()                            
                            shorNameStr = fieldRow.findtext("szShortName", default="").strip() 
                            longNameStr = fieldRow.findtext("szLongName", default="").strip() 
                            
                            xlatDict = self._getTranslateValues(fieldNameStr_, rootNode_)

                            fieldObj = FieldDefinition(
                                name = fieldNameStr_,
                                field_type = fieldTypeDescrStr,
                                length = nLengthStr,
                                decimals = nDecimalPosStr,
                                # labelid = labelIDstr,
                                long_name = longNameStr,
                                short_name = shorNameStr,
                                # description = atmShortNameStr,
                                translate_values = xlatDict
                            )

                            return fieldObj
        return None

    def _getProcessDefinition(self, processTypeStr_: str, processNameStr_: str, rootNode_) -> ProcessDefinition | None:

        """
        Gets Process definition

        :param processTypeStr_: Process Type
        :param processNameStr_: Process Name
        :param rootNode_: where cursor is positioned
        :return: a Process Definition object
        """
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
                                        process_group = szPrcsGrpStr
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
                                process_groups = procGrpDict
                            )

                            return procDefnObj
        return None

    def _getJobDefinition(self, jobNameStr_: str, rootNode_) -> JobDefinition | None:

        """
        Gets Job definition

        :param jobNameStr_: Job Name
        :param rootNode_: where cursor is positioned
        :return: a Job Definition object
        """
        jobProcArray=[]

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
                            jobProcNode = jobRow.find(".//lpItemList/rowset[@name='PsjItem']")
                            
                            if jobProcNode is not None:
                                for procRow in jobProcNode.findall("row"):
                                    nJobSeqStr = procRow.findtext("nJobSeq", default="").strip()
                                    szPrcsTypeStr = procRow.findtext("szPrcsType", default="").strip()
                                    szPrcsNameStr = procRow.findtext("szPrcsName", default="").strip()                                    

                                    jobProcObj = JobProcessDefinition(
                                        job_seq_nbr = nJobSeqStr,
                                        process_type = szPrcsTypeStr,
                                        process_name = szPrcsNameStr
                                    )
                                    jobProcArray.append(jobProcObj)
                            
                            jobDefnObj = JobDefinition(
                                job_name = jobNameStr_,
                                job_descr = szDescrStr,
                                process_category = szPrcsCategoryStr,
                                process_list = jobProcArray
                            )
                            return jobDefnObj
        return None

    def _getSQLDefinition(self, sqlNameStr_: str, sqlTypeStr_: str, rootNode_) -> SQLDefinition | None:

        """
        Gets SQL definition

        :param sqlNameStr_: SQL Name
        :param sqlTypeStr_: SQL Type
        :param rootNode_: where cursor is positioned
        :return: a SQL Definition object
        """

        # Initialize variables
        sqlTypeStr=""

        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "SRM":         
                sqlNode = instance.find(".//rowset[@name='SrmDefn']")

                if sqlNode is not None:
                    for sqlRow in sqlNode.findall("row"):
                        szSqlIdStr = sqlRow.findtext("szSqlId", default="").strip()
                        szSqlTypeStr = sqlRow.findtext("szSqlType", default="").strip()  
                        
                        # print(f"Debug SQL: szSqlId={szSqlIdStr}, szSqlType={szSqlTypeStr}, {sqlTypeStr_}")

                        if szSqlIdStr == sqlNameStr_ and szSqlTypeStr == sqlTypeStr_:

                            descrElement = sqlRow.find(
                                        "lpStmtT"
                                        "/rowset[@name='SrmStmt']/row"
                                        "/szDescr"
                                    )
                            szDescrStr = descrElement.text if descrElement is not None and descrElement.text else ""

                            # print (f"Debug SQL: szDescr={szDescrStr}")

                            sqlTextElement = sqlRow.find(
                                "lpStmtT"
                                "/rowset[@name='SrmStmt']/row"
                                "/lpszSqlText"
                                "/rowset[@name='char']/row"
                                "/lpszSqlText"
                            )
                            szSQLTextStr = sqlTextElement.text if sqlTextElement is not None and sqlTextElement.text else ""

                            match sqlTypeStr_:
                                case "0": # SQL Object
                                    sqlTypeStr = "SQL Object"        
                                case "1": # Application Engine SQL
                                    sqlTypeStr = "Application Engine SQL"
                                case "2": # SQL View
                                    sqlTypeStr = "SQL View"
                                case _:
                                    sqlTypeStr = "Unknown SQL Type"
                            # debug print (f"Debug SQL: szSQLText={szSQLTextStr}")

                            sqlDefnObj = SQLDefinition(
                                name = szSqlIdStr,
                                sql_type = sqlTypeStr,
                                description = szDescrStr,
                                sql_text = szSQLTextStr
                            )

                            return sqlDefnObj
        return None

    def _getAEPeopleCode(self, objectValue0_: str, objectValue1_: str, objectValue2_: str, objectValue3_: str, objectValue4_:str, objectValue5_:str, objectValue6_:str, rootNode_) -> AEPeopleCode | None:

        """
        Gets Application Engine PeopleCode

        :param objectValue1_: Application Engine Name
        :param objectValue2_: Section Name
        :param objectValue3_: Market
        :param objectValue4_: default
        :param objectValue5_: Effective Date
        :param objectValue6_: Step Name
        :param rootNode_: where cursor is positioned
        :return: a Application Engine PeopleCode object
        """

        for instance in rootNode_.iter("instance"):                       
            if instance.get("class") == "PCM":
                pcNode = instance.find(".//rowset[@name='PcmProg']")                
                if pcNode is not None:
                    
                    for pcRow in pcNode.findall("row"):                        
                        szObjectValue_0Str = pcRow.findtext("szObjectValue_0", default="").strip() # App Engine
                        szObjectValue_1Str = pcRow.findtext("szObjectValue_1", default="").strip() # Section
                        szObjectValue_2Str = pcRow.findtext("szObjectValue_2", default="").strip() # Market
                        szObjectValue_3Str = pcRow.findtext("szObjectValue_3", default="").strip() # default
                        szObjectValue_4Str = pcRow.findtext("szObjectValue_4", default="").strip() # Effective Date
                        szObjectValue_5Str = pcRow.findtext("szObjectValue_5", default="").strip() # Step Name
                        szObjectValue_6Str = pcRow.findtext("szObjectValue_6", default="").strip() # OnExecute
                        
                        if szObjectValue_0Str == objectValue0_ and szObjectValue_1Str == objectValue1_ and szObjectValue_2Str == objectValue2_ and \
                        szObjectValue_3Str == objectValue3_ and szObjectValue_4Str == objectValue4_ and szObjectValue_5Str == objectValue5_ and \
                        szObjectValue_6Str == objectValue6_:
                            peopleCodeText = instance.find(".//peoplecode_text")    
                            
                            pcEventObj = AEPeopleCode(
                                name = objectValue0_,
                                section = objectValue1_,
                                market = objectValue2_,
                                step = objectValue5_,
                                action = objectValue6_,
                                source_code = peopleCodeText.text.strip() if peopleCodeText is not None and peopleCodeText.text else ""
                            )

                            peopleCodeTypeStr = "Application Engine PeopleCode"
                            return pcEventObj
        return None

    def _getEventPeopleCode(self, objectValue0_: str, objectValue1_: str, objectValue2_: str, objectValue3_: str, objectValue4_:str , eventTypeStr_: str, rootNode_) -> PeopleCodeEvent | None:


        """
        Gets Event PeopleCode

        :param objectValue0_: Record Name or Component Name
        :param objectValue1_: Field or Market
        :param objectValue2_: Event Type 
        :param objectValue3_: Event when Component Record | Field when Component Record Field
        :param objectValue4_: Event when Component Record Field
        :param eventTypeStr_: REC (Record), CMP (Component), CR (Component Record), CRF (Component Record Field)
        :param rootNode_: where cursor is positioned
        :return: a PeopleCode object
        """

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
                            case "PG":
                                # Page PeopleCode
                                szObjectValue_0Str = pcRow.findtext("szObjectValue_0", default="").strip() # Page
                                szObjectValue_1Str = pcRow.findtext("szObjectValue_1", default="").strip() # Activate
                                if szObjectValue_0Str == objectValue0_ and szObjectValue_1Str == objectValue1_ :

                                    peopleCodeTypeStr = "Page"
                                    peopleCodeText = instance.find(".//peoplecode_text")    
                                    pcEventObj = PeopleCodeEvent(
                                            component = "",
                                            market = "",
                                            record_name = objectValue0_,
                                            field_name = "",
                                            event_type =  objectValue1_,          # Activate, PreActivate, PostActivate, etc.
                                            code_type = peopleCodeTypeStr,                                                            
                                            source_code = peopleCodeText.text.strip() if peopleCodeText is not None and peopleCodeText.text else ""
                                    )
                                    return pcEventObj
                            case "REC" | "CMP":
                                # Record Field
                                # Component
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
                                            field_name = objectValue1_ if eventTypeStr_ == "REC" else "",
                                            event_type =  objectValue2_,          # FieldDefault, FieldFormula, RowInit, RowInsert, RowDelete,
                                                                    # SavePreChange, SavePostChange, FieldEdit, FieldChange,
                                                                    # PrePopup, Activate, ItemSelected, etc.
                                            code_type = peopleCodeTypeStr,                                                            
                                            source_code = peopleCodeText.text.strip() if peopleCodeText is not None and peopleCodeText.text else ""
                                    )
                                    return pcEventObj
                            
                            case "CR":
                                # Component Record
                                szObjectValue_0Str = pcRow.findtext("szObjectValue_0", default="").strip() # Component
                                szObjectValue_1Str = pcRow.findtext("szObjectValue_1", default="").strip() # Market
                                szObjectValue_2Str = pcRow.findtext("szObjectValue_2", default="").strip() # Record
                                szObjectValue_3Str = pcRow.findtext("szObjectValue_3", default="").strip() # Event

                                peopleCodeTypeStr = "Component Record"

                                if szObjectValue_0Str == objectValue0_ and szObjectValue_1Str == objectValue1_ and szObjectValue_2Str == objectValue2_ and szObjectValue_3Str == objectValue3_ :

                                    peopleCodeText = instance.find(".//peoplecode_text")                                        
                                    pcEventObj = PeopleCodeEvent(
                                        component = objectValue0_,
                                        market = objectValue1_,                                        
                                        record_name = objectValue2_,
                                        field_name = "",
                                        event_type =  objectValue3_,          # FieldDefault, FieldFormula, RowInit, RowInsert, RowDelete,
                                                                    # SavePreChange, SavePostChange, FieldEdit, FieldChange,
                                                                    # PrePopup, Activate, ItemSelected, etc.
                                        code_type = peopleCodeTypeStr,                                                            
                                        source_code = peopleCodeText.text.strip() if peopleCodeText is not None and peopleCodeText.text else ""
                                    )                                
                                    return pcEventObj

                                    
                            case "CRF":
                                # Component Record Field
                                szObjectValue_0Str = pcRow.findtext("szObjectValue_0", default="").strip() # Component
                                szObjectValue_1Str = pcRow.findtext("szObjectValue_1", default="").strip() # Market
                                szObjectValue_2Str = pcRow.findtext("szObjectValue_2", default="").strip() # Record
                                szObjectValue_3Str = pcRow.findtext("szObjectValue_3", default="").strip() # Field
                                szObjectValue_4Str = pcRow.findtext("szObjectValue_4", default="").strip() # Event

                                peopleCodeTypeStr = "Component Record Field"

                                if szObjectValue_0Str == objectValue0_ and szObjectValue_1Str == objectValue1_ and szObjectValue_2Str == objectValue2_ and szObjectValue_3Str == objectValue3_  and  szObjectValue_4Str == objectValue4_ :

                                    peopleCodeText = instance.find(".//peoplecode_text")    
                                    pcEventObj = PeopleCodeEvent(
                                        component = objectValue0_,
                                        market = objectValue1_,                                        
                                        record_name = objectValue2_,
                                        field_name = objectValue3_,
                                        event_type =  objectValue4_,          # FieldDefault, FieldFormula, RowInit, RowInsert, RowDelete,
                                                                    # SavePreChange, SavePostChange, FieldEdit, FieldChange,
                                                                    # PrePopup, Activate, ItemSelected, etc.
                                        code_type = peopleCodeTypeStr,                                                            
                                        source_code = peopleCodeText.text.strip() if peopleCodeText is not None and peopleCodeText.text else ""
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

                        #print("------")
                        #print(f"Debug App Package PeopleCode: packageNameStr_={packageNameStr_}, objectValue1_={objectValue1_}, objectValue2_={objectValue2_}, objectValue3_={objectValue3_}")
                        #print(f"Debug App Package PeopleCode: szObjectValue_0={szObjectValue_0Str}, szObjectValue_1={szObjectValue_1Str}, szObjectValue_2={szObjectValue_2Str}, szObjectValue_3={szObjectValue_3Str}")
                        if szObjectValue_0Str == packageNameStr_ and szObjectValue_1Str == objectValue1_ and (szObjectValue_2Str == objectValue2_ or szObjectValue_2Str == objectValue3_) \
                            and (szObjectValue_3Str == objectValue3_ or szObjectValue_3Str == ""):
                            
                            peopleCodeText = instance.find(".//peoplecode_text")       

                            eventTypeStr = f"{szObjectValue_0Str}:{szObjectValue_1Str}"
                            if objectValue2_ != " ":
                                eventTypeStr=f"{szObjectValue_0Str}:{szObjectValue_1Str}:{szObjectValue_2Str}"
                                if objectValue3_ != "OnExecute":
                                    eventTypeStr=f"{szObjectValue_0Str}:{szObjectValue_1Str}:{szObjectValue_2Str}:{szObjectValue_3Str}"
                                else:
                                    #eventTypeStr=f"{packageNameStr_}:{objectValue1_}:{objectValue2_}.{objectValue3_}"
                                    eventTypeStr=f"{szObjectValue_0Str}:{szObjectValue_1Str}.{szObjectValue_2Str}"
                            
                            #print(f"Debug App Package PeopleCode: source_code={peopleCodeText.text.strip()}")

                            pcEventObj = AppPackagePCode(
                                app_package=szObjectValue_0Str,
                                event=eventTypeStr,
                                code_type="Application Package PeopleCode",
                                source_code=peopleCodeText.text.strip() if peopleCodeText is not None and peopleCodeText.text else ""
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
                            pageTypeDescrStr = helpers.decodePageType(ePnlTypeStr)
                            szDescrStr = pageRow.findtext("szDescr", default="").strip() 

                            pageObj = PageDefinition(
                                name=pageNameStr_,
                                page_type=pageTypeDescrStr,
                                description=szDescrStr
                            )

                            return pageObj
        return None

    def _getMessage(self, messageNameStr_: str, rootNode_) -> messageDefinition | None:
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "MSDM":         
                msgNode = instance.find(".//rowset[@name='MsgDefn']")

                if msgNode is not None:
                    for msgRow in msgNode.findall("row"):
                        szMsgNameStr = msgRow.findtext("szMsgName", default="").strip()
                                                    
                        if szMsgNameStr == messageNameStr_:

                            handleNode = instance.find(".//rowset[@name='MsgVer']")
                            for handleRow in handleNode.findall("row"):                               
                                szMsgTypeStr = handleRow.findtext("nMsgType", default="").strip()
                                szMsgVerStr = handleRow.findtext("szVerName", default="").strip()  
                                szPkgIdStr = handleRow.findtext("szIb_packageid", default="").strip() 
                                szSchemaNameStr = handleRow.findtext("szIb_schemaname", default="").strip()
                                szPkgVerStr = handleRow.findtext("szIb_variantname", default="").strip()

                            messageObj = messageDefinition(
                                name=messageNameStr_,
                                message_type=szMsgTypeStr,
                                message_version=szMsgVerStr,
                                package_id=szPkgIdStr,
                                schema_name=szSchemaNameStr,
                                package_ver=szPkgVerStr
                            )
                        
                            return messageObj
        return None

    def _getDocumentDefinition(self, packageStr_: str, nameStr_: str, versionStr_: str, rootNode_) -> DocumentDefinition | None:


        documentObj = None

        # --- Esquema logico (LSDM): etiqueta y elementos
        for instance in rootNode_.iter("instance"):
            if instance.get("class") == "LSDM":  

                defnNode = instance.find(".//rowset[@name='LSDEFN']")

                if defnNode is not None:
                    for docRow in defnNode.findall("row"):
                        strPackageName = docRow.findtext("m_key.m_atmPackageName", default="").strip()
                        strSchema = docRow.findtext("m_key.m_atmLogicalSchemaName", default="").strip()
                        strVersion = docRow.findtext("m_key.m_atmVariantName", default="").strip()
                        strLabel = docRow.findtext("m_atmLabel", default="").strip()

                        #print(f"Debug Document: strPackageName={strPackageName}, strSchema={strSchema}, strVersion={strVersion}")

                        if strPackageName == packageStr_ and strSchema == nameStr_ and strVersion == versionStr_:
                            documentObj = DocumentDefinition(
                                package = packageStr_,
                                name = nameStr_,
                                version = versionStr_,
                                label = strLabel,
                            )

                            elementNode = instance.find(".//rowset[@name='LSELEMENT']")
                            if elementNode is not None:
                                for elementRow in elementNode.findall("row"):

                                    elementNameStr = elementRow.findtext("m_atmName", default="").strip()

                                    if elementRow.findtext("m_bIsCollection", default="0").strip() == "1":
                                        elementTypeStr = "Collection"
                                    elif elementRow.findtext("m_bIsCompound", default="0").strip() == "1":
                                        elementTypeStr = "Compound"
                                    else:
                                        elementTypeStr = "Primitive"

                                    documentObj.elements.append(DocumentElement(
                                        name = elementNameStr,
                                        sequence = int(elementRow.findtext("m_nSequenceNumber", default="0").strip() or 0),
                                        element_type = elementTypeStr,
                                        label = elementRow.findtext("m_atmLabel", default="").strip(),
                                        is_required = elementRow.findtext("m_bIsRequired", default="0").strip() == "1",
                                    ))

                                return documentObj
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
                                    uriTemplateElement = uriTemplRow.find("lpszURITemplate/rowset/row/lpszURITemplate")
                                    uriTemplateStr = uriTemplateElement.text if uriTemplateElement is not None and uriTemplateElement.text else ""
                                    uriTemplateObj = uriTemplateDefinition(
                                        uri_sequence  = uriSeqStr,
                                        uri_template = uriTemplateStr
                                    )
                                    uriTemplateArray.append(uriTemplateObj)
                                    # print(f"{uriTemplateStr}")

                            serviceOperObj = serviceOperationDefinition(
                                name = serviceOpDefStr_,
                                rest_method = restMethodStr,
                                description = szDescrStr,
                                comments = operDescrStr,
                                rest_base_url = restBaseUrlStr,
                                uri_templates = uriTemplateArray
                            )
                        
                            return serviceOperObj
        return None


    def _aeIterator(self, sqlNode_, strAction_ : str, rootNode_) -> AeStepAction | None:
        for sqlRow in sqlNode_.findall("row"):
            sqlIDStr = sqlRow.findtext("szSqlId", default="").strip()                                                    
            szDescr = sqlRow.findtext("szDescr", default="").strip() # Está un nivel más arriba
            sqlObj = self._getSQLDefinition(sqlIDStr, "1", rootNode_) # 1 means Application Engine SQL
            
            if sqlObj is not None:
                
                stepActionObj = AeStepAction(
                    action_type = strAction_,
                    description = szDescr,  #sqlObj.description,
                    sql = sqlObj
                )
                return stepActionObj
        return None


    def _getAppEngine(self, appEngineStr_: str, rootNode_) -> AppEngineProgram | None:

        # Default values
        aeSectionDict = []
        returnObjectBool = False
        aeTypeStr = ""
        disableRestartStr = ""
        aeDescrStr = ""
        aetDict = []
        tempDict = []
        
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
                            tmpNode = aeDefNode.find(".//lpTempTblList/rowset[@name='AeTempTbl']")
                            if tmpNode is not None:
                                for tmpRow in tmpNode.findall("row"):
                                    tmpRecStr = tmpRow.findtext("szRecName", default="").strip()

                                    tempDict.append(tmpRecStr)

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
                                    
                                    marketStr = sectionRow.findtext("szMarket", default="").strip() # Market, está a este nivel
                                    effdtStr = sectionRow.findtext("szEffDt", default="").strip() # Effective Date, está a este nivel    

                                    if aeStepNode is not None:
                                        aeStepsDict = []
                                        
                                        for aeStepRow in aeStepNode.findall("row"):
                                            stepsStr = ""
                                            stepDict = []
                                            aeStepNameStr = aeStepRow.findtext("szStep", default="").strip()
                                            
                                            # ============== Do Steps (Do While, Do When, Do Select, Do Until) ==============
                                            # Do When
                                            sqlNode = aeStepRow.find("lpAeStmtWhen/rowset[@name='AeStmtWhen']") 
                                            if sqlNode is not None:
                                                resultObject = self._aeIterator(sqlNode, "Do When", rootNode_)
                                                if resultObject is not None:
                                                    stepDict.append(resultObject)
                                                """
                                                for sqlRow in sqlNode.findall("row"):
                                                    sqlIDStr = sqlRow.findtext("szSqlId", default="").strip()                                                    
                                                    
                                                    sqlObj = self._getSQLDefinition(sqlIDStr, "1", rootNode_) # 1 means Application Engine SQL
                                                    
                                                    if sqlObj is not None:
                                                        
                                                        stepActionObj = AeStepAction(
                                                            action_type = "Do When",
                                                            description = sqlObj.description,
                                                            sql = sqlObj
                                                        )
                                                        # print(f"Debug Do When SQL: sqlID={sqlIDStr}: sqlText={sqlObj.sql_text}")    
                                                        stepDict.append(stepActionObj)
                                                """

                                            # Do While
                                            sqlNode = aeStepRow.find("lpAeStmtWhile/rowset[@name='AeStmtWhen']") 
                                            if sqlNode is not None:
                                                resultObject = self._aeIterator(sqlNode, "Do While", rootNode_)
                                                if resultObject is not None:
                                                    stepDict.append(resultObject)

                                            # Do Until
                                            sqlNode = aeStepRow.find("lpAeStmtUntil/rowset[@name='AeStmtWhen']") 
                                            if sqlNode is not None:
                                                resultObject = self._aeIterator(sqlNode, "Do Until", rootNode_)
                                                if resultObject is not None:
                                                    stepDict.append(resultObject)

                                            # Do Select
                                            sqlNode = aeStepRow.find("lpAeStmtSelect/rowset[@name='AeStmtWhen']")                                                    
                                            if sqlNode is not None:
                                                resultObject = self._aeIterator(sqlNode, "Do Select", rootNode_)
                                                if resultObject is not None:
                                                    stepDict.append(resultObject)


                                            # ============== PeopleCode Step ==============
                                            pcodNode = aeStepRow.find("lpAePcode/rowset[@name='AePcode']")
                                            if pcodNode is not None:
                                                stepNameStr = aeStepRow.findtext("szStep", default="").strip() # Está un nivel más arriba
                                                szDescr = aeStepRow.findtext("szDescr", default="").strip() # Está un nivel más arriba
                                                pcObj = self._getAEPeopleCode(appEngineStr_, sectionNameStr, marketStr, "default", effdtStr , stepNameStr, "OnExecute", rootNode_)
                                                # print(f"Debug PeopleCode: appEngine={appEngineStr_}, section={sectionNameStr}, market={marketStr}, step={stepNameStr}, effdt={effdtStr}")
                                                if pcObj is not None:
                                                    stepActionObj = AeStepAction(
                                                        action_type = "PeopleCode",
                                                        description = szDescr,
                                                        peoplecode = pcObj
                                                    )

                                                    stepDict.append(stepActionObj)
                                            
                                            # ============== Application Engine SQL ==============
                                            sqlNode = aeStepRow.find("lpAeStmtSql/rowset[@name='AeStmtWhen']")   
                                            if sqlNode is not None:                                            
                                                for sqlRow in sqlNode.findall("row"):
                                                    sqlIDStr = sqlRow.findtext("szSqlId", default="").strip()  # EngineSection Step S
                                                    sqlObj = self._getSQLDefinition(sqlIDStr, "1", rootNode_) # 1 means Application Engine SQL
                                                    if sqlObj is not None:
                                                        
                                                        stepActionObj = AeStepAction(
                                                            action_type = "SQL",
                                                            description = sqlObj.description,
                                                            sql = sqlObj
                                                        )

                                                        stepDict.append(stepActionObj)
                                            
                                            # ============== Log Message ==============
                                            logNode = aeStepRow.find("lpAeMsg/rowset[@name='AeMsg']")
                                            if logNode is not None:
                                                for logRow in logNode.findall("row"):
                                                    msgSetStr = logRow.findtext("lMessageSetNbr", default="").strip()
                                                    msgNumStr = logRow.findtext("lMessageNbr", default="").strip()
                                                    # msgCatObj = self._getMsgCatalog(msgSetStr, msgNumStr, rootNode_)
                                                    szDescrStr = logRow.findtext("szDescr", default="").strip()


                                                    stepActionObj = AeStepAction(
                                                        action_type = "Log Message",
                                                        log_message = "(" + msgSetStr + ", " + msgNumStr + ")",
                                                        # log_message_text = f"{msgCatObj.severity} - {msgCatObj.message_text}",
                                                        description = szDescrStr,
                                                        # msg_catalog = msgCatObj
                                                    )
                                                    # print(f"Debug Log Message: msgSet={msgSetStr}, msgNum={msgNumStr}")
                                                    stepDict.append(stepActionObj)

                                            # ============== Call Section ==============
                                            callSectNode = aeStepRow.find("lpAeDoSect/rowset[@name='AeDoSect']")
                                            if callSectNode is not None:
                                                callAppElement = aeStepRow.find("lpAeDoSect/rowset[@name='AeDoSect']/row/szDoApplId")
                                                callAppStr = callAppElement.text if callAppElement is not None and callAppElement.text else ""
                                                callAppSectElement = aeStepRow.find("lpAeDoSect/rowset[@name='AeDoSect']/row/szDoSection")
                                                callAppSectStr = callAppSectElement.text if callAppSectElement is not None and callAppSectElement.text else ""
                                                stepActionObj = AeStepAction(
                                                    action_type = "Call Section",
                                                    call = "Call Section " + callAppStr + "." + callAppSectStr ,
                                                    #sql = sqlObj
                                                )
                                                # print(f"Debug Call Section: callApp={callAppStr}, callSection={callAppSectStr}")
                                                stepDict.append(stepActionObj)
                                            
                                            # print(f"Debug Section: {sectionNameStr} , Step: {aeStepNameStr}, actions count: {len(stepDict)}")
                                            aStepsObj = AppEngineSteps(
                                                section_name = sectionNameStr,
                                                program_name = appEngineStr_,
                                                step_name = aeStepNameStr,
                                                step_actions = stepDict
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
                ae_type = aeTypeStr,
                aet_records = aetDict,
                temp_records = tempDict,
                sections =  aeSectionDict,
                disable_restart = disableRestartStr,
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
                                # print (f"mensaje {msgNumberStr} = {msgNumberstr_}")
                                if msgNumberStr == msgNumberstr_:
                                    
                                    match msgNumberRow.findtext("cMsgSeverity", default="").strip():
                                        case "M":
                                            severityCodeStr = "Message"
                                        case "E":
                                            severityCodeStr = "Error"
                                        case _:
                                            severityCodeStr = "Unknown"

                                    msgTextElement = msgNumberRow.find(".//pszMsgText/rowset/row/pszMsgText")
                                    pszMsgText = msgTextElement.text if msgTextElement is not None and msgTextElement.text else ""

                                    msgCatObj = MsgCatalog(
                                        message_set = msgSetStr_,
                                        message_number = msgNumberstr_,
                                        severity = severityCodeStr,
                                        message_text = pszMsgText
                                    )
                                    
                                    return msgCatObj
        return None

    def _getFileLayout(self, fileLayoutStr_: str, rootNode_) -> FileLayoutDefinition | None:
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "FLM":         
                fileDefnNode = instance.find(".//rowset[@name='FldFileDefn']")

                if fileDefnNode is not None:
                    for fileDefnRow in fileDefnNode.findall("row"):
                        szFileLayoutStr = fileDefnRow.findtext("szDefnName", default="").strip()
                        # formatStr  = fileDefnRow.findtext("eFormat", default="").strip()

                        if szFileLayoutStr == fileLayoutStr_:
                            szDescrStr = fileDefnRow.findtext("szDescr", default="").strip() 

                            segmentNode = fileDefnNode.find(".//hSegTable/rowset[@name='FldSegDefn']")
                            if segmentNode is not None:
                                segmentDict = []
                                szDelimiterStr = ""
                                for segmentRow in segmentNode.findall("row"):
                                    if szFileLayoutStr == segmentRow.findtext("szDefnName", default="").strip():
                                        szSegmentNameStr = segmentRow.findtext("szSegmentName", default="").strip()
                                        szDelimiterStr = segmentRow.findtext("szDelimiter", default="").strip()

                                        fieldNode = segmentNode.find(".//hFieldTable/rowset[@name='FldFldDefn']")
                                        if fieldNode is not None:
                                            for fieldRow in fieldNode.findall("row"):                                        
                                                recrdStr = fieldRow.findtext("szDefnName", default="").strip()
                                                segmentStr = fieldRow.findtext("szSegmentName", default="").strip()
                                                fieldStr =  fieldRow.findtext("szFieldName", default="").strip()
                                            
                                                segmentObj = FLSegment(
                                                    record_name=recrdStr,
                                                    segment_name=segmentStr,
                                                    field_name=fieldStr
                                                )
                                                segmentDict.append(segmentObj)

                        # moví la indentación dentro del if szFileLayoutStr == fileLayoutStr_:
                            fileLayoutObj = FileLayoutDefinition(
                                name = fileLayoutStr_,
                                file_type = "pending",            # CSV, Fixed, XML, etc.
                                description = szDescrStr,
                                delimiter = szDelimiterStr,
                                records = segmentDict
                            )
                            return fileLayoutObj
        return None

    def _getQueryDefinition(self, queryNameStr_: str, rootNode_) -> QueryDefinition | None:
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "QDM":         
                queryNode = instance.find(".//rowset[@name='QdmDefn']")

                if queryNode is not None:
                    for queryRow in queryNode.findall("row"):
                        szQryNameStr = queryRow.findtext("szQryName", default="").strip()

                        if szQryNameStr == queryNameStr_:
                            szDescrStr = queryRow.findtext("szDescr", default="").strip() 

                            psQueryObj = QueryDefinition(
                                name = queryNameStr_,
                                query_type = "pending",     # Public, Private... No sé en qué campo está
                                sql_text = "pending",       # Esto se obtiene procesando los nodos de QdmDefn
                                description = szDescrStr
                            )
                            return psQueryObj
        return None

    def _getMenuDefinition(self, menuNameStr_: str, rootNode_) -> MenuDefinition | None:
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "MDM":         
                menuNode = instance.find(".//rowset[@name='MdmDefn']")

                if menuNode is not None:
                    for menuRow in menuNode.findall("row"):
                        szMenuNameStr = menuRow.findtext("szMenuName", default="").strip()
                        menuTypeStr = menuRow.findtext("eMenuType", default="").strip() # Main, Popup, etc.
                              
                        if szMenuNameStr == menuNameStr_:
                            szDescrStr = menuRow.findtext("szDescr", default="").strip() 

                            menuDefnObj = MenuDefinition(
                                name = menuNameStr_,
                                menu_type = menuTypeStr,
                                description = szDescrStr
                            )
                            """
                            Pendiente menu items. El problema es que trae todos los ítems, independiente de
                            si son nuevos o ya existían
                            """

                            return menuDefnObj
        return None

    def _getPermissionList(self, permissionListStr_: str, rootNode_) -> PermissionListDefinition | None:

        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "CLM":         
                plNode = instance.find(".//rowset[@name='ClmDefn']")

                if plNode is not None:
                    for plRow in plNode.findall("row"):
                        permListStr = plRow.findtext("szClassId", default="").strip()  
                        descrStr = plRow.findtext("szClassDefnDescr", default="").strip()

                        itemsDict = []
                        """ Not used for now. It generates a huge amount of information.
                        if permListStr == permissionListStr_:                           
                            plAuthItemNode = plNode.find(".//hAit/rowset[@name='ClmAuthItem']")

                            
                            for plAuthItemRow in plAuthItemNode.findall("row"):
                                authMenuStr = plAuthItemRow.findtext("atmMenuName", default="").strip()
                                authBarStr = plAuthItemRow.findtext("atmBarName", default="").strip()
                                authBarItemStr = plAuthItemRow.findtext("atmBarItemName", default="").strip()
                                authPnlItemStr = plAuthItemRow.findtext("atmPnlItemName", default="").strip()
                                displayOnlyStr = plAuthItemRow.findtext("bDisplayOnly", default="").strip()
                                authFlagsStr = plAuthItemRow.findtext("wAuthorizedActions", default="").strip()
                                
                                authItemObj = MenuDefinitionSec(
                                    name = authMenuStr,
                                    bar_name = authBarStr,
                                    bar_item_name = authBarItemStr,
                                    pnl_item_name = authPnlItemStr,
                                    display_only = displayOnlyStr,
                                    auth_flags = authFlagsStr  
                                )
                                
                                itemsDict.append(authItemObj)
                            """
                        permListObj = PermissionListDefinition(
                            name = permissionListStr_,
                            description = descrStr,
                            menu_items = itemsDict
                        )
                        return permListObj
        return None

    def _getBIReportDefinition(self, reportNameStr_: str, rootNode_) -> BIReportDefinition | None:
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "XRRDM":         
                reportNode = instance.find(".//rowset[@name='ReportDefn']")

                if reportNode is not None:
                    for reportRow in reportNode.findall("row"):
                        szReportNameStr = reportRow.findtext("szReport_defn_id", default="").strip()
                                                    
                        if szReportNameStr == reportNameStr_:
                            rptDescrStr = reportRow.findtext("szDescr", default="").strip() 
                            dataSrcStr = reportRow.findtext("szDs_type", default="").strip() #XML, PSQUERY
                            dataSrcID = reportRow.findtext("szDs_id", default="").strip() 
                            templateStr = reportRow.findtext("szTemplate_type", default="").strip()

                            # Only default output format.
                            outputNode = reportRow.find(".//pXprptoutfmt/rowset[@name='OutFormat']")
                            outputFormatStr = ""
                            if outputNode is not None:
                                for outputRow in outputNode.findall("row"):
                                    if outputRow.findtext("cIs_default", default="").strip() == "Y":
                                        outputFormatStr = outputRow.findtext("szFormat_type", default="").strip()
                            
                            # Only default template.
                            tmpltNode = reportRow.find(".//pXprpttmplt/rowset[@name='RptTmpl']")
                            templateStr = ""
                            if tmpltNode is not None:
                                for tmpltRow in tmpltNode.findall("row"):
                                    if tmpltRow.findtext("cIs_default", default="").strip() == "Y":
                                        templateStr = tmpltRow.findtext("szTemplate_id", default="").strip()

                            reportDefnObj = BIReportDefinition(
                                name = reportNameStr_,
                                description = rptDescrStr,
                                data_source = dataSrcStr,
                                template_type = templateStr,
                                template_id = templateStr,
                                output_format = outputFormatStr
                            )

                            return reportDefnObj
        return None

    def _getComponentDefinition(self, componentNameStr_: str, marketStr_: str, rootNode_) -> ComponentDefinition | None:
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "PGM":         
                cmpNode = instance.find(".//rowset[@name='PgmDefn']")

                if cmpNode is not None:
                    pageDict = []
                    for cmpRow in cmpNode.findall("row"):
                        pageComp = cmpRow.find(".//hPgt/rowset[@name='PnlMenuItem']")

                        # Navegar por las páginas del componente
                        if pageComp is not None:
                            for pageCompRow in pageComp.findall("row"):
                                pageName = pageCompRow.findtext("szItemName", default="").strip()
                                pageDict.append(pageName)

                            szCmpNameStr = cmpRow.findtext("szPnlGrpName", default="").strip()

                            # Valido que esto en el componente que estoy procesando.     
                            if szCmpNameStr == componentNameStr_:
                                searchRecStr = cmpRow.findtext("szSearchRecName", default="").strip() 
                                addSearchRecStr = cmpRow.findtext("szAddSearchRecName", default="").strip() 
                                compDescrStr = cmpRow.findtext("szPgmDescr", default="").strip()

                                componentDefnObj = ComponentDefinition(
                                    name = componentNameStr_,
                                    market = marketStr_,
                                    search_record = searchRecStr,
                                    add_search_record = addSearchRecStr,
                                    description = compDescrStr,
                                    pages = pageDict
                                )

                                return componentDefnObj
        return None

    def _getComponentInterface(self, componentInterfaceStr_: str, rootNode_) -> ComponentInterfaceDefinition | None:
        for instance in rootNode_.iter("instance"):
            if instance.get("class") == "BCM":
                ciNode = instance.find(".//rowset[@name='BcmDefn']")
                if ciNode is not None:
                    for ciRow in ciNode.findall("row"):
                        ciNameStr = ciRow.findtext("szBcName", default="").strip()
                        if ciNameStr == componentInterfaceStr_:
                            displayNameStr = ciRow.findtext("szBcDisplayName", default="").strip()
                            descrStr = ciRow.findtext("szBcDescr", default="").strip()
                            panelGroupStr = ciRow.findtext("szBcPanelGroup", default="").strip()
                            searchRecStr = ciRow.findtext("szBcSearchRec", default="").strip() 
                            addSearchRecStr = ciRow.findtext("szBcAddSearchRec", default="").strip() 

                            componentInterfaceDefnObj = ComponentInterfaceDefinition(
                                name = componentInterfaceStr_,
                                display_name = displayNameStr,
                                description = descrStr,
                                panel_group = panelGroupStr,
                                search_record = searchRecStr,
                                add_search_record = addSearchRecStr
                            )

                            return componentInterfaceDefnObj
        return None

    def _getRoleDefinition(self, roleNameStr_: str, rootNode_) -> RoleDefinition | None:
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "ROLM":         
                roleNode = instance.find(".//rowset[@name='Roledefn']")

                if roleNode is not None:
                    for roleRow in roleNode.findall("row"):
                        szRoleNameStr = roleRow.findtext("szRolename", default="").strip()
                        
                        if szRoleNameStr == roleNameStr_:
                            szDescrStr = roleRow.findtext("szDescr", default="").strip() 
                            
                            # Permission lists
                            permissionsDict = []
                            classNode = roleNode.find(".//pRoleclass/rowset[@name='Roleclass']")
                            if classNode is not None:
                                for classRow in classNode.findall("row"):
                                    classStr = classRow.findtext("szClassid", default="").strip()
                                    permissionsDict.append(classStr)                                    
                            
                            roleDefnObj = RoleDefinition(
                                name = roleNameStr_,
                                description = szDescrStr,
                                permissions = permissionsDict
                            )

                            return roleDefnObj
        return None

    def _getPortalDefinition(self, portalNameStr_: str, portalTypeStr_: str, objectValue2_: str, rootNode_) -> PortalDefinition | None:
        for instance in rootNode_.iter("instance"):            
            if instance.get("class") == "PRSM":         
                portalNode = instance.find(".//rowset[@name='PrsmDefn']")

                if portalNode is not None:
                    for portalRow in portalNode.findall("row"):
                        portalNameStr = portalRow.findtext("szPortalName", default="").strip()
                        objNameStr =  portalRow.findtext("szObjName", default="").strip()
                        portalTypeStr = portalRow.findtext("cRefType", default="").strip()
                                                    
                        if portalNameStr == portalNameStr_ and portalTypeStr == portalTypeStr_ and objNameStr == objectValue2_:
                            descrStr = portalRow.findtext("szDescr", default="").strip() 
                            labelNameStr = portalRow.findtext("szLabelName", default="").strip()

                            urlStr = ""
                            urlNode = portalRow.find(".//pszURLLogical/rowset[@name='char']")
                            if urlNode is not None:
                                for urlRow in urlNode.findall("row"):
                                    urlStr = urlRow.findtext("pszURLLogical", default="").strip()

                            if portalTypeStr_ == "C":
                                portalStr = "Content Reference"
                            elif portalTypeStr_ == "F":
                                portalStr = "Folder"

                            portalDefnObj = PortalDefinition(
                                name = portalNameStr_,
                                object_name = objNameStr,
                                portal_type = portalStr,
                                label = labelNameStr,
                                url = urlStr,
                                description = descrStr
                            )

                            return portalDefnObj
        return None

    def _describeItems(self, objectTypeNode_, objectValue0_, objectValue1_, objectValue2_, objectValue3_, objectValue4_, rootNode_):

        """
        Parsea el archivo XML exportado desde PeopleSoft Application Designer
        y retorna una estructura de datos normalizada con todas las definiciones
        del proyecto
        """

        match objectTypeNode_:
            case "0":
                # Record Definition and its fields
                resultObj = self._getRecordDefinition(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.records.append(resultObj)                
            case "2":
                # Field Definition.
                # ObjectValue1 empty means it's the default definition of the field.
                if objectValue1_ == "":
                    resultObj = self._getFieldDefinition(objectValue0_, rootNode_)
                    if resultObj is not None:
                        self.fields.append(resultObj)
            case "4":
                print(f"📄 Xlat of {objectValue0_} handled in Field Definition")
            case "5":
                # Page Defition
                resultObj = self._getPageDefinition(objectValue0_, rootNode_)       
                if resultObj is not None:
                    self.pages.append(resultObj)
            case "6":
                # Menu
                resultObj = self._getMenuDefinition(objectValue0_, rootNode_)       
                if resultObj is not None:
                    self.menus.append(resultObj)
            case "7":
                # Component
                resultObj = self._getComponentDefinition(objectValue0_, objectValue1_, rootNode_)
                if resultObj is not None:
                    self.components.append(resultObj)
            case "8":
                # Record PeopleCode
                resultObj = self._getEventPeopleCode(objectValue0_, objectValue1_, objectValue2_, objectValue3_, "", "REC", rootNode_)
                if resultObj is not None:
                    self.peoplecode.append(resultObj)
            case "10":                    
                # PS Query
                resultObj = self._getQueryDefinition(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.queries.append(resultObj)
            case "19":
                # Role Definition
                resultObj = self._getRoleDefinition(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.roles.append(resultObj)
            case "20":
                # Process Definition
                resultObj = self._getProcessDefinition(objectValue0_, objectValue1_, rootNode_)
                if resultObj is not None:
                    self.processes.append(resultObj)
            case "23":
                # Job Definition
                resultObj = self._getJobDefinition(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.jobs.append(resultObj)             
            case "25":
                # Message Catalog
                resultObj = self._getMsgCatalog(objectValue0_, objectValue1_, rootNode_)
                if resultObj is not None:
                    self.msg_catalog.append(resultObj)                 
            case "29":
                print(f"📄 Application Package: {objectValue0_}")
            case "30":
                # SQL Object
                if objectValue1_ == "0":
                    resultObj = self._getSQLDefinition(objectValue0_, objectValue1_, rootNode_)
                    if resultObj is not None:
                        self.sql_objects.append(resultObj)
            case "31":
                # File Layout
                resultObj = self._getFileLayout(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.file_layouts.append(resultObj)
            case "32":
                # Component Interface
                resultObj = self._getComponentInterface(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.component_interfaces.append(resultObj)
            case "33":
                # Application Engine
                resultObj = self._getAppEngine(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.app_engines.append(resultObj)
            case "34":
                print(f"📄 Application Engine Section: {objectValue0_} handled in Application Engine Defintion")
            case "37":
                resultObj = self._getMessage(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.messages.append(resultObj)                
            case "43":
                print(f"📄 Application Engine Step: {objectValue0_} handled in Application Engine Defintion")
            case "40":
                print(f"📄 Service Operation: {objectValue0_}")
            case "44":
                # Page PeopleCode
                resultObj = self._getEventPeopleCode(objectValue0_, objectValue1_, objectValue2_, objectValue3_, "", "PG", rootNode_)
                if resultObj is not None:
                    self.peoplecode.append(resultObj)
            case "46":
                # Component PeopleCode
                resultObj = self._getEventPeopleCode(objectValue0_, objectValue1_, objectValue2_, objectValue3_, "", "CMP", rootNode_)
                if resultObj is not None:
                    self.peoplecode.append(resultObj)
            case "47":
                # Component Record PeopleCode                
                resultObj = self._getEventPeopleCode(objectValue0_, objectValue1_, objectValue2_, objectValue3_, "", "CR", rootNode_)
                if resultObj is not None:
                    self.peoplecode.append(resultObj)                    
            case "48":
                # Component Record Field PeopleCode
                objectValue3Str_, objectValue4Str_ = objectValue3_.split()
                resultObj = self._getEventPeopleCode(objectValue0_, objectValue1_, objectValue2_, objectValue3Str_, objectValue4Str_, "CRF", rootNode_)
                if resultObj is not None:
                    self.peoplecode.append(resultObj)
            case "53":
                resultObj = self._getPermissionList(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.permission_lists.append(resultObj)
            case "54":
                print(f"📄 Activity Guide?: {objectValue0_}")
            case "55":
                resultObj = self._getPortalDefinition(objectValue0_, objectValue1_, objectValue2_, rootNode_)
                if resultObj is not None:
                    self.portals.append(resultObj)
            case "58":
                # print(f"Application Package PeopleCode: {objectValue0_} {objectValue1_} {objectValue2_} {objectValue3_}")
                if objectValue3_ =="":
                    resultObj = self._getAppPackagePeopleCode(objectValue0_, objectValue1_, objectValue2_, "OnExecute", rootNode_)
                    if resultObj is not None:
                        self.ap_peoplecode.append(resultObj)
                elif objectValue3_ != "":
                    resultObj = self._getAppPackagePeopleCode(objectValue0_, objectValue1_, objectValue2_, objectValue3_, rootNode_)
                    if resultObj is not None:
                        self.ap_peoplecode.append(resultObj)
            case "66":
                print(f"📄 Style Sheet: {objectValue0_}")
            case "80":
                # Service Operation
                resultObj = self._getServiceOpDef(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.service_operations.append(resultObj)
            case "86":
                resultObj = self._getBIReportDefinition(objectValue0_, rootNode_)
                if resultObj is not None:
                    self.bi_reports.append(resultObj)
            case "92":
                print(f"Documentos: {objectValue0_} {objectValue1_}  {objectValue2_}")
                resultObj = self._getDocumentDefinition(objectValue0_, objectValue1_, objectValue2_, rootNode_)
                if resultObj is not None:
                    self.documents.append(resultObj)
            case "116":
                print(f"📄 Integration Broker: {objectValue0_}")
            case _:
                print(f"📄 Unhandled object type: {objectTypeNode_} {objectValue0_}")


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
                projectDescrLong = instance.find(".//rowset[@name='PjmDefn']/row/hDescrLong/rowset[@name='char']/row/hDescrLong")

                projectObj.description = projectDescrStr.text.strip() if projectDescrStr is not None and projectDescrStr.text else ""
                projectObj.longdescription = projectDescrLong.text.strip() if projectDescrLong is not None and projectDescrLong.text else ""

                for lpPit in instance.iter("lpPit"):
                    
                    if lpPit is None:
                        print("⚠️  lpPit node not found in XML.")
                        continue

                    pjmPitNode = lpPit.find(".//rowset[@name='PjmPit']")

                    if pjmPitNode is not None:
                        print(f"Total rows: {pjmPitNode.get('count')}")
                        
                        for row in pjmPitNode.findall("row"):
                            objectTypeNode = row.findtext("eObjectType", default="").strip()
                            objectValue0 = row.findtext("szObjectValue_0", default="").strip()
                            objectValue1 = row.findtext("szObjectValue_1", default="").strip()
                            objectValue2 = row.findtext("szObjectValue_2", default="").strip()
                            objectValue3 = row.findtext("szObjectValue_3", default="").strip()
                            objectValue4 = ""

                            projectObj._describeItems(objectTypeNode, objectValue0, objectValue1, objectValue2, objectValue3, objectValue4, root)

                    return projectObj
            else:
                print("⚠️  Project name not found in XML.")
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
            raise ValueError("Couldn't extract project name from XML.")
        
        return project
