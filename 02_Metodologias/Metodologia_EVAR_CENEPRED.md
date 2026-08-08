# 📐 Metodología EVAR: Lineamientos Técnicos CENEPRED

> [!NOTE]
> Esta nota técnica describe la metodología oficial del **CENEPRED (Centro Nacional de Estimación, Prevención y Reducción del Riesgo de Desastres - Perú)** para la [[Gestion_de_Riesgos_EVAR|Evaluación de Riesgos]] originados por fenómenos naturales en obras de infraestructura vial.
> Enlace principal: [[MOC_Ruta_HU_112|Volver al Panel de Control]]

---

## 1. El Enfoque Conceptual del Riesgo

Según CENEPRED, el **Riesgo ($R$)** es una función del **Peligro ($P$)** y de la **Vulnerabilidad ($V$)**, expresado conceptualmente como:

$$R = f(P, V)$$

Donde:
- **Peligro ($P$):** La probabilidad de que un fenómeno físico, de origen natural o tecnológico, potencialmente dañino, se presente en un lugar específico, con una cierta intensidad y en un período de tiempo determinado.
- **Vulnerabilidad ($V$):** La susceptibilidad de la población, la estructura física o las actividades socioeconómicas de sufrir daños ante la ocurrencia de un peligro.

---

## 2. Proceso de Análisis Jerárquico (AHP) de Saaty

Para la ponderación de las variables de peligro y vulnerabilidad, se aplica el **Proceso de Análisis Jerárquico (AHP)** desarrollado por Thomas Saaty. Este método permite tomar decisiones multicriterio estructurando el problema en una jerarquía y realizando comparaciones pareadas.

### Matriz de Comparación Pareada
Se utiliza la escala de Saaty (del 1 al 9) para comparar la importancia relativa de cada factor:

| Valor numérico | Definición de importancia |
| :---: | :--- |
| **1** | Igual importancia |
| **3** | Moderada importancia de uno sobre otro |
| **5** | Fuerte importancia |
| **7** | Muy fuerte importancia |
| **9** | Extrema importancia |
| *2, 4, 6, 8* | Valores intermedios entre dos juicios adyacentes |

El análisis de consistencia de la matriz comparativa se evalúa calculando la **Razón de Consistencia (RC)**:

$$RC = \frac{CI}{RI}$$

Donde:
- $CI$ es el Índice de Consistencia: $CI = \frac{\lambda_{max} - n}{n - 1}$ ($\lambda_{max}$ es el valor propio máximo y $n$ es el número de criterios).
- $RI$ es el Índice de Consistencia Aleatoria.
- **Criterio de Aceptación:** Si $RC < 0.10$ ($10\%$), el juicio de consistencia es aceptable; de lo contrario, se deben revisar las comparaciones pareadas.

---

## 3. Determinación de los Niveles de Riesgo

Una vez calculados los descriptores de Peligro ($P$) y Vulnerabilidad ($V$), se cruzan los valores en una matriz de doble entrada para definir el **Nivel de Riesgo**:

```text
       Matriz de Aceptabilidad del Riesgo (CENEPRED)
      ┌──────────┬──────────┬──────────┬──────────┐
      │  Riesgo  │  Riesgo  │  Riesgo  │  Riesgo  │
 Alto │  Medio   │   Alto   │ Muy Alto │ Muy Alto │
      ├──────────┼──────────┼──────────┼──────────┤
      │  Riesgo  │  Riesgo  │  Riesgo  │  Riesgo  │
 Med. │   Bajo   │  Medio   │   Alto   │ Muy Alto │
      ├──────────┼──────────┼──────────┼──────────┤
      │  Riesgo  │  Riesgo  │  Riesgo  │  Riesgo  │
 Bajo │   Bajo   │   Bajo   │  Medio   │   Alto   │
      └──────────┴──────────┴──────────┴──────────┘
                 Bajo       Medio      Alto      (Peligro)
```

### Rangos de Estratificación de Riesgo
- **Muy Alto:** Zonas propensas a la pérdida total de plataforma o colapso de puentes, con alta exposición de vidas humanas.
- **Alto:** Zonas con inestabilidad de taludes frecuente que bloquean la vía temporalmente.
- **Medio:** Tramos con erosión menor en bermas o cunetas colmatadas que no interrumpen el tránsito.
- **Bajo:** Zonas planas estables, sin cauces pluviales cercanos ni problemas geotécnicos.

---
*Esta guía metodológica sirve de base de conocimiento para la gestión de riesgos en [[Gestion_de_Riesgos_EVAR]] y es ejecutada por el [[Agente_EVAR_Especialista]].*


---
## 🔗 Enlaces Puente de Unificación (Cerebro Digital Integrado)
- **Hub Central:** [[MOC_Master_Cerebro_Tecnico]] | [[Memoria_Maestra]]
- **Proyectos Históricos:** [[MOC_Ruta_HU_112]] | [[MOC_Estadio_Ambo]] | [[MOC_Conchumayo_GORE]] | [[MOC_EIA_Estadio_Panao]]
- **Investigación y UDH:** [[MOC_UDH_Academico]] | [[MOC_Tesis_Luz]] | [[Investigacion_Papers]]
- **Metodologías Unificadas:** [[Metodologia_EVAR_CENEPRED]] | [[Metodologia_EVAP_CONESA]] | [[Metodologia_SST_G050]]
- **Auditores y Agentes:** (ninguno registrado — ver MOC_Skills_Sistema)
- [[AHP_Saaty_EVAR_EVAR-IIEE-IPARIA]] (Referencia temática: ahp)
- [[Absolucion_EVAR_EVAR-IIEE-IPARIA]] (Referencia temática: iparia)

---
## 🌐 Red de Conexiones Semánticas (Cerebro Digital)
- **Hub Central:** [[MOC_Master_Cerebro_Tecnico]] | [[Memoria_Maestra]]
- **Disciplinas:** [[01_Proyectos]] | [[02_Metodologias]] | [[03.Agentes]]
- **Auditores Especializados:** (ninguno registrado — ver MOC_Skills_Sistema)
## 📌 APLICACIÓN EN CAMPO
- [[Inspeccion_Elite_5Pilares_2026-07-28]]
- [[Inspeccion_2026-07-28_Irrigacion_Conchumayo]]
- [[MOC_Master_Cerebro_Tecnico]]
