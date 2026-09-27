---
title: "SKILL"
tags: [docling, ingestión, documento]
status: procesado
---

# SKILL

> [!info] Documento procesado automáticamente con Docling.

## Skill: Excel para Importaci ó n SewerCAD 2024 Alcantarillado Sanitario

## Descripción

Skill para transformar datos crudos de un proyecto de alcantarillado sanitario (topografía, población, parámetros de diseño) en un archivo Excel (.xlsx) listo para importar directamente en SewerCAD 2024 mediante la herramienta ModelBuilder de Bentley OpenFlows.

## Activación

Activar SIEMPRE que el usuario mencione: importar a SewerCAD, ModelBuilder SewerCAD, Excel para SewerCAD, exportar a SewerCAD, preparar datos para SewerCAD, generar archivo de importación SewerCAD, alcantarillado sanitario a SewerCAD, convertir datos a SewerCAD, formato ModelBuilder, cámaras y tuberías para SewerCAD, nodos y conduits SewerCAD, crear modelo SewerCAD desde Excel, datos crudos a SewerCAD, o cualquier solicitud de transformar información de un diseño de alcantarillado sanitario al formato de importación de SewerCAD 2024.

## Datos de Entrada Requeridos

El usuario debe proporcionar (en Excel, CSV, o descripción textual) los siguientes datos crudos:

## 1. Cámaras / Nodos (Manholes)

- Identificador (nombre o número de cámara)
- Cota de terreno (elevación del terreno natural en metros)
- Coordenadas X, Y (Este, Norte - preferiblemente UTM)
- Profundidad de la cámara (o cota de fondo/invert)

## 2. Tramos / Tuberías (Conduits)

- Identificador del tramo
- Cámara de fin (aguas abajo)
- Cámara de inicio (aguas arriba)
- Longitud (metros)
- Diámetro (mm)
- Material / Coeficiente de Manning (o asumir HDPE n=0.013 si no se indica)

## 3. Parámetros de Diseño (para calcular caudales)

- Población inicial y futura (o tasa de crecimiento + período de diseño)
- Coeficiente de retorno (C)
- Dotación de agua (L/hab/día)
- Factores punta k1, k2
- Caudal de conexiones erradas (o % del QMH)
- Caudal de infiltración (o longitud de red para calcularlo)

## 4. Caudales por Cámara (opcional)

- Si el usuario ya tiene los caudales asignados por cámara, se usan directamente.
- Si no, se calculan proporcionalmente por longitud acumulada de tubería según NB-688.

## Formato de Salida - Excel para ModelBuilder SewerCAD 2024

El archivo generado debe tener las siguientes hojas, con encabezados en la Fila 1 (sin filas de título ni comentarios arriba):

## Hoja 1: Manholes

| Columna   | Nombre Exacto    | Tipo     | Unidad   | Descripción                                  |
|-----------|------------------|----------|----------|----------------------------------------------|
| A         | Label            | Texto    | -        | Identificador único de la cámara (Key Field) |
| B         | X                | Numérico | m (UTM)  | Coordenada Este                              |
| C         | Y                | Numérico | m (UTM)  | Coordenada Norte                             |
| D         | Ground Elevation | Numérico | m        | Elevación del terreno natural                |

| E   | Rim Elevation    | Numérico   | m   | Elevación de la tapa (igual a Ground Elevation si no hay dato específico)   |
|-----|------------------|------------|-----|-----------------------------------------------------------------------------|
| F   | Invert Elevation | Numérico   | m   | Elevación del fondo de la cámara                                            |

## Hoja 2: Conduits

| Columna   | Nombre Exacto          | Tipo     | Unidad   | Descripción                         |
|-----------|------------------------|----------|----------|-------------------------------------|
| A         | Label                  | Texto    | -        | Identificador único del tramo       |
| B         | Start Node             | Texto    | -        | Label de la cámara aguas arriba     |
| C         | Stop Node              | Texto    | -        | Label de la cámara aguas abajo      |
| D         | Length                 | Numérico | m        | Longitud del tramo                  |
| E         | Diameter               | Numérico | mm       | Diámetro interno de la tubería      |
| F         | Manning n              | Numérico | -        | Coeficiente de rugosidad de Manning |
| G         | Start Invert Elevation | Numérico | m        | Cota solera en nodo de inicio       |
| H         | Stop Invert Elevation  | Numérico | m        | Cota solera en nodo de fin          |

## Hoja 3: Sanitary Loads

| Columna   | Nombre Exacto   | Tipo     | Unidad   | Descripción                                 |
|-----------|-----------------|----------|----------|---------------------------------------------|
| A         | Label           | Texto    | -        | Label de la cámara donde se aplica la carga |
| B         | Load Type       | Texto    | -        | Siempre = Sanitary Hydrograph               |
| C         | Base Flow       | Numérico | L/s      | Caudal sanitario asignado a esa cámara      |

## Hoja 4: Parametros (Referencia)

Hoja informativa (no se importa) con los parámetros de diseño utilizados para trazabilidad.

## Reglas de Procesamiento

1. Cota Invert de Cámara : Si solo se tiene profundidad (HC), calcular como:  Invert Elevation = Ground Elevation - HC
2. Rim Elevation : Si no se especifica, usar  Rim Elevation = Ground Elevation
3. Cotas Solera de Tuberías :
- Start Invert Elevation  = Invert Elevation de la cámara de inicio
- Stop Invert Elevation  = Invert Elevation de la cámara de fin
4. Pendiente : Se calcula como  (Start Invert - Stop Invert) / Length  pero NO se incluye en el Excel de importación (SewerCAD la calcula automáticamente).
5. Caudales por cámara (si no se proporcionan):
- Calcular  q\_unit = Q\_diseño / Longitud\_total\_red  (L/s por metro)
- Método según NB-688 (longitud acumulada)
- Para cada cámara:  Base Flow = q\_unit × Longitud\_acumulada\_tributaria
6. Manning n : Si no se especifica material, usar n=0.013 (HDPE).
7. Diámetro mínimo :  200 mm según NB-688.
8. Formato numérico : Usar punto decimal, sin separador de miles.
9. Labels : No usar espacios ni caracteres especiales. Formato recomendado:  C.1 ,  C.2 , etc. para cámaras;  T.1 ,  T.2 , etc. para tramos.

## Validaciones Antes de Generar el Archivo

- Verificar que todas las cámaras referenciadas en Conduits existan en Manholes.
- Verificar que  Start Invert Elevation &gt;= Stop Invert Elevation  para cada tramo (pendiente positiva aguas abajo).
- Verificar que  Invert Elevation &lt; Ground Elevation  para cada cámara.
- Alertar si algún diámetro es menor a 200 mm.
- Verificar que no haya Labels duplicados.
- Alertar si alguna pendiente resulta negativa o cero.

## Flujo de Trabajo

1. Recibir datos crudos del usuario (Excel, CSV, o texto).
2. Identificar qué datos están disponibles y cuáles faltan.
3. Solicitar datos faltantes al usuario si son críticos.
4. Procesar y transformar los datos según las reglas anteriores.
5. Ejecutar validaciones.
6. Generar el archivo  .xlsx  con las 4 hojas en el formato exacto de ModelBuilder.
7. Entregar el archivo al usuario con un resumen de estadísticas (total cámaras, tramos, longitud de red, rango de pendientes, diámetros usados).

## Ejemplo de Uso

Usuario : "Tengo un Excel con las coordenadas y cotas de 50 cámaras y los tramos entre ellas. La población futura es 5000 hab, dotación 120 L/hab/día, coeficiente de retorno 0.80. Quiero el archivo listo para importar en SewerCAD."

Respuesta esperada : Procesar los datos, calcular caudales, generar el Excel con las 4 hojas en formato ModelBuilder, validar y entregar.

## Notas Importantes sobre ModelBuilder

- ModelBuilder mapea columnas del Excel a propiedades de SewerCAD mediante nombre o posición.
- Los nombres de columna en el Excel NO necesitan ser idénticos a los de SewerCAD; el mapeo se hace manualmente en el wizard. Sin embargo, usar nombres similares facilita el proceso.
- Cada hoja se importa por separado: primero Manholes, luego Conduits, luego Loads.
- El orden de importación es importante: los nodos deben existir antes de importar las tuberías que los conectan.
- Las unidades se configuran en el paso de mapeo de ModelBuilder; asegurarse de que coincidan con las del Excel.