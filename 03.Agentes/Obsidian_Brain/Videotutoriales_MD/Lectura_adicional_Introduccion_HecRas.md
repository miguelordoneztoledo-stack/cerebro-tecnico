---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\MAESTRIA GRD\0.0 MATERIAL EXTRA-20250507T141946Z-1-001 (2)\0.0 MATERIAL EXTRA\Lectura_adicional_Introduccion_HecRas.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]

_______________________________________________________ Capitulo 3.Introducción_ 

# CAPITULO 3. INTRODUCCIÓN AL HEC-RAS. LIMITACIONES DEL MODELO. 

1 INSTALACION Y LINKS INTERESANTES. 

El programa Hec-Ras es un modelo hidráulico unidimensional creado por la USACE (United States Army Corps of Engineers), de libre distribución (a diferencia de otros softwares europeos), que se puede descargar directamente desde la web (free download): 

− <u>http://www.hec.usace.army.mil/software/hec-ras/</u> 

La última versión disponible del programa es la HEC-RAS 4.2, aparecida en mayo del 2008 que ha subsanado los errores existentes en la versión anterior HEC-RAS 4.0, (2007). La versión 4.2 realiza algunas mejoras respecto a la versión HEC-RAS 3.1.3 (Mayo 2005), sobretodo la incorporación de nuevos módulos de cálculo de transporte de sedimentos y efectos de la temperatura en el flujo. 

De la página web de la USACE puede ser descargada una serie de documentación indispensable  y distintos materiales (en inglés), como son: 

|**HEC-RAS User's Manual**|Manual de uso del programa.|
|---|---|
|**HEC-RAS**<br>**Hydraulic**<br>**Reference**<br>**Manual**|Descripción de algoritmos y conceptos hidráulicos<br>utilizados por los programadores|
|**HEC-RAS Applications Guide**|Descripción de diversos ejemplos prácticos de<br>aplicación.|



La instalación de Hec-Ras es inmediata es el PC, y las nuevas versiones no invalidan las antiguas. No se han registrado incompatibilidades hacia atrás de las nuevas versiones con los proyectos antiguos. Cualquier incidencia sobre problemas de programación de las nuevas versiones puede ser reportada a hec.ras@usace.army.mil. 

Otros productos muy interesantes de la USACE son: 

HEC-HMS 3.0.1:  Modelo hidrológico <u>http://www.hec.usace.army.mil/software/hec-hms/</u> 

HEC-GeoRAS 4: Aplicaciones de Hec-Ras para entornos GIS (ArcView) <u>http://www.hec.usace.army.mil/software/hec-ras/hec-georas.html</u> 

HEC-GeoHMS 1.1   Aplicaciones de Hec-Hms para entornos GIS (ArcView) <u>http://www.hec.usace.army.mil/software/hec-geohms/</u> 

Estos programas y aplicaciones son muy importantes para el trabajo ingenieril/fluvial actual, pero no se debe olvidar que únicamente son elementos complementarios (pre y post proceso) de los verdaderos motores de cálculo hidráulico (Hec-Ras) e hidrológico (Hec-Hms). Un conocimiento a fondo de estos últimos programas es indispensable para la resolución de problemas fluviales. 

Otro programa libre, creado por GITS,  para la delimitación de líneas de inundación (postproceso) en proyectos Hec-Ras geo-referenciados es: 

LAMINA 

<u>http://www.gits.ws/03software/software.htm</u> 

1 

_______________________________________________________ Capitulo 3.Introducción_ 

## 2 INICIANDO UN PROYECTO. ESTRUCTURA DEL PROYECTO. 

Un proyecto Hec-Ras tiene una estructura conceptual muy clara, que se traduce en una serie de archivos de datos y resultados muy definidos que cabe conocer para sacar todo el provecho a las posibilidades del programa. 

Un  estudio hidráulico consta de dos elementos fundamentales, que son por un lado la geometría del cauce, y por otra, las condiciones de flujo, definidas por el caudal y las condiciones de contorno. La combinación de distintas geometrías y condiciones de flujo provoca diferentes resultados, que pueden ser analizados por separado o conjuntamente. Esta es la filosofía de la estructura del proyecto Hec-Ras, donde un único proyecto puede contener multiplicidad de cálculos distintos. 

Iniciamos el proyecto Hec-Ras asignando un nombre al proyecto (“filename”), que se mantendrá invariablemente para todos y cada uno de los ficheros generados posteriormente. También es muy importante definir las unidades o métrica utilizada (en Sistema Internacional, SI, en esta parte de Europa). Así, en el primer nivel se general el archivo” **filename. prj”,** que contiene la información general de la estructura del  proyecto (ficheros existentes y enlaces) 



Figura 3.1. Estructura de un proyecto. Diagrama de flechas de relación entre los distintos archivos del programa (fuente:  HEC-RAS Hydraulic Reference Manual) 

2 

_______________________________________________________ Capitulo 3.Introducción_ 

El segundo nivel consiste en los ficheros correspondientes a los datos de geometría y condiciones de flujo: 

|**Archivos de Geometría (.g)**|Se denominan “**filename.g****”, donde el atributo<br>puede ir de .g01 hasta .g99 para cada una de las<br>geometrías<br>distintas<br>e<br>independientes<br>almacenadas.|
|---|---|
|**Archivos de Flujo (.f)**|Se denominan “**filename.f****”, donde el atributo<br>puede ir de .f01 hasta .f99 para cada una de las<br>condiciones de flujo distintas e independientes<br>almacenadas.|



En este punto se define toda combinación entre una Geometría .g<sup>i</sup> (i=01 a 99) y una condición de flujo .f<sup>j</sup> (j=01 a 99) como un <u>Plan (.p). El archivo resultante es denominado</u> “ **filename.p**** ”, e incluye la información sobre la geometría .g<sup>i</sup> utilizada con el flujo .f<sup>j</sup> impuesto. Así, la numeración del atributo del Plan (.p<sup>k</sup> ) es independientes de i, j, y tan sólo depende del orden temporal en el que se creó. El archivo de Plan  “ **filename.p**<sup>**k**</sup> ”, con k=01 a 99, estará asociado a los resultados hidráulicos y funciona como una unidad. 

|**Archivos de Plan (.p)**|El archivo “**filename.p****” incluye la información|
|---|---|
||sobre la geometría .g utilizada con el flujo .f<br>impuesto.|



Una vez realizada la simulación numérica del Plan “ **filename.p**<sup>**k**</sup> ” en cuestión, los resultados hidráulicos son almacenados en dos archivos de nueva creación que son: 

|**Archivos Run(.r)**|El archivo “**filename.r**<sup>**k**</sup>” contiene resultados que<br>son editables (ASCII)|
|---|---|
|**Archivos Output(.o)**|El archivo “**filename.o**<sup>**k**</sup>” contiene resultados que|
||<br>no son editables (Binario).|



Por tanto, el cálculo hidráulico correspondiente al Plan **k** consta de 3 archivos, “ **filename.p**<sup>**k**</sup> ”, “ **filename.r**<sup>**k**</sup> ” y“ **filename.o**<sup>**k**</sup> ”.  La gran ventaja de este sistema de almacenamiento de resultados es que se pueden visualizar y comparar distintos Planes con mucha rapidez de manejo, dentro de un mismo proyecto. 

En la Figura 3.1 se presenta un diagrama de flechas que describe la estructura del proyecto y la composición de los distintos Planes generados como combinación de 3 archivos de geometría y 1 de flujo. Como resultado, dentro del proyecto se generan 3 planes con sus archivos de resultados correspondientes. 

En la Figura 3.2 se muestra la Ventana Principal de Hec-Ras con un proyecto generado, “exemple1.prj” que incluye un Plan (Plan 1) con su fichero de geometría y flujo asociados (Figura 3.3). 

3 

_______________________________________________________ Capitulo 3.Introducción_ 



Figura 3.2. Ventana Principal donde se muestran los archivos de proyecto, de geometría, flujo y el archivo de Plan utilizado en ese momento. 



Figura 3.3. Ventana de cálculo donde aparece definido el Plan a calcular y los archivos de geometría y flujo asociados. 

A pesar de que el objetivo de este capítulo no es la descripción minuciosa de todos y cada uno de los comandos del programa Hec-Ras, a modo de introducción se realiza una breve descripción de los botones principales que aparecen en la Ventana Principal del Programa, que servirá para tomar conciencia de las posibilidades de simulación y visualización  de los resultados hidráulicos. 

|**_Open Project_**|Abre un proyecto existente a través del archivo “*.prj”.|
|---|---|
|**_Save Project_**|Guarda el  proyecto actual con el mismo nombre asignado<br>anteriormente.|
|**_Geometric Data_**|Abre la pantalla de Geometría, en la que podemos crear,<br>modificar, combinar e importar geometrías procedentes de otros<br>modelos. Existen una serie de menús de transformación de<br>geometría, interpolación, asignación de rugosidades y otras<br>propiedades para las secciones transversales.|
|**_Steady Flow Data_**|Introduce o edita las condiciones de flujo para el régimen<br>permanente. Se introducen datos de caudal en las distintas|



4 

_______________________________________________________ Capitulo 3.Introducción_ 

||secciones de los distintos perfiles. Se escogen además el tipo de<br>condición de contorno a aplicar y su localización.|
|---|---|
|**_Unsteady Flow Data_**|Introduce o edita las condiciones de flujo para régimen no<br>permanente o variable. La información requerida son las<br>Condiciones de Contorno variables en el tiempo (caudal(t) y<br>niveles(t)) en las localizaciones correspondientes, así como la<br>condición inicial (caudal (t=0) y niveles(t=0).|





<!-- Start of picture text -->
Unsteady Flow Data:  Profiles:  Stage & flow Hydrographs:<br>Introduce o edita las<br>Visualiza los perfiles  Visualiza los hidrogramas y/o<br>condiciones de flujo<br>Save Project:  longitudinales (lámina,  limnogramas en cada sección<br>caudal(t)+CC(t) para<br>Guarda un proyecto  Energía…)<br>existente régimen no permanente o  Hydraulic Properties:<br>variable<br>Tablas y dibujos de<br>Steady Flow Data:  Hydraulic Design Functions:  propiedades hidráulicas<br>Introduce o edita las  Cálculos Adicionales hidráulicos y  interesantes<br>condiciones de flujo  de transporte de sedimentos<br>(caudal+CC) para el  (Extensiones)  XYZ perspectiva Plots:  View DSS:<br>régimen permanente   Visualiza la lámina de agua  Visualiza la<br>en 3D<br>información contenida<br>en formato DSS<br>Cross Sections:<br>Warnings:<br>Visualiza las Secciones<br>Resumen de los<br>Transversales de Cálculo<br>erroresy  avisos<br>UnsSteady Flow Analysis:<br>en el cálculo.<br>Cálculo en régimen  no<br>permanente (variable en el  Profile Table:<br>tiempo)  Tabla Configurable de<br>Resultados para cada perfil<br>Steady Flow Analysis:<br>Cálculo en régimen  Rating Curves:  Cross Table:<br>permanente  Visualiza las curvas  Resultados detallados de<br>de Aforo de cada  cada sección, puente, obra<br>Geometric Data:<br>sección (calado- de paso o aliviadero<br>Introduce o edita una<br>caudal)<br>Geometría existente<br>Open Project:<br>Abre un proyecto<br>existente<br><!-- End of picture text -->

Figura 3.4. Ventana Principal de Hec-Ras y explicación de los botones principales. 

5 

_______________________________________________________ Capitulo 3.Introducción_ 

|**_Steady Flow Analysis_**|Cálculo en régimen permanente. Se genera y almacena el Plan<br>correspondiente y se configuran los parámetros de cálculo.|
|---|---|
|**_UnSteady Flow Analysis_**|Cálculo en régimen  no permanente (variable en el tiempo)<br>donde se definen los parámetros de cálculo (pasos de<br>tiempo,…) del método implícito.|
|**_Hydraulic_**<br>**_Design_**<br>**_Functions_**|Extensiones de nueva creación para diversos cálculos<br>complementarios como:<br>1. Erosiones en puentes.<br>2. Cálculo en Uniforme.<br>3. Transporte de sedimentos.<br>4. Diseño estable de canales por distintos métodos.|
|**_Cross Sections_**|Visualiza las Secciones Transversales de Cálculo (niveles de<br>agua, velocidades, Energía, estructuras,…)|
|**_Profiles_**|Visualiza los perfiles longitudinales, tanto de lámina de agua,<br>energía y calados críticos, como una multitud de variables<br>hidráulicas complementarias y derivadas, de fácil manejo.|
|**_Rating Curves_**|Permite visualizar las curvas de Aforo (calado-caudal) de cada<br>una de las secciones.|
|**_XYZ perspectiva Plots_**|Este menú permite generar una vista dinámica de la geometría y<br>la lámina de agua en 3D para cada perfil y Plan. Dada su<br>potencia visual, permite una interpretación rápida de las<br>“manchas de inundación”. Para el cálculo en no permanente, se<br>genera un video de inundación.|
|**_Stage_**<br>**_and_**<br>**_flow_**<br>**_Hydrographs_**|Visualiza los hidrogramas (Q(t)) y/o limnogramas (y(t)) en cada<br>sección (sólo en el cálculo en no permanente).|
|**_Hydraulic Properties_**|Tablas y perfiles longitudinales de propiedades hidráulicas<br>interesantes (Áreas y Conveyance), para los resultados<br>provenientes del cálculo en régimen no permanente.|
|**_Cross Table_**|Resultados detallados de cada sección, puente, obra de paso o<br>aliviadero|
|**_Profile Table_**|Tabla resumen de resultados de las distintas secciones para uno<br>o varios perfiles. Esta Tabla es fácilmente configurable para las<br>distintas variables calculadas, y exportable a entorno Windows.|
|**_Warnings_**|En este menú se muestra un listado de todos los errores, avisos<br>y comentarios sobre la calidad del cálculo numérico<br>(convergencias del modelo), sección por sección.|



6 

_______________________________________________________ Capitulo 3.Introducción_ 

**_View DSS_** Visualiza la información contenida en formato DSS (código de información hidrológica propia de la USACE). 

Dentro de los objetivos del presente curso, y debido en parte a las limitaciones de tiempo, se encuentra únicamente el cálculo y  análisis de los regimenes permanentes (sin variaciones temporales). Las versiones 4.2 y 3.1.3 ofrecen la posibilidad de cálculos en régimen no permanente (variados), que serán introducidos, analizados y trabajados en posteriores ediciones del Curso (niveles más avanzados). 

## 3 LIMITACIONES DEL MODELO HEC-RAS 

El uso de un modelo numérico unidimensional como el Hec-Ras (que resuelve la ecuación de la energía) y todo su entorno complementario (pre y post-proceso en Arc-View)  para la resolución de problemas hidráulicos y/o fluviales conlleva una responsabilidad importante en cuanto a la necesidad de conocer las limitaciones en su aplicación. Debemos entender como profesionales de la ingeniería hidráulica la absoluta necesidad de analizar con visión crítica los resultados numéricos ofrecidos por este tipo de modelos. Cualquier resultado calculado por Hec-Ras no es una solución real…tan sólo es un posible resultado. Se debe aplicar nuestro conocimiento de las leyes y principios hidráulicos para determinar la bondad del resultado. 

A continuación se pasa a describir una serie de Ventajas y de inconvenientes que se deben tener en cuenta: 

## 3.1 _VENTAJAS:_ 

- Un modelo unidimensional en energías permite el cálculo en dominios con escalas <u>muy grandes, de modo que la simulación de kms de río se realiza con una velocidad de cálculo</u> enorme (orden de segundos). Por tanto, la capacidad de repetición y corrección de un cálculo es muy alta. 

- El uso de la ecuación de la energía para el balance entre secciones, dada la incertidumbre existente en la estimación de las pérdidas de carga (resistencia al flujo),  es un método bastante aproximado en problemas de gran escala (fluviales). La simplificación del flujo turbulento tridimensional a un flujo unidimensional es relativamente aceptable para grandes escalas (ríos y barrancos) con precisiones poco exigentes. 

- <u>Gran libertad geométrica: Permite el análisis con secciones naturales no regulares</u> (secciones fluviales: cauce principal y llanuras de inundación). Es una gran ventaja sobre otro tipo de modelos hidráulicos existentes (y mucho más rígidos). 

- <u>Facilidad de creación, modificación y edición de geometrías (entorno visual muy</u> cómodo y rápido) e introducción de datos de rugosidad y estructuras transversales (puentes, obras de paso, aliviaderos). Gran comodidad de visualización de resultados y edición de figuras. 

7 

_______________________________________________________ Capitulo 3.Introducción_ 

- <u>Gran capacidad de importación y exportación de datos</u> en entorno Windows (comunicación con Excel ,Word, Autocad) para el post-proceso de resultados y presentación. 

- Las nuevas tecnologías SIG (Sistemas de Información Geográfica), tipo Arc-View, permiten el proceso de grandes cartografías para generar la geometría del cauce con gran precisión, en formatos importables Hec-Ras (.geo). Asimismo, existen extensiones para el Post-proceso de láminas de inundación y mallas (“grids”) de inundación y velocidad. 

- Uso extendido en todo el mundo y gran experiencia de uso. Hec-Ras es un modelo bien contrastado, herencia directa (y mejorada) del antiguo HEC-2 (1984) en MSDOS. 

- **ES GRATIS  !!!!!!!** (sin licencia). 

## 3.2 _INCONVENIENTES Y LIMITACIONES._ 

- Hec-Ras no es un modelo turbulento. La ecuación de la energía supone siempre distribuciones hidrostáticas de presiones y la ecuación de fricción permanente de Manning. Por tanto, la solución es una pura simplificación, y no se ajusta a la realidad en casos donde las presiones y las tensiones turbulentas se alejan del modelo lineal. 

- Hec-Ras no es un modelo 3D (x,y,z) ni 2D (x,y) , sino que es un modelo 1D (x), de modo que la solución siempre es una aproximación o promedio de la real. Un ejemplo tan importante como la extensión del flujo por las llanuras de inundación para grandes avenidas es un fenómeno que Hec-Ras no puede evaluar, en principio. La posibilidad de dividir la sección en subsecciones lo convierte en un modelo quasi 2D muy debil pues no tiene en cuenta la transferencia lateral de momentum del flujo. La distribución lateral de velocidades no es correcta.  En consecuencia, la solución de flujo en curvas (método de los Flowpaths) es tremendamente aproximada. 

- Sólo se pueden modelar ríos y barrancos con pendientes menores de 10º (α< 10º, So <0.18), ya que no se tiene en cuenta la componente vertical del peso de la columna de agua (cos α) en las ecuaciones. 

- Ni Saltos ni los obstáculos son reproducidos correctamente (Hec-Ras no realiza balance de fuerzas). Existen métodos para simular o reproducir dichos efectos, pero son altamente arbitrarios y dependen mucho del tipo de flujo. 

- El resultado viene altamente condicionado por las consideraciones geométricas adoptadas (Trazado de secciones, Areas Inefectivas, Leeves, Pérdidas de estrechamiento y expansión, etc…). Por tanto, el resultado sigue siendo bastante “manual” (bajo criterio del calculista) 

- Problemas en la elección del calado crítico. Dificultad para hallar el calado crítico en secciones naturales complejas que contienen varios calados críticos (terrazas fluviales). Por defecto el programa escoge el de calado más bajo. 

- Siempre ofrece por defecto una solución, es decir,  Hec-ras no se cuelga nunca. En consecuencia, se debe ser crítico con el resultado numérico. 

8 

_______________________________________________________ Capitulo 3.Introducción_ 

- Limitación en la convergencia de la energía a 40 iteraciones en cada sección de cálculo. Por defecto adopta el valor de calado de menor error. 

## 4 COMENTARIOS SOBRE ENTORNOS GIS. 

Una de las grandes ventajas del trabajo con entornos SIG (o GIS) es la de extraer directamente de la cartografía unos modelos de terreno que estén Georeferenciados, es decir, que cada una de la secciones transversales contenga sus propias coordenadas UTM (Xutm,Yutm). Ello permite trabajar cómodamente con los resultados Hec-Ras y la Cartografia/Ortofotomapas/MDT, a nivel de identificación de zonas, posibles puntos críticos, etc. 

## 5 EJEMPLOS DE ERRORES DE CÁLCULO DE HEC-RAS. 

Si bien se acepta la fiabilidad del modelo Hec-Ras en modo general, aparecen errores muy básicos al someter el programa a condiciones de flujo cercanas al crítico con geometrías extremadamente simples y triviales.  Las limitaciones en los algoritmos de convergencia de energía, que son de 1º orden,  proporciona, en dichos casos soluciones diferentes para las mismas condiciones de flujo y geometría. Por ejemplo, se destacan los errores de este tipo que el programa comete en el cálculo de regimenes cercanos al calado crítico ( _yc_ ). Se han seleccionado 3 casos ilustrativos. 

## 5.1 _Caso (a): Dos posibles soluciones._ 

En condiciones de canal recto, largo y trapezoidal, de pendiente So=0.003 y Q=40m<sup>3</sup> /s se calcula la curva de remanso, que evoluciona hacia el calado normal ( _yn_ ). Antes unas mismas condiciones de contorno del problema (aguas arriba y aguas abajo), y nºFr entre 0.9 y 1.15, el valor del calado normal _yn_ calculado por Hec-ras depende de cómo se halla realizado el cálculo, y ambos los adopta como buenos (Figura 3.5). Si se calcula en régimen rápido, el valor de calado normal resulta con Fr>1, mientras que si lo calcula en régimen mixto, el valor de calado normal resulta con Fr<1. 



<!-- Start of picture text -->
Canal Tramo1 Canal Tramo1<br>Legend Legend<br>EG  PF 1 EG  PF 1<br>8 CASO (a.1) SoQyc===40 m1.36 m 0.003  3 /s  Cri t  PF 1WS  PF 1Ground 8 CASO SoQyc===1.36 m 40 m0.003 (a.2 3 /s ) WS  PF 1Cri t  PF 1Ground<br>yn=1.23 m  yn=1.43 m<br>6 Fr=1.15 Reg.Rápido 6 FrReg. Lento=0.93<br>4 4<br>2 2<br>0 0<br>500 1000 1500 2000 500 1000 1500 2000<br>Main Channel Di stance (m) Main Channel Distance (m)<br>Elevation (m) Elevation (m)<br><!-- End of picture text -->

Figura 3.5. Caso (a). Validez de 2 calados normales distintos para el mismo canal y caudal. 

9 

_______________________________________________________ Capitulo 3.Introducción_ 

## 5.2 _Caso (b): Influencia de la distancia entre secciones._ 

En condiciones de canal recto, largo y rectangular, de pendiente So=0.01065 y q=20 m<sup>2</sup> /s se calcula la curva de remanso que evoluciona hacia el calado normal ( _yn_ ). El Fr teórico es de Fr=1.47 , el _yc_ teórico de _yc=3.43 m_ y el normal _yn_ =2.66 m. Como se aprecia en la Figura 3.6, los 3 cálculos con interdistancias ∆x de 20, 10 y 5 m entre secciones interpolación) ofrecen soluciones diferentes. Los balances de energía convergen de forma distinta para distintas ∆x, y es la solución de menor ∆x(= 5m) la que ofrece el único resultado correcto. El método de resolución de Newton-Raphson tiene problemas graves de convergencia con Fr cercanos al crítico (gradientes de energía específica E(y) cercanos a cero). 









Figura 3.6. Caso (b). Influencia de la distancia entre secciones en el resultado numérico (problemas de convergencia con Fr cercanos a Fr= 1). 

## 5.3 _Caso (c): Influencia de la distancia entre secciones._ 

En condiciones de canal recto, largo y rectangular, de pendiente So=0.0065 y q=20 m<sup>2</sup> /s se calcula la curva de remanso que evoluciona hacia el calado normal ( _yn_ ). El Fr teórico es de Fr=1.12 , el _yc_ teórico de _yc=3.43 m_ y el normal _yn_ =3.22 m. De la Figura 3.7 se desprende que tan sólo una interpolación igual o menor de ∆x=1 m permite una correcta convergencia de la energía y un resultado válido. 

10 

_______________________________________________________ Capitulo 3.Introducción_ 





Figura 3.7. Caso (c). Influencia de la distancia entre secciones en el resultado numérico (problemas de convergencia con Fr cercanos a Fr= 1). 

## 6 ANÁLISIS NUMÉRICO DE ERRORES 

Para ciertos cálculos en canales rectos de secciones sencillas, el programa HEC-RAS parece incapaz de dar soluciones correctas a problemas simples. El ejemplo con el que se va a tratar consiste en una canal de sección rectangular de 10 metros de ancho con una pendiente del 4 por mil, la rugosidad de Manning es de 0.02, el caudal total es de 100 m<sup>3</sup> /s. 

Con estas características se trata de un canal de tipo M, el calado crítico _yc_ es de 2.16 metros y el calado normal _yn_ de 2.28 metros (estos cálculos se realizan con la hipótesis de canal suficientemente ancho con lo que Rh = h). 

La solución del problema consiste en un canal en régimen normal con un Froude de 0.92. En el caso de calcular en régimen mixto se obtiene la solución deseada. Las condiciones de contorno son un calado rápido aguas arriba y un calado lento aguas abajo. De esta manera se debe formar un resalto en la parte alta del canal. 



<!-- Start of picture text -->
Primer ejemplo del curso       Plan: Rectangular    20/03/2006<br>Ejemplo1 Recto<br>7<br>Legend<br>WS  PF 1<br>6<br>Crit  PF 1<br>Ground<br>5<br>4<br>3<br>2<br>1<br>0<br>0 200 400 600 800 1000<br>Main Channel Distance (m)<br>Elevation (m)<br><!-- End of picture text -->

Figura 3.8. Resolución del canal tipo M en modo Mixed 

11 

_______________________________________________________ Capitulo 3.Introducción_ 

Se observa en la figura 3.8 que efectivamente se ha formado un resalto en la parte alta del canal. Por otra parte si ahora se impone que la solución debería ser en régimen rápido (Supercrítico) el modelo debería dar un resultado tal que toda la solución en rápido fuese al crítico. Sin embargo, la solución del cálculo en régimen rápido que se obtiene aparece en la Figura 3.9. 



<!-- Start of picture text -->
Primer ejemplo del curso       Plan: Rectangular    20/03/2006<br>Ejemplo1 Recto<br>7<br>Legend<br>Crit  PF 1<br>6<br>WS  PF 1<br>Ground<br>5<br>4<br>3<br>2<br>1<br>0<br>0 200 400 600 800 1000<br>Main Channel Distance (m)<br>Elevation (m)<br><!-- End of picture text -->

Figura 3.9. Resolución del canal tipo M en modo Supercrítico (rápido) 

Es decir, el programa devuelve una solución válida de Froude constante de valor 1.2 como si se tratase de un régimen normal en régimen rápido, es decir de un canal de tipo S. En el caso de que esta solución errónea tenga mayor fuerza específica que la solución correcta en régimen lento el programa dará este resultado que es totalmente equivocado. 

Para resolver el _Step Method_ , HEC-RAS utiliza un método numérico propio basado en el método de la secante, sin embargo realiza algunas modificaciones para garantizar la estabilidad. Así, cuando la diferencia entre el error en la ecuación de energía de dos iteraciones consecutivas es menor que 0.01, pasa a un método de substitución sucesiva, que es más lento pero más estable cerca de puntos críticos. 

Una posible causa de la anomalía podría ser que en el caso en el que estamos, el método no convergiese, o que de hacerlo no convergiese hacia el calado crítico sino hacia un valor erróneo que finalmente queda como un falso “régimen normal”. 

Para realizar la pertinente comprobación numérica, se implementa un EXCEL con el algoritmo HEC-RAS y se introduce el calado de 1.8 metros que el programa está dando como falso “normal” en régimen rápido. 

En la Tabla 3.1 se puede ver que el algoritmo sí converge, y que lo hace a un valor de 1.93 metros, es decir realmente el algoritmo funciona correctamente y converge hacia un calado más cercano al crítico. Es decir, en ningún caso parece que caiga en un falso “normal” en rápido sino que se va hacia el crítico, señal inequívoca de que no existe solución en rápido. 

En la Tabla 3.1 se presentan los resultados de unas cuantas iteraciones con el algoritmo HEC-RAS, h1 es el calado en la sección aguas arriba y vemos como el calado en la sección h2 converge hacia 1.93 m, es decir se acerca al crítico como debería ser: 

12 

_______________________________________________________ Capitulo 3.Introducción_ 

|Delta X|q|h1|S0|V1|n|Sf1|E1|
|---|---|---|---|---|---|---|---|
|20|10|1.8|0.004|5.55555556|0.025|0.00880991|3.45309875|



|Delta X|q|h2|V2|n|Sf2|E2|
|---|---|---|---|---|---|---|
|20|10|1.5|6.66666667|0.025|0.01617742|3.7652622|
|20|10|1.10657427|9.03689904|0.025|0.04459417|5.26893637|
|20|10|1.36512698|7.32532586|0.025|0.0221464|4.10011164|
|20|10|1.54263714|6.48240585|0.025|0.01473446|3.6844101|
|20|10|1.71178823|5.84184412|0.025|0.01041629|3.45119408|
|20|10|1.82828402|5.46960968|0.025|0.00836375|3.35308678|
|20|10|1.89871674|5.26671504|0.025|0.0073736|3.31249285|
|20|10|1.92832792|5.18583996|0.025|0.00700289|3.29901784|
|20|10|1.93530255|5.16715075|0.025|0.00691911|3.29613062|
|20|10|1.93560414|5.16634563|0.025|0.00691552|3.29600818|
|20|10|1.93576007|5.16592946|0.025|0.00691366|3.29594495|
|20|10|1.93583821|5.16572096|0.025|0.00691273|3.29591328|
|20|10|1.93587732|5.1656166|0.025|0.00691227|3.29589744|
|20|10|1.93589688|5.16556439|0.025|0.00691204|3.29588952|
|20|10|1.93590667|5.16553828|0.025|0.00691192|3.29588555|
|20|10|1.93591156|5.16552522|0.025|0.00691186|3.29588357|
|20|10|1.93591401|5.1655187|0.025|0.00691183|3.29588258|
|20|10|1.93591523|5.16551543|0.025|0.00691182|3.29588208|
|20|10|1.93591584|5.1655138|0.025|0.00691181|3.29588184|
|20|10|1.93591615|5.16551298|0.025|0.00691181|3.29588171|
|20|10|1.9359163|5.16551257|0.025|0.0069118|3.29588165|
|20|10|1.93591638|5.16551237|0.025|0.0069118|3.29588162|
|20|10|1.93591642|5.16551227|0.025|0.0069118|3.2958816|



Tabla  3.1. Resultado de la iteración entre dos secciones mediante algoritmo HecRas. 

13 

_______________________________________________________ Capitulo 3.Introducción_ 

El hecho de que converja más o menos rápido hacia el calado crítico depende de la discretización, en este caso es de Delta X=20 metros. En la  Figura 3.10 se observa una gráfica con la función de error (Error) y los sucesivos valores de h2 ofrecidos por el algoritmo. 



<!-- Start of picture text -->
0.5<br>0<br>0 1 2 3 4 5 6<br>-0.5<br>-1<br>-1.5<br>-2<br>-2.5<br>-3<br>h2<br>Error<br><!-- End of picture text -->

Figura 3.10. Evolución de las iteraciones de h2 según el algoritmo Hec-Ras. 

Se comprueba  que realmente converge. Por todo ello resulta extraño que el programa no converja correctamente y siga dando como resultado 1.8 metros, como si se tratase de un calado normal. 

Si se observa el _log_ generado por HEC-RAS para una sección cualquiera obtenemos lo siguiente (las unidades son pies, ya que el módulo de calculo funciona en estas unidades): 

|At ri|ver stat|ion 500.*|||||
|---|---|---|---|---|---|---|
||****|CRITWS ****||DETERMINE|CRITICAL WS|EL|
|NTRY|IPAR|WSEL<br>EGC|WSEL1|EG1<br>EG2|HTINC X|Y|
|2|2|13.681 17.231|13.681|17.296 17.32|0.3554 0.01|0.0006|
|3|3|14.036 17.257|13.681|17.231 17.32|0.3554 0.01|0.0006|
|4|4|14.392 17.326|13.681|17.231 17.257|0.3554 0.01|0.0006|
|5|5|13.649 17.231|13.681|17.231 17.257|0.391 0.01|10.1265|
|6|6|13.671 17.231|13.681|17.231 17.257|0.391 0.01|0.0006|
|6|2|13.671 17.231|13.671|17.231 17.257|0.391 0.01|0.0006|
|7|3|14.026 17.255|13.671|17.231 17.257|0.355 0.01|0.0006|
|8|4|14.381 17.324|13.671|17.231 17.255|0.355 0.01|0.0006|
|9|5|13.651 17.231|13.671|17.231 17.255|0.3905 0.01|10.1217|
|10|6|13.665 17.231|13.671|17.231 17.255|0.3905 0.01|0.0006|
|11|7|13.67 17.231|13.671|17.231 17.255|0.3905 0.01|0.0006|
|12<br>|8<br>PARAB|13.671 17.231<br>OLIC METHOD C|13.671<br>ONVERG|17.231 17.255<br>ED|0.3905 0.01|0.0006|



FINAL CRITICAL WATER SURFACE = <mark>13.67</mark> DID IT CONVERGE?     T 

14 

_______________________________________________________ Capitulo 3.Introducción_ 

Por lo tanto el valor del calado crítico es el correcto, sin embargo en la parte en la que itera sobre la ecuación de la energía, se puede ver cómo el error mínimo no aparece para un valor más cercano al calado crítico (yc=13.67), sino para un valor alejado de este; es decir, el programa encuentra una clase de régimen normal en rápido que es incorrecto (y=12.82): 

||****|STD_REA|L ****   PERF|ORM STANDARD STEP BETWEEN|TWO CR|OSS SEC|TIONS|
|---|---|---|---|---|---|---|---|
|I<br>0|ASSUME<br>1287|D CALC<br>1282|ERROREG<br>00497 1739|HL<br>FL<br>F_SLOPE<br>01147 01147 000699|K<br>42237|A<br>2069|WP<br>454|
|<br>1|.<br>12.83|.<br>12.76|. .<br>0.0712 17.41|. . .<br>0.1207 0.1156 0.00705|<br>41892|.<br>205.7|.<br>45.4|
|2|12.95|12.9|0.0487 17.36|0.1465 0.1125 0.00686|43036|209.5|45.6|
|3|13.2|13.13|0.064 17.28|0.2376 0.1062 0.00647|45538|217.7|46.1|
|4|12.15|11.45|0.7085 17.91|0.2589 0.136 0.00829|35320|183.5|44|
|5|13.49|13.37|0.1123 17.24|0.3309 0.0994 0.00606|48482|227.2|46.7|
|6|13.67|13.51|0.1583 17.23|0.3846 0.0954 0.00581|50394|233.2|47|
|7|13.03|12.98|0.0509 17.33|0.1791 0.1103 0.00672|43894|212.3|45.8|
|8|12.73|12.59|0.1392 17.46|0.1386 0.1184 0.00722|40893|202.4|45.1|
|9|13.21|13.14|0.0653 17.28|0.2414 0.1059 0.00646|45651|218.1|46.1|
|10|13.63|13.48|0.1469 17.23|0.3728 0.0963 0.00587|49957|231.8|46.9|
|11|12.87|12.82|0.0495 17.39|0.1164 0.1146 0.00698|42280|207|45.4|
|12|12.49|12.15|0.3398 17.61|0.1855 0.1255 0.00765|38505|194.4|44.7|
|13|13.67|13.51|0.1583 17.23|0.3846 0.0954 0.00581|50394|233.2|47|
|14|13.33|13.24|0.0817 17.26|0.2805 0.1031 0.00629|46839|221.9|46.3|
|15|12.96|12.91|0.0488 17.36|0.1499 0.1123 0.00685|43125|209.8|45.6|
|16|12.41|12|0.4138 17.67|0.2013 0.1278 0.00779|37769|191.9|44.5|
|17|13.67|13.51|0.1583 17.23|0.3846 0.0954 0.00581|50394|233.2|47|
|18|12.97|12.92|0.0489 17.35|0.1548 0.112 0.00683|43252|210.2|45.6|
|19|12.66|12.46|0.1957 17.5|0.1526 0.1206 0.00735|40149|199.9|45|
|20|13.67|13.51|0.1583 17.23|0.3846 0.0954 0.00581|50394|233.2|47|
|21|13.67|13.51|0.1583 17.23|0.3846 0.0954 0.00581|50394|233.2|47|
|22|13.67|13.51|0.1583 17.23|0.3846 0.0954 0.00581|50394|233.2|47|
|23|13.67|13.51|0.1583 17.23|0.3846 0.0954 0.00581|50394|233.2|47|
|24|13.67|13.51|0.158317.23|0.3846 0.0954 0.00581|50394|233.2|47|



Estudiando las posibles causas de que el hecho de minimizar el error en la ecuación de la energía para este caso no converja al régimen crítico, aparece como única causa posible la incorporación al balance de energía de las pérdidas por contracción-expansión. Estas pérdidas son aplicadas siempre que existe una diferencia de velocidades entre secciones, independientemente de que exista o no cambios de anchura de la sección. Por lo tanto, se comprueba que al eliminar estas pérdidas (situando sus valores en 0.0/0.0) se obtiene la solución correcta, tal como se muestra en la Figura 3.11 

15 

_______________________________________________________ Capitulo 3.Introducción_ 



<!-- Start of picture text -->
Primer ejemplo del curso       Plan: Rectangular    20/03/2006<br>Ejemplo1 Recto<br>7<br>Legend<br>Crit  PF 1<br>6<br>WS  PF 1<br>Ground<br>5<br>4<br>3<br>2<br>1<br>0<br>0 200 400 600 800 1000<br>Main Channel Distance (m)<br>Elevation (m)<br><!-- End of picture text -->

Figura 3.11. Resolución del canal tipo M en modo Supercrítico (rápido), pero con pérdidas por contracciónexpansión=0.0 

Se comprueba como ahora la solución es la correcta, pues en cada sección la solución converge al crítico, sin crear el falso régimen normal en régimen rápido. 

Evidentemente las pérdidas por contracción expansión modifican las curvas de remanso. Por lo tanto en los casos como los colectores, canales y otros elementos de sección constante se deberían eliminar por completo en el cálculo ya que únicamente están pensadas para modelar perdidas por ensanchamiento/contracción de la sección. 

16 

