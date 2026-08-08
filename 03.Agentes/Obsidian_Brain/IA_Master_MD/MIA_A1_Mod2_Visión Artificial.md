---
tags:
  - master_ia
  - teoria
source: MIA_A1_Mod2_Visión Artificial.pdf
---

**Módulo Visión Artificial** 



# **Módulo Visión Artificial** 

|**1. INTRODUCCIÓN A LA VISIÓN ARTIFICIAL ..........................................................04**|
|---|
|1.1. QUÉ ES LA VISIÓN ARTIFICIAL Y CUÁLES SON SUS OBJETIVOS .......................04<br>|
|1.1.1. OBJETIVOS DE LA VISIÓN ARTIFICIAL ......................................................10<br>|
|1.2. MÉTODOS Y PROCESOS .................................................................................22<br>|
|1.2.1. FASE 1. DISEÑO Y DESARROLLO .............................................................25<br>|
|1.2.2. FASE 2. IMPLANTACIÓN DEL SISTEMA. DESPLIEGUE ................................31|
|1.3. BREVE HISTORIA Y CAMPOS RELACIONADOS ................................................34<br>|
|1.4. CARACTERÍSTICAS EN LA ACTUALIDAD .........................................................36<br>|
|**2. TÉCNICAS DE PROCESAMIENTO DE IMÁGENES Y RECONOCIMIENTO VISUAL.**|
|**COLOR, FILTROS Y EXTRACCIÓN DE CARACTERÍSTICAS .......................................39**|
|2.1. PREPARACIÓN DEL ENTORNO DE DESARROLLO Y PRUEBAS ...........................39<br>|
|2.1.1. INSTALACIÓN DE PYTHON, ANACONDA Y JUPYTER NOTEBOOK ............41|
|2.1.2. INSTALACIÓN DE OPENCV ......................................................................52<br>|
|2.2. IMÁGENES, MATRICES Y COLOR  ...................................................................57|
|2.2.1. ESPACIO DE COLOR HSV ........................................................................61|
|2.2.2. ESPACIO DE COLOR CIELAB ....................................................................68|
|2.3. REPRESENTACIÓN Y TRANSFORMACIONES DE IMÁGENES .............................70<br>|
|2.3.1. REPRESENTACIÓN DE IMÁGENES ............................................................70<br>|
|2.3.2. TRANSFORMACIÓN DE IMÁGENES .........................................................77|
|2.3.3. OPERACIONES MORFOLÓGICAS .............................................................90|
|2.4. FILTRADO: DESENFOQUE, NITIDEZ Y SUAVIZADO ...........................................91|
|2.4.1. BLURRING Y DENOISING. ........................................................................94|
|2.4.2. SHARPENING ..........................................................................................97|
|2.5. DETECCIÓN DE BORDES, CONTORNOS, RECTAS Y ESQUINAS ........................98<br>|
|2.5.1. DETECCIÓN DE BORDES MEDIANTE CONVOLUCIÓN: SOBEL, PREWITT|
|Y LAPLACIAN EDGE ........................................................................................100|
|2.5.2. DETECCIÓN DE BORDES MEDIANTE CANNY .........................................101<br>|
|2.5.3. DETECCIÓN DE CONTORNOS ...............................................................106|
|2.5.4. DETECCIÓN DE RECTAS Y CÍRCULOS ....................................................108<br>|
|2.5.5. DETECCIÓN DE ESQUINAS ....................................................................114|
|2.6. EXTRACCIÓN DE CARACTERÍSTICAS GLOBALES E INVARIANTES:|
|DETECTORES Y DESCRIPTORES ............................................................................119|
|2.6.1. SIFT (SCALE-INVARIANT FEATURE TRANSFORM) ....................................119|
|2.6.2. SURF (SPEEDED UP ROBUST FEATURES) .................................................121|
|2.6.3. ORB (ORIENTED FAST AND ROTATED BRIEF) ..........................................123|
|2.7. FEATURE MATCHING Y RECONOCIMIENTO DE OBJETOS CON ORB ..............129|
|2.7.1. MATCHING POR FUERZA BRUTA ...........................................................130|
|2.7.2. RECONOCIMIENTO DE OBJETOS CON ORB Y BRUTE FORCE|
|MATCHING: HOMOGRAFÍA ............................................................................134|



|**3. APLICACIÓN DE OBJETIVOS Y DEEP LEARNING ..............................................137**|
|---|
|3.1. PREPARACIÓN DEL ENTORNO DE GOOGLE COLAB .......................................138|
|3.2. CLASIFICACIÓN DE OBJETOS MEDIANTE TÉCNICAS CLÁSICAS .....................142<br>|
|3.2.1. MÁQUINAS DE VECTORES DE SOPORTE (SVM Y K-NEAREST<br>NEIGHBORHS (KNN) ........................................................................................143<br>|
|3.2.2. ÁRBOLES DE DECISIÓN .........................................................................147<br>|
|3.3. CLASIFICACIÓN DE OBJETOS MEDIANTE DEEP LEARNING ............................149|
|3.3.1. LAS REDES NEURONALES CONVOLUCIONALES .....................................149<br>|
|3.3.2. MODELOS DE CNN PARA CLASIFICACIÓN DE OBJETOS ........................166<br>|
|3.4. DETECCIÓN DE OBJETOS MEDIANTE DEEP LEARNING ..................................175|
|3.4.1. REGION-BASED CONVOLUTIONAL NEURAL NETWORK (R-CNN) ............177|
|3.4.2. FAST R-CNN ..........................................................................................178|
|3.4.3. FASTER R-CNN ......................................................................................179|
|3.4.4. YOU ONLY LOOK ONCE (YOLO) ............................................................180|
|3.4.5. OTROS MODELOS .................................................................................183|
|3.4.6. EJEMPLO PRÁCTICO .............................................................................184|
|3.5. SEGMENTACIÓN DE OBJETOS MEDIANTE DEEP LEARNING ...........................189|
|3.5.1. CONVOLUTIONAL AND DECONVOLUTIONAL NETWORKS|
|(ENCODER-DECODER) .....................................................................................190|
|3.5.2. MASK R-CNN ........................................................................................194|
|3.5.3. LA FAMILIA DEEPLAB ............................................................................195<br>|
|3.5.4. EJEMPLO PRÁCTICO .............................................................................197|
|3.6. GANS (REDES GENERATIVAS ADVERSARIAS).................................................201|
|3.6.1. CONDITIONAL GAN: PIX2PIX ................................................................205|
|3.6.2. CYCLEGAN ...........................................................................................206|
|3.6.3. STYLEGAN ............................................................................................208<br>|
|**4. MACHINE VISION. INSTRUMENTACIÓN PARA LA VISIÓN ...............................210**<br>|
|4.1. ELEMENTOS BÁSICOS DE UN DISPOSITIVO DE CAPTURA ..............................211|
|4.1.1. EL SENSOR ............................................................................................211|
|4.1.2. EL OBJETIVO O LA LENTE ......................................................................214<br>|
|4.1.3. EL OBTURADOR Y EL TIEMPO DE EXPOSICIÓN ......................................218|
|4.1.4. FRAME RATE .........................................................................................220|
|4.2. TIPOLOGÍA DE DISPOSITIVOS DE CAPTURA ..................................................220|
|4.3. ORIGEN DE LA CAPTURA .............................................................................227<br>|
|4.3.1. SELECCIÓN DE UN CONJUNTO DE COMPONENTES ..............................228|
|**BIBLIOGRAFÍA ........................................................................................................230**|



**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

## **1. Introducción a la Visión Artificial** 

_“Los modelos de visión artificial de deep learning están basados en redes neuronales y aprenden automáticamente a solventar los objetivos deseados por medio del proceso de entrenamiento. El diseñador desarrolla la estructura de la red neuronal, pero las operaciones a nivel pixel son decididas por el propio algoritmo de forma autónoma.”_ 

### **1.1. Qué es la visión artificial y cuáles son sus objetivos** 

Actualmente, el mundo está inundado de imágenes y videos. Todos los teléfonos móviles tienen cámaras capaces de tomar fotografías y de capturar vídeos en movimiento, permitiendo que prácticamente cualquier persona puede crear contenido de este tipo y almacenarlo o subirlo a cualquier red social de su elección, donde se convertirán en un reclamo para los posibles seguidores del creador de contenido. 

La plataforma de video YouTube es el segundo motor de búsqueda más potente del mundo, en el que se suben miles de horas de video cada minuto, y miles de millones de vídeos son visualizados cada día. 

En definitiva, además del texto, las imágenes y los videos son el tejido básico de internet. Sin embargo, hay una gran diferencia entre estos dos tipos de información. Las computadoras tienen una relación sencilla con el texto, aunque no tanto con el lenguaje humano, como veremos más adelante. Es relativamente sencillo indexar texto y permitir realizar búsquedas sobre el mismo para obtener resultados precisos en cuestión de décimas de segundo, como hacen los buscadores más empleados en la actualidad. 

En el caso de las imágenes y los vídeos esta tarea se complica. Durante la mayor parte de la existencia de internet, el contenido de imágenes y vídeos no han sido procesados e indexados más que por el texto que las acompañaba y las conocidas etiquetas en blogs y redes sociales. Sin embargo, las máquinas no eran capaces de “ver” estas imágenes, y de comprender el contenido que sus píxeles almacenaban de forma exclusiva para humanos. 

Para nosotros, los humanos, procesar esta información es absolutamente trivial. Cualquier ser humano desde la infancia es capaz de realizar tareas tales como: 

- Describir con precisión el contenido de una imagen y lo que está sucediendo en ella 

- Resumir lo sucedido en un video que ve por primera vez en una línea de texto 

- Reconocer una cara que ha visto una única vez 

04 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Para conseguir que una máquina realice tareas similares a estas, es necesario desarrollar una serie de métodos y técnicas que se ejecuten de forma automática. Esta necesidad, generada hace décadas con el surgimiento de la fotografía digital, el vídeo digital, internet, los blogs y las redes sociales; así como derivada de necesidades en procesos de producción, son las que provocaron el surgimiento y auge de la Visión Artificial. 

La visión artificial, también denominada visión por computador, o en inglés, _Computer Vision_ , es un campo de estudio derivado de la Inteligencia Artificial. 

Este campo de estudio es interdisciplinar, y persigue el objetivo de obtener sistemas **capaces de interpretar información valiosa derivada de imágenes, vídeos** y otros tipos de captura – que serán analizados más adelante – de forma automática. Dentro del objetivo general de la IA de conseguir sistemas capaces de realizar tareas asociadas a seres inteligentes, la visión artificial se encarga de la parte relacionada con la comprensión de imágenes y vídeos. Para ello, trata de imitar el sistema compuesto por el ojo, el nervio óptico y el cerebro humano. 

En los seres humanos, el proceso de comprender el entorno que nos rodea mediante rayos de luz para formar imágenes comienza en el ojo. La luz penetra en el ojo atravesando la córnea, la pupila y el cristalino, y acaba llegando a la retina. En la retina, gracias a la fotosensibilidad de una serie de células denominadas conos y bastones que están alojadas en la misma, la naturaleza electromagnética de la luz es transformada en señales eléctricas. Estas señales eléctricas se desplazan a lo largo del nervio óptico hasta la corteza visual, la zona del cerebro encargada del procesamiento de imágenes. Mediante complejos sistemas de redes neuronales, nuestro cerebro es capaz de percibir realidades como la profundidad, los colores, las formas, los objetos y su tipología, sus bordes… 

Para tratar de emular este complejo sistema biológico, los ingenieros de IA han desarrollado a lo largo de las décadas diversas propuestas de sistema que siempre están basadas en la misma estructura. 

El dispositivo de captura, que es el ojo en el caso del ser humano, se sustituye por medio de cualquier sensor artificial compuesto por materiales sensibles a la luz. De igual forma que los conos y bastones, ciertos materiales como por ejemplo los llamados “semiconductores complementarios de óxido metálico” (CMOS) son capaces de generar una señal eléctrica cuya intensidad varía en función de la intensidad de la luz que reciben. Cada celda de este semiconductor, denominadas fotositos, actúa como una célula de la retina humana, generando una señal en reacción a la luz que recibe. 

La transferencia de esta señal generada, que en el ser humano ocurre a través del nervio óptico, se efectúa por medio de cualquier protocolo de transferencia. Este puede ser cableado o inalámbrico, tales como conexiones USB, Ethernet o Bluetooth que irán a la unidad de procesamiento visual. 

05 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por último, el paso más complicado es sustituir la corteza visual de forma artificial. Para lograr hacer esto es necesario dar con algoritmos de IA que sean capaces de cumplir con los mismos objetivos que el cerebro humano en el órgano de la visión. 



Si un sistema es adecuadamente planificado y desarrollado, la cantidad de información visual que es capaz de procesar es muy superior a la que puede procesar un ser humano, y por tanto es sencillo superar a este en numerosas tareas que veremos a lo largo del módulo. 

Actualmente, este es uno de los campos con mayor número de publicaciones científicas anuales dentro de la disciplina de la Inteligencia Artificial, así como uno de los sectores con más oferta de trabajo del mercado laboral actual. Está enmarcado en una posición multidisciplinar, ya que no solo emplea métodos asociados a aprendizaje automático para resolver sus problemas. Como veremos en la siguiente unidad, una gran cantidad de las herramientas que se emplean para el procesado y reconocimiento de imágenes distan de ser inteligentes, aunque el resultado de su correcta aplicación pueda llegar a parecerlo. Hay problemas de visión artificial que se solucionan mediante algoritmos considerados como ”clásicos” debido a sus características, mientras que otros precisan de los más complejos modelos de aprendizaje profundo basado en Redes Neuronales Convolucionales. 

Una de las tareas más importantes en el campo de la visión artificial es decidir en qué caso será necesario cada modelo, así como conocer las restricciones, ventajas y desventajas de cada una de las aproximaciones a la visión artificial. 

Es importante recalcar que la visión artificial va más allá del simple procesado de imágenes. En un procesamiento de imágenes estas sencillamente son manipuladas para obtener otras imágenes, a priori, de mejor calidad. Se modifican la iluminación, el contraste, la tonalidad de color, se eliminan imperfecciones, objetos no deseados… Si bien estas herramientas en ocasiones serán útiles para problemas de visión artificial, no generan conocimiento ni comprensión acerca de las imágenes por lo que no se consideran parte de la visión artificial ni de la inteligencia artificial. 

06 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Como ya hemos mencionado, la visión artificial trabaja con imágenes que trata de comprender y de las que extrae información relevante. Estas imágenes no son otra cosa que matrices de píxeles en las que cada posición de la matriz tiene un valor específico – profundizaremos en este concepto más adelante – relacionado con la intensidad de la luz que incide en dicho pixel. 

En la actualidad, la mayoría de imágenes con las que se trabaja son imágenes a color, representadas por los tres colores primarios de luz: rojo, azul y verde. Es importante comprender la diferencia entre los colores luz y los colores pigmento, ya que habitualmente estamos acostumbrados a trabajar con los segundos, más relacionados con las artes y los procesos de impresión. Sin embargo, dado que en este módulo vamos a tratar con imágenes digitales, vídeos y pantallas, los colores que usaremos y por tanto las operaciones que realicemos sobre ellos serán los colores luz. 

Los colores pigmento, denominados así por ser los empleados en la pintura desde tiempos ancestrales, se comportan de forma totalmente distinta que los colores luz. Los colores pigmento son aquellos que contienen todos nuestros útiles de dibujo, desde lápices y acuarelas hasta rotuladores o aerosoles, y que trasladamos a un lienzo, un folio de papel o un cartel publicitario. Estos colores, que son los que estudiamos desde la escuela, parten todos de un conjunto inicial de tres colores primarios: el magenta, el azul cian y el amarillo. A partir de estos colores junto con el blanco y el negro se pueden generar todos los pigmentos deseados para la fabricación de pinturas y tintas. Los pigmentos se estudian en un espacio de color denominado CMYK ( _Cyan, Magenta, Yellow, blacK_ ). Un espacio de color es la forma de representar cualquier color posible por medio de una serie de valores. En este caso, cada color tendrá un valor, que representará la cantidad de cian, magenta, amarillo y negro que tiene un pigmento determinado. Veremos los espacios de color en más profundidad en la siguiente unidad. El proceso por el cual la unión de los distintos colores primarios produce otros nuevos se denomina, en el caso de los colores pigmento, el proceso de **síntesis sustractiva** . 

Por ejemplo, si unimos un pigmento amarillo y un pigmento azul, obtendremos un pigmento verde. Y si unimos un pigmento magenta con otro amarillo obtendremos un color rojo intenso. 

Por otro lado, nos encontramos con los colores luz. Estos son los colores que perciben nuestros ojos como resultado de la luz blanca del sol impactando en objetos de distintas naturalezas, que absorben cierta parte de esta luz y solo reflejan otra, que es la que compone su color luz. Los colores luz primarios son los que ya hemos mencionado, rojo, verde y azul. Habitualmente estos colores se estudian en el espacio de color RGB ( _red, green, blue_ ), aunque existen otros muchos espacios de color que estudiaremos en la siguiente unidad. En este caso, los colores forman nuevos colores mediante el proceso de **síntesis aditiva** . Contra toda intuición, si unimos una luz roja con una luz verde, obtendremos una luz amarilla. Y si unimos todos los colores, obtendremos una luz perfectamente blanca. Esto ocurre así por los tipos de células que pueblan nuestra retina. 

07 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Ya hemos hablado de los conos y los bastones. Los bastones se emplean principalmente para distinguir formas, bordes y contrastes. Los conos son las células que reaccionan a distintos tipos de luz, indicando a nuestro cerebro el color de las cosas. Hay tres tipos de conos: sensibles a la luz en el espectro rojo, sensibles a la luz en el espectro azul, y sensibles a la luz en el espectro verde. Todos los demás colores se generan a nivel percepción en nuestro cerebro sumando la información de estos tres tipos de conos, mediante la ya mencionada síntesis aditiva. 

Este proceso es el que emplean todas nuestras pantallas para generar cualquier color necesario con tan solo tres LEDs por pixel: uno rojo, uno verde, y uno azul. Como podemos observar en el siguiente diagrama, la diferencia entre la síntesis sustractiva y la aditiva se percibe a simple vista. 



Comparación entre los colores primarios y su unión en los colores luz (izq.) y pigmento (dcha.) 

En definitiva, en visión artificial operaremos matemáticamente sobre estos tres colores dan lugar a las imágenes RGB ( _red, green, blue_ ). Una imagen es, en definitiva, un conjunto de tres matrices de pixeles, una para cada uno de los colores primarios. 

Una matriz es un conjunto de números o expresiones dispuestos de forma rectangular, es decir, en una disposición de filas y columnas. 

Un pixel es el elemento más pequeño que compone una imagen digital. Su nombre proviene de una abreviatura de _“Picture Element”_ . Son elementos de tamaño homogéneo, que pueden asimilarse a los distintos puntos de componen una imagen. 

08 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por ejemplo, una imagen de 10 píxeles de ancho por 5 píxeles de alto, y por tanto de un total de 50 píxeles, estará conformada por tres matrices distintas de estos mismos tamaños, para poder generar cada color necesario. Es más sencillo comprobarlo visualmente en la siguiente figura. Estos conceptos serán ampliados a lo largo del módulo, y son esenciales para sentar una base sólida en la comprensión de la visión artificial. 



Representación de una imagen a color como tres matrices RGB 

Los monitores de nuestras pantallas encienden en cada pixel tres LEDs (en el caso de las últimas pantallas basadas en tecnología LED), cada uno con una intensidad determinada, para producir el color deseado. 

Esta intensidad se mide entre dos valores. Si la intensidad tiene el valor más bajo, indica que no hay absolutamente nada de luz de un color. El valor más alto indica que hay la mayor cantidad de luz posible de un color determinado. 

Por el momento, lo más importante es comprender que las imágenes son, en definitiva, números. Y, por tanto, los modelos de visión artificial trabajan con matrices de varias dimensiones – en el caso de las imágenes de RGB trabajan con tres dimensiones, una por cada color – sobre las que efectúan diversas operaciones. 

En definitiva, para una máquina las imágenes no son luz, color y movimiento, como lo son para nosotros, lo seres humanos, y en general para los mamíferos y otros animales. Para una máquina las imágenes son meros conjuntos de números sobre los que operar, para así poder encontrar características numéricas específicas que puedan ayudar a detectar ciertos aspectos de la realidad que estas imágenes representan. Por ejemplo, buscarán numéricamente formas, bordes, colores, brillos, sombras… 

Es por ello que el campo de la visión artificial está íntimamente relacionado con las matemáticas, en concreto con los espacios vectoriales, las transformaciones matemáticas y los tensores, que son objetos matemáticos en espacios vectoriales. No obstante, a lo largo de este módulo trataremos de limitar las expresiones matemáticas al mínimo imprescindible para facilitar el avance en el mismo y mejorar la comprensión de las técnicas que vamos a estudiar. Sin embargo, proporcionaremos libros de referencia en la sección de bibliografía para permitir profundizar en las bases teóricas de las diversas técnicas que vamos a explorar en el campo de la visión artificial. 

09 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **1.1.1. Objetivos de la visión artificial** 

Los problemas de visión artificial suelen poder clasificarse dentro de una serie de objetivos genéricos que componen esta disciplina. Serán estos objetivos los que estudiaremos y desarrollaremos a lo largo de este módulo, por lo que será esencial conocerlos desde el inicio del mismo. La visión artificial procesa imágenes, pero es importante hacer una distinción entre imágenes estáticas e imágenes en movimiento. Si bien es cierto que un video no es más que un conjunto de imágenes concatenadas, los objetivos que se pueden perseguir en el caso estático y en el caso dinámico varían dada la naturaleza de cada uno de estos tipos de archivos (imagen y vídeo). 

#### **Visión artificial estática** 

En el caso de las **imágenes estáticas** nos encontramos habitualmente con problemas que se enmarcan dentro de alguna de las siguientes categorías. Son las categorías más relevantes, aunque es importante tener en cuenta que existen tantas como posibles casos de uso, y que solo cubriremos las que más impacto tienen en la disciplina de la visión artificial en la actualidad. 

- **Clasificación.** La clasificación de objetos, también conocida como reconocimiento de objetos, es el objetivo más sencillo que se puede plantear en un problema de visión artificial. Este tipo de objetivo – y por tanto de algoritmos – trata de decidir qué hay de forma global en una imagen. 

El algoritmo tendrá una serie de clases previamente entrenadas entre las que podrá escoger para proporcionarnos una respuesta. Por ejemplo, un algoritmo de clasificación de marcas de vehículos tendrá previamente entrenadas todas las marcas de vehículo que se desea procesar (por ejemplo: Chevrolet, Ford, Toyota, Volkswagen, Nissan…). Al mostrarle una imagen de un vehículo, el algoritmo reconocerá la clase de vehículo que está observando, es decir, lo clasificará, en este caso en función de su marca. 

La gran limitación de la clasificación de objetos es que los modelos que persiguen este objetivo solo son capaces de procesar la imagen en su conjunto, y por tanto solo son capaces de asociar una única clase a la imagen. Si la imagen es una fotografía de una jirafa, un algoritmo clasificador correctamente entrenado, será perfectamente capaz de devolver la clase “jirafa”. Ahora bien, si en la fotografía salen varios animales, la etiqueta será “animales”. Es decir, no será capaz de diferenciar los distintos animales presentes en la imagen, por lo que la usabilidad de este tipo de modelos está limitada a casos de uso en los que las imágenes solo contengan un tipo de objeto cada vez, o bien en aquellos en los que podamos agrupar objetos en grupos más grandes como es el caso de este ejemplo. En el caso de la siguiente figura podemos observar un modelo de clasificación asignando la tipología de vehículo de cada uno de los siguientes objetos. Como podemos observar, hay **un único objeto** en cada imagen y una única clase de salida. 

10 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Clasificación de modelos de vehículos en base a una imagen de entrada por visión artificial 

• **Localización.** La localización de objetos trata de identificar la ubicación espacial de uno o más objetos en una imagen, sin asociarles una clase, o lo que es lo mismo, sin clasificarlos. Los modelos más básicos de localización son capaces de ubicar un **único objeto** que sea claramente diferenciable del fondo de la imagen, como veremos a lo largo de la unidad 2. No obstante, también existen modelos que localizan **múltiples** objetos en una misma imagen, que serán los que estudiaremos en la tercera unidad de esta asignatura. 

Para poder comunicar el resultado de esta ubicación, los modelos de visión artificial de localización emplean un sistema de coordenadas que para cada objeto localizado devuelve un rectángulo que lo contiene completamente. Este rectángulo recibe el nombre de _Bounding Box_ (caja contenedora). En el caso de la localización, como hemos mencionado, la tipología de los objetos en la imagen no se considera relevante, no se busca clasificar la imagen. Tan solo se trata de ubicar los objetos espacialmente para comprender dónde hay algo que no sea el fondo de una imagen. Podemos entender este objetivo como la búsqueda de todo objeto relevante en una imagen dada, aunque no se comprenda el contenido de dichos elementos relevantes. En la siguiente imagen se puede observar un ejemplo de _Bounding Boxes_ calculadas por un algoritmo de localización sobre una imagen de vehículos circulando por una carretera, en la que se dibuja un rectángulo alrededor de cada uno de ellos de manera autónoma. El modelo comprende que estos son los objetos que están en la imagen y son distintos del fondo de la misma. Sin embargo, carece de información acerca de su tipología, como sí haría un modelo de clasificación, que para esta fotografía nos habría devuelto la clase “vehículos”. 

11 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Representación de _bounding boxes_ localizando objetos en una imagen 

- **Detección.** La detección de objetos es la unión de los objetivos de localización y clasificación, y es uno de los objetivos más importantes en la actualidad del campo de la visión artificial. Un modelo de detección objetos primero ejecutará un proceso de localización para obtener las _Bounding Boxes_ que enmarcan cada objeto de una imagen. Posteriormente, realizará un proceso de clasificación a cada uno de estos rectángulos, para así poder comprender la tipología de cada objeto previamente localizado. Gracias a este proceso, como veremos con gran profundidad en la sección específica de _Object Detection_ en la tercera unidad de esta asignatura, podemos procesar **múltiples objetos de múltiples clases** en la misma imagen sin ninguna limitación al respecto. 

Gracias a ello, la gran mayoría de requisitos de búsqueda y diferenciación de objetos en una imagen pueden ser satisfechos. La gran mayoría de modelos de detección de objetos están basados en arquitecturas de redes neuronales de _deep learning_ , concretamente Redes Neuronales Convolucionales (CNN) como veremos en unidades futuras. Este objetivo es uno de los campos con mayor número de publicaciones anuales dentro de la disciplina de la visión artificial. Esto es debido a su gran flexibilidad y aplicabilidad en prácticamente cualquier tipo de industria en la actualidad. Por ejemplo, con un modelo de visión artificial para la detección de objetos, se puede tratar de comprobar que los trabajadores de una mina portan con ellos en todo momento los equipos de protección individual como máscaras, cascos y chalecos reflectantes, así como podemos tratar de estimar la marca de vehículo que circula en un momento dado por una autopista, como podemos ver en la siguiente imagen. Para poder entrenar este tipo de modelos es necesario previamente etiquetar manualmente las imágenes, es decir, dibujar los rectángulos en torno a los objetos de interés según el caso de uso, e indicar la clase a la que pertenecen. Actualmente hay modelos de IA de detección de objetos capaces de funcionar a tiempo real, es decir, llegan a procesar hasta 120 imágenes por segundo, más de las que tiene un vídeo habitualmente. 

12 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Modelo de detección de objetos ejecutando en orden la localización y posteriormente la clasificación de marcas de vehículos 

- **Segmentación.** Como hemos visto, la detección de objetos permite conocer la ubicación espacial y la tipología de los objetos que se encuentran en una imagen. Esto se hace por medio de la ya mencionada _Bounding Box_ , que no es más que un rectángulo que contiene de la forma más precisa posible cada uno de los objetos detectados. El gran contratiempo de emplear siempre rectángulos para el marcaje de los objetos, es que esto imposibilita obtener información acerca de la forma de los objetos o del espacio real que ocupan. Por ejemplo, si quisiéramos detectar barras de metal y conocer su superficie, podríamos encontrarnos con un gran problema que observamos en la siguiente imagen. Si la barra se encuentra en horizontal o vertical, el rectángulo se aproximará enormemente a su forma y superficie reales, y podremos asumir este dato para resolver nuestro problema. Sin embargo, cuanto más inclinada esté la barra, más diferencia habrá entre el tamaño de la _Bounding Box_ y el tamaño de la barra, lo que haría inviable desarrollar un proyecto en base a la tecnología de detección de objetos. 



Limitación de la tecnología de detección de objetos para el análisis de formas y tamaños 

13 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Para resolver esta limitación, es necesario emplear técnicas que nos permitan conocer con precisión los bordes y formas de los objetos que deseamos procesar. Estas técnicas son denominadas segmentación de objetos. Gracias a la segmentación de objetos, se puede conocer a qué tipología de objeto pertenece **cada pixel** de una imagen, para de esta forma obtener información granularizada a la escala más pequeña disponible en una imagen y poder hacer análisis y mediciones precisas. Veremos que hay dos tipos de segmentación en función del objetivo específico que persigan: la segmentación semántica y la segmentación de instancias. 

- Segmentación semántica. Los modelos de segmentación semántica – o _semantic segmentation_ en inglés – asignan una etiqueta a cada pixel de una imagen, o lo que es lo mismo, clasifican cada uno de los píxeles de la imagen. Si un modelo de clasificación asigna una clase a la imagen completa, un modelo de segmentación semántica hace el mismo proceso a nivel de pixel. De entre una serie de clases conocidas previamente, cada uno de los pixeles de la imagen será etiquetado con una clase para obtener un resultado como el que podemos observar en la siguiente imagen, tomada por la cámara a color de un vehículo autónomo. Como podemos observar, cada pixel de la imagen es segmentado – y colorado para facilitar la comprensión del resultado – con una de las clases que conoce este modelo, para así entender qué tipo de objeto es cada pixel que procesa. 



Segmentación semántica de una calle en siete clases conocidas más una desconocida 

14 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- Segmentación de instancias. La segmentación de instancias trata de resolver el problema principal que presenta la segmentación semántica. Al segmentar semánticamente cada pixel, podemos conocer la composición de una imagen pixel a pixel, pero no obtenemos información de objetos completos. Por ejemplo, en la imagen anterior todos los pixeles rojos son vehículos, pero si quisiéramos saber cuántos vehículos hay o cuánto espacio de aparcamiento ocupa cada uno no seríamos capaces. Esto es porque si bien conocemos a qué clase pertenece cada pixel, no estamos detectando objetos con esta información. Para ubicar objetos gracias a la información proporcionada por un modelo de segmentación semántica, es necesario pasar a un modelo de segmentación de instancias. 

En definitiva, el objetivo principal de un modelo de segmentación de instancias es **detectar objetos individuales** – también denominados instancias – partiendo de una segmentación semántica. Los modelos de segmentación de instancias suelen ser más complejos computacionalmente, pero permiten obtener información notablemente más útil y completa, por lo que tienden a ser los más empleados en la actualidad. En la siguiente imagen podemos observar la diferencia entre un modelo de segmentación semántica y un modelo de segmentación de instancias. 



A la izquierda, resultado de un modelo de segmentación semántica. A la derecha, el resultado de una segmentación de instancias en las que los objetos individuales son identificados. 

15 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- **Reconocimiento de relación entre objetos.** En este objetivo derivado bien de la detección de objetos o de la segmentación de instancias – es decir, de métodos de reconocimiento de múltiples objetos, su clase y su ubicación espacial – los modelos de reconocimiento de relaciones tratan, a partir de un conjunto de objetos y ubicaciones, de inferir la relación existente entre los diversos objetos detectados. Por ejemplo, en una imagen en la que se detectan como objetos a un ser humano, una silla y una guitarra, este tipo de modelos serán capaces de devolver salidas como <”persona”, “sentada”, “silla”> o <”persona”, “toca”, “guitarra”>. Esto aporta una capa más de conocimiento a la hora de procesar automáticamente imágenes y permite conocerlas de forma más similar a como las procesa el cerebro humano, ya que no solo sabremos qué objetos hay, sino cómo interactúan entre ellos en el momento de la captura de la imagen. 

- **Descripción de imágenes.** Un paso más allá de la comprensión de las relaciones entre objetos se encuentra la descripción de imágenes, conocida como _image captioning_ en inglés. Este tipo de objetivo trata de definir una imagen en lenguaje natural pero sencillo, por lo que es una intersección entre las disciplinas de NLP y visión artificial. Para entrenar estos modelos se pide a numerosos sujetos de estudio que definan en una frase corta una gran serie de imágenes de entrenamiento, para tratar de emular el comportamiento de la visión y procesamiento humanos en un sistema inteligente. En definitiva, su capacidad descriptiva ayuda a comprender el contenido de una imagen en aplicaciones para personas con problemas de visión, así como para etiquetar automáticamente contenido multimedia en grandes corporaciones. En la siguiente figura se puede observar un modelo de _imagen captioning_ en funcionamiento. 



Resultados arrojados por un modelo de _image captioning_ en un set de tres imágenes distintas 

16 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- **Restauración de imágenes.** Los objetivos de restauración de imágenes tratan de mejorar automáticamente la calidad de una imagen dada con ruido, baja calidad o inciso corrupta. Trata de contrarrestar afectos negativos de la resolución del dispositivo de captura, aberraciones debidas a las lentes, ruidos en el sensor, desenfoque, fogonazos, exposición elevada, desenfoque por movimiento… Todo ello de forma automatizada. Existen desde modelos sencillos que aplican filtros de ruido y distorsión, hasta complejos modelos de _deep learning_ capaces de comprender los objetos y la disposición de una fotografía para mejorar su resolución, aspecto y enfoque con precisiones sorprendentes. Un ejemplo de este tipo de objetivos es el subobjetivo conocido como _inpainting_ . Esta técnica consiste en rellenar zonas de fotografías deterioradas de forma automática, por ejemplo, para eliminar censura mediante una inferencia del contenido censurado, o generar el contenido que falta en una fotografía por un deterioro físico de la misma. Esto implica que los modelos de visión artificial traten de estimar qué debería haber en un hueco en una imagen para permitir rellenarlas de forma que no resulte incoherente para un ser humano que la observe. 

Numerosos modelos de redes neuronales tratan de realizar este tipo de tareas con diversos grados de éxito basándose en el contexto que son capaces de extraer de las imágenes que se proporcionan como entrada. Este tipo de tareas están íntimamente relacionadas con el siguiente objetivo de la visión artificial, la generación automática de contenido, principalmente mediante redes Adversarias Generativas (GANs). En la siguiente imagen se puede observar el funcionamiento de uno de estos modelos, que, partiendo de una imagen ampliamente deteriorada, tratan de completar una imagen no corrupta en base al contexto disponible. 



En la imagen de la izquierda, una serie de pixeles están corruptos, denominados “agujeros”. Los pixeles correctos sirven de ground truth al modelo, que trata de inferir el contenido de los “agujeros” para de esta forma completar la imagen de la forma más realista posible 

17 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

#### • **Generación de contenido** 

Este objetivo, que ya comentamos en el primer módulo de Introducción a la Inteligencia Artificial, tanto en el campo del procesamiento del lenguaje natural como en el de la visión artificial. En este módulo, como no puede ser de otra manera, nos centraremos en la generación de contenido visual. Los modelos de generación de contenido pertenecen mayoritariamente a dos clases denominadas _“Variational Autoencoders (VAE)” y las “Generative Adversarial Networks” (GAN)”_ , siendo estas últimas las más precisas y por tanto las más empleadas en la actualidad. Se emplean tanto para generar caras humanas que no existen como para crear obras de arte, tal y como vimos en el primer módulo de este máster. Se emplean también para aumentar la muestra disponible para entrenar modelos de cualquier otro tipo en el ámbito de la visión artificial. 

Por ejemplo, si necesitamos entrenar una red neuronal para detectar señales de tráfico, necesitaríamos miles de imágenes que contengan estas. Para aumentar esta muestra de entrenamiento, podríamos emplear una GAN para generar imágenes sintéticas de carreteras con señales de tráfico, y así poder usarlas para entrenar nuestro detector de objetos centrado en señales. 

Con todos estos objetivos mencionados hasta el momento, hemos cubierto la gran mayoría de los que se aplican en la actualidad a imágenes estáticas. Desde clasificarlas hasta segmentarlas pasando por comprender su contenido o incluso crearlas desde cero o restaurarlas. Por supuesto, hay otros muchos objetivos de visión artificial que pueden aplicarse a imágenes estáticas, aunque habitualmente pueden ser enmarcados en alguno de los que hemos visto hasta ahora. El reconocimiento de caracteres y texto en imágenes, la detección de la pose humana, y la estimación de espacios tridimensionales a partir de imágenes a color son tan solo ejemplos de otros objetivos que podrían mencionarse en esta sección, pero que realmente podrían ser incluidos en cualquiera de los anteriores. En cada sector y en cada caso de uso es necesario definir un objetivo mucho más concreto que estos que estamos estudiando. Sin embargo, conocer las grandes categorías de objetivos será lo que nos ayudará a entender el problema, a buscar posibles algoritmos que lo solucionen y a afinar las arquitecturas entrenadas todo lo que sea necesario posteriormente. 

Estos objetivos presentados son los que, habitualmente, se trabajan desde el mundo de la investigación de visión artificial, pero también en los que las empresas dedicadas a esta disciplina dividen sus tecnologías y proyectos. En muchos proyectos encontraremos que es necesario aplicar varios de estos tipos de modelos, por ejemplo, podríamos necesitar primero restaurar una imagen y ampliar su resolución para posteriormente segmentarla en instancias, o detectar objetos en la misma. En las siguientes unidades profundizaremos en las distintas técnicas que pueden aplicarse para la consecución de cada uno de estos objetivos, desde técnicas clásicas hasta los últimos descubrimientos basados en _deep learning_ . 

18 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

#### **Visión artificial dinámica** 

Tal y como ya hemos visto, hay múltiples operaciones y transformaciones que pueden aplicarse sobre imágenes estáticas. El siguiente paso es tratar de aplicar la visión artificial a imágenes en movimiento, es decir, a vídeos. Un video digital no es más que un conjunto de imágenes almacenadas en una lista de forma ordenada, denominadas fotogramas. Las cámaras de video capturan una imagen cada X segundos, lo que se denomina el _framerate_ . Este _framerate_ , expresado en _frames per second (fps)_ indica la cantidad de fotogramas que han sido capturados en el lapso de un segundo. 

Por tanto, la primera intuición que tendremos es que es posible aplicar cualquiera de los objetivos mencionados hasta el momento (visión artificial estática) a cada uno de los fotogramas de un video y así podremos procesar un video con visión artificial. Esto es totalmente cierto y acertado. Si a cada _frame_ de un video le aplicamos un modelo de detección de objetos, o de segmentación de instancias, podremos conocer dónde se ubicaba cada objeto en cada momento del vídeo, así como su tipología. 

Sin embargo, tratar un video únicamente como fotogramas aislados concatenados implica perder una de las características más importantes de un video, así como de la visión humana; el movimiento. Gracias a la percepción del movimiento somos capaces de orientarnos espacialmente y percibir un mundo tridimensional más preciso que si fuera estático. También podemos realizar un seguimiento visual de objetos, calculando trayectorias y trazadas con gran precisión, así como inferir la ubicación de objetos que salen de plano, pero se han podido percibir durante algunos momentos. Todos estos objetivos pertenecen a la conocida como “visión artificial dinámica” en contraposición con el procesamiento estático de imágenes fijas. 

- **Análisis del movimiento.** El análisis de movimiento – denominado en inglés _“Motion Analysis”_ , es una tarea que los seres humanos realizamos todos los días sin ser conscientes de ello. Nuestra fisiología humana ha evolucionado desde nuestros ancestros hasta dotarnos de la gran capacidad de percepción y análisis del movimiento que tenemos en la actualidad. Las técnicas de análisis de movimiento forman parte de la visión artificial dinámica, y permiten a las máquinas detectar el movimiento, comprenderlo y analizarlo para así tener la posibilidad de estimar mapas de profundidad, reconocer determinadas acciones humanas relativas al movimiento, comprender los eventos que suceden en un video, mejorar la calidad de la compresión y digitalización de un video y realizar cálculos de espacios y velocidades de diversos objetos en un vídeo. 

19 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Existen numerosas técnicas de análisis de movimiento como son el flujo óptico, el análisis de diferencia de imágenes, la sustracción de fondo y los métodos de salto. Todas ellas persiguen detectar el movimiento que se da en una secuencia de frames, analizarlo y comprenderlo. Una gran mayoría de estos modelos se aplican al análisis y reconocimiento de acciones humanas, como puede ser detectar los movimientos que realiza un tenista durante el saque, para tratar de evaluar su riesgo de lesión. En este caso, sería necesario primero detectar al tenista, y posteriormente analizar el movimiento de sus extremidades y las posiciones de las mismas para estimar si su saque es correcto. Se emplean en numerosas industrias como la seguridad vial, la industria de protección balística, la biología, y el estudio de las mareas y el avance de incendios forestales entre otros muchos ejemplos. En la siguiente imagen podemos observar un modelo de análisis del movimiento centrado en el reconocimiento de acciones deportivas durante un partido de voleibol. El modelo procesa todos los _frames_ de un vídeo, y trata de estimar en cada uno de ellos la acción que está realizando cada jugadora. 



Modelo de análisis de movimiento para la detección de actitudes deportivas en voleibol 

- **Seguimiento de objetos.** Una de las características esenciales de la visión humana es movimiento es la noción del tiempo y la continuidad. Los objetos se mueven siguiendo una trayectoria continua, y esto es algo que nuestro cerero comprende en base a su experiencia. Esta capacidad de seguimiento es parte de la disciplina del análisis del movimiento, pero requiere una explicación dedicada. Hasta ahora hemos visto cómo detectar objetos, bien sea por medio de _bounding boxes_ o de métodos de segmentación. Sin embargo, no hemos mencionado ningún modelo capaz de comprender que un objeto que aparece en un determinado _frame_ es el mismo objeto que aparece en el siguiente _frame_ ligeramente desplazado, ya que se está moviendo. Para poder realizar esta tarea, es necesario desarrollar modelos de seguimiento de objetos, denominados en inglés _trackers_ ya que siguen objetos ( _object tracking_ ). 

20 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

La gran mayoría de modelos de seguimiento de objetos tienen la misma estructura. Primero, se busca en cada _frame_ la ubicación de cada objeto, habitualmente mediante un algoritmo de detección de objetos. Con esto, conseguimos una serie de rectángulos en torno a cada uno de ellos ( _bounding box_ ). Para ser capaces de comprender hacia donde se mueve cada uno de estos rectángulos, o si bien pertenecen estáticos, es necesario emplear un algoritmo de seguimiento. Los dos algoritmos de seguimiento más empleados son el Algoritmo Húngaro, y el Filtro de Kalman, que veremos más adelante. Estos algoritmos nos ayudan a comprender qué objetos corresponden con qué objetos a lo largo del vídeo, y sus posiciones más probables en el futuro. Generalmente, se emplean para multitud de casos de uso, como monitorización del tráfico, desplazamientos robóticos, vehículos autónomos y aplicaciones relacionadas con la salud y la imagen médica. 

En la siguiente tabla trataremos de resumir todos los objetivos de visión estática y dinámica a modo de tabla de referencia para poder acudir a ella en cualquier momento. 

||**VISIÓN ESTÁTICA**|
|---|---|
|**Objetivo**|Descripción|
|**Clasificación de**<br>**objetos**|Dada una imagen, se trata de categorizarla en una clase<br>predefinida. Se procesa una clase por imagen, y no se localiza el<br>objeto.|
|**Localización de objetos**|Además de clasificar la imagen, se busca la ubicación del objeto<br>principal.|
|**Detección de objetos**|Se trata de localizar espacialmente y clasificar todos los objetos de<br>una imagen en una o múltiples clases.|
|**Segmentación de**<br>**objetos**|Se realiza una clasificación a nivel de píxel de las imágenes. Los<br>objetos quedan totalmente delimitados.|
|**Relación entre objetos**|Una vez detectados los objetos, se trata de comprender las<br>relaciones y acciones que hay entre ellos.|
|**Descripción de**<br>**imágenes**|Se persigue dar una breve descripción de una imagen con tan solo<br>procesarla por el algoritmo.|
|**Restauración de**<br>**imágenes**|Dada una imagen en mal estado, con espacios vacíos o<br>deformados, se trata de recuperar en la medida de lo posible la<br>imagen original con la máxima resolución posible.|
|**Generación de**<br>**contenido**|Dada una imagen o una frase de “inspiración”, estos modelos<br>generan imágenes nuevas del tema que se les haya proporcionado.|



21 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

||**VISIÓN DINÁMICA**|
|---|---|
|**Objetivo**|Descripción|
|**Análisis de movimiento**|Detectar, analizar y comprender el movimiento que existe en un<br>archivo de video (una sucesión de imágenes)|
|**Seguimiento de**<br>**objetos**|Dado un objeto detectado, seguir su trayectoria a lo largo de un<br>video, así como poder predecir el lugar hacia el que se dirige.|



### **1.2. Métodos y procesos** 

Encontraremos a lo largo de este módulo dos tipos principales de métodos de visión artificial, dependiendo de la tecnología subyacente que empleen. Estos serán los métodos clásicos, y los métodos basados en aprendizaje profundo o _deep learning._ 

_Los métodos clásicos, denominados en inglés “traditional computer vision techniques”, emplean de forma dirigida la información numérica de los píxeles de una imagen para tratar de encontrar características relevantes en la imagen, denominadas “features”._ 

Estas _features_ pueden ser extraídas por diversos métodos como detección de bordes, detección de líneas, de esquinas, de objetos concretos, de cambios de contraste… La característica principal de estos métodos es que **sabemos las operaciones que realizamos sobre los píxeles y las características que buscamos.** Cuando busquemos bordes, por ejemplo, podremos buscar diferencias entre un pixel y el contiguo de más de un determinado porcentaje. Controlamos todos los factores que afectan a nuestro algoritmo, para bien o para mal. Es por esto que con pocas imágenes de ejemplo podemos desarrollar un algoritmo clásico completo. 

La decisión tanto de qué características se desea extraer, como de los métodos que se emplean para hacerlo, provienen íntegramente del diseñador. Si bien cuantas más imágenes usemos para diseñar el sistema, mejores ejemplos tendremos para desarrollar la estrategia de búsqueda de _features_ , con tan solo conocer la casuística general se puede implementar uno de estos algoritmos de visión artificial. Esta es una gran ventaja en proyectos en los que la recolección de imágenes es compleja. 

22 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por otro lado, esta es una de sus mayores debilidades. Si el conjunto de las operaciones y _features_ a extraer proviene de una decisión del diseñador, si esta decisión no es la más correcta, el algoritmo será subóptimo. Por ejemplo, para detectar una cara humana podremos buscar cejas en forma de bordes o de líneas, ojos en forma de círculos o de zonas oscuras, y calcular o no la relación de distancia entre ambos elementos. Tomando estas decisiones estamos incurriendo en un coste de oportunidad al no buscar otras _features_ o emplear otros métodos de extracción que quizá podrían ser mejores para nuestro problema concreto. 

La opción para resolver esta gran desventaja es optar por los modelos de _deep learning_ basados en redes neuronales que comenzaron su auge en 2012, como vimos en el primer módulo de este máster. 

_Los modelos de visión artificial de deep learning están basados en redes neuronales y aprenden automáticamente a solventar los objetivos deseados por medio del proceso de entrenamiento. El diseñador desarrolla la estructura de la red neuronal, pero las operaciones a nivel pixel son decididas por el propio algoritmo de forma autónoma._ 

Los modelos de redes neuronales constan de una serie de operaciones genéricas que veremos más adelante, realizadas por neuronas artificiales. Sin embargo, la forma de realizar estas operaciones se decide internamente en la red neuronal mediante el proceso de entrenamiento, gracias a algoritmos de aprendizaje automático como el algoritmo de _backpropagation_ , que ya conocemos. En este caso, la decisión final de las operaciones a realizar no es por tanto del diseñador del sistema inteligente, sino del algoritmo de aprendizaje. Para que este algoritmo obtenga resultados sólidos y que aporten flexibilidad y robustez al modelo final, es necesario contar con una gran cantidad de datos etiquetados, lo que en ocasiones supone una restricción importante en los proyectos de visión artificial. El gran beneficio que aportan estos sistemas es la liberación del diseñador de seleccionar manualmente las características que se deben extraer, así como la forma de hacerlo. Una red neuronal solo necesita comprender qué tarea debe realizar, y decidirá por su cuenta las regiones y características de las imágenes que debe procesar para alcanzar sus objetivos. 

23 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Para comprender mejor la diferencia entre ambos tipos de método podemos recurrir a un ejemplo. Imaginemos que queremos reconocer distintas especies de plantas. El algoritmo recibirá una imagen de una planta tomada por cualquier usuario desde cualquier dispositivo y deberá devolver la especie a la que esta pertenece. 

Si optáramos por un método clásico, deberíamos identificar manualmente las características que diferencian cada especie de planta. Quizá es la forma del borde de las hojas, el color de las mismas, su textura, la forma y color de las flores y los frutos… Para cada característica identificada deberemos encontrar un método clásico de visión artificial que nos permita extraerla. Buscaremos bordes, formas concretas, colores… Cada operación estará seleccionada por el desarrollador y podrá proporcionar resultados más o menos buenos. Por ejemplo, podemos emplear una técnica de búsqueda de contornos y aplicar una máscara – veremos todos estos métodos más adelante – para obtener la forma perfecta de la hoja. En blanco tendríamos la hoja y en negro el fondo. 



Una vez seleccionada la característica, en este caso la forma de la hoja, es necesario clasificarla. Para hacerlo podemos aplicar un algoritmo de SVM que nos permita clasificar estos contornos – de nuevo veremos este algoritmo a lo largo del módulo – lo que puede resultar en todo un éxito, o todo un fracaso. 

Como podemos comprobar, las decisiones que toma el diseñador en un proyecto basado en métodos clásicos dependen enormemente de la selección de los algoritmos que se realice, así como de las características que se desea procesar de las imágenes de entrada. 

En el lado contrario, podemos optar por un modelo de _Deep Learning_ para clasificación de objetos. Generalmente se emplean Redes Neuronales Convolucionales (CNN) para este tipo de objetivos. En este caso, el paso más crítico sería recolectar una gran cantidad de imágenes de hojas de plantas etiquetadas con la especie de cada una para poder alimentar el entrenamiento de la red neuronal con suficientes imágenes. 

24 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Una vez se le proporcionan suficientes imágenes etiquetadas de cada especie de planta, será capaz de realizar esta tarea. El programador no habrá tenido que seleccionar las características ni los métodos de extracción de las mismas, sencillamente habrá seleccionado una arquitectura de clasificación de objetos de entre todas las existentes. Una vez tomada esta decisión, la gran mayoría del trabajo será realizado por la red neuronal, aunque habrá posibilidad de facilitar el mismo como veremos en futuras unidades. 

Para diseñar, desarrollar y finalmente obtener satisfactoriamente un sistema de visión artificial, independientemente del método que escojamos, es necesario conocer sus dos fases más importantes, así como los procesos que, de forma general, se ejecutan en la disciplina de la visión artificial. 

A grandes rasgos, hay dos fases por las que es necesario pasar. Por una parte, deberemos obtener el algoritmo o los algoritmos que nos permitan obtener el sistema inteligente deseado. En esta primera fase lo esencial será obtener tantas imágenes como sea posible para desarrollar y poner a prueba el sistema; y conocer las técnicas más relevantes de visión artificial para seleccionar de entre todas ellas la más adecuada. Esta es la fase del **diseño y desarrollo del sistema** . Esta es la fase en la que decidimos qué aspecto va a tener el sistema inteligente, y lo entrenamos para aprender a cumplir su objetivo. Es importante recalcar que **no todos los sistemas de visión artificial son sistemas de aprendizaje automático** . Como veremos, encontraremos en esta disciplina tanto algoritmos clásicos como sistemas punteros de aprendizaje profundo, y ambas tecnologías conviven en la actualidad, cada una de ellas aplicada a casos de uso distintos. 

Después de desarrollar el sistema, es necesario implantarlo. Esto quiere decir desplegar este sistema para que se enfrente al objetivo para el que fue diseñado en el mundo real. En el mundo del desarrollo de software esta fase se denomina informalmente “pasar a producción”. En términos más correctos, podríamos hablar de una fase de **implantación del sistema** . Podríamos decir que es la manera en la que el sistema funciona definitivamente. 

### **1.2.1. Fase 1. Diseño y desarrollo** 

Es esta primera fase trataremos de obtener todos los datos necesarios para comenzar a trabajar, elegiremos los algoritmos a emplear, los entrenaremos y posteriormente los evaluaremos. 

1. Análisis y comprensión del problema. 

El primer paso de todo sistema inteligente es conocer y comprender el problema que debe resolverse y sus objetivos. Esto es común a todos los sistemas inteligentes y no es específico de la visión artificial, por lo que será desarrollado en otros módulos. En el caso de la visión artificial, lo primero será comprender el tipo de problema al que nos enfrentamos, dentro de los que conocemos. 

25 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Puede tratarse de un problema de clasificación de objetos, de detección, de segmentación, de reconocimiento de texto, de visión 3D, de reconocimiento facial, de análisis de bordes, de seguimiento… Iremos conociendo todos estos objetivos a lo largo del módulo. Una vez comprendido el tipo de problema de visión al que nos enfrentamos, es imprescindible recopilar todos los datos que podamos acerca del mismo, para mejorar si cabe nuestra comprensión del mismo, y comenzar a construir una base de datos de la que nuestro futuro sistema pueda aprender eventualmente. 

#### 2. Recolección y anotación de datos. 

Tanto si optamos finalmente por algoritmos clásicos o por aprendizaje profundo, será necesario hacerse con todos los datos posibles para la preparación de los algoritmos. En el caso de la visión artificial estos datos serán distintas variaciones de imágenes. Imágenes y vídeos capturados con diversos dispositivos, desde cámaras digitales a color, hasta dispositivos complejos de _machine visión_ – que veremos más adelante – como microscopios, cámaras hiperespectrales o cámaras estereoscópicas. Sea como sea, el primer paso será **recopilar una muestra** compuesta por una serie de fotogramas que contendrán el problema al que nos enfrentamos. Serán imágenes de caras humanas, vídeos de una calle de una ciudad, imágenes láser de productos manufacturados en una industria determinada, o imágenes en tres dimensiones de grandes espacios abiertos. 

El número de imágenes a recolectar dependerá de los algoritmos que finalmente decidamos emplear. Las técnicas clásicas requieren una cantidad notablemente menor de imágenes de muestra que los algoritmos de aprendizaje profundo, lo que implica una gran ventaja en situaciones en las que es complejo obtener grandes cantidades de datos. Por otro lado, los algoritmos de aprendizaje profundo tienden a ser más robustos y flexibles, pero requieren de grandes cantidades de datos para lograr un funcionamiento adecuado. Por norma general, cuantos más datos logremos capturar, más preciso será nuestro sistema. Esto es porque seremos capaces de capturar todas las posibles variaciones del problema al que nos enfrentamos. 

Una vez los datos han sido capturados y están almacenados en algún tipo de soporte, llega el momento de la **anotación o etiquetado** de los datos. Lo más probable es que las imágenes que hemos recolectado sean sencillamente imágenes. Para poder pasar a la siguiente fase del diseño y desarrollo de un sistema de visión artificial es imprescindible dotar a estas imágenes de información añadida. Estas etiquetas serán diversas en función del problema al que nos enfrentemos. En algunas ocasiones serán puntos importantes de la imagen, en otras solo la clase a la que pertenecen. Pero este proceso manual de etiquetado de imágenes es esencial para posteriormente poder traspasar todo este conocimiento a nuestro sistema inteligente en ciernes. 

26 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

3. Análisis del estado del arte y selección de algoritmo(s) 

Cuando ya hemos analizado el problema, comprendido su tipología y capturado y anotado datos al respecto, nos encontramos en el punto en el que tenemos toda la información requerida para poder seleccionar el tipo de algoritmo para resolver nuestro reto. 

Por supuesto, el tipo de objetivo será el **primer filtro** . En problemas de clasificación solo contemplaremos clasificadores; y en problemas de reconocimiento de texto solamente algoritmos centrados en esta tarea. 

El **segundo filtro** pasa por el número de datos que hemos conseguido capturar. Como ya hemos comentado, si el número de observaciones solo llega a las decenas, el único camino al que podremos optar es el de los métodos clásicos, más centrados en el análisis numérico. Por el contrario, si contamos con grandes cantidades de datos quizá podamos beneficiarnos de las ventajas que ofrecen los modelos basados en redes neuronales como parte del _Deep Learning_ . 

El **tercer filtro** pasa por un análisis del estado del arte actual. ¿Alguien ha tratado de resolver este problema previamente en algún artículo científico? ¿Podemos encontrar problemas similares al que nos ocupa en la literatura científica? ¿Hay modelos genéricos con buenos resultados independientemente del caso de uso? Para resolver estas cuestiones es imprescindible conocer los algoritmos más importantes dentro de cada objetivo de esta disciplina, y por tanto este será uno de nuestros objetivos en este módulo del máster. 

Por lo general encontraremos una serie de algoritmos candidatos tras esta búsqueda, bien sea fruto de la experiencia pasada o de un análisis pormenorizado del estado del arte. De cualquier forma, deberemos seleccionar el mejor candidato o los mejores candidatos para implementarlos y ponerlos a prueba en las siguientes fases de nuestro proceso de diseño y desarrollo. Este proceso es habitualmente desarrollado por el departamento de I+D (investigación y desarrollo) en caso de enfrentarse a problemas no trabajados previamente, o por el departamento de desarrollo de software en caso de ser un problema previamente acometido. 

4. Implementación o entrenamiento 

Las tres fases anteriores han logrado que comprendamos el problema y su tipología, que recopilemos todos los datos anotados posibles y que decidamos qué algoritmo o algoritmos serán los candidatos a resolver el reto ante el que nos encontramos y por tanto a ser el núcleo del sistema inteligente que nos hemos planteado desarrollar. En este punto, es el momento de desarrollar nuestros algoritmos y tratar de que obtengan conocimiento. 

27 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por lo general, nunca partiremos desde el principio, sino que emplearemos diversas librerías de visión artificial que iremos explorando en las siguientes unidades, como OpenCV o Tensorflow. En base a estas librerías, se construirá el código requerido para el funcionamiento completo del algoritmo. Este proceso será desarrollado habitualmente por los departamentos de desarrollo del software. En el caso de técnicas clásicas este proceso será un ejercicio de programación en el que construyamos el flujo necesario para aplicar cada algoritmo seleccionado. 

En el caso de los métodos de aprendizaje profundo la implementación es solo el primer paso. Una vez construido el código requerido para que el algoritmo funcione, este algoritmo debe entrenarse. Como ya hemos visto en módulos anteriores, el proceso de entrenamiento de un algoritmo de aprendizaje profundo implica pasar por los datos que hemos recolectado previamente un gran número de veces, hasta que la red neuronal aprende a generalizar la información que estos contienen y, con suerte, a resolver el problema de forma autónoma. 

Tanto si solo necesitamos desarrollar un método compuesto de algoritmos clásicos como si debemos entrenar una red neuronal, esta fase finaliza cuando obtenemos un modelo informático que es, a priori, capaz de procesar datos visuales de entrada y generar de salida la información necesaria para resolver nuestro caso de uso. 

#### 5. Evaluación y _fine tuning_ 

Tal y como hemos analizado en módulos previos, nunca usaremos la totalidad de los datos recolectados en la muestra para el proceso de implementación y entrenamiento. Esto es por un motivo sencillo. Si empleamos el 100% de los datos para programar nuestro algoritmo de visión artificial, no tendremos ningún dato para poner a prueba al algoritmo que no haya visto antes. De esta forma, podríamos estar manipulando de forma no deseada nuestras métricas de precisión, porque el algoritmo obtendrá grandes resultados si empleamos las mismas imágenes que usó para aprender, para evaluarle. Es por esto que habitualmente se realiza una separación de un 70% de imágenes para entrenar los algoritmos y un 30% para evaluarlos, aproximadamente. Estos porcentajes dependerán del número de datos con el que contemos y de la facilidad con la que podamos obtener más, pero sirven como referencia. 

Este conjunto de entrenamiento también deberá estar etiquetado, ya que será contra estas etiquetas contra las que evaluaremos a nuestros algoritmos. 

Durante el proceso de evaluación, compararemos los resultados arrojados por nuestros modelos contra los resultados esperados en base a nuestras etiquetas manuales. Gracias a este proceso, podremos obtener métricas de precisión para comprender dónde falla nuestro modelo más a menudo. 

28 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Sabiendo esto, podemos ejecutar entonces un proceso conocido como _fine tuning_ o ajuste fino, en el que nos centramos en reentrenar nuestro modelo para evitar estos fallos detectados durante el proceso de evaluación. 

Llegados a este punto, tenemos un modelo completo y listo para su despliegue. Desde el análisis del problema, pasando por la recolección y anotación de los datos, la selección de algoritmos potenciales, hasta su entrenamiento, evaluación y _fine tuning_ , hemos pasado por una serie de fases consecutivas que nos han permitido obtener de forma procedimental un sistema que resuelve el problema que nos plantea un cliente. El siguiente paso será decidir en qué condiciones lo desplegaremos, y qué flujo será necesario para su ejecución en producción. El modelo por sí mismo no funciona, y es preciso integrarlo con el resto de sistemas de captación y reporte de la información para que comience a formar parte de los procesos de nuestro cliente de forma transparente. 

Para comprender mejor las fases que hemos analizado en esta sección, se plantea el siguiente ejemplo de proyecto de forma que podamos observar de forma práctica la aplicación de todas ellas en un caso real. 

Supongamos que un zoológico con una sección de acuario desea crear una aplicación para que sus usuarios puedan grabar con la cámara de sus móviles el interior de los tanques de animales, y la aplicación indique las especies que se están observando en tiempo real. 

Para **comprender el problema** deberemos plantear los siguientes puntos. El número total de especies que se desea detectar, la iluminación tanto de los pasillos como de los tanques de agua, los posibles brillos que pueda generar el cristal, las diversas calidades de las cámaras de cada dispositivo móvil y la posibilidad de conexión de internet en el interior del zoológico, por ejemplo. Dado que en cada fotograma de vídeo encontraremos más de una tipología de animal marino, nos encontramos ante un problema de visión artificial denominado **detección de objetos.** 

Una vez comprendido el problema, deberemos comenzar a recolectar datos. O bien nuestro cliente (el zoológico), o bien sus clientes a cambio de algún tipo de recompensa, o bien nosotros, deberemos grabar tantos vídeos como sea posible para la fase de **recolección de datos** . Estos vídeos deberán ser tan variados como sea posible, para capturar todas las posibles variaciones de luz, dispositivo móvil, tipo de grabación… 

Una vez recolectados los datos, expertos biólogos marinos de nuestro cliente deberán **anotar** los vídeos. Dado que nos encontramos ante un problema de detección, estas etiquetas consistirán en diversos rectángulos – denominados _bounding boxes_ – en torno a cada animal, en cada fotograma, indicando la especie a la que pertenece. Tendría un aspecto similar a la siguiente imagen. 

29 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



##### Ejemplo de etiquetas para la detección de peces y sus especies 

Tras etiquetar todos los fotogramas de todos los vídeos capturados, deberemos realizar una **búsqueda acerca de los algoritmos** más empleados en tareas de detección de objetos, y en concreto analizar si alguno de ellos ha sido empleado para la detección de animales marinos. 

Encontraremos que uno de los artículos más recientes relativos a este problema fue publicado en mayo de 2020 y se llama _“Temperate Fish Detection and Classification: a Deep Learning based Approach”._ En él, sus autores plantean un método de visión artificial para la detección de animales marinos basado en el conocido algoritmo de detección de objetos YOLO unida a un clasificador del tipo Squeeze-and-Excitation (SE). Los resultados parecen prometedores, así que decidimos implementar esta solución 

Pasaremos, por tanto, a la fase de **implementación y entrenamiento** en la que, gracias a los datos recolectados previamente, entrenaremos estos dos algoritmos para que trabajen de manera conjunta analizando peces y sus especies. 

Tras este entrenamiento, emplearemos el conjunto de evaluación para auditar el comportamiento de nuestro nuevo algoritmo y, en caso de ser necesario, realizar pequeños ajustes de **_fine tuning_** para obtener definitivamente el mejor modelo posible. 

Cuando tengamos nuestro algoritmo listo, el último paso será desplegarlo en producción. Esto quiere decir, en esencia, ponerlo a funcionar en un entorno real para el que nuestro cliente nos haya solicitado este proyecto. En caso de que en la puesta en producción de nuestro algoritmo la precisión no fuera la misma que hemos medido en el proceso de evaluación – algo que suele suceder – deberemos volver a realizar un proceso de evaluación y _fine tuning_ tantas veces como sea necesario. De esta forma, los modelos podrán ser cada vez mejores, aprendiendo de la experiencia y sacando el máximo posible de la muestra que se genera en su uso habitual. 

30 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **1.2.2. Fase 2. Implantación del sistema. Despliegue** 

Una vez entrenado, evaluado y ajustado nuestro modelo, es el momento de integrarlo en un flujo de arquitectura que marque el flujo más adecuado para nuestro sistema. 

Habitualmente, todos los sistemas de visión artificial comparten una serie de procesos consecutivos en su implantación y ejecución en producción. Vamos a proceder a listarlos y conocerlos. 

#### **Adquisición de imágenes** 

Los sistemas de visión artificial necesitan imágenes como entrada, como es natural. Estas imágenes pueden provenir de dos fuentes principales 

- a. Imágenes previamente capturadas. En este caso nuestro sistema recibe imágenes capturadas por otros sistemas, por lo que no tenemos control sobre su captura. Estas imágenes pueden venir en una gran variedad de formatos – que veremos más adelante – e incluso estar incrustadas en archivos de presentaciones, texto, PDF, o ser archivos de video en los que se encuentran ordenadas en forma de fotogramas. 

- b. Imágenes capturadas como parte del flujo del sistema. En este caso, la captura de las imágenes está implementado en nuestro sistema. Tendremos control total sobre el dispositivo de captura, la iluminación, el contraste, y la tipología de archivo a capturar. Como veremos en unidades posteriores, hay más opciones de captura además de las cámaras a color, como algunas que se mencionaron en el curso de introducción tales como las cámaras estereoscópicas o las cámaras hiperespectrales. 

Mediante cualquiera de estas dos vías, el resultado final será que nuestro sistema recibe una o varias imágenes que debe procesar mediante los siguientes procedimientos en el flujo. 

#### **Preprocesado de imágenes** 

En muchas ocasiones las imágenes que capturemos no serán directamente empleables por nuestro sistema. Es posible que tengamos que realizar algunos ajustes de preprocesado para asegurarnos los mejores resultados y tiempos de cómputo, como pueden ser, entre otros: 

- Ajustes de brillo, color, nitidez y contraste 

- Disminución de la resolución o selección de regiones de interés dentro de la imagen (ROIs) 

- Cambios de espacios de color (RGB a HSV, YCrCb, CIELAB…) 

- Binarización de la imagen: Convertir la imagen a blanco y negro 

31 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- Suavizados y operaciones morfológicas ( _open, close, erode, dilate…_ ) 

- Normalización de la imagen 

- Balance de blancos automático, negativización, ajustes de gamma 

- Un largo etcétera 

Veremos todos estos procesos en detalle a lo largo del módulo. Por ahora es importante diferenciar esta fase previa de preprocesado que nos permitirá ajustar diferentes parámetros de las imágenes capturadas para encontrar unas características óptimas que permitan a nuestros algoritmos realizar el mejor desempeño posible. 

#### **Extracción de características** 

Una vez nuestras imágenes están listas para ser procesadas, aplicaremos algoritmos de visión artificial para extraer las características más determinantes de nuestra imagen. En caso de que apliquemos técnicas clásicas de visión artificial, todas las funciones empleadas para la extracción de características – que estudiaremos en la siguiente unidad – serán seleccionadas y ejecutadas por el ingeniero de visión artificial. En caso de emplear métodos basados en aprendizaje profundo o _deep learning_ , será la propia red neuronal la que ejecute esta extracción de características, aprendiendo a hacerlo mediante un proceso de entrenamiento que también veremos en la tercera unidad. 

De forma más o menos automatizada, el resultado será detectar líneas, formas, bordes, colores, texturas o brillos, que puedan ayudarnos a encontrar aquellos elementos que estamos buscando tal y como lo deseamos. Estos elementos básicos, también llamados características – o **_features_** en inglés – son los que permiten a los algoritmos de más alto nivel encontrar objetos complejos. A fin y al cabo, una cara humana es un conjunto de bordes, colores y sombras que componen espacialmente las cejas, los ojos, la nariz y la boca. 

La fase de extracción de características encontrará los elementos de bajo nivel (líneas, bordes, etc.) que permitan posteriormente analizarlas a un nivel más alto y clasificar, encontrar o segmentar los objetos que deseamos extraer. 

#### **Aplicación del objetivo** 

Con las características visuales esenciales capturadas en las imágenes, es el momento de ejecutar el objetivo que tenga nuestro algoritmo principal. Este, como ya hemos estudiado, puede ser de clasificación de objetos, de detección de objetos, de segmentación, reconocimiento de escenas… Cada uno de estos objetivos tiene sus propios algoritmos tanto en la vertiente clásica como en las redes neuronales, los cuales estudiaremos en la tercera unidad. Por ahora lo importante es recordar que la aplicación de objetivos siempre parte en todo momento de una imagen capturada, preprocesada y con características extraídas para poder aplicar cualquiera que fuera el objetivo marcado. 

32 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

#### **Toma de decisión y reporte** 

Por último, con nuestro objetivo cumplido, podremos pasar a emplear la información extraída para integrarnos en el proceso de negocio en el que se ha requerido el desarrollo y despliegue de nuestro sistema. Con los objetos clasificados, segmentados, relacionados o reconocidos, podremos generar señales de alarma en el caso de proyectos de control de calidad industrial, o visualización de datos en reportes mediante herramientas de BI ( _business intelligence_ ) en casos orientados a procesos internos de nuestros clientes. 

Sea como sea, con el objetivo de visión correctamente aplicado, será cuestión de seleccionar la forma en la que queremos emplear estos datos para satisfacer las necesidades de nuestro cliente y solucionar el punto crítico que este ha descubierto en sus procesos. 

En el siguiente diagrama podemos observar un resumen acerca de las fases de un sistema de visión artificial y comparar la diferencia entre los modelos de visión tradicional y aquellos basados en redes neuronales 



33 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **1.3. Breve historia y campos relacionados** 

Dado que ya hemos profundizado en la historia general de la inteligencia artificial durante nuestra primera asignatura del máster, no vamos a entrar más en detalle en esta, y sencillamente vamos a remarcar los hechos más relevantes que afectarán a nuestro estudio de la asignatura desde una perspectiva práctica. 

En 1959 se diseña el primer sistema que permite escanear imágenes para convertirlas en matrices de números. Es, por tanto, el nacimiento de la imagen digital, permitiendo almacenar información visual en dispositivos de memoria para acceder a ella y trabajar con la misma posteriormente. Con la creación del concepto de IA en Dartmouth, surgió inmediatamente el de visión artificial, ya que desde los inicios de la IA esta fue una de sus disciplinas más estudiadas y esperadas. 

Durante los años 70 surgieron los primeros algoritmos de extracción de características a partir de estas matrices numéricas denominadas imágenes digitales. Durante esta década comenzaron las técnicas de extracción de bordes, estimación del movimiento y detección de líneas y formas básicas. Surgieron en consecuencia los primeros detectores de caracteres (OCRs por sus siglas en inglés de Reconocimiento Óptico de Caracteres) que permitían leer el texto contenido en imágenes, originalmente como apoyo a las personas con limitaciones en la visión. 

A lo largo de la década de los 80, estos métodos fueron complicándose a medida que se aplicaba el análisis matemático a estas matrices de números, y se comenzó a trabajar con el concepto de textura, de sombreado y de contornos complejos. Comenzó a comprenderse que la extracción de información de una imagen no era más que un problema matemático que podía resolverse mediante herramientas existentes desde décadas atrás, en este caso aplicadas a información visual. Como ya hemos estudiado, esta fue la época en la que se presentaron por primera vez los primeros modelos de redes neuronales complejas destinadas a la visión artificia, tales como las Redes Neuronales Convolucionales (CNN) l, aunque quedaban décadas para que la capacidad de cómputo de los equipos fuera suficiente como para ejecutarlos con solvencia. 

En los años 90, el foco se puso en los dispositivos de captura. La calibración espacial de cámaras, así como la extracción de información de profundidad a base de dos cámaras - como en las cámaras estereoscópicas – centraron toda la atención. La fotogrametría y la reconstrucción de escenas ganaron terreno, abriendo además el camino de los enormemente deseados vehículos autónomos. Por primera vez durante esta época se aplicaron modelos estadísticos – precursores del machine learning actual – para detectar elementos complejos en imágenes, como son las caras humanas. En esta década, más de 100 empresas ya estaban dedicadas en exclusiva al sector de la visión artificial. Gracias a la gran expansión de internet durante esta década, la red se llenó de imágenes digitales, lo que sería el campo de cultivo sobre el que crecerían las bases de datos para entrenar los grandes modelos de aprendizaje automático posteriores. 

34 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Ya en el siglo XXI aparecen las grandes competiciones de reconocimiento de imágenes como PascalVOC o ImageNet. También comienza a crecer enormemente el sector del vehículo autónomo, siempre sustentado en los últimos algoritmos de visión artificial. Y el sector de la videovigilancia comienza a usar en masa algoritmos clásicos de detección de personas y segmentación de espacios (que veremos más adelante). Sin embargo, no será hasta 2012, cuando gracias al empleo de las GPUs de NVIDIA para ejecutar Redes Neuronales Convolucionales, que explotaría esta disciplina. A partir de este momento, el empleo de redes neuronales de aprendizaje profundo se ha extendido por todos los sectores que emplean visión artificial, y cientos de miles de empresas de todos los tamaños se han especializado en esta tecnología. En la actualidad la gran mayoría de dispositivos cuentan con algoritmos de visión artificial embebidos. Desde nuestros dispositivos móviles hasta las cámaras de seguridad pasando por los vehículos autónomos. Pero también en la grandísima mayoría de líneas de producción industriales, de controles de calidad de fabricación y de análisis de imagen médica y de laboratorio. La década de 2020 se considera como aquella en la que la visión artificial se consolidará como tecnología predominante dentro de la IA, con avances tales como las Redes Adversarias Generativas (GANS) que generan contenido automático, o los últimos avances en Transformers. 

En definitiva, hasta hace diez años toda la visión artificial desarrollada y desplegada correspondía a los algoritmos denominados como “clásicos”, orientados a la extracción dirigida de características y a la clasificación y detección de objetos sencillos. Gracias a las redes neuronales, en concreto a las CNN, y al empleo de la potencia de cómputo de las GPUS, la visión artificial entró en una nueva era en la que la precisión y velocidad de cómputo superaron con creces todas las predicciones. A lo largo del resto de esta asignatura, profundizaremos en estos algoritmos y en cómo implementarlos en procesos reales, para conocer desde dentro una de las tecnologías más prometedoras de la década. 

La visión artificial es un campo que no se puede comprender de forma aislada a otras muchas disciplinas. Por supuesto, es parte de la disciplina más amplia de la Inteligencia Artificial, y como tal, comparte muchas características con esta, así como con otras ramas de la misma como puede ser el Procesamiento del Lenguaje Natural. 

Sin embargo, hay otros campos menos obvios que juegan o han jugado un papel muy relevante a la hora de ampliar la base de conocimiento y capacidades de la visión artificial. 

Por supuesto, uno de los campos más importantes relacionados con la visión artificial son las matemáticas. Por un lado, los modelos clásicos son, como ya hemos comentado, operaciones sobre matrices para encontrar ciertas características. Las funciones que detectan bordes son las mismas que detectan máximos y mínimos en una matriz, contenga esta lo que contenga, por ejemplo. Todos los métodos tanto clásicos como basados en aprendizaje profundo están sustentados en modelos matemáticos y estadísticos, por lo que un ingeniero de visión artificial deberá conocer y dominar estos campos en caso de desear investigar y ampliar el conocimiento disponible a día de hoy. 

35 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por otro lado, nos encontramos a la física, en concreto la física de estado sólido. Todos los dispositivos de captura que generan las imágenes procesadas por los algoritmos de visión artificial están basados en sensores de imagen, que básicamente detectan la radiación electromagnética de la luz, sea esta infrarroja, visible o perteneciente a cualquier otro espectro. En este mismo punto de captura, la óptica en la que se basan las lentes de las cámaras es esencial para poder modificar las características de la imagen origina, como veremos en la unidad de _machine vision_ . 

La robótica, la ingeniería industrial y el control de calidad son otros campos científicos y técnicos íntimamente relacionados con la visión artificial. 

Generalmente, los equipos de visión artificial son multidisciplinares, y tratan de cubrir todos estos elementos con profesionales específicos, desde la selección de dispositivos de captura y lentes, a la infraestructura de procesado, pasando por la decisión sobre los algoritmos a implementar y por último la visualización de los resultados, cada uno tiene un sitio esencial en la cadena de valor de las soluciones de visión artificial. 

### **1.4. Características en la actualidad** 

La disciplina de la visión artificial pasó de ser un campo minoritario en el mundo de la IA a ser una de las disciplinas más importantes en tan solo un año, desde la publicación del artículo de AlexNet en 2012 acerca del uso de Redes Neuronales Convolucionales entradas sobre tarjetas gráficas (GPUs). Desde entonces, han surgido incontables librerías y _frameworks_ en numerosos lenguajes de programación para intentar dar respuesta a un mundo empresarial enormemente interesado en desarrollar esta tecnología. En la actualidad todos los lenguajes de programación tienen librerías orientadas a la visión artificial, desde lenguajes de bajo nivel como C y C++ hasta lenguajes web como JavaScript. A día de hoy se pueden desarrollar algoritmos de visión artificial en prácticamente cualquier lenguaje de programación. 

No obstante, hay una serie de lenguajes de programación que suelen tener más éxito en el mundo de la visión artificial, por diversos motivos. 

La librería más extendida de visión artificial tradicional del mundo, OpenCV, surgió originalmente en C++. Esta librería, originalmente orientada al tratamiento de imágenes y la extracción de características, fue la base sobre la que se desarrollaron la inmensa mayoría de sistemas de visión artificial desde principios de siglo. Desde la explosión del _deep learning_ en esta disciplina, incontables grupos de investigación de numerosas universidades a lo largo del mundo comenzaron a desarrollar sus propios modelos y arquitecturas de algoritmos de visión artificial, algunos de los cuales estudiaremos más adelante. Originalmente los lenguajes de programación de los científicos de datos y de los investigadores universitarios orientados al tratamiento de datos – numéricos o de imágenes – eran Matlab y R. Ambos son lenguajes de programación de muy alto nivel, con funciones estadísticas y matemáticas previamente diseñadas, acelerando notablemente el tiempo de desarrollo en investigaciones. 

36 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Sin embargo, con el surgimiento del _deep learning_ un lenguaje de programación desbancó a todos por su facilidad, flexibilidad y legibilidad: Python. Este es el lenguaje en el que están programados la práctica mayoría de artículos de visión artificial a día de hoy. Pensar en desarrollar algoritmos de _deep learning_ sobre GPUs es pensar en Python. La mayoría de repositorios que encontraremos en las grandes universidades con modelos propios de _deep learning_ estarán desarrollados en Python, así como los principales _frameworks_ para desarrollar soluciones de aprendizaje profundo. 

Estos _frameworks_ son variados y han evolucionado a lo largo de la década que lleva siendo el _deep learning_ predominante en visión artificial. Todos ellos ofrecen un conjunto de módulos en Python que permiten construir de forma más o menos intuitiva los distintos componentes de distintos tipos de redes neuronales. Cuentan con distintos niveles de abstracción, desde la programación minuciosa neurona a neurona, hasta la importación de modelos previamente desarrollados para su entrenamiento y despliegue automáticos. Estos _frameworks_ son esenciales en el trabajo de cualquier desarrollador de visión artificial, ya que evitan partir de cero en cada proyecto, y permiten reutilizar módulos previamente preparados para acortar tiempos y asegurarse de la calidad del resultado del trabajo. Detrás de estos _frameworks_ suele haber grandes corporaciones como Google o Facebook, que son las que financian y liberan el código para hacerlo accesible a todo el mundo. Los _frameworks_ más importantes en la actualidad son: 

- TensorFlow. TensorFlow es una librería de Python gratuita y de código abierto desarrollada por Google. Está centrada en la creación, entrenamiento y optimización de modelos de _deep learning_ basados en redes neuronales. Cuenta con integración directa con las GPUs de NVIDIA y es el _framework_ más empleado en la actualidad para el diseño y despliegue de proyectos de _deep learning_ , no solo en visión artificial. 

- Keras. Esta librería trata de ser una interfaz de abstracción entre TensorFlow y el desarrollador. Cuenta con una gran cantidad de modelos, arquitecturas y tipos de capas neuronales previamente desarrollados de forma que se pueden importar. Esto abstrae a los desarrolladores noveles de la complejidad de la implementación de las distintas operaciones que realizan las redes neuronales convolucionales, permitiendo que construyan complejos modelos sin entrar en el nivel matemático más profundo de las mismas. Esta será la librería que utilizaremos mayoritariamente para los ejemplos que ejecutaremos con redes neuronales profundas. También pertenece a Google en la actualidad. 

- PyTorch. Esta librería, de nuevo en Python, persigue un objetivo mixto entre los que persiguen TensorFlow y Keras. Cuenta con módulos automáticos para la creación de redes neuronales profundas, así como integración con GPUs de CUDA para aprovecharse de las capacidades de aceleración de las tarjetas gráficas. Es actualmente el _framework_ que más rápido está creciendo, ya que cada vez se publican más artículos cuyo código de ejemplo está desarrollado en PyTorch. 

37 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por ello, dedicaremos un ejemplo a ejecutar una red neuronal profunda en PyTorch de forma que hayamos interactuado con él antes de finalizar la asignatura. Tiene sus orígenes en las librerías de Facebook Caffe y Caffe 2, que acabaron integrándose en este proyecto más grande y actualizado. 

- MxNet. MxNet es el intento de Microsoft de competir contra TensorFlow-Keras y PyTorch. Es un sistema basado en Apache – el _cloud_ de Microsoft – que permite gestionar tanto la infraestructura subyacente de los modelos como las propias redes neuronales. Soporta una grandísima variedad de lenguajes de programación (Python, C++, Matlab, R, JavaScript), pero está notablemente menos extendido que el resto de _frameworks_ por lo que su utilidad es limitada en esta disciplina. 

Cada vez hay más perfiles relacionados con la visión artificial en el mercado laboral. Habitualmente, los desarrolladores de visión artificial provienen de ramas cercanas a la ingeniería. Ingenieros informáticos, ingenieros de computadores, ingenieros de software, matemáticos, estadísticos e ingenieros en telecomunicaciones suelen copar los puestos de desarrollo de visión artificial. Sin embargo, aún a día de hoy existe una falta de perfiles relacionados con la gestión de proyectos relacionados con visión artificial. Esto implica desde la toma de requisitos, hasta la selección de los dispositivos de captura y de los algoritmos más indicados para resolver según qué problema. 

El objetivo de esta asignatura es proporcionar una perspectiva lo más amplia posible sobre el campo de la visión artificial. Debido a limitaciones de espacio y tiempo, no podremos cubrir la totalidad de algoritmos, aproximaciones, arquitecturas de redes neuronales y dispositivos de captura que existen en la actualidad. Sin embargo, trataremos de proporcionar una base común que permita al alumno conocer esta disciplina tecnológica, sus capacidades, sus limitaciones, y la tecnología que la hace posible. Por suerte, esta disciplina es realmente abierta a todos los que quieran participar de ella. Absolutamente todos los artículos en los que se presentan nuevos modelos y arquitecturas están disponibles en arXiv, un servicio de distribución gratuito de artículos científicos. Además, cada vez más artículos cuentan con un repositorio con el código relacionado con el artículo, de forma que podemos acceder al mismo y ejecutarlo. Por último, tecnologías como los cuadernos de Google Colab – que probaremos – para poder ejecutar código de visión artificial en remoto, hacen que el acceso a esta tecnología sea totalmente abierto. NO obstante, es necesario contar con una base teórica y práctica consolidada para comprender estos artículos y poder sacar todo el provecho de los mismos. Esta asignatura trata de ser un resumen de la tecnología de forma que la conozcamos en toda su amplitud, y para aquellos que deseen profundizar en ella, un primer paso que pueda abrir las puertas de futuros desarrollos, proyectos y éxitos. 

38 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

## **2. Técnicas de procesamiento de imágenes y reconocimiento visual. Color, filtros y extracción de características** 

_“Una imagen es una matriz de numerosos elementos elementales denominados píxeles. Cada uno de estos píxeles tiene un valor numérico. Generalmente el valor de este pixel está relacionado con la intensidad del color que debe representar.”_ 

### **2.1. Preparación del entorno de desarrollo y pruebas** 

Para el aprendizaje, desarrollo y pruebas de los distintos métodos que vamos a estudiar en este módulo, vamos a hacer uso de una serie de herramientas que facilitarán nuestro trabajo de desarrollo y permitirán que nos centremos en comprender las diversas técnicas y poder abstraernos del código fuente. En esta primera sección, trataremos de conocerlos y de dar las pautas para preparar nuestros entornos – es decir, nuestros PC – para poder probar los distintos ejemplos que se proponen a lo largo del módulo. **No es necesario ejecutar ninguno de los ejemplos para superar la asignatura, y no será considerado para la evaluación, ya que es suficiente con comprenderlos** , no obstante, se recomienda encarecidamente tratar de preparar el entorno personal y de ejecutar los ejemplos para poder sacar el máximo provecho al estudio de esta asignatura. 

Es importante recalcar que tampoco es necesario tener ningún conocimiento previo de programación para poder instalar todas las librerías y ejecutar los diversos fragmentos de código relativos a cada técnica. No obstante, el conocimiento de cualquier lenguaje de programación, y más en concreto de Python, permitirá al alumno poder integrar estos métodos en aplicaciones de mayor envergadura con orientación a producción. No es este nuestro objetivo en este módulo, ya que nos centraremos en la teoría de cada método o técnica, y veremos cómo ejecutarlo en nuestros entornos personales, sin profundizar en cómo están codificados en sus respectivas librerías ni en cómo integrarlos en aplicaciones comerciales. 

39 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Para resumir, **no es necesario** conocer el lenguaje de programación Python ni siquiera tener conocimientos de programación para estudiar y superar este módulo de visión artificial. Los ejemplos de código servirán para ilustrar cada técnica y poder ponerla en práctica. Sin embargo, para aquellos alumnos con conocimientos de programación o con interés en tenerlos, será interesante ejecutar y comprender en profundidad los _snippets_ (fragmentos de ejemplo) de código ya que podrán sacar provecho de todos ellos en el futuro. 

Para tratar de ofrecer una guía de cualquier nivel a aquellos interesados en aprender o profundizar en Python, se proponen los siguientes libros en función del nivel con el que se comienza, de forma que puedan complementar este módulo – y los siguientes – para aquellos que lo deseen. **En ningún caso su lectura es obligatoria** , y no se dará por sentado ningún concepto que pueda aparecer en ellos. Sin embargo, su lectura es enriquecedora y facilitará el avance a lo largo del máster a cualquiera que los lea, muy especialmente a aquellos alumnos de nivel iniciación que nunca hayan programado. A los alumnos con experiencia en programación con otros lenguajes se les recomienda estudiar los básicos de Python para poder sacar el máximo provecho. Aquellos con experiencia previa en Python podrán comprender, ejecutar e incluso modificar sin dificultad los ejemplos que emplearemos y no será necesario ampliar su conocimiento, aunque propondremos lecturas para ellos también. 

Es importante que, en el caso de leer cualquiera de ellos, se obtenga la edición más actualizada del mismo y que **se analicen preferentemente los ejemplos basados en Python3** , ya que la versión 2 de Python es actualmente empleada únicamente para mantener aplicaciones ya desarrolladas, y a lo largo de este módulo solo emplearemos ejemplos basados en versiones de Python3, por lo que será optimo centrarse en este Python a la hora de estudiarlo. 

a. Alumnos sin ningún conocimiento de programación. 

   - _“Think Python: How to Think Like a Computer Scientist”_ por Allen B. Downey. Diseñado para aprender a programar desde cero, empleando Python como lenguaje de soporte. Nos ayudará a comprender mejor los ejemplos de código e incluso a modificarlos. 

- b. Alumnos con conocimientos de programación en otros lenguajes o con experiencia muy limitada en Python. 

   - _“Python in a Nutshell: A Desktop Quick Reference”_ por Alex Martelli, Anna Martelli y Steve Holden. Orientado a programadores que empiezan a usar Python y desean conocer su funcionamiento y librerías básicas. 

   - _“Python Programming for Beginners”_ - AMZ Publishing. Un recorrido por los tipos de datos, variables, operaciones y sintaxis de Python con ejemplos basados en la vida real listos para ser ejecutados. 

40 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

   - _“Fluent Python: Clear, Concise, and Effective Programming”_ por Luciano Ramalho. Orientado al traspaso de un lenguaje de programación a Python3 con el foco en la claridad y eficacia del código desde el principio. 

- c. Alumnos con experiencia previa en desarrollos de Python. Si bien no será necesario profundizar en técnicas específicas antes del estudio del módulo, se propone un libro orientado a la optimización y eficiencia del código para aplicaciones comerciales avanzadas. 

   - _“Expert Python Programming: Become a master in Python by learning coding best practices and advanced programming concepts in Python 3.7”_ por Michal Jaworski. Orientado a refinar las habilidades y conocimientos en Python para desarrollar código fácil de gestionar, escalable y óptimo. 

### **2.1.1. Instalación de Python, Anaconda y Jupyter Notebook** 

Para facilitar la instalación de todas las herramientas y librerías que vamos a emplear en este módulo, usaremos un _software_ de recopilación de herramientas (llamado _toolkit_ en inglés) que está orientado al desarrollo de proyectos de _machine learning_ con Python, denominado **Anaconda.** Dentro de este paquete, usaremos un aplicativo de edición y ejecución visual de código fuente llamado **Jupyter Notebook** . 

#### **Python** 

Python es un lenguaje de programación de alto nivel, interpretado y orientado a objetos, con un tipado dinámico. Esto implica: 

- a. El programador puede olvidarse de los detalles físicos del hardware de su ordenador como la memoria (alto nivel) 

- b. Se ejecuta línea a línea mediante un intérprete, lo que permite realizar ejecuciones parciales sin necesidad de compilar todo el código fuente a código máquina (interpretado) 

- c. Permite programar mediante instancias individuales de objetos, que siguen un esquema perteneciente a clases previamente definidas, sirviendo así de modelo simple y reutilizable (orientado a objetos) 

- d. No requiere de una definición del tipo de variable previamente al empleo de la misma, ya que el intérprete es capaz de inferir el tipo de cada variable, y además las mismas variables pueden tomar valores de distinto tipo (tipado dinámico). 

No es imprescindible comprender estos conceptos para poder avanzar en esta asignatura, si bien son relevantes para comprender por qué Python es el lenguaje más empleado actualmente en la investigación y desarrollo de nuevos algoritmos y modelos de visión artificial. 

41 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Gracias a ser uno de los lenguajes de programación más simples y concisos de entre aquellos de uso mayoritario, con fácil legibilidad, un número creciente de librerías, y gracias a la velocidad de desarrollo que proporciona, así como a su flexibilidad, se ha convertido en el lenguaje de programación por excelencia para desarrollos de _data science_ e Inteligencia Artificial, incluyendo, cómo no, la visión artificial. Es por ello que todos los ejemplos que emplearemos estarán basados en Python. 

Es un lenguaje de programación que puede ejecutarse en una consola de comandos en cualquier sistema operativo, pero esta no suele ser la forma más intuitiva de usarlo. Habitualmente se emplean programas dedicados específicamente al desarrollo de software con Python (llamados IDES, por sus siglas en inglés Entorno de Desarrollo Integrado), que facilitan la tarea del desarrollador a la hora de importar librerías, definir clases y definir métodos. Iremos avanzando en estos conceptos a lo largo del desarrollo de esta asignatura. 

#### **Anaconda** 

Anaconda es una distribución de Python y R – otro lenguaje de programación empleado para el tratamiento estadístico de grandes cantidades de datos – que proporciona todo lo necesario para comenzar a desarrollar de forma fácil y directa, incluyendo Python, numerosas librerías, IDEs para desarrollar programas, y un gestor de paquetes propio. También tiene la posibilidad de añadir numerosas aplicaciones extra, como es el caso de la aplicación que emplearemos en este módulo: Jupyter Notebook. 

#### **Jupyter Notebook** 

Jupyter notebook es una aplicación que se ejecuta en nuestro PC en forma de servidor web local, y que se usa accediendo a ella a través de cualquier navegador web, sin necesidad de tener una conexión a internet activa. Permite ejecutar código de Python de forma fragmentada para mejorar la comprensión y análisis del código. Permite también añadir elementos de diseño como imágenes, gráficos, y edición de texto que enriquecen los ejemplos durante cualquier formación. Es también una de las herramientas más empleadas para mostrar y compartir ejemplos de código en Python entre distintos investigadores y desarrolladores, así como para aprender a usar nuevas librerías, técnicas y métodos en _machine learning_ y visión artificial. 

Gracias al conjunto de estas tres utilidades que acabamos de mencionar, junto a la instalación de librerías específicas de visión artificial, seremos capaces de construir y ejecutar todos los _snippets_ de esta asignatura y así hacer funcionar nuestros propios algoritmos de visión artificial. 

Para alumnos avanzados en programación será posible instalar Python, sus librerías y Jupyter Notebook mediante cualquier otro método distinto a la distribución Anaconda, pero esta opción no tendrá soporte por parte del profesorado de máster debido a las innumerables opciones que existen para realizar esta tarea y por tanto la gran variabilidad de problemas que pueden llegar a surgir derivados de las mismas. 

42 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En caso de no tener un motivo de peso para desviarse de las instrucciones que vamos a ofrecer a continuación, recomendamos encarecidamente emplearlas. Para aquellos alumnos con entornos Python instalados en sus equipos, es importante recordar que se pueden tener varias distribuciones de Python en el mismo sistema, por lo que podemos seguir estas instrucciones sin que el resto de nuestros entornos corran peligro, como veremos a lo largo de las instrucciones. 

Debido a que Windows es el Sistema Operativo más extendido a comienzos de 2022 (73.72%) frente a macOS (15.33%) y Linux (2.09%), todos los ejemplos de esta sección estarán orientados al sistema operativo Windows de Microsoft. 

Sin embargo, como en todos los casos, será posible instalar y ejecutar todos los programas, librerías y _snippets_ de código tanto en macOS como en Linux, ya que existe soporte de Python, Anaconda y Jupyter Notebook para ambos. Los pasos a seguir serán prácticamente los mismos, y en caso de haber alguna diferencia se indicará en las instrucciones, aunque estas diferencias son muy escasas. En caso de tener un equipo con dos sistemas operativos gracias a _dual boot_ , recomendamos emplear Windows para poder seguir las instrucciones con mayor facilidad. Es preciso recalcar que la gran mayoría de investigación en el ámbito de la visión artificial se realiza en Linux, pero a lo largo de este módulo no vamos a realizar tareas de investigación sino de implementación y desarrollo, para lo que Windows es el OS más extendido desde el punto de vista comercial e industrial. 

**NOTA IMPORTANTE:** Es posible que los alumnos no tengan el hardware necesario en su equipo personal para instalar y ejecutar estos programas por limitaciones de capacidad de cómputo, por limitaciones de memoria o espacio en disco, o no deseen instalar ninguno de estos tres paquetes de software por motivos personales cualesquiera, que no serán analizados en ningún momento. 

En cualquiera de estos casos, merece la pena recalcar que **todos los ejemplos que vamos a mostrar a lo largo de esta asignatura también pueden ser ejecutados directamente en la nube mediante una herramienta llamada Google Colab** , que permite usar Python y todas las librerías de visión artificial tan solo con tener un navegador web instalado y una cuenta de Google, de forma totalmente gratuita. La única desventaja es que se necesita una conexión a internet constante y estable para su uso. 

Si bien es recomendable tratar de poner en marcha un entorno local de visión artificial según las instrucciones indicadas debajo de esta nota, ya que esta experiencia es muy valorada en el mercado laboral, aquellos alumnos que no deseen hacerlo podrán usar directamente Google Colab para ejecutar **cualquier ejemplo de esta asignatura desde el primero de ellos** . Esto no supondrá ningún tipo de penalización desde el punto de vista del aprendizaje ni, por supuesto, para su calificación final. 

43 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Para los alumnos que opten por Google Colab directamente, recomendamos saltar el contenido restante de esta sección y leer a continuación y por orden las dos secciones indicadas en el siguiente párrafo para poder ejecutar todos los ejemplos restantes en Google Colab sin problemas. 

Por un lado, es imprescindible leer la unidad 3.1, en la que se indican los principios básicos de Google Colab desde cero. Una vez comprendida esta sección, es necesario saltar directamente a la unidad 2.2 (omitiendo el texto restante de esta sección) para comenzar directamente el aprendizaje teórico y práctico de esta asignatura, omitiendo por tanto todas las instrucciones para instalar Python, Anaconda, Jupyter Notebook y OpenCV, que no serán necesarios en caso de usar Google Colab. 

**Ambas opciones son totalmente válidas, y depende de las capacidades del equipo del alumno, de su conectividad a internet y de sus preferencias personales ejecutar los ejemplos de esta sección en un equipo local (para lo que debe seguir las instrucciones indicadas a continuación) o en cuadernos en la nube de Google Colab (para lo que debe leer las dos secciones indicadas y continuar con el desarrollo de la asignatura).** 

Esta es también una opción válida para aquellos alumnos que traten de instalar un entorno local, pero por cualquier motivo esto no resulte posible finalmente. Si tras varios intentos no es posible tener un entorno local preparado para los ejemplos, nuestro consejo es que se use directamente Google Colab desde el principio. 

Si hemos decidido emplear un entorno local para los primeros ejemplos de esta asignatura, a continuación, se presentan los pasos e instrucciones para hacerlo. 

Para comenzar a preparar nuestro equipo local, **en caso de haber optado por ello** , descargaremos el paquete de instalación de la _suite_ de Anaconda desde su página web oficial. Para ello, accederemos a la dirección enlazada, y haremos click en el botón de descarga (“Download”). Descargaremos siempre la **última versión** , que es la que aparece por defecto en la página web. Debido a que este manual se ha generado en un momento del tiempo concreto, es posible que en el momento de la descarga por parte del alumno la versión no coincida exactamente con la mostrada en las capturas de pantalla. Esto es totalmente normal y no debe preocuparnos. Siempre descargaremos la última versión para nuestro sistema operativo – que se detectará automáticamente, pero puede cambiarse manualmente en los botones inferiores en caso de ser necesario – y procederemos a la instalación. 

44 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Para comenzar la instalación, abriremos el archivo “.exe” que se ha descargado. Una vez abierto, recibiremos una advertencia que deberemos aceptar y haremos click en “Ejecutar” 



Después, haremos click en los botones “Next”  “I Agree”  “Next” en las siguientes dos pantallas sin necesidad de cambiar ninguna configuración en las mismas. 



45 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

A continuación, debemos elegir dónde deseamos que se instale Anaconda. A no ser que tengamos algún motivo para cambiar la ubicación, recomendamos que se mantenga intacta la ubicación que el programa de instalación ofrece por defecto y se pulse “Next”. 

Por último, es deberemos revisar la configuración de instalación. Recomendamos mantener la configuración por defecto, que es la que se muestra en la captura de pantalla de la derecha, **excepto en un único caso** . Si estamos instalando Anaconda en un PC en el que ya estamos desarrollando aplicaciones con Python previamente – bien sean personales o laborales – **NO debemos marcar la segunda casilla** , ya que indicará al sistema operativo que este es el Python por defecto de nuestro sistema, y podríamos estropear las configuraciones de lanzamiento de nuestros proyectos previos que tengamos en otros IDEs, así como el lanzamiento por defecto de Python desde la consola de Windows. 

En cualquier otro caso, que serán la mayoría, mantendremos las opciones por defecto tal y como se observa en la imagen, y seleccionaremos “Install”. 



Una vez empiece la instalación, veremos una barra de progreso que demorará unos minutos. Cuando esta llegue a su fin podremos hacer click en el botón “Next”. En este momento, el instalador puede que nos recomiende un IDE (entorno de desarrollo, un programa diseñado para desarrollar código) llamado PyCharm. Si bien este IDE no es necesario en ningún momento a lo largo del módulo, es recomendado para todos aquellos que decidáis seguir algún libro de Python para aprender o ganar soltura en este lenguaje. También es recomendable para aquellos que deseéis modificar los ejemplos de este módulo y construir en base a ellos proyectos más complejos, ya que PyCharm es el entorno de desarrollo mejor integrado con las herramientas que acabamos de instalar y que vamos a emplear. No obstante, por supuesto los resultados serán idénticos en caso de desear emplear cualquier otro IDE como pueden ser Spyder, Visual Studio, Sublime, Atom, IDLE, Eclipse… 

46 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por último, es recomendable que cuando pasemos la última pantalla, deseleccionemos ambas casillas que vienen por defecto marcadas, ya que ambas nos llevarán a tutoriales online que no son necesarios para avanzar con la preparación de nuestro entorno. Al hacer click en “Finish”, tendremos Anaconda totalmente instalado en nuestro sistema. 

Anaconda no es más que una distribución y un conjunto de herramientas unidas para facilitar la vida del desarrollador de _data science & machine learning_ en Python, que se encuentran unidas en un menú principal denominado Anaconda Navigator. Para lanzar su vista principal y comenzar a explorar esta herramienta, accederemos al menú de todos los programas de nuestro equipo y, bajo la carpeta de Anaconda, lanzaremos haciendo click el programa “Anaconda Navigator”. En Windows bastará con presionar la tecla Windows y escribir el nombre de este programa. 



Esta que se muestra más abajo es la vista principal de Anaconda Navigator y desde la que podemos lanzar las diversas aplicaciones que contiene esta distribución especial de Python. Nosotros usaremos Jupyter Notebook para crear y ejecutar nuestros ejemplos de visión artificial. En las últimas versiones de Anaconda, esta aplicación se instala por defecto por lo que, para iniciarla, sería suficiente con hacer click en el botón “Launch” que se encuentra debajo del logo y del nombre de Jupyter Notebook, como se ve señalado en la siguiente imagen. Es importante que usemos Jupyter Notebook y **no JupyterLab** , ya que esta aplicación tiene otro propósito. 

47 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



En caso de que Jupyter Notebook no esté instalado, el botón “Launch” no aparecerá, y veremos un botón indicando “Install” en su lugar. Si este fuera el caso, haremos click en este botón “Install” y tras unos minutos sin requerir ninguna acción por parte del usuario, la aplicación se habrá instalado automáticamente y el botón habrá pasado a llamarse “Launch”. Ahora ya podremos por tanto iniciar la aplicación de Jupyter Notebook con facilidad. 

Cuando lancemos la aplicación de Jupyter Notebook por primera vez, se debería abrir nuestro navegador web predeterminado al cabo de unos segundos (Google Chrome, Mozilla Firefox, Microsoft Edge…) y veremos la pantalla principal de Jupyter Notebook. 

El servicio web que emplea para funcionar – es decir, donde se aloja esta web que estamos viendo – está alojado de forma local en nuestro sistema, es por esto que no necesitamos conexión a internet. Esta web es accesible mediante el puerto 8888 de nuestro `localhost` , que es la dirección con la que nuestra máquina puede acceder a sí misma. Esto implica que Jupyter Notebook es accesible desde cualquier navegador. Por tanto, si no se ha abierto el navegador automáticamente, o si deseamos usar otro navegador, para abrir la aplicación una vez iniciada desde Anaconda Navigator podremos hacerlo accediendo mediante la barra de navegación de nuestro navegador introduciendo la URL <u>http://localhost:8888/tree y pulsando ENTER.</u> 

Si todo ha salido bien, veremos una pantalla como la que se muestra en la siguiente imagen, que es la pantalla de inicio de Jupyter Notebook. Una vez en ella, para comprobar que la instalación de Anaconda ha sido totalmente exitosa haremos click sobre el botón New, que se encuentra arriba a la derecha, recuadrado en la siguiente imagen, para crear nuestro primer Notebook, seleccionando la opción de `Python3 (pykernel)` , tal y como se muestra en la imagen. 

48 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Se abrirá una nueva pestaña en el navegador, con nuestro nuevo Notebook. Este Notebook, denominado cuaderno en la documentación traducida, no es más que un archivo que se acaba de crear en nuestro PC según la carpeta que esté abierta en la pantalla inicial de Jupyter. Si queremos que este archivo se cree en una carpeta concreta, deberemos navegar hasta esta carpeta en la página de inicio de Jupyter y posteriormente hacer click en el botón “New”. Este archivo tendrá la extensión `“.ipynb”` , y es un archivo de Python enriquecido diseñado para ser editado, visualizado y ejecutado desde la aplicación web de Jupyter Notebook. 

El nombre de nuestro nuevo notebook se encuentra arriba a la izquierda en una tipografía más grande y se rellena automáticamente al crearlo con el nombre `“Untitled”` . Si pulsamos sobre él, podremos darle un nombre más descriptivo que el que viene por defecto, como por ejemplo `“First Notebook”` . Esto cambiará el nombre del archivo en nuestro sistema local. 

Si nos fijamos en la interfaz de Jupyter Notebook, es muy sencilla. Por un lado, en la parte superior, contamos con una barra de menús desplegables habituales en cualquier aplicación de escritorio `[File, Edit, View, Insert, …]` , y por otro lado una barra botones de acceso rápido para guardar, crear, cortar, copiar, pegar… 

En la parte principal, es decir, todo el resto del espacio, observamos una primera celda, denominada “Cell”. En el rectángulo gris claro será donde escribamos nuestro código en Python para después poder ejecutarlo y observar su resultado. Para comprobarlo, vamos a copiar y pegar el siguiente código adjunto en nuestra primera y nueva celda vacía, como se puede ver en la imagen posterior. Esta dinámica va a ser la que sigamos a lo largo de toda la asignatura para los ejemplos con cuadernos, que serán todos. En cada ejemplo habrá una serie de celdas de código, que deberemos copiar en pegar en celdas de nuestros cuadernos. Es **esencial** copiar las celdas enteras (en ocasiones puede que una celda ocupe varias páginas, pero siempre deberemos copiarlas y pegarlas **íntegras** ). 

49 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

También es imprescindible no modificar la estructura del código. En Python, cada espacio es relevante a nivel de programación, por lo que, si cambiamos cualquier espacio o signo de puntuación, o nos olvidamos de copiar alguno de estos, el código no funcionará. Por ello, lo más fácil es seleccionar el código que se encuentra dentro de cada recuadro negro, y sin hacer ninguna modificación, pegarlo en la celda del ejemplo que estamos ejecutando. Es importante que tampoco incluyamos ninguna tilde en los comentarios, ya que Python no soporta estos caracteres en los comentarios y el código no podrá ejecutarse. 

Vamos a hacerlo por primera vez. Seleccionaremos todo el código de Python del siguiente recuadro, y lo pegaremos en la celda vacía que ha creado Jupyter Notebook en este, nuestro primer cuaderno. 



Este código en Python sencillamente pide al usuario que introduzca dos números mediante su teclado, posteriormente los suma, e imprime el resultado por pantalla. 

Todas las líneas precedidas por el carácter # son comentarios, que sirven para comprender el código, pero no son ejecutados por Python. Los comentarios se usan para describir lo que se espera que haga cada sección del texto, y para que otros desarrolladores puedan comprender el funcionamiento del programa sin necesidad de descifrar el funcionamiento línea por línea de un _script_ . 

Si nos fijamos entonces, este código que hemos introducido en nuestra primera celda tiene cuatro líneas de código. Las dos primeras líneas almacenan los números introducidos por el usuario, que se llaman `num1` y `num2` y guardarán los números introducidos. La tercera línea de código suma estos dos números y guarda el resultado en una variable llamada `sum_numbers` . Por último, la cuarta línea imprime por pantalla estos tres números gracias al método `print()` de Python, y el programa termina. 

Una vez hayamos pegado este código en nuestra primera Cell, podremos ejecutarlo pulsando el botón . En el futuro podremos usar el atajo de teclado de Jupyter Notebook `ctrl+ENTER` , que efectúa la misma acción, si no deseamos pulsar este botón. 

50 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Una vez pulsamos `“Run”` , el intérprete de Python ejecuta nuestro código, línea a línea. Por tanto, lo primero que hace Python es pedirnos introducir un número, luego otro, y finalmente nos comunica el resultado de la suma de ambos. Esto sucede en el espacio que se crea debajo de la Cell, que es donde Jupyter Notebook muestra los resultados de la ejecución de cada celda al usuario. 



Si el resultado de nuestra ejecución es similar al mostrado en la imagen anterior, hemos conseguido instalar con éxito Python, Anaconda y Jupyter Notebook. ¡Enhorabuena! 

En definitiva, hemos preparado a nuestro computador para que comprenda el lenguaje de programación Python. Esto implica que sea capaz de interpretar las líneas de código que vayamos escribiendo, y ejecutarlas correctamente según su código máquina – es decir, las instrucciones en 1 y 0 – que es el lenguaje que comprende su procesador. 

Python puede ser empleado para multitud de aplicaciones, y nosotros nos vamos a centrar en aquellas relacionadas con los datos y el aprendizaje automático, en las que se enmarca la visión artificial. Es por ello que nos hemos ayudado de Anaconda, que no es más que un programa que nos ayuda a instalar Python, así como otras herramientas que emplearemos para facilitar la ejecución de ejemplos. Por último, hemos empleado una de estas herramientas, llamada Jupyter Notebook. 

Si bien podemos ejecutar Python desde un archivo cualquiera con la extensión `“.py”` , esto no es óptimo para el aprendizaje que vamos a realizar, ya que no podríamos ver el código y el resultado en la misma pantalla, así como tampoco ciertos gráficos e imágenes. Con esta intención surge – y nosotros empleamos – Jupyter Notebook. Gracias a esta aplicación basada en web, podemos escribir y ejecutar comandos en Python paso por paso, para así comprender mejor qué resultados obtenemos de cada uno, y permitir un proceso de aprendizaje más fluido y enriquecedor. 

51 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **2.1.2. Instalación de OpenCV** 

Como ya hemos mencionado en la unidad de introducción, una de las librerías más extendidas en el campo de la visión artificial en la actualidad es OpenCV. 

OpenCV ( _Open Source Computer Vision Library_ ) es una librería de programación de código abierto destinada a la visión artificial y el aprendizaje automático. Esto implica se puede acceder al código fuente de todos los métodos. Además, tiene una licencia BSD, que impone restricciones mínimas a la hora de usar, modificar y redistribuir su código, siendo muy cercana al dominio público. Actualmente cuenta con más de 2500 algoritmos optimizados, incluyendo tanto algoritmos clásicos de visión artificial como otros que se encuentran el estado del arte y que están basados en aprendizaje automático y aprendizaje profundo. Entre otros, encontraremos algoritmos para el reconocimiento facial, la identificación de objetos, la detección de pose, el seguimiento del movimiento ocular, la detección de bordes y características y un largo etcétera. 

Ofrece soporte para C++, Python y Matlab, así como para Windows, MacOS, Linux y Android. También cuenta con algoritmos que soportan la integración con la tecnología CUDA de NVIDIA – que vimos en el primer módulo – para permitir así la aceleración de los mismos gracias a la enorme capacidad de cómputo de una GPU. Es, en definitiva, **la librería más empleada a nivel mundial en el campo de la visión artificial** , con un estimado de 18 millones de descargas en todo el mundo. Por ello, se considera un básico esencial de esta disciplina y será una de las librerías que estudiaremos con mayor profundidad a lo largo de este módulo. 

El primer paso para conocer y experimentar con esta librería será incorporarla a nuestro recién instalado entorno basado en Python, Anaconda y Jupyter Notebook. 

Para instalar OpenCV en nuestro entorno, abriremos de nuevo la aplicación de escritorio Anaconda Navigator y esta vez, en vez de Jupyter Notebooks, lanzaremos la aplicación denominada “CMD.exe Prompt” mediante el botón “Launch”, que suele ser la primera aplicación de toda la lista. Podemos ver el icono de esta aplicación y su ubicación en la siguiente imagen para estar seguros de que estamos lanzando la aplicación correcta. Esta aplicación iniciará un terminal de Windows – que veremos como una pantalla negra tal y como la que se puede observar en la imagen – para poder ejecutar comandos sobre ella. 

Lo único que tenemos que hacer en esta aplicación es copiar y pegar una serie de comandos, y la instalación de OpenCV en nuestro entorno se ejecutará automáticamente sin necesitar de nuestra interacción, por lo que no es necesario tener ningún tipo de conocimiento sobre la terminal de Windows. Para proceder, copiaremos el siguiente comando, y lo pegaremos directamente sobre la ventana de terminal que se ha abierto automáticamente. 

```
 pip install opencv-contrib-python
```

52 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Una vez pegado este comando en nuestra terminal, pulsaremos la tecla ENTER. 

Se descargará e instalará durante unos minutos automáticamente el paquete de OpenCV para Python. Cuando recibamos el mensaje `“Successfully intalled opencv-contrib-python-X.X.X.XX”` , ya estará instalado en nuestro entorno. Ahora, podemos cerrar la ventana de terminal, y volver a la página principal de Anaconda Navigator. 



Ahora, vamos a instalar otra librería de apoyo para gestión de imágenes llamada scikit image, de la que usaremos varias funciones e imágenes de ejemplo. Para ello, repetimos los mismos pasos. Sin salir de la aplicación de terminal, copiamos y pegamos el siguiente comando, y pulsamos la tecla ENTER. 

```
pip install scikit-image
```

Según la distribución de Anaconda, scikit image puede estar ya instalada. En este caso, veremos una salida por terminal similar a la siguiente, indicando que la librería ya está instalada. Este es un resultado igual de bueno que si la salida del terminal nos indica que la instalación ha sido satisfactoria. Este paso lo realizamos dado que hay ciertas distribuciones de Anaconda que no tienen este paquete instalado por defecto, y es un paquete que necesitaremos para múltiples ejemplos en esta unidad. 

53 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Para comprobar que la instalación de ambas librerías ha sido satisfactoria, crearemos un nuevo Notebook en el que podremos probar por primera vez la librería de OpenCV en Python en nuestro entorno recién preparado. Para ello, repetimos los pasos que hemos dado con anterioridad: 

1. Abrimos Anaconda Navigator en nuestro equipo 

2. Después, lanzamos la aplicación de Jupyter Notebook, que abrirá nuestro navegador por defecto en la pantalla principal, o si no accederemos a él mediante el enlace en cualquier navegador: http://localhost:8888/tree. 

3. Una vez en la pantalla principal, haremos click arriba a la derecha en “New” y posteriormente seleccionaremos la opción “Python 3” para así crear un nuevo Notebook, que se abrirá en una nueva pestaña. 

4. Una vez dentro de esta nueva pestaña, podremos cambiarle el nombre por defecto “Untitled” por “OpenCV installation test”, tan solo pulsando sobre el nombre del notebook. 

5. Ahora, veremos de nuevo una Cell vacía, preparada para que introduzcamos nuestro código en Python para poder ejecutarlo. Pegaremos en la primera celda todo el contenido del código adjunto más adelante, sin cambiar nada del mismo. 

6. Una vez introducido en la Cell lo ejecutaremos pulsando el botón “Run”. 

54 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



El resultado para confirmar que la instalación ha sido correcta debería ser tal y como se muestra en la siguiente imagen. Si es así, la instalación de OpenCV ha sido satisfactoria y nuestro entorno está en condiciones para comenzar a avanzar por todos los métodos y técnicas de visión artificial clásica. 



55 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Si bien el objetivo de este código es meramente probar la instalación de OpenCV, vamos a explicarlo brevemente para satisfacer la curiosidad de algún alumno. Las tres primeras líneas sencillamente indican a Python las librerías con las que vamos a trabajar, y las importa dentro de nuestro código. 

Después, línea a línea: 

1. OpenCV trabaja con matrices, que como ya hemos mencionado son la base de una imagen digital. Estas matrices tienen un alto, un ancho, y un profundo. El alto y el ancho varían en función de la imagen, y la profundidad suele ser de 3, que es el número de canales que tiene una imagen RGB (canal rojo, canal verde, canal azul). En la primera línea de código, estamos creando una matriz de 512 de alto, 512 de ancho y 3 de profundo. Además, la estamos rellenando entera de ceros, lo que en una imagen implica que estamos creando una imagen negra. Si todos los píxeles son 0, entonces no hay color, por lo que toda la imagen es negra. Tenemos por tanto un cuadrado de 512 x 512 pixeles de color negro, que hemos llamado img. 

2. Usamos la función `“line”` de opencv para dibujar una línea en nuestro cuadrado. La línea empieza en el pixel (0,0) - esquina superior izquierda - y acaba en el pixel (511,511) – esquina inferior derecha-. Es de color rojo (255,0,0) y tiene 5 puntos de grosor. 

3. Usamos la función `“rectangle”` de opencv para dibujar un rectángulo que empieza en el pixel (384,0) y acaba en el pixel (510,128), de color verde (0,255,0) y con 3 puntos de grosor. 

4. Usamos la función `“circle”` de opencv para dibujar un círculo cuyo centro está en el pixel (477,63), que tiene 63 pixeles de radio, es de color azul (0,0,255) y está relleno en su interior (-1). 

5. Por último, mostramos la imagen por pantalla gracias a una librería llamada pyplot, que trabaja con gráficos e imágenes. Esta será la librería que usaremos en toda la asignatura para mostrar imágenes en los resultados de nuestras celdas en Jupyter Notebook. Veremos que siempre usaremos los mismos comandos para mostrar estas imágenes, que acabarán resultando familiares. 

**IMPORTANTE:** No es necesario comprender esta explicación, ya que el propósito de este código es únicamente comprobar la instalación de OpenCV. Si no has entendido nada, no te preocupes, vamos a analizar con mucho más detalle todas estas funciones – y más – en la siguiente sección. 

56 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **2.2. Imágenes, matrices y color** 

Como ya hemos comentado brevemente, una imagen es una matriz de numerosos elementos elementales denominados píxeles. Cada uno de estos píxeles tiene un valor numérico. Generalmente el valor de este pixel está relacionado con la intensidad del color que debe representar, aunque como veremos hay otras opciones para representar el color. 

Cada pixel es por tanto un conjunto de bits para nuestros computadores, o lo que es lo mismo, una lista de unos y ceros. La cantidad de unos y ceros que tenga el ordenador disponible para representar cada pixel se denomina profundidad de color. 

La mínima profundidad de color que podemos emplear es 1bit, que nos permite únicamente tener dos opciones: uno o cero, o dicho de otra forma, blanco o negro. Estas son las **imágenes binarias** en las que los píxeles solo pueden tomar dos valores para representar visualmente la información. La siguiente es un ejemplo de una imagen **binaria** . Como podemos ver, cada uno de los elementos es blanco o negro, según tome el valor 0 o 1 cada pixel. 



Si aumentamos el número de bits que empleamos en una imagen, podemos aumentar los colores que somos capaces de representar. El siguiente paso es emplear más bits para representar imágenes en escala de grises, o como se conocen formalmente **imágenes monocromáticas** . Para este tipo de imágenes se suelen usar 8 bits, que permiten tener números desde el 0 hasta el 255, como podemos observar en la siguiente tabla. 

|**Decimal**|**Binario (8 bits)**|
|---|---|
|1|00000001|
|2|00000010|
|3|00000011|
|…|…|
|253|11111101|
|254|11111110|
|255|11111111|



57 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Estos 255 valores nos permiten tener el mismo número de colores entre el blanco y el negro, o lo que es lo mismo, una escala de grises. Cuanto más cercano a 0 sea un pixel, menos brillo tendrá, y cuanto más cercano a 255, más brillo. Podemos comprobarlo en la siguiente imagen de ejemplo. Ahora ya no tenemos solo dos valores, sino que con esta nueva gama podemos representar mejor diversas formas y sombras. 



Por último, para conseguir imágenes a color, ya hemos analizado por qué, debido al funcionamiento de la luz de color, necesitamos al menos tres colores primarios con los que poder construir todos los demás. En este caso, el de las **imágenes a color,** cada pixel tendrá tres valores en lugar de uno, uno para cada color. 

El espacio de color más empleado en la actualidad es el RGB, que descompone los colores en rojo, verde y azul. Empleando la misma profundidad de color que las imágenes en escala de grises, es decir, 8 bits, podremos representar imágenes con un total de más de 16 millones de colores gracias al empleo de tres canales distintos. En este caso, cada pixel contendrá, por tanto, la información de la cantidad de rojo, de verde y de azul que tiene entre 0 y 255 cada uno de ellos. Es más sencillo observarlo en un ejemplo. 

Si queremos obtener un rojo puro, querremos saturar este canal de color, y tener el verde y el azul apagados. Esto sería tener 255 de rojo, 0 de azul y 0 de verde. Por tanto, un pixel rojo puro tendría el valor (255,0,0). Lo mismo para verde puro (0,255,0) y para el azul puro (0,0,255). Cualquier otra variación de estos valores produce uno de los más de 16 millones de valores intermedios, como podemos observar en la siguiente imagen. 



58 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En resumen, hemos visto que las imágenes son matrices de píxeles que pueden tener uno o varios canales y una cierta profundidad de color, que no es más que el número de bits que se emplea para representar el mismo. Aunque hay imágenes con mayor profundidad de color, como las imágenes médicas de 16 bits, la gran mayoría de imágenes con las que trabajaremos serán una de las siguientes: 

- a. **Imagen binaria:** Un canal y un bit. Blanco o negro. 

- b. **Imagen monocromática:** Un canal y 8 bits (255 posibilidades). Escala de grises. 

- c. **Imagen a color:** Tres canales y 8 bits (255 x 255 x 255 posibilidades). Más de 16 millones de colores. 

Los parámetros que tienen las imágenes digitales y que las caracterizan en términos de contenido y codificación son: 

- Alto y ancho de la imagen en pixeles. Indica la resolución de la imagen y por tanto la cantidad de información total que está almacenada en la imagen. 

- Profundidad del color (bits per pixel, bpp) 

- Espacio de color empleado (RGB, HSV, YCbCr, CIELAB…) 

- Resolución espacial para impresión, medida en pixeles por pulgada o dpis. No es relevante para trabajar en visión artificial, ya que solo se emplea en imprentas para comprender el tamaño real que tiene una imagen en relación a su tamaño en píxeles. 

Las imágenes digitales pueden estar almacenadas en distintos tipos de archivos según la compresión a la que hayan sido sometidas para limitar el espacio que ocupan. Esta compresión se hace reduciendo el número de colores codificados a aquellos que aparecen en la imagen (¿por qué tener 16 millones de colores posibles si la imagen que deseamos almacenar solo tiene 125?). Esta compresión puede suponer que, en imágenes con colores muy variados, se pierda información de colores muy parecidos para ahorrar espacio. 

Imágenes sin comprimir 

- RAW. Es el formato con el que capturan imágenes las cámaras digitales. No tiene ningún tipo de compresión, lo que implica que las imágenes ocupan más que en ningún otro método. Por desgracia, este formato no está estandarizado y cada fabricante tiene su propia versión, por lo que no es un formato con el que se trabaje en aplicaciones industriales o comerciales. 

59 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- BMP. Este formato sin compresión de Microsoft permite almacenar la información sin comprimir de cualquier imagen de forma estandarizada. El gran inconveniente es la gran cantidad de espacio que usan estas imágenes sin comprimir, lo que será un problema para el cómputo de nuestros algoritmos de visión artificial. 

- Otros, como PPM, PSP, PSD, PBM… Son formatos específicos de programas de edición y retoque fotográfico como Photoshop. 

#### Imágenes con comprensión 

La compresión sin pérdida genera una imagen idéntica a la original una vez descomprimida, por lo que son métodos ideales para ahorrar espacio sin perder calidad de imagen. Sin embargo, estos métodos tienen una limitación de colores a partir de la cual se empiezan a generar pérdidas, por lo que es relevante tener en cuenta las limitaciones de cada tipo de archivo a la hora de trabajar con él. 

- PNG. De las siglas _Portable Network Graphics_ es un formato que nos permite mantener los mismos 16 millones de colores una vez descomprimida la imagen, por lo que esta no pierde calidad. Además, añade un cuarto canal al formato RGB para permitir indicar transparencias, por lo que pueden llegar a ser imágenes muy pesadas. 

- JPG. Este formato estándar así llamado por las siglas de _Joint Photographic Experts Group_ realiza una gran compresión. Convierte el conjunto de pixeles de la imagen en una serie de bloques para componer un mosaico, que a la hora de descomprimirse puede mostrar pérdidas de calidad. 

- TIFF. Este formato con una baja compresión fue diseñado para almacenar los artes finales previos a la impresión de diversos elementos gráficos, y tiene como gran ventaja la capacidad de almacenar capas. Es ampliamente usado en el mundo del diseño gráfico y de la impresión, pero no así en la captura de imagen y video digital orientados a sistemas de visión artificial. 

- GIF: Este formato de imagen ofrece 256 colores, o lo que es lo mismo, trata de comprimir los tres canales RGB en un solo canal de 8 bits. En caso de que la imagen tenga menos de 256 colores, la calidad de esa no se verá afectada. En caso contrario, perderemos información que puede ser muy valiosa. Este formato es tan usado en animaciones porque el color es menos relevante en ellas, y permite almacenar todos los fotogramas necesarios en un formato de archivo muy poco pesado. 

Ya hemos comprendido que las imágenes son matrices de píxeles que representan la intensidad luminosa con un valor numérico. Estas matrices, que se almacenan en una gran variedad de tipos de archivos con y sin compresión, tienen entre sus propiedades más destacadas un determinado ancho, alto, profundidad de color, número de canales y espacio de color principalmente. 

60 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Solo hemos mencionado el espacio de color denominado RGB, pero existen otros que es interesante conocer. 

El espacio RGB emplea tres canales para definir cada uno de los colores primarios de luz. Pero hay más formas de emplear todos estos bits disponibles en cada pixel – en concreto 8 bits x 3 canales o lo que es lo mismo, 24 bits. En función del tipo de problema al que nos enfrentemos será mejor definir los colores en base a otros valores. En esta asignatura trabajaremos con otros dos espacios de color: HSV y CIELAB. 

### **2.2.1. Espacio de color HSV** 

HSV responde a las siglas de Hue, Saturation Value. Esto quiere decir que los 3 canales de una imagen pasan de ser la R, la G y la B, a ser la H, la S y la V. 

Este espacio de color surgió como alternativa al RGB debido a su mayor cercanía a cómo el ser humano percibe los colores, ya que nuestro cerebro no solo procesa tres canales de color, sino que reacciona intensamente ante la saturación y el brillo de los colores. 

El valor hue ( **H** ), es el responsable del código de color que observamos. Este color se representa como una porción de 1 grado dentro de un círculo de 360 grados, por lo que hay 360 posibles valores de **H** y por tanto 360 posibles valores de color, que se distribuyen de la siguiente forma: 

- Los rojos se encuentran entre 0 y 60 grados 

- Los amarillos se encuentran entre 61 y 120 grados 

- Los verdes se sitúan entre 121 y 180 grados 

- Los cianes están entre 181 y 240 grados 

- Los azules están entre 241 y 300 grados 

- Y, por último, los colores con tonos magenta están situados entre 301 y 360 grados 

Por otro lado, nos encontramos con el valor de la saturación ( **S** ). Este valor indica la cantidad de gris que contiene un determinado color, una vez conocido su valor **H** . Se mide en porcentaje, por lo que varía desde 0 hasta 100. Si la saturación es del 100%, no hay absolutamente nada de gris y el color es puro. Por otro lado, a medida que la saturación se desplaza hacia el 0% nos encontramos con un color con mayor componente de gris hasta que se convierte en gris puro en el 0%. 

61 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por último, tenemos el “valor” ( **V** ), que es la intensidad con la que se presenta el color. El valor también varía entre 0 y 100, y se mide en porcentaje. Cuando el valor es del 0% se considera que no hay cantidad alguna del color que marca **H** y, por tanto, tendremos negro. Cuando el valor es del 100% hay una cantidad máxima de color **H** y tendremos el color más intenso de todos. 

Para representar la relación entre estos tres valores se suele emplear una representación tridimensional como la siguiente figura. En esta representación, vemos como la **H** determina el sector del círculo en el que nos encontramos (es decir, el color), la **S** determina lo cerca o lejos que nos encontramos del centro del círculo, y la **V** determina la intensidad del color, es decir, la altura a la que nos encontramos. HSV es, por tanto, un espacio de color cilíndrico ya que nos movemos por una superficie tridimensional cuya base es el círculo de los posibles valores de **H** . 

Otra versión con la misma perspectiva es el espacio de color HSL, que en vez de trabajar con el valor del color ( **V** ), trabaja con la luminosidad ( **L** ). En este caso, cuando L es del 100% el color es totalmente blanco, ya que la luz es total. Sin embargo, al 0% encontraremos el mismo comportamiento que en HSV, ya que en ausencia de luz todos los colores son negro. Ambos se emplean ampliamente en visión artificial, por la capacidad de representación del color cercana a la percepción humana que nos ofrecen, simplificando ciertas tareas de preprocesamiento de imágenes y de tratamiento del color, como veremos más adelante. 

En la imagen podemos también comparar los espacios HSV (en vertical las opciones varían desde el color puro hasta el negro) y HSL (en vertical pasamos de blanco a negro, pasando por el color puro en el medio). 



A la izquierda podemos observar el cilindro de HSL y a la derecha el de HSV 

62 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

#### **Ejemplo de uso de HSV en visión artificial** 

En ocasiones, en visión artificial segmentamos objetos tan solo por su color. Imaginemos que queremos detectar posibles enfermedades en las hojas de las plantas que previamente hemos sido capaces de identificar en ejemplos anteriores. 

La enfermedad que nos ocupa es un hongo denominado roya, que produce una especie de erupción en la planta, con puntos de color naranja. Debido a su característico color, deberíamos ser capaces de emplearlo para detectar si una hoja tiene este hongo o no. 

Sin embargo, la naturaleza no es perfecta, y el tipo de naranja que muestra este hongo no es un código RGB exacto con un naranja concreto. Por el contrario, este color suele variar, por lo que lo más recomendable sería usar un rango de color para detectar este naranja. 

No obstante, tenemos otro problema. La iluminación de este tipo de color también varía enormemente, por lo que no será suficiente con seleccionar un rango de naranjas ya que el aspecto de este color variará según la luz. 

Habitualmente, este problema se resuelve recurriendo a un espacio de color alternativo HSV o HSL. Esto es debido a que podemos aislar los códigos de color (el hue en la **H** ) de la saturación e iluminación que se encuentran en los canales **S** y **V/L** , a diferencia del espacio de color RGB. 

Si somos capaces de buscar aquellos píxeles con un hue dentro de un rango naranja, podríamos llegar a detectar automáticamente la roya gracias a sus puntos naranjas, y resolver el problema. 

Recordemos que **no es obligatorio ejecutar estos ejemplos** , por lo que es posible sencillamente leerlos para comprenderlos. 

En caso de desear ejecutarlo para sacar el máximo provecho, lo primero que vamos a hacer es descargar una imagen de una hoja enferma de Roya en este enlace: 

<u>https://www.massogarden.com/images/enfermedades-plagas/roya.jpg</u> 

y la vamos a almacenar en nuestro computador, en una ruta conocida. Podemos guardarla con click derecho  Guardar imagen como…  Guardar 

Ahora, vamos a abrir Anaconda Navigator, y vamos a iniciar la aplicación de Jupyter Notebook. Crearemos un nuevo “notebook” de Python 3 mediante el botón “New”, al que daremos un nombre reconocible, por ejemplo “Roya detection”. 

63 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En la primera celda, que Jupyter Notebook crea automáticamente para nosotros, copiaremos el código del siguiente bloque de código de Python. 

**IMPORTANTE:** Es **esencial que cambiemos la ruta de la imagen** que se encuentra tras la variable `path_to_image` en el código por la ruta de nuestro equipo en la que nos hayamos descargado la imagen. Esta ruta no es más que la ubicación del archivo en nuestro equipo, en la que se indican el disco y las carpetas que hay que recorrer para encontrarlo. Por ejemplo, `'C:/Users/Juan/Desktop/roya.jpg'` sería la ruta de nuestra imagen en el caso de que un usuario llamado Juan la haya guardado en su escritorio. O bien `'C:/Users/Rosa/Downloads/roya.jpg'` , si el usuario llamado Rosa ha guardado esta imagen en su carpeta de Descargas. Cualquier carpeta es válida, sencillamente tenemos que asegurarnos de que le indicamos a nuestro script la ubicación correcta de nuestra imagen. 

La ruta completa la podemos consultar en Windows directamente haciendo click derecho sobre la imagen que acabamos de descargar en el propio navegador de archivos de Windows - es decir, en la carpeta en la que se encuentra el archivo - y seleccionando “Copiar como ruta de acceso”. 



Esto guardará en nuestro portapapeles la ruta completa de nuestro archivo, por lo que si hacemos Ctrl+V en nuestra celda, tendremos la ruta pegada en el código. 

**IMPORTANTE: Windows tiene un gran problema que debemos solucionar.** Para separar las carpetas dentro de las rutas, Windows usa las barras mirando hacia la derecha “\”, mientras que Python necesita trabajar con barras mirando a la izquierda “/”. Por tanto, tendremos que asegurarnos de que cambiamos las barras de las rutas. 

Si al pegar la ruta vemos que tenemos una ruta similar a esta `'C:\Users\Pedro\ Images\roya.jpg'` , tendremos que cambiar las barras de sentido, de tal forma que la separación sea esta “/” para que el script funcione. Esto es esencial y pasará en **todos los ejemplos de la asignatura.** 

64 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

El código que debemos incorporar en nuestra celda es el siguiente: 



El resultado de esta ejecución, que realizaremos pulsando el botón “Run” o el atajo de teclado correspondiente Ctrl+ENTER, debería ser el que vemos en la siguiente imagen adjunta. En caso de no conseguirlo, asegurarse de que la variable `“path_to_image”` ha sido correctamente rellenada con la dirección en la que hemos descargado la imagen “roya.jpg” del enlace anterior y que las barras son estas “/” y no estas “\”. 

Es importante recalcar dos aspectos de OpenCV y su tratamiento de los espacios de color. Por un lado, por una cuestión histórica OpenCV abre las imágenes por defecto en BGR en lugar de en RGB, por lo que lo primero que haremos para poder observar correctamente nuestra imagen es convertir el espacio de color de BGR a RGB, cosa que hacemos gracias a la función cvtColor, que será la que posteriormente usaremos para convertir nuestra imagen al espacio de color definitivo, que será HSV. 

Por otro lado, es importante recordar que, si bien hemos mencionado que los valores de S y de V se daban en porcentaje, OpenCV aprovecha las 255 posibilidades de los 8 bits de cada canal, y las expresa en un número entre 0 y 255, por lo que S = 0 es una saturación del 0%, S = 255 es una saturación del 100%, y así con cualquier valor intermedio que podamos encontrarnos. 

65 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Ahora, crearemos una nueva celda empleando el botón para ello. En esta segunda celda, pegaremos el código que se incluye más abajo, que convierte nuestra imagen a HSV, define los rangos deseados de naranja, y ejecuta el cribado. Estos rangos se han definido previamente por prueba y error, y se ofrecen ya calculados para simplificar la ejecución de este _snippet_ por parte del alumnado. 



Para ejecutar esta segunda celda nos aseguraremos de que el cursor está colocado dentro de esta segunda celda, y de nuevo haremos click sobre el botón “Run” para ejecutar el código de Python que acabamos de pegar. 

El resultado de esta ejecución serán dos imágenes. La primera es la denominada máscara, o “mask”. En ella, vemos señalados en amarillo sobre morado aquellos píxeles que tenían un color dentro del rango de naranja que hemos definido. 

66 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En la segunda imagen, hemos seleccionado estos píxeles en la imagen original para ver las Roya segmentada en base al color. 



Podemos probar con otra imagen de una hoja enferma por otra infección, como es el Oídio. Este hongo se presenta como manchas blancas en la hoja, por lo que no deberíamos encontrar valores de color cercanos al naranja, y por tanto podríamos concluir que la hoja no tiene Roya. Por supuesto, este ejemplo es solo a efectos de comprender las ventajas de HSV, y este problema se resolvería por métodos más precisos y robustos en una aplicación industrial. 

El resultado de procesar la hoja con oídio de este enlace: 

<u>https://www.massogarden.com/es/plagas-y-enfermedades/enfermedades/cenizo-oidio-mal-blanco-blanquilla</u> 

Debería ser similar al siguiente, en el que no hemos encontrado rastros de naranja característico de la Roya.  Para volver a procesar pulsaremos el botón “Run” de nuevo sobre ambas celdas. Primero, colocamos el cursor dentro de la primera celda y pulsamos “Run”. Después, colocamos el cursor en la segunda celda y pulsamos “Run”. 

**Es importante que ejecutemos la segunda celda DESPUÉS de ejecutar la primera. En caso de hacerlo en distintos momentos, PRIMERO EJECUTAR LA CELDA 1, y posteriormente la celda 2** , ya que comparten variables que de otra forma no serán accesibles y obtendremos un error al ejecutar. 

67 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



### **2.2.2. Espacio de color CIELAB** 

Este espacio de color será el último de los que analizaremos y trabajaremos en esta asignatura. LAB surge en 1940 de mano de Richard Hunter, tratando de emular la percepción humana del color. Fue el organismo CIE (Comisión Internacional de la Iluminación) quien lo reeditó treinta años más tarde y por el que recibe la denominación de CIELAB. 

Este espacio de color, como todos los demás, está compuesto por tres canales: L, A y B. Está diseñado para poder representar todos y cada uno de los colores que es capaz de percibir el ojo humano con la menor superposición posible. Los componentes de este espacio son los siguientes: 

- **L,** Lightness. La luminosidad se representa con valores entre el 0 (sin luz, o negro absoluto) y 100 (la mayor luz disponible, es decir, blanco puro) 

- **a,** es el valor de rojo/verde. Este valor va de -128 hasta 127 (para completar los 255 posibles valores). Los valores negativos de **a** indican tonos verdes y los valores positivos indican tonos rojos. 

- **b,** es el valor de azul/amarillo. Se comporta igual que el canal **a** , siendo los valores negativos colores azules y los valores positivos colores amarillos. 

De esta forma, se interpreta que cualquier color perceptible por el ser humano puede ser representado por una combinación de **L** (0, 100), **a** (-128, 127), y **b** (-128, 127). 

68 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Este espacio de color se representa habitualmente como una esfera frente a los cilindros de HSV y HSL, como se puede comprobar en esta figura. 



La esfera de CIELAB, en la que la luminosidad es el eje vertical Y, la A es el eje horizontal X y la B es el eje horizontal Z 

Como resumen acerca de los espacios de color, podemos considerar que cada uno de ellos trata de aproximar la representación de color con un objetivo específico. 

- RGB está basado en los colores primarios de la luz y es fácilmente computable, por lo que se emplea ampliamente en visión artificial. Una de sus mayores limitaciones es que representa menos colores del total que puede percibir un ser humano, lo que en ocasiones puede ser una limitación 

- HSV y CIELAB son espacios de color menos intuitivos, que tratan de aproximarse a la percepción real del color. Esta percepción se ve influida por la cantidad de luz en el entorno, el material de los objetos, características de las células de cada ojo y características neuronales de procesamiento del color. Para tratar de encontrar sistemas objetivos de representación de color y medir distancias entre colores independientemente del observador, surgen estos espacios de color que incluyen aspectos como la cantidad de color ( **L** ) o la saturación ( **S** ) de tal forma que no solo sean los componentes primarios de la luz los que caractericen un color. 

Como hemos podido comprobar, habrá situaciones en las que estos espacios de color alternativos ayuden a resolver un problema concreto de visión artificial. 

69 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **2.3. Representación y transformaciones de imágenes** 

Ahora que hemos estudiado qué es una imagen digital y sus características como la profundidad de color, el tamaño, o el espacio de color; ha llegado el momento de comenzar a aplicar operaciones sobre estas imágenes para realizar preprocesados y búsqueda de características, dos de los pasos más importantes en un sistema de visión artificial. 

El primer aspecto que analizaremos es la representación de las imágenes en formatos que puedan aumentar nuestro conocimiento al respecto de las mismas. Si bien las imágenes están compuestas por matrices de píxeles, hay una serie de operaciones matemáticas y estadísticas que podemos hacer sobre estas matrices para sencillamente representarlas de una forma distinta, que nos permitan comprender mejor estas imágenes, trabajar con ellas, e incluso encontrar objetos de interés que puedan contener. Los cambios de representación se basan en mostrar la misma imagen de una forma distinta, sin manipular su contenido, los valores de los píxeles, el espacio de color ni ninguna característica. 

### **2.3.1. Representación de imágenes** 

#### **Histograma de intensidades** 

El histograma de intensidades de una imagen es un descriptor de la frecuencia con la que se da cada uno de los posibles valores de nivel de intensidad en una imagen. 

Un histograma, no limitado al entorno de la visión artificial, es un tipo de gráfico que se emplea en numerosas disciplinas para representar y visualizar frecuencias en cualquier tipo de dominio. Por ejemplo, podemos querer tratar de estudiar la frecuencia con la que una persona ha nacido en una determinada década en una clase grupal en la Universidad. Para hacer esto, preguntamos a cada miembro de la clase la década en la que ha nacido. Cada vez que una persona nos indica ha nacido en una década determinada, se suma uno a la frecuencia acumulada de esta década. Cuando tenemos todas las frecuencias, las ponemos en un gráfico de barras en el que el eje vertical es la frecuencia acumulada (cuántos alumnos) y el eje horizontal la década de nacimiento. En definitiva, construiríamos un gráfico como el siguiente. 



70 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Podemos realizar este mismo ejercicio con los valores de los píxeles de una imagen, en lugar de preguntarle a cada alumno la década en la que nació, le preguntaremos a cada píxel qué intensidad tiene (o lo que es lo mismo, su valor numérico). 

Partamos de una imagen monocromática, es decir, en escala de grises. En este tipo de imagen los pixeles representan directamente la intensidad de la luz, sin tener en cuenta el color. Por tanto, un histograma de una imagen monocromática se construirá contando cuantas veces se da cada uno de los valores entre 0 y 255 en cada pixel de la imagen. Cada vez que un pixel tiene una intensidad dada, sumaremos uno a la frecuencia acumulada de esta intensidad. En una imagen de 2Mpx tenemos 2 millones de píxeles. Por tanto, en cada uno de ellos analizaremos su valor, y sumaremos uno a la frecuencia de la intensidad que tenga. La suma de todas las frecuencias acumuladas será de 2 millones, ya que solo tenemos en cuenta una vez a cada píxel. 

Este proceso de generación de un histograma puede ayudarnos a caracterizar automáticamente los tipos de imagen sin necesidad de mirarlas manualmente, ya que la distribución de la intensidad de la luz da mucha información. Por ejemplo, podemos emplear el histograma para diferenciar imágenes oscuras o con fondo negro, de imágenes muy claras o con fondo blanco de forma automática. Esto podría ayudarnos a generar automáticamente una carpeta de fotografías tomadas por la noche, y otra con fotografías tomadas durante el día. Para poner en práctica la ejecución de un histograma, y ver el resultado que produce en una imagen real, vamos a crear un Jupyter Notebook que nos ayudará a poner en práctica la extracción y visualización del histograma de una imagen. 

**Como siempre, recordemos que no es obligatorio realizar estos pasos, aunque sí recomendable. En caso de no desear ejecutar los ejemplos, es interesante al menos leerlos y tratar de comprenderlos ya que en todos los casos complementarán a la parte meramente teórica de todas las secciones de esta asignatura.** 

Para leer una imagen, extraer su histograma y mostrarlo usaremos tres funciones que se explican a continuación: 

- cv.imread(filename, flags) . Esta es la función de OpenCV para abrir imágenes. La usaremos en prácticamente todos los ejemplos de esta unidad. Ya la hemos empleado en ejemplos anteriores. Necesita una ruta de acceso y permite añadir opciones de configuración en el parámetro “flags”. 

- `plt.hist(x, bins, range)` , que calcula el histograma de una lista de datos “x”, con un número de divisiones verticales “bins” dentro de un rango “range”. Para poder usarla, tendremos que convertir una imagen – que es una matriz de ancho x alto – en una lista de datos. 

- `np.ravel()` , que “aplana” la matriz de la imagen para convertirla en una lista plana de pixeles. Es decir, una matriz de altura 1, como vemos en esta imagen de ejemplo. 

71 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



#### **Ejemplo de histograma monocromático** 

Primero vamos a descargar una imagen de ejemplo de la librería OpenCV, que son imágenes libres de derechos y pensadas para ejemplos de visión artificial, para trabajar con ella. Se encuentra en este link. 

#### <u>https://github.com/opencv/opencv/blob/master/samples/data/home.jpg</u> 

Podemos guardarla directamente desde nuestro navegador de preferencia con click derecho  Guardar imagen como…  Guardar. Seleccionaremos la carpeta que deseemos para posteriormente introducirla como ruta de la imagen. 

Abrimos Anaconda Navigator como otras veces, y lanzamos la aplicación de Jupyter Notebook. Creamos un nuevo Notebook de Python3 con el botón “New”, le damos un nombre representativo, y por último copiamos todo el siguiente fragmento de código en nuestra primera celda que viene creada por defecto en nuestro cuaderno. 

**IMPORTANTE: ecordemos cambiar la ruta de acceso de la imagen por aquella en la que hayamos guardado la imagen descargada, cambiando la orientación de las barras (la correcta es ‘/’), como en el ejemplo anterior.** 

Como podemos comprobar, OpenCV ofrece una opción para abrir imágenes que originalmente están a color directamente convertidas a escala de grises, sencillamente con añadir un 0 después del comando “imread”. Esto nos ayuda a trabajar con cualquier imagen como si se tratara de una imagen monocromática. Ejecutaremos la celda 1 mediante el botón “Run”. 

72 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



El resultado será por tanto la visualización de nuestra imagen “home.jpg” en escala de grises y el histograma asociado. En el eje horizontal de nuestro histograma veremos los distintos valores de nuestros píxeles, que van en un rango desde 0 hasta 255. En el eje vertical veremos cuántos píxeles hay en nuestra imagen que tengan exactamente la intensidad que marca el eje horizontal. 

En este histograma que acabamos de generar, podemos comprobar que la imagen tiene muy pocos valores blancos (0-50) ya que las barras de frecuencia son realmente bajas en comparación con el resto de las barras de frecuencias. 

No tendremos casi ningún valor negro (<225) ya que directamente no hay barras de frecuencia para estas intensidades. 

Tenemos sin embargo una gran cantidad de pixeles de una intensidad media (casi 4000 píxeles con una intensidad de en torno a 110), representada en nuestra imagen por los valores intermedios de gris, y por tanto la imagen es una imagen bien iluminada y contrastada. Desde luego, no es una imagen oscura ya que a partir de 200 prácticamente no encontramos píxeles, lo que quiere decir que hay escasez de píxeles oscuros. Es, por tanto, una imagen que probablemente haya sido tomada de día, o al menos con una muy buena iluminación. 



73 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

También podemos calcular histogramas de imágenes a color, que nos permiten conocer con más detalle la distribución de colores de una imagen y realizar segmentaciones de determinados objetos. En este caso lo que analizaremos será la intensidad de la luz de cada uno de los colores. Recordemos que solo con luz roja, verde y azul se puede generar cualquier color de luz con cualquier intensidad, y que por esto existe el espacio de color de RGB. 

El histograma de una imagen a color RGB con tres canales no es más que tres histogramas superpuestos, uno para cada canal de la imagen, como ya hemos hecho para el único canal monocromático de nuestra imagen. 

Podemos verlo en el siguiente ejemplo, en el que reutilizaremos la misma imagen y una lógica muy similar, pero en este caso calcularemos un histograma por cada color, en lugar de abrir la imagen directamente como escala de grises. 

#### **Ejemplo de histograma a color** 

Creamos una segunda celda en el mismo Jupyter Notebook del ejemplo anterior, haciendo click sobre el botón “+”, y pegamos en ella el siguiente _snippet_ de código. 

NOTA: Desde un punto de vista de optimización y las buenas prácticas este código es a todas luces incorrecto, ya que debería haberse resuelto mediante un bucle `for` para recorrer los tres canales de la imagen y no repetir comandos iguales en Python para pasar por el canal 0, 1 y 2. Sin embargo, a efectos explicativos, se ha decidido reutilizar código para este ejemplo, ya que se evita la abstracción de un bucle for y la complejidad que puede introducir para alumnos sin experiencia en programación. 

Ejecutamos esta segunda celda con el botón “Run” y deberíamos ver el resultado inmediatamente. 

**IMPORTANTE: Es esencial que ejecutemos la segunda celda DESPUÉS de ejecutar la primera. En caso de probar estos dos ejemplos en distintos momentos, al volver a abrir nuestro Jupyter Notebook deberemos recordar PRIMERO EJECUTAR LA CELDA 1 que copiamos en el ejemplo anterior, y posteriormente la celda 2** , ya que comparten variables que de otra forma no serán accesibles y obtendremos un error al ejecutar. 

74 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



En el resultado podemos observar que la gran mayoría de píxeles tienen intensidades de rojo muy bajas (las frecuencias rojas son la mayoría muy cercanas a 0, lo que significa que hay poco rojo en nuestra imagen), esto indica colores suaves predominantes como naranjas. 

En el caso del color verde, la gran mayoría de píxeles muestran intensidades intermedias, de entre 75 y 150, que son los que sirven para construir colores como los marrones y los amarillos que podemos observar en la imagen. 

Por último, el color azul es predominantemente intenso (los picos de frecuencia son notables en el entorno cercano a 180) lo que podría indicarnos sin mirar a la imagen que o bien hay gran cantidad de cielo, o una gran masa de agua. 

Este tipo de información nos ayuda a comprender mejor la distribución e intensidad de color de nuestra imagen, sobre todo si lo comparamos con el ejemplo de histograma en escala de grises, en el que solo éramos capaces de percibir si la imagen es más luminosa u oscura, sin ningún tipo de información de color. 

75 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



En definitiva, un histograma es un modo de representar una imagen que nos permite ver la intensidad de sus valores – y por tanto colores – en forma de gráfico, lo que puede aportar mucha información de cara a una futura búsqueda de características, y es una herramienta básica para todo análisis de imágenes. Es útil para medir propiedades de la imagen como promedios, brillos, contrastes, distribución y entropía, varianza… 

Por último, es interesante mencionar que en ocasiones en lugar de representar el histograma de una imagen RGB en forma de la superposición de tres histogramas de dos dimensiones diferentes, se representa como un cubo tridimensional en el que se observan en cada dimensión los histogramas de cada canal. Si bien ayuda a la visualización de los datos en algunos casos, no aporta información nueva desde el punto de vista matemático, ya que el resultado del conteo de frecuencias es exactamente el mismo. Para construir este tipo de histogramas, habitualmente se emplean programas como “Color Inspector”, que produce resultados como el que podemos observar a continuación. 



76 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **2.3.2. Transformación de imágenes** 

En ocasiones, como ya hemos comentado, será necesario manipular las imágenes que entran en un sistema de visión artificial para facilitar la tarea del algoritmo principal. Estas operaciones pueden perseguir una eliminación del ruido, un aumento de la nitidez, manipulación del brillo y del contraste, una ecualización del histograma o un adelgazamiento de líneas y bordes, entre otros. 

Para todos estos objetivos, ejecutaremos operaciones de transformación, de las que encontraremos dos tipos: 

- a. **Transformaciones en intensidad:** Este tipo de transformaciones se aplican a las imágenes para manipular el contraste y el gamma de la imagen. 

- b. **Transformaciones geométricas:** Estas transformaciones modifican la relación espacial entre los distintos píxeles de la imagen. Deformando, rotando o comprimiendo ciertas zonas de la imagen, obtendremos imágenes transformadas desde las originales. 

Todos estos tipos de transformación entran dentro de los procesos de preprocesado de imagen. 



Las transformaciones de imágenes se enmarcan dentro del **preprocesado de imagen** . A continuación, trataremos de extraer características gracias a técnicas clásicas de visión artificial. 

#### **Transformaciones en intensidad** 

Emplearemos transformaciones de intensidad cuando deseemos mejorar la calidad de los objetos negros o con sombras, mejorar los brillos y destellos que puedan tener nuestras imágenes capturadas, o intercambiar negros y blancos de forma automatizada, por ejemplo. Este tipo de transformaciones son las que realizan los softwares de edición fotográfica cuando manipulamos el contraste, el brillo y el gamma, entre otros procesos que permiten realizar. En esta sección aprenderemos la lógica detrás de estas manipulaciones, las pondremos en práctica y trataremos de comprender sus posibles aplicaciones. 

77 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Un ejemplo de la utilidad de las transformaciones de intensidad podemos observarlo en la siguiente fotografía, en la que podemos observar que en la imagen original la chaqueta del hombre es totalmente negra, mientras que tras una transformación de la intensidad podemos observar detalles como los botones o bolsillos, mejorando así las posibilidades de detectar dichos elementos. 



A la izquierda podemos observar la imagen original, mientras que a la derecha se ha aplicado una transformación de la intensidad para mejorar el contraste de los elementos de la chaqueta 

#### 1. Negativos 

La transformación de intensidad más sencilla es la generación del negativo de una imagen. Para hacer esto, trabajaremos con imágenes en escala de grises. La idea básica es que los máximos se convierten en mínimos y viceversa. Esto quiere decir que el blanco puro pasa a ser negro puro, y de igual manera en sentido contrario el negro puro pasa a ser blanco puro. Todos los valores intermedios buscarán su valor opuesto, por lo que el gris claro se convertirá en gris oscuro, y el único que no se modificará será el valor exactamente intermedio ya que su opuesto es él mismo. 

En OpenCV conseguiremos este efecto mediante la función `cv2.bitwise_not(img):` Que niega todos los pixeles para obtener su valor opuesto. Veremos el resultado en el ejemplo final de esta sección. 

#### 2. Corrección de gamma 

La corrección de gamma es un proceso complejo que emplea operaciones no lineales, en cuya definición matemática no entraremos. Sin embargo, es interesante saber que este proceso se realiza para tratar de mostrar la mayor cantidad de información posible en una imagen teniendo en cuenta las características específicas de la visión humano en cuanto a la percepción del color y de la luz. Si no aplicamos corrección gamma, estaremos “malgastando” los píxeles más brillantes y más oscuros de la imagen, en los que el ser humano no percibe nada, mientras que podríamos maximizar la información almacenada en los valores intermedios de intensidad. 

78 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Es un proceso esencial a la hora de mostrar imágenes por pantalla, pero en ocasiones también puede ayudar a resaltar determinados elementos de una fotografía para un sistema de visión artificial. Gamma es un parámetro que puede tomar valores positivos, y modificará la intensidad de los pixeles según su valor. 

Si seleccionamos un valor gamma < 1 veremos como aumenta digitalmente la exposición, y la imagen se acerca a estar “quemada”. Por el contrario, si seleccionar un valor de gamma > 1 percibiremos la imagen algo más oscura y contrastada. De nuevo, veremos la corrección de gamma en acción en el ejemplo de código con OpenCV posterior. 

Habitualmente esta transformación nos ayudará a trabajar con imágenes que no tienen la exposición correcta, y que por ello no se observan correctamente ciertos detalles que pueden llegar a ser de interés para nuestro algoritmo de visión artificial. 

#### 3. Mejora del contraste 

De igual forma que las correcciones de gamma nos permiten mejorar visualmente una imagen para percibir más detalles en ella, la mejora automática del contraste de una imagen puede ser un gran aliado para este objetivo. Nos encontraremos diversos métodos automáticos en visión artificial, entre los que nos centraremos en tres. 

- Ecualización del histograma 

Este método permite mejorar el contraste de una imagen. En concreto se emplea en imágenes con un rango estrecho de valores de intensidad, es decir, con poca variación de intensidad entre sus píxeles (todos muy claros, o todos muy oscuros). Esto implica que hay muchos valores posibles en cada pixel que jamás son usados, y por tanto se está “desperdiciando” espacio de almacenamiento de información y, por ende, visual. 

La ecualización del histograma consigue distribuir de forma homogénea la intensidad preexistente de los píxeles para aprovechar al máximo el rango de 8 bits (0-255) que tienen las imágenes digitales. Esto permite que las zonas con menor contraste mejoren, y sus detalles se observen mejor. Es decir, si todos los píxeles tienen valores entre 0 y 20, tenemos 235 valores sin usar que podrían ayudarnos a distinguir mejor los detalles de la imagen. 

Si movemos estos valores para que en lugar de entre 0 y 20 ocupen todo el rango de 255, las diferencias de intensidad se verán mucho más claramente y esto ayudará a la capacidad de procesado de un algoritmo de visión artificial sobre esta foto. Recordemos que todas estas técnicas se enmarcan dentro de la categoría de preprocesado de la imagen. 

79 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Como siempre, es más sencillo observar este método de ajuste de contraste con una serie de imágenes y sus histogramas. En la primera imagen vemos una imagen en escala de grises de un paisaje junto a su histograma. Como podemos comprobar, solo hay píxeles con valores de intensidad entre 100 y 200 (en rojo), y el acumulado de píxeles (en negro) total pasa del 0% al 100% en un espacio muy pequeño. Esto implica que estamos desaprovechando todos los píxeles entre 0 y 100, y entre 200 y 255 a la hora de mostrar información y por tanto habrá un contraste realmente malo en nuestra imagen, como efectivamente podemos comprobar. 



Si a esta imagen le aplicamos un proceso de ecualización del histograma, podemos lograr utilizar todos los valores disponibles para cada pixel, amplificando las diferencias entre las zonas de distinta intensidad (claras y oscuras). Como vemos, el histograma (en rojo) ahora ocupa todo el rango de valores, y el acumulado de píxeles sube de forma totalmente lineal y escalada. Como consecuencia, observaremos una gran mejora en el contraste y visualización de la imagen, que es a fin de cuentas nuestro objetivo con esta transformación de intensidad de los píxeles. 



80 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Matemáticamente este método encuentra una equivalencia para cada valor original con el nuevo valor ecualizado, analizando el rango original y trasladándolo al rango deseado. En este caso el rango original era [100,200] y el rango deseado [0,255], por lo que, por ejemplo, la tabla de trasposición sería como sigue: 

|**Valor original**|**Valor ecualizado**|
|---|---|
|100|0|
|150|128|
|200|255|



En ocasiones, la imagen no muestra un histograma comprimido, pero sí que hay regiones específicas en las que esto sucede. Es decir, que hay zonas con intensidades realmente bajas y zonas con intensidades realmente altas, por lo que si aplicamos la ecualización de histograma podríamos incluso estropear aún más la visualización de la imagen. 

Para resolver este problema surge la ecualización del histograma realizada de forma local. 

- Ecualización local del histograma´ 

Con esta transformación de intensidad tratamos de mejorar el contraste a base de ecualizar el histograma de una imagen de forma local. Con este método, dividimos una imagen en una serie de regiones llamadas teselas, o “tiles” en inglés. En cada una de estas regiones ejecutamos la ecualización del histograma, para que el resto de regiones no afecten a su ecualización. Una vez ecualizadas todas las regiones, se aplica un algoritmo de interpolación para evitar bordes artificiales, denominados “artifacts”. De esta forma, conseguimos ecualizar imágenes con zonas muy distintas de luz y oscuridad. Veremos el resultado de aplicar este concepto en un ejemplo de OpenCV más adelante. 

Estas transformaciones de intensidad son las bases de los procesos que se ejecutan en programas de edición de fotografía cuando modificamos los valores “brillo” y “contraste”. 

En visión artificial se emplean a menudo para destacar ciertas _features_ de nuestras imágenes que pueden resultar más difíciles de clasificar, detectar o segmentar con la imagen original, y que gracias a estas modificaciones de gamma y contraste pueden aumentar la precisión de nuestros algoritmos. 

Vamos a comprobar estos tres tipos de transformación de intensidad con OpenCV mediante un ejemplo en nuestro entorno de prueba de Anaconda Navigator y Jupyter Notebook. 

81 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

#### **Ejemplo de negativos** 

El primer operador que usaremos será una función de transformación para generar negativos a partir de una imagen en escala de grises (monocromática). Como hemos dicho, generar un negativo de una imagen pasa por buscar el opuesto de cada uno de sus bits (es decir, negar el valor de cada uno de sus píxeles). 

Para hacer esto, usaremos la función de OpenCV `cv.bitwise_not(image)` que realizará esta operación por nosotros. Por lo demás usaremos en el código las funciones ya vistas para leer imágenes y mostrar imágenes. **Recordemos cambiar la variable “path_to_image” por la ruta local en la que tengamos descargada la misma imagen que en ejemplos anteriores, “home.png” y adecuar las “/” de la misma.** 

Tras lanzar Anaconda Navigator y abrir Jupyter Notebook, crearemos un nuevo Jupyter Notebook de Python3, le cambiaremos el nombre para tenerlo identificado y pegaremos en la primera celda el siguiente _snippe_ t de código. 



Como salida observaremos dos imágenes. Por un lado, tendremos la imagen “home. jpg” leída como escala de grises, porque usamos la opción 0 en la función “ `imread` ”. Esta es la imagen original, de la que en el ejemplo anterior calculamos el histograma. 

A continuación, veremos la imagen que hemos llamado en el código “ `img_not` ”, en la que vemos esta misma imagen en negativo. Veremos como todos los píxeles que eran totalmente negros (las ventanas de la torre) se han convertido en píxeles totalmente blancos, y que los píxeles más claros, como las paredes del edificio o las nubes, ahora son los píxeles más oscuros de esta fotografía. 

82 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



#### **Ejemplo de corrección gamma** 

A continuación, vamos a poner a prueba un ajuste de gamma para comprender visualmente los efectos de esta transformación de intensidad sobre nuestras imágenes. 

Vamos a seleccionar un valor para gamma extremadamente bajo, en concreto emplearemos un gamma de 0.5, para así sobreexponer la imagen exageradamente, y que podamos comprobar a primera vista el efecto que causa esta transformación de intensidad. 

OpenCV no tiene un método predeterminado para realizar un ajuste de gamma, y hay que generar una tabla de búsqueda para poder aplicar este método. En esta tabla se generan las correspondencias entre los valores originales de los píxeles y los valores corregidos a través del valor gamma que deseemos. Nos es necesario comprender el funcionamiento de la creación de esta tabla. 

Es suficiente con comprender que empleando la función de OpenCV 

`cv.LUT(img, lookUpTable)` aplicamos la transformación de intensidad mediante ajuste de gamma en función de la tabla de búsqueda que realicemos. 

Crearemos una nueva celda en nuestro Jupyter Notebook, el mismo que hemos empleado para ejecutar el ejemplo anterior de realización de negativos pulsando sobre el botón “+”. 

El código que deberemos introducir en la **segunda celda** de nuestro Notebook y que debemos ejecutar (botón “Run”), es mostrado a continuación. 

**Es importante que ejecutemos la segunda celda DESPUÉS de ejecutar la primera. En caso de hacerlo en distintos momentos, es necesario PRIMERO EJECUTAR LA CELDA 1, y posteriormente la celda 2** , ya que comparten variables que de otra forma no serán accesibles y obtendremos un error al ejecutar. 

83 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Como salida veremos dos imágenes. Por un lado, la imagen original, almacenada en la variable “color_img”. Por otro lado, el resultado de aplicar una corrección con gamma 0.5, que es la segunda imagen, en la que vemos claramente un exceso de exposición debido a esta transformación de intensidad. 



La búsqueda del valor de gamma es un proceso que puede realizarse de forma manual, gracias a un proceso de prueba y error, o empleando algoritmos de selección automática de gamma como pueden ser la maximización de la varianza, o la minimización de la dispersión, así como aplicando la media de las intensidades. 

84 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

#### **Ejemplo ecualización global y local de histogramas** 

Por último, en este mismo cuaderno de Jupyter Notebook vamos a crear una tercera celda (botón “+”) para comprobar la diferencia entre realizar una ecualización de histograma a nivel global o dividiendo la imagen en regiones. 

Para este ejemplo no vamos a necesitar descargar ninguna imagen, ya que usaremos una imagen de ejemplo que trae una librería que ya tenemos en nuestro entorno, llamada `skimage` . Usaremos una fotografía de la superficie lunar a la que accederemos mediante la función `img_as_ubyte(data.moon())` 

Para la ejecución de la ecualización de histogramas emplearemos dos funciones de OpenCV preparadas a tal efecto: 

- `cv.equalizeHist(img)` Nos permite ecualizar directamente el histograma de cualquier imagen tal y como hemos comentado previamente en los apuntes. 

- `cv.createCLAHE(clipLimit, tileGridSize)` nos permite ecualizar localmente un histograma e indicar dos parámetros. El contraste máximo (que marcaremos en 2.0) y el tamaño de las regiones (que marcaremos en cuadrados de 8 pixeles) 

El código a introducir en la celda y posteriormente ejecutar es el siguiente. Recordemos que tenemos que haber ejecutado previamente las celdas #1 y #2 para que funcione correctamente. 



85 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Veremos que la ecualización global del histograma ofrece resultados muy malos en este tipo de imagen. Esto es porque tiene zonas muy oscuras y zonas muy claras, por lo que no podemos ecualizarla de forma global. 

Sin embargo, gracias a la ecualización local del histograma de la imagen, obtenemos una imagen en la que se aprecian mejor ciertos detalles y texturas, lo que puede ser realmente interesante para un algoritmo de visión artificial a la hora de procesar una imagen que podría ser de este tipo. 

De izquierda a derecha vemos a continuación la imagen original, la ecualización global de la misma, y la ecualización local. 



Con esto concluyen nuestros ejemplos en código de las transformaciones de imágenes en intensidad. 

#### 4. Umbralización ( _thresholding_ ) 

Esta transformación de intensidad es el método más simple existente para segmentar imágenes, es decir, cae ya del lado de la **extracción de características** . Si recordamos la sección inicial de objetivos de la visión artificial, la segmentación consiste en etiquetar cada pixel de una imagen para comprender su tipología. En este caso, hablamos de una segmentación en dos clases: fondo y objeto. 

Hay diversos métodos de umbralización, pero todos comparten la misma lógica. Partiendo de una imagen en escala de grises (es decir, con valores 0-255 de intensidad), seleccionaremos una intensidad umbral ( _threshold_ ). Todos los píxeles que tengan menos intensidad que la elegida serán convertidos a negro puro. Todos los píxeles que tengan más intensidad que la elegida serán convertidos a blanco puro. 

86 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

De esta manera, obtendremos una imagen binaria, ya que solo habrá pixeles negros y pixeles blancos, que estará segmentada (negro = fondo, blanco = objeto de interés). Esto puede dar grandes resultados en aquellas imágenes con un fondo más oscuro y unos objetos en primer plano más brillantes, o viceversa, como puede ser la siguiente imagen, en la que se aplica un umbralizado a la imagen anterior en la que observábamos una persona con una cámara de video. Como podemos observar, tanto el suelo como el cielo han quedado transformados a negro, porque no tenían suficiente intensidad. Sin embargo, tanto la persona, como la cámara, como los edificios, han sido transformados a blanco porque superaban el umbral de intensidad. 



Umbralización de una imagen mediante un _threshold_ dado 

La gran mayoría de métodos de umbralización persiguen automatizar la selección de este valor. Si bien es posible seleccionar a mano la intensidad de umbral, en aras de la automatización han surgido numerosos métodos para seleccionar este valor de forma automática, entre otros, destacan: 

- Umbralizado basado en histograma: En este caso se usa la forma del histograma para decidir la intensidad de umbral. Se trata de emplear puntos críticos como picos o valles para encontrar este punto. 

- Umbralizado global automático: Selecciona el valor medio entre la intensidad máxima y la mínima para seleccionar el umbral de división 

- Umbralizado de Otsu: En este caso se trata de encontrar el valor que minimiza la varianza dentro de una misma clase, o lo que es lo mismo, maximiza la varianza entre la clase 0 y la clase 1. 

- Umbralizado local adaptativo: En este caso cada imagen se divide en pequeñas subregiones para umbralizar cada una de ellas por separado, mejorando el resultado en casos en los que el brillo y el contraste varían mucho entre las distintas regiones de la imagen. 

87 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

El concepto de umbralizado no debe habernos sorprendido demasiado, ya que, aunque sin saberlo, ya lo hemos aplicado en uno de nuestros ejemplos. El ejercicio que realizamos en la sección de espacios de color en que buscábamos los píxeles de un cierto tono de naranja no era sino un ejercicio de umbralizado. En esta ocasión el valor del umbral lo estábamos seleccionando nosotros manualmente, ya que buscábamos diferenciar un color muy específico. 

No obstante, es posible aplicar umbralizado y métodos automáticos de selección de umbral tanto a imágenes en escala de grises como a color, y es una herramienta realmente útil para la **extracción de características** . 

#### **Transformaciones geométricas** 

Las transformaciones geométricas son aquellas que manipulan el espacio existente entre los distintos píxeles de una imagen. En lugar de manipular el valor del pixel – como sucede en las transformaciones de intensidad – en este caso modificamos el lugar que ocupa dicho pixel. Este tipo de transformaciones son menos empleadas en visión artificial ya que en raras ocasiones mejoran las probabilidades de encontrar características relevantes, pero es esencial conocerlas. Veremos todos los ejemplos sobre imágenes, pero en esta sección no incorporaremos ejemplos de código ejecutables. 

Estas modificaciones pueden preservar algunas de las características de los píxeles de la imagen, que pueden ser: 

- **Distancia entre píxeles:** Si las distancias entre píxeles se mantienen, estamos tratando con transformaciones geométricas **rígidas** . Entre ellas encontramos la traslación y la rotación. 

   - Traslación: Desplazamos una serie de píxeles de la imagen a otro lugar, sin alterar la distancia entre ellos. 

   - Rotación: Efectuamos una rotación de la imagen con un ángulo previamente determinado sin ningún tipo de deformación, por lo que mantenemos la distancia entre píxeles, pero no su posición espacial original. 

- **Ángulos entre píxeles:** Hablamos en este caso de transformaciones geométricas **semejantes** . Entre ellas encontramos el escalado. 

   - Escalado: Ampliamos o reducimos una imagen, generando pixeles inexistentes o destruyendo pixeles, pero siempre manteniendo la relación de aspecto original entre ellos. 

88 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- **Afinidad entre píxeles:** Transformaciones geométricas **afines** . En este caso deformamos las imágenes, pero mantenemos la ubicación relativa de las imágenes, por ejemplo, estirándolas o achatándolas. 

   - Escalado en un único eje. En este caso solo modificaremos la escala de uno de los ejes, que puede ser el vertical o el horizontal. Haciendo esto, deformaremos la imagen, pero los píxeles seguirán teniendo los mismos vecinos, es decir, los mismos píxeles encima, debajo, a la derecha y a la izquierda. 

- **Colinealidad entre píxeles:** Transformaciones geométricas **proyectivas** . En este caso cambiamos la perspectiva de la imagen, manteniendo el resto de propiedades de acuerdo con la nueva perspectiva. 

   - Transformación proyectiva: Se emplea una nueva perspectiva para rectificar o deformar imágenes en función de un punto de fuga definido por código. 



Ejemplos visuales de distintas transformaciones geométricas sobre el logo de OpenCV 

Con las transformaciones en intensidad y las transformaciones geométricas hemos visto técnicas de preprocesado de imágenes. Recordemos que estas técnicas se emplean al principio del flujo de un sistema de visión artificial, y que habitualmente se usan para mejorar ciertos aspectos de nuestras imágenes para facilitar el trabajo posterior de extracción de características y aplicación de nuestros objetivos. 

Como hemos visto, las imágenes pueden ser mejor aprovechadas si optimizamos su contraste, su brillo, la diferencia de intensidades de sus píxeles o incluso si cambiamos su tamaño, escala o perspectiva. La última modificación que vamos a estudiar desde el punto de vista de la morfología antes de proseguir a otros tipos de preprocesado serán las operaciones morfológicas. 

89 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **2.3.3. Operaciones morfológicas** 

Las operaciones morfológicas son transformaciones aplicadas a imágenes binarias y monocromáticas (o en escala de grises). Estas operaciones están especialmente diseñadas para ser aplicadas sobre formas y estructuras dentro de estas imágenes. Este tipo de operaciones nos pueden ayudar a hacer objetos más grandes o más pequeños. También podemos usar estas operaciones para aumentar el espacio existente entre objetos, así como para reducirlo. 

Las operaciones morfológicas emplean un elemento estructural, en inglés denominado _structuring element_ para realizar su función. Este elemento define la zona que va a ser analizada alrededor de cada pixel de la imagen de entrada, para aplicar sobre esta zona la operación morfológica deseada. Esta definición es más sencilla de comprender analizando las cuatro operaciones morfológicas más importantes en visión artificial. 

1. **Erosión (erosion)** . Esta operación reduce los objetos a base de “erosionar” sus bordes. Básicamente trata de eliminar todas las zonas de la imagen en la que los píxeles no sean sólidos, o lo que es lo mismo, las zonas en las que hay píxeles negros (0) se convierten automáticamente a negro (0). Para ello, se usa un _structuring element_ con la forma que se desee. Puede ser un cuadrado, un rectángulo, un círculo… Esta forma será nuestra “zona de actuación”, o empleando un símil, nuestra lupa. Moviendo la lupa a lo largo de la imagen de izquierda a derecha y de arriba abajo, podremos ir seleccionando distintas zonas de la imagen. En cada zona de la imagen se transformarán a 0 todos los píxeles si hay algún pixel negro en la zona. Esto sirve para eliminar pequeñas zonas con ruido en la que no hay objetos claramente definidos, así como para reducir los bordes de los objetos. En la siguiente figura podremos observar en el centro el efecto de erosionar una imagen binaria. 

2. **Dilatación (dilate).** Esta operación es la operación contraria a la erosión. La dilatación mueve el _structuring element_ a lo largo de la imagen de igual forma que la erosión. En cada zona procesada se analizará el valor de los píxeles. Si hay algún pixel blanco (1), entonces todos los píxeles se convertirán a blanco. Esto sirve para aumentar el tamaño de los objetos y para detectar objetos pequeños que nuestros algoritmos de visión artificial no son capaces de detectar debido a su tamaño. En la siguiente imagen vemos la comparación entre ejecutar una erosión y una dilatación a la misma imagen. A la izquierda tenemos la imagen original, en el centro el resultado de una erosión y a la derecha el resultado de una apertura. 

Como vemos, la ejecución de la erosión ha disminuido nuestro objeto blanco, convirtiendo a negro (0) todas las zonas que no eran completamente blancas. En la tercera imagen vemos lo contrario. Toda zona con cualquier pixel blanco ha sido convertida íntegramente a blanco, aumentando así los bordes y consecuentemente el tamaño de nuestro objeto. 

90 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



3. **Apertura (open).** Una apertura es una erosión seguida inmediatamente por una dilatación. Generalmente se emplea para reducir el ruido de nuestras imágenes mejorando por tanto el desempeño de nuestros algoritmos, pero manteniendo el tamaño original del objeto (ya que primero quitamos las zonas más pequeñas, pero luego volvemos a hacer grandes aquellas que hemos mantenido). 

4. **Cierre (close).** Es lo contrario de una apertura, por lo que es una dilatación seguida de una erosión. En este caso, se suele emplear para cerrar agujeros en los objetos, reduciendo los pequeños puntos negros en objetos que puedan entorpecer a nuestros algoritmos de visión artificial. 

En la siguiente imagen vemos a la izquierda una apertura y a la derecha un cierre. 



### **2.4. Filtrado: desenfoque, nitidez y suavizado** 

En ocasiones, además de imágenes con valores no óptimos de contraste, brillo o umbral, nos encontraremos imágenes con ruido o con artefactos que pueden empeorar el desempeño de nuestros algoritmos de visión artificial. De igual forma que los ajustes de brillo o contraste, es posible filtrar o suavizar una imagen mediante un programa de edición fotográfica. Sin embargo, esto no sería óptimo en un sistema comercial de visión artificial, ya que todos los pasos deben estar tan automatizados como sea posible, y no podremos permitirnos la necesidad de interactuar con cada imagen por medio de un programa de edición. 

91 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Es por ello que estudiamos tanto las transformaciones como los filtros y suavizados, ya que en la mayoría de las ocasiones son la primera parte de un flujo completo de visión artificial, y debemos conocer su existencia y la posibilidad de automatizarlos por medio de código. Los ejemplos de esta sección estarán contenidos en los ejemplos de siguientes secciones, ya que la aplicación de todos estos filtros pasa por una única línea de código en forma de función predefinida de OpenCV. Los usaremos para preprocesar imágenes en los ejemplos de extracción de características. Por tanto, esta sección es eminentemente teórica, y es esencial para comprender conceptos más complejos como las Redes Neuronales Convolucionales de la siguiente unidad. 

Antes de empezar a discutir los diferentes tipos de filtros y suavizados, es importante que comprendamos el concepto de núcleo de convolución, o como se acostumbra a llamar en inglés, “ _convolution kernel_ ”. Un kernel es una matriz de dos dimensiones que se usa para filtrar imágenes. Se puede llamar también matriz de convolución, y habitualmente es una matriz cuadrada de M x N, como por ejemplo una matriz de 3x3 que podemos ver en la siguiente imagen. 



Estos kernels se usan para aplicar distintas operaciones matemáticas sobre la imagen para obtener un determinado efecto deseado (desenfoque, suavizado, aumento de nitidez…). Para usarlos, se realiza una operación **esencial** para una gran mayoría de técnicas de visión artificial llamada **convolución** . Es importante que destinemos un tiempo a comprender el concepto de convolución y su funcionamiento, porque haremos referencia a ello en diversos momentos más adelante. 

Convolucionar un kernel consiste en multiplicar los valores de la matriz cuadrada M x N por los valores de los píxeles de nuestra imagen de forma sucesiva. Si tenemos un kernel como el ejemplo anterior, de 3x3, iremos multiplicando el contenido de este kernel por todos los cuadrados de 3x3 que podamos generar en nuestra imagen, **deslizando el kernel por la imagen** (lo que se denomina _sliding window_ ). 

Una única aplicación del kernel a una imagen se puede comprender mejor observando la siguiente imagen. 

92 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



El kernel de 3x3 se multiplica por el cuadrado de 3x3 resaltado en azul en la imagen original que hemos llamado _input_ . El resultado de esta multiplicación se almacena en una nueva imagen de salida llamada _output_ (en rojo), que será nuestro resultado ya filtrado o suavizado, según sea el tipo de kernel que usemos. Como vemos, la aplicación del kernel a un cuadrado de 3x3 produce **un único pixel de salida** , correspondiente con el central. 

Desde el punto de vista numérico, todos los valores del kernel se multiplican por todos los valores del cuadrado azul y se suman. Este resultado de la suma de multiplicaciones se almacena en la posición central del cuadrado azul original en su correspondiente lugar en la imagen de salida. 

La convolución de este kernel no es más que irlo desplazando por la imagen para que pase por **todos** los cuadrados de 3x3 que podamos encontrar en la imagen, hasta completar la imagen de salida _output_ . Es más sencillo comprenderlo observando su funcionamiento en la siguiente figura. 



Primeros seis pasos de la convolución de un kernel de 3x3 en una imagen de 8x8 píxeles. 

93 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En función de los valores que tenga el kernel, conseguiremos diferentes efectos. Por ejemplo, el kernel que hemos empleado de ejemplo más arriba – denominado filtro Gaussiano, como veremos en seguida – da el máximo valor al pixel central (4), un valor de la mitad (2) a los pixeles directamente colindantes, y un valor mínimo (1) a los píxeles en diagonal. Si razonamos sobre estos valores, lo que estamos haciendo es modificar el valor de un pixel en función de los valores de los píxeles de su alrededor, lo que a fin de cuentas en un suavizado ya que eliminará los bordes y diferencias más marcadas. Veamos este comportamiento en un ejemplo. 

Pongamos que tenemos una región de nuestra imagen de 3 x 3 datos en escala de grises con los siguientes valores de píxeles y nuestro kernel con los valores también mostrados. Analicemos el resultado operación a operación. Cada pixel se multiplica por su valor correspondiente en el kernel, se calcula el valor promedio y este será el valor del pixel correspondiente en la imagen de _output_ . 



Hemos comentado que gracias a los filtros podemos suavizar una imagen, aumentar su nitidez o desenfocarla. Pero, ¿por qué podríamos llegar a querer desenfocar una imagen? Principalmente el motivo está relacionado con el ruido. Si bien desde nuestra perspectiva visual la imagen será menos agradable, esto puede ayudar a nuestros algoritmos a no verse afectados por este ruido. La realidad es que el suavizado y el desenfocado son el mismo proceso, la única diferencia es como percibe nuestro cerebro el resultado final. 

### **2.4.1. Blurring y denoising.** 

El _blurring_ , denominado desenfoque o difuminación es un proceso de tratamiento de imágenes que reduce el ruido y los detalles de la imagen. Se emplea ampliamente en visión artificial en la fase de preprocesado de la imagen. El _denoising_ es el proceso específico de reducir el ruido de imágenes para mejorar su calidad. 

Vamos a ver los métodos más empleados para difuminar imágenes en visión artificial. 

94 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- a. Averaging Blurring 

Este tipo de filtrado se consigue empleando un kernel en el que todos sus valores son 1. Esto quiere decir que todos los píxeles tienen el mismo valor a la hora de multiplicar el kernel por la matriz. Si empleamos todos los píxeles que rodean un pixel para generar su salida, estaremos difuminando la imagen ya que usaremos todo su entorno para generar la salida. 

Esto dará un resultado como el siguiente: 



Valores de un kernel de “average”. En el medio, el logotipo original y a la dcha la aplicación del filtro. 

- b. Gaussian Blurring 

El filtro Gaussiano preserva mucho mejor los bordes en la imagen al darle más importancia al pixel central, posteriormente a los colindantes y por último a los píxeles en diagonal. En función del tamaño del kernel, los valores van cambiando como podemos ver a continuación: 



Valores de un kernel gaussiano de 3x3, de 5x5 y de 7x7. Podemos ver cómo el valor central es el más importante y cómo el valor desciende a medida que se alejan del mismo. 

95 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Al final, si nos fijamos en los valores todos ellos persiguen el mismo objetivo, que es dar más importancia a los pixeles más cercanos al pixel central, frente al _Averagin Blurring_ que da la misma importancia a todos los píxeles. En la siguiente imagen podemos observar el resultado de aplicar un filtro gaussiano a la misma imagen del logo de OpenCV de tamaño 5x5 (que es el kernel central de la imagen superior). Como vemos, se mantienen mejor los bordes mientras que se sigue ejecutando la difuminación de la imagen. 

En futuros ejemplos y aplicaciones veremos lo esencial que es la aplicación del _Gaussian Blurring_ para mejorar la precisión y resultados de numerosos métodos de extracción de características por métodos tradicionales como puede ser la detección de bordes, de esquinas, de contornos… 



Ejecución de un filtro gaussiano con un kernel de 5x5 al logotipo de OpenCV 

#### c. Median Blurring 

En el filtro de mediana **no** aplicamos un kernel con valores determinados en el que multipliquemos los píxeles de la imagen por una serie de valores. En este caso, lo que hace el _Median Blurring_ es calcular la mediana de todos los píxeles que caben dentro del kernel. Es decir, el kernel no es una matriz por la que multiplicar, sino una operación a realizar en sus M x N posiciones. Recordemos que la mediana es el valor estadístico que divide una distribución en dos, es decir, quedan el mismo número de valores a ambos lados. 

Por ejemplo, en la distribución (1,1,2,2,3,4,5,5,5,6,7) la mediana es (4), ya que a la izquierda del 4 quedan el mismo número de valores (1,1,2,2,3) que a la derecha (5,5,5,6,7). Esto es lo que hará un filtro Median con todos los píxeles de la imagen de entrada que quepan en el tamaño de kernel seleccionado para su aplicación. Es decir, en un kernel de 3x3 haremos la mediana de 9 valores. En un kernel de 5x5 haremos la mediana de 25 valores. Y así sucesivamente para cualquier tamaño de kernel. 

96 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Este filtro se emplea especialmente para reducir el ruido en imágenes, ya que es capaz de reducir enormemente la entropía y el ruido, ayudando así a limpiar las imágenes. Esto contribuirá positivamente a nuestros algoritmos de visión artificial a la hora de buscar características y aplicar objetivos. Para poner un ejemplo, emplearemos la misma imagen del logo de OpenCV, pero en este caso habremos introducido en la imagen ruido artificial para observar mejor el funcionamiento de este filtro para la eliminación del ruido. 



Aplicación de un filtro de mediana (Median Blurring) a un logotipo de OpenCV con ruido, para observar la reducción del ruido gracias a este filtro. 

### **2.4.2. Sharpening** 

La otra operación que podemos realizar gracias a los filtros basados en kernels es el _sharpening_ . Esta operación cuyo nombre proviene de _sharpen_ , afilar en inglés, por lo que persigue aumentar la nitidez y contraste en los bordes de las imágenes. 

Para realizar esta operación, sencillamente usaremos un kernel como el que podremos observar en la siguiente imagen. Básicamente, estamos aumentando el valor del propio pixel y reduciendo el valor de los píxeles circundantes, por lo que conseguimos que todos los detalles se resalten hasta el extremo. En la siguiente imagen podemos observar un ejemplo de aplicación de un filtrado de _sharpening_ . 



Aplicación de un filtro de sharpening sobre una imagen en la que podemos ver cómo cada pixel ha sido aumentado y todos los bordes y diferencias se observan notablemente más. 

97 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por ahora, todo lo que hemos aplicado son tecnologías de **preprocesado de imagen** . A partir de la siguiente sección, comenzaremos a estudiar técnicas de visión artificial centradas en la **extracción de características** , el siguiente paso del flujo habitual de un sistema de visión artificial.  En la siguiente imagen podemos comprobar dónde se encuentran las técnicas estudiadas hasta el momento, y podemos observar hacia donde se dirigen nuestros esfuerzos formativos desde este punto. 



### **2.5. Detección de bordes, contornos, rectas y esquinas** 

Hasta el momento todas las técnicas de visión artificial que hemos estudiado han pertenecido a la categoría del preprocesado de imagen. Gracias a ellas, somos capaces de optimizar una imagen previa mediante el procesado de la misma. Bien sea mejorando el brillo, el contraste o la nitidez; cambiando de escala o de perspectiva e incluso reduciendo el ruido y suavizando los bordes, conseguiremos que los algoritmos de visión artificial posteriores puedan desempeñarse en su máximo rendimiento. Una vez alcanzado el mejor punto para las imágenes que capturamos o recibimos, es el momento de convertir una imagen en información útil para resolver el problema de visión artificial que nos hayamos planteado. El primer paso para esto será encontrar las características básicas de nuestra imagen, aquellas que nos puedan ayudar a que nuestro sistema inteligente las comprenda mejor. 

Continuamos en esta sección con nuestra aproximación a las **técnicas clásicas de visión artificial** . A partir de este momento, como hemos comentado, trataremos de **extraer características** o _features_ de nuestras imágenes. Recordemos que las _features_ son características distintivas de una región específica de una imagen. Pueden ser estructuras, formas, bordes, objetos, cambios de iluminación… 

_Las características son por tanto elementos de información visual que pertenecen a una imagen y pueden ayudar a resolver un determinado objetivo de visión artificial._ 

98 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Debido a la gran cantidad de información no estructurada que tiene una imagen, la extracción de características se convierte en un proceso esencial para extraer la información más relevante de cada imagen. Gracias a esta información preseleccionada, podremos aplicar posteriormente algoritmos de visión artificial para la clasificación, detección o segmentación de objetos entre otros. 

Una vez preprocesada la imagen, cuando esta tiene las mejores combinaciones de parámetros para maximizar la precisión de nuestro método, debemos buscar ciertos elementos diferenciales dentro de nuestra imagen que nos puedan ayudar a encontrar determinados objetos, a clasificarlos e incluso a segmentarlos. 

Una de las características más básicas en una imagen es el conjunto de los bordes que contiene. Los seres humanos procesamos el mundo como formas contenidas dentro de bordes, y por tanto tratamos de que nuestros algoritmos de visión artificial hagan lo mismo. Cuando los seres humanos dibujamos objetos, generalmente primero dibujamos sus bordes y posteriormente nos centramos en los elementos interiores y en el color de los mismos. Los bordes, por tanto, suelen ayudarnos a definir la tipología y la ubicación de un objeto, y es por tanto de vital importancia ser capaces de extraerlos en nuestras imágenes. Esta será la primera _feature_ que perseguiremos extraer de nuestras imágenes de manera totalmente automática. 



A partir de esta sección abandonaremos el preprocesado de imágenes para centrarnos en la extracción de características, previas a la aplicación del objetivo final. 

Desde un punto de vista matemático, un borde en una imagen es una región en la que la intensidad cambia de forma brusca o abrupta, o desde un punto de vista formal: presenta discontinuidades. Para detectar bordes podremos emplear dos tipos de métodos, que son aquellos basados en convoluciones, y Canny. 

99 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **2.5.1. Detección de bordes mediante convolución: Sobel, Prewitt y Laplacian Edge** 

Ya hemos analizado el funcionamiento de las convoluciones en las imágenes. En resumen, partiremos de un kernel de M x N posiciones con determinados valores que multiplicamos por cada ventana disponible de M x N en nuestra imagen. Para ello, convolucionamos el kernel (es decir, lo vamos deslizando por la imagen) para obtener un valor de cada pixel procesado. Recordemos que independientemente del tamaño del kernel, siempre calcularemos un único valor para cada kernel, que es el que corresponde al pixel central. 

Los valores de nuestro kernel determinarán a qué le prestamos más atención – y por tanto qué buscamos – en nuestra imagen de entrada. En todos los ejemplos anteriores hemos empleado kernels de filtrado, que perseguían suavizar, desenfocar e incluso acentuar imágenes. En este caso, tendremos que usar kernels que nos permitan detectar bordes, es decir, cambios bruscos de intensidad. Para aplicar este tipo de métodos, buscaremos tres tipos de bordes: 

- Bordes verticales: Analizaremos píxeles contiguos de forma vertical. 

- Bordes horizontales: Analizaremos píxeles contiguos de forma horizontal. 

- Bordes diagonales: Compararemos los píxeles contiguos en diagonales opuestas. 

Hay tres tipos principales de kernel para esta búsqueda (es decir, tres posibles selecciones de valores): Sobel, Prewitt y Laplace. 

Los métodos de **Sobel y Prewitt** se basan en encontrar los máximos y mínimos de la intensidad de nuestra imagen en cada uno de los ejes, para así extraer los bordes. 

Esto es una operación similar al uso de la primera derivada de una función matemática para así hallar sus máximos y mínimos locales. A continuación, podemos ver los kernels que emplean cada uno de estos dos métodos en el eje horizontal (x) y el eje vertical (y). 



En la fila superior observamos los kernels de Sobel para el eje vertical a la izquierda y para el eje horizontal a la derecha. En la fila inferior, los correspondientes de Prewitt. 

100 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Como podemos ver ambas perspectivas se centran en las diferencias de intensidad a la derecha e izquierda en el eje horizontal y en las diferencias de intensidad entre la fila superior y la inferior en el eje vertical. Para obtener el resultado final de la búsqueda de bordes tendremos que sumar el resultado de la búsqueda de bordes horizontales y verticales. Como podemos ver, estos métodos no están centrados en la detección de bordes diagonales. 

Por otra parte, el método **laplaciano** se basa en trabajar con la segunda derivada, a diferencia de los métodos anteriores que trabajaban con la primeria. La ventaja de trabajar con la segunda derivada es que podemos encontrar bordes en dos dimensiones con el mismo kernel, mientras que Sobel y Prewitt necesitan dos kernels, uno para el eje horizontal y otro para el eje vertical. Esta gran ventaja que divide entre dos la complejidad del algoritmo, conlleva una desventaja importante: este método es muy sensible al ruido. Al buscar bordes en las dos dimensiones a la vez, será complejo diferenciar el ruido de bordes reales, y podemos acabar usando un algoritmo inservible. 

Para evitar esto, debemos recordar las secciones de preprocesado. Ya hemos analizado diversos filtros y métodos para eliminar el ruido de las imágenes, de entre los cuales los que mejores resultados ofrecen son el filtro Gaussiano y el _Median Filter_ . Si aplicamos estos filtros antes de buscar bordes con el método de _Laplace_ , obtendremos resultados excelentes. A continuación, podemos observar dos de los kernels más típicos aplicados en la ejecución de un _Laplacian Edge Detection_ . Hay más opciones de kernel, pero todos siguen la misma lógica, como podemos comprobar en la imagen. 



Dos kernels empleados para filtros Laplacianos 

### **2.5.2. Detección de bordes mediante Canny** 

Este algoritmo de detección de bordes recibe su nombre de su creador, John F. Canny. Este algoritmo pasa por varios estados de forma ordenada para ejecutar la detección de bordes al final de todos ellos. 

En primer lugar, se ejecuta un filtro de reducción del ruido mediante un filtro gaussiano con un kernel de 5x5. Después se ejecuta un filtro de Sobel tanto en las direcciones vertical como horizontal para encontrar el gradiente de la intensidad, como ya hemos mencionado previamente. 

101 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Una vez ejecutado Sobel, se ejecuta un algoritmo conocido como “ _non-maximum suppression_ ” en el que se mantienen únicamente los máximos y mínimos locales, por lo que se obtiene una imagen con bordes potenciales de un ancho reducido. 

Por último, para seleccionar los bordes reales de entre los bordes potenciales, se emplea un algoritmo denominado “ _Hysteresis thresholding_ ” que como indica su nombre, es un tipo de umbralizado ( _thresholding_ ). Gracias a este umbralizado, solo los bordes con un valor entre un máximo y un mínimo – tal y como siempre funciona un algoritmo de umbralizado – son mantenidos como bordes. Por tanto, es un algoritmo que haciendo uso de todas las técnicas que hemos estudiado hasta el momento encuentra de forma muy precisa los bordes de una imagen, con un algoritmo más complejo que un mero convolucionado de un kernel de M x N. 

#### **Ejemplo de detectores de bordes** 

Vamos a ver en un ejemplo en Jupyter Notebook la aplicación de todos estos detectores de bordes. En este ejemplo usaremos otra fotografía de ejemplo incluida en la librería skimage, llamada “astronaut”. 

Para aplicar los tipos de detección de bordes que hemos mencionado ejecutaremos las siguientes funciones de OpenCV: 

- `cv.Sobel(src, ddepth, dx, dy, ksize)` : En el parámetro ddepth indicaremos la profundidad de bits que queremos usar en la salida. En este caso usaremos imágenes en escala de grises con una profundidad de 8 bits. Los parámetros dx y dy sirven para indicar en qué eje queremos ejecutar Sobel. En este caso, lo ejecutaremos en ambos. Por último, ksize nos pregunta por el tamaño de nuestro kernel, que en este ejemplo será de 5 x 5 

- `cv.Laplacian(src, ddepth, ksize)` : Emplea los mismos parámetros, pero en este caso no se seleccionan ejes ya que la detección Laplaciana se efectúa sobre las dos dimensiones de la imagen por defecto. 

- `cv.Canny(image, threshold1, threshold2)` : En este caso seleccionaremos los dos límites de Canny para ejecutar este método (recordemos que el último paso de Canny es un umbralizado entre dos valores). En este método, OpenCV aúna todos los pasos del algoritmo Canny en una única llamada. 

Abrimos como siempre Anaconda Navigator, y ejecutamos la aplicación Jupyter Notebook. Cuando se abra la página principal en nuestro navegador, crearemos un nuevo notebook de Python3 y le cambiaremos el nombre por “Edge Detection”. 

102 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Pegaremos el siguiente código en la primera celda y lo ejecutaremos con el botón “Run”. 

Lo primero que hacemos en este código es aplicar un filtro para reducir el ruido de la imagen y mejorar así el resultado de la detección de bordes, principalmente de los métodos Laplaciano y Canny. 

Después, pasaremos esta imagen a escala de grises, ya que la gran mayoría de métodos de visión artificial orientados a la detección de bordes funcionan sobre imágenes de un único canal, y la imagen que estamos procesando es una imagen a color. Hechas estas dos operaciones, mostraremos por pantalla la imagen a color original, esta misma imagen a color con un filtro gaussiano aplicado gracias a la función `cv.GaussianBlur()` con un kernel de 3 x 3 – en el que podremos observar como los detalles se difuminan, pero también el ruido se reduce – y por último la imagen en escala de grises, que es un proceso que ya hemos realizado en otras ocasiones mediante la función `cv.cvtColor()` . 





103 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

El resultado de la ejecución de esta celda de código será el siguiente (original, Gaussiano, escala de grises) 



Una vez tenemos nuestra imagen filtrada y en escala de grises, es el momento de aplicar el primer detector de bordes; Sobel. Para ello, creamos una segunda celda de código comn el botón “+” e introducimos el siguiente snippet de código. 



Veremos como salida la imagen en escala de grises con todos los bordes que ha encontrado Sobel, tanto en el eje horizontal como en el vertical marcados en intensidades altas (blancos y grises claros) mientras que el fondo queda a 0 (negro) 

A continuación, aplicaremos una búsqueda de bordes Laplaciana con OpenCV. Creamos una tercera celda y ejecutamos dentro de ella el siguiente código en Python. 



En este caso veremos la salida del filtro Laplaciano, que como era de esperar es una salida más limpia y con los bordes mucho mejor definidos. 

104 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por último, añadimos una celda con “+” y ejecutamos el siguiente código para probar el algoritmo de Canny sobre nuestra imagen en blanco y negro de una astronauta. En este caso tenemos unos bordes mucho más finos y definidos, seguramente más representativos de los bordes reales de la imagen original por los motivos y ventajas que ya hemos mencionado en la parte teórica. 



A continuación, mostramos las imágenes en orden de los siguientes detectores de bordes: Sobel, Laplace, Canny. 



Como ejercicio adicional proponemos cambiar los parámetros de las tres funciones para ver cambios en los resultados. Podemos variar los tamaños de kernel (por ejemplo 3 x 3 o 7 x 7) o variar el “threshold” de la función Canny. Con cada cambio que hagamos, deberemos ejecutar de nuevo la celda correspondiente, y veremos como la detección de bordes varia con cada cambio realizado. 

Como podemos observar, los bordes arrojados por el método de Canny son notablemente más escasos y estrechos. Esto es debido a la gran cantidad de pasos previos y del filtrado por umbralizado que realiza este algoritmo para mejorar esta detección de bordes. 

105 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **2.5.3. Detección de contornos** 

Ahora que hemos analizado los bordes de las imágenes, es posible encontrar una característica mucho más relevante de las imágenes: **Los contornos** . 

Si bien la extracción de bordes ( _edges_ ) es una característica relevante en visión artificial, es poco común que los bordes por sí mismos nos ayuden a encontrar o clasificar objetos. Una de las operaciones más básicas que pueden realizarse con bordes es la búsqueda de contornos sobre los mismos. La diferencia entre un borde y un contorno es que el segundo tiene que ser una curva cerrada. Es decir, 

_Un contorno es un borde que está cerrado, y por tanto se asume que contiene un objeto o una parte completa del mismo._ 

En ocasiones, para encontrar un contorno es necesario unir varios bordes, hasta conseguir una línea cerrada que cumpla con la definición de contorno. Esto nos ayudará tanto a analizar formas en futuras secciones como a detectar y segmentar los objetos de una imagen. 

Generalmente el primer paso para buscar contornos es, por tanto, buscar los bordes de una imagen. Podremos hacerlo mediante métodos simples o mediante el algoritmo de Canny. Una vez obtengamos una imagen binaria con los bordes obtenidos, podremos comenzar con la búsqueda de contornos. Habitualmente la búsqueda de contornos sigue la lógica de unir los píxeles de los contornos que tienen intensidades similares entre ellos. 

Los contornos se pueden extraer teniendo en cuenta la jerarquía que existe entre ellos ( _hierarchy_ ) o no. La jerarquía entre contornos indica qué contornos se encuentran dentro de otros, lo que puede aproximarse a qué contornos son objetos y qué contornos son partes de objetos. Los contornos de mayor jerarquía serán objetos, y las jerarquías inferiores serán partes de objetos o partes de partes de objetos. 

Hay dos métodos principales para la detección de contornos: 

- a. Sin aproximación en cadena.  Con este tipo de método, buscamos contornos con todos los puntos posibles dentro de los bordes que hemos obtenido previamente. Los bordes cercanos espacialmente y con intensidades conocidas se unen, y se consideran parte del mismo contorno, almacenando todos los puntos intermedios a lo largo del contorno. 

- b. Con aproximación en cadena. En este caso, solo se mantienen los puntos extremos de cada contorno, es decir, se simplifican los contornos a sus puntos más extremos, lo que resulta en una menor cantidad de datos y una mayor velocidad de procesado. 

106 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Para calcular contornos con OpenCV emplearemos la siguiente función, tras haber buscado bordes previamente sobre nuestra imagen: 

cv.findContours(image, mode, method). Los parámetros necesarios son los `siguientes:` 

- `image: La imagen que queremos emplear, previamente buscados sus bordes` 

- `mode: Elegiremos el modo de contornos según si queremos analizar todos los contornos o solo los de jerarquía mayor` 

- `method: seleccionaremos el método que deseamos emplear de entre los dos que hemos mencionado, que en OpenCV son CHAIN_APPROX_NONE y CHAIN_APPROX_SIMPLE` 

Vamos a buscar contornos en la imagen del astronauta sobre el que ya hemos aplicado la búsqueda de contornos, por lo que el siguiente ejemplo será una continuación del ejemplo anterior. Esto quiere decir que **no debemos crear un Jupyter Notebook** , sino añadir una última celda al cuaderno que teníamos del ejemplo anterior, que terminó con la ejecución del algoritmo Canny sobre la imagen de la astronauta. 



107 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

El resultado serán dos imágenes. La primera de ellas mostrará el resultado del algoritmo de detección de contornos sin aproximación. La segunda de ellas, con aproximación simple. Podremos comprobar que las diferencias son muy sutiles, casi imperceptibles. Si nos fijamos en los contornos, resaltados en verde, veremos que en efecto se han generado artefactos que corresponden a elementos únicos de la imagen. Las estrellas de la bandera, los ojos, la nariz, la boca, la insignia, el casco… 

Gracias a estos contornos podríamos lanzar un algoritmo de segmentación de objetos de una forma relativamente sencilla y sin necesidad de emplear redes neuronales, como veremos más adelante. 



### **2.5.4. Detección de rectas y círculos** 

En ocasiones estaremos interesados en detectar un tipo específico de bordes o contornos, como pueden ser las líneas rectas. Las líneas rectas pueden ayudarnos a comprender la ubicación, orientación y perspectiva de numerosos objetos. También podemos querer buscar círculos y elipses en numerosos casos de uso, como veremos en el ejemplo más adelante. 

El algoritmo de detección de rectas **más empleado en la actualidad** es un algoritmo que fue ideado en 1962 conocido como la transformada de Hough, o Hough Lines. 

Este algoritmo trabaja con imágenes binarias – es decir, con imágenes de profundidad de un bit – por lo que el primer paso para aplicarlo siempre será pasar nuestras imágenes a una escala binaria, preferiblemente mediante un método de detección de bordes y a ser posible previo filtrado para eliminar el ruido y suavizar la imagen. 

El algoritmo de Hough toma cualquier punto y analiza las infinitas rectas que pueden pasar por él, y efectúa esta misma operación con todos los demás puntos, obteniendo una serie de rectas potenciales dada cualquier imagen. Cada recta obtiene una votación según lo probable que sea una recta. Esto se hace dividiendo la imagen en una cuadrícula definida por los parámetros _rho resolution_ y _theta resolution_ en cada una de las dimensiones. 

108 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Una vez buscadas rectas potenciales en cada celda de la cuadrícula, se trata de encontrar aquella de mayor distancia con mayor probabilidad de ser una recta en la imagen. Las candidatas más votadas serán las consideradas definitivamente rectas, y devueltas por tanto por el algoritmo. Las rectas son representadas en coordenadas polares en este algoritmo, de forma que la ecuación de una recta viene determinada por la siguiente expresión, en la que el primer término es la pendiente y el segundo el punto de corte en el eje vertical. 



A diferencia de las coordenadas cartesianas en las que el punto es descrito por su distancia a cada uno de los ejes, las coordenadas polares constan de un valor de distancia al eje de coordenadas ( r ) y un ángulo ( θ ) que indica la inclinación de la recta que va desde el origen de coordenadas hasta P. 

Para ejecutar este algoritmo con OpenCV usaremos la siguiente función 

```
cv.HoughLines(image, rho, theta, threshold):
```

- image: Nuestra imagen de entrada. Deberá estar suavizada y bina `- rizada` 

- `rho: Número de píxeles por celda` 

- `theta: Ángulo entre las celdas` 

- `threshold: Número mínimo de votos para considerar que una recta lo es` 

Para nuestro siguiente ejemplo vamos a descargarnos la siguiente imagen, empleada de ejemplo por el repositorio de OpenCV en Github: https://raw.githubusercontent. <u>com/opencv/opencv/3.4/samples/data/sudoku.png</u> 

La almacenaremos en una ruta conocida para así poder emplearla en el ejemplo. Se trata de una imagen de un sudoku. Pongamos que queremos programar un sistema que sea capaz de resolver un sudoku a partir de una fotografía. Para hacer esto, lo primero que necesitaremos será encontrar las líneas que conforman este sudoku y por tanto nos ayudan a comprender las distintas celdas que componen el sudoku. En nuestro ejemplo cambiaremos varias veces los distintos valores de configuración de la función Hough Lines para ver cómo varían los resultados según el valor que demos a los distintos parámetros. 

109 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Tras lanzar Anaconda Navigator e iniciar Jupyter Notebook, crearemos un nuevo Jupyter Notebook de Python3 y en la primera celda introduciremos el siguiente código. 

**Recordemos introducir correctamente la ruta de la imagen de Sudoku, cambiando si fuera necesario las barras de orientación para que todas sean esta ‘/’ y Python pueda acceder a nuestro archivo.** 



Con la ejecución de esta celda podremos comprobar que hemos cargado correctamente la imagen del sudoku en escala de grises. Esto dará como resultado la imagen de la izquierda de las dos siguientes. 



Ahora, crearemos una nueva celda en la que introduciremos el código que se muestra a continuación, con el que buscaremos sus bordes gracias al algoritmo Canny, generando así una imagen binaria con la que podamos trabajar posteriormente con HoughLines, y la mostraremos por pantalla. Esta imagen es la que podemos observar a la derecha, donde vemos una imagen binarizada en la que los píxeles a “1” son los bordes encontrados por el algoritmo de Canny. 



110 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Esta imagen se puede observar a la derecha de la imagen anterior, en blanco y negro. Por último, vamos a ejecutar la función de HoughLines en la que buscaremos las líneas y las trataremos de dibujar en color violeta sobre la imagen original. 

Crearemos una tercera y última celda para esta ejecución, con el siguiente código que ejecutaremos acto seguido. Recordemos que hay que ejecutar todas las celdas y siempre en orden para que los ejemplos se ejecuten correctamente. 



111 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Esta última ejecución podemos verla en la última de las tres imágenes que se han mostrado más arriba, donde podemos observar que la práctica mayoría de líneas han sido detectadas y dibujadas en violeta (255, 0, 255). Sin embargo, podemos ver cómo hay algunas líneas que no son totalmente detectadas por el algoritmo, dando como resultado una extracción incompleta de las mismas, lo que según el objetivo que tuviéramos puede ser un resultado insatisfactorio. Para tratar de mejorar este resultado podemos modificar los parámetros de entrada de la función de HoughLines. Si bajamos el valor del _threshold_ , por ejemplo, cambiando la llamada a la función por la siguiente línea: 

```
lines = cv.HoughLines(canny, 1, np.pi / 180, 105)
```

Podremos observar cómo, al bajar el número de votos necesarios para considerar una recta como tal, el algoritmo detecta demasiadas rectas, haciendo inutilizable esta solución. Este resultado lo podemos ver en la imagen de la izquierda. Si por el contrario cambiáramos el threshold por un número mayor, por ejemplo 

```
lines = cv.HoughLines(canny, 1, np.pi / 180, 210)
```

Veríamos el efecto contrario, en el que las rectas necesitarían tantos votos para ser consideradas candidatas adecuadas, que perderíamos la detección de una gran cantidad de rectas y nos encontraríamos con el mismo problema en el otro extremo del espectro. 

Este es el resultado mostrado en la imagen derecha. En definitiva, afinar este algoritmo clásico es un trabajo manual basado en prueba y error, y en ocasiones detectaremos que no es posible detectar todas las líneas por mucho que cambiemos los parámetros. Estas son las limitaciones habituales de los métodos clásicos de visión artificial. 



112 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Otro elemento relevante que podemos plantearnos buscar entre nuestros _edges_ son los círculos. Para ello, emplearemos un algoritmo muy similar al que hemos empleado para buscar líneas, denominado Hough Circles. Este método, similar en lo teórico, incluye parámetros para limitar el tamaño mínimo y máximo del círculo. En este caso, no hablamos de rectas definidas por dos parámetros ( r,θ ), sino de un círculo definido por el punto central (x, y) y la longitud de su radio (r). Este algoritmo, por tanto, nos devolverá una serie de círculos detectados, por los que podremos iterar y emplearlos para detectar o segmentar determinados objetos de interés. Veamos un ejemplo en código. Como siempre, es recomendable suavizar la imagen mediante un filtrado si esta tiene ruido, y ejecutar un algoritmo de búsqueda de bordes para binarizar la imagen de forma orientada. 

Lo primero que debemos hacer es descargar la imagen con la que vamos a trabajar. Vamos a emplear una imagen que ya hemos visto previamente: el logotipo de OpenCV. La descargaremos del siguiente enlace, y la almacenaremos en una ubicación conocida: 

<u>https://raw.githubusercontent.com/opencv/opencv/4.x/samples/data/opencv-logo.png</u> 

En el mismo Jupyter Notebook en el que lanzamos el algoritmo de HoughLines, creamos una nueva celda con el botón “+” e incorporamos el siguiente _snippet_ de código. 



113 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



### **2.5.5. Detección de esquinas** 

Hasta el momento hemos sido capaces de encontrar bordes, contornos, líneas rectas y círculos. La última característica concreta que vamos a tratar de extraer de nuestras imágenes en esta asignatura desde el punto de vista individual son las esquinas. 

Ya hemos comentado como en la detección de objetos tendemos a tratar de encontrar las cajas ( _bounding boxes_ ) que contienen los objetos de interés. Generalmente, estos objetos de interés están delimitados por contornos y rectas, pero para encontrar sus extremos es imprescindible detectar las esquinas. Esta característica ayudará a nuestros sistemas de visión artificial a detectar puntos críticos sobre los que posteriormente ejecutar un procesado para detectar objetos. Las esquinas son una de las _features_ consideradas como más relevantes en visión artificial, ya que tienden a delimitar objetos en el mundo visual. En el caso de la visión artificial dinámica, es decir, la relativa a los videos, las esquinas son uno de los métodos más robustos para seguir objetos a lo largo de los distintos fotogramas. 

Esto es porque a medida que una imagen se mueve, se rota y se cambia de escala (es decir, de _zoom_ ), los bordes y contornos cambian. Los bordes irán cambiando de longitud, intensidad, contraste, ubicación… Convirtiendo la tarea de identificarlos y seguirlos en un video en misión imposible. Sin embargo, las esquinas siguen siendo esquinas siempre, aunque se roten, se cambie su escala o su perspectiva. Esto las convierte en una característica robusta muy interesante de identificar, por lo que estudiaremos una serie de métodos para hacerlo. 

El método más sencillo que veremos para detectar esquinas se denomina el método Harris, que fue propuesto por Chris Harris y Mike Stephens en su artículo “A Combined Corner and Edge Detector” publicado en 1988. Este método diferencia entre tres tipos de regiones en la imagen. Aquellas zonas en las que no hay un cambio significativo de intensidad, se clasifican como planas, o _flat_ . 

114 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Las zonas en las que la intensidad cambia en el eje vertical o en el eje horizontal, se denominan bordes, o _edges_ , y para detectarlos se emplea el método Sobel que hemos mencionado antes, ya que es el método que mira la primera derivada y por tanto puede diferenciar entre dimensiones. Por tanto, el método de Harris busca bordes además de esquinas. 

Por último, y esta es la novedad, las zonas en las que hay cambios de intensidad tanto en el eje horizontal como en el vertical, se denominan esquinas, o _corners_ . Estas diferentes zonas se pueden observar de forma visual en la siguiente imagen, que nos ayudará a comprender de un vistazo el funcionamiento del algoritmo de Harris. 



A la izquierda observamos una zona _flat_ , en el centro una zona con diferencia en el eje vertical y por tanto un _edge_ , y por último una zona con cambios en horizontal y vertical que resulta ser una esquina, una _corner._ 

Para ejecutar este algoritmo, emplearemos el método de OpenCV corner Harris, que muestra el siguiente funcionamiento 

```
cv2.cornerHarris(src, blockSize, ksize, k:
```

- `src: La imagen de entrada` 

- `blockSize: El tamaño de la ventana de calibración (en color sepia en la imagen anterior)` 

- `ksize: El tamaño del kernel con el que aplicaremos Sobel` 

- k: El parámetro de ajuste del método Harris 

El resultado de ejecutar el algoritmo de Harris sobre una imagen es una imagen en escala de grises en la que la intensidad de los píxeles significa la probabilidad de cada uno de ellos de ser una esquina. Por tanto, si aplicamos un umbralizado en el que marquemos un valor mínimo de intensidad, podremos seleccionar las esquinas encontradas con Harris con mayor o menor probabilidad. Lo veremos de forma práctica en un ejemplo más adelante. 

115 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Seis años después de la publicación del algoritmo de Harris, surgió una mejora de manos de Shi-Tomasi, con un algoritmo denominado “ _Good Features To Track_ ”, que fue publicado en 1994. Este algoritmo trata no solo de encontrar esquinas, sino de encontrar aquellas que pueden ser relevantes para detectar y seguir objetos en imágenes y videos. Es decir, no busca todas las esquinas por métodos meramente matemáticos basados en cambios de intensidad, sino que trata de estimar cuales de todas estas zonas de _corner_ pueden ser interesantes de cara a realizar una identificación posterior en un proyecto de visión artificial. Además, el algoritmo permite indicar el número de esquinas que se desea encontrar, por lo que en problemas en los que conocemos la imagen que vamos a encontrarnos, esto reduce mucho la incertidumbre de la búsqueda de esquinas. 

El algoritmo encuentra las N esquinas ( _corners_ ) más fuertes (es decir, con mayor puntuación de probabilidad de ser una esquina). Esto hace que sea un algoritmo algo más complejo, pero más ampliamente empleado que Harris. 

En OpenCV emplearemos el siguiente método, que ejecutará este algoritmo en base a una serie de parámetros de entrada 

```
cv.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance)
```

- `image: La imagen de entrada` 

- `maxCorners: La N que indica el número de esquinas que buscamos` 

- `qualityLevel: Las esquinas inferiores a este nivel de calidad son rechazadas` 

- `minDistance: Distancia mínima entre esquinas (para evitar solapes)` 

**Importante que recordemos** que el proceso de búsqueda de esquinas, y en especial el de Good Features to Track **no busca encontrar todas las esquinas de una imagen** , sino aquellas suficientemente buenas como para considerar que van a mantenerse invariables independientemente de la rotación y la escala. Eso nos asegura que si empleamos estos puntos para caracterizar los objetos de nuestra imagen, podremos reconocerlos en imágenes similares y durante el transcurso de un video. No debe por tanto alarmarnos que los algoritmos de detección de esquinas no nos proporcionen todas las esquinas de una imagen, ya que precisamente este comportamiento estará demostrando el funcionamiento adecuado de los algoritmos. 

Vamos a ver en un ejemplo la ejecución del algoritmo de Good Features to Track, que como veremos es realmente sencilla. 

116 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

#### **Ejemplo detección de esquinas** 

Para ello, descargaremos otra imagen de ejemplo de OpenCV, en este caso “blox”, que se encuentra en el siguiente enlace 

#### <u>https://raw.githubusercontent.com/opencv/opencv/master/samples/data/blox.jpg</u> 

La almacenaremos en una ruta conocida, e iniciaremos Anaconda Navigator. Lanzaremos Jupyter Notebook y crearemos un nuevo cuaderno de Python3. Una vez hecho esto, en la primera celda introduciremos el siguiente código, que nos ayudará a visualizar el funcionamiento de un algoritmo de búsqueda de esquinas mediante OpenCV. 



117 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En la salida de la ejecución de esta única celda, veremos la imagen original en escala de grises y la imagen coloreada con las 25 esquinas más importantes seleccionadas. Si quisiéramos seguir objetos, deberíamos emplear estas esquinas para identificarlos y seguirlos a lo largo de las distintas imágenes. 



Hasta este punto, hemos analizado todos los diferentes tipos de características específicas que podemos buscar mediante algoritmos de visión artificial. Todos estos procesos de extracción de características son técnicas clásicas de visión artificial, pero esto no implica que no estén relacionadas con las redes neuronales profundas. Las Redes Neuronales Convolucionales (CNN) efectúan **todos** estos procesos de forma interna dentro de sus capas ocultas, pero se basan en estos mismos principios para clasificar, detectar y segmentar objetos. Es por esto que es esencial conocer estas técnicas y las posibilidades que ofrecen. Por descontado, hay numerosos métodos que no se han mencionado a lo largo de esta sección por limitaciones temporales, pero se han cubierto todos los algoritmos básicos de extracción de características esenciales. Los alumnos podrán profundizar en variaciones de los algoritmos estudiados, ajuste fino de los parámetros de los algoritmos empleados en función del caso de uso al que se enfrenten e incluso encontrar nuevos algoritmos para resolver los mismos problemas. 

El objetivo de esta sección no ha sido generar una lista exhaustiva de técnicas y algoritmos para encontrar características, sino comprender los procesos más habituales a la hora de realizar este proceso como son la binarización, el suavizado y la búsqueda de bordes para posteriormente encontrar contornos, líneas, círculos, esquinas … 

A partir de este momento iremos aumentando la complejidad y abstracción de las características y objetivos de visión artificial, ya que hasta el momento solo hemos visto técnicas clásicas aisladas con algoritmos relativamente sencillos para resolver problemas concretos y extremadamente acotados. 

118 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **2.6. Extracción de características globales e invariantes: detectores y descriptores** 

### **2.6.1. SIFT (Scale-invariant feature transform)** 

Hasta ahora hemos hablado de extracción manual de características. Esto es, hemos podido seleccionar el tipo de característica ( _feature_ ) que queríamos obtener sobre la imagen (contornos, líneas, esquinas…) y las hemos podido buscar gracias a una serie de algoritmos. Este fue el enfoque original del campo de visión artificial, en el que mediante la ejecución de algoritmos basados en la intensidad de los pixeles y sus vecinos, podían encontrar estas características. A medida que el campo de la Inteligencia Artificial avanzó, también lo hizo el enfoque empleado para la extracción de características. 

En 1999, David Lowe publicó el algoritmo que marcaría el cambio de enfoque: SIFT (Scale-invariant feature transform). Este algoritmo perseguía extraer de forma automática las características más relevantes de una imagen para posteriormente poder detectar o reconocer objetos. Con este enfoque, ya no era necesario seleccionar manualmente las características más relevantes de una imagen para extraerlas, sino que SIFT se encargaría de ello. 

Uno de los puntos más fuertes que planteaba SIFT era la invariancia, es decir, la capacidad de las características de ser estables independientemente de la escala, la rotación, el ruido o el cambio de contraste, entre otros. Uno de los grandes problemas de los detectores de esquinas que se empleaban hasta el momento es que las esquinas son invariantes frente a la rotación, pero no son invariantes al escalado. Una esquina puede dejar de serlo si se acerca o se aleja la imagen, y esto las convierte en una característica compleja de emplear en el reconocimiento y seguimiento de objetos de imágenes en movimiento que se acercan y se alejan. SIFT primero busca cualquier característica suficientemente representativa, como pueden ser bordes, esquinas o líneas. Posteriormente, aplica sucesivos suavizados con filtros Gaussianos para analizar is estas características son estables con ruido. Aplica distintos escalados y desescalados para comprobar cuáles son las características que se siguen detectando tras estas operaciones. 

Finalmente, una vez seleccionadas las mejores características, trata de describirlas para que se puedan emplear con el objetivo de seguirlas a lo largo de un video, por ejemplo, o de detectar objetos en imágenes diferentes. Digamos que tenemos un contorno detectado que es totalmente invariante a la rotación, la escala y el ruido. Para poder informar a un algoritmo de que esta característica es X y cómo debe buscarla en otras imágenes diferentes, deberemos describirla. 

119 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

SIFT describe las características mediante un algoritmo llamado Histograma de Gradientes Orientados (HOG) que, como cabe esperar, es un algoritmo denominado un **descriptor de características** . Hasta este momento hemos estado detectando múltiples características, pero no nos habíamos planteado como describirlas para trasladar esta información a futuros modelos o sistemas. Esta tarea es la que realizan los descriptores de características. 

Cuando un ser humano observa una escena, su cerebro se fija en puntos de interés esenciales para reconocer la imagen. Los colores de los objetos, sus bordes y esquinas, su forma y su tamaño. Cuando vemos un objeto, somos capaces de describirlo visualmente. Por ejemplo, un televisor sería “un rectángulo horizontal de color negro brillante”. Sus características serían “cuatro esquinas negras en el interior y del color de la pared en su exterior”. Esta es la tarea de un descriptor de características como es HOG. 

HOG funciona de una forma similar al método Sobel para la búsqueda de bordes. Analiza el gradiente de una imagen (la primera derivada, es decir, los cambios de intensidad en cada una de las dimensiones) para determinar cambios de intensidad. HOG fue descrito en 1996. Dado que es un histograma, su funcionamiento básico es analizar la dirección de los bordes de cada región de la imagen, y estimar la frecuencia con la que apuntan a cada dirección en una región determinada de la imagen. Es decir, es un algoritmo que analiza la dirección principal que tienen los bordes y esquinas de una imagen en una cuadrícula homogénea. Esto ayuda a describir cada región de una imagen en base a sus características. 

En la siguiente imagen, podemos observar un ejemplo del funcionamiento de HOG, sobre nuestra ya conocida imagen de una mujer estadounidense vestida con un traje de astronauta.  Es importante que nos fijemos muy de cerca en la imagen, para comprender la diferencia de esta técnica con una mera extracción de bordes. En esta técnica estamos observando **todos los bordes** existentes de la imagen, divididos en casillas cuadradas. En cada casilla, observamos una especie de haz de rayos formado por varias líneas. Cada una de estas líneas es la dirección de un borde detectado estudiando el gradiente de la imagen. Veremos, por ejemplo, que en los hombros de la astronauta las líneas son todas diagonales, indicando que en este lugar los bordes son totalmente homogéneos (y sugiriendo, además, una buena característica que observar). Lo mismo sucede con los laterales del cohete del fondo. Sin embargo, si miramos los ojos, hay líneas mirando en todas direcciones. Esto indica que no hay un borde claramente definido que mira hacia una dirección concreta. Sin embargo, esto también es algo muy característico, ya que solo puede significar un círculo cerrado sobre sí mismo. 

120 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En esta imagen de ejemplo estamos mostrando HOG aplicado a toda la imagen. Sin embargo, lo que hacen métodos como SIFT – y también SURF, que veremos más adelante – es aplicar este análisis de la orientación del gradiente únicamente a las zonas en las que han determinado previamente que existen características relevantes. Gracias a esto, pueden describir las características invariantes que han encontrado, permitiendo así almacenar este conocimiento para aplicarlo en situaciones posteriores. 

En definitiva, HOG no es un método inteligente de extracción de características, como si lo son SIFT y SURF, sino que es una mera forma estandarizada de describir regiones de una imagen. Si esta región de la imagen coincide con una característica relevante, entonces habremos dado con un algoritmo que nos permite encontrar características invariantes y relevantes de una imagen, y además podremos describirlas en lenguaje matemático para que las máquinas puedan reconocer distintos objetos de la misma forma que nosotros, por ejemplo, somos capaces de reconocer y describir cualquier tipo de vehículo tan solo en base a una serie de características básicas que comparten. 



### **2.6.2. SURF (Speeded Up Robust Features)** 

Tras el surgimiento de SIFT, el mundo de la visión artificial comenzó una carrera por encontrar el mejor detector y descriptor de características robustas e invariantes, hasta que las Redes Neuronales Convolucionales lo revolucionaran todo. SURF fue el heredero directo de SIFT, surgido en 2006 y patentado por sus creadores. El objetivo principal del desarrollo de SURF fue incrementar la eficiencia del proceso, reduciendo el tiempo y las operaciones necesarias para encontrar características invariantes. Este objetivo fue completado, y SURF es notablemente más rápido que SIFT a la hora de seleccionar características. En este caso, para encontrar características se basa en un método de detección de contornos que no hemos mencionado llamado “Hessian detector”, que permite detectar características en una fracción del tiempo que necesita SIFT con el empleo de Sobel. Por lo demás, SURF también ejecuta un suavizado Gaussiano en la imagen, para reducir el ruido y generar en ocasiones un cierto desenfoque que ponga a prueba las características seleccionadas. Además del empleo del algoritmo Hessian, realiza cambios de escala mediante reducciones de escala, asegurando así la invariabilidad de sus características. 

121 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En este caso, para la descripción de las características que encuentra, SURF usa un algoritmo llamado “Ondícula de Haar”, en contraposición con HOG, que es empleado por SIFT. El principio de funcionamiento es similar, y permite conocer la orientación del gradiente de cada una de las características encontradas, para así poder almacenar una descripción formal de las mismas. De nuevo, el funcionamiento pasa por dividir la imagen en una cuadrícula. Dentro de cada una de sus celdas se ejecutará el análisis de la orientación del gradiente para así poder describir cada característica. 

SURF demostró ser igual de eficaz que SIFT a la hora de encontrar características relevantes e invariables en una fracción del tiempo. No obstante, ninguno de ellos es suficientemente rápido para funcionar en aplicaciones en tiempo real, lo que limita enormemente su potencial en proyectos reales, limitándolo a procesos por lotes o a vídeos con extremadamente pocos frames por segundo. Ambos métodos están patentados, por lo que es necesario adquirir una licencia para su uso. No obstante, los desarrolladores de OpenCV dieron con un método similar a ambos, pero lo suficientemente distinto como para no estar bajo las restricciones de ninguna de estas patentes, por lo que, si en algún momento necesitáramos emplearlos, podríamos acudir a OpenCV, siempre sabiendo que el modelo será ligeramente distinto de los estudiados en esta asignatura. 

En la siguiente imagen podemos ver la comparación entre las _features_ extraídas por SIFT y por SURF de una misma imagen. Por supuesto, no encuentran las mismas características ya que, aunque son métodos que siguen una misma estructura, emplean algoritmos distintos para cada paso (detección y descripción de características). Sin embargo, esto no es un problema ya que el reto es descubrir automáticamente las características visuales de esta imagen que sean invariantes a la escala, el ruido y la rotación, y que por tanto sean relevantes para que un algoritmo de visión artificial pueda realizar cualquier tarea que le sea encomendada. El centro de los círculos verdes es la característica encontrada, y la línea marcada es la orientación del gradiente de esta característica. En el caso de SIFT, las características se han encontrado analizando el gradiente como cuando buscamos bordes con Sobel. En el caso de SURF, mediante un detector de Hessian. Para la selección de la orientación del gradiente, en la imagen de la izquierda veremos el resultado arrojado por HOG (empleado en SIFT), y a la derecha el arrojado por Haar (empleado por SURF). 



A la izquierda, el resultado de buscar características invariantes con SIFT. A la derecha, el mismo proceso realizado con SURF. 

122 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Recordemos el propósito de los detectores y descriptores de características. En una aplicación de visión artificial, el paso esencial tras la captura y preprocesado de una imagen es encontrar las características más relevantes de la misma desde una perspectiva visual. De igual forma que nuestros cerebros reconocen una rana porque es “un animal verde, pequeño, con dos ojos saltones, dos patas muy largas y otras dos más pequeñas y que suele estar rodeado de agua”, los algoritmos de visión artificial necesitan poder tener características esenciales de los objetos que deben buscar, para poder procesar la información visual. Si bien podemos seleccionar estas características de forma manual mediante prueba y error, esta aproximación suele ser arriesgada ya que las características que elijamos pueden no mantenerse de forma estable en distintas imágenes, y entonces nuestros algoritmos perderían la referencia. 

Las características siempre son sucesos relativos a cambios de intensidad de los píxeles de la imagen, como pueden ser un borde, una esquina, o una forma geométrica. Es por ello que podemos tratar de encontrarlas manualmente por medio de kernels y de diversas operaciones matemáticas como las que hemos analizado hasta el moento. Sin embargo, si somos capaces de que un algoritmo seleccione las mejores características posibles por nosotros, aumentaremos notablemente nuestras probabilidades de éxito en el siguiente paso del proceso de la visión artificial, al que no hemos llegado: la aplicación de nuestro objetivo. 

### **2.6.3. ORB (Oriented FAST and Rotated BRIEF)** 

Por ahora hemos visto que contamos con dos algoritmos principales de selección y descripción automática de características: SIFT y SURF. Ambos están patentados y requieren tantas operaciones que no funcionan en tiempo real, por lo que su uso suele implicar un desembolso elevado y altos tiempos de cómputo. 

Para tratar de enfrentarse a este problema, surge en 2011 el último de los métodos relevantes de detección y descripción de características: ORB. Recordemos que en 2012, la primera Red Neuronal Convolucional (CNN) entrenada sobre una GPU demostró al mundo las enormes capacidades que el _deep learning_ podía poner en manos de la visión artificial, y comenzó la transición entre las técnicas clásicas y el aprendizaje profundo. Por tanto, ORB es el último gran esfuerzo por mejorar los algoritmos de visión artificial sin referencia a las redes neuronales. 

ORB fue el resultado del trabajo de los desarrolladores de OpenCV Labs, que publicaron un artículo llamado “ _ORB: An efficient alternative to SIFT or SURF_ ”, en el que declaraban abiertamente la intención de su desarrollo. 

123 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Como todos los detectores y descriptores de características que hemos visto, ORB tiene un proceso ordenado que permite llegar al resultado. Al principio, detecta potenciales características mediante un algoritmo llamado FAST, que analizaremos a continuación, y además una aplicación modificada del detector Harris de esquinas. Una vez seleccionadas las características potenciales, se trata de asegurar de que estas son invariantes a la escala, la rotación y el ruido. Con todas aquellas que pasan este examen, se aplica un descriptor de características, que en este caso es BRIEF, que también analizaremos. 

ORB es un método mucho más rápido que SURF y SIFT, permitiendo ser usado en tiempo real, lo que aumenta exponencialmente sus posibilidades. Además, funciona mejor que SURF, y según el caso de uso iguala el funcionamiento de SIFT. 

El algoritmo de búsqueda de características FAST fue propuesto en 2006, y era en esencia un detector de esquinas rápido y mejorado respecto a los algoritmos de detección de esquinas que hemos analizado con anterioridad en profundidad. A diferencia del resto de métodos de detección de esquinas (que nacieron mucho antes, en torno a las décadas de 1980 y 1990), no emplea una ventana de análisis de forma cuadrada de NxN píxeles, sino que se emplea **un círculo** . Para cada pixel a analizar, se traza un círculo de 16 pixeles de longitud. Si en este círculo trazado hay más de n pixeles (n es un valor parametrizado que podemos modificar en el código) con una intensidad mayor o menor en t (t es otro valor parametrizable que podremos seleccionar), entonces el método de FAST considera que el pixel es una esquina, y lo almacena en una lista de esquinas potenciales para su posterior tratamiento. En la siguiente imagen podemos ver una imagen del artículo original en la que se trata de explicar este comportamiento de forma visual. Vemos como se numeran los píxeles en la longitud de la “circunferencia” del 1 al 16, que serán los que se analicen para determinar si el pixel p forma parte de una esquina o si, por el contrario, es parte de una superficie plana o sencillamente de un borde que no puede ser considerado como esquina. 



124 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Gracias a este comportamiento se analizan muchísimos menos píxeles que en ventanas completas, y por tanto el algoritmo es tremendamente rápido, característica que le dio su nombre. 

ORB ejecuta FAST para encontrar las esquinas más relevantes. Sobre el resultado de FAST se ejecuta el algoritmo clásico de búsqueda de esquinas de Harris para así elegir las N mejores esquinas que serán consideradas características esenciales por ORB. Todas estas son evaluadas, como en el resto de algoritmos, frente a un suavizado Gaussiano y a un cambio de escala de tal forma que se pueda asegurar que las características detectadas son invariantes. Estas características serán en este caso, esencialmente, esquinas. 

Para describir estas esquinas, ORB emplea el algoritmo descriptor BRIEF. Recordemos que SIFT y SURF empleaban cada uno su propio descriptor. En el caso de BRIEF (Binary Robust Independent Elementary Features). En este caso, no se trata de analizar las orientaciones de los gradientes de cada punto clave encontrado por FAST. En cambio, BRIEF trata de describir cada característica como un número binario (es decir, una combinación de 1 y 0) de entre 128 y 512 bits de largo. 

Para cada característica encontrada, BRIEF analiza sus pixeles de dos en dos. Si el primer pixel es más brillante que el segundo, añade un 1 a la secuencia binaria. Si es más oscuro, añade un 0. Realizando este proceso a lo largo de todos los pares de píxeles de cada característica detectada, es capaz de describirla para que se pueda recocer y trackear en el futuro. 

En definitiva, ORB tiene un funcionamiento muy similar a SIFT y a SURF. En concreto, emplea el algoritmo FAST para detectar características invariantes a la escala, que en este caso son únicamente esquinas, y el algoritmo BRIEF para describir estas características. 

Dado que ORB es el único detector y descriptor de características que es de uso libre y está disponible en OpenCV, vamos a comprobar su funcionamiento por medio de un ejemplo de código de tal forma que podamos observar su funcionamiento en tiempo real en un Jupyter Notebook. Para empezar, vamos a analizar las funciones que necesitaremos emplear en OpenCV. 

**`cv.ORB_create():`** `Con este método crearemos un objeto de la clase ORB,` que será el que nos permitirá ejecutar los dos pasos necesarios para el `algoritmo ORB sobre nuestra imagen` 

```
orb.detect(img): Este método nos permite buscar los puntos clave o ca-
racterísticas de nuestra imagen. Devuelve un array de puntos clave.
```

- `img: La imagen de entrada en la que deseamos detectar features` 

125 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

```
orb.compute(img, keypoints): Por último, ejecutaremos el descriptor
(BRIEF) sobre nuestra imagen dadas las features encontradas en el punto
anterior
```

- `img: La imagen de entrada de la que queremos describir features` 

- `keypoints: El array con todos los puntos clave encontrados previamente por FAST` 

Vamos a emplear la misma imagen que usamos en nuestro ejemplo de detección de esquinas. Tendremos que prestar especial atención a una diferencia esencial con estos. En esencia, **no se detectarán todas las esquinas** . Recordemos que la funcionalidad principal de estos detectores automáticos de características es seleccionar **únicamente aquellas que son invariantes a los cambios de escala y rotación** . Por tanto, habrá muchas esquinas que se detectaron con Harris y con Good Features to Track que no aparecerán en la salida de esta ejecución porque no se consideran invariantes según los criterios de ORB. 

Abrimos Anaconda Navigator y ejecutamos Jupyter Notebook. Creamos un nuevo cuaderno con Python3. 

Para este ejemplo, volveremos a emplear la imagen “blox.jpg”, por lo que es importante que la tengamos almacenada del ejemplo anterior. En caso de no encontrar la imagen, el enlace se encuentra en la sección anterior, previo al ejemplo de código de detección de esquinas. 

En la primera celda, escribiremos el siguiente código, con la precaución de cambiar la ruta de la imagen por allá donde esté almacenada nuestra copia de la imagen “blox. jpg”. 



126 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Lo que vemos en esta imagen son todos los puntos clave que el algoritmo de ORB considera que son importantes para poder hacer reconocimiento y seguimiento de objetos. En la siguiente sección veremos cómo estos puntos se relacionan entre sí con imágenes similares. 



En resumen, hemos visto algoritmos que nos permiten seleccionar las características esenciales de nuestras imágenes de forma automática. Sin embargo, esto no parece ayudarnos de forma directa y sencilla a aplicar objetivos de visión artificial. Por ahora tenemos una imagen con una serie de características descritas, que sabemos que son de calidad e invariantes a la escala y la rotación. No obstante, ¿cómo relacionar estas características con otras imágenes similares? Este es nuestro último objetivo: Una vez seleccionadas y descritas las mejores características, querremos poder buscarlas en otras imágenes para realizar un proceso conocido como “ _feature matching_ ”, en el que profundizaremos en la siguiente sección. 

Estos algoritmos de detección de características siguen estando vigentes a día de hoy, a pesar de la gran extensión de las Redes Neuronales Convolucionales CNN. Como ya mencionamos al comienzo de esta asignatura, hay problemas que no pueden o no deben resolverse por medio de _Deep Learning_ . Los métodos clásicos como ORB son poco complejos, y no requieren de grandes capacidades computacionales. Por el contrario, las redes neuronales profundas requieren de una gran capacidad de cómputo, generalmente ejecutada sobre tarjetas gráficas (GPU) de última generación. En determinados proyectos, esto puede suponer una limitación seria para la viabilidad de un despliegue basado en Deep Learning. 

127 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por ejemplo, hay proyectos que deben desplegarse en campo en los que no podemos instalar un servidor con grandes GPUs, ni contar con una conexión estable a internet para poder emplear servidores con GPU desplegados en _cloud_ . Si bien en la actualidad existen numerosas CNN enormemente eficientes incluso pensadas para ser ejecutadas en dispositivos móviles, el entrenamiento de las mismas sigue siendo necesario realizarlo en GPU en la mayoría de las ocasiones. 

Aun así, el _deep learning_ tiene otro obstáculo que las técnicas clásicas evitan en todas las ocasiones. Los modelos de aprendizaje profundo requieren de un entrenamiento basado en una gran cantidad de muestra etiquetada. Una red neuronal no basta con programarla, hay que entrenarla. En muchos casos reales, los clientes no son capaces de obtener suficiente muestra como para entrenar una red neuronal, por motivos de negocio. 

Por ejemplo, en un caso de visión artificial en el que debemos controlar la calidad del embotellado del vino, deberemos contar con muestra de botellas correctamente embotelladas y erróneamente embotelladas para poder desarrollar una red neuronal que distinga entre ambas. Supongamos que nuestro cliente solo comente 1 error al mes en el embotellado de botellas, pero que este error le supone un gran coste económico porque inutiliza todo el lote. Si necesitamos 1000 imágenes de botellas incorrectamente embotelladas para poder entrenar una red neuronal de clasificación – como veremos más adelante – deberíamos esperar 1000 meses para poder comenzar nuestro proyecto, y su viabilidad se vería enormemente comprometida. Es aquí cuando un buen equipo de visión artificial recurre a las técnicas clásicas. Si somos capaces de capturar la botella de vino siempre en la misma posición, bajo la misma iluminación, podríamos aplicar un detector y descriptor de características como SIFT, SURF y ORB sobre las botellas. Una vez seleccionadas las características más robustas, podríamos tratar de comprobar que todas ellas se encuentran presentes en las botellas que se van rellenando en la línea de producción. En caso de que no estén presentes todas (o un cierto porcentaje de ellas), la botella se consideraría como errónea, y se lanzaría un aviso. 

Gracias al empleo de las técnicas clásicas, habríamos sido capaces de ahorrar a nuestro cliente no solo tiempo, sino también el coste de un servidor de procesamiento de _deep learning_ con una GPU potente asociada. Si bien es probable que la tasa de fallo sea ligeramente mayor con un detector como ORB, es la única forma en la que este proyecto es viable, y empleando distintas herramientas como el ajuste gamma, el suavizado de la imagen, la detección automática de características y, por último, el _feature matching_ , podríamos llegar a implementar un proyecto de una calidad muy similar a otro basado en redes neuronales por una fracción del tiempo y del dinero que este necesitaría. 

128 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Esta sección ha sido la última en la que trataremos la extracción de características. Hemos pasado desde las características más simples (los bordes) hasta su extracción más compleja y automática, y su descripción. A partir de este punto, no es posible buscar más características, y **pasaremos a la aplicación de los objetivos de visión artificial** , en los que tendremos que trabajar con la mejor combinación de preprocesado de nuestra imagen (transformaciones, ajustes, filtrados) y extracción de características que hayamos sido capaces de obtener. Es por ello que las secciones estudiadas hasta ahora son de vital importancia, ya que son la base de todo lo que está por venir. Y esta base necesita ser firme para soportar un proyecto completo de visión artificial. 

### **2.7. Feature Matching y reconocimiento de objetos con ORB** 

Como hemos comentado, a partir de esta sección entramos dentro del terreno de la aplicación de nuestros objetivos. Una vez preprocesada la imagen y extraídas sus características tenemos que **hacer algo con las características extraídas** . Para ello, lo más importante es poder relacionarlas entre sí. 



Una vez seleccionadas las características más importantes, y que además sabemos que son invariantes, necesitamos poder reconocer estas mismas características en futuras imágenes para así relacionar objetos entre sí, y alcanzar al fin y por primera vez, una comprensión visual real en nuestros sistemas. En la siguiente imagen podemos observar dos fotogramas de la película “El Padrino”. En la primera de ellas se ha ejecutado un detector de características. En la segunda, se ha tratado de encontrar estas mismas características, que debido al movimiento de la cámara se han desplazado. Podemos ver visualmente la relación entre estas características. Este proceso, que estudiaremos en profundidad en esta sección, es el proceso conocido como relación de características, o _feature matching_ . Podemos comprobar cómo en ocasiones este _matching_ no es perfecto. Por ejemplo, en la primera imagen se ha seleccionado el primer cajón como característica, pero por cambios de posición e iluminación, en la segunda imagen se ha detectado el segundo cajón. Este es uno de los grandes problemas de la detección y _matching_ de características. Si hay puntos de la imagen que se parecen demasiado, podríamos llegar a confundirlos con pequeños cambios en las condiciones de iluminación. 

129 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



### **2.7.1. Matching por fuerza bruta** 

Este es el método más simple para relacionar características. Primero, extraemos las características de cada una de las imágenes, la primera y la segunda. Después, para cada descriptor de característica obtenido de la primera imagen, lo comparamos con todos los descriptores de la segunda imagen. La característica más parecida, será la que se asuma que es el _match_ . El problema con este método es que asume que todas las características van a estar presentes en ambas imágenes, lo que en la gran mayoría de ocasiones es una estrategia demasiado arriesgada. La opción para evitar esto es aplicar el cross check, que compara también la segunda imagen con la primera, para así solo extraer las características que se comparten entre ambas, y evitar sobre relacionar características. 

Para ejecutar este algoritmo, usaremos la siguiente función de OpenCV, que creará un objeto de tipo BFMatcher (Brute Force Matcher): 

```
cv.BFMatcher(normType, crossCheck):
```

- `normType: Decide el método con el que se mide la distancia entre características.` 

- crossCheck: Si ponemos a True este valor, se ejecutará el algoritmo `en sentido contrario (comparando la segunda con la primera) y solo` se devolverán aquellos matches que se cumplan en ambas direcciones. 

Una vez creado este objeto, podremos emplear el método “ `match` ”, que tienen las instancias de esta clase, para analizar las características comunes de ambas imágenes en base a sus descriptores. 

```
bf.match(img1,img2):
```

- `img1: La imagen original en la que hemos detectado características en primer lugar` 

- `img2: La imagen en la que queremos encontrar las mismas características para seguir objetos` 

```
Devuelve un objeto de tipo DMatch que contiene toda la información acerca
de las distancias entre las diferentes características
```

130 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por último, para poder visualizar la correspondencia entre las distintas características de nuestras imágenes, usaremos el método `drawMatches` de OpenCV 

```
cv.drawMatches(img1, kpi1, img2, kp2, matches):
```

- `img1: La primera imagen original` 

- `kp1: Las características extraídas para la primera imagen` 

- `img2: La imagen en la que queremos detectar las mismas características` 

- `kp2: Las características de la segunda imagen` 

- matches: El resultado de la ejecución de bf(match) para ambas imá `- genes` 

Este método devolverá una imagen con las características de cada imagen `y una línea que las une, tal y como hemos visto en las fotos de “El Padrino” anteriormente` 

Vamos a tratar de descargarnos dos imágenes para poner a prueba todos estos conceptos en un ejemplo de código real. En este ejemplo vamos a tratar de **identificar un objeto en una imagen** . Es decir, trataremos de cumplir un objetivo de **reconocimiento de objetos** . Para ello, necesitaremos una imagen del objeto a identificar que será nuestra imagen de muestra. Además, necesitaremos una imagen en la que este objeto se encuentre en un escenario real. Trataremos de identificar el objeto de la primera imagen en la segunda imagen por medio de _feature matching_ por fuerza bruta. 

El objeto que vamos a tratar de encontrar es una caja de galletas de almendras, que se encuentra en el siguiente enlace: 

<u>https://raw.githubusercontent.com/opencv/opencv/master/samples/data/box.png</u> 

La imagen en la que trataremos de buscar este objeto será la siguiente: https://raw.githu- <u>busercontent.com/opencv/opencv/master/samples/data/box_in_scene.png</u> 

En la primera imagen veremos el objeto que buscamos perfectamente recortado y enfocado. En la segunda, este objeto está en otra posición, iluminación, rodeado de otros objetos y parcialmente ocluido. Trataremos de ejecutar el _feature matching_ para encontrar nuestra caja de almendras en una imagen real en la que está mezclada de otros objetos y fondos. 

131 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



A la izquierda podemos observar la caja de galletas que queremos buscar. A la derecha se encuentra la misma caja rodeada de otros objetos apoyados sobre una silla. 

Una vez descargadas ambas imágenes en una ruta conocida, abriremos Anaconda Navigator y lanzaremos Jupyter Notebook. Crearemos un nuevo cuaderno de Python 3, y en la primera celda copiaremos el siguiente fragmento de código, y lo ejecutaremos. Recordemos cambiar las rutas de las imágenes por aquellas donde hemos almacenado las imágenes descargadas desde los servidores de Github de OpenCV. Con esta celda, estaremos ejecutando el algoritmo de OBR sobre ambas imágenes, igual que hemos hecho en el algoritmo anterior. Esta celda **no tiene datos de salida** , por lo que no debemos preocuparnos si no arroja ningún resultado por pantalla al ejecutarla. 



132 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Ahora tenemos las características de cada imagen (kp1 y kp2) y los descriptores de las mismas (des1 y des2). El siguiente paso será ejecutar un _matching_ por fuerza bruta para tratar de encontrar las características de la imagen 1 en la imagen 2. Para ello, creamos una nueva celda e introducimos el siguiente código, que ejecutaremos: 



En este caso sí que veremos una imagen de salida, que se adjunta a continuación. En esta imagen, generada por el método drawMatches, podemos ver tanto las características encontradas en la primera y segunda imagen, como aquellas que han dado _match_ gracias a nuestro algoritmo. Como podemos ver, las características unidas por líneas son aquellas que se han encontrado en ambas imágenes, arrojando resultados muy buenos para la identificación de nuestra caja de galletas en la segunda imagen. Acabamos de ejecutar nuestro primer algoritmo de **reconocimiento de objetos** únicamente mediante técnicas clásicas de visión artificial. 



133 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **2.7.2. Reconocimiento de objetos con ORB y Brute Force Matching: Homografía** 

El último algoritmo que vamos a ver en esta unidad va a ser la búsqueda de objetos gracias a las características que devuelve SIFT mediante un algoritmo llamado FLANN y una técnica conocida como homografía. En nuestro último ejemplo hemos sido capaces de encontrar características distintivas de un objeto en otra imagen, lo que nos permitiría repetir esto con cualquier otra imagen, como puede ser un vehículo atravesando un peaje, o para asegurarse de que un minero está correctamente vestido con todos los elementos de protección necesarios (casco, gafas, guantes, respirador…). Sin embargo, no hemos llegado a recuadrar el objeto, a generar su _bounding box_ , que en muchas ocasiones es esencial en Visión Artificial. 

Si bien vamos a estudiar la gran mayoría de ejemplos de detección de objetos en forma de redes neuronales, veremos un último algoritmo de visión artificial clásica para realizar esta tarea. 

Para ser capaz de encontrar el objeto completo tras hacer un _matching_ de las características, necesitamos emplear un algoritmo que comprenda el cambio de perspectiva entre el objeto original y su situación en la imagen real, en base a la disposición de sus características comunes. En definitiva, un algoritmo de homografía trata de encontrar el cambio de perspectiva que relaciona una serie de puntos dos a dos. Nuestro cerebro humano hace esto de una forma innata. Si miramos a nuestras dos imágenes, podemos imaginar perfectamente en 3 dimensiones las rotaciones a las que tenemos que someter a la caja de galletas para poder verla exactamente como se muestra en la segunda imagen. Esto es más complicado hacerlo de forma matemática sin un cerebro visual como el nuestro. 

El método “ findHomography ” de OpenCV busca la relación tridimensional entre pares de puntos. Gracias a nuestras características obtenidas por ORB, tenemos suficientes puntos como para tratar de estimar esta modificación tridimensional. Si somos capaces de entenderla, podremos estimar los bordes de nuestro objeto, ya que encontraremos exactamente la relación entre una perspectiva y otra, bordes de la caja incluidos. 

134 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Crearemos una tercera celda en nuestro ejemplo anterior, para así poder reaprovechar las características encontradas en la primera imagen y poder buscar la perspectiva de nuestra caja directamente. En esta tercera celda, introducimos el siguiente fragmento de código y lo ejecutamos. 



Con esto habremos conseguido encontrar la caja de galletas en la segunda imagen, pero no solo eso, sino también sus bordes, que es lo más importante para este caso de visión artificial en el que tratamos de reconocer objetos y las coordenadas completas que los definen. Gracias a esta transformación de perspectiva, **tenemos las cuatro esquinas de nuestra caja** , que hemos dibujado en nuestra imagen gracias a la función `cv.polylines()` que dibuja polígonos dados los puntos de sus aristas. 

135 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

La salida de esta celda es la imagen 2 con nuestra caja de galletas segmentada gracias a la transformación de perspectiva de las características que previamente habíamos hecho match con ellas. Hemos terminado el último ejemplo de código de esta sección y, con él, esta unidad de nuestra asignatura de visión artificial. 



136 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

## **3. Aplicación de objetivos y** **_deep learning_** 

_“La clasificación de objetos puede realizarse tanto por medio de algoritmos básicos de machine learning que beben de características seleccionadas manualmente mediante técnicas clásicas de visión artificial, o bien puede realizarse gracias a Redes Neuronales Convolucionales diseñadas y entrenadas para este fin.”_ 

A partir de esta unidad, nos centraremos en la aplicación de los distintos objetivos de la visión artificial. Ya hemos visto en la sección introductoria un resumen de todos ellos: clasificación de objetos, detección de objetos, segmentación, estimación de pose y acciones, generación de contenido… 

Hasta este momento hemos analizado los pasos previos a la aplicación de los objetivos, conocidos como preprocesamiento de imágenes y extracción de características. No está de más recordar que la extracción de características puede realizarse de dos formas según el enfoque de visión artificial que apliquemos: 

- Técnicas clásicas: La extracción de características es un proceso manual. Deberemos seleccionar las características más relevantes de los objetos que deseamos clasificar / detectar / segmentar, y encontrar el método adecuado para poder extraerlas. 

- _Deep learning_ : En este caso es el propio modelo basado en redes neuronales profundas el que hace de forma autónoma la extracción de características. Estos modelos reciben una imagen, extraen las características más relevantes, y aplican el objetivo deseado en un mismo algoritmo. Esto no quiere decir que no haya una extracción de características, sino que será automática y el desarrollador no tendrá que seleccionarlas manualmente. 

En el caso de la aplicación de objetivos, el desarrollador tiene plena potestad para seleccionar el objetivo y la manera de la que se va a tratar de cumplir este. En el caso de las técnicas clásicas, partiremos de una serie de características ya extraídas. En el caso de los modelos de aprendizaje profundo, partiremos de una imagen y el resultado será la aplicación del objetivo. 

137 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

A lo largo de esta unidad vamos a analizar los distintos algoritmos que nos permiten llevar a cabo cada uno de los objetivos típicos de visión artificial ordenados de más sencillo a más complejo. Para los objetivos más complejos, veremos primero las técnicas clásicas asociadas a los mismos, y posteriormente las arquitecturas de redes neuronales profundas que son capaces de realizar estas mismas tareas. Sin embargo, en el caso de los objetivos más complejos como pueden ser la generación de contenido o la detección de acciones humanas, únicamente estudiaremos modelos de _deep learning_ . Esto es debido a que no hay algoritmos con una calidad suficiente en el terreno de las técnicas clásicas para llevar a cabo estos objetivos, y por tanto carece de sentido explorarlos ya que nunca será recomendable explorarlos. 

### **3.1. Preparación del entorno de Google Colab** 

**Nota:** Esta es la sección que se debe leer si al comienzo de la asignatura se ha optado por no instalar un entorno local para visión artificial, y se desea usar desde el principio cómputo en la nube con Google Colab. 

En esta unidad no vamos a poder usar un entorno en local para la gran mayoría de ejemplos, ya que para ejecutar modelos basados en _Deep Learning_ sabemos que necesitamos potentes GPUs para realizar el entrenamiento y la inferencia de estos modelos. Por ello, vamos a emplear una tecnología muy similar a Jupyter Notebook, pero que en este caso será ejecutada en la nube, para poder tener acceso a GPUs con capacidad de cómputo suficiente como para ejecutar los modelos. Esto significa que para poder ejecutar los ejemplos de código de esta unidad en tiempo real, será necesaria una conexión a internet. De igual manera que en la unidad anterior, **en ningún caso es necesario ejecutar los ejemplos** , y es suficiente con analizarlos y comprenderlos para poder avanzar en la asignatura. 

Sin embargo, esto nos proporciona una ventaja clara: No tendremos que instalar ningún software en nuestro equipo. Tan solo con acceder al siguiente enlace, podremos usar nuestro primer cuaderno de Colab: 

<u>https://colab.research.google.com/notebooks/welcome.ipynb</u> 

Como podemos ver, el formato de archivo es el mismo que Jupyter Notebook, y es que, al fin y al cabo, Google Colab no es más que un cuaderno de Jupyter siendo ejecutado en una máquina remota en la nube, de la que vemos resultados al momento en nuestro navegador. La gran ventaja es que vamos a seguir trabajando los ejemplos de la misma manera que hacíamos hasta ahora. Tendremos celdas de código, botones de crear celdas y ejecutar, y pantallas de salida para ver el resultado de nuestras ejecuciones. 

138 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Hasta ahora hemos empleado Jupyter Notebook por dos motivos. Por un lado, evitábamos tener la obligación de contar con una conexión a internet constante y estable para poder ejecutar los ejemplos. Por otro, hemos aprendido a poner a punto un sistema local para proyectos de visión artificial, que es al fin y al cabo como se trabaja en el mundo real. Sin embargo, dado que seguramente no contemos con una GPU de última generación, las limitaciones técnicas del _Deep Learning_ nos fuerzan a emplear un software en la nube, con las ventajas y desventajas que esto acarrea. 

Por último, es una gran noticia que una vez terminemos esta asignatura hayamos empleado dos tipos de sistema de desarrollo y ejecución de algoritmos de visión artificial (local y nube, Jupyter y Colab, clásico y deep learning) ya que mejorará enormemente nuestras aptitudes de cara al futuro laboral. 

Es necesario tener una cuenta de Google para usar Google Colab, e iniciar sesión en esta, ya que nos ayudará a poder guardar nuestros cuadernos de una vez para otra, lo cual es bastante importante. Cada vez que queramos iniciar Google Colab, bastará con acceder a la raíz del dominio: <u>https://colab.research.google.com/</u> y emplear el menú Archivo > Nuevo cuaderno para crear un nuevo cuaderno de igual forma que hemos hecho hasta ahora en Jupyter Notebook. 

Vamos a crear un cuaderno nuevo en Google Colab para comprobar su funcionamiento, antes de saltar a los primeros compases de teoría y práctica de esta Unidad. 

Vamos a tratar de mostrar un histograma de una imagen descargada de internet directamente en un cuaderno de Google Colab para comprobar cómo los procesos y rutinas son prácticamente idénticos que en Jupyter Notebook. Desde la página inicial de Google Colab, y con la sesión de Google iniciada, haremos Archivo > Nuevo cuaderno. Veremos como el aspecto de Google Colab es realmente similar a Jupyter Notebook 



Es importante saber que todos los cuadernos de Google Colab que creemos serán almacenados en el Google Drive asociado a la cuenta de Google con la que hemos iniciado sesión en esta herramienta. Por tanto, podremos volver a ellos en cualquier momento bien desde la aplicación de Google Colab, o bien desde nuestra unidad en drive, donde veremos archivos con el símbolo del infinito dorado, que serán los que podremos abrir directamente con Google Colab haciendo doble click sobre ellos. 

139 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Vamos a tratar de descargar por código una imagen desde una URL determinada, aprovechando que estamos conectados a internet con la máquina virtual que corre por debajo de nuestro Google Colab, introduciendo el siguiente código en la primera celda. Después, ejecutaremos la celda con el botón play . Anteriormente estas imágenes las descargábamos de forma manual en nuestro sistema, pero Google Colab no nos proporciona un navegador de archivos, por lo que es más sencillo almacenar en la máquina la imagen desde un código en Python. Para hacerlo usaremos la función `io.` read de `skimage` , que nos permite descargar una imagen desde una url para directamente poder mostrarla por pantalla gracias a `matplotlib.pyploy (plt)` , como vemos en el siguiente fragmento de código. 



El resultado debería ser como el que se muestra en la siguiente imagen. 



140 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Vamos ahora a tratar de extraer el histograma de esta imagen, tal y como hicimos en uno de nuestros primeros ejemplos en la unidad anterior, y vamos a mostrarlo por pantalla. Para ello, usaremos como en aquel momento la función `ravel()` de Numpy y la función `hist()` de Pyplot. 

Creamos una nueva celda haciendo click en el botón e introducimos  en ella las siguientes dos líneas de código para ver el histograma de nuestra imagen. Después, ejecutaremos esta segunda celda pulsando el botón play . 



Veremos cómo el histograma indica que hay una gran cantidad de píxeles totalmente negros, y que el resto de la imagen está correctamente iluminada ya que las intensidades se reparten de una forma muy homogénea. 



Vamos por último a aprovechar una gran ventaja que ofrece Google Colab para el desarrollo de visión artificial: OpenCV para Python viene instalado de serie en las máquinas. Esto nos quitará potenciales problemas relacionados con versiones y facilitará las pruebas que podamos necesitar realizar con nuestros cuadernos de Google Colab. 

Para hacer esta prueba, vamos a tratar de buscar los bordes de nuestra imagen, gracias a la función `Canny()` de OpenCV, que ya hemos estudiado previamente. Crearemos una nueva celda de código e introduciremos el siguiente fragmento. Después, ejecutaremos este código. 



141 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Veremos que inmediatamente nuestro cuaderno de GoogleColab ejecuta la función correspondiente y nos devuelve una imagen con los bordes detectados mediante el método Canny, que deberá ser similar a la siguiente imagen. 



Como podemos comprobar, podemos ejecutar todos los ejemplos que hemos usado en esta asignatura hasta el momento en cuadernos de Google Colab, incluso empleando los mismos cuadernos ya que la extensión es la misma. Tan solo tendremos que subir los archivos “.ipynb” a nuestro Google Drive y abrirlos con Google Colab para así poder ejecutarlos de forma remota. 

**Los alumnos que han decidido comenzar empleando Google Colab observarán que no comprender ninguna de las funciones mostradas en este ejemplo. Esto no es importante ya que la clave para ellos es comprender cómo funciona Google Colab en términos de creación de cuadernos, de celdas de código y de ejecución.** 

### **3.2. Clasificación de objetos mediante técnicas clásicas** 

En la unidad introductoria vimos cómo la clasificación de objetos es uno de los objetivos básicos de la visión artificial. Este objetivo tiene innumerables aplicaciones. Por ejemplo, puede emplearse para realizar control de calidad de procesos industriales. Si colocamos una cámara a color encima de una línea de producción de tartas, podemos tener dos clases: “tarta_OK” y “tarta_NOK”, para automatizar la eliminación de la línea de producción de las tartas que no cumplan con los estándares de calidad de la compañía. 

También podemos emplearla para tratar de estimar la edad de una persona, si creamos una clase para cada década de vida, y entrenamos un modelo que dado un rostro humano nos devuelva la década estimada en la que se encuentra. 

142 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

O quizá queremos saber el modelo de una motocicleta que hemos visto por la calle, y creamos una aplicación que, dada una imagen de una motocicleta, nos devuelva su modelo y precio. 

En definitiva, la clasificación de objetos emplea una fotografía de un objeto, y le asocia una clase predeterminada. Por tanto, el número de salidas es discreto, es decir, está limitado. En el caso de las tartas tendremos 2 clases. En el caso de las edades, 10 clases. En el caso de las motocicletas tantas clases como motocicletas se encuentren en el mercado actual. 

En todos los casos, el _input_ de nuestro sistema será una imagen, y el _output_ un número asociado a la clase que el algoritmo estima que pertenece nuestra imagen. En el caso de las tartas si el algoritmo devuelve un ‘0’, la tarta continúa su viaje por la fábrica. Si el algoritmo devuelve un ‘1’, la tarta es descartada por motivos de calidad. 

La clasificación de objetos puede realizarse tanto por medio de algoritmos básicos de machine learning que beben de características seleccionadas manualmente mediante técnicas clásicas de visión artificial, o bien puede realizarse gracias a Redes Neuronales Convolucionales diseñadas y entrenadas para este fin. Vamos a ver ambos enfoques y a comparar sus ventajas y desventajas en función de las características del caso de uso al que nos enfrentemos, para así siempre poder tomar las mejores decisiones posibles a la hora de implantar un modelo en el mundo real. 

**3.2.1. Máquinas de vectores de soporte (SVM y K-Nearest Neighborhs** 

### **(KNN)** 

Las máquinas de vectores de soporte (SVM) son modelos de aprendizaje automático ( _machine learning_ ) que permiten solucionar problemas de clasificación y regresión. En este caso, nos centraremos en los problemas de clasificación. 

Ya hemos analizado en profundidad el funcionamiento de las SVM en la asignatura de “Machine Learning y Deep Learning” por lo que solo haremos un rápido repaso de las mismas a efectos de recordatorio. Una máquina de vectores de soporte (support-vector machine en inglés) para clasificación recibe una serie de datos etiquetados según su clase asociada, que conocemos como _training set_ o conjunto de entrenamiento. La SVM trata de encontrar la frontera que divide estos datos en el espacio, para así poder clasificar cualquier nuevo punto de datos en una de las clases predeterminadas.  Para hacer esto usa tantas dimensiones como sea necesario (y posible) para encontrar las fronteras en estas dimensiones, que determinarán a qué clase pertenece cada punto del conjunto de datos proporcionado. 

143 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En la siguiente imagen podemos ver un ejemplo de SVM procesando un conjunto de datos de 3 dimensiones y 2 clases, en las que es capaz de encontrar un plano que deja cada una de las clases a un lado, convirtiéndose así en un clasificador para este conjunto de datos. 



Para construir una SVM que cumpla un objetivo de clasificación de objetos, debemos convertir las imágenes – enormes matrices de datos en 3 o 4 dimensiones – en puntos. Para ello usaremos la extracción de características. Como ya hemos visto, algoritmos como ORB convierten imágenes en un conjunto de características binarizadas (1 y 0) que se asumen invariantes de forma global. Este es el tipo de dato perfecto para que una SVM trate de encontrar la diferencia entre nuestras clases en base a las características encontradas de todas ellas. 

Por ejemplo, en el ejemplo de la fábrica de tartas, el proceso sería como sigue: 

1. Necesitaríamos recopilar imágenes de tartas_OK y tartas_NOK en cantidades suficientes. Por ejemplo, podríamos tratar de buscar 100 imágenes de cada tipo. 

2. Para cada imagen, extraeríamos sus características con ORB, convirtiendo las imágenes en un vector de características. 

3. Lanzaríamos una SVM con la información de todas las imágenes y su clase asociada. La SVM llegaría a un _fit_ con el que podríamos realizar la inferencia. 

4. Para cualquier imagen nueva, deberíamos extraer sus características con ORB y pasárselas a la SVM. La SVM inferiría una clase, y nos devolvería un resultado con el que podríamos tomar una decisión. 

Con esto, el objetivo de clasificación de objetos estaría cubierto. 

144 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

De igual forma que hemos aplicado el proceso con una SVM, podríamos aplicarlo con un modelo de K-Nearest Neighbors, que también hemos estudiado en la asignatura de “Machine Learning y Deep Learning”. Este algoritmo, que asume que los objetos que comparten clase deben ser los que más cerca están, emplea una medida de distancia entre los distintos datos de nuestro _training set_ . Una vez analizada la distancia entre las características de nuestros datos, dos a dos, tendrá la distancia de cada punto a los demás. Conociendo el número de clases, trata entonces de seleccionar tantos grupos de datos como clases se requieran, uniéndolos por la proximidad entre ellos. 

Por ejemplo, la ejecución de un algoritmo KNN sobre un conjunto de imágenes de flores en las que hemos extraído las características “largo de pétalo” y “ancho de pétalo”, que pertenecen a uno de tres tipos de flores Iris capturados ( _Setosal, Versicolor, Virginica_ ), daría como resultado la siguiente separación del espacio para tratar de ejecutar una clasificación de futuras flores conociendo las dimensiones de sus pétalos. 



Como vemos, la lógica detrás de KNN y de SVM es realmente similar. Necesitaremos un conjunto de datos etiquetados de los que hayamos extraído una serie de características visuales. Posteriormente, usaremos la descripción numérica de estas características – por alguno de los métodos que hemos estudiado – para entrenar uno de estos dos modelos de _machine learning_ . Si tenemos suerte, acabaremos teniendo un modelo que, dada una imagen y sus características, clasifique de forma automática y precisa la tipología a la que pertenece. Hay infinidad de modelos de clasificación “espacial” que emplean diversas dimensiones para hallar fronteras entre nuestros datos etiquetados que nos permitan definir matemáticamente tantas clases como deseemos. 

145 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Cada uno de ellos genera superficies de decisión distintas en función de la aproximación que tenga, y nos permitirá aproximar distintos problemas de clasificación hasta dar con el mejor de ellos. Dado el escaso coste computacional de este tipo de modelos, habitualmente se trata de entrenar tantos clasificadores como sea posible para determinar el mejor modelo de _machine learning_ para nuestra problemática concreta. 

En la siguiente imagen podemos ver cómo diversos modelos de clasificación de _machine learning_ responden al mismo conjunto de datos, generando superficies de decisión totalmente distintas y mostrando por tanto la variedad expresiva de todos ellos. Como podemos observar hay dos patrones principales, uno que concentra la clase azul en el centro con forma circular (KNN, SVM, Naive Bayes, QDA), y otro que opta por una superficie rectangular casi cuadrada (Decision Tree, Random Forest, AdaBoost). Este es el motivo por el que deberemos probar tantos algoritmos como sea posible en caso de optar por un enfoque clásico basado en _machine learning_ para la clasificación de objetos. 



Diversos modelos de clasificación de ML y las superficies de clasificación que produce cada uno de ellos a modo de ejemplo de las diferencias entre ellos 

La realidad es que todos estos métodos clásicos de clasificación tienen una serie de desventajas que es esencial conocer. En esencia, debido a que se basan en una serie de características concretas, estas características pueden o no ser suficiente información como para que un modelo de ML pueda separar el espacio en tantas clases como se desee, abriendo la puerta a entrenamientos deficientes y resultados pobres. Las limitaciones por tanto son elevadas, ya que los resultados suelen ser muy prometedores en los conjuntos de entrenamiento, pero cuando se trata de llevar el modelo al mundo real, encontraremos que mínimas variaciones en la captura, la iluminación y el contraste pueden echar por tierra las métricas de precisión que podamos haber calculado. 

**Es por esto que este tipo de aproximación es principalmente empleado en casos industriales** , en los que el sistema se encuentra bajo unas condiciones totalmente controladas. Si tenemos una cámara ubicada sobre una línea de producción por la que pasa un único tipo de objeto (por ejemplo, nuestras tartas), con una velocidad e iluminación constantes y siempre desde la misma perspectiva, hay altas probabilidades de que diseñemos un modelo de visión artificial exitoso. 

146 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En otros sectores, por desgracia, la captura habitualmente no está tan controlada, y nos encontraremos con una gran variedad de dispositivos de captura, escenarios, iluminaciones, perspectivas y objetos que harán la tarea de clasificación realmente compleja por medio de técnicas clásicas. Es por ello que solo vamos a ver un método más de clasificación mediante técnicas clásicas de forma breve, los árboles de decisión, y pasaremos inmediatamente a tratar el mundo de las Redes Neuronales Convolucionales (CNN) que serán las que realmente nos permitan obtener modelos flexibles y robustos en condiciones no controladas y cambiantes. 

Podemos encontrar implementaciones de SVM, KNN y otros clasificadores lineales en la librería de Python `scikit-learn` . Esta librería ofrece todos estos modelos preparados para sencillamente ser alimentados por un conjunto de datos de entrenamiento y generar el modelo de clasificación correspondiente. En concreto encontramos en <u>este enlace</u> la información relativa a SVM para clasificación, y <u>en este otro enlace</u> la información relativa a KNN para clasificación. A partir de estos enlaces es relativamente sencillo navegar hasta la documentación del resto de algoritmos como los Random Forest, los Decision Trees o los AdaBoost. 

En todos los casos se proporcionan en esta documentación varios ejemplos preparados para ejecutar, así como una gran cantidad de teoría para poder comprender en profundidad el método que se desea usar. Es muy recomendable acceder a esta documentación y tratar de ejecutar alguno de los ejemplos en un Jupyter Notebook (para lo que habrá que instalar la librería `scikit-learn` en nuestro entorno), si bien es algo que queda fuera del alcance de esta asignatura y por tanto no vamos a profundizar más en ello. 

### **3.2.2. Árboles de decisión** 

En la sección anterior analizamos cómo partiendo de una serie de características descritas de nuestras imágenes podemos aplicar clasificadores de aprendizaje automático para automatizar la selección de la clase a la que pertenece cada imagen. Los modelos hasta el momento han sido clasificadores lineales, es decir, tratan de buscar una frontera entre cada una de las clases de datos, para así compartimentarlas y automatizar la decisión. Esta frontera puede ser en dos dimensiones (una línea), en tres dimensiones (un plano), o en múltiples dimensiones. Sin embargo, es solo una frontera, una única línea divisoria. La realidad de los datos en muchas ocasiones es más compleja que una simple línea para dividir nuestros datos. Si bien podemos diferenciar tipos de flores por el ancho y alto de sus pétalos, ¿creemos que podríamos hacer lo mismo para diferenciar tipos de vehículo? Necesitaríamos una gran cantidad de dimensiones – es decir, una gran cantidad de características – y aun así sería muy poco probable que encontráramos una línea que dividiera cada clase de forma estanca y con alta precisión. 

147 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Con este problema en mente surgen los árboles de decisión. Si en lugar de buscar una única frontera vamos tomando decisiones anidadas acerca de las características de nuestras imágenes, es mucho más probable que seamos capaces de determinar diversas clases con mayor precisión. Podemos imaginarnos un ejemplo de árbol de decisión en función de las características de una imagen para diferenciar vehículos para así visualizar el funcionamiento de este algoritmo. Pongamos que queremos saber si en una fotografía aparece un barco, un avión, una bicicleta, una motocicleta, un automóvil, un camión o un autobús. Seguramente, por muchas características que extraigamos, un modelo lineal como SVM o KNN no fuera capaz de separar correctamente clases realmente cercanas, como pueden ser las bicicletas y las motocicletas, o los autobuses y los camiones. Sin embargo, un árbol de decisión nos permite aumentar notablemente el número de fronteras que trazamos entre nuestras clases, gracias al anidado de las mismas. Observemos la siguiente imagen para comprender de forma visual lo que implica un árbol de decisión a la hora de clasificar objetos. 

Básicamente en cada paso del procesamiento de un árbol de decisión creamos dos subconjuntos por medio de una condición que puede ser verdadera o puede ser falsa. Esto se llaman arcos o ramas, que van pasando por distintos nodos. Al final del árbol se encuentran las hojas, que son nodos en los que no hay una condición, sino un resultado. En el caso de la clasificación de objetos las hojas serán los resultados de la clasificación, es decir, las clases en las que podemos llegar a clasificar nuestros objetos. 



148 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

De igual manera que en el caso de los clasificadores lineales como SVM y KNN, una de las librerías más completas para ejecutar árboles de decisión para clasificación es scikitlearn en Python. De nuevo, contamos con una documentación bastante completa en este <u>enlace, donde podemos consultar la teoría y los ejemplos básicos de implementación de</u> árboles de decisión para clasificación. Podemos probar a ejecutar estos ejemplos en un cuaderno de Jupyter Notebook o en un cuaderno de Google Colab si deseamos comprobar el funcionamiento de estos algoritmos desde una perspectiva más centrada en la programación de los mismos que en su teoría. 

Si bien los árboles de decisión son métodos más complejos que los clasificadores lineales, y que suelen mostrar resultados notablemente mejores que estos en problemas con múltiples clases y características relevantes, sigue siendo un método poco robusto y muy dependiente de las condiciones del entorno, por lo que según el caso de uso puede llegar a ser muy recomendable – como en ocasiones con condiciones de captura totalmente controladas y un gran número de clases y características – pero en otros muestra limitaciones importantes debido a su poca flexibilidad. Es por esto que vuelve a formar parte, como SVM y KNN, de los clasificadores empleados en industria y casos de uso controlados, pero que quedan lejos del alcance y precisión que ofrecen los modelos de aprendizaje profundo. Es por ello que nuestra siguiente sección por fin hará foco en esta tecnología. Hablaremos de Redes Neuronales Convolucionales. 

### **3.3. Clasificación de objetos mediante deep learning** 

### **3.3.1. Las redes neuronales convolucionales** 

A lo largo de la primera asignatura de este máster, “Introducción a la Inteligencia Artificial”, pudimos estudiar la cronología de las Redes Neuronales Convolucionales y la evolución del uso que se les ha dado a lo largo de las décadas. Refresquemos los hitos más importantes para poner en contexto esta tecnología, antes de profundizar en sus capacidades para la clasificación de objetos. 

En 1980, Kunihiko Fukushima introdujo las que serían – y son – las capas principales de una red neuronal convolucional: Las capas de convolución, y las capas de _downsampling_ . Como veremos a continuación, las capas convolucionales ejecutan una convolución – ya hemos visto este concepto en los kernel de las técnicas clásicas – sobre el resultado de la capa anterior. Por otra parte, las capas de _downsampling_ reducen el tamaño de la salida de la capa anterior mediante operaciones estadísticas como extraer el máximo, el mínimo, o la media. 

Fue en 1989 cuando el equipo de investigación de Yann LeCun propuso por primera vez el uso de estas dos capas para aplicarlos a un problema de visión artificial. Con su famoso experimento de los códigos postales, LeCun unió las CNN con el algoritmo de _backpropagation_ propuesto por Hinton años antes, para dar con el primer modelo de CNN de reconocimiento visual. Esta investigación sentó las bases de toda la visión artificial que vamos a ver desde este momento en adelante. 

149 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

El único problema que tenían las CNN en visión artificial era su gran complejidad. Debido a lo costoso de ejecutar el algoritmo de _backpropagation_ en los dispositivos computacionales de finales y principios de siglo, las CNN quedaron como una solución brillante, pero demasiado costosa como para ser implementada con éxito. 

Esto cambió con el último de los hitos históricos que vamos a repasar. A partir de 2004 se comenzó a estudiar la posibilidad de usar las unidades de procesamiento de gráficos (GPU) que hasta el momento se empleaban para la edición de video y el renderizado de gráficos tridimensionales, para entrenar modelos de redes neuronales. Se dieron casos de entrenamientos sobre GPU desde el año 2006, pero no fue hasta 2012 cuando el _deep learning_ aplicado a la visión artificial comenzó a ser la tecnología predominante en el sector. Esto sucedió cuando Alex Krizhevsky, estudiante doctoral de Hinton, diseñó y entrenó un modelo de CNN para clasificación de objetos conocido como AlexNet, que ganó el certamen de visión artificial ImageNet de 2012 por un amplio margen. AlexNet había sido entrenada en una GPU, y también realizaba su inferencia en esta tecnología. Tras esta gran noticia, el mundo de la visión artificial sufrió una gran sacudida, y comenzó a olvidar las técnicas clásicas en favor de las redes neuronales profundas. 

Ahora, más de una década después, la disciplina de la visión artificial está llegando a un equilibrio necesario. Tanto en el ámbito investigador como en el ámbito comercial, universidades y corporaciones han descubierto que, si bien el _deep learning_ ofrece unas capacidades jamás esperadas, trae consigo una serie de desventajas que se deben tener en cuenta. Es por ello que en la actualidad los proyectos de visión artificial seleccionan una técnica clásica o un modelo de aprendizaje profundo en función de las características del proyecto como pueden ser la cantidad de muestra disponible, la capacidad computacional del cliente, la necesidad de ejecutar un algoritmo en tiempo real, o lo controladas que están las condiciones de captura. 

No obstante, la gran mayoría de nuevos desarrollos de visión artificial se realizan sobre CNN y otros tipos de redes neuronales que veremos más adelante, por lo que, para estar en el estado del arte, tanto investigadores como empresas necesitan ser solventes en la selección, diseño y desarrollo de algoritmos de _deep learning_ de visión artificial. 

Vamos a tratar de comprender de forma intuitiva la idea que hay detrás de las capas convolucionales y de las capas de _downsampling_ que componen principalmente una CNN, ahora que comprendemos una gran cantidad de conceptos de visión artificial. 

Lo primero que debemos saber es que una Red Neuronal Convolucional (CNN) está compuesta por las mismas partes que hemos estudiado hasta ahora para la clasificación de objetos mediane técnicas clásicas y _machine learning_ , y todas ellas son ejecutadas de forma automática. 

150 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por un lado, a través de las primeras capas de neuronas de este tipo de redes neuronales, se extraen las características más relevantes de la imagen, las _features_ . Estas _features_ **son las mismas que hemos estudiado hasta ahora** . La gran diferencia es que en este caso no las seleccionamos nosotros (bordes, esquinas, contornos, líneas), ni diseñamos un algoritmo que las seleccione mediante un sistema de votación (SIFT, SURF, ORB). Delegamos esta tarea en la red neuronal, despreocupándonos de la selección de características. Esta es la tarea principal de las capas de convolución y de _downsampling_ : extraer las características más relevantes de las imágenes de entrenamiento de forma automática. 

Por otro lado, en las últimas capas de red neuronal se produce la clasificación en base a las _features_ previamente extraídas. Esto es muy similar a la aproximación de alimentar un modelo de _machine learning_ (SVM, KNN, _Decision Tree_ ) con características extraídas manualmente. Pero en este caso no seleccionamos las características ni el algoritmo clasificador. Todo sucede dentro de la red neuronal, que se convierte en una caja negra. El programador introduce imágenes en la red neuronal, y espera que esta sea capaz de clasificarlas, aplicando las distintas capas neuronales disponibles hasta llegar a un resultado. 



#### **Capa de convolución** 

La capa de convolución, que da nombre a este tipo de red neuronal, tiene exactamente el mismo tipo de funcionamiento que la convolución de un kernel para filtrar una imagen, o para buscar bordes, que vimos en la unidad anterior, pero en este caso los valores del kernel no vienen definidos por el desarrollador, sino que es la red neuronal las que los decide y aprende gracias al entrenamiento por medio del algoritmo de _backpropagation_ . 

Recordemos que una neurona no es más que un operador matemático que tiene una serie de entradas a las que se aplica un peso determinado ( _weight_ ) para ponderar cada una de ellas. Después de multiplicar cada entrada por su peso, se suman todas las entradas. Por último, se aplica una función que determina el resultado final de la operación. Este mismo proceso es exactamente el que se realiza con la aplicación de un kernel, por lo que lo veremos representado de dos formas indistintamente. 

151 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Pongamos que tenemos una imagen de 5x5 pixeles binarizada – es decir, que solo está formada por 1 y 0 – como la que vemos a la izquierda de la imagen. Si aplicamos un kernel de convolución de 3x3 con los valores que vemos en rojo (también 1 y 0) a la primera ventana de 3x3 disponible en nuestra imagen (resaltada en amarillo) obtendríamos el valor de 4 (resaltado en rosa). Recordemos que para aplicar este kernel haríamos la siguiente operación. 

#### 1x1+1x0+1x1+0x0+1x1+1x0+0x1+0x0+1x1=4 

Si queremos representar este mismo comportamiento en forma de neurona artificial, el diagrama sería el de la derecha. Tendríamos una neurona de 9 entradas, cada una de ellas con su peso, que corresponden a los valores del kernel de 3x3. La función de esta neurona es el sumatorio, representado en su interior. Por tanto, si introducimos en cada entrada de nuestra neuronal un pixel de la ventana de 3x3 (amarillo) por orden, obtenemos el mismo resultado que si aplicamos el kernel. Veremos en la literatura científica y divulgativa ambas representaciones indistintamente, lo importante es recordar que **la operación es exactamente la misma** . Estaremos convolucionando un kernel a lo largo de una imagen, hasta obtener una matriz con el resultado de este kernel. Es importante notar una diferencia frente a los kernels de filtrado o de extracción de bordes: En las convoluciones de las CNN **no hay un resultado por cada pixel analizado, sino un resultado por cada ventana** . Si recordamos la explicación de los kernels en las técnicas clásicas, cada pixel de la imagen de entrada tenía una correspondencia en la imagen de salida (es decir, una imagen de 32x32 pixeles de entrada, produce una imagen de 32x32 pixeles de salida). En este caso, no estamos filtrando imágenes, sino buscando características que **resuman** la imagen. Es por ello que obtendremos un resultado por cada ejecución de nuestro kernel sobre una ventana (amarilla en los ejemplos). 

El kernel puede deslizarse una serie de píxeles hacia la derecha y hacia abajo según lo indique el programador. En este ejemplo, el kernel solo se desplaza 1 pixel cada vez, es decir, una fila cada vez, y una columna cada vez. 

152 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Es mucho más sencillo verlo de forma visual, tal y como vemos en la siguiente imagen. En una imagen de 5x5 píxeles solo somos capaces de mover una ventana de 3x3 un total de 9 veces si la movemos un píxel cada vez. La ventana siempre tiene que ser completa y no puede emplear pixeles que no existen, o que quedarían fuera de la imagen real. De esta forma podemos entender una convolución como un extractor de características (de igual forma que los kernels que ya hemos estudiado), pero también como una forma de “resumir” una imagen, o de reducir sus dimensiones. Si de una imagen de 5x5 obtenemos una matriz de 3x3 que tiene características esenciales, estaremos reduciendo la cantidad de información, pero mejorando enormemente la calidad de esta, acercándonos así a nuestro objetivo, que en este caso es clasificar objetos, pero podrá ser detectarlos o segmentarlos, como veremos más adelante. 



Como podemos ver, en cada paso de la convolución se selecciona una ventana (amarilla) que se multiplica por el kernel, se computa el resultado, y se almacena en la posición correspondiente de la matriz de salida (rosa) hasta que toda la imagen ha sido convolucionada. 

Supongamos ahora que nuestra imagen ya no es binaria, sino que es una imagen a color con una profundidad de 8 bits, que es el caso más habitual que nos encontraremos en el mundo real. Recordemos del principio de esta asignatura que esto significa que tenemos tres matrices, y que cada celda – o pixel – podrá tener un valor entre 0 y 255. La convolución en este caso funcionará exactamente igual para cada uno de los canales, pero se ejecutará tres veces. Pasaremos de tener un kernel a tener tres kernels, lo que también puede interpretarse como que tenemos un kernel de 3 dimensiones, para adecuarse a las características de nuestra imagen. 

153 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Este es el único requisito para que las convoluciones con varias dimensiones funcionen. La capa convolucional debe tener la misma profundidad que las imágenes con las que va a trabajar, en este caso una imagen RGB necesitará kernels de 3 en 3, ya que cada uno se aplicará a su canal De forma intuitiva podemos pensar que es necesario un kernel para cada canal, y que al final se suman los resultados de aplicar a cada canal su kernel. 

En cada paso de la convolución multiplicaremos cada ventana de cada canal (R, G y B) por su kernel correspondiente, lo que arrojará tres matrices, y posteriormente sumaremos las tres matrices para obtener una única matriz que será el resultado. Tendremos por tanto una matriz bidimensional en cada paso de la convolución. 

Veamos un ejemplo: Si tenemos una imagen en RGB de 5x5 píxeles, nuestra imagen en realidad será una matriz de 5(alto)x5(ancho)x3(canales). Dado que tenemos 3 canales, necesitamos un kernel formado por 3 matrices. Imaginemos que tenemos un kernel de 3(alto)x 3(ancho) x 3(canales). Representemos esto de la siguiente manera: 



Para convolucionar esta imagen de 3 canales, haremos lo siguiente: 

- Cogeremos una ventana de 3x3 en cada uno de los canales disponibles (rojo, verde y azul) y la multiplicaremos por su kernel correspondiente. Esto nos dará **un único número por cada canal** , o lo que es lo mismo, tres números. 

- Seguiremos convolucionando – moviendo por orden – la ventana para ir aplicando el kernel sobre nuestra imagen, con la política que deseemos – asumamos que movemos 1 pixel a la derecha y hacia abajo cada vez – lo que nos seguirá dando 3 números cada vez (un único número por canal). 

- Finalmente, cuando hayamos realizado todas las convoluciones, tendremos un resultado de 3 matrices de 3x3, que en la siguiente imagen se representan como matrices roja, azul y verde atenuados. Esto sería igual que si realizáramos tres veces el proceso que hemos visto en la imagen anterior, una vez por cada uno de los canales. Ahora, sumaremos los elementos correspondientes de las tres matrices de salida entre sí. 

154 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Es decir, sumaremos las tres posiciones de arriba a la izquierda, y guardaremos el valor en una matriz de salida de 3x3 posiciones en la posición de arriba a la izquierda. Después, sumaremos las tres posiciones de arriba en el centro y guardaremos el valor en una matriz de salida en su posición de arriba en el centro. Siguiendo con este proceso para todas las posiciones, acabaremos con una única matriz de 3x3x1. Este es el resultado de una convolución sobre una imagen RGB. 



Este funcionamiento que acabamos de analizar es el de **una única neurona** de convolución. Para formar una **capa de neuronas convolucional** sencillamente aplicaremos en el mismo momento múltiples convoluciones de distintos kernels. Cada uno de estos kernels acabará buscando una característica específica de las imágenes: un borde, una esquina, una sombra, un brillo… 

En definitiva, la imagen pasará por _n_ neuronas convolucionales, tantas como tenga la capa. Veamos como ejemplo la primera capa de convolución de una red neuronal convolucional para la detección de objetos. 



155 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En este caso tenemos una imagen de entrada de 32x32 píxeles. Es probable que esta imagen nos resulte conocida, ya que está extraída de la base de datos MNIST de códigos postales manuscritos, de la que hablamos durante la primera asignatura introductoria de este máster. El objetivo de esta CNN es, por tanto, clasificar dígitos. 

En esta red neuronal, la **primera capa (C1)** , está formada por 6 convoluciones de kernels de 5x5 píxeles. La convolución de cada uno de estos kernels a lo largo de la imagen de entrada produce una matriz de salida para cada neurona de tamaño 28x28. O dicho de otra forma, cada neurona de esta capa devuelve una matriz de 28x28. 

Esto significa que la salida de esta primera capa de neuronas está formada por 6 matrices (una por cada neurona) de 28x28 posiciones (el resultado de convolucionar un kernel de 5x5 a lo largo de una matriz de 32x32). Esta matriz, resultado de la ejecución de una capa convolucional de una CNN se denomina **_feature map_** , o mapa de características, ya que es precisamente lo que buscamos con la ejecución de una capa neuronal. Estamos tratando de **extraer características** de la imagen **de forma automática** gracias a nuestras neuronas convolucionales. 

Los valores de nuestro kernel **no son seleccionados por nosotros** , sino que la red neuronal los aprende automáticamente **gracias al algoritmo de** **_backpropagation_** . Habitualmente estos valores comienzan en valores aleatorios, y mediante el proceso de entrenamiento la CNN los va ajustando para aumentar su precisión al máximo. Este es el gran valor de las redes neuronales basadas en _deep learning_ frente a cualquier método clásico de extracción de características. Podemos ejecutar tantos kernels de búsqueda de características como queramos, sin que esto implique un esfuerzo manual por definirlos para las características que el desarrollador considere oportunas. 

Gracias a este primer paso, ejecutado por una capa convolucional, hemos convertido nuestra imagen de entrada en 6 mapas de características que se han generado automáticamente, y que podremos usar para realizar la clasificación de objetos. Pero, como podemos ver, la siguiente capa de nuestra red neuronal es una capa de _subsampling_ . En la siguiente sección analizaremos para qué sirven este tipo de capas. 

#### **Capa de** **_downsampling, subsampling o pooling_** 

Ya hemos visto el funcionamiento de una capa convolucional, que está orientada a resumir las características de nuestra imagen de forma totalmente automática. El problema con el que nos encontramos en este punto es que tenemos 6 matrices de características de nuestra imagen de entrada. Esto es una cantidad de datos ingente comparada con la salida que esperamos: una salida en forma de una clase entre el 0 y el 9. Tenemos que ser capaces de ir condensando la información que tenemos en estos mapas de características para conseguir reducirlas a único número entre el 0 y el 9. En el caso de cualquier otro ejemplo, este número dependerá del número de clases. Cualquier red neuronal convolucional (CNN) de detección de objetos perseguirá que su salida sea un número, que indicará la clase detectada. 

156 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Para conseguir reducir la cantidad de información que proporciona una capa convolucional, se suele usar acto seguido una capa de _downsampling_ , también llamada _subsampling_ ambas derivadas de la idea de reducir las dimensiones de una matriz; más comúnmente conocidas como _pooling_ por el método que se emplea para lograr este objetivo. El propósito de estas capas es sencillamente resumir la información generada por las capas convolucionales en los _feature maps_ para así acercarse a la salida deseada de nuestra red neuronal. 

La operación más habitual por medio de la cual se realiza esta función se llama _pooling_ . Básicamente el _pooling_ es cualquier operación estadística que permita resumir el contenido de una matriz obteniendo otra matriz más pequeña. El reto en visión artificial, y por tanto en el diseño de las capas de _pooling_ en una CNN, es conseguir que no se pierdan características relevantes para nuestro objetivo visual. Si mediante la aplicación de una operación de _pooling_ perdemos bordes esenciales para la detección de una de nuestras clases, no será la operación adecuada, por mucho que resuma información de forma eficaz. En el _pooling_ también tendremos una ventana de aplicación cuyo tamaño decidirá el programador. Por ejemplo, esta ventana puede ser de 3x3, 5x5, 7x7… 

En este caso, no habrá un kernel, sino una operación matemática, habitualmente una función estadística. Aplicaremos esta función a todos los píxeles que entran dentro de la ventana seleccionada, y obtendremos un resultado para la ejecución de dicha ventana. Lo veremos más claro con los ejemplos concretos que se mostrarán a continuación. 

Hay dos tipos principales de _pooling_ para realizar _downsampling o subsampling_ : 

- Max _pooling_ : El método de _max pooling_ consiste en emplear el valor máximo de todos aquellos que han cabido en la ventana seleccionada, como se ve en la siguiente imagen. Como vemos, en este caso sencillamente se aplica una ventana de 3x3 sobre una imagen de 5x5. Para cada conjunto de 9 píxeles que caben en la ventana, se selecciona el mayor, en este caso el 221. Desplazaremos esta ventana por toda la matriz hasta obtener el resultado, con el mayor número de cada ventana en la matriz de salida (rosa). 



157 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- _Average pooling:_ En este caso, en lugar de seleccionar el mayor valor, seleccionaremos el valor medio. Para ello, sumaremos todos los valores de la ventana y dividiremos por el número de píxeles de nuestra ventana, que en este caso sería realizar la siguiente operación: 



Por lo que el resultado del _average pooling_ sobre nuestro _feature map_ anterior, sería el siguiente: 



Como vemos, con ambos métodos hemos sido capaces de convertir un _feature map_ de 5x5 posiciones en otro de 3x3, reduciendo así notablemente la cantidad de información con la que trabajamos. Recordemos que en este caso no estamos extrayendo ninguna característica, sino que estamos tratando de resumir estas características mediante una reducción de sus dimensiones. 

Si analizamos ahora la continuación de la CNN que hemos visto antes, podremos observar que ya comprendemos todo el proceso de extracción automática de características de una CNN básica. A partir de este punto, la estrategia es ir sucediendo capas convolucionales y capas de _pooling_ para continuar extrayendo características mientras que reducimos las dimensiones. Esta es una de las grandes fortalezas de las CNN: extraen características de la extracción de características. Si nos fijamos, aplicamos capas convolucionales a la salida de capas de _pooling_ , lo que quiere decir que estamos buscando características en _feature maps_ previos. Gracias a esto, las CNN pueden detectar características mucho más complejas de las que detectan las técnicas clásicas. Si en las primeras capas se suelen buscar bordes, esquinas, colores o líneas, en posteriores capas convolucionales se ha demostrado que las CNN buscan composiciones de objetos, elementos abstractos (como ruedas, puertas o ventanas), y por tanto alcanzan un conocimiento mucho más complejo y abstracto que las técnicas clásicas que no están basadas en _deep learning_ . 

158 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Analicemos con detalle la parte de extracción de características ( _feature extraction_ ) de esta red neuronal. Hasta el momento habíamos llegado a tener 6 _feature maps_ de 28x28. 

En el siguiente paso se aplica una capa de _pooling_ con una ventana de 2x2, lo que da como resultado el resumen de estos mismos 6 _feature maps_ en forma de mapas de dimensión reducida hasta 14x14 **(S1)** . Hemos conseguido reducir a la mitad la dimensión de estos mapas de características y por tanto nos hemos aproximado a nuestro objetivo. 

En la siguiente capa de red neuronal contamos con 16 neuronas convolucionales que emplean kernels de 5x5 posiciones. Esto nos deja con 16 _feature maps_ de 10x10 posiciones cada uno **(C2)** . Hemos extraído características de los _feature maps_ anteriores a la par que hemos resumido la información que estos contenían. Por último, aplicaremos una última capa de _pooling_ de nuevo con una ventana de 2x2. Este será el último paso de la extracción automática de características, y dará como resultado 16 _feature maps_ resumidos al reducir sus dimensiones a 5x5 posiciones **(S2)** . 

En resumen, hemos convertido una imagen de 32x32 píxeles en 16 mapas de características de 5x5. La duda ahora es, ¿cómo pasamos de este punto a una clasificación de un dígito entre el 0 y el 9? Para eso necesitaremos las capas totalmente conectadas, o Fully Connected Layers. 

#### **Capas totalmente conectadas (** **_FC_ )** 

Hasta este momento hemos llegado a tener una serie de _feature maps_ de tamaño muy reducido, que son la extracción compleja y abstracta de características de nuestra imagen inicial con una gran reducción dimensional. Recordemos que nuestro objetivo es que la red neuronal devuelva una clase concreta de entre un conjunto de clases previamente definidas y etiquetadas. Para pasar de estos pequeños _feature maps_ a la clasificación, debemos pasar por la última zona de nuestra red neuronal que está orientada a la **aplicación del objetivo** , en este caso es la **clasificación** . 

159 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En esta fase de nuestra red neuronal convolucional emplearemos las conocidas como capas totalmente conectadas (o _fully connected layers_ ). Este tipo de capa es en esencia una red neuronal básica, conocida como _feed forward neural network_ . No tendremos ventanas, kernels ni convoluciones. Sencillamente neuronas que reciben entradas, las multiplican por sus pesos, y se activan o no en función del resultado que obtengan de su función de activación. 

Para poder alimentar a esta capa, debemos convertir nuestras matrices – es decir, los _feature maps_ del final de la fase de _feature extraction_ – en vectores aplanados (conocidos como _flattened_ ) para que puedan ser leídos por las neuronas artificiales. 

Todos los valores de este vector aplanado pasarán por la capa totalmente conectada – de ahí su nombre – a diferencia de una capa convolucional, en la que este proceso se realiza a nivel de ventana. En realidad, esta capa podría ser cualquier clasificador lineal (como SVM, KNN, Árboles de decisión…). Sin embargo, se emplea una capa de neuronas artificiales básicas para lograr entrenar nuestro modelo de punto a punto, incluyendo tanto la extracción de características como la clasificación en un mismo proceso de entrenamiento. Es decir, basando ambos pasos en _deep learning_ , conseguimos un modelo entrenable mediante _backpropagation_ en su totalidad. En la siguiente imagen podemos observar el proceso de aplanamiento de un _feature map_ y su consiguiente paso completo por la capa _Fully Connected_ . 

Para simplificar el ejemplo, supongamos que la salida de la extracción de características de una CNN ha consistido en 2 _feature maps_ que tras la reducción de dimensiones tienen un tamaño de 2x2. En esta CNN contaremos con dos capas totalmente conectadas (FC), la primera consta de seis neuronas, y la segunda de dos neuronas. 

El primer paso, como vemos, consiste en aplanar los _feature maps_ para convertirlos en un único array unidimensional. Cada uno de los valores de este array unidimensional **está conectado con todas** las neuronas artificiales de la segunda capa. De aquí el nombre “f _ully connected_ ”. Tras esta primera capa hemos transformado nuestro vector de entrada (8 posiciones) en un vector de 4 posiciones – una posición por cada _output_ de cada neurona – que será la entrada de la siguiente capa totalmente conectada. 

160 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Esta última capa, resaltada en naranja, es la encargada final de realizar la clasificación. En este caso, contamos con una última capa formada de dos neuronas, por lo que este modelo de CNN trabaja con dos clases. Cada una de estas neuronas está asociada a una de las dos clases. Pongamos que la neurona superior está asociada a la clase “gato”, y la neurona inferior está asociada a la clase “perro”. 

Cada una de las salidas de las neuronas de la primera capa (amarillo) están conectadas con la entrada de todas las neuronas de la segunda capa (naranja), por lo que seguimos trabajando con una capa de neuronas totalmente conectadas. Tras procesar las entradas con sus correspondientes pesos y función de activación, las neuronas de la última capa ofrecerán un número entre 0 y 1, que será la probabilidad de que la imagen que entró inicialmente en la red neuronal pertenezca a su clase. En este caso, la primera neurona, que hemos asociado con “gato”, indica que cree que hay un 98% de probabilidad de que la imagen de entrada en la CNN fuera un gato. La segunda neurona, por el contrario, indica que solo hay un 2% de probabilidades de que fuera un perro. El resultado de la aplicación del objeto y, por tanto, de la clasificación, sería en este caso una etiqueta “gato” a la imagen asociada. 

161 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En definitiva, hemos aplicado finalmente nuestro objetivo. Para ello hemos usado tres componentes principales. 

1. Capas convolucionales. Estas capas, formadas por neuronas que deslizan un kernel a lo largo de una imagen de entrada, son las encargadas de extraer las características de la imagen. Las más cercanas al comienzo de la red extraen características más básicas (líneas, bordes, sombras), y aquellas más alejadas extraen conocimiento abstracto (posiciones relativas, objetos y formas, partes de objetos). 

2. Capas de _pooling._ Estas capas son las encargadas de reducir dimensionalmente los mapas de características extraídos por las capas convolucionales, para así permitir en última instancia aplicar una capa totalmente conectada de forma eficaz para clasificar el objeto. No están compuestas por neuronas. 

3. Capas _fully connected_ . Estas capas, al final de la red neuronal, procesan los mapas de características finales para tratar de clasificar el objeto. Convierten matrices en vectores unidimensionales hasta que acaban obteniendo la probabilidad de que el objeto pertenezca a cada una de las clases para las que ha sido entrenada la CNN. 

Al fin, podemos comprender el funcionamiento completo de nuestra red de clasificación de códigos postales manuscritos de MNIST. Observemos como en su última zona, la delimitada como “ _classification_ ”, contamos con dos capas de neuronas totalmente conectadas que trabajan con el vector aplanado resultante de aplanar los mapas de características de 5x5 que vemos en **S2** . En la última capa totalmente conectada ( **n2** ) contamos con diez neuronas. Esto quiere decir que cada una de ellas computará la probabilidad de que el dígito de entrada pertenezca a la clase que representan. En el caso de nuestra imagen de entrada, que es un 3, la neurona más excitada – es decir, aquella que compute una probabilidad más alta – será la cuarta neurona, que representa el dígito “3”. Hemos conseguido convertir una imagen de 32x32 píxeles en blanco y negro en una clasificación de objetos precisa y certera, que es capaz de indicarnos el tipo de dígito que está contenido en nuestra imagen. 



162 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

#### **Proceso de entrenamiento: Backpropagation y Stochastic Gradient Descent** 

Las capas convolucionales y las capas totalmente conectadas están formadas por neuronas artificiales, lo único que cambia entre ellas es la forma de aplicarlas, bien sea deslizando una ventana por la imagen ( _convolution_ ), o conectando todo un vector de entrada a las entradas de una neurona de una única vez ( _fully connected_ ). Las capas de pooling son sencillamente funciones estadísticas, por lo que no se consideran neuronas artificiales y quedan fuera del proceso de entrenamiento. 

Como ya hemos explicado numerosas veces, estas neuronas tienen una serie de parámetros esenciales que las definen, que son: 

- El número de entradas ( _inputs_ ). Cuántos dígitos son capaces de procesar en una única ejecución. 

- Los pesos ( _weights_ ) de cada entrada. El valor ponderado que se asocia a cada una de las entradas. 

- La función de suma ( _net input function_ ): Que suma de forma ponderada todas las entradas multiplicadas por sus pesos. 

- La función de activación. Es la función matemática que, aplicada a la suma de las entradas ponderadas, decide el resultado de la ejecución de la neurona. Esta función suele ser una función no lineal, por ejemplo, una sigmoide. Esta salida estará comprendida siempre entre 0 y 1. 

- La salida ( _output_ ). Que es única, y determina el resultado final. 

Esto podemos observarlo en la siguiente imagen. 



El algoritmo de _backpropagation_ propuesto por Hinton cambió las posibilidades de las redes neuronales artificiales (ANN) incluyendo las redes neuronales convolucionales (CNN). Hasta aquel momento, los pesos de cada una de las neuronas debían ser seleccionados a mano. Esto implicaría que el proceso de emplear redes neuronales profundas para visión artificial sería muy similar al proceso seguido por las técnicas clásicas, decidiendo qué características debía extraer cada neurona de convolución, pero además sería realmente poco intuitivo hacerlo. 

163 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Sin embargo, gracias a la retropropagación ( _backpropagation_ ), las redes neuronales adquirieron la posibilidad de **aprender** . El proceso de entrenamiento (CNN), desde un nivel absolutamente abstracto, consiste en lo siguiente: 

1. Inicializar la red neuronal con un conocimiento totalmente aleatorio 

2. Mostrarle a la red neuronal imágenes para que trate de clasificarlas en base a su conocimiento aleatorio. Devolverá clases aleatorias para estas imágenes. 

3. Comparar el resultado que hemos obtenido en estas imágenes con el _ground-truth_ que conocemos de ellas. Es decir, comparar las expectativas con la realidad. 

4. Informar a la CNN de los errores que ha cometido para que trate de actualizar su conocimiento de tal forma que estos errores se reduzcan. 

5. Volver a enseñarle un set de imágenes, y seguir haciéndolo hasta que el error haya sido reducido al mínimo (y por tanto la precisión sea máxima). 

Ahora bien, ¿cómo conseguimos que la red neuronal sea capaz de aprender de sus errores actualizando su conocimiento? Partiendo de que el conocimiento de la red neuronal se limita a los pesos de cada una de sus neuronas, el problema se reduce a actualizar el valor de estos pesos para que el resultado de la CNN sea cada vez más preciso. 

Es, en definitiva, un proceso de optimización, en el que tratamos de minimizar el error que comete la CNN modificando los parámetros de peso en todas las neuronas. El algoritmo de _backpropagation_ define cómo este error debe ser trasladado desde las capas más cercanas al resultado (en nuestro caso las _fully connected_ ) hasta las primeras capas (en nuestro caso las convolucionales). Dado que esta asignatura se ha planteado sin afán matemático, no se pretende profundizar en las bases algorítmicas de esta idea. En caso de que algún alumno desee profundizar en su funcionamiento, se recomienda acudir a la fuente original y leer el artículo de 1986 “ _Learning representations by back-propagating errors_ ”, que puede encontrarse, entre otros lugares, en este enlace. Hay también numerosos artículos online en los que este _paper_ es analizado minuciosamente desde una perspectiva matemática. 

Una vez se ha definido cómo se traslada el error hacia atrás, es necesario contar con un algoritmo que ejecute la optimización propiamente dicha. El algoritmo más empleado a este efecto en las CNN se denomina Stochastic Gradient Descent (SGD). Este algoritmo trata de encontrar el punto mínimo en el que, en función del valor de los pesos de las neuronas, la precisión se maximiza (o lo que es lo mismo, el error se minimiza). 

164 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Uno de los mayores retos de este algoritmo de entrenamiento son los mínimos locales. Si sencillamente perseguimos encontrar mínimos – que es un proceso que habitualmente se realiza analizando la derivada o gradiente ( _gradient_ ) – podemos quedar estancados en un mínimo local, que no es por tanto el punto óptimo de entrenamiento de nuestra CNN. Gracias a la _backpropagation_ , podemos calcular el gradiente de cada una de las neuronas y sus pesos. SGD, por su parte, trata de encontrar el mínimo absoluto del error relativo a cada uno de los _weights_ , como podemos observar en la siguiente figura. 



Lo que vemos en esta gráfica es como el error ( _loss_ ) varía en función del valor del peso de la entrada de la neurona que estamos actualizando ( _weight_ ). El algoritmo de Stochastic Gradient Descent trata de buscar el mínimo global de esta curva (en azul), ya que será el que maximice la precisión de nuestra CNN.  Podemos aprender más sobre los detalles matemáticos de esta combinación de algoritmos en una publicación abierta de la Universidad de Berlín que podemos encontrar <u>en este enlace.</u> 

En definitiva, gracias al proceso de entrenamiento de CNN, podemos obtener automáticamente los valores de extracción de características - en las neuronas de las capas convolucionales – y los valores del clasificador – en las neuronas de las capas totalmente conectadas – para conseguir realizar automáticamente la tarea de clasificación de objetos gracias al _deep learning_ . 

Este proceso es el que limitó realmente el desarrollo de las CNN en visión artificial hasta hace poco más de una década. Es este proceso que implica la ejecución de _backpropagation_ y SGD numerosas veces el que tiene tal requerimiento computacional que sin una GPU es imposible de realizar en un tiempo razonable. Pensemos que una red neuronal básica como puede ser la AlexNet cuenta con 660.00 neuronas que suman entre ellas un total de 61 millones de parámetros (es decir, de _weights_ individuales) y más de 600 millones de conexiones. Sin una gran potencia de cómputo es imposible actualizar tantos millones de parámetros. Gracias a las GPU, a NVIDIA y a CUDA, este proceso actualmente puede realizarse incluso en algunos dispositivos portátiles de altas prestaciones, lo cual era impensable hace tan solo quince años. 

165 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Ya hemos mencionado que la gran desventaja de las CNN frente a las técnicas clásicas viene dada por este proceso de entrenamiento. Para que el conjunto de _backpropagation_ y SGD sean capaces de entrenar correctamente nuestra red neuronal, necesitan **muchos ejemplos etiquetados** . Necesitaremos cientos de fotografías de gatos – si no miles – y otros tantos de fotografías de perros, con una etiqueta asociada, para poder aplicar correctamente estos algoritmos de entrenamiento. Si tenemos acceso a esta gran capacidad de captura de imágenes y etiquetado manual de las mismas, seguramente las técnicas de aprendizaje profundo sean las más adecuadas para nuestro problema de visión artificial. En caso contrario, es posible que tengamos que recurrir a técnicas clásicas, más manuales y poco flexibles, pero que funcionan desde el primer ejemplo para el que las programamos. 

### **3.3.2. Modelos de CNN para clasificación de objetos** 

Tenemos por tanto una estructura básica que conocemos como Red Neuronal Convolucional (CNN) que es capaz de aprender de forma autónoma las características visuales que debe extraer de las imágenes para poder clasificar estas en una serie de clases predefinidas. Esta estructura admite numerosas variaciones en función de las decisiones del desarrollador que incluyen: 

- Número de capas convolucionales, número de capas _pooling_ y número de capas _fully connected_ 

- Número de neuronas en cada capa de cada tipo 

- Tamaño de los kernels de cada una de las capas convolucionales y política de movimiento de la ventana de aplicación 

- Estrategia de _downsampling_ , tamaño y política de movimiento 

- Algoritmo de entrenamiento y parámetros del mismo 

En función de todas estas decisiones se pueden definir prácticamente infinitas arquitecturas de CNN. Los investigadores de visión artificial centrados en el _deep learning_ trabajan constantemente por encontrar las mejores combinaciones posibles para desarrollar las CNN más precisas posibles en función del tipo de problema. Para ello, emplean _datasets_ previamente etiquetados y estandarizados como ImageNet o PascalVOC, que mencionamos en la asignatura introductoria. 

Del entrenamiento y evaluación contra estas bases de imágenes, cada arquitectura obtiene un valor de precisión que determina por tanto su valor añadido frente a arquitecturas previas. Además, hay arquitecturas centradas en la eficiencia para poder ejecutarse en dispositivos móviles, y otras centradas en la precisión que requieren centenares de GPU en paralelo para poder ser entrenadas. Vamos a analizar alguna arquitectura de clasificación de objetos y, lo más importante, vamos a ponerla en práctica por primera vez, para ejecutar al fin un modelo de _deep learning_ de visión artificial. 

166 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En la siguiente tabla podemos consultar algunas de las CNN de clasificación que actualmente se consideran el estado del arte debido a que son las que tienen una mayor precisión en el reto de ImageNet. La columna “Top-1” se refiere a la precisión de la red a la hora de clasificar correctamente una imagen en la neurona que mayor probabilidad da. Es decir, es la precisión real. En el caso de “Top-5” se considera un acierto que la clase correcta se encuentre entre las 5 neuronas que mayores probabilidades dan, facilitando bastante el trabajo a la CNN. Después podemos analizar el número de parámetros y la profundidad de la red, es decir, el número de capas que emplea. Es interesante resaltar que a medida que la tecnología ha ido avanzando, un mayor número de parámetros y de capas no implica una mejor precisión, como podemos comprobar directamente en la tabla. VGG16 y VGG19 fueron de los primeros modelos de CNN orientados a la clasificación de objetos, y si bien a día de hoy siguen vigentes, son modelos con hasta seis veces más parámetros que otros más actuales que han conseguido obtener una mayor precisión, como puede ser Xception, o incluso redes mínimas orientadas a dispositivos móviles como MobileNetV2, que con menos de un 10% de parámetros obtiene la misma precisión que sus antecesoras. 



Vamos a ponernos manos a la obra para definir, entrenar y posteriormente clasificar objetos con nuestra primera Red Neuronal Convolucional. Para hacerlo, vamos a emplear la librería más extendida de _deep learning_ en la actualidad, llamada TensorFlow, que ya hemos mencionado muchas veces a lo largo del máster. Tensorflow cuenta con una API de alto nivel para construir modelos de IA sin necesidad de bajar a los fundamentos matemáticos de los mismos en Python, por lo que será nuestra plataforma ideal para comenzar. Tensorflow proporciona todas las funcionalidades de bajo nivel necesarias para construir nuestra propia CNN paso a paso, pero en este ejemplo usaremos Keras y sus modelos previamente diseñados para comprender el proceso de entrenar y ejecutar una CNN. 

Para ello, vamos a emplear un _dataset_ de imágenes conocido como Fashion MNIST. Este _dataset_ surge para actualizar la base de datos original de MNIST con dígitos manuscritos. En su lugar, es una base de imágenes de ropa, cada una de ellas con una etiqueta asociada. Estas imágenes tienen un tamaño de 28x28, lo que hace que tanto el entrenamiento como la inferencia sean realmente rápidos de realizar. Contaremos con 70.000 imágenes etiquetas entre diez clases – el mismo número de clases que la MNIST original. Esto nos indica que en la última capa de nuestra CNN habrá 10 neuronas. 

167 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Cada imagen tendrá por tanto una etiqueta formada por un dígito de entre 0 y 9, que se referirá a un tipo de ropa o complemento de moda. 

Vamos a abrir Google Colab y a crear un nuevo cuaderno. Nada más abrir el cuaderno, es esencial cambiar el tipo de entorno de ejecución, para indicar a Google que deseamos trabajar con una GPU, ya que vamos a entrenar una red neuronal convolucional. 

Para ello, abriremos el menú “Entorno de ejecución” y seleccionaremos la opción “Cambiar tipo de entorno de ejecución”. 



Se abrirá un modal en el que deberemos seleccionar aceleración de hardware mediante GPU como podemos ver en la imagen. Esto es muy importante, ya que de lo contrario el entrenamiento de nuestra CNN podrá tardar cerca de media hora si lo ejecutamos sobre una CPU. Hecho esto, vamos a ir creando distintas celdas de código para comenzar a definir nuestra primera red neuronal desde cero. 

168 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Primero, importaremos las librerías de Python necesarias para nuestro proyecto: 



Después, vamos a descargar el banco de imágenes y a preparar los conjuntos de entrenamiento y evaluación. Introducimos el siguiente fragmento de código en una nueva celda y ejecutamos esta celda para realizar dichas operaciones. 



Vamos a tratar de observar algunas imágenes del set de entrenamiento para visualizar cómo son estas fotografías de artículos de moda con las que tendrá que trabajar nuestra CNN. Para ello, vamos a usar la librería de pyplot, gracias a la cual podremos pintar por pantalla una matriz de 10 imágenes con sus clases asociadas. 



Esta matriz deberá ser como la siguiente, en la que vemos distintos ejemplos de artículos de moda junto a la etiqueta que tienen asociada en el banco de imágenes. 

169 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Vamos ahora a definir la arquitectura de nuestra CNN. Usaremos dos capas convolucionales, dos capas de _pooling_ y dos capas totalmente conectadas para llevar a cabo nuestra clasificación. Keras hace este proceso realmente sencillo, ya que basta con indicar las distintas capas que deseamos en nuestra red neuronal, así como el orden en el que queremos que se ejecuten, y la API de Keras compilará un modelo en Tensorflow por nosotros, para que podamos entrenarlo y emplearlo en el mundo real. Creamos por tanto una nueva celda de código, introducimos el siguiente, y lo ejecutamos para compilar nuestro modelo. 



170 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Tras la ejecución de esta celda tenemos en la variable “model” nuestra arquitectura de red neuronal, con sus dos capas convolucionales, dos _max poolings_ y dos capas totalmente conectadas, muy similar a la CNN que hemos empleado de ejemplo a lo largo de toda esta sección. 

Ahora queda uno de los pasos más importantes: el entrenamiento. Para realizarlo usaremos el método “fit” de nuestro modelo de Keras. Ya hemos definido nuestro conjunto de test y sus etiquetas, y nuestro conjunto de evaluación y sus etiquetas. Solo nos quedan dos parámetros del entrenamiento por definir para poder lanzar correctamente un entrenamiento. Estos son los siguientes: 

- _batch_ : El número de ejemplos que procesa la CNN antes de ejecutar el algoritmo de retropropagación y reducción de error. Si es demasiado pequeño, por ejemplo 1 – en este caso ajustamos los pesos con cada imagen – generaremos un ruido innecesario y será difícil que la CNN converja en un resultado adecuado. Por ello, tendremos que elegir un número suficiente como para que los errores sean significativos. Este parámetro tiene como valores habituales 32, 64, 128. 

- _epochs_ : Es el número de veces que se pasa por el conjunto completo de _training_ . 

En conjunto determinan cada cuanto se calcula el error y se optimiza, y la duración total del entrenamiento. En este caso vamos a usar un _batch_ de 64, lo que quiere decir que cada 64 imágenes la red tratará de ajustar sus pesos para mejorar la precisión. 

Usaremos 10 épocas por lo que pasaremos 10 veces por todo el conjunto de imágenes de entrenamiento. 

Crearemos una nueva celda de código e introduciremos el siguiente fragmento. Esta celda tardará un tiempo significativo en completarse y no debemos pararla mientras entrenamos nuestra CNN. Gracias a la aceleración por GPU de Google Colab veremos como cada época tarda tan solo unos segundos en completarse, por lo que el proceso completo de entrenamiento no superará los 2 minutos. A medida que la celda se ejecuta y por tanto la CNN se entrena, veremos una salida por pantalla indicando una serie de datos que analizaremos a continuación. 

171 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



En la salida de esta celda (ver la siguiente figura) podemos observar una serie de datos interesantes acerca del desarrollo de nuestro entrenamiento. Primero, se nos indica la época en la que nos encontramos. Después, se muestran los siguientes parámetros: 

- `ms/step` : El tiempo que ha tardado la CNN en procesar un batch (es decir, 64 imágenes) 

- `loss:` El error final calculado tras la ejecución de la época. Este valor deberá ir decreciendo para que consideremos que un entrenamiento está siendo satisfactorio. 

- `accuracy` : La precisión de nuestra CNN a medida que avanza el entrenamiento. Este valor deberá crecer para considerar un entrenamiento válido. 

- `val_loss` : El error calculado sobre el conjunto de evaluación. Dado que este conjunto no se emplea para entrenar es el mejor indicador de cómo evoluciona el error en nuestra CNN 

- `val_accuracy` : La precisión de la CNN sobre el conjunto de evaluación tras cada época de entrenamiento. Veremos como crece paulatinamente época tras época. 



Cuando lleguemos a la décima época, el proceso de entrenamiento terminará, y los pesos de nuestra red neuronal quedarán fijados. A continuación, vamos a medir la precisión final sobre el conjunto de evaluación, para obtener el % de acierto de nuestra red neuronal. Usaremos el método `evaluate()` de nuestro modelo de Keras. Para ello, creamos una nueva celda en Google Colab y añadimos en la misma el siguiente código, que acto seguido ejecutamos. 

172 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



La precisión de nuestro modelo debería rondar el 90% con una variación de aproximadamente 1% hacia arriba o hacia abajo. Esto quiere decir que nuestra CNN construida desde cero es capaz tras el entrenamiento de acertar 9 de cada 10 veces el tipo de artículo de moda que le estamos mostrando. Veamos este comportamiento en tiempo real para terminar este ejemplo. Vamos a emplear para ello 3 imágenes de nuestro set de evaluación. Calcularemos su clase mediante el método `predict()` de nuestro modelo de Keras. El resultado de este método es, como ya sabemos, la probabilidad de que nuestro objeto pertenezca a cada una de las distintas clases. Por tanto, será un vector de 10 posiciones, todas ellas comprendidas entre 0 y 1. Vamos a mostrar por pantalla cada una de las imágenes y el resultado de la predicción de nuestra CNN. La barra más alta será la de la clase que ha obtenido una mayor probabilidad, y por tanto la del resultado final de la clasificación de objetos de nuestro modelo. 

Crearemos una nueva celda de código en Google Colab e introduciremos el siguiente código. Al ejecutarlo, veremos la gran velocidad con la que nuestra CNN recién entrenada es capaz de inferir la clase de nuestros objetos, prácticamente en tiempo real. Es importante recordar que estamos empleando aceleración mediante GPU, y que es esta la responsable de la velocidad que muestra nuestro modelo. 



173 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



El resultado de esta ejecución variará notablemente entre los aquí presentados, así como entre distintos alumnos, así como la precisión estimada de la red. Esto se debe a que hay un cierto componente aleatorio en el entrenamiento, dependiendo del orden en el que se procesen las imágenes en los distintos _batches_ y por tanto cómo se calcula el error. Lo importante es comprender lo que significan los gráficos que obtenemos en esta última celda de código. Al lado de cada imagen podemos observar una serie de barras que indican la probabilidad que la CNN asocia a cada una de las clases en las imágenes de nuestro conjunto de entrenamiento. En algunos casos, la probabilidad de una clase roza el 100%, lo que quiere decir que nuestra CNN tiene la práctica certeza de que un determinado objeto pertenece a una clase. En otras ocasiones, veremos probabilidades mucho más dispersas, indicando las dudas de la CNN a la hora de asignar una clase a nuestro objeto. 



Con esto podemos concluir que hemos tenido éxito a la hora de diseñar, programar, entrenar y evaluar nuestra primera Red Neuronal Convolucional para clasificación de objetos. 

174 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por suerte, no siempre necesitaremos construir nuestra CNN desde cero. La mayoría de librerías de _deep learning_ ofrecen una categoría denominada _model zoo_ y en otras ocasiones _model hub_ , en el que los principales modelos de CNN – como los que hemos visto en la tabla anterior de precisiones – vienen desarrollados y listos para ser usados. Cuando deseemos implementar un proyecto de visión artificial por _deep learning_ lo más habitual es que seleccionemos la arquitectura que deseemos en función de sus fortalezas y debilidades, que podremos consultar en artículos científicos de metaanálisis y en la propia documentación de librerías como Tensorflow y Keras. Una vez seleccionado el modelo, trataremos de encontrar su implementación en la librería de nuestra preferencia. Estas implementaciones vienen preparadas para ejecutar un proceso de entrenamiento, evaluación e inferencia para aplicarlas directamente en proyectos reales. En la siguiente sección, orientada a detección de objetos mediante CNN, veremos el uso de _model hub_ de Tensorflow, que será idéntico para cualquier objetivo de visión artificial. 

En esta sección hemos analizado la construcción por bloques de una Red Neuronal Convolucional para clasificar objetos. Este fue el primer objetivo que se planteó para este tipo de modelos a principios de siglo, pero no ha sido el último ni mucho menos. En la siguiente sección veremos un objetivo con un punto más de complejidad y dificultad para nuestros algoritmos inteligentes: La detección de objetos. 

### **3.4. Detección de objetos mediante** **_deep learning_** 

Como ya sabemos, la clasificación de objetos es capaz de decirnos si una imagen contiene un determinado tipo de objeto o no. Sin embargo, no es capaz de decirnos dónde se encuentra este objeto. Esta tarea se denomina **localización de objetos** y consiste en encontrar la ubicación de un objeto dentro de una imagen. 

Además, la clasificación de objetos solo es capaz de asociar una clase predominante a una imagen. Podemos tener un modelo que diferencie entre imágenes de perros e imágenes de gatos, pero ¿qué sucede si en una imagen hay dos gatos y tres perros? Lo más probable es que nuestras dos neuronas de salida muestren una probabilidad cercana al 50% y nuestro objetivo falle. Dicho de otra forma, la clasificación de objetos solo es capaz de tratar con un único tipo de objeto por imagen y, además, no es capaz de ubicar estos objetos en la misma. 

El objetivo de detectar objetos trata de paliar ambas limitaciones. La detección de objetos consta de dos objetivos separados. Por un lado, debe **localizar** todos los objetos de interés en la imagen, independientemente de su clase. Después, **clasifica** individualmente cada objeto localizado. Esto da como resultado una serie de rectángulos o _bounding boxes_ que enmarcan distintos objetos de potencialmente distintas clases. 

175 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

De igual forma que la clasificación de objetos, la detección de objetos es un problema supervisado, ya que necesitamos tener muestra etiquetada de los objetos que deseamos detectar para poder ser capaces de dar con ellos en nuestras imágenes. Estas etiquetas contendrán la información necesaria para ubicar todos los objetos de interés de la imagen, así como la clase a la que pertenece cada uno de ellos. 

Todas las arquitecturas de _Object Detection_ devuelven el resultado de su inferencia con una estructura similar. Por un lado, devuelven el resultado de la localización de objetos en forma de un conjunto de _bounding boxes_ . Las _bounding boxes_ suelen venir delimitadas por las coordenadas esquina superior izquierda y de la esquina inferior derecha. Con estos dos puntos, podemos trazar el rectángulo que encuadra a cada objeto localizado. 

Para cada uno de los objetos localizado s- es decir, de las _bounding boxes_ – podremos consultar el resultado de cada una de las neuronas de nuestra capa de clasificación. En un problema en el que hay 5 clases posibles y hemos encontrado dos objetos en una imagen, la salida para esta imagen sería la que mostramos en la siguiente figura. Veremos que hay una lista de _bounding_boxes_ detectados por el algoritmo de localización de objetos. Cada una de las _bounding_boxes_ tiene sus coordenadas y sus clases detectadas por el algoritmo de clasificación de objetos. La clase que tenga una precisión más alta – es decir, la más cercana a 1 – será la que sea la seleccionada por la CNN de clasificación. En la figura observamos a la derecha un ejemplo de JSON que podría devolver un algoritmo de _Object Detection_ y a la izquierda tenemos este mismo archivo estructurado para facilitar su comprensión. 



A lo largo de esta sección vamos a analizar los algoritmos y arquitecturas más relevantes tanto históricamente como en la actualidad, y posteriormente podremos en marcha uno de ellos para comprender sobre el terreno su funcionamiento. 

176 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **3.4.1. Region-based Convolutional Neural Network (R-CNN)** 

En 2014 se propuso la primera arquitectura exitosa de _Object Detection_ llamada _Regionnased Convolutional Neural Network_ (2014), desarrollada por investigadores de la Universidad de California. La idea era bastante intuitiva, ya que reutilizaba las CNN de clasificación de objetos con un paso previo. 

Gracias a un algoritmo de visión artificial clásica basado en detección de bordes mediante kernels, se realizaba una búsqueda de regiones de interés, conocidas como ROIs por sus siglas en inglés ( _Regions of Interest_ ). Este selector extraía en torno a 2000 regiones de interés de cada imagen. Estas regiones eran entonces recortadas de la imagen y reescaladas a un tamaño común. Después, cada una de estas regiones se pasa por una CNN de clasificación de objetos para comprender su tipología. En definitiva, se ejecuta una localización de objetos “tradicional”, junto con una clasificación de objetos “inteligente” para así cumplir con el objetivo de detección de objetos. Una de las clases de salida de esta CNN es siempre la clase _background_ (fondo) para así identificar aquellas ROI que no son objetos de interés en función del problema. Esta CNN no era otra que AlexNet, que se empleaba para la extracción de características y clasificación de cada una de las regiones. 

En la siguiente imagen podemos observar la propuesta de arquitectura original de R- CNN. La principal problemática que presenta esta arquitectura es la complejidad de extraer y recortar 2000 regiones de una imagen. Además, debe computar 2000 imágenes por imagen en la CNN lo que implica una gran cantidad de coste computacional y, por tanto, de tiempo. Por último, el modelo está compuesto de dos tipos de algoritmos diferentes, por lo que **no puede ser entrenado de punto a punto** . La parte de localización de objetos no es inteligente, y esto limita enormemente la capacidad de este algoritmo para aprender. 



Junto al artículo en el que publicaron esta arquitectura, los investigadores ofrecieron un repositorio con la arquitectura desarrollada en Python y MATLAB, que a día de hoy denominan un “artefacto histórico” ya que todas las librerías que usa están descontinuadas. Aun así, se puede acceder a comprobarlo en <u>este repositorio de GitHub.</u> 

177 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

La precisión de R-CNN en los principales retos de _Object Detection_ como son los retos de VOC de 2007, 2010 y 2012 oscilaba entre el 50% y el 60%, lo que fue una gran novedad en su momento, aunque sería fácil y rápidamente sobrepasada por otros modelos más rápidos y eficientes, como su descendiente Fast R-CNN. 

### **3.4.2. Fast R-CNN** 

Los creadores de R-CNN llegaron en tan solo un año (2015) a una idea para acelerar el proceso y no necesitar tanto tiempo para procesar una imagen. En lugar de recortar cada una de las ROI y pasarlas individualmente por la CNN, ¿por qué no primero ejecutar la CNN una única vez, y de la salida de sus _feature maps_ tratar de encontrar ROIs? 

Es decir, en lugar de usar los _feature maps_ para pasarlos por una capa totalmente conectada y así clasificar la imagen, la detección de regiones de interés mediante bordes se aplica directamente sobre la salida de la extracción de características, es decir, los _feature maps_ , y con las regiones de estos se aplica entonces la clasificación gracias a las capas totalmente conectadas. Gracias a este cambio, somos capaces de ejecutar una única vez las capas convolucionales de _pooling_ en lugar de 2000 veces. Es intuitivo pensar que el tiempo se reduce notablemente. Sin embargo, el algoritmo de selección de regiones sigue siendo en este caso un algoritmo basado en detección de bordes, aunque en este caso los bordes se busquen sobre mapas de características y no sobre la imagen original. Esto impide que el modelo se pueda entrenar de punto a punto, y complica este proceso en exceso. Podemos comprobar visualmente la descripción que hemos hecho de Fast R-CNN en la siguiente imagen, donde vemos cómo la imagen primero pasa por las capas convolucionales, que producen diversos _feature maps_ . Después, se buscan regiones y, por último, cada región propuesta ( _proposals_ ) es analizada por una capa totalmente conectada para clasificar su tipología de objeto. 



178 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **3.4.3. Faster R-CNN** 

Tan solo un año después, en 2016, surgió la arquitectura de Faster R-CNN, que trataba de dar solución al gran problema de Fast R-CNN que a su vez había heredado esta de su origen, R-CNN: el entrenamiento del algoritmo de búsqueda de ROIs potenciales. Era demasiado costoso, y al no poder entrenar el modelo completo de punto a punto, se perdía una gran cantidad de la potencia que ofrece el _deep learning_ . 

Para solucionar esto se propuso un concepto de CNN novedoso, llamado “ _region proposal network_ ”, o RPN. Esta CNN tiene una arquitectura similar a todas las redes neuronales convolucionales que hemos visto hasta ahora, con capas convolucionales, de _pooling_ y totalmente conectadas. La gran diferencia con una red neuronal de clasificación es que en su última capa no hay neuronas que calculen las probabilidades de las distintas clases, sino las **coordenadas más probables de los objetos de interés. Es decir, produce** **_bounding boxes_** . 

El resto de la arquitectura es realmente similar a la original, ya que esta RPN se ejecuta en el mismo lugar en el que se ejecuta el algoritmo basado en bordes de búsqueda de ROIs en Fast R-CNN, es decir, tras la obtención de los _feature maps_ de la imagen original. 

En este caso no se usó AlexNet, sino una arquitectura más moderna conocida como VGG16, que vimos entre los modelos más destacados de CNN para clasificación de objetos en la sección anterior. Sin embargo, se había producido un gran cambio. Por primera vez la detección de objetos se producía íntegramente a través de _deep learning_ , lo que permitía realizar un único entrenamiento de punto a punto de ambas redes neuronales, la de localización de ROIs y la de clasificación de objetos. 

No obstante, aún quedaba un gran reto por resolver, que R-CNN nunca fue capaz de afrontar. Aún eran necesarias demasiadas pasadas a lo largo de una imagen para realizar la detección de objetos, ya que teníamos dos Redes Neuronales Convolucionales, y el final de ellas debía ejecutarse una vez por cada región potencial. Serían algoritmos más modernos y avanzados los que resolverían este problema, como YOLO y RetinaNet. 

Es importante notar que encontraremos innumerables implementaciones de Faster R- CNN, ya que es una arquitectura muy flexible. Dado que usa una CNN de clasificación de objetos aislada – lo que a su vez es su gran problema – veremos Faster R-CNNs desarrolladas con AlexNet, con VGG, con Inception, con ResNet… En definitiva, cualquier modelo de CNN de clasificación de objetos en el estado del arte es susceptible de ser incorporada a esta arquitectura. En la sección de ejemplo práctico de Object Detection pondremos en marcha una “Faster R-CNN con InceptionResnet v2” en Tensorflow. 

179 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **3.4.4. You Only Look Once (YOLO)** 

Entre los años 2015 y 2016 surgió la aproximación más novedosa hasta el momento para integrar las dos partes de la detección de objetos: la localización y la clasificación. Esto sucedió en un artículo llamado “ _You Only Look Once: Unified, Real-Time Object Detection_ .”, liderado por el investigador Joseph Redmon. Para esto se propuso una única red neuronal que realizara ambas tareas, simplificando enormemente el proceso. En lugar de extraer las características primero, posteriormente encontrar regiones, y por último clasificarlas, se hacen todos estos procesos de una única pasada. 

Si bien los resultados de la localización de objetos son ligeramente menores que en una Faster R-CNN, YOLO fue la primera red neuronal de detección de objetos capaz de operar sobre un video en tiempo real. De hecho, es capaz de procesar hasta 60 _frames_ en un segundo, lo que fue un avance espectacular en su momento. La aproximación del algoritmo de YOLO es la siguiente: 

1. División de la imagen en celdas homogéneas: Habitualmente este valor es de 7 x 7 celdas. Se recorta cada una de estas celdas de la imagen para pasarla a los siguientes métodos. 

2. Mapa de probabilidad de clases en cada una de las celdas generadas, que habitualmente son 49 zonas. Por tanto, cada una de estas celdas tendrá una clase asociada, que será la que la clasificación determine como la más probable. 

3. Predicción de _bounding boxes_ en cada una de las celdas. Esto es que en cada una de las celdas se tratará de estimar si hay algún objeto, y si este objeto está completo en la celda, o si continúa hacia otras celdas, con las que se tendrá que comunicar para generar las _bounding box_ definitivas. 

4. Combinación de las _bounding boxes_ y el mapa de probabilidad para llegar al resultado final, en el que daremos objetos y clases definitivos en un formato similar al JSON que hemos presentado a principios de esta sección. 

En la siguiente imagen podemos comprobar este flujo visualmente, tal y como se presenta en el artículo original de YOLO. 

180 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Estos pasos se realizan en una única CNN, sorprendentemente compuesta únicamente por las capas que ya hemos mencionado, como podemos ver en la siguiente imagen. Contamos con una gran cantidad de capas convolucionales y de _pooling_ , que acaban en tres capas totalmente conectadas para llegar al resultado final. YOLO es por tanto el primer ejemplo de modelo único para la detección de objetos por medio de CNNS. 



En 2016 se presentó la primera iteración de YOLO en el papel “ _YOLO9000: Better, Faster, Stronger_ ”. En esta arquitectura se parte de una serie de puntos iniciales para buscar las _bounding boxes_ en lugar de partir únicamente de una cuadrícula. Estos puntos, llamados _anchors_ se usan para encontrar de forma más rápida las ROI ya que, en lugar de buscar desde cero en las celdas, el modelo trata de modificar el tamaño y posición de estos _anchor_ para que se ajusten a posibles objetos, lo que reduce la complejidad. 

181 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Además, esta segunda versión de YOLO proporciona soporte para imágenes de entrada de alta resolución sin reducir por ello su velocidad de cómputo, permitiendo predecir hasta 9.000 clases en ellas. La última iteración oficial de YOLO surgió en 2018 con el último artículo de Joseph Redmon llamado “YOLOv3: An Incremental Improvement” en el que se presentaban pequeñas mejoras de eficacia y de representación interna. 

A partir de este momento, Redmon abandonó la investigación de YOLO, y numerosos investigadores han tratado de seguir su trabajo iterando sobre esta arquitectura. Una de las más conocidas es la publicada por el ingeniero de Apple Alexey Bochkovskiy, con el nombre de YOLOv4. Además de mejorar la eficiencia del modelo, Alexey tiene un repositorio abierto en Github desde el que cualquiera puede descargarse sus modelos de YOLO compilados para Windows y Linux, incluso con los pesos de ciertas redes pre entrenadas, lo que hace prácticamente inmediato comenzar a utilizarlas. 

Este repositorio se encuentra en este enlace de Github, y contiene toda la información necesaria para poder montar un entorno local en el que entrenar, evaluar y realizar inferencia de imágenes y vídeos. Es importante recordar que para una ejecución fluida es prácticamente necesario contar en nuestro equipo con una GPU de NVIDIA que tenga soporte para tecnología CUDA, como puede ser una GeForce RTX 2080 Ti. 

Este es el motivo por el que en esta asignatura no veremos ejemplos de la ejecución de YOLO, ya que precisa de un entorno local muy potente. Sin embargo, animamos a todos los alumnos con este tipo de tarjetas gráficas instaladas en sus equipos a tratar de seguir el Readme de este repositorio para probar esta arquitectura de primera mano, e incluso para tratar de entrenar su propio modelo con imágenes para proyectos pequeños. 

La última iteración ampliamente aceptada de YOLO es la conocida como YOLO v5. En este caso las mejoras sobre la arquitectura anterior están orientadas a simplificar el proceso de reentrenamiento. Esto quiere decir que una vez que nuestra red está entrenada para un determinado conjunto de imágenes estándar, podemos adaptarla a un nuevo conjunto de imágenes con relativa facilidad y velocidad. Esta versión está desarrollada por Ultralytics, una empresa de código abierto que ha desarrollado esta iteración en Pythorch, un _framework_ para el desarrollo de _deep learning_ muy similar a TensorFlow. En este caso, podemos encontrar la implementación así como el Readme con las instrucciones para levantar esta arquitectura en el siguiente enlace de Github. YOLOv5 está preparada para ser ejecutada en Google Colab directamente. Dado que está desarrollado en Pytorch y hasta el momento hemos estudiado la combinación de TensorFlow y Keras, no vamos a profundizar en la complejidad de su definición y entrenamiento. 

182 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **3.4.5. Otros modelos** 

Si bien actualmente el estado del arte de los modelos de detección de objetos está disputado entre las últimas mejoras de Faster R-CNN y los últimos desarrollos de YOLO, existen una gran variedad de métodos de detección de objetos basados en _deep learning_ . Cada uno de ellos aportó en su momento una novedad que, seguramente, haya sido añadida en las últimas iteraciones de estos dos grandes y predominantes algoritmos. Entre los más destacados encontramos los siguientes: 

- R-FCN (Region based – Fully Convolutional Neural Network) 

- SSD (Single Shot Multibox Detector) 

- RetinaNet 

- EfficientDet (Scalable and Efficient Object Detection) 

Para comparar modelos se usan métodos estándar que permiten conocer las mejoras que aporta cada uno de ellos. Hay dos grandes _datasets_ de imágenes disponibles para evaluar la precisión de un nuevo modelo que es presentado: PASCAL VOC y COCO. Ambas son conjuntos de un gran número de imágenes etiquetadas con _bounding boxes_ , que pueden ser usadas para entrenar y evaluar modelos. Ambas tienen distintas ediciones en función del año en el que se capturaron las imágenes. Al emplear las mismas imágenes con todos los modelos, la competición es justa y significativa. Por otro lado, se evalúa la velocidad a la que son capaces de procesar, ya que hay algunos casos de uso en los que el procesamiento en tiempo real es esencial, y otros en los que sencillamente no es necesario. 

En la siguiente tabla podemos comparar todos los modelos de los que hemos hablado hasta el momento en función de su precisión en cada uno de los bancos de imágenes de pruebas disponibles. Es importante recordar que YOLO es el único algoritmo de esta tabla capaz de procesar video a tiempo real sobre una GPU. 



183 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **3.4.6. Ejemplo práctico** 

Vamos a probar a ejecutar los dos modelos principales de detección de objetos que hemos estudiado en Tensorflow gracias a su _model hub_ . Primero, ejecutaremos un modelo de _Faster R-CNN_ y posteriormente otro de _YOLOv5_ sobre el mismo conjunto de imágenes, para así poder comparar sus rendimientos, aunque sea de forma visual. 

Para comenzar, creamos un nuevo Google Colab en nuestra cuenta de Google. Vamos a repetir los mismos pasos que en el ejemplo anterior para indicar a Google Colab que deseamos usar GPU como acelerador por hardware para nuestras redes neuronales. Para ello, haremos click en Entorno de ejecución  Cambiar tipo de entorno de ejecución  Acelerador por hardware  GPU  Guardar. 

En la primera celda vamos a importar todas las librerías necesarias para este proyecto, que son las ya habituales además de alguna relacionada con el sistema y el tratamiento de imágenes. Introducimos en la primera celda de nuestro cuaderno el siguiente fragmento de código, y lo ejecutamos. 



Ahora, crearemos una celda en la que vamos a descargar el modelo de Object Detection que queremos ejecutar. Cada modelo de Tensorflow _model hub_ tiene una URL, que debemos indicar a la librería para que se pueda descargar el modelo. 



184 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Vamos a descargar una imagen libre de derechos de Wikipedia directamente desde la máquina virtual de Google Colab, para ello creamos una nueva celda de código, introducimos el siguiente _snippet_ y la ejecutamos: 



Veremos una imagen de una terraza con una sombrilla, sillas y mesas, además de algunas plantas de exterior, que es la imagen que nos hemos descargado de Wikipedia. 



185 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En la siguiente celda, vamos a ejecutar el modelo previamente compilado y entrenado de _model hub_ sobre esta imagen, para tratar de detectar todos los objetos que hay en ella. 



Nuestra variable result contiene los resultados de la inferencia de la CNN. Estos son una serie de _bounding boxes_ con una lista de probabilidades de las clases que pueden pertenecer a cada una de ellas. Para simplificar la forma de mostrar estos resultados por pantalla, Tensorflow ha desarrollado una libería a tal efecto. En las tres siguientes celdas vamos a descargar esta librería y a instalarla en el entorno de nuestro Google Colab. Es importante que respetemos las tres celdas por separado, ya que cada una de ellas necesita ser ejecutada de forma independiente. Estas tres celdas, que deberemos crear y ejecutar de forma iterativa son las siguientes: 

**Primera celda:** 



#### **Segunda celda: (¡Importante copiar el punto final!)** 



Puede que entre la gran cantidad de información que proporciona el sistema operativo Linux que hay detrás de nuestra sesión de Google Collab veamos algún aviso de ERROR. Esto no debe preocuparnos, ya que las librerías habrán sido instaladas con toda probabilidad correctamente. 

186 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

#### **Tercera celda:** 



Ahora, ya estamos listos para mostrar por pantalla el resultado de nuestra detección de objetos. El código es largo, pero no es relevante para lo que intentamos comprobar, que es el funcionamiento de un modelo de detección de objetos en _model hub_ . Crearemos la última celda de este ejemplo y la ejecutaremos. 





187 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Finalmente, veremos el resultado de nuestra detección de objetos. Nuestra red neuronal previamente entrenada basada en Faster R-CNN ha detectado una serie de ROIs a las que ha asociado distintas clases. Veremos que en la mayoría de los casos ha acertado, aunque haya perdido algún que otro objeto, y se haya inventado otros tantos. Sin embargo, en términos generales el resultado es sorprendentemente bueno, y todos los objetos que tenían una clase previamente entrenada en el modelo, han sido encontrados, recuadrados, y clasificados. Esta es la salida más habitual de una CNN de detección de objetos. Podemos tratar de ejecutar este mismo proceso con cualquier otra imagen como pueden ser esta, <u>esta</u> o esta, en las que veremos distintos tipos de objetos para hacernos una mejor idea de cómo funciona este proceso. Tan solo tendremos que cambiar la variable image_path por la URL de cualquiera de los 3 enlaces propuestos, y **Reiniciar el entorno de ejecución de Google Colab (Entorno de ejecución**  **Reiniciar entorno de ejecución)** , para poder ejecutar imágenes distintas. 

A continuación, mostramos el resultado para estas imágenes. 



188 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Con este ejemplo terminamos la sección de _Object Detection_ . Hemos aprendido que un algoritmo de detección de objetos siempre está compuesto por un detector de objetos de interés (localizador) y un clasificador. También que hay varias arquitecturas totalmente basadas en _deep learning_ de entre las que destacan YOLO y Faster R-CNN, y que cada una de ellas tiene una serie de puntos fuertes y débiles que tendremos que tener en cuenta a la hora de seleccionar un algoritmo para nuestros proyectos. Por último, hemos puesto en práctica la inferencia de un modelo de detección de objetos gracias a los modelos previamente entrenados de TensorFlow _model hub_ , que también nos permiten realizar entrenamientos para nuestros propios conjuntos de datos de cara a posibles proyectos en los que las clases pre entrenadas no sean suficientes. Ahora ha llegado el momento de pasar el tercer gran objetivo de la visión artificial, el más complejo hasta el momento. La segmentación de objetos. 

### **3.5. Segmentación de objetos mediante** **_deep learning_** 

A lo largo de la unidad anterior vimos distintos métodos de segmentación de objetos, aunque no les diéramos este nombre. Gracias a la umbralización que analizamos en ejemplos como en la detección de Roya en hojas de plantas, a operaciones morfológicas, a la detección de bordes, contornos y líneas, así como mediante los descriptores automáticos de características como SIFT, SURF y ORB, ya hemos segmentado diversos objetos. Segmentar no es más que analizar cada uno de los píxeles de una imagen y clasificarlos. Si en la clasificación categorizábamos la imagen en su conjunto, y en la detección clasificábamos ROIs (regiones de interés) previamente detectadas, en la segmentación **clasificamos todos y cada uno de los píxeles de la imagen** . Si nos quedamos aquí, estamos hablando de segmentación semántica. 

Si vamos un paso más allá, y queremos detectar objetos dada la clasificación de los píxeles, estamos hablando de segmentación de instancias. La segmentación de instancias trata de distinguir los distintos objetos de una imagen a partir de su segmentación. Podemos ver la diferencia entre ambos tipos de segmentación en la siguiente imagen. 



189 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Como vemos, en el primer caso todos los cubos están etiquetados como cubo, porque no se han encontrado los cubos, sino que se han clasificado cada uno de esos píxeles como pertenecientes a la clase “ _cube_ ”, en morado. En el segundo caso, sin embargo, el algoritmo sabe que hay tres cubos y dónde están sus límites, por lo que se han diferenciado las instancias de los objetos “ _cube_ ”. A continuación, analizaremos como se han empleado las CNN para resolver este objetivo de la visión artificial desde la publicación del primer artículo al respecto, en 2015. 

### **3.5.1. Convolutional and Deconvolutional Networks (encoder-decoder)** 

Tres años después del gran éxito de AlexNet, J.Long propuso en 2015 la primera arquitectura entrenable de punto a punto para segmentar objetos. Esta arquitectura, conocida como FCN, es una modificación de las CNN de clasificación que se habían empleado hasta el momento (AlexNet, VGG16) en las que las capas totalmente conectadas son reemplazadas por capas convolucionales, con una característica especial: **funcionan al revés** , como veremos a continuación. 

En paralelo, H.Noh propone en este mismo año la misma aproximación, conocida desde entonces como Convolutional and Deconvolutional Network, por el funcionamiento de estas últimas capas de la red, que ejecutan el proceso contrario de la convolución. Esto quiere decir que, en lugar de reducir cada vez más los _feature maps_ , estas capas convolucionales reconstruyen _feature maps_ hasta alcanzar la dimensión original de la imagen, por lo que se denominan capas **deconvolucionales** . 

Además, se incorporan las capas de _unpoolng_ , que como podemos imaginar realizan la función contraria del _pooling_ , es decir, buscan aumentar las dimensiones de las matrices que reciben, en lugar de reducirlas. En el siguiente diagrama, publicado en el artículo de 2015 de H.Noh,  podemos entender mejor la diferencia entre una capa convolucional y una capa deconvolucional, y de igual manera la comparación entre una capa de _pooling_ y una capa de _unpooling_ . 



La salida final de esta red es una matriz con el mismo alto y el mismo ancho de la imagen de salida, pero con una dimensión por cada clase deseada. En definitiva, vamos reduciendo la imagen a distintos _feature maps_ cada vez más pequeños hasta que, llegado un punto, tratamos de convertir estos _feature maps_ en matrices cada vez más grandes en las que se predice, pixel a pixel, la clase a la que pueden pertenecer. 

190 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En la siguiente imagen, obtenida de la publicación original de FCN, podemos ver una simplificación de este proceso, que puede ayudar visualmente a comprender el funcionamiento de esta arquitectura. 



En la primera mitad de red las capas convolucionales y las capas de _pooling_ comienzan a reducir dimensiones a medida que van extrayendo características de la imagen de entrada (en naranja). En la mitad de la red vemos que se ha llegado a tener tantos _feature maps_ de 7x7 como clases objetivo tenemos. Es decir, si buscamos segmentar entre cielo, tierra y edificio, en este punto tendremos 3 _feature maps_ de 7x7. 

A partir de este momento, comienza la deconvolución. Mediante una serie de capas convolucionales y de _upsampling o unpooling_ (es decir, lo contrario que el _downsampling_ y que el _pooling_ ), conseguimos una matriz del tamaño original de nuestra imagen en alto por ancho. La profundidad será el número de clases, ya que para cada clase se genera un _feature map_ con las predicciones de esa clase para cada pixel. Esta es una representación visual de este proceso. En este ejemplo tenemos 4 clases, por lo que la matriz de salida será la que observamos en el centro, es decir, 4 matrices con las probabilidades de cada una de las clases. Para obtener el resultado final basta con quedarse con la clase más probable para tener nuestra imagen definitivamente segmentada. 



191 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

La arquitectura propuesta por H.Noh es prácticamente idéntica, por lo que no la comentaremos ya que tiene exactamente la misma perspectiva. Se puede consultar <u>en el artículo original</u> si se desea, en el que se explica con gran detalle el funcionamiento propuesto para las capas de _unpooling_ y las capas deconvolucionales. 

La siguiente iteración de este tipo de aproximación es una de las arquitecturas más conocidas y usadas a día de hoy, y se denomina **U-net** . Originalmente U-net surgió como una iteración sobre FCN para el caso específico de imágenes microscópicas de microbiología. La idea novedosa en esta arquitectura fue conectar en diversos puntos las capas convolucionales y deconvolucionales, en lugar de hacer una única pasada hacia adelante. Dicho de otra forma, se crean atajos que alimentan a las capas deconvolucionales no solo de la salida de las capas anteriores, sino también de algunas de las salidas de las capas iniciales de la arquitectura. El nombre de esta arquitectura proviene de la representación que propusieron de la misma sus autores, en la que se ve a la izquierda la parte de contracción de la red, y a la derecha la parte de expansión, formando un diagrama que recuerda a la letra U. 

Una de las grandes ventajas de este tipo de redes, que también se denominan encoderdecoder ya que primero codifican las características y luego vuelven al tamaño original, especialmente la U-net, es que no emplea ninguna capa totalmente conectada, y esto reduce enormemente la cantidad de parámetros que necesita una red neuronal. Estas capas totalmente conectadas tienen una enorme cantidad de entradas por neurona, al estar conectadas con todas las neuronas de la capa anterior, por lo que son el principal foco de aumento de tamaño de parámetros en una CNN. Gracias a este tipo de arquitecturas deconvolucionales, se abre la puerta al entrenamiento de modelos con cantidades menores de imágenes etiquetadas en un set de entrenamiento y evaluación. Por tanto, casos de uso que anteriormente no era posible afrontar por la escasez de muestra se vuelven viables por medio de _deep learning_ . En el desarrollo de U-net se empleó un dataset de tan solo 30 imágenes, lo que era impensable hasta este momento.  En la siguiente figura, con la arquitectura de la U-net, vemos que el comportamiento es realmente similar excepto por los tamaños de las capas y sus números. Destacan la simetría en este caso (hay el mismo número de capas en ambas fases de la red neuronal) y los atajos, señalados como flechas grises, que surgen por primera vez en este tipo de arquitecturas. 

192 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



La última de las arquitecturas basadas en esta aproximación, con gran relevancia en la actualidad, es una aproximación realmente similar a U-net, presentada en 2016, denominada Pyramid Scene Parsing Network (PSPNet). Esta arquitectura, que es una pequeña variación en cuanto a número y tamaño de capas convolucionales y deconvolucionales, además de generar distintos atajos, llegó a obtener un 85,4% de previsión en el reto de segmentación de PASCAL VOC 2012. Con esta precisión en la segmentación, este tipo de arquitecturas pasaron de ser meras investigaciones en universidades a convertirse en uno de los algoritmos por defecto a la hora de diseñar e implementar proyectos de visión artificial. En la siguiente imagen la estructura de la PSPNet, en la que se menciona un módulo “piramidal” que no es más que una sucesión de más convoluciones que posteriormente pasan por un módulo de _upsampling_ para llegar a un resultado realmente similar que el resto de arquitecturas. 



193 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Como hemos podido comprobar, en el mundo investigador de la visión artificial y especialmente en la rama de _deep learning_ es relativamente habitual que cuando un grupo de investigación hace pequeños cambios sobre publicaciones anteriores, le den un nombre totalmente nuevo a su arquitectura y traten de hacer ver que es totalmente novedosa. La realidad es que todos estos modelos son pequeñas variaciones del mismo modelo, y en función del caso de uso cada uno de ellos obtendrá una mejor o peor precisión, algo que solo es posible determinar mediante prueba o error entrenando diversos modelos para el mismo caso de uso con el mismo banco de imágenes, y posteriormente comparando los resultados de precisión en la fase de evaluación. 

La primera arquitectura realmente novedosa y que dio un gran salto de calidad a los modelos de segmentación de objetos fue la arquitectura conocida como Mask R-CNN, a la que vamos a dedicar una sección específica por su importancia y relevancia a día de hoy. 

### **3.5.2. Mask R-CNN** 

En 2017 K.He presentó el algoritmo Mask R-CNN que superó con creces la precisión de cualquier otro modelo previo en el reto de COCO. Como podemos intuir, Mask R-CNN está basada en el modelo de R-CNN, concretamente en la iteración de 2015 de Faster R- CNN, que hemos estudiado en la sección anterior de detección de objetos. 

Recordemos que la gran novedad de Faster R-CNN fue la introducción de una red de proposición de regiones o _Region Proposal Network_ (RPN). Esta pequeña red neuronal propone candidatos a objetos de interés, así como sus _bounding boxes_ , en el caso de Faster R-CNN para posteriormente clasificar cada una de estas _bounding boxes_ . 

Es decir, Faster R-CNN, como todos los algoritmos de detección de objetos, tiene dos salidas. Por un lado, una lista de _bounding boxes_ y por otro lado una lista de clases asociadas a cada una de estas _bounding boxes_ . Mask R-CNN añade sencillamente una tercera salida: la máscara de cada uno de los objetos contenidos dentro de cada una de las _bounding boxes_ . Para extraer esta máscara, Mask R-CNN emplea dos CNN concatenadas que denomina “Mask Classifier”. Esta CNN recibe cada ROI, y trata de obtener la máscara del objeto clasificando cada pixel dentro de la ROI entre dos clases: “objeto” y “no objeto”. Aquellos píxeles que hayan sido clasificados como “objeto” formarán parte de la segmentación de la instancia. Aquellos que no, serán parte del fondo. 

En el siguiente diagrama podemos consultar una simplificación del funcionamiento de Mask R-CNN, con sus CNNs y resultados principales. 

194 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Una de las mayores ventajas de Mask R-CNN frente al resto de arquitecturas previas es que permite **segmentar instancias** . Dado que ya tenemos los objetos detectados y por tanto sabemos cuántos hay y de que tipo antes de segmentar la imagen, podemos diferenciar los objetos. Las arquitecturas anteriores analizaban la imagen pixel a pixel, lo que impedía que pudieran realizar esta segmentación de instancias. El cambio de perspectiva de Mask R-CNN no solo mejora la precisión del resultado, sino que aporta mucha más información que en ciertos casos puede llegar a resultar vital. 

### **3.5.3. La familia DeepLab** 

Este conjunto de arquitecturas nacidas en 2017 de la mano de L.-C Chen en el seno de Google, denominadas DeepLab, introdujeron un nuevo concepto en las capas convolucionales: Las conocidas como _atrous convolution_ , que también encontraremos en la literatura como _dilated convolution_ . Este tipo de convolución es una forma de encontrar mapas de características a distintas escalas, o, dicho de otra forma, para objetos de distintos tamaños. 

En función de un parámetro conocido como _rate_ , este tipo de capa convolucional solo procesa 1 de cada _n_ píxeles en función del valor que se dé a este parámetro. Es decir, si una capa _atrous convolution_ tiene un valor _rate=2_ , el kernel de la convolución solo empleará 1 pixel de cada 2 para computar la salida. El nombre procede del francés, “ _á trous_ ”, que literalmente significa “con agujeros”. 

La ejecución en paralelo de distintas capas _atrous convolution_ sobre la misma imagen de entrada se denominó _Atrous Spatial Pyramid Pooling_ , y es capaz de detectar patrones en el espacio a distintas escalas, lo que es realmente útil a la hora de generar segmentaciones. 

195 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En la siguiente figura, obtenida del artículo original, vemos como la aplicación de convoluciones con un _rate_ cada vez más grande, da como resultado una serie de matrices de diverso tamaño que posteriormente se fusionan en una sola matriz, en la que se detectan estructuras, patrones y formas a distintas escalas. Esta idea ayuda a encontrar objetos de la misma clase en distintas escalas, que era un problema que estaba detectado desde las primeras arquitecturas de segmentación. En definitiva, mejora el contexto espacial de la red neuronal. 



Por último, DeepLab incorpora un nuevo tipo de módulo en esta arquitectura, llamado _Fully Connected Conditional Random Field_ o CRF. Nos sonarán las primeras palabras, que nos hacen pensar desde el principio en capas totalmente conectadas. El problema es que no estamos hablando de neuronas, sino de filtros como los que vimos en la primera unidad. Estos filtros, que son un filtro bilateral y un filtro Gaussiano, tratan de limpiar la salida de la red neuronal para ofrecer una segmentación más nítida. Esto implica que esta arquitectura inicial no es entrenable de punto a punto, lo que implica un modelo menos flexible y con menor capacidad de entender. Esta segmentación es una segmentación meramente semántica, ya que no se están detectando objetos ni instancias, solo detectando estructuras en el espacio a distintas escalas. En la siguiente figura vemos la salida real de una inferencia realizada por DeepLab sobre una imagen a color. 



El nombre de esta sección hace referencia a la “familia DeepLab”, y esto es porque el algoritmo original fue evolucionando hacia arquitecturas mejores y más precisas. 

196 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En la primera iteración relevante de este algoritmo de Google, la DeepLab v3 y posteriormente la DeepLab v3+, se trata de mejorar la calidad de los bordes de las segmentaciones. Para ello, DeepLab se rinde a la arquitectura más laureada de la segmentación de objetos e incorpora dos fases en su procesamiento, una fase de extracción de características y otra fase de ampliación de estas características gracias a deconvoluciones y _unpooling_ . Sin embargo, no abandona la idea de las capas _atrous convolutions_ , y las incluye en la fase de extracción de características. Eso implica que la primera fase de convolución y _downsampling_ se realiza con capas de _atrous convolution_ , aunque posteriormente se aplica una estructura muy similar a U-net y otras, como vemos en el siguiente diagrama. La primera ejecución es un _Atrous Spatial Pyramid Pooling_ denotado como DCNN, y posteriormente la estructura es muy similar a las que ya hemos analizado. 



### **3.5.4. Ejemplo práctico** 

En este ejemplo vamos a tratar de levantar una DeepLab v3 en un entorno de Google Colab para ver el funcionamiento de una red neuronal de segmentación de primera mano. En este ejemplo vamos a usar por primera vez pytorch, una librería que hemos mencionado anteriormente y que persigue el mismo fin que TensorFlow, proporcionando bloques funcionales para construir modelos de _deep learning_ , así como un _model hub_ muy similar al de Tensorflow, que nos permite cargar directamente modelos pre entrenados y ejecutar inferencia sobre las imágenes que deseemos. 

Usaremos pytorch porque el modelo pre entrenado de DeepLab v3 en esta librería es realmente intuitivo de usar, frente al modelo pre entrenado de TensorFlow que requeriría una sección específica solo para probar por primera vez este modelo. Dicho esto, vamos a comenzar el ejemplo de inferencia de segmentación de objetos con _deep learning_ . 

197 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Crearemos un nuevo cuaderno de Google Colab desde nuestra cuenta de Google. De nuevo, y como siempre que ejecutamos procesos de _deep learning_ , es recomendable cambiar el tipo de entorno de ejecución por uno con aceleración con GPU, como ya hemos hecho en todos los ejemplos anteriores. 

Una vez hecho esto, podremos comenzar introduciendo el siguiente fragmento de código en la primera celda de nuestro cuaderno, que será el que importe todas las librerías necesarias, y ejecutándolo mediante el botón “play”. 



Ahora vamos a cargar el modelo desde pytorch model hub, de una forma muy similar a la que usábamos para cargar modelos desde TensorFlow. 



La salida de esta celda en la que cargamos y levantamos el modelo de pytorch nos muestra la estructura de las redes que vamos a emplear. Como podemos ir viendo, la gran mayoría de bloques son convoluciones con distintos tamaños de kernel, seguidas de MaxPooling. Si nos fijamos con detalle, hay capas convolucionales que emplean un parámetro llamado “dilation”. Este es el parámetro que define nuestras _dilated convolutions_ , como en esta capa que muestra la siguiente captura de pantalla. En este caso, estaremos procesando 1 pixel de cada 2, tanto en vertical como en horizontal. 



Veremos que la última sección recibe el nombre de FCN, tal y como hemos analizado en la sección de teoría. 



198 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Una vez ejecutada esta segunda celda, crearemos una tercera celda en la que vamos a descargar y preprocesar una imagen, que será la que evaluemos con nuestro modelo de DeepLab v3. En caso de haber activado la aceleración por GPU, moveremos el modelo y la imagen a la tarjeta gráfica para acelerar la inferencia. 



Con todo preparado, es el momento de ejecutar la inferencia sobre nuestra imagen. Para ello, crearemos una nueva celda e introduciremos el siguiente código. 



199 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por último, vamos a tratar de visualizar el resultado ofrecido por DeepLab en forma de segmentación semántica. Para ello, crearemos una paleta de color de tal forma que cada clase tenga su propio color, y pintaremos la segmentación de la imagen de entrada para posteriormente mostrarla por pantalla. Crearemos una última celda e introduciremos el siguiente fragmento de código. 



El resultado de la ejecución debería ser el siguiente, en el que vemos las imágenes segmentadas. 



200 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

De igual forma que hicimos con el ejemplo anterior, podemos probar con tantas imágenes como deseemos. Por ejemplo, si usamos la última imagen de los enlaces que probamos al final del ejemplo anterior, obtendremos el siguiente resultado, pero por supuesto podemos probar con tantas imágenes como deseemos. **Recordemos que es necesario ejecutar todas las celdas al cambiar de imagen, y que, si obtuviéramos algún error, tendremos que reiniciar el entorno de ejecución y entonces ejecutar todas las celdas.** 



### **3.6. GANs (redes generativas adversarias)** 

Las Redes Adversarias Generativas o Generative Adversarial Networks son una de las últimas incorporaciones al ya complejo mundo del _deep learning_ , y una de las más interesantes a día de hoy. Este tipo de modelos de _deep learning_ son lo que se conoce como modelos generativos. Son capaces de generar datos que se parecen a aquellos datos con los que fueron entrenados, pero que no existen. Esto se denominan datos sintéticos, y en el caso de la visión artificial pueden ser cualquier tipo de imagen o video. 

Los modelos de GAN consiguen grandes niveles de realismo gracias a una estructura primaria basada en dos elementos clave: el generador y el discriminador. El generador es la parte de la arquitectura que crea datos nuevos dado un cierto input. El discriminador es un modelo a priori capaz de discernir datos reales de datos sintéticos en un determinado dominio. Al enfrentar a estas dos redes entre sí, es decir, al convertirlas en adversarios, se consigue que el generador sea cada vez mejor engañando al discriminador y, por tanto, generando imágenes verosímiles y creíbles. Vamos a ver este proceso con detenimiento, primero profundizando en cada uno de estos dos elementos. 

201 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- El modelo **generador** crea nuevos datos. Para ello, trata de imitar la forma en la que la información real está distribuida en el espacio visualmente. Sin embargo, no tiene acceso a estos datos – en nuestro caso imágenes – reales, sino que tiene que partir de cero para conseguir simular datos que desconoce. Todos los datos que produce el generador en las sucesivas épocas de entrenamiento, se convierten en ejemplos negativos para el discriminador. Veremos este proceso en detalle a continuación. En resumen, el generador es una red neuronal que recibe un determinado input y genera una imagen de dimensiones dadas. El objetivo de este elemento dentro de una GAN es que las imágenes que se produzcan sean cada vez más realistas, y por tanto, que sea más probable que el discriminador clasifique los datos que genera como reales. 

- El modelo **discriminador** es el que decide acerca de la adecuación de los datos, es decir, si estos datos pertenecen al mundo real o si bien han sido generados de forma sintética. Son en esencia clasificadores, por lo que tratan de delimitar el espacio en dos conjuntos. En uno de ellos es en el que se encuentran los datos “válidos” o “reales”. Todo dato que no pertenezca a este conjunto, será dado por “sintético” o “no real”. 

Es importante mencionar que no solo hay modelos generativos en el campo de la visión artificial, como ya estudiaremos en asignaturas futuras como la de Procesamiento del Lenguaje Natural (NLP). Sin embargo, en el caso de esta sección nos vamos a ceñir a los modelos generativos cuya salida es una imagen o, en su defecto, un video. 

Durante el entrenamiento de un modelo GAN, el generador trata de producir imágenes que engañen al discriminador, sin saber si quiera de qué se tratan estas imágenes. Esto implica que, en las primeras etapas del entrenamiento, en las que los pesos de las neuronas son inicializados de forma aleatoria, las imágenes del generador serán, en esencia, ruido. Imágenes sin ningún tipo de sentido ni coherencia espacial, sencillamente píxeles al azar. El discriminador estará entrenado para determinar si una imagen pertenece a su conjunto de entrenamiento de imágenes reales o no, por lo que, en estas primeras etapas, las imágenes aleatorias del generador serán etiquetadas como ruido sin ningún tipo de duda. 

Sin embargo, a medida que el discriminador etiquete como “negativos” los ejemplos que va produciendo el generador en las distintas épocas del entrenamiento, el generador irá ajustando los pesos de sus distintas neuronas para tratar de reducir el error que reporta el discriminador acerca de sus datos sintéticos. De esta forma, en cada iteración del entrenamiento los ejemplos producidos por el generador serán más plausibles, hasta que llegará – con suerte – el momento en el que el discriminador no sea capaz de diferenciar un ejemplo que proviene del mundo real frente a otro que viene del generador. Cuando el discriminador ya no puede delimitar el espacio, el entrenamiento ha concluido con éxito. En el siguiente diagrama podemos ver una abstracción de todo el sistema. 

202 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Tanto el generador como el discriminador son redes neuronales que se entrenan gracias a la retropropagación. El error que detecta el descriptor sobre las imágenes del generador es el origen del aprendizaje para el generador. El error a la hora de discriminar entre imágenes reales y generadas que produce el discriminador es su propio _input_ para el entrenamiento. Veamos uno a uno estos conceptos. 

El **discriminador** de una GAN es una red neuronal de clasificación de objetos. La clase “0” es la clase que pertenece a imágenes reales, y la clase “1” es la clase negativa o falsa, de ejemplos que han sido generados artificialmente. Por esto decíamos antes que los ejemplos del generador se convierten en muestra negativa para el discriminador. Construiremos un dataset de entrenamiento que cambiará en cada época del entrenamiento. Por un lado, tendremos las imágenes reales. Estas nunca cambiarán, y estarán etiquetadas como ejemplos positivos para nuestro discriminador. 

Por otro lado, tenemos las imágenes del generador. Estas cambian cada vez que actualizamos los pesos de las neuronas del generador, por lo que los ejemplos de la clase negativa cambian cada época, complicando la tarea de la clasificación del descriptor cada vez un poco más y al mismo momento aumentando notablemente la precisión del descriptor a cada iteración del entrenamiento. 

El discriminador en una GAN es una CNN de clasificación de objetos con una arquitectura habitualmente conocida que dependerá del artículo al que acudamos. En algunos casos será una ResNet, una Inception, una VGG… No tiene una arquitectura en la que merezca la pena detenerse, ya que está directamente heredada de aquellas que estudiamos en la sección de clasificación de objetos. Es en el generador en el que nos detendremos para estudiar la última variación de capas convolucionales que vamos a estudiar en esta unidad. 

El objetivo principal del generador es aprender la distribución espacial del dominio en el que se esté entrenando la GAN. Por ejemplo, si queremos entrenar una GAN para que produzca imágenes de autobuses, el objetivo de nuestra GAN no es “hacer imágenes parecidas a autobuses”, ya que no tiene comprensión acerca de qué es un autobús. Su objetivo real es aprender la distribución espacial de los píxeles que consiguen pasar por imágenes reales ante su adversario, el discriminador. 

203 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Cabe destacar que el verdadero objetivo de una GAN es que el discriminador – en caso de haber sido adecuadamente desarrollado – falle tanto como sea posible, porque esto implica un modelo generativo realmente preciso. Para conseguir esto, necesitamos una red neuronal que dado un input de tamaño fijo – que puede ser un vector aleatorio, un texto, otra imagen, una etiqueta – produzca una imagen de dimensiones conocidas que cumplan con los requisitos del discriminador. 

Este objetivo no puede perseguirse mediante capas convolucionales normales ni dispersas, ya que estas están diseñadas para convertir imágenes en _feature maps_ . Tampoco mediante deconvoluciones ya que estas hacen en el proceso contrario, pero nuestro input no es un _feature map_ , como hemos visto, por lo que no podemos aplicar estas capas tampoco. Es aquí cuando surge la última modificación de las capas convolucionales en redes neuronales **la convolución traspuesta** o **_transposed convolution_** . 

Una convolución normal trata de resumir una matriz de entrada mediante el deslizamiento de un kernel a lo largo de la misma. Multiplica los valores del kernel por los píxeles de cada ventana seleccionada en la matriz de entrada, y construye una matriz de salida más pequeña y con información clave condensada. En el caso de un generador queremos hacer totalmente lo opuesto, partiendo de un input de tamaño menor, generar una imagen realista. Para ello, podríamos aplicar una convolución al revés. El concepto es realmente similar a las deconvoluciones, y en según qué fuentes poco especializadas podemos encontrar ambos términos mezclados. Sin embargo, recordemos que el objetivo de una deconvolución es transformar un _feature map_ previamente generado por una convolución en una máscara para segmentar una imagen. Por el contrario, una convolución traspuesta no parte de la salida de ninguna convolución previa, sino que recibe datos aleatorios y genera, tras varias capas, una imagen completa. 

Matemáticamente el funcionamiento de una convolución traspuesta es relativamente sencillo. Si bien en una convolución obtengo un único valor a partir de una ventana multiplicada por un kernel, en una convolución traspuesta haremos exactamente la misma operación en sentido contrario. Partiremos de un único valor en nuestro input, lo pasaremos por un kernel en sentido contrario, y obtendremos una ventana de tamaño mucho mayor que pasará a formar parte del _output_ de nuestra capa traspuesta en el generador. En la siguiente figura se comprende de forma intuitiva. En ella vemos como de una matriz de 2x2 que empleamos como _input_ (azul) somos capaces de generar ventanas de 3x3 por cada pixel original, que superpuestas en una matriz de salida construyen un output de 5x5. Este es el proceso básico que se da en una red neuronal generativa dentro de una GAN. También se emplean capas de _upscaling_ en este caso sí que son idénticas a las capas de _unpooling_ que hemos analizado en las arquitecturas encoder-decoder en la sección de segmentación de objetos. En definitiva, partiremos de una entrada de tamaño reducido y mediante convoluciones traspuestas y _upscaling_ seremos capaces de obtener imágenes de tamaño completo, con la misma distribución espacial que un set de imágenes de muestra que nuestra red **nunca verá** . 

204 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 



Para aprender a imitar estas imágenes de muestra, el generador se basará en la salida del discriminador, gracias a la retropropagación ajustará los pesos de sus capas convolucionales traspuestas, hasta ser capaz así de generar imágenes adecuadas. 

Vamos a analizar algunas de las arquitecturas más empleadas en la actualidad de redes GAN, comentando sus aspectos diferenciales, así como sus ventajas e inconvenientes. Como en todas las secciones, esta será tan solo una muestra de los innumerables modelos y arquitecturas que existen de GANs, por lo que no será exhaustivo ni pretende serlo. 

### **3.6.1. Conditional GAN: pix2pix** 

Este tipo de GAN está centrado en convertir imágenes de entrada en imágenes de salida que se conoce como _image translation_ . Se denominan _conditional_ GAN debido a que generan imágenes siempre bajo una condición determinada. Esto es así en contra de las primeras GAN que se propusieron en 2014, cuya entrada era un vector de valores aleatorios. En este caso, la condición de entrada es una imagen o un mapa de segmentación que sirve como condición – también podríamos llamarlo guía – para el generador. Esta es una forma de enriquecer la información con la que trabaja el generador, y permite resultados más finos que aquellos que parten de un vector aleatorio de información. Además, permite mantener ciertas características espaciales de la imagen de entrada, por lo que se denomina traducción de imágenes. Para hacer esto, el generador ya no solo usa convoluciones traspuestas, sino que necesita ser una red con estructura **encoder-decoder** . En el caso específico de pix2pix se emplea la estructura de U-net, que ya hemos analizado anteriormente. 

Primero se convoluciona la imagen de entrada hasta llegar a un mapa de características que nos permitirá generar una imagen totalmente distinta gracias a las convoluciones traspuestas. Sin embargo, como es de esperar, esta imagen generada por la parte de decodificación (la segunda parte de la arquitectura) mantendrá ciertas características de la imagen de entrada, ya que parte de esta. Esta gran diferencia con la GAN básica que hemos analizado anteriormente permite a las aplicaciones basadas en pix2pix aplicaciones como aplicar distintos estilos a una imagen, o generar imágenes realistas a partir de mapas de segmentación dibujados a mano por los usuarios. 

205 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

La gran desventaja de pix2pix es que necesita pares de imágenes relacionados entre sí para poder entrenarse. Por ejemplo, si queremos que a partir de un mapa de segmentación diseñe fachadas, nuestra muestra tendrá que tener un par de matrices por cada punto de datos, una con una imagen de una fachada real, y otra con la segmentación de esta fachada en las clases que deseemos, lo que aumenta exponencialmente la cantidad de trabajo requerida para poder entrenar este modelo. 



### **3.6.2. CycleGAN** 

CycleGAN surge para tratar de solucionar la gran limitación de las redes condicionales como pix2pix, la necesidad de tener pares de imágenes etiquetadas para entrenar el algoritmo. Es decir, el objetivo es pasar de un set de imágenes pareadas (como podemos ver a la izquierda de la siguiente imagen) a un set de imágenes sin relación entre ellas, lo que complica enormemente la arquitectura necesaria para conseguir tal objetivo. 



En esencia, la propuesta de CycleGAN parece sencilla. En lugar de usar un generador y un discriminador, CycleGAN emplea **dos generadores y dos discriminadores** . 

Si tenemos dos dominios de imágenes, por ejemplo, en el ejemplo de la izquierda de la imagen anterior: boceto de un calzado (X) e imagen real de dicho calzado (Y), los generadores funcionarían de la siguiente manera. 

- Generador 1: Genera imágenes en X (bocetos de calzado) a partir de imágenes en Y (calzado real) 

- Generador 2: Genera imágenes en Y (calzado real) partiendo de imágenes en X (bocetos de calzado) 

206 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Por tanto, un discriminador tratará de decidir si los bocetos generados por (1) son reales o sintéticos, y otro discriminador tratará de discriminar si las imágenes generadas por (2) son reales o sintéticos. 

Este sencillo cambio permite que las imágenes no estén pareadas, ya que los generadores solo son evaluados por su resultado, y no por la relación de su resultado con la entrada que reciben. Pero entonces, ¿cómo conseguir que relacionen el _output_ con el _input_ ? Mediante la función de objetivo de estos elementos. Y esta función objetivo es una **función en ciclo** ( _cycle_ ). 

La idea es ejecutar el proceso en ciclo, de tal forma que los bocetos que genera (1) pasen a ser la entrada de (2), que generará imágenes de calzado real, que a su vez serán la entrada de (1) de nuevo, que tratará de convertir un boceto suficientemente bueno y que será la entrada de (2) ... Y así sucesivamente hasta completar el entrenamiento. Gracias a este ciclo, el resultado proporcionado por cada generador está condicionado a que tenga alguna relación con su entrada, ya que de otra forma ambos generadores acabarían produciendo poco más que ruido aleatorio. 

La arquitectura de los generadores de CycleGan es muy similar a la de redes como pix2pix y está basada en la filosofía de **encoder-decoder** empleando convoluciones en la primera parte – para extraer características del _input_ – y convoluciones traspuestas en la segunda parte – para generar el _output_ – apoyadas por funciones de _downsampling_ y _upsampling_ respectivamente. La siguiente figura es la representación de esta estructura, que recordemos es la del **generador** . 



El **discriminador** es una red totalmente convolucional de clasificación llamada PatchGAN con una arquitectura estándar en la que no nos detendremos. 

207 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Este artículo es muy conocido por el ejemplo que empleó para mostrar su funcionamiento, en el que convertían una imagen en “cuadros” artificiales de distintos artistas de renombre como Monet, Van Gogh y Cézanne. El artículo completo se puede consultar en <u>este enlace de arXiv.</u> 

### **3.6.3. StyleGAN** 

Uno de los principales problemas de todos los modelos que hemos visto hasta el momento es el poco control que tiene el desarrollador sobre la salida de la GAN. Si bien en los objetivos de traducción de imágenes como pix2pix y CycleGAN hemos visto que podemos emplear una imagen de entrada para condicionar la imagen de salida, esta estrategia está limitada y no permite modificar elementos específicos como características concretas. Sirva de ejemplo la generación de caras humanas. Quizá podríamos desear manipular el color de la piel, del pelo, de los ojos, la forma de la cara… Esto no es posible con los modelos que hemos visto hasta ahora. 

NVIDIA trató de resolver este problema con la publicación de StyleGAN en 2018, orientada concretamente a la generación de caras humanas a partir de un vector numérico, es decir, no es una red de traducción de imágenes sino de generación aleatoria. Es esta aleatoriedad la que NVIDIA deseaba poder manipular hasta cierto punto, y el origen de esta arquitectura. En este artículo se presentan dos grandes avances en el mundo de las GAN: La red llamada _Mapping Network_ y la normalización adaptativa (AdaIN). 

La idea de la red llamada _Mapping Network_ es generar un vector codificado para diferenciar distintas características visuales a distintas escalas. En StyleGAN, refiriéndose a características de caras humanas, estas características fueron: 

- Grandes: Afectan a la pose, el estilo de pelo, la forma de la cara, etc. 

- Medianas: Afectan a características faciales, estilo de ojos, nariz y boca, forma del pelo 

- Pequeñas: Están relacionadas con el mapa de colores (ojos, boca, piel, pelo) y con pequeñas características (pecas, granos, cicatrices) 

Para hacer esto se introdujeron 8 capas totalmente conectadas de neuronas ( _fully connected_ ) para determinar todas estas características en un vector de salida que condensara toda la información relevante a los tres tipos de características. Esta red se ejecuta en primer lugar, antes que ningún otro módulo de la GAN. El resultado se denomina _style mapping array “W”_ ya que es el que determina las distintas características de la imagen de salida. 

208 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Para generar esta imagen de salida no se procesa todo el vector, sino que gracias a un módulo llamado AdaIN ( _Adaptive Instance Normalization_ ), el vector es separado en distintos vectores llamados _styles “A”_ , que son partes del vector completo de _style mapping “W”_ . 

Esto implica que según los vectores “A” con los que alimentemos a la segunda parte de la red neuronal, la imagen de salida tendrá unas características y otras. Esto puede ayudar a manipular el resultado, ya que, si asociamos distintos valores de los vectores “A” con distintas características, estaremos consiguiendo estilizar nuestras imágenes de forma voluntaria. En la siguiente imagen podemos ver como los resultados de la misma ejecución de una GAN varían en función de los vectores “A” que se le proporcionen, permitiendo así seleccionar distintas características en nuestras imágenes de salida. 



En esta sección no vamos a ver ejemplos de código, pero si algún alumno estuviera interesado en construir su propia GAN, en esta serie de tutoriales de TensorFlow está todo preparado para montar GANs sobre Keras en Google Colab. Requieren un nivel más alto de programación del que hemos empleado hasta este momento dada la complejidad de estos algoritmos, pero pueden resultar muy interesantes. 

209 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

## **4. Machine Vision. Instrumentación para la visión** 

_“Existe todo un campo dedicado a la captura en visión artificial, denominado en ocasiones machine vision o visión industrial. En este campo se encuentran investigadores y empresas dedicadas a diseñar, desarrollar y producir los distintos dispositivos de captura específicos para proyectos de visión artificial.”_ 

Por ahora hemos analizado numerosos algoritmos disponibles para construir proyectos de visión artificial, desde el preprocesado de una imagen, pasando por sus características y hasta la aplicación de los objetivos. Hemos tratado técnicas clásicas de visión artificial y otras basadas en _deep learning_ y hemos analizado las ventajas e inconvenientes de cada una de ellas, así como su funcionamiento y en algunos casos implementación. 

Hasta el momento hemos dado por sentada la parte fundamental de un proyecto de visión artificial: **las imágenes** . Los investigadores en universidades y centros de investigación que desarrollan todos los algoritmos que hemos analizado hasta ahora no tienden a usarlos en aplicaciones del mundo real. Como consecuencia, se centran en la teoría e implementación genéricas, sin un caso de uso concreto. Tanto es así, que la inmensa mayoría de modelos que encontramos actualmente publicados están entrenados con los mismos conjuntos de datos: ImageNet, PASCAL VOC, COCO… Las imágenes son un mero trámite para los investigadores, pero para desarrollar un proyecto en el mundo real son **esenciales** . 



El origen de todas las imágenes está en un dispositivo de captura digital, que transforma la luz que observa en una matriz tridimensional a color, habitualmente. Sin profundizar en exceso en los detalles de un dispositivo de captura, sí es importante conocer los principales aspectos de los mismos que afectan a la captura y son esenciales conocer y escoger para completar con éxito cualquier proyecto de visión artificial. 

210 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Existe todo un campo dedicado a la captura en visión artificial, denominado en ocasiones _machine vision_ o visión industrial. En este campo se encuentran investigadores y empresas dedicadas a diseñar, desarrollar y producir los distintos dispositivos de captura específicos para proyectos de visión artificial. Así como hay empresas dedicadas a la fabricación de cámaras para el rodaje de películas y otras centradas en la producción de cámaras fotográficas de alta gama, existen multitud de empresas centradas únicamente en productos de captura de imagen orientados a visión artificial. Como veremos, los proyectos de visión artificial tienen necesidades muy concretas a la hora de capturar sus imágenes, y este campo trata de dar respuesta a estas necesidades. Veremos que no solo se trata de capturar imágenes a color como en una cámara fotográfica, sino que hay numerosos tipos de información y longitudes de onda que podemos capturar con un dispositivo de captura. La selección del dispositivo de captura y de la información que este devuelve serán elementos esenciales a la hora de determinar el éxito o fracaso de cualquier proyecto de visión artificial. 

### **4.1. Elementos básicos de un dispositivo de captura** 

Todo dispositivo de captura de imágenes, sea del tipo que sea (veremos esta tipología más adelante) tiene una serie de elementos que lo definen, que a su vez determinan sus capacidades. Es esencial conocerlos y comprender el impacto que tiene cada uno de ellos en los _setups_ de proyectos de visión artificial que podamos llevar a cabo, tanto para tener la solvencia necesaria a la hora de seleccionar el dispositivo de captura, como para cumplir con los requisitos mínimos de imagen que puedan llegar a tener nuestros algoritmos de visión artificial. Además, veremos que no solo es posible trabajar con imágenes a color en el espectro visible, y que por tanto será importante elegir el mejor tipo de señal para cada caso concreto. En las siguientes secciones vamos a estudiar los elementos básicos de un dispositivo de captura. Estos son los que conforman la base de dicho dispositivo, y sobre todo, aquellos que podemos seleccionar y que marcarán en gran medida los resultados de nuestro despliegue. 

### **4.1.1. El sensor** 

Al comienzo de la asignatura se presentó una primera intuición de cómo funciona un sensor para capturar imagen digital. El sensor de una cámara digital está compuesto por pequeños componentes electrónicos que reaccionan a la luz llamados celdas **fotosensibles** , formadas principalmente por un pequeño componente electrónico conocido como fotodiodo. Estos componentes electrónicos son los encargados de convertir la energía de la luz que incide sobre ellos en una señal eléctrica que pueda permitir generar posteriormente una imagen digital mediante el tratamiento de dicha señal. Actualmente en la mayoría de los casos estos fotodiodos tienen superpuesta una lente microscópica, que concentra la luz sobre la zona sensible del fotodiodo para así aprovechar al máximo las capacidades de este. Estas celdas reciben también el nombre de pixel, ya que cada una de ellas proporcionará el valor de intensidad a cada uno de los píxeles de la imagen digital de salida con los que trabajaran nuestros algoritmos. 

211 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Teniendo en cuenta que las imágenes que genera una cámara digital están compuestas por tres dimensiones distintas, un por cada canal de la imagen (RGB), sería razonable pensar que en cada cámara hay tres sensores, uno especializado en cada uno de los colores primarios de la luz. 

En efecto, esto es lo que sucede en la gran mayoría de cámaras digitales en la actualidad, aunque hay una serie de matices al respecto que es necesario comentar. Realmente, en la amplia mayoría de los casos no es que haya tres sensores distintos, sino que cada celda fotosensible está formada por tres tipos de píxeles. Gracias a un filtro de luz bayesiano podemos filtrar los colores de la luz y redirigirla, de tal forma que cada pixel reciba solo la luz filtrada de uno de los tres canales. Habrá por tanto píxeles que solo reaccionen a la luz roja, otros que solo reaccionen a la luz azul, y por último un tercer tipo que solo reaccione a la luz verde. Los tres tipos de pixel están compuestos por el mismo fotodiodo, lo que cambia es el filtro que deja pasar un tipo de luz u otro hasta este fotodiodo Generalmente, dado que las celdas deben ser cuadradas, se emplean dos pixeles para capturar el color verde (que es frente al que el ojo humano tiene más sensibilidad, y por esto las cámaras de visión nocturna se muestran en una escala de verdes) y un pixel para capturar el rojo, junto a otro único pixel para capturar el color azul, sumando un total de cuatro píxeles por celda. 

Hay otras opciones para filtrar el color como son los sensores Foveon X3, que emplean las distintas propiedades del silicio para automáticamente procesar una cierta longitud de onda u otra. En este caso tendremos en efecto tres fotodiodos distintos sin un filtro, que igualmente compondrán celdas de cuatro fotodiodos cada una. Por último, están los sensores 3CCD, en cuyo caso sí que se emplean tres sensores distintos, cada uno de los cuales recibe un rango de luz u otro en función de un prisma que se coloca antes de los sensores. El prisma separa los colores de la luz que recibe la cámara y los redirige a cada uno de los sensores para extraer tres canales de color. 

Los sensores pueden tener distintas formas y tamaños, lo que será determinante para el resultado que puedan producir. Los sensores más grandes, entre 370 mm<sup>2</sup> y 864 mm<sup>2</sup> de área, tienden a producir mejores imágenes, ya que permitirán tener celdas fotosensibles de mayor tamaño, recogiendo así la luz de una forma más óptima y generando mucho menos ruido. Por el contrario, sensores más pequeños, de en torno a 25 mm2 son notablemente menos costosos, pero reciben menor cantidad de luz y por tanto las imágenes son de peor calidad y tendrán bastante más ruido. Es por esto que la selección del tamaño del sensor a la hora de diseñar despliegues de visión artificial no es una decisión trivial. 

En cuanto a la forma del sensor, habitualmente los sensores fotográficos tienen forma rectangular, tratando de simular la percepción visual humana que tiene un mayor rango horizontal que vertical. Las relaciones de aspecto más habituales, es decir, cómo se relaciona el lado más largo con el lado más corto, son las denominadas 3/2 y 4/3, siendo el primero el más habitual en aplicaciones de visión artificial. 

212 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Una de las características más importantes de un sensor de imagen digital es el **rango dinámico** . Esta variable hace referencia a la capacidad de un sensor para captar de forma correcta y simultánea objetos muy luminosos y objetos muy oscuros. Concretamente es la relación que existe entre la intensidad de la luz capturada en la parte más iluminada, y la cantidad mínima de intensidad de luz necesaria para poder capturar un objeto. Para analizar el rango dinámico de una imagen se emplea el histograma, que estudiamos al comienzo de esta asignatura. Un histograma con valores repartidos entre todas las intensidades – como es el resultado de un histograma ecualizado – indica que la imagen está correctamente tomada dadas las circunstancias de iluminación dadas, y que por tanto el rango dinámico ha sido adecuado para la captura. 

El tipo de sensor afectará enormemente al rango dinámico que puede detectar, por lo que será un parámetro esencial a tener en cuenta en nuestras aplicaciones de visión artificial. 

Hay dos tipos principales de sensores a color empleados en imagen digital, dependiendo de la tecnología que empleen para captar la luz y el tratamiento que hagan de la señal que proporcionan los fotodiodos de su estructura. Ambos sensores están basados en la tecnología MOS, basada en semiconductores de óxido metálico, pero difieren en la aproximación global como vemos a continuación. 

- CCD ( _charge-coupled device_ ): Este tipo de sensores son los que encontramos en cámaras de alta gama, tanto de fotografía como de _machine vision_ . Estos sensores están basados en tecnología analógica, y su salida es por tanto una señal analógica compuesta que debe ser posteriormente procesada por un chip fuera del sensor. La señal eléctrica generada por cada pixel viaja a lo largo de sus vecinos en vertical - es decir, hacia los píxeles de su misma columna - hasta llegar al extremo del sensor, donde se suma al resto de señales hasta construir una única señal analógica, que es la que se procesará posteriormente para poder obtener una imagen digital. Esto permite incluir más pixeles por unidad de espacio ya que en cada celda solo habrá fotodiodos, sin electrónica asociada. Sin embargo, requiere de una circuitería externa para convertir esta señal analógica en una digital. Gracias a esta aproximación los sensores CCD generan muy poco ruido a la hora de capturar imágenes ya que la señal solo se manipula al final y se conserva su integridad durante una mayor cantidad de tiempo. Además, tienen un gran rango dinámico y su respuesta es más uniforme y constante, lo que implica que si exponemos el sensor dos veces a la misma fuente de luz, la respuesta será prácticamente idéntica, lo cual es una gran cualidad para el procesamiento de imágenes. 

213 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- CMOS ( _Complementary metal–oxide–semiconductor_ ). A diferencia de CCD, en CMOS cada pixel es totalmente independiente del resto. La digitalización de la señal se realiza a nivel de cada pixel, por lo que no es necesaria circuitería externa a este tipo de sensores, ya que de cada pixel ya sale una señal digital procesada. Gracias a esta independencia, son sensores más robustos y flexibles ante posibles fallos, además de ser notablemente menos costosos. No obstante, CMOS tiene la mitad de rango dinámico que un sensor CCD, además de generar más ruido ya que la señal se procesa tantas veces como píxeles tiene el sensor. Al necesitar de un procesado en cada pixel, los pixeles en los sensores CMOS son más pequeños, recogiendo menos luz y por tanto proporcionando un menor rendimiento. Por último, son sensores menos uniformes, lo que quiere decir que, si capturamos una imagen dos veces con exactamente la misma luz, el resultado variará entre una captura y otra, complicando esto el posible rendimiento de nuestros algoritmos. 

En la siguiente figura podemos observar a la izquierda una representación de un sensor CCD y a la derecha la representación de un sensor CMOS. 



### **4.1.2. El objetivo o la lente** 

Ya hemos analizado como el sensor es un dispositivo electrónico que recibe luz y la convierte en una señal digital que se acaba convirtiendo en una matriz con una serie de píxeles repartidos habitualmente en tres dimensiones. Si usáramos un sensor directamente contra una escena que deseamos capturar, toda la luz del ambiente incidiría en él sin ningún tipo de enfoque, por lo que solo podríamos generar ruido desenfocado, que variaría en intensidad según la intensidad de la luz. 

Para que un sensor pueda “ver”, es necesario que cuente con una determinada óptica que concentre la luz de un cuadro de imagen que nos llegue a interesar sobre las células fotosensibles del sensor. Si usamos un símil con la visión humana, el sensor es la retina. Los seres humanos no podemos ver sin un cristalino que enfoque la imagen sobre la retina, de forma que esta se aprecie de forma nítida. Este es el papel que cumple el objetivo en un dispositivo de captura. El objetivo o lente se coloca encima del sensor, de forma que el sensor reciba la imagen que deseemos y que esta esté enfocada. Hay una serie de parámetros básicos en un objetivo que es necesario conocer para poder tomar decisiones acerca del objetivo que necesita nuestro dispositivo según nuestro proyecto. 

214 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

#### **Distancia focal** 

Este parámetro lo encontraremos habitualmente indicado en las especificaciones de nuestro objetivo o lente en milímetros. Es una medida de distancia que indica la separación existente entre el centro del objetivo y el centro del sensor. Esta distancia afecta directamente al siguiente parámetro que vamos a mencionar, el ángulo o campo de visión. Cuanto más amplia sea la distancia focal - es decir, más separada esté la lente del sensor - más estrecho será el campo de visión, pero mayor será el zoom o aumento que se producirá sobre los objetos alejados. Por el contrario, si la distancia focal es corta, veremos un gran ángulo de visión, pero con muy poco acercamiento hacia los objetos enfocados. Es decir, con grandes distancias focales podremos ver objetos muy lejanos pero con muy poco ángulo de visión, y con distancias focales pequeñas veremos los objetos a su tamaño original pero contaremos con un gran ángulo de visión. 

Distancias focales muy grandes generan imágenes más cercanas, pero con un águlo de visión pequeño (como un teleobjetivo) y distancias focales muy pequeñas generan imágenes más lejanas, pero con un gran ángulo de visión (como un gran angular). Veremos esta relación en detalle un poco más adelante. 

#### **Campo de visión (FOV)** 

Este parámetro se suele medir con un valor en grados para cada una de las dimensiones, vertical, horizontal y profundidad. Como hemos mencionado, está directamente relacionado con la distancia focal. Podremos encontrar desde campos de visión de 12º en el caso de los teleobjetivos más largos, hasta más de 180º en las lentes similares a un ojo de pez. 



215 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

#### **La apertura del diafragma. La profundidad de campo** 

Según el tipo de dispositivo de captura el diafragma puede encontrar en la lente o en la propia cámara, pero su función siempre será la misma: variar la intensidad de luz que llega al sensor controlando la **apertura** . 

Esta apertura no es más que abrir o cerrar el agujero por el que pasa la luz del exterior hacia el sensor, de igual forma que en los seres humanos las pupilas cambian de tamaño según la iluminación del ambiente, dejando pasar más o menos luz a la retina para evitar deslumbrarnos (que en el caso de la captura de imágenes sería sobre exponer una imagen). El diafragma es un dispositivo mecánico que se puede ajustar por parte del usuario para adaptarse a distintas condiciones de captura. Cuanta más luz deseemos que pase hacia nuestro sensor, más abriremos el diafragma, y viceversa. 

El diafragma no solo se emplea para ajustar la captura a las condiciones de iluminación, sino que afecta directamente a otro parámetro conocido como **profundidad de campo** . La profundidad de campo determina el espacio de imagen que está correctamente enfocado en la dimensión de profundidad. En la siguiente imagen es más fácil comprenderlo. Cuanto más cerrado está el diafragma más profundidad está enfocada: vemos el fondo, el árbol y a la persona enfocadas. A medida que vamos cerrando el diafragma la profundidad de campo se reduce, y comenzamos a solo ver enfocados algunos objetos de la profundidad de la escena. La profundidad de campo se expresa mediante la letra _f._ Cuanto más pequeño es _f_ , mayor es la apertura y menor es la profundidad de campo, como vemos en el siguiente diagrama. 



El valor de _f_ varía desde _f/32_ para un paso de luz mínimo hasta _f/2.8_ para un diafragma totalmente abierto. Según la lente que se desee instalar en la cámara se permitirán unos u otros valores de diafragma, no siendo posible seleccionar cualquiera de ellos. 

216 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Además, la apertura del diafragma afecta al último elemento de un dispositivo de captura que vamos a analizar, el obturador y el tiempo de exposición. Cuanto más podemos abrir el diafragma, más luz pasa, por lo que podemos capturar la imagen más rápido, o, dicho de otra manera, podremos permitirnos tener menos tiempo abierto el obturador y por tanto tener un menor tiempo de exposición. Analizaremos estos dos conceptos más adelante. 

#### **Tipos de lente** 

Existen tantas lentes como configuraciones de distancia focal podamos imaginar. Sin embargo, hay una serie de grupos básicos en los que podemos clasificar las distintas lentes, que son entre otros: 

- Objetivos estándar: Se consideran los objetivos más similares a la visión humana, y son aquellos con una distancia focal de entre unos 30 mm y 70 mm. Se emplean en proyectos de visión artificial en los que solo debe procesarse un área determinada de información y en aquellos en los que se evita en todo momento posibles deformaciones en la imagen. 

- Grandes angulares: Un gran angular cubre ángulos superiores al que cubre la visión humana, con valores inferiores a 28 mm para ser considerados como tales. Los encontraremos ampliamente en proyectos de visión artificial ya que proporcionan mejores campos de visión sin renunciar a la calidad de imagen, lo que al fin y al cabo supone una reducción de costes para el cliente que adquiere estos dispositivos de captura. 

- Ojos de pez: Estos objetivos dan valores de FOV de 180º o más. Realmente no son lentes que dependan de su distancia focal ya que esto sería imposible, sino elementos ópticos más complejos para conseguir introducir tanta cantidad de información enfocada sobre el sensor. Generan un gran efecto de deformación en las imágenes por lo que puede ser peligroso trabajar con ellos en según qué proyectos de visión artificial. 

- Teleobjetivos: Son objetivos con distancias focales mayores a las de los objetivos estándar, por lo que parten desde los 70-80mm y pueden llegar hasta los 300 mm de distancia focal (35 cm de objetivo). Con estas lentes se pueden captar objetos realmente lejanos con gran calidad, es decir, aplican una gran ampliación, pero sin embargo si campo de visión es realmente reducido. Es realmente extraño ver este tipo de objetivos en problemas de visión artificial. 

217 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En la siguiente figura podemos ver una relación de tipos de objetivo frente a la distancia focal. 



### **4.1.3. El obturador y el tiempo de exposición** 

Por último, tras hablar del sensor y de la lente u objetivo, vamos a analizar el último componente esencial de un dispositivo de captura de imágenes: el obturador. El obturador es el elemento de los dispositivos de captura que se encarga de controlar la cantidad de tiempo durante la cual la luz incide sobre el sensor fotosensible. Si el diafragma controla la cantidad de luz modificando **la apertura** , el obturador controla la cantidad de luz modificando el **tiempo** durante el que esta llega al sensor. 

En función del tiempo que permanezca abierto el obturador de nuestro dispositivo de captura estaremos trabajando con una **velocidad de obturación** determinada, que es un parámetro modificable. La velocidad de obturación define el tiempo que permanece abierto un obturador. Este valor es el que determina el **tiempo de exposición** . Una velocidad de obturación considerada rápida es aquella en la que el obturador permanece abierto menos de 1/60 segundos, por lo que la luz incide tan solo un instante sobre las células fotosensibles de nuestro sensor. Con una obturación rápida, las imágenes son estáticas y nítidas, aunque los objetos estén en movimiento, pero por el contrario el sensor recibe notablemente mucha menos luz. 

218 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

En el caso contrario tenemos las velocidades de obturación lentas, que mantienen el obturador abierto más de 1/60 segundos. Con este tipo de velocidades la exposición es muy elevada, es decir, la luz permanecerá incidiendo durante el sensor durante un periodo de tiempo relativamente amplio, y los objetos en movimiento dejarán una estela en nuestro sensor, aunque conseguiremos la máxima cantidad de luz disponible para nuestra fotografía. Por ejemplo, las velocidades de obturación más altas, que superan el minuto e incluso en ciertos casos las horas, se emplean principalmente para fotografiar fenómenos astronómicos de noche. Las velocidades de obturación más rápidas, de en torno a 1/8000 segundos se emplean en casos de uso de visión artificial en los que es necesario capturar objetos a grandes velocidades, por ejemplo, en líneas de producción. En estos casos, dado que la velocidad de obturación es tan pequeña, será importante iluminar muy bien estos objetos y abrir el diafragma todo lo que nuestra lente y el campo de visión nos lo permitan, para compensar el poco tiempo que la luz estará sobre nuestras células fotosensibles. 

Otra característica importante relacionada con el obturador y el tiempo de exposición para visión artificial es la diferencia entre el _rolling shutter_ , y el _global shutter_ . 

#### **_Global shutter_** 

Este tipo de obturador gestiona electrónicamente la intensidad de tal forma que todos los pixeles del sensor se vean expuestos a la misma luz en el mismo momento. Gracias a este comportamiento, conseguimos que las imágenes que capturamos realmente sean capturas de un único momento en el tiempo. Por desgracia, esto acarrea el coste de una limitación en cuanto a los frames por segundo que es capaz de procesar un equipo. 

#### **_Rolling shutter_** 

Los obturadores _rolling_ van desplazando la luz a lo largo del sensor línea a línea de pixeles. En cada instante, una línea de píxeles está recibiendo la luz del entorno. Esto quiere decir que la imagen final es en realidad una concatenación de momentos en el tiempo. Si bien esto permite una gran capacidad de transmisión de frames por segundo, este tipo de cámaras deforman los objetos en movimiento como se puede observar en la siguiente imagen, ya que para cuando la luz llega a la última línea de píxeles, el objeto puede no estar en su lugar original. 



219 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **4.1.4. Frame Rate** 

Por ahora hemos hablado de elementos estáticos, es decir, para capturar una única imagen pensando en capturas estáticas. Sin embargo, en una gran cantidad de proyectos de visión artificial nos encontraremos con la necesidad de trabajar con cámaras que capturan imágenes de forma continua, o lo que es lo mismo, con vídeo. Estos dispositivos no tienen ninguna diferencia de funcionamiento con los demás, sencillamente están constantemente tomando imágenes. El número de imágenes que captura un dispositivo por segundo se llama _Frame Rate_ y se mide en fps ( _frames per second_ ). Es un valor que se puede modificar en la gran mayoría de dispositivos, pero todos ellos tienen un límite que no son capaces de superar. Este es el _max Frame Rate_ de una cámara. 

Es posible capturar video desde 1 _fps_ , es decir, capturando una imagen al segundo, hasta capturas con altísimas velocidades de más de 300 _fps_ en cámaras de alta velocidad. Las características del sensor, del objetivo y del obturador limitarán el número máximo de capturas que podremos realizar por segundo. En proyectos en los que tengamos que procesar objetos que se mueven muy rápido necesitaremos una gran cantidad de imágenes por segundo, lo que se traduce en un tiempo de exposición muy corto y por tanto necesidad de diagramas muy abiertos y seguramente de _global shutter_ . Sin embargo, si vamos a capturar vídeo en entornos controlados con poco movimiento, con tomar 30 imágenes por segundo será suficiente, y no necesitaremos tanta luz, podremos usar un _global shutter_ y, además, los archivos de vídeo que se generen de nuestras capturas serán mucho menos pesados. 

### **4.2. Tipología de dispositivos de captura** 

Si bien todos los dispositivos de captura están formados por un sensor, un obturador, un objetivo y una cierta electrónica, hay una enorme variedad de sensores que proporcionan información sustancialmente diferente. Conocerlos nos ayudará a decidir cuál de ellos es el más adecuado según el caso de uso al que nos enfrentemos, por lo que vamos a hacer un pequeño repaso acerca de los tipos de sensor más importantes. 

#### **Cámaras lineales** 

Las cámaras lineales son el tipo más básico de cámara, pero son totalmente desconocidas fuera del mundo de la visión artificial. Los sensores de las cámaras lineales solo tienen **una fila de píxeles** . Funcionan por tanto como un escáner o un fax. Hay una única línea sensible a la luz. Es necesario por tanto desplazar o bien la cámara o bien el objeto para obtener una imagen de más de una línea de píxeles. La gran ventaja de estas cámaras es su **altísima velocidad** de captura. Dado que no hay más que una línea, no es relevante la diferencia entre el _global_ y el _rolling shutter_ . Sencillamente capturan una línea de píxeles, la transfieren, y capturan la siguiente, de forma continua. Además, son las cámaras con mayor rango dinámico existente, y con un precio realmente asequible. 

220 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Son empleadas principalmente sobre líneas de producción, en las que los objetos se mueven a velocidades vertiginosas y las condiciones están realmente controladas. Es necesario un preprocesado de la imagen para construir imágenes matriciales después de la captura, que puedan ser procesadas por nuestros algoritmos de visión artificial. 

#### **Cámaras matriciales** 

Las cámaras conocidas como matriciales, también denominadas _frame camera_ y _area camera_ son las que nos imaginamos al pensar en una cámara. Su sensor tiene una forma rectangular (matricial) y capturan una serie de filas y columnas en el mismo momento. Como ya hemos mencionado, en este tipo de cámaras es muy importante el tipo de obturador, ya que podemos encontrar deformaciones en los objetos en movimiento. Tienen un mayor coste que las cámaras lineales, menos rango dinámico y frame rate disponible y además se pueden producir superposiciones de objetos entre las distintas capturas si la velocidad de captura, lo que haría que estemos “desperdiciando” espacio de almacenamiento. En cuanto a sus ventajas nos permite obtener directamente una imagen matricial con la que trabajar, y no es necesario desplazar la cámara ni los objetos que queremos capturar para obtener una imagen completa. Es por esto que suelen ser las cámaras seleccionadas en la inmensa mayoría de proyectos de visión artificial en los que no se trabaja con líneas de producción industriales. 

En la siguiente figura podemos observar la comparación entre ambos tipos de cámara mencionados hasta el momento. 



#### **Cámaras estereoscópicas y 3D** 

Las cámaras lineales y matriciales capturan el mundo en dos dimensiones. Con esto no nos referimos a las dimensiones de la matriz de color, sino a las dimensiones en el espacio. Una fotografía es una proyección de un mundo tridimensional en una imagen bidimensional, en función de cómo incide la luz sobre un sensor. Esto nos aporta información acerca de la forma y tamaño de los objetos, pero pierde una capacidad esencial: **medir distancias** . Al estar proyectando toda la profundidad de campo de nuestro dispositivo en un único plano – el sensor – estamos perdiendo la capacidad de medir distancias en cualquiera de las dimensiones del espacio. Los seres humanos vemos en tres dimensiones y calculamos distancias gracias a que tenemos dos ojos. Dado que cada ojo tiene una perspectiva ligeramente diferente, el cerebro puede triangular los objetos en función de la diferencia de percepción entre un ojo y otro, y calcular distancias en tres dimensiones. 

221 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Este es el mismo principio, denominado visión binocular, es que usan las cámaras estereoscópicas para visión 3D. Esta idea no tiene nada de nuevo, ya que a mediados de siglo XIX ya existían este tipo de cámaras, que permitían tomar imágenes tridimensionales que posteriormente se podían ver con un visor compuesto de dos lentes. 

En visión artificial se emplean principalmente para casos de uso relacionado con robótica y orientación en el espacio, pero también para el control de calidad relativo a cotas, tamaños y formas de distintos objetos de producción, así como para el control de aforos y conteo de personas. Prácticamente todas estas cámaras funcionan de la misma forma. Primero se toman dos imágenes a color con cada una de las cámaras, y posteriormente un algoritmo trata de simular el proceso que realiza el cerebro humano y estima una nube de puntos tridimensional en función de las diferencias observadas por cada una de las cámaras. Una simplificación de este proceso se puede observar en la siguiente imagen. 



El problema de las cámaras estereoscópicas a color es que es necesario calibrarlas, ya que no tiene forma de conocer la distancia a la que se encuentran los objetos de la propia cámara. Es posible por tanto determinar una captura tridimensional, pero sin una calibración previa no es posible tomar medidas sobre estas imágenes. 

Para tratar de solucionar este problema surgen las cámaras estereoscópicas infrarrojas, que son las más empleadas a día de hoy. Estas cámaras usan la misma perspectiva, pero sus sensores en lugar de ser sensibles a la luz visible, son sensibles a la luz infrarroja. Además, cuentan con un emisor de infrarrojos, que emite un patrón de infrarrojos determinado que ya se encuentra calibrado con la cámara. Gracias a esta idea, la cámara puede comprobar como el patrón se deforma al chocar contra distintos objetos y en función de su forma y el tiempo que la luz infrarroja tarde en volver a la cámara desde su emisión, es posible calcular la distancia real a la que se encuentra la cámara de cada objeto, permitiendo así realizar mediciones tridimensionales sin una calibración previa. 

222 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Uno de los ejemplos más conocidos de estas cámaras está fabricado por Intel, y se denomina RealSense. Son cámaras de 10 cm de largo. En la siguiente fotografía de este dispositivo podemos ver en los extremos dos cámaras con sensores infrarrojos.  En el lado derecho hay una segunda cámara RGB, para así poder ver en color el entorno y poder añadir profundidad. Por último, en el centro se encuentran dos emisores de infrarrojos que son los encargados de hacer llegar el patrón a todos los objetos que se encuentren hasta a 12 metros. Existen distintos modelos con distintos alcances, patrones, obturadores y _Frame Rates_ , por lo que es imprescindible conocer estos elementos para poder seleccionar la cámara correcta en el caso de que un caso de uso al que nos enfrentemos requiera una medición de distancia entre píxeles con precisión y sin requisitos de calibración previos. 



#### **Cámaras infrarrojas y termográficas** 

Ya hemos visto de pasada las cámaras infrarrojas para capturar información en tres dimensiones del entorno. Este no es el único uso de los sensores sensibles a la radiación infrarroja. La radiación infrarroja es una radiación electromagnética – como la luz – que se encuentra fuera del espectro visible, es decir, los seres humanos no podemos percibirla con nuestros ojos. El espectro visible incluye todas las longitudes de onda electromagnética que pueden ser percibidas por lo seres humanos, y se encuentran entre 400 y 700 nm. Desde las longitudes de onda más pequeñas en este espectro visible que corresponden a los colores azules y violetas hasta las longitudes de onda más elevadas que corresponden a los colores rojos, todas las ondas electromagnéticas entre estos valores son percibidas en forma de colores por nuestro sentido de la vista. 

Sin embargo, las ondas no se quedan entre estas longitudes de onda. De hecho, las longitudes de onda más pequeñas corresponden a los rayos cósmicos y los rayos gamma, que son inferiores a un nanómetro. Por el contrario, las ondas con una longitud de onda mayor son las que empleamos para transmitir señales de radar y radio, tanto en onda corta, media y larga. Cerca de nuestro espectro visible se encuentran dos tipos de ondas, una a cada extremo del espectro visible, que son las ondas ultravioletas y las ondas infrarrojas. 

Las ondas infrarrojas son, por tanto, aquellas ondas de más de 700 nm y menos de 1 mm de longitud, que no pueden percibirse por el ojo humano ya que están “más allá del rojo”. No obstante, podemos diseñar sensores con células fotosensibles a estas ondas de igual forma que lo hacemos con la luz visible. Los materiales en este caso cambian, empleándose materiales como el nitrato de galio o el nitrato de cesio. El funcionamiento es exactamente el mismo que en los fotodiodos de luz visible. 

223 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Las cámaras infrarrojas tienen dos usos principales. Por una parte, permiten ver en condiciones de oscuridad “a ojos humanos” si se cuenta con un emisor de infrarrojos. Dado que los seres humanos no vemos este tipo de onda, podemos “iluminar” una escena con luz infrarroja para que una cámara infrarroja pueda percibirla, sin generar luz por ello y manteniendo la oscuridad desde un punto de vista humano. Esto es muy empleado en cámaras de seguridad y videovigilancia, pero no suele tener aplicaciones en visión artificial. Sin embargo, hay otra aplicación de las cámaras sensibles a la luz infrarroja que son realmente útiles en visión artificial: las cámaras termográficas. 

Una cámara termográfica, también denominada cámara térmica, tiene las mismas características que una cámara infrarroja: un sensor sensible a la luz infrarroja. Tienen un añadido muy interesante, y es que calibran la intensidad de luz infrarroja con la temperatura de los cuerpos que observan. Todos los cuerpos emiten una cierta cantidad de radiación infrarroja asociada a su temperatura siempre y cuando estén por encima del cero absoluto de temperatura (-273º C). Cuanto más intensa es la radiación infrarroja, más caliente está el cuerpo. Esta relación permite calibrar una cámara infrarroja para medir temperatura, ya que, según la intensidad de cada uno de los píxeles, podemos asociar un valor de temperatura a los mismos. Un dato a tener en cuenta a la hora de emplear cámaras infrarrojas y termográficas es que las lentes que se emplean en este tipo de dispositivo son distintas que, en las cámaras de espectro visible, ya que el cristal bloquea la luz infrarroja por lo que las lentes para este tipo de cámaras están fabricadas de otros materiales como el germanio o el fluoruro de calcio. Es probable que hayamos visto imágenes de cámaras termográficas en una escala de colores como la siguiente. La realidad es que las cámaras termográficas – y las infrarrojas en general – son monocromáticas, ya que solo capturan la intensidad de onda y no colores (no podríamos verlos). Estos colores que observamos son una colorización artificial de las imágenes en las que en lugar de representar el 0 como negro puro y el 255 como blanco puro, se cambian estos colores por una escala que habitualmente va desde el azul/morado en los colores cercanos a 0 al rojo/amarillo en los colores cercanos a 255 sencillamente para facilitar la comprensión de este tipo de imágenes. A la izquierda vemos la representación de una imagen infrarroja en escala de grises, y a la derecha recolorizada. 



Encontraremos proyectos de visión artificial en los que por motivos de oscuridad absoluta en la captura, o por un interés especial en la temperatura de los objetos observados, necesitaremos emplear este tipo de sensores para solucionar el problema que plantee el cliente. 

224 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

#### **Cámaras multiespectrales e hiperespectrales** 

El último tipo de cámara que vamos a analizar está comprendido por las cámaras multiespectrales e hiperespectrales. Hemos visto cómo existen sensores capaces de analizar ondas electromagnéticas más allá del espectro visible, como las cámaras infrarrojas. Estas cámaras capturan la intensidad de una onda en un rango distinto al visible, y la proporcionan en un valor de 0 a 255. Si bien esto permite conocer la temperatura de los objetos, o tener visión nocturna, hay una información que se pierde en las cámaras infrarrojas. Esta información perdida es el valor de intensidad **en cada longitud de onda** . Una cámara infrarroja indica la intensidad de cualquier onda entre 700 nm y 1 mm (o cualquier otro rango), pero no especifica de qué longitudes de onda concretas procede esta radiación. ¿Para qué querríamos conocer este dato? 

Desde hace más de un siglo se conoce que los distintos elementos químicos, moléculas y materiales, tienen una determinada firma espectral, también denominada huella espectral. Cada objeto concreto refleja la radiación infrarroja de una forma distinta. En función de su composición molecular absorberá unas longitudes de onda u otras de forma única. Esto puede ayudarnos a clasificar materiales y moléculas de una forma que la visión en el espectro visible no es capaz de hacer. También puede que necesitemos información detallada acerca de qué longitudes de onda generan qué intensidades. Una cámara RGB divide el espectro visible en tres partes, y analiza la intensidad en cada una de ellas. Existen cámaras multi e hiperespectrales en el espectro visible que son capaces de proporcionarnos información de intensidad en cinco dimensiones, en siete dimensiones e incluso en doce dimensiones. En este caso, trabajaremos con imágenes de más de tres dimensiones, por lo que deberemos adaptar la entrada de nuestros algoritmos y redes neuronales para que puedan trabajar con estas dimensiones, pero el funcionamiento tanto de las técnicas clásicas como de las CNN serán exactamente los mismos, y los procesos de preprocesado y extracción de características también. 

Existen distintos tipos de cámara multiespectral, e incluso contamos en la actualidad con cámaras hiperespectrales. Cada una de estas cámaras es capaz de captar la intensidad de la onda en un rango muy pequeño de longitudes de onda denominados “bandas”. 

Por ejemplo, una cámara puede procesar tres bandas si analiza la intensidad en las siguientes bandas: 700-799 nm, 800-899 nm, 900-999 nm. En este caso, la salida de nuestra cámara multiespectral sería una matriz tridimensional, igual que las matrices RGB. Sin embargo, en este caso las dimensiones no harían referencia al color, sino a las distintas bandas en las que la cámara captura la intensidad de la luz. 

225 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

Las cámaras hiperespectrales llegan a tener hasta 224 bandas, lo que quiere decir que su _output_ está formado por 224 matrices de intensidad. Gracias a esta información podemos desarrollar redes neuronales de clasificación, detección o segmentación de objetos que, en lugar de contar con tres dimensiones de entrada, cuentan con 224, con las ventajas y desventajas en cuanto a precisión y necesidad de capacidad de cómputo que esto conlleva. La diferencia entre una cámara multiespectral e hiperespectal es, en esencia, la cantidad de bandas que tienen. Cuantas más bandas tenga la cámara, más continua será la firma espectral que obtengamos, y más sencillo será clasificar materiales y moléculas, aunque más pesados serán los archivos que tendremos que manejar. En la siguiente imagen podemos analizar visualmente la diferencia entre ambos tipos de cámara. 



Este espectro capturado es el que posteriormente procesaremos con una CNN como si de una imagen normal se tratara. Sin embargo, tendremos numerosas dimensiones que nos ayudarán a conocer características de nuestros objetos que no sería posible conocer mediante luz visible. Este tipo de cámaras se emplean en aplicaciones generalmente relacionadas con la agricultura – para conocer el nivel de irrigación de un campo, la madurez de un fruto o la presencia de plagas – con el control de calidad alimentario – para detectar objetos extraños no deseados en la línea de producción o para controlar la podredumbre de los alimentos – y con el reciclaje de materiales – donde se trata de diferenciar materiales para hacer el proceso de reciclaje más eficiente – entre otros. 

Las cámaras espectrales suelen tener la capacidad de ver un rango determinado de longitudes de onda. Estos rangos se han clasificado de forma que cada cámara está especializada en un conjunto de ondas específico. Los principales son el espectro ultravioleta, la luz visible, el espectro cercano a la luz visible NIR ( _near infra red_ ), infrarrojos de onda corta (SWIR), infrarrojos de onda media (MWIR) e infrarrojos de onda larga (LWIR). Cada uno de estos rangos de longitudes de onda permiten detectar ciertas características de los materiales, por lo que tienen un uso concreto en cada caso. 

226 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

### **4.3. Origen de la captura** 

Para todo proyecto real de visión artificial hay dos opciones principales respecto a la captura de imágenes que debemos conocer y saber cómo afrontar en cada caso: 

1. **Captura de imágenes proporcionada por el cliente.** En este caso las imágenes pueden venir dadas por una serie de fuentes sobre las que no tendremos control, por lo que la mayor dificultad provendrá de adaptar los algoritmos a las condiciones dadas de captura, que generalmente distarán de ser óptimas: 

   - a. Señal de video de CCTV (circuito cerrado de televisión). En este caso el cliente tiene instaladas cámaras de seguridad y desea que empleemos la señal que estas ofrecen para ejecutar un proyecto de visión artificial. Esto significa un riesgo alto de oclusiones, mala perspectiva, resolución insuficiente de la imagen, iluminación deficiente… Es una opción que habitualmente es recomendable evitar, ya que no tendremos ningún control sobre estas circunstancias y esto podría perjudicar a nuestro sistema. 

   - b. Señal de video de TV o en streaming. Si nuestro cliente es un medio de comunicación o difusión, lo más probable es que nos solicite emplear la señal de video que genera dicho medio para el procesado de nuestros algoritmos. La buena noticia en este caso es que este tipo de señales están tremendamente cuidadas por parte del _broadcaster_ en términos de iluminación, foco, nitidez… Por lo que habitualmente ofrecen mucho mejores prestaciones que la señal de CCTV. El principal problema con este tipo de captura de imágenes es relativo a las oclusiones y la potencial diferencia entre lo que el realizador desea mostrar y lo que nuestro sistema debe ver, por lo que también es una opción con un riesgo moderado asociado. 

   - c. Imágenes capturadas por dispositivos móviles. En este supuesto, el cliente pretende que los usuarios del sistema capturen imágenes mediante sus propios dispositivos móviles (teléfonos inteligentes o tabletas). Este es el caso más arriesgado de todos, ya que no solo dependemos de la habilidad del usuario como fotógrafo, sino también de las características del hardware de cada uno de estos posibles dispositivos móviles como pueden ser la óptica, el sensor, la resolución de la captura, el software de preprocesado automático… Sin embargo, hay proyectos en los que este tipo de captura es inevitable. En este tipo de proyectos es altamente recomendable, si no indispensable, recurrir a modelos basados en _deep learning_ que sean capaces de lidiar con la variabilidad que encontraremos en las distintas imágenes o videos capturados como resultado de un grupo de numerosos usuarios con distintos dispositivos cada uno. 

227 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

   - d. Otro tipo de capturas: Encontraremos clientes que desean trabajar con imágenes tomadas por satélite, con cámaras instaladas en vehículos autónomos, con imágenes infrarrojas de seguridad e incluso con cámaras termográficas ya instaladas en procesos industriales. En estos casos será necesario evaluar si la captura propuesta tiene las condiciones mínimas necesarias para poder (satélites, vehículo autónomo, cámaras termográficas) 

2. **Captura de imágenes seleccionada por el desarrollador.** 

### **4.3.1. Selección de un conjunto de componentes** 

Con todos los elementos que hemos estudiado hasta el momento llega el momento crucial en toda fase de captura en visión artificial: seleccionar los componentes necesarios para nuestro proyecto.  Para hacerlo, tendremos que hacernos una serie de preguntas cuyas respuestas influirán en el equipamiento que necesitaremos. 

- ¿Es suficiente trabajar con luz visible? En la mayoría de los casos será suficiente con trabajar con ondas electromagnéticas dentro del espectro visible (400 nm – 700 nm) pero puede que encontremos proyectos en los que por motivos como la falta de iluminación, la necesidad de conocer temperaturas, o requisitos de clasificación que no pueden ser satisfechos únicamente observando luz visible; necesitemos dispositivos como cámaras de infrarrojos o espectrales. 

- ¿Necesito medir distancias en tres dimensiones? Las cámaras matriciales y lineales ofrecen muy buenos resultados en 2 dimensiones. Si necesitamos medir la distancia real entre dos píxeles es probable que debamos optar por una cámara estereoscópica – de espectro visible o infrarrojo – para poder acometer este problema de visión artificial. 

- ¿La uniformidad, constancia y falta de ruido son un requisito indispensable? En caso afirmativo deberíamos plantearnos optar por un sensor CCD, a pesar de su elevado coste y menor robustez. En caso contrario, podremos optar por un sensor CMOS, más sencillo de encontrar y más asequible. 

- ¿A qué distancia se encuentra el objeto que deseo capturar? Según esta respuesta podremos necesitar un objetivo estándar, o de menor o mayor distancia focal en función de la ampliación que necesitemos realizar sobre el objeto u objetos a procesar. 

- ¿Qué campo de visión necesito? ¿Qué tamaño tienen mis objetos? Si vamos a tener muchos objetos cercanos esparcidos, u objetos muy grandes, necesitaremos lentes con gran angular. Si por el contrario los objetos se encuentran ubicados en un lugar concreto del espacio y o bien son medianos o están lejos, necesitaremos objetivos que variarán entre estándar y teleobjetivos. 

228 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- ¿Qué profundidad de campo requiero? Si todos los objetos se van a encontrar a una distancia similar del dispositivo de captura, podré permitirme seleccionar una apertura de diafragma mayor para emplear toda la luz disponible, aunque esto implique reducir la profundidad de campo. Por el contrario, si los objetos están diseminados a lo largo de una gran profundidad, deberé cerrar el diafragma notablemente. 

- ¿De cuánta luz dispongo? Si la luz está limitada por motivos inevitables, tendremos que tener en cuenta que puede ser necesario abrir más el diafragma (perdiendo profundidad de campo, o aumentar el tiempo de exposición (pudiendo perder nitidez en objetos en movimiento). En caso de ser posible siempre es recomendable aumentar la iluminación todo lo posible para no contar con esta restricción. 

- ¿Se mueven los objetos? ¿A qué velocidad?: Si los objetos a procesar están en movimiento habrá que evaluar la velocidad para seleccionar un tiempo de exposición, tipo de obturador ( _global o rolling_ ) y _frame rate_ que se adecúen a este movimiento para evitar objetos poco nítidos y con estelas. 

Si somos capaces de responder a estas preguntas, podremos elegir el mejor dispositivo de captura posible para nuestro proyecto de visión artificial. 

Con esta sección concluimos esta asignatura de visión artificial. Hemos realizado un repaso de las técnicas más comunes de captura, preprocesado, extracción de características y aplicación de objetivos desde una perspectiva clásica y una perspectiva basada en _deep learning_ . Absolutamente todos los campos mencionados han sido descritos únicamente en su superficie, y es posible profundizar en ellos a niveles muchísimo más avanzados. Sin embargo, ahora tenemos una visión de conjunto de la disciplina de visión artificial, sus posibilidades, fortalezas y debilidades. En el caso práctico trataremos de complementar toda esta información con una investigación sobre dos temas muy relevantes que no hemos mencionado: la visión dinámica y los _Transformers_ . Esto nos acercará a la investigación en visión artificial, y nos servirá de ejemplo para descubrir las fuentes y procedimientos a seguir cada vez que tengamos que enfrentarnos a un nuevo problema de visión artificial, en un paso más hacia comprender la disciplina de la Inteligencia Artificial y sus proyectos asociados. 

229 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

## **Bibliografía** 

- Szeliski, Richard. “Computer Vision: Algorithms and Applications”. Springer. 1st Edition, 2010. 

- Md. Atiqur Rahman Ahad. “Computer Vision and Action Recognition: A Guide for Image Processing and Computer Vision Community for Action Understanding”. Atlantis Press, 2011 

- Boguslaw Cyganek. “Object Detection and Recognition in Digital Images: Theory and Practice.” John Wiley & Sons, 2013. 

- Miano, John. “Compressed image file formats JPEG, PNG, GIF, XBM, BMP”. 1999 

- A. S. Tarawneh, A. B. Hassanat, I. Elkhadiri, D. Chetverikov and K. Almohammadi, “Automatic Gamma Correction Based on Root-Mean-Square-Error Maximization”. (ICCIT-1441), 2020 

- Scott E Umbaugh, “Computer Imaging: Digital Image Analysis and Processing”. CRC Press, 2005 

- Canny, J. “A Computational Approach to Edge Detection”. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2006 

- E. Rosten; T. Drummond. “Machine learning for high-speed corner detection”. European Conference on Computer Vision, 2006 

- R. Haralick, “Ridges and Valleys on Digital Images”, Computer Vision, Graphics, and Image Processing, 1983. 

- Nicu Sebe; Ira Cohen; Ashutosh Garg; Thomas S. Huang. “Machine Learning in Computer Vision”. Springer Science & Business Media, 2005 

- Nixon, Mark; Aguado, Alberto. “Feature Extraction and Image Processing for Computer Vision (4th ed.)”. Academic Press, 2019 

- J. R. Parker. “Algorithms for Image Processing and Computer Vision (2nd ed.)”. Wiley, 2011 

- Lowe, D.G., “Object recognition from local scale-invariant features”. The Proceedings of the Seventh IEEE International Conference, 1999 

230 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- David G. Lowe, “Distinctive Image Features from Scale-Invariant Keypoints”. Int. J. Comput. Vision 60, 2004 

- Herbert Bay, Andreas Ess, Tinne Tuytelaars, Luc Van Gool, “Speeded Up Robust Features”, ETH Zurich, Katholieke Universiteit Leuven, 2007 

- P. M. Panchal, S. R. Panchal, S. K. Shah, “A Comparison of SIFT and SURF “, International Journal of Innovative Research in Computer and Communication, 2013 

- Herbert Bay, Andreas Ess, Tinne Tuytelaars, Luc Van Gool, “SURF: Speeded Up Robust Features”, Computer Vision and Image Understanding, 2008 

- Murphy, Kevin, “Probabilistic Machine Learning: An Introduction. Probabilistic Machine Learning: An Introduction”. MIT Press, 2021 

- Bottou, Léon, “Online Algorithms and Stochastic Approximations”. Cambridge University Press, 1998 

- LeCun, Yann A., et al. “Efficient backprop.” Neural networks: Tricks of the trade. Springer Berlin Heidelberg, 2012 

- Bottou, Léon, “Stochastic Learning”, Advanced Lectures on Machine Learning, Springer, 2004 

- Spall, James C., “Introduction to Stochastic Search and Optimization”, Wiley, 2003 

- Goodfellow, Ian; Bengio, Yoshua; Courville, Aaron. “6.5 Back-Propagation and Other Differentiation Algorithms”. Deep Learning. MIT Press. 2016 

- Rojas, Raúl, “The Backpropagation Algorithm”, 1996 

- Gandhi, Rohith. “R-CNN, Fast R-CNN, Faster R-CNN, YOLO — Object Detection Algorithms”. Towards Data Science. 2018 

- Kaiming He, Georgia Gkioxari, Piotr Dollár, Ross Girshick, “Mask R-CNN”, arXiv, 2017 

- Liang-Chieh Chen, George Papandreou, Iasonas Kokkinos, Kevin Murphy, Alan L. Yuille . “DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs”. arXiv, 2016, 

- Liang-Chieh Chen, George Papandreou, Florian Schroff, Hartwig Adam. “Rethinking Atrous Convolution for Semantic Image Segmentation”. arXiv, 2017 

- Joseph Redmon, Ali Farhadi. “YOLO9000: Better, Faster, Stronger”. arXiv , 2016 

231 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi. “You Only Look Once: Unified, Real-Time Object Detection”. arXiv,  2015 

- Jonathan Long, Evan Shelhamer, Trevor Darrell. “Fully Convolutional Networks for Semantic Segmentation.” arXiv, 2014 

- Hyeonwoo Noh Seunghoon Hong Bohyung Han. “Learning Deconvolution Network for Semantic Segmentation,” CvF , 2016, 

- Jun-Yan Zhu, Taesung Park, Phillip Isola, Alexei A. Efros. “Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks”, arXiv, 2017 

- Tero Karras, Samuli Laine, Timo Aila. “A Style-Based Generator Architecture for Generative Adversarial Networks”, 2018, arXiv 

- Phillip Isola, Jun-Yan Zhu, Tinghui Zhou, Alexei A. Efros, “Image-to-Image Translation with Conditional Adversarial Networks”, arXiv, 2016 

- Li, Li-Jia; Wang, Gang; Fei-Fei, Li, “OPTIMOL: automatic Online Picture collection via Incremental MOdel Learning”, Proc. IEE, 2007 

- Dalal, Navneet, “Histograms of oriented gradients for human detection”, Computer Vision and Pattern Recognition, 2005 

- Zhang, Shifeng, “Single-Shot Refinement Neural Network for Object Detection”, Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2018 

- Zhu, Xizhou , “Deformable ConvNets v2: More Deformable, Better Results”, arXiv, 2018 

- Liu, Wei, “SSD: Single shot multibox detector”. Computer Vision – ECCV 2016. European Conference on Computer Vision, 2016 

- Pang, Jiangmiao; Chen, Kai; Shi, Jianping; Feng, Huajun; Ouyang, Wanli; Lin, Dahua, “Libra R-CNN: Towards Balanced Learning for Object Detection”, arXiv, 2019 

- Hengshuang Zhao, Jianping Shi, Xiaojuan Qi, Xiaogang Wang, Jiaya Jia, “Pyramid Scene Parsing Network”, arXiv, 2016 

- Olaf Ronneberger, Philipp Fischer, Thomas Brox, “U-Net: Convolutional Networks for Biomedical Image Segmentation”, arXiv, 2015 

- Guosheng Lin, Anton Milan, Chunhua Shen, Ian Reid, “RefineNet: Multi-Path Refinement Networks for High-Resolution Semantic Segmentation”, arXiv, 2016 

232 

**Módulo. Visión Artificial** 

**Centro Europeo de Postgrado** 

- Liang-Chieh Chen, George Papandreou, Iasonas Kokkinos, Kevin Murphy, Alan L. Yuille, “Semantic Image Segmentation with Deep Convolutional Nets and Fully Connected CRFs”, arXiv, 2014 

- Liang-Chieh Chen, Yukun Zhu, George Papandreou, Florian Schroff, Hartwig Adam, “Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation”, arXiv, 2018 

- Fisher Yu, Vladlen Koltun, “Multi-Scale Context Aggregation by Dilated Convolutions”, arXiv, 2015 

- Sze, Simon Min; Lee, Ming-Kwei, “MOS Capacitor and MOSFET”, Semiconductor Devices: Physics and Technology, 2012 

- Fossum, Eric R.; Hondongwa, D. B. “A Review of the Pinned Photodiode for CCD and CMOS Image Sensors”, IEEE Journal of the Electron Devices Society, 2014 

- Nakamura, Junichi , “Image Sensors and Signal Processing for Digital Still Cameras, CRC Press, 2005 

- Chilton, Alexander, “The Working Principle and Key Applications of Infrared Sensors”, AZoSensors, 2013 

- L. J. Kozlowski and W. F. Kosonocky, “Infrared detector arrays,” McGraw-Hill, 1995 

- Chein-I Chang, “Hyperspectral Imaging: Techniques for Spectral Detection and Classification”. Springer Science & Business Media, 2003 

- Hagen, Nathan; Kudenov, Michael W. “Review of snapshot spectral imaging technologies”. Optical Engineering, 2013 

233 







**CEUPE** Centro Europeo de Postgrado 

**Web** 

www.ceupe.com 

**E-mail** info@ceupe.com 

