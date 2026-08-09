---
tags:
  - master_ia
  - teoria
source: MIA_A2_Mod5_Cognitive Devices.pdf
---

# **Módulo Cognitive Devices** 



# **Módulo Cognitive Devices** 

|**1. EVOLUCIÓN DE LOS SISTEMAS COMPUTACIONALES .......................................04**|
|---|
|1.1. LA PRIMERA GENERACIÓN (1940 A 1955): TUBOS DE VACÍO ........................06<br>|
|1.2. LA SEGUNDA GENERACIÓN (1955 A 1965): TRANSISTORES Y SISTEMAS DE|
|PROCESAMIENTO DE DATOS .................................................................................08<br>|
|1.3. TERCERA GENERACIÓN (1965 A 1975): CIRCUITOS INTEGRADOS Y<br>MULTIPROGRAMACIÓN ........................................................................................11<br>|
|1.4. LA CUARTA GENERACIÓN (1970 -1980): LAS PC O COMPUTADORAS<br>PERSONALES .........................................................................................................15|
|1.5. LA QUINTA GENERACIÓN (1980-1990 A LA ACTUALIDAD): LA ERA DE LA IA .18|
|1.6. SEXTA GENERACIÓN DE COMPUTADORAS: REDES NEURONALES<br>ARTIFICIALES .........................................................................................................25<br>|
|1.7. SÉPTIMA GENERACIÓN DE COMPUTADORAS: PARALELIZACIÓN DE CARGAS 25|
|1.8. OCTAVA GENERACIÓN DE COMPUTADORAS: NANOTECNOLOGÍA ................25|
|**2. CO-PROCESADORES ............................................................................................26**|
|2.1. ARQUITECTURA DE UN COMPUTADOR ..........................................................26|
|2.1.1. HARDWARE DE UN COMPUTADOR .........................................................26|
|2.2. COPROCESADORES MATEMÁTICOS ...............................................................38|
|2.3. COPROCESADORES DE ENTRADA / SALIDA ....................................................39|
|2.4. COPROCESADORES CRIPTOGRÁFICOS ...........................................................40|
|2.5. COPROCESADORES DE PROCESAMIENTO DE SEÑAL ......................................41|
|2.6. COPROCESADORES CUÁNTICOS ....................................................................42|
|2.6.1. GOOGLE .................................................................................................44|
|2.6.2. MICROSOFT ............................................................................................44|
|2.6.3. AMAZON WEB SERVICES ........................................................................45|
|2.6.4. IBM .........................................................................................................45|
|2.6.5. USTC (UNIVERSITY OF SCIENCE AND TECHNOLOGY FROM CHINA) ........46|
|2.7. COPROCESADORES GRÁFICOS ......................................................................46|
|2.8. TENSOR PROCESING UNIT (TPU) .....................................................................54|
|2.9. UNIDADES DE PROCESAMIENTO VISUAL ........................................................56|
|2.10 FPGA .............................................................................................................59|
|2.11. NUEVAS ARQUITECTURAS HARDWARE ........................................................62<br>|
|2.11.1. EXPERIMENTO CHIP FUSIÓN .................................................................62|
|2.11.2. BRAIN-INSPIRED COMPUTING ...............................................................63|
|2.11.3. EDGE COMPUTING ...............................................................................64|
|**3. INTERNET OF THINGS ..........................................................................................66**|
|3.1. HARDWARE ...................................................................................................71|
|3.2. REDES ............................................................................................................73|
|3.3. SOFTWARE .....................................................................................................73|
|3.4. INDUSTRIA 4.0 ...............................................................................................76|



|**4. DISPOSITIVOS Y SENSORES ................................................................................82**|
|---|
|4.1. SENSORES DE PROPÓSITO GENERAL ..............................................................83|
|4.2. SENSORES Y DISPOSITIVOS INDUSTRIALES ......................................................88|
|4.2.1. SENSORES MEMS ....................................................................................88|
|4.2.2. SENSORES DE PAR ..................................................................................89<br>|
|4.2.3. SENSORES DE VISIÓN ..............................................................................90|
|4.3. SENSORES Y DISPOSITIVOS BIOMÉDICOS .......................................................92|
|4.3.1. SENSOR GSR ...........................................................................................92|
|4.3.2. SENSOR DE RITMO CARDIACO ...............................................................93|
|4.3.3. SENSOR EMG ..........................................................................................93|
|4.3.4. SENSORES ECG .......................................................................................94|
|4.3.5. SENSOR DE HUELLA DIGITAL ...................................................................95|
|4.3.6. SISTEMAS DE IMAGEN MÉDICA ..............................................................95|
|4.3.7. DISPOSITIVOS WEREABLES ......................................................................96<br>|
|4.4. SENSORES Y DISPOSITIVOS DE DOMÓTICA ....................................................98|
|**5. INTERACCIÓN COMPUTADOR-HUMANO .........................................................103**|
|5.1. INTERFACES DE USUARIO .............................................................................104|
|5.1.1. GRAPHICAL USER INTERFACE (GUI) .......................................................105|
|5.1.2. VOICE USER INTERFACE ........................................................................107|
|5.1.3. NATURAL USER INTERFACE ...................................................................108|
|5.2. REALIDAD VIRTUAL ......................................................................................110|
|5.2.1. METAVERSO .........................................................................................113|
|5.3. NUEVOS PARADIGMAS ................................................................................114|
|**BIBLIOGRAFÍA ........................................................................................................116**|



**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

## **1. Evolución de los sistemas computacionales** 

_“En la actualidad hay múltiples empresas trabajando por liderar la revolución de la [[Índice_IA en la era del cloud computing|computación cuántica]]. IBM, Google, Intel y Honeywell son las empresas estadounidenses que ya tienen ordenadores cuánticos funcionales con una capacidad interesante como entorno de pruebas e investigación.”_ 

El origen de los sistemas computacionales empleados por los seres humanos se remonta a las antiguas civilizaciones griegas y romanas con la aparición del ábaco, considerado como el primer sistema de cálculo construido por el ser humano. Este instrumento compuesto por cuentas insertadas en varillas montadas sobre un marco rectangular permitía realizar cálculos complejos con gran rapidez y precisión. Sin embargo, este instrumento no puede ser considerado un computador ya que carece de un elemento fundamental: un programa que permita operar con él. 

A lo largo del siglo XVII los sistemas de cálculo fuero evolucionado y siendo perfeccionados. La primera calculadora mecánica que apareció fue la Pascalina, inventada por el matemático francés Blaise Pascal [1]. Esta calculadora era capaz de realizar sumas y restas de manera automática, pero debido a su complejidad y el elevado precio que suponía para la época tuvo poco éxito comercial y apenas se produjeron unas pocas unidades. Mas adelante en 1670 el filósofo y matemático Gottfied Leibniz [2] perfecciono esta máquina e invento una que también era capaz de multiplicar. A estos inventos se unieron el telar automático diseñado por el francés Joseph Marie Jacquard [3] que utilizó placas de madera perforadas para controlar el tejido y que sirvió como base para el estadístico estadounidense Herman Hollerith [4] que en la década de 1880 concibió la idea de utilizar tarjetas perforadas para procesar datos. 



Ilustración 1: Tarjeta perforada de Hollerith [5] 

04 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Durante el s.XIX apareció de la mano de Charles Babbage [6] la máquina analítica, un dispositivo que debía funcionar con un motor a vapor y habría tenido un tamaño de 30 metros de largo y 10 de ancho. Esta máquina tenía como objetivo ser un computador mecánico diseñado originalmente para construir tablas de logaritmos y funciones trigonométricas evaluando polinomios, termino convirtiéndose en el primer computador programable. El primer programa de computación fue desarrollado por Ada Lovelace [7], matemática y escritora británica considerada como la madre de la programación moderna en 1843 utilizando la máquina analítica de Babbage. Este programa consistía en un algoritmo para calcular los números de Bernoulli. Para la entrada de datos se utilizaba un sistema de tarjetas perforadas derivadas del telar de Jacquard y la salida estaba producida por una impresora, un equipo de dibujo y una campana. La máquina poseía capacidad para almacenar 1000 números de 50 dígitos cada uno y al igual que la unidad de procesamiento de un computador moderno (CPU), la máquina contaba con un molino con sus propios procedimientos internos que le permitían llevar a cabo las instrucciones del programa del usuario. 



Ilustración 2: Máquina Analítica de Charles Babbage, expuesta en el Museo de Ciencias de Londres 

Los primeros ordenadores analógicos comenzaron a construirse a principios del siglo XX. Estos realizaban cálculos mediante ejes y engranajes giratorios y permitían evaluar aproximaciones numéricas de ecuaciones complejas. Algunas de las primeras aplicaciones de este tipo de sistemas podemos encontrarlas en la primera y segunda guerra mundial donde comenzaron a utilizarse sistemas informáticos analógicos primero mecánicos y luego eléctricos en la predicción de la trayectoria de torpedos submarinos y el manejo de bombas a larga distancia. 

05 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Sin embargo, la historia y la evolución de la computación moderna se considera que comienza a partir de los años cuarenta con la aparición de los primeros computadores basados en tubos de vacío. 

### **1.1. La primera generación (1940 a 1955): tubos de vacío** 

Durante la década de los cuarenta surgieron distintas investigaciones a nivel mundial en el campo de la computación que sirvieron como primera generación de los ordenadores que conocemos hoy en día. Esta generación se caracteriza por la utilización de la tecnología de tubos de vacío, lo cual se traducía en ordenadores de enormes dimensiones que requerían un espacio físico muy grande para poder operar con ellos. 

La primera computadora que podemos definir como tal fue el Z3 creada por Konrad Zuse [8] en 1941. Esta fue la primera máquina programable y completamente automática que podemos encontrar en la primera generación de computadores. Pese a que esta máquina se clasifica de manera general en la primera generación esta no utilizaba la tecnología de tubos de vacío si no tecnología electromecánica, ya que contaba con 2300 relés que trabajaban con una frecuencia de 5Hz. Esta máquina trabajaba con aritmética en coma flotante binaria y tenia una longitud de palabra de 22 bits. 

A partir de 1943 comienza el desarrollo del primer gran computador de propósito general basado en la tecnología de los tubos de vacío. Este computador conocido como ENIAC por su acrónimo en inglés Electronic Numerical Integrator And Computer era una máquina capaz de ser programada para resolver una serie problemas numéricos, digital y considerada como Turing-completa. Esta máquina fue desarrollada por el laboratorio de investigación balística de Estados Unidos y al frente de su desarrollo estuvieron los ingenieros John Presper Ecket y John William Mauchly, junto a las mujeres encargadas de programar la computadora  Betty Snyder Holberton, Jean Jennings Bartik, Kathleen McNulty Mauchly Antonelli, Marlyn Wescoff Meltzer, Ruth Lichterman Teitelbaum y Frances Bilas Spence. 



Ilustración 3: Computador ENIAC [9] 

06 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Esta computadora se basaba en la tecnología de los tubos de vacío, componente electrónico utilizado para amplificar o conmutar una señal eléctrica mediante el control del movimiento de los electrones en un espacio vacío a muy baja presión. Este tipo de tecnología requería de una gran cantidad de electricidad, la computadora ENIAC tenia mas de 17000 tubos de vacío y consumía entorno a 150 kilovatios de potencia eléctrica [10]. Estos tubos eran de una gran importancia ya que el mínimo fallo en uno de los miles de tubos que conformaban la computadora podía dar lugar a errores en los resultados calculados por lo que en la construcción de este tipo de computadores se emplearon tubos de calidad especial para el servicio informático con unos estándares mas altos en materiales, inspección y pruebas que los tubos estándar. 



Ilustración 4: Tubo de vacío usado en computación 

Además de tubos de vacío el computador ENIAC contaba con 1500 relés, 7500 interruptores, miles de resistencias, condensadores e inductores. Este sistema pesaba entorno a unas 30 toneladas y ocupaba una habitación de 6x12 metros, además requería de un importante equipo de aire acondicionado para poder disipar el gran calor que producía. La complejidad de este sistema unido a las limitaciones de hardware de la época hacia que las válvulas fallaran con bastante frecuencia, especialmente durante el encendido y el apagado de la máquina, por lo que los ingenieros trataron de reducir estos fallos tomando la decisión de no apagar el ENIAC. De acuerdo con una entrevista a Eckert en 1989 el fallo de las válvulas ocurría aproximadamente cada dos días. 

A el ENIAC le sucedió una versión modificada propuesta por Jonh Von Newmann [11] conocido como EDVAC por su acrónimo en inglés Electronic Discrete Variable Automatic Computer y que fue construido en 1952. Al igual que el ENIAC este computador fue diseñado en el laboratorio de balística del ejército de Estados Unidos. Las principales diferencias entre ambos computadores es que el este último empleaba aritmética binaria en lugar de decimal como hacia el ENIAC y en segundo lugar que este permitía trabajar con un programa almacenado. El ENIAC se programaba enchufando centenares de clavijas y activando un pequeño número de interruptores. Cuando había que resolver un problema distinto, era necesario cambiar todas las conexiones, proceso que llevaba muchas horas. 

07 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Generalmente para cada máquina existía un grupo de profesionales ingenieros que diseñaban, construían, programaban, operaban y daban mantenimiento a estas grandes máquinas, por lo que era muy costoso económicamente mantenerlas, además toda la programación se realizaba en lenguaje binario o mediante conexiones de cables a tableros de conexiones o plugboards para controlar las funciones básicas de la máquina. Los lenguajes de programación o incluso el lenguaje ensamblador era desconocido. 

Cabe destacar en el desarrollo de estas tecnologías el papel de las mujeres en la programación de estos computadores. Durante el desarrollo del proyecto, las profesionales encargadas de llevar a cabo la programación de estos computadores eran mujeres. Este equipo era considerado como sub-profesionales posiblemente por una cuestión de género o para reducir costos laborales, sin embargo, su trabajo caracterizado por habilidades matemáticas y lógicas supuso la invención de la programación tal como la conocemos en la actualidad. 

### **1.2. La segunda generación (1955 a 1965): transistores y sistemas de procesamiento de datos** 

Esta segunda generación estuvo caracterizada por la incorporación del transistor a las computadoras, lo que las hizo mas accesibles y ágiles. Esta nueva generación de computadores reemplazaba las válvulas de vacío por circuitos lo que reducía el consumo de electricidad haciéndolas mas confiables y menos costosas. A diferencia de la primera generación que se perdía mucho tiempo en terminar algún trabajo para seguir con el siguiente, esta generación evoluciono en gran sentido esa desventaja con la aparición de sistemas operativos diseñados para hacer mas fluida la transmisión entre trabajos. Es en este punto cuando comienzan los sistemas de procesamiento por lotes. 

Los transistores fueron desarrollados por los laboratorios Bell en el año 1947 por un grupo de científicos dirigido por William Shockley, impulsados por la necesidad de encontrar un sucesor a las válvulas de vacío empeladas en ese momento se utilizaban como elemento de comunicación a modo de amplificador de señal en computación. Estos nuevos dispositivos permiten realizar las mismas funciones que los tubos de vacío pero con tres ventajas principales: son mas fiables, mas pequeños y mas eficientes. 

Durante los años 50 los transistores comenzaron a utilizarse en las radios portátiles, pero no fue hasta la segunda mitad de la década cuando empezaron a emplearse este tipo de dispositivos en las computadoras. Las principales ventajas que presentaba el uso de esta tecnología pasaba por un aumento de la velocidad, fiabilidad y eficiencia, mientras que se reducía el tamaño de los computadores, el consumo eléctrico y la necesidad de ventilación ya que estos dispositivos eran mas estables y se calentaban menos. 

08 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 5: Comparación de un transistor (izq) con un tubo de vacío (dcha) 

En esta época aparecieron también los primeros lenguajes de programación. En 1957 IBM desarrollo el lenguaje de programación Fortran [12] con el objetivo de crear una alternativa a los lenguajes de ensamblador para el computador IBM 704. Este computador fue el primero producido en masa con arquitectura basada en aritmética de coma flotante y estaba caracterizada por emplear memoria de núcleos en lugar de utilizar tubos de Williams como en la generación anterior. 

Los programadores de Fortran utilizaban tarjetas perforadas de 80 columnas, que sirvieron como precursoras de los shells e interpretes de comandos modernos. 

Durante este periodo también se estableció también el primer estándar universal para el intercambio de información. Este es el conocido como ASCI (American Standard Code for Information Interchange) y fue desarrollado por el Comité Estadounidense de Estándares como una evolución de los códigos utilizados en ese momento en telegrafía. 

Durante la segunda generación se produjo una gran inversión por parte de la industria en el desarrollo de estas tecnologías, ya que la reducción de costes abría un nuevo mercado de consumidores finales mucho mas extenso. Esto permitió democratizar el uso de los computadores que hasta ese momento las computadoras habían estado restringidas a las élites empresariales y gubernamentales. 

Algunos de los sistemas operativos mas destacados que se desarrollaron para esta nueva generación de computadores fueron los siguientes: 

- GM-NAA I/0 (Input and Output system o sistema de entrada/salida) [13]: Este es considerado como el primer sistema operativo de la historia, fue creado en 1956 por Robert L. Patrick de General Motors y Owen Mock de North American Aviation para operar con el ordenador de IBM 704. Este sistema estaba basado en el sistema de procesamiento por lotes y su principal función es que ejecutaba automáticamente un nuevo programa cada vez que terminaba la ejecución del anterior. 

09 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- SOS (Share Operating System o Sistema operativo compartido) [14]: Este sistema operativo se planteo como una mejora del GM-NAA con el objetivo de mejorar el sistema de compartición de programas. Este SO presentaba mejoras en la gestión de buffers y los dispositivos de entrada/salida del computador. Este sistema fue creado por el grupo de usuarios SHARE en 1959 para el sistema de IBM 709. 

- El FMS (Fortran Monitor System o sistema de monitoreo Fortran): Este sistema operativo fue desarrollado por IBM para compilar programas de Fortran en las computadoras IBM 709 y posteriormente migrándolo las IBM 7090 e IBM 7094 bajo el nombre de IBSYS 

- IBSYS: Este sistema fue creado por IBM, basado en el FMS y SOS, fue era el sistema operativo de IBM 7090/94. 

De la misma forma que se produjo un enorme avance en los sistemas operativos disponibles para los nuevos computadores, este avance también se vio en los nuevos modelos de hardware disponibles durante esta segunda generación. Algunos de los computadores mas destacados de esta era son los siguientes: 

- IBM 1401: El IBM 1401 supuso una revolución en el área de la computación ya que era un ordenador compacto disponible para el publico general y que las empresas odian comprar o alquilar. El IBM 1401 salió al mercado en 1959. Funcionaba con un sistema de tarjetas perforadas a través de las cuales se introducían los datos. Era fácil de programar en comparación con otros ordenadores de la época. La empresa había avanzado notablemente en términos de usabilidad y había lanzado un software más accesible. 

- Honeywell 800: Este computador fue anunciado en 1958 y lanzado al mercado en 1960 bajo las siglas H-800. Incluía 6.000 transistores en un sistema básico que se podía complementar con periféricos adicionales y bancos de memoria extra, además de una opción multiprograma que, básicamente, permitía el funcionamiento simultáneo de varios programas distintos, cada uno con sus propios registros. 

- IBM 1620: Este computador fue presentado por IBM en 1959 bajo la premisa de presentar un “equipo científico económico”. En esta serie también se sustituyeron las válvulas por transistores y, como el 1401, empleaba un sistema de tarjetas perforadas (inicialmente, fueron cintas perforadas, pero, poco después de su lanzamiento, se pasó a las tarjetas). Su memoria de núcleo magnético que abarcaba más de 60.000 dígitos decimales. 

10 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 6: Un Sistema IBM 1401. Desde la izquierda: lector/perforador 1402, procesador 1401, impresora 1403. [15] 

- PDP-1: Digital Equipment Corporation (DEC) fue una empresa estadounidense que se especializó en computadoras de tamaño reducido. Fundada en 1957, en los 80 fue una de las compañías líderes en fabricación y venta de ordenadores a nivel mundial. Y se estrenó en la segunda generación de computadoras, con su PDP-1 (Programmed Data Processor 1), un diseño de Ben Gurley que se empezó a producir en 1960. 

### **1.3. Tercera generación (1965 a 1975): circuitos integrados y multiprogramación** 

La tercera generación de computadores estuvo caracterizada por el diseño de los primeros chips lo que supuso un importante avance en la democratización de la informática. Al igual que el salto de la primera generación a la segunda estuvo marcado por la aparición de los transistores, que permitían reducir el tamaño de las computadoras y mejorar su rendimiento, el cambio de la segunda a la tercera generación estuvo motivado por la aparición de los circuitos integrados. 

El circuito integrado fue una invención de Robert Noyce [16] cofundador de Fairchild Semiconducto e Intel y Jack S. Kilby [17] trabajador de Texas Instruments, dos científicos que, en compañías diferentes y sin tener conocimiento mutuo de sus investigaciones, dieron con la forma de crear circuitos electrónicos en una sola pieza. Y, además, lo hicieron casi al mismo tiempo. Los CI se hicieron posibles gracias a descubrimientos experimentales que mostraban que artefactos semiconductores podían realizar las funciones de los tubos de vacío, así como a los avances científicos de la fabricación de semiconductores a mediados del siglo XX. La integración de grandes cantidades de pequeños transistores dentro de un pequeño espacio fue un gran avance en la elaboración manual de circuitos utilizando componentes electrónicos discretos. La capacidad de producción masiva de los circuitos integrados, así como la fiabilidad y acercamiento a la construcción de un diagrama a bloques en circuitos, aseguraba la rápida adopción de los circuitos integrados estandarizados en lugar de diseños utilizando transistores discretos. 

11 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Las principales ventajas que presentaban estos circuitos integrados frente a los transistores de la generación anterior se centraban en la reducción del coste de fabricación y en un aumento del rendimiento. Antes de la creación del chip, los circuitos electrónicos se construían interconectando componentes creados de forma independiente y en distintos materiales. Se fabricaba un transistor, una resistencia, un condensador y estos se conectaban. Kilby llevó todos estos componentes a un único bloque de silicio en el que los componentes se conectaban con hilos de oro. Por su parte Noyce, conocido como el alcalde de Sylicon Valley se baso en el planar process de su colega Juean Hoerni con el que trabajaba en Fairchild Semiconductor. El desarrollo de esta tecnología no esta extenta de polémica debido a la partida de Noyce junto a siete de sus colegas de Shockley Semiconductor Laboratory, para fundar Fairchild Semiconductor. Esta huida causada por la mala relación con William Bradford Shockley el fundador de Shockley Semiconductor Laboratory ha pasado a la historia como los 8 traidores de Silicon Valley y podría convertirse en una serie de Netflix. Como curiosidad puedes leer más sobre sobre esta historia en el siguiente artículo: <u>https://agenciab12.com/noticia/8-traidores-de-silicon-valley</u> 



Ilustración 7: El primer circuito integrado funcional de Jack Kilby. Un solo transistor y componentes secundarios en una capa de germanio. (Museo Nacional de Historia Estadounidense) [17] 

La inclusión de la tecnología de los circuitos integrados las computadoras aumentó el poder de las mismas, por lo cual se pudieron implementar cambios más que importantes. Todas estas novedades permitieron que fueran mucho más flexibles, y que pudieran ser utilizadas con diferentes propósitos. 

Uno de los principales obstáculos que presentaban las computadoras disponibles hasta el momento era la compatibilidad entre sí. Las compañías que adquirían computadores debían invertir una gran suma de dinero en el mantenimiento de estas máquinas que no podían interactuar con otras de su misma generación. En esta línea IBM introdujo la línea de computadores System 360, que contaban con software compatible y una arquitectura de circuitos integrados que se adoptó como estándar de la industria. 

12 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

La multiprogramación en esta generación se hizo una técnica popular para crear los sistemas operativos, es básicamente particionar la memoria, cada una con distintos trabajos, lo que redujo en gran medida la brecha del tiempo ejecución y terminación de un trabajo con el siguiente. 



##### Ilustración 8: Esquema de multiprogramación 

Otra técnica fue el Spooling u operación simultánea de periféricos en línea, permitía al sistema operativo ejecutar trabajos conforme era necesario, cada que terminaba una ejecución de un programa, el sistema operativo cargaba el siguiente en la partición que había quedado vacía y posteriormente lo ejecutaba, con esta técnica desapareció en gran medida el uso del transporte de cintas. 

A pesar de grandes avances, el tiempo de presentación de un trabajo y terminación de la misma seguía siendo de unas horas. Una respuesta a lo anterior, se opto por una variante de la multiprogramación llamada el tiempo compartido o el CTSS (sistema serio de tiempo compartido) en la que cada usuario tiene una terminal en línea y varios procesos podían ejecutarse en el CPU. 

Si durante la segunda generación aparecían los primeros computadores de uso empresarial, con la llegada de esta nueva generación la apuesta por las computadoras de uso generalista para empresas se hizo mas patente. Algunas de las computadoras mas representativas de esta generación son: 

- IBM 360: Este sistema supuso el salto entre la segunda generación y la tercera. Anunciada en 1964 supuso la confluencia de las dos líneas de trabajo con las que operaba IBM en ese momento, la línea comercial y la línea científica. La IBM 360 es una de las más importantes computadoras comerciales de esta generación, debido fundamentalmente gracias a que incluía funciones que le permitían al dispositivo realizar análisis numéricos, administración o procesamiento de archivos, es decir que podía ser programada para cumplir con múltiples propósitos. Asimismo, dada la mayor capacidad y velocidad de estos modelos, se podían ejecutar varios de programas de forma simultánea, a través de la multiprogramación. Tal fue el éxito de estas computadoras que IBM logró fabricar y vender más de 30.000. 

13 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- Burroughs B-2500 y B-3500 [18]: Burroughs presento sus modelos B-2500 en 1966 entrando de lleno en la tercera generación de computadores. Estos computadores estaban desarrollados y fabricados por Burroughs [19] Corporation en Pasadena, California y se caracterizaban por estar orientados a mejorar la experiencia del usuario e incrementar la eficiencia en el trabajo. Estos computadores operaban directamente con datos decimales de COBOL y mientras el ENIAC podía almacenar veinte números de diez dígitos, estos podían almacenar millones de números. 

- PDP: La familia de las computadoras PDP o Computer Data Processor fueron una serie de ordenadores fabricados por la compañía Digital Equipment Corporation en la década de los 60. El primer ordenador de esta línea fue el PDP-1 y es conisderado como el primer miniordenador de la historia. A este le siguió toda una línea de ordenadores con distintas arquitecturas, entre las que mas destaco fue la PDP-8. Se lanzó en abril de 1965 al mercado la Straight 8, también llamada PDP-8, perteneciente a Digital Equipment Corporation y supusieron una completa revolución debido a su manejabilidad. Este modelo fue uno de los primeros ordenadores de sobremesa disponibles para el público general y la empresa logró vender mas de 50.000 de estos modelos gracias a presentar un precio bastante accesible. La aparición de las PDP tuvo gran influencia en el desarrollo del sistema operativo UNIX, donde un programador escribió en una PDP-7 una versión reducida de MULTICS para un usuario. UNIX se dio a conocer principalmente en el mundo académico, el código fuente se podía obtener fácilmente y  muchos desarrollaron sus versiones incompatibles entre sí. A razón de esto IEEE creo un estándar para UNIX llamado POSIX que define una interfaz de llamadas al sistema que todas las versiones de UNIX deben reconocer. 



Ilustración 9: Minicomputadora Digital Equipment Corp PDP-8 [20] 

14 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

### **1.4. La cuarta generación (1970 -1980): las PC o computadoras personales** 

La cuarta generación de computadores estuvo caracterizada por la aparición del microprocesador que permitió la aparición de una nueva era de ordenadores más precisos, más pequeños y más baratos. Estos ordenadores se asemejan mucho más a los ordenadores que podemos utilizar hoy en día, ya que esta generación se conoce como la era de los computadores personales. Las principales empresas tecnológicas que se encontraban en la carrera de desarrollo de computadoras dieron un giro en su estrategia y comenzaron a orientar sus productos hacia un ámbito doméstico, sin dejar atrás las áreas empresariales. 

Los circuitos LSI o integración a gran escala, que contenían miles de transistores en un chip de silicio, fue un gran avance de la electrónica y ciertamente el principio de las computadoras personales. La primera compañía en presentar un microprocesador fue Intel. Esta compañía fundada en 1968 por Gordon Moore [21] y Robert Noyce [22], quienes inicialmente quisieron llamar a la empresa Moore Noyce, pero sonaba mal, por lo que eligieron como nombre las siglas de Integrated Electronic, en español Electrónica Integrada. 

Esta compañía comenzó en el mercado de la computación fabricando memorias, donde se convirtieron en lideres de mercado gracias a sus diseños de memoria DRAM, SRAM y ROM, sin embargo, lo que supuso una revolución y por lo que han pasado a la historia como compañía ha sido por el desarrollo de microprocesadores. 

Intel [23] presento el 15 de noviembre de 1971 el Intel 4004 [24] diseñado por Gordon Moore y Robert Noyce. Este es considerado como la primera CPU completa construida en una sola pieza, ya que hasta este momento las CPUs tenían sus componentes divididos en varios chips distintos. Este microchip se presento originalmente para facilitar el diseño de una calculadora. En lugar de incluir varios circuitos integrados específicos para cada parte de la calculadora, diseñaron uno que permitía realizar todas ellas. 



Ilustración 10: Microchip Intel 4004 [24] 

15 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Como evolución de este microprocesador, Intel anunció en 1972 el procesador Intel 8008 [25] que permitía acceder a más memoria y procesar 8 bits. La velocidad de reloj de este procesador alcanzaba los 740 Hz. Tras este procesador Intel lanzo el Intel 8080, el primer procesador que se integro en un ordenador personal [26]. El primer ordenador personal presentado por Intel fue el conocido como Altair, que contenía el procesador 8080 que permitía multiplicar el rendimiento de microchips previos al alcanzar una velocidad de reloj de 2Mhz y contener una memoria de 64 kb. Este ordenador supuso la chispa del ordenador personal y el bus de computador diseñado para esta máquina se convirtió en el estándar de facto conocido como el S-100. El primer lenguaje de programación para esta máquina fue el Altair BASIC [27] desarrollado por Bill Gates y Paul Allen, quienes lo escribieron previamente a la fundación de Microsoft. 

Sin embargo, el ordenador personal no se popularizó hasta la aparición de IBM, en el mercado. Algo que sucedió en dos ocasiones en los meses de junio de 1978 y de 1979. Fechas en las que respectivamente, hacían su aparición los microprocesadores 8086 y 8088, que pasaron a formar el denominado IBM PC, que vendió millones de unidades de ordenadores. IBM hasta ese momento únicamente contaba con un proyecto de bajo presupuesto llamado Project Chesse para los ordenadores personales. Este se basaba en utilizar un hardware ya existente y para ello tomaban como ejemplo los ordenadores derivados del Altair, sin embargo, la producción de la CPU mas avanzada (68000) no estaba lista para producirse en masa por lo que se aceptó la presencia de un segundo proveedor que proporcionaba los procesadores 8086 y 8088. En este caso el proveedor encargado de proporcionar estos procesadores fue AMD. 

A principios de los 80, IBM rediseña su IBM PC con un sistema operativo de Seattle Computers Products modificado por Microsoft, el MS-DOS [28] (sistema operativo en disco de Microsoft) que se basaba en características tomadas de UNIX. 



Ilustración 11: IBM PC 5150 

16 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

A pesar de los avances la operación de estos equipos se basaba en línea de comandos a través de teclado. En este momento fue cuando Apple produjo un cambio radical en el mercado presentando el primer ordenador Macintosh con interfaz gráfica de usuario. 

Hasta ese momento Apple, había comercializado varias generaciones de ordenadores personales diseñados por Steve Jobs y Steve Wozniak ‘Woz’, entre los que destacaron el Apple I, primer producto comercializado por la compañía en 1976 y el Apple II con el que lograron posicionarse dentro del mercado. Este último contaba con incluía un procesador MOS 6502 y estaba basado en una arquitectura de 8 bits. Entre otras cosas, era relativamente fácil de usar (en comparación con otras máquinas de la época), incluía sonido y gráficos a color en alta resolución. Y, además, era bonito. Esto se convirtió en una seña de identidad de la marca hasta la actualidad. Sin embargo, el ordenador que supuso una verdadera revolución fue el Macintosh 128k presentado en 1984) gracias a su GUI intuitiva y fácil de utilizar. Este no fue el primer ordenador con GUI presentado por Apple (podemos encontrar el Lisa en 1983, o el Apple IIC en 1984), sin embargo, fue el primero que cosecho un gran éxito comercial y que inicio la línea de productos de consumo masivo que se mantiene hasta la actualidad. 



Ilustración 12: Macintosh 128k [28] 

Otros dispositivos relevantes de esta generación de computadores y que merecen ser mencionadas en una descripción de la cuarta generación de computadores son las siguientes: 

- Kenbak-1: Diseñado por John V. Blankebaker fue diseñado en 1970 y se comercializo a principios de año siguiente. Este ordenador es considerado por el Computer History Museum [30] como el primer ordenador personal de la historia, aunque este titulo es difícil de establecer dado a la carrera tecnológica que se vivió en esa época. Este ordenador se encuentra en el límite entre la tercera y la cuarta generación dado que esta considerado como un ordenador personal, pero este no incluía un microprocesador. Este ordenador contaba con limitaciones importantes y fue ensombrecido por la aparición de el PC de IBM y el Apple Computer. 

17 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- TRS-80: El TRS-80 fue el primer ordenador de Tandy Corporation [31], que se vendió a través de la cadena de tiendas Radio Shack. Salió al mercado en agosto del 77 y en octubre ya se habían vendido más de 10.000 unidades a 599 dólares cada una. 

- PET y VIC-20: El Personal Electronic Transactor fue el primer ordenador presentado por la compañía estadounidense Commodore International [32] en 1977, el cual fue sucedido por el VIC-20 en junio del 80. Este ordenador destaco por ser el primer ordenador de uso domestico de un precio inferior a 300 dólares lo cual aumento su accesibilidad a los hogares. Este ordenador no destacaba en características con sus coetáneos, sin embargo su sucesor el Commodore 64 tuvo tal éxito que ostenta el título del ordenador personal mas vendido de todos los tiempos de acuerdo al Computer History Museum. 

### **1.5. La quinta generación (1980-1990 a la actualidad): La era de la IA** 

La línea divisoria entre las generaciones de computadoras pasa a hacerse mas difusa debido a que la tecnología que se esta desarrollando se basa en descubrimientos modernos. En este caso la línea divisoria entre la cuarta generación y la quinta no se basa en la aparición de una tecnología revolucionaria si no que esta última generación se nutre de las invenciones que han tenido lugar en las generaciones anteriores que han sido evolucionadas. La quinta generación de computadoras esta asociada a las tecnologías de inteligencia artificial, nanotecnología, procesamiento paralelo y computación cuántica. Además, en esta generación cabe destacar el papel del software empleado, componente con menor relevancia en generaciones anteriores. 

El principal objetivo de las computadoras de la quinta generación pasa por la aplicación de inteligencia artificial y computación cuántica. Para ello es necesario aunar las mejoras de hardware disponibles con un software que permita a los computadores tomas sus propias decisiones. La integración de múltiples procesadores trabajando en paralelo, nuevos sensores disponibles y mejoras en la capacidad de memoria unidos al desarrollo de nuevos lenguajes de programación y aplicaciones logran que estas computadoras alcancen altos estándares de operación. 

Los principales avances de hardware de los computadores de la quinta generación se centran en la tecnología VLSI y ULSI. Estas tecnologías permiten el desarrollo de microchips de circuitos integrados. Estos chips de electrónica digital basados en el uso de puertas lógicas permiten integrar de forma simultánea en un mismo dispositivo una serie de puertas lógicas que permiten realizar funciones determinadas. En la actualidad podemos encontrar cientos de miles de puertas lógicas integradas en un chip de milímetros de tamaño. La capacidad de integrar transistores dentro de un microchip se conoce como ‘Escala de Integración’ [33] y nos permite clasificar los microchips en función de la densidad de componentes que contienen y las puertas lógicas que son capaces de soportar: 

18 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- SSI (Small Scale Integration) Integración a pequeña escala: Es la escalad e integración mas pequeña de toas y comprende todos los circuitos integrados de menos de 12 puertas lógicas. Contienen entre 10 y 100 transistores por chip 

- MSI (Medium Scale Integration) Integración a media escala: Esta escala comprende todos los chips cuyo número de puertas oscila entre 12 y 100. Estos integradores se utilizaban en los primeros ordenadores personales que surgieron durante la cuarta generación. Contienen entre 100 y 1000 transistores por chip. 

- LSI (Large Scale Integration) Integración a gran escala: A esta escala pertenecen todos aquellos chips que contienen mas de 100 puertas lógicas hasta 1000 puertas. Estos circuitos permiten realizar funciones completas, como por ejemplo el procesado de una calculadora y son considerados como microprocesadores. Contienen entre 1000 y 10000 componentes por chip. 

- VLSI (Very Large Scale Integration) Integración a muy gran escala: Esta tecnología permite desarrollar y fabricar circuitos integrados que contengan entre 10.000 y 100.000 transistores, lo que equivale aproximadamente a entre 1000 y 10000 puertas lógicas. Estos circuitos consolidan la industria de los circuitos integrados y desplazan la tecnología de los componentes aislados. Este tipo de integración a muy gran escala es la tecnología utilizada por los principales productores de microchips. En la actualidad algunas de las compañias que producen este tipo de circuitos integrados son Intel, Texas Instruments, Samsung, AMD, NVIDIA, Toshiba, Qualcom o Microm. 

- ULSI (ultra large scale integration) integración a ultra gran escala: Tecnología de circutos integrados que emplea entre 10000 y un millón de transistores por circuito integrado que permite contener entre 10000 y 100000 puertas lógicas. Este tipo de tecnología se emplea en la actualidad para fabricar microprocesadores complejos 

- GLSI (giga large scale integration) integración a giga gran escala: Tecnología de circuitos integrados que utiliza más de un millón de transistores por circuitos integrado y más de 100.000 puertas lógicas. 

En la actualidad se utilizan para la fabricación de chips de computadora las tecnologías VLSI y ULSI. 

La relación entre los transistores que pueden ser contenidos en un microprocesador fue recogida por Gordon E. Moore, cofundador de Intel en abril de 1965 por medio de la teoría conocida como Ley de Moore. Esta teoría establece aproximadamente cada dos años se duplica el número de transistores en un microprocesador. Originalmente Moore estableció que esta relación se duplicaría año a año, sin embargo en 1975 modificó su propia ley al corroborar que este ritmo bajaría y estableció que la capacidad de integración no se duplicaría cada año si no cada dos. Desde la formulación de la ley esta se ha cumplido hasta la década de los dosmil, sin embargo, el propio Moore aseguró en una conferencia en 2007 que su ley dejaría de cumplirse en 10 o 15 años. 

19 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 13: Ley de Moore comparada con datos históricos [34] 

En la actualidad la ley de Moore esta llegando a su fin ya que el escalado de los procesadores se realiza de manera diferente y con otras normas. El estancamiento de la Ley de Moore es una consecuencia del límite físico de la tecnología actual. Al aumentar la densidad de transistores aumenta el calor generado para un mismo volumen. Por lo tanto, no es posible extraer el calor suficientemente rápido sin riesgo a sobrecalentar y dañar el microprocesador. Además, normalmente los transistores se hacen cada vez más pequeños para aumentar la cantidad de éstos en los chips, sin cambiar el tamaño de estos últimos, lo cual tiene un límite físico impuesto por el tamaño de los átomos. 

Unido a las mejoras disponibles en circuitos integrados algunas de las características destacables de esta quinta generación son: 

- Adaptación del entorno para el desarrollo de inteligencia artificial: Para lograr entrenar y desplegar modelos de inteligencia artificial requerimos de un gran poder computacional. Esta quinta generación de computadores incluye coprocesadores dentro de su arquitectura especialmente diseñados para llevar a cabo estas tareas. 

- Avance en el procesamiento paralelo: El uso de la tecnología del procesamiento paralelo, los circuitos unidos mediante fibra óptica y de los materiales superconductores está ayudando a hacer realidad la inteligencia artificial. 

- Desarrollo del procesamiento del lenguaje natural: La interrelación con los computadores hasta el momento se ha realizado mediante lenguajes máquina o lenguajes de programación. En esta última generación se incluye la integración del procesamiento del lenguaje natural a través de software especializado como método de comunicación con los computadores. 

20 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

La quinta generación de computadores comenzó a desarrollarse en la década de los 80. Oficialmente comenzó como un proyecto llevado a cabo en Japón en 1981 el FGCS (Fifth Generation Computer Systems) que tenía como objetivo el desarrollo de una nueva clase de computadores que emplearían las tecnologías de inteligencia artificial tanto en el plano del hardware como en el software usando el lenguaje PROLOG a nivel de lenguaje máquina y serían capaces de resolver problemas complejos como la traducción automática de una lengua natural a otra. En este anuncio se indicaba que sus más importantes compañías de tecnología se unirían para darle forma a una quinta generación de computadoras. Estas deberían ser capaces de interrelacionarse con sus usuarios en lenguaje natural, y además deberían reconocer imágenes, entre otras características que le permitieran ser más independientes. 

Si bien en parte el proyecto fue un fracaso, toda la tecnología desarrollada en aquellos primeros pasos se puede ver en la actualidad en diversas formas. Ejemplos de ello son los diversos asistentes de voz como Siri, Cortana y Google Assistant. Otro importante avance que nos deja la quinta generación de computadoras es la capacidad de algunos dispositivos de interactuar con su entorno. Esto permitió que se desarrollaran conceptos como el de Internet de las cosas. 

Algunas de las computadoras más relevantes que dieron el pistoletazo de salida a esta quinta generación son las siguientes: 

- CRAY-1 [36]: El considerado como el primer supercomputador del mundo fue considerado como el más rápido desde 1976 hasta 1982. Diseñado por Seymour Cray [35], un apasionado de arte de diseñar PCs que fundó Cray Research en 1972, reescribió la tecnología de computación desde el procesamiento hasta la refrigeración y el embalaje. Este supercomputador medía 26 metros de ancho y 20 pies de alto, y contenía 90 kilómetros de cables. obtuvo un rendimiento excepcional de 160 megaflops en un tamaño reducido y su forma cilíndrica, una memoria de semiconductor con capacidad de 1 millón de palabras, un tamaño de palabra de 64 bits, un compilador Fortran optimizado y una técnica llamada «encadenamiento». La misión de Cray Research en sus inicios fue construir los ordenadores más rápidos del sector y liderar la computación científica a gran escala. Pero cuando la empresa observó lo que la gente podía hacer con esos sistemas, la misión dio un giro. El concepto de velocidad se amplió incorporando el compromiso de ayudar a resolver los problemas científicos e industriales. A partir de este primer modelo se desarrollaron múltiples supercomputadores siguendo la línea de Cray, hoy en dia orientados al aprovechamiento del big data. En 2019 Cray Research fue adquirido por HPE en su apuesta por el supercomputing. 

21 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 14: Cray-1 [36] 

- Osborne 1 [37]: Primera microcomputadora de tipo portátil que aparece en el año 1981 en la Feria de Computación de la Costa Oeste para ponerse a la venta, aunque sin demasiado éxito, dos años después. Con 13 kg, un SO CP/M, teclado separable y una pantalla ínfima, peca de inspirarse demasiado en el Xerox PARC, del 1976. Incluía dos puertos, el IEEE-488 y el todavía utilizable RS-232. Esta computadora es considerada como la primera computadora portátil, sin embargo, tenia muchas deficiencias. A esta le siguió un equipo de Epson, el Espson HX-20, mucho mas eficaz 

- NCR System 3125: Anunciado justo antes de la PC Expo de 1991 en la ciudad de Nueva York, el NCR System 3125 es uno de los primeros y muy costosos sistemas de computadora portátil basados en lápiz, que podría ejecutar múltiples sistemas operativos diferentes, incluido Microsoft MS-DOS 5.0 (con NCR PenOS) , Windows para Pen Computing, sistema operativo GO PenPoint y GRiD PenRight. Incluye multitud de funciones y su acceso requiere de escritura manual. Se trata del antecesor de las tabletas y smartphones táctiles. 

- Compaq Portable SLT/286 1903 [38]: Muy rimbombante por incluir una pantalla significativamente más grande que permitía trabajar con una mucha mayor comodidad. Su chip gráfico fue superior, mostrando 9x14 caracteres e incluía una BIOS Compaq, diseñada por ingeniería inversa y el famosísimo procesador Intel 8088. 

Estos computadores sirvieron de predecesores a los ordenadores que conocemos hoy en dia, sin embargo durante esta generación se realizaron grandes cambios debido a la aparición de tecnología como las memorias DIMM de 108 pines , las placas de video AGP, el perfeccionamiento de los buses de comunicación, pero principalmente y de una forma muy diferencial la aparición en el mercado de los procesadores Intel Pentium, , el primero de ellos, el Pentium I en el año 1997, el Pentium II en 1999 y finalmente el Pentium IV, en el año 2001. 

22 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Hoy en día sólo han quedado dos combatientes en el terreno de los procesadores para computadoras, Intel y AMD. Entre ambos fabricantes cubren casi la totalidad de las necesidades de proceso de cómputo en ámbitos como el hogar, la oficina y la industria, y han puesto en el mercado CPUs con velocidades y rendimientos imposibles de imaginar tan sólo una década atrás. 

Entre los más destacados productos de estas firmas podemos mencionar los procesadores Intel Core, en sus variantes i3, i5 e i7 de dos o cuatro núcleos y velocidades de reloj que superan ampliamente los 3.4 Ghz. En cuanto a AMD, su modelo Fusion es uno de los diseños más avanzados, ya que logra combinar en la misma cápsula de la CPU al chip gráfico. Otro acierto de la firma es el Phenom II, el cual puede llegar a montar en su interior hasta 6 núcleos corriendo a 3.6 Ghz [39]. 

Otro de los grandes hitos de esta generación y del que aún estamos empezando a entrever su potencial, es la aparición de la computación cuántica [40]. La mecánica cuántica comenzó a desarrollarse a principios del siglo XX de la mano de científicos como Max Plank, Albert Einstein o Niels Bohr. Fue en 1925 cuando Edwin Schrödinger presento ecuación de onda en la que se describe la evolución temporal de una partícula subatómica. Esta ecuación es el eje central sobre el que después se desarrolló la teoría de la mecánica cuántica. Esta ecuación dio lugar a la teoría del Gato de Schrödinger, en la cual se presenta la paradoja de un gato que se encuentra en un estado de superposición entre la vida y la muerte que solo es rota mediante la intervención de un observador. 

Esta es una de las paradojas más famosas de la computación cuánticas, puedes leer una explicación accesible a esta teoría en el siguiente artículo: <u>https://computerhoy.com/noticias/tecnologia/gato-shrodinger-paradoja-736517</u> 

La primera persona en proponer la idea de una computadora cuántica fue Paul Benioff en 1981. Más tarde Richard Feynman, entre 1981 y 1982 planteó que, una computadora cuántica que se basase en las leyes de la mecánica cuántica, podría hacer cálculos complejos de forma muy rápida [41]. 

Durante los años 90 aparecieron los primeros algoritmos cuánticos y con ellos las primeras aplicaciones y máquinas capaces de realizar cálculos cuánticos. 

Desde 2016 se puede usar un simulador gratuito de computador cuántico de IBM en la nube, IBM Quantum Experience [42], de modo que cualquier persona con conexión a internet puede diseñar y ejecutar sus propios circuitos cuánticos. 

En 2019 IBM presenta al mundo la primera computadora cuántica comercial, llamada IBM Q System One, con un sistema de 20 qubits que puede emplearse tanto en el ámbito científico como en el empresarial. Este, es considerado como uno de los saltos más importantes en la historia de la computación. 

23 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 15: Q System one 

Finalmente, el 23 de octubre de ese mismo año, la revista Nature publicó que Google había alcanzado de forma oficial la “supremacía cuántica” [43], es decir, que había logrado construir un dispositivo de computación cuántica que podía dar solución a problemas que la computación clásica no podía. 

En la actualidad hay múltiples empresas trabajando por liderar la revolución de la computación cuántica. IBM, Google, Intel y Honeywell son las empresas estadounidenses que ya tienen ordenadores cuánticos funcionales con una capacidad interesante como entorno de pruebas e investigación. Sin embargo, Estados Unidos no es el único país que esta liderando el desarrollo de la computación cuántica, su inmediato perseguidor se trata de China. En junio de 2020 consiguió transmitir un mensaje cifrado [44] que no podía ser comprometido entre dos estaciones terrestres separadas por una distancia de 1120 km utilizando el entrelazamiento cuántico. 

A estas dos principales potencias se les han sumado en esfuerzos de desarrollo mas recientemente países como Francia, Alemania, Australia, India o Japón, que están invirtiendo fuertes sumas de dinero en el desarrollo de esta tecnología. 

Esta tecnología se prevé que traiga consigo importantes avances en áreas como la criptografía, el aprendizaje automático, el procesamiento de datos y problemas de optimización. 

Junto a la computación cuántica existen otras tecnologías en vías de desarrollo como los materiales superconductores o la nanotecnología. Algunas de las teorías ya plantean la posibilidad de estar entrando en la sexta generación de computadoras y especulan sobre la séptima y la octava. 

24 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

### **1.6. Sexta Generación de computadoras: Redes neuronales artificiales** 

Basándonos en las tendencias de desarrollo de hardware y software actuales una de las características que definirán a la sexta generación serán las computadoras inteligentes basadas en redes neuronales artificiales. Estas supercomputadoras estarán basadas en el uso de materiales semiconductores. El uso de estos materiales permite la utilización de toda la energía en el proceso de cálculo sin necesidad de disipar parte de ella como calor. Esto permitirá obtener un importante incremento de potencia respecto a los chips actuales de silicio. 

### **1.7. Séptima Generación de computadoras: Paralelización de cargas** 

El modelo de procesamiento paralelo ya esta siendo explotado en la actualidad, sin embargo, se prevé una explosión de esta tecnología en futuras generaciones de la mano del uso masivo de redes. Actualmente podemos encontrar ejemplos de este tipo de computación a través de la computación distribuida, en la cual múltiples computadoras y procesadores trabajan de manera simultanea en el mismo problema. En la actualidad este tipo de computación tiene la limitación física del traspaso de datos entre las distintas computadoras que trabajan en paralelo, con el desarrollo masivo de redes en el área mundial, podremos acceder a todo tipo de servicios en línea de forma instantánea y en tiempo real. 

### **1.8. Octava Generación de computadoras: Nanotecnología** 

La octava generación de computadores se basa en teorías y especulaciones más que en tecnología tangible que podamos encontrar en su fase de desarrollo. Esta generación se caracterizaría por la ausencia de medios físicos convencionales a los que estamos acostumbrados como periféricos de ordenador (pantalla, ratón, teclado…) y en su lugar utilizaríamos implantes de nanotecnología que nos permitan comunicarnos con servicios alojados en la nube. Aunque la tecnología nanométrica ya ha comenzado a desarrollarse, aun no tenemos ejemplos viables de su aplicación en esta área 

Esta tecnología no solo crearía un nuevo paradigma en el área de la computación si no que tendrían aplicaciones directas en otras áreas como la medicina, la interacción entre humanos y computadores y las comunicaciones. 

25 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

## **2. Co-procesadores** 

_“Para poder entender los co-procesadores y su importancia a la hora de desarrollar distintos modelos computacionales es necesario com-_ _<u>prender la arquitectura general de un computador.”</u>_ 

Los coprocesadores son elementos de una computadora que nos permite complementar las funciones del procesador principal o CPU. Estos pueden realizar distintas funciones desde aritmética de punto flotante, gráficos, procesamiento de señales. El objetivo de estos sistemas es mejorar el rendimiento global del sistema y dar respuesta a necesidades de cómputo específicas para las que la CPU no esta optimizada. 

Para poder entender los co-procesadores y su importancia a la hora de desarrollar distintos modelos computacionales es necesario comprender la arquitectura general de un computador. 

### **2.1. Arquitectura de un computador** 

Dentro de la arquitectura de un computador diferenciamos dos componentes principales, el hardware que corresponde con la parte física o tangible del computador y el software, que corresponde con el conjunto de instrucciones que nos permiten operar con el computador. 

### **2.1.1. Hardware de un computador** 

En el hardware de un computador podemos encontrar dos grandes grupos de componentes electrónicos, internos y periféricos. Los componentes internos son aquellos que forman parte de la unidad funcional del computador. En el caso de tratarse de un ordenador personal, estaríamos hablando de la caja del ordenador, mientras que los periféricos son la mayoría de los dispositivos de entrada y de salida que se consideran componentes de hardware externos “no esenciales” porque la computadora puede funcionar sin ellos. Por ejemplo, altavoces, cámara web, teclado, micrófono, impresora, escáner, ratón… 

**Los componentes internos básicos de todo computador serían: placa base, CPU, memoria RAM, disco duro, fuente de alimentación y tarjetas de red.** Estos componentes nos permiten llevar a cabo las distintas operaciones que queramos realizar con nuestro computador, sin embargo, también debemos considerar como componentes primarios los elementos que nos permiten disipar el calor que generan todos estos componentes electrónicos. En este caso los principales componentes que encontramos son disipadores de calor, ventiladores y /o refrigeración líquida. 

26 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

#### **Placa base** 

La placa base es una placa de circuito impreso o PCB en la que encontramos un circuito integrado que interconecta una serie de chips condensadores y conectores. La arquitectura interna de la placa base es muy compleja a nivel electrónico sin embargo a la hora de entender la arquitectura de un ordenador los factores debemos tener en cuenta son: 

- El socket: Elemento de la placa base donde se instala el procesador del ordenador. No todas las placas base son compatibles con todos los procesadores disponibles en el mercado si no que cada fabricante de procesador tendrá su propia placa base. 

- Chipset: Es el conjunto de circuitos integrados que hacen de puente entre los dispositivos de entrada y salida y el procesador. En modelos mas antiguos podemos encontrar dos tipos de chipsets, el puente norte que se encarga de conectar la CPU con la memoria y las ranuras PCI y el puente sur que conectaba la CPU con los dispositivos de entrada salida. En las placas base mas modernas únicamente encontramos un tipo de chipset, el puente sur ya que las funcionalidades del puente norte se han integrado dentro del chip del procesador. Las especificaciones del chipset atienden al número de LANES PCI que tenga, es decir las líneas de conexión que existen entre la CPU y el resto de los componentes de la máquina. Cuanto mayor sea este número mayor será la cantidad de datos simultáneos que se pueden transportar hacia la CPU. 



Ilustración 16: Ejemplo placa base 

Dentro de las placas base podemos encontrar algunas funcionalidades integradas que antes solo podíamos encontrar por medio de tarjetas de expansión. 

- BIOS: La BIOS o Basic Input-Output System es una memoria de tipo Flash que almacena un pequeño programa con información sobre la configuración de la placa base y los dispositivos en ella conectados, así como los dispositivos conectados a ella. Actualmente las BIOS reciben el nombre de UEFI o EFI (Extensible Firmware Interface) la cual es básicamente una actualización mucho más avanzada de la BIOS, con interfaz gráfica de alto nivel, mayor seguridad, y con un control mucho más avanzado de los componentes conectados a la placa base. 

27 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- Ranuras de expansión: son la clave de las placas bases, en ellas podremos instalar las memorias RAM, tarjetas gráficas, Discos duros y otros puertos o conexiones de nuestro ordenador. 

- Tarjetas de red y sonido: Las placas base actuales cuentan con tarjetas de red y sonido integradas dentro de la placa base. Estas tarjetas se encargan de procesar el sonido del ordenador y conexiones LAN respectivamente. 

#### **CPU o microprocesador** 

La CPU o Central Processing Unit por sus siglas en inglés es el componente central de todo computador. Este se encarga de procesar todas las instrucciones del dispositivo, leyendo las órdenes del sistema operativo y las instrucciones del resto de componentes del computador. 



Ilustración 17: Microprocesador Intel i7 [49] 

Tu ordenador o portátil tendrán una CPU dedicada para realizar todas las operaciones y procesos que requiera el sistema. Mientras, los móviles tienen el denominado SoC o System on Chip, que es un chip que contiene tanto la CPU como otros componentes, como chips gráficos integrados. Con ello, los SoC suelen poder hacer más que las funciones de las CPU estándar. 

Los procesadores actuales están fabricados con circuitos integrados, aunque existen procesadores multinúcleo en los que podemos encontrar varias CPUs en un solo circuito integrado. 

Dentro de una CPU encontramos los siguientes componentes: 

- ALU: Por sus siglas en ingles Aritmetic Logical Unit es la Unidad Aritmético lógica que se encarga de realizar las operaciones aritméticas (sumas y restas) y las operaciones lógicas (SI, Y, O, NO). Además de los operadores lógicos y aritméticos, la ALU cuenta con una serie de registros para almacenar los datos, y bits de información sobre los resultados, también llamados banderas. Dentro de cada núcleo de un microprocesador podemos encontrar múltiples ALUs. Este tipo de circuitos se limita a realizar operaciones, es decir requiere de un mecanismo de control que le permita saber que tipo de operación debe realizar. 

28 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 18: Diagrama de ALU donde A y B son operandos, R es la salida, F la entrada de la unidad de control y de el estado de la salida [45] 

- Unidad de control (CU): Se encarga de buscar las instrucciones en la memoria principal, decodificarlas y conectarlas con la ALU para su ejecución 

- Registros internos: registro es una memoria de alta velocidad y poca capacidad, integrada en el microprocesador, que permite guardar transitoriamente y acceder a valores muy usados, generalmente en operaciones matemáticas. 

- Bus de entrada y salida: es el sistema encargado de transferir los datos a través de todos los componentes del CPU. 

Las operaciones que llevan a cabo las CPUs consisten en ejecutar una serie de instrucciones provenientes de los programas. La mayor parte de las computadoras utilizan la arquitectura de von Neumann [46]. En esta arquitectura las CPUs contienen una unidad aritmético lógica, registros del procesador, una unidad de control que contiene un registro de instrucciones y un contador de programa, una memoria para almacenar tanto datos como instrucciones, almacenamiento masivo externo y mecanismos de entrada/salida. 



Ilustración 19: Arquitectura von Neumann [47] 

29 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Los computadores que utilizan este tipo de arquitectura en su CPU generalmente utilizan cuatro pasos en su modo de operación: 

- Fetch o búsqueda: Es el primer paso de una operación y consiste en recuperar una instrucción de la memoria RAM con los datos requeridos para ejecutar la operación. 

- Decode o decodificación:  la instrucción es dividida en partes que tienen significado para otras unidades de la CPU, los datos son analizados para entender de que trata la instrucción. 

- Execute o ejecución: Una vez se han llevado a cabo los pasos de lectura y decodificación la información es procesada conectando las distintas unidades de la CPU. Por ejemplo si requerimos realizar una instrucción de adicción, se proporcionará a una unidad ALU a través de las unidades de entrada y salida los números a ser sumados. 

- Writeback o escritura: Es el paso final a través del cual la CPU ‘escribe’ el resultado obtenido. En este proceso la información toma el mismo camino que en el proceso de búsqueda pero de manera inversa. Los datos son escritos en la memoria del sistema. 



Ilustración 20: Diagrama de bloques de una CPU simple [48] 

30 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Independientemente del tipo de CPU que utilicemos todas tienen una serie de características en común que determinan su rendimiento y funcionalidad: 

- Numero de hilos de procesador: Los hilos del procesador son las instrucciones de programa que se encargan de ejecutar varios procesos de forma simultanea. Son frecuentemente confundidos con los núcleos de los procesadores, ya que estos también permiten paralelizar procesos, sin embargo, estos últimos se tratan de componentes físicos de un procesador mientras que los hilos funcionan a través de instrucciones de software. Lo mas común es encontrarnos dos hilos por núcleo de procesador en procesadores de tipo x86 aunque en el mercado podemos encontrar otros tipos de procesadores que permiten ejecutar hasta 8 hilos de procesador en simultaneo. Este tipo de procesadores están orientados a computación de alto rendimiento y los podemos encontrar en servidores distribuidos de tipo empresarial. 

- Numero de núcleos del procesador: Cuanto mayor es la cantidad de nucleos que incluimos dentro de un procesador mas tareas va a poder ejecutar la CPU y la velocidad a la que lo va a hacer. 

- Frecuencia del procesador: Es una medida de la potencia del procesador, que marca la cantidida de operaciones que un microprocesador será capaz de realizar, cuanto mas alta es la frecuencia mayor cantidad será capaz de realizar. Podemos medirla eh MHz o GHz. Podemos encontrar dos tipos de frecuencia de procesador 

   - Frecuencia base: Corresponde con la potencia mínima que requiere la CPU para ejecutar tareas básicas como el encendido / apagado, ejecución de sistema operativo… 

   - Frecuencia turbo: Potencia utilizada para ejecutar procesos complejos como procesado de datos 

- Ancho de bus: Las líneas de comunicación entre los dististintos elementos de la CPU se conocen como buses. Mientras mas ancho sea este bus mas grande serán las operaciones que podrá realizar un procesador. Los procesadores actuales de uso generalista son de 64 bits, es decir, pueden hacer operaciones con cadenas de 64 unos y ceros consecutivos. 

- Memoria Caché: mientras más memoria cache tenga el procesador, más cantidad de instrucciones podremos guardar en ellas para cogerlas rápidamente. La memoria caché es una memoria mucho más rápida que la memoria RAM y sirve para almacenar las instrucciones que van a ser inmediatamente utilizadas. 

- Consumo energético: El consumo de energía de la CPU se mide en vatios (W) y a mayor capacidad del CPU, mayor consumo de energía. 

31 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Otro factor importante que debemos de conocer a la hora de analizar una CPU es el fabricante de la misma y la arquitectura que esta utilizando. Actualmente el mercado de procesadores de PC esta ocupado prácticamente en su totalidad por dos fabricantes Intel y AMD. 

Intel por su parte fabrica con procesadores de tipo x86 con transistores de 14nm. Podemos identificar sus procesadores a través del nombre comercial que le han dado a cada una de sus generaciones: i3, i5, i7, i9. Actualmente es el principal fabricante del mercado y se prevé que próximamente saquen al mercado su nueva generación de procesadores por primera vez con una litografía de 10nm. 

AMD es su principal competidor y también fabrica procesadores con arquitectura x86. Estos procesadores tienen una litografía de 12nm y podemos localizarlos bajo el nombre comercial de Zen, en sus diferentes versiones. 

Además de los procesadores x86 podemos encontrar otras arquitecturas de procesador en el mercado generalista. Un ejemplo de estas nuevas arquitecturas es las desarrolladas por AMD para Apple, con el chip M1 incluido en los nuevos portátiles MacBook en los cuales redibujan el esquema de procesador tradicional. 

Mas allá de las arquitecturas generalistas podemos encontrar en el mercado otros tipos de arquitecturas abiertas como la arquitectura RISC-V frecuentemente utilizada en ámbitos universitarios o la arquitectura OpenPower que se encuentra bajo el paraguas de la Linux Foundation y proporciona una arquitectura de procesador libre y abierta. 

#### **Memoria RAM** 

La memoria RAM (Random Access Memory) es un componente interno que se instala en la placa base y sirve para cargar y almacenar todas las instrucciones que se ejecutan en el procesador. Estas instrucciones son enviadas desde todos los dispositivos conectados a la placa base y a los puertos de nuestro equipo. 

Esta memoria se conoce como memoria de acceso aleatorio porque la información se almacena de forma dinámica en las celdas sin un orden aparente, si no que va completando el espacio que se encuentra libre. La información que almacenamos en la memoria RAM es volátil ya que no queda grabada de manera permanente si no que es eliminada cada vez que apagamos el ordenador. 

32 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 21: Tarjeta de memoria RAM DIMM 

La memoria RAM esta conectada a la placa base y cuenta con buses de acceso directo desde la CPU, lo que permite que la transferencia de datos sea mucho mas rápida que desde los discos de almacenamiento. Los datos transferidos desde la memoria RAM a la CPU son almacenados en la memoria caché del procesador antes de su procesado. 

A la hora de configurar la memoria RAM de un equipo debemos tener en cuenta varias características de la misma: 

- Tipo de memoria RAM: Durante los últimos años las memorias utilizadas en los ordenadores portátiles han sido de tecnología DDR SDRAM (Double Data Rate Synchronous Dynamic-Access Memory). Esta tecnología comenzó en la generación DDR1 y en la actualidad se encuentra en la DDR4, la mas comun que podemos encontrar en ordenadores nuevos. Las actualizaciones de esta tecnología han pasado por amentar la frecuencia del bus de acceso, la capacidad de la memoria mientras se disminuye el voltaje necesario para su funcionamiento. 

- Cantidad de memoria: Los módulos de memoria RAM actuales van desde los 2GB hasta los 32GB. La cantidad total de memoria que podamos instalar en un computador dependerá de la cantidad de ranuras que incluya la placa base así como de la cantidad de memoria que sea capaz de direccionar el procesador. 

- Ranuras de instalación: Las ranuras de instalación de la placa base son los conectores donde se instala la memoria RAM. Actualmente existen dos tipos de ranuras: 

   - DIMM: Son las ranuras que podemos encontrar en las placas bases de los ordenadores de torre y en servidores. Se emplean con tarjetas de memoria DDR 1,2,3 y 4. El bus de conexión es de 64 bits y en memorias DDR4 puede tener hasta 288 conectores 

   - SO-DIMM: Estas ranuras son similares a las DIMM pero con un tamaño mas pequeño. Estos conectores se utilizan en ordenadores portátiles y equipos con espacio limitado 

33 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- Acceso simultáneo a la memoria: La memoria RAM puede trabajar en dos modos, dual channel y quad channel. Esta tecnología determina la cantidad de bloques de memoria a los que es capaz de acceder el procesador de manera simultanea. En un modo de dual channel el procesador accederá a dos bloques de 64 bits de manera simultánea, accediendo a 128 bits al mismo tiempo y en el modo quad channel accederá a 256 bits. 

#### **Disco Duro** 

El disco duro es el componente encargado de almacenar de manera permanente los datos del ordenador, así como el sistema operativo que nos permite trabajar con el. Existen múltiples tecnologías en el mercado de almacenamiento, aunque los mas comunes son: 

- Discos mecánicos o HDD: Estos discos utilizan el magnetismo para grabar sus datos, y se componen de uno o varios discos rígidos unidos por un eje que gira a gran velocidad. En cada plato y en cada una de sus caras un cabezal de lectura/escritura lee o graba los datos sobre los discos. Cuanto más finos sean los discos mejor será la grabación, y cuanto más rápido giran a mayor velocidad se transmiten los datos, tanto a la hora de leerlos como al escribirlos. Por lo general, la velocidad de los discos duros suele ser de 5400 o 7200 RPM (revoluciones por minuto), aunque en algunos discos pueden llegar a hasta 15.000 RPM. Estos últimos son utilizados en servidores. Estos discos son mas lentos y bastante mas económicos que los discos de estado sólido. 



Ilustración 22: Disco duro mecánico o HDD [51] 

34 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- Discos de estado sólido: La principal diferencia entre estos discos y los discos mecánicos es que en este caso los SSD no utilizan componentes mecánicos si no que almacenan los archivos en microchips con memorias flash interconectadas entre si. Estos discos normalmente utilizan memorias flash basadas en tecnología NAND[50], estas son un tipo de memoria no volátil que no requiere energía para almacenar datos por lo que la información se mantiene intacta cuando estos son desconectados. No tienen cabezales físicos para grabar los datos, en su lugar incluyen un procesador integrado para realizar operaciones relacionadas con la lectura y escritura de datos. La eficiencia de estos procesadores es lo que hace que estos discos sean significativamente mas rápidos que los discos rotacionales. Al mismo tiempo estos discos son mas caros que los discos rotacionales. 

Ambos tipos de disco están diseñados con el mismo tamaño para facilitar su integración con las ranuras de las placas base. 

#### **Fuente de alimentación** 

Uno de los componentes necesarios para el funcionamiento de un ordenador son las fuentes de alimentación. Estas fuentes se encargan de transformar la corriente alterna que llega a los enchufes en corriente continua. También se encarga de distribuir esta corriente entre todos los componentes electrónicos del ordenador. 



Ilustración 23: Fuente de alimentación [52] 

#### **Tarjetas de red** 

La tarjeta de red es el componente que va a permitir al computador conectarse con el mundo exterior a través de internet. Estas tarjetas en ordenadores portátiles pueden encontrarse integrada dentro de la placa base o encontrarse como tarjeta de expansión. Existen dos tipos de tarjetas de red: 

- Tarjetas de Ethernet: Cuentan con un conector RJ45 que nos permite conectarnos a una red LAN mediante un cable de ethernet. Actualmente en el mercado podemos encontrar velocidades entre 1GB/s y 10 Gb/s 

- WiFi: Generalmente integrado dentro de la placa base permite realizar conexiones inalámbricas a internet. 

35 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

#### **Disipadores y refrigeración** 

Dentro de los componentes necesarios de un ordenador debe estar incluido algún elemento que permita la gestión del calor generado por los distintos componentes electrónicos. Este componente no es estrictamente necesario ya que un ordenador puede funcionar sin ellos, pero con el uso prolongado los distintitos componentes físicos fallaran debido a las altas temperaturas. Algunos de los elementos que pueden utilizarse con este fin, de manera individual o combinados son los siguientes: 

- Disipadores: Estos elementos se encargan de recoger el calor que generan los componentes electrónicos y lo transmiten al ambiente. Entre sus componentes encontramos: un bloque metálico que esta en contacto directo con el procesador por medio de una pasta térmica, un bloque de aluminio también conocido como intercambiador formado por alteas de metal por las que pasa aire, unos ventiladores que fuerzan el flujo de aire a través de las aletas del bloque de aluminio. 



Ilustración 24: Disipador de calor [53] 

- Ventiladores de aire: Ventiladores internos que generan un flujo de aire que permite sacar parte del calor hacia el exterior del ordenador. 

- Refrigeración líquida: Este sistema de refrigeración se utiliza principalmente en sistemas de high perfomance computing o HPC. Estos sistemas están compuestos por una serie de servidores de sistema distribuido que generalmente trabajan procesando grandes volúmenes de datos de manera paralela. También podemos encontrar ejemplos de uso de refrigeración liquida en ordeandores personales diseñados para ejecutar programas que exigen un alto rendimiento de los componentes, como por ejemplo videojuegos. En la refrigeración líquida los elementos de disipación se dividen en dos grandes grupos. El primero se situará junto al procesador y estará compuesto por un bloque de cobre con pequeños tubos que contienen un liquido circulante accionado por una bomba. En segundo lugar, encontramos un intercambiador aleteado con ventiladores que se encarga de trasladar el calor recogido por el agua a el aire. 

36 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 25:Kit de refrigeración líquida[54] 

Estos son los componentes primarios de un ordenador necesarios para el correcto funcionamiento del mismo. Estos componentes son de propósito generalista con ellos podemos ejecutar distintas cargas de trabajo. Para optimizar la ejecución de algunas cargas de trabajo como puede ser el entrenamiento de modelos de inteligencia artificial, desarrollo de algoritmos de computación cuántica o analizar grandes volúmenes de datos podemos emplear una serie de co-procesadores. El objetivo de estos es complementar las funciones de la CPU de tal manera que permiten realizar tareas especificas para cada tipo de problema y acelerar el rendimiento global del sistema, puesto que descargan al procesador principal de tareas intensivas de computación [55]. 

Los aceleradores de propósito específico tienen una arquitectura similar a la de un procesador de propósito generalista con una unidad de control y una ALU sin embargo están diseñados para ejecutar un juego especifico de instrucciones de una manera mucho mas eficiente que una CPU convencional. Los coprocesadores se sustentan sobre tres pilares principales: 

1. Especialización: A la hora de diseñar los ALUs de las CPUs no es viable cablear todas las instrucciones posibles dentro del chip por falta de espacio, por ello en los procesadores de propósito generalista lo que se hace es ejecutar las instrucciones mas complejas a partir de la combinación de instrucciones mas simples. Esto conlleva un gasto de recursos en cuanto a tiempo y energía a la hora de realizar el proceso de captación-descodificación-ejecución. Las dos primeras etapas de captación y descodificación son las que mas energía consumen. En un coprocesador las instrucciones complejas están directamente integradas dentro del hardware de tal forma que en el acelerador se puede ejecutar de manera directa utilizando menos instrucciones que en un procesador de uso generalista. Esto reduce la cantidad de accesos necesarios a la memoria para la captación y decodificación de instrucciones, reduciendo el consumo energético y también la latencia entre la ejecución de instrucciones. 

37 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

2. Complejidad de los datos utilizados: Según el tipo de ALU que empleemos vamos a tener un consumo energético diferente. Para calcular una operación aritmética de suma con datos de 8 bits en un ALU de 32 bits necesitaremos la energía que consume un ALU de 32 bits. Sin embargo, esta operación puede realizarse en un ALU de 8 bits reduciendo de esta manera el consumo energético. Hay problemas que no requieren una alta precisión matemática y que pueden ser resueltos con ALUs más simples que consumen menos y ocupan menos espacio por lo que podríamos colocar una mayor cantidad. Hay que tener en cuenta que las ALUs de procesadores complejos como las CPUs han de ser anchas para poder ejecutar lo más rápidamente posible instrucciones con datos de alta precisión, pero esto es una contrapartida de cara a tareas que requieren trabajar con menor precisión acaban consumiendo mucho más de lo que deberían. 

3. Memoria: Los coprocesadores cuentan con su propia memoria RAM interna. El acelerador no tiene capacidad para acceder a la RAM del sistema y requiere que otra unidad busque los datos y se los proporcione a su RAM privada. Esto reduce el consumo energético ya que los datos recorren una distancia mucho menor entre el la RAM del acelerador y su ALU. 

Con la Ley de Moore llegando a su fin podemos ver que las arquitecturas seguidas hasta ahora consistentes en mejorar el rendimiento aumentando el número de núcleos o con arquitecturas mas complejas cada vez es menos viable por ello el desarrollo de aceleradores para tareas especificas esta cada vez mas en auge. 

Algunos de co-procesadores que podemos encontrar como elemento de apoyo al procesado de las CPUs son los siguientes 

### **2.2. Coprocesadores matemáticos** 

Los coprocesadores matemáticos o unidades de coma flotante son componentes especializados en el cálculo de operaciones aritméticas [56]. Las operaciones básicas que pueden llevar a cabo todos los coprocesadores matemáticos son la suma y la multiplicación, aunque algunos sistemas permiten la integración de operaciones mas avanzadas como cálculos trigonométricos o exponenciales. Este tipo de coprocesadores son frecuentemente sustituidos por programas de microcódigo que permiten emular una función de coma flotante a través de la unidad aritmético lógica (ALU) integrada dentro de la CPU. La representación de coma flotante es una notación científica empleada en computación que permite representar números muy grandes o pequeños de una manera eficiente. Integrar este tipo de coprocesadores dentro de la CPU permite reducir el coste del hardware al no requerir la integración de un coprocesador dedicado para este tipo de operaciones, pero conlleva una importante pérdida de velocidad a la hora de procesar estas operaciones. 

38 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Este tipo de coprocesadores eran bastante comunes en los desarrollos de chips llevados a cabo durante la década de los noventa, sin embargo, en la mayoría de los ordenadores domésticos disponibles actualmente integran esta funcionalidad dentro de la propia CPU. 

El primer coprocesador matemático que salió al mercado fue el Intel 8087. Fue anunciado en 1980 para la línea de procesadores de Intel 8086 y 8088 y permitía acelerar las funciones aritméticas básicas como sumas, restas, multiplicaciones y divisiones  pero también integraba funciones exponenciales y trigonométricas. Este tipo de coprocesadores permitían un aumento del rendimiento enorme respecto a las CPUs del momento ya que era capaz de realizar hasta 50000 FLOPS (floating point operations per second). A este le siguieron otros como el MMX, el SSE o el 3DNow que fueron integrado cada vez mas instrucciones para realizar este tipo de operaciones. En la actualidad este tipo de operaciones se encuentran integradas dentro de la CPU en las arquitecturas estandarizadas. 



Ilustración 26: Coprocesador Intel 8087 

### **2.3. Coprocesadores de Entrada / Salida** 

Los coprocesadores de entrada/salida surgieron en los computadores mainframe para encargarse de las operaciones de entrada/salida de la máquina, las cuales consumían una gran cantidad de tiempo y recursos. Con la integración de este nuevo dispositivo el mainframe no requería ningún tipo de procesamiento de entrada/salida si no que establecía una seria de parámetros para la operación y esta era llevada a cabo por los sistemas de canal. El hecho de dedicar estos coprocesadores relativamente simples para manejar el formato y procesamiento de E/S se mejoro el rendimiento general del sistema. 

Este tipo de coprocesadores se integraron en el desarrollo de servidores distribuidos y de ordenadores de uso personal. Algunos de los coprocesadores de entrada salida mas empleados son los siguientes: 

- Intel 8089: Es un procesador de entrada/salida diseñado para ser utilizado con los procesadores de Intel 8086 y 8088. Este coprocesador empleaba las mismas técnicas de programación que el coprocesador numérico 8087 pero aplicadas a operaciones de entrada /salida y transferencia de datos. Este procesador fue anunciado en 1979 sin embargo no tuvo un desarrollo mas allá de la generación de procesadores para la que fue diseñado. 

39 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- UART: Se trata de un coprocesador de entrada /salida que atiende a las siglas en ingles Universal Asynchonous Reciever-Transmitter y permite el control de los puertos y dispositivos en serie. Este dispositivo hardware es capaz de traducir datos con formato paralelo a formato serie permitiendo la comunicación entre sistemas electrónicos [57]. Actualmente este tipo de dispositivos se encuentran integrados en la placa base o en la tarjeta adaptadora del dispositivo. 

- DMA: El acceso directo a memoria o DMA por sus siglas en inglés direct memory Access, permite a ciertos componentes del sistema acceder a la memoria TAM para leer o escribir sin necesidad de la intervención de la CPU. Muchos sistemas hardware utilizan DMA, incluyendo controladores de unidades de disco, tarjetas gráficas y tarjetas de sonido. DMA es una característica esencial en todos los ordenadores modernos, ya que permite a dispositivos de diferentes velocidades comunicarse sin someter a la CPU a una carga masiva de interrupciones [58]. 

### **2.4. Coprocesadores Criptográficos** 

Los coprocesadores criptográficos son microprocesadores dedicados a realizar operaciones criptográficas incluyendo un paquete con múltiples medidas de seguridad física lo cual les aporta un alto grado de resistencia a la manipulación. El propósito de un criptoprocesador seguro es actuar como la piedra angular de un subsistema de seguridad, eliminando la necesidad de proteger el resto del subsistema con medidas de seguridad físicas [59]. Estos coprocesadores a diferencia de los vistos hasta ahora no tienen como objetivo reducir la carga de la CPU si no añadir funcionalidades con las que estos dispositivos no cuentan. Algunos ejemplos de coprocesadores criptográficos que podemos encontrar en la actualidad son los siguientes: 

- HSM son las siglas de Hardware Security Module (Módulo de Seguridad de Hardware). Estos son un dispositivo de hardware destinado al almacenamiento y protección de claves de tecnología PKI mediante criptografía. Las PKI o infraestructura de claves pública nos permite administrar certificados digitales y administrar el cifrado de estas claves públicas. Utilizando un procesador dedicado en exclusiva a este tipo de operaciones, es posible obtener un mejor rendimiento que con otros dispositivos con capacidades criptográficas cuyos procesadores, además, deben ser utilizados para otras funciones del sistema. Los HSM pueden encontrarse como dispositivos portátiles, dispositivos autocontenidos (appliances), tarjetas inteligentes (smartcards) o tarjetas criptográficas [60]. 

40 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- TPM son las siglas de Trusted Platform Module o módulo de plataforma de confianza. Este coprocesador se encuentra integrado dentro de la placa base y permite almacenar claves de cifrado. Una de sus características principales es que solo se comunica con el procesador de tu ordenador y ningún otro componente del equipo puede acceder a el. El chip TPM permite almacenar contraseñas de administrador, las de los sistemas DRM de protección de datos, o permitir el cifrado de unidades de almacenamiento o carpetas y archivos. También permite que los clientes con características de firma digital puedan enviar correos electrónicos de forma segura, o almacenar los datos biométricos de inicio de sesión. 

- Tarjeta inteligente (Smart card): Las tarjetas inteligentes modernas son probablemente la forma más extendida de criptoprocesador seguro. Estas son cualquier tarjeta de tamaño de bolsillo con circuitos integrados que permita la ejecución de cierta lógica programada 

### **2.5. Coprocesadores de procesamiento de señal** 

Los DSP (Digital Signal Processors) o procesadores digitales de señal son microprocesadores específicamente diseñados para el procesado digital de señal. Algunas de sus características más básicas como el formato aritmético, la velocidad, la organización de la memoria o la arquitectura interna hacen que sean o no adecuados para una aplicación en particular, así como otras que no hay que olvidar, como puedan ser el coste o la disponibilidad de una extensa gama de herramientas de desarrollo [61]. 

Este tipo de coprocesadores se caracterizan por utilizar arquitecturas especiales para acelerar los cálculos matemáticos necesarios para llevar a cabo el procesado de señales en tiempo real. La mayoría de los sistemas de audio, video y transmisión de datos digitales usados en la actualidad, requieren algoritmos de una elevada complejidad matemática. La solución que aportan los DSP es que pueden realizar operaciones matemáticas complejas en un solo ciclo de reloj por lo que el procesado (de señales de audio, de video, etc.) es el ideal, en contraposición a lo que aportan los microprocesadores convencionales [62] 

Una de las principales características de estos coprocesadores es su diseño preparado para operar de manera autónoma, es decir embebidos en sistemas como teléfonos móviles, cámaras digitales… 

La función principal de un DSP es el tratamiento digital de la señal a través de operaciones MAC (Multiply, Add, Accumulate). El proceso ejecutado por un DSP es el siguiente: 

- La entrada es una señal analógica, ya sea audio, video, cualquier señal recibida por cable, o por otro medio. 

- El DSP convierte la señal analógica a digital para su posterior procesado 

- Procesado matemático de la representación de la señal. 

41 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- Se vuelve a convertir la señal obtenida de digital a analógica. 

- Se da a la salida una señal analógica. 

De esta forma se obtiene un procesamiento en tiempo real de la representación matemática de la señal. 

### **2.6. Coprocesadores cuánticos** 

La computación cuántica es un nuevo paradigma de la computación en la cual se aplica a la informática las leyes de la física cuántica. Los procesadores cuánticos nos permiten resolver problemas que no pueden ser abordados desde la computación clásica. Estos se complementan con los computadores tradicionales, son formas diferentes de trabajar. Un computador cuántico no permite realizar las tareas cotidianas que pueden ser resueltas por un computador clásico. 

Entre las propiedades cuánticas se incluyen la superposición cuántica, el entrelazamiento cuántico, y el teletransporte cuántico: 

- La **superposición cuántica** describe cómo una partícula puede encontrarse en dos estados al mismo tiempo. Este modelo de superposición fue descrito por Paul Dirac en base al trabajo previo de Heisenberg y Schrödinger. 

- El **entrelazamiento cuántico** describe cómo dos partículas tan separadas como se desee pueden estar correlacionadas de forma que, lo que le sucede a una adeca de forma inmediata a la segunda. 

- El **teletransporte cuántico** utiliza el entrelazamiento cuántico para enviar información de un lugar a otro del espacio sin necesidad de viajar a través de él. 

La computación tradicional trabaja con un modelo binario de bits los cuales solo pueden tener un valor fijo de 0 o de 1. Estos se configuran mediante el voltaje físico aplicado sobre el transistor, si el voltaje es alto representará un uno mientras que si es bajo representará un cero. En la computación cuántica el valor son los ‘cúbits’ que pueden ser 1, 0 o 1 y 0 a la vez, superponerse y entrelazarse según las leyes físicas. Esto hace que los ‘cúbits’, a diferencia de los ‘bits’, puedan tomar varios valores a la vez y puedan desarrollar cálculos que no puede hacer un ordenador convencional. 

El efecto de superposición cuántica solo se mantiene hasta el instante en el que medimos el valor de un cúbit. Cuando llevamos a cabo esta operación la superposición colapsa y el cúbit adopta un único valor, que será 0 o 1. El problema es que dada la propia naturaleza de los sistemas cuánticos resulta muy difícil saber si se ha producido o no un error. 

42 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

En la actualidad, a diferencia de la informática clásica, no existe un lenguaje computacional cuántico como tal. Los investigadores trabajan en desarrollar algoritmos que puedan dar soluciones concretas a problemas planteados. 

Los procesadores cuánticos disponibles hasta el momento son sistemas con una arquitectura mas sencilla que la de un computador tradicional ya que no cuentan con memoria o procesador convencional, únicamente cuentan con un grupo de cúbits con los que se escribe la información y se opera sobre ellos, sin embargo, cuentan con una capacidad de cómputo muy potente. 

Si observamos un computador cuántico nos encontramos con una campana recubierta de cables de cobre y aislada en vacío en un cubículo de vidrio. Esto es debido a que estos sistemas son extremadamente sensibles, en el momento en el que un agente externo influye o interacciona con ellos afecta a la superposición cuántica. Las perturbaciones externas obligan al sistema a definirse hacia 1 o 0. Para evitar esto hay que aislar el sistema muy bien.  Estos computadores deben estar a una temperatura de -273º C, sin apenas presión atmosférica y asilados del campo magnético terrestre. Al mismo tiempo, la información no puede ser almacenada por lo que sus periodos de funcionamiento son muy cortos. 



Ilustración 27: Computador cuántico de Google [Hanna Benet /Google] 

43 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Actualmente los principales laboratorios y empresas tecnológicas como Google, Microsoft, Honeywell, AWS o IBM están inmersos en una carrera por el desarrollo de ordenadores cuánticos. 

Algunos de los computadores desarrollados hasta el momento son los siguientes 

### **2.6.1. Google** 

Google se encuentra centrado en el desarrollo de un computador cuántico con habilidad para corregir errores. La fecha estimada de lanzamiento de este sistema es 2029. Uno de los grandes hitos de computación cuántica logrados por Google fue el procesador Sycamore[63], que en 2019 fue capaz de realizar una operación en 200 segundos que en el superordenador clásico mas grande del mundo disponible en ese momento (Summit, desarrollado por IBM en el laboratorio de Oak Ridge [64]) habría tardado 10000 años. Este hito se considera como el alcance de la supremacía cuántica [65]. Google con todo un ecosistema de colaboración y educación alrededor de su tecnología cuántica disponible de manera gratuita. El simulador de computación cuántica de google se conoce como Cirq [66], y permite la implementación de algoritmos cuánticos a través de una biblioteca de software de Python para escribir, manipular y optimizar circuitos cuánticos y luego ejecutarlos en computadoras cuánticas y simuladores cuánticos. Este sistema es abierto y esta disponible para su uso: <u>https://quantumai.google/cirq</u> 

### **2.6.2. Microsoft** 

Microsoft también se posiciona como uno de los lideres en el desarrollo de la computación cuántica, sin embargo, en esta carrera esta tomando una dirección diferente al resto de sus competidores. Microsoft basa su tecnología en el desarrollo de cúbits estables que no requieran corrección de errores para funcionar. Para ello han logrado crear lo que se conoce como “modos cero de Majorama”, en los extremos de un nanocable, lo que permite crear una capa de protección para el cubit, aislandalo de las perturbaciones ambientales. Desde un punto de vista teórico las partículas de Majorana podrían estar involucradas en la fabricación de cúbits de más calidad que los utilizados en los ordenadores cuánticos actuales. 

Por su parte también cuenta con todo un ecosistema y un servicio en la nube que permite a los usuarios acercarse a su modelo de desarrollo de tecnología. Este ecosistema permite acceder a diversas soluciones, hardware y software cuántico de Microsoft y sus asociados. Con Azure Quantum y el kit de desarrollo de Quantum, los desarrolladores pueden explorar la programación cuántica y obtener más información sobre aplicaciones cuánticas, tales como búsqueda de datos, aprendizaje automático cuántico o soluciones de optimización. Este ecosistema es accesible desde los sevicios cloud de Azure: https:// <u>docs.microsoft.com/es-es/azure/quantum/overview-azure-quantum</u> 

44 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

### **2.6.3. Amazon Web Services** 

Amazon Web Services ha sido una de las últimas compañías en unirse a la carrera de la computación cuántica. Amazon lanzó el AWS Center for Quantum Computing en 2019 con el objetivo de acelerar el desarrollo de tecnologías y aplicaciones de computación cuántica. Ahora, la compañía está lanzando una nueva instalación para computación cuántica en el Instituto de Tecnología de California (Caltech) con el ambicioso objetivo de construir una computadora cuántica “tolerante a fallos”. Los equipos se centrarán en desarrollar hardware informático cuántico más potente e identificar nuevas aplicaciones para tecnologías cuánticas. 

Por otra parte, ya cuenta con su propio ecosistema abierto, el Amazon Braket. Este es un servicio de informática cuántica completamente administrado que se diseñó para ayudar a acelerar la investigación científica y el desarrollo de software para la informática cuántica. El objetivo que Amazon persigue con este entorno es investigar algoritmos de computación cuántica, permitir probar distintos hardware cuánticos y explorar el kit de desarrollo de software empleado por Amazon (SDK de Amazon Braket). Este ecosistema puede encontrarse a través de los servicios de AWS: <u>https://aws.amazon.com/es/braket/</u> 

### **2.6.4. IBM** 

IBM comenzó en el área del desarrollo de la computación cuántica desde los primeros ordenadores cuánticos de uso generalizado. El 16 de noviembre de 2021 anuncio el procesador cuántico Eagle [67] el cual cuenta con 127 qubits, rompiendo por primera vez la barrera de los 100 qbits. Otro importante hito desarrollado por la compañía es la puesta en mercado del primer computador cuántico de uso comercial con el IBM Q System One [68]. 

Por su parte IBM también cuenta con su ecosistema de desarrollo en el que podemos encontrar herramientas para desarrollar algoritmos de computación cuántica bajo el framework de Qiskit, un entorno de desarrollo basado en Python. 

Este entorno es accesible de manera gratuita a través del portal de IBM Quantum: <u>https:// quantum-computing.ibm.com</u> 

45 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 28: IBM Q System One 

### **2.6.5. USTC (University of Science and Technology from China)** 

En la carrera por liderar el desarrollo de la computación cuántica, China es otro de los líderes mundiales en presentar resultados corroborables en revistas científicas internacionales. En 2021 presentaron dos computadores cuánticos capaces de superar en rendimiento al Sycamore de Google, quien reclamo la supremacía cuántica en 2019. Su computador es capaz de detectar 113 fotones, lo que marca un paso importante para acelerar el desarrollo de esta nueva tecnología de la computación, al usar estas partículas de luz como portadores de información. A diferencia de los desarrolladores de occidente la tecnología utilizada no esta disponible para su desarrollo en un ecosistema abierto con el que podamos interactuar. 

El desarrollo de la computación cuántica no ha hecho mas que comenzar y en los próximos años veremos grandes avances en esta área, así como las primeras aplicaciones prácticas reales. Este tipo de computación va a tener sus principales aplicaciones en el procesamiento de grandes volúmenes de datos y la resolución de problemas complejos. La integración de la computación cuántica con el desarrollo de modelos de inteligencia artificial dará lugar a una nueva era computacional. 

### **2.7. Coprocesadores gráficos** 

Las GPUs o procesadores gráficos son el tipo de procesador más utilizado en la actualidad. Una gran parte de los ordenadores domésticos que se producen cuentan con este tipo de procesadores. 

Una unidad de procesamiento de gráficos (GPU) es un circuito electrónico especializado diseñado para manipular y alterar rápidamente la memoria para acelerar la creación de “imágenes” en un búfer de cuadros destinado a la salida a un dispositivo de visualización. Las GPU se utilizan en sistemas integrados, teléfonos móviles, computadoras personales, estaciones de trabajo y consolas de juegos. 

46 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 29: GPU en un ordenador convencional [69] 

El objetivo principal de este tipo de procesadores es liberar a la CPU de tareas de procesamiento gráfico repetitivas que pueden ser resueltas de una manera más eficiente mediante el procesamiento paralelo multinúcleo. Las GPUs actuales cuentan con varios núcleos que permiten el procesamiento paralelo. 

Si comparamos una CPU con una GPU obtenemos que ambos procesadores se tratan de microcontroladores programables. La principal diferencia entre ambos procesadores es la frecuencia y el ancho de banda al que trabajan. Las CPUs trabajan con una frecuencia media de 3.5Hz pero con un menor ancho de banda, mientras que las GPUs tiene una frecuencia alrededor de los 1500MHz y un mayor ancho de banda. 

Las GPU modernas son muy eficientes en la manipulación de gráficos de computadora y procesamiento de imágenes, y su estructura altamente paralela las hace más eficientes que las CPU de propósito general para algoritmos donde el procesamiento de grandes bloques de datos se realiza en paralelo. Esta capacidad de paralelizar el procesado de grandes volúmenes de datos las hace idóneas para llevar a cabo el entrenamiento de modelos de inteligencia artificial, especialmente aquellos basados en el procesado de imágenes y el Deep learning. 

Una forma sencilla de comprender la diferencia entre una GPU y una CPU es comparar la forma en que procesan las tareas. Una CPU tiene unos cuantos núcleos optimizados para el procesamiento en serie secuencial, mientras que una GPU cuenta con una arquitectura en paralelo enorme que consiste de mieles de núcleos más pequeños y eficaces, y que se diseñaron para resolver varias tareas al mismo tiempo [70]. 

47 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 30: Organización módulos operativos de CPU y GPU[71] 

Las CPUs tienen una menor densidad de unidades de cómputo y una lógica de control más compleja. En el mercado podemos encontrar distintas arquitecturas de CPU cuya densidad de núcleos oscila entre los 4 y los 12 (Intel y AMD) y hasta 15 en arquitecturas especializadas (IBM Power). Estos controladores trabajan con una velocidad de procesador más rápida optimizado para tareas secuenciales. 

Por su parte las GPUs tienen una densidad de unidades de cómputo mucho mayor capaces de realizar más operaciones de cálculo por cada acceso a memoria. En la actualidad podemos encontrar GPUs con una densidad de núcleos mayor a 512 (NVidia). Estos controladores tienen una velocidad de procesador más lenta optimizada para operaciones en paralelo. 

Cada uno de estos procesadores está indicado para resolver un tipo de tarea especifica y trabajar de forma conjunta. La computación acelerada de una GPU permite que se asignen tareas con una computación más intensiva y que las CPU se encarguen de llevar a cabo instrucciones más complejas. 

Las CPUs por su parte también permiten cierta paralelización de tareas, pero enfocada de manera diferente a las GPUs. Las CPUs están diseñadas para realizar un paralelismo a nivel de instrucción, es decir, ejecutar varias instrucciones de un programa de manera simultánea con el objetivo de reducir el tiempo total de ejecución del programa. 

Por su parte las GPUs están especializadas en el paralelismo a nivel de hilo, en esta arquitectura los núcleos toman varios programas al mismo tiempo y los ejecutan en paralelo. Por ello las GPUs se encargan de ejecutar instrucciones mas cortas y autocontenidas, es decir cuando un hilo llega a las ALUs del núcleo de la GPU contiene la instrucción y el dato de manera directa sin tener que pasar por cache o memoria. Cuando las GPUs se encuentran con instrucciones para las cuales deben buscar dato en memoria llevan a cabo un proceso conocido como Round-Robin que consiste en aplazar la ejecución de ese hilo. 

48 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Es por ello que cuando ejecutamos un programa de software el procesado del código es dirigido hacia el hardware óptimo en función de las necesidades computacionales de cada parte del mismo. El usuario final observa una mejora en los tiempos de ejecución de las aplicaciones sin necesitar visibilidad donde se está ejecutando cada subconjunto de instrucciones. 



Ilustración 31: Ejecución de programas de software 

En el siguiente video podemos ver un ejemplo bastante ilustrativo de las principales diferencias que presentan las CPUs y las GPUs a la hora de ejecutar un conjunto de instrucciones: 

<u>https://www.youtube.com/watch?v=-P28LKWTzrI</u> 



La base matemática de las redes neuronales y la manipulación de imágenes son tareas paralelas similares que involucran matrices, lo que lleva a que las GPU se utilicen cada vez más para tareas de aprendizaje automático. 

49 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

En las tarjetas gráficas también encontramos una arquitectura interna con distintos componentes que se encargar de realizar tareas específicas de una forma similar a las CPUs 

- Chipset: Núcleo de la tarjeta gráfica, en el encontramos los distintos núcleos de la misma con sus respectivos ALUs y la memoria caché asociada al chip, que normalmente tiene dos niveles L1 y L2. Dependiendo del fabricante los núcleos reciben distintas denominaciones: Nvidia denomina a sus núcleos CUDA o CUDA cores mientras que en tarjetas AMD se denominan Stream Processors o procesadores de flujo. Además Nvidia también desarrolla otros tipos de núcleos denominados Tensor Cores y RT Cores especializados en el procesado de instrucciones más complejas. 

- Memoria GRAM: Realiza prácticamente la misma función que la memoria RAM de un computador, este tipo de memoria se encarga de almacenar los dato a procesar por la GPU. Esta memoria es de tipo DDR al igual que las memorias RAM utilizando en la actualidad tecnología de tipo GDDR6, mientras que las RAM normales son DDR4. Estas memorias son mucho mas veloces alcanzando frecuencias de hasta 140000 MHz efectivos, además presentan un ancho de bus mucho mayor que en las memoria RAM convencionales. 

- VDR: Elemento encargado de suministrar enegía a todos los componentes de la tarjeta gráfica 

- Interfaz de conexión: Las tarjetas gráficas emplean una interfaz de conexión de tipo PCI express para conectarse a la placa base. En la actualidad estamos en un punto de transición entre el PCI-Express 3.0 y el 4.0, aunque en servidores especializados para este propósito podemos encontrar los primero conectores PCI-Express 5.0, aun no existen tarjetas en el mercado con esa tecnología. Este estándar ofrece compatibilidad entre las distintas generaciones 

50 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 33: Arquitectura GPU Nvidia 

Unida a la arquitectura de hardware de una GPU encontramos la arquitectura de software especializado que nos permite explotar los recursos físicos que ofrecen estos procesadores. Cada fabricante ofrece su propio sistema de drivers especialmente desarrollados para su arquitectura específica.  Una de las más destacadas dentro del mercado es la arquitectura CUDA (Compute Unified Device Architecture) desarrollada para las GPUs de Nvidia. 

Nvidia es una de las compañías líderes en el sector de computación, especialmente centrada en el área de HPC (High Performance Computation). La compañía invento las GPUs, sacando la priemera al mercado en el año 2006, actualmente ofrece soluciones para distintos sectores del mercado a través de sus distintas líneas de diseño especializado como los productos GeForce para diseño gráfico, NVIDIA Quadro especializados en la visualización de imágenes y el mercado de sistemas computacionales de alto rendimiento con sus productos Tesla y RT. 

51 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Las tarjetas gráficas fueron diseñadas originalmente para el procesado de imágenes sin embargo la comunidad científica aprovecho su enorme potencial para el desarrollo de aplicaciones de inteligencia artificial. La utilización de las tarjetas gráficas para el cálculo de propósito general (en inglés GPGPU - General-Purpose Computing on Graphics Processing Units) conllevaba el desarrollo de los programas simulando problemas gráficos ya que estos procesadores originalmente solo soportaban programación específica para procesados gráficos, utilizando programas como OpenGL o Cg. NVIDIA fue consciente del potencial que suponía acercar este enorme rendimiento a la comunidad científica en general y decidió investigar la forma de modificar la arquitectura de sus GPUs para que fueran completamente programables para aplicaciones científicas además de añadir soporte para lenguajes de alto nivel como C y C++. De este modo, en noviembre de 2009, NVIDIA introdujo para sus tarjetas gráficas la arquitectura CUDA, una nueva arquitectura para cálculo paralelo de propósito general, con un nuevo repertorio de instrucciones y un nuevo modelo de programación paralela, con soporte para lenguajes de alto nivel, y constituidas por cientos de núcleos que pueden procesar de manera concurrente miles de hilos de ejecución. En esta arquitectura, cada núcleo tiene ciertos recursos compartidos, incluyendo registros y memoria. La memoria compartida integrada en el propio chip permite que las tareas que se están ejecutando en estos núcleos compartan datos sin tener que enviarlos a través del bus de memoria del sistema [71]. 



Ilustración 34: Arquitectura CUDA diseñada para soportar varios lenguajes de programación 

En las arquitecturas clásicas de las GPUs podíamos encontrar dos tipos diferentes de procesadores, de vértices y de fragmentos, originalmente diseñados para realizar tareas diferenciadas en el procesamiento gráfico, con repertorio de instrucciones diferenciadas. En la arquitectura CUDA, a diferencia de arquitecturas previas, no se distingue entre diferentes tipos de procesadores si no que se presentan de manera unificada donde todos ellos requieren el mismo repertorio de instrucciones y recursos. 

52 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Este diseño permite la programación sencilla de los núcleos de la GPU, utilizando lenguaje de alto nivel como puede ser el lenguaje C. De este modo, el programador simplemente escribe un programa secuencial dentro del cual se llama a lo que se conoce como kernel, que puede ser una simple función o un programa completo. Este kernel se ejecuta de forma paralela dentro de la GPU como un conjunto de hilos (threads) y que el programador organiza dentro de una jerarquía en la que pueden agruparse en bloques (blocks), y que a su vez se pueden distribuir formando una malla (grid), tal como se muestra en la Figura 35. 

- Un thread de un bloque ejecuta una instancia de un kernel. Tiene su propio id dentro de su bloque, registros, memoria privada, entradas y salidas. 

- Un bloque es un conjunto de threads concurrentes que pueden cooperar entre ellos, sincronizarse y comparten memoria. Un bloque tiene su propio id dentro del grid. 

- Un grid es un arreglo de bloques de threads que ejecutan el mismo kernel, leen entradas desde memoria global, escriben resultados en memoria global, y se sincronizan entre otras llamadas a kernels. 

Cuando se invoca un kernel, el programador especifica el número de hilos por bloque y el número de bloques que conforman la malla. Una vez en la GPU, a cada hilo se le asigna un único número de identificación dentro de su bloque, y cada bloque recibe un identificador dentro de la malla. Esto permite que cada hilo decida sobre qué datos tiene que trabajar, lo que simplifica enormemente el direccionamiento de memoria cuando se trabaja con datos multidimensionales, como es el caso del procesado de imágenes o la resolución de ecuaciones diferenciales en dos y tres dimensiones. 



Ilustración 35: Jerarquia de hilos dentro de una GPU 

53 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Este nuevo paradigma de programación fue el que abrió la puerta a la utilización de las GPUs en el procesado de modelos de inteligencia artificial. Actualmente la utilización de GPUs a la hora de realizar un entrenamiento de un modelo supone una diferencia abismal de rendimiento, siendo en muchas ocasiones imprescindibles para poder realizarlo en un tiempo asequible. Además, debido al uso más eficiente de los recursos de hardware las GPUs resultan más eficientes energéticamente que las CPUs. Podemos encontrar un gráfico comparativo proporcionado por Nvidia  en la Figura 36 de las diferencias en tiempos de procesado /consumo energético al que podemos hacer frente comparando entrenamientos del mismo modelo llevados a cabo por CPU y por GPU con distintas configuraciones. 



Ilustración 36: Comparativa entrenamiento CPU y GPU 

### **2.8. Tensor Procesing Unit (TPU)** 

Una unidad de procesamiento tensorial o TPU es un tipo de coprocesador formado por un circuito integrado con una aplicación específica de aceleración de IA desarrollado por Google para el aprendizaje automatico y el Deep learning. Este coprocesador esta optimizado para utilizar TensorFlow, una biblioteca de código abierto desarrollada por la misma compañía para el aprendizaje automático. 

Los recursos de TPU aceleran el rendimiento de los cálculos de álgebra lineal, muy utilizados en las aplicaciones de aprendizaje automático. Las TPU minimizan el tiempo necesario para alcanzar la exactitud cuando entrenas modelos de redes neuronales complejas y extensas. Un modelo que antes tardaba semanas en entrenarse con otras plataformas de hardware ahora puede converger con las TPU en cuestión de horas. 

Están diseñados para un alto volumen de computación de baja precisión (en comparación con una GPU) con mayores IOPS (operaciones de entrada/salida por segundo) por vatio, y carece de hardware para rasterización/mapeo de texturas. 

54 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Las TPUs de Google realizan cálculos vectoriales y matrices de alta densidad muy rápidamente, por lo que encuentran su principal cuello de botella en las latencias de transferencia de datos entre la TPU y la memoria que se basa en buses PCI. La compilación parcial de un modelo, en el que la ejecución pasa de un lado a otro entre el host y el dispositivo, hace que la TPU esté inactiva la mayor parte del tiempo, a la espera de que lleguen los datos por medio del bus PCIe. A fin de solucionar este problema, el modelo de programación de Cloud TPU está diseñado para ejecutar gran parte del entrenamiento en la TPU, idealmente el ciclo de entrenamiento completo. Algunas de las características del modelo de entrenamiento ejecutado en TPU son las siguientes: 

- Se guardan todos los parámetros del modelo en la memoria del chip. 

- El coste computacional de trasladar los datos hasta el coprocesador TPU desde la memoria es amortizado es amortizado mediante la ejecución de las instrucciones de entrenamiento en bucle 

- Su integración con TensorFlow permite un preprocesado de los datos en CPU para aprovechar las características de hardware de las TPUs 

- Paralelización de procesado: Los cores de las TPUs ejecutan el mismo set de instrucciones de manera síncrona realizando una operación de reducción tras cada paso de la red neuronal en todos los núcleos. 

Las Cloud TPU están optimizadas para cargas de trabajo específicas. Existen cargas de trabajo cuyo entrenamiento es mas efectivo si se lleva a cabo en CPUs o en GPUs en lugar de en TPUs. En general, puede decidir qué hardware es mejor para su carga de trabajo según las siguientes pautas: 

#### CPUs 

- Creación rápida de prototipos que requiere la máxima flexibilidad 

- Modelos sencillos que no tardan en entrenar 

- Modelos pequeños con tamaños de batch pequeños 

- Modelos dominados por operaciones personalizadas de TensorFlow escritas en C++ 

#### GPUs 

- Modelos con una cantidad significativa de operaciones 

- Modelos medianos y grandes con tamaños de batch significativos 

55 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- Modelos que requieren operaciones complejas 

- Modelos no compatibles con TensorFlow 

TPUs 

- Modelos dominados por cálculos matriciales 

- Modelos sin operaciones personalizadas de TensorFlow dentro del ciclo de entrenamiento principal 

- Modelos que entrenan durante semanas o meses 

- Modelos grandes y muy grandes con tamaños de batch muy grandes 



Ilustración 37: TPU de Google 

### **2.9. Unidades de procesamiento visual** 

Una unidad de procesamiento de visión (VPU) es un tipo de microprocesador destinado a acelerar el aprendizaje automático y las tecnologías de inteligencia artificial. Es un procesador especializado que está diseñado para admitir tareas como el procesamiento de imágenes. 

Con la tendencia del aprendizaje profundo surge la necesidad de nuevas arquitecturas de hardware que permitan un mayor rendimiento para las tareas de aprendizaje automático, tanto durante el entrenamiento como durante la inferencia. 

El uso de procesadores de propósito general para aplicaciones de aprendizaje automático es limitado, principalmente debido a la irregularidad del acceso a la memoria que viene con largas paradas de memoria y grandes requisitos de ancho de banda. Como efecto secundario, esto conduce a aumentos significativos en el consumo de energía y los requisitos de disipación térmica. La industria se está desplazando hacia el diseño de procesadores donde el costo, la potencia y la disipación térmica son clave. Por lo tanto, han surgido coprocesadores especializados con el propósito de reducir las restricciones de consumo de energía y mejorar el rendimiento general para tareas de aprendizaje profundo. 

56 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Una unidad de procesamiento de visión (VPU) es un tipo de procesador que surge como una categoría de chips cuyo objetivo es proporcionar capacidades de consumo ultra bajo sin comprometer el rendimiento. Por lo tanto, los chips de la Unidad de procesamiento de visión están optimizados para realizar tareas de inferencia utilizando modelos de red convolucional (CNN) previamente entrenados. 

La unidad de procesamiento de visión es, en cierto modo, similar a una unidad de procesamiento de video que se usa con redes neuronales convolucionales. Cuando una unidad de procesamiento de video es un tipo específico de procesamiento de gráficos, una VPU se describe como más adecuada para ejecutar diferentes tipos de algoritmos de visión artificial. Estas herramientas pueden construirse con recursos específicos para obtener datos visuales de las cámaras y están diseñadas para procesamiento en paralelo. Al igual que las unidades de procesamiento de video, están especialmente orientadas al procesamiento de imágenes. Algunas de estas herramientas se describen como “de bajo consumo y alto rendimiento” y se pueden conectar a interfaces que permiten un uso programable. 

Un ejemplo de VPU que podemos encontrar en el mercado son las diseñadas por Intel para operar con su software de visión artificial. Una de ellas es el Movidius Myriad 2 VPU basado en la plataforma Intel Neural Compute Stick (NCS) que puede usarse para inferencia en redes convolucionales con una red preentrenada. 

La VPU Myriad 2 está diseñada como un coprocesador de 28 nm que proporciona aceleración de tensor de alto rendimiento. Por lo tanto, proporciona API de alto nivel que permiten a los programadores de aplicaciones aprovechar fácilmente sus características y un subsistema de memoria controlado por software que permite un control detallado de diferentes cargas de trabajo. Una curiosidad sobre estas unidades es que están diseñadas como si fueran un pen drive, lo cual facilita su accesibilidad y montaje en cualquier dispositivo [74]. 

La arquitectura de este chip está inspirada en la observación de que más allá de un cierto límite de frecuencia y tecnología de proceso, el costo es cuadrático en potencia para aumentos lineales en la frecuencia operativa. La VPU Myriad 2 fue diseñada siguiendo este principio, con 12 procesadores vectoriales altamente paralelizables, denominados Streaming Hybrid Architecture Vector Engines (SHAVE). Su arquitectura de conjunto de instrucciones y paralelismo proporciona una eficiencia de rendimiento altamente sostenible en una variedad de aplicaciones de visión artificial, incluidas aquellas con requisitos de baja latencia del orden de milisegundos. 

57 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 38:Intel Neural Compute Stick (NCS) 

Los benchmarks de rendimiento han demostrado que una combinación de varios chips VPU pueden proporcionar potencialmente un rendimiento equivalente en comparación con un sistema basado en CPU y GPU de referencia, al tiempo que reduce la potencia de diseño térmico (TDP) hasta 8 veces. 

Mientras tanto, la cantidad de inferencias por vatio de VPU es más de 3 veces mayor en comparación con los sistemas de CPU o GPU de referencia. En las pruebas, la tasa de error estimada top-1 fue del 32 % en promedio, con una diferencia de error de confianza del 0,5 %. 



Ilustración 39: Comparación de rendimiento entre CPU, GPU y multi VPU para varios tamaños de batch [75] 

La VPU Myriad X de Intel es la tercera generación y la VPU más avanzada de Movidius. La VPU Myriad X, por primera vez en su clase, presenta Neural Compute Engine, un acelerador de IA de hardware especializado para inferencias de aprendizaje profundo de redes neuronales profundas. 

Neural Compute Engine, junto con los 16 núcleos SHAVE y un rendimiento ultraalto (Movidius afirma que puede lograr más de un billón de operaciones por segundo de rendimiento máximo de inferencia DNN), hace que Myriad X sea una opción popular para dispositivos neuronales profundos. Redes y aplicaciones de visión artificial. 

58 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

La VPU Myriad X tiene un canal de procesamiento de imágenes 4K nativo con soporte para hasta 8 sensores HD que se conectan directamente a la VPU. Al igual que con Myriad 2, la VPU Myriad X se puede programar a través del kit de desarrollo Myriad (MDK), que incluye herramientas de desarrollo, marcos y API para implementar cargas de trabajo personalizadas de visión, imágenes y redes neuronales profundas en el chip. 

### **2.10 FPGA** 

Un FPGA o Field Programable Gate Array es un conjunto de circuitos integrados, como puede ser cualquier chip, que está pensado para entregarse sin ser configurado para que luego cada uno lo personalice y programe según la tarea que necesite que haga esa pieza, una vez esta ya se ha fabricado. 

Las FPGAs fueron inventadas en el año 1984 por Ross Freeman y Bernard Vonderschmitt, co-fundadores de Xilinx. Algunos de los principales fabricantes son Xilinx, Altera (comprado por Intel en 2015), MicroSem, Lattice Semiconductor o Atmel, entre otros. 

Los FPGA son más lentos que un ASIC (Application-Specific Integrated Circuit), procesadores específicos desarrollados para desarrollar una determinada tarea. Sin embargo, la gran flexibilidad de poder cambiar su configuración hace que su coste sea menor tanto para pequeños lotes de fabricación como para prototipado, debido al enorme gasto requerido para desarrollar y fabricar un ASIC. Los FPGA son empleados en la industria dedicadas al desarrollo de circuitos integrados digitales y centros de investigación para crear circuitos digitales para la elaboración de prototipos y pequeñas series de ASIC. 

El usuario programa el circuito o circuitos de hardware. La programación puede ser una simple y sencilla puerta lógica (una función Y u O), o puede implicar una o más funciones complejas, incluyendo funciones que, en conjunto, actúan como un procesador integral de múltiples núcleos. 

Una FPGA puede utilizarse cuando se necesita optimizar un chip para una carga de trabajo particular, o cuando sea probable que sea necesario hacer cambios en el nivel del chip más adelante. Los usos de las FPGAs cubren una amplia gama de áreas: desde equipos para vídeo e imágenes, hasta circuitos para aplicaciones informáticas, automovilísticas, aeroespaciales y militares, además de electrónica para procesamiento especializado y más. Las FPGAs son particularmente útiles para la creación de prototipos de circuitos integrados específicos para aplicaciones (ASIC) o procesadores. Una FPGA puede reprogramarse hasta que el diseño del ASIC o del procesador sea definitivo y esté libre de fallos, y comience la fabricación real del ASIC definitivo. El propio Intel utiliza FPGAs para hacer prototipos de nuevos chips [76]. 

59 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 40: Estructura interna de una FPGA [77]] 

Las FPGAs están adquiriendo una especial relevancia en el área de la inteligencia artificial debido a la flexibilidad que proporcionan, permitiendo modificar el comportamiento hardware en base a las necesidades especificas de cada modelo, pudiendo optimizarlo para cada uno de ellos. 

Para tener éxito, la inferencia de modelos requiere flexibilidad y baja latencia. Los FPGA pueden resolver ambos problemas. La naturaleza reprogramable de un FPGA asegura la flexibilidad requerida por la estructura en constante evolución de las redes neuronales artificiales. Los FPGA también proporcionan el paralelismo personalizado y la memoria de gran ancho de banda necesarios para la inferencia en tiempo real de un modelo. Los sistemas basados en FPGA pueden procesar datos y resolver tareas complejas más rápido que sus análogos virtualizados. Y aunque la tarea de reprogramar un FPGA no está al alcance de todo el mundo, los servicios en la nube acercan los servicios de procesamiento de datos basados en FPGA a los clientes. Algunos proveedores de la nube como Microsoft Azure incluso ofrecen un nuevo servicio, Aceleración como servicio (AaaS), que otorga a sus clientes acceso a los aceleradores FPGA. Una ventaja más es que las FPGA consumen menos energía que las GPU estándar. 

Algunos fabricantes de FPGA ya están trabajando en la implementación de FPGA basados en la nube para la aceleración de cargas de trabajo de IA y todo tipo de aplicaciones que requieran una computación intensa. Por ejemplo, Intel está impulsando el servicio Alibaba Cloud AaaS llamado instancias f1. Acceleration Stack para CPU Intel Xeon con FPGA, también disponible para usuarios de Alibaba Cloud, ofrece dos flujos de desarrollo de software populares, RTL y OpenCL [78]. 

La tecnología FPGA muestra un gran potencial para acelerar las cargas de trabajo relacionadas con la IA. Sin embargo, también tiene numerosos inconvenientes que debe tener en cuenta al considerar el uso de un FPGA para acelerar el procesamiento de datos. Veamos las ventajas y desventajas más importantes de usar un FPGA para acelerar las aplicaciones de IA. 

60 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

#### **Ventajas** 

- Flexibilidad: la capacidad de ser reprogramado para múltiples propósitos es uno de los principales beneficios de la tecnología FPGA. En cuanto a las soluciones relacionadas con la IA, se pueden reprogramar bloques separados o un circuito completo para adaptarse a los requisitos de un algoritmo de procesamiento de datos en particular. 

- Paralelismo: una FPGA puede manejar múltiples cargas de trabajo mientras mantiene el rendimiento de la aplicación a un alto nivel y puede adaptarse a cargas de trabajo cambiantes cambiando entre varios programas. 

- Latencia reducida: una FPGA tiene un ancho de banda de memoria mayor que una GPU normal, lo que reduce la latencia y le permite procesar grandes cantidades de datos en tiempo real. 

- Eficiencia energética: el aprendizaje automático y el aprendizaje profundo son soluciones que consumen muchos recursos. Pero es posible garantizar un alto nivel de rendimiento de la aplicación a bajo consumo para el aprendizaje automático mediante el uso de una FPGA. 

#### **Desventajas** 

- Programación: la flexibilidad de los FPGA tiene el precio de la dificultad de reprogramar el circuito. No hay suficientes programadores experimentados en el mercado. 

- Complejidad de implementación: si bien el uso de FPGA para acelerar el aprendizaje profundo parece prometedor, solo unas pocas empresas han intentado implementarlo en la vida real. Para la mayoría de los desarrolladores de soluciones de IA, un tándem más común de GPU y CPU podría parecer menos problemático. 

- Gastos: los dos primeros inconvenientes inevitablemente hacen que el uso de un FPGA para acelerar las aplicaciones basadas en IA sea una solución costosa. El costo de múltiples reprogramaciones de un circuito es considerablemente alto para proyectos de pequeña escala. 

- Falta de bibliotecas: hay pocas o ninguna biblioteca de aprendizaje automático que admita FPGA listas para usar. Sin embargo, hay un proyecto prometedor, LeFlow, iniciado por un equipo de investigadores de la Universidad de Columbia Británica. Este equipo quiere hacer posible el uso de FPGA con el marco de aprendizaje automático de TensorFlow, lo que facilita a los desarrolladores de Python el uso de FPGA para probar problemas de aprendizaje automático. 

61 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Los FPGA merecen un lugar entre los chips de IA basados en GPU y CPU para big data y aprendizaje automático. Muestran un gran potencial para acelerar las cargas de trabajo relacionadas con la IA, en particular la inferencia. Las principales ventajas de usar un FPGA para acelerar los procesos de aprendizaje automático y aprendizaje profundo son su flexibilidad, el paralelismo personalizado y la capacidad de reprogramarse para múltiples propósitos. 

Sin embargo, el concepto de IA impulsada por FPGA necesita un mayor desarrollo. A día de hoy, solo dos grandes empresas de TI, Alibaba y Microsoft, ofrecen aceleración en la nube basada en FPGA a sus clientes. La falta de fabricantes que ofrezcan circuitos que puedan manejar cargas de trabajo de tan alto nivel también impide que este concepto florezca. 

### **2.11. Nuevas arquitecturas hardware** 

### **2.11.1. Experimento Chip Fusión** 

Algunas de las arquitecturas a nivel de hardware en las que se está trabajando para continuar la evolución del hardware especializado en el procesado de modelos de inteligencia artificial es el hardware conocido como Analog AI. La IA analógica ofrece mejoras de rendimiento radicales al combinar cómputo y memoria en un solo dispositivo, eliminando el cuello de botella de von Neumann, en el cual supone la transferencia repetitiva de daros entre la memoria y el procesador. Estos viajes requieren tiempo y energía, lo que tiene un impacto negativo en el rendimiento. Esto se conoce como el cuello de botella de von Neumann. Al aprovechar las propiedades físicas de los dispositivos PCM (pase-change memory), el cálculo se realiza en el mismo lugar donde se almacenan los datos, lo que reduce drásticamente el consumo de energía. Debido a que no hay movimiento de datos, las tareas se pueden realizar en una fracción del tiempo y con mucha menos energía. Esto es diferente de una computadora convencional, donde los datos se transfieren desde la memoria DRAM a la CPU cada vez que se realiza un cálculo. Por ejemplo, mover 64 bits de datos de DRAM a CPU consume 1-2nJ, que es 10 000-2 000 000 veces más energía que la que se disipa en un dispositivo PCM que realiza una operación de multiplicación (1-100fJ). 



Ilustración 41: Arquitectura convencional vs Analog AI 

62 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

En la inferencia de aprendizaje profundo, la propagación de datos a través de múltiples capas de una red neuronal implica una secuencia de multiplicaciones de matrices, ya que cada capa se puede representar como una matriz de pesos sinápticos. En el experimento del chip Fusion, estos pesos se almacenan en los estados de conductancia de los dispositivos PCM. Los dispositivos están dispuestos en matrices de barras cruzadas, lo que crea una red neuronal artificial donde todas las multiplicaciones de matriz se realizan en el lugar de manera analógica. Esta estructura permite que la inferencia se realice usando poca energía con una alta densidad de área de sinapsis. 

El chip Fusion es un prototipo de prueba con el que solo se puede acceder a un único dispositivo PCM a la vez. Los futuros chips permitirán realizar todas las multiplicaciones de matrices en paralelo en un solo paso de tiempo, lo que mejorará en gran medida la velocidad y la eficiencia energética [72]. 

### **2.11.2. Brain-inspired computing** 

Otro ejemplo de desarrollo de hardware específicamente diseñado para la resolución de problemas de Deep Learning son los chips con inspiración en la arquitectura cerebral humana. El cómputo basado en eventos es un paradigma de inspiración biológica para representar datos como eventos asincrónicos, como picos de neuronas en el cerebro. 

Un ejemplo de desarrollo de este tipo de chips es el procesador neurosinaptico TrueNorth de IBM cuyo diseño imita la arquitectura de un cerebro humano pero basándose en transistores. 

Sin embargo el mayor proyecto de estas características que se está desarrollando en estos momentos se trata del Human Brain Project. Este proyecto es uno de los tres proyectos emblemáticos FET (Future and Emerging Technology). Iniciado en 2013, es uno de los proyectos de investigación más grandes del mundo. Más de 500 científicos e ingenieros de más de 140 universidades, hospitales docentes y centros de investigación de toda Europa se unen para abordar uno de los objetivos de investigación más desafiantes: el cerebro humano. Para abarcar la complejidad del cerebro, el proyecto está construyendo una infraestructura de investigación para ayudar a avanzar en la neurociencia, la medicina, la informática y las tecnologías inspiradas en el cerebro: EBRAINS. El HBP proporciona un marco en el que equipos de investigadores y tecnólogos trabajan juntos para ampliar ideas ambiciosas del laboratorio, explorar los diferentes aspectos de la organización del cerebro y comprender los mecanismos detrás de la cognición, el aprendizaje o la plasticidad. Los científicos del HBP realizan estudios experimentales específicos y desarrollan teorías y modelos para arrojar luz sobre el conectoma humano, abordando los mecanismos que subyacen al procesamiento de la información, desde la molécula hasta la señalización celular y las redes a gran escala. 

63 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Los equipos del proyecto transfieren los conocimientos adquiridos para tener un impacto en la salud y la innovación: los conocimientos de la investigación básica se traducen en aplicaciones médicas, para preparar el terreno para nuevos diagnósticos y terapias. Los descubrimientos sobre el aprendizaje y los mecanismos de plasticidad cerebral se utilizan para inspirar el progreso tecnológico, por ejemplo, en inteligencia artificial. Además, el proyecto estudia las implicaciones éticas y sociales del avance de la neurociencia y campos relacionados. 

En su fase final (abril de 2020 - marzo de 2023), el enfoque de HBP es avanzar en tres áreas científicas centrales: redes cerebrales, su papel en la conciencia y redes neuronales artificiales, mientras expande aún más EBRAINS [73]. 

### **2.11.3. Edge Computing** 

Edge computing acerca el procesamiento de datos a las cosas y las personas que producen y consumen los datos. 

El término “edge” es casi sinónimo de “local”, y se refiere a los datos en el límite de la red, en realidad en, cerca o alrededor del lugar físico donde se producen los datos, como una máquina, una torre de red, un vehículo autónomo o un robot. Edge Computing utiliza computadoras integradas, módulos y sistemas integrados de hardware/software que permiten extraer, calcular y compartir los datos en el origen. 

Edge AI combina la computación local con la inteligencia artificial (IA). Esto implica ejecutar algoritmos de IA en dispositivos locales con capacidad computacional. Edge AI no requiere conectividad e integración entre sistemas, lo que permite a los usuarios procesar datos en el dispositivo en tiempo real. 

El Edge computing choca frontalmente con el concepto cada vez más de moda de cloud computing o computación en la nube. La mayoría de los procesos de IA se realizan actualmente en centros basados en la nube, porque requieren una capacidad de cómputo sustancial. La desventaja es que los problemas de conectividad o de red pueden provocar un tiempo de inactividad o una ralentización significativa del servicio. Edge AI elimina estos problemas al hacer que los procesos de IA sean una parte integral de los dispositivos computacionales locales. Esto permite a los usuarios ahorrar tiempo gestionar los datos sin comunicarse con otras ubicaciones físicas. 

La ventaja más importante del Edge computing es que las aplicaciones se ejecutan directamente sobre los dispositivos que generan los datos. El procesamiento de datos en la nube toma segundos. El procesamiento de datos en local, por otro lado, puede tomar milisegundos o menos. Por ejemplo, los vehículos autónomos que realizan el procesamiento de datos en el borde pueden tomar decisiones mucho más rápido que si los datos se procesan en la nube. Dado que estas decisiones afectan la vida humana, el procesamiento de datos casi en tiempo real es fundamental. 

64 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Otra ventaja que presenta este modelo computacional reside en la privacidad de los datos. Cuando los datos se procesan en local no es necesario enviarlos a la nube, ni a localizaciones de terceros. Esto reduce el riesgo de vulnerabilidades en la gestión de los datos y facilita el cumplimiento de las leyes de protección de datos y GDPR. Sin embargo que los datos no sean trasladados de su localización original no quiere decir que este completamente seguros, deben implantarse protocolos de seguridad del dato y protección ante ataques externos. 

Edge AI realiza la mayor parte de su procesamiento de datos localmente, envía menos datos a través de Internet y, por lo tanto, ahorra una gran cantidad de ancho de banda de Internet. Además, el costo de los servicios de inteligencia artificial basados en la nube puede ser alto. 

Debido a que Edge AI procesa datos a nivel local, ahorra costos de energía. Los dispositivos están diseñados con un consumo de energía altamente eficiente, lo que significa que los requisitos de energía para ejecutar IA en local son mucho más bajos que en los centros de datos en la nube [79]. 

Existen múltiples ejemplos de utilización de Edge computing para aplicaciones de Inteligencia Artificial, algunas de las mas desarrolladas actualmente son: 

- Cámaras de seguridad: Las cámaras de vigilancia tradicionales graban imágenes durante horas y almacenan y utilizan los datos según sea necesario. Sin embargo, con Edge AI, el proceso algorítmico se ejecuta en el propio sistema en tiempo real, lo que permite que la cámara detecte y maneje actividades sospechosas en tiempo real. Esto asegura un servicio más eficiente y menos costoso. 

- Análisis de video: por ejemplo, Edge AI puede ayudar a generar respuestas automatizadas a estímulos audiovisuales en robots. También se puede utilizar para el reconocimiento en tiempo real de espacios y escenas. 

- Mejorar la eficacia del Internet industrial de las cosas (IIoT): los algoritmos de IA pueden monitorizar posibles defectos y errores en la cadena de producción y permitir ajustes en tiempo real en los procesos de producción. 

El Edge computing está directamente relacionado con el área de internet de las cosas, el cual nos permite obtener datos para alimentar a los modelos de inteligencia artificial, y facilitar su procesado en tiempo real reduciendo las latencias y mejorando los resultados. 

65 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

## **3. Internet of Things** 

_“Tomar decisiones con el internet de las cosas supone una importante reducción de costes a las empresas. Los expertos consideran que la tecnología del internet de las cosas (IoT) no solo puede crear procesos nuevos, sino que aporta valor añadido a los que ya existen y los mejora en combinación con la inteligencia artificial (IA)”_ 

La internet de las cosas (IoT, por sus siglas en inglés) es un sistema de dispositivos de computación interrelacionados, máquinas mecánicas y digitales, objetos, animales o personas que tienen identificadores únicos y la capacidad de transferir datos a través de una red, sin requerir de interacciones humano a humano o humano a computadora [80]. En términos simples, el Internet de las cosas (IoT) hace referencia a la tendenciaconstante de conectar todo tipo de objetos físicos al Internet, especialmente aquellos que quizá ni se imagina. Para ser más específicos, el término IoT hace referencia a los sistemas de dispositivos físicos que reciben y transfieren datos a través de redes inalámbricas sin la intervención humana. 

Esta tecnología está recibiendo una gran cantidad de atención en los últimos tiempos. 

La curva del Hype de Tecnologías Emergentes de Gartner es una representación gráfica de la madurez, adopción y aplicación comercial de tecnologías específicas. El informe Hype Cycles publica de forma anual y proporciona una perspectiva transversal de las tendencias de las industrias tecnológicas emergentes, ayudando a discernir si nos encontramos ante una sobreexpectacióno ante una tecnología viable [90]. 



Ilustración 42: Hype Cycle de Garthner 

66 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Esta curva sitúa el internet de las cosas en su punto álgido de expectativas y se espera que logre su madurez tecnológica en el próximo lustro, aunque a día de hoy podemos encontrar ya una gran implantación de esta tecnología. 

El área de Internet de las cosas representa uno de los mayores campos de actuación para la implementación de inteligencia artificial y al mismo tiempo supone una enorme fuente de datos disponibles para el desarrollo de nuevos modelos. Por ello cuando se habla de internet de las cosas es necesario tener en cuentas las aplicaciones de inteligencia artificial que pueden ser integradas en los propios dispositivos. 

Los modelos de inteligencia artificial que se ejecutan con analítica de datos convencional son a menudo estáticos y de uso restringido con información no estructurada y con cambios rápidos a los que el modelo no es capaz de adaptarse. Sin embargo, los modelos de inteligencia artificial que se aplican sobre dispositivos de internet de las cosas son capaces de compaginar múltiples fuentes de información provenientes de sensores y componentes externos que generan una gran cantidad de datos en tiempo real. 

Por su parte el Internet de las cosas tiene una importante limitación en cuanto a la capacidad de actuación, ya que no es capaz de aprender por si mismo y, por tanto, adaptar su aplicación. Integrando la Inteligencia Artificial con una red de objetos conectados les permitirá tomar decisiones autónomas. 

Tomar decisiones con el internet de las cosas supone una importante reducción de costes a las empresas. Los expertos consideran que la tecnología del internet de las cosas (IoT) no solo puede crear procesos nuevos, sino que aporta valor añadido a los que ya existen y los mejora en combinación con la inteligencia artificial (IA) [81]. 

Por ello es importante tener un conocimiento general de las tecnologías y arquitecturas IoT para poder aplicar técnicas de Inteligencia Artificial que nos permitan explotar al máximo esta área de actuación. 

Dentro del área de Internet de las Cosas es necesario definir una serie de conceptos para poder comprender de qué manera funciona esta tecnología: 

#### **Internet** 

Internet es un conjunto descentralizado de redes de comunicación interconectadas que utilizan la familia deprotocolosTCP/IP, lo cual garantiza que las redes físicas heterogéneas que la componen constituyan una red lógica única de alcance mundial. 

#### **Things (las cosas)** 

Una “cosa” es cualquier objeto susceptible de incorporar electrónica que pueda transferir datos a través de una red sin ninguna interacción humana. Pueden o no disponer de sensores y también pueden ser más o menos inteligentes en función de su capacidad de procesamiento. 

67 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

#### **Soluciones IoT** 

Una solución de IoT es un conjunto de dispositivos y sensores conectados a una plataforma clouda través de un gateway. Las soluciones IoT son el resultado de la convergencia de varias tecnologías, incluyendo las comunicaciones inalámbricas, los sistemas microelectrónicos e Internet. 

#### **Sensor** 

Los sensores son componentes que miden variables físicas y las convierten a señales eléctricas (voltaje). Existe una gran disponibilidad comercial, listos para usar y específicos para medir un amplio abanico de variables 

#### **Solución IoT** 

Una solución de IoT es un conjunto de dispositivos y sensores conectados a una plataforma clouda través de un gateway. Las soluciones IoT son el resultado de la convergencia de varias tecnologías, incluyendo las comunicaciones inalámbricas, los sistemas microelectrónicos e Internet. 

#### **Gateway** 

En el ámbito de las telecomunicaciones, el objetivo principal de un Gateway es servir de puente entre los diferentes tipos de tecnologías de la comunicación. Por ejemplo, su Gateway de Internet en casa conecta su Red de Área Local (LAN) con su Proveedor de Servicios de Internet (ISP). Un Gateway IoT crea un puente entre los sensores/actuadores IoT e Internet, agregando todos los datos, traduciendo protocolos y preprocesandolos datos antes de enviarlos. 

#### **Plataforma IoT** 

Plataforma cloudque proporciona la infraestructura necesaria para gestionar gran variedad de dispositivos IoT además de permitir almacenar, asegurar y analizar una gran cantidad de datos para extraer información de valor. 



Ilustración 43: Esquema procesamiento Internet de las Cosas 

68 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

El término de Internet de las cosas se acuño en 1999, aunque esta tecnología ha sido desarrollada durante décadas. El primer dispositivo considerado como IoT, es la máquina de vending que apareció en 1982 [82], y desde entonces la cantidad de dispositivos disponibles no ha hecho más que aumentar hasta la actualidad donde podemos encontrar dispositivos inteligentes en todas partes. Algunos ejemplos de dispositivios de IoT que podemos encontrar en la actualidad son los smartphones, asistentes de voz, o los coches autónomos. Además de estos dispositivos complejos también podemos encontrar otros dispositivos más sencillos que se encuentran conectados dentro de la red como cámaras de vigilancia, sensores térmicos o simples infrarrojos. 

Previa a la aparición de los sistemas de IoT, existieron otros protocolos de comunicación que nos permitían conectar dispositivos y transmitir datos sin emplear internet. Un ejemplo de ello es el sistema ACARS (Aicraft Communications Addressing and Reporting System) empleado en aviación. Este es un sistema de enlace de datos digital para la transmisión de mensajes cortos entre la aeronave y las estaciones terrestres vía radio banda aérea o satélite. El protocolo fue diseñado por ARINC y se implementó en 1978 [83]. 

La evolución de estos dispositivos también se ha visto directamente influenciada por la ley de Moore, que determinaba que aproximadamente cada dos años se duplicaba el número de transistores en un procesador. Esto unido a la economía a gran escala ha permitido la democratización de los sensores y otros componentes electrónicos, facilitando el desarrollo del IoT. A día de hoy existen más de 50000 millones de dispositivos conectados a internet, lo cual nos indica que esta tecnología ha llegado para quedarse. 



Ilustración 44: Evolución de los dispositivos conectados a internet [84] 

Este aumento exponencial de dispositivos conectados también ha repercutido en la cantidad de datos generados y disponibles para su tratamiento. Si tratamos el IoT desde la perspectiva del Big Data y la Inteligencia Artificial, este adquiere una especial relevancia gracias a los datos que proporciona con tres perspectivas diferentes: volumen, velocidad y variedad. 

69 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

#### **Volumen** 

En el informe de 2018 de IDC Data Age 2025 [85], se hace una previsión (por ahora acertada) del volumen de datos existente para los años próximos hasta el 2025. 



Ilustración 45: Crecimiento estimado de los datos disponibles 

Equivalencias (en sistema decimal) 

1 Terabyte (TB) = 1000 Gigabytes (GB). 

1 Petabyte (PB) = 1000 Terabytes. 

1 Exabyte (EB) = 1000 Petabytes. 

1 Zettabyte (ZB) = 1000 Exabytes = 1 millón de petabytes = 1000 millones de terabytes. 

#### **Variedad** 

De esta inabarcable cantidad de datos, en el mismo informe Data Age 2025, se estima que para 2025 de los 175 totales, 90 ZB serán originados por dispositivos IoT. Estos, en su mayoría se tratarán de datos no estructurados, no analizables con analítica tradicional. 

#### **Velocidad** 

De una manera similar, en el mismo informe Age 2025, se hace un cálculo y una previsión del % de datos en tiempo real respecto al volumen total donde, el IoT y el Edge Computing tienen una importancia vital. 

Una consecuencia directa del amadurez del IoT es el incremento exponencial en el número de dispositivos conectados, y directamente relacionado, el aumento significativo en la cantidad de datos que procesar. 

Esta ingente cantidad de datos no es de utilidad hasta que son recopilados, almacenados y analizados, entrando en juego el Big Data y la Inteligencia Artificial. 

70 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

El IoT pasará pronto a ser la primera fuente de generación de datos del planeta, por lo que su importancia en el contexto de la Inteligencia Artificial es vital. 

La democratización de ambas tecnologías el IoT y la Inteligencia Artificial (abaratamiento de dispositivos y de la capacidad de procesamiento) se traduce una verdadera explosión de aplicaciones revolucionaras. Ciudades inteligentes, un mejor aprovechamiento de los recursos energéticos, domótica o el coche autónomo, son algunos de los muchos campos donde estas dos tecnologías tendrán recorrido en los próximos años. 

Las soluciones de Internet of Things están compuestas por tres pilares principales: hardware, conectividad de red y software. 

### **3.1. Hardware** 

Los dispositivos conectados son el core del IoT. En el contexto del IoT, un dispositivo se refiere a cualquier instrumento que como mínimo capte información y la transmita sin necesidad de intervención humana. Algunos ejemplos podrían ser: 

- Un sensor de presión dentro de una tubería 

- Un sensor de temperatura dentro de un camión frigorífico 

- Pequeños chips insertados bajo la piel de una vaca 

Los dispositivos pueden ser independientes o trabajar en sincronía con otros. 

En un sistema IoT, el hardware hará referencia a todos aquellos componentes físicos que: 

- Tengan capacidad de procesamiento 

- Tengan capacidad de percibir señales o actuar con el entorno 

- Permitan la comunicación con la red u otros dispositivos. 

Aunque para entornos productivos el hardware suele diseñarse y fabricarse para una solución específica, existen algunas plataformas como Arduino o RaspberryPi que ayudan a hacer realidad prototipados rápidos sin incurrir en altas inversiones en costes y tiempo de implementación. 

Hay características claves que son comunes a los dispositivos de IoT y que proporcionan una base de comparación a la hora de tomar decisiones a la hora de configurar una nueva red o para desarrollar y ampliar una ya existente. Los dispositivos IoT pueden caracterizarse por sus capacidades de: 

71 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- Captación y gestión de datos: Recogida de información analógica a intervalos fijos (data samplerate). 

   - Sensores: Miden las variables físicas y las convierten en señales eléctricas (voltaje) 

   - Actuadores: Dispositivo capaz de transformar un estímulo eléctrico en otro tipo de energía, movimiento u otra forma de trabajo, con la finalidad de generar un efecto sobre un sistema. Ej: motores, diodos led… 

- Procesamiento y almacenamiento de los datos: Tradicionalmente los dispositivos IoT tan solo captaban la información y la enviaban para ser almacenada y posteriormente analizada en centros de procesamiento de datos. Con el aumento de la capacidad de procesamiento y la reducción del tamaño de los procesadores, se ha ido posibilitando la capacidad de pre-tratar los datos antes de enviarlos a los gatewayso aplicaciones en la nube para su posterior agregación y análisis. Con el tiempo, los avances en la tecnología han permitido la aparición del Edge Computing que permite realizar el procesado y el análisis de los datos en los dispositivos IoT de una red en lugar de en una ubicación centralizada. Los datos pueden ser analizados en tiempo real en los dispositivos mismos en lugar de transmitir grandes volúmenes de datos a un servidor cloud o a un centro de datos para su posterior análisis. 

- Conectividad: La conectividad de la red es una característica definitoria de cualquier dispositivo IoT. Los dispositivos pueden trabajar de forma autónoma, enviando la información a internet por medio de un gateway, o bien, trabajar de forma colaborativa interconectándose entre varios. Podemos encontrar ejemplos de conectividad por cable, apropiada para dispositivos fijos como aparatos de domótica o aplicaciones industriales y comunicación inalámbrica, apropiada tanto para dispositivos fijos como móviles puede realizarse mediante distintos protocolos como WiFi, Bluetooth, Redes de telefonía, RFID… 

- Gestión de la energía: El manejo de la energía es un factor crítico para los dispositivos de IoT portátiles y llevables ya que dependen de una fuente de energía inalámbrica, como las baterías o las células fotovoltaicas (solares). Según los patrones de uso y los requisitos de energía de los sensores, actuadores o circuitos integrados conectados, un dispositivo puede ponerse en modo de suspensión o en modo de bajo consumo periódicamente para conservar la energía. 

72 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

### **3.2. Redes** 

Las redes permiten que los dispositivos de IoT se comuniquen unos con otros, con aplicaciones y con servicios que se ejecutan en la nube. Una red está constituida por distintos elementos: 

- Dispositivos finales: Aquellos que hagan uso de la red, es decir, aquellos que envían y reciben información. Entre ellos encontramos PCs, teléfonos, servidores, cámaras IP… 

- Equipos de red: Aquellos elementos que hacen funcionar a la red, asegurando la trasnferencia de información desde un origen hasta un destino. Entre ellos encontramos firewalls, routers, switches, access points… 

- Enlaces: Interconectan la red entre sí y con los dispositivos finales, ej. Cables de cobre, cables de fibra óptica, enlaces de radio… 

- Protocolos y Estándares: Son conjuntos de reglas que permiten la comunicación entre dos dispositivos. Cuando estos protocolos se utilizan de manera extendida se conocen como protocolos estándar, por ejemplo, HTTP 

### **3.3. Software** 

Los dispositivos de IoT trabajan con un software especifico que les permite realizar las funciones para las que están diseñados. En dispositivos comerciales el software se encuentra diseñado específicamente para el hardware del dispositivo y generalmente no requiere desarrollo propio. Sin embargo en la actualidad existe una gran variedad de dispositivos para soluciones IoT que permiten el desarrollo de software específico para cada problema. Algunos de los dispositivos mas representativos dentro del área de IoT que permiten su personalización son: 

- Arduino: Arduino es una plataforma de creación de electrónica de código abierto, la cual está basada en hardware y software libre, flexible y fácil de utilizar para los creadores y desarrolladores, orientado principalmente a la formación y al prototipado. 



Ilustración 46: Arduino 

73 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- RaspberryPi: La RaspberryPi es una serie de ordenadores de placa única (SBC) de bajo coste desarrollados con el objetivo de poner en manos de las personas de todo el mundo el poder de la informática y la creación digital 



Ilustración 47: RaspberryPi 

- ASICs: Un circuito integrado específico de la aplicación (ASIC) es un término usado para describir un circuito integrado (IC) que se fabrica a pedido y en forma personalizada para un uso particular 

Una solución completa de Internet of Things incluye el procesado por medio de Big Data de los datos recogidos y su aplicación por medio de modelos de inteligencia artificial para transformar los dispositivos en agentes inteligentes capaces de tomar decisiones. El flujo de una solución de IoT contemplaría las siguientes fases: 

1. Inicial: La solución está compuesta por sensores, dispositivos ad hoc, NFC… Estos cuentan con una funcionalidad limitada ya que no se encuentran conectados a la red y solo trabajan en un modelo de comunicación M2M (machine to machine) 

2. Conectado: Entran en juego dispositivos conectados como dispositivos wereables (relojes inteligentes, gafas interactivas, auriculares…), redes de baja potencia como LoRa y protocolos como MQTT. En esta fase los dispositivos están conectados entre si a través de protocolos específicos. 

3. Online: En esta fase se incorpora el acceso online a los dispositivos, conexión ERP, monitorización de los dispositivos… Esto permite una gestión remota de los mismos lo que facilita la calidad del servicio. 

4. Analítico: En esta fase se pasa al procesado de los datos generados por los dispositivos. Estos análisis han de realizarse en base al contexto con el que se han tomado los datos y suponen una importante fuente de conocimiento. Pueden aplicarse distintos modelos de Big Data que nos permiten obtener estadísticas, gráficas, dashboards… 

5. Operacional: En la última fase del IoT entra en juego la Inteligencia Artificial, inclusión de modelos, y APIs y RPAs que permitan la aplicación de los resultados de los mismos. Esto permite a los dispositivos tomar decisiones inteligentes, adaptar su comportamiento en base al aprendizaje y sincronizarse con otros dispositivos. 

74 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Dentro del ecosistema del Internet de las Cosas encontramos distintos actores que permiten la cohesión de las distintas áreas tecnológicas que conforman estas soluciones. 

- Fabricantes de Hardware: Se encargan de proporcional los dispositivos de IoT. Actualmente en el mercado existen muchos fabricantes de dispositivos, pero algunos de los más destacados son CISCO, QUALCOMM o INTEL. 

- Empresas de telecomunicaciones: Proporcionan los entornos de red necesarios para la comunicación entre los diferentes dispositivos. Algunos ejemplos de líderes del mercado son Telefónica, Vodafone, Orange… 

- Proveedores de soluciones: En este área encontramos a gigantes tecnológicos que desarrollan sus propias soluciones y también actúan como consultoras de IoT como Amazon, IBM, Google o Microsoft amen de múltiples startups que están generando grandes impactos en el mercado. 

Algunos de los sectores donde el IoT puede tener una mayor área de aplicación son los siguientes: 

- Salud: Los dispositivos wearables y dispositivos integrados dentro del cuerpo humano permiten monitorizar las constantes humanas permitiendo el seguimiento de enfermedades, mantenimiento fitness e incrementar la productividad 

- Domótica: Es una de las áreas mas desarrolladas en la actualidad para el IoT, sin embargo, aún tiene un amplio recorrido en la gestión inteligente de edificios y sistemas de seguridad. 

- Retail: Los espacios comerciales que incluyen la participación del consumidor final como tiendas, bancos, restaurantes… pueden ser un campo de aplicación del IoT mediante la automatización de algunos procesos como el auto-pago, gestión de ofertas u optimización de inventarios. 

75 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- Oficinas: Gestión inteligente de edificios, pero también la gestión de la movilidad de los empleados, la utilización de la energía o la seguridad. 

- Fábricas: Existen múltiples tareas susceptibles de automatización, mejora de eficiencia de procesos, equipos e inventarios 

- Industria energética: Customización de entornos productivos como minas, refinerías o plantas solares mediante la integración de sensores inteligentes que faciliten el control de la situación. 

- Vehículos: El ejemplo clásico de aplicación de IoT en transporte pasa por el coche autónomo, sin embargo esta tecnología es aplicable a otras áreas como mantenimiento, mejoras de diseño en base a la utilización, o analíticas de consumo 

- Ciudades: Las Smart cities son uno de los grandes campos de actuación del IoT. Esta tecnología presenta aplicaciones en el control del tráfico, planificación de espacios urbanísticos, control medioambiental, y gestión de recursos. 

### **3.4. Industria 4.0** 

Un de los puntos de encuentro entre la tecnología de internet de las cosas y la inteligencia artificial se encuentra en lo que se conoce como Industria 4.0. Sinónimo de manufactura inteligente, la Industria 4.0 es la realización de la transformación digital del campo (industrial), que brinda toma de decisiones en tiempo real, productividad mejorada, flexibilidad y agilidad [86]. 

Hablar de Industria 4.0 implica comprender el abanico de nuevas tecnologías que aparecen con esta revolución como: los Sistemas MES (Manufacturing Execution Systems), Sistemas MOM (Manufacturing Operation Management), la Analítica Avanzada, la Inteligencia Artificial (AI), la Robótica Colaborativa, el Industrial Internet of Things (IIoT), el Big Data, entre muchas otras. Cada una de estas tecnologías responde a una necesidad específico entorno a la eficiencia productiva, pero uno de los mayores retos de la Industria 4.0 es determinar cuáles son los objetivos particulares y la ruta adecuada para implantar un proyecto [87]. 

La evolución de la tecnología aplicada a la industria marco un antes y un después con la tercera revolución industrial, que comenzó a mediados del siglo XX y agregó computadoras, telecomunicaciones avanzadas y análisis de datos a los procesos de manufacturación. La digitalización de las fábricas comenzó con la incorporación de controladores lógicos programables (PLC) en la maquinaria para ayudar a automatizar algunos procesos y recopilar y compartir datos. 

76 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Actualmente estamos en medio de la cuarta revolución industrial, también conocida como la Industria 4.0. Caracterizada por una creciente automatización y el empleo de máquinas y fábricas inteligentes. Los datos ayudan a producir bienes de manera más eficiente y productiva en toda la cadena de producción. Se mejora la flexibilidad para que los fabricantes puedan satisfacer mejor las demandasde los clientes mediante la personalización masiva. 

Al recopilar más datos de la planta y combinarlos con otros datos operativosde la empresa, una fábrica inteligente puede lograr transparenciade la información y mejores decisiones. 



Ilustración 48: Evolución de la industria 

Los principios de la filosofía de la industria 4.0 son: 

- Más automatización de la toma de decisiones 

- Cambio de rol para la fuerza de trabajo trasladando el trabajo a las máquinas 

- Nueva organización industrial y nuevos paradigmas de colaboración 

- Conexión de sistemas ciber-físicos incluyendo la seguridad desde el inicio 

- Conversión de datos desde varias fuentes IT (tecnología de la información) y OT (tecnología operacional) hacia nuevos modelos de decisión y negocio 

El objetivo de la Industria 4.0 es la automatización y mejora de los procesos optimizando la productividad y la producción, lo cual se traduce en innovación, transición a nuevos modelos de negocios y transición a nuevas fuentes de beneficio a través de la información y los servicios. 

77 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Las motivaciones de este cambio vienen dadas por distintos factores como el económico, ya que la actualización de la industria permite la flexibilización del proceso productivo facilitando la personalización de lotes de productos más pequeños sin incrementar los gastos de producción mediante la digitalización de los productos y maquinaria. La inclusión de tecnologías modernas como el Internet de las cosas, Big Data, la inteligencia artificial y el blockchain permite aplicar los principios del Lean Manufacturing a lo largo de la cadena industrial. 

El lean manufacturing  es un modelo de gestión que se enfoca en minimizar las pérdidas de los sistemas de manufactura al mismo tiempo que maximiza la creación de valor para el cliente final. Para ello utiliza la mínima cantidad de recursos, es decir, los estrictamente necesarios para el crecimiento [88]. 

Mas allá de los intereses meramente económicos podemos encontrar intereses políticos en la aplicación de este tipo de tecnología ya que optimizar las cadenas de suministro hace atractiva la producción local incluso en países altamente desarrollados donde los salarios cualificados son altos. El proceso de automatización hace que la brecha salarial no sea un problema gracias a la reducción de costes y de personal necesario para operar. 

La industria 4.0 converge distintos tipos de tecnologías que permiten la evolución de los procesos productivos. 

#### **Computación en la nube** 

La computación en la nube es la piedra angular de cualquier estrategia de Industria 4.0. La plena realización de la manufactura inteligente exige conectividad e integración de ingeniería, cadena de suministro, producción, ventas, distribución y servicio. La nube permite que esto sea posible. Además, la gran cantidad de datos que normalmente se almacenan y analizan se puede procesar de manera más eficiente y rentable con la nube. La computación en la nube también puede reducir los costos iniciales para los fabricantes pequeños y medianos que pueden ajustar sus necesidades y escalar a medida que crece su negocio. 

#### **Internet de las cosas (IoT)** 

El Internet de las cosas (IoT) es un componente principal de las fábricas inteligentes. Las máquinas en la planta de producción están equipadas con sensores que cuentan con una dirección IP que permite que las máquinas se conecten con otros dispositivos habilitados para la web. Esta mecanización y conectividad hacen posible que se recopilen, analicen e intercambien grandes cantidades de datos valiosos. 

78 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

#### **IA y machine learning** 

La inteligencia artificial y el machine learning permiten a las empresas manufactureras aprovechar al máximo el volumen de información generada no solo en la planta de producción, sino en todas sus unidades comerciales, e incluso de socios y fuentes de terceros. La IA y el machine learning pueden crear insights que brinden visibilidad, previsibilidad y automatización de operaciones y procesos comerciales. Por ejemplo: las máquinas industriales tienden a averiarse durante el proceso de producción. El uso de datos recopilados de estos activos puede ayudar a las empresas a realizar un mantenimiento predictivo basado en algoritmos de machine learning, lo que resulta en más tiempo. 

#### **Edge computing** 

Las demandas de las operaciones de producción en tiempo real significan que algunos análisis de datos deben realizarse en el “borde”, es decir, donde se crean los datos. Esto minimiza el tiempo de latencia desde que se producen los datos hasta que se requiere una respuesta. Por ejemplo, la detección de un problema de seguridad o calidad puede requerir una acción casi en tiempo real con el equipo. El tiempo necesario para enviar datos a la nube empresarial y luego volver a la fábrica puede ser demasiado largo y depende de la confiabilidad de la red. El uso de edge computing también significa que los datos permanecen cerca de su fuente, lo que reduce los riesgos de seguridad. 

#### **Ciberseguridad** 

Las empresas manufactureras no siempre han considerado la importancia de la ciberseguridad o los sistemas ciberfísicos. Sin embargo, la misma conectividad de los equipos operativos en la fábrica o el campo (OT) que permite procesos de manufactura más eficientes también expone nuevas rutas de entrada para ataques maliciosos y malware. Al pasar por una transformación digital hacia la Industria 4.0, es esencial considerar un enfoque de ciberseguridad que abarque los equipos de IT y OT. 

#### **Gemelo digital** 

La transformación digital que ofrece la Industria 4.0 ha permitido a los fabricantes crear gemelos digitales que son réplicas virtuales de procesos, líneas de producción, fábricas y cadenas de suministro. Un gemelo digital se crea al extraer datos de sensores, dispositivos, PLC y otros objetos del IoT conectados a Internet. Los fabricantes pueden usar gemelos digitales para ayudar a aumentar la productividad, mejorar los flujos de trabajo y diseñar nuevos productos. Al simular un proceso de producción, por ejemplo, los fabricantes pueden probar cambios en el proceso para encontrar formas de minimizar el tiempo de inactividad o mejorar la capacidad. 

79 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 49: Gemelo Digital [89] 

Algunas de las ventajas de los gemelos digitales son: 

- Reducir los riesgos operativos, al poder simularse fallos y poder corregirse antes de su implementación 

- Permitir monitorizar escenarios hipotéticos bajo la premisa de “Qué pasaría si…” por ejemplo, para implementaciones de alta densidad 

- Poder enfocar mejor la planificación de la capacidad del centro de datos, reduciendo el coste ya que se ajusta “a medida” las demandas de infraestructura, energía o recursos de refrigeración. 

Una fábrica inteligente cuenta con las siguientes características: 

- **Análisis de datos para una óptima toma de decisiones:** Los sensores integrados y la maquinaria interconectada producen una cantidad significativa de bigdata para las empresas manufactureras. La analítica de datos puede ayudar a los fabricantes a investigar tendencias históricas, identificar patrones y tomar mejores decisiones. Las fábricas inteligentes también pueden usar datos de otras partes de la organización y su ecosistema extendido de proveedores y distribuidores para crear insights más detallados. Al observar los datos de recursos humanos, ventas o almacenamiento, los fabricantes pueden tomar decisiones de producción basadas en los márgenes de ventas y el personal. Se puede crear una representación digital completa de las operaciones como un “gemelo digital”. 

- **Integración de IT y OT:** La arquitectura de red de la fábrica inteligente depende de la interconectividad. Los datos en tiempo real recopilados de sensores, dispositivos y máquinas en la planta de producción pueden ser consumidos y utilizados de inmediato por otros activos de la fábrica, así como compartidos entre otros componentes en el lote de software empresarial, incluida la planificación de recursos empresariales (ERP) y otro software de gestión comercial. 

80 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 50: IT vs OT 

- **Fabricación personalizada:** Las fábricas inteligentes pueden producir productos personalizados que satisfagan las necesidades de los clientes individuales de manera más rentable. De hecho, en muchos segmentos de la industria, los fabricantes aspiran a lograr un “tamaño de lote 1” de manera económica. Mediante el uso de aplicaciones de software de simulación avanzadas, nuevos materiales y tecnologías como la impresión 3D, los fabricantes pueden crear fácilmente pequeños lotes de artículos especializados para clientes particulares. Mientras que la primera revolución industrial fue sobre la producción en masa, la Industria 4.0 se trata de la personalización en masa. 

- **Cadena de suministro:** Las operaciones industriales dependen de una cadena de suministro transparente y eficiente, que debe integrarse con las operaciones de producción como parte de una sólida estrategia de Industria 4.0. Esto transforma la forma en que los fabricantes obtienen sus materias primas y entregan sus productos terminados. Al compartir algunos datos de producción con los proveedores, los fabricantes pueden programar mejor las entregas. 

Si, por ejemplo, una línea de montaje experimenta una interrupción, las entregas se pueden desviar o retrasar para reducir el tiempo o los costos perdidos. Además, al estudiar el clima, los datos de los socios de transporte y de los minoristas, las empresas pueden utilizar el envío predictivo para enviar productos terminados en el momento justo para satisfacer la demanda de los consumidores. Blockchain está emergiendo como una tecnología clave para permitir la transparencia en las cadenas de suministro. 

81 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

## **4. Dispositivos y sensores** 

_“Los sensores son una importante fuente de datos para alimentar los modelos de inteligencia artificial. Actualmente existen multitud de sensores disponibles en el mercado los cuales se agrupan generalmente en función de la magnitud física que permiten medir.”_ 

La sensorización y captura de datos es un mundo extremadamente amplio y complejo debido a la multitud de aplicaciones, sectores y ámbitos donde requerimos extraer información. Capturar datos y métricas siempre ha sido una necesidad en el mundo de los procesos y operaciones industriales, y desde hace unos años, con los nuevos avances tecnológicos y con la transformación digital encima de la mesa, la extracción de datos se ha convertido en unos de los ejes principales de la revolución tecnológica de la inteligencia artificial ya que nos permite obtener información en tiempo real fomentando la capacidad de tomar decisiones de forma rápida y flexible. 

Los sensores son los dispositivos capaces de convertir el mundo real (físico/químico) en el mundo digital (electrónico), nos permiten llevar la realidad a una dimensión que podemos gestionar para finalmente tomar decisiones e, incluso, actuar sobre el propio entorno. Son equipos que convierten la magnitud de entrada (temperatura, humedad, nivel, presión, etc.) en una señal eléctrica medible e interpretable por los dispositivos electrónicos, y capaz de ser almacenada en una base de datos para su posterior uso y proceso. 

Una magnitud eléctrica puede ser una resistencia eléctrica (como en un detector de temperatura), una capacidad eléctrica (como en un sensor de humedad o un sensor capacitivo), una corriente eléctrica (como en un transistor sensible a la luz), etc… Los sensores, se pueden clasificar en función de los datos de salida en Digitales o Analógicos, y se utilizan para desarrollar interfaces físicas, sistemas robóticos,… 



Ilustración 51: Esquema de actuación de un sensor 

82 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Gracias a la revolución de la industria conectada (Industria 4.0) cada vez existe una mayor oferta de sensores inteligentes (“Smart Sensors”) que, además de medir la magnitud en cuestión, llevan integrado un circuito electrónico compatible con los estándares de comunicaciones más habituales en el mundo de IoT. 

Los sensores son una importante fuente de datos para alimentar los modelos de inteligencia artificial. Actualmente existen multitud de sensores disponibles en el mercado los cuales se agrupan generalmente en función de la magnitud física que permiten medir. Estos van desde sensores sencillos como sensores térmicos, magnéticos o de humedad a complejos dispositivos que nos permiten obtener fuentes de datos limpias y disponibles para su análisis, o en los que podemos integrar las funciones de inferencia del proceso de inteligencia artificial. 

En función de su campo de actuación podemos encontrar distintos tipos de sensores. Es esta unidad vamos a repasar algunos de los mas relevante a la hora de proporcionar datos útiles para su integración en modelos de inteligencia artificial. La cantidad de dispositivos y sensores disponibles en el mercado cada vez es mayor, incrementando la disponibilidad de datos. 

### **4.1. Sensores de propósito general** 

Existen múltiples sensores de propósito general que podemos encontrar integrados en distintos dispositivos, de manera independiente o integrados en instalaciones complejas, utilizándose como fuentes de datos. Algunos ejemplos de estos dispositivos son: 

- Sensores de temperatura: Un sensor de temperatura es un dispositivo que recopila información sobre la temperatura de un recurso y la cambia a una forma que puede ser entendida por otro dispositivo. Estos son categoría de sensores de uso común que detectan temperatura o calor y también mide la temperatura de un medio. 

- Sensores de presión: El sensor de presión es un instrumento que capta la presión y la transforma en una señal eléctrica donde la cantidad depende de la presión aplicada. Las piezas torneadas para sensores de presión y sensores de vacío son algunos de los principales sensores de presión utilizados en la automatización industrial. Algunas aplicaciones de estos sensores son: medir la presión por debajo de la presión atmosférica en un lugar determinado, instrumentación meteorológica, aeronaves, vehículos y cualquier otra maquinaria que tenga implementada la funcionalidad de presión, integrarse en sistemas para medir otras variables, como el flujo de fluido / gas, la velocidad, el nivel del agua y la altitud. 

83 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- Sensores de luminosidad: Un sensor de luminosidad es un dispositivo que permite conocer el grado de iluminación de un entorno concreto. Los sensores de luminosidad suelen estar conectados a otros dispositivos, que son los receptores de esta información respecto a la luminosidad ambiental detectada y, a partir de esta información, actúan de un modo u otro. Existen diferentes tipos de sensores de luminosidad. No obstante, en la mayoría de casos, un sensor de luminosidad está formado por dos partes claramente diferenciadas: un emisor de luz y un receptor de luz.El emisor de luz, como su nombre indica, emite luz. Esta luz, así como la luz ambiental preexistente, es la que es percibida por el receptor de luz. Al conocer la luz inicial que emite el emisor, en comparación con la luz total que recibe el receptor, se puede conocer la cantidad de luz ambiental exacta que hay en el entorno en el que se ha instalado el sensor de luz. 

- Sensores infrarrojos:  los sensores infrarrojos están diseñados especialmente para la detección, clasificación y posicionado de objetos; la detección de formas, colores y diferencias de superficie, incluso bajo condiciones ambientales extremas.  Se utilizan para medir la temperatura y detectar objetos calientes,  y además nos permiten la visión nocturna y la posibilidad de atravesar algunos objetos opacos para la luz visible. En el sector de la seguridad, estos dispositivos son un mecanismo utilizado en los diferentes detectores perimetrales, de movimiento, gas, inundación, etc, mientras que en el ámbito doméstico, por ejemplo, los sensores infrarrojos se utilizan en algunos electrodomésticos, como en los hornos microondas, para permitir la medición de la distribución de la temperatura en el interior. Estos dispositivos se usan también para el control climático de la casa y detectar oscilaciones de temperatura. Estos sistemas facilitan el ahorro de energía maximizando los recursos ayudando, de este modo, a la ralentización del cambio climático. En el campo de las ciencias médicas y biológicas se pretende desarrollar nuevos métodos de diagnóstico no invasores con procedimientos de reconocimiento mediante sensores infrarrojos, por ejemplo, los de mama y de músculos. Otra aplicación médica es la medición instantánea de la temperatura del cuerpo, es decir, como un termómetro remoto. 

- Sensores magnéticos: Un sensor magnético es un dispositivo que tiene como objetivo detectar campos magnéticos (atracción o repulsión de elementos) a través de imanes o energía eléctrica. Esta acción la produce por medio de láminas compuestas de pequeños imanes empotrados en una cápsula. el sensor magnético se acciona por medio de atracción o repulsión, ahora bien, la mediciones se pueden presentar por medio de la fuerza, la dirección o los fluidos. es el instrumento apropiado en la industria para ser utilizados en situaciones complejas, como por ejemplo; actividades relacionadas con químicos agresivos, humedad, rebosamiento de polvo, turbinas de vapor, altas temperaturas, etcétera. En todo el sector industrial tiene una incidencia significativa, pero en las empresas dedicadas a la fabricación de teléfonos móviles, su aplicación es fundamental para la elaboración de los chips. los sensores magnéticos se clasifican en lineales y digitales. 

84 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Los lineales son aquellos que poseen una salida de corriente eléctrica, que varía de acuerdo a la fuerza del cambio magnético externo. Por su parte en los sensores digitales cuando la fuerza del campo externo es mayor a un valor determinado, el sensor cambia de encendido a la condición de apagado. 

- Sensores acústicos: Los sensores acústicos son micrófonos pequeños que detectan o bien la presión de la onda de sonido (omnidireccional) o bien la velocidad de la onda de sonido (direccional). Estos sensores son sensibles a las presiones que emiten las ondas acústicas, y las transforma en pulsos eléctricos.  Por su parte, los sensores piezoeléctrico se utiliza a menudo para  el tacto, la vibración y las medidas de choque. 

- Sensores de desplazamiento e inclinación: Los sensores rotatorios o deslizantes, también conocidos como potenciómetros, son resistores eléctricos con un valor de resistencia variable. Por su parte los sensores de inclinación, son dispositivos que en función  de la inclinación,  permiten o no el paso de la corriente  funcionando como si fueran un interruptor. 

- Sensores de aceleración: Un acelerómetro es un dispositivo que mide la vibración o la aceleración del movimiento de una estructura. La fuerza generada por la vibración o el cambio en el movimiento (aceleración) hace que la masa “comprima” el material piezoeléctrico, generando una carga eléctrica que es proporcional a la fuerza ejercida sobre él. El hecho de que la carga sea proporcional a la fuerza y que la masa sea constante hace que la carga también sea proporcional a la aceleración [95]. 

- Sensores capacitivos: Se trata del sensor en el que están basadas las pantallas táctiles actuales. Estas pantallas tienen un conductor transparente donde circula corriente de forma constante, y está cubierto por una capa de aislamiento como el cristal. Cuando acercas el dedo, que también es conductor eléctrico, el contacto con la superficie de la pantalla genera una distorsión electrostática que el sensor es capaz de medir para determinar dónde estás pulsando. Es por esta necesidad de detectar una distorsión electrostática que las pantallas táctiles no las puedes utilizar con un puntero de plástico o con unos guantes que no estén especialmente preparados para ello. 

- Giroscopios: Un giroscopio es un dispositivo que utiliza la gravedad de La Tierra para ayudar a determinar la orientación. Los sensores giroscopios son dispositivos que detectan la velocidad angular, el cambio en el ángulo rotacional por unidad de tiempo. La velocidad angular generalmente se expresa en grados sobre segundos. Existen tres tipos básicos de giroscopios: giroscopios rotatorios (clásicos), giroscopios de estructura vibradora y giroscopios ópticos. 

85 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Su diseño consiste en un disco que rota libremente, llamado rotor, montado en un eje giratorio en el centro de una rueda más grande y estable. A medida que el eje da vueltas, el rotor permanece quieto para indicar la acción gravitacional central y, en consecuencia, la dirección hacia abajo. El giroscopio mantiene su nivel de efectividad al ser capaz de medir la tasa de rotación en torno a un eje particular. Usando los principios básicos del momento angular, el giroscopio ayuda a indicar la orientación. Los giroscopios están disponibles para medir la velocidad rotacional en una, dos o tres direcciones. Los giroscopios de tres ejes a menudo se implementan con acelerómetros de tres ejes para ofrecer un sistema de seguimiento del movimiento con un total de 6 grados de libertad [97]. 

- Sensores de proximidad: Los sensores de proximidad son sensores discretos que detectan cuando un objeto se ha acercado a la cara del sensor. Son capaces de detectar la presencia de objetos cercanos sin ningún contacto físico. Un sensor de proximidad emite un haz de radiación electromagnética y busca cambios en el campo o señal de retorno. Los sensores de proximidad se usan comúnmente en los teléfonos inteligentes para detectar toques accidentales en la pantalla táctil cuando se acercan a la oreja durante una llamada. Hay cuatro tipos fundamentales de sensores de proximidad: sensor de proximidad inductivo, sensor de proximidad capacitivo, sensor de proximidad ultrasónico y sensores fotoeléctricos u optoelectrónicos. 

- Sensores de corriente: Un sensor de corriente es un dispositivo que detecta y convierte la corriente en un voltaje de salida fácilmente medible, que es proporcional a la corriente medida. Existe una amplia variedad de sensores, cada uno adecuado para un rango de corriente específico y una condición ambiental. La selección de un sensor de corriente depende de los requisitos de magnitud, ancho de banda, precisión, robustez, aislamiento, costo, tamaño o costo. El valor producido se puede convertir a una forma digital para que lo use un sistema de control o monitoreo, o se puede mantener en forma analógica y mostrarse directamente mediante un instrumento de prueba actual. Una resistencia de detección de corriente es el sensor de corriente más utilizado. Puede considerarse un convertidor de corriente a voltaje, donde al insertar una resistencia en la ruta de la corriente, la corriente se convierte en voltaje de forma lineal. La tecnología utilizada por el sensor de corriente es importante ya que diferentes sensores pueden tener diferentes características para una variedad de aplicaciones [97]. 

86 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- Sensores de flujo: Un sensor de flujo (o medidor) es un dispositivo que mide la tasa de flujo de un fluido o gas lineal, no lineal, másico o volumétrico. Los sensores de flujo utilizan subsistemas eléctricos y mecánicos para medir los cambios en los atributos físicos del fluido y calcular su flujo. Los sensores de flujo son aplicables a gases con un rango de temperatura de funcionamiento de -20 °C a +400 °C, líquidos con un rango de temperatura de funcionamiento de -50 °C a +180 °C y pueden medir caudales y direcciones de 0 m/s a 100 milisegundo. Se implementan para detectar fugas, obstrucciones y roturas de tuberías. La medición del flujo es importante para el control de muchos tipos de equipos. Estos sensores se usan comúnmente en dispositivos médicos, sistemas HVAC, automóviles, fábricas de productos químicos, procesos industriales y aplicaciones de energía inteligente. Los factores que se deben considerar al seleccionar los medidores de flujo son la facilidad de calibración y mantenimiento, el tiempo promedio entre los historiales de fallas y la disponibilidad de repuestos en el sitio específico de la planta. 

- Sensores de humedad: Los sensores de humedad miden el nivel de líquido o la humedad relativa en un área dada, permiten controlar la humedad del aire y la temperatura. Las magnitudes medidas por el sensor de humedad se transforman en una señal eléctrica. Estos sensores pueden medir distintas capacidades físicas para obtener el grado de humedad [93] 

   - Sensores mecánicos: Son aquellos que aprovechan los cambios de dimensiones que sufren ciertos tipos de materiales en presencia de la humedad, por ejemplo: el cabello, fibras orgánicas o sintéticas. 

   - Sensores de conductividad: Ya que el agua es buena conductora de corriente es posible que a través de unas rejillas de oro circule una corriente eléctrica y según la medida de corriente es posible deducir el valor de la humedad. 

   - Sensores capacitivos: Se debe al cambio de la capacidad que sufre un capacitor o condensador en presencia de la humedad. 

   - Sensores infrarrojos: Lo que hacen es absorber parte de la radiación que contiene el vapor de agua 

   - Sensores resistivos: Basados en un principio de conductividad de la tierra, cuanta más cantidad de agua hay en la muestra, más alta es la conductividad de la tierra. 

87 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 52: Ejemplos de sensores generalistas [94] 

Este tipo de sensores suelen integrarse en dispositivos con mayor complejidad que permiten la transformación de la señal generada y la explotación de esta. 

Estos pueden aplicarse en múltiples áreas, algunas de las más desarrolladas actualmente son las siguientes. 

### **4.2. Sensores y dispositivos industriales** 

El área industrial es uno de los sectores donde podemos encontrar una mayor aplicación de la integración de sensores. Todas las cadenas de producción cuentan con sensores que permiten controlar el proceso. Los datos de estos dispositivos y sensores son integrados por medio del IoT y pueden ser empleados como fuentes de datos para el desarrollo de modelos de inteligencia artificial que permiten mejorar el rendimiento de la cadena productiva y facilitar la automatización de ciertos procesos. 

Algunos de los dispositivos y sensores utilizados en la industria son los siguientes: 

### **4.2.1. Sensores MEMS** 

MEMS son unas siglas que significan microelectromechanical systems, lo cual se traduce en sistemas microelectromecánicos. Su particularidad es que reúne sistemas de electromecánica miniaturizados al máximo, tanto que pueden integrarse dentro de un chip. Su complejidad es variable y podemos encontrar desde mecanismos muy simples a otros tan complejos como un reloj. El primero de ellos en implementarse al mercado fueron los acelerómetros, los se habían utilizado en los airbags de los automóviles y en los cartuchos de tinta de las impresoras hasta el momento. Se popularizaron con el auge de los smartphones después demostraron que los acelerómetros podían servir como sensores, aunque los que les brindaron popularidad fueron Nintendo en el desarrollo de la Nintendo Wii. Los MEMS son dispositivos sumamente complejos de diseñar y fabricar, ya que reúne varias disciplinas de ingeniería completamente dispares. En primer lugar se encuentran inte- 

88 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

grados en dispositivos electrónicos, son dispositivos mecánicos en los que además los materiales son importantes. Algunos incluso llegan a utilizar tecnologías complejas como la óptica y la mecánica de fluidos. Y pese a su enorme complejidad se encuentran en centenares de millones de dispositivos a precios que se suelen vender a céntimos. A día de hoy los dispositivos MEMS se utilizan para multitud de tareas y toman diferentes formas. 

Estos tienen numerosas aplicaciones que van desde la industria, el entretenimiento, los deportes hasta la educación. Por ejemplo, desencadenar despliegues de bolsas de aire o monitoreo de reactores nucleares. Se utiliza para medir la aceleración estática (gravedad), la inclinación de un objeto, la aceleración dinámica en una aeronave, el impacto de un objeto en un automóvil, la vibración de un objeto. Teléfonos celulares, lavadoras o computadoras. 



Ilustración 53: Sensores MEMS [98] 

### **4.2.2. Sensores de par** 

Los sensores de par miden la fuerza de torsión a la que se somete un eje durante las diferentes fases de su funcionamiento, bien sea en arranque, dinámico o parada. Se suele ensayar y estudiar en elementos de potencia como motores, generadores, alternadores, etc. Un transductor de par proporciona una variación mecánica en una eléctrica, en este caso una torsión se traduce en una variación de voltaje. 

Los tipos de sensor de par son diferentes, pero por tecnología se dividen en estáticos o dinámicos, a su vez, estos últimos se dividen en sensores de par dinámicos sin escobillas o anillos rozantes y sensores de par con escobillas o anillos rozantes. Los sensores de par tienen una amplia gama de aplicaciones, industrias de fabricación y automotriz. Los medidores de par se utilizan en plataformas de prueba y plataformas de control de producción, así como en sistemas de ensamblaje o atornillado. 

89 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 54: Ejemplo de sensores de par 

### **4.2.3. Sensores de visión** 

Las cámaras inteligentes pueden considerarse como uno de los sistemas con mayor aplicación en el área industrial. Alrededor de los datos obtenidos por las mismas se desarrolla una de las áreas de aplicación de inteligencia artificial más extensas como es los sistemas de visión industrial. 

Se pueden definir los sistemas de visión industrial como un campo de la Inteligencia Artificial que, mediante la utilización de las técnicas adecuadas, permite la obtención, procesamiento y análisis de cualquier tipo de información especial obtenida a través de imágenes digitales. 

Hoy en día estos sistemas de visión industrial son altamente importantes, y tienen una gran demanda en el sector industrial, ya que facilitan las tareas con gran eficiencia y calidad. Con la visión artificial se puede realizar: 

- Automatizar tareas repetitivas de inspección realizadas por operadores. 

- Realizar controles de calidad de productos que no era posible verificar por métodos tradicionales. 

- Realizar inspecciones de objetos sin contacto físico. 

- Realizar la inspección del 100% de la producción (calidad total) a gran velocidad. 

- Reducir el tiempo de ciclo en procesos automatizados. 

- Realizar inspecciones en procesos donde existe diversidad de piezas con cambios frecuentes de producción. 

90 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Esto se debe a sus amplias características y funcionalidades, podemos lograr los requerimientos necesarios dentro de la industria. Las características principales con las que cuenta el sistema de visión artificial son: 

- Analizan luz o color reflejado: Miden nivel de luz 

- Detectan bordes y formas 

- Analizan color 

- Actúan sin contacto: No deforman el material 

- Se puede analizar un objeto en movimiento 

- Son automáticos: Alta velocidad de procesado 

- Flexibles: basados en software 

Algunas de las aplicaciones donde podemos encontrar estos sistemas de visión industrial son: 

- Sistema de presencia-ausencia: Inspección de un área donde entre otras funciones, puede definirse en cada imagen las regiones de interés (ROI) y en ellas buscar objetos, medir distancias y reconocer patrones para verificar procesos. 

- Sistemas de pick-up and place: Localización de la posición de un objeto detectando las coordenadas del mismo en el espacio para recogerlo y desplazarlo al lugar deseado 

- Sistemas de control de calidad por visión artificial: A través de los sistemas de visión artificial se verifica el cumplimiento de los requisitos y especificaciones técnicas de un objeto a partir de un patrón dado. 

- Visión 3D y control dimensional mediante la obtención de las magnitudes físicas de un objeto, para verificar que se corresponden con el patrón exigido. 



Ilustración 55: Visión 3D y control dimensional [99] 

91 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- Sistemas de clasificación industrial: Asignar un objeto a su clase a la que pertenece mediante la extracción y procesado de sus características visuales. 

Los sistemas de visión artificial efectúan tareas repetitivas con precisión y rapidez y permiten trabajar fuera del espectro visible distinguiendo detalles no visibles por el ojo humano y aportando numerosos beneficios. 

### **4.3. Sensores y dispositivos biomédicos** 

Los sensores disponibles en el área de la medicina son un área en expansión en la cual cada vez encontramos un mayor número de dispositivos disponibles para el público general y no de uso limitado a especialistas. Algunos de los sensores disponibles en la actualidad son los siguientes 

### **4.3.1. Sensor GSR** 

Los sensores GSR (Galvanic Skin Response, o respuesta galvánica de la piel), miden cambios en la actividad de las glándulas sudoríparas que reflejan la intensidad de nuestro estado emocional, también conocido como excitación emocional. 

La conductancia de la piel ofrece información directa sobre la regulación emocional autónoma, ya que no está bajo control consciente. Por ejemplo, si estás asustado, contento, agitado o con cualquier respuesta emocional relacionada, experimentaremos un aumento en la actividad de las glándulas sudoríparas ecrinas que el sensor puede detectar a través de los electrodos y transmitir al dispositivo maestro. 

La señal GSR es muy fácil de registrar: en general sólo son necesarios dos electrodos colocados en el segundo y tercer dedo de una mano. La variación de una corriente aplicada de bajo voltaje entre los dos electrodos se utiliza como medida de la actividad electrodérmica (EDA). Recientemente, se han desarrollado nuevos dispositivos médicos comerciales cada vez más portátiles (brazaletes, relojes) por lo tanto dicha medida también se puede utilizar en actividades de investigación en el campo de la neurociencia en entornos fuera del laboratorio [100]. 



Ilustración 56: Sensor de respuesta galvánica de la piel 

92 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

### **4.3.2. Sensor de ritmo cardiaco** 

También conocido como monitor de ritmo cardíaco, es un dispositivo de monitoreo personal que permite al usuario rastrear y mostrar su ritmo cardíaco en tiempo real o con fines de estudio [101]. 

Hay dos formas (óptica y eléctrica) de que este sensor monitoree tu ritmo cardíaco que son: 

- Eléctrico: consta de 2 elementos que son un monitor y un receptor. Cuando se detecta un latido cardíaco, se transmite una señal de radio o una señal codificada, que el receptor utiliza para mostrar / determinar la frecuencia cardíaca actual. 

- Óptico: utiliza una luz que brilla a través de la piel humana para luego medir la cantidad de luz que se refleja. Los reflejos de luz variarán a medida que los pulsos de sangre debajo de la piel pasen la luz, que luego se interpretan como latidos cardíacos. Este tipo de sensores se utilizan en los pulsimetros de dedo 



Ilustración 57: Sensor de frecuencia cardiaca [102] 

### **4.3.3. Sensor EMG** 

EMG es sinónimo de electromiograma, que es la medición de potenciales eléctricos creados por la contracción de los músculos. Internamente, los músculos generan tensiones alrededor de 100mV cuando se contraen. A medida que las señales eléctricas viajan a través de los nervios hacia las uniones neuromusculares, se puede medir el cambio en los potenciales eléctricos (voltaje).El EMG puede ser monitoreado a través de electrodos insertados dentro de los músculos (electrodos intramusculares) o a través de electrodos en la superficie de la piel sobre el músculo (electrodos superficiales). El EMG es usado por científicos para estudiar el sistema neuromuscular, por médicos para el diagnóstico de enfermedades neuro musculares, y por fisioterapeutas para monitorear la activación de músculos de un paciente 

La medición de la actividad muscular se ha utilizado tradicionalmente en la investigación médica mediante la detección de la electromiografía (EMG). Sin embargo, con la aparición de micro-controladores más pequeños pero más potentes y circuitos integrados, los circuitos y sensores EMG se pueden utilizar en una variedad de aplicaciones. Actualmente este tipo de dispositivos se encuentran comercializados para su utilización con controladoras como Arduino o RaspberryPi asi como integradas en dispositivos de uso generalista como relojes inteligentes o pulseras de actividad. 

93 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 58: Ejemplo sensor EMG 

### **4.3.4. Sensores ECG** 

Un electrocardiograma registra las señales eléctricas del corazón.  Los electrocardiogramas (también llamados ECG) con frecuencia se realizan en el consultorio del médico, en una clínica o en una habitación de hospital. Las máquinas de electrocardiograma son un equipo estándar en los quirófanos y las ambulancias. Algunos dispositivos personales, como los relojes inteligentes, ofrecen control de electrocardiograma. El sensor ECG mide las señales eléctricas producidas por el cora- zón. La gráfica de ECG, que se muestra en el ordenador o registrador de datos, ilustra gráficamente el latido del corazón. 



Ilustración 59: Ejemplo de medida de ECG [103] 

94 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

### **4.3.5. Sensor de huella digital** 

Al igual que los sensores ópticos, los escáneres capacitivos de huellas digitales generan una imagen de las crestas y valles que forman una huella digital. Sin embargo, en lugar de detectar la impresión con luz, los condensadores usan corriente eléctrica. Las matrices de circuitos de pequeños condensadores recopilan datos sobre una huella digital que, cuando se conectan a placas conductoras en la superficie del escáner, se pueden utilizar para rastrear los detalles de una huella digital. 



Ilustración 60: Sensor de huella digital 

### **4.3.6. Sistemas de imagen médica** 

En la actualidad existen múltiples sistemas y técnicas utilizados para obtener imágenes médicas. Este tipo de datos son de gran utilidad en la práctica clínica pero también en el área de investigación, donde se extrae y magnifica la información obtenida a partir de estos datos. 

Dentro de los sistemas de imagen medica podemos encontrar dos grandes clasificaciones atendiendo al método de obtención de las imágenes: 

- Técnicas basadas en radicación ionizante. La radiación ionizante es un tipo de energía liberada por los átomos en forma de ondas electromagnéticas o partículas: 

   - Rayos X: Los rayos X (RX) son una forma de radiación electromagnética, de una frecuencia muy superior a la luz visible. Un tubo de RX lanza un haz de RX a través de un cuerpo humano. Al otro lado del cuerpo, un receptor sensible a los RX recoge la radiación transmitida. Dependiendo de las diferencias en la absorción de los RX, la cantidad de radiación que atraviesa cada tejido varía formando una imagen en el receptor. 

   - Tomografía computerizada: La tomografía computarizada es una técnica asistida por computador que permite generar una imagen de una sección o plano cualquiera del sujeto. Se basa en tomar múltiples imágenes del sujeto a distintos ángulos, moviendo mecánicamente la fuente de radiación y/o el receptor. Las imágenes se procesan digitalmente para obtener un corte o sección del sujeto. 

95 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

   - Medicina Nuclear: Se introduce una sustancia radiactiva (radiofármaco) en el paciente, el cual se fija en un órgano concreto o células específicas desde dónde emite rayos gamma. Estos rayos pueden ser visualizados a través de cámaras especialmente diseñadas para captar este tipo de radiación. 

- Técnicas no ionizantes 

   - Resonancia magnética nuclear: La RMN utiliza el magnetismo para producir imágenes detalladas del cuerpo en cualquier plano. Todos los átomos del cuerpo contienen átomos de hidrógeno en distintas composiciones. Estos átomos son afectados por un campo magnético que alinea los átomos de hidrógeno de manera paralela al campo. Tras esto se aplica una señal de radio frecuencia que excita estos átomos y los hace resonar. Al detenerse esta señal los átomos dejan de resonar emitiendo una señar de radiofrecuencia característica. 



Ilustración 61: Ejemplo de imágen producida por resonancia magnética [104] 

- Ultrasonidos: Las ondas sonoras de alta frecuencia son reflejadas de distinta manera por cada tipo de tejido del cuerpo humano. Al igual que el sonar, un haz de ultrasonidos es enviado al cuerpo y su reflejo (eco) es medido, dando información de cada cambio de tejido. La información se adquiere a través de cortes en forma de abanico (2D) o mediante un barrido en 3D 

### **4.3.7. Dispositivos Wereables** 

Gracias a la cuarta revolución industrial, muchos de estos sensores han sido democratizados y se encuentran al alcance del público general al integrarse dentro de dispositivos de uso cotidiano, como Smart watches, pulseras de actividad, o incluso en la ropa. Estos dispositivos se conocen comúnmente como wereables y cada vez están más integrados en nuestra vida diaria. Wearable hace referencia al conjunto de aparatos y dispositivos electrónicos que se incorporan en alguna parte de nuestro cuerpo interactuando de forma continua con el usuario y con otros dispositivos con la finalidad de realizar alguna función concreta, relojes inteligentes o smartwatchs, zapatillas de deportes con GPS incorporado y pulseras que controlan nuestro estado de salud son ejemplos entre otros muchos de este género tecnológico que se halla poco a poco más presente en nuestras vidas. 

96 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

La tecnología wearable se halla presente en un extenso abanico de campos que satisfacen nuestras necesidades, con la finalidad de mejorar nuestra calidad de vida estando muy presente en la salud de los pacientes, la seguridad de las personas que se exponen a determinados peligros en su trabajo diario, el adiestramiento de los atletas que se preparan para una competición etc… 

#### **Gafas Inteligentes** 

Google fue pionero en el desarrollo de esta tecnología al lanzar al mercado  las primeras lentes inteligentes de esta compañía que son controladas a través de instrucciones pronunciadas con nuestra voz disponiendo de una pequeña pantalla donde se muestra la información solicitada. Con estas gafas wearables podremos hacer fotografías y grabar videos en alta definición de todo aquello que estemos viendo y reproducirlos en otro instante, podemos consultar nuestro correo electrónico, el tráfico, las últimas noticias o la ruta más corta para llegar a tu destino, traducir a cualquier idioma los carteles que te halles por la calle o incluso realizar una videoconferencia en directo [105]. 



Ilustración 62: Gafas inteligentes de Google [105] 

#### **Accesorios y complementos** 

Relojes, anillos y pulseras que se encienden al identificar tu huella digital, estos complementos digitales guardan toda la información sobre tu modo de vida como los kilómetros que andas a lo largo del día, el ritmo cardíaco, los ciclos de sueño… Toda esta información puede ser sincronizada con otros dispositivos electrónicos ya que se trata de dispositivos conectados. Generalmente este tipo de dispositivos cuentan con modelos de inteligencia artificial integrada que les permiten analizar los datos que recogen in situ y proporcionar nuevos datos de utilidad al usuario, como por ejemplo la calidad del sueño, estado de salud o recomendaciones sobre actividad física. 

97 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 63: Ejemplos de dispositivos wereables [106] 

#### **Industria Textil** 

En la actualidad existen multitud de sensores integrados sobre prendas de ropa que nos permiten obtener datos y extraer información de los mismos. Por ejemplo, prendas infantiles que señalan y mandan una señal a tu smartphone cuando tu bebe posee fiebre, ropa de deporte que te ayuda a realizar los movimientos adecuados mientras que aprendes a jugar al golf, sudaderas con leds que te alumbran en las calles oscuras mientras que haces running y que al mismo tiempo contabiliza los kilómetros recorridos, el ritmo cardíaco, las calorías quemadas y el desempeño durante todos los días que practicas deporte. 

### **4.4. Sensores y dispositivos de domótica** 

En el área de la domótica podemos encontrar una gran área de aplicación de los sensores que permiten captar información sobre el entorno. De esta forma, la industria de la domótica ha conseguido revolucionar una gran diversidad de sectores, que van desde la arquitectura, hasta el sector automotriz, el de climatización e, incluso, ayuda a preservar la seguridad en diferentes sitios. 

Existen varios tipos de sensores para domótica que detectan y emiten distintas señales en la vivienda. Estos funcionan con contacto directo, sin contacto, pudiendo ser iónicos, ópticos, mecánicos o eléctricos. Asimismo, la mayoría de dichas señales se transmiten a tu móvil o dispositivo de tu elección, de tal manera que puede alertarte de existir alguna situación fuera de lo normal. 

Algunos de los sensores más utilizados en domótica son: 

- Sensor de climatización: Por medio de este tipo de sensor para domótica se controla la temperatura en los diferentes ambientes dentro del domicilio, en concreto, el dispositivo capta los grados externos, regulando el sistema operativo interno. 

- Sensor detector de humos: el detector de humos es capaz de identificar la acumulación anormal de este agente en los diferentes espacios. 

98 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- Sensores de seguridad: Este tipo de sensores para domótica captan el movimiento de las personas y, normalmente, estos vienen integrados con un set de cámaras que monitorean los accesos a las instalaciones. 

- Sensor de gas: Un sensor de detección de gas sirve para alertar, con la ayuda de un sistema de alarma técnico inteligente, de las posibles fugas de gas ocasionadas por los distintos aparatos del hogar que lo utilicen. La captación de este tipo de sensor domótico trabaja de forma iónica u óptica. 

- Sensor de humedad: Permite controlar la humedad de los diferentes espacios 

- Sensor de iluminación: A través de este dispositivo obtienes la regulación de todo el sistema de luz, generando un ahorro energético significativo 

Todos estos sensores pueden integrarse con dispositivos inteligentes que permiten analizar los datos obtenidos a través de los mismos así como controlarlos de manera eficiente, facilitando la gestión del usuario final. 

Algunos ejemplos de inteligencias artificiales que permiten la integración con estos tipos de dispositivos son los asistentes personales que podemos encontrar embebidos dentro de nuestros smarphones o como dispositivos independientes. En el mercado existe cada vez una oferta mayor de este tipo de asistentes aunque la mayor parte del nicho de mercado esta ocupado por las grandes multinacional como Google, Apple, Samsung, Microsoft y Amazon. 

#### **Google Assistant** 

Google Assistant o Asistente de Google, es un asistente virtual creado por la empresa del buscador. Este asistente funciona principalmente por voz, de manera que vas a poder hacerle preguntas y él te dirá las respuestas. 

El asistente de Google puede ser utilizado en varios sitios. Por ejemplo, vas a poder encontrarlo en un teléfono móvil Android, o incluso en iOS dentro de la aplicación de Google. También está integrado en otros tipos de dispositivos, desde televisores a altavoces inteligentes, incluyendo auriculares, y todos los dispositivos conectados a Internet en los que veas que en la caja hay una insignia con el logo del asistente. se trata de un asistente que vas a encontrar en varios tipos de dispositivo, permitiendo controlar unos con otros. Además, en todos los dispositivos se utilizará con los mismos comandos de voz. 

99 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 64: Google Home 

#### **Siri** 

Siri es la asistente personal controlada por voz de Apple y ella, o él, ha existido durante varios años. El asistente apareció por primera vez en el iPhone 4S, pero Siri también está disponible en iPad, iPod touch, Apple Watch, AirPods, HomePod y Mac. 

Siri está diseñado para ofrecer una forma fluida de interactuar con el resto de productos de apple al hablar con ella. Puede hacerle preguntas, decirle que le muestre algo o darle órdenes para que las ejecute en su nombre, con las manos libres. 

Siri tiene acceso a todas las demás aplicaciones integradas en los dispositivos Apple (correo, contactos, mensajes, mapas, Safari, etc.) y recurrirá a esas aplicaciones para presentar datos o buscar en sus bases de datos siempre que lo necesite. 

#### **Cortana** 

Cortana es el asistente virtual de Windows que te ayudará a acceder a tus intereses, lugares favoritos, correos, entre otros, por medio de comando de voz. Al igual que el resto de asistentes su integración se limita a los dispositivos de la compañía por lo que en este caso contara con una menor disponibilidad de dispositivos ya que Microsoft no tiene un catálogo de productos destinados a la domótica tan extenso como algunos de sus competidores. 

#### **Bixby** 

Bixby es un asistente virtual desarrollado por Samsung Electronics. El 20 de marzo de 2017, Samsung anunció el asistente digital de voz llamado “Bixby”. Bixby se presentó junto con el Samsung Galaxy S8 y S8+. 

Este asistente virtual aprende sobre tus gustos y rutinas, mediante la recopilación de información basada en tus preferencias y tu patrón de uso. 

100 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

A diferencia de Siri y el Asistente de Google, Bixby está más enfocado en hacer cosas dentro de su teléfono: cambiar configuraciones, enviar mensajes de texto, tomar notas, configurar recordatorios y alarmas. No se centra en responder consultas basadas en la web, por lo que muchos usuarios prefieren Google Assistant: ofrece lo mejor de ambos mundos. 

#### **Alexa** 

Alexa es el asistente virtual controlado por voz creado por Amazon, y lanzado en noviembre de 2014 junto a su línea de altavoces inteligentes Echo. Su nombre fue elegido por tener una consonante fuerte al principio e incluir una x, algo que haría que el asistente reconociese más fácil su nombre, y también en honor a la Biblioteca de Alejandría. 

El funcionamiento de Alexa es muy parecido al de otros asistentes como Google Assistant, Siri y Cortana. Empiezas invocándolo diciendo su nombre, momento en el que el altavoz o dispositivo en el que esté integrado se pondrá a escuchar. Entonces debes decirle un comando con tu voz, y el asistente reconocerá lo que le preguntas y te dirá una respuesta. 

En un principio, el asistente estaba únicamente vinculado a los altavoces inteligentes creados por Amazon. Pero a los pocos meses se abrió su SDK para que otros fabricantes y desarrolladores pudieran empezar a trabajar sobre él. Desde entonces, el asistente ha sido incluido en una gran cantidad de dispositivos, desde relojes de pared hasta microondas. 

Gracias a esa capacidad de expansión, Alexa se ha convertido en uno de los asistentes de referencia. Amazon incluso llegó a cerrar un acuerdo con Microsoft para integrar Alexa dentro de Cortana, y poder acceder así a millones de PCs y portátiles en todo el mundo. Sin embargo este acuerdo llego a su fin en octubre de 2021, ya que Microsoft parece seguir centrada en orientar el uso de Cortana hacia el software empresarial, ya sea por medio de PC o de dispositivos móviles, sobre todo gracias a la integración con Microsoft 365 y Outlook, dejando a un lado los usos personales. 



Ilustración 65: Altavoz inteligente de Alexa 

101 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Las funciones de Alexa dependen de dos elementos claves. Por una parte están los comandos de voz que integra, y con los que puedes realizarle una gran variedad de peticiones. Y luego están las skills, que son complementos que le puedes instalar para añadirles aún más funcionalidades. 

Las Alexa Skills son el equivalente a aplicaciones de terceros que hay disponibles para Alexa. Con ellas se pueden ampliar las posibilidades del asistente, añadiendo más comandos de voz o diferentes fuentes con las que hacer más completas sus funcionalidades. A nivel mundial hay decenas de miles de skills diferentes, e incluso puedes crear tu propia skill. [107] 

_Blueprints de skills de Alexa_ , es una página web diseñada para ayudarte a crear tus propias skills sin saber programar y sin tener ningún tipo de conocimiento técnico. Lo hace mediante planos, ya que plano es lo que significa la palabra blueprint. La web te ofrece distintos planos, y puedes utilizarlos para crear tu skill. 

#### <u>https://blueprints.amazon.es</u> 

Puedes probar a construir tu propia skill de Alexa para comprobar la flexibilidad que aportan los asistentes personales, sin necesidad de tener conocimientos de programación. 

Las plantillas están creadas para poder crear las skills desde cero. Esto quiere decir que no son skills funcionales, sino que funcionan como una especie de guías en las que tienes los diferentes campos donde puedes añadir tu contenido, y solo tienes que rellenarlas dependiendo de lo que quieras hacer. 

Las plantillas están diseñadas para que crear una skill sea lo más sencillo del mundo, y no vas a tener que hacer nada ni remotamente complejo para crearlas. Eso sí, no son skills demasiado complejas, sino unas básicas que pueden ayudarte en tu día a día. Como punto de partida para algunas tareas no está mal. 

Alexa también ofrece la posibilidad de crear skills mas complejas aprovechando el Alexa Skills Kit (ASK). Este es un conjunto de herramientas, documentación, muestras de código y API en self-service con el que puedes añadir Skills a Alexa de forma rápida y sencilla. El ASK permite a diseñadores, desarrolladores y marcas crear Skills atractivas y llegar a los consumidores. Con este kit, puedes aprovechar el conocimiento y la innovación de Amazon en el sector del diseño de voz. 

<u>https://developer.amazon.com/en-US/alexa/alexa-skills-kit</u> 

102 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

## **5. Interacción computador-humano** 

_“Las interacciones con los sistemas han evolucionado desde los primeros PC que solo contaban con un teclado y una pantalla hasta los paradigmas actuales de iteración. En los últimos años abriendo la puerta a nuevas vías de comunicación con los sistemas adaptadas a los avances de la tecnología y la comodidad del usuario.”_ 

La disciplina que estudia cómo las personas interactúan con las computadoras y hasta qué punto las computadoras se desarrollan para interactuar con las personas se llama Interacción Humano-Computadora. HCI consta de tres componentes: los usuarios, los ordenadores y la interacción entre ellos. 

La Interacción Humano-Computadora se convirtió oficialmente en una disciplina con el advenimiento de la computadora personal. Con el primer Macintosh, IBM PC 5150 y Commodore 64 utilizados en la oficina, la gente empezó a darse cuenta de cómo esta transición afectará no sólo a su trabajo sino a sus vidas en general. Los PCs fueron lanzados con muchas nuevas características como procesadores de texto, facilidades de juego y ayudas de contabilidad. Con el tiempo, su nivel de sofisticación aumentó hasta el punto en que el objetivo era hacer que la interacción hombre-computadora se asemejara a la interacción entre humanos, de la forma más natural y sin fisuras posible. 

HCI es un dominio interdisciplinario que abarca disciplinas como la informática, la ingeniería de los factores humanos, la inteligencia artificial, la lingüística, la filosofía, la antropología y la ciencia cognitiva. 

En los últimos cinco años, HCI ha pasado rápidamente de estudiar la interacción con los ordenadores de sobremesa a centrarse casi exclusivamente en los dispositivos móviles. 

En la Interacción Humano-Computadora, las palabras clave son usabilidad, seguridad y funcionalidad. Además, para producir sistemas con estas características, la investigación de HCI debe ser consciente de las siguientes cosas: 

- Investigar y comprender los factores organizacionales, sociales y psicológicos que determinan cómo las personas utilizan la tecnología debe ser el punto de partida de cualquier proyecto de HCI. Es un proceso de aprendizaje continuo que se desarrolla a lo largo de la duración del proyecto. 

103 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- La segunda parte más importante de la investigación de HCI es el enfoque centrado en las personas. John M. Carroll [109], autor y fundador del campo de la interacción hombre-computadora, escribe que HCI se está centrando cada vez más en las personas. Se ha expandido para crear soluciones para proyectos como la accesibilidad para las personas mayores, los discapacitados cognitivos y físicos. En esta fase tan evolucionada, los diseñadores de interacción ya no están en el negocio del diseño, sino en el negocio de las personas. En última instancia, el Diseño de Interacción Humana consiste en crear sistemas y marcos que mejoren la vida de las personas [110]. 

- Crear una interacción del sistema de usuario que sea efectiva, eficiente y segura. 

Las interacciones con los sistemas han evolucionado desde los primeros PC que solo contaban con un teclado y una pantalla hasta los paradigmas actuales de iteración. En los últimos años abriendo la puerta a nuevas vías de comunicación con los sistemas adaptadas a los avances de la tecnología y la comodidad del usuario. La iteración de los sistemas de gestión de los computadores ha evolucionado hacia nuevos paradigmas: 

- Primeras interfaces de usuario: Texto, teclado y pantalla 

- Evolución de los sistemas operativos: Menús y navegación 

- Integración de tecnologías táctiles: Manipulación directa 

- Procesado del lenguaje natural: Control por voz 

- Nuevos paradigmas 

### **5.1. Interfaces de usuario** 

En el campo de la interacción humano-computadora, una interfaz de usuario (UI) es el espacio donde ocurren las interacciones entre humanos y máquinas. El objetivo de esta interacción es permitir la operación y el control efectivos de la máquina desde el extremo humano, mientras que la máquina retroalimenta simultáneamente información que ayuda en el proceso de toma de decisiones de los operadores. 

Generalmente, el objetivo del diseño de la interfaz de usuario es producir una interfaz de usuario que haga que sea fácil, eficiente y agradable (amigable para el usuario) operar una máquina de la manera que produce el resultado deseado (es decir, máxima usabilidad). Esto significa que el operador necesita proporcionar una entrada mínima para lograr la salida deseada, y también que la máquina minimiza las salidas no deseadas para el usuario. 

104 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Las interfaces de usuario compuestas (CUI) son UI que interactúan con dos o más sentidos. La CUI más común es una interfaz gráfica de usuario (GUI), que se compone de una interfaz de usuario táctil y una interfaz de usuario visual capaz de mostrar gráficos. Cuando se agrega sonido a una GUI, se convierte en una interfaz de usuario multimedia (MUI). Hay tres categorías amplias de CUI: estándar, virtual y aumentado. CUI estándar utiliza dispositivos de interfaz humana estándar como teclados, ratones y monitores de computadora. Cuando el CUI bloquea el mundo real para crear una realidad virtual, el CUI es virtual y utiliza una interfaz de realidad virtual. Cuando el CUI no bloquea el mundo real y crea realidad aumentada, el CUI se aumenta y utiliza una interfaz de realidad aumentada 

### **5.1.1. Graphical User Interface (GUI)** 

Este software se aplica con elementos gráficos de control e imágenes que se toman como referencia de objetos de la realidad. En este sentido, se suele recurrir al ratón y al teclado como dispositivos de control, aunque también ya es muy común que entren pantallas táctiles. Aquí los iconos también se introducen en el mundo digital, al igual que el escritorio la papelera. El diseño gráfico se basa en el diseño de una oficina tradicional, el resultado es que todos los elementos se puedan identificar de forma sencilla, resultando más intuitivo en comparación con la lista de comandos de una Command Line Interface. Así, los usuarios con menor experiencia también logran entender las funciones de los iconos con mayor rapidez, estos símbolos son un factor tanto para las user interfaces como para las GUI. 

Las interfaces clásicas de comunicación con los computadores se mantienen a día de hoy contando con evoluciones tecnológicas, por ejemplo, la línea de comandos es la primera forma de interacción humano-computadora. Esta se ha mantenido a pesar de los grandes cambios gráficos dentro de los sistemas ya que permite dar instrucciones a la computadora por medio de texto simple. 

Otro elemento que se ha mantenido desde el origen de los primeros sistemas operativos, contando con actualizaciones acorde a la tecnología disponible son los sistemas de navegación y menús. Estos hacen posible mantener una organización y realizar búsquedas más rápidas. En la actualidad, existen infinidad de modelos de diseños creados según la necesidad. Las interfaces de usuario se componen de una o más capas, incluida una interfaz hombre-máquina (HMI) que conecta las máquinas con hardware de entrada física, como teclados, ratones o almohadillas de juegos, y hardware de salida, como monitores de computadora, altavoces e impresoras. 

105 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Algunos de los elementos que se utilizan en la actualidad y que forman parte de los sistemas de interacción clásicos son los siguientes: 

#### **Pantallas** 

Las pantallas son uno de los elementos de comunicación originales que mayor implantación tiene a día de hoy. La mayor parte de dispositivos electrónicos destinados a usuarios cuentan con pantallas como elemento de comunicación. Estas han evolucionado a lo largo de los años, desde los monitores monocromáticos de los años ochenta, diseñados únicamente para texto, ya que no incorporaban modo gráfico hasta las pantallas que encontramos en la actualidad. Algunas de sus características mas significativas son las siguientes: 

- Mejora de calidad: Las pantallas actuales cuentan con tecnología con grandes escalas de resolución llegando hasta 4k o UltraHD y 8k. La resolución de una pantalla viene definida por el número de pixels que es capaz de mostrar. 

- Pantallas táctiles: Tecnología plenamente integrada en la actualidad permite la manipulación mediante el toque directo sobre la superficie y actúa como dispositivo de entrada y salida. Este tipo de interfaz es muy utilizado en todo tipo de dispositivos electrónicos. Detras de este tipo de pantallas podemos encontrar distintos tipos de tecnologías como pueden ser las pantallas táctiles resistivas, capacitivas, de tecnología infrarroja y de imágenes ópticas. 

- Simulación de papel: Las pantallas de tinta electrónica están principalmente pensadas para libros electrónicos, ya que facilitan la lectura prolongada y presentan una autonomía muy superior a otros tipos de tecnologías. Sin embargo, esta cuenta con un importante obstáculo, su tasa de refresco, que hace que su utilización sea inadecuada para contenidos de vídeo e incómoda para pensar en ellos como soluciones de productividad. 



Ilustración 66: Pantalla de tinta electrónica plegable [111] 

106 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- Pantallas flexibles: Las pantallas OLED están hechas de materiales orgánicos que emiten luz cuando la electricidad pasa a través de ellas. No requieren retroiluminación para funcionar y, como resultado, se pueden hacer lo suficientemente delgadas hasta el punto en que se vuelven flexibles, formando la base de pantallas flexibles. Este tipo de tecnología esta teniendo una acogida paulatina en el mercado, donde podemos encontrar algunos modelos de smartphones y tablets que incorporan esta tecnología. 

#### **Teclados** 

Periférico de entrada inspirado en el teclado de las máquinas de escribir, permite interactuar con la computadora en modo texto. Estos dispositivos tienen tendencia a ser miniaturizados, además han emergido tecnologías como teclados flexibles o teclados láser ‘sensorboard’. En la actualidad existen dos tipos de teclado de computadora: los mecánicos y los de membrana, y pueden tener cables o ser inalámbricos. En los mecánicos cada tecla funciona de forma independiente, mientras que los de membrana tienen todas las teclas interconetadas. El diseño QWERTY es el más usado en los teclados de computadora. Fue creado para aprovechar las limitaciones de las máquinas de escribir que existían a principios de los setentas. 



Ilustración 67: Teclado infrarrojo 

### **5.1.2. Voice User Interface** 

El control de dispositivos por voz ha avanzado a la par que ha avanzado el campo de procesado de lenguaje natural dentro de la inteligencia artificial. En la actualidad existen múltiples dispositivos que cuentan con interfaces de voz para interactuar con ellos a través de comandos, un ejemplo es Apple con Siri, Amazon con Alexa, Microsoft con Cortana o la búsqueda de Google mediante voz. De esta forma, se puede acceder a algunas aplicaciones de un modo más efectivo y garantizando una mayor accesibilidad. Una VUI acepta la entrada del usuario a través de la voz, la procesa y luego proporciona una salida basada en la voz, que puede ir acompañada de texto, gráficos o video en la pantalla. Una de las grandes ventajas de la tecnología VUI es que permite a los usuarios un control completo de la tecnología manos libres. Para hacerlo posible se utiliza una combinación de tecnologías de Inteligencia Artificial (IA), incluido el reconocimiento de voz automático, el reconocimiento de entidad de nombre y la síntesis de voz, entre otros. 

107 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Por su propia naturaleza, las VUI pueden estar contenidas en dispositivos o dentro de aplicaciones. La infraestructura de back-end, incluidas las tecnologías de inteligencia artificial utilizadas para crear los componentes de voz del VUI, a menudo se almacenan en una nube pública o privada donde se procesa la voz del usuario. En la nube, los componentes de IA determinan la intención del usuario y devuelven una respuesta determinada al dispositivo o aplicación donde el usuario está interactuando con la VUI. Para ello la tecnología empleada dentro de la inteligencia artifcial se basa en dos pilares: [[Índice_Procesamiento del Lenguaje Natural|Procesamiento del Lenguaje Natural]] y la tecnología speech to text. 

- PLN: Estas siglas hacen referencia al Procesamiento de Lenguaje Natural (PLN), la denominación que recibe un subcampo de la informática y la inteligencia artificial relacionada con las interacciones entre las computadoras y los lenguajes humanos. Se utiliza para aplicar algoritmos de aprendizaje automático al texto y al habla. Entre otras aplicaciones, se pueden crear sistemas como reconocimiento de voz, resumen de documentos, traducción automática, detección de correo no deseado, reconocimiento de entidades con nombre, respuesta a preguntas, autocompletado, escritura predictiva, entre otros. 

- Speech To Text: es el proceso por el cual las palabras habladas se convierten en textos escritos. Este proceso también se suele llamar reconocimiento de voz. Aunque estos términos son casi sinónimos, el reconocimiento de voz a veces se usa para describir el proceso más amplio de extracción de significado del habla, es decir, la comprensión del habla. 

### **5.1.3. Natural User Interface** 

En la búsqueda de una interacción humano-computadora más natural ha llevado a los investigadores a diseñar interfaces con capacidad de reconocer gestos humanos. Con Natural User Interface, la comunicación con la computadora se da de forma más intuitiva, puede ser considerada como una evolución de la interfaz gráfica de usuario y de la Voice User Interface. Los diferentes sensores, cámaras y micrófonos permiten una comunicación versátil, la interfaz de usuario interactiva reacciona a los gestos, a los movimientos y al lenguaje, siendo capaz de reconocer rostros y objetos. 



Ilustración 68: Evolución de la interfaz de usuario [112] 

108 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Lo que propone Natural User Interface es eliminar en la medida de lo posible el “hardware intermediario”, esto es el ratón y el teclado, y aprovecharse de los comportamientos naturales del ser humano para mediar con la máquina. Los comportamientos que se podrían asociar a NUI incluirían: 

- Movimientos y gestos naturales 

- Lenguaje verbal y no verbal 

- Gestos faciales 

- Trayectoria del ojo humano 

Además, Natural User Interface incluye otros comportamientos humanos no tan visibles, como pueden ser los aspectos relacionados con la neuroergonomía. Estos contemplan cambios inconscientes o no voluntarios en el estado del cuerpo (sueño, temperatura, respiración, dilatación de la púpila, tasa cardiaca). 

Seguramente donde primero empezó a desarrollarse esta tecnología fue en los videojuegos de las distintas consolas, tanto Play Station como Xbox y especialmente la Wii, adoptaron estas tecnologías para permitir a los usuarios interactuar con dichos juegos de manera más directa y real. A día de hoy, el ejemplo más popular en cuanto a desarrollo embrionario de NUIs se refiere posiblemente sea el dispositivo Kinect desarrollado por Microsoft para la Xbox 360. La idea es eliminar el controlador clásico de videojuegos y usar los gestos espaciales del jugador como input. 



Ilustración 69: dispositivo kinect para la xbox 360 

El dispositivo de Kinect cuenta con múltiples sensores, entre ellos cámaras infrarojas, cámaras de profundidad o un emisor de infrarrojos que le permiten captar la información sobre el usuario. Una vez que los sensores captan la información, son inmediatamente procesados por un software de inteligencia artificial. Es capaz de clasificar los diferentes objetos que hay dentro de una escena. Reconoce a los seres humanos por su cabeza y extremidades. 

Kinect entiende cómo se mueve un ser humano y asume, por ejemplo, que somos incapaces de girar la cabeza 360º y demás acciones imposibles que podemos realizar. Esto es muy sencillo para nosotros, pero para una máquina conlleva un periodo de aprendizaje largo. Kinect captura el movimiento de las personas a través de más de 48 puntos de articulación. Esto se lleva a cabo a través de un algoritmo bastante complejo, que tiene en cuenta múltiples factores. 

109 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Este tipo de tecnología se encuentra aún en vías de desarrollo, pero presenta escenarios muy prometedores en diversas áreas [113]: 

- Medicina: La tecnología de natural user interface tiene un amplio campo de actuación en sectores como la rehabilitación motriz o el desarrollo de nuevas técnicas de imágenes médicas. 

- Integración: Investigadores de China, en colaboración con Microsoft Research, desarrollaron un traductor de lenguaje de signos. Esto permite comunicarse entre personas que hablan la lengua de signos y los que no. Lo hace en los dos sentidos, tanto traducir el lenguaje de signos a texto escrito cómo habla y viceversa, a través de un avatar mostrar en lenguaje de signos lo que está diciendo una persona [114]. 

- Realidad Aumentada: El desarrollo de esta tecnología será uno de los elementos claves de comunicación en la tecnología de realidad aumentada. 

- Juegos: Este es el área más explorada en la actualidad, sin embargo aun cuenta con un amplio recorrido de desarrollo tecnológico. 

### **5.2. Realidad Virtual** 

La Realidad Virtual (RV) es un entorno de escenas y objetos de apariencia real —generado mediante tecnología informática— que crea en el usuario la sensación de estar inmerso en él. Dicho entorno es contemplado por el usuario a través de un dispositivo conocido como gafas o casco de realidad virtual. Este puede ir acompañado de otros dispositivos, como guantes o trajes especiales, que permiten una mayor interacción con el entorno así como la percepción de diferentes estímulos que intensifican la sensación de realidad. 

La realidad virtual comprende dos elementos principales: el entorno del usuario y el entorno virtual. Mientras el usuario interactúa con el sistema de realidad virtual, los dos entornos se comunican e intercambian información a través de una barrera llamada interfaz. La interfaz puede considerarse como un traductor entre el usuario y el sistema de realidad virtual. Cuando el usuario aplica acciones de entrada (por ejemplo, movimiento, generación de fuerza, voz, etc.), la interfaz traduce estas acciones en señales digitales, que pueden ser procesadas e interpretadas por el sistema. Por otro lado, las reacciones calculadas del sistema también se traducen por la interfaz en cantidades físicas, que el usuario puede percibir mediante el uso de diferentes tecnologías de pantalla y actuador (por ejemplo, imágenes, sonidos, olores, etc.). Finalmente, el usuario interpreta esta información y reacciona al sistema en consecuencia. 

110 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 



Ilustración 70: Ejemplo de interacción con la realidad virtual [115] 

Los tipos de realidad virtual se clasifican en función del nivel de inmersión que presentan para el usuario: 

- Realidad virtual no inmersiva: Es el modelo más simple de realidad virtual y no cuenta con dispositivos como gafas 3D. Se conoce como no inmersiva porque el usuario tiene mayor conciencia de que se trata de una realidad simulada. Se trata del tipo más común de todos y por ello puede ser pasado por alto. Por lo general incluyen sistemas de sonidos envolventes y accesorios como audífonos, para lograr estimular los sentidos, pero en un grado inferior. 

- Realidad virtual semi inversiva: En este tipo de realidad el usuario aún distingue el mundo real del virtual, aunque esta línea se vuelve más difusa que en el caso de la no inmersiva. Para lograr una experiencia semi inmersiva se necesita de elementos virtuales apoyados de otros elementos físicos, creando así una realidad mixta. Por ejemplo, las cámaras de simulación de vuelo que cuentan con un espacio físico similar a una cabina real, pero en lugar de cristales tiene pantallas en las que se proyecta la simulación. Por su naturaleza, esta tecnología tiene un mayor aprovechamiento en el sector industrial y de educación, ya que facilita en gran medida la interacción con la información sin la necesidad de abandonar por completo el entorno real. 

- Realidad virtual inmersiva: Esta es la que ofrece la máxima experiencia de inmersión y la que se puede considerar más “futurista”. Un dispositivo habitual de RV inmersiva consiste en un casco conectado a un ordenador, que tiene una pantalla de alta resolución y ocupa toda la visión del usuario, además de sensores de movimiento conectados por todo el cuerpo. El usuario es sumergido en un mundo completamente virtual. 

En ocasiones la realidad virtual es confundida con la realidad aumentada y aunque son términos relacionados no son sinónimos. La realidad aumentada —RA por sus siglas en español— es el conjunto de tecnologías que permiten al usuario interactuar con el mundo real a través de un dispositivo electrónico, pero añadiendo a este elementos gráficos de una dimensión virtual. 

111 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Dicho recurso se puede utilizar en teléfonos móviles de casi cualquier sistema operativo, por lo que es mucho más accesible para el usuario promedio, tanto por el costo como por la disponibilidad. Uno de los ejemplos más famosos, porque fue todo un movimiento a nivel mundial, es el videojuego Pokémon GO, con su mecánica de juego que combina el uso de la cámara del celular con los pokemons virtuales. 



Ilustración 71: Interacción con la realidad aumentada de Pokemon Go [116] 

Dentro del campo de la realidad virtual encontramos un modelo de dispositivos conocidos como interfaces hápticas. Estas permiten al usuario tocar, sentir o manipular objetos simulados en entornos virtuales y sistemas teleoperados. 

Desde los inicios de la era de la computación y el auge de la interacción humano computadora es que diseñadores, desarrolladores e investigadores se han esmerado de crear interfaces que sean capaces de interactuar con las personas de manera mucho más acorde a las capacidades del cuerpo humano. 

Algunas de las áreas donde la realidad virtual se apoya sobre dispositivos hápticos son las siguientes: 

- Medicina: Simuladores quirúrgicos para entrenamiento médico, micro robots para cirugía mínimamente invasiva, etc. 

- Educación: Proporcionando a los estudiantes la posibilidad de experimentar fenómenos a escalas nano y macro, escalas astronómicas, como entrenamiento para técnicos, etc. 

- Entretenimiento: Juegos y consolas de video y simuladores que permiten al usuario sentir y manipular objetos virtuales, etc. 

- Industria: Integración de interfaces hápticos en los sistemas CAD de tal forma que el usuario puede manipular libremente los componentes de un conjunto en un entorno inmersivo. 

- Artes gráficas: Exhibiciones virtuales de arte, museos, escultura virtual etc. 

112 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

### **5.2.1. Metaverso** 

El proyecto de realidad virtual con mayor auge en la actualidad es el Metaverso, un concepto de mundo virtual impulsado por el creador de Facebook Mark Zuckerberg, pero en el que también están invirtiendo empresas como Google, Nvidia o Microsoft. 

En cuanto al concepto preciso de metaverso por el que apuestan Facebook y otras empresas, la idea sería la de crear un universo paralelo y completamente virtual, al que podremos acceder con dispositivos de realidad virtual y realidad aumentada, de forma que podamos interactuar entre nosotros dentro de él, y desde fuera con el contenido que tenemos dentro. 

La clave de este metaverso es que pueda ser totalmente inmersivo, o por lo menos mucho más de lo que es la actual realidad virtual. Sí, tendremos unas gafas que posiblemente sean parecidas a las actuales para sumergirnos en él, pero también sensores que registren nuestros movimientos físicos para que nuestro avatar dentro de ese metaverso haga exactamente lo mismo. 

Si estas experiencias llegan a ser exitosas, es probable que el o los metaversos se conviertan en la puerta de entrada para la mayoría de las experiencias digitales y en un sucesor natural de lo que es hoy internet. Entre los usos que se han delineado para estos espacios se encuentran: 

- Conciertos: ofrecería la posibilidad de ingresar virtualmente a un concierto en 3D, después de verlo de manera inicial en una pantalla de 2D. Por ejemplo, en 2019 el rapero Travis Scott protagonizó un concierto en Fortnite y reunió a cerca de 100,000 usuarios. 

- Trabajo: Las salas de reuniones virtuales pasarían de ser videconferencias a una experiencia inmersiva donde podrán compartirse impresiones como si de una reunión presencial se tratase. Facebook está impulsando la Infinite Office, un espacio que permite a los usuarios crear su lugar de trabajo ideal a través de la realidad virtual. 

- Videojuegos: El metaverso genera un nuevo escenario para los mundos virtuales creados dentro de los videojuegos ofreciendo a los usuarios un mundo en el que pueden jugar como si se tratase de la realidad. 

113 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

### **5.3. Nuevos paradigmas** 

El desarrollo de nuevas interfaces que permitan a los humanos comunicarse con computadores está en auge. En la actualidad existen muchos proyectos de investigación que trabajan sobre este paradigma. Uno de los que mayor atención ha acaparado por su controversia y debates éticos generados es el Neuralink. 

Neuralink es la empresa de tecnología de interfaz neuronal de Elon Musk. La compañía está construyendo un dispositivo que podría introducirse en el cerebro de una persona, desde donde podría registrar la actividad cerebral y estimularla. Musk ha comparado la tecnología con poner un “FitBit en tu cráneo”. 

El chip que está desarrollando Neuralink tiene aproximadamente el tamaño de una moneda y se incrustaría en el cráneo de un paciente. Desde el chip, una serie de cables diminutos, cada uno aproximadamente 20 veces más delgado que un cabello humano, se abre en abanico hacia el cerebro. 

Los cables están equipados con 1.024 electrodos que pueden monitorizar la actividad cerebral y, en teoría, estimular eléctricamente el cerebro. Todos estos datos se transmiten de forma inalámbrica a través del chip a los ordenadores donde los investigadores pueden estudiarlos. 



Ilustración 72: Implante de neuralink 

Este proyecto originalmente planteado como un nuevo paradigma médico que puede tener aplicaciones sobre múltiples enfermedades neurológicas ha sufrido varios reveses en su proceso de desarrollo. El más sonado y que ha causado la ralentización del proyecto es la experimentación llevada a cabo con monos. Originalmente la compañía aseguro que los experimentos estaban logrando un resultado muy positivo e incluso difundió un video de uno de los sujetos del experimento jugando a un videojuego utilizando solamente la mente gracias a el implante cerebral. Sin embargo, este proyecto a sufrido las denuncias de múltiples asociaciones animalistas. Además el Comité de Médicos por la Medicina Responsable acusa a los investigadores de someter a los monos a malos tratos ilegales y “sufrimiento extremo” mientras prueban implantes cerebrales para Neuralink. 

114 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

Esta organización, tal y como recoge el _New York Post_ , afirma que de los 23 monos de la la Universidad de California Davis en los que se habrían implantado los chips cerebrales de Neuralink entre 2017 y 2020 solamente habrían sobrevivido ocho. Esta información se habría descubierto a través de más de 700 páginas de documentos, registros veterinarios e informes de necropsias conseguidos gracias una solicitud de registros públicos en la universidad. 

Este tipo de dispositivos están en fases de pruebas y aún queda mucho para que sean una realidad. 

115 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

## **Bibliografía** 

- [1] <u>https://en.wikipedia.org/wiki/Blaise_Pascal#Pascaline</u> 

- [2] <u>https://es.wikipedia.org/wiki/Gottfried_Leibniz</u> 

- [3] <u>https://es.wikipedia.org/wiki/Joseph_Marie_Jacquard</u> 

- [4] <u>https://es.wikipedia.org/wiki/Herman_Hollerith</u> 

- [5] Library of Congress <u>http://memory.loc.gov/mss/mcc/023/0008.jpg, Dominio</u> público, <u>https://commons.wikimedia.org/w/index.php?curid=30538485</u> 

- [6] <u>https://es.wikipedia.org/wiki/Charles_Babbage</u> 

- [7] <u>https://es.wikipedia.org/wiki/Ada_Lovelace</u> 

- [8] <u>https://es.wikipedia.org/wiki/Konrad_Zuse</u> 

- [9]“U.S. Army Photo” from the archives of the ARL Technical Library 

- [10] <u>https://americanhistory.si.edu/comphist/pr4.pdf</u> 

- [11] <u>https://es.wikipedia.org/wiki/John_von_Neumann</u> 

- [12] <u>https://dl.acm.org/doi/abs/10.1145/960118.808380</u> 

- [13] <u>http://www.softwarepreservation.org/projects/os/gm.html</u> 

- [14] Franz Leopold, ed. (1959-07-03) [April 1959]. “(various)”. <u>Journal of the ACM.</u> New York, USA: <u>Association for Computing Machinery. 6 (2). ISSN 0004-5411.</u> 

- [15] Gobierno de los Estados Unidos - <u>http://ed-thelen.org/comp-hist/BRL61ibm1401.html#IBM-1401</u> 

- [16] <u>https://es.wikipedia.org/wiki/Robert_Noyce</u> 

- [17] Integrated circuit by Jack Kilby, September 1958. Gift of Texas Instruments 

- [18] <u>https://www.computerhistory.org/revolution/mainframe-computers/7/169/680</u> 

- [19] Gray, George (octubre de 1999). “Computadoras de tercera generación de Burroughs” . Boletín de Historia de Unisys . 3 (5). Archivado desde el original el 26 de septiembre de 2017 

116 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- [20] The PDP-8 on display at the National Museum of American History in Washington, D.C.. Originally uploaded to English Wikipedia by Alkivar (00:10, 14 April 2005). 

- [21] <u>https://es.wikipedia.org/wiki/Gordon_Moore</u> 

- [22] <u>https://es.wikipedia.org/wiki/Robert_Noyce</u> 

- [23] <u>https://www.britannica.com/topic/Intel</u> 

- [24] <u>https://www.intel.es/content/www/es/es/history/museum-story-of-intel-4004. html</u> 

- [25] <u>https://enciclopedia_universal.es-academic.com/15808/Intel_8008</u> 

- [26] <u>https://hipertextual.com/2012/08/historia-intel-8080</u> 

- [27] <u>https://www.xataka.com/historia-tecnologica/altair-8800-todo-comenzo-haceya-40-anos</u> 

- [28] <u>https://www.academia.edu/27854470/History_of_MS_DOS</u> 

- [29] <u>Macintosh 128k. All About Apple Museum. Archived from the original</u> on 2004-01-01. 

- [30] <u>https://www.computerhistory.org/revolution/personal-computers/17/297</u> 

- [31] <u>https://www.linkedin.com/company/tandy-corporation</u> 

- [32] <u>https://es.wikipedia.org/wiki/Commodore_International</u> 

- [33] <u>https://ri.uaemex.mx/bitstream/handle/20.500.11799/63803/secme-35342. pdf?sequence=1</u> 

- [34] De Seofilo - <u>http://seofilo.com/que-es-la-ley-de-moore/, CC BY-SA 4.0, https:// commons.wikimedia.org/w/index.php?curid=74321614</u> 

- [35] <u>https://es.wikipedia.org/wiki/Seymour_Cray</u> 

- [36] <u>https://www.hpe.com/es/es/compute/hpc/cray.html</u> 

- [37] <u>https://parceladigital.com/2017/03/21/osborne-1-el-primer-ordenador-portatil-deexito-comercial-de-la-historia</u> 

- [38] <u>https://internetpasoapaso.com/quinta-generacion-computadoras/</u> 

117 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- [39] <u>https://www.tecnologia-informatica.com/generaciones-computadoras-sexta-generacion/#La_ Quinta_Generacion_de_Computadoras_(desde_1991)</u> 

- [40] <u>http://www.scielo.org.bo/scielo.php?script=sci_arttext&pid=S1683-07892001000200006</u> 

- [41] <u>https://www.techedgegroup.com/es/blog/introduccion-computacion-cuantica-i</u> • [42] <u>https://quantum-computing.ibm.com</u> 

- [43] <u>https://www.nature.com/articles/s41586-019-1666-5</u> 

- [44] <u>https://www.xataka.com/investigacion/china-consolida-su-superioridad-comunicaciones-cuanticas-acaba-llegar-lejos-que-nadie-su-red-cuantica-invulnerable</u> 

- [45] <u>https://es.wikipedia.org/wiki/Unidad_aritmética_lógica</u> 

- [46] <u>https://es-academic.com/dic.nsf/eswiki/106471</u> 

- [47] David Strigoi 

- [48] R.S. Shawn <u>https://commons.wikimedia.org/wiki/File:CPU_block_diagram. png</u> 

- [49] <u>https://www.amazon.es/Procesador-Intel-i7-4790-Haswell-Reacondicionado/ dp/B07PYJF9WP</u> 

- • [50] <u>https://www.profesionalreview.com/2019/12/10/memorias-nand/</u> 

- [51] <u>https://es.wikipedia.org/wiki/Unidad_de_disco_duro</u> 

- [52] <u>https://www.pccomponentes.com/l-link-fuente-de-alimentacion-500w-sfx-micro-atx?gclid=CjwKCAjwloCSBhAeEiwA3hVo_SIgszFqFdYdp8uX-kTOEgNvZtwKNG7ByuxxbGRfat0Jil9sPxCB6BoCLnAQAvD_BwE</u> 

- [53] <u>https://culturacion.com/como-limpiar-el-disipador-de-calor-del-cpu-parte-ii/</u> 

- [54] <u>https://www.pccomponentes.com/corsair-hydro-h100x-kit-de-refrigeracion-liquida?gclid= CjwKCAjwloCSBhAeEiwA3hVo_XPg7YDkX0lWCr5VCHjQIETV7h9oMVkbxMG2wHUU3JdzhVluVUdNxBoCNCIQAvD_BwE</u> 

- [55]https://books.google.es/books?hl=en&lr=&id=KJORYTHOxbEC&oi=fnd&pg=P <u>P1&dq=coprocesors&ots=y9zeijcm_u&sig=cUeFhfoOJ2NA728OH04Ar_jigco#v=o nepage&q=coprocesors&f=false</u> 

- [56] <u>http://www.upv.es/amiga/258.htm</u> • [57] <u>https://e-archivo.uc3m.es/handle/10016/23730?show=full</u> 

118 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- [58] <u>http://www.fdi.ucm.es/profesor/mendias/512/docs/tema9.pdf</u> 

- [59] Gestión de derechos digitales: conceptos, metodologías, herramientas y aplicaciones . Asociación de Gestión de Recursos de Información. Hershey, Pa .: Information Science Reference (una impresión de IGI Global). 2013. p. 609. ISBN 9781466621374. OCLC  811354252 .CS1 maint: otros 

- [60] <u>https://link.springer.com/chapter/10.1007/978-1-4614-7915-4_17</u> 

- [61] <u>https://www.um.es/documents/4874468/19345367/ssee-da-t04-01.pdf/20ed49bb-90d74d1b-a5d5-bc5cadc34fef</u> 

- [62] <u>https://www.electronicasi.com/wp-content/uploads/2013/04/dspElectronicaavanzada.pdf</u> 

- [63] https://quantumai.google/hardware 

- [64] <u>https://en.wikipedia.org/wiki/Summit_(supercomputer)</u> 

- [65] <u>https://www.nature.com/articles/s41586-019-1666-5</u> 

- [66] <u>https://quantumai.google/cirq</u> 

- [67] <u>https://research.ibm.com/blog/127-qubit-quantum-processor-eagle</u> 

- [68] <u>https://research.ibm.com/interactive/system-one/</u> 

- [69] <u>https://riunet.upv.es/bitstream/handle/10251/174441/Gimenez%20-%20APLICACIONES%20DE%20GPUs%20EN%20VISION%20E%20INTELIGENCIA%20 ARTIFICIAL%20PARA%20EL%20RECONOCIMIENTO%20DE%20FORMAS. pdf?sequence=1&isAllowed=y</u> 

- [70] <u>https://www.nvidia.com/es-la/drivers/what-is-gpu-computing/</u> 

- [71]https://riubu.ubu.es/bitstream/handle/10259/3933/Programacion_en_CUDA. <u>pdf;jsessionid=35E82C7EE8B0AFA1AB874C13AC556487?sequence=1</u> 

- [72] <u>https://analog-ai-demo.mybluemix.net/hardware</u> 

- [73] <u>https://www.humanbrainproject.eu/en/about/overview/</u> 

- [74] <u>https://viso.ai/edge-ai/vision-processing-unit-vpu-for-inference/</u> 

- [75] https://arxiv.org/pdf/1810.04150.pdf 

- [76] <u>https://descubrearduino.com/fpga/</u> 

119 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- [77] FPGA Wars • [78] https://www.apriorit.com/dev-blog/586-fpgas-for-ai • [79] <u>https://www.run.ai/guides/machine-learning-operations/edge-ai</u> • [80] <u>https://www.computerweekly.com/es/definicion/Internet-de-las-cosas-IoT</u> • [81]https://cincodias.elpais.com/cincodias/2022/01/28/companias/1643379371_380130. <u>html</u> 

- • [82] <u>https://www.ibm.com/blogs/industries/little-known-story-first-iot-device/</u> • [83] <u>https://en.wikipedia.org/wiki/ACARS</u> • [84]https://www.cisco.com/c/dam/global/es_mx/solutions/executive/assets/pdf/ <u>internet-of-things-iot-ibsg.pdf</u> 

- • [85] <u>https://www.seagate.com/files/www-content/our-story/trends/files/idc-seagate-dataage-whitepaper.pdf</u> 

- • [86] <u>https://www.ibm.com/es-es/topics/industry-4-0</u> • [87]https://mesbook.com/industria40entufabrica/?gclid=CjwKCAiAvOeQBhBk <u>EiwAxutUVGmpqstQN6ON_udl2Xo2rBrZXo83W4vrb1U2eR-vljzz6LY9dS-gqhoC5yEQAvD_BwE</u> 

- • [88] <u>https://es.wikipedia.org/wiki/Lean_manufacturing</u> • [89] <u>https://cliatec.com/gemelo-digital-modelo-predictivo-para-los-centros-de-datos/</u> 

- • [90] <u>http://www.bigdata-social.com/el-hype-cycle-tecnologico-de-gartner-es/</u> • [91] <u>https://www.lisdatasolutions.com/blog/que-es-la-industria-4-0/#language</u> • [92] <u>https://www.nespra.net/blog/sensores-iot-tipos-y-aplicaciones/</u> • [93] <u>https://www.mecatronicalatam.com/es/tutoriales/sensores/sensor-de-humedad/</u> 

- • [94] <u>https://prototipadolab.com/2018/05/05/que-son-los-sensores/</u> • [95] <u>https://es.omega.com/prodinfo/acelerometro.html</u> 

- [96] <u>https://es.farnell.com/sensor-gyroscope-technology</u> 

120 

**Módulo. Cognitive Devices** 

**Centro Europeo de Postgrado** 

- [97] <u>https://es.farnell.com/sensor-technology</u> 

- [98] <u>https://hardzone.es/reportajes/que-es/mems/</u> 

- [99] <u>https://www.autracen.com/blog/blog-autracen-1/sistemas-de-vision-industrial-38</u> 

- [100] <u>https://www.brainsigns.com/es/science/s2/technologies/gsr</u> 

- [101] <u>https://hacedores.com/sensores-biomedicos/</u> 

- [102] <u>https://www.i-run.es/electronica/banda-de-frecuencia-cardiaca/polar/sensor-de-frecuencia-cardiaca-H9--XS-S_fiche_93407.html</u> 

- [103] <u>https://d2n0lz049icia2.cloudfront.net/product_document/PS-2111-Sensorde-Electrocardiograma.pdf</u> 

- [104] <u>https://www.msdmanuals.com/es/hogar/temas-especiales/pruebas-de-diagnóstico-por-la-imagen-habituales/resonancia-magnética-nuclear-rmn</u> 

- [105] <u>https://www.google.com/glass/start/</u> 

- [106] <u>https://www.bbva.com/es/negocio-wearables-quiere-pasar-pantalla/</u> 

- [107]https://www.amazon.com/-/es/gp/help/customer/display.html?nodeId=GG3RZLAA3RH83JAA 

- [108] <u>https://developer.amazon.com/en-US/alexa/alexa-skills-kit</u> 

- [109] <u>https://jcarroll.ist.psu.edu</u> 

- [110] <u>https://blog.opinno.io/es/blog/que-es-la-interaccion-humano-computadora</u> 

- [111] <u>https://www.xataka.com/otros-dispositivos/crean-pantalla-tinta-electronicaplegable-que-se-pueden-tomar-notas</u> 

- [112] https://es.wikipedia.org/wiki/Interfaz_natural_de_usuario#/media/Archivo:CLI- <u>GUI-NUI,_evolución_de_interfaces_de_usuario.png</u> 

- [113] <u>https://programarfacil.com/podcast/86-sensor-kinect-inteligencia-artificial/</u> 

- [114] <u>https://www.microsoft.com/en-us/research/blog/kinect-sign-language-translator-part-1/?from=http%3A%2F%2Fresearch.microsoft.com%2Fen-us%2Fcollaboratio n%2Fstories%2Fkinect-sign-language-translator.aspx</u> 

- [115] <u>https://www.xataka.com/realidad-virtual-aumentada/quiero-dar-salto-a-realidad-virtual-2020-donde-empiezo</u> 

- [116] <u>https://pokemongolive.com/es/</u> 

121 







**CEUPE** Centro Europeo de Postgrado 

**Web** 

www.ceupe.com 

**E-mail** info@ceupe.com 

