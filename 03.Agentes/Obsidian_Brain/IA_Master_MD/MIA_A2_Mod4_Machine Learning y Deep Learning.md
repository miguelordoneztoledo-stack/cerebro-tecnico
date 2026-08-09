---
tags:
  - master_ia
  - teoria
source: MIA_A2_Mod4_Machine Learning y Deep Learning.pdf
---

# **Módulo Machine Learning y Deep Learning** 



# **Módulo Machine Learning y Deep Learning** 

|**INTRODUCCIÓN A PYTHON ....................................................................................03**<br>|
|---|
|**1. ORIGEN Y CLASIFICACIÓN DE LA INTELIGENCIA ARTIFICIAL ............................07**|
|**2. APRENDIZAJE SUPERVISADO .............................................................................12**<br>|
|2.1. CLASIFICACIÓN ..............................................................................................13<br>|
|2.1.1. REGRESIÓN LOGÍSTICA ...........................................................................14|
|2.1.2. CLASIFICADOR NAIVE BAYES ..................................................................20|
|2.1.3. K-NEAREST NEIGHBOURS   .....................................................................26<br>|
|2.1.4. SUPPORT VECTOR MACHINE (SVM) ........................................................35<br>|
|2.1.5. ÁRBOLES DE DECISIÓN ...........................................................................42<br>|
|2.2. REGRESIÓN ....................................................................................................48<br>|
|2.2.1. REGRESIÓN LINEAL .................................................................................48<br>|
|2.2.2. TÉCNICAS DE REGULARIZACIÓN .............................................................52|
|2.2.3. STEPWISE REGRESSION ...........................................................................54<br>|
|2.2.4. OTROS MODELOS DE REGRESIÓN ...........................................................57|
|**3. APRENDIZAJE NO SUPERVISADO .......................................................................58**|
|3.1. CLUSTERING ..................................................................................................59|
|3.1.1. K-MEANS ................................................................................................60|
|3.1.2. K-MEDIAN  .............................................................................................66|
|3.1.3. HYERARCHICAL CLUSTERING O AGRUPAMIENTO JERARQUICO .............66<br>|
|3.2. REDUCCIÓN DE DIMENSIONALIDAD ..............................................................76<br>|
|3.2.1. EXTRACCIÓN DE CARACTERÍSTICAS .......................................................78|
|3.2.1.1. CLASIFICADORES LINEALES ..................................................................78|
|3.2.1.2. CLASIFICADORES NO LINEALES ............................................................86|
|3.2.2. SELECCIÓN DE CARACTERÍSTICAS ..........................................................87|
|**4. APRENDIZAJE POR REFUERZO ............................................................................90**|
|**5. DEEP LEARNING ...................................................................................................99**|
|5.1. REDES NEURONALES ....................................................................................101|
|5.1.1. REDES NEURONALES ARTIFICIALES .......................................................103|
|5.1.1.1. PERCEPTRÓN SIMPLE .........................................................................108<br>|
|5.1.1.2. PERCEPTRÓN MÚLTIPLE......................................................................109|
|5.1.2. REDES PROFUNDAS ..............................................................................111|
|5.1.3. REDES NEURONALES RECURRENTES (RNN) ............................................113|
|5.1.4. REDES NEURONALES CONVOLUCIONALES (CNN) .................................116|
|5.1.5. DECONVOLUTIONAL NETWORK (DN) ....................................................118|
|5.1.6. REDES DE CREENCIAS PROFUNDAS (DBN) .............................................119|
|5.1.7. AUTO ENCODER (AE) ............................................................................121|
|5.1.8. RED GENERATIVA ANTAGÓNICA (GAN) ................................................122|
|5.1.9. DEEP RESIDUAL NETWORK (RESNET) .....................................................123|
|5.2. LIMITACIONES DEL DEEP LEARNING .............................................................124|
|**BIBLIOGRAFÍA ........................................................................................................126**|



**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

## **Introducción a Python** 

_“Uno de los objetivos que se persigue con este lenguaje de programación es que se automaticen procesos para que así se consiga ahorrar tiempo y evitar complicaciones. Por esa razón son varias las soluciones que se logran con pocas líneas de código en este programa.”_ 

A lo largo de esta guía docente vamos a ver una serie de ejemplos prácticos de modelos de inteligencia artificial basados en el lenguaje de programación Python. 

La asignatura no se centra en los métodos de programación si no mas bien en que el alumno disponga de herramientas para la resolución práctica de cálculos habituales en el desarrollo de modelos de inteligencia artificial. 

Para superar la asignatura no será necesario tener conocimientos de programación en Python, pero si se recomienda la familiarización del alumno con el entorno. 

La facilidad de Python en la creación y uso de estructuras de datos indexadas y asociativas (en forma de listas/tuplas y diccionarios), así como de conjuntos, permite que los conceptos de programación se demuestren sin necesidad de una discusión detallada de los específicos del lenguaje de programación.  Además, este lenguaje de programación esta concebido con una filosofía que hace hincapié en una sintaxis legible. 

Uno de los objetivos que se persigue con este lenguaje de programación es que se automaticen procesos para que así se consiga ahorrar tiempo y evitar complicaciones. Por esa razón son varias las soluciones que se logran con pocas líneas de código en este programa. 

Python se trata de un lenguaje de programación de código abierto disponible de manera gratuita a través de distintas distribuciones. La forma mas sencilla de trabajar con Python es hacerlo a través de su distribución de Anaconda. 

Esta distribución nos permite instalar de forma gratuita los lenguajes de Python y R en nuestro ordenador de una forma muy sencilla. 

Para poder obtener la distribución nos dirigimos a la web oficial de la distribución y descargamos la edición individual en nuestro ordenador. 

03 

**Módulo. Machine Learning y Deep Learning** 

**Centro Europeo de Postgrado** 

#### <u>https://www.anaconda.com</u> 

Seguimos las instrucciones del instalador gráfico y tendremos en nuestro equipo el Anaconda-Navigator. Desde aquí podemos elegir un editor con el que trabajar con Python. Podemos utilizar el editor web de Jupyter Notebook /Jupyter Lab o el editor local Spyder. Para acceder a ambos únicamente tenemos que hacer click en el botón “launch” que podemos ver representado en la Ilustración 1. A través de cualquiera de estos editores es posible ejecutar los distintos ejemplos de modelos de inteligencia artificial que encontraremos en la guía docente. 

Para desarrollar los ejemplos de esta guía se ha empleado el editor web Jupyter Notebook, el cual nos permite ejecutar scripts de Python desde un navegador web sin necesidad de instalar ningún software local en nuestro ordenador. 



Ilustración 1:Ejecución de editor de Python desde Anaconda Navigator 

Cuando lo ejecutamos abrirá una nueva pestaña en nuestro navegador web desde la que podemos ver la estructura de carpetas de nuestro PC. Simplemente debemos dirigirnos a la carpeta en la que queremos trabajar y desde ahí crear un nuevo Notebook de Python en el que ejecutar nuestro código. 

04 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 2: Ejecución de Jupyter Notebook 

En ese momento se abrirá un nuevo kernel de Python donde podemos ejecutar las distintas funciones de Python. 



##### Ilustración 3: Python Kernel 

En el transcurso de la asignatura emplearemos Python para ejemplificar la codificación de algunos de los modelos estudiados. Para ello nos apoyaremos en librerías ya desarrolladas que nos van a facilitar el proceso, reduciendo la creación de un modelo a unas pocas líneas de código. Algunas de las librerias que vamos a utilizar durante este módulo son las siguientes: 

- CSV: Permite leer y escribir ficheros en formato CSV 

- Numpy: Es una librería que nos permite definir un tipo de dato con el que podemos trabajar con vectores y matrices. Además de esto permite utilizar múltiples funciones matemáticas de alto nivel. 

- Pandas: Es una librería escita como una extensión de numpy que nos ofrece estructuras de datos y operaciones para trabajar con tablas numéricas y series temporales. 

- Matplotlib: Es una librería diseñada para la generación de gráficos a partir de datos contenidos en listas o matrices. Esta librería también es una extensión de Numpy 

05 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- Scikit-learn: Es una librería diseñada para trabajar con inteligencia artificial. Basa su estructura en Numpy, Scipy y Matplotlib y nos permite trabajar con varios algoritmos de clasificación, regresión y análisis de grupos entre los que podemos encontrar k-mean, maquinas de vectores de soporte, bosques aleatorios entre muchos otros. Esta librería es muy fácil de utilizar y de aprender ya que nos permite reducir la creación de un modelo de inteligencia artificial a una sola línea. 

06 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

## **1. Origen y clasificación de la Inteligencia Artificial** 

_“En el aprendizaje automático o machine learning los humanos suministramos una serie de datos de entrada, así como las respuestas esperadas a dichos datos de entrada con el fin de obtener como salida una serie de reglas que nos permitan obtener la correspondencia entre los datos de entrada y salida.”_ 

La inteligencia artificial (IA) nació a principios del siglo pasado de la mano de una serie de pioneros de la ciencia computacional que comenzaron a desarrollar su actividad centrándola en el objetivo de que las máquinas “pensaran” por si mismas con el objetivo de poder automatizar una seria de tareas cotidianas intelectuales llevadas a cabo por humanos. 

El concepto de inteligencia artificial nació como tal en 1956 de la mano de John McCarthy, Marvin Minsky y Claude Shannon, tres científicos destacados de la época que acuñaron este término durante la conferencia de Darthmounth y la definieron como: “la ciencia e ingenio de hacer máquinas inteligentes, especialmente programas de cálculo inteligentes”. [1] 

Sin embargo, el origen de la inteligencia artificial es anterior al acuñado del nombre. En 1936, Alan Turing publico su famoso artículo “On computable numbers, with an application to the entscheidungs problem” [2] donde sentaba las bases teóricas de la inteligencia artificial. En este artículo aparece por primera vez la ‘Máquina de Turing’ que establece el concepto de algoritmo y actúa como precursora de los computadores actuales. 

La máquina de Turing asemeja el funcionamiento de una CPU actual, cuenta con tira de cinta sobre la que la máquina puede leer y escribir símbolos de manera mecánica de acuerdo con una serie de reglas. Estas instrucciones son finitas y son consideradas como el primer algoritmo. 

07 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Como continuación de su trabajo Alan Turing publico un nuevo artículo en 1950 llamado “Computing Machinery and Intelligence” [3] de donde se extrae la famosa prueba de Turing o test de Turing. Esta prueba consiste en un examen de la capacidad de una máquina para exhibir un comportamiento inteligente similar al de un ser humano o indistinguible de este. Esta prueba consistía en que un observador externo (humano) evaluara una conversación en [[MIA_A1_Mod3_Procesamiento Lenguaje Natural|lenguaje natural]]. En el test participaban tanto humanos como una máquina diseñada para generar respuestas similares a las de un humano. El observador debía ser capaz de discernir en cinco minutos de conversación si su interlocutor era humano o máquina. Esta prueba se realizaba a través de un teclado y un monitor para eliminar la capacidad de la máquina de convertir texto en habla. 

A partir de esta prueba Alan Turing llego a la conclusión de que ordenadores de propósito general podrían ser capaces de “aprender”. Esto abrió la puerta a nuevas cuestiones como: ¿Seria un ordenador capaz de realizar tareas como si fuese un ser humano? ¿Podría un ordenador aprender por si mismo a realizar una tarea especifica? ¿Podría hacerlo en base a los datos que le proporcionamos? 

Estas preguntas abrieron la puerta a un nuevo paradigma de programación. A diferencia del paradigma clásico de programación simbólico en el que los humanos proporcionaban una serie de instrucciones precisas (un programa o algoritmo) y datos para que sean procesados con estas reglas, obteniendo las respuestas como salida del programa surge el aprendizaje automático. 

En el aprendizaje automático o machine learning los humanos suministramos una serie de datos de entrada, así como las respuestas esperadas a dichos datos de entrada con el fin de obtener como salida una serie de reglas que nos permitan obtener la correspondencia entre los datos de entrada y salida. 

Estas reglas son luego aplicadas a nuevos datos para producir respuestas originales, es decir generadas automáticamente por las reglas que el sistema ha creado y no por reglas codificadas por programadores. 

El aprendizaje automático tuvo su consagración en 1997 cuando IBM lanzó el super ordenador Deep Blue. Esta super computadora fue la primera que venció a un campeón del mundo vigente, Gary Kaspárov, con un ritmo de juego lento. Esto ocurrió el 10 de febrero de 1996, en una memorable partida. Sin embargo, Kaspárov ganó 3 y empató 2 de las siguientes partidas, derrotando a Deep Blue por 4-2. El encuentro concluyó el 17 de febrero de 1996. A este le siguió Watson, otro ordenador de IBM, al que se le asigno ese nombre en honor del fundador y primer presidente de IBM, Thomas J. Watson. Para probar sus capacidades reales participó durante tres días en febrero de 2011 en el popular concurso de televisión estadounidense de preguntas y respuestas Jeopardy! concursando y derrotando a dos participantes humanos. Siguiendo la misma línea Google presento en octubre de 2015 AlphaGo un programa informático de inteligencia artificial para jugar al juego de mesa Go, este se convirtió en la primera máquina de Go en ganar a un jugador profesional de este juego. 

08 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Esto dio lugar a una carrera tecnológica en la que las grandes compañías comenzaron a invertir grandes sumas de dinero por liderar esta tecnología. Hoy en día esta tecnología esta extendida en múltiples sectores como el financiero, salud, seguridad, educación etc. Su éxito ha estado influido también por los avances realizados en el campo del hardware y la mayor disponibilidad de conjuntos grandes de datos sobre los que se sustenta la creación de algoritmos de aprendizaje automático. 

Dentro del campo de la inteligencia artificial, el aprendizaje automático se ha convertido en el subcampo mas popular y exitoso y sobre el se han generado nuevas técnicas de reciente aparición como el Deep Learning. Este se basa la generación de una estructura jerarquica de redes neuronales artificiales, que buscan imitar la estructura cerebral humana. 

La forma en la que se relacionan los conceptos de inteligencia artificial, aprendizaje automático y aprendizaje profundo o deep learning que acabamos de introducir se encuentra reflejada en la Ilustración 1. 



Ilustración 4: Machine Learning y Deep Learning como subcampos de la inteligencia artificial 

Como podemos observar, el concepto de aprendizaje automático se encuentra dentro del campo de la inteligencia artificial, pero no supone la totalidad de la misma. 

09 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Esta área de la inteligencia artificial esta fuertemente relacionado con la estadística matemática como veremos mas adelante, sin embargo, difiere de la misma en su construcción y aplicaciones. El objetivo del aprendizaje automático se basa en la creación de unas reglas extrapolables a nuevos conjuntos de datos sin programación explicita, mientas que la estadística es un subcampo de las matemáticas basado en espacios de probabilidad, donde se busca caracterizar la relación entre los datos y la variable resultado sin tratar de realizar predicciones sobre datos futuros. Asimismo, el aprendizaje automático trabaja con grandes y complejos conjuntos de datos para los cuales el análisis estadístico clásico no podría ser utilizado por volumen y nivel de complejidad. 

Los problemas que podemos resolver a través del aprendizaje automático pueden ser clasificados en tres clases: 

- Aprendizaje supervisado (Supervised Learning) 

- Aprendizaje no supervisado (Unsupervised Learning) 

- Aprendizaje por refuerzo (Reinforcement Learning) 

En el primer caso hablamos de aprendizaje supervisado cuando tenemos un conjunto de datos para los cuales conocemos la respuesta correcta que tratamos de predecir y en base a la misma construimos el algoritmo que nos va a permitir relacionar los datos de entrada con los datos de salida y aplicarlo a nuevos subconjuntos de datos. [4] 

En el caso del aprendizaje no supervisado no conocemos la respuesta correcta que tratamos de predecir para el conjunto de datos que estamos utilizando para crear nuestro modelo por lo que se basa en identificar estructuras dentro de los datos. En este tipo de aprendizaje lo que buscamos es extraer la máxima información de los datos, sin que nadie le haya dicho al algoritmo que esperamos encontrar. 

Entre el aprendizaje supervisado y el aprendizaje no supervisado podemos encontrar una categoría intermedia llamada aprendizaje semi-supervisado. En este tipo de aprendizaje contamos con un conjunto de datos mixto, parte del mismo contiene las respuestas correctas al conjunto de datos con el que estamos trabajando y una parte de los datos, habitualmente mayoritaria, para la cual no tenemos la respuesta correcta. Este tipo de aprendizaje combina funciones del aprendizaje supervisado y del no supervisado realizando co-entrenamientos de los datos. 

En el vocabulario utilizado dentro del campo de la inteligencia artificial vamos a considerar los datos utilizados en el aprendizaje supervisado como datos etiquetados y los datos utilizados en el aprendizaje no supervisado como datos no etiquetados. 

10 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Finalmente nos encontramos con un último modelo de aprendizaje, el aprendizaje por refuerzo. Este tipo de aprendizaje es mas complejo que los anteriores ya que contaremos con mas elementos que ambientales que afectan a la creación de nuestros modelos. 

Este esta basado en la psicología conductista, en la cual un agente (en nuestro caso un modelo o elemento de software) recibe inputs del ambiente. Estos pueden ser positivos o negativos, en función del comportamiento que pretendamos que nuestro agente aprenda. Un buen ejemplo de funcionamiento de inteligencia artificial por medio de aprendizaje por refuerzo es la de los coches autónomos. Estos aprenden en base a las distintas respuestas que les proporciona el entorno, que pueden ser negativas (choque, patinazo de ruedas, atropello…) o positivas (tomar el carril correcto, cruzar un semáforo en verde, respetar el límite de velocidad…). [5] 

Además, dentro del aprendizaje automático también podemos abordar el análisis de datos de una forma no lineal, empleando una estructura jerárquica.  En este caso estaríamos hablando de un subcampo dentro del aprendizaje automático, el aprendizaje profundo. 

Este, emplea una estructura jerárquica basada en la estructura neuronal del cerebro humano, con distintos nodos conectados como si de una tela de araña se tratara. El sistema se basa en distintos niveles y cada uno de estos niveles tiene una función cognitiva en los datos que se están procesando. En el primer nivel el modelo aprende algo sencillo y esta información es pasada al segundo nivel, donde se procesan nuevos datos junto a la información obtenida en el primer nivel obteniendo una complejidad cognitiva mas alta. De esta forma la información va pasando por una serie de niveles hasta que se llega a un procesamiento completo de la información. [6] 

Un ejemplo de como funciona el Deep learning lo podemos encontrar en el procesamiento de video. Cuando un algoritmo de aprendizaje profundo tiene como objetivo el análisis de un video lo hace dividiendo la información a procesar sobre sus diferentes capas neuronales. En el primer nivel de procesado, el algoritmo es capaz de distinguir el contraste del video, separando las zonas claras de las oscuras, determinando que puntos de la imagen están iluminados y cuales están oscuros. Esta información pasa al segundo nivel de procesado de la red neuronal, donde se identifican las formas básicas de los objetos ayudándose de la información de contraste obtenida en el nivel anterior. Este nuevo conjunto de información pasa al tercer nivel de procesado donde se extraen nuevas características del video basándose en las imágenes crudas y la información obtenida en las capas previas. Este proceso se repite hasta obtener unos resultados de identificación de objetos que cumplan con el objetivo de exactitud que estemos buscando. 

Este tipo de aprendizaje esta recibiendo una gran atención últimamente debido a los resultados que esta logrando. Algunas de las aplicaciones en las que se esta utilizando el Deep learning son el procesamiento de imágenes (búsqueda de productos por imágenes, determinar logos de marcas, videovigilancia…), prevención de fraude basado en el comportamiento habitual de los clientes, investigación médica, ciberseguridad. 

11 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

## **2. Aprendizaje supervisado** 

_“El aprendizaje supervisado permite que los algoritmos ‘aprendan’ de datos históricos/de entrenamiento y los apliquen a entradas desconocidas para obtener la salida correcta.”_ 

El aprendizaje supervisado es una de las técnicas mayoritarias dentro del aprendizaje automático. Este tipo de técnicas están caracterizadas por trabajar con datos de entrenamiento etiquetados, es decir, los datos con los que realizamos el entrenamiento consisten en pares de objetos donde encontramos datos de entrada y datos de salida. El aprendizaje supervisado permite que los algoritmos ‘aprendan’ de datos históricos/de entrenamiento y los apliquen a entradas desconocidas para obtener la salida correcta. El objetivo del aprendizaje supervisado es el de crear una función que permita correlacionar los datos de entrada con los datos de salida. 



Ilustración 5: Esquema de funcionamiento de aprendizaje supervisado 

12 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Una vez hemos llevado a cabo el entrenamiento de nuestro modelo de aprendizaje supervisado lo que obtenemos es un modelo que podemos emplear con nuevos datos de entrada, de los cuales no conocemos sus etiquetas o datos de salida que pretendemos obtener mediante la aplicación del modelo. Este tipo de modelos dentro de la inteligencia artificial se consideran modelos predictivos ya que si objetivo es predecir los datos de salida o etiquetas asociadas al conjunto de datos de entrada. Dentro de los modelos de aprendizaje supervisado podemos encontrar dos grandes grupos: modelos de clasificación y modelos de regresión. Los modelos se clasifican dentro de estas dos subcategorías en función del tipo de salida que buscamos obtener con nuestros datos. 

Los modelos de clasificación tienen como salida un valor categórico por ejemplo una enumeración o un conjunto finito de clases, por ejemplo, dada una letra escrita a mano, determinar de que letra se trata. Otro ejemplo que podemos encontrar dentro de los algoritmos de tipo clasificación es el que podemos encontrar en la Ilustración 3, donde se presenta una clasificación de imágenes en base a un conjunto finito de posibilidades, en este caso tipos de animales. 

Por otro lado, los modelos de regresión se caracterizan por tener como salida un atributo numérico especifico, es decir tienen como objetivo predecir un resultado que varia dentro de un rango continuo. En la regresión, un algoritmo necesita identificar una relación funcional entre los parámetros de entrada y salida. El valor de la salida no es discreto como en el caso de la clasificación si no que su valor se calcula en base a una función construida con los datos de entrada. Un ejemplo muy común que podemos encontrar dentro de los modelos predictivos de regresión son los modelos que tratan de predecir el valor de mercado de un bien. Este tipo de modelos de aplican frecuentemente en los mercados financieros, urbanísticos...Para ello se emplean datos de entrada como precio histórico, ubicación, área, metros cuadrados de la vivienda y la salida será el valor estimado de un inmueble específico.[7] 

### **2.1. Clasificación** 

Como acabamos de ver, los algoritmos de clasificación es uno de los principales subgrupos dentro del aprendizaje supervisado. Este tipo de algoritmo tiene como objetivo predecir las etiquetas de clase de nuevos registros basándose en observaciones pasadas. Dependiendo de la etiqueta, se puede decir que la clasificación es binaria o multi-clase.[8] 

- Clasificación binaria: Es un tipo de clasificación en la que solo podemos asignar dos tipos de clases diferentes: 0 o 1, positivo o negativo, aprobado o suspenso… Un posible ejemplo de este tipo de clasificación binaria lo podemos encontrar en medicina cuando analizamos una imagen patológica, su salida puede ser positiva :la imagen muestra la enfermedad, o negativa: la imagen no muestra señales de presencia de la enfermedad. 

13 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- Clasificación multi-clase: Se pueden asignar múltiples categorías a los datos objeto de la clasificación. Un buen ejemplo de este tipo de clasificación puede ser el reconocimiento de un grupo de imágenes de frutas las cuales pueden pertenecer a un grupo preestablecido de etiquetas: manzanas, peras, naranjas… 

Existen muchos tipos de algoritmos que utilizan este tipo de entrenamiento. En este curso haremos un repaso de los mas comunes y sus aplicaciones. 

### **2.1.1. Regresión Logística** 

La regresión logística es un método de regresión que nos permite estimar la probabilidad de observar una variable cualitativa en función de variables cuantitativas. Podemos encontrar dos modelos de regresiones logísticas atendiendo al número de clasificadores posibles: simple o binaria, cuando trabajamos con modelos binarios de salida o múltiple si podemos tener varias salidas cualitativas para nuestros datos de entrada [9]. Pese a tratarse de un modelo de regresión se encuentra incluido dentro del grupo de algoritmos de clasificación debido a que su salida es categórica y no continua. La regresión logística se confunde a menudo con la regresión lineal, en la cual podemos intentar predecir un valor continuo de variables y que pertenece al grupo de los algoritmos de regresión. 

La construcción de un modelo de regresión logística se subdivide en dos partes 

- Una combinación lineal o regresión lineal a partir de la cual combinamos las distintas variables cuantitativas que estamos empleando como datos de entrada 

- Aplicación de una función logística o sigmoide con la que convertimos las variables obtenidas en la primera fase del algoritmo en un clasificador. Esta función pese a parecer complicada y arbitraria en su forma matemática tiene una forma bastante simple que podemos observar en la Ilustración X. Esta función tiene unas características que nos permiten interpretar sus resultados como probabilidades. Esta acotada entre 0 y 1, su valor mínimo es 0 y su valor máximo es 0. En función de los datos que hayamos empleado para el entrenamiento pondremos nuestro límite en un valor específico. Por ejemplo, en un problema de clasificación binaria podremos suponer que los valores menores a 0.5 corresponden con la clase 0 y los valores superiores a 0.5 a la clase 1. [10] 

14 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 6: Representación gráfica de la función sigmoide 

Un ejemplo sencillo de como podemos aplicar este tipo de funciones se trata de un problema clasificatorio muy común en lo manuales de iniciación a la inteligencia artificial. Se trata de identificar una base de datos con características de flores de iris en función de la especie a la que pertenecen: setosa, veriscolor y virginica. 

El conjunto de datos de flores de Iris o el conjunto de datos de Iris de Fisher es un conjunto de datos multivariado introducido por el estadístico y biólogo británico Ronald Fisher en su artículo de 1936 El uso de mediciones múltiples en problemas taxonómicos como ejemplo de análisis discriminante lineal. A veces se denomina conjunto de datos de iris de Anderson porque Edgar Anderson recopiló los datos para cuantificar la variación morfológica de las flores de iris de tres especies relacionadas. Dos de las tres especies fueron recolectadas en la península de Gaspé “todas del mismo pasto, y recogidas el mismo día y medidas al mismo tiempo por la misma persona con el mismo aparato”. 

15 

**Módulo. Machine Learning y Deep Learning** 

**Centro Europeo de Postgrado** 

Esta base de datos se encuentra incluida dentro del paquete de Python scikit-learn, y es muy utilizado debido a su simplicidad. Scikit-learn [11] es una biblioteca de software para el aprendizaje automática que podemos encontrar dentro de Python y que contiene los principales algoritmos de clasificación, regresión, análisis de grupos… A lo largo de este manual lo utilizaremos como herramienta principal para ejemplificar los distintos algoritmos que vamos a estudiar. 

La base de datos de Iris contiene datos de 150 flores con una serie de variables cuantitativas asociadas a ellas. 

El primer paso en la construcción de un modelo de inteligencia artificial es importar dentro de Python las distintas librerías que vamos a utilizar para trabajar con nuestros datos. 



Ilustración 7:Librerías empleadas en la creación del modelo de regresión logística 

El segundo paso es obtener la base de datos que vamos a emplear como entrenamiento. En nuestro caso vamos a utilizar una base de datos incluida dentro de la librería scikitlearn, por lo que podemos importarla directamente a Python sin necesidad de cargar la base de datos desde otros repositorios o podemos descargarla de un repositorio de bases de datos publicas como Kaggle y cargarla como archivo csv en Python. En este caso vamos a utilizar una base de datos ampliamente distribuida y empleada en múltiples ejemplos de iniciación a la inteligencia artificial, pero si estamos interesados en aprender a desarrollar modelos de inteligencia artificial, necesitaremos obtener bases de datos que podamos utilizar con este propósito. Kaggle es una plataforma colaborativa en la que podemos encontrar múltiples bases de datos abiertas disponibles para su descarga además de proyectos sobre esas mismas bases de datos desarrollados por la comunidad. 

Una vez tenemos nuestra base de datos disponible para su utilización, vamos a comenzar por explorar el tipo de datos que tenemos disponibles para la construcción de nuestro modelo de regresión logística. Al cargar nuestra base de datos hemos visto que las variables con las que vamos a trabajar son cuatro y corresponden con el alto y el ancho de los pétalos y los sépalos de las flores de Iris respectivamente. Podemos obtener mas información de nuestra base de datos analizando la cabecera de esta. En la Ilustración 8 podemos encontrar información sobre el tamaño de la base de datos, su estructura y la descripción de cada una de las variables. 

16 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 8: Carga de la base de datos 

Para comprender mejor como se distribuyen los datos dentro de nuestra base de datos podemos representarla de manera gráfica utilizando la librería de matplotlib que hemos importado en el primer paso. Esto nos permitirá crear distintos tipos de gráficos como histogramas (Ilustración 9) o graficas de dispersión (Ilustración 10).  A partir de estas gráficas podemos observar que las variables cuantitativas de las que disponemos dentro de nuestra base de datos crean agrupaciones visibles a simple vista, por lo qué podemos esperar que nuestro modelo de regresión logística sea capaz de diferenciar las distintas clases con bastante facilidad. 



Ilustración 9: Histograma de la variable petal width de los datos de entrenamiento 

17 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 10: Gráfica de dispersión de los datos de entrenamiento 

Para la creación del modelo tomamos los datos que hemos estado analizando y los dividimos en dos grupos: datos de entrenamiento y datos de validación. Para llevar a cabo la construcción de un modelo de machine learning es necesario separar los datos que tenemos disponibles en dos subconjuntos de datos para poder comprobar como esta funcionando nuestro modelo respecto a los valores reales que tenemos como referencia. Esto nos generará dos subconjuntos de datos, uno mayor que contendrá entorno al 80% de los datos disponibles y que se dedicará al entrenamiento y uno mas pequeño que contendrá el 20% de los datos restantes y que será empleado en la fase de prueba del algoritmo. 



Ilustración 11: Separación de datos de entrenamiento y test 

Una vez hemos dividido la base de datos que tenemos disponible para el entrenamiento obtenemos dos nuevas bases de datos, una en la que vamos a encontrar los datos destinados al entrenamiento del modelo con sus respectivas etiquetas que contienen la especie a la que pertenecen cada una de las entradas de la tabla y un segundo subconjunto de datos que contendrá los datos destinados a comprobar la precisión con la cual nuestro modelo es capaz de clasificar nuevos datos de entrada. 

18 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

En el código descrito en la Ilustración 11 podemos identificar el conjunto de datos de entrenamiento como la variable X_train y sus respectivas etiquetas como Y_train, mientras que el subconjunto de datos de test lo podemos identificar como X_validation y sus respectivas etiquetas como Y_validation. Para llevar a cabo la división de esta base de datos hemos establecido un peso del 80% para los datos de entrenamiento y un 20% para los datos de validación. Para garantizar la división aleatoria de la base de datos y evitar incluir ningún patrón a la hora de dividir nuestra base de datos, hemos incluido dentro de la función utilizada para realizar esta división un punto aleatorio a partir del cual la función debe dividir la base de datos. 

Con estos datos podemos crear un algoritmo que contenga la función LogisticRegression que hemos importado desde el paquete de scikit-learn [12]. Este algoritmo lo vamos a entrenar con los datos que hemos seleccionado como conjunto de entrenamiento haciendo uso de la función fit. Este proceso podemos verlo reflejado en el cuadro de código de la Ilustración 12. 



Ilustración 12: Función de regresión logistica 

En este punto ya hemos entrenado nuestro primer modelo de inteligencia artificial. Una vez tenemos nuestro algoritmo entrenado con nuestros datos de entrada debemos comprobar que nivel de precisión nos aporta a la hora de clasificar nuevos datos. Para ello vamos a utilizar los datos que hemos reservado como subconjunto de validación. 

En primer lugar, aplicamos el algoritmo sobre el conjunto de datos reservado X_validation, de donde obtenemos las predicciones realizadas por nuestro modelo sobre estos datos. A continuación, comprobamos la predicción que hemos obtenido con las etiquetas reales de estos datos mediante la función accuracy_score. En este caso podemos comprobar que la precisión que nos devuelve esta función es del 100%. Pese a que nuestro objetivo a la hora de construir un modelo es obtener la máxima precisión posible a la hora de realizar predicciones debemos ser cautos cuando obtengamos precisiones tan altas puede que estemos causando sobreajuste en nuestro modelo. Podemos causar sobreajuste en un modelo cuando lo entrenamos con muchos datos y durante el proceso de entrenamiento, este comienza a aprender del ruido presente dentro de base de datos, así como de las entradas inexactas. Esto provoca una mala categorización de los datos, por ello podemos obtener unos resultados de exactitud muy buenos cuando realizamos la validación del modelo ya que se emplea un subconjunto de la misma base de datos que hemos empleado en el entrenamiento, incluyendo el ruido y las inexactitudes. Si esto ocurre cuando exportemos nuestro modelo hacia la producción no vamos a obtener los mismos niveles de exactitud ya que los nuevos datos no van a seguir la misma estructura [13]. 

19 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 13: Validación del algoritmo de regresión logística 

En nuestro caso pese a haber obtenido un resultado muy alto de exactitud, no debemos de sospechar de sobreajuste u overfitting, ya que hemos utilizado una base de datos pequeña cuyas entradas contienen variables con mucha información. 

### **2.1.2. Clasificador Naive Bayes** 

El clasificado de Naive Bayes es uno de los algoritmos mas simples y mas empleados en problemas de clasificación. Este esta basado en el Teorema de Bayes y nos permite obtener buenos resultados sin necesidad de muchos recursos. El Teorema de Bayes fue propuesto por Thomas Bayes y publicado póstumamente en 1763 y es de enorme relevancia en el campo de las matemáticas ya que vincula la probabilidad de A dado B con la probabilidad de B dado A, resolviendo el problema de la “probabilidad inversa”. En el campo de la estadística existe cierta controversia sobre el tipo de probabilidad que emplea, ya que en la estadística clásica solo se admiten probabilidades basadas en experimentos repetibles mientas que los llamados estadísticos bayesianos permiten utilizar probabilidades subjetivas. 

Una de las características principales de este algoritmo es que se basa en la hipótesis de que las variables que utilizamos como predictores son independientes unas de otras, de ahí obtiene su nombre de naive o ingenuo. Además, este tipo de algoritmos también asume que todas las variables que se toman en consideración tienen el mismo valor o peso. Ninguno de los atributos de una base de datos es considerado como irrelevante y se asume que contribuye de manera equitativa a la predicción del modelo. Este tipo de algoritmos tienen un escalado bastante sencillo, por lo que en muchas ocasiones podemos encontrarnos con estos algoritmos como base de un modelo combinados con otros mas complejos y precisos desde un punto de vista computacional.[14] 

Para poder comprender como funciona este algoritmo primero debemos entender el concepto probabilístico que encontramos detrás de él. 

Como hemos dicho el algoritmo de clasificación de Naive Bayes se basa en la formula del teorema de Bayes. 

20 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Donde: 

- P(A) es la probabilidad a priori de que ocurra la hipótesis A 

- P(B) es la probabilidad a priori de que ocurra la evidencia B 

- P(B|h) probabilidad de que se de de la evidencia B cuando se cumple la hipótesis A 

- P(h|B) probabilidad de que se cumpla la hipótesis dado que la evidencia B ha ocurrido. 

Esta fórmula podemos interpretarla como la probabilidad de que se de la hipótesis dado que se ha producido el evento B, pero ¿en que consiste esta probabilidad condicional y como es posible calcularla? 

Un buen ejemplo para entender como funciona la probabilidad condicional es calcular la probabilidad de obtener un número concreto al lanzar un dado. Si yo lanzo un dado de seis caras al aire, la probabilidad que tengo de obtener como resultado el número dos es de 1/6. 



Pero ¿que ocurre si este dado de caras ya ha sido lanzado y se que ha caído en un número par? La probabilidad que tenemos ahora de obtener un dos en el resultado ha aumentado hasta ser de 1/3. Cuando tenemos información previa sobre la variable que pretendemos calcular esta afecta a los posibles resultados que vamos a obtener. 



21 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

En la definición del algoritmo de Naive Bayes hemos visto que este asume que las variables que estamos utilizando como predictores son independientes unas de otras. Eso quiere decir que la probabilidad de que ocurra el evento A no se va a ver afectada por la probabilidad de que ocurra el evento B, con lo cual podemos decir que la probabilidad de que ocurran los eventos A y B al mismo tiempo es la misma que la del producto de las probabilidades de A y B por separado. 



¿Cómo podemos aplicar esto a un clasificador de Naive Bayes? Vamos a verlo a través de un ejemplo. Supongamos que predecir la posibilidad de que un nuevo email en nuestra bandeja de entrada sea spam. Para poder realizar esta predicción tenemos una serie de datos de todos los emails que entran en nuestra bandeja de entrada: Si contiene o no imágenes adjuntas, si el remitente es conocido y si el email ocupa mas de 50kb. Podemos definir un posible email con las siguientes características: <Contiene imágenes, remitente desconocido y pesa mas de 50kb> 

||**Contiene**<br>**imágenes**|**Remitente**<br>**desconocido**|**Pesa mas de 50**<br>**Kb**|**Spam**|
|---|---|---|---|---|
|1|Si|No|Si|No|
|2|No|No|No|Si|
|3|No|No|Si|Si|
|4|Si|Si|No|No|
|5|No|No|Si|Si|
|6|No|Si|Si|No|
|7|No|Si|No|Si|
|8|No|Si|Si|Si|
|9|Si|No|Si|Si|
|10|No|Si|Si|No|
|11|No|Si|No|No|
|12|SI|No|No|Si|
|13|SI|SI|Si|No|
|14|Si|No|No|Si|
|15|No|No|Si|No|



Tabla 1: Base de datos de entrenamiento del algoritmo Naive Bayes 

22 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Con estos datos podemos plantear la probabilidad de que este email sea spam de la siguiente manera: 



Si la probabilidad de Spam es mayor que la probabilidad de que no sea spam entonces podemos clasificar el email como correo no deseado, de lo contrario podemos clasificarlo como correo útil y debe de ir a la bandeja de entrada. ¿Cómo calculamos estas probabilidades? Aplicando el Teorema de Bayes que acabamos de ver: 



Esto nos deja una formula compleja y muy costosa de calcular de manera manual, pero como hemos visto antes el teorema de Bayes se basa en la independencia de las variables unas de otras por lo que podemos reducir nuestra formula a la siguiente: 



Como el denominador de esta fórmula es constante para cualquier input que vayamos a introducir en el podemos eliminar ese término ya que no va a afectar a la salida de la fórmula. 



Esta formula es mucho mas sencilla de abordar y podemos calcular las probabilidades independientes de cada variable en función de los datos históricos que tenemos como datos de entrenamiento contando las entradas que están clasificadas como Spam y contenían la variable cuya probabilidad estamos tratando de analizar. 

23 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Si analizamos las probabilidades de nuestra base de datos de manera individual obtenemos los siguientes resultados 

|**Contiene**|**Spam**|**No Spam**|**P(Spam)**|**P(No**|
|---|---|---|---|---|
|**imágenes**||||**spam)**|
|Si|3|3|3/6|3/7|
|No|3|4|3/6|4/7|
|Total|6|7|100%|100%|



Tabla 2: Probabilidades variable imágenes 

|**Remitente**|**Spam**|**No Spam**|**P(Spam)**|**P(No**|
|---|---|---|---|---|
|**desconocido**||||**spam)**|
|Si|2|5|2/8|5/7|
|No|6|2|6/8|2/7|
|Total|8|7|100%|100%|



Tabla 3: Probabilidades variable remitente 

|**Pesa mas de**|**Spam**|**No Spam**|**P(Spam)**|**P(No**|
|---|---|---|---|---|
|**50kb**||||**spam)**|
|Si|4|5|2/8|5/7|
|No|4|2|4/8|2/7|
|Total|8|7|100%|100%|



Tabla 4: Probabilidades variable peso 

|**P(Spam)**|**P(No spam)**|
|---|---|
|8/15|7/15|



Tabla 5: Probabilidades Spam 

24 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Siguiendo los mismos pasos que en la formula original podemos derivar la formula para la hipótesis contraria 



Además como sabemos que la probabilidad total tienes que ser 1 podemos normalizar los siguientes resultados y obtener un porcentaje 



Como podemos comprobar la probabilidad de que un email con las características de <Contiene imágenes, remitente desconocido y pesa mas de 50kb> tiene un 86% de probabilidades de no ser spam y un 14% de probabilidades de si serlo, según el clasificador que hemos entrenado con nuestros datos de entrada. Sin embargo, el resultado de la clasificación va a venir determinado por el umbral que hayamos decidido definir en base a los ciclos de entrenamiento por los que haya pasado el modelo. Este no tiene por que estar definido siempre en el término medio de 50%, podemos establecer el umbral mas alto o mas bajo en función de los datos que tengamos de entrada y la importancia que le demos a los falsos positivos, falsos negativos, verdaderos positivos y falsos positivos. 

Este tipo de algoritmos tiene una serie de ventajas y desventajas que debemos de tener en cuenta a la hora elegirlo como el óptimo para nuestra tarea de clasificación 

25 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

#### Ventajas 

- Es un algoritmo fácil y rápido de aplicar y de entrenar. 

- Funciona bien en la predicción multi-clase 

- Requiere un menor volumen de datos de entrenamiento que otros clasificadores de tipo supervisado como puede ser la regresión logística. 

- Funciona bien con las entradas categóricas y nos permite integrar múltiples variables en los cálculos para clasificar datos 

- Es fácil de integrar con otros algoritmos por lo que podemos utilizarlo como una parte de un modelo compuesto de múltiples algoritmos. 

#### Desventajas 

- Asume que las variables actúan de manera independiente. En la vida real es muy raro encontrarnos con predictores completamente independientes, por lo que al utilizar este tipo de algoritmos perderíamos parte de la información contenida en la base de datos. 

- Asume que la distribución de los datos de entrenamiento es normal, lo cual es frecuente pero que debemos comprobar para cada caso específico. 

- Si alguna de las variables que estamos utilizando como entrada en nuestro modelo no tiene ninguna observación en los datos de entrenamiento, la probabilidad que se le asignará a la misma es de cero. En ese caso habría que implementar un sistema de corrección en los datos de entrada conocido como técnica de alisamiento, lo que aumentaría la complejidad y el tiempo de implementación del modelo. 

- El esfuerzo computacional requerido para entrenar el modelo aumenta a medida que añadimos características a nuestra base de datos. 

Pese a la simplicidad de este algoritmo su potencia hace que se haya implementado con éxito en muchas aplicaciones, desde el análisis de texto hasta algoritmos predictivos del diagnostico de cáncer. 

### **2.1.3. K-nearest Neighbours** 

El algortimo de K-nearest Neighbours o clasificador de vecinos cercanos es un algoritmo simple que se emplea generalmente en problemas de clasificación, pero también podemos encontrar ejemplos en los cuales este tipo de algoritmos se han empleado en problemas de regresión. Es un algoritmo muy versátil que también se emplea como herramienta de preprocesado de datos par imputar valores vacios y remuestrear conjuntos de datos. 

26 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Como sugiere el nombre (K vecino más cercano), considera K vecinos más cercanos (puntos de datos) para predecir la clase o el valor continuo para el nuevo punto de datos, asumiendo que las variables similares existen en proximidad. En la imagen del ejemplo podemos ver como los puntos de datos similares están cerca unos de otros. El algoritmo de clasificador de vecinos cercanos depende de que esta suposición sea lo suficientemente cierta para que este sea útil. 



Ilustración 14: Ejemplo de clasificación usando K-NN 

El algoritmo K-NN toma un montón de puntos etiquetados y los usa para aprender a etiquetar otros puntos. Este algoritmo clasifica los casos en función de su similitud con otros casos, así, los puntos de datos que están cerca entre sí se denominan “vecinos”. K-vecinos más cercanos se basa en este paradigma: “Casos similares con las mismas etiquetas de clase están cerca uno del otro.” El proceso que sigue este algoritmo para clasificar los nuevos puntos de entrada es el siguiente: 

1. Elegimos un valor k. Este determinará el numero de vecinos que vamos a tener en cuenta para clasificar nuestra nueva variable 

2. Calculamos la distancia desde nuestro nuevo caso a el resto de los casos de nuestros datos de entrenamiento 

3. Elegimos los k puntos mas cercanos a nuestra incógnita 

4. Predecimos la clase del punto de datos desconocido usando el valor de respuesta más popular de los K vecinos más cercanos. 

27 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Para entender como funciona este algoritmo vamos a verlo a través de un ejemplo gráfico. En la imagen podemos ver una serie de datos que pertenecen a dos clases diferentes y un nuevo dato que debemos clasificar en alguna de las dos clases 



Ilustración 15: Datos de clasificación K-NN 

En primer lugar, se selecciona un valor para k. Este valor va a determinar el numero de puntos vecinos que vamos a tener en cuenta a la hora de clasificar nuestra nueva variable. Si seleccionamos un valor para k=1 entonces nuestro algoritmo será conocido como algoritmo de vecino mas cercano. Este caso es el mas sencillo que nos podemos encontrar y pese a que dependiendo de la base de datos que empleemos podemos obtener un buen nivel de acierto no es recomendable emplear modelos tan sencillos, ya que podemos encontrarnos ante un outlier. En este caso como podemos comprobar, el punto mas cercano a nuestra nueva variable corresponde a clase B por lo tanto nuestra nueva variable se clasificaría como Clase B. 



Ilustración 16: Algoritmo de K-NN k=1 

28 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Sin embargo, si modificamos el valor de K, y en lugar de emplear solo el vecino mas cercano lo ampliamos hasta 3 u hasta 5 vemos que el resultado de nuestro algoritmo de clasificación cambia. 



Ilustración 18: Algoritmo K-NN k = 3 



Ilustración 17: Algoritmo K-NN k = 7 

En las graficas podemos observar que cuando escogemos los 3 vecinos mas cercanos para realizar la clasificación, nuestra incógnita es clasificada como Clase A mientas que si elegimos los 7 vecinos mas cercanos nuestra incógnita es clasificada como Clase B. ¿Entonces como debemos de elegir el número de vecinos óptimo para nuestro algoritmo? Esto va a depender de la base de datos con la que estemos trabajando, no existe un número de vecinos óptimo que podamos emplear en todos nuestros modelos. Si empleamos un número de vecinos muy pequeño el ruido va a tener una mayor influencia en el resultado, mientras que si elegimos un número muy grande tendremos un coste computacional muy alto, además de correr el peligro de caer en el infra-ajuste o underfitting. 

29 

**Módulo. Machine Learning y Deep Learning** 

**Centro Europeo de Postgrado** 

Al contrario que el overfitting, el underfiting aparece cuando el algoritmo no se encuentra suficientemente entrenado o no tiene suficientes datos de entrada lo que causa unos resultados poco ajustados. Habitualmente para calcular un correcto valor de K se llevan a cabo varios ciclos de entrenamiento y test del modelo para poder ajustar este parámetro. Generalmente se emplea un valor K impar cuando trabajamos con bases de datos pares, pero siempre debemos realizar un ajuste previo al entrenamiento final del algoritmo. [17,18] 

Otra variable que debemos tener en cuenta a la hora de definir nuestro algoritmo es la métrica que vamos a utilizar para calcular la distancia entre el punto que buscamos clasificar y los vecinos seleccionados. En la definición del algoritmo de K-NN se definen varias métricas estandarizadas, pero es común encontrar aplicaciones de K-NN con modificaciones de las mismas para adaptarlo a la base de datos empleada en el estudio.[19] 

**Distancia Euclidiana:** Es la métrica mas estandarizada y corresponde con la distancia en línea recta entre dos puntos dentro del espacio Ecluideo. Su fórmula es simple y se basa en la proyección en un plano 2D de los puntos cuya distancia tratamos de calcular. 





**Distancia Manhattan:** Esta métrica mide la distancia entre dos puntos en un espacio vectorial de N dimensiones. Es la suma de las longitudes de las proyecciones del segmento de línea entre los puntos en los ejes de coordenadas. En términos simples, es la suma de la diferencia absoluta entre las medidas en todas las dimensiones de dos puntos. Esta métrica es coloquialmente conocida como la métrica del taxista, ya que se podría equiparar a tomar el camino mas corto a través de las distintas calles que podemos recorrer en un mapa. 



30 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 19: Ejemplo gráfico de calculo de la distancia Manhattan 

En la figura del ejemplo, las líneas roja, azul y amarilla tienen la misma longitud. En la geometría clásica o euclidiana la línea verde es mas corta que las demás, mientras que en la geometría Manhattan la línea verde tiene la misma longitud que las líneas roja, azul y amarilla. 

**Distancia de Chebyshev:** En esta métrica definida dentro de un espacio vectorial “la distancia entre dos puntos es la mayor de sus diferencias a lo largo de cualquiera de sus dimensiones coordenadas”. Podemos entenderlo de una forma mas sencilla con el ejemplo del tablero de ajedrez. La distancia a cualquier casilla del tablero de ajedrez será tantas casillas tenga que recorrer moviéndome en cualquier dirección. 



Ilustración 20: Ejemplo gráfico de distancia de Chevyshev 

31 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Este tipo de algoritmo podemos programarlo de manera sencilla en Python utilizando librerías de inteligencia artificial incluidas dentro de la propia herramienta. Para ver como como podemos poner en práctica este algoritmo vamos a recuperar la base de datos que empleamos en nuestro primer algoritmo, la regresión logística. 

Esta base de datos consistía en entradas de datos de 150 flores de Iris, donde se recogían sus características respecto a el alto y ancho de sus pétalos y sépalos. Para este ejemplo vamos a seguir la misma estrategia que con el ejemplo de regresión logística. Comenzaremos por importar dentro de nuestro espacio de trabajo las librerías que vamos a utilizar para entrenar nuestro modelo. 



Ilustración 21:Librerias utilizadas para la creación del modelo de K-NN 

Vamos a utilizar los módulos integrados dentro del paquete de inteligencia artificial sklearn de Python. A continuación, cargamos la base de datos de Iris ya incluida dentro del paquete de sklearn. 



Ilustración 22: Carga de base de datos para el modelo K-NN 

Una vez tenemos nuestros datos disponibles, dividimos el set de datos en dos subgrupos, datos de entrenamiento y datos des test. Para ello tomamos un 20% para el conjunto de prueba extraídos de manera aleatoria. 



Ilustración 23: División de la base de datos en subgrupo de entrenamiento y test 

32 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

A continuación, importamos el algoritmo y realizamos el entrenamiento del mismo utilizando el subconjunto de datos de entrenamiento. Podemos obtener métricas de exactitud de nuestro algoritmo también con los datos que utilizamos para entrenar. Estas métricas no deben ser utilizadas en sustitución de las de validación, pero nos pueden ayudar a comprender como esta funcionado nuestro modelo. 



##### Ilustración 24: Entrenamiento del modelo de K-NN 



Finalmente aplicamos nuestro modelo al subconjunto de datos de test que hemos dejado reservado para comprobar la exactitud con la que esta trabajando nuestro modelo. 



Ilustración 25: Test del modelo de K-NN 



Si queremos obtener una representación mas visual de como ha funcionado nuestro algoritmo podemos representar graficas de dispersión en las cuales podemos distinguir que datos se han clasificado dentro de cada grupo respecto a los valores reales de estos grupos. En nuestro caso la grafica de dispersión que podemos observar representa la clasificación de cada uno de los datos de entrada en sus posibles clases representados a través de las variables de ancho y largo de sépalo. 

33 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 26: Gráfica de dispersión del modelo de K-NN 

El principal caso de uso del algoritmo de vecinos cercanos son los sistemas de recomendación basados en nuestro comportamiento. Por ejemplo, el algoritmo que utiliza Netflix o HBO para recomendarte series y películas esta basado en un modelo de K-NN. Toma como datos de entrada las películas que ya has visto, las que has valorado de manera positiva o negativa, y los géneros que mas visualizas. Pero para calcular sus recomendaciones no solo emplea tus datos, si no los datos de millones de personas con un perfil similar al tuyo. Si una persona con la que coinciden tus películas mejor valoradas le ha gustado un nuevo estreno es mas probable que la plataforma de video te lo muestre a ti aunque sea un género con el que no estas familiarizado, que una película de un genero que sueles consumir pero que a perfiles similares al tuyo no les ha gustado. 

Otro caso de uso bastante común de este tipo de algoritmos es la búsqueda en base a conceptos. La información almacenada electrónicamente de manera no estructurada es complicada de organizar, por ello para acceder a ella se emplean motores de búsqueda basados en conceptos, es decir buscan la información basándose en las ideas que esta expresa. [20] 

Emplear este tipo de algoritmos tiene una serie de ventajas y de desventajas respecto a otros sistemas de clasificación 

Ventajas: 

- Es un algoritmo sencillo, tanto a nivel implementación como de explicar. 

- Sin suposiciones sobre los datos: útil, por ejemplo, para datos no lineales 

34 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- Alta precisión (relativamente): es bastante alta pero no competitiva en comparación con mejores modelos de aprendizaje supervisado 

- Versátil: útil para clasificación o regresión 

Desventajas: 

- Requiere muchos recursos computacionales ya que el algoritmo almacena todos los datos de entrenamiento 

- Alto requerimiento de memoria 

- La etapa de predicción puede ser lenta 

- Sensible a las características irrelevantes y la escala de los datos. 

### **2.1.4. Support Vector Machine (SVM)** 

El método de clasificación-regresión Máquinas de Vector Soporte (Support Vector Machines, SVMs) fue desarrollado en la década de los 90, dentro de campo de la ciencia computacional. Se presentó en Se presento en COLT-92 (Boser, Guyon, Vapnik)[22]. Si bien originariamente se desarrolló como un método de clasificación binaria, su aplicación se ha extendido a problemas de clasificación múltiple y regresión. Aunque su utilización es mas frecuente en ejemplos de clasificación podemos encontrar casos en los que se emplea como algoritmo de regresión cuando trabajamos con variables numéricas (no categóricas). Este tipo de algoritmos es frecuentemente utilizado por los científicos de datos ya que pese a ser un algoritmo relativamente sencillo matemáticamente hablando, tiene un gran poder de predicción, produciendo modelos con buenos niveles de exactitud cuando se emplea de manera correcta. Además, este algoritmo cuenta con la ventaja de ser computacionalmente eficiente frente a otro tipo de algoritmos que nos permite producir los mismos niveles de exactitud. El algoritmo de Support Vector Machine esta basado en el concepto de hiperplano y Maximal Margin Classifier. El análisis en profundidad de estos conceptos requiere un conocimiento previo en algebra lineal y teoría de cálculo por lo que no vamos a adentrarnos en el transforndo matemático del mismo. Un buen libro para profundizar en este tema es “The Nature of Statistical Learning Theory (Information Science and Statistics) de Vladimir Vapnik [22]. En esta guía docente vamos a introducir los conceptos de manera general para comprender el funcionamiento de este algoritmo y cuales son sus posibles aplicaciones. 

35 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

En primer lugar, debemos comprender cual es el objetivo de este tipo de algoritmos. Este tipo de algoritmos busca clasificar los puntos de un conjunto de datos en grupos, empleando un hiperplano que divida estos grupos, por lo tanto, el objetivo de entrenamiento de este algoritmo es encontrar ese hiperplano que nos permita realizar esta clasificación. Pero ¿Qué es un hiperplano? Los hiperplanos son límites de decisión que ayudan a clasificar los puntos de datos. Los datos van a encontrarse a un lado u al otro del hiperplano dependiendo a que clase pertenezcan. La dimensión del hiperplano depende del número de características o variables que empleamos para construirlo. Por ejemplo, si el número de variables de entrada es 2, entonces el hiperplano es solo una línea en un plano. Sin embargo, si el número de variables de entrada es 3, el hiperplano se convierte en un plano bidimensional. Estos dos ejemplos podemos representarlos gráficamente de manera sencilla en la Ilustración 24. 



Ilustración 27: Ejemplo de hiperplano en 2 dimensiones y 3 dimensiones [23] 

Cuando el número de dimensiones empleadas en la construcción del hiperplano aumenta es difícil imaginárnoslo de manera gráfica, pero siempre va a seguir el criterio de p-1, donde p será el número de variables empleadas en la construcción del hiperplano. 

Un hiperplano en dos dimensiones lo podemos definir matemáticamente con la ecuación de una recta 



Ecuación de un hiperplano en dos dimensiones 

36 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Para un mismo grupo de datos den entrenamiento pueden existir múltiples hiperplanos que nos permitan dividir las diferentes clases. En la Ilustración 25 podemos ver un ejemplo de una división de dos subgrupos de datos con distintos posibles hiperplanos. ¿De que manera podemos determinar cual es el mejor hiperplano para dividir el espacio que determinará en que grupo serán clasificados los datos? 



Ilustración 28: Conjunto de posibles hiperplanos de división 

La solución a este problema consiste en seleccionar como clasificador óptimo al que se conoce como maximal margin hyperplane o hiperplano óptimo de separación, que se corresponde con el hiperplano que se encuentra más alejado de todas las observaciones de entrenamiento. Para ello se calcula la distancia entre los posibles hiperplanos y los puntos de entrenamiento, buscando maximizar todo lo posible esta distancia. Los puntos que se encuentra mas próximos al hiperplano se conocen como los Support vectors y son los que nos van a ayudar a determinar la posición y orientación de nuestro hiperplano. 



Ilustración 29: Maximización del margen de los vectores de soporte 

37 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

El hiperplano que acabamos de describir en el ejemplo anterior es muy simple, y se basa en un conjunto de datos para el cual existe un hiperplano de separación que podemos maximizar de manera directa. Los datos que vamos a encontrar en la vida real no van a mostrar un comportamiento tan lineal y no siempre vamos a poder definir un hiperplano que permita dividirlos. Además, en el caso de poder encontrar un hiperplano que nos permita separar nuestros datos en dos clases de manera ideal va a presentar una serie de inconvenientes. En primer lugar, un hiperplano que divida perfectamente el conjunto total de los datos va a ser muy sensible a la incorporación de nuevos datos, por lo que una ampliación de los datos de entrenamiento puede causar grandes modificaciones en el hiperplano. En este caso estaríamos ante un ejemplo de un modelo poco robusto. Otro aspecto que debemos tener en cuenta a la hora de utilizar un clasificador que permita separar perfectamente el conjunto de datos es que corremos el riesgo de sobreentrenar nuestro modelo. Si el hiperplano que definimos para separar los conjuntos de datos se ajusta de manera ideal a los datos de entrenamiento, cuando pongamos este modelo en producción con nuevos datos estos van a presentar una distribución que no se ajuste de manera ideal a los datos de entrenamiento por lo que la exactitud de nuestro modelo se va a ver reducida. 



Ilustración 30: Ejemplo de hiperplano ajustado 

Para evitar estas situaciones cuando se desarrolla un modelo de vector de soporte se permite emplear hiperplanos que, aunque no separe perfectamente las dos clases, sean más robusto y tengan mayor capacidad predictiva al aplicarlo a nuevas observaciones. En estos casos es incluso posible emplear un hiperplano que no separe de manera ideal las clases de nuestra base de datos, si no que permita un pequeño volumen de errores que maximicen el ajuste de las predicciones futuras. 

38 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Otro ejemplo de datos que podemos encontrar es aquellos en los que los datos no pueden clasificados de manera lineal en un plano de dos dimensiones. Esto no quiere decir que no puedan ser clasificado en espacios de mayores dimensiones. Un ejemplo es el que podemos encontrar en la Ilustación 31. Este conjunto de datos en dos dimensiones esta aparentemente bien definido, pero no podemos separarlo utilizando un hiperplano en dos dimensiones. En estos casos lo que debemos hacer es añadir una tercera dimensión. En este caso vemos que los datos si pueden ser clasificados empleando un hiperplano lineal. En esto consisten las máquinas de vector soporte. Nos permiten definir limites de separación lineales en espacios multidimensionales que se convierten en limites de separación no lineales si los proyectamos en el espacio original de nuestros datos. 



Ilustración 31: Ejemplo de datos no separables linealmente en dos dimensiones 

En la Ilustración 29 podemos observar como al añadir una nueva dimensión a nuestro conjunto de datos estos pasan a poder ser separados de manera lineal. 

Esto se conoce como funciones tipo kernel y es la base sobre la que se sustenta el funcionamiento de las máquinas de vector soporte. 



Ilustración 32: Ejemplo de datos separables linealmente en tres dimensiones 

39 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Vamos a ver un ejemplo de como podemos implementar una máquina de vector soporte de manera sencilla en Python. Para ello vamos a utilizar la base de datos de Iris que hemos utilizado en ejemplos anteriores. La versatilidad de esta base de datos la hace idónea para probar sobre ella distintos métodos de clasificación y contrastar sus resultados. 

Siguiendo los mismos pasos que en ejemplos anteriores empezamos por cargar las librerías que vamos a emplear en la construcción de nuestro modelo. 



##### Ilustración 33: Librerias utilizadas en el modelo SVM 

En segundo lugar, vamos a cargar nuestra base de datos. En este ejemplo solo vamos a utilizar en nuestro clasificador las dos primeras características de la base de datos ya que queremos construir un clasificador lineal en un kernel de dos dimensiones. 



##### Ilustración 34: Carga de base de datos para SVM 

Definimos nuestro algoritmo utilizando la base de datos de sklearn y realizamos el ajuste con nuestra base de datos de entrenamiento. 



Ilustración 35:Ajuste del modelo SVM a la base de datos de entrenamiento 

Con esto hemos generado un clasificador que nos permite dividir nuestra base de datos en los tres grupos que contiene en base a las dos primeras características de la misma. 

40 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 36: Clasificación SVM 

Este tipo de clasificador se podría ampliar incluyendo el resto de la base de datos y el número de dimensiones definidas en el kernel. En la Ilustración 36 podemos ver el resultado de la clasificación que acabamos de llevar a cabo. 

Este tipo de algoritmos al igual que el resto de los algoritmos que podemos encontrar dentro del mundo de la inteligencia artificial presenta una serie de ventajas e inconvenientes que debemos tener en cuenta a la hora de ponerlo en práctica con nuestros datos. 

Ventajas: 

- Es un algoritmo eficaz en espacios de grandes dimensiones o variables. 

- Mantiene su eficacia en casos donde encontramos un mayor número de dimensiones respecto al número de datos o muestras del que disponemos para realizar el entrenamiento. 

- Eficiente computacionalmente en términos de memoria, ya que conserva en memoria la función de decisión o vector de soporte. 

- Versátil: se pueden especificar diferentes funciones de kernel para la función de decisión, que pueden ser personalizadas para cada subconjunto de datos. 

Deventajas: 

- El algoritmo es propenso a sobreajustarse, si el número de características es mucho mayor que el número de muestras. 

- No proporcionan directamente estimaciones de probabilidad, que son deseables en la mayoría de los problemas de clasificación. 

41 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- No son muy eficientes desde el punto de vista computacional de cálculo, si su conjunto de datos es muy grande, como cuando tiene más de mil filas. 

Y ahora, nuestra pregunta final es: “¿En qué situación debo usar SVM?” Bueno, SVM es bueno para tareas de análisis de imágenes, como la clasificación de imágenes y el reconocimiento de dígitos escritos a mano. Además, SVM es muy efectivo en tareas de minería de textos, particularmente debido a su efectividad en el manejo de datos de alta dimensión. Por ejemplo, se utiliza para detectar spam, asignación de categorías de texto y análisis de sentimientos. Otra aplicación de SVM es la clasificación de datos de expresión génica, nuevamente, debido a su poder en la clasificación de datos de alta dimensión. SVM también se puede usar para otros tipos de problemas de aprendizaje automático, como la regresión, la detección de valores atípicos y la agrupación en clústeres. 

### **2.1.5. Árboles de Decisión** 

Los árboles de decisión son un método de aprendizaje supervisado que se puede utilizar tanto en problemas de clasificación como de regresión. El objetivo es crear un modelo que prediga el valor de una variable de destino mediante el aprendizaje de reglas de decisión simples basadas en si o no, inferidas de los datos de entrenamiento. 

El proceso de creación de un árbol de decisión es sencillo, se divide de manera sucesiva las variables de predicción en nodos terminales en base a la frecuencia de sus datos de entrada, empleando particiones recursivas para clasificar los datos. La principal dificultad a la hora de construir arboles de decisión radica en la elección de las variables en base a las cuales se van a dividir los datos. Para ello se emplea lo que se conoce como medida de selección de atributos. Dentro de estas medidas podemos encontrar varias técnicas, pero las mas utilizadas en machine learning son dos: Ganacia de información y método Gini. [24,25] 

**Ganancia de información:** Esta técnica se basa en la medición en los cambios de entropía de los datos una vez hemos realizado la división. A la hora de construir un árbol de decisión siempre debemos tratar de maximizar la ganancia de información y minimizar la entropía de los datos. La fórmula que se emplea en la ganancia de información se basa en la propiedad estadística que mide que tan bien un atributo dado separa los ejemplos de entrenamiento de acuerdo con la clasificación final que se pretende obtener. 

42 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Para poder calcular la ganancia de información de un nodo al siguiente necesitamos calcular la entropía de cada uno de los nodos. El concepto de entropía en flisica se conoce como el grado de desorden molecular de un sistema. Si extrapolamos esta definición a datos de clasificación podemos considerar la entropía como el grado de pureza que contienen nuestros nodos. Por ejemplo, si yo estoy tratando de clasificar un grupo de personas por género, un nodo en el cual solo contengo datos de hombres es un nodo con baja entropía por lo tanto se considera como puro, mientras que si tengo un nodo en el cual encuentro un 30% de hombres un 70% de mujeres este nodo contendría un nivel alto de desorden por lo cual no podríamos considerarlo como puro. La fórmula que se emplea para calcular la ganancia de información y determinar si el clasificado que hemos elegido es el óptimo para construir nuestro árbol de decisión es la siguiente. 



Mientras que la entropía podemos calcularla con la siguiente fórmula: 



Donde podemos identificar a p y a q como la probabilidad de que nuestra predicción sea correcta en ese nodo. Podemos ver esto con un ejemplo. Supongamos que tenemos una clase de colegio en la cual queremos clasificar a los alumnos en base a si practican deporte o no. Conocemos distintas variables de la clase como el género y la nota media del curso. Como dato de entrada de entrenamiento sabemos que hay un 50% de un total de 30 alumnos que practican deporte. 

Calculamos la entropía de nuestro nodo original: 



43 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Y después planteamos dos escenarios, el primero en el que dividimos a nuestra clase en función de su género: 



Ilustración 37: División de nodo de árbol de decisión por género 



Por lo tanto, la entropía total del nodo es la siguiente: 



Y la ganancia total de información por división de género es 1- 0,68 = 0,32 

Si realizamos el mismo cálculo para la variable de nota media obtenemos el siguiente esquema. 

44 

**Módulo. Machine Learning y Deep Learning** 

**Centro Europeo de Postgrado** 



Ilustración 38: Ejemplo nodo árbol de decisión división por notas 

De nuevo calculamos la entropía de todos los nodos 



La entropía media de estos nodos es 



La ganancia de información si llevamos a cabo esta división es de 1-0,99= 0,01. 

Si comparamos ambos resultados podemos ver que la ganancia de información cuando dividimos a la clase por género es mayo que si dividimos a la clase en función de sus notas para clasificar a los alumnos en base a si son deportistas o no. 

45 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

**Índice de Gini:** El índice de Gini también se basa en la pureza o impureza de las decisiones que tomamos a la hora de definir las divisiones de nuestro árbol. Esta se basa únicamente en divisiones binarias. Cuanto mas alto sea el valor del Índice de Gini mayor será la homogeneidad. 

El Índice de Gini se calcula con la siguiente fórmula: 



Donde p y q son las probabilidades de éxito y de fracaso en la clasificación de nuestro nodo respectivamente. Si volvemos al ejemplo que hemos visto antes podemos calcular el Índice de Gini para ambas opciones de división de nodo. 

En el caso de división por género, en el caso de las mujeres teníamos un 60% de posibilidades de que la alumna seleccionada sea deportista (12/20) y un 40% de que no lo sea (8/20). El cálculo del índice de Gini para el grupo de mujeres es el siguiente 



Mientras que el Índice de Gini para el grupo de los hombres teniendo en cuenta que tenemos un 30% de posibilidades de que el alumno seleccionado sea deportista (3/10) y un 70% de que no lo sea (7/10). 



Si ponderamos este índice entre ambos nodos obtenemos el siguiente resultado para la división por género. 



Si aplicamos la misma fórmula en caso de dividir a los alumnos en función de sus notas obtenemos los siguientes índices de Gini: 

Los alumnos con buenas notas tienen un 43% de posibilidades de ser deportistas (6/14) y un 57% de no serlo, mientras que los alumnos con malas notas tienen un 56% de posibilidades de ser deportistas (9/16) y un 44% de no serlo. 



46 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Por lo tanto, podemos calcular el índice de Gini ponderado para este nodo como: 



Con estos datos podemos comprobar que el Índice de Gini es mayor para la división en caso de género por lo tanto emplearemos esta variable como clasificador. 

La medida del Índice de Gini se emplea como selector de atributos en los arboles CART (Clasiffication and Regression Tree), algoritmo mas frecuente dentro de los árboles de decisión empleados en machine learning. 

Este tipo de algoritmos al igual que el resto de algoritmos tiene una serie de ventas e inconvenientes a la hora de aplicarlo. 

#### Ventajas 

- Son fáciles de construir, interpretar y visualizar. 

- Emplean una selección de las variables mas importantes de todas las disponibles, reduciendo el procesado de predictores. 

- No requiere de ningún supuesto previo en los datos como normalidad o linealidad 

- Pueden emplearse como método de clasificación y regresión ya que admiten variables cualitativas y cuantitativas como predictores 

- Permiten relaciones no lineales entre las variables explicativas y la variable dependiente. 

#### Desventajas 

- En caso de bases de datos incompletas no podremos recorrer el árbol completo, pero si hacerlo de manera parcial. 

- Tienden al sobreajuste u overfitting de los datos, por lo que el modelo al predecir nuevos casos no estima con el mismo índice de acierto. 

- La creación de este tipo de modelos se ve afectado por la presencia de outliers en los datos por lo que se debe realizar un preprocesado de los mismos. 

- Pueden aparecer sesgos cognitivos si una de las clases a clasificar es mucho mas frecuente que otra. 

47 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

### **2.2. Regresión** 

Los algoritmos de regresión tienen como objetivo establecer una relación entre las variables descriptoras de los datos de entrenamiento y una variable objetivo que varia dentro de un rango continuo que tratamos de predecir. Este tipo de algoritmos   pueden enmarcarse en algoritmos de aprendizaje supervisado ya que este tipo de algoritmos son entrenados empleando datos de entrada etiquetados.  Dentro de los algoritmos de regresión encontramos un subconjunto especifico de algoritmos clasificados como algoritmos de Deep learning o aprendizaje profundo que   son estudiados de manera independiente. 

Existen múltiples algoritmos de regresión disponibles actualmente. A lo largo de este capitulo haremos un repaso de los mas empleados y sus aplicaciones. 

### **2.2.1. Regresión lineal** 

La regresión lineal es una de las técnicas mas utilizadas en machine learning. Su fortaleza unida a su simplicidad hace que sea un algoritmo frecuentemente utilizado de manera autónoma o combinada con otros tipos de algoritmos. Esta es además una técnica muy interpretable lo cual facilita su utilización en modelos que requieran ser transparentes, un requisito cada vez mas extendido a la hora de implementar modelos de inteligencia artificial por las empresas. [26] 

Este tipo de modelos ha sido importado desde el ámbito de la estadística y trata de explicar la relación que existe entre una variable dependiente Y (variable que tratamos de predecir) y un conjunto de variables independientes X1, X2,…Xn (predictores o variables explicativas. Este algoritmo en su forma mas simple consite en la ecuación de una línea recta. 



Donde X es la variable predictora, m es la pendiente de la curva y b la constante de la ecuación. El objetivo del entrenamiento de este tipo de modelos es encontrar cuales son los parámetros óptimos para los datos de entrada. Para encontrar estos coeficientes debemos minimizar alguna métrica de error. En el caso de la regresión lineal la métrica mas comúnmente utiliza es el error cuadrático medio o MSE por sus siglas en ingés Mean Squared Error. Esta métrica podemos calcularla por medio de la siguiente fórmula: 



48 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Esta formula representa la media de la de los cuadrados de los errores.  Además de el MSE podemos emplear otro tipo de métricas de optimización numérica como el gradiente descendiente. Este último método no va a servir únicamente para resolver regresiones lineales y polinómicas si no que es también fundamental para el aprendizaje automático de redes neuronales y aprendizaje profundo. El gradiente descendiente podemos calcularlo por medio de derivadas parciales de la función de coste. Calcular este tipo de gradientes requiere la aplicación de bases de cálculo avanzado. Para evitarnos tener que realizar este tipo de cálculos podemos emplear las librerías disponibles dentro de las herramientas de programación, donde estas funciones ya se encuentran predefinidas.[27] 

Para entender como funciona este tipo de modelos vamos a verlo a través de un ejemplo gráfico construido en Python. Para este ejemplo, en lugar de tomar una base de datos de código abierto vamos a construir la nuestra. Comenzamos por importar los paquetes de código que vamos a necesitar en este ejemplo. 



Ilustración 39: Módulos empleados en el algoritmo de regresión lineal 

Una vez tenemos las herramientas que vamos a utilizar disponibles, construimos nuestra base de datos. En este caso vamos a tratar de buscar la relación entre el número de horas estudiadas por un alumno y la nota que obtiene en su examen final. Para ello cosntruimos un DataFrame en el que incluimos los datos de las horas estudiadas por cada alumno y las respectivas notas que han obtenido en su examen final. Podemos construirlo con las siguientes líneas de código descritas en la Ilustración 40. 



Ilustración 40: Base de datos utilizada para el algoritmo de regresión logística 

49 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Si dibujamos estos datos podemos observar que a simple vista presentan una relación linear como se puede ver en la Ilustración 38. 



Ilustración 41: representación gráfica de la base de datos empleada para el algoritmo de regresión lineal 

Utilizando estos datos podemos construir un modelo de regresión lineal utilizando la librería de sklearn que hemos importado al principio del ejemplo. 



Ilustración 42: Entrenamiento del modelo de regresión lineal 

Podemos obtener los parámetros que conforman esta regresión lineal con las siguientes líneas de código 



Ilustración 43: Coeficientes regresión lineal 

De aquí podemos obtener la ecuación de nuestra recta, que en este caso será: 



50 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Si representamos gráficamente esta línea sobre sobre nuestra base de datos obtenemos el siguiente resultado. 



Ilustración 44: Representación grafica de la regresión lineal 

Empleando esta fórmula podemos predecir la nota que obtendrá un estudiante en su examen final en base al número de horas que haya estudiado. Supongamos que tenemos un nuevo estudiante en clase que ha dedicado 12 horas a la preparación del examen final. Aplicando la fórmula de regresión podemos calcular que obtendrá una nota de 91.2 puntos sobre 100 



Para poder emplear este tipo de aproximación a la hora de realizar una regresión logística nuestros datos de entrada deben de cumplir una serie de supuestos. 

- **Independencia:** Las variables utilizadas en los datos de entrada deben ser independientes unas de otras. 

- **Homocedasticidad (igualdad de varianzas):** La diferencia de errores que calculamos en el error cuadrático medio para construir la ecuación debe ser similar sea cual sea el valor que tome X 

- **Distribución normal** de los datos de entrenamiento. 

51 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Esta serie de supuestos hacen que la regresión lineal presente una serie de limitaciones a la hora de su aplicación. 

- Sólo podemos aplicarla en caso de tener relaciones lineales dentro de nuestras varibles, lo cual no siembre es correcto. 

- Al asumir una distribución normal de los datos y una homocedasticidad es muy sensible a datos anómalos y outliers. 

Aun así, este algoritmo es uno de los más utilizados dentro de la inteligencia artificial debido a su sencillez y robustez. Algunas de las aplicaciones que podemos encontrar de las regresiones lineales se encuentran dentro de los sectores financieros y de márketing por su facilidad para tratar datos numéricos con muchas características. 

Además, dentro de la ciencia de datos son empleados muy frecuentemente para realizar el análisis de un conjunto de datos previo a su entrenamiento para determinar cual es el modelo optimo que debe ser aplicado. 

### **2.2.2. Técnicas de Regularización** 

La regularización consiste en una serie de técnicas que empleadas para prevenir el sobre entrenamiento de los modelos de regresión lineal. Estas estrategias incorporan penalizaciones al modelo a medida que la complejidad del mismo aumenta, para tratar de reducir el overfitting, la varianza y tratar de reducir el impacto en el modelo de los predictores con menor relevancia. Aplicando este tipo de técnicas se obtienen modelos con un mayor poder predictivo asi como mejorar la interpretabilidad del modelo. 

**Precisión de la predicción:** Si los predictores tienen una relación lineal con la variable respuesta, entonces los algoritmos de regresión lineal tendrán un sesgo bajo, sin embargo, si nos encontramos con pocas variables predictoras, vamos a tener una fuerte variabilidad en el ajuste por minimos cuadrados, dando lugar a predicciones segadas. 

**Interpretabilidad del modelo:** En una regresión lineal sin correcciones se incluyen todas las variables predictoras disponibles podemos dar lugar a un modelo con una excesiva complejidad dado por variables. Un ajuste de este tipo de modelos consiste en eliminar las variables irrelevantes del modelo, ajustando a cero el coeficiente de estas variables, generando un modelo mas sencillo de intepretar. 

Las técnicas de regularización tienen como objetivo aumentar la precisión del modelo asi como su interpretabilidad. Existen múltiples técnicas para llevar a cabo la regularización de un modelo, en este módulo estudiaremos los princicipales modelos lineales generalizados y los mas utilizados. [28] 

52 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

#### **_Modelo de regresión de Ridge_** 

La regresión de Ridge es una técnica de regularización por la cual se penaliza el peso de los coeficientes de predicción de las características predictivas. De esta forma reduce de forma proporcional el valor de todos los coeficientes del modelo, sin que estos lleguen a ser cero. Esto facilita que las variables predictivas se encuentren todas dentro de la misma escala, evitando que predictores con un valor muy alto produzcan desviación en la predicción. 

El modelo de regresión de Ridge se rige por la siguiente fórmula, en la que el parámetro λ define la penalización de que va a sufrir un coeficiente. 



Hay que recordar que la suma de los residuos cuadrados es el error que tratamos de minimizar para calcular nuestro modelo de regresión. A medida que el valor de λ aumenta mayor es la penalización a ese predictor, mientras que si el valor de λ es 0 ese predictor no sufrirá ninguna penalización. La desventaja de este modelo de regularización es que se incluyen todos los predictores, porque, aunque λ sea muy grande, la penalización al predictor nunca va a ser cero (salvo que λ = ∞ ). Esto no supone un problema en la predicción del modelo, pero si en su interpretabilidad ya que vamos a tener todos los coeficientes de entrada generando un modelo complejo. 

#### **_Modelo de regresión de Lasso_** 

El modelo de regresión de Lasso al igual que el modelo de regresión de Ridge consiste en un método de regularización por el cual se tratan de ajustar los coeficientes de la regresión. En este caso el modelo de regresión de Lasso penaliza el valor absoluto de los coeficientes de regresión por lo que el efecto que produce en la ecuación es que los coeficientes de los predictores tiendan a cero. Dado que un predictor con coeficiente cero no influye en el modelo de predicción, Lasso si selecciona las variables que van a estar incluidas en el modelo de regresión. Podemos definir la fórmula de regresión de Lasso de la siguiente manera 



Igual que en el modelo de Ridge en el modelo de Lasso la penalización esta controlada por el parámetro de λ por lo que cuando λ =0 el predictor no sufrirá ninguna penalización y cuando este aumente mayor será la penalización 

53 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

#### **_Comparación entre Lasso y Ridge_** 

La principal diferencia que vamos a encontrar entre realizar la rgularización de nuestro modelo utilizando el método de Lasso o el de Ridge es la eliminación de algunos componentes. Mientras que Ridge puede reducir el peso de algunas variables, Lasso elimina de la ecuación las variables que no son importantes para predecir la variable objetivo. La segunda diferencia que podemos encontrar entre estos dos modelos de regularización se encuentra en la selección de variables predictoras correlacionadas entre si. Si tenemos varias variables que nos aportan el mismo tipo de información al modelo, la regresión de Ridge va a reducir la influencia de todas ellas de forma proporcional para evitar que su sobrerrepresentación afecte al resto de variables, mientras que la regresión de Lasso seleccionará una única variable de aquellas correlacionadas y eliminará el resto para evitar su sobrerrepresentación. 

Una forma de combinar ambos modelos de regularización se conoce como Elastic Net, una estrategia que combina ambas propiedades buscando un equilibrio dentro de la ecuación. [29] 

### **2.2.3. Stepwise Regression** 

La regresión de Stepwise es un tipo de modelo de regresión caracterizado por la construcción del modelo regresivo de manera iterativa. Este tipo de modelos se desarrollaron como un método de selección de variables para su aplicación en los modelos de regresión lineal, ya que su objetivo final es construir un modelo de regresión con los mejores clasificadores disponibles. Este tipo de modelos se construyen de manera iterativa, añadiendo o eliminando variables en cada ciclo y comprobando el resultado que se obtiene después de cada iteración. Este tipo de modelos pueden construirse por medio de tres aproximaciones: 

- **Forward selection o selección hacia adelante:** La construcción del modelo parte de cero, las variables se van añadiendo al modelo una a una y tras cada una de ellas se observa el efecto que la nueva variable produce en la exactitud del modelo. Esto se realiza mediante el análisis estadístico de la salida del modelo, manteniendo únicamente las variables que se consideran estadísticamente significativas. 

- **Backward selection o selección hacia atrás:** La construcción del modelo funciona de manera inversa a selección hacia adelante. Se parte de un modelo de regresión en el que se incluyen todas las variables disponibles y se van eliminando del modelo de manera iterativa. Tras cada ciclo en el que se ha eliminado una variable se realiza un análisis estadístico de la salida del modelo resultante y si esta variación es estadísticamente significante, se considera que esa variable tiene un peso significativo dentro del modelo y debe ser utilizada en la regresión 

54 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- **Eliminación bidireccional:** Este último método es una combinación de los dos anteriores, en cada uno de los ciclos variables pueden ser añadidas o eliminadas. De la misma manera se realiza un análisis estadístico de las mismas para comprobar si el cambio en el modelo ha sido significativo o no. 

El criterio que se sigue de manera general para determinar si una variable va a formar parte de del modelo de regresión se basa en el valor p estadístico. Este valor define la significancia estadística de la variable, en estadística se utiliza como determinante a la hora de definir si una hipótesis nula es rechazada o aceptada. Un criterio de entrada típico es que un valor p debe ser inferior a 0,15 para que una variable entre en el modelo y debe ser superior a 0,15 para que una variable abandone el modelo. En el ejemplo de selección hacia adelante, se crea un conjunto de modelos N, donde N es el numero total de variables disponibles para realizar la regresión y se selecciona aquel con un mayor peso estadístico. En el siguiente ciclo del modelo se añade una nueva característica al modelo y si el peso estadístico del modelo es inferior a 0.15 la nueva variable es incluida dentro del modelo. [30] 

Este tipo de selección de variables tiene una serie de inconvenientes. En primer lugar corremos el riesgo de incluir variables que no tengan un peso estadístico significativo real ya que en el proceso de creación de este tipo de modelos repetimos constantemente la misma hipótesis nula: Este predictor no añade información significativa al modelo. Este problema se hace mas frecuente cuando en el conjunto de predictores encontramos variables con mucha correlación entre ellas. En segundo lugar, corremos el riesgo de generar sobreentrenamiento del modelo u overfitting debido a la correlación de las distintas variables que incluimos dentro del modelo. 

Un ejemplo de como podemos llevar a cabo la selección hacia atrás de variables es tratar de construir un modelo de regresión en el cual tratemos de predecir la demanda de electricidad de una ciudad. Entre las variables vamos a encontrar parámetros como el tiempo atmosférico, la época del año, la inflación económica, la movilidad interurbana, o si tenemos datos recientes, la incidencia acumulada del coronavirus en la ciudad. Si construimos un modelo de regresión lineal con todos estos datos y los vamos eliminando de manera iterativa del mismo en función de la significancia estadística que aporte cada uno nos vamos a quedar con las variables con mas peso como productoras en nuestro modelo final. Esto va a facilitar la interpratibilidad del modelo, ya que trabajaremos con un modelo mucho mas simple y también reducirá el esfuerzo computacional que debemos de realizar para poner en producción nuestro modelo. Cuando hablamos de interpretabilidad del modelo, no solo nos referimos a la facilidad que tenemos para explicar que esta ocurriendo tras los cálculos matemáticos del mismo si no a la información que podemos extraer de este proceso. Por ejemplo, en el modelo de regresión hacia atrás que estamos planteando, podemos extraer mas información derivada de las variables con mas peso que se mantengan dentro de nuestro modelo. 

55 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Si en el modelo final, obtenemos que una de las variables incluida es la época del año, podemos plantear nuevas hipótesis en base a la significancia de esta variable, como por ejemplo que el aumento del consumo eléctrico es debido a los aires acondicionados que están funcionando en verano. 

Este tipo de regresión es muy empleada dentro del campo de la inteligencia artificial para la creación de modelos, pero cuenta con una serie de limitaciones que hacen que desde el campo de la estadística sea fuertemente criticado el uso de este tipo de modelos. Estas son algunas de las ventajas e inconvenientes que podemos encontrar cuando empleamos este tipo de modelos 

Ventajas: 

- Nos permite trabajar con bases de datos muy grandes seleccionando las variables mas significativas de todas las que tenemos disponibles 

- Es un método rápido en comparación con otros métodos automáticos de selección de variables 

- Conocer el orden en que las variables han sido incluidas o eliminadas nos aporta información extra sobre la calidad de los predictores que estamos empleando. 

Desventajas: 

- Una de las principales desventajas de este tipo de modelos es como trabaja con las variables predictoras que están correlacionadas entre si. Si alguna de las variables predictoras esta fuertemente correlacionada con otra puede que solo una de ellas sea incluida dentro del modelo, sin tener en cuenta que ambas variables puedan añadir peso significativo al modelo. 

- Este tipo de regresiones funciona bien en la tarea de selección de variables predictoras pero no obtiene buenos resultados en la estimación de los coeficientes que acompañan a estas variables en comparación con otro tipo de algoritmos de regresión. 

- Pueden eliminar variables que hemos incluido en los datos de manera artificial. Esto puede ocurrir con lo que se conoce como dummy variables. Estas variables se emplean cuando queremos añadir datos al conjunto de entrenamiento, o queremos preprocesar alguno de los datos disponibles. Por ejemplo si contamos con una variable categórica que defina si un individuo es hombre o mujer, podemos incluir esta variable como una variable dummy en la cual 1 implica que el sujeto es un hombre y un 0 que el sujeto no es un hombre. Este tipo de escollo es fácil de solventar ya que podemos añadir de manera manual estas variables una vez hayamos realizado la selección de caracteristicas para la regresión. 

56 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

### **2.2.4. Otros modelos de regresión** 

Existen múltiples modelos de regresión en esta guía se pretende dar una visión general sobre los mas importantes. Alguno de estos modelos ya los hemos estudiado como modelos de clasificación en la unidad anterior. Estos modelos tienen aplicaciones tanto en el campo de la clasificación como en el campo de la regresión. Cabe destacar los siguientes: 

#### **_K-Nearest Neighbour_** 

Estos algoritmos se pueden aplicar tanto en la construcción de modelos de clasificación como en modelos de regresión. La diferencia radica en el tratamiento de los datos. Mientras que en los algoritmos de clasificación tomábamos como valores las etiquetas categóricas de los puntos vecinos seleccionados para establecer el sistema de votación, en caso de estar trabajando en un escenario de regresión con datos continuos, se considerará el valor que toma la etiqueta cada uno de ellos, y se devolverá como predicción el valor medio de los mismos. 

La implementación en Python de este tipo de modelos con datos en un espacio continuo se puede llevar a cabo empleando la misma librería de sklearn, pero en lugar de utilizar el paquete de KNeighborsClassifier, utilizaremos el paquete de KNeighborsRegressor. 

#### **_Support Vector Machines (SVM)_** 

En el caso de los Support Vector Machines, el funcionamiento del algoritmo es la misma que en el caso de los problemas de clasificación, con alguna diferencia en el proceso de construcción del hiperplano, en el cual se establece un margen de tolerancia para las predicciones. La idea detrás de este enfoque sigue siendo semejante: transformar los datos a un espacio de mayor dimensionalidad en el que poder realizar un análisis de regresión lineal. 

#### **_Arboles de decisión_** 

Los arboles de decisión pueden emplearse tanto para problemas de clasificación como para problemas de regresión. En el caso de estar ante el segundo tipo de problemas, la división de los nodos se realizará mediante la minimización de la suma de cuadrados residual. Este proceso emplea la misma métrica que los problemas de regresión lineal. 

57 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

## **3. Aprendizaje no supervisado** 

_“Este tipo de aprendizaje no puede aplicarse directamente sobre problemas de clasificación o regresión ya que, al no contar con etiquetas en los datos de entrada existe la posibilidad de entrenar un modelo en la forma en la que lo hacíamos con el aprendizaje supervisado.”_ 

El aprendizaje no supervisado agrupa el conjunto de algoritmos en los cuales el modelo se ajusta a las observaciones. A diferencia de el aprendizaje supervisado en este caso no contamos con resultados conocidos o etiquetas de los datos a priori. Este tipo de aprendizaje no puede aplicarse directamente sobre problemas de clasificación o regresión ya que, al no contar con etiquetas en los datos de entrada existe la posibilidad de entrenar un modelo en la forma en la que lo hacíamos con el aprendizaje supervisado. El objetivo del aprendizaje no supervisado pasa por la agrupación de datos no estructurados según las similitudes y patrones que podemos encontrar en la estructura subyacente de los datos. Por ejemplo, en la imagen podemos ver un conjunto de animales de los cuales no conocemos su clasificación. Si aplicamos un algoritmo de aprendizaje no supervisado, no obtendremos una clasificación de los animales en función de su especie ya que es un dato que el algoritmo desconoce, pero si una clasificación en función de las características especificas de cada conjunto de datos, por ejemplo el grupo uno tiene las orejas grandes, el grupo dos tiene trompa, el grupo tres camina sobre dos patas, el grupo cuatro camina sobre cuatro patas. 



Ilustración 45: Diagrama aprendizaje no supervisado 

58 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Estos algoritmos son capaces de localizar estos patrones en los datos sin necesidad de intervención humana. Este tipo de aprendizaje genera un gran reto a la hora de construir modelos de inteligencia artificial ya que, al no contar con datos etiquetados de entrada no existe un output predeterminado. Si comparamos este tipo de algoritmos con el aprendizaje supervisado podemos observar que permiten realizar tareas de procesamiento mas complejas que los algoritmos de aprendizaje supervisado sin embargo sus resultados van a resultar mas impredecibles. Este tipo de algoritmos con frecuencia se utilizan en combinación con algoritmos de tipo supervisado, ya que permiten encontrar características que pueden resultar útiles en la categorización de las variables. Dentro del aprendizaje no supervisado podemos encontrar tres principales objetivos: agrupación de datos o clustering, asociación de datos y reducción de dimensionalidad. En esta unidad del módulo veremos en detalle en que consiste cada uno de estos objetivos y que algoritmos tenemos a nuestro alcance para ponerlo en práctica. 

Los ejemplos de aplicación del aprendizaje no supervisado no son tan directos como los que podemos encontrar en el aprendizaje supervisado, pero su habilidad para descubrir patrones ocultos en los datos los hace ideales para la exploración de datos, segmentación de clientes, análisis de mercados y reconocimiento de imágenes. 

### **3.1. Clustering** 

El clustering es un subconjunto de técnicas de aprendizaje no supervisado cuyo objetivo es encontrar patrones en los datos que formen grupos claramente separados. El análisis detrás de estos modelos se basa en la suposición de que es posible agrupar las muestras en base a sus similitudes. Para ello se pueden emplear distintas métricas de distancia que permitan agrupar los datos pertenecientes a clúster mediante la minimización de las mismas, en comparación con el resto de los registros de la base de datos. Generar estas agrupaciones en los datos tiene varias aplicaciones, por ejemplo, este tipo de algoritmos son muy frecuentemente en marketing para segmentar los clientes y así poder ofrecer a cada grupo el tipo de productos especifico para sus características. Otro ejemplo muy común de utilización de técnicas de clustering es en investigación genómica. Cuando se trabaja con volúmenes de datos tan grandes este tipo de técnicas nos permiten extraer caracteristicas de los mismos que con otras técnicas seria demasiado costoso computacionalmente. Este tipo de algoritmos se puede utilizar como aplicación final pero también podemos utilizarlo como un paso previo a otras técnicas de aprendizaje, ya sean supervisadas o no supervisadas, como exploración de datos y técnica de preprocesado de datos. Uno de los problemas de este tipo de técnicas es la subjetividad de esta. Sobre un mismo conjunto de datos se pueden generar distintos agrupamientos en función de las características que empleemos para optimizar nuestro algoritmo de clustering. 

Dentro de los algortimos de agrupación podemos encontrar distintas técnicas según el tipo de aproximación que hagamos al problema. En esta sección vamos a repasar las principales y sus aplicaciones. 

59 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

### **3.1.1. k-means** 

K-means o k-medias es una de las técnicas de clustering mas utilizada para el agrupamiento de datos no estructurados. El objetivo de este algoritmo es encontrar grupos en los datos, con el número de grupos representado por la variable K. En estos grupos vamos a encontrar las variables que comparten características semejantes, separándolas de otros grupos con los que no comparten esas características. Para determinar que datos pertenecen a cada grupo el algoritmo de k-mean minimiza la distancia entre los datos disponibles, generalmente utilizando como métrica la distancia euclideana aunque también puede aplicarse este algoritmo utilizando otros tipos de métricas de distancia.[31] 

Este algoritmo funciona de manera iterativa, y requiere como datos de entrada el número de clusters que van a ser definidos dentro de los datos. Este valor se define con la variable k y se denomina centroide, ya que actua como centro del cluster. Asimismo, requiere que los datos que vamos a utilizar como entrada o datos de entrenamiento sean valores numéricos continuos. Si tenemos valores categóricos (por ejemplo, tipos de frutas: manzanas, peras, plátanos…) podemos tratar de transformarlas en variables numéricas, pero esto afectara al rendimiento del algoritmo. En estos casos es mejor decantarse por otros tipos de técnicas de clasificación. También es recomendable que los valores que vayamos a utilizar estén normalizados (en la misma escala) para evitar disparidad geográfica en la creación de clusters. El objetivo del k-means es minimizar la suma de las distancias entre los puntos y el centroide al que pertenecen.[32] 

El proceso iterativo que sigue el algoritmo es el siguiente: 

1. Inicialización de las coordenadas de los centroides. En la base de datos disponible se inicializan los centroides en posiciones aleatorias. 



Ilustración 46: Inicialización de coordenadas de k-means 

2. Asignación de cada punto a un cluster en base a la distancia a cada centroide. Cada punto de los datos se incluye en el cluster del centroide mas próximo. 

60 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 47: Asignación de puntos al cluster inicial 

3. Recalculo de los centroides. Una vez se han asignado todos los puntos a un cluster, se recalcula el centro del mismo y este se toma como nuevo centroide 



Ilustración 48: Reasignación de centroides 

4. Se repiten los pasos 2 y 3 de manera iterativa hasta que se llega al criterio de parada. 



Ilustración 49: resultado del algoritmo de k-means 

61 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Existen distintos criterios de parada a la hora de finalizar la iteración del algoritmo: 

- Los centroides dejan de cambiar su posición. Tras varias iteraciones los centroides dejan de reubicarse en el centro del cluster por lo que no existirá reasignación de puntos a distintos clusters. 

- Los puntos dejan reasignarse a distintos clusters. Siguiendo el mismo principio que la parada de reubicación de los centroides, en el momento en que los puntos de los datos dejan de cambiar de punto hemos llegado a la estabilidad del algoritmo. 

- Parada establecida. Podemos definir un límite de iteraciones en el cual no se reasignarán los centroides y la agrupación de los datos se mantendrá en la última iteración. 

Una de las características mas importantes a la hora de implementar este tipo de algoritmos es definir un correcto valor de k para nuestros datos. Este valor va a variar en función de los datos que empleemos. Para aproximar un valor razonable de k se emplea lo que se conoce como la técnica del codo. En esta técnica se compara los resultados del algoritmo para distintos valores de k, midiendo la distancia media entre los puntos que conforman cada uno de los clusters y su centroide. Como la distancia media disminuirá a medida que aumente el valor de k, se emplea la distancia media al centroide en función de k. En el punto en que este valor disminuya drásticamente podemos considerar que hemos encontrado el numero optimo de centroides para ese grupo de datos. 

Podemos construir un ejemplo de clustering de una forma muy simple en Python. En primer lugar, importamos las librerías que vamos a utilizar en el ejemplo. 



Ilustración 50: Importar librerias para el algoritmo de k-means 

En este caso vamos a crear nuestra propia base de datos aleatoria. Para que los puntos puedan ser fácilmente agrupables en tres clusters, vamos a generar estos datos de manera independiente y a concatenarlos. De esta manera vamos a introducir de manera artificial una relación en nuestros datos. 



Ilustración 51: Generación base de datos para algoritmo k-means 

62 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Si visualizamos los datos que acabamos de obtener podemos ver que se distribuyen en tres nubes de puntos aleatorias. Podemos observar esta relación de manera gráfica en la Ilustración 52 



Ilustración 52: Datos de entrada algoritmo k-means 

Con estos datos podemos construir nuestro algoritmo de k-means. En primer lugar definimos el número de centroides que vamos a emplear, o lo que es lo mismo cuantos clusters queremos generar en nuestros datos. Con este valor inicializamos el modelo que hemos importado de la librería sklearn. Una vez tenemos inicializado el modelo lo ejecutamos sobre los datos de entrada que hemos generado previamente (X). 



##### Ilustración 53: Aplicamos el algoritmo de k-means sobre los datos 

Podemos ver los resultados de este algoritmo de manera gráfica. Identificamos los centroides que ha definido el algortimo con la función k_means.cluster_centers_, así como las etiquetas del cluster en el cual se ha incluido cada uno de los puntos (k_means.labels_). Con estos datos representamos gráficamente de nuevo los datos de entrada y podemos ver como han sido agrupados en tres clusters diferenciados en función de su ubicación. 



63 

**Módulo. Machine Learning y Deep Learning** 

**Centro Europeo de Postgrado** 



Ilustración 54: Resultado algoritmo de k-means 

En este caso hemos definido el número de centroides en 3, ya que para el ejemplo hemos definido los datos de manera artificial, generando tres nubes de puntos claramente diferenciadas, en la vida real, los datos pueden presentar multiples distribuciones y es necesario estimar el numero de centroides correcto. Para ello se emplea la técnica del codo, en la cual se computa la distancia media al centro del cluster en función de k. Esta distancia se representa de forma grafica y se toma como k el valor en el cual la gráfica se aplana, ya que a partir de ahí la distancia media se estabiliza y no generamos ganancia de información si aumentamos la segmentación de los datos. En nuestro caso vamos a computar el algoritmo de k-means sobre los datos de entrada con diferentes valores de k, desde uno hasta diez, para poder observar en que momento la curva se aplana. 

Podemos observar en la gráfica que la curva se estabiliza en el valor de k=3 por lo que hemos elegido el numero correcto de clusters a la hora de implementar este algoritmo. Esta técnica se conoce como la técnica del codo ya que la gráfica siempre va a estar representada por una curva y para determinar el valor óptimo de k debemos de buscar el “codo” del brazo. 



64 

**Módulo. Machine Learning y Deep Learning** 

**Centro Europeo de Postgrado** 



Ilustración 55: Aplicación de la técnica del codo 

Este tipo de algoritmo tiene muchas aplicaciones directas en casos reales como puede ser la segmentación del comportamiento de clientes o grupos de usuarios en función su actividad y sus intereses, así como la clasificación de medidas de distintos sensores, por ejemplo en casos de video vigilancia podemos agrupar las imágenes obtenidas permitiéndonos discernir distintos objetos y su clasificación. Otro caso de uso bastante común de este tipo de algoritmos es la detección de anomalías dentro de los datos, por ejemplo para tratar de detectar actividad de bots sobre grandes bases de datos, o la detección de cambios significativos en los datos a lo largo del tiempo. Este tipo de algoritmos tiene unos usos potenciales ilimitados, ya que se trata de modelos muy versátiles que pueden ser utilizados en el clustering de cualquier tipo de datos. También tenemos que tener en cuenta que pese a su fortaleza, al igual que otros tipos de algoritmos también tiene sus desventajas y supuestos que debemos tener en cuenta antes de emplearlo. 

- La definición del parámetro k no es trivial. Contamos con algunas herramientas como la regla del codo que hemos descrito, pero en datos reales su aplicación no es tan sencilla ni directa. 

- El algoritmo es sensible al ruido y los outliers 

- Si los datos pertenecientes a cada cluster no están equilibrados, el efecto de agrupamiento no será optimo y encontraremos algunas anomalías en el resultado final del algoritmo. 

65 

**Módulo. Machine Learning y Deep Learning** 

**Centro Europeo de Postgrado** 

### **3.1.2. k-median** 

El algoritmo de k-medians comparte bases y objetivo con el algoritmo de K-means. Es un algoritmo de clustering cuyo objetivo es dividir la base de datos en un número específico de clústeres o agrupaciones de datos. Para ello emplea el mismo proceso iterativo que utilizamos en k-means, en el que definimos una serie de centroides a los asignamos los puntos de nuestros datos creando diferentes clusters. La principal diferencia entre estos dos algoritmos la encontramos en la métrica utilizada para calcular la distancia entre los puntos pertenecientes al cluster y el centroide del mismo. Mientras que el algoritmo de k- means minimiza la distancia euclidiana entre un punto y el centro del clúster, el algoritmo de k-median minimiza la distancia de Manhattan o métrica del taxista. Recordemos que la distancia eucleidea era calculada como la distancia mas corta en línea recta entre dos puntos y se representaba con la siguiente fórmula: 



Mientras que la distancia de Manhattan mide la distancia entre dos puntos en un espacio vectorial, y se representaba con la siguiente fórmula 



Desde una perspectiva de optimización, cuando trabajamos con el algoritmo de k-means estamos más expuestos a que nuestros clústeres se vean afectados por outliers, mientas que el algoritmo de k- medianas es mas robusto frente  a los outliers y vamos a lograr obtener clústerese más compactos. 

Dentro de este subtipo de algoritmos podemos encontrar los algoritmos de k-medioides que se basan en el mismo principio de agrupación mediante algoritmos iterativos que k- means y k-medias pero emplean cualquier otro tipo de distancia a la hora de minimizar la distancia entre los datos y el centroide del clúster.[33] 

### **3.1.3. Hyerarchical clustering o agrupamiento jerarquico** 

El agrupamiento jerárquico o hyerarchical clustering es un tipo de algoritmo de clustering en el que se busca generar grupos o clústeres con los datos disponibles en los cuales los objetos contenidos dentro del clúster compartan una serie de características que les diferencien de los demás datos del conjunto. El objetivo de este algoritmo es el mismo que el que podemos encontrar en el algoritmo de k-means. La diferencia entre ambos algoritmos es la aproximación con la que se construyen los grupos. Además, el agrupamiento jerárquico tiene una ventaja adicional sobre el agrupamiento de K-means, en el sentido de que da como resultado una atractiva representación basada en árboles de las observaciones, denominada dendrograma. 

66 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

El agrupamiento jerárquico puede dividirse en dos tipos principales: aglomerativo y divisivo 

- **Agrupamiento aglomerativo:** Este tipo de agrupamiento también conocido como AGNES por sus siglas en inglés Agglomerative Nestign, construye los clúster de abajo arriba. Es decir cada objeto inicial es considera como un clúster independiente y estos se van fusionando en cada iteración del algoritmo con otros clúster con los que comparten un nivel de similitud, generando un clúster mayor. Este proceso se repite hasta que todos los puntos de la base de datos están contenidos dentro del mismo clúster final (raíz del dendrograma) 

- **Agrupamiento divisivo:** Este tipo de agrupamiento también es conocido como DIANA por sus siglas en ingles Divisive Analysis. En este caso el algoritmo trabaja de arriba hacia abajo. Se parte de un único clúster general (clúster raíz) del cual se van dividiendo distintos clústeres en función de la similitud de sus datos hasta llegar a tener cada una de las observaciones de los datos en un clúster individual. 

Los clústeres aglomerativos son útiles si lo que buscamos es identificar clusters pequeños, mientras que si nuestro objetivo es localizar grandes clusters de datos nos resultará mas útil emplear el método de agrupamiento divisivo.[34,35] 



Ilustración 56: Ejemplo de dendrograma 

67 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

La elección crucial al decidir sobre un algoritmo de clusteres jerarquicos es decidir cómo cuantificar las diferencias entre los conjuntos de datos. Para ello existen múltiples métodos, los mas comunes son los siguientes: 

- **Agrupamiento máximo o completo:** Con este método se calcula todas las diferencias por pares entre los elementos del grupo 1 y los elementos del grupo 2, y considera el valor más grande (es decir, el valor máximo) de estas diferencias como la distancia entre los dos grupos. Tiende a producir racimos más compactos. 

- **Agrupamiento mínimo o único:** En este método se calculan todas las diferencias por pares entre los elementos del grupo 1 y los elementos del grupo 2, y considera la menor de estas diferencias como un criterio de enlace. Tiende a producir racimos largos y “sueltos”. 

- **Agrupación de vinculación media:** En este método se calculan todas las diferencias por pares entre los elementos del grupo 1 y los elementos del grupo 2, y considera el promedio de estas diferencias como la distancia entre los dos grupos. 

- **Agrupamiento de centroide:** En este método se calcula la diferencia entre el centroide del grupo 1 y el centroide del grupo 2. 

- **Método de la varianza mínima de Ward:** En este método se minimiza la varianza total dentro del clúster. En cada paso, se fusionan el par de clústeres con una distancia mínima entre clústeres. [36] 

Para comprender mejor el funcionamiento de este tipo de algoritmos vamos a construir un ejemplo práctico. Supongamos que tenemos datos de consumo de telefonía de un conjunto de clientes. Queremos dividir a estos clientes en distintos grupos para poder ofrecerles una oferta que se adapte a su consumo. Tenemos los siguientes datos de entrada para construir nuestro modelo de agrupamiento jerárquico. 

|**Cliente ID**|**Consumo telefónico**|
|---|---|
|1|20 €|
|2|50 €|
|3|7 €|
|4|15 €|
|5|12 €|



68 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Con esta tabla de datos de entrada podemos construir una matriz de proximidad que nos sirva como base para construir nuestro dendrograma. En esta matriz vamos a calcular la distancia entre los distintos puntos utilizando la métrica de distancia eucleidiana con la fórmula 



Por ejemplo, la distancia entre los clientes 1 y será de 

La distancia de la diagonal será siempre cero ya que la distancia entre un punto y si mismo va a ser siempre de cero. 

|**ID**|**1**|**2**|**3**|**4**|**5**|
|---|---|---|---|---|---|
|1|0|30|13|5|8|
|2|30|0|43|35|38|
|3|13|43|0|8|5|
|4|5|35|8|0|3|
|5|8|38|5|3|0|



Matriz de proximidad para la primera iteración de un clúster jerárquico 

Una vez hemos construido nuestra matriz de proximidad nos fijamos en los valores mas próximos y los unimos en un solo clúster. Los valores mas próximos se corresponderán con la menor distancia dentro de la matriz, en este caso entre los clientes 4 y 5. En la primera iteración de nuestro algoritmo fusionaremos estos dos clústeres. Podemos verlo reflejado en el dendrograma de la Ilustración 57. 



Ilustración 57:Dendrograma de primera iteración 

69 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Para recalcular nuestra matriz de proximidad para la nueva iteración debemos actualizar la tabla de datos que empleamos. Como hemos fusionado los clusters 4 y 5 pasamos a considerarlos como un único segmento. A la hora de calcular la matriz de proximidad lo hacemos tomando el valor mas alto de los dos contenidos dentro del clúster. 



<!-- Start of picture text -->
Cliente ID Consumo telefónico<br>1 20 €<br>2 50 €<br>3 7 €<br>(4, 5) 15 €<br>ID 1 2 3 4,5<br>1 0 30 13 5<br>2 30 0 43 35<br>3 13 43 0 8<br>4, 5 5 35 8 0<br><!-- End of picture text -->

Con estos datos podemos generar la segunda iteración de nuestro algoritmo uniendo los dos clústeres mas próximos, que en este caso son los clústeres 1 y el conjunto formado por 4 y 5. Con esta segunda iteración podemos actualizar nuestro dendrograma. 



Ilustración 58: Dendrograma de segunda iteración 

70 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

En este nuevo dedrograma podemos ver como nuestros clusteres se van agrupando hasta llegar a la raíz del dendrograma donde todos se unen. Para realizar una nueva iteración debemos actualizar de nuevo nuestra matriz de proximidad y la base de datos reflejando los nuevos clústeres que se han formado. 



<!-- Start of picture text -->
Cliente ID Consumo telefónico<br>2 50 €<br>3 7 €<br>(1, 4, 5) 20 €<br>ID 2 3 1,4,5<br>2 0 43 30<br>3 43 0 13<br>1,4, 5 30 13 0<br><!-- End of picture text -->

Con estos nuevos datos podemos actualizar nuestro dendrograma fijándonos en la distancia mínima que encontramos en la matriz de proximidad. En este caso vamos a unir los clústeres 3 con el conjunto de 1,4 y 5. 



Ilustración 59: Dendrograma final 

71 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Ahora que hemos visto un ejemplo de como funciona el algoritmo de clustering jearquico vamos a ver como generar este tipo de árboles de manera automática utilizando Python. Para ello vamos a descargar una base de datos de código abierto disponible en Kaggle. Para este ejemplo vamos a utilizar una base de datos que contiene información sobre la actividad financiera de un grupo de clientes a través de los movimientos de su tarjeta de crédito. Con estos datos vamos a tratar de clasificar a los clientes en grupos para poder ofrecerles las mejores ofertas en base a su comportamiento.Para ello vamos a comenzar por descargar la base de datos de Kaggle (https://www.kaggle.com/vipulgandhi/ <u>hierarchical-clustering-explanation/data). Una vez tenemos disponible nuestra base de</u> datos podemos empezar a crear nuestro modelo en Python. Como siempre al comenzar cualquier tipo de programa en Python debemos cargar los módulos que vamos a emplear. 



Ilustración 60: Carga módulos para modelo de Cluster jerarquico 

El siguiente paso es cargar la base de datos que hemos obtenido de kaggle y visualizar su estructura. 



Ilustración 61:Base de datos para clustering jerarquico 

En estos datos podemos observar que la primera columna contiene un identificador de cada cliente. Esta es una variable categórica que no podemos emplear en la creación de nuestro modelo de clúster jerárquico en conjunto con variables continuas. También podemos observar en la base de datos que hay valores que no existen. Este tipo de valores se representan por un NaN en lugar del valor numérico. Antes de continuar con la creación de nuestro modelo debemos pre-procesar los datos para eliminar estas anomalías y que nuestro modelo funcione de manera correcta. 

72 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 62: Pre-procesado de la base de datos 

Una vez tenemos nuestra base de datos completa y en formato categórico debemos realizar un último paso en el proceso de preprocesado. Como podemos observar cada una de las variables disponibles se encuentra en una escala diferente. Para poder calcular las distancias entre cada punto de la base de datos necesitamos que todos se encuentren en la misma escala, de lo contrario obtendremos distancias dispares en función de la métrica de medida que estemos utilizando. Para ello vamos a normalizar nuestra base de datos, de esta forma todas las variables tendrán un valor entre 0 y 1. 



Ilustración 63: Normalización de la base de datos 

En este punto estamos listos para construir nuestro dendrograma. Este tipo de esquema nos va a permitir decidir cuantos cústeres nos interesa construir para este problema en concreto. Para ello simplemente debemos importar la librería que contiene el algoritmo y aplicarla sobre los datos normalizados. En este caso en lugar de utilizar la librería de sklearn vamos a utilizar la librería de scipy. Esta también es una biblioteca libre y de código abierto compilada para Python. En ella vamos a poder encontrar herramientas y algoritmos matemáticos. 

73 

**Módulo. Machine Learning y Deep Learning** 

**Centro Europeo de Postgrado** 



Ilustración 64: Construcción de dendrograma 



Ilustración 65: Dendrograma 

Si observamos el resultado del dendrograma podemos ver que existen tres clusteres principales, y dado que la distancia entre clústeres viene dada por la longitud de las líneas verticales podemos observar que el primero de los clústeres se encuentra bastante alejado de los otros dos. En base a este dendrograma vamos a aplicar la función de clúster jerárquico sobre nuestros datos normalizados, esta vez clasificando cada uno de los puntos en tres posibles clústeres. Para ello vamos a utilizar la librería de sklearn que contiene la función de Aglomerative Clustering. 



Ilustración 66: Aplicación de función de algomerative clustering 

74 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Como output de esta función obtenemos un array (o vector) que contiene las etiquetas del clúster en el que se ha clasificado cada uno de los puntos. Para poder observar esto de manera visual podemos dibujar la gráfica en la que representemos las dos primeras variables y su clasificación por color en función del clúster al que pertenecen. 



Ilustración 67: representación gráfica de los clústeres de datos 

La clasificación de todos los clientes en grupos nos permitirá definir una estrategia especifica para cada uno de estos grupos en función de sus características. 

Este tipo de algoritmos como todos los que hemos visto tienen casos prácticos de aplicación en la vida real, pero para poder utilizarlos debemos tener en cuenta el tipo de datos con los que estamos trabajando. En este caso debemos utilizar el algoritmo cuando trabajamos con datos que sabemos que contienen una estructura jerárquica subyacente, la cual deseamos recuperar. Un buen ejemplo de uso de estos modelos es con datos financieros los cuales presentan una jerarquía clara. Este tipo de modelos trabaja en contraposición a los modelos de clustering de k-mean o k-median, ya que estos últimos no permiten conservar la jerarquía de los datos al tratarse de algoritmos con enlaces planos que construyen una jerarquía que no es la adecuada para datos anidados. 

75 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

### **3.2. Reducción de dimensionalidad** 

Los métodos de reducción de dimensionalidad son algoritmos trasladan el conjunto de datos originales desde un espacio original a uno de menos dimensiones. De esta manera permite hacer una descripción de los datos con un menor coste computacional, facilitando la descripción de los datos y asegurando la independencia de las variables de la base de datos. Los principios de este tipo de algoritmos se centran en mantener la información relevante intacta en el nuevo espacio dimensional mientras reducimos los datos no válidos, información duplicada… 

_“Cuando se trata de datos de gran dimensión, suele ser útil reducir la dimensionalidad proyectando los datos a un subespacio de menor dimensión que capte la «esencia» de los datos. Esto se denomina reducción de la dimensionalidad.”_ -Página 11, Aprendizaje automático: Una Perspectiva Probabilística, 2012 [37] 

La reducción de dimensionalidad es importante en escenarios en los que nuestra base de datos es muy grande o contiene muchos elementos dependientes unos de otros. En estos casos cuando creamos un algoritmo de inteligencia artificial el modelo tratará de emplear todos los datos que encuentre disponibles, lo cual derivará en una reducción de rendimiento del modelo en el momento en el que estemos incluyendo nuevos datos que no nos aporten nueva información relevante y en overfitting o sobre-entrenamiento, provocando un modelo demasiado ajustado a los datos de entrenamiento y poco generalizado para ser utilizado con nuevas bases de datos de entrada. Para realizar esta reducción de dimensionalidad podemos emplear dos técnicas principales: 

- **Selección de características:** Consiste en eliminar de nuestra base de datos variables redundantes o aquellas que no estén aportando ninguna información relevante a la hora de generar predicciones. Debemos ser cautos empleando este tipo de reducciones de dimensionalidad ya que podemos perder parte de la información relevante si no se realiza de manera correcta. Esto nos va a permitir trabajar con un conjunto de datos mas pequeño reduciendo los requerimientos computacionales y el costo temporal de entrenamiento. 

- **Extracción de características:** En este caso el proceso incorpora nuevas variables a nuestra base de datos. Estas nuevas variables son generadas como combinaciones de las variables originales potenciando la extracción de información de las mismas. 

Este tipo de técnicas son utilizadas muy frecuentemente en procesamiento de imágenes y texto, procesado del lenguaje natural y aquellos problemas en los cuales podemos encontrar muchos datos redundantes que procesar. Por ejemplo, si debemos procesar una imagen en la cual encontramos un objeto en el centro de la misma mientras que el resto de pixel de esta contienen un valor cero, estos pueden ser clasificados como información inútil y desechados en el proceso de procesado de imagen. 

76 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Un claro ejemplo de esto lo podemos encontrar en el procesado de imágenes médicas de resonancia magnética. En la imagen del ejemplo [38], el resultado de la extracción de una imagen funcional de resonancia magnética, podemos ver que la información relevante para su procesado se encuentra en el interior del cráneo mientras que el fondo, el cual contiene el ruido propio de la generación de este tipo de imágenes no nos aporta ninguna información relevante al procesado. En estos casos podemos desechar estos datos y quedarnos solo con los pixels que nos interesan para su procesado. 



Ilustración 68: Ejemplo de imagen con valores no útiles para el procesado 



77 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

### **3.2.1. Extracción de características** 

Dentro de los algoritmos de selección de características podemos encontrar dos grandes clasificaciones en función del tipo de transformación que utilizan para extraer las características: lineales y no lineales. En este bloque vamos a estudiar el comportamiento de varios de estos modelos 

### **3.2.1.1. Clasificadores lineales** 

#### **Análisis factorial** 

El análisis factorial es una técnica de reducción de datos que emplea reducciones estadísticas y que tiene como objetivo explicar las posibles correlaciones que existen entre ciertas variables. Las variables con máximas correlaciones se incluyen en grupos homogéneos, procurando que estos grupos sean independientes unos de otros. 

Este método puede utilizarse para reducir la cantidad de datos empleados ya que permite identificar un pequeño número de factores que expliquen la mayor parte de la varianza de los datos. Este tipo de análisis tiene otros tipos de aplicaciones en el campo de la estadística como por ejemplo generar nuevas hipótesis o inspeccionar las variables para definir nuevos métodos de análisis. La principal aplicación en inteligencia artificial de este método pasa por el objetivo principal del método, emplear el mínimo posible de variables para explicar la mayor cantidad de información posible contenida en los datos. Para obtener estas nuevas variables el modelo realiza una serie de combinaciones lineales entre las variables observadas para obtener las un número más pequeño de dimensiones latentes (factores) no observables. Estos nuevos factores buscan explicar las relaciones que se establecen entre las variables observadas perdiendo el mínimo posible de información. [40] 

El funcionamiento de este método se basa en descomponer las variables que tenemos en nuestra base de datos original en la combinación lineal de distintos factores. 

Estos algoritmos pueden ser clasificados en función de la metodología que utilizan a la hora realizar la reducción de dimensionalidad. En el siguiente árbol podemos encontrar la clasificación a la que pertenecen cada uno de los modelos que vamos a ver en este módulo. [39] 



El objetivo del análisis factorial es determinar el peso de estos nuevos factores de manera que equiparen la varianza de los datos originales. Por medio de esta técnica logramos reducir el número original de variables a uno mucho mas manejable.[43] 

78 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

#### **Análisis de componentes principales (PCA)** 

El análisis de componentes principales o PCA por sus siglas en inglés (Principal Componen Analysis) es una de las técnicas de reducción de dimensionalidad mas utilizadas en aprendizaje máquina. Esta técnica se caracteriza por describir un conjunto de datos en términos de nuevas variables no relacionadas. Con esto se busca reducir el número de variables de forma que pasemos de tener bases de datos complejas representadas por un gran número de variables a un mínimo número de nuevas variables que representen las originales de la forma mas fiel posible. Este tipo de técnicas también facilitan la representación grafica de los datos al poder reducir los datos originales a un espacio de dos dimensiones (plano) o tres dimensiones (gráfico 3D). Esto nos va a simplificar comprender las relaciones entre las variables y nos ayudará en la toma de decisiones. 

El proceso de extracción de estas nuevas características tiene una inherente complejidad matemática para la cual es necesario el conocimiento de los principios del algebra lineal. En este capitulo describiremos a grandes rasgos como funciona el algoritmo, pero no debemos preocuparnos en exceso por las matemáticas subyacentes ya que, en la vida real, la aplicación de este tipo de modelos se realiza a través de librerías preconfiguradas las cuales nos evitan realizar todos los cálculos matemáticos necesarios. Los pasos que realiza el algoritmo para calcular estas nuevas características son los siguientes: 

1. En primer lugar, comenzamos normalizando los datos de entrada para que todas nuestras variables se encuentren dentro de la misma escala. 

2. Obtenemos los autovalores y autovectores de la matriz de covarianza.  Estos valores contienen la información extraída de las variables de la base de datos. Cada auto valor está asociado a un autovector. La fórmula para extraer estos valores es la siguiente: 



Donde A es la matriz de covarianza construida con los datos de entrada, v es el autovector y λ es el autovalor asociado. Los autovectores representan la dirección mientras que los autovalores representan la magnitud. 

3. Ordenamos los auto valores y sus asociados auto vectores de mayor a menor y seleccionamos los mas grandes. El número de autovalores seleccionados va a determinar el numero de dimensiones que va a tener nuestras nuevas variables. Los mayores autovalores y sus asociados autovectores contienen mas información mientras que los menores contienen mucha menos. Al seleccionar los mas grandes estamos manteniendo la máxima información posible extraída de las características originales. 

79 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

4. Con estos autovectores construimos una matriz que transformará nuestros datos. 

5. Transformamos los datos originales que habíamos estandarizado multiplicándolos por la matriz de autovalores que hemos construido. El resultado de esta transformación serán nuestras nuevas características. 

Como hemos dicho no debemos preocuparnos por el proceso matemático subyacente ya que es demasiado complejo y se escapa del alcance de esta asignatura. Lo que si podemos hacer es aprender a aplicar este proceso sobre una base de datos utilizando Python para comprobar como mediante la reducción de dimensionalidad obtenemos un nuevo espacio de características mas reducido en el cual conservamos la información relevante de nuestra base de datos. Para ello vamos a utilizar de nuevo la base de datos de Iris que hemos empleado a lo largo del módulo. 

Como en cada ejemplo comenzamos cargando las librerías que vamos a necesitar para ejecutar nuestro código. 



Ilustración 69: Carga librerias para PCA 

Una vez tenemos nuestras librerias disponibles, el siguiente paso es cargar la base de datos que vamos a utilizar. 



Ilustración 70: Base de datos para PCA 

80 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Como podemos ver en la cabecera de nuestros datos, el archivo que hemos cargado contiene una columna de identificación que no nos va a aportar información al modelo y que va a interferir con los cálculos por lo que debemos hacer un paso de preproprocesado para eliminarla. También vamos a separa nuestros datos en función de las variables que vamos a utilizar como entrada en nuestro algoritmo y la variable ‘target’ que tratamos de predecir. 



##### Ilustración 72: Preprocesado base de datos 

Como podemos observar en la salida de la función tenemos nuestros datos limpios y libres de ruido que pueda afectar al modelo. En el siguiente paso vamos a separar los datos disponibles en datos de entrenamiento y datos de test. Este paso no es necesario para aplicar el algoritmo de análisis de componentes principales, vamos a realizar esta división para poder comprobar, aplicando otro tipo de clasificador, la cantidad de información que conservamos una vez hemos aplicado el PCA sobre nuestros datos. 



Ilustración 71: División de base de datos en entrenamiento y test 

Una vez tenemos nuestros datos disponibles vamos a aplicar el primer paso del algoritmo de PCA, normalización de los datos. Para ello vamos a utilizar una función previamente definida en Python y que hemos cargado con la función “from sklearn.preprocessing import StandardScaler” Esta función vamos a aplicarla en los datos de test y de entrenamiento. 



Ilustración 73:Estandarización de los datos 

81 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

El paso siguiente dentro del algoritmo consiste en extraer los eigenvalues y eigenvectors de los datos originales y utilizarlos como matriz de transformación para trasladar esos datos a un nuevo espacio. Para evitarnos complejos cálculos matemáticos vamos a utilizar de nuevo una función predefinida. 



##### Ilustración 74: Aplicación de PCA 

Dentro del algoritmo que hemos aplicado podemos encontrar una variable que definimos como ratio de varianza, la cual nos indica la cantidad de información que vamos a encontrar en cada uno de los componentes principales que hemos generado a partir de nuestros datos. Como no le hemos definido en la entrada de la función cuantos componentes debe generar, por defecto la función va a crear el mismo número de componentes principales que de variables disponibles, en este caso serán cuatro. 



##### Ilustración 75: Varianza del PCA 

Podemos interpretar la salida de esta variable como la cantidad de información que contiene cada uno de los componentes principales que hemos extraido. En este caso podemos observar que el primer componente contiene el 72% de la información disponible en la base de datos, mientras que el segundo contiene el 23%. Los componentes tercero y cuarto apenas contienen información por lo que podríamos desecharlos sin que esta pérdida afecte significativamente a la precisión del modelo. 

Como hemos visto que la mayor parte de información se encuentra contenida en el primer componente extraído, vamos a generar una PCA en la cual solo obtengamos el primer componente. 



##### Ilustración 76: PCA primer componente 

Podemos comprobar el contenido de este primer componente ejecutando la descripción del dataframe en el que este contenido. 

82 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



##### Ilustración 77: Datos primer componente PCA 

Para comprobar si realmente este componente contiene la mayor parte de la información que teníamos en la base de datos original vamos a aplicar una función de clasificación utilizando este componente como dato de entrada en lugar de hacerlo con los datos originales. Para ello vamos a usar la función de K vecinos cercanos. Esta función la hemos comprobado con la base de datos original en la descripción del algoritmo de K-NN. Para poder comparar los resultados vamos a utilizar el mismo valor K de entrada que empleamos en el algoritmo original. Aplicamos la función sobre los datos de entrenamiento transformados al nuevo espacio dimensional. 



##### Ilustración 78: Aplicación modelo K-NN 

Para comprobar la efectividad de nuestro modelo lo aplicamos sobre los datos de test también transformados al espacio de PCA y comprobamos el grado de precisión que obtenemos utilizando los datos de la variable ‘target’ que tenemos almacenados en y_test. 



##### Ilustración 79: Accuracy score modelo PCA 

Podemos observar que obtenemos una precisión de predicción del 83% utilizando únicamente el primer componente de PCA extraído de los datos de entrenamiento. 



Ilustración 80: Accuracy score modelo datos originales 

83 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Si comparamos este resultado con el obtenido aplicando el mismo modelo de K-NN sobre los datos originales de entrada podemos comprobar que la precisión de la clasificación ha disminuido parcialmente, ya que en el modelo original obteníamos una accuracy del 96%, pero aun asi mantenemos un valor alto de precisión en nuestro modelo clasificador, generando un modelo mas simple y que requiere una menor potencia computacional a la hora de ser entrenado. En el caso de estos modelos de ejemplo el consumo de recursos no es un problema ya que son modelos muy sencillos, pero cuando estos se escalan a nivel productivo, la reducción de características puede convertir un modelo inasumible computacionalmente en un modelo gestionable. 

#### **Análisis discriminatorio lineal (LDA)** 

El análisis discriminatorio lineal o LDA por sus siglas en ingles (Linear Discriminant Analysis) es un método de reducción de dimensionalidad lineal también muy utilizado en aprendizaje máquina. El método fue presentado por primera vez por Ronald Fisher en 1936 y se ha convertido en uno de los métodos mas utilizados a día de hoy en el preprocesamiento de los datos utilizados para aprendizaje máquina. Este método se basa en el mismo fundamento que el análisis de componentes principales de reducción de las variables disponibles en la base de datos original mediante su proyección a un nuevo espacio dimensional de menores dimensiones. Con esto se pretende lograr una reducción de variables que facilite la aplicación de modelos de inteligencia artificial de una manera mas sencilla y menos costosa computacionalmente hablando.[41,42] 

Aunque el principio fundamental del método de análisis discriminatorio lineal sea el mismo que el de PCA, el funcionamiento de estos dos algoritmos difiere en cuanto a la técnica utilizada para transformar las variables al nuevo espacio dimensional. En el caso de LDA el proceso que se sigue para obtener esta reducción consta de tres pasos: 

1. En primer lugar, se calcula la varianza entre clases (between-class variance). Esta varianza mide la distancia entre las medias de las distintas clases presentes en nuestra base de datos. La fórmula que se utiliza para calcular esta varianza entre clases es la siguiente: 



Fórmula between class variance 

2. En segundo lugar, calculamos la varianza intra-clase (within class variance). Esta varianza va a representar la distancia entre el valor medio de la clase y cada una de las muestras recogidas en ella. Esta varianza se calcula utilizando la siguiente fórmula: 

84 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Fórmula within class variance 

3. Finalmente se construye el nuevo espacio dimensional de menores dimensiones maximizando el valor de la varianza entre clases y minimizando el valor de la varianza intra-clase. De esta manera se obtiene la proyección a el menor espacio dimensional posible. Para ello se emplea la siguiente fórmula: 



Fórmula LDA 

Al igual que en el modelo de PCA, no debemos de preocuparnos en exceso por el trasfondo matemático del algoritmo ya que en las aplicaciones de la vida real estos cálculos serán realizados por funciones ya implementadas dentro de los distintos lenguajes de programación. 

Esta técnica de reducción de dimensionalidad se utiliza muy frecuentemente en conjunto con modelos aprendizaje supervisado de tipo clasificatorio. Un ejemplo muy común de uso conjunto es la aplicación del modelo de Naive Bayes sobre las nuevas variables obtenidas mediante LDA. Esto va a permitir generar un modelo con un menor número de variables, logrando una mayor interpretabiliad y rapidez del modelo. La principal ventaja que nos aporta este modelo respecto a otros modelos de reducción de dimensionalidad es su sencillez, velocidad y escalabilidad. Por otro lado, este algoritmo asume una serie de características en los datos de entrada que no siempre se cumplen, como la distribución normal de los datos. También requiere un importante esfuerzo computacional para llevar a cabo las operaciones de reducción de dimensionalidad (trabaja con complejas operaciones matriciales), por lo que debemos estimar los esfuerzos que nos va a suponer el computo de este tipo de modelos respecto a los posibles beneficios que podemos obtener de sus resultados. 

85 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

### **3.2.1.2. Clasificadores no lineales** 

Los clasificadores no lineales persiguen el mismo objetivo de reducción de dimensionaliadad de las variables disponibles. La principal diferencia respecto a los clasificadores de tipo lineal consiste en los métodos utilizados para realizar esta reducción de dimensionalidad, en este caso empleando transformaciones no lineales. 

#### **Escala multidimensional (MDS)** 

La escala multidimensional o MDS por sus siglas en ingles (Multi Dimensional Scale) es una técnica de reducción de dimensionalidad en la cual el conjunto de variables originales es transformado a un nuevo espacio dimensional de menores dimensiones, generando un nuevo conjunto de variables. Esta técnica utiliza el espacio geométrico para determinar la similitud o disimilitud de los datos disponibles. Este modelo proyecta los datos a un espacio de dimensiones inferior de manera que los puntos de datos que están cerca unos de otros, en términos de distancia euclidiana, en la dimensión superior también estén cerca en la dimensión inferior. 

#### **Mapeo de características isométricas (Isomap)** 

El mapeo de las características isométricas opera de una forma muy similar al método de escala multidimensional, la principal diferencia se encuentra en la métrica utilizada para determinar la distancia entre los datos. Mientras que en el modelo de escalas multidimensionales se utiliza la distancia euclidiana en los mapas de características isométricas se emplea la distancia geodésica. Esta distancia podemos definirla como la distancia mas corta entre dos puntos dentro de una curva. 

Este algoritmo consta de tres fases: 

1. En la primera fase el algoritmo definirá el número de vecinos cercanos utilizando el método de K-NN 

2. En el segundo paso el algoritmo calculará la distancia geodésica entre los puntos. La característica principal de este cálculo es que no se tendrá en cuenta el camino mas corto en el plano (distancia euclidiana) si no que se empleará el camino mas corto de todos los posibles. 

3. En el último paso se aplicará el método de escala multidimensional sobre las distancias geodésicas que hemos calculado para reconstruir nuestra base de datos en el espacio euclidiano. 

Este algoritmo es una modificación del algoritmo de escala multidimensional que nos permite eludir muchos problemas relacionados con la linealidad. 

86 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

#### **Incrustación local lineal (LLE)** 

Este método de reducción de dimensionalidad esta caracterizado por tratar de preservar la estructura local lineal de los datos de entrada y recuperar la estructura no lineal global de los datos mediante los ajustes locales. De la misma forma que el resto de los algoritmos no lineales revisados, también esta basado en la reducción de dimensionalidades, transformando los datos de entrada. 

#### **Mapas Hessien (HLLE)** 

Este método de reducción de dimensionalidad se caracteriza por la conservación de la estructura local, de la misma forma que lo hace el LLE, pero con la característica especifica de utilizar el operador Hessian, el cual determina el nombre del método. 

Existen múltiples métodos de extracción de características basados en la reducción de dimensionaliad aplicados a datos de inteligencia artificial. En este capítulo hemos repasado algunos de los mas importantes, aunque el método seleccionado siempre va a depender de las características de nuestros datos y el objetivo de parametrización final que tengamos para ellos. Todos estos métodos tienen como característica común la formación de nuevas variables a partir de las antiguas. 

### **3.2.2. Selección de características** 

Los métodos de selección de características se basan en la discriminación de aquellas variables que contienen información poco relevante. Algunos ejemplos de variables que deben ser eliminadas del conjunto de datos original son aquellas que resultan redundantes respecto a otras variables, las que no aportan ninguna información nueva, o aquellas cuya información no es útil para el propósito del modelo. Para llevar a cabo esta eliminación de términos existen varias técnicas que nos permiten identificar que variables no resultan de utilidad en la creación de un modelo. En esta sección analizaremos algunas de las mas utilizadas en ciencia de datos [44] 

#### **Ratio de valores perdidos** 

El ratio de valores perdidos o missing values es un método de selección de parámetros muy sencillo pero no por ello menos útil. Este método se basa en la premisa de que una columna a la cual le faltan demasiados valores es poco probable que vaya a aportar información útil al proceso de creación del modelo, por lo tanto, la variable puede ser eliminada. Para ello se define un umbral de aceptación de datos faltantes por encima del cual la variable es eliminada. Cuanto mas bajo sea el umbral mayor será la eliminación de variables de la base de datos. 

87 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

#### **Filtro de baja varianza** 

Otro método para eliminar variables de nuestra base de datos original consiste en filtrar la calidad de los datos en función de su varianza. Una columna en la cual la varianza es mínima podemos asumir que contiene poca información ya que los cambios en los datos van a ser muy pequeños. De la misma manera que podíamos establecer un umbral para eliminar variables con muchos valores perdidos, también podemos definir un umbral minimo de varianza para considerar una variable com útil e incluirla dentro de nuestra base de datos 

#### **Filtro de alta correlación** 

En este método de selección de características tomamos como referencia la correlación que unas variables presentan respecto a otras. Para ello se calcula el coeficiente de correlación de Pearson en el caso de variables continuas y el coeficiente de correlación de chi-cuadrado en el caso de trabajar con variables nominales. Entre todas las variables que presente una alta correlación se selecciona únicamente la columna que exceda el umbral definido. Esta técnica se basa en la premisa de que las variables con tendencias muy similares contengan el mismo tipo de información por lo que incluirlas todas en la base de datos de entrenamiento supondría una redundancia incrementando la complejidad del modelo y el coste computacional del mismo. 

#### **Bosques aleatorios** 

Los algoritmos de bosques aleatorios o random forest son algoritmos de aprendizaje supervisado que pueden emplearse en tareas tanto de regresión como de supervisión. Este tipo de algoritmos también están contemplados a la hora de seleccionar variables. Este algoritmo trabaja de una forma bastante similar a los arboles de decisión, con la diferencia de que los genera de manera aleatoria sin atender a un criterio estadístico y después los combina hasta obtener un modelo clasificatorio robusto. De este resultado clasificatorio final podemos obtener información para seleccionar las variables con mayor peso dentro de nuestra base de datos. 

Dentro de los distintos arboles de decisión generados, si una columna es seleccionada muy a menudo como la mejor división de datos posibles, es probable que esa columna contenga poca información, o que la información que contenga sea de poca utilidad para el modelo que se trata de construir. 

88 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Existe muchos mas métodos de selección de características que se emplean habitualmente en modelos de preprocesado de datos. Muchas de estas técnicas contienen derivados estadísticos de las que ya hemos estudiado o son desarrolladas específicamente para el tipo de modelo que queremos construir. 

Es importante realizar un correcto preprocesado de nuestros datos previo a la construcción de neustro modelo, ya que esto va a condicionar directamente el tipo de resultado que obtengamos del mismo. 

89 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

## **4. Aprendizaje por refuerzo** 

_“El aprendizaje por refuerzo esta caracterizado por la toma de decisiones de un agente en función de su ambiente, basándose en un sistema de recompensas y penalizaciones, tratando de maximizar las primeras.”_ 

El aprendizaje por refuerzo es un área dentro de la inteligencia artificial en plena explosión. Su crecimiento ha sido exponencial desde su aparición en los años 50, en paralelo al resto de técnicas de aprendizaje automático.  El desarrollo del aprendizaje por refuerzo ha estado siempre limitado por la capacidad computacional disponible para ejecutar este tipo de modelos. Un punto de inflexión en la implantación de este tipo de algoritmos fue la aparición de TD-Gammon, un programa informático programado para jugar al backgamon, desarrollado por Gerald Tesauro en 1992 en el laboratorio de investigación de IBM Thomas J. Watson. Este programa supuso una gran revolución ya que exploró nuevas estrategias de juego que los humanos contra los que se había entrenado no habían empleado. La evolución de los algoritmos aplicados unido al progreso de la tecnología computacional abrió la puerta al desarrollo de nuevas aplicaciones impensables hasta el momento. Actualmente existe un subcampo de aprendizaje por refuerzo en el cual se emplean algoritmos de Deep Learning con los que se ha logrado programar agentes capaces de vencer a jugadores humanos en juegos mucho mas complejos como el Starcraft II o el Dota-2. Esto supone una gran mejora respecto a logros anteriores y logra un gran progreso en el estado del arte de este tipo de modelos. 

En términos de clasificación, el aprendizaje por refuerzo no puede incluirse en una categoría especifica dentro de las clasificaciones tradicionales de inteligencia artificial ya que este tipo de aprendizaje se basa en la aplicación especializada de distintas técnicas de machine learning y Deep learning. En un modelo de aprendizaje por refuerzo vamos a poder encontrar algoritmos de regresión en combinación con redes neuronales de Deep Learning. A diferencia del aprendizaje supervisado, en el que contamos con los datos de entrenamiento en los que encontramos la respuesta correcta que tratamos de predecir, en el aprendizaje por refuerzo no existe una respuesta correcta concreta, el agente debe tomar una decisión sobre que responder en base a experiencias pasadas, tanto positivas como negativas. En ausencia de un conjunto de datos de entrenamiento, está obligado a aprender de su experiencia. También se diferencia de otros tipos de modelos de inteligencia artificial en el modo en el que interpreta las cosas. Por ejemplo, si presentamos una manzana a distintos tipos de algoritmos vamos a encontrarnos con diferentes respuestas: 

90 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- El aprendizaje supervisado, habrá aprendido de la base de datos de entrenamiento que es el nuevo objeto que le estamos presentando y como respuesta nos dará una respuesta categórica: Eso es una manzana 

- El aprendizaje no supervisado, no tendrá etiquetas con las que identificar el nuevo objeto que le hemos presentado, pero será capaz de correlacionarlo con otros objetos similares, por ello nos dará como respuesta un conjunto de objetos similares (manzanas verdes, manzanas rojas…) 

- En el caso del aprendizaje por refuerzo, el algoritmo identificará el objeto por interacciones previas con el mismo y realizará una acción con el. Nos comemos la manzana porque esta rica y nos hace sentir bien. 

El aprendizaje por refuerzo esta caracterizado por la toma de decisiones de un agente en función de su ambiente, basándose en un sistema de recompensas y penalizaciones, tratando de maximizar las primeras. Dentro de los modelos de aprendizaje por refuerzo encontramos cuatro elementos esenciales: 

- **[[Agente_Coordinador|Agente]]:** El programa que entrenamos para la toma de decisiones. El algoritmo en si es el agente. 

- **Acción:** Es el conjunto de todos los posibles movimientos que puede realizar el agente. Este elemento es bastante auto-explicativo, pero debemos tener en cuenta que el agente debe elegir entre un conjunto de acciones predefinidas y finitas para realizar en respuesta a un estímulo del ambiente. 

- **Ambiente:** El entorno en el cual se desarrolla el programa, es decir donde el agente realiza acciones y toma decisiones. El ambiente puede ser el mundo real, un mundo virtual desarrollado para un juego, o un entorno específicamente desarrollado para el entrenamiento del algoritmo. 

- **Recompensas:** Consiste en la evaluación de una acción. Esta puede ser positiva o negativa. Dentro de las recompensas además de positivas y negativas directas podemos definir otros tipos de recompensas que afecten al comportamiento del agente. Un ejemplo son los factores de descuento. Estos se multiplican por las recompensas positivas futuras, reduciéndolas, para amortiguar el efecto de estas recompensas en el sistema de decisión del agente. De esta manera logramos que las recompensas inmediatas tengan un mayor valor que las recompensas futuras. 

91 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Para comprender mejor estos conceptos lo mas sencillo es hacerlo a través de un ejemplo. Imaginemos que nos encontramos dentro de un videojuego, por ejemplo, Mario Bros. En este caso, el **agente** será Mario que se encuentra controlado por nosotros (el algoritmo que toma las decisiones), el **ambiente** será el mundo virtual en el que se desarrolla el juego, donde estaremos sometidos a una serie de estímulos al lo largo del juego. Estos estímulos van a consistir en una serie de objetos de los que podemos hacer uso. Estos objetos traerán consigo una **recompensa** . Esta puede ser positiva, como comer un champiñón y hacernos mas grandes, o recoger una estrella y tener superpoderes de manera temporal, o negativa, chocar con una tortuga y perder una vida, o tocar el fuego y hacernos mas pequeños. Las **acciones** que desarrollemos dentro del juego producirán estas recompensas. 

Los modelos de aprendizaje por refuerzo se basan en comportamientos conductuales, imitando los que ejecutamos los seres humanos de manera innata. Un ejemplo de aprendizaje por refuerzo que podemos encontrar en la vida real ejecutado por personas es la identificación de anuncios en una página web. De manera inconsciente cuando abrimos una pagina que contiene anuncios tendemos a ignorarlos y a centrar nuestra atención en el contenido que estábamos buscando dentro de la página. En este ejemplo el agente del aprendizaje conductual somos nosotros mismos la página web será el ambiente y los estímulos que nos presenta serán el contenido que estábamos buscando dentro de la página y anuncios a su alrededor. De manera inconsciente el agente (nosotros) ejecutamos la acción de ignorar los anuncios y centrar nuestra atención en el contenido que estábamos buscando, ya que la recompensa es localiza lo que estábamos buscando o quedarnos con una información irrelevante para nosotros. Sabemos que la información del anuncio nos va a resultar irrelevante en comparación con la información del resto de la página ya que nos hemos encontrado en esta situación en repetidas ocasiones. La primera vez que abrimos una página web con anuncios, inspeccionamos la página completa y asociamos unas recompensas positivas y negativas para cada tipo de contenido. 



Ilustración 81: Diagrama de aprendizaje por refuerzo [45] 

92 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Imitar este tipo de comportamiento conductual mediante algoritmos es una tarea compleja, ya que al tratarse de sistemas dinámicos en los cuales no existe una respuesta explicita correcta requieren un proceso de exploración antes de ser útiles. A lo largo de este proceso de exploración el agente debe decidir entre obtener recompensas positivas de manera inmediata o continuar explorando y encontrar nuevas formas de encontrar recompensas. El aprendizaje por refuerzo resuelve el difícil problema de correlacionar las acciones inmediatas con los resultados tardíos que producen. Al igual que los humanos, los algoritmos de aprendizaje por refuerzo a veces tienen que esperar para ver el fruto de sus decisiones. Operan en un entorno de retorno retrasado, donde puede ser difícil comprender qué acción conduce a qué resultado en muchos pasos de tiempo. Este tipo de modelos se basan en un proceso de decisión múltiple, con un fin último al que deben llegar por medio de recompensas positivas, evitando las negativas. 

Existen muchas aplicaciones de aprendizaje por refuerzo en la vida real, uno de los que esta acaparando una gran atención últimamente por sus avances es proceso del coche autónomo. 

El proceso de aprendizaje del coche autónomo es uno de los mas complejos que podemos encontrar en los modelos de aprendizaje por refuerzo, ya que el agente va a encontrarse con situaciones en las que ninguna de las acciones posibles va a resultar positivas, en cuyo caso deberá decantarse por la que genere un menor impacto negativo en el proceso. En el ejemplo del coche autónomo podemos identificar claramente los componentes del modelo de aprendizaje por refuerzo. El agente será el sistema de conducción autónoma del coche. El ambiente en este caso supone un reto adicional ya que el ambiente de aprendizaje del modelo no puede ser el mismo ambiente que en el que se va a desarrollar la actividad, ya que no podemos entrenar un modelo de aprendizaje reforzado en las carreteras por las que se encuentran circulando el resto de los coches, ya que las respuestas de tipo negativo pueden causar efectos fatales. A la hora de desarrollar un modelo capaz de conducir un coche autónomo es crucial contar con un simulador realista. Otro de los grandes desafíos se encuentra en transferir el sistema fuera del entorno de entrenamiento a el mundo real. Escalar y ajustar la red a parámetros reales supone un gran reto en el desarrollo de coches autónomos. En cuanto al sistema de recompensas varía en función del desarrollador, pero todos tienen como objetivo común llegar al destino de manera segura. Este sistema es la única forma que existe de comunicación con el algoritmo (el agente solo responde a través del sistema de recompensas y penalizaciones), por lo que debemos preparar al sistema ante todas las posibilidades imaginables. 

Esto trae consigo un desafío aun mayor, ya que la introducción de nuevos estímulos en el sistema puede hacer que algunas de las respuestas pre entrenadas sean sustituidas por otras nuevas. Este escenario es especialmente peligroso en el caso de la conducción autónoma dato que ante una situación de emergencia no podemos contar con la seguridad de que el piloto va a responder con la acción que esperamos o ha desarrollado una nueva habilidad de la que no tenemos constancia. 

93 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

El mercado de la conducción autónoma esta en plena explosión con múltiples modelos disponibles en producción. El más conocido de todos es el piloto automático disponible dentro de los coches de Tesla. Estos modelos son los primeros que han salido al mercado de manera generalizada, pero podemos encontrar otros muchos ejemplos de desarrollo de conducción autónoma que pronto podremos ver en el mercado.  Amazon por ejemplo tiene en marcha un proyecto de un coche de carreras autónomo. AWS DeepRacer es un automóvil de carreras autónomo que se diseñó para probar RL en una pista física. Utiliza cámaras para visualizar la pista y un modelo de aprendizaje de refuerzo para controlar el acelerador y la dirección. Dentro de su plataforma de AWS ofrece la posibilidad de probar este modelo a desarrolladores [46]. Por otra parte, Google ha avanzado en el desarrollo de su proyecto de coche autónomo Waymo, y ya esta realizando pruebas en el mundo real. En contraposición con los éxitos que podemos encontrar en el mercado de los coches autónomos también encontramos ejemplos de proyectos que han sido suspendidos por errores fatales, como puede ser las pruebas que realizó Uber con sus coches autónomos en las cuales una de ellas termino en fatal accidente donde falleció una mujer por atropello. 

Los coches autónomos son solo un ejemplo de las aplicaciones de aprendizaje por refuerzo que podemos encontrar hoy en día implantadas en la vida real 

- Automatización de procesos industriales: Agentes de modelos de aprendizaje por refuerzo están desarrollando múltiples tareas dentro del ámbito industrial. Estos modelos están siendo desarrollado especialmente para realizar tareas potencialmente peligrosas para los seres humanos o cuyo rendimiento puedan superar con facilidad. Un ejemplo del uso de este tipo de modelos es la implantación que ha hecho Google del sistema de Deepmind para la gestión energética de la refrigeración de sus centros de datos[47]. Este modelo de aprendizaje por refuerzo funciona mediante las siguientes fases: 

   1. Cada 5 minutos se recogen datos de los sensores físicos instalados en el datacenter mediante una aplicación desarrollada en la nube. 

   2. Esta información se utiliza para predecir como las diferentes combinaciones afectarán a el consumo energético en el futuro. 

   3. El agente selecciona acciones que satisfacen las restricciones de seguridad y minimizan el futuro consumo de energía. 

   4. Las acciones óptimas se devuelven al datacenter, donde el sistema local verifica sus propias limitaciones de seguridad antes de la implementación. 

94 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- Aplicaciones en mercados financieros: Una de las áreas en las que mas se ha desarrollado modelos de aprendizaje por refuerzos son los mercados de activos. IBM ha desarrollado una compleja plataforma basada en aprendizaje por refuerzo que cuenta con la habilidad de realizar compraventas en mercados. Esta calcula la función de recompensa en función de la pérdida o ganancia de cada transacción financiera. 

- Aprendizaje por refuerzo en procesado de lenguaje natural: El aprendizaje por refuerzo tiene un importante papel en el procesado de lenguaje natural, ya que se puede programar un agente para responder preguntas, traducir textos o resumirlos. 

- Aprendizaje por refuerzo en salud: Este tipo de algoritmos son frecuentemente utilizados en el área de salud como dispensación de tratamientos, o diagnostico basado en pruebas médicas. Existen múltiples agentes en desarrollo, pero su aplicación en pacientes reales aun se encuentra bastante restringido debido a los potenciales riesgos de esta tecnología 

- Aprendizaje por refuerzo en marketing: Uno de los ejemplos clásicos de aplicación de este tipo de modelos se encuentra en los motores de recomendación personalizados en base al histórico de nuestras acciones, la situación en la que estemos realizando la búsqueda, por ejemplo, los motores de recomendación se ven afectados por la hora del día al que realices la búsqueda, o la disponibilidad de recursos. 

El aprendizaje por refuerzo es una tecnología en pleno desarrollo y que va a tener aplicaciones en prácticamente todas las áreas de la vida real. El aumento de la capacidad computacional disponible y el desarrollo de nuevos algoritmos de software dan lugar a la aparición constante de nuevas aplicaciones que hace unos pocos años solo podíamos imaginar a través de la ciencia ficción.[50] 

Actualmente existen múltiples plataformas de desarrollo especializadas en el aprendizaje por refuerzo. Una de las mas interesantes se conoce como Gym [49] y esta desarrollada para Python. Gym es un conjunto de herramientas para desarrollar y comparar algoritmos de aprendizaje por refuerzo. Esta plataforma es de código abierto y en ella vamos a poder encontrar un entorno especializado en aprendizaje de refuerzo y múltiples modelos desarrollados con los que podemos iniciarnos dentro del mundo del aprendizaje supervisado. En esta librería podemos encontrar algunos ejemplos de problemas de teoría de control de la literatura clásica de Reinforcement Learning, con los que podemos comenzar en el mundo del desarrollo de este tipo de modelos. 

95 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Uno de los ejemplos clásicos mas utilizados para comprender el funcionamiento de este tipo de modelos es problema planteado por Barto, Sutton y Anderson en “Elementos adaptativos similares a neuronas que pueden resolver un problema de control de aprendizaje difícil”[51]. En este problema Un poste está unido por una articulación no accionada a un carro, que se mueve a lo largo de una pista sin fricción. El péndulo comienza en posición vertical y el objetivo es evitar que se caiga aumentando y reduciendo la velocidad del carro. Para ello debemos programar un agente que se encargue de realizar distintas acciones con el objetivo final de que el poste no llegue a tocar el suelo. 



Ilustración 82: Problema del poste y el carro 

Dentro de la propia librería podemos encontrar un ejemplo resuelto de como entrenar a un agente para hacerle frente a este problema. Vamos a utilizar este ejemplo para entender los distintos parámetros que debemos tener en cuenta a la hora de enfrentarnos a este tipo de modelos. 

Para poder ejecutar este modelo en primer lugar debemos de instalar los módulos de gym en Python. Esta librería es de código abierto y podemos incluirla dentro de nuestro entorno ejecutando el siguiente comando dentro de nuestro editor de notebooks. 

96 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 83: Instalación librería gym 

Podemos comprobar en la salida del comando que la librería es descargada de los repositorios oficiales de Python e instalada en nuestro entorno. 

A continuación, ejecutamos el código que podemos encontrar como ejemplo en la documentación de la librería [52]. 



Si ejecutamos este código después de haber instalado las librerías necesarias, se abrirá una nueva ventana en la que podemos ver el resultado de la toma de decisiones del agente de manera interactiva. 

Si analizamos este código podemos ver las distintas partes de un modelo de aprendizaje reforzado dentro del script: 

- El ambiente esta definido por la variable env, en la que importamos el entorno predefinido de CartPole 

- El agente define sus acciones mediante la variable de action 

- Las recompensas positivas o negativas son recibidas como respuesta a una acción en el ambiente 

97 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

El proceso que sigue este modelo es el siguiente: 

En la primera línea importamos la librería que vamos a emplear. 

A continuación, inicializamos el entorno predefinido dentro de la librería de CartPole. Este entorno nos construirá el ambiente en el cual el agente va a realizar la toma de decisiones. Iniciamos el entorno en su punto inicial con el comando env.reset() y a continuación entramos en un bucle en el que el agente puede realizar una acción. Las acciones disponibles en este entorno consisten en empujar el carro hacia la izquiera o hacia la derecha con una velocidad fija. 

El entorno nos devuelve una serie de variables cada vez que el agente realiza una acción: 

- Observation: Esta variable nos proporcionará información sobre el ambiente, en este caso sobre la posición de carro, su velocidad, el ángulo del poste y su velocidad angular 

- Reward: Esta variable nos devolverá la puntuación que obtenemos tras cada acción 

- Done: Si el juego ha terminado o no 

- Info: En este entorno podemos contar con información adicional que nos ayude a programar nuestro agente 

En base a estas variables nuestro agente realizará una acción (mover el carro a la derecha o a la izquierda) para tratar de maximizar los refuerzos positivos, creando un equilibrio en el poste que se encuentra adherido al carro. 

En este ejemplo contamos con un agente pre-programado que realizará las acciones por nosotros. Si deseamos adentrarnos mas dentro del mundo de la programación podríamos generar nuestro propio agente que realice acciones en base a las variables que nos devuelve nuestro entorno. 

98 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

## **5. Deep Learning** 

_“El aprendizaje profundo tiene como objetivo la imitación del comportamiento humano, es decir trata de que los modelos realicen funciones que son naturales para un humano: aprender de la experiencia.”_ 

El Aprendizaje Profundo o Deep Learning, es un campo de la inteligencia artificial que se encuentra englobado dentro del Machine Learning. Este tipo de aprendizaje se caracteriza por emplear una estructura jerárquica de redes neuronales artificiales que se construyen tratando de imitar la estructura interna de un cerebro humano, utilizando nodos conectados que imitan las conexiones sinápticas neuronales. Este tipo de arquitectura nos permite abordar en análisis de datos de una forma no lineal 

El aprendizaje profundo tiene como objetivo la imitación del comportamiento humano, es decir trata de que los modelos realicen funciones que son naturales para un humano: aprender de la experiencia. 

El aprendizaje profundo es una tecnología clave detrás de los vehículos sin conductor, que les permite reconocer una señal de tráfico o distinguir un peatón de un farola. Es la clave para el control por voz en dispositivos de consumo como teléfonos, tabletas, televisores y altavoces inteligentes. El aprendizaje profundo está recibiendo mucha atención últimamente y es por una buena razón: está logrando resultados que antes no eran posibles. 

El origen del Deep learning se remonta a los años 40 donde surgieron los primero estudios sobre las aplicaciones de modelos biológicos al campo de la computación, las bases del Deep learning fueron asentadas por Warren McCulloch y Walter Pitts con la publicación de su artículo “A logical calculus of the ideas immanent in nervous activity”[53]. En este articulo se presentaba un modelo de neurona que evolucionaria hacia lo que hoy conocemos como Deep learning. Este tipo de aprendizaje fue evolucionando a lo largo de las siguientes décadas donde cabe destacar las aportaciones realizadas al campo por Frank Rosenblatt, el cual presento su modelo de perceptrón en 1958 [54]. Durante las décadas de los 80 y 90 surgieron nuevos modelos que han dado lugar a las aplicaciones que podemos encontrar hoy en dia de Deep learning. Sin embargo, no fue hasta la época de los 2000 cuando se definió el concepto de Deep Learning que conocemos en la actualidad. Históricamente el Deep learnign ha sido asociado a los modelos Artificial Neural Networks (ANN), debido a su similitud con el cerebro humano. 

99 

**Módulo. Machine Learning y Deep Learning** 

**Centro Europeo de Postgrado** 

Hoy en día, el Deep Learning ya no se encuentra tan relacionado con la perspectiva neurocientífica.  Ahora, esta área trabaja con modelos que compuestos por múltiples niveles entrelazados entre si. 

Pese a que el origen de esta tecnología se remonta a los años cuarenta, no ha sido hasta la actualidad cuando este tipo de aprendizaje ha empezado a mostrar precisión de vanguardia, que a veces supera el rendimiento a nivel humano. El aprendizaje profundo logra una precisión de reconocimiento en niveles más altos que nunca. Esto en parte es debido a los requerimientos técnicos necesarios para la construcción de este tipo de modelos. El aprendizaje profundo requiere de dos factores cruciales para lograr estos resultados: 

- **Gran volumen de datos:** El aprendizaje profundo requiere grandes cantidades de datos etiquetados. No ha sido hasta la década de 2010 cuando se produjo la gran explosión de datos, que en la actualidad mantiene un crecimiento exponencial. De acuerdo con Statista [55] la cantidad total de datos que se consumen a nivel mundial aumentará rápidamente a 64,2 zettabytes en 2020 y 79 zettabytes en 2021, mientras que se prevé que crezca a más de 180 zettabytes hasta 2025. La disponibilidad de estos grandes volúmenes de datos va a permitir el desarrollo de modelos cada vez mas complejos y eficientes. En contraposición la gestión de estas bases de datos cada vez requerirá un aumento en la capacidad de almacenamiento. Según la misma encuesta se espera que la base instalada de capacidad de almacenamiento aumente a una tasa de crecimiento anual compuesto de 19,2% de 2020 a 2025. 

- **Capacidad computacional:** El aprendizaje profundo requiere una gran potencia de cálculo. La aparición de GPU _(Graphics Processing Unit)_ de alto rendimiento que tienen una arquitectura paralela eficiente para el aprendizaje profundo supuso un gran avance en esta tecnología. Cuando se combina con clústeres o computación en la nube, esto permite a los equipos de desarrollo reducir el tiempo de entrenamiento para una red de aprendizaje profundo de semanas a horas o menos. 

Estos factores ayudan a que los productos electrónicos de consumo generen produzcan resultados no vistos hasta el momento. 

El factor diferenciador que presenta el Deep learning respecto a otras áreas de la inteligencia artificial es que este es capaz de aprender por si mismo sin necesidad de que el ser humano (el programador) le de las indicaciones necesarias para realizar su labor. Este tipo de aprendizaje se asemeja al proceso de aprendizaje que realiza un niño pequeño capaz de resolver tareas que no le han sido enseñadas específicamente. Por ejemplo, en modelos de aprendizaje máquina tradicionales, para poder identificar a un perro, debemos de contar con una base de datos de perros, de la cual hemos extraído una serie de características identificativas, y le hemos presentado al algoritmo estas características indicándoles que son aquellas que son determinantes a la hora de identificar a un perro. 

100 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

El programa entonces entiende que esas características son propias de los perros y si se le proporciona una nueva imagen y esta contiene las características dadas, entonces el programa nos va a devolver la respuesta de que la imagen proporcionada corresponde a un perro con un intervalo de confianza definido por el algoritmo. 

En contraposición en un modelo de aprendizaje profundo no necesitamos darle al algoritmo ningún tipo de parámetro de entrada mas allá de los datos de entrenamiento. La red neuronal a través de sus distintas capas extraerá las características de todas las imágenes proporcionadas. Cada foto se deconstruirá en múltiples niveles de detalle, desde formas grandes y generales hasta líneas pequeñas. Si una forma se repite mucho, el algoritmo lo etiquetará como una característica importante. Tras analizar suficientes imágenes el modelo será capaz de identificar que características se corresponden con un perro y será capaz de identificarlo en cualquier escenario. Este tipo de lógica es la misma que sigue un infante en sus primeros años de vida. Si nadie le enseña lo que es un perro cuando haya visto los suficientes será capaz de identificarlos como tal en cualquier escenario sin necesidad de intervención externa. 

Dentro del aprendizaje profundo podemos realizar una clasificación de los distintos tipos de redes que podemos utilizar para realizar estos modelos. En este capítulo vamos a introducir las bases necesarias para comprender el funcionamiento de las redes neuronales y las principales redes profundas que se esta empleando actualmente en la industria. 

### **5.1. Redes Neuronales** 

El término de redes neuronales hace referencia al modelo biológico de procesado de información. Aunque este termino se emplea frecuentemente como sustituto del término red neuronal artificial, es importante diferenciar ambos términos. La comprensión del modelo biológico de redes neuronales facilita la comprensión e implantación de las redes neuronales artificiales. 

La investigación de las redes neuronales tuvo su gran revolución a finales del siglo XIX tras la presentación de los trabajos de Santiago Ramón y Cajal [56] a principio de siglo sobre la estructura neuronal. Sus trabajos supusieron tal cambio de paradigma en el área de la neurociencia que le hicieron ganar el premio Nobel de Fisiología y Medicina de 1906 que compartió con Camilo Golgi. Unido a este trabajo también apareció durante el siglo XIX el trabajo de Sherrington [57], el cual explicó el funcionamiento de las neuronas. El hallazgo de Cajal de que las neuronas eran estructuras anatómicas independientes resaltaba la importancia del espacio entre ellas, ahí era donde la información tenía que pasar de una a otra, el punto clave de la función cerebral. Sherrington completó este trabajo dando lugar al modelo de neurona con el que se trabaja actualmente en neurociencia. 

101 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

La célula nerviosa se denomina **neurona** , que es la unidad funcional del sistema nervioso. Estas están clasificadas en base a su función, pudiendo ser neuronas sensoriales, motoras y de asociación. Se estima que en cada milímetro cúbico del cerebro hay cerca de 50.000 neuronas. La estructura de una neurona se muestra en la Ilustración 84. 



Ilustración 84: Esquema de una neurona 

Dentro de esta estructura cabe destacar tres estructuras principales: el cuerpo de la neurona o soma, se encarga de realizar los distintos procesos metabólicos de la neurona, las dendritas, estructuras que permiten las conexiones de entrada hacia la neurona y el axón que es la estructura de salida de la neurona. Este último se encarga de transmitir la información a las neuronas colindantes mediante impulsos eléctricos dirigidos hacia las dendritas de otras células. 

Esta transmisión de información se realiza mediante un proceso químico que permite tienen como efecto elevar o disminuir el potencial eléctrico dentro del cuerpo de la célula receptora. Si su potencial alcanza un cierto umbral, se envía un pulso o potencial de acción por el axón. 

El sistema de neuronas biológico está compuesto por neuronas receptoras (sensores), que se encargan de recibir los impulsos del medio externo, neuronas de transferencia o procesado (neuronas ocultas), que se encargan de transmitir la información hacia el último tipo de neuronas, las neuronas de salida. Estas neuronas se encargan de ejecutar el mandato final, por ejemplo, el movimiento de un músculo o la activación de un órgano. 

El grueso de neuronas de transferencia se encuentra en el cerebro y en el sistema nervioso central, que permite el procesado de la información y la transferencia de esta hacia el sistema nervioso periférico, en el que encontramos las neuronas receptoras, que reciben señales de los órganos sensoriales, ojos, oídos… y las neuronas de salida que se encargan de ejecutar el mandato. 

102 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

### **5.1.1. Redes Neuronales Artificiales** 

Las redes neuronales artificiales son una representación de las redes neuronales biológicas. Estas imitan el modelo de transmisión de información del cerebro debido a su flexibilidad, lo que le brinda una gran capacidad para resolver una amplia variedad de problemas. Al igual que sucede en la estructura de un sistema neuronal biológico, los elementos esenciales de proceso de un sistema neuronal artificial son las neuronas. 

El concepto de red neuronal ha sido definido por múltiples autores, en concreto Hassoun lo definió en su libro _“Fundamentals of Artificial Neural Networks”_ [58] como “un modelo computacional en paralelo, compuesto de unidades procesadoras adaptativas con una alta interconexión entre ellas” 

Estas unidades procesadoras es lo que conocemos como neuronas artificiales, que nos permiten generar una respuesta o salida a partir de un conjunto de datos de entrada. 

Las neuronas se agrupan dentro de la red formando niveles o capas. Dependiendo de su situación dentro de la red, se distinguen tres tipos de capas: 

- La capa de entrada, que recibe directamente la información procedente del exterior, incorporándola a la red. Estas neuronas se corresponderían con las neuronas sensoriales en un sistema biológico 

- Las capas ocultas, internas a la red y encargadas del procesamiento de los datos de entrada. Estas capas pueden estar precedidas de otras capas ocultas o de capas de entrada. 

- La capa de salida, que transfiere información de la red hacia el exterior, esta capa proporciona la solución de la RN. 

Las RNAs pueden tener varias capas ocultas o no tener ninguna. Los enlaces sinápticos (las flechas llegando o saliendo de una neurona) indican el flujo de la señal a través de la red y tienen asociado un peso sináptico correspondiente. El número de capas de una RNA es la suma de las capas ocultas más la capa de salida. 

103 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 85: Esquema de una red neuronal artificial[59] 

La unidad central de procesado de este tipo de redes se conoce como neurona artificial o perceptrón. Estas están caracterizadas por comparar la salida del sistema con una señal deseada. El perceptrón es la unidad central de procesamiento de la red, recibe información del exterior o de otras neuronas y genera una salida que se envía hacia la siguiente capa oculta o hacia la capa de salida. 

El proceso de aprendizaje de estas neuronas se basa en reglas de propagación de información. Cada una de las conexiones de entrada de la neurona se conocen como pesos sinápticos, como analogía del proceso biológico. La propagación de esta información se basa en la modificación de los pesos sinápticos asignados para realizar la tarea asignada a esa neurona. 



Ilustración 86: Esquema de funcionamiento de una neurona artificial [60] 

104 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

En la Ilustración 86 podemos ver los diferentes elementos que intervienen en el proceso de aprendizaje de una neurona. 



- Un conjunto de datos de entrada 

- Pesos sinápticos asociados a los datos de entrada. Estos pesos definen la intensidad del parámetro de entrada. El ajuste de estos pesos es lo que nos permite resolver un determinado problema. 

- • Una función de entrada que combine los datos con sus respectivos pesos sinápticos dentro de la neurona 

- Una regla de propagación, que permite obtener a partir de las entradas y los pesos el valor del potencial post-sináptico de la neurona 

- Una función de salida o transferencia que se encarga de proporcionar la salida de la neurona 

El modo en el que se organizan las distintas capas de las redes neuronales se conoce como [[MOC_Arquitectura_IA|arquitectura neuronal]]. Por medio de esta arquitectura se busca emular una serie de conceptos claves de la arquitectura biológica [61] 

- **Procesamiento paralelo:** En un modelo biológico la información se procesa al mismo tiempo en millones de neuronas. Las redes artificiales pretenden emular este comportamiento, logrando acortar significativamente los tiempos de entrenamiento. 

- **Memoria distribuida:** En un procesamiento clásico de la información, esta se encuentra en posiciones definidas mientras que en una red neuronal la información se encuentra distribuida a lo largo de las sinapsis de la red, generando una redundancia en los datos, evitando pérdidas de información. 

- **Adaptabilidad al entorno** : La adaptabilidad de las redes biológicas permite aprender de la experiencia generalizar conceptos a partir de casos particulares. Esta es probablemente la característica mas importante y que aporta el poder a las redes neuronales. 

A rasgos generales dentro de la arquitectura neuronal podemos encontrar la definición de tres niveles: 

**Microestructura:** Es el nivel mas bajo dentro de la arquitectura neuronal y hace referencia al nodo central de la red: la neurona o perceptrón. En este nivel se fijan características troncales de la red como la función de entrada. 

105 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

**Mesoestructura:** Es el nivel intermedio dentro de la arquitectura neuronal. En este nivel se fijan las formas de conexión y la disposición de los elementos que actúan en la neurona. 

**Macroestructura:** Es el último nivel contemplado dentro de la arquitectura de redes neuronales. En el se pueden combinan distintas redes para generar modelos mas precisos. No todas las redes neuronales llegan a este nivel. 

Además de por niveles podemos clasificar la arquitectura de una red neuronal en base a tres parámetros: número de capas, tipo de conexiones y grado de conexión 

#### **Número de capas** 

Atendiendo al número de capas las redes neuronales se pueden clasificar en dos grupos principales: 

- **Redes Neuronales monocapa:** Son las redes neuronales mas sencillas. Estas solo contienen una capa de neuronas de entrada y una capa de neuronas de salida, sin capas ocultas intermedias. Es en la capa de salida donde se realizan los cálculos de la red neuronal. 

- **Redes Neuronales multicapa:** A diferencia de la clasificación anterior las redes que encontramos dentro de esta clasificación  cuentan con capas intermedias (capas ocultas) entre la entrada y la salida. Este tipo de red puede estar total o parcialmente conectada. 

#### **Tipo de conexiones** 

En función de la dirección de transmisión de la información podemos clasificar las redes neuronales en dos tipos 

- Redes Neuronales unidireccionales o no recurrentes ( feedforward): En este tipo de redes la propagación de la señal se realiza en un único sentido (hacia adelante). En estas redes no existe retroalimentación y las estructuras no presentan memoria. 

- Redes Neuronales retroalimentadas o recurrentes (feedback): Este tipo de redes la propagación de la señal puede presentarse en todas las direcciones de la red. Dentro de la red vamos a encontrar lazos de retroalimentación que pueden conectar neuronas de diferentes capas, de la misma capa o una neurona consigo misma. Esta estructura recurrente la hace especialmente adecuada para estudiar la dinámica de sistemas no lineales 

106 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

#### **Grado de conexión** 

- **Redes Neuronales totalmente conectadas:** En este tipo de redes todos los perceptrones o neuronas de un modelo están conectadas con la capa contigua. Esta conexión puede realizarse con la capa siguiente en el caso de redes unidireccionales o con las de la anterior en el caso de redes retroalimentadas. 

- **Redes parcialmente conectadas:** En este tipo de redes todos no se da la conexión total entre neuronas de diferentes capas. 



Ilustración 87: a) Red neuronal monocapa, b) Red neuronal multicapa no retroalimentada c) Red neuronal multicapa retroalimentada[59] 

Dentro de las redes neuronales podemos encontrar distintos métodos de aprendizaje en función del método que se haya implementado dentro de cada una de sus neuronas para calcular los pesos sinápticos de los datos de entrada y la función de salida que es enviada a la siguiente neurona de la red. Estos métodos de aprendizaje son los que podemos encontrar dentro del esquema genera de aprendizaje máquina. Podemos clasificar las redes neuronales en función de los métodos de los algoritmos o reglas de aprendizaje utilizadas en cada una de las neuronas. 

- **Redes neuronales de aprendizaje supervisado:** Las neuronas son presentadas con la salida correcta de los patrones de entrada. La neurona es entrenada como si se tratara de un modelo de aprendizaje supervisado aislado. Se compara la salida de la neurona con los parámetros deseados y se modifican los pesos sinápticos conforme al error cometido. En este tipo de redes neuronales es necesario proporcionar datos de entrenamiento etiquetados a la neurona para poder realizar el ajuste de los parámetros de diseño. 

- **Redes neuronales de aprendizaje no supervisado:** Las neuronas no son presentadas con la salida correcta de los datos de entrada. En este caso la neurona organiza las bases de datos proporcionadas mediante métodos de clústering. 

107 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- **Redes neuronales de aprendizaje por refuerzo:** En este caso las neuronas no son presentadas con los parámetros correctos de salida, si no con una respuesta de tipo verdadero o falso en función de si la respuesta generada por la red corresponde con la respuesta correcta o no. 

- **Redes neuronales hibridas:** En este tipo de redes algunas se mezclan distintos tipos de aprendizaje, algunas capas presentan aprendizaje supervisado y otro aprendizaje no supervisado. 

### **5.1.1.1. Perceptrón simple** 

El modelo de perceptrón simple fue el primer modelo de Deep learning explorado. Este modelo fue presentado por Rosenblatt en 1959 [62]. La estructura del perceptrón se inspira en las primeras etapas de procesamiento de los sistemas sensoriales de los animales, en los cuales la información va atravesando sucesivas capas de neuronas, que realizan un procesamiento progresivamente de más alto nivel. El perceptrón simple es un modelo neuronal unidireccional, compuesto por dos capas de neuronas, una de entrada y otra de salida. 



Ilustración 88: Perceptrón simple 

Las neuronas de entrada no realizan ningún cómputo, únicamente envían la información a las neuronas de salida. En esta capa es donde se realizan las operaciones de la red que aplica una función de activación paso o signo. 

Este tipo de modelos son útiles en problemas de clasificación lineales, sin embargo, no es útil en problemas de clasificación no lineal, como demostraron Minsky y Papert [63] en 1969. En la actualidad este tipo de modelo es poco utilizado ya que se puede realizar las mismas tareas mediante métodos de inteligencia artificial mas sencillos y que no requieren tanta potencia computacional. 

108 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

### **5.1.1.2. Perceptrón múltiple** 

El modelo de perceptrón múltiple surgió como una evolución del perceptrón simple. Este tipo de modelo permite la resolución de problemas no lineales, al incluir diferentes capas de neuronas ocultas entre la capa de entrada y la capa de salida. Este modelo de perceptrón fue presentado por Rumelhart et al. [64] en 1986. Las características de el modelo presentado se basaban en una red multicapa unidireccional en la que el aprendizaje era supervisado. Este modelo continuó evolucionando hasta las redes de perceptón múltiple que conocemos a dia de hoy, las cuales están caracterizadas por presentar una estructura no lineal. Además, las redes de perceptrón múltiple modernas presentan tolerancia ante fallos, y están consideradas como aproximadores universales. Este tipo de redes requieren largos periodos de entrenamiento antes de estar disponibles para su uso, pero en contraposición son muy rápidas procesando nuevos datos. 

La arquitectura de un modelo de perceptrón múltiple esta representada en la Ilustración NNN. En esta arquitectura podemos encontrar los siguientes elementos: 

- **Capa de entrada:** Se encuentran las neuronas sensoriales o receptivas. Se encargan de pasar la nueva información al modelo 

- **Capa de salida:** Se encuentran las neuronas de salida o ejecutoras. Proporciona al exterior la respuesta de la red para cada patrón de entrada. 

- **Capas ocultas:** Realizan un procesamiento no lineal de los datos recibidos. 



Ilustración 89: Ejemplo de perceptrón multicapa 

109 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Los primeros algoritmos de entrenamiento de redes multicapa fueron desarrollados como un concepto general y solamente incluían la propagación hacia delante de la red. Mas adelante se desarrolló el algoritmo de backpropagation, el cual cambió por completo el paradigma de las redes neuronales. Este algoritmo fue descubierto por varios investigadores al mismo tiempo y se popularizó cuando fue incluido en el libro “Parallel Distributed Processing Group” [65]. Este nuevo modelo de entrenamiento suponía un gran cambio respecto los modelos anteriores de propagación hacia adelante ya que este permitía la paralelización del proceso de aprendizaje. Además, la interconexión entre las distintas neuronas de la red, permite la reorganización de las neuronas de las capas ocultas, de manera que las distintas neuronas aprender a reconocer diferentes características. Esto acelera mucho el proceso de predicción una vez la red ha sido entrenada. 

Una de las principales ventajas que presenta este tipo de modelos de redes neuronales multicapa pasan por la solución de problemas complejos en cortos periodos de tiempo gracias a la paralelización del procesado de los datos. Otras de las características que hacen especialmente potentes a este tipo de algoritmos son: 

- Son sistemas no lineales: Esto les permite resolver problemas no lineales y caóticos, que con otro tipo de sistemas no serian posibles de abordar. Esto además nos permite trabajar con conjuntos de datos que no cumplan los requisitos de distribuciones normales que tenemos en el caso de utilizar modelos clásicos de aprendizaje máquina. 

- Son algoritmos con una fuerte capacidad adaptativa: Al trabajar mediante un proceso de ajuste de pesos, todos los datos procesados a lo largo de la vida del modelo son “recordados” dentro de la estructura interna de las neuronas 

- Tienen una mayor tolerancia a errores respecto a los modelos clásicos: Al tratarse de redes complejas configuradas en una estructura paralelizada, el fallo de una neurona no afecta significativamente a la salida global del algoritmo. 

- Capacidad de generalización: Las redes neuronales son capaces de procesar elementos a los cuales no han estado expuestas nunca. Este tipo de procesado es posible gracias al proceso de extracción de características que lleva a cabo la red neuronal, la cual le permite correlar esas características ocultas con datos previos a los que si ha sido expuesta. 

110 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

### **5.1.2. Redes profundas** 

Las redes neuronales profundas se caracterizan por contar con varias de neuronas ocultas entre la capa de entrada y la capa de salida. No existe un umbral claro definido que divida el aprendizaje superficial del aprendizaje profundo, pero se considera que una red profunda el flujo de información debe recorrer al menos dos capas neuronales. 

El entrenamiento de este tipo de redes difiere del entrenamiento clásico de modelos de inteligencia artificial superficial. Como hemos visto en la descripción del perceptrón la unidad básica de la red neuronal es la neurona artificial. Esta cuenta con Un conjunto de datos de entrada y una serie de pesos sinápticos asociados a ellos. En el proceso de entrenamiento de una red neuronal se ajustan los pesos dentro de cada neurona. Para ello se compara el error entre la función de la red y la función deseada, tratando de minimizar este valor. El proceso de entrenamiento de las redes neuronales consta de fases: 

- **Fase de propagación:** Es la primera fase del entrenamiento y en ella se propagan los datos de entrada desde la primera capa neuronal hasta la última. Una vez se ha generado la salida, esta se compara con la deseada y se obtiene un valor para el error. 

- **Fase de retroalimentación:** En esta segunda fase se propagan los datos en dirección contraria, desde la capa de salida hasta la capa inicial pasando por todas las capas de neuronas ocultas intermedias. En este proceso cada neurona recibe un valor del error relativo que esta ha aportado al error general con el que puede ajustar sus pesos. 

El algoritmo que se utiliza en proceso de aprendizaje se conoce como descenso de gradiente. Este algoritmo esta caracterizado por definir cuanto crece la función del error en cada punto. Como tratamos de minimizar este error el algoritmo va a dirigirse en dirección contraria. Esto se conoce como gradiente negativo. 

Este algoritmo se clasifica en función de la cantidad de datos que introduzcamos en el sistema en cada iteración: 

- **Descenso de gradiente en batch:** Introducimos en la red neuronal todos los datos disponibles en una única iteración. Esto puede provocar que los datos se estanquen dentro de la red y que la minimización de la función del error o función de coste presentará pocas variaciones. 

- **Descenso de gradiente estocástico:** Los datos se introducen en el modelo de manera individual, es decir una nueva muestra aleatoria en cada iteración. El error se va a minimizar para cada muestra de manera individual lo que aumentará la información contenida en las capas ocultas y evitará el estancamiento de la información. Como desventaja este método requiere largos periodos de tiempo para entrenar la totalidad del modelo. 

111 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- **Descenso del gradiente estocástico en mini-batch:** Introducimos los datos de entrenamiento en el modelo en pequeños batches o lotes. Esto nos permite minimizar la función de error con una buena precisión, evitando el estancamiento y reduciendo el tiempo de entrenamiento. Este modelo además nos permite paralelizar el proceso de entrenamiento entre todas las neuronas de cada capa. 

Durante el proceso de entrenamiento, además de la minimización del error debemos tener en cuenta otro factor para obtener una red neuronal efectiva: el factor de generalización. Cuando ajustamos nuestra red neuronal mediante el proceso de backpropagation con los datos de entrenamiento corremos el riesgo de generar sobre-entrenamiento u overfitting cuando nuestro modelo se ajusta muy bien a los datos de entrenamiento, pero pierde efectividad con los datos de prueba. Esto puede estar causado por la gran flexibilidad que presentan este tipo de modelos, lo que les hace mas propensos a captar patrones en los datos generados de forma accidental (por ejemplo, cuando estos han pasado por un pre-procesado manual). Para combatir esto existen múltiples técnicas de regularización que podemos aplicar a nuestros modelos. Algunas de ellas pasan por incluir un sistema de parada del entrenamiento dentro del algoritmo (early stopping), o definir un limite en el valor de los pesos para evitar que estos produzcan modelos descompensados. Otros pasan por la combinación de distintos modelos, o por realizar el entrenamiento con bases de datos con orígenes independientes para evitar introducir sesgo dentro del modelo. 

Que un modelo sea capaz de generalizar correctamente es critico a la hora de su implantación en producción ya que este puede no responder bien a un nuevo entorno lo que puede derivar en resultados catastróficos. 

Atendiendo a la estructura interna de la red podemos definir una serie de modelos de red neuronal predefinidos. En esta sección analizaremos algunos ejemplos de los modelos mas utilizados en la industria. 

Para ilustrar la arquitectura de estos modelos se va a emplear el diagrama generado por Fjodor Van Veen en 2016 que nos permite identificar la arquitectura de las distintas células de red en base a su función. Cuando ilustramos una red neuronal nos entramos con el inconveniente de que muchas de ellas comparten estructura en cuanto a sus capas y conexiones, pero las operaciones realizadas dentro de cada una de ellas son completamente diferentes. Por ello en sus diagramas Fjodor ha incluido la representación de la funcionalidad de las células. En la Ilustración podemos encontrar la leyenda correspondiente a este tipo de representaciones. 

112 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 90: Leyenda mapa Fjodor Van Veen 

### **5.1.3. Redes Neuronales Recurrentes (RNN)** 

Las redes neuronales recurrentes son la arquitectura base sobre la cual se implementa el resto de las redes neuronales. Este modelo de redes fue presentado por David Rumelhart en 1986 [66] y su característica principal es que estas redes incorporan la retroalimentación, lo cual permite incorporar en el modelo el concepto de temporalidad. Podemos definir la temporalidad de un modelo como el hecho de que el mismo tenga memoria y pueda aumentar la exactitud de sus predicciones en cada ciclo de entrenamiento. Esto se puede lograr gracias a la retroalimentación del modelo, pudiendo incorporar conexiones neuronales dentro de la misma capa y hacia capas anteriores. 

Una neurona de una capa de red recurrente es capaz de retroalimentase a si misma, de enviar una salida a la capa siguiente de la red neurona y también hacia la capa anterior. 



Ilustración 91: Esquema de una neurona de red recurrente 

En este tipo de neuronas podemos tener como entrada en el mismo instante temporal los datos de entrada procedentes de la capa neuronal anterior, los datos de entrada que acaban de ser procesados por la propia neurona y los datos de entrada procedentes de la capa neuronal siguiente. El procesado que se realiza en ese momento va a ajustar la función de los pesos neuronales en función del momento anterior. Esto es lo que se conoce como memoria celular. Esta característica es lo que hace a los modelos recurrentes idóneos para el procesado de datos temporales, como por ejemplo el procesado de videos, reconocimiento de voz o reconocimiento de escritura manual. 

Este tipo de conexiones puede darse a lo largo de las distintas capas neuronales y en distintas direcciones como podemos observar en la Ilustración 91. 

113 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 92: Ejemplo de red neuronal recurrente 

Dentro de las redes neuronales recurrentes podemos encontrar una clasificación atendiendo a la arquitectura interna del modelo y el tipo de problema para el cual son idóneas. 

#### **Redes neuronales simples** 

Las redes neuronales simples son el modelo de red neuronal recurrente mas sencillo y cuya arquitectura sirve como base para implementar redes recurrentes mas complejas. Este tipo de redes fueron presentadas por Jeffrey L. Elman en 1990 en su artículo “Finding Structure in time” [68] y están caracterizadas por ser el primer modelo de redes que presentaba retroalimentación entre las capas inmediatamente contiguas. Esto hace que las neuronas de este modelo de redes posean memoria de los eventos inmediatamente anteriores y estos afecten a las actualizaciones sucesivas de los pesos en cada una de las capas de la red. 



Ilustración 93: Ejemplo de red de Elman 

114 

**Módulo. Machine Learning y Deep Learning** 

#### **Redes LSTM (Long Short Term Memory)** 

Las redes neuronales de LSTM fueron descritas por primera vez por Hochreiter y Schmidhuber en 1997 [69], sin embargo, no ha sido hasta la actualidad que este tipo de redes neuronales no han crecido en popularidad gracias a las aplicaciones que presentan en la resolución de problemas que requieren trabajar con memoria a largo plazo. Este tipo de redes son capaces de trabajar con memoria a mas largo plazo ya que se caracterizan por incluir pasos en la red que permiten decidir que información es almacenada y cual es eliminada. Esto permite recordar a la célula que valor es importante y no únicamente la que ha sido aportada por el instante inmediatamente anterior. Las neuronas de este tipo de red contienen tres puertas que controlan el modo en el que la información fluye dentro o fuera de la unidad 

- Puerta de entrada: La puerta de entrada controla cuándo puede ingresar nueva información a la memoria. 

- Puerta del olvido: La puerta de olvido controla cuando se olvida una parte de la información existente, lo que permite a la celda recordar datos nuevos. 

- Puerta de salida: La puerta de salida controla cuando la información que está contenida en la celda se utiliza en la salida de la celda. 

La celda también contiene pesos, que controlan cada puerta. 



Ilustración 94: Ejemplo de red LSTM 

#### **Redes GRU** 

Las redes Gatod Recurrent Unit o redes GRU son una simplificación de las redes LSTM. Este tipo de redes fueron introducidas por Kyunghyun Cho et al. en 2014 y están compuestas por un tipo especial de neurona recurrente. Este modelo a diferencia del LSTM solo cuenta con dos puertas de control de la información almacenada dentro de la neurona: 

115 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- Puerta de actualización: Indica la cantidad de información que va a ser mantenida de las celdas anteriores 

- Puerta de reajuste: Define la entrada de nuevos datos y su incorporación a los contenidos anteriores de la celda. 

Este tipo de redes se consideran mas sencillas que las redes de Long Short Term Memory ya que contienen menos parámetros y carecen de puerta de salida. Esto permite que las redes sean entrenadas mucho mas rápido y sean mas eficientes en su ejecución. Ambas redes permiten conservar características importantes a través del proceso de memoria controlada por puertas, sin embargo la aplicación de cada una de estas redes va a depender del escenario especifico. 



Ilustración 95: Ejemplo de red GRU 

### **5.1.4. Redes Neuronales Convolucionales (CNN)** 

Las redes neuronales convolucionales son un tipo de redes profundas caracterizadas por su inspiración en la arquitectura que presentan las neuronas de la corteza visual primaria en un cerebro biológico. Este tipo de red esta especialmente indicada en aplicaciones de visión artificial, procesado de imágenes y modelos de clasificación y segmentación de archivos audiovisuales. Por ello la aparición de estos algoritmos ha supuesto un antes y un después en el campo de la visión artificial. La primera red de este tipo fue presentada por Yann LeCun en 1989 en un articulo que trataba el reconocimiento de letras manuscritas [71]. 

La arquitectura de estas redes convolucionales consta de múltiples capas ocultas que permiten realizar un procesado de elementos simples como líneas o curvas que se van especializando a medida que recorren las capas del modelo hasta poder identificar formas, siluetas… 

Dentro de las capas que podemos encontrar en un modelo podemos encontrar dos tipos: capas convolucionales y capas de reducción o pooling. Estas capas se encuentran alternadas hasta llegar a una capa de salida que se conoce como fully connected layer. 

116 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Un ejemplo de uso de este tipo de modelos es el procesado de una imagen para determinar su contenido. En la capa de entrada la imagen es dividida por pixels y cada uno de ellos es asignado a una neurona para su procesado. Si trabajamos con una imagen en blanco y negro solo necesitaremos una neurona para procesar cada pixel en la capa de entrada, sin embargo, si la imagen es a color, esta imagen se descompondrá en tres canales: rojo (R), verde (G) y azul (A) y cada una de estas capas se procesara de manera paralela hasta fusionarse en el estadio final del algoritmo. 

El proceso de convolución del algoritmo consiste en tomar un grupo de pixels de la capa de entrada y aplicar sobre el un kernel o filtro. Este filtro se aplica sobre la imagen para extraer las características y patrones mas importantes de la misma. El kernel recorre todas las neuronas de entrada (es decir la imagen completa) generando una nueva matriz que pasará a formar parte de las capas ocultas. 



Ilustración 96: Aplicación de convolución en una red CNN 

Previo a la aplicación del kernel el común realizar una operación conocida como Padding. Esta consiste en añadir pixeles de valor cero alrededor de la imagen a procesar. Esto permite que la convolución de la imagen procesada tenga en cuenta los datos representados en las esquinas de la imagen, ya que la aplicación del filtro de kernel pasa más por el centro de la imagen que por las esquinas. 

Sobre esta matriz de salida se aplica una función de activación que nos permite extraer características de la convolución del kernel. Normalmente la función de activación que se aplica es la función conocida como ReLu por sus siglas en inglés Rectifier Linear Unit, la cual nos permite extraer información de la imagen. 

117 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 97: Ejemplo de una red convolucional 

En una misma capa convolucional se emplean mútiples kernels para extraer características de la imagen. Esto provoca que las nuevas capas de convolución crezcan de manera exponencial, ya que cada resultado de multiplicación de kernel es almacenado en una nueva neurona. Por ello es frecuente que tras la capa de convolución se aplique una capa de reducción o pooling en la que se disminuye la cantidad de parámetros al quedarse con las características más comunes. Esta reducción de características se lleva a cabo utilizando medidas estadísticas y provoca que la red pierda precisión, sin embargo, esta mejor su compatibilidad. 

El modelo de redes convolucionales generalmente alterna capas de convolución y capas de pooling hasta llegar a un estadio final en el que la red convolucional es conectada a una red neuronal multicapa que se encarga de “aplanar” la útima capa de neuronas ocultas de red convolucional y convertirlas en la capa de salida. En esta última fase se aplica la función conocida como SoftMax. Esta función es una generalización de la regresión logística aplicada a múltiples dimensiones. Con ella podemos extraer las clases que tratamos de obtener de la imagen que estamos procesando. 

Una de las principales ventajas que presenta este tipo de redes en el procesado de las imágenes es que cada parte de la red es entrenada para realizar un tipo de tarea, lo cual reduce enormemente el tiempo necesario para realizar el procesado de una imagen. 

### **5.1.5. Deconvolutional network (DN)** 

Las redes desconvolucionales son redes neuronales convolucionales que se ejecutan en sentido inverso. Estas redes trabajan con modelos de ingeniería inversa, es decir construyen la imagen a partir de las distintas capas de la misma. Este tipo de redes son frecuentemente utilizadas para recuperar características que han podido ser eliminadas por una red convolucional recurrente. Estas características pueden ser perderse al mezclarse con otras características dentro de la red convolucional. Estas redes tienen su principal campo de aplicación dentro de la investigación científica y en ingeniería como método de apoyo en el desarrollo algorítmico. 

118 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 



Ilustración 98: Red deconvolucional 

### **5.1.6. Redes de creencias profundas (DBN)** 

Una red de creencias profundas o DBN por sus siglas en ingles (Deep Belief Network) es un tipo de red neuronal caracterizada por utilizar un modelo de aprendizaje no supervisado. Este tipo de redes están compuestas por múltiples capas de variables latentes y se caracterizan por realizar un entrenamiento capa por capa. El entrenamiento de estas capas neuronales es llevado a cabo por las máquinas de Boltzman. Estas máquinas fueron introducidas por Geoffrey Hinton en 2006 [72] y basan su funcionamiento en las leyes estadísticas de la probabilidad. En esta red las neuronas solo pueden tener dos estados, positivo o negativo (0 o 1). Toman su nombre del modelo de distribución estadística de Boltzmann y están compuestas por neuronas aleatorias completamente conectadas de manera simétrica que consta de una capa oculta y una capa visible.  Estas máquinas pueden utilizarse tanto en aprendizaje supervisado como en aprendizaje no supervisado y son capaces de resolver complejos problemas combinatorios. Sin embargo, estas máquinas requieren un tiempo de entrenamiento excesivamente largo como para que su uso pueda hacerse de manera extensivo. 



Ilustración 99: Máquina de Boltzmann 

119 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Para contrarrestar este efecto surgieron las Máquinas de Boltzmann Restringidas (RBM) las cuales son una simplificación de las Máquinas de Boltzmann originales mas fáciles de utilizar. Estas máquinas también cuentan con una capa oculta y una capa visible, sin embargo, no existe conectividad intracapa, es decir las neuronas de la capa oculta están conectadas con las de la capa visible y de manera viceversa sin embargo no están conectadas entre si. 



Ilustración 100: Máquina de Boltzmann Restringida 

Esta arquitectura es muy útil a la hora de entrenar modelos de aprendizaje no supervisados y pueden ser utilizados para tareas como reducción de dimensionalidad, extracción de características… 

Después de entrenar una RBM, los datos proporcionados como salida pueden ser utilizados como datos de entrenamiento para la siguiente RBM. En este método las capas de la red neuronal son apiladas formando una red de creencias profundas. 



Ilustración 101: Red de creencias profundas 

120 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

En las DBN, la capa de entrada representa las entradas sensoriales en bruto, y cada capa oculta aprende representaciones abstractas de esta entrada. La capa de salida, que se trata de manera algo diferente a las otras capas, implementa la clasificación de red. El aprendizaje se realiza en dos pasos: entrenamiento previo sin supervisión y ajuste fino supervisado. 

Este tipo de redes son frecuentemente utilizadas en reconocimiento de imágenes, secuencias de video, captura de datos en movimiento y reconocimiento de voz. 

### **5.1.7. Auto encoder (AE)** 

Los autoencoders son redes neuronales que tienen como objetivo generar unos datos de salida igual a los datos de entrada. Estos modelos se encargan de comprimir los datos de entrada transformándolos en un espacio de menor dimensionalidad y después reconstruyen los datos a partir de esta representación. Estos algoritmos están compuestos por tres componentes: 

- Encoder: Parte de la red encargada de comprimir los datos de entrada y transformarlos ene una representación latente 

- Code: Representación latente de los datos en un espacio de menores dimensiones al espacio de los datos de entrada 

- Decoder: Parte de la red neuronal encargada de descomprimir la representación latente de los datos 



Ilustración 102: Auto Encoder 

Este tipo de algoritmos se utilizan principalmente como reductores de dimensionalidad en los datos y eliminación de ruido. 

121 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

### **5.1.8. Red generativa antagónica (GAN)** 

Las redes generativas antagónicas son un modelo de redes neuronales diseñadas para el entrenamiento de modelos generativos. En el aprendizaje máquina podemos identificar dos tipos de modelos, modelos discriminativos y modelos generativos. Los modelos discriminativos se caracterizan por tratar de diferenciar los ejemplos de entrada entre diferentes clases. Un ejemplo de modelos discriminativos son los modelos de clasificación. Por su parte los modelos generativos son modelos que aprenden los patrones que existen en los datos y son capaces de generar datos similares a los que se utilizaron en el entrenamiento. Estos nuevos datos generados pueden utilizarse para realizar estimaciones de clasificación o para utilizar como datos de entrenamiento que se utilicen como datos de entrada para otros modelos. 

Las redes generativas antagónicas permiten generar nuevas imágenes similares a las que se han empleado como datos de entrenamiento.  La arquitectura de estas redes esta compuesta por dos redes “contrarias”, en las cuales una de ellas se encarga de generar las imágenes y la segunda se encarga de discriminar aquellas que no encajan con los datos de entrada. 

Este tipo de redes se han utilizado para la construcción de imágenes realistas de diseños industriales, ropa, complementos, incluso escenas de videojuegos, esto genera una importante área de aplicación en el campo de la publicidad y el marketing, sin embargo, estas redes tienen otras muchas aplicaciones. Su capacidad para detectar anomalías les permite detectar imágenes falsas lo que genera un nuevo área de actuación en el mundo de la seguridad. También se están empleando este tipo de redes dentro del sector salud para detectar estructuras anómalas en imágenes médicas que pueden indicar la presencia de algún tipo de enfermedad. 



Ilustración 103: Red generativa antagónica 

122 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

Un ejemplo bastante conocido de este tipo de redes neuronales es el proyecto llevado a cabo por Philip Wang. Este ingeniero de software, trabajador de Uber, utilizo el software StykeGAN publicado como open source por Nvidia en diciembre de 2018 para crear un modelo de red generativa antagónica capaz de generar caras de personas aparentemente reales. Este proyecto comenzó como un método para llamar la atención sobre las posibilidades de la inteligencia artificial pero se ha convertido en un recurso para las pruebas de detección de perfiles falsos y fraude en redes sociales. En este modelo la primera red construye la imagen y la segunda trata de discernir si esta es real o ha sido creada de manera artificial. Este proceso se repite hasta que la primera red es capaz de engañar a la segunda y se presenta esta imagen como salida. El proyecto es accesible desde la web <u>https:// thispersondoesnotexist.com donde se puede ver el resultado de las redes. Asociado a este</u> proyecto se ha desarrollado con la misma tecnología redes capaces de generar imágenes de caballos, estructuras químicas, gatos e incluso obras de arte. 

### **5.1.9. Deep Residual Network (ResNet)** 

Las Deep residual Network son un modelo de redes neuronales especialmente diseñado para el procesado de imágenes. Este modelo fue presentado en 2015 por Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun en un articulo titulado ‘Deep Residual Learning for Image Recognition’ [73]. Este modelo tiene como objetivo abordar el problema que presentan las redes convolucionales cuando se agregan demasiadas capas ocultas al modelo y estas generan degradación del resultado tanto en datos de entrenamiento como en datos de test. Esta degradación no es producida por un sobreentrenamiento del modelo si no por funciones de optimización o afectación en la minimización de los gradientes (tras muchas capas estos pueden crecer descontroladamente o desaparecer por completo). Para ello este tipo de redes utiliza bloques residuales para mejorar el rendimiento del modelo. Dentro de estos bloques se produce lo que se conoce como “salto de conexiones”. Estos saltos de conexiones permiten a la red evitar los cambios bruscos de gradiente, facilitando un nuevo camino por el que continuar el modelo. Además, incluyen en el modelo un proceso por cual las capas superiores no pueden tener un rendimiento menor al de las capas inferiores. 



Ilustración 104: Deep Residual Network 

123 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

### **5.2. Limitaciones del Deep Learning** 

Las limitaciones clásics asociadas al Deep Learning venían definidas por los requirimientos técnicos necesarios para ejecutar este tipo de modelos. Por un lado, la potencia computacional no era la suficiente para poder llevar a cabo los entrenamientos y por otro la disponibilidad de grandes bases de datos era limitada. 

Actualmente estas limitaciones han sido resueltas por el avance de la tecnología tanto a nivel de disponibilidad de nuevos procesadores capaces de manejar estas redes neuronales como de capacidad de almacenamiento para gestionar tales volúmenes de datos. 

Sin emabargo, estas no son las únicas limitaciones a las que debemos hacer frente a la hora de implementar un modelo de Deep Learning. 

Los dos principales problemas que encontramos en la actualidad derivados del desarrollo de modelos de Deep Learning son el sobre ajuste y las cajas negras. 

Igual que muchos otros modelos de aprendizaje máquina el Deep Learning es propenso al sobreentrenamiento. Para evitar este problema existen múltiples técnicas que nos permiten crear un modelo generalizado que sea flexible ya adecue las activaciones neuronales a las nuevas entradas de datos en lugar de memorizar las posibles salidas y no ajustarlas a los datos. Algunas de estas técnicas pasar por el preprocesado de los datos para eliminar cantidades excesivas de dimensiones, ajuste de parámetros dentro del modelo o limitaciones en la cantidad de iteraciones posibles. 

La segunda potencial limitación que nos encontramos en este tipo de modelos es lo conocido como “caja negra”. Cuando construimos un modelo de Deep learning dependiendo de la arquitectura que utilicemos podemos desconocer como están llegando las neuronas a los diferentes resultados, esto convierte al modelo en gran medida en una caja negra cuyo funcionamiento desconocemos. Para utilizar inteligencia artificial en determinadas aplicaciones podemos encontrarnos con regulaciones legales que exijan la interpretabilidad del modelo debido a la sensibilidad del proceso para el cual se este utilizando. 

124 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

El desconocimiento del proceso por el cual una red neuronal llega a una conclusión hace que estas puedan ser vulnerables a ataques y no seamos conscientes de la repercusión de ello. Un buen ejemplo de alteración premeditada de un algoritmo de Deep learnign son los sistemas de recomendación de las redes sociales. El algoritmo esta preparado para mostrarte un contenido publicitario en función de tus interacciones dentro de la red social. En ocasiones para que un articulo se recomiende a un público mas amplio se generan interacciones falsas desde cuentas con un perfil digital similar al del grupo de perfiles al que se trata de alcanzar. Esto puede ocurrir también en el sentido opuesto haciendo que un producto o perfil determinado nunca se recomiende. Este problema cuando lo vemos desde el punto de las redes sociales puede resultarnos superficial (a no ser que nos dediquemos al product placement), pero este tipo de ataques son extrapolables a sistemas de aprendizaje profundo empleados en sistemas de seguridad, detección de fraudes y sistemas sanitarios. Por este motivo existen ejemplos de compañías y gobiernos que no permiten el uso de Deep learning para determinadas tareas. 

125 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

## **Bibliografía** 

- [1] <u>https://250.dartmouth.edu/highlights/artificial-intelligence-ai-coined-dartmouth</u> 

- [2] <u>https://www.wolframscience.com/prizes/tm23/images/Turing.pdf</u> 

- [3] <u>https://www.csee.umbc.edu/courses/471/papers/turing.pdf</u> 

- [4] Supervised and Unsupervised Learning for Data Science, <u>https://doi. org/10.1007/978-3-030-22475-2, Michael W. Berry Azlinah Mohamed Bee Wah Yap</u> 

- [5] van Otterlo M., Wiering M. (2012) Reinforcement Learning and Markov Decision Processes. In: Wiering M., van Otterlo M. (eds) Reinforcement Learning. Adaptation, Learning, and Optimization, vol 12. Springer, Berlin, Heidelberg. <u>https://doi. org/10.1007/978-3-642-27645-3_1</u> 

- [6] LeCun, Y., Bengio, Y. & Hinton, G. Deep learning. Nature 521, 436–444 (2015). <u>https://doi.org/10.1038/nature14539</u> 

- [7] Roman, V. (2019, Marzo 27). Aprendizaje Supervisado: Introducción a la Clasificación y Principales Algoritmos. Obtenido de Medium: <u>https://medium.com/datosy-ciencia/aprendizaje-supervisado-introducci%C3%B3n-a-la-clasificaci%C3%B3ny-principales-algoritmos-dadee99c9407</u> 

- [8] Wilson, A. (2019, Septiembre 29). A Brief Introduction to Supervised Learning. Obtenido de towards data science: <u>https://towardsdatascience.com/a-brief-introduction-to-supervised-learning-54a3e3932590</u> 

- [9]https://www.cienciadedatos.net/documentos/27_regresion_logistica_ <u>simple_y_multiple#Regresión_log%C3%ADstica_múltiple</u> 

- [10] <u>https://www.iartificial.net/regresion-logistica-para-clasificacion/</u> 

- [11] <u>https://scikit-learn.org/stable/</u> 

- [12] <u>https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html</u> 

- [13] <u>https://protecciondatos-lopd.com/empresas/overfitting/</u> 

- [14] <u>https://www.freecodecamp.org/espanol/news/como-funcionan-los-clasificadores-naive-bayes-con-ejemplos-de-codigo-de-python/</u> 

126 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- [15] Swinburne, Richard (2002). Introduction to Bayes’s Theorem. In _Bayes’s Theorem_. Oxford University Press. 

- [16] <u>https://commons.wikimedia.org/wiki/File:Map1NNReducedDataSet.png</u> 

- [17] Guo G., Wang H., Bell D., Bi Y., Greer K. (2003) KNN Model-Based Approach in Classification. In: Meersman R., Tari Z., Schmidt D.C. (eds) On The Move to Meaningful Internet Systems 2003: CoopIS, DOA, and ODBASE. OTM 2003. Lecture Notes in Computer Science, vol 2888. Springer, Berlin, Heidelberg. <u>https://doi. org/10.1007/978-3-540-39964-3_62</u> 

- [18] S. Cost, S. Salzberg (1993). A weighted nearest neighbour algorithm for learning with symbolic features, Machine Learning 10(1), 57-78 

- [19] <u>http://www.sc.ehu.es/ccwbayes/docencia/mmcc/docs/t9knn.pdf</u> 

- [20] <u>https://medium.com/@avulurivenkatasaireddy/k-nearest-neighbors-and-implementation-on-iris-data-set-f5817dd33711</u> 

- [21] Boser, B.E., Guyon, I.M. and Vapnik, V.N. (1992) A Training Algorithm for Optimal Margin Classifiers. Proceedings of the 5th Annual Workshop on Computational Learning Theory (COLT’92), Pittsburgh, 27-29 July 1992, 144-152. 

- [22] Vladimir Vapnik, The Nature of Statistical Learning Theory, DOI https://doi. <u>org/10.1007/978-1-4757-3264-1,  Series Title Statistics for Engineering and Informa-</u> tion Science 

- [23] <u>https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47</u> 

- [24] Quinlan, J.R. Induction of decision trees. Mach Learn 1, 81–106 (1986). https:// <u>doi.org/10.1007/BF00116251</u> 

- [25] Rokach L., Maimon O. (2005) Decision Trees. In: Maimon O., Rokach L. (eds) Data Mining and Knowledge Discovery Handbook. Springer, Boston, MA. https:// <u>doi.org/10.1007/0-387-25465-X_9</u> 

- [26] Applied Linear Regression, Sandford Weisberg, University of Minessota, School of Statistics, 2005 

- [27] Montgomery, D. C., Peck, E. A., & Vining, G. G. (2021). Introduction to linear regression analysis. John Wiley & Sons. 

- [28] Regularización, Ridge y LASSO Modelo Lineal María Eugenia Szretter Noste Instituto de Cáculo FCEyN, UBA, <u>http://cms.dm.uba.ar/academico/ materias/1ercuat2019/modelo_lineal/ridgeclase2.pdf</u> 

127 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- [29] Regularization and variable selection via the elastic net, Hui Zou, Trevor Hastie, 09 March 2005, <u>https://doi.org/10.1111/j.1467-9868.2005.00503.x</u> 

- [30] <u>https://bookdown.org/max/FES/greedy-stepwise-selection.html</u> 

- [31] S. Na, L. Xumin and G. Yong, “Research on k-means Clustering Algorithm: An Improved k-means Clustering Algorithm,” 2010 Third International Symposium on Intelligent Information Technology and Security Informatics, 2010, pp. 63-67, doi: 10.1109/IITSI.2010.74. 

- [32] Jin X., Han J. (2011) K-Means Clustering. In: Sammut C., Webb G.I. (eds) Encyclopedia of Machine Learning. Springer, Boston, MA. <u>https://doi.org/10.1007/9780-387-30164-8_425</u> 

- [33] <u>http://worldcomp-proceedings.com/proc/p2015/CSC2663.pdf</u> 

- [34] <u>http://www.econ.upf.edu/~michael/stanford/maeb7.pdf</u> 

- [35] Saraçli, S., Doğan, N. & Doğan, İ. Comparison of hierarchical cluster analysis methods by cophenetic correlation. J Inequal Appl 2013, 203 (2013). <u>https://doi. org/10.1186/1029-242X-2013-203</u> 

- [36] <u>https://uc-r.github.io/hc_clustering</u> 

- [37] Aprendizaje automático: Una Perspectiva Probabilística, Kevin Patrick Murphy. MIT Press, 2012. 

- [38] A high-resolution 7-Tesla fMRI dataset from complex natural stimulation with an audio movie, <u>https://www.openfmri.org/dataset/ds000113/</u> This data was obtained from the OpenfMRI database. 

- [39] Métodos de reducción de dimensionalidad: Análisis comparativo de los métodos APC, ACPP y ACPK 

- [40]https://www.fuenterrebollo.com/Economicas/ECONOMETRIA/MULTIVA- <u>RIANTE/FACTORIAL/analisis-factorial.pdf</u> 

- [41] Methods and Applications of Longitudinal Data Analysis, 2016, Pages 205-242 

- [42]http://www.music.mcgill.ca/~ich/classes/mumt611_07/classifiers/lda_theory. <u>pdf</u> 

- [43] Scientia et Technica Año XII, No 32, Diciembre de 2006. UTP. ISSN 0122-1701 181 REDUCCIÓN DE DIMENSIONES PARA CLASIFICACIÓN DE DATOS MULTIDIMENSIONALES USANDO MEDIDAS DE INFORMACIÓN 

128 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- [44] <u>https://medium.com/@nicolasarrioja/13-técnicas-de-reducción-de-dimensionalidad-b33b2340a060</u> 

- • [45]https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2n- <u>dEd.pdf</u> 

- • [46] <u>https://aws.amazon.com/es/deepracer/.</u> • [47] <u>https://deepmind.com/blog/article/safety-first-ai-autonomous-data-centrecooling-and-industrial-control</u> 

- • [48] <u>https://www.ibm.com/blogs/digital-transformation/in-en/blog/trade-finance-workflow-automation-using-ai/</u> 

- • [49] <u>https://gym.openai.com</u> • [50] <u>http://www.incompleteideas.net/book/RLbook2018trimmed.pdf</u> • [51] <u>https://ieeexplore.ieee.org/document/6313077</u> • [52]https://github.com/openai/gym/blob/master/gym/envs/classic_control/cart- <u>pole.py</u> 

- • [53]https://home.csulb.edu/~cwallis/382/readings/482/mccolloch.logical.calculus. <u>ideas.1943.pdf</u> 

- [54]https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.335.3398&rep=rep1& <u>type=pdf</u> 

- • [55] https://www.statista.com/statistics/871513/worldwide-data-created/ 

- [56] Ramón y Cajal, S. (1906). Morfología de la célula nerviosa. _Archivos de Pedagogía y Ciencias Afines, 1_ . 

- [57] The Integrative Action of the Nervous System, Charles Sherrington 

- [58] Hassoun, Mohamad H. _Fundamentals of Artificial Neural Networks_ . Cambridge, Massachusetts;: The Mit press, 1995. Print. 

- [59] Manjarrez, Lino. (2014). Relaciones Neuronales Para Determinar la Atenuación del Valor de la Aceleración Máxima en Superficie de Sitios en Roca Para Zonas de Subducción. 

- [60] BONETTI, C. (2013). “Estimación de la variación de la resistencia al corte en suelos marinos usando Redes Neuronales”. Tesis de Maestría, Facultad de Ingeniería, UNAM. 

129 

**Centro Europeo de Postgrado                                                             Módulo. Machine Learning y Deep Learning** 

- [61] <u>http://www.sc.ehu.es/ccwbayes/docencia/mmcc/docs/t8neuronales.pdf</u> 

- [62] Rosenblatt, F. (1958). The perceptron: A probabilistic model for information storage and organization in the brain. Psychological Review, 65(6), 386–408. <u>https:// doi.org/10.1037/h0042519</u> 

- [63] Minsky, M., & Papert, S. 1969. Perceptron: an introduction to computational geometry. The MIT Press, Cambridge, MA. 

- [64] Rumelhart, D. E., Hinton, G. E., & Williams, R. J 1986. Parallel Distributed Processing: Explorations in the Microstructure of Cognition. The MIT Press, Cambridge, MA. 

- [65] <u>https://stanford.edu/~jlmcc/jlmderapa.pdf</u> 

- [66] Rumelhart, D., Hinton, G. & Williams, R. Learning representations by backpropagating errors. Nature323, 533–536 (1986). <u>https://doi.org/10.1038/323533a0</u> 

- [67] <u>https://www.asimovinstitute.org/neural-network-zoo/</u> 

- [68] Elman, J. L. (1990). Finding structure in time. Cognitive science, 14(2), 179-211. 

- [69] Sepp Hochreiter, Jürgen Schmidhuber; Long Short-Term Memory. Neural Comput 1997; 9 (8): 1735–1780. doi: <u>https://doi.org/10.1162/neco.1997.9.8.1735</u> 

- [70] Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation,Kyunghyun Cho, Bart van Merrienboer, Caglar Gulcehre, Dzmitry Bahdanau, Fethi Bougares, Holger Schwenk, Yoshua Bengio 

- [71] <u>http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf</u> 

- [72] <u>https://www.cs.toronto.edu/~fritz/absps/ncfast.pdf</u> 

- [73] He, K., Zhang, X., Ren, S., & Sun, J. (2016). Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 770-778). 

130 







**CEUPE** Centro Europeo de Postgrado 

**Web** 

www.ceupe.com 

**E-mail** info@ceupe.com 

