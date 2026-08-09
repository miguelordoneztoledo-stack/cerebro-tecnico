---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\MAESTRIA GRD\0.0 MATERIAL EXTRA-20250507T141946Z-1-001 (2)\0.0 MATERIAL EXTRA\Lectura_adicional_ejercicio_HecRAS.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]

Julio 2007 

# **Manual introductorio a HEC-RAS** 

### **<mark>Conceptos básicos</mark>** 

Estudiamos un tramo determinado de un río  y queremos saber hasta dónde llegaría el agua si el caudal alcanzara un cierto valor. ¿Será suficiente el cauce principal? ¿Hasta qué altura? ¿O serán inundadas las áreas próximas, y en qué extensión? 

La respuesta, para un caudal determinado, dependerá de la forma del cauce, de la pendiente y de su naturaleza (tipo de materiales, presencia de vegetación,...). El problema se complica si existen puentes u otro tipo de obras, o si deseamos saber qué sucedería si se construyera un puente, una canalización, etc. 

En este documento se hace una introducción muy elemental: aprender lo necesario para comenzar a utilizar el modelo en casos muy simples. La aplicación en casos reales, siempre complejos, requerirá el estudio exhaustivo de los manuales y, sobre todo, mucha experiencia. 

El problema consta de dos partes bien diferenciadas: 

- **1.‐ Evaluación del caudal** 

Normalmente queremos evaluar el efecto producido por un caudal máximo, por ejemplo, con un periodo de retorno de 100 años. Ese dato de caudal puede obtenerse mediante un tratamiento estadístico de datos de **caudales** , o, si no disponemos de ellos, calculando los caudales que se generarán a partir de unas determinadas **precipitaciones** . Todo esto se trata en otros temas, aquí suponemos que el caudal ya es un dato conocido del problema. 

- **2.‐ Evaluación del área inundable** 

Como hemos indicado, la sección que ocupará un caudal determinado y las áreas del valle que serán inundadas dependen de la geometría del cauce, de la pendiente y de otros factores. La sección correspondiente a un cierto caudal se puede evaluar mediante la fórmula de Manning o similar,  a partir de la sección evaluar la **altura** del agua y a partir de ésta hacer una estimación de las áreas que serán inundadas<sup>1</sup> . 

Pero el método idóneo para abordar esta parte del trabajo es mediante el programa **[[Lectura_adicional_Introduccion_HecRas|HEC‐RAS]]** . Es un programa gratuito que se obtiene en Internet<sup>2</sup> . (Estamos utilizando la versión 4<sup>3</sup> ) 

- 1 Ver en Complementos : “Cálculo de la altura del agua para un caudal determinado” 

- 2 http://www.hec.usace.army.mil/software/hec‐ras/ 

> 3 **Atención** : Hasta esta fecha (julio 07) la versión 4 de HEC‐RAS requiere ajustar el sistema Windows a Inglés (me dicen los autores que esto se va a solucionar en breve). El cambio es sencillo, pero en el resto de los programas aparecerán las decimales y los formatos de fecha al modo americano: 

> Panel de control >> Configuración regional y de idioma >> Inglés (Estados Unidos) 

- 1 - 

_F. Javier Sánchez San Román ‐ Dpto. Geología, Universidad de Salamanca ‐_ <u>http://web.usal.es/javisan/hidro</u> 

Hay dos versiones del programa:  HEC‐RAS y HEC‐GeoRAS. Si deseamos interactuar con Sistemas de Información Geográfica (ArcGIS, ArcView) debemos utilizar **HEC‐GeoRAS** , que se obtiene en el mismo sitio web. (En este documento nos vamos a referir al programa HEC‐RAS, **no** a HEC‐GeoRAS). 

Para el funcionamiento de HEC‐RAS debemos aportar **dos tipos de datos** : geométricos y de caudales. 

Los **datos geométricos** fundamentales son **diversas secciones transversales** a lo largo del cauce o cauces considerados. Dichas secciones se introducen mediante la cota de  varios puntos; de este modo, mediante la cota de dos secciones contiguas, separadas por una distancia conocida , el modelo calcula la pendiente de ese tramo. 

El **caudal** puede ser un solo valor constante o bien un caudal variable en el tiempo. 

Las **fases de trabajo** son las siguientes: 

1. Creación de un nuevo proyecto. (File >> New Project...) 

2. Datos geométricos (Edit >> Geometric Data...) 

3. Datos de caudales y condiciones de contorno (Edit >> Steady (Unsteady) Flow Data...) 

4. Cálculo (Run >> Steady (Unsteady) Flow Analysis...) 

5. Observación de los resultados  ( View >> varias opciones del menú ) 

### **<mark>Comenzar a trabajar: ajustes iniciales</mark>** 

Vamos a realizar el ejemplo más simple posible. Consideremos un tramo de un río, y dos secciones transversales para calcular la altura alcanzada por el agua para un caudal dado. 

Al abrir el programa aparece el cuadro principal: 



Lo primero (y sólo la primera vez usemos el programa) indicamos a HEC‐ RAS que utilice unidades del Sistema Internacional (métrico), así: Menú Options , opción Unit system (US Customary/SI)... .; en el cuadro que aparece marcar las opciones que aparecen aquí al lado: 



- 2 - 

_F. Javier Sánchez San Román ‐ Dpto. Geología, Universidad de Salamanca ‐_ <u>http://web.usal.es/javisan/hidro</u> 

La opción Set as default ... la marcamos para que todos los proyectos que iniciemos en el futuro ya comiencen con el Sistema Métrico) 

Ahora inauguramos un nuevo Proyecto: En el menú Archivo, elegimos New project... Allí hemos de dar nombre al Proyecto ( Title ) y al Archivo  ( File Name ). El segundo ( File Name ) es con el que aparecerá el archivo guardado, cuando lo veamos en Windows. 

### **<mark>Geometría del cauce</mark>** 

#### **Dibujar el río** 

Para abrir la ventana Geometric Data , en el Cuadro Principal picamos en el botón 

y aparece la ventana que mostramos a continuación: 

Inicialmente picamos en el botón 

, y el cursor se convierte en un lápiz; con sucesivos clics trazamos un esquema del cauce. Para terminar, doble clic: entonces aparece un cuadro para darle nombre al río y a ese tramo ( reach ). 

Puede considerarse un río con un único tramo, en cuyo caso darle un nombre al tramo único no tiene mucho sentido, pero es obligado. 

En la figura adjunta, hemos creado un tramo del “Río Grande” y al único tramo le hemos denominado “Tramo estudiado” (Las líneas transversales rotuladas como 1 y 2 aún no deberían estar ahí: son las secciones transversales que construiremos a continuación) 



#### **Secciones Transversales** 

En la ventana Geometric Data (donde acabamos de dibujar el cauce), picamos el 

botón , y aparece una nueva ventana: Cross Section Data . (figura pág 5). Esta es fundamental: aquí introduciremos la forma transversal del cauce y otros datos básicos para la calidad del resultado. 

**1. Crear una nueva sección transversal** 

En el menú Option elegimos la opción Add a new Cross Section... 

- 3 - 

_F. Javier Sánchez San Román ‐ Dpto. Geología, Universidad de Salamanca ‐_ <u>http://web.usal.es/javisan/hidro</u> 

y aparece el cuadrito siguiente: ‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐ > 

Aquí debemos escribir una referencia para la sección que vamos a crear (darle un nombre), pero **sólo se pueden escribir números y el punto o la coma** . Lo más elemental es numerarlas: 1, 2, ... Siempre teniendo en cuenta que en HEC‐RAS la numeración va aumentando aguas arriba, de modo que la número 1 estará al final, aguas abajo. 



Si trabajamos con un río formado por varios tramos, para los perfiles del primer tramo podemos utilizar: 1.1, 1.2,...,  para el segundo: 2.1, 2.1,... y así sucesivamente. 

##### **2. Geometría del cauce** 

En la misma ventana Cross Section Data , escribimos en las dos columnas de la izquierda: en la primera columna ( Station ) la distancia desde la margen izquierda, en la segunda columna ( Elevation ) la cota del fondo del cauce en ese punto (Ojo: NO profundidades, sino cotas o alturas desde cualquier punto de referencia). Por ejemplo, supongamos que disponemos de este croquis para una sección del cauce (la línea de trazos representa el cauce principal): 



En la tabla de la ventana Cross Section Data , 

introducimos esos datos así: ‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐ > 

Picando arriba en , la geometría de la sección aparece dibujada a la derecha. 

**3. Distancia hasta la sección siguiente** 

En la misma ventana Cross Section Data , en este 

cuadro ‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐> 

indicamos las distancias desde esta sección a la 





inmediata siguiente **aguas abajo** , que en este caso es 0, 

ya que esta sección “1” va a ser la primera (es decir, no tiene ninguna aguas abajo de ella): LOB , distancia entre las márgenes izquierdas, ROB , entre las márgenes derechas, y Channel distancia a lo largo del centro del canal. Lógicamente, si indicamos los tres valores iguales, los dos perfiles transversales consecutivos aparecerán paralelos. 

- 4 - 

_F. Javier Sánchez San Román ‐ Dpto. Geología, Universidad de Salamanca ‐_ <u>http://web.usal.es/javisan/hidro</u> 

##### **4. Acotación del canal principal** 

Estos puntos definen la parte de la sección que puede considerarse como canal principal. El resto de la sección se considerará como llanura de inundación. 



Se introducen dos valores de distancias en horizontal, en este ejemplo hemos escrito 4.2 y 12.8 (en el croquis a lápiz está señalado con una línea de trazos). La distancia 4.2 coincide con unos de los puntos que habíamos introducido previamente, pero la 12.8 no; por eso, tras introducir ese valor, el programa pregunta si queremos crear ese punto, decimos que Sí , y le adjudicará una cota interpolada al punto 12.8, que aparece como una nueva línea de datos en la tabla de la izquierda. 

Picamos el botón y los dos puntos que acotan el canal principal aparecen en rojo ( ) en el dibujo. Después de todo el trabajo realizado, la ventana Cross Section Data aparece así: 



(esta ventana Cross Section Data , la presentamos aquí cortada en dos para reproducirla sin reducción) 



- 5 - 

_F. Javier Sánchez San Román ‐ Dpto. Geología, Universidad de Salamanca ‐_ <u>http://web.usal.es/javisan/hidro</u> 

##### **5. Valores “n” de Manning y coeficientes de contracción/expansión** 

Picando en los signos que aparecen al lado, se presentan en pantalla las tablas de valores del coeficiente de Manning, para elegir el adecuado<sup>4</sup> 

El programa utiliza los coeficientes de contracción/expansión para determinar las pérdidas de energía entre dos secciones contiguas. Los autores para una transición gradual aconsejan 0.1 (contracción) y 0.3 (expansión), mientras que en las proximidades de un puente pueden ser, respectivamente de 0.3 y 0.5 o mayores, por la mayor pérdida de energía<sup>5</sup> 

##### **6. Otra sección transversal** 

Para la aplicación más simple de HEC‐RAS se necesitan al menos dos secciones transversales del cauce. Para preparar otra sección debemos repetir todo lo que hemos hecho en la primera (puntos 1 a 5 anteriores). Pero si la segunda sección es muy similar a la primera, podemos duplicarla, y en la copia obtenida elevar las cotas de acuerdo con la pendiente observada en el campo. El procedimiento sería el siguiente: 

En la ventana Cross Section Data , en el menú Options > Copy Current Cross Section.. . (Aunque se denomine Copy , en realidad hace la función de Copiar y Pegar, es decir, duplica la sección que estábamos viendo y nos ofrece el siguiente cuadro para que le pongamos nombre a la nueva: 

En este ejemplo, la hemos llamado “2”. 

Cerrando esta ventana con OK , 

aparece la nueva sección 2 en la ventana Cross Section Data , que de momento es idéntica a la 1. Supongamos que, en nuestro ejemplo, hemos medido entre dos puntos del cauce situados a una distancia de 70 metros un desnivel de 0,90 metros. Sobre los datos de la sección 2 tenemos que cambiar dos cosas: 

a) Para asignar a toda la sección una cota 0,40 m más elevada, en el menú Options > Adjust elevations... , y en el cuadrito que sale, escribimos: +0.40. De vuelta en la ventana Cross Section Data , picamos en el botón y en el dibujo aparecerá la sección con sus nuevas cotas. 

b) Hemos de indicar que esta sección está a 70 metros de la siguiente estación aguas abajo, para ello, cambiamos los datos siguientes: 



(Como hemos dicho más arriba, se trata de la distancia medida por la margen izquierda, por el centro y por la margen derecha) 

> 4 Reference Manual, pp. 81‐83 

> 5 Reference Manual, pág 88 

- 6 - 

_F. Javier Sánchez San Román ‐ Dpto. Geología, Universidad de Salamanca ‐_ <u>http://web.usal.es/javisan/hidro</u> 

Cerramos la ventana Cross Section Data , y ahora en la ventana Geometric Data , ya deben aparecer las dos secciones 1 y 2, igual que en la figura de la pág. 3. (Podemos cerrar esta ventana Geometric Data ) 

### **<mark>Caudales</mark>** 

En la ventana principal de HEC‐RAS, picamos el botón , o bien, menú Edit > Steady Flow Data.. . 



En primer lugar hay que indicar el número de “perfiles” ( Profiles )  que hay que calcular. Con “perfiles” se refiere a diversas hipótesis de cálculo que deseamos plantear simultáneamente, para varios caudales. Es necesario al menos un dato de caudal para cada tramo y cada perfil. 

En nuestro ejemplo, hemos indicado (arriba) 2  perfiles, que aparecen inicialmente como PF1 y PF2 . Posteriormente, los hemos renombrado como 50 años y 200 años , (supongamos que se trata de caudales de retorno para esos periodos). El cambio de esos nombres se hace en el menú Options> Edit Profile Names.. . Para cada uno de los dos “perfiles” introducimos un dato de caudal (en m<sup>3</sup> /s) 

Los datos de caudal se introducen comenzando aguas arriba para cada tramo. Cuando se introduce un caudal en el extremo superior (aguas arriba), el programa supone el mismo caudal para el resto de secciones dentro de ese tramo del río, aunque pueden cambiarse en cada sección. 

En nuestro ejemplo, hemos indicado el caudal para la sección 2  (ver en la figura anterior: ), que es la sección que está situada aguas arriba, así que el programa supondrá que por la sección 1 (aguas abajo) pasa el mismo caudal. 

#### **Condiciones de contorno** 

En la ventana en que introducimos los datos de caudales es necesario especificar las “condiciones de contorno” ( Boundary conditions ), picando arriba en 



> <sup>6</sup> aparece  una nueva ventana. 

> 6 User’s Manual, pag 256,   Reference Manual, pág 91 (número de página del documento Acrobat) 

- 7 - 

_F. Javier Sánchez San Román ‐ Dpto. Geología, Universidad de Salamanca ‐_ <u>http://web.usal.es/javisan/hidro</u> 



HEC‐RAS necesita esta información en cada tramo para establecer el nivel del agua inicial en ambos extremos del tramo del río: aguas arriba  y/o aguas abajo. En un régimen subcrítico<sup>7</sup> sólo se necesita en el extremo de aguas abajo  (downstream); en régimen supercrítico, sólo es necesario aguas arriba (upstream), y si se va a calcular en un régimen mixto (por variaciones del caudal), se necesitaría en ambos extremos del tramo. 

Estas condiciones de contorno pueden valer para todos los “perfiles” (es decir: hipótesis de cálculo, varios caudales, en nuestro ejemplo: dos), o bien, podemos desear indicarlo específicamente para cada “perfil”, picando en la opción Set boundary for one profile at a time (=Indicar las condiciones de contorno para cada perfil). 

- Existen cuatro posibilidades (ver los botones de la figura de arriba): 

- **Alturas de la superficie del agua conocidas** ( Known Water Surface Elevations ). El usuario debe introducir la altura del agua para cada uno de los perfiles que se van a calcular 

- **Profundidad crítica** ( Critical Depth ). Con esta opción, el usuario no tiene que introducir nada. El programa calcula la profundidad crítica para cada uno de los perfiles y la utilizará como condición de contorno. 

- **Profundidad Normal** ( Normal Depth ). En este caso, el usuario debe introducir el pendiente de la línea de energía (egergy slope) que se utilizará para calcular la profundidad normal en ese punto (ecuación de Manning). Si no se conoce ese dato, se puede sustituir por la pendiente del agua o la pendiente del fondo del cauce. 

- **Curva de gastos** ( Rating Curve ). En esta opción debemos introducir una serie de parejas de valores nivel‐caudal 

### **<mark>Ejecución del modelo</mark>** 

En la ventana principal de HEC‐RAS, menú Run > Steady Flow Analysis... (ya que en este caso hemos utilizado un caudal constante ( Steady ). Aparece la correspondiente ventana (página siguiente). 

Si hemos preparado diversas geometrías (tramos y secciones) y varios caudales, aquí podremos elegir con cuales de ellos vamos a ejecutar los cálculos. 

> 7 Subcrítico (~ flujo lento) = nº Froude <1, Supercrítico (~ flujo rápido) = nº Froude >1 

- 8 - 

_F. Javier Sánchez San Román ‐ Dpto. Geología, Universidad de Salamanca ‐_ <u>http://web.usal.es/javisan/hidro</u> 

También hemos de especificar si el régimen es subcrítico (lento) o supercrítico (rápido), lo que debe estar de acuerdo con las condiciones de contorno especificadas: en régimen subcrítico, condiciones de contorno aguas arriba del tramo, régimen supercrítico, condiciones especificadas aguas abajo. 

Lo que aparece en 



esta ventana como 

“ Plan ” es el conjunto de condiciones elegidas para efectuar la computación (geometría, caudal, régimen). En el menú File se puede guardar este “Plan” ( Save Plan ) o comenzar uno nuevo ( New Plan ). 

Picando en se ejecutará el modelo, y si no obtenemos mensajes de error, podremos ver los resultados. 

### **<mark>Observación de los resultados</mark>** 

En la ventana principal de HEC‐RAS, menú View disponemos de varias opciones: 

- Secciones transversales (menú View >>Cross Sections... ) 

```
o
```



- Perfil longitudinal (menú View >> Water Surface Profiles... ) 

- Vista en perspectiva (menú View >> X-Y-Z Perspective Plots...) 

- Curva de gastos (menú View >> Rating Curve...) : Relación altura-caudal 

- Tabla para cada sección ( menú View >> Detailed Output Tables) 

- Tabla para todo el tramo ( menú View >> Profile Summary Table) 



- 9 - 

_F. Javier Sánchez San Román ‐ Dpto. Geología, Universidad de Salamanca ‐_ <u>http://web.usal.es/javisan/hidro</u> 

## Apéndice. Traducción Inglés ‐ Español de algunas palabras o expresiones 

|Add a new Cross Section...|Añadir una nueva sección transversal|
|---|---|
|Cross Section|Sección transversal (del cauce)|
|Downstream Reach Lenghts|Distancias (hasta la siguiente sección) aguas abajo|
|Enter a new river station for the new<br>cross section in reach...|Introducir una referencia para la nueva sección<br>transversal en el tramo...|
|Geometric Data|Datos Geométricos|
|New project...|Nuevoproyecto...|
|Plan|“Plan” (conjunto de datos geométricos y de caudal<br>que se eligenpara efectuar los cálculos)|
|Profile|“Perfil” (Hipótesis de cálculo con un cierto caudal)|
|Reach Boundary Conditions|Condiciones de contorno (de ese tramo)|
|Reach, River Reach|Tramo, Tramo del río|
|River Station|Referencia (un número)  de cada sección<br>transversal|
|Select existing River or enter a new<br>River name, and enter Reach name|Seleccione un nombre ya existente o introduzca un<br>nuevo nombre para el Rio, e introduzca un<br>nombrepara el Tramo|
|Set as default for new projects|Establecer “por defecto” para nuevos proyectos (o<br>sea: Recordar esta elección en el futuro)|
|Set boundary for all profiles|Establecer condiciones de contorno para todos los<br>perfiles (para todos igual)|
|Set boundary for one profile at a time|Establecer las condiciones de ocntorno de los<br>perfiles unopor uno|
|Station|(En la geometría de las secciones transversales:)<br>situación de cadapunto de la sección, en metros|
|Steady Flow|Caudal constante, o flujo uniforme o régimen<br>permanente|
|System International (Metric System)|Sistema Internacional (Sistema Métrico)|
|Unit system (US Customary/SI)|Sistema de unidades  (USA/ Sistema Internacional)|
|Unsteady Flow|Caudal variable, o flujo no uniforme o régimen<br>variable|



- 10 - 

_F. Javier Sánchez San Román ‐ Dpto. Geología, Universidad de Salamanca ‐_ <u>http://web.usal.es/javisan/hidro</u> 

