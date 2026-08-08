# 📚 MOC: Evaluación de Propiedades Mecánicas y Huella de Carbono — Tesis Luz Clarita

**Autor:** Ing. Luz Clarita Valdivia Martel
**Institución:** Universidad Nacional Hermilio Valdizán (UNHEVAL)
**Escuela de Posgrado:** Maestría en Diseño y Construcción de Obras Viales
**Fecha:** Mayo 2026
**Bóveda Relacionada:** [[MOC_UDH_Academico]], [[MOC_Quimica_Ambiental]], [[MOC_Master_Gestion_Riesgos]]

---

## 📝 1. Resumen de la Investigación

La investigación evalúa el efecto técnico y ecológico de incorporar **partículas de caucho reciclado de neumáticos** como sustituto del agregado fino en mezclas de concreto destinadas a pavimentos rígidos. El objetivo declarado fue *"Calcular cómo varían las propiedades mecánicas, la durabilidad y la huella de carbono del concreto para pavimentos con la adición de productos de llantas recicladas"*.

### Mezclas Evaluadas:
- **MP (0%):** Mezcla Patrón (Concreto Convencional).
- **MCR-1 (10%):** Adición de 10% de caucho reciclado.
- **MCR-2 (20%):** Adición de 20% de caucho reciclado.
- **MCR-3 (30%):** Adición de 30% de caucho reciclado.
- **MCR-4 (40%):** Adición de 40% de caucho reciclado.

---

## 📊 2. Ensayos de Laboratorio: Resistencia a la Compresión ($f'_c$)

A continuación se tabulan los resultados reales registrados en las probetas ensayadas a los 7, 14 y 28 días de curado en prensa hidráulica (NTP 339.034 / ASTM C39):

| Mezcla / Dosificación | Resistencia 7 días ($kg/cm^2$) | Resistencia 14 días ($kg/cm^2$) | Resistencia 28 días ($kg/cm^2$) | Variación Real a 28 días (%) |
| :--- | :---: | :---: | :---: | :---: |
| **MP (0% Caucho)** | 231.00 | 259.33 | **280.00** | **0.0% (Patrón)** |
| **MCR-1 (10% Caucho)** | 156.67 | 181.33 | **193.67** | **⚠️ -30.8%** |
| **MCR-2 (20% Caucho)** | 95.00 | 103.33 | **114.00** | **❌ -59.3%** |
| **MCR-3 (30% Caucho)** | 62.00 | 70.00 | **82.67** | **❌ -70.5%** |
| **MCR-4 (40% Caucho)** | 50.00 | 55.33 | **65.33** | **❌ -76.7%** |

> [!CAUTION] Alerta Crítica de Ingeniería
> Físicamente, la incorporación de caucho reciclado produce una **pérdida severa de la resistencia a la compresión**. A mayor porcentaje de caucho, menor es la capacidad de carga del concreto. A los 28 días, el concreto decae de un rango estructural apto para pavimentos ($280\ kg/cm^2$) a un rango de mortero extremadamente débil ($65.33\ kg/cm^2$), lo que representa una **caída de hasta -76.7%**.

---

## ⚠️ 3. Auditoría de Errores Críticos Detectados en el Borrador

Un análisis exhaustivo del borrador final reveló dos inconsistencias de extrema gravedad que requieren sincera corrección técnica antes de la sustentación formal:

### A. La Contradicción Matemática Aritmética
- **Declaración en el Borrador:** En el *Resumen* e *Introducción*, la tesista afirma que *"la mezcla MCR-4 (40% de caucho) logró un incremento del 27.2% en resistencia en comparación con el concreto tradicional"*.
- **Causa del Error:** La tesista confundió el ratio de retención con el ratio de incremento. La mezcla MCR-4 retiene únicamente el **23.3%** ($65.33 / 280.00$) de la resistencia patrón, perdiendo el **76.7%** ($100\% - 23.3\%$). Es un error de interpretación grave presentar una caída catastrófica de $280\ kg/cm^2$ a $65\ kg/cm^2$ como un "incremento".

### B. El Sesgo en la Prueba No Paramétrica de Kruskal-Wallis (SPSS)
La tesista concluyó mediante la prueba de Kruskal-Wallis en SPSS que *"la adición de caucho de 10% a 40% no afecta significativamente la resistencia a la compresión y flexión del concreto viales"* (obteniendo un p-valor de **0.204** para compresión y **0.051** para abrasión).

* **Falla de Diseño Muestral:** En el software SPSS, la base de datos se cargó desequilibrada: **$N = 1$ para la mezcla patrón (MP)** y **$N = 3$ para cada grupo MCR**. Al excluir dos probetas del grupo control, el análisis pierde consistencia de rangos.
* **Falta de Potencia Estadística:** Un tamaño de muestra total de solo **$N = 13$** probetas es incapaz de alcanzar la significancia estadística requerida, incluso si las diferencias físicas reales son abismales.
* **Peligro Conceptual:** Afirmar ante un jurado de posgrado que una reducción de más de las tres cuartas partes de la resistencia estructural "no es significativa" representa una negligencia técnica que causaría la desaprobación inmediata.

---

## 🍃 4. Huella de Carbono y Sostenibilidad

En términos de sostenibilidad ambiental (análisis Kruskal-Wallis para $CO_2$-eq, SPSS v.25), se observaron los siguientes valores de impacto ecológico:

* La mezcla **MCR-3 (30% de caucho)** registró la huella de carbono más baja, alcanzando **26.02 kg CO₂-eq**, representando un beneficio ambiental importante debido a la reutilización y reciclaje de llantas de desecho.
* Sin embargo, debido al mismo sesgo de muestra reducida, la prueba estadística arrojó un p-valor de **0.067** (superior a 0.05), indicando que a nivel estadístico no hay diferencias concluyentes por dosificación, aun cuando hay una tendencia ecológica positiva notable.

---

## 🛠️ 5. Hoja de Ruta para Reestructuración y Sinceramiento Técnico

Para asegurar la aprobación de la tesis en la UNHEVAL, se proponen las siguientes acciones correctivas:
1. **Sincerar las Conclusiones:** Modificar la redacción para indicar que la adición de caucho reduce la resistencia a compresión y flexión, posicionando el material **no como concreto estructural para pavimentos de alta velocidad**, sino como **concreto ciclovía, subbases, bermas de estacionamiento o pavimentos peatonales** de baja solicitación de carga.
2. **Re-analizar en SPSS:** Cargar la base de datos de manera equilibrada ($N=3$ por grupo, total $N=15$) y aplicar pruebas post-hoc que demuestren que el MCR-1 ($193.67\ kg/cm^2$) representa la dosificación óptima para pavimentos de tránsito ligero.
3. **Resaltar la Economía Circular:** Enfocar el valor principal del estudio en el análisis ambiental y la mitigación de acumulación de neumáticos usados en el Perú, donde la mezcla MCR-3 destaca por su excelente desempeño ecológico.


---
## 🌐 Red de Conexiones Semánticas (Cerebro Digital)
- **Hub Central:** [[MOC_Master_Cerebro_Tecnico]] | [[Memoria_Maestra]]
- **Disciplinas:** [[01_Proyectos]] | [[02_Metodologias]] | [[03.Agentes]]
- **Auditores Especializados:** (ninguno registrado — ver MOC_Skills_Sistema)
