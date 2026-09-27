---
tags: [proyecto, FITSA, HU-112, datos-tecnicos]
tipo: datos
estado: vaciado-parcial (presupuesto + cronograma OK; pendiente: áreas auxiliares, monitoreo, entregables)
actualizado: 2026-08-23
---

# 📐 FITSA HU-112 — Datos Técnicos

Nota de consolidación de los parámetros técnicos del expediente **FITSA Ruta HU-112 (La Esperanza – Callagán Manzano)**.

## Fuente autoritativa

> [!IMPORTANT]
> Los datos se transcriben **desde el Excel aprobado del expediente**, no desde memoria ni versiones previas de esta nota.

```
C:\Users\DESKTOP\OneDrive\DOCUMENTOS-MIGUEL\FITSA-MANTEN- PERIODICO\FITSA- Ruta HU-112 (La Esperanza - Callagan Manzano)\
```

## 1. Identificación del proyecto

| Dato | Valor |
| :--- | :--- |
| Ruta | HU-112 |
| Tramo | Emp. PE-18 A (La Esperanza) – Paucar – Shismay – Parquincho – Linda Linda – Callagán Manzano |
| Progresiva fin | KM 51+987 |
| Longitud | 51.987 km |
| Tipo | Mantenimiento periódico de carretera no concesionada |
| Sistema de coordenadas | EPSG:32718 (UTM WGS84 Zona 18S) |
| Duración cronograma | 60 días (01/04/2026 – 30/05/2026) |

## 2. Presupuesto aprobado (Excel `03.04 PRESUPUESTO TOTAL/presupuestocliente.xls` — verificado 23/08/2026)

| Item | Descripción | Und. | Metrado | Precio S/. | Parcial S/. |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 01 | OBRAS PRELIMINARES | | | | 60,378.48 |
| 01.01 | Movilización y desmovilización de equipos y maquinarias | glb | 1 | 4,668.25 | 4,668.25 |
| 01.02 | Trazo y replanteo | km | 51.99 | 905.29 | 47,066.03 |
| 01.03 | Mantenimiento de tránsito y seguridad vial | glb | 1 | 8,644.20 | 8,644.20 |
| 02 | CONSERVACIÓN DE CALZADA EN AFIRMADO | | | | 1,518,738.83 |
| 02.01 | Reposición de afirmado | m3 | 30,994.67 | 49.00 | 1,518,738.83 |
| 03 | TRANSPORTE | | | | 611,928.00 |
| 03.01 | Transporte de material para afirmado hasta 1 km | m3k | 30,184.67 | 7.75 | 233,931.19 |
| 03.02 | Transporte de material para afirmado > 1 km | m3k | 299,997.47 | 1.26 | 377,996.81 |
| 04 | SEÑALIZACIÓN | | | | 79,391.08 |
| 04.01 | Instalación de postes kilométricos | und | 53 | 190.95 | 10,120.35 |
| 04.02 | Señal preventiva | und | 102 | 501.11 | 51,113.22 |
| 04.03 | Señal reglamentaria | und | 13 | 713.63 | 9,277.19 |
| 04.04 | Señal informativa | und | 4 | 2,220.08 | 8,880.32 |
| 05 | IMPACTO AMBIENTAL | | | | 80,890.29 |
| 05.01 | Plan de Manejo Ambiental | glb | 1 | 80,890.29 | 80,890.29 |

**Resumen económico (verificado aritméticamente):**

| Concepto | S/. |
| :--- | :--- |
| Costo Directo | 2,351,326.68 |
| Gastos Generales (10%) | 235,132.67 |
| Utilidad (8%) | 188,106.13 |
| Sub Total | 2,774,565.48 |
| IGV (18%) | 499,421.79 |
| Costo de ejecución del servicio | 3,273,987.27 |
| Gastos de supervisión (10%) | 327,398.73 |
| **Costo Total del Servicio** | **3,601,386.00** |

> ⚠️ Nota: el literal del Excel dice "DOS MILLONES TRESCIENTOS CINCUENTIUN MIL..." (refiere al costo directo, no al total). Verificar redacción del literal en el documento final.

## 3. Cronograma (carpeta `04. CRONOGRAMA DE EJECUCION/` — revisión en curso 23/08)

| Partida | Duración | Inicio | Fin |
| :--- | :--- | :--- | :--- |
| OBRAS PRELIMINARES | 15 d | 01/04/26 | 15/04/26 |
| Conservación de calzada en afirmado | 45 d | 06/04/26 | 20/05/26 |
| Transportes | 48 d | 03/04/26 | 20/05/26 |
| Señalización | 10 d | 21/05/26 | 30/05/26 |
| Plan de Manejo Ambiental | 60 d | 01/04/26 | 30/05/26 |

> ⚠️ Hallazgo preliminar (para la revisión Antigravity): el GANTT lista "MATERIAL GRANULAR DE CANTERA PARA ESTABILIZADO E=0.15 (45 d)" que NO aparece como partida en el presupuesto aprobado (solo "Reposición de afirmado" 02.01). Verificar si es partida desagregada o error.

## Bloques de consolidación

| Bloque | Estado |
| :--- | :--- |
| Presupuesto ambiental — partidas y montos | ✅ vaciado 23/08 (tabla completa arriba) |
| Metas físicas del tramo | ✅ parcial (L=51.987 km; metrados por partida en tabla) |
| Cronograma de monitoreo | ⬜ pendiente (buscar en Gestion_Ambiental_y_PMA.md) |
| Áreas auxiliares — coordenadas UTM (EPSG:32718) | ⬜ pendiente |
| Lista de entregables | ⬜ pendiente |

## Convención geodésica
Todos los shapefiles del proyecto usan **EPSG:32718** — UTM WGS 84, Zona 18 Sur.

## Relacionadas
[[MOC_Ruta_HU_112]] | [[Gestion_Ambiental_y_PMA]] | [[Memoria_Descriptiva]]
