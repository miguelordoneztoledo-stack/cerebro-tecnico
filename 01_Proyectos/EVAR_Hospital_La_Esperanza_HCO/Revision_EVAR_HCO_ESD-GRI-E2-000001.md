---
tags: [evar, cenepred, hospital, huanuco, revision-tecnica, anin]
tipo: auditoria
proyecto: Hospital La Esperanza - Amarilis - Huánuco (HCO)
codigo_documento: 100030-JYS01-000-XXX-ESD-GRI-E2-000001
fecha_revision: 2026-10-01
estado: observado
---

# Revisión EVAR multipeligro (MHA) — Hospital La Esperanza, Amarilis (HCO)

> [!WARNING] Documento observado
> El EVAR R00 del 28/09/2026 (158 pág., contrato ANIN, código de idea 350185) **no debe aprobarse en su estado actual**. Se identificaron **8 hallazgos bloqueantes** y 24 mayores. Cuello de botella principal: el EVAR no integra los estudios insumo del propio expediente.

## Ficha

| Campo | Valor |
| :--- | :--- |
| Documento | `100030-JYS01-000-XXX-ESD-GRI-E2-000001` — Estudios de Evaluación de Riesgos de Múltiples Peligros (MHA) |
| Proyecto | Creación de atención de servicios de salud hospitalarios en La Esperanza, distrito de Amarilis, Huánuco |
| Entidad | Autoridad Nacional de Infraestructura (ANIN) — PCM |
| Código de idea | 350185 |
| Extensión / revisión | 158 páginas — R00, emisión 28/09/2026 |
| Peligros evaluados | inundación pluvial, inundación fluvial, sismo |
| Elaboró | Ing. Geógrafo Eddy Charlie Condezo Chuquijajas — R.J. N.° 017-2019-CENEPRED/J |
| Revisó / Aprobó | Jesús Choque (Kp 2) / Carlos Gallo (KP 1) |

## Estudios insumo del mismo expediente (no citados en el EVAR)

- `...-INF-GTC-E2-000002` — Estudio de Peligro Sísmico, 447 p. (Luis Fernando Vergaray Astupiña)
- `...-INF-HGE-E2-000001` — Estudio de Evaluación de Riesgos de Inundación, 106 p. (Eddy Charlie Condezo)
- `...-INF-HGE-E2-000003` — Estudio Hidrológico, 243 p. (Patricio Pareja Calderón)

## Hallazgos bloqueantes

1. **Demanda sísmica subestimada.** El EVAR usa PGA 0.23 g y Z = 0.25 (mapa regional IGP / E.030). El estudio de sitio del mismo expediente determina **Z de sitio = 0.313 g (S1, Vs30 640 m/s) y 0.356 g (S2, Vs30 420 m/s)** y ordena emplear sus valores (Cuadro 14, p. 66). Desfase de 20 % a 42 % a la baja.
2. **Dos descriptores de altura de inundación pluvial para el mismo predio:** «De 20 a 30 cm» (3.5.2, p. 66) vs «De 10 a 20 cm» (3.5.4, p. 73 y conclusión p. 147) → según el Cuadro 46, cambia el nivel de MEDIO a ALTO.
3. **Tirantes dentro del predio contradichos:** el EVAR afirma que «las alturas superiores a 40 cm se localizan fuera del predio» (p. 65); el estudio de inundación mide **28,5 m² > 0,30 m y 6,0 m² > 0,50 m dentro del predio** (18 076,7 m²), con máximo local de 0,423 m (PC-05).
4. **Escala de vulnerabilidad duplicada:** Cuadro 129 (p. 115) fija 0.085/0.150/0.263/0.453; la matriz pluvial (Cuadro 132, p. 119) usa 0.080/0.146/0.264/0.463 **y arrastra esa misma escala a sus filas de peligro**. Las matrices sí reproducen P × V; el error es de asignación de escalas.
5. **Valores P y V del predio no publicados.** No hay valor de vulnerabilidad del predio, ni fórmula exposición/fragilidad/resiliencia, ni matriz de la dimensión económica, ni árboles de ponderación del Cap. III: el nivel declarado no es reproducible.
6. **Capítulo VI no controla el riesgo.** Sin riesgo residual ni verificación de efectividad; pluvial y fluvial declarados «nivel 3 - Inaceptable» y el sismo «2 - tolerable» con prioridad III, sin prioridad I o II para los inaceptables. El mismo nivel numérico se rotula «Alto» (pluvial/fluvial) y «Medio» (sismo).
7. **Conclusiones vs recomendaciones:** «riesgo alto por inundación pluvial» (p. 147) frente a «reducción del riesgo medio por inundación pluvial» (p. 148).
8. **Sección ANEXOS vacía** (p. 152) pese a remitir al «Anexo Hidrológico» y al «Anexo 3 del IGP»; y perfil de suelo S2 adoptado sin estudio geotécnico del predio (se usa calicata referencial de INDECI-PNUD).

## Hallazgos mayores destacados

- Peligro caracterizado sin el modelamiento HEC-RAS 2D disponible (TR50/TR100, caudal 13,89 m³/s, quebrada Jancao 65,9 m³/s, tirantes PC-01 a PC-06).
- Escala sísmica del manual CENEPRED sin adaptar en el Gráfico 26 (p. 64): «magnitud > 7.9 Mw», «aceleración > 0.25 gal», «formación Chimú», techo 0.447.
- Descriptor «Malo» definido sobre SUCS distintos: `CL-OL-ML` (Cuadro 18, p. 41) vs `CL-OL-MH` (Cuadros 76/77, p. 91). El suelo del predio es ML/CL → asignación indeterminada.
- Umbral MUY ALTO/ALTO pluvial: 0.244 (Cuadro 45, p. 73) vs 0.264 (Cuadro 46, p. 74).
- Descriptor «S3–S4 transición» sin definición en la tabla E.030 transcrita (Cuadro 23).
- Borde libre de 0,40 m en el EVAR frente a los 0,50 m exigidos por los TdR (estudio de inundación, p. 98).
- Norma mal designada: «A.040 – Saneamiento» (A.040 del RNE es Educación; corresponde A.050 Salud e IS.010).
- Medidas de 5.11 sin metrado, ACU ni presupuesto, y declaradas «orientadoras».
- Tres áreas/perímetros distintos del mismo predio (18 076,94 m² / 18 039,40 m² / 595,95 ml) y altitud 1 926,25 vs 1 900,00 msnm.

## Lo que está bien (no reabrir)

- 156 cuadros, 18 figuras y 30 gráficos **sin duplicados ni faltantes**; paginación correcta en las 158 páginas.
- AHP correctamente calculado: RC recalculado entre 0.004 y 0.055, con RI de Saaty correcto (n=3 → 0.58; n=5 → 1.12). Consistencia verificada en los Cuadros 28 y 49.
- Exclusión de peligros justificada: fallas (SIGRID) y movimientos en masa (susceptibilidad muy baja, relieve llano).

## Ruta recomendada

1. **Mesa 01 Expedientes y Obras:** matriz de valores únicos entre los cuatro documentos (aceleración, TR, caudales, tirantes, suelo, descriptores). Habilita todo lo demás.
2. **Mesa 02 Riesgos y SST:** recalcular peligro sísmico con Z de sitio; reevaluar descriptor de inundación con los tirantes modelados; unificar escala de vulnerabilidad y publicar V del predio.
3. **Mesa 02:** rehacer matriz pluvial, homogeneizar topes de riesgo, cerrar conclusión/recomendación y completar el Cap. VI con riesgo residual.
4. **Mesa 01:** medidas con metrado y ACU en soles, borde libre 0,50 m, corrección A.040 → A.050 / IS.010, EMS del predio como anexo.
5. **Mesa 02:** forma y ortografía conforme a `ESTANDAR_CALIDAD_DOCUMENTAL.md`.

## Insumo crítico faltante

**Términos de Referencia del contrato ANIN** (alcance del EVAR, borde libre exigido, peligros obligatorios, plazo). Sin ellos no puede establecerse si la omisión de los estudios insumo es incumplimiento contractual o decisión de alcance. Complementarios: EMS del predio con Vs30 justificado, archivo AHP sin redondear, planilla de cálculo con V y R numéricos.

## Artefactos

- Informe consolidado: `C:\IA_Proyectos\artifacts\results\INFORME_REVISION_EVAR_HCO_ESD-GRI-E2-000001.md`
- Subauditorías: `AGT_AUDIT_EVAR_CAP3.md`, `AGT_AUDIT_EVAR_CAP45.md`, `AGT_AUDIT_EVAR_MARCOS.md`
- Texto extraído: `evar_hco_texto_completo.txt`, `insumo_peligro_sismico_completo.txt`, `insumo_inundacion_completo.txt`
- Fuente original: `C:\Users\DESKTOP\OneDrive\Desktop\CONSULTORA-DOCENCIA UDH\3. OBRAS CIVILES\HOSPITAL-HCO\OCTUBRE\SEMANA 1\EVAR\`

---

## 🔗 Enlaces
- Hub central: [[MOC_Master_Cerebro_Tecnico]]
- Metodología: [[Metodologia_EVAR_CENEPRED]] · [[AHP_Saaty_EVAR_EVAR-IIEE-IPARIA]]
- Antecedentes EVAR: [[Dictamen_EVAR_Creacion_Defensas_Ribereñas_Conchumayo]] · [[Absolucion_EVAR_EVAR-IIEE-IPARIA]]
