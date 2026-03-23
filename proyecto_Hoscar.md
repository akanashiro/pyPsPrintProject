# Proyecto PeopleSoft: HCPO_INT_MERGE_20160728

Merge de integraciones PO

## Resumen del Proyecto

| Tipo de Objeto | Cantidad |
|----------------|----------|
| Records | 13 |
| Fields | 1 |
| Pages | 8 |
| SQL Objects | 8 |

---
## Records

### HCPO_BODEGA_MV

**Tipo:** Table  
**Descripción:** Bodega MV, Sug. Compra.  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| SETID | 0 | 5 | — |  |
| HCPO_SHIPTO_ID_MV | 0 | 8 | — |  |
| DOC_SEQ_NBR | 0 | 12 | — |  |
| INV_ITEM_ID | 0 | 18 | — |  |
| QTY_REQ | 2 | 16 | — |  |
| UNIT_OF_MEASURE | 0 | 3 | — |  |
| TRANSACTION_DTTM | 6 | 26 | — |  |

### HCPO_FUNCLIB_WR

**Tipo:** Derived/Work  
**Descripción:** Funciones HCPO  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| HCPO_LICITACION | 0 | 15 | — |  |

### HCPO_ITM_CAT_VW

**Tipo:** View  
**Descripción:** Sugerencia Compra  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| SETID | 0 | 5 | — |  |
| CATEGORY_ID | 0 | 5 | — |  |
| INV_ITEM_ID | 0 | 18 | — |  |
| DESCR | 0 | 30 | — |  |
| UNIT_OF_MEASURE | 0 | 3 | — |  |
| QTY_REQ | 2 | 16 | — |  |
| HCPO_SHIPTO_ID_MV | 0 | 8 | — |  |
| TRANSACTION_DTTM | 6 | 26 | — |  |

### HCPO_ITM_UN_MSR

**Tipo:** View  
**Descripción:** Unidad de Medida Artículo  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| SETID | 0 | 5 | — |  |
| INV_ITEM_ID | 0 | 18 | — |  |
| UNIT_OF_MEASURE | 0 | 3 | — |  |
| DESCR | 0 | 30 | — |  |
| DESCRSHORT | 0 | 10 | — |  |

### HCPO_PICK_OR_WS

**Tipo:** Table  
**Descripción:** Artículos Recepción MV.  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| BUSINESS_UNIT | 0 | 5 | — |  |
| RECEIVER_ID | 0 | 10 | — |  |
| INV_ITEM_ID | 0 | 18 | — |  |
| QTY_SH_RECVD | 2 | 16 | — |  |
| RECEIVE_UOM | 0 | 3 | — |  |
| CLOSE_SHORT_FLG | 0 | 1 | — |  |

### HCPO_PICK_O_WRK

**Tipo:** Derived/Work  
**Descripción:** Integración Recepción MV  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PB_SELECT_PO | 0 | 1 | — |  |
| PB_CANCEL_RECPT | 0 | 1 | — |  |
| QTY_SH_RECVD | 2 | 16 | — |  |

### HCPO_P_SLECT_WS

**Tipo:** Table  
**Descripción:** Selcción Acc. Recepción MV.  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| BUSINESS_UNIT | 0 | 5 | — |  |
| RECEIVER_ID | 0 | 10 | — |  |
| PB_SELECT_PO | 0 | 1 | — |  |
| PB_CANCEL_RECPT | 0 | 1 | — |  |

### HCPO_RSLT_INTEG

**Tipo:** Table  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| VALUE | 0 | 254 | — |  |
| DESCRLONG | 1 |  | — |  |
| DESCRLONG2 | 1 |  | — |  |

### HCPO_SLCT_RPSCN

**Tipo:** Derived/Work  
**Descripción:** Derived Sugerencia Compra  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| SELECT | 0 | 1 | — |  |

### HCPO_SOL_RPSCN

**Tipo:** Derived/Work  
**Descripción:** Derived Link Sugerencia Compra  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| LINK | 0 | 1 | — |  |

### HCPO_SRCH_RPSCN

**Tipo:** Derived/Work  
**Descripción:** Busqueda Sugerencia de compra.  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| SETID | 0 | 5 | — |  |
| SHIPTO_ID | 0 | 10 | — |  |
| SEARCH_BUTTON | 0 | 1 | — |  |
| SELECT_ALL | 0 | 1 | — |  |
| FLAG | 0 | 1 | — |  |
| TREE_NODE | 0 | 20 | — |  |
| DELETE_BUTTON | 0 | 1 | — |  |

### PO_PNLS_WRK

**Tipo:** Derived/Work  
**Descripción:** Purchase Order Entry Work Rec  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| ADD_KIT | 0 | 1 | — |  |
| ADJ_AMT | 3 | 17 | — |  |
| ADJ_AMT_TTL | 3 | 28 | — |  |
| ADJ_AMT_TTL_LBL | 3 | 28 | — |  |
| ADJ_REQ_OPEN | 0 | 1 | — |  |
| AMT_OPEN | 3 | 28 | — |  |
| AMT_REMAIN | 3 | 28 | — |  |
| APPROVAL_DT | 4 | 10 | — |  |
| APPROVE_BUTTON | 0 | 1 | — |  |
| APPROVE_PB | 0 | 1 | — |  |
| ASSET_INFO_FLG | 0 | 1 | — |  |
| BACKORDER_STATUS | 0 | 1 | — |  |
| BUSINESS_UNIT | 0 | 5 | — |  |
| BUSINESS_UNIT_IN | 0 | 5 | — |  |
| CALC_PRICE_FLG | 0 | 1 | — |  |
| CANCEL_LINE_PB | 0 | 1 | — |  |
| CANCEL_DISTRIB_PB | 0 | 1 | — |  |
| CANCEL_FLAG | 0 | 1 | — |  |
| CANCEL_PB | 0 | 1 | — |  |
| CANCEL_PO_PB | 0 | 1 | — |  |
| CANCEL_SCHED_PB | 0 | 1 | — |  |
| CATALOG_PB | 0 | 1 | — |  |
| CATEGORY_ID | 0 | 5 | — |  |
| CHANGE_HDR | 0 | 1 | — |  |
| CHANGE_LINE | 0 | 1 | — |  |
| CHANGE_PRICE_PB | 0 | 1 | — |  |
| CHANGE_SHIP | 0 | 1 | — |  |
| CHECK_SHIP_COMM | 0 | 1 | — |  |
| CHGD_CONV_RT | 0 | 1 | — |  |
| CHGD_CONV_RT_ANY | 0 | 1 | — |  |
| CHGD_PRICE | 0 | 1 | — |  |
| CHGD_QTY | 0 | 1 | — |  |
| CHGD_UOM | 0 | 1 | — |  |
| CHNG_ORD_MSG | 0 | 30 | — |  |
| CHNG_ORD_REC_STAT | 0 | 18 | — |  |
| CHNG_SOURCE | 0 | 3 | — |  |
| CLEAR_REQ_PB | 0 | 1 | — |  |
| CNTRCT_LOADED | 0 | 1 | — |  |
| CNTRCT_SETID | 0 | 5 | — |  |
| CNTRCT_PB | 0 | 1 | — |  |
| COMMENT_SORT | 0 | 1 | — |  |
| COMMENT_SORT_MTHD | 0 | 1 | — |  |
| COMMENT_SORT_SEQ | 0 | 1 | — |  |
| CONVERSION_RATE | 3 | 17 | — |  |
| COPY_CNTRCT_ID | 0 | 25 | — |  |
| VERSION_NBR | 2 | 5 | — |  |
| COPY_CNTRCT_LINE | 2 | 5 | — |  |
| CNTRCT_CANCEL | 0 | 1 | — |  |
| COPY_CAT_LINE | 2 | 5 | — |  |
| COPY_FROM_ID | 0 | 10 | — |  |
| COPY_NOW | 0 | 1 | — |  |
| COPY_PO_FROM | 0 | 1 | — |  |
| COUNTRY_CODE | 0 | 3 | — |  |
| CURRENCY_CD | 0 | 3 | — |  |
| CURRENCY_CD_BASE | 0 | 3 | — |  |
| CURRENCY_PAY_CD | 0 | 3 | — |  |
| DEFAULTS_ACCESSED | 0 | 1 | — |  |
| DELETE_FLAG | 0 | 1 | — |  |
| DELETE_PO_PB | 0 | 1 | — |  |
| DELETING_DIST | 0 | 1 | — |  |
| DELETING_LINE | 0 | 1 | — |  |
| DELETING_SCHED | 0 | 1 | — |  |
| DESCR | 0 | 30 | — |  |
| DESCR254_MIXED | 0 | 254 | — |  |
| DISPATCH_FLAG | 0 | 1 | — |  |
| DISPATCH_PB | 0 | 1 | — |  |
| DISP_DISTRIB | 0 | 1 | — |  |
| DISP_DISTRIB_AM | 0 | 1 | — |  |
| DISP_DISTRIB_DTLS | 0 | 1 | — |  |
| DISP_VAL_ADJ | 0 | 1 | — |  |
| DISTRIB_LINE_ROW | 2 | 5 | — |  |
| DROP_SHIP_FLAG | 0 | 1 | — |  |
| EDIT_PO_FLG | 0 | 1 | — |  |
| EFFDT | 4 | 10 | — |  |
| ENTERED_DT | 4 | 10 | — |  |
| EXTENSION | 0 | 6 | — |  |
| EMAILID | 0 | 70 | — |  |
| GOTO_ACTIVITIES | 0 | 1 | — |  |
| GOTO_ASSET | 0 | 1 | — |  |
| GOTO_BACKORDER | 0 | 1 | — |  |
| GOTO_BILL_ADDRESS | 0 | 1 | — |  |
| GOTO_CATALOG | 0 | 1 | — |  |
| GOTO_CONFIGURATION | 0 | 1 | — |  |
| GOTO_CURR_INFO | 0 | 1 | — |  |
| GOTO_DEFAULTS | 0 | 1 | — |  |
| GOTO_DISTRIB | 0 | 1 | — |  |
| GOTO_DISTRIB_DTLS | 0 | 1 | — |  |
| GOTO_DISTRIB_REQ | 0 | 1 | — |  |
| GOTO_DISTRIB_SUT | 0 | 1 | — |  |
| GOTO_DISTRIB_VAT | 0 | 1 | — |  |
| GOTO_DROP_SHIP | 0 | 1 | — |  |
| GOTO_EXCHNG_DTL | 0 | 1 | — |  |
| GOTO_HDR_DTL | 0 | 1 | — |  |
| GOTO_HDR_VAT | 0 | 1 | — |  |
| GOTO_INV | 0 | 1 | — |  |
| GOTO_ITM_DESCR | 0 | 1 | — |  |
| GOTO_LINE_DTLS | 0 | 1 | — |  |
| GOTO_LINE_MISC | 0 | 1 | — |  |
| GOTO_MATCHING | 0 | 1 | — |  |
| GOTO_MISC_CHARGES | 0 | 1 | — |  |
| GOTO_MULTI_SPCHART | 0 | 1 | — |  |
| GOTO_PO_GROUP | 0 | 1 | — |  |
| GOTO_REQ | 0 | 1 | — |  |
| GOTO_REQ_FORM | 0 | 1 | — |  |
| GOTO_SCHED | 0 | 1 | — |  |
| GOTO_SCHED_DTLS | 0 | 1 | — |  |
| GOTO_SCHED_RTV | 0 | 1 | — |  |
| GOTO_SCHED_SUT | 0 | 1 | — |  |
| GOTO_SCHED_TIME | 0 | 1 | — |  |
| GOTO_SCHED_VAT | 0 | 1 | — |  |
| GOTO_SHIP_ADDRESS | 0 | 1 | — |  |
| GOTO_SUBCNTRCT | 0 | 1 | — |  |
| GOTO_SUP_HIERARCHY | 0 | 1 | — |  |
| GOTO_VAL_ADJ | 0 | 1 | — |  |
| GOTO_VENDOR | 0 | 1 | — |  |
| GOTO_VENDOR_REQ | 0 | 1 | — |  |
| HOME_PB | 0 | 1 | — |  |
| INS_DEF_SHIP_COMM | 0 | 1 | — |  |
| INS_VAL_ADJ_PB | 0 | 1 | — |  |
| INSERTING_VAL_ADJ | 0 | 1 | — |  |
| INV_INFO_FLG | 0 | 1 | — |  |
| INV_ITEM_ID | 0 | 18 | — |  |
| ITEM_AVAIL | 0 | 1 | — |  |
| ITM_SETID | 0 | 5 | — |  |
| KIT_ITEM | 0 | 18 | — |  |
| KIT_ROW_NUM | 2 | 3 | — |  |
| LAST_DTTM_UPDATE | 6 | 26 | — |  |
| LBL_ITM_DESCR | 0 | 1 | — |  |
| LINE_NBR | 2 | 5 | — |  |
| LINE_NBR_FROM | 2 | 5 | — |  |
| LINE_NBR_MAX | 2 | 5 | — |  |
| LINE_NBR_TO | 2 | 5 | — |  |
| LINE_NBR_WRK | 2 | 5 | — |  |
| LINE_GROUP_PB | 0 | 1 | — |  |
| LINE_REFRESH | 0 | 1 | — |  |
| LINE_ROW | 2 | 5 | — |  |
| LINES_SAVED | 0 | 1 | — |  |
| LINE_SELECT | 0 | 1 | — |  |
| LOAD_COMMENTS_PB | 0 | 1 | — |  |
| MAINTAIN_CF_PCODE | 0 | 1 | — |  |
| MERCH_AMT_BSE | 3 | 28 | — |  |
| MERCHANDISE_AMT | 3 | 28 | — |  |
| MERCH_AMT_TTL | 3 | 28 | — |  |
| NBR_OF_PO | 2 | 2 | — |  |
| NEW_ROW | 0 | 1 | — |  |
| OPEN_QTY_RFQ | 3 | 17 | — |  |
| OPRCLASS | 0 | 30 | — |  |
| OPRDEFNDESC | 0 | 30 | — |  |
| OPRID | 0 | 30 | — |  |
| OPRID_ENTERED_BY | 0 | 30 | — |  |
| OPRID_APPROVED_BY | 0 | 30 | — |  |
| OPRID_MODIFIED_BY | 0 | 30 | — |  |
| PEG_STAT_PO | 0 | 2 | — |  |
| PHONE | 0 | 24 | — |  |
| PO_AMT1 | 3 | 28 | — |  |
| PO_AMT2 | 3 | 28 | — |  |
| PO_AMT3 | 3 | 28 | — |  |
| PO_AMT_TTL | 3 | 28 | — |  |
| PO_FIRST | 0 | 10 | — |  |
| PO_ID | 0 | 10 | — |  |
| PO_LAST | 0 | 10 | — |  |
| PRCSINSTANCE | 2 | 10 | — |  |
| PRICE_ADJUSTED | 3 | 17 | — |  |
| PRINT_BTN | 0 | 1 | — |  |
| PRINT_FLG | 0 | 3 | — |  |
| QTY_KIT | 2 | 16 | — |  |
| QTY_OPEN | 2 | 16 | — |  |
| QTY_PO | 2 | 16 | — |  |
| QTY_PO_PRIOR | 2 | 16 | — |  |
| QTY_REMAIN | 3 | 17 | — |  |
| QTY_RFQ | 2 | 16 | — |  |
| RATE_DATE | 4 | 10 | — |  |
| REFERENCED_FLG | 0 | 1 | — |  |
| RELEASE_ID | 0 | 5 | — |  |
| REQ_INFO_FLG | 0 | 1 | — |  |
| RE_SOURCE_QTY | 0 | 1 | — |  |
| RESERVE_PO | 0 | 1 | — |  |
| RESET_APPROVAL_PB | 0 | 1 | — |  |
| RFQ_ID | 0 | 10 | — |  |
| RSRVE_PO_BLOCK_FLG | 0 | 1 | — |  |
| RT_RATE | 2 | 16 | — |  |
| RT_TYPE | 0 | 5 | — |  |
| RUN_CNTL_ID | 0 | 30 | — |  |
| SALES_USE_TX_FLG | 0 | 1 | — |  |
| SCHED_ROW | 2 | 5 | — |  |
| SCROLL_SELECT | 0 | 1 | — |  |
| SEL_CHNG_LN_FLDS | 0 | 1 | — |  |
| SEL_CHNG_SHP_FLDS | 0 | 1 | — |  |
| SEL_COMM_FLG | 0 | 1 | — |  |
| SEL_DESEL_ALL | 0 | 1 | — |  |
| SEL_DIST_FLG | 0 | 1 | — |  |
| SEL_LINE_FLG | 0 | 1 | — |  |
| SEL_MISC_HDR_FLG | 0 | 1 | — |  |
| SEL_MISC_LINE_FLG | 0 | 1 | — |  |
| SEL_SCHED_FLG | 0 | 1 | — |  |
| SEL_VAL_ADJ_FLG | 0 | 1 | — |  |
| SELECT_OPT | 0 | 1 | — |  |
| SHIPTO_SETID | 0 | 5 | — |  |
| SHIPTO_ID | 0 | 10 | — |  |
| SHIP_TYPE_ID | 0 | 10 | — |  |
| SORT_VAL_ADJ_PB | 0 | 1 | — |  |
| SPEEDCHART_FLG | 0 | 1 | — |  |
| SPEEDCHART_KEY | 0 | 10 | — |  |
| SPEEDCHART_OPT | 0 | 1 | — |  |
| SPEEDCHART_SHOW | 0 | 1 | — |  |
| STOCKLESS_FLG | 0 | 1 | — |  |
| SUBCNTRCT_INFO_FLG | 0 | 1 | — |  |
| SUB_ITEM_PB | 0 | 1 | — |  |
| SUBITM_USE | 0 | 1 | — |  |
| TAX_PCT | 2 | 7 | — |  |
| UPDATE_AUC | 0 | 1 | — |  |
| UPDATE_REQS | 2 | 1 | — |  |
| UPN_ID | 0 | 20 | — |  |
| USER_OPRCLASS | 0 | 8 | — |  |
| USER_OPRID | 0 | 30 | — |  |
| YES_INDICATOR | 2 | 1 | — |  |
| VAT_APORT_CNTRL | 0 | 1 | — |  |
| VAT_CALC_PB | 0 | 1 | — |  |
| VAT_CALC_TREAT | 0 | 1 | — |  |
| VAT_ENTITY | 0 | 20 | — |  |
| VENDOR_SETID | 0 | 5 | — |  |
| VENDOR_ID | 0 | 10 | — |  |
| VENDOR_CNTRCT | 0 | 10 | — |  |
| VENDOR_CNTRCT_SET | 0 | 5 | — |  |
| VENDOR_NAME_SHORT | 0 | 14 | — |  |
| VNDR_NAME1 | 0 | 40 | — |  |
| VIEW_LN_DETAIL | 0 | 1 | — |  |
| VISUAL_RATE | 2 | 16 | — |  |
| VNDR_LOC | 0 | 10 | — |  |
| BUDGET_CHECK_LINE | 0 | 1 | — |  |
| VIEW_APPR | 0 | 1 | — |  |
| JUSTIFICATION | 1 |  | — |  |
| COMMENTS_2000 | 1 |  | — |  |
| DENY_PB | 0 | 1 | — |  |
| PUSHBACK_PB | 0 | 1 | — |  |
| GOTO_ACT_SUMMARY | 0 | 1 | — |  |
| PO_ALERT | 1 |  | — |  |
| ENCUM_BALANCE_LBL | 3 | 28 | — |  |
| PO_DT | 4 | 10 | — |  |
| ORIG_INV_ITEM_ID | 0 | 18 | — |  |
| STD_ID_NUM_SHIPTO | 0 | 20 | — |  |
| CNTR_LN_TYPE_ID | 0 | 30 | — |  |
| UOM_CHNG | 0 | 1 | — |  |
| APPLY_SPEED | 0 | 1 | — |  |

### PV_REQ_APPPG_WK

**Tipo:** Derived/Work  
**Descripción:** ePro Approval Page Work Record  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| MERCHANDISE_AMT | 3 | 28 | — |  |
| REQUESTOR_ID | 0 | 30 | — |  |
| DESCR | 0 | 30 | — |  |
| DESCR254_MIXED | 0 | 254 | — |  |
| TITLE56 | 0 | 56 | — |  |
| PV_NAME | 0 | 50 | — |  |
| EDIT_PB | 0 | 1 | — |  |
| APPROVAL_PB | 0 | 1 | — |  |
| DENY_PB | 0 | 1 | — |  |
| HOLD_PB | 0 | 2 | — |  |
| PUSHBACK_PB | 0 | 1 | — |  |
| COMMENTS_PB | 0 | 1 | — |  |
| SAVE_PB | 0 | 1 | — |  |
| CURRENCY_DISP_PB | 0 | 3 | — |  |
| CURRENCY_CD | 0 | 3 | — |  |
| DESCR_AMT1 | 0 | 50 | — |  |
| REQ_ANALYTICS | 0 | 1 | — |  |
| BUDGET_CHECK_PB | 0 | 1 | — |  |
| IMAGE_NAME | 0 | 30 | — |  |
| PV_CONNECTOR_IMG | 9 | 30 | — |  |
| COMMENTS_2000 | 1 |  | — |  |
| COMMENTS_2000_WRK | 1 | 32700 | — |  |
| PV_MONITOR_HTML | 1 |  | — |  |
| JUSTIFICATION | 1 |  | — |  |
| HTML_AREA_01 | 1 |  | — |  |
| FORMULA | 0 | 1 | — |  |
| HTML_AREA_02 | 1 |  | — |  |
| HTML_AREA_04 | 1 |  | — |  |
| PV_PRINT_REQ | 1 |  | — |  |
| HTML_AREA_03 | 1 |  | — |  |
| PV_REQ_ALERT | 1 |  | — |  |
| GROUP_BOX | 0 | 1 | — |  |
| PV_INFOBOX | 1 | 999 | — |  |
| BUTTON_WORKLIST | 1 |  | — |  |
| RETURN_PAGE_PB | 0 | 1 | — |  |
| RETURN_PB | 0 | 1 | — |  |
| LINE_COMMENT | 1 | 2000 | — |  |
| PV_MODAL | 1 | 16959 | — |  |
| START_DATE | 4 | 10 | — |  |
| REPORT_NAME | 0 | 30 | — |  |
| END_DATE | 4 | 10 | — |  |
| REPORT_PB | 0 | 1 | — |  |
| LINE_DETAILS_GB | 0 | 1 | — |  |
| ADJ_AMT_TTL | 3 | 28 | — |  |
| PAGETITLE | 0 | 254 | — |  |
| PV_PREV_BTTN | 0 | 1 | — |  |
| PV_NEXT_BTTN | 0 | 1 | — |  |
| DESCR_AMT2 | 0 | 50 | — |  |
| DESCR_AMT3 | 0 | 50 | — |  |
| DESCR254_FROM | 0 | 254 | — |  |
| DESCR254_TO | 0 | 254 | — |  |
| CHANGE_REQ_LINE | 0 | 1 | — |  |
| APPROVAL_HISTORY | 0 | 1 | — |  |

---
## Fields

### HCPO_SHIPTO_ID_MV

**Tipo:** Character  
**Longitud:** 8  

---
## Pages

### HCPO_BODEGA_MV_PG

**Tipo:** Standard  
**Descripción:** 
            "controls": [
                {
                    "control_type": c.control_type,
                    "record_name": c.record_name or "",
                    "field_name": c.field_name or "",
                    "label": c.label or "",
                }
                for c in p.controls
            ],
            "control_count": len(p.controls),
              
### HCPO_RECV_INV_WPO

**Tipo:** Standard  
**Descripción:** Integración Recepción MV.  
### HCPO_SRCH_RPSCN

**Tipo:** Popup  
**Descripción:** Sugerencia de Compra.  
### PO_HEADER_SBP

**Tipo:** Secondary  
**Descripción:** 
            "controls": [
                {
                    "control_type": c.control_type,
                    "record_name": c.record_name or "",
                    "field_name": c.field_name or "",
                    "label": c.label or "",
                }
                for c in p.controls
            ],
            "control_count": len(p.controls),
              
### PO_LINE

**Tipo:** Standard  
**Descripción:** PO - Line  
### PV_ALL_RQST_OPTION

**Tipo:** Standard  
**Descripción:** All Request Options  
### PV_REQ_CATBRW_RES

**Tipo:** Standard  
**Descripción:** Catalog Browse Results  
### PV_REQ_CHECKOUT

**Tipo:** Standard  
**Descripción:** ePro Req Review and Submit  
---
## SQL Objects

### HCPO_BORRAR_ARTICULOS_MV_SQL


```sql
DELETE FROM PS_HCPO_BODEGA_MV WHERE HCPO_SHIPTO_ID_MV = ( SELECT HC_VALOR_MV FROM PS_HC_RELACN_PSMV WHERE FIELDNAME = 'SHIPTO_ID' AND hc_funcionalidad = 'ALMACEN' AND HC_MODULO_FIN = 'PO' AND HC_vALOR_PS = :1)
```

### HCPO_BUSINESS_UNIT_MV_SQL


```sql
 SELECT B.HC_VALOR_MV ,B.DESCR60 FROM PS_PO_HDR A JOIN PS_HC_RELACN_PSMV B ON A.BUSINESS_UNIT = B.HC_VALOR_PS WHERE B.FIELDNAME = 'BUSINESS_UNIT' AND B.HC_FUNCIONALIDAD = 'UNIDAD_NEGOCIO' AND B.HC_MODULO_FIN = 'PO' AND A.BUSINESS_UNIT = :1 AND A.PO_ID = :2
```

### HCPO_CHNG_CAN_LINE_NBR_DTL_SQL


```sql
 SELECT 'X' FROM ps_PO_CHNG_SHIP A JOIN PS_PO_LINE B ON A.BUSINESS_UNIT = B.BUSINESS_UNIT AND A.PO_ID = B.PO_ID AND A.LINE_NBR = B.LINE_NBR WHERE A.BUSINESS_UNIT = :1 AND A.PO_ID = :2 AND B.INV_ITEM_ID = :3 AND A.CHNG_ORD_BATCH = :4 AND A.CHNG_ORD_SEQ = ( SELECT MAX(AX.CHNG_ORD_SEQ) FROM PS_PO_CHNG_SHIP AX WHERE AX.BUSINESS_UNIT = A.BUSINESS_UNIT AND AX.PO_ID = A.PO_ID AND AX.LINE_NBR = A.LINE_NBR AND AX.FIELDNAME = A.FIELDNAME) AND A.FIELDNAME = 'CANCEL_STATUS' AND A.CHNG_CHAR_VALUE = 'X'
```

### HCPO_INGR_LINE_NBR_DTL_SQL


```sql
 SELECT 'X' FROM ps_PO_CHNG_SHIP A JOIN PS_PO_LINE B ON A.BUSINESS_UNIT = B.BUSINESS_UNIT AND A.PO_ID = B.PO_ID AND A.LINE_NBR = B.LINE_NBR WHERE A.BUSINESS_UNIT = :1 AND A.PO_ID = :2 AND B.INV_ITEM_ID = :3 AND A.CHNG_ORD_BATCH = :4 AND A.CHNG_ORD_SEQ = ( SELECT MAX(AX.CHNG_ORD_SEQ) FROM PS_PO_CHNG_SHIP AX WHERE AX.BUSINESS_UNIT = A.BUSINESS_UNIT AND AX.PO_ID = A.PO_ID AND AX.LINE_NBR = A.LINE_NBR AND AX.FIELDNAME = A.FIELDNAME) AND A.FIELDNAME = 'CHNG_TYPE' AND A.CHNG_CHAR_VALUE = 'I'
```

### HCPO_ORDENES_COMPRA_A_MV_SQL


```sql
SELECT BUSINESS_UNIT ,PO_ID FROM PS_PO_HDR WHERE EXISTS ( SELECT 'X' FROM %Table(PODISPUPD_TAO) WHERE %Table(PODISPUPD_TAO).PROCESS_INSTANCE = :1 AND %Table(PODISPUPD_TAO).BUSINESS_UNIT = PS_PO_HDR.BUSINESS_UNIT AND %Table(PODISPUPD_TAO).PO_ID = PS_PO_HDR.PO_ID AND PS_PO_HDR.POA_STATUS IN ('WD','A','NR') AND %Table(PODISPUPD_TAO).UPDATE_ACTION = 'Y') AND NOT EXISTS ( SELECT 'X' FROM PS_CNTRCT_RPO_XREF CNT WHERE CNT.BUSINESS_UNIT = PS_PO_HDR.BUSINESS_UNIT AND CNT.PO_ID = PS_PO_HDR.PO_ID);
```

### HCPO_ORIGIN_MV_SQL


```sql
SELECT HC_VALOR_MV ,DESCR60 FROM PS_HC_RELACN_PSMV WHERE HC_VALOR_PS = :1
```

### HCPO_SHIPTO_ID_MV_SQL


```sql
SELECT B.HC_VALOR_MV ,B.DESCR60 FROM PS_REQ_DFLT_TBL A JOIN PS_HC_RELACN_PSMV B ON A.SHIPTO_ID = B.HC_VALOR_PS WHERE FIELDNAME = 'SHIPTO_ID' AND HC_FUNCIONALIDAD = 'ALMACEN' AND A.BUSINESS_UNIT = :1 AND A.REQ_ID = :2
```

### HCPO_SHIPTO_ID_PO_MV_SQL


```sql
SELECT B.HC_VALOR_MV ,B.DESCR60 FROM PS_PO_LINE_SHIP A JOIN PS_HC_RELACN_PSMV B ON A.SHIPTO_ID = B.HC_VALOR_PS WHERE FIELDNAME = 'SHIPTO_ID' AND HC_FUNCIONALIDAD = 'ALMACEN' AND A.BUSINESS_UNIT = :1 AND A.PO_ID = :2
```
