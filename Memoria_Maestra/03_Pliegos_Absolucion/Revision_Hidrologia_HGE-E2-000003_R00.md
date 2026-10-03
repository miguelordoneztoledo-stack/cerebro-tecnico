---
tags: [pliego, revision, hidrologia, hospital-la-esperanza, ANIN]
tipo: nota
fecha: 2026-09-28
documento_revisado: 100030-JYS01-000-XXX-INF-HGE-E2-000003 (R00, 263 págs., emisión 11/09/2026)
estado: observado
---

# Revisión forense · Estudio de Hidrología · Hospital La Esperanza (Amarilis, Huánuco)

Entregable completo: `PLIEGO_OBS_Hidrologia_HGE-E2-000003_R00.docx` (misma carpeta). Recomendación: **OBSERVADO** (no aceptable en R00). Relacionado: [[Metodologia_EVAR_CENEPRED]] · [[MOC_Master_Cerebro_Tecnico]].

## Observaciones críticas / altas
| N° | Tema | Evidencia clave |
|---|---|---|
| OBS-01 | Caudal de desborde 12.24 m³/s vs canal levantado | Canal 0.30–0.45 m de ancho, tubería Ø0.20 m → capacidad 0.3–1.15 m³/s (tubería 0.07–0.10). Factor 10–40 |
| OBS-02 | Calibración mal condicionada | 12.6→25.2 m³/s solo cambia 0.09 m el nivel (0.007 m por m³/s). 12.73 no es el resultado del optimizador (ratio 1.951 → 19.5 m³/s). Q local congruente con la huella ≈ 2.2–2.7 m³/s |
| OBS-03 | Fig. 4-1 pico 13.22 m³/s ≠ Cuadro 3-11 (13.89) | 13.22 = 12.73 + 0.49 (TR 2.33). Base 12.73 vs 12.24 |
| OBS-04 | «TR 25/50/100» no dependen del TR | 15 min de lluvia sobre el mismo caudal; simulación de 60 min; ≈32 700 m³ entran (1.8 m de lámina); poza séptica = hueco del DEM |
| OBS-05 | IDF del informe = 55 % de IDF SENAMHI citada | 1 h: 11.27/22.47 vs 20.8/39.8 mm/h; regresión circular (n = 0.75 exacto) |
| OBS-06 | CN 97, C 0.75, tc 15 min | Pico TR100 microcuenca 0.26–3.8 m³/s según CN e IDF |
| OBS-07 | Sin consistencia/homogeneidad | Pettitt 1997 (p≈0.016); IC90 TR100 = 39–64 mm |
| OBS-08 | Cunetas supercríticas | Fr 3.3–3.7, 7–7.7 m/s; resalto 2.31/1.72 m vs secciones 0.90/0.60 m; sobreelevación 0.5–0.6 m (r = 5 m) |
| OBS-09 | TR 35 años de alcantarillas viales | Riesgo 35 % / 15 años; hospital = infraestructura esencial |
| OBS-10 | Peligro/riesgo | Sin d·v; hospital con 0.10–0.40 m = «riesgo medio» |
| OBS-11 | Alcances omitidos | Jancao, sedimentos, geotecnia, Niño Costero, parámetros HEC-RAS/HMS |

## Verificado conforme
Serie 1981–2025, estadísticos, Log-Pearson III, K-S, Peschke, IDF, hietogramas, tc FAA, área/perímetro del predio, cuneta interior (0.40 m³/s).

## Acciones pendientes
- [ ] Decidir aceptación A/B/C en el sello ANIN.
- [ ] Solicitar al consultor el paquete del Anexo C del pliego (archivos HEC, topografía del canal, hidrología de Jancao).
- [ ] Verificar M-12: cómputos HEC-HMS del 18/09/2026 posteriores a la emisión del 11/09/2026.

> Cifras de sensibilidad hechas con reimplementación propia (SCS-CN + UH SCS); no reemplazan una corrida de los modelos del consultor.
