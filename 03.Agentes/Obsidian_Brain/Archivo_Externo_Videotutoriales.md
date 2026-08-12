---
tags: [archivo, referencia, indice]
tipo: referencia
fecha_archivo: 2026-08-12
---

# 🗄️ Archivo Externo — Videotutoriales e Indexación Masiva

El corpus `Videotutoriales_MD` fue **retirado de la bóveda el 2026-08-12** por saturación: 8,221 notas que representaban el 98% del vault y ahogaban grafo, búsqueda global y switcher.

## Ubicación actual

```
C:\IA_Proyectos\Archivo_Videotutoriales_MD\
```

| Subcarpeta | Notas | Qué contiene |
| :--- | ---: | :--- |
| `_CONTENIDO_REAL\` | 843 | Notas > 20 KB con texto extraído aprovechable |
| _(raíz)_ | 669 | Notas intermedias (600 B – 20 KB) |
| `_CASCARAS_VACIAS\` | 6,709 | Punteros sin contenido a archivos `.dwg`, `.dwl2`, `.pptx` en la unidad `H:` (no montada) |
| `_STUBS_DUPLICADOS_RETIRADOS\` | 29 | MOC duplicados que competían con los reales |
| `MOC_Videotutoriales_Ingenieria.md` | — | Índice original (538 KB) |

## Por qué se archivó y no se borró

Nada fue eliminado. Las 843 notas de `_CONTENIDO_REAL\` conservan valor: son extracciones de PDFs técnicos (normativa MTC, hidráulica, sismorresistencia, EVAR). El criterio es **reingresar solo lo que se use**, con nombre propio y tags, no reimportar el bloque completo.

## 📇 Índice temático del corpus

Las 843 notas de `_CONTENIDO_REAL\` están catalogadas por tema en:

```
C:\IA_Proyectos\Archivo_Videotutoriales_MD\INDICE_TEMATICO.md
```

| Tema | Docs |
| :--- | ---: |
| GIS / Topografía / Dron | 189 |
| Investigación / Estadística | 182 |
| EVAR / Gestión de Riesgos | 124 |
| Ambiental / EIA | 106 |
| **Colección Enciclopedia OIT (SST)** | **94** |
| Hidráulica / Hidrología | 78 |
| SST / Seguridad | 86 |
| Estructuras / Concreto | 27 |
| Costos / Contrataciones | 18 |
| Vial / MTC | 17 |
| Geotecnia / Suelos | 14 |

De ellas, **77 son normas, manuales o guías oficiales** identificadas (Ley 29664, DS 048-2011-PCM, PLANAGERD, ABC del SENACE, ISO 45001, manuales MTC, parámetros ANA, errores frecuentes en expedientes OSCE, entre otras).

El hallazgo de mayor valor es la **Enciclopedia de Salud y Seguridad en el Trabajo de la OIT** — 94 capítulos completos que estaban dispersos con nombres numéricos ilegibles (`33.md`, `48.md`…) y ahora están identificados por tema.

## Cómo reingresar una nota

1. Localizarla en `_CONTENIDO_REAL\`.
2. Copiarla a la carpeta temática que corresponda (`02_Metodologias\`, `Normativa\`, …).
3. Renombrarla con nombre descriptivo (no el del PDF original).
4. Añadir frontmatter con `tags` y `tipo`.
5. Enlazarla desde su MOC temático.

> [!NOTE]
> Las 6,709 cáscaras de `_CASCARAS_VACIAS\` no tienen contenido recuperable: solo registran la ruta original en la unidad `H:`. Sirven como inventario de qué existía, nada más.

## Relacionadas
[[MOC_Master_Cerebro_Tecnico]] | [[MOC_Arquitectura_IA]]
