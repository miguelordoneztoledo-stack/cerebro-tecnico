---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\EIA\ECOMAS - DIPLOMADO EN ESTUDIO DE IMPACTO AMBIENTAL\DIPLOMADO EN ESTUDIO DE IMPACTO AMBIENTAL\9.-MODULO IX-ELABORACION DE MAPAS TEMATICOS CON ARGCIS\DIPLOMADO EIA[SEAT-GIS_F].pdf"
---







**UNIVERSIDAD NACIONAL DE PIURA ESCUELA DE POSGRADO** 

**Elaboración de mapas temáticos con ArcGIS** 

**PONENTE:** 

**Ing. Salvador Alvarado Tovar MSc** 



## **_Temario_** 

- <u>Fundamentos de Cartografía y Escalas.</u> 



- Sistemas de información, geográfica y conceptos básicos de ARCGIS. 

- Fuentes de información cartográfica. 

- Elementos del mapa y construcción de mapas base y temáticos. 

- Modelamiento espacial. 

- Análisis espacial multicriterio. 



###### **Fundamentos de la cartografia** 









**Antiguo Egipto** 

**Babilonios** 

**Mapa astronómico Chino** 



**Europa de la Edad Media** 



**Cartografía en el Renacimiento** 





**Cartografía Contemporánea** 





**Mapamundi de Ptolomeo** 

**Proyección de Mercator** 



<!-- Start of picture text -->
Fotografías Aéreas<br><!-- End of picture text -->



**Imágenes de Satélite** 







###### **Fundamentos de la cartografia** 



Cartografiar consiste en representar una porción de la superficie terrestre sobre una superficie reducida, generalmente plana. El producto de la cartografía son los mapas, las cartas y los planos. 







Para la elaboración de los mapas se deben resolver de forma satisfactoria tres problemas : 



###### **Fundamentos de la cartografia** 





<!-- Start of picture text -->
CARTOGRAFÍA PROBLEMAS SOLUCIONES<br>a) Trasladar un espacio real<br>grande a un espacio  ESCALA<br>dibujado pequeño<br>b)  Dibujar un superficie esférica<br>(tierra) en un espacio plano  PROYECCIÓN<br>(mapa).<br>c)  Representar un espacio<br>tridimensional (realidad) sobre un<br>TOPOGRÁFÍA<br>espacio bidimensional (mapa).<br><!-- End of picture text -->



###### **Diferencia entre plano y mapa** 



La escala tiene sentido si las distancias entre puntos de la representación plana son proporcionales. Si el **mapa** abarca una región terrestre amplia, es imposible conservar la proporción de todas las distancias entre puntos, debido a la curvatura de la tierra. 





En el caso de espacios pequeños, como un terreno, una urbanización o una ciudad, la región que queremos representar se aproxima mucho a una región plana. Decimos que se trata de un **_plano_** . En el caso de continentes o grandes regiones, se debe escoger algún tipo de proyección y esto produce ciertas deformaciones, alterando las distancias, los ángulos o las áreas y estaríamos hablando de **mapas** . 

Fuente: http://maps.google.es/ y CNICE 



###### **Sistemas de Coordenadas** 



Es un conjunto de valores que permiten definir de manera única e irrepetible la posición de cualquier punto en un espacio. 

Todo mapa deberá está referido a por lo menos un sistema de coordenadas universal. 

Existen varios tipos de sistemas de coordenadas, El más común es el Sistema de Coordenadas Geográficas: paralelos y meridianos, los cuales forman una retícula que envuelve a la Tierra para poder ubicar y localizar cualquier punto en su superficie. 



###### **Sistemas de Coordenadas Geográfica** 

Divide a la Tierra en una serie de anillos imaginarios paralelos al Ecuador llamados paralelos 

y una serie de semicírculos perpendiculares al Ecuador que convergen en los polos llamados meridianos 

Es un conjunto de valores que permiten definir de manera única e irrepetible la posición de cualquier punto en un espacio. 

Son los Valores de Latitud y de Longitud que indican la posición vertical y horizontal de un punto sobre la superficie de la Tierra en un mapa, están expresados en grados, minutos y segundos 







###### **Proyecciones** 



Al ser La Tierra casi esférica, no es posible representarla sobre un plano, a escala, pues la esfera es una figura geométrica que no se puede desarrollar (transformar en plano, como si se puede hacer con un cono, un cilindro, o un poliedro). Para representar la esfera terrestre se debe escoger un método de proyección. Estos métodos son muy variados y debemos conocer sus propiedades para poder decidir cuál es el que más nos conviene para el fin para el que queremos utilizar el mapa. 





<!-- Start of picture text -->
Cubo<br><!-- End of picture text -->





<!-- Start of picture text -->
¿?<br>Esfera<br><!-- End of picture text -->

Cono 



###### **Tipos de proyecciones** 





**Cilíndricas** 







**Cónicas** 

**AZIMITAL** 



###### **Propiedades geométricas de las proyecciones** 



PROYECCIÓN  CONFORME:   conserva el ángulo entre dos puntos medidos en la superficie de referencia y en el mapa. Si no lo conserva se dice que la proyección tiene anamorfosis angular. 



PROYECCIÓN  EQUIDISTANTE:  conserva las distancias; en todo el mapa no se cumple esta propiedad, pero debido a la escala, se puede considerar que las deformaciones son tan pequeñas que se admiten como tolerables. Cuando la proyección no cumple esta propiedad tiene anamorfosis lineal. 

PROYECCIÓN  EQUIVALENTE:  conservan las superficies. Cuando no lo cumplen tienen anamorfosis superficial. 

PROYECCIÓN  AFILÁCTICA:  no conservan ninguna de las propiedades anteriores pero tienen valores tolerables para determinadas zonas. 



**UTM (Proyección Universal Transversal de Mercator)** 



El sistema de proyección universal transversal de Mercator (UTM) es una proyección que divide el globo en 60 zonas, cada una de las cuales abarca 6° de longitud a partir del meridiano de Greenwich de este a oeste. 











**UTM (Proyección Universal Transversal de Mercator)** 



###### **UTM (Proyección Universal Transversal De Mercator)** 



El origen de una coordenada UTM es la intersección del meridiano central con el ecuador  a este origen se le da un valor relativo de 500 km ESTE, y 0 km norte cuando consideramos el hemisferio norte y un valor de 500 km ESTE y 10.000 km norte cuando consideramos el hemisferio sur 









###### **Datum** 

Es un modelo matemático basado en un elipsoide, que permite representar un punto de la mejor forma posible en un mapa con sus valores de coordenadas. 













**Datum** 



###### **Datum (WGS 1984)** 



El WGS84 es un sistema de coordenadas geográficas mundial que permite localizar cualquier punto de la Tierra (sin necesitar otro de referencia) por medio de tres unidades dadas. WGS84 son las siglas en inglés de World Geodetic System 84 (que significa Sistema Geodésico Mundial 1984). El Sistema Geodésico Mundial es un estándar para su uso en la cartografía, geodesia y navegación 



###### **DATUM (PSAD 56)** 



El PSAD56 (Provisional Sudamericano 56) es un sistema de proyección de coordenadas de tipo proyección cilíndrica y su punto de referencia está dado por la ciudad de laLa Canoa en Venezuela. 

En el Perú buena parte de la información geoespacial procesada por las instituciones publicas hasta antes del 2000 se generaba en usando esta proyección 





###### **Consideraciones importantes** 

**1.Datum Geodésico 2.Tipo de Proyección 3.Unidades de Medida** 



**4.Precisión de las Coordenadas** 

**5.Conversión entre Sistemas de Coordenadas 6.Zona UTM (en caso de UTM)** 

**7.Transformaciones de Coordenadas 8.Aplicación Específica** 



###### **Escala** 



La escala de un mapa es el cociente entre las distancias medidas sobre el mapa y las correspondientes distancias reales sobre el terreno. Se utilizan para poder reducir de manera proporcional el tamaño real de un espacio. Sobre un mapa puede venir indicada de dos maneras: 

**Escala numérica** 1: 50000 

Indica la relación entre la realidad y el mapa en forma de cociente, siendo el numerador la distancia sobre el mapa y el denominador la distancia en la realidad. 



###### **Escala gráfica** 

Indica mediante segmentos la distancia real que corresponde a cada uno de ellos. 

###### **Escala cromática** 

En los mapas que representan, por ejemplo, el relieve de un terreno, se utilizan diferentes colores para identificar las distintas alturas y profundidades. 





###### **Aspectos importantes** 



Debemos tener en cuenta que las escalas siempre tendrán valores exactos, convencionalmente no se aceptan escalas con valores decimales o fraccionados 



###### **Escalas Correctas** 

###### **Escalas Incorrectas** 

1/5000 1/5300 1/10000 1/10030 1/25000 1/25700 1/50000 1/52356 1/100000 1/100200 1/250000 1/2500,20 



###### **Escalas Pequeñas** 

Representan amplias zonas de la superficie terrestre por lo general usan sistemas de coordenadas geográficas y no presentan detalles 

**Ejemplos** : 

1/100000 1/250000 



###### **Aspectos importantes** 

###### **Escalas grandes** 

Representan pequeñas zonas de la superficie terrestre por lo general usan sistemas de coordenadas proyectadas como las UTM 

**Ejemplos:** 



1/500 

1/5000 1/10000 









**Ejemplo** 





###### **Topografía** 

Un mapa tiene dos dimensiones, anchura y profundidad, mientras que en la realidad existen tres, ya que también tenemos la altura. 





<!-- Start of picture text -->
PROFUNDIDAD<br>ANCHURA<br><!-- End of picture text -->



<!-- Start of picture text -->
ALTURA<br>Nivel del mar<br>PROFUNDIDAD<br>ANCHURA<br><!-- End of picture text -->

MAPA: dos dimensiones 

REALIDAD: tres dimensiones 



**Mapas topográficos** , representan gráficamente los principales elementos que conforman la superficie terrestre, como vías de comunicación, entidades de población, hidrografía, relieve, con una precisión adecuada a la escala. 





###### **Topografía** 





<!-- Start of picture text -->
la<br>las<br><!-- End of picture text -->

**Mapa administrativo** , Representa los hechos principales de la organización administrativa de un territorio especialmente las cuestiones relativas a las fronteras, divisiones y capitales. 



###### **Curvas de Nivel** 









<!-- Start of picture text -->
.<br><!-- End of picture text -->

Las curvas de nivel unen puntos con la misma altitud. Las curvas de nivel son equidistantes, normalmente cada 20 metros. Aquellas líneas que coinciden con números exactos múltiplos de cien son las llamadas **curvas maestras** . Suelen ser ellas las únicas que llevan indicación de la altura en el propio mapa. 



###### **Curvas de Nivel** 







A partir de las curvas de nivel de un mapa se pueden realizar cortes topográficos, que no son mas que un gráfico en el que en el eje vertical se localizan las alturas y en el horizontal los lugares por los que pasa la curva de nivel. Uniendo los puntos aparece el perfil del relieve . 



###### **Símbolos cartográficos** 



Los símbolos cartográficos son representaciones de los distintos elementos que se encuentran en la superficie terrestre. Para poder uniformar la lectura de los mapas se acordó su forma a través de convenciones internacionales. 











**UNIVERSIDAD NACIONAL DE PIURA ESCUELA DE POSGRADO** 

**Elaboración de mapas temáticos con ArcGIS** 

**PONENTE:** 

**Ing. Salvador Alvarado Tovar MSc** 



## **_Temario_** 

- Fundamentos de Cartografía y Escalas. 



<!-- Start of picture text -->
.<br><!-- End of picture text -->

- <u>.</u> 

- <u>Sistemas de información, geográfica y conceptos básicos de ARCGIS</u> 

- Fuentes de información cartográfica. 

- Elementos del mapa y construcción de mapas base y temáticos. 

- Modelamiento espacial. 

- Análisis espacial multicriterio. 



###### **Desarrollo de los GIS en la historia** 



###### **Década de 1960:** 

Se considera que el desarrollo de los SIG comenzó en la década de 1960 con investigaciones y experimentos iniciales en el campo de la cartografía automatizada y el procesamiento de datos espaciales. 

###### **Década de 1970:** 

En la década de 1970, se introdujeron los primeros sistemas computarizados que permitían el almacenamiento y análisis de datos geoespaciales. Surgieron proyectos gubernamentales y académicos. 

###### **Década de 1980:** 

Los SIG se volvieron más accesibles y comenzaron a utilizarse en diversas disciplinas, incluyendo la planificación urbana, la gestión de recursos naturales y la geografía. Las tecnologías de hardware y software avanzaron significativamente. Década de 1990: 



###### **Desarrollo de los GIS en la historia** 



**Durante los años 90** , los SIG se volvieron más comunes en organizaciones gubernamentales, empresas y sectores académicos. El acceso a datos geoespaciales mejoró con la disponibilidad de información satelital. 

###### **Principios de los años 2000:** 

Los SIG se integraron en la vida cotidiana a través de servicios basados en la ubicación, como los sistemas de navegación GPS y las aplicaciones de mapas en línea. La interoperabilidad y la estandarización de datos se volvieron temas importantes. 

###### **Década de 2010:** 

Los SIG siguieron evolucionando con el auge de la tecnología móvil y la recopilación masiva de datos geoespaciales. La nube y las plataformas en línea facilitaron el acceso y la colaboración en tiempo real. 

###### **Década de 2020:** 

Los SIG continúan avanzando con tecnologías como la inteligencia artificial y el aprendizaje automático aplicadas al análisis espacial. La visualización de datos geoespaciales se ha vuelto más inmersiva y accesible. 



##### **¿Qué es un GIS O SIG?** 

Un sistema de información geográfica es una herramienta informática que nos permite crear, almacenar, analizar, manipular y representar cartográficamente todo tipo de datos. Con la finalidad de poder tomar las mejores decisiones respecto a diversos problemas que se presentan en el  territorio. 











**El mundo real** 













**Introducción a los Sistemas de Información Geográfica** 











**Como se muestra la información en un SIG** 





###### **Esquema metodológico de los SIG** 



<!-- Start of picture text -->
Mundo Real<br>Fuente de<br>Información<br>SIG<br>Usuarios<br>Manejo de<br>Datos<br>Análisis<br><!-- End of picture text -->







##### **Funciones de un SIG** 

**Recopilar** información **Gestionar y Almacenar** datos que se convertirán en información **Consultar y Analizar** los datos que hemos almacenado **Visualizar** la información mediante mapas gráficos  que permitan una optima toma de decisiones por las autoridades **Difundir** los resultados o las alternativas de solución a determinados problemas 



**Procedimientos** 

**Personas** 

##### **Componentes de un GIS** 









**SIT** 

**Hardware y Software** 

**Datos** 



Los programas SIG pueden almacenar muchos datos,  que están asociados a cierto lugares o ámbitos del territorio 

- Datos vectoriales 

- Datos raster 

###### **Datos GIS/SIG** 





Los datos vectoriales proporcionan una forma de representar entidades del mundo real dentro del entorno GIS 

Una característica común de los SIG es que asociar información no permiten (datos geográficos) con los lugares (datos geográficos). De hecho, un programa SIG puede almacenar muchos datos que están asociados a cada lugar, estos datos los almacena en una base de datos 



###### **Datos Vectoriales** 







**Formas de los Datos Vectoriales** 







Una polilínea 



<!-- Start of picture text -->
Un punto<br><!-- End of picture text -->





<!-- Start of picture text -->
DIAGRAMA FUNCIONAMIENTO DE LOS DATOS<br>VECTORIALES<br>Datos<br>vectoriales<br>Punto Línea  Polígono<br>Cuenta con  Tiene al  Cuenta con  Tiene al  Cuenta con<br>Un solo vértice atributos que  menos dos  atributos que  menos cuatro  atributos que<br>lo describen  vértices lo describen  vértices lo describen<br>X (Longitud) X (Longitud) X (Longitud)<br>Y(Latitud) Y(Latitud) Y(Latitud)<br><!-- End of picture text -->



#### **Que podemos lograr con los SIG** 

El verdadero poder de los SIG comienza a manifestarse cuando nos empezamos a hacer preguntas del tipo. ¿Cuántas viviendas están dentro del área inundable de un río? ¿Dónde está el mejor lugar para proponer la ubicación de un hospital ¿Cuál es la mejor ubicación para zonas de expansión urbana?”. 





###### **Problemas con los datos vectoriales** 



###### Problemas comunes de los datos vectoriales 

- Toma tiempo y dinero la captura de los datos. 

- Ausencia de procedimientos para la captura y mantenimiento de datos. 

- Limitado presupuestos para manteamiento de la información. 

- Personal de manteamiento de datos no tiene el cuidado en el proceso de edición de datos. 





#### **Atributos de los datos vectoriales** 







Si todas las líneas de un mapa fueran del mismo color, ancho, grosor y tuvieran la misma etiqueta, sería muy difícil distinguir lo que estaba pasando. El mapa también nos daría muy poca información 





###### **Como se almacenan los datos vectoriales** 

Existen diferentes formatos para datos SIG, pero el mas común es el **Shapefile,** es un formato vectorial de almacenamiento digital donde se guarda la localización de los elementos geográficos y los atributos asociados a ellos. 

Un shapefile es un formato multiarchivo, es decir, está generado por varios ficheros informáticos. 





##### **SHP** 



Si desea compartir datos vectoriales almacenados en shapefiles con otra persona, es importante darles todos los archivos para esa capa. Entonces, en el caso de la capa de árboles que se muestra en necesitaría darle a la persona 

Las base de datos es una buena solución porque la base de datos puede almacenar **grandes cantidades** de datos **eficientemente** 





Los rásters están formados por una matriz de píxeles (también llamados celdas) Cada uno de los cuales contiene un valor que representa las condiciones para el área cubierta por esa celda. 

Un conjunto de datos ráster esta compuesto de filas (corriendo de un lado a otro) y columnas (corriendo hacia abajo) de píxeles (también conocidos como celdas). Cada píxel representa una región geográfica, y el valor en ese píxel representa alguna característica de dicha región 



#### **Datos raster** 









#### **Datos ráster** 







Imágenes ráster de color verdadero (izquierda) son útiles ya que proporcionan una gran cantidad de detalles que es difícil de captar como objetos espaciales vectoriales, pero fácilmente de notar al ver la imagen ráster. 

Los datos ráster también pueden ser no fotográficos, como la capa ráster mostrada a la derecha 





#### **Georreferenciación** 

Georeferenciar es el de definir proceso exactamente en que parte de la superficie de la tierra fue creada una imagen o conjunto de datos ráster, tomando como referencia Cuando el programa GIS abre la imagen, utiliza la información de posición para asegurar que aparezca en el lugar correcto en el mapa 







#### **Fuentes de datos ráster** 



Los rásteres pueden ser obtenidos de diversas formas, las mas comunes son las imágenes de satélite y las fotografía aéreas 

En fotografía aérea, un avión sobrevuela un área con una cámara montada debajo. Luego, las fotografías se importan a una computadora y se georreferencian. 

Las imágenes de satélite se crean cuando los satélites que orbitan alrededor de la Tierra apuntan cámaras digitales especiales hacia la Tierra y luego toman una imagen del área terrestre por la que pasan . 









#### **Resolución espacial** 



La resolución espacial (también conocido como el tamaño de celda) es la dimensión del área de terreno representada por una sola celda. 

La escala es la proporción o relación entre una distancia o área en un mapa (o imagen) y la correspondiente distancia o área sobre el terreno. Normalmente se expresa como una fracción o proporción. La resolución espacial o tamaño de celda influye en el nivel de detalle de una imagen en una escala dada 





### **Comparación** 



|**Punto de comparación**|**Datos vectores**|**Datos raster**|
|---|---|---|
|Representación de datos|Se representan mediante puntos, líneas y<br>polígonos|Se representan mediante una cuadrícula de celdas<br>o píxeles|
|Tipo de datos|Adecuados para representar características<br>geográficas discretas|Adecuados para representar fenómenos<br>geográficos continuos|
|Precisión espacial|Mayor precisión espacial debido a la<br>representación detallada de la geometría de los<br>objetos geográficos|Precisión espacial limitada por el tamaño de la<br>celda o píxel|
|Tamaño de archivo|Tamaño de archivo más compacto en<br>comparación con los datos raster|Tamaño de archivo más grande debido a la gran<br>cantidad de datos almacenados en cada celda o<br>píxel|
|Análisis espacial|Más adecuados para análisis que requieren la<br>identificación precisa de la ubicación de objetos<br>geográficos|Más adecuados para análisis que implican la<br>manipulación de datos continuos|
|Edición y actualización|Más fáciles de editar y actualizar debido a la<br>modificación de puntos, líneas y polígonos<br>individuales|Más difíciles de editar y actualizar debido a la<br>manipulación de la cuadrícula de celdas completa|
|Visualización|Visualización más clara y precisa debido a la<br>representación detallada de la geometría de los<br>objetos geográficos|Más adecuados para la superposición de capas y la<br>representación de la información en diferentes<br>escalas|









##### **Obtención de datos** 

**VECTOR                                   RASTER** 

Digitalización manual o automática de un mapa impreso Datos de Autocad GPS / Topografía Mediciones fotogramétricas 

Percepción remota Imágenes satelitales Vuelos de drones Scanner 





















**Softwares GIS** 





##### **Aplicaciones de los SIG** 

- Planificación Urbana y Regional 

- Gestión de Recursos Naturales 

- Cartografía y Producción de Mapas 

- Servicios de Emergencia y Gestión de Desastres 

- • Salud Pública 

- Análisis de Mercado y Ubicación Comercial 

- • Gestión Ambiental y Conservación 

- Transporte y Logística 

- Agricultura de Precisión 

- Educación 

- Investigación Científica 

- Defensa y Seguridad 







###### **Aplicaciones de los SIG en Medio Ambiente** 

- Cartografía de Ecosistemas y Hábitats 

- Análisis de Cambios en el Uso del Suelo 

- Modelado de Impacto Ambiental 

- Monitoreo de Calidad del Agua y del Aire 

- Gestión de Residuos y Vertederos 

- Identificación y Evaluación de Riesgos Naturales 

- Monitoreo de Biodiversidad 

- Evaluación de Impacto Ambiental (EIA) 

- Planificación de Corredores Ecológicos 

- Estudios de Carga Contaminante 

- Identificación de Zonas Sensibles 

- Planificación de Energías Renovables 











**ArcGis** 



## **_Temario_** 

- Fundamentos de Cartografía y Escalas. 



- Sistemas de información, geográfica y conceptos básicos de ARCGIS. 

- • <u>Fuentes de información cartográfica.</u> 

- Elementos del mapa y construcción de mapas base y temáticos. 

- Modelamiento espacial. 

- Análisis espacial multicriterio. 



###### **Fuentes de Información cartográfica** 





https://www.geoidep.gob.pe/servicios-idep 



#### **Geoportales** 



|Geoportales|Direccion WEB|
|---|---|
|Presidencia del Consejo de Ministros|http://www.geoidep.gob.pe/servicios-idep/geoportales|
|Presidencia del Consejo de Ministros|https://visor.geoperu.gob.pe/|
||http://geoservidorperu.minam.gob.pe/geoservidor/download.a|
|Ministerio del Ambiente|spx|
|Ministerio de Educacion|http://sigmed.minedu.gob.pe/descargas/#|
|Ministerio de Trasportes y Comunicaciones|http://portal.mtc.gob.pe/estadisticas/descarga.html|
|SERNANP|http://geo.sernanp.gob.pe/geoserver/principal.php|
|Autoridad Nacional del Agua|https://snirh.ana.gob.pe/ObservatorioSNIRH/|
|Instituto del Mar del Perú|https://satelite.imarpe.gob.pe/#/|
|Instituto Geográfico Nacional|http://www.idep.gob.pe/|
|Instituto Nacional de Estadística e Informática|https://ide.inei.gob.pe/|
|Instituto Nacional de Investigación en<br>Glaciares|https://inaigem.gob.pe/web2/geoportal/|
|Ministerio de Cultura|https://sigda.cultura.gob.pe/|
|Ministerio de Cultura|https://geoportal.cultura.gob.pe/mapa/portal|









**UNIVERSIDAD NACIONAL DE PIURA ESCUELA DE POSGRADO** 

**Elaboración de mapas temáticos con ArcGIS** 

**PONENTE:** 

**Ing. Salvador Alvarado Tovar MSc** 



## **_Temario_** 

- Fundamentos de Cartografía y Escalas. 



- Sistemas de información, geográfica y conceptos básicos de ARCGIS. 

- Fuentes de información cartográfica. 

- <u>Elementos del mapa y construcción de mapas base y temáticos.</u> 

- Modelamiento espacial. 

- Análisis espacial multicriterio. 





#### **Generalización de  mapas** 



La generalización en cartografía se refiere al proceso de simplificar y representar de manera más clara y comprensible la información geográfica en un mapa. Sin embargo, este proceso puede llevar a la pérdida de detalles. 





##### **Aspectos que afectan la generalización** 



**La precisión:** esta referida a la posición de los elementos representados en el mapa respecto a su verdadera ubicación sobre el terreno 

**Escala del Mapa:** La escala del mapa influye directamente en el nivel de detalle que puede representarse. A escalas más pequeñas, se requiere mayor generalización para abordar la reducción de detalles. 

**Propósito del Mapa:** El propósito del mapa determinará la cantidad de generalización necesaria. Por ejemplo, un mapa turístico puede requerir menos generalización que un mapa de referencia para la planificación urbana. 



###### **Área mínima cartografiable en un mapa (AMC)** 



El término "área mínima cartografiable" se refiere al tamaño más pequeño de una característica o elemento geográfico que puede ser representado de manera efectiva en un mapa. 

Cuando se cartografía una región, especialmente a escalas pequeñas, no es posible representar todos los detalles exactos del terreno o de los objetos presentes. Algunas características geográficas son tan pequeñas en comparación con la escala del mapa que representarlas de manera precisa no sería práctico ni útil. 





Un mapa provincial detallado usaría una escala de 1:200.000 o 1:100.000, por ejemplo, según el tamaño de la provincia o del tamaño que se desee para el mapa 



##### **Escala de generalización** 







**Escala Gráfica:** La escala gráfica muestra la relación entre las distancias en el mapa y las distancias reales en la Tierra. Puede expresarse en unidades como kilómetros o millas. 

**Escala Numérica:** La escala numérica es una representación numérica de la relación entre las distancias en el mapa y las distancias reales en la Tierra. Por ejemplo, 1:50,000 indica que una unidad en el mapa es igual a 50,000 unidades en la realidad. 



###### **Escala** 





**1:1,000 1:25,000 1:50,000 1:100,000** 



###### **Título del Mapa** 





Uno de los elementos de un mapa más básicos y simples, pero que sin embargo son uno de los que más facilitan comprender que se está viendo. El título nos indica con palabras la temática representada, la zona geográfica o el tipo de mapa que estamos observando. Por ejemplo “mapa climático” o “mapa político del Perú”. 





La simbología en un mapa se refiere al conjunto de símbolos y convenciones gráficas utilizadas para representar diferentes características geográficas y temáticas en el mapa. 

Estos símbolos son elementos visuales que comunicar información de manera permiten eficiente y comprensible. La simbología es esencial para la interpretación correcta de un mapa y para transmitir de manera efectiva la información geoespacial. 



###### **Simbología** 





















###### **Simbología (ccpp)** 



Es la representación de las diferentes ciudades, poblados, asentamientos y caseríos que se localizan en una región determinada. 

En mapas topográficos la jerarquía político territorial de los centros poblados se indica con un tamaño, forma y tipología de nomenclatura que se adapta a la escala de edición del mapa. 

En cartografía a escalas pequeñas y en cartografía temática la clasificación de los centros poblados se apoya con el uso de una simbología específica, tal y como se señala a continuación: 





Los topónimos son nombres geográficos que se utilizan para identificar y referirse a lugares específicos en la superficie terrestre. Estos nombres pueden abarcar una amplia gama de características geográficas, como ciudades, pueblos, ríos, montañas, valles, lagos, islas y otros elementos geográficos y culturales. Los topónimos suelen reflejar la historia, la cultura, la geografía y otros aspectos relevantes de un lugar 



###### **Toponimos** 





###### **Cuadricula (grilla)** 



La cuadrícula o grilla de un mapa es una red de líneas imaginarias que divide la superficie del mapa en celdas o cuadrados. Estas líneas forman un sistema de coordenadas que facilita la localización precisa de puntos en el mapa. 

La cuadrícula es una herramienta importante en la cartografía y se utiliza para varios propósitos, como la referencia espacial, la medición de distancias y la ubicación de elementos geográficos. 





###### **Norte (rosa de vientos)** 



La rosa de los vientos, también conocida como el norte, es un símbolo cartográfico que representa las direcciones cardinales y subcardinales en un mapa. Esta herramienta ayuda a los lectores del mapa a orientarse y entender la disposición de los elementos geográficos en relación con los puntos cardinales. 





###### **Membrete** 



El membrete en un mapa es una sección o área generalmente ubicada en la parte inferior o en una esquina del mapa que contiene información clave sobre la cartografía, el mapa en sí o la entidad que lo produce. 

Es una especie de encabezado detalles que proporciona importantes relacionados con la fuente de información, la fecha de creación, el propósito del otros elementos mapa y relevantes. 









###### **Elaboración de un mapa temático** 





https://geoservidor.minam.gob.pe/zee-aprobadas/cajamarca/ 

https://geoservidor.minam.gob.pe/zee-aprobadas/cusco/ 



## **_Temario_** 

- Fundamentos de Cartografía y Escalas. 



- Sistemas de información, geográfica y conceptos básicos de ARCGIS. 

- Fuentes de información cartográfica. 

- Elementos del mapa y construcción de mapas base y temáticos. 

- <u>Modelamiento espacial.</u> 

- Análisis espacial multicriterio. 



###### **Modelado espacial** 



El modelamiento cartográfico3 es un conjunto de operaciones de análisis y comandos interactivos utilizando mapas que actúan como una superposición, cuyo fin es procesar decisiones de tipo espacial. La realidad está representada en mapas. 

Este modelamiento está orientado a procesos y no a productos. Se refiere a la utilización de las funciones de análisis de un sistema de información geográfica bajo una secuencia lógica, de tal manera que se puedan resolver problemas espaciales complejos 





###### **Características de los modelados** 



 Presentación de una secuencia lógica de operaciones analíticas expresadas en diagramas de flujo.  Usualmente esta codificados en macros; es decir, lenguajes de comandos  Apoyan el uso de SIG en planeamiento, realización de consensos y resolución de conflictos. 





###### **Tipos de modelamientos** 



**Modelo Descriptivo** Este modelo presenta información directamente de los patrones y distribuciones de rasgos o elementos espaciales. Dicho modelo no conduce a recomendaciones. 

**Modelo de Simulación** El presente modelo trata de crear escenarios ficticios o potencialmente reales simulando un fenómeno complejo de la naturaleza o los que estiman que puedan suceder bajo ciertas condiciones. 





###### **Tipos de modelamientos** 



**Modelo de Decisión y/o Predictivo** Dicho modelo, es una técnica SIG de gran potencial, trata de generar escenarios futuros de acuerdo a tendencias o modelamiento estadístico a partir de datos de ocurrencia histórica y reales. 

Se analiza la forma como intervienen los factores en el tiempo, cómo están asociados e identifica qué factores son adecuados en el proceso de la solución de un problema. 



###### **MODELAR  ESCENARIOS** 

**ANÁLISIS INTEGRADO DE DATOS ESPACIALES Y DE ATRIBUTOS** 



###### **Análisis y modelamiento** 



**PRODUCIR  NUEVA INFORMACIÓN** 





**MÚLTIPLES ALTERNATIVAS** 



**ANALISIS INTEGRADO DE DATOS ESPACIALES Y NO ESPACIALES** 





###### **Funciones  de análisis de los GIS** 

**OPERACIONES DE CONSULTA RECLASIFICACIÓN MEDICION** 



**OPERACIONES SUPERPOSICION** 

**Funciones de búsqueda Línea en polígono y punto en polígono Funciones topográficas Polígonos de Thiessen Interpolación Generación de isolíneas** 

**OPERACIONES DE VECINDAD** 

**Contigüidad Proximidad Redes Esparcimiento Optimización de rutas Intervisibilidad Iluminación Vista en perspectiva** 

**OPERACIONES DE CONECTIVIDAD** 









**Modelamientos** 



###### **Modelos de elevación digital mediante imágenes** 



ASTER DEM hace referencia a un conjunto de datos de modelos de elevación digital derivados de la misión ASTER (Advanced Spaceborne Thermal Emission and Reflection Radiometer) a bordo del satélite Terra de la NASA. 

El ASTER DEM se genera a partir de datos estereoscópicos de imágenes adquiridas por el instrumento ASTER. Estos datos estereoscópicos permiten medir las diferencias de elevación y crear un modelo de elevación digital de alta resolución. 

Precisión relativa de 10 m sin puntos de control Precisión absoluta de 7 m metros con puntos de control 









**Modelos digital de terreno** 









**Modelos digitales de superficie** 





<!-- Start of picture text -->
)<br><!-- End of picture text -->



**Shuttle Radar Topography Mission** ( **SRTM** ) 



## **_Temario_** 

- Fundamentos de Cartografía y Escalas. 



- Sistemas de información, geográfica y conceptos básicos de ARCGIS. 

- Fuentes de información cartográfica. 

- Elementos del mapa y construcción de mapas base y temáticos. 

- Modelamiento espacial. 

- <u>Análisis espacial multicriterio.</u> 



###### **Análisis multicriterio** 



El análisis multicriterio en Sistemas de Información Geográfica (SIG) es una metodología que permite tomar decisiones espaciales al considerar y combinar múltiples criterios o factores relevantes para un problema o decisión específica. Esta técnica se utiliza para evaluar y comparar diferentes opciones o ubicaciones en función de varios criterios ponderados. 





###### **Aspectos a considerar en AMC** 



###### **1.Criterios Múltiples:** 

En lugar de basarse en un solo criterio, el análisis multicriterio implica la consideración de varios criterios que son relevantes para la toma de decisiones en un contexto espacial. 

**2.Pesos y Ponderación:** 

Cada criterio se pondera según su importancia relativa en la toma de decisiones. Los usuarios asignan pesos a los diferentes criterios para reflejar su relevancia en el contexto específico. **3.Mapas Temáticos:** 



Se utilizan mapas temáticos para representar la distribución espacial de cada criterio. Cada criterio se mapea y se presenta como una capa en un SIG. 



###### **Aspectos a considerar en AMC** 



3. **Superposición y Combinación:** 



La superposición de capas temáticas permite combinar la información de los diferentes criterios para obtener una evaluación integrada. 

4. **Análisis y Evaluación:** 

Se realiza un análisis para evaluar y clasificar las opciones o ubicaciones potenciales en función de la combinación de los criterios ponderados. 



###### **Aspectos a considerar en AMC** 



###### **6. Modelos de Decisión:** 

Algunos análisis multicriterio utilizan modelos de decisión formal para estructurar y automatizar el proceso de toma de decisiones. **7.Visualización:** 

Los resultados se pueden visualizar mediante mapas temáticos que representan la clasificación final o la ponderación de las ubicaciones en función de los criterios. 











**Análisis multicriterio de la ZEE** 



# **_Gracias por su atención_** 



**<u>.com atsalva@gmail</u> Celular 975586258** 



---
**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]
