---
cssclasses:
  - dashboard
---

# 🏢 Panel de Control: Oficina de IA

Este panel orquesta y monitorea el estado de los proyectos delegados a los subagentes autónomos.

## 📊 Estado de Proyectos Actuales

| Expediente / Proyecto | Fase Actual | Subagente Asignado | Estado | Progreso |
| :--- | :--- | :--- | :--- | :--- |
| **FITSA - Ruta HU-112** | Generación EVAR | `auditor-riesgos` | 🟢 Completado | [x] 100% |
| **FITSA - Ruta HU-112** | Informe Ambiental | `auditor-ambiental`| 🟡 En Espera | [ ] 0% |
| **Plantilla Piloto** | Extracción TDR | `research` | ⚪ Pendiente | [ ] 0% |

---

## 🤖 Estado de la Fuerza Laboral (Agentes)

```mermaid
graph LR
    Manager[🧠 Manager Antigravity] -->|Rutea| Hecras[🌊 Analista Hidráulico]
    Manager -->|Rutea| SST[👷 Especialista SST]
    Manager -->|Rutea| Amb[🌿 Auditor Ambiental]
    Manager -->|Rutea| Riesgos[🌋 Auditor EVAR]
    
    style Manager fill:#2874a6,stroke:#154360,stroke-width:2px,color:#fff
    style Hecras fill:#d5f5e3,stroke:#239b56
    style SST fill:#d5f5e3,stroke:#239b56
    style Amb fill:#d5f5e3,stroke:#239b56
    style Riesgos fill:#d5f5e3,stroke:#239b56
```

## 📋 Registro de Tareas del Tribunal Adversarial
- [x] Validación de márgenes y formato en Word (Paso 1)
- [x] Verificación de rutas absolutas vs relativas en scripts de generación.
- [ ] Auditoría de precios unitarios vs Base de Datos Histórica.
