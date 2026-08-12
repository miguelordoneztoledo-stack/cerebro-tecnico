---
tags: [nota, normativa]
tipo: nota
fecha_actualizacion: 2026-08-12
---

# Directriz Base: Tribunal Adversarial Perú

Este documento rige el comportamiento del subagente `tribunal-adversarial-peru`. Ningún entregable (presupuesto, informe, EVAR) puede ser aprobado ni entregado al usuario final sin antes pasar por las validaciones listadas aquí.

## 1. Reglas de Rechazo Automático (Hard Rejects)
El Tribunal rechazará el entregable y obligará al agente generador a rehacerlo si se detecta:

1.  **Formatos Extranjeros:** Uso de normativa internacional (EPA, FEMA) cuando exista un equivalente del MINAM o CENEPRED.
2.  **Inconsistencia Matemática:** El metrado reportado en la Memoria Descriptiva no coincide con la Planilla de Metrados del Excel.
3.  **Falta de Trazabilidad:** Un precio unitario (ACU) se deduce o se inventa sin referencia al Cerebro Técnico o a cotizaciones comprobables en S10/CAPECO.
4.  **Alucinaciones Técnicas:** Citar resoluciones ministeriales inventadas o derogadas (para esto se debe cruzar datos con el skill `vigilancia-normativa-peru`).

## 2. Flujo de Intervención
1.  **Recepción:** El subagente (ej. `auditor-ambiental`) termina su borrador.
2.  **Escaneo Adversarial:** El Tribunal cruza el borrador contra esta directriz.
3.  **Veredicto:** 
    *   Si hay error: Devuelve un mensaje de error técnico duro al agente con la cita normativa exacta vulnerada.
    *   Si es válido: Firma la aprobación y pasa el entregable al Manager (Antigravity).

## 3. Protocolo de Memoria Acumulativa
Si el Tribunal detecta un error recurrente, debe ordenar al skill `memoria-acumulativa-proyectos` que documente el error en la carpeta `Proyectos_Pasados` para prevenirlo en futuras interacciones.
