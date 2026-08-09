---
tags:
  - IA
  - skills
  - automatizacion
  - fitsa
  - orquestacion
aliases:
  - Suite Avanzada de Expedientes
---

# 🚀 Suite de Herramientas Avanzadas (Estilo Claude Code)

Este documento registra la implementación de la nueva suite de habilidades autónomas instaladas en `C:\IA_Proyectos\skills\`. Estas herramientas fueron inspiradas en las capacidades avanzadas de Claude Code (Codex, Remote Control, MCP Visual) y adaptadas para el flujo de trabajo de [[01_Proyectos|[[01_Proyectos]]]] y proyectos como [[fitsa_hu112_datos_tecnicos]].

## 🛠️ Herramientas Implementadas

### 1. [[mapeador-visual-expedientes]]
- **Concepto:** Emula la integración de "System Design" y conectores MCP.
- **Función:** Escanea la estructura completa de un expediente (hasta 3 niveles) y genera automáticamente un `Dashboard_Mapa_Expediente.html` utilizando diagramas interactivos de Mermaid JS.
- **Categorización:** Distingue visualmente entre Informes (Word), Datos/Metrados (Excel) y Resoluciones (PDF).

### 2. [[orquestador-fitsa-multisession]]
- **Concepto:** Emula la delegación a sub-modelos (Codex) y ejecución asíncrona (Remote Control `/rc`).
- **Función:** Permite invocar a 3 especialistas en paralelo mediante el agente principal:
  1. **Auditor Ambiental:** Especialista en Línea Base y Matrices Ambientales.
  2. **Auditor de Riesgos:** Especialista en cálculos EVAR/CENEPRED.
  3. **Auditor Presupuestal:** Especialista en ACU y presupuestos CAPECO (Soles S/).
- **Ejecución:** Trabaja en segundo plano (Background Tasks) para que el ingeniero no deba bloquear su interfaz mientras ocurre el escaneo masivo de documentos.

### 3. [[generador-assets-ingenieria]]
- **Concepto:** Integración con APIs de generación multimedia (Image Generation).
- **Función:** Permite al agente generar automáticamente recursos visuales (ej. paneles fotográficos, secciones de carretera andina, esquemas lógicos) para ser insertados directamente en los informes de Word (.docx) del expediente.

---
**Notas Adicionales:** 
Todas estas herramientas cumplen con la normativa del **Modo País (Perú)** y respetan la regla **Cero Fluff** para entrega de resultados quirúrgicos e inmediatos. Fueron probadas exitosamente durante la orquestación del proyecto HU-112.
