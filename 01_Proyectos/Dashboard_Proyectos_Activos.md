---
tags:
  - Dashboard
  - Proyectos
  - Control
aliases:
  - Monitor de Portafolio
---

# 📊 Dashboard "Live" de Proyectos
*Última actualización: 2026-08-02 14:50:28*

> [!NOTE] 
> Este tablero es generado y actualizado automáticamente por la skill `dashboard-proyectos-live` escaneando el disco duro local.

## 🧭 Mapa de Estado de Expedientes

```mermaid
flowchart LR
    Portafolio[(Portafolio Local)]
    Portafolio --> P0["📁 [[FITSA|FITSA]]- Ruta HU-112 (La Esperanza - Callagan Manzano)"]
    P0 --- P0_EVAR([EVAR: 🟢 OK])
    P0 --- P0_AMB([Ambiental: 🔴 PENDIENTE])
    P0 --- P0_PRES([Presupuesto: 🔴 PENDIENTE])
    style P0_EVAR fill:#d4edda,stroke:#28a745
    style P0_AMB fill:#f8d7da,stroke:#dc3545
    style P0_PRES fill:#f8d7da,stroke:#dc3545
```

## 📝 Detalle de Proyectos

| Proyecto | Riesgos (EVAR) | Ambiental | Presupuesto |
| :--- | :---: | :---: | :---: |
| FITSA- Ruta HU-112 (La Esperanza - Callagan Manzano) | ✅ | ❌ | ❌ |
