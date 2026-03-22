# Proyecto PeopleSoft: IIC_CHG0077637

SAP GL i1028

## Resumen del Proyecto

| Tipo de Objeto | Cantidad |
|----------------|----------|
| Records | 3 |
| Fields | 4 |
| Process Definitions | 1 |

## Records

### IIC_I1028_AET

**Tipo:** Derived/Work  
**Descripción:** I1028 process aet  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE | 2 | 10 | — |  |
| IB_OPERATIONNAME | 0 | 30 | — |  |
| IIC_CALL_NBR | 2 | 3 | — |  |
| IIC_DAYS_DIF | 2 | 3 | — |  |
| IIC_IM_FUND | 0 | 4 | — |  |
| IIC_IM_BLARTL | 0 | 3 | — |  |
| IIC_IM_BLARTH | 0 | 3 | — |  |
| IIC_IM_HKONTL | 0 | 3 | — |  |
| IIC_IM_HKONTH | 0 | 3 | — |  |

### IIC_I1028_TBL

**Tipo:** Table  
**Descripción:** I1028 setup tbl  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| IB_OPERATIONNAME | 0 | 30 | — |  |
| IIC_CALL_NBR | 2 | 3 | — |  |
| IIC_DAYS_DIF | 2 | 3 | — |  |
| IIC_IM_FUND | 0 | 4 | — |  |
| IIC_IM_BLARTL | 0 | 3 | — |  |
| IIC_IM_BLARTH | 0 | 3 | — |  |
| IIC_IM_HKONTL | 0 | 3 | — |  |
| IIC_IM_HKONTH | 0 | 3 | — |  |

### IIC_SAP_I1028

**Tipo:** Table  
**Descripción:** i1028 Int. Status  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE | 2 | 10 | — |  |
| IIC_CALL_NBR | 2 | 3 | — |  |
| IIC_TOTAL_COUNT | 2 | 3 | — |  |
| IIC_OK_COUNT | 2 | 3 | — |  |
| IIC_ERROR_COUNT | 2 | 3 | — |  |


## Fields

### IIC_ERROR_COUNT

**Tipo:** Number  
**Longitud:** 3  

### IIC_IM_FUND

**Tipo:** Character  
**Longitud:** 4  

### IIC_OK_COUNT

**Tipo:** Number  
**Longitud:** 3  

### IIC_TOTAL_COUNT

**Tipo:** Number  
**Longitud:** 3  


## Process Definitions

### IIC_SAPI1028

**Tipo:** Application Engine  
**Run Location:** 2  
**Descripción:** SAP I1028 Interface  
