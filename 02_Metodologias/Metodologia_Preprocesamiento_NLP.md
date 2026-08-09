---
tags:
  - nlp
  - preprocesamiento
  - arquitectura
  - expedientes
---
# 🧠 Metodología de Preprocesamiento de Expedientes Técnicos (Data Pipeline)

## 🎯 Objetivo
Evitar que el agente procese PDFs sucios (Zero-shot sucio) al analizar expedientes masivos (FITSA, EIA, EVAR). Aplicar los principios del Módulo 3 y 4 del Máster IA: **Limpieza de Datos, Normalización y Fragmentación (Chunking)** antes de inyectar contexto al LLM.

## 🛠️ Reglas del Data Pipeline (NLP Aplicado)

### 1. Limpieza de Texto Base (Noise Reduction)
Antes de analizar cualquier PDF de OSCE o MTC, el agente o script debe ejecutar una pasada de limpieza:
- **Remover marcas de agua:** Ignorar textos repetitivos como *"COPIA NO CONTROLADA"* o *"DOCUMENTO BORRADOR"*.
- **Limpiar pies de página y encabezados:** Descartar números de página, sellos notariales y fechas de impresión que rompen la continuidad semántica de los párrafos.
- **Corrección de OCR Pobre:** Detectar saltos de línea artificiales (ej. una palabra cortada por un guion al final de la línea) y unirlos, reconstruyendo oraciones completas.

### 2. Fragmentación Semántica (Chunking Inteligente)
No enviar expedientes de 500 páginas de un solo golpe. Seguir la ley de los Transformers:
- **Separación por Capítulos:** Extraer el índice y fragmentar el texto en bloques lógicos (ej. Capítulo 1, Capítulo 2).
- **Mantener Tablas Intactas:** Las tablas de S10 (presupuestos) y cronogramas **NO** deben dividirse en la mitad. Si un bloque excede el token-limit, el punto de corte debe ser al final de una sección completa, nunca en medio de una tabla.

### 3. Normalización Estructural (Machine Learning Prep)
Las redes neuronales necesitan datos ordenados. 
- Al extraer ACUs (Análisis de Costos Unitarios) de Excel o PDF, forzar un formato JSON o CSV uniforme antes de pedirle a la IA que calcule totales.
- Aplicar expresiones regulares (Regex) para aislar números de partidas (ej. `01.02.03`) de su descripción textual, reduciendo la confusión del LLM al sumar montos.

### 4. Mejora de Contraste para Visión Artificial
Cuando se analicen fotos de fallas geológicas o calicatas (usando `analizador-fotografico-tecnico`):
- Rechazar fotos subexpuestas. 
- Priorizar imágenes donde las texturas del suelo (Geomorfología) sean distinguibles antes de enviarlas al modelo multimodal.

---
> **Regla Maestra:** 
> *Basura entra, basura sale (GIGO).* Un LLM avanzado (como Claude 3.5 Sonnet) alucina un 80% menos si el texto base fue limpiado y despojado de ruido estructural.
