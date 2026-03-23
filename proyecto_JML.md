# Proyecto PeopleSoft: CLAGP_8619_JML

Ticket 8619 Cert Renta LCL_HVA

## Resumen del Proyecto

| Tipo de Objeto | Cantidad |
|----------------|----------|
| Records | 2 |
| Pages | 1 |
| SQL Objects | 1 |

---
## Records

### LCL_RUNCERT_AET

**Tipo:** Table  
**Descripción:** Record Certificado de Renta  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| PROCESS_INSTANCE | 2 | 10 | — |  |
| OPRID | 0 | 30 | — |  |
| RUN_CNTL_ID | 0 | 30 | — |  |
| YEAR | 0 | 4 | — |  |
| EMPLID | 0 | 11 | — |  |
| GPCL_PUB_SS | 0 | 1 | — |  |

### LCL_RUN_CERT_RE

**Tipo:** Table  
**Descripción:** Record Certificado de Renta  

#### Campos

| Campo | Tipo | Long. | Flags | Label |
|-------|------|-------|-------|-------|
| OPRID | 0 | 30 | — |  |
| RUN_CNTL_ID | 0 | 30 | — |  |
| YEAR | 0 | 4 | — |  |
| EMPLID | 0 | 11 | — |  |
| GPCL_PUB_SS | 0 | 1 | — |  |

---
## Pages

### LCL_CERT_RENTA

**Tipo:** Standard  
**Descripción:** Página Certificado de Renta  
---
## SQL Objects

### GPCL_CERRRENTCL_SQL


```sql
SELECT DISTINCT A.EMPLID , B.FPY_PERSON_NUM FROM %Table(LCL_CERTREN_TMP) A , %Table(FPY_EMPLID_XREF) B WHERE A.PROCESS_INSTANCE=:1 AND A.EMPLID = B.EMPLID AND B.PROCESS_INSTANCE = ( SELECT MAX(B1.PROCESS_INSTANCE) FROM %Table(FPY_EMPLID_XREF) B1 WHERE B1.EMPLID = B.EMPLID)
```
