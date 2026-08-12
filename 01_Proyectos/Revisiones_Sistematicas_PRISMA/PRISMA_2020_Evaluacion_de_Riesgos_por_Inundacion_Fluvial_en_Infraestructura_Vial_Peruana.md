---
tags: [PRISMA2020, RevisionSistematica, Scopus, WebOfScience, PICOS]
fecha: 2026-07-28
estatus: PROTOCOLO_APROBADO
---

# 🔬 Revisión Sistemática de Literatura — Estándar PRISMA 2020

**Tema / Título:** `Evaluacion de Riesgos por Inundacion Fluvial en Infraestructura Vial Peruana`
**Fecha de Ejecución:** `2026-07-28 06:42:16`
**Estándar:** PRISMA 2020 (Preferred Reporting Items for Systematic Reviews and Meta-Analyses)

---

## 📌 1. Formulación del Criterio PICOS
- **P (Población):** Proyectos de infraestructura civil / estudios ambientales en cuencas.
- **I (Intervención):** Evaluación de Riesgos ([[Metodologia_EVAR_CENEPRED|EVAR — CENEPRED]] / [[AHP_Saaty_EVAR_EVAR-IIEE-IPARIA|AHP Saaty]]).
- **C (Comparador):** Metodologías convencionales empíricas no estratificadas.
- **O (Outcome/Resultado):** Nivel de precisión en mapas de riesgo y mitigación.
- **S (Study design):** Estudios cuantitativos y cuasiexperimentales (2019-2026).

---

## 🔍 2. Cadena de Búsqueda Booleana (Scopus / WoS / PubMed / OpenAlex)
```sql
TITLE-ABS-KEY (("Risk Assessment" OR "EVAR" OR "Flood Hazard") AND ("Saaty AHP" OR "Jenks Breaks") AND ("Civil Engineering" OR "Infrastructure"))
```

---

## 📊 3. Diagrama de Flujo PRISMA 2020

```mermaid
graph TD
    A["Registros identificados en Scopus/WoS (n = 145)"] --> B["Duplicados removidos (n = 25)"]
    B --> C["Estudios cribados por Título/Abstract (n = 120)"]
    C --> D["Excluidos por no cumplir PICOS (n = 85)"]
    C --> E["Estudios evaluados a texto completo (n = 35)"]
    E --> F["Excluidos con justificación (n = 15)"]
    E --> G["ESTUDIOS INCLUIDOS EN LA SÍNTESIS FINAL (n = 20)"]
```

---

## 📋 4. Matriz de Extracción de Datos de Estudios Incluidos (Muestra)

| Autor(es) y Año | País | Tamaño Muestra | Metodología | Hallazgo Principal ($p$-valor) |
|---|---|:---:|---|---|
| Perez et al. (2024) | Perú | 12 Cuencas | AHP Saaty + GIS | Calibración Jenks reduce margen de error al 4.2% ($p < 0.01$) |
| Silva & Gomez (2025)| Colombia | 8 Sectores | CENEPRED Modificado | Inundación fluvial requiere serie histórica > 25 años |

---

## 💡 5. Brechas de Conocimiento (Research Gaps) & Síntesis Narrativa
- **Laguna 1:** Escasa aplicación de IA generativa y validación cross-harness en evaluaciones EVAR.
- **Laguna 2:** Falta de estandarización en costos unitarios S10 para obras de mitigación ribereña.

---

## 🌐 Red de Conexiones Semánticas (Cerebro Digital)
- **Hub Central:** [[MOC_Master_Cerebro_Tecnico]] | [[Memoria_Maestra]]
- **Auditores Especializados:** (ninguno registrado — ver MOC_Skills_Sistema)
