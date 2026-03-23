# Proyecto PeopleSoft: IIC_CHG0075241

Concur fix email

## Resumen del Proyecto

| Tipo de Objeto | Cantidad |
|----------------|----------|
| Records | 17 |
| Fields | 3 |
| Pages | 3 |
| App Package PeopleCode | 1 |
| SQL Objects | 23 |
| Process Definitions | 1 |

---
## Records

### IIC_CNCRVRF_AET

**Tipo:** Derived/Work  
**Descripción:** IIC_CNCR_VRF aet  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE | 2 | 10 | — |  |
| PRCSNAME | 0 | 12 | — |  |
| BATCHID | 0 | 13 | — |  |
| SEQUENCENUMBER | 0 | 13 | — |  |
| CT_EMPLOYEE_EMP_ID | 0 | 48 | — |  |
| CT_E_ORG_UNIT2 | 0 | 48 | — |  |
| CT_REPORT_RPT_KEY | 0 | 48 | — |  |
| CT_ALL_CUSTOM1 | 0 | 48 | — |  |
| CT_ALL_CUSTOM2 | 0 | 48 | — |  |
| CT_ALL_CUSTOM3 | 0 | 48 | — |  |
| FUNCLIB | 0 | 1 | — |  |
| ERROR_FLAG | 0 | 1 | — |  |

### IIC_CNCR_AET

**Tipo:** Derived/Work  
**Descripción:** Concur Aet  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE | 2 | 10 | — |  |
| EMAIL_FROM | 0 | 254 | — |  |
| EMAIL_SUBJECT | 0 | 30 | — |  |
| IIC_EMAIL_TEXT | 0 | 250 | — |  |
| PRCSNAME | 0 | 12 | — |  |
| SETID | 0 | 5 | — |  |
| DEPTID | 0 | 10 | — |  |
| ERROR_FLAG | 0 | 1 | — |  |
| IIC_CNCR_DELAY | 2 | 2 | — |  |

### IIC_CNCR_DTL

**Tipo:** Table  
**Descripción:** Concur line validation  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE2 | 2 | 10 | — |  |
| IIC_INTERFACE_ID | 0 | 30 | — |  |
| BATCHID | 0 | 13 | — |  |
| SEQUENCENUMBER | 0 | 13 | — |  |
| BATCHDATE | 0 | 10 | — |  |
| PRCSNAME | 0 | 12 | — |  |
| CT_EMPLOYEE_EMP_ID | 0 | 48 | — |  |
| CT_E_ORG_UNIT2 | 0 | 48 | — |  |
| CT_REPORT_RPT_KEY | 0 | 48 | — |  |
| CT_C_ALPHA_CODE | 0 | 3 | — |  |
| CT_E_TYPE_LANG_NAM | 0 | 64 | — |  |
| CT_P_CODE_LANG_PAT | 0 | 4 | — |  |
| CT_JOURNAL_AMOUNT | 0 | 23 | — |  |
| CT_ALL_CUSTOM1 | 0 | 48 | — |  |
| CT_ALL_CUSTOM2 | 0 | 48 | — |  |
| CT_ALL_CUSTOM3 | 0 | 48 | — |  |
| CT_TR_REQUESTID | 0 | 20 | — |  |
| IIC_CNCR_L_STATUS | 0 | 1 | — |  |

### IIC_CNCR_HDR

**Tipo:** Table  
**Descripción:** Concur Header  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE2 | 2 | 10 | — |  |
| PROCESS_INSTANCE | 2 | 10 | — |  |
| IIC_INTERFACE_ID | 0 | 30 | — |  |
| PRCSNAME | 0 | 12 | — |  |
| DTTM_IMPORTED | 6 | 26 | — |  |
| BATCHID | 0 | 13 | — |  |
| TOTAL_ROWS | 2 | 6 | — |  |
| TOTAL_LINES | 2 | 4 | — |  |
| TOTAL_AMT | 3 | 28 | — |  |
| IIC_CNCR_L_STATUS | 0 | 1 | — |  |

### IIC_CNCR_RB_AET

**Tipo:** Derived/Work  
**Descripción:** Concur Rollback AET  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE | 2 | 10 | — |  |
| BATCHID | 0 | 13 | — |  |
| PROCESS_INSTANCE2 | 2 | 10 | — |  |
| OPRID | 0 | 30 | — |  |
| COUNT_1 | 2 | 3 | — |  |
| COUNT_2 | 2 | 3 | — |  |
| COUNT_3 | 2 | 3 | — |  |

### IIC_CNCR_RB_RUN

**Tipo:** Table  
**Descripción:** Concur Rollback RunCntl  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| OPRID | 0 | 30 | — |  |
| RUN_CNTL_ID | 0 | 30 | — |  |
| BATCHID | 0 | 13 | — |  |
| PROCESS_INSTANCE2 | 2 | 10 | — |  |

### IIC_CNCR_REC_VW

**Tipo:** View  
**Descripción:** Concur reconciled information  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE2 | 2 | 10 | — |  |
| BATCHID | 0 | 13 | — |  |
| BATCHDATE | 0 | 10 | — |  |
| CT_EMPLOYEE_EMP_ID | 0 | 48 | — |  |
| NAME | 0 | 50 | — |  |
| CT_E_ORG_UNIT1 | 0 | 48 | — |  |
| CT_E_ORG_UNIT2 | 0 | 48 | — |  |
| CT_REPORT_RPT_KEY | 0 | 48 | — |  |
| CT_TR_REQUESTID | 0 | 20 | — |  |
| CT_C_ALPHA_CODE | 0 | 3 | — |  |
| AMOUNT1 | 3 | 27 | — |  |
| CT_ALL_CUSTOM1 | 0 | 48 | — |  |
| CT_ALL_CUSTOM2 | 0 | 48 | — |  |
| CT_ALL_CUSTOM3 | 0 | 48 | — |  |
| DESCR_LBL | 0 | 1 | — |  |
| PROCESS_INSTANCE | 2 | 10 | — |  |
| VOUCHER_ID | 0 | 8 | — |  |
| GROSS_AMT | 3 | 28 | — |  |
| ENTRY_STATUS | 0 | 1 | — |  |
| DESCRSHORT | 0 | 10 | — |  |
| PYMNT_SELCT_STATUS | 0 | 1 | — |  |
| DESCRSHORT2 | 0 | 10 | — |  |
| APPR_STATUS | 0 | 1 | — |  |
| DESCRSHORT3 | 0 | 10 | — |  |

### IIC_CNCR_SETUP

**Tipo:** Table  
**Descripción:** Concur setup  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PRCSTYPE | 0 | 30 | — |  |
| PRCSNAME | 0 | 12 | — |  |
| SETID | 0 | 5 | — |  |
| EMAIL_FROM | 0 | 254 | — |  |
| EMAIL_SUBJECT | 0 | 30 | — |  |
| IIC_EMAIL_TEXT | 0 | 250 | — |  |
| DEPTID | 0 | 10 | — |  |
| OPRID | 0 | 30 | — |  |
| LASTUPDDTTM | 6 | 26 | — |  |
| IIC_CNCR_DELAY | 2 | 2 | — |  |

### IIC_CNCR_TMP

**Tipo:** Table  
**Descripción:** Concur Temp Record  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE | 2 | 10 | — |  |
| CONSTANT | 0 | 6 | — |  |
| BATCHID | 0 | 13 | — |  |
| BATCHDATE | 0 | 10 | — |  |
| SEQUENCENUMBER | 0 | 13 | — |  |
| CT_EMPLOYEE_EMP_ID | 0 | 48 | — |  |
| CT_EMPLOYEE_LAST_N | 0 | 32 | — |  |
| CT_EMPLOYEE_FIRST | 0 | 32 | — |  |
| CT_EMPLOYEE_MI | 0 | 1 | — |  |
| CT_E_CUSTOM21 | 0 | 48 | — |  |
| CT_E_ORG_UNIT1 | 0 | 48 | — |  |
| CT_E_ORG_UNIT2 | 0 | 48 | — |  |
| CT_E_ORG_UNIT3 | 0 | 48 | — |  |
| CT_E_ORG_UNIT4 | 0 | 48 | — |  |
| CT_E_ORG_UNIT5 | 0 | 48 | — |  |
| CT_E_ORG_UNIT6 | 0 | 48 | — |  |
| CT_E_BANK_ACCO_NUM | 0 | 15 | — |  |
| CT_E_BANK_ACCO_ROU | 0 | 48 | — |  |
| NA18 | 0 | 48 | — |  |
| CT_R_REPORT_ID | 0 | 32 | — |  |
| CT_REPORT_RPT_KEY | 0 | 48 | — |  |
| CT_LEDGER_LEDGER_C | 0 | 20 | — |  |
| CT_C_ALPHA_CODE | 0 | 3 | — |  |
| CT_C_LANG_NAME | 0 | 64 | — |  |
| CT_R_SUBMIT_DATE | 0 | 10 | — |  |
| CT_R_USER_DEF_DATE | 0 | 10 | — |  |
| CT_R_PROCESS_DATE | 0 | 10 | — |  |
| CT_REPORT_NAME | 0 | 40 | — |  |
| CT_R_IMAGE_REQ | 0 | 1 | — |  |
| CT_R_HAS_VAT_ENTRY | 0 | 1 | — |  |
| CT_R_HAS_TA_ENTRY | 0 | 1 | — |  |
| TOTAL_POSTED_AMOUN | 0 | 23 | — |  |
| TOTAL_APP_AMOUNT | 2 | 32 | — |  |
| CT_POLICY_LANG_NAM | 0 | 64 | — |  |
| NA34 | 0 | 48 | — |  |
| CT_R_ORG_UNIT1 | 0 | 48 | — |  |
| CT_R_ORG_UNIT2 | 0 | 48 | — |  |
| CT_R_ORG_UNIT3 | 0 | 48 | — |  |
| CT_R_ORG_UNIT4 | 0 | 48 | — |  |
| CT_R_ORG_UNIT5 | 0 | 48 | — |  |
| CT_R_ORG_UNIT6 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM1 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM2 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM3 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM4 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM5 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM6 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM7 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM8 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM9 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM10 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM11 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM12 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM13 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM14 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM15 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM16 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM17 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM18 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM19 | 0 | 48 | — |  |
| CT_REPORT_CUSTOM20 | 0 | 48 | — |  |
| CT_REPORT_RPE_KEY | 0 | 13 | — |  |
| CT_R_ENTRY_TRANS_T | 0 | 3 | — |  |
| CT_E_TYPE_LANG_NAM | 0 | 64 | — |  |
| CT_R_ENTRY_TRANS_D | 0 | 10 | — |  |
| CT_C_ALPHA_CODE1 | 0 | 3 | — |  |
| CT_R_ENTRY_EXCH_RA | 0 | 23 | — |  |
| EXCHANGE_RATE_DIRE | 0 | 1 | — |  |
| REPORT_E_IS_PERSON | 0 | 1 | — |  |
| CT_R_ENTRY_DESCRIP | 0 | 64 | — |  |
| CT_LIST_IT_LANG_VA | 0 | 64 | — |  |
| CT_R_ENTRY_VENDOR | 0 | 64 | — |  |
| CT_R_ENTRY_RECEIPR | 0 | 1 | — |  |
| CT_R_ENTRY_RECEIPT | 0 | 1 | — |  |
| TOTAL_EMPLOYEE_ATT | 0 | 23 | — |  |
| TOTAL_SPOUSE_ATTEN | 0 | 23 | — |  |
| TOTAL_BUSINESS_ATT | 0 | 23 | — |  |
| CT_R_ENTRY_ORUNIT1 | 0 | 48 | — |  |
| CT_R_ENTRY_ORUNIT2 | 0 | 48 | — |  |
| CT_R_ENTRY_ORUNIT3 | 0 | 48 | — |  |
| CT_R_ENTRY_ORUNIT4 | 0 | 48 | — |  |
| CT_R_ENTRY_ORUNIT5 | 0 | 48 | — |  |
| CT_R_ENTRY_ORUNIT6 | 0 | 48 | — |  |
| CT_R_ENTRY_CUSTOM1 | 0 | 48 | — |  |
| CT_R_ENTRY_CUSTOM2 | 0 | 48 | — |  |
| CT_R_ENTRY_CUSTOM3 | 0 | 48 | — |  |
| CT_R_ENTRY_CUSTOM4 | 0 | 48 | — |  |
| CT_R_ENTRY_CUSTOM5 | 0 | 48 | — |  |
| CT_R_ENTRY_CUSTOM6 | 0 | 48 | — |  |
| CT_R_ENTRY_CUSTOM7 | 0 | 48 | — |  |
| CT_R_ENTRY_CUSTOM8 | 0 | 48 | — |  |
| CT_R_ENTRY_CUSTOM9 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM10 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM11 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM12 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM13 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM14 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM15 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM16 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM17 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM18 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM19 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM20 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM21 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM22 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM23 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM24 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM25 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM26 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM27 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM28 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM29 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM30 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM31 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM32 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM33 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM34 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM35 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM36 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM37 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM38 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM39 | 0 | 48 | — |  |
| CT_R_ENTY_CUSTOM40 | 0 | 48 | — |  |
| CT_R_ENTRY_TANS_AM | 0 | 23 | — |  |
| CT_R_ENTRY_POS_AMO | 0 | 23 | — |  |
| CT_R_ENTRY_AP_AM | 0 | 23 | — |  |
| CT_P_CODE_LANG_PAT | 0 | 4 | — |  |
| CT_P_CODE_LANG_NAM | 0 | 80 | — |  |
| VIRTUAL_PMT_REIMBT | 0 | 1 | — |  |
| CT_CC_TRANS_BILL | 0 | 36 | — |  |
| CT_CC_ACC_NUMBER | 1 | 255 | — |  |
| CT_CC_ACC_NAME | 1 | 255 | — |  |
| CT_CC_TRANSACT_JRK | 0 | 13 | — |  |
| CT_CC_TRANS_REF_NO | 0 | 64 | — |  |
| CT_CC_TRANSACT_KEY | 0 | 13 | — |  |
| CT_CC_TRANSACT_TYP | 0 | 3 | — |  |
| CT_CC_TRANSACT_ID | 0 | 32 | — |  |
| CT_CC_TRANS_AMOUNT | 0 | 23 | — |  |
| CT_CC_TRA_TAX_AM | 0 | 23 | — |  |
| CT_CC_TRA_CUR | 0 | 3 | — |  |
| CT_CC_TRA_POS_AM | 0 | 23 | — |  |
| CT_CC_TRA_POS_CU | 0 | 3 | — |  |
| CT_CC_TRANS_DATE | 0 | 10 | — |  |
| CT_CC_TRA_POS_D | 0 | 10 | — |  |
| CT_CC_TRA_DESC | 0 | 42 | — |  |
| CT_CC_TRA_MC_CO | 0 | 5 | — |  |
| CT_CC_TRA_MER_NA | 0 | 50 | — |  |
| CT_CC_TRA_MER_CI | 0 | 40 | — |  |
| CT_CC_TRA_MER_ST | 0 | 32 | — |  |
| CT_CC_TRA_MER_CT | 0 | 2 | — |  |
| CT_CC_TRA_MER_RE | 0 | 15 | — |  |
| CT_CC_TRA_BIL_TY | 0 | 2 | — |  |
| CT_CC_TRA_BIL_EM | 0 | 6 | — |  |
| CT_JRNL_BILLING_AM | 0 | 23 | — |  |
| CT_CC_ACC_NUMBER1 | 1 | 255 | — |  |
| CT_CC_ACC_NAME_CA | 1 | 255 | — |  |
| CT_CC_ACC_BUSIN_AS | 0 | 64 | — |  |
| CT_CC_TRA_ACQ_REF | 0 | 50 | — |  |
| CT_LOC_NAME_CTRYCO | 0 | 2 | — |  |
| CT_LOC_NAME_CODE | 0 | 6 | — |  |
| CT_R_ENTRY_FO_DOME | 0 | 4 | — |  |
| CT_CC_ACC_PROV_MAR | 1 | 255 | — |  |
| CT_CC_TRA_PROC | 0 | 64 | — |  |
| CT_P_TYPE_LANG_NAM | 0 | 64 | — |  |
| CT_P_CODE_LANG_NA1 | 0 | 80 | — |  |
| CT_P_TYPE_LANG_NA1 | 0 | 64 | — |  |
| CT_P_CODE_LANG_NA2 | 0 | 80 | — |  |
| CT_JRNL_ACC_CODE | 0 | 48 | — |  |
| CT_JRNL_DEBIT_CR | 0 | 2 | — |  |
| CT_JOURNAL_AMOUNT | 0 | 23 | — |  |
| CT_JOURNAL_RPJ_KEY | 0 | 48 | — |  |
| CT_CAR_LOG_E_B_DIS | 0 | 13 | — |  |
| CT_CAR_LOG_E_P_DIS | 0 | 13 | — |  |
| CT_CAR_LOG_E_PAS_C | 0 | 13 | — |  |
| CT_CAR_VEHICLE_ID | 0 | 30 | — |  |
| NA175 | 0 | 48 | — |  |
| NA176 | 0 | 48 | — |  |
| CT_CASH_ADV_REQ_AM | 0 | 23 | — |  |
| CT_C_ALPHA_CODE2 | 0 | 3 | — |  |
| CT_CURRENCY_NUM_CO | 0 | 3 | — |  |
| CT_CASH_ADV_EX_RAT | 0 | 23 | — |  |
| CT_C_ALPHA_CODE3 | 0 | 3 | — |  |
| CT_C_NUM_CODE1 | 0 | 3 | — |  |
| CT_CASH_ADV_ISS_DA | 0 | 10 | — |  |
| CT_P_CODE_LAN_NA3 | 0 | 80 | — |  |
| CT_CASH_ADVANCE | 0 | 1 | — |  |
| CT_CASH_ADVE_REQDA | 0 | 10 | — |  |
| CT_CASH_ADV_CA_KEY | 0 | 13 | — |  |
| NA188 | 0 | 48 | — |  |
| CT_ALLO_ALLOC_KEY | 0 | 13 | — |  |
| CT_ALL_PERCENTAGE | 0 | 11 | — |  |
| CT_ALL_CUSTOM1 | 0 | 48 | — |  |
| CT_ALL_CUSTOM2 | 0 | 48 | — |  |
| CT_ALL_CUSTOM3 | 0 | 48 | — |  |
| CT_ALL_CUSTOM4 | 0 | 48 | — |  |
| CT_ALL_CUSTOM5 | 0 | 48 | — |  |
| CT_ALL_CUSTOM6 | 0 | 48 | — |  |
| CT_ALL_CUSTOM7 | 0 | 48 | — |  |
| CT_ALL_CUSTOM8 | 0 | 48 | — |  |
| CT_ALL_CUSTOM9 | 0 | 48 | — |  |
| CT_ALL_CUSTOM10 | 0 | 48 | — |  |
| CT_ALL_CUSTOM11 | 0 | 48 | — |  |
| CT_ALL_CUSTOM12 | 0 | 48 | — |  |
| CT_ALL_CUSTOM13 | 0 | 48 | — |  |
| CT_ALL_CUSTOM14 | 0 | 48 | — |  |
| CT_ALL_CUSTOM15 | 0 | 48 | — |  |
| CT_ALL_CUSTOM16 | 0 | 48 | — |  |
| CT_ALL_CUSTOM17 | 0 | 48 | — |  |
| CT_ALL_CUSTOM18 | 0 | 48 | — |  |
| CT_ALL_CUSTOM19 | 0 | 1 | — |  |
| CT_ALL_CUSTOM20 | 0 | 48 | — |  |
| NA211 | 0 | 48 | — |  |
| CT_TA_R_MEAL_LODG | 0 | 1 | — |  |
| CT_TA_R_DISPLAY_LI | 0 | 23 | — |  |
| CT_TA_R_ALLOW_LIMI | 0 | 23 | — |  |
| CT_TA_R_ALLOW_THRE | 0 | 23 | — |  |
| CT_TA_FIXMEAL_LODG | 0 | 1 | — |  |
| CT_TA_FIX_BASE_AMO | 0 | 23 | — |  |
| CT_TA_FIX_ALL_AMOU | 0 | 23 | — |  |
| CT_TA_FIX_OVERNIGH | 0 | 1 | — |  |
| CT_TA_FIX_BRKF_PRO | 0 | 3 | — |  |
| CT_TA_FIX_LUNCH_PR | 0 | 3 | — |  |
| CT_TA_FIX_DIN_PROV | 0 | 3 | — |  |
| NA223 | 0 | 48 | — |  |
| NA224 | 0 | 48 | — |  |
| CT_TAX_AU_LANG_TAX | 0 | 50 | — |  |
| CT_TAXAU_LAN_LABEL | 0 | 5 | — |  |
| CT_RE_TAX_TRANS_AM | 0 | 23 | — |  |
| CT_RE_TAX_POSAM | 0 | 23 | — |  |
| CT_RE_TAX_SOURCE | 0 | 4 | — |  |
| CT_RE_TAX_REC_TRAN | 0 | 23 | — |  |
| CT_RE_TAX_POS_AM1 | 0 | 23 | — |  |
| CT_RE_TAX_CODE | 0 | 20 | — |  |
| CT_TAX_C_RECL_DOME | 0 | 1 | — |  |
| CT_RE_TA_TAXADJ_AM | 0 | 23 | — |  |
| CT_RE_TA_REC_ADJ_A | 0 | 23 | — |  |
| CT_RE_TA_REC_CODE | 0 | 20 | — |  |
| CT_RE_TA_REC_TR_AD | 0 | 23 | — |  |
| CT_RE_TA_ALL_REC_C | 0 | 20 | — |  |
| CT_TR_REQUESTID | 0 | 20 | — |  |
| CT_TR_REQUEST_TRNA | 0 | 40 | — |  |
| CT_TR_REQ_TOTALPOS | 0 | 23 | — |  |
| CT_TR_REQ_TOTAL_AP | 0 | 23 | — |  |
| CT_TR_REQ_START_DA | 0 | 10 | — |  |
| CT_TR_REQ_END_DATE | 0 | 10 | — |  |
| CT_TRAVEL_REQUEST | 0 | 10 | — |  |
| CT_RE_TOTAL_TAX_PO | 0 | 23 | — |  |
| CT_RE_VIEW_NET_TAX | 0 | 23 | — |  |
| CT_RE_TOTAL_REC_AD | 0 | 23 | — |  |
| CT_RE_VIEW_REC_ADJ | 0 | 23 | — |  |
| CT_P_TYPE_LANG | 0 | 64 | — |  |
| NA251 | 0 | 48 | — |  |
| NA252 | 0 | 48 | — |  |
| NA253 | 0 | 48 | — |  |
| CT_EFTPAY_ACC_CASH | 0 | 48 | — |  |
| CT_EFT_PAY_ACC_LIA | 0 | 48 | — |  |
| NA256 | 0 | 48 | — |  |
| C_FLAG | 0 | 1 | — |  |
| C_FLAG1 | 0 | 1 | — |  |
| BUSINESS_UNIT | 0 | 5 | — |  |
| VOUCHER_ID | 0 | 8 | — |  |
| PROCESS_INSTANCE2 | 2 | 10 | — |  |

### IIC_CNDTL_TAO

**Tipo:** Unknown (7)  
**Descripción:** Concur line validation  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE | 2 | 10 | — |  |
| BATCHID | 0 | 13 | — |  |
| SEQUENCENUMBER | 0 | 13 | — |  |
| BATCHDATE | 0 | 10 | — |  |
| CT_EMPLOYEE_EMP_ID | 0 | 48 | — |  |
| CT_E_ORG_UNIT2 | 0 | 48 | — |  |
| CT_REPORT_RPT_KEY | 0 | 48 | — |  |
| CT_C_ALPHA_CODE | 0 | 3 | — |  |
| CT_E_TYPE_LANG_NAM | 0 | 64 | — |  |
| CT_P_CODE_LANG_PAT | 0 | 4 | — |  |
| CT_JOURNAL_AMOUNT | 0 | 23 | — |  |
| CT_ALL_CUSTOM1 | 0 | 48 | — |  |
| CT_ALL_CUSTOM2 | 0 | 48 | — |  |
| CT_ALL_CUSTOM3 | 0 | 48 | — |  |
| CT_TR_REQUESTID | 0 | 20 | — |  |

### IIC_CNHDR_TAO

**Tipo:** Unknown (7)  
**Descripción:** Concur Header validation  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE | 2 | 10 | — |  |
| DTTM_IMPORTED | 6 | 26 | — |  |
| BATCHID | 0 | 13 | — |  |
| TOTAL_ROWS | 2 | 6 | — |  |
| TOTAL_LINES | 2 | 4 | — |  |
| TOTAL_AMT | 3 | 28 | — |  |

### IIC_FUNCLIB_AP

**Tipo:** Derived/Work  
**Descripción:** AP Custom functions  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| FUNCLIB | 0 | 1 | — |  |
| FUNCLIB_01 | 0 | 1 | — |  |

### IIC_INTFCERR_VW

**Tipo:** View  
**Descripción:** Interface Errors  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE | 2 | 10 | — |  |
| PRCSNAME | 0 | 12 | — |  |
| BATCHID | 0 | 13 | — |  |
| IIC_INTERFACE_ID | 0 | 30 | — |  |
| ERROR_TYPE_1 | 0 | 3 | — |  |
| ERROR_MESSAGE_TXT | 1 | 256 | — |  |

### IIC_INTFC_ERR

**Tipo:** Table  
**Descripción:** Interface Errors  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE | 2 | 10 | — |  |
| PRCSNAME | 0 | 12 | — |  |
| SEQUENCENUMBER | 0 | 13 | — |  |
| BATCHID | 0 | 13 | — |  |
| IIC_INTERFACE_ID | 0 | 30 | — |  |
| ERROR_TYPE_1 | 0 | 3 | — |  |
| ERROR_MESSAGE_TXT | 1 | 256 | — |  |

### IIC_INTFERR_WRK

**Tipo:** Derived/Work  
**Descripción:** Interface Errors Wrk  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| BATCHID | 0 | 13 | — |  |
| PROCESS_INSTANCE | 2 | 10 | — |  |
| PROCESS_INSTANCE2 | 2 | 10 | — |  |
| SEARCH_BTN | 0 | 1 | — |  |
| REVERT_BUTTON | 0 | 1 | — |  |
| IIC_INTERFACE_ID | 0 | 30 | — |  |
| GROUPBOX1 | 0 | 1 | — |  |
| GROUPBOX2 | 0 | 1 | — |  |

### IIC_INTFPRC2_VW

**Tipo:** View  
**Descripción:** Interface ID Prompt  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE2 | 2 | 10 | — |  |
| PRCSNAME | 0 | 12 | — |  |
| IIC_INTERFACE_ID | 0 | 30 | — |  |

### IIC_INTFPRC_VW

**Tipo:** View  
**Descripción:** Interface ID prompt  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE | 2 | 10 | — |  |
| PRCSNAME | 0 | 12 | — |  |
| IIC_INTERFACE_ID | 0 | 30 | — |  |

---
## Fields

### IIC_CNCR_DELAY

**Tipo:** Number  
**Longitud:** 2  

### IIC_CNCR_L_STATUS

**Tipo:** Character  
**Longitud:** 1  

### IIC_INTERFACE_ID

**Tipo:** Character  
**Longitud:** 30  

---
## Pages

### IIC_CNCR_RECON_PG

**Tipo:** Standard  
**Descripción:** Concur Reconcile Page  
### IIC_CNCR_SETUP_PG

**Tipo:** Standard  
**Descripción:** Setup Concur  
### IIC_INTFC_ERR_PG

**Tipo:** Standard  
**Descripción:** Interface errors  
---
## SQL Objects

### IIC_CNCR_ERR_GET_SQL

**Descripción:** Get Line Error  

```sql
SELECT ERROR_MESSAGE_TXT   FROM %Table(IIC_INTFC_ERR) a   , %Table(iic_cncr_dtl) b   WHERE a.process_instance = :1   AND a.error_type_1 = 'DTL'   AND a.batchid = :2   AND a.batchid = b.batchid   AND b.ct_report_rpt_key = :3   AND b.iic_cncr_l_status = 'E'   AND a.sequencenumber = b.sequencenumber   AND a.process_instance = b.process_instance2   AND b.ct_all_custom1 = :4   AND b.ct_all_custom2 = :5   AND b.ct_all_custom3 = :6
```

### IIC_CNCR_JOBINST_GET_SQL

**Descripción:** Get Concur Job Inst  

```sql
SELECT MAINJOBINSTANCE  FROM PSPRCSRQST   WHERE PRCSJOBNAME = 'IICLDCNC'   AND prcsinstance = :1
```

### IIC_CNCR_PRCINST_GET_SQL

**Descripción:** Get Concur Max Proc Inst  

```sql
SELECT MAX(PR.PRCSINSTANCE)   FROM %Table(PSPRCSRQST) PR   WHERE PR.PRCSNAME IN ('IIC_CNCR_UPL','IIC_CNCR_UP2')   AND PR.PRCSINSTANCE < :1
```

### IIC_CNCR_RB_RUNNING_SQL

**Descripción:** Is Concur rollback running?  

```sql
SELECT 'Y'   FROM PSPRCSRQST   WHERE prcsname = 'IIC_CNCR_RB'   AND RUNCNTLID = 'CONCUR_ROLLBACK'   AND RUNSTATUS IN ('16','18','19','4','5','6','7','10')
```

### IIC_CNCR_UP_INST_GET_SQL

**Descripción:** Get Concur PI  

```sql
SELECT MAX(PRCSINSTANCE)   FROM PSPRCSRQST   WHERE prcsname IN ('IIC_CNCR_UP2','IIC_CNCR_UPL')   HAVING MAX(prcsinstance) < :1
```

### IIC_CNCR_VCHRAPRV_INST_SQL

**Descripción:** Get Voucher Apprvl Inst  

```sql
SELECT PRCSINSTANCE   FROM PSPRCSRQST   WHERE PRCSJOBNAME = 'IICLDCNC'   AND PRCSNAME = 'VCHR_APRV_AF'   AND JOBINSTANCE = :1
```

### IIC_CNCR_VCHRBLD_INST_SQL

**Descripción:** Get Voucher Build Inst  

```sql
SELECT PRCSINSTANCE FROM PSPRCSRQST   WHERE PRCSJOBNAME = 'IICLDCNC'   AND PRCSNAME = 'AP_VCHRBLD'  AND JOBINSTANCE = :1
```

### IIC_CNCR_VCHR_LNE_GET_SQL

**Descripción:** Count Concur line errors  

```sql
SELECT %Coalesce(VX.VENDOR_ID,' ')   , C.ct_employee_last_n %Concat ', ' %Concat C.ct_employee_first AS name_display   , c.ct_tr_requestid   , a.batchdate   , SUM (CAST (a.ct_journal_amount AS DECIMAL (23, 3))) AS ct_journal_amount   , b.ERROR_MESSAGE_TXT   FROM %Table(IIC_CNCR_DTL) A LEFT OUTER JOIN %Table(VENDOR) VX ON A.ct_employee_emp_id= VX.VNDR_FIELD_C30_A   , %Table(IIC_INTFC_ERR) B   , %Table(IIC_CONCUR_TBL) C   WHERE A.process_instance2 = :1   AND A.iic_cncr_l_status = 'E'   AND A.PROCESS_INSTANCE2 = B.PROCESS_INSTANCE   AND A.BATCHID = B.BATCHID   AND A.SEQUENCENUMBER = B.SEQUENCENUMBER   AND B.ERROR_TYPE_1 = 'DTL'   AND A.PROCESS_INSTANCE2 = C.PROCESS_INSTANCE2   AND A.BATCHID = C.BATCHID   AND A.SEQUENCENUMBER = C.SEQUENCENUMBER   AND A.BATCHDATE = C.BATCHDATE   AND A.ct_employee_emp_id = C.ct_employee_emp_id   GROUP BY VX.VENDOR_ID, c.ct_tr_requestid , a.batchdate , b.ERROR_MESSAGE_TXT , C.ct_employee_last_n, C.ct_employee_first
```

### IIC_CNCR_VCHR_LNE_SQL

**Descripción:** Count Concur line errors  

```sql
SELECT COUNT(COUNT(CT_REPORT_RPT_KEY))   FROM %Table(IIC_CNCR_DTL)   WHERE process_instance2 = :1   AND iic_cncr_l_status = 'E'   GROUP BY CT_REPORT_RPT_KEY
```

### IIC_CNCR_VCHR_LOAD_GET_SQL

**Descripción:** Vouchers loaded  

```sql
SELECT sqlView.PROCESS_INSTANCE   , sqlView.BATCHDATE   , sqlView.BUSINESS_UNIT   , sqlView.VOUCHER_ID   , sqlView.CT_REPORT_RPT_KEY   , sqlView.CT_EMPLOYEE_EMP_ID   , sqlView.VENDOR_ID   , sqlView.EMP_NAME   , sqlView.CT_E_ORG_UNIT2   , sqlView.GROSS_AMT_BSE   , sqlView.BUDGET_STATUS  , sqlView.CT_TR_REQUESTID  FROM (   SELECT A.PROCESS_INSTANCE   , A.BATCHDATE   , A.BUSINESS_UNIT   , A.VOUCHER_ID   , A.CT_REPORT_RPT_KEY   , A.CT_EMPLOYEE_EMP_ID   , B.VENDOR_ID   , A.CT_EMPLOYEE_LAST_N %Concat ', ' %Concat A.CT_EMPLOYEE_FIRST AS EMP_NAME   , A.CT_E_ORG_UNIT2   , B.GROSS_AMT_BSE   , %Coalesce(XLAT.XLATSHORTNAME ,' ') AS BUDGET_STATUS   , A.CT_TR_REQUESTID   FROM %Table(IIC_CONCUR_TBL) A   , %Table(VOUCHER) B LEFT OUTER JOIN PSXLATITEM XLAT ON XLAT.FIELDNAME = 'BUDGET_HDR_STATUS'   AND XLAT.FIELDVALUE = B.BUDGET_HDR_STATUS   , %Table(VENDOR) C   WHERE A.BUSINESS_UNIT = B.BUSINESS_UNIT   AND A.VOUCHER_ID = B.VOUCHER_ID   AND C.SETID = B.VENDOR_SETID   AND C.VENDOR_ID = B.VENDOR_ID   AND B.ENTRY_STATUS = 'P'   AND A.PROCESS_INSTANCE BETWEEN :1 AND :2 /* AND A.PROCESS_INSTANCE2 = 1*/   AND (XLAT.EFFDT IS NULL   OR %EffdtCheck(PSXLATITEM XLAT1, XLAT, %CURRENTDATEIN)) ) sqlView   GROUP BY sqlView.PROCESS_INSTANCE, sqlView.BATCHDATE, sqlView.BUSINESS_UNIT, sqlView.VOUCHER_ID, sqlView.CT_REPORT_RPT_KEY, sqlView.CT_EMPLOYEE_EMP_ID, sqlView.EMP_NAME, sqlView.VENDOR_ID, sqlView.CT_E_ORG_UNIT2, sqlView.GROSS_AMT_BSE, sqlView.BUDGET_STATUS, , sqlView.CT_TR_REQUESTID
```

### IIC_CNCR_VCHR_LOAD_SQL

**Descripción:** Count Vouchers loaded  

```sql
SELECT COUNT(COUNT(*))   FROM %Table(IIC_CONCUR_TBL) A   , %Table(VOUCHER) B   WHERE A.BUSINESS_UNIT = B.BUSINESS_UNIT   AND A.VOUCHER_ID = B.VOUCHER_ID /* AND A.ct_e_org_unit1='IIC' AND A.ct_p_code_lang_pat NOT LIKE '%COPD%' */   AND B.ENTRY_STATUS = 'P'   AND A.PROCESS_INSTANCE BETWEEN :1 AND :2 /* AND A.PROCESS_INSTANCE2 = 1 */   GROUP BY B.VOUCHER_ID
```

### IIC_CNCR_VCHR_NOTB_GET_SQL

**Descripción:** Voucher(s) not balanced  

```sql
SELECT NB.business_unit   , NB.voucher_id   , nb.vendor_id   , nb.name_display   , nb.invoice_id   , nb.invoice_dt   , NB.gross_amt   , NB.ct_journal_amount   FROM (   SELECT a.process_instance   , a.business_unit   , a.voucher_id   , a.vendor_id   , b.ct_employee_last_n %Concat ', ' %Concat b.ct_employee_first AS name_display   , a.invoice_id   , a.invoice_dt   , a.gross_amt  , SUM (CAST (b.ct_journal_amount AS DECIMAL (23, 3))) AS ct_journal_amount   FROM %Table(voucher) a   , %Table(iic_concur_tbl) b   WHERE a.voucher_id = b.voucher_id   AND a.business_unit = b.ct_all_custom1   GROUP BY a.process_instance,a.business_unit,a.voucher_Id,a.gross_amt,a.vendor_id, b.ct_employee_last_n , b.ct_employee_first, a.invoice_id,a.invoice_dt ) NB   WHERE NB.gross_amt <> NB.ct_journal_amount   AND NB.process_instance IN (:1,:2)
```

### IIC_CNCR_VCHR_NOTB_SQL

**Descripción:** Count Voucher(s) not balanced  

```sql
SELECT COUNT(*)   FROM (   SELECT a.process_instance   , a.business_unit   ,a.voucher_id   , a.gross_amt   ,SUM(b.ct_journal_amount) AS ct_journal_amount   FROM %Table(voucher) a   , %Table(iic_concur_tbl) b   WHERE a.voucher_id = b.voucher_id   AND a.business_unit = b.ct_all_custom1   GROUP BY a.process_instance,a.business_unit,a.voucher_Id,a.gross_amt) NB   WHERE NB.gross_amt <> NB.ct_journal_amount   AND NB.process_instance BETWEEN :1 AND :2
```

### IIC_CNCR_VCHR_RECV_SQL

**Descripción:** Count Vouchers received  

```sql
SELECT COUNT(*)   FROM %Table(VOUCHER) A   WHERE A.PROCESS_INSTANCE BETWEEN :1 AND :2
```

### IIC_CNCR_VCHR_RECY_GET_SQL

**Descripción:** Get vouchers recycled  

```sql
SELECT DISTINCT A.BUSINESS_UNIT   , A.VOUCHER_ID   , %Coalesce(A.VENDOR_ID, ' ')   , %Coalesce(B.NAME1, ct_employee_last_n %concat ', ' %concat ct_employee_first)   , A.INVOICE_ID   , %DateOut(A.INVOICE_DT)   , A.GROSS_AMT   , A.TXN_CURRENCY_CD   FROM %Table(IIC_VEDERRLOGVW) A LEFT OUTER JOIN %Table(vendor) B ON A.VENDOR_ID = B.VENDOR_ID   , %Table(iic_concur_tbl) C   WHERE A.VCHR_SRC = 'XML'   AND a.PROCESS_INSTANCE BETWEEN :1 AND :2   AND A.INVOICE_ID = C.CT_TR_REQUESTID   AND C.PROCESS_INSTANCE2 = :3
```

### IIC_CNCR_VCHR_RECY_SQL

**Descripción:** Get vouchers recycled  

```sql
SELECT COUNT(*)   FROM %Table(IIC_VEDERRLOGVW) A   WHERE A.VCHR_SRC = 'XML'   AND A.PROCESS_INSTANCE BETWEEN :1 AND :2
```

### IIC_CNCR_VCHR_VALID_SQL

**Descripción:** Concur Voucher validation  

```sql
SELECT 'CONCUR'   , sqlView.process_instance   , sqlView.batchdate   , sqlView.batchid   , sqlView.process_instance2   , COUNT(sqlView.number_vouchers)   , COUNT(vchr_created)   , sqlView.total_amount   , sqlView.vchrs_amount   FROM (   SELECT a.process_instance   , a.batchdate   , a.batchid   , a.process_instance2   , a.ct_report_rpt_key AS number_vouchers   , a.voucher_id AS vchr_created   , SUM(A.CT_JOURNAL_AMOUNT) AS total_amount   , b.GROSS_AMT_BSE AS vchrs_amount   FROM %Table(IIC_CONCUR_TBL) A   , %Table(VOUCHER) B   WHERE A.BUSINESS_UNIT = B.BUSINESS_UNIT   AND A.CT_TR_REQUESTID = B.INVOICE_ID   AND A.ct_e_org_unit1 = 'IIC'   AND A.ct_p_code_lang_pat NOT LIKE '%COPD%'   AND A.PROCESS_INSTANCE2 = :1   GROUP BY a.process_instance, a.batchdate, a.batchid, a.process_instance2,b.GROSS_AMT_BSE, a.ct_report_rpt_key, a.voucher_id ) sqlView   GROUP BY sqlView.process_instance, sqlView.batchdate, sqlView.batchid, sqlView.process_instance2, sqlView.total_amount, sqlView.vchrs_amount
```

### IIC_CNCR_VNDR_ABS_GET_SQL

**Descripción:** Get without valid vendor  

```sql
SELECT A.batchdate   , A.ct_report_rpt_key   , A.ct_employee_emp_id   , %Coalesce(VX.VENDOR_ID,' ')   , A.ct_employee_last_n ||', ' ||A.ct_employee_first   , A.ct_e_org_unit2   , D.BUSINESS_UNIT   , D.VOUCHER_ID   , SUM (CAST (A.CT_JOURNAL_AMOUNT AS DECIMAL (23, 3)))   FROM %Table(IIC_CONCUR_TBL) a LEFT OUTER JOIN %Table(VENDOR) VX ON A.ct_employee_emp_id= VX.VNDR_FIELD_C30_A   , %Table(IIC_VEDERRLOGVW) C   , %Table(VCHR_ERR_VW2) D   WHERE C.VCHR_SRC = 'XML'   AND A.PROCESS_INSTANCE BETWEEN :1 AND :2   AND C.BUSINESS_UNIT = D.BUSINESS_UNIT   AND C.VOUCHER_ID = D.VOUCHER_ID   AND D.TSE_FIELDNAME = 'VENDOR_ID'   AND C.process_instance = A.PROCESS_INSTANCE   AND A.CT_TR_REQUESTID = C.INVOICE_ID   AND (VX.VENDOR_STATUS = 'I'   AND NOT EXISTS (   SELECT 'X'   FROM %Table(VENDOR) VY   WHERE VY.SETID = VX.SETID   AND VY.VNDR_FIELD_C30_A = VX.VNDR_FIELD_C30_A   AND VY.VENDOR_STATUS = 'A'))   GROUP BY a.batchid, a.CT_ALL_CUSTOM1, A.batchdate, A.ct_report_rpt_key, A.ct_employee_emp_id, A.ct_employee_last_n, A.ct_employee_first, A.ct_e_org_unit2, VX.VENDOR_ID
```

### IIC_CNCR_VNDR_ABS_SQL

**Descripción:** Count without valid vendor  

```sql
SELECT COUNT(*)   FROM %Table(IIC_VEDERRLOGVW) A   , %Table(VCHR_ERR_VW2) B   WHERE A.VCHR_SRC = 'XML'   AND A.PROCESS_INSTANCE BETWEEN :1 AND :2   AND A.BUSINESS_UNIT = B.BUSINESS_UNIT   AND A.VOUCHER_ID = B.VOUCHER_ID   AND B.TSE_FIELDNAME = 'VENDOR_ID'
```

### IIC_INTFC_ERR_GET_SQL

**Descripción:** Interface errors by Batchid  

```sql
SELECT process_instance   , prcsname   , batchid   , iic_interface_id   , error_type_1   , error_message_txt   FROM %Table(IIC_INTFCERR_VW)   WHERE batchid = :1   AND process_instance = :2
```

### IIC_INTFC_ERR_NOTIF_SQL

**Descripción:** Notify interface errors  

```sql
SELECT '1st Reading'   , A.IIC_INTERFACE_ID   , A.PROCESS_INSTANCE2   , A.BATCHID   , A.DTTM_IMPORTED   , A.TOTAL_LINES   , A.TOTAL_ROWS AS VOUCHERS   , A.IIC_CNCR_L_STATUS   FROM %Table(IIC_CNCR_HDR) A   WHERE A.IIC_CNCR_L_STATUS = 'E'   AND A.PROCESS_INSTANCE2 = :1   UNION   SELECT '2nd Reading'   , 'CONCUR'   , B.PROCESS_INSTANCE   , B.BATCHID   , B.DTTM_IMPORTED   , B.TOTAL_LINES   , B.TOTAL_ROWS AS VOUCHERS   , 'E'   FROM %Table(IIC_CNHDR_TAO) B   WHERE B.PROCESS_INSTANCE = :1 AND 'Y' = :2
```

### IIC_VCHR_IMP_HDR_SQL

**Descripción:** Header select  

```sql
SELECT CASE WHEN x.Header = 1 THEN (x.SUM_CT_JOURNAL_AMOUNT - x.CT_CASH_ADV_REQ_AM) ELSE x.SUM_CT_JOURNAL_AMOUNT END AS TotHdr   , x.CT_ALL_CUSTOM1   , x.CT_C_ALPHA_CODE   , x.VENDOR_ID   FROM (   SELECT CASE WHEN (   SELECT DISTINCT(CT_CASH_ADV_REQ_AM)   FROM sysadm.ps_iic_concur_tbl   WHERE CT_EMPLOYEE_EMP_ID = :1   AND (CT_REPORT_RPT_KEY) LIKE :2   AND CT_CASH_ADV_REQ_AM <> ' ') > 0 THEN 1 ELSE 0 END AS Header, SUM( CASE WHEN TRIM(CT_JOURNAL_AMOUNT) IS NULL THEN 0 ELSE CAST (CT_JOURNAL_AMOUNT AS DECIMAL (23, 3)) END) AS SUM_CT_JOURNAL_AMOUNT, (   SELECT SUM(CT_CASH_ADV_REQ_AM)   FROM (   SELECT DISTINCT(CT_CASH_ADV_CA_KEY)   , CT_CASH_ADV_REQ_AM   FROM sysadm.ps_iic_concur_tbl   WHERE CT_EMPLOYEE_EMP_ID = :1   AND CT_REPORT_RPT_KEY = :2   AND CT_CASH_ADV_REQ_AM <> ' '   GROUP BY CT_CASH_ADV_CA_KEY, CT_CASH_ADV_REQ_AM ) ) AS CT_CASH_ADV_REQ_AM, t1.CT_ALL_CUSTOM1, t1.CT_C_ALPHA_CODE, %Coalesce(t2.vendor_id,' ') AS VENDOR_ID   FROM sysadm.ps_iic_concur_tbl t1 LEFT OUTER JOIN %Table(vendor) t2 ON t1.CT_EMPLOYEE_EMP_ID = T2.VNDR_FIELD_C30_A   WHERE CT_EMPLOYEE_EMP_ID = :1   AND CT_REPORT_RPT_KEY = :2   AND t1.PROCESS_INSTANCE ='0'   AND CT_P_CODE_LANG_PAT NOT LIKE '%COPD%'   AND CT_JRNL_DEBIT_CR <> 'CR'   GROUP BY CT_ALL_CUSTOM1, CT_C_ALPHA_CODE, VENDOR_ID )x
```

### IIC_VCHR_IMP_REPKEY_NOERR_SQL

**Descripción:** report key select  

```sql
SELECT DISTINCT(con.CT_REPORT_RPT_KEY)   ,MAX(con.CT_TR_REQUESTID)   FROM ps_iic_concur_tbl con   WHERE con.CT_EMPLOYEE_EMP_ID =:1   AND C_FLAG1='N'   AND con.process_instance = 0   AND con.CT_REPORT_RPT_KEY NOT IN (   SELECT D.CT_REPORT_RPT_KEY   FROM %Table(IIC_CNCR_DTL) D   WHERE D.BATCHID = con.BATCHID   AND D.PROCESS_INSTANCE2 = con.PROCESS_INSTANCE2   AND D.IIC_CNCR_L_STATUS IN ('E') )   GROUP BY CON.CT_REPORT_RPT_KEY
```

---
## PeopleCode

### Application Package: IIC_AZURE

#### IIC_AZURE:AppFunctionInterfaces:Handlers:Concur2ndRead

```peoplecode
/*----------------------------------------------------------------------------------------------------------------
Changes Track
Date		Project	 		    Developer	Comments
11/10/2023  IIC_CHG0075241      AKANASHIRO  CTASK0189899 - ConcurExtract extension in order to gather data
											from 2nd reading and dump the information to a temporary table.
----------------------------------------------------------------------------------------------------------------*/
/* Start - 11/10/2023 - IIC_CHG0075241 - AKANASHIRO - CTASK0189899  ConcurExtract extension  */
import IIC_AZURE:AppFunctionInterfaces:Handlers:ConcurExtract;

class Concur2ndRead extends IIC_AZURE:AppFunctionInterfaces:Handlers:ConcurExtract;
   method Concur2ndRead(&nbrProcInstance_ As number);
   method moveJsonToRowset(&s_json As string) Returns boolean;
   
protected
   
   property number nbrProcInstance;
end-class;

method Concur2ndRead
   /+ &nbrProcInstance_ as Number +/
   %Super = create IIC_AZURE:AppFunctionInterfaces:Handlers:ConcurExtract();
   %This.nbrProcInstance = &nbrProcInstance_;
   
end-method;


method moveJsonToRowset
   /+ &s_json as String +/
   /+ Returns Boolean +/
   /+ Extends/implements IIC_AZURE:AppFunctionInterfaces:Handlers:ConcurExtract.moveJsonToRowset +/
   
   Local JsonParser &o_parser = CreateJsonParser();
   REM created to control error in set of data;
   Local boolean &b_error = False;
   
   If &o_parser.Parse(&s_json) Then
      Local JsonObject &j_object = &o_parser.GetRootObject();
      Local JsonArray &coll = &j_object.GetJsonArray("");
      
      Local Rowset &rs_ = CreateRowset(Record.IIC_CNCR_TMP);
      Local SQL &insert = CreateSQL("%Insert(:1)");
      Local integer &i;
      Local Record &rc_ = CreateRecord(Record.IIC_CNCR_TMP);
      For &i = 1 To &coll.Length()
         Local array of string &aFieldname = CreateArrayRept("", 0);
         %This.resetError();
         
         &rc_.PROCESS_INSTANCE.Value = 0;
         &rc_.PROCESS_INSTANCE2.Value = %This.nbrProcInstance;
         rem GetRecord().PROCESS_INSTANCE.Value;
         &rc_.BATCHID.Value = &coll.GetJsonObject(&i).GetAsString("batchID");
         Local string &Icc_BatchDT = &coll.GetJsonObject(&i).GetAsString("batchDate");
         If All(&Icc_BatchDT) Then
            &rc_.BATCHDATE.Value = %This.dateToString(&Icc_BatchDT);
         End-If;
         
         &rc_.SEQUENCENUMBER.Value = &coll.GetJsonObject(&i).GetAsString("sequenceNumber");
         &rc_.CT_EMPLOYEE_EMP_ID.Value = &coll.GetJsonObject(&i).GetAsString("employeeID");
         &rc_.CT_EMPLOYEE_LAST_N.Value = &coll.GetJsonObject(&i).GetAsString("lastName");
         &rc_.CT_EMPLOYEE_FIRST.Value = &coll.GetJsonObject(&i).GetAsString("firstName");
         &rc_.CT_E_CUSTOM21.Value = &coll.GetJsonObject(&i).GetAsString("groupID");
         &rc_.CT_E_ORG_UNIT1.Value = &coll.GetJsonObject(&i).GetAsString("employeeOrgUnit1");
         &rc_.CT_E_ORG_UNIT2.Value = &coll.GetJsonObject(&i).GetAsString("employeeOrgunit2");
         &rc_.CT_REPORT_RPT_KEY.Value = &coll.GetJsonObject(&i).GetAsString("reportKey");
         &rc_.CT_C_ALPHA_CODE.Value = &coll.GetJsonObject(&i).GetAsString("reimbursementCurrency");
         &rc_.CT_E_TYPE_LANG_NAM.Value = &coll.GetJsonObject(&i).GetAsString("expenseType");
         &rc_.CT_P_CODE_LANG_PAT.Value = &coll.GetJsonObject(&i).GetAsString("entryPaymentCode");
         &rc_.CT_ALL_PERCENTAGE.Value = &coll.GetJsonObject(&i).GetAsString("allocationPercentage");
         &rc_.CT_ALL_CUSTOM1.Value = &coll.GetJsonObject(&i).GetAsString("allocationCustom1");
         &rc_.CT_ALL_CUSTOM2.Value = &coll.GetJsonObject(&i).GetAsString("allocationCustom2");
         &rc_.CT_ALL_CUSTOM3.Value = &coll.GetJsonObject(&i).GetAsString("allocationCustom3");
         &rc_.CT_TR_REQUESTID.Value = &coll.GetJsonObject(&i).GetAsString("travelRequestID");
         &rc_.CT_RE_VIEW_NET_TAX.Value = &coll.GetJsonObject(&i).GetAsString("netAdjusted");
         &rc_.CT_CASH_ADV_REQ_AM.Value = &coll.GetJsonObject(&i).GetAsString("cashAdvanceAmount");
         &rc_.CT_JOURNAL_AMOUNT.Value = &coll.GetJsonObject(&i).GetAsString("journalAmt");
         &rc_.CT_CASH_ADV_CA_KEY.Value = &coll.GetJsonObject(&i).GetAsString("caKey");
         &rc_.CT_JRNL_DEBIT_CR.Value = &coll.GetJsonObject(&i).GetAsString("drcr");
         &rc_.CT_R_ENTRY_TRANS_D.Value = &coll.GetJsonObject(&i).GetAsString("entryTransactionDate");
         &rc_.CT_REPORT_RPE_KEY.Value = &coll.GetJsonObject(&i).GetAsString("entryId");
         %This.moveFromRecordToDB(&rc_, &insert);
         /* 
         If Not %This.hasErrors() And
               %This.isValidData(&rc_) Then
            %This.moveFromRecordToDB(&rc_, &insert);
         Else
            &b_error = True;
            %This.setError();
         End-If;
         
         If %This.hasErrors() Then
            &b_error = True;
         End-If;*/
      End-For;
      &insert.Close();
   End-If;
   
   If &b_error Then
      Return False;
   End-If;
   
   Return True;
end-method;

/* End - 11/10/2023 - IIC_CHG0075241 - AKANASHIRO - CTASK0189899  ConcurExtract extension  */
```

---
## Process Definitions

### IIC_CNCR_RB

**Tipo:** Application Engine  
**Run Location:** 2  
**Descripción:** Concur rollback  
