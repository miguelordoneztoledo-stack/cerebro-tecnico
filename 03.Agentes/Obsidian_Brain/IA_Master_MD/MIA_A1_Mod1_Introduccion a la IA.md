---
tags:
  - master_ia
  - teoria
source: MIA_A1_Mod1_Introduccion a la IA.pdf
---

# **Módulo Introducció a la Inteligencia Artificial** 



# **Módulo Introducción a la Inteligencia Artificial** 

|**1. ¿QUÉ ES LA IA? CONCEPTOS BÁSICOS, OBJETIVOS Y TIPOLOGÍA ...................03**<br>|
|---|
|1.1. DEFINICIÓN DE LA INTELIGENCIA ARTIFICIAL. EL TEST DE TURING ..................03|
|1.2. TIPOS DE INTELIGENCIA ARTIFICIAL. CLASIFICACIONES ..................................08<br>|
|1.2.1. IA GENÉRICA, IA ESPECÍFICA Y “SÚPER” IA ............................................08|
|1.2.2. SISTEMAS HUMANOS Y RACIONALES .....................................................14<br>|
|1.2. LA CLASIFICACIÓN DE LA IA DE HINTZE .........................................................19<br>|
|**2. CRONOLOGÍA Y LÍMITES DE LA INTELIGENCIA ARTIFICIAL ..............................26**<br>|
|2.1. CRONOLOGÍA DE LOS ALGORITMOS Y LAS COMPUTADORAS .......................27<br>|
|2.2. CRONOLOGÍA DE LA INTELIGENCIA ARTIFICIAL ..............................................31<br>|
|ETAPA 0. LOS ANCESTROS: MATEMÁTICAS Y NEUROCIENCIA. .........................32<br>|
|ETAPA 1. PROPUESTA TEÓRICA Y PRIMEROS PASOS 1940 – 1959 .....................35|
|ETAPA 2. EL PRIMER INVIERNO DE LA IA 1960 – 1979 .......................................41<br>|
|ETAPA 3. LOS PRIMEROS ÉXITOS, VUELTA DE LA FINANCIACIÓN 1980 – 1987 ..48|
|ETAPA 4. EL SEGUNDO INVIERNO DE LA IA 1988 – 1993 ..................................56<br>|
|ETAPA 5. LA GRAN EXPANSIÓN 1994 – 2011 ....................................................60|
|ETAPA 6. LA ERA DEL BIG DATA Y EL DEEP LEARNING: DESDE 2012 .................73<br>|
|**3. MÉTODOS Y TECNOLOGÍAS FUNDACIONALES ...............................................119**|
|**4. APLICACIONES E IMPACTO EN EL MUNDO REAL ............................................131**<br>|
|**BIBLIOGRAFÍA ........................................................................................................140**|



**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

## **1. ¿Qué es la IA? Conceptos básicos, objetivos y tipología** 

La IA es _“la ciencia e ingeniería de crear máquinas inteligentes, concretamente programas de ordenador inteligentes. Está relacionada con el objetivo de emplear ordenadores para comprender la inteligencia humana, pero la IA no está necesariamente limitada a métodos observables biológicamente.”_ 

John McCarthy 

### **1.1. Definición de la Inteligencia Artificial. El test de Turing** 

El primer paso en el camino hacia la capacidad de diseñar, implantar y gestionar proyectos basados en Inteligencia Artificial es ser capaz de responder la pregunta ¿qué es la Inteligencia Artificial? Conocer la respuesta a esta cuestión nos permitirá diferenciar con certeza qué potenciales proyectos se engloban en esta disciplina, así como las limitaciones que podemos encontrar tanto de carácter teórico como práctico a la hora de implantar esta tecnología. 

Esta no es una pregunta con una única respuesta correcta, ya que existen numerosas definiciones de este concepto según la fuente a la que se acuda. Como una primera aproximación, se pueden consultar varias de las definiciones ofrecidas por distintos diccionarios e instituciones tanto de carácter general como técnico para comprender los rasgos generales compartidos entre todas ellas y comenzar a despejar la incógnita que nos hemos planteado. 

Como representante de casi 450 millones de personas que viven en la Unión Europea, el Parlamento Europeo ha tratado de definir la Inteligencia Artificial a efectos de su regulación y limitación legal de la siguiente manera: _“Es la habilidad de una máquina de presentar las mismas capacidades que los seres humanos, como el razonamiento, el aprendizaje, la creatividad y la capacidad de planear.”_ 

A través de esta definición, el máximo órgano legislativo de la Unión Europea considera la Inteligencia Artificial como una habilidad propia de las máquinas, que parece que permitiera a estas imitar al ser humano en términos de inteligencia. 

03 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Si se atendiera únicamente a esta definición podría llegarse a pensar que las máquinas adquieren esta habilidad por sí mismas y que su límite se encuentra allá donde llegue la inteligencia del ser humano, ya que el principal objetivo es comportarse a imagen y semejanza del mismo. Esta definición es quizá limitada en cuanto _a qué_ es la Inteligencia Artificial pero también en cuanto _a qué_ hace, ya que olvida dos conceptos esenciales de la IA. 

Por un lado, la IA no surge en las máquinas por generación espontánea, ni tampoco adquieren la habilidad de razonar en base a la práctica. La realidad, aunque obvia, es que es precisa la actividad de un desarrollador o equipo de desarrolladores para que esta máquina adquiera dichas habilidades pseudohumanas a través de un algoritmo. Esto implica, por tanto, que estos serán los responsables últimos de lo que la máquina haga con dichas habilidades. 

Y, por otro lado, como veremos en otras propuestas de definición, hay expertos que afirman que podría considerarse un error sostener que la IA está basada en adquirir una inteligencia humana, ya que esto infravalora con creces el potencial de esta tecnología. 

Esta afirmación no es solo teoría, ya que en ciertos ámbitos la Inteligencia Artificial ya se ha conseguido a día de hoy de superar las capacidades de la inteligencia de un individuo humano con creces. Por poner un ejemplo concreto, un grupo de investigación liderado por la doctora Raquel Pérez-López en el Vall d’Hebron Institut of Oncology (VHIO) en Cataluña, España, presentó en enero de 2021 un sistema de IA que predice qué pacientes con cánceres avanzados responderán mejor a inmunoterapia con mayor acierto que ningún oncólogo en el mundo, gracias a la gran capacidad de procesamiento de datos y de predicción precisa de los modelos empleados en este estudio. 

Sin perjuicio de lo anterior, es importante recordar que el Parlamento Europeo es un órgano legislativo de carácter genérico y no técnico, así como que la definición de IA que ofrecen tiene como propósito guiar la redacción de directrices de uso de la misma en el territorio de la Unión Europea. A tales efectos legislativos, esta definición puede ser perfectamente válida, pero nos permite explorar las limitaciones de ciertas definiciones oficiales de la tecnología estudiada a lo largo de este Máster. 

Más allá de órganos oficiales, se puede acceder a dos de las más reconocidas publicaciones de definiciones del mundo para conocer la aproximación a la IA que ofrecen. Estas son el diccionario de Oxford y la Enciclopedia Británica. 

El diccionario Oxford por su parte sostiene que la Inteligencia Artificial se trata de “ _la teoría y desarrollo de sistemas de computación capaces de realizar tareas que habitualmente requieren inteligencia humana tales como la percepción visual, el reconocimiento del lenguaje, la toma de decisiones y la traducción entre idiomas.”_ 

La Enciclopedia Británica trata de sintetizar la amplia realidad de esta tecnología en la siguiente definición: _“La Inteligencia Artificial (IA) es la capacidad de un ordenador o de un robot controlado por ordenador de realizar tareas comúnmente asociadas con seres inteligentes.”_ 

04 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Ambas definiciones arrojan luz sobre nuestra incógnita gracias a una definición más amplia y certera de la Inteligencia Artificial. La definición del diccionario de Oxford incorpora un concepto interesante: afirma que la IA es, lejos de una habilidad adquirida por las máquinas, **un campo tanto teórico como práctico** relativo al desarrollo de programas informáticos. En este caso ya no se trata de una “habilidad de una máquina” sino del trabajo de un humano que teoriza modelos para posteriormente desarrollarlos en la práctica en forma de algoritmos. Con este añadido se puede afirmar que es un ser humano el creador y responsable de la existencia y despliegue de todo algoritmo de IA, como es en efecto. De hecho, la definición parece asumir que la IA es, ante todo, una **disciplina científica.** Sin embargo, las capacidades a las que puede optar el resultado de esta investigación científica siguen - según esta definición - limitadas a aquellas de los humanos, entre las que se ofrecen una serie de ejemplos. 

La Enciclopedia Británica aporta en su caso una visión novedosa del potencial alcance de la IA. Abandona frente a las definiciones previas el concepto de inteligencia humana como objetivo a alcanzar, para sustituirlo por aquello que son capaces de ejecutar los _“seres inteligentes”_ . Este pequeño matiz supone, sin embargo, una gran diferencia frente a limitar la IA a las capacidades de los seres humanos, como veremos más adelante, ya que estos denominados seres inteligentes no tienen por qué ser humanos, ni siquiera biológicos. Sin embargo, la _Britanica_ insiste en el aspecto de la “capacidad” asociada a un ser artificial, sin hacer referencia a la IA como una disciplina o campo científico. 

Este tipo de disparidades entre definiciones es comprensible debido a lo reciente que es el campo de la Inteligencia Artificial incluso para los profesionales más técnicos. Es por ello que, por el momento, no hay una definición cerrada y acordada por todas las partes, a pesar de que lleva habiendo intentos de hacerlo desde tan pronto como la década de os cincuenta. Hasta ahora hemos podido comprobar como tanto legisladores como lingüistas tratan de proponer las mejores aproximaciones posibles, con más o menos acierto según la dimensión que sea analizada. 

Otra posibilidad para acercarse a una definición consensuada de la Inteligencia Artificial que tenga en cuenta todas sus aristas es acercarse a la proporcionada por los científicos y profesionales de esta disciplina, más allá de instituciones y enciclopedias. 

Una de las definiciones más empleadas en el mundo investigador es la de John McCarthy, prestigioso científico que introdujo el término de Inteligencia Artificial en 1956. Como veremos en la Unidad 2, la IA ha evolucionado vertiginosamente desde su primera concepción, por lo que no es esta definición la que será analizada, aunque veremos que supuso un hito fundacional en el que profundizaremos. La definición más empleada en el sector actualmente es la que en 2004 el mismo McCarthy propuso en su artículo _“What is Artificial Intelligence?”_ . En él, proponía definir la IA como _“la ciencia e ingeniería de crear máquinas inteligentes, concretamente programas de ordenador inteligentes. Está relacionada con el objetivo de emplear ordenadores para comprender la inteligencia humana, pero la IA no está necesariamente limitada a métodos observables biológicamente.”_ 

05 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Es en esta definición en la que se pueden encontrar más aspectos acordados en la actualidad dentro de la comunidad científica, a pesar de las distintas visiones que aún perduran hoy. Tratando de cerrar posibles debates, McCarthy considera la IA como una **ciencia e ingeniería** por derecho propios. No son, si quiera, una rama de la ingeniería informática (o _computer science_ en inglés) ni de las matemáticas, sino que tiene entidad por sí misma. Por otro lado, menciona que la IA no es, ni más ni menos, que un **programa informático** . Líneas de código fuente compiladas que son ejecutadas en una unidad de procesamiento y que ejecutan instrucciones previamente definidas por un desarrollador humano. Al menos, hasta este momento, esta afirmación sigue siendo cierta más de quince años después. 

Por último, trata de aclarar que la IA no trata – o no debería de tratar – de imitar la inteligencia humana, sino de comprenderla y trabajar con ella. Es decir, se trata de obtener sistemas inteligentes, tal y como mencionaba la Enciclopedia Británica, sean estos similares a aquellos que suceden en la naturaleza o no. 

Las redes neuronales, por ejemplo, están inspiradas en la estructura de nuestro cerebro humano, y son grandes aliadas a la hora de procesar información lingüística y visual como resumir un artículo o diferenciar nódulos benignos y malignos en una tomografía computerizada. Sin embargo, si queremos agrupar los tipos de usuarios de una plataforma VoD ( _Video on Demand_ ) emplearemos algoritmos de _clustering_ como _K-Means_ o _Mean-Shift_ que en nada se parecerán a la inteligencia de ningún ser vivo conocido, pero efectuarán su trabajo con una precisión espectacular. 

El propio McCarthy se pregunta si es posible definir una inteligencia no humana o que no dependa de los seres humanos para definirla. Concluye que hasta el momento no somos capaces de definir qué es un sistema computacional inteligente sin mencionar la inteligencia humana. Esto es debido a que la inteligencia implica mecanismos complejos que no han sido completamente definidos y comprendidos por la ciencia, por lo que lo más cercano a una definición general de inteligencia que tenemos disponible actualmente implica usar al humano como baremo. 

Esta incertidumbre hace más compleja si cabe la pregunta ¿qué es un sistema inteligente? 

En uno de los primeros intentos de responder esta pregunta Alan Turing, nacido en 1912 en Londres, Reino Unido, y considerado el padre de la informática actual, planteó un test para resolver la pregunta que planteó en su ensayo titulado _“Computing machinery and intelligence”_ : ¿pueden las máquinas pensar? 

Este test se basa en la capacidad de mantener una conversación solvente en lenguaje natural. El experimento es en definitiva una conversación entre un ser humano y un programa que se encuentran en habitaciones separadas. El ordenador está diseñado para ser capaz de mantener un diálogo en el que el humano no sea capaz de detectar si su interlocutor es humano o sintético. En un tiempo de cinco minutos, la persona que evalúa el test tiene que no percibir la diferencia entre humano y software al menos durante un 30% del tiempo. Si esto sucede, la máquina habrá superado el test de Turing y será considerada inteligente. 

06 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Como se puede observar, el baremo es de nuevo la inteligencia humana, ya que la máquina sencillamente trata de imitar al humano, en un concepto denominado “El juego de la imitación”. Ya se ha mostrado que las definiciones más completas de IA huyen de esta comparación estricta con el ser humano, pero no son capaces de definir ningún tipo de inteligencia no biológica con precisión. Esto es debido a que, a día de hoy, no conocemos ninguna inteligencia con capacidades superiores a la humana y esto implica que se trate de definir algo inexistente, lo cual complica bastante el trabajo. 

En la siguiente sección veremos cómo distintos expertos en el campo de la Inteligencia Artificial han tratado de definir y delimitar inteligencias que llegan a tener la misma capacidad de razonamiento que los seres humanos. Incluso aprenderemos que algunos de ellos se han propuesto definir seres más inteligentes que nosotros, aunque esto implique entrar en terrenos de la teorización sin posibilidad de constraste a día de hoy. No obstante, todos estos tipos de inteligencia tanto inferiores, iguales o superiores a la del ser humano, pueden encajar en la definición de IA que emplearemos basada en la que propuso McCarthy en el año 2004. De esta forma tendremos un marco común a partir del cual ir desentrañando esta disciplina. 

En sucesivas secciones veremos otras propuestas de experimentos para analizar la inteligencia de una máquina, pero como corolario a este objetivo de definir la Inteligencia Artificial, podemos observar que, en definitiva, todas estas definiciones ofrecen una serie de elementos comunes consolidados que pueden ayudar a entender qué es y qué hace la IA. En la siguiente tabla se reúnen los aspectos comunes y aceptados por la comunidad científica que pueden ayudar a comprender qué es la Inteligencia Artificial. 

#### **_La Inteligencia Artificial, definición:_** 

- **_Campo científico y de la ingeniería_** _con una base_ **_teórica_** _y aplicación_ **_práctica_** 

- _Basado en diseño y desarrollo de algoritmos en forma de programas informáticos_ 

- _Trata de resolver_ **_problemas complejos_** _habitualmente asociados a_ **_seres inteligentes_** _como problemas visuales, lingüísticos, creativos y de toma de decisiones._ 

- _La inteligencia puede ser similar a la biológica/humana o distar de esta enormemente siempre que se cumpla el objetivo_ 

07 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

### **1.2. Tipos de Inteligencia Artificial. Clasificaciones** 

A diferencia de las definiciones, las diversas clasificaciones en las que se puede dividir la IA no son excluyentes entre ellas, y cuentan con un amplio consenso al considerarse como válidas más de una de ellas. Cada una de las clasificaciones que van a proponerse consideran diversas dimensiones de la IA para realizar su división, por lo que será indispensable comprender la dimensión que se emplea en cada caso para posteriormente marcar una frontera que permita clasificar la IA en diversos subtipos. 

### **1.2.1. IA genérica, IA específica y “súper” IA** 

En la actualidad los expertos en el campo de la IA hacen referencia de forma habitual a tres tipos de inteligencia en función de las capacidades que muestre: la IA específica, la IA general y la “súper” IA. Esta clasificación fue inicialmente propuesta por John Searle, un filósofo estadounidense en 1980, en su artículo “Minds, Brains, and Programs” publicado en la revista Behavioral and Brain Sciences. 

Para ser capaz de diferenciar los distintos tipos de IA, Searle propuso un experimento mental denominado **la habitación china.** 

Este experimento mental parte de la definición del pensamiento racional y la comprensión en contraste con las capacidades de un sistema computacional. 

Searle propone que “la computación está definida de forma puramente formal o sintáctica. Por el contrario, la mente tiene contenido mental y semántico y no podemos pasar de la sintaxis a la semántica sencillamente conociendo las operaciones sintácticas y nada más.” en palabras más claras sostiene que “Un sistema como un humano no llegaría a comprender el chino sencillamente siguiendo los pasos de un algoritmo que ha aprendido a simular el comportamiento de un hablante de chino”. 

Para ilustrar esta compleja afirmación se basa en el siguiente experimento mental. 

Una persona que no habla chino está sentada en una habitación cerrada. En la habitación hay un libro que contiene al completo el algoritmo empleado por un ordenador para hablar chino. Es decir, contiene todas las instrucciones por las que pasaría una máquina para procesar una frase en chino y generar una frase de vuelta de manera que el resultado fuera una imitación perfecta de un hablante nativo de chino. 

Otra persona, que habla chino, le pasa notas escritas en chino al sujeto inicial por debajo de la puerta. Con la ayuda del libro y siguiendo las instrucciones de forma precisa, la persona dentro de la habitación es capaz de procesar los mensajes y generar respuestas adecuadas para el hablante chino, sin que este pueda determinar si las respuestas que recibe han sido generadas por un nativo en chino o por un completo ajeno a su idioma. 

08 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

A pesar de haber sido capaz de procesar el mensaje y responderlo, Searle sostiene que la persona sentada en la habitación no comprende chino. Ha sido capaz de realizar una simulación de comprensión de chino mediante un conjunto de instrucciones, pero no ha comprendido ni un solo carácter de los que ha leído o escrito, ni las ideas que recibía y emitía. 

Con este ejemplo, Searle trata de resaltar el significado de “comprender” y “pensar”. Una máquina que alcanza la excelencia en responder a frases en chino no comprenderá chino, ni tendrá consciencia ni intencionalidad en sus respuestas. Sencillamente seguirá instrucciones, por perfectas que estas sean. 

En contraposición con el test de Turing, la habitación china trata de resaltar que el “juego de la imitación” no es una muestra de inteligencia, sino de una programación certera y experta. La inteligencia según Searle no se mide a través de la capacidad de imitar las capacidades humanas, sino de la consciencia y comprensión de las tareas que se están llevando a cabo, tal y como procede la mente humana. 

Tanto este experimento como el test de Turing se consideran anticuados según las nuevas ramas de la ciencia cognitiva y los dispositivos cognitivos, ya que cuando se formularon en 1980 y 1950 respectivamente la tecnología de Inteligencia Artificial estaba en sus inicios y Searle estaba realizando reflexiones filosóficas y teóricas sobre las mismas. 

Sin embargo, el experimento de la habitación china sigue teniendo un enorme impacto en el campo de la Inteligencia Artificial debido a la clasificación de la IA que de él deriva, ya que sigue siendo la división más empleada a día de hoy para categorizar los tipos de Inteligencia Artificial posibles. 

En esta clasificación la dimensión empleada para distinguir distintos tipos de inteligencia artificial es la capacidad de esta para imitar el comportamiento humano, teniendo en cuenta que la inteligencia real va más allá de esta capacidad. Tal y como hemos visto en el apartado de la definición de la IA, la inteligencia no está necesariamente limitada a la inteligencia humana biológica, pero históricamente ha sido el baremo con el que se han medido las capacidades de los sistemas inteligentes artificiales ya que, a día de hoy, no conocemos otra superior. 

Mediante esta herramienta de medida se obtienen los siguientes tipos de IA: 

- a. **ANI** . Inteligencia Artificial Específica o Débil ( _Artificial Narrow Intelligence_ por sus siglas en inglés) 

- b. **AGI** . Inteligencia Artificial General o Fuerte ( _Artificial General Intelligence_ por sus siglas en inglés) 

- c. **ASI** . Súper Inteligencia Artificial ( _Artificial Super Intelligence_ por sus siglas en inglés). 

09 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

#### **Inteligencia Artificial Específica (ANI)** 

Todas las IA que han sido programadas hasta el momento actual son, sin ningún tipo de dudas, de la clase ANI, o IA específica. Esto quiere decir que están centradas en aprender a cumplir un objetivo de manera autónoma y precisa, tanto o más que los humanos, imitando a la perfección pequeñas parcelas de nuestra inteligencia. La característica clave de los objetivos que llevan a cabo es que son absolutamente concretos y específicos. Bien sea hablar chino a la perfección, identificar la especie a la que pertenece una determinada planta a través de una fotografía, detectar aterosclerosis en una imagen médica o conversar con un humano acerca de los billetes de tren que este no está siendo capaz de comprar, las Inteligencias Artificiales actuales están totalmente centradas en tareas muy bien definidas y en alcanzar la excelencia en las mismas. Sus variados mecanismos convierten ingentes cantidades de datos ( _big_ data) en información y conocimiento abstracto para poder detectar patrones, hacer predicciones y tomar decisiones 

Si bien las máquinas con ANI pueden llegar a parecer más inteligentes que un humano, la realidad es que siempre realizan sus tareas bajo un conjunto de limitaciones y condiciones específicas que son indispensables para su funcionamiento. Esta limitación es el origen de la denominación “débil” ya que cualquier variación del contexto y el entorno hacen totalmente inservible a estos sistemas. Carecen de la consciencia y comprensión humanas, aunque en ocasiones puedan imitarla con gran precisión. 

Si a un _chatbot_ de asistencia para la compra de billetes de tren le pidiéramos entradas para un concierto, opciones de recetas saludables, o los resultados de un partido de fútbol se limitaría a devolver un mensaje similar a “lo siento, no entiendo lo que necesitas, inténtalo de nuevo”. Si a una IA de detección de arterioesclerosis le mostráramos una radiografía de una columna vertebral se limitaría a no devolver ningún resultado, y de igual manera una red neuronal de clasificación de especies de plantas devolvería un “ _Unknown_ ” si se le adjuntara la foto de un perro. 

Los sistemas ANI dependen de manera inevitable de los parámetros y decisiones de diseño que tomen sus desarrolladores, así como del set de datos que procesan para ser entrenadas, por lo que son capaces de optimizar un proceso muy específico, pero carecen de la capacidad de realizar otros procesos, así como de aprender por sí mismos nuevas habilidades. 

En definitiva, estos sistemas son inteligentes, ya que resuelven problemas complejos con numerosos parámetros de entrada y aprenden de la experiencia del pasado, pero son especialistas inteligentes que, a día de hoy, se encuentran limitados a la tarea específica para las que le has destinado su desarrollador humano. 

10 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

#### **Inteligencia Artificial General (AGI)** 

Los seres humanos tenemos una inteligencia categorizada como general. Sabemos realizar más de una tarea, incluso de forma simultánea. En un mismo día cocinamos, conducimos, desempeñamos nuestro trabajo, mantenemos conversaciones y leemos el periódico sin que ninguna de estas tareas afecte negativamente al rendimiento de las demás. Además, aprendemos a realizar estas tareas en base a la experiencia. En la actualidad, una Inteligencia Artificial que sea tan polivalente como un ser humano es un mero constructo teórico que no ha llegado a materializarse. 

Las voces de ciertos expertos como el director del departamento de IA del CSIC, Ramón López de Mántaras, creen que “Por muy inteligentes que lleguen a ser las futuras inteligencias artificiales, incluidas las de tipo general, nunca serán comparables a la inteligencia humana”. Sin embargo, personalidades tan destacadas como Marvin Minsky, cofundador del laboratorio de inteligencia artificial del Instituto de Tecnología de Massachusetts (MIT) y compañero de McCarthy en los inicios de su carrera, se ha mostrado realmente optimista de las posibilidades que tiene la AGI de convertirse en una realidad en un futuro no muy lejano. 

Este tipo de inteligencia, posible o no en el futuro, describe un tipo específico de mentalidad a la hora de desarrollar algoritmos. Si los desarrolladores fueran capaces de desarrollar una Inteligencia Artificial General, esta poseería una inteligencia igual que la humana, con autoconsciencia, capacidad para resolver problemas, aprender y planificar para el futuro. 

La AGI implicaría por tanto sistemas computacionales que fueran indistinguibles de la mente humana por medio de cualquier test disponible. Para conseguir cumplir este objetivo exitosamente, sería necesario encontrar una manera de que las máquinas fueran conscientes, programando un conjunto de habilidades cognitivas. Los ordenadores deberían poder alcanzar el aprendizaje por experiencia por completo, más allá de las capacidades actuales relativas a tareas únicas, siendo capaces de aplicar conocimiento basado en la experiencia a una amplia gama de problemas. 

Esto implicaría que las máquinas fueran capaces de sentir, procesar y distinguir necesidades, emociones, creencias y los procesos de pensamiento de otras entidades inteligentes. Esto se denomina la “teoría de la mente”, que no trata de replicar o simular una inteligencia, sino de crear inteligencias que puedan entender realmente los humanos y el mundo. 

El intento que más cerca ha quedado de alcanzar la AGI por el momento es el ordenador “K” diseñado y construido por Fujitsu. Su principio se basa en una aproximación biológica: simular todos y cada uno de los componentes del cerebro humano que conocemos a día de hoy y las interacciones entre ellos. Las neuronas y sus neurotransmisores se simulan por medio de millones de líneas de código que permiten emular con toda precisión posible el funcionamiento orgánico de una “mente”. Dado que “K” necesita 40 minutos de procesamiento para procesar un segundo de actividad neuronal real, no es sencillo predecir cómo o cuándo la AGI podría convertirse en una realidad. 

11 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

La definición de inteligencia de Searle y en concreto de la AGI no tienen implicaciones críticas para los profesionales que desarrollan IA en la actualidad. Stuart Russel y Peter Norving, investigadores en las universidades de Berkeley y Standford respectivamente, afirman que la gran mayoría de investigadores en el campo de la IA “no se ven afectados por la hipótesis de la Inteligencia Artificial General, ya que siempre y cuando el programa funcione y cumpla con su tarea, la diferenciación entre una simulación o inteligencia real no va a cambiar el resultado”. Es decir, que el objetivo principal de la IA es crear sistemas útiles que actúen de forma inteligente, no siendo relevante si esa inteligencia es “sencillamente” una simulación. Como veremos más adelante, estos dos profesores desarrollaron su propia propuesta de clasificación de sistemas inteligentes para tratar de acercarse a la realidad de la IA desde una perspectiva más práctica. 

#### **Súper Inteligencia Artificial (ASI)** 

La Super Inteligencia Artificial (ASI) es la última clasificación de IA según esta clasificación. Este tipo de inteligencia es, a día de hoy, meramente teórica e hipotética, ya que en ningún caso se ha conseguido ningún intento por lejano que fuera a este tipo de sistema. 

Fue definida por el profesor Nick Bostrom de la Universidad de Oxford en su libro “Superintelligence: Paths, Dangers, Strategies” en 2014 como colofón a la clasificación original de Searle. En este libro, se presenta la IA como “cualquier inteligencia que exceda con creces el rendimiento cognitivo humano en cualquier dominio de interés”. 

La premisa de este tipo de inteligencia es que no solo imita o comprende conscientemente la inteligencia humana y su comportamiento, sino que supone que las máquinas pueden llegar a ser conscientes de sí mismas y superar las habilidades mentales de los seres humanos. 

Las máquinas con ASI podrían pensar en abstracciones e interpretaciones de la realidad que son inconcebibles para los seres humanos. El cerebro humano está limitado a los sentidos que lo relacionan con el mundo y a un número limitado de neuronas que procesan toda esta información. ¿Por qué estarían las máquinas limitadas también por estas restricciones biológicas? 

Un sistema con ASI podría teóricamente ser mejor en cualquier actividad que un humano puede realizar, incluyendo relaciones sociales y emociones. Pero también tendría una mayor memoria, habilidad de procesar y analizar datos y respuesta estímulos. En consecuencia, la capacidad de toma de decisiones y de resolución de problemas de estos seres inteligentes sería notablemente superior que la de los seres humanos. 

Tanto Bostram como David Chalmers, catedrático de neurociencia en la Universidad de Nueva York y codirector del centro de la mente, cerebro y consciencia de esta misma universidad, sostienen que la ASI será una consecuencia directa de la consecución de la AGI. Entre otros argumentos, esgrimen que el cerebro humano es un mero conjunto 

12 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

de elementos mecánicos y que, por tanto, podría ser replicado sintéticamente. Uniendo esto a que la velocidad de un microprocesador actual puede alcanzar picos de 5GHz y una neurona opera a picos de 200Hz, aducen que es probable que un sistema que mejore el cerebro humano acabe por existir. Sin embargo, otros profesionales de la Inteligencia Artificial categorizan este tipo de sistema inteligente como parte de la ciencia ficción, y no de una realidad cercana. 

En resumen, en función de esta propuesta de división, la IA puede ser clasificada en función del tipo de inteligencia que muestra. Aquellos sistemas que muestren una inteligencia limitada a una serie de problemas específicos y bien definidos serán parte de la denominada Inteligencia Artificial Específica (ANI). Aquellos que sean capaces de conocer y sentir como lo hace un ser humano, resolviendo problemas genéricos con solvencia, pertenecerán a la Inteligencia Artificial General (AGI), siendo a día de hoy sistemas que no han sido desarrollados pero que se asume que acabarán siéndolo en algún punto del desarrollo tecnológico. Por último, los agentes inteligentes que, además de conocer y ser consciente, excedan las capacidades de la inteligencia humana son denominados agentes con Super Inteligencia (ASI), que actualmente son una teoría puesta en duda por ciertos expertos. 

La siguiente tabla muestra los aspectos más relevantes de las tres clasificaciones de la IA según la clasificación ANI – AGI – ASI. 

|**ANI**|**AGI**|**ASI**|
|---|---|---|
|Inteligencia<br>específica,<br>limitada a un problema<br>concreto en situaciones<br>concretas.|Inteligencia general capaz de<br>desarrollar herramientas propias<br>para la resolución de problemas<br>complejos que no hayan procesa-<br>do nunca.|Inteligencia que excede los lími-<br>tes de las capacidades cognitivas<br>humanas.|
|No conocen, sienten ni<br>procesan como un huma-<br>no, siguen un algoritmo.|Son capaces de conocer, sentir y<br>procesar el entorno y los proble-<br>mas como un ser humano.|Son conscientes de sí mismas y<br>de sus habilidades cognitivas.|
|Todas las IA por el mo-<br>mento son ANIs.|Se espera que el ser humano<br>llegue a desarrollar AGI en el<br>futuro|Gran parte de los expertos<br>consideran que la ASI no es un<br>objetivo alcanzable|



13 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

### **1.2.2. Sistemas humanos y racionales** 

Stuart Russell y Peter Norvig publicaron en su libro _“Artificial Intelligence: A Modern Approach”_ una posible clasificación de la IA en cuatro clases basadas en el propósito que cada una de estas persigue.  La premisa de esta clasificación parte de diversas definiciones de la IA con distintas perspectivas respecto a su propósito, ofrecidas por distintos expertos en la materia, que Russell y Norvig organizan tal y como puede consultarse en la siguiente tabla: 

“Un emocionante esfuerzo por conseguir que las computadoras piensen… máquinas con mentes, en todo su sentido.” (Haugeland) 

“La automatización de actividades que asociamos con el pensamiento humano, como la toma de decisiones, la resolución de problemas o aprender” (Bellman) 

“El estudio de las facultades mentales a través del uso de modelos computacionales” (Charniak y McDermott) 

“La rama de la computación que permite percibir, razonar y actuar” (Winston) 

“El arte de crear máquinas que realicen funciones que precisan de inteligencia cuando las realizan las personas” (Kurzweil) 

“El estudio de cómo hacer que los computadores hagan cosas que, por el momento, las personas hacen mejor” 

“Un campo de la ciencia que busca explicar e imitar un comportamiento inteligente en términos de procesos computacionales” (Schalkoff) 

“La rama de la informática que está centrada en la automatización del comportamiento inteligente” (Luger y Stubblefield) 

Como puede observarse, las distintas definiciones de IA han sido organizadas en dos dimensiones diferenciadas. Por un lado, se concibe la IA desde una perspectiva centrada en procesos mentales, conocimiento y aprendizaje; estas son las definiciones de la fila superior. Por otro, la IA se contempla como un problema relacionado con el comportamiento y la acción; representadas en la fila inferior. Por otro lado, se pueden agrupar las definiciones de la izquierda como aquellas que recurren al ser humano para justificar el éxito de la IA, mientras que aquellas de la derecha hacen referencia a un concepto teórico de la inteligencia, del raciocinio. 

Si, por tanto, transformamos esta tabla de definiciones en sus correspondientes clases basadas en las dimensiones del pensamiento y la actuación, y de lo humano contra lo teórico, obtendremos la siguiente clasificación de los tipos de IA que existen en función de su meta. 

14 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

|Sistemas que piensan como humanos|Sistemas que piensan racionalmente|
|---|---|
|Sistemas que actúan como humanos|Sistemas que actúan racionalmente|



#### **Sistemas que piensan** 

En esta clasificación se enmarcan los sistemas que están centrados en los procesos del pensamiento, aquello que se denomina razonamiento. Los agentes inteligentes que piensan, así como sus desarrolladores, tratarán de emular los procesos de argumentación, aprendizaje, lógica y comprensión del entorno. En algunos casos, tratarán de emular estos procesos cuando suceden en el humano y se denominarán “sistemas que piensan como un humano”. En otras ocasiones, la perspectiva partirá del razonamiento teórico, por lo que estos sistemas “pensarán de forma racional”, como veremos a continuación. 

#### **_Sistemas que piensan como humanos_** 

Los sistemas que piensan como humanos están focalizados en automatizar procesos relacionados con la resolución de problemas, la toma de decisiones y el aprendizaje basándose en los procesos que ocurren en el interior de un ser humano cuando este trata de hacerlo. 

Si un sistema es capaz de adquirir conocimiento por medio de la experiencia y la repetición, y posteriormente resolver problemas relacionados con aquello que observó, estará incluido en esta categoría. El ejemplo real más extendido en la actualidad es el de las redes neuronales. Estos algoritmos están basados en Aprendizaje Profundo o Deep Learning denominado así por la profundidad de capas de neuronas que componen estos modelos. Aunque esta tecnología será explorada en profundidad en próximas unidades y módulos, es relevante comprender por qué se considera que son sistemas que **piensan** como **humanos** . 

Las redes neuronales artificiales están diseñadas a imagen y semejanza de aquellas que hay en el cerebro humano. Tratan de replicar la compleja maraña de señales y conexiones que existen en nuestro cerebro, saltando de neurona a neurona hasta completar un pensamiento, o resolver un problema. En el cerebro cada neurona recibe una señal de entrada ( _input_ ) y produce una señal de salida ( _output_ ). Este comportamiento es perfectamente modelable matemáticamente e implementable en código fuente. 

15 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Pero no es por su estructura por lo que se les incorpora habitualmente en esta categoría, sino por su funcionamiento. Una red neuronal es un algoritmo sin conocimiento _a priori,_ un cascarón vacío al que nadie indica cuál es la lógica subyacente del mundo en el que debe aprender a resolver problemas. A medida que se la enseña o entrena (por el término más empleado en este proceso, _train_ , en inglés), sus neuronas se adaptan al problema que se trata de que resuelvan, es decir, aprenden. A través de este proceso de aprendizaje que será más elaborado en otras secciones y unidades, las redes neuronales consiguen obtener conocimiento abstracto de los ejemplos que experimentan. Una vez entrenadas, podrán aplicar este conocimiento en cualquier problema o tarea de igual índole. Este proceso de aprendizaje y posterior toma de decisiones es el que convierte a las redes neuronales en sistemas que piensan como humanos, ya que simulan tanto las estructuras físicas como los procesos de aprendizaje y pensamiento que por el momento las ciencias de la vida asocian a los seres humanos. 

#### _Sistemas que piensan racionalmente_ 

En contraposición al pensar mundano de un ser humano en su entorno habitual, surge el concepto teórico de cómo pensar, una reflexión sobre el pensamiento de forma teórica y enunciada. Esta idea de pensar de forma racional ha acompañado a la filosofía y posteriormente a las matemáticas, la lógica y la informática desde el siglo IV a.C. 

Fue Aristóteles el que planteó originalmente que la forma “correcta” de pensar era por medio de la lógica. Esta lógica estaba compuesta en su primer momento de los silogismos, un tipo de argumento lógico que siempre devolverá resultados ciertos si sus premisas lo son. Gracias al posterior desarrollo de la lógica formal en el que no profundizaremos, fue posible generar el sustento de los primeros sistemas de inteligencia artificial lógica a mediados de siglo XX. En este tipo de sistemas inteligentes “primitivos”, un programa informático era capaz de analizar un problema expresado a base de premisas lógicas y encontrar una solución en caso de haberlo. 

La gran diferencia con pensar como un humano es el conocimiento _a priori_ . En este caso, el sistema inteligente conoce una serie de reglas lógicas por las que se ordena el mundo, y el problema a resolver se le plantea como una serie de premisas que se deben comprobar ciertas o no en función de estas reglas. 

El principal problema de desarrollar sistemas que piensan de forma racional, es decir, que siguen las normas de la lógica matemática, es asumir que todo es susceptible de ser descrito como verdades absolutas. En la gran mayoría de problemas del mundo real, el nivel de incertidumbre es notablemente alto, y existen variables que no pueden ser meramente expresadas como afirmaciones lógicas. Por otro lado, existe una gran distancia entre la resolución teórica de un problema y su aplicación. Esta distancia supone que este tipo de sistemas tienden a cometer fallos a la hora de tomar decisiones correctas sobre problemas reales, ya que solo contemplan las premisas con las que han sido alimentados para resolver un problema, y estas difícilmente habrán podido modelar la realidad al completo. 

16 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Los desarrolladores de este tipo de sistemas les proporcionan un conocimiento _a priori_ y una serie de reglas teóricas que pueden ayudarles a ejecutar sus objetivos, pero no les proporcionan la capacidad de pensar y aprender como humanos. 

Este tipo de sistemas, en definitiva, no tiene en cuenta la incertidumbre ni la complejidad de los problemas reales, por los que su uso es limitado a casos muy específicos. 

Uno de los mayores éxitos de sistemas basados en la lógica es el de Dendral. Este programa fue desarrollado en la década de 1960 en Standford, en los albores de la creación de sistemas inteligentes. Su conocimiento partía de una serie de complejas reglas lógicas denominadas heurísticas, gracias a cuya aplicación estricta era capaz de inferir la estructura molecular de una determinada molécula. En la década de los 60 ser capaces de analizar la estructura de una molécula de forma teórica fue de gran ayuda para biólogos y químicos. 

No obstante, la mayor limitación de Dendral, que sus propios creadores observaron, es que no era capaz de aprender conceptos nuevos, ni abstraer conocimiento de su experiencia. Sencillamente aplicaba la lógica más estricta según la definición de sus desarrolladores, y proporcionaba resultados en base a la ejecución de la misma. 

Con el tiempo y la aparición de sistemas inteligentes más complejos como las redes neuronales, este tipo de programas acabaron desapareciendo de la gran mayoría de casos de uso comerciales, y actualmente forman parte de una dimensión de la IA que se aleja de la realidad del desarrollo y las necesidades de la industria actual. 

#### **Sistemas que actúan** 

En contraposición con los sistemas que piensan, Russell y Norving proponen los sistemas que actúan como aquellos centrados en la acción y el comportamiento. En estos sistemas el rasgo definitorio no es que proceso por el cual se llega a la resolución de un problema, sino el comportamiento y acciones específicas realizadas por un sistema. 

#### **_Sistemas que actúan como humanos_** 

Aquellos agentes que tengan un comportamiento asimilable con un ser humano formarán parte de esta categoría. Para evaluar esto, Russel y Norving proponen emplear el Test de Turing, ya desarrollado previamente. Para ser capaz de superar el Test de Turing, un computador necesitará poseer, al menos, las siguientes capacidades. 

- Procesamiento del Lenguaje Natural (NLP): Capacidad para comprender, procesar y comunicarse de forma fluida y satisfactoria en un lenguaje humano. 

- Representación del conocimiento: Gracias a esta habilidad, la máquina podrá almacenar información que ha recibido antes y durante la resolución de un problema 

- Razonamiento automático: La capacidad de extraer conclusiones en base al co- 

17 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 

nocimiento extraído y modelado en base a una conversación en lenguaje natural. 

- Aprendizaje Automático (Machine Learning): La capacidad para detectar patrones y extrapolar conocimiento abstracto de la experiencia de forma automática para actualizar automáticamente todas las demás capacidades y habilidades de tal forma que se perciba una mejora a medida que avanza la interacción de la máquina con el problema. 

A pesar de que el Test de Turing solo menciona la interacción verbal con una máquina para determinar si actúa o no como un humano, posteriormente se ha desarrollado el denominado Test de Turing completo que trata de subsanar esta limitación. En este test, la comprobación no solo se realiza mediante una conversación, sino que la máquina debe interactuar visual y táctilmente con distintos elementos a efectos de evaluación de su comportamiento humano. 

Actualmente, el Test de Turing completo es el que se emplea para determinar si un sistema actúa como un humano, por lo que a las habilidades anteriores sería necesario añadir otras dos para completar un sistema que forme parte de esta categoría. 

- Visión Artificial ( _computer vision_ ): Esta tecnología permite a un sistema interactuar visualmente con su entorno, comprendiendo imágenes y vídeos captados a través de cualquier tipo de sensor, detectando objetos, ubicándolos espacialmente y comprendiendo su tipología, estado y finalidad. 

- Robótica y tecnología háptica: Gracias a la robótica un sistema inteligente podría interactuar con diversos objetos y con la tecnología háptica comprender sus texturas, ubicación, dureza, material… 

Como se puede observar, en este caso la dimensión principal no es el medio por el que los sistemas reflexionan sus respuestas, sino el tipo y calidad de sus respuestas. En este caso no es relevante si un sistema razona como un humano o según la lógica matemática, siempre y cuando sean capaces de convencer a un evaluador de que son tan humanas como él. 

#### **_Sistemas que actúan racionalmente_** 

Por último, se encuentran los agentes inteligentes que tienen un comportamiento basado en el raciocinio, los denominados agentes inteligentes. Mientras que en la perspectiva del pensamiento racional nos encontrábamos con agentes que siguen reglas lógicas teóricas para obtener razonamientos que siempre sean ciertos, es decir, en el pensamiento, esta perspectiva se centra en la acción racional. Hay ocasiones en las que no hay algo correcto o verdadero que hacer según la lógica, pero es necesario actuar. 

18 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Por otro lado, frente a la perspectiva del comportamiento similar al de un humano, actuar de manera racional proporciona una forma más descriptiva para la ciencia de acercarse a un estándar de raciocinio bien definido y general, evitando preguntarse cómo piensa un humano o cómo actúa un humano. Sin embargo, el comportamiento perfectamente racional no es posible computacionalmente, ya que requiere demasiadas consideraciones y cálculos, aunque es posible aproximarse al mismo. 

Esta aproximación a la IA es la forma más empleada actualmente para pensar en un sistema inteligente, basada en construir agentes inteligentes y centrada en los posibles componentes de estos. Buscará, por tanto, maximizar el resultado dado el conocimiento con el que cuenta, independientemente de su similitud en el razonamiento o en el comportamiento con los de un ser humano. 

### **1.2. La clasificación de la IA de Hintze** 

Una tercera forma de distinguir entre tipos de IA la encontramos en la categorización que hizo Arend Hintze, profesor de biología integradora e ingeniería y ciencias de la computación en la Universidad Estatal de Michigan. Hintze distingue entre 4 tipos de IA, tanto existentes hoy en día como todavía por desarrollarse. Los vemos en detalle a continuación: 

#### **Máquinas reactivas** 

Las máquinas reactivas son el tipo más básico de Inteligencia Artificial según esta propuesta de clasificación. Este tipo de máquinas son capaces de percibir el mundo en el que se encuentran y reaccionar al mismo en el momento instantáneo en el que lo perciben. Este tipo de sistema no dispone de una memoria, por lo que carece de la capacidad de emplear la experiencia pasada para aprender ni para generar nuevo conocimiento que le permita reaccionar de una forma más precisa o eficiente en próximas ocasiones. No son capaces de evolucionar hacia mejores versiones de sí mismas, y una vez desarrolladas realizarán los mismos pasos una y otra vez, tal y como los sistemas que piensan racionalmente en la clasificación de Russel y Norvig. 

Un sistema que analiza el número de ejes de un vehículo para aplicar una cuantía u otra en un peaje es un sistema reactivo. A través de tecnología de visión artificial, procesa una instantánea de las ruedas de un vehículo, aplica reconocimiento de patrones, las cuenta y aplica una tarifa estándar predefinida. En ningún caso necesitará volver a aprender qué es una rueda, a contar, o a recordar los últimos vehículos que han pasado para modificar la forma de contar ejes en el futuro. 

El objetivo de este tipo de sistemas está limitado a una serie de tareas concretas bien definidas, por lo que también son asimilables a parte de los sistemas de inteligencia artificial específica o ANI que vimos en la primera propuesta de clasificación de IA. En algunos casos de uso específicos, la decisión de que un sistema inteligente sea una máquina reactiva 

19 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 

sin memoria ni evolución no significa que esta desempeñe peor su tarea, sino una mejora notable en la eficiencia del sistema a desarrollar. Esto es porque no todos los sistemas inteligentes precisan de un razonamiento complejo ni de una capacidad de aprendizaje, si su tarea fundamental es, por ejemplo, preparar sushi en un restaurante automatizado. 

Cuando el objetivo de un sistema inteligente sea la automatización de un proceso concreto y específico basado en la repetición pero que requiere de una cierta percepción del entorno y de la capacidad de realizar una toma de decisiones en tiempo real, las máquinas reactivas suponen el mejor compromiso entre precisión y coste computacional posible, por lo que son altamente recomendables. 

#### **Memoria limitada** 

Como bien indica su nombre, los sistemas IA con memoria limitada tienen la capacidad de recordar eventos próximos en el tiempo, pero con un _buffer_ limitado. La mejor forma de imaginarlo es mediante una serie de ranuras en las que se pueden almacenar recuerdos. Si una máquina tiene diez ranuras, podrá almacenar los primeros diez sucesos que perciba en el desarrollo de una tarea. Sin embargo, cuando experimente un nuevo suceso, el undécimo, deberá prescindir del primero para avanzar todos los sucesos una posición y poder almacenar el undécimo. Esto se denomina en jerga informática una cola FIFO, por sus siglas en inglés _First In, First Out,_ es decir, el primer recuerdo que llega a la máquina será el primero en salir cuando llegue uno nuevo que exceda la capacidad de memoria de esta. 

Esta limitada capacidad de recordar les permite detectar patrones a corto plazo por lo que pueden adaptar su lógica interna para dar respuestas distintas a los mismos estímulos en función de la información recopilada en el pasado. Sin embargo, al carecer de un modelo de representación del conocimiento y la experiencia, si bien pueden modificar su comportamiento a corto plazo, no son realmente capaces de obtener representaciones del conocimiento perdurables en el tiempo. 

Un buen ejemplo de máquinas de IA de memoria limitada es el coche autónomo. Un coche autónomo necesita conocer qué ha percibido en los últimos segundos para tomar decisiones acerca de lo que va a hacer en los siguientes. Si un coche autónomo fuera una simple máquina reactiva solo sería capaz de actuar según la información instantánea que percibe. Esto supondría un problema enorme teniendo en cuenta que las decisiones en conducción se basan principalmente en cálculos de trayectorias, tiempos de intersección y atención a objetos sobrepasados o que se acercan por el horizonte. Es por ello que un coche autónomo necesita memoria a corto plazo, ya que recordará que ha adelantado a un camión hace dos segundos, y por tanto no puede volver al carril en el que estaba sin provocar una colisión. 

20 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Las implicaciones de la limitación de la memoria son claras en este ejemplo. Un coche autónomo no cambia su representación del mundo en cada viaje.  Las señales, normas y tipos de vehículo que conoce aplican cada día que transita la vía pública, y no necesita actualizar este conocimiento de manera automática, por lo que no precisa de una memoria a largo o medio plazo que le permita aprender de la experiencia de forma perdurable. De la misma manera que sucede con las máquinas reactivas, la decisión de dotar a un sistema de una memoria a corto plazo es una decisión de diseño estratégica ya que permite ahorrar una gran cantidad de espacio de almacenamiento y del coste computacional que requiere un algoritmo que aprende de forma duradera de su experiencia. 

Hay tres tipos de algoritmo principales que permiten a un sistema inteligente aprender de la experiencia reciente, todos ellos bajo el paraguas del _Machine Learning (ML)._ Todos ellos, así como el ML, serán analizados en profundidad en próximas unidades y módulos, pero se podría hacer un resumen de la siguiente manera: 

- a. **Reinforcement Learning.** Los sistemas que aprenden por refuerzo aprenden por medio de un sistema de prueba y error. Un algoritmo refuerza positivamente las acciones hacia las que el sistema debe encaminarse, y penaliza aquellas que van en dirección contraria. Con cada refuerzo positivo, el modelo modifica ligeramente su comportamiento para poder repetirlo, y con cada refuerzo negativo el algoritmo vuelve a versiones anteriores. En ningún momento se genera un conocimiento abstracto sobre el problema, sencillamente se trata de no ser penalizado. Los modelos que aprenden a jugar a videojuegos clásicos como el PacMan o el Tetris tienden a funcionar por aprendizaje por refuerzo, ya que juegan innumerables partidas en las que los movimientos acertados se premian y los incorrectos se penalizan. 

- b. L **ong Short Term Memory (LSTM).** Este tipo de modelos se emplean para comprender cadenas de elementos como pueden ser conjuntos de palabras que forman una frase. Para comprender una frase no es suficiente comprender el significado de cada palabra que la compone, sino que es imprescindible analizar el conjunto, generando una suerte de vector resumen de todas las palabras procesadas hasta el momento para poder analizar el significado de la frase completa una vez esta termine. Contar algo más de LSTM 

- c. **Evolutionary Generative Adversarial Networks (E-GAN).** Estas redes neuronales son capaces de explorar distintos caminos de procesamiento basándose en la última experiencia que han tenido en cada decisión. Esto quiere decir que son modelos que están constantemente buscando la mejor manera de realizar tareas a base de simular qué habría pasado si en vez de tomar una decisión hubieran tomado otra distinta. 

21 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Todos los sistemas con memoria limitada forman parte, de igual forma que las máquinas reactivas, de la Inteligencia Artificial Específica (ANI). En este caso, son máquinas capaces de aprender de la experiencia, pero en ningún caso hablamos de inteligencias capaces de realizar cualquier tarea que se les encomiende de igual forma que un humano como haría un sistema con AGI, y aún menos son conscientes de su propia inteligencia ni superan las capacidades abstractas de la inteligencia humana. 

#### **Teoría de la mente** 

A partir de esta clase de IA, Hintze se adentra en el terreno de lo teórico. A día de hoy no se ha logrado desarrollar ningún sistema que cumpla la denominada _Theory of Mind._ 

Este concepto está basado en la premisa de la comprensión acerca de que otros seres vivos tienen pensamientos y emociones que afectan al comportamiento de los demás. 

La teoría de la mente juega un papel esencial a la hora de explicar la formación de sociedades humanas, ya que reconocer las emociones y deseos tanto propias como de otros individuos, permitió que trabajar de forma conjunta fuera una realidad. 

Si una máquina tuviera esta capacidad, podrían comprender cómo los seres humanos y otras máquinas son capaces de tomar decisiones y de sentir emociones a través de la observación de uno mismo y de la determinación. Con esta habilidad, serían capaces de tomar decisiones propias genuinas. Podrían comprender su entorno a través de la observación y, más importante, la comprensión de nuestros gustos, necesidades, modelos de comportamiento y deseos. Es decir, podrían llevar a cabo una interacción social indistinguible de aquella que realiza un ser humano, creando una relación bidireccional entre los humanos y la inteligencia artificial. 

Este concepto es muy cercano a las definiciones de Inteligencia Artificial General (AGI) y de sistemas que piensan y se comportan como humanos. 

#### **Autoconciencia** 

Hintze considera el último paso para culminar el desarrollo de la IA la capacidad de desarrollar sistemas que pueden tener conciencia sobre sí mismos, siendo capaces de tener una representación interna de su propio ser. Son sistemas que se reconocen como entidades independientes, que pueden tomar sus propias decisiones diferenciando entre su propio ser y el del resto de individuos y objetos de su entorno. En este sentido, las máquinas con autoconciencia solo se distinguen de aquellas que cumplen la teoría de la mente en el auto reconocimiento. Es, como en la Super Inteligencia Artificial (ASI), un sistema que conoce, siente y es consciente de su propia existencia. 

Obtener esta tecnología sería el primer paso hacia obtener la denominada singularidad tecnológica, que sostiene que, llegado a este nivel de tecnología, los sistemas computacionales podrían mejorarse a sí mismos recursivamente, e incluso construir sistemas mejores que ellos mismos. En este hipotético futuro, los desarrolladores humanos no serían necesarios para continuar el desarrollo de la IA. La IA crearía IA. 

22 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Las diversas formas de clasificar a los sistemas inteligentes son meras divisiones propuestas por diversos investigadores del campo de la IA para comprender mejor dónde estamos y dónde podemos estar. Como puede observarse, de todas ellas se puede obtener una hoja de ruta que trata de predecir el futuro de la IA en base a diversas consideraciones. 

Russell y Norvig se centran en su clasificación en los sistemas que han existido hasta el momento en la práctica, aunque en la última de sus divisiones, los sistemas que actúan racionalmente, dejan abierta la puerta a cualquier posible avance de la Inteligencia Artificial. 

Sin embargo, empleando las clasificaciones de Searle y Hintxe, a día de hoy la realidad del campo de la Inteligencia Artificial es que todos los sistemas que existen en la actualidad pertenecen exclusivamente a los primeros escalones de cada clasificación. Actualmente los sistemas inteligentes que tenemos no cumplen con una definición de inteligencia ni remotamente parecida a la de los seres humanos, por lo que no exceden en ningún caso las capacidades de la Inteligencia Artificial Débil (ANI). 

Hemos conseguido desarrollar sistemas que ejecutan acciones repetitivas y procedimentales con mejor acierto que los seres humanos. Contamos incluso con sistemas creativos, que escriben poemas, canciones y reseñas en internet. También con asistentes personales y coches que se conducen a sí mismos. Pero ninguno de ellos es más que un algoritmo que en base a un buen diseño previo y a un proceso de aprendizaje por medio de soluciones de ecuaciones de optimización matemática o por ejercicios eternos de prueba y error, es capaz de realizar una tarea procedimental con una precisión notable. 

La realidad es que ningún sistema en la actualidad es capaz de comprender emociones, sentimientos ni deseos, ni de experimentar estas sensaciones o ser conscientes de sí mismos. Actualmente, todo agente inteligente que se asemeje a la variada y flexible inteligencia humana es un mero ejercicio teórico para cuya concesión aún quedan décadas. Estas clasificaciones teóricas son un ejercicio académico interesante, ya que ayudan a marcar objetivos, límites, beneficios y riesgos de la IA que vendrá. En el mundo actual de la Inteligencia Artificial, tanto en su vertiente investigadora como en la comercial, no hay una preocupación real por alcanzar este tipo de sistemas, ya que se estima que no será hasta 2070 que una IA alcanzará niveles de inteligencia parecidos a la humana. En la actualidad la investigación de Inteligencia Artificial está centrada en solucionar problemas cada vez menos concretos pero centrados en campos un tanto cerrados. Por ejemplo, la tarea de conducir un vehículo de forma autónoma puede parecer un ejemplo de ANI, incluso de inteligencia débil. Sin embargo, estos algoritmos están compuestos por numerosas redes neuronales profundas que realizan millones de cálculos por segundo para tratar de ser conscientes de su entorno, y llegar con seguridad a su destino. 

23 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

La cantidad de sistemas que están entrelazados para hacer de este tipo de tecnología una realidad distan de considerarse débiles por la opinión experta, sino que demuestran altos niveles de inteligencia y especialización. La discusión filosófica sobre la conciencia, los sentimientos y la empatía siguen siendo altamente interesantes para los investigadores más teóricos de este campo científico, pero a día de hoy el foco de las compañías reales no está en conseguir que nuestro vehículo tenga conciencia de sí mismo y pueda sentir que es un ser artificial, sino en que cada vez sea más seguro y autónomo hasta no precisar de ningún tipo de supervisión humana para cumplir con sus objetivos. 

De igual forma sucede con todos los sistemas inteligentes en la actualidad. Los sistemas de generación de texto automático como el reciente GPT-3, que analizaremos en detalle en las siguientes unidades y módulos, da la impresión de ser un ser inteligente con conciencia dado que escribe artículos de opinión, música y guiones de películas entre otras cosas. Sin embargo, nada más lejos de la realidad. GPT-3 ha aprendido por pura imitación, y eso no hace algo menos valioso de este sistema. A día de hoy no hay un interés comercial ni un caso de uso real en el que sea imprescindible que la IA llegue a un nivel de ASI. No obstante, si las predicciones se cumplen, en medio siglo podríamos contar con sistemas inteligentes de tipo AGI, que podrían resolver a la vez problemas de conducción autónoma, escribir artículos científicos, programar otros sistemas inteligentes y conversar sobre sus emociones entre otras cosas. La realidad es que en la experiencia de los investigadores más veteranos de la IA, que conoceremos en la siguiente unidad, este tipo de afirmaciones excesivamente optimistas nunca han contribuido al desarrollo de la IA sino que han generado burbujas de optimismo que al explotar dañaban ampliamente a la disciplina. Conoceremos en la Unidad 2 todas estas realidades para comprender la importancia del realismo en el desarrollo de los sistemas inteligentes. 

Para terminar esta sección, trataremos de resumir los tipos de Inteligencia Artificial que hemos descrito hasta el momento desde una perspectiva de capacidades. Lo más importante es recordar que hasta el momento, y parece que así seguirá en las próximas décadas, todos nuestros sistemas son de IA débil, y que esto no implica ninguna realidad negativa. En la siguiente tabla se puede consultar una correspondencia entre las clasificaciones de Searle y Hintze. Es importante recordar que todas las clasificaciones de Russell y Norvig caen bajo el paraguas de la ANI. 

24 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 



#### **_Dato importante_** 

_La realidad es que ningún sistema en la actualidad es capaz de comprender emociones, sentimientos ni deseos, ni de experimentar estas sensaciones o ser conscientes de sí mismos._ 

25 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

## **2. Cronología y límites de la Inteligencia Artificial** 

La IA es _“la ciencia e ingeniería de crear máquinas inteligentes, concretamente programas de ordenador inteligentes. Está relacionada con el objetivo de emplear ordenadores para comprender la inteligencia humana, pero la IA no está necesariamente limitada a métodos observables biológicamente.”_ 

John McCarthy 

En el mundo actual, la gran mayoría de nosotros damos por hecho la existencia de la Inteligencia Artificial hasta el punto de haberla integrado por completo en nuestras vidas. Sin embargo, es un ejercicio esencial retroceder al pasado para comprender el presente y el futuro de esta tecnología, y para aprender de errores ya cometidos para no caer en ellos de nuevo. La historia de la IA ha sido esencialmente tumultuosa, con grandes periodos de expansión y grandes periodos de estancamiento, que invitan a reflexionar sobre la relación entra la IA y el hardware en el que se ejecuta, el optimismo frente al realismo de las capacidades reales de los sistemas inteligentes y los grandes errores que se han cometido a lo largo de las distintas etapas por no querer cambiar el statu quo. 

¿Cuándo surgió la idea de una inteligencia artificial? ¿En qué momento fue posible llevarla a cabo? ¿Han quedado ideas por el camino? Incluso antes de hacerse estas preguntas, es importante comprender cuándo y cómo surge la idea teórica de un computador artificial, así como cuándo se pone en práctica por primera vez, ya que la existencia de un computador que ejecute algoritmos es la premisa esencial de la existencia de la IA. Como veremos a lo largo de las diferentes asignaturas, a día de hoy todo sistema con IA es, en definitiva, un algoritmo. Un conjunto de instrucciones, por complejas que sean, que parten de la mente de un desarrollador humano y que son ejecutadas sobre algún tipo de máquina de cómputo. Desde el sistema más sencillo hasta el más complejo cumplen estas premisas. 

Qué son y cuándo surgieron los algoritmos y de dónde vienen nuestras máquinas de cómputo son asuntos que se tratarán en la siguiente sección de forma breve a modo introductorio. 

26 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 

### **2.1. Cronología de los algoritmos y las computadoras** 

El concepto teórico de algoritmo surgió hace más de mil años, concretamente en el primer siglo después de cristo. Se estima que en el año 830 en Persia el matemático al-Juarismi, llamado por los romanos Algorithmi, escribió sobre la posibilidad de un constructo matemático que permitiera la resolución metódica de problemas de álgebra y cálculo numérico mediante una lista predefinida de operaciones. En honor a Algorithmi se denomina algoritmo a todo conjunto de instrucciones predeterminadas que busca la resolución de un problema concreto. Actualmente no limitamos el concepto de algoritmo a problemas aritméticos, sino que le damos una definición más amplia en la que englobamos cualquier tipo de proceso ordenado que guía a un ejecutor hacia la consecución de un objetivo. O, en palabras del _Oxford Dictionary_ , “un conjunto de reglas que deben ser seguidas para resolver un problema concreto”. 

Es decir, una receta de cocina es un algoritmo, pero también lo es el protocolo de seguridad que sigue un vigilante de un aeropuerto o el sistema que cambia de precio los billetes de avión según nuestro comportamiento online previo. 

Al-Juarismi teorizaba su concepto de algoritmo con un ejecutor humano en mente, alguien que realizara los cálculos o, dicho de otra forma, computara. Una computadora. En ningún momento mencionó la remota posibilidad de algún tipo de maquinaria que pudiera resolver sus listas ordenadas de operaciones. 

No fue hasta 1642 cuando el célebre científico francés Blas Pascal desarrolló, gracias a las posibilidades que abrió el descubrimiento de los logaritmos neperianos por parte de John Napier, la primera calculadora mecánica. Esta calculadora estaba compuesta por una serie de ruedas y engranajes, y era capaz de ejecutar una serie de movimientos internos en un orden específico para sumar o restar números. Esta máquina sería mejorada por Leibniz posteriormente para ser capaz de multiplicar y dividir. 

Estas primeras calculadoras permitían realizar operaciones sencillas, pero supusieron un cambio de paradigma esencial. Por primera vez en la historia las operaciones aritméticas no se realizaban en un cerebro humano ayudado por tablillas de cera, pergaminos o libretas. Ahora las máquinas podían resolver problemas, aunque en el S.XVII estos problemas se redujeran a las operaciones aritméticas más básicas. 

Para que las máquinas fueran capaces de realizar procesos más complejos, fueron necesarios más de cien años. A mediados de S. XIX, el matemático británico Charles Babbage trabajó para generalizar las capacidades de estas máquinas calculadoras de forma que pudieran realizar un abanico mucho más amplio de operaciones, empleando por primera vez el término computadora en sus escritos. Esta computadora o “máquina analítica”, tal y como la bautizó, fue definida en 1837 y empleaba tarjetas perforadas como soporte para información de entrada. En estas tarjetas perforadas se representaba la información de entrada a la máquina en una disposición estructurada, tanto operaciones aritméticas 

27 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

complejas como constantes y operaciones de almacenamiento. Esta máquina, alimentada por un motor a vapor, es considerada como el primer diseño completo de un sistema de cómputo artificial en la historia, pero lamentablemente no pudo ser construida jamás dadas las limitaciones de fabricación existentes en el S.XIX. 

A pesar de ello, esta creación llamó la atención de la matemática y escritora británica Ada Lovelace que en la traducción que realizó de los trabajos de Babbage incluyó un anexo en el que postuló por primera vez el concepto de “programa de ordenador” en el año 1843. Según la propuesta de Ada Lovelace, programar un ordenador, reduciéndolo a su esencia, no es más que proporcionarle una serie de instrucciones que debe ejecutar de forma matemáticamente precisa para obtener un resultado según los datos que reciba de entrada. Es decir, aunar los dos conceptos más importantes en el desarrollo de esta tecnología: ejecutar un algoritmo sobre una computadora artificial. 

En su descripción, Ada Lovelace realizó un trabajo minucioso de detalle acerca de cómo la información contenida en las tarjetas perforadas iba generando distintas operaciones en la máquina analítica hasta llegar a su resultado. Para mostrarlo a través de un ejemplo, desarrolló un algoritmo para esta máquina que permitía calcular los números de Bernoulli a través de tarjetas perforadas. 

Este conjunto de tarjetas es considerado como las primeras líneas de código escritas en la historia, el primer algoritmo que fue desarrollado para su ejecución en una computadora. Es por este hito en la historia que a día de hoy se considera a Ada Lovelace la primera programadora, y por el que se desarrolló el lenguaje “Ada” como homenaje a su persona. 

En 1936, Alan Turing definió de forma teórica su máquina de Turing. Esta máquina teórica sentó las bases de lo que sería el cómputo mecánico y electrónico durante el S. XX. Su funcionamiento permitía realizar cualquier proceso computacional a través de un dispositivo hipotético que manipulaba símbolos sobre una cinta de acuerdo con una serie de normas previamente definidas. Este sería el objetivo de los futuros diseñadores de computadoras. Un sistema que leyera datos de un soporte de entrada, los manipulara según un conjunto de reglas y produjera resultados en el menor tiempo posible. 

Dos años más tarde, en 1938 el ingeniero alemán Konrad Zuse presentó la primera computadora considerada completa, que fue denominada Z1. Funcionaba a base de relés electromecánicos de centralita telefónica para realizar sus operaciones y pesaba cerca de una tonelada. Estaba basada en un sistema binario, sentando el precedente de todos los sistemas de cómputo actuales y lógica booleana (para más información sobre la lógica booleana ver _Boolean Algebra and Its Applications_ publicado por _Dover Books_ ). Inspirado por las tarjetas perforadas originales de Babbage, empleó este soporte como sistema de almacenamiento e intercambio de información. Su programación estaba limitada a una serie de instrucciones muy concretas. No sería hasta el desarrollo de la tercera iteración de este sistema, la máquina denominada Z3, cuando Zuse obtuvo una computadora programable sin limitaciones y completamente automática. Estas máquinas fueron los comienzos de la **primera generación de computadoras.** 

28 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Estas dos características son actualmente las empleadas para definir una computadora, por lo que la Z3 es el ancestro común de todas las que se desarrollaron posteriormente. 

En 1944 se suceden dos hitos de la historia del diseño y construcción de las computadoras. Por una parte, la empresa IBM desarrolla la computadora electromecánica Harvard Mark I, la primera de estas características construida en Estados Unidos. En paralelo, El Reino Unido construye los ordenadores Colossus I y II con ayuda de Alan Turing para descifrar los mensajes encriptados que la Alemania Nazi se enviaba durante la Segunda Guerra Mundial. 

Hasta este momento todas las computadoras estaban compuestas por sistemas electromecánicos. Eran máquinas con piezas móviles como válvulas y relés que, gracias a la electricidad, podían desplazarse y realizar operaciones, así como almacenar información. Esto cambió radicalmente con la invención del transistor en 1947. Los transistores son pequeños dispositivos electrónicos que devuelven una determinada señal eléctrica en función de las señales que reciben. Esto permite que lo analógico pase a ser digital, ya que a partir de este momento las instrucciones y operaciones dejan de realizarse sobre relés móviles, para pasar a ser ejecutadas sobre pequeños dispositivos electrónicos. Los unos y los ceros ya no son objetos en distintas posiciones, sino cargas eléctricas a través de transistores. 

Gracias a los transistores surge la **segunda generación de computadoras** , de las que la IBM 650 es la primera representante con fecha de salida en 1953. La gran diferencia de esta máquina con sus predecesoras es que abandona el uso de relés y válvulas para usar placas de circuito impreso basadas en transistores. Este ordenador fue el primero en venderse a gran escala en el mundo. 

La **tercera generación de computadoras** surge con el paso de los circuitos impresos a los circuitos integrados, también llamados chips. A partir del IBM S/360, primer sistema comercial basado en chips, aparecen los ordenadores de uso comercial en el año 1964. La empresa de máquinas de escribir Olivetti presenta el primer ordenador de escritorio en 1965. 

A partir de la notable invención del primer microprocesador de Intel en 1971 y de la fundación de Microsoft en 1975 y Apple en 1976, y sus grandes éxitos MS-DOS y Apple II respectivamente, surge la era actual de las computadoras. En la actualidad las computadoras están todas regidas por un mismo patrón heredado de todas las computadoras de las que hemos hablado hasta el momento. Toda computadora está compuesta por chips basados en transistores, su unidad central de procesamiento o CPU es un microprocesador, tiene soportes de memoria, periféricos de entrada y salida y buses de datos. Además, todas son programables y automáticas. 

29 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

A partir de este momento, el _hardware_ de las computadoras empieza a mejorar año tras año sobre la misma base de diseño, dando una gran oportunidad al mundo del _software_ de recuperar terreno. En la década de los noventa del S. XX, Linus Torvald presenta el Núcleo de Sistema Operativo Linux, que abriría las puertas del software libre para el mundo de la computación, permitiendo a los investigadores y usuarios tener diversos sistemas operativos de código abierto pudiendo así acabar con su dependencia de Microsoft y Apple. 

También en esta década se populariza la programación orientada a objetos. Este tipo de programación, como veremos más adelante, incorporaría conceptos desarrollados por el campo de la IA décadas antes, y permitiría escribir programas informáticos con una gran orientación a negocio además de orientadas a una interfaz gráfica, algo que a partir de este momento sería esencial. Lenguajes como C++ y Eiffel, que posteriormente sería Java, surgieron para quedarse en el entorno del desarrollo para aplicaciones industriales, generalizando este tipo de aplicaciones a lo largo de todos los sectores económicos y democratizando los desarrollos ad-hoc en las distintas empresas. 

Durante los años noventa Microsoft sacaría su primer sistema operativo con soporte para múltiples usuarios, Windows NT en 1993 y tan solo dos años después Windows 95 que emplearía por primera vez en la historia un navegador gráfico integrado, el conocido Internet Explorer. Por su parte Apple presentaría el Mac OS 9 en 1999 con uno de los buscadores más potentes del momento, Sherlock 2, y tan solo un año después el Mac OS X que marcaría el inicio de los sistemas operativos de nueva generación de Apple. 

A partir de la unificación de la gran mayoría de usuarios bajo el paraguas de Windows, Linux y Mac OS, comienzan a aparecer tecnologías de bases de datos, páginas y servidores web como SQL, HTML y Apache respectivamente, que unificarían el almacenamiento de datos y la creación de páginas web a lo largo de la gran mayoría de empresas de desarrollo, permitiendo así una gran interoperabilidad de sistemas. 

En 1993 se funda una de las empresas más relevantes en el mundo de la Inteligencia Artificial en la actualidad, con ninguna intención de serlo originalmente: NVIDIA. Desde California crearon su primer producto, NVIDIA NV1, una tarjeta para el renderizado de texturas en 3D. A partir de la siguiente generación, las NVIDIA NV2 se empezó a emplear la nomenclatura GeForce para las tarjetas gráficas de NVIDIA. En la siguiente sección estudiaremos la enorme influencia que han tenido las GPU de NVIDIA en el desarrollo de la Inteligencia Artificial y, en concreto, del _Deep Learning._ 

Con la creación de grandes empresas tecnológicas como Yahoo!, Google, Mozillla y Hotmail se siembran las semillas de lo que posteriormente serían parte de grandes grupos privados de investigación en Inteligencia Artificial, además de generar productos de consumo como los navegadores web abiertos o los servicios de correo electrónico que modelarían el futuro. 

30 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Durante el S XXI el crecimiento de la computación es exponencial. Comienzan a aparecer supercomputadores a lo largo del mundo como el Earth Simulator en 2002, el MareNostrum en 2005, o el IBM Roadrunner el primer ordenador el superar el PetaFLOP, es decir, 1015 operaciones por segundo. También surgen las video-consolas, los servicios de alojamiento de imágenes y videos, y las redes sociales. 

En cuanto a hardware, destacan como novedades la aparición de las PDAs en los primeros años de siglo XXI y algo más tarde, con la presentación del iPhone en 2007, el surgimiento la era de los dispositivos móviles y en última instancia de IoT (internet of Things) que continúa su avance a día de hoy entre _smartphones_ , _tablets_ , convertibles y consolas portátiles, pero también en prendas de ropa conectadas y relojes inteligentes. 

Esta breve cronología desde principios del primer milenio hasta la actualidad es esencial para contextualizar qué ha sido y cómo ha evolucionado la programación informática desde su concepción hasta hace escasos años. Desde la idea inicial de al-Juarismi, hasta la descripción teórica de Ada Lovelace y las primeras ejecuciones de algoritmos en las máquinas Z de Zuse, en las masivas computadoras de IBM de mitad de S. XX y en los PDA de principios de siglo, los programas informáticos han tenido una característica principal en su gran mayoría: no han sido inteligentes. 

Ya hemos analizado qué es la inteligencia y por tanto qué es la inteligencia artificial. En esta historia acelerada de la computación hemos sentado las bases de lo posible. La fuerza bruta necesaria para computar la inteligencia. Las tripas y recovecos de las máquinas y algoritmos hasta nuestros días, cómo los superconductores nos han permitido automatizar procesos con gran eficiencia. En definitiva, conocemos el soporte sobre el cual se pueden ejecutar complejos programas informáticos y la evolución que ha seguido a lo largo de los años. Pero ¿en qué momento alguien se planteó desarrollar un sistema inteligente que funcionara sobre estas computadoras? ¿cuándo se consiguió por primera vez? ¿ha evolucionado la capacidad de los sistemas de IA junto a la capacidad de cómputo del hardware en el que las ejecutamos? ¿hacia dónde caminan hardware y software en el mundo de la Inteligencia Artificial? 

Para responder a todas estas preguntas, analizaremos con detalle los hechos más destacados en la historia de los sistemas inteligentes artificiales. 

### **2.2. Cronología de la Inteligencia Artificial** 

La historia de la Inteligencia Artificial no ha ido siempre ligada al desarrollo de la tecnología y arquitectura de computadores. Antes de la existencia de grandes servidores que leían y escribían en tarjetas perforadas, grandes mentes de diversas disciplinas científicas teorizaban sobre la capacidad del humano de generar mentes artificiales, sin interesarles en exceso el soporte sobre el que podrían llegar a ejecutarse en un lejano futuro. Una vez surgieron los computadores, se darían situaciones en las que el crecimiento exponencial de ideas y teorías en IA no se verían seguidos por los avances necesarios en computación, 

31 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

lo que supondría divergencias entre la teoría y la práctica. Como todo campo científico, es necesario que la investigación básica en matemáticas, física y biología sienten un precedente de investigación que siente las bases de un conocimiento abstracto para su posterior empleo en el desarrollo de teorías específicas y de desarrollos aplicados concretos como son los sistemas inteligentes. Siglos antes de que el término Inteligencia Artificial fuera acuñado, números matemáticos, físicos y biólogos contribuirían a los ancestros de la IA, sin los que a día de hoy esta disciplina no habría llegado hasta el punto en el que está. 

### **Etapa 0. Los ancestros: matemáticas y neurociencia.** 

Ya hemos comentado la importancia que tuvieron los filósofos del mundo antiguo en las primeras formalizaciones del razonamiento en forma de lógica. Algunos de los ejemplos más destacados son los silogismos de Aristóteles, el razonamiento formal de Euclides o los algoritmos de al-Juarismi. No obstante, el propósito de estos desarrollos no fue en ningún caso la creación ni propuesta de un razonamiento artificial, sino que perseguían la descripción formal del proceso de razonamiento que llevamos a cabo los seres humanos cuando nos enfrentamos a problemas de toda índole, como mero ejercicio de observación y definición filosófico y matemático, jamás orientándolo hacia una ejecución artificial o no biológica. 

La historia del razonamiento artificial definido como tal comienza en la Edad Media, en concreto en el **S XIV.** En una publicación de 1315 titulada Ars Magna, el filósofo español Ramon Llull expuso una de las ideas más revolucionarias que sugeriría en su vida: la máquina lógica, también llamada máquina de pensar. Esta máquina tenía como finalidad deducir la verdad. Para ello, este constructo empleaba en su diseño una serie de discos concéntricos de papel que trataban de resumir todo el conocimiento de lógica combinatoria conocido hasta entonces. La lógica combinatoria es un conjunto de reglas que permiten computar resultados a través de entradas como, por ejemplo, las funciones de adición (AND) o de exclusión (XOR). Permitían introducir un sujeto, predicado e hipótesis y por medio de una serie de poleas y palancas la máquina computaba si la hipótesis era verdadera o falsa en base a una serie de operaciones combinatorias del tipo ya descrito. Este desarrollo fue el primer ejemplo tangible de una máquina capaz de razonar fuera de un cerebro humano. Aunque sus usos fueran limitados, supuso un gran hito en el futuro desarrollo del razonamiento artificial ya que supuso el primer intento de que una serie de razonamientos se ejecutaran sin una base biológica, sin vida. Con papel, cuerdas, poleas y palancas cualquiera podía computar hipótesis, aunque no tuviera ni un remoto conocimiento de las aplicaciones de la lógica combinatoria. 

#### **_Dato importante_** 

_En el S.XIV, Ramon Llull expuso una de las ideas más revolucionarias: la máquina lógica o máquina de pensar_ 

32 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 



Ars Magna. Máquina lógica. Imagen de dominio público 

Continuando en el terreno de lo filosófico y lo matemático, ya en la Edad Moderna, en el **S. XVII** grandes pensadores como Thomas Hobbes, René Descartes y Gottfried Leibniz estaban inmersos en una exploración acerca de las posibilidades de definir de forma científica el razonamiento humano por medio de procesos describibles y objetivos para así poder abstraerse del cerebro humano a la hora de llegar a postulados y conclusiones lógicas. 

Para hacer esto trataron de crear un lenguaje común para el razonamiento, y así convertirlo en una rama más de las matemáticas formales. Esta fue su gran contribución a la Inteligencia Artificial. Propusieron los primeros sistemas de símbolos físicos, o sistemas formales, que permitían llegar a expresiones nuevas a través de la manipulación de una serie de símbolos de entrada. Para hacernos una idea, todos los símbolos matemáticos y lógicos en una ecuación, en una serie o en una sucesión, son símbolos físicos con los que se puede operar para llegar a conclusiones como por ejemplo hallar el resultado de una integral o comprobar si un cierto predicado expresado en términos de la lógica formal es verdadero o falso. Esta idea es la que posteriormente moverá con mayor fuerza el campo de la Inteligencia Artificial durante décadas. En analogía con el pensamiento humano, en un cerebro los símbolos son la información almacenada en nuestro cerebro y al manipularlos mediante los procesos internos de reflexión se llegan a pensamientos y conclusiones. Por su parte, en la IA los símbolos son los datos de entrada, la manipulación de estos son los algoritmos que procesan los datos y las conclusiones son datos agregados y abstractos a los que llega la IA como resultado de su “reflexión”. 

33 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Leibniz definió un lenguaje formal de este tipo de nombre characteristica universalis, o lenguaje universal. Defendía un lenguaje basado en símbolos pictográficos, a diferencia de la actualidad, que representaban la tierra, el agua, el fuego y el aire. Estos símbolos se combinaban para obtener la lógica del origen de cada uno de ellos sobre un disco realmente similar al que propuso Ramón Lull siglos atrás, en el que se podía realizar una serie de operaciones lógicas para obtener resultados. La innovación residía en el uso de símbolos físicos para resumir información. De esta manera, el razonamiento artificial estaba un paso más cerca del razonamiento humano. Era capaz de emplear información abstracta para operar con ella y llegar a conclusiones. 



Characteristica Universalis. 

Durante la transición a la Edad Contemporánea, en el S XVIII, la contribución más notable a la discusión sobre el razonamiento artificial fue realizada por Thomas Bayes, un ilustre matemático británico. La lógica bayesiana o inferencia bayesiana que desarrolló y publicó en 1763, es uno de los métodos más usados a día de hoy en modelos de machine Learning, casi trescientos años después. Bayes desarrolló un método matemático para el razonamiento formal sobre la probabilidad de que ocurran sucesos, que recibió posteriormente el nombre de teorema de Bayes. Su enorme relevancia surge porque fue el primero en proponer un método que calculara la probabilidad de un suceso A dado B relacionándola con la probabilidad del suceso B dado A. Su enorme potencia de cálculo de probabilidades matemáticas permitió en el futuro el diseño de procesos que tomaran decisiones de manera autónoma en función de probabilidades calculadas para un par sucesos. 

Profundizaremos en los métodos fundacionales del aprendizaje automático en futuros módulos, lo que nos ayudará a comprender la gran influencia ejercida por Bayes en el desarrollo actual de algoritmos inteligentes. 

34 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 



Si bien este conjunto de métodos bayesianos aún era ejecutado sobre mentes humanas, el ser humano que aplicaba la lógica bayesiana no era el diseñador del cálculo, tan solo el motor. Se trataba de un razonamiento artificial sobre un hardware biológico. 

Hasta este punto, por tanto, había una serie de métodos y máquinas que permitían un razonamiento objetivo por medio de métodos estandarizados a través de la lógica formal y del cálculo probabilístico para que la toma de una decisión pudiera ser externalizada de las emociones y razonamientos de un cerebro humano y fueran lo más “puras” posibles. 

Pero el estudio de este imperfecto sistema biológico que compone el cerebro humano fue otro de los asombrosos descubrimientos gracias a los cuales la ciencia básica ayudaría a despegar a la Inteligencia Artificial. 

El impulso principal del conocimiento de cerebro durante principios de siglo XX ayudaría de forma notable al desarrollo de posteriores modelos y propuestas de sistemas inteligentes que veremos más adelante. Grandes avances fueron proporcionados al mundo por dos galardonados con el premio Nobel de Medicina llamados Santiago Ramón y Cajal, y Charles Scott Sherrington. Uno de los descubrimientos principales de estos dos eminentes doctores fue la observación y descripción detallada del funcionamiento y estructura del sistema nervioso y, más específicamente, la observación de la neurona como unidad estructural y funcional del mismo. Sus estudios demostraron que las neuronas de nuestro sistema nervioso reciben una serie de impulsos químicos y eléctricos que son procesados en su interior y generan un impulso de salida que se comunica al resto de las neuronas circundantes. Esta idea sería recuperada décadas más tarde para plantear por primera vez las precursoras de las hoy omnipresentes redes neuronales artificiales. 

Todos estos avances en matemáticas, cálculo, ingeniería, lógica formal e incluso neurociencia, unidas al emergente campo de las computadoras artificiales formaron la combinación de ingredientes perfecta para permitir el estallido de la tecnología que hemos estado analizando desde el principio de este módulo: la Inteligencia Artificial. 

### **Etapa 1. Propuesta teórica y primeros pasos 1940 – 1959** 

En **1943** la neurociencia y la ciencia de computadores se unieron en la primera y brillante idea que guiaría el futuro de la IA y que sigue siendo esencial en nuestros días. El neuropsicólogo Warren McCullough y el matemático Walter Pits publicaron un artículo científico titulado _“A Logical Calculus of Ideas Immanent in Nervous Activity”_ , en español “Cálculo lógico de ideas inmanentes a la actividad nerviosa “. 

35 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

En este histórico artículo, ambos científicos se basaron en los descubrimientos de la estructura del cerebro y el sistema nervioso para teorizar sobre una posible “neurona artificial” simplificada que podría realizar funciones lógicas para llevar a cabo cómputos complejos. Su propuesta sostenía que mediante una red finita de neuronas artificiales simulando un cerebro humano, una máquina podría ejecutar las tareas más complejas. Esta idea de construir una red neuronal artificial sustituyendo las neuronas reales de las redes neuronales biológicas por meras operaciones lógicas que recibían entradas y producían salidas tienen una gran influencia en absolutamente todos los desarrollos históricos y actuales en el campo del _Deep Learning_ . Posteriormente, ambos científicos trabajaron en la definición formal de estas redes neuronales para su posterior desarrollo, momento que ninguno de los dos presenció. 

En **1950** , como ya hemos descrito anteriormente, Alan Turing, considerado padre de la informática, presentó su Test de Turing para valorar si un sistema era inteligente artificialmente e indistinguible de un humano manteniendo una conversación. 

A partir de este momento, los tres ingredientes principales para el desarrollo de la Inteligencia Artificial se habían dado. Por un lado, los primeros computadores permitían la ejecución de complejos cálculos en cuestión de minutos y sin esfuerzo humano. Por otro, existía un camino que seguir tras la propuesta de las redes neuronales artificiales. Y, por último, había una vara de medir; un sistema por el cual decidir si los algoritmos desarrollados eran realmente inteligentes según Alan Turing. 

Con todos estos elementos y en **1950** , Marvin Minsky, discípulo de Pitts y McCulloch decidió desarrollar de forma práctica la teoría que sus maestros habían propuesto. Junto a su compañero Dean Edmons, desarrolló el primer computador basado en redes neuronales de la historia. El SNARC ( _Stochastic Neural Analog Reinforcement Calculator_ ) era una máquina neuronal con 40 neuronas artificiales primitivas que, lejos de ser líneas de código como en la actualidad, eran capacitores electrónicos. La máquina era capaz de aprender automáticamente a realizar funciones sencillas por medio de un sistema de refuerzo ( _Reinforcement_ ). Cada vez que acertaba en la ejecución de sus objetivos, recibía un refuerzo positivo y de manera opuesta cuando su cómputo era erróneo. Este refuerzo modificaba el comportamiento de cada neurona de la máquina para tratar de mejorar en cada ejecución. Como veremos, esta es la base de todo el desarrollo, más de medio siglo después, del campo denominado _Deep Learning_ o aprendizaje profundo. La SNARC está considerada como uno de los primeros intentos pioneros de ejecutar en la práctica las teorías de Inteligencia Artificial. 

El siguiente intento reseñable de obtener un sistema inteligente lo llevó a cabo el ingeniero Arthur Samuel en **1952** . Desarrolló uno de los primeros programas capaces de aprender por si solos, y lo hizo con un propósito que se mantendría en el deseo de la gran mayoría de científicos de IA: jugar al ajedrez. Su “ _Checkers-playing Program”_ , un programa que jugaba al ajedrez fue uno de los primeros ejemplos reales del campo del Machine Learning. Esta máquina estaba compuesta por un árbol de búsqueda, que cal- 

36 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

culaba posibles situaciones en la partida y que elegía el movimiento que otorgaba una mayor probabilidad de ganar. Para ello, empleaba un algoritmo basado en el número y tipo de piezas del oponente. Para que el programa pudiera mejorar, de forma posterior a la partida se repasaban los cálculos realizados y se comparaban con los resultados reales. De igual forma que la SNARC, a mejores cálculos más refuerzo positivo recibía el algoritmo en forma de persistencia en el comportamiento. En caso de peores cálculos, el algoritmo modificaba su cálculo de la probabilidad para tratar de mejorar en siguientes partidas. Tras numerosas partidas jugadas, logró convertirse en un jugador de ajedrez que podía imitar a la perfección el comportamiento de un aficionado. 

De manera sorprendente, el concepto Inteligencia Artificial no fue mencionado en ninguno de estos experimentos. Se trataba de “agentes con capacidad de aprendizaje” o “redes neuronales” pero jamás se mencionó el concepto de IA. 

En **1956** Martin Minsky y John McCarthy, de los que ya hemos hablado, convocaron un taller de verano en Dartmouth llamado _“Dartmouth Summer Research Project on Artificial Intelligence”_ empleando por primera vez este término en público. En esta convención se definió por primera vez el campo científico de la Inteligencia Artificial. Se trató de dar una primera descripción, que ya hemos analizado, pero también una misión. Se considera este momento como el nacimiento definitivo del campo de la IA. 

En los años posteriores a la conferencia de Dartmouth se consiguieron enormes avances en las capacidades de la IA en tan solo unos pocos años. Empezaron a aparecer máquinas capaces de resolver problemas de álgebra, de demostrar teoremas geométricos e, incluso, de traducir ciertas frases cuidadosamente seleccionadas del ruso al inglés. Estos computadores estaban basados en técnicas muy específicas para cada uno de los problemas que traban de afrontar, con aproximaciones más parecidas a los árboles de decisión de Arthur Samuel que a las redes neuronales de Pitts, McCulloch y posteriormente Minsky, que quedaron como curiosidad sin una aplicación específica. 

No obstante, la aproximación de una sinapsis artificial cobró fuerza cuando en **1958** , el psicólogo estadounidense Frank Rosenblatt recuperó la posibilidad de definir una estructura matemática que mimetizara el comportamiento de una neurona humana para ejecutar cálculos complejos tal y como los hace el cerebro. En este caso, esta neurona artificial fue bautizada como Perceptrón. Rosenblatt también imaginó sumar múltiples unidades de estos perceptrones, construyendo una red de perceptrones compleja. La diferencia con las neuronas artificiales originales residía en que estas nuevas neuronas artificiales no eran componentes electromecánicos, sino estructuras matemáticas. 

Esta diferencia marcaría la gran diferencia en la aproximación de Rosenblatt. Definió el perceptrón como una estructura que recibiría una serie de señales de entrada, las procesaría a través de una función de activación y generaría una única señal de salida. 

37 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 

Este es exactamente el funcionamiento de una neurona humana. Cada neurona está conectada a otro gran número de neuronas por medio de las dendritas, de donde recibe información. Una vez la procesa y genera una señal de salida, la transmite a través del axón para su propagación por las distintas redes neuronales del cerebro. 



El perceptrón de Rosenblatt trata de ejecutar una función similar por medio de estructuras matemáticas. Una serie de entradas a la neurona (x0, x1, …, xn) proporcionarían información que sería primero ponderada, es decir, priorizada, por medio de una serie de pesos o “weights” que multiplicarían la señal por un número comprendido entre cero y uno (w0, w1, …, wn). 

Una vez multiplicada cada entrada por su peso específico, se realizaría un sumatorio de las entradas ( Σ = x1·w1 + x2·w2 + … xn·wn). 

Con este sumatorio se ejecutaría una función de activación ( φ ). Una función de activación es una función matemática que genera como salida un 0 (apagado) o un 1 (encendido) como respuesta a la entrada que recibe. Una vez computada la salida, la neurona se la transmite a las entradas de otras neuronas, componiendo así la denominada red neuronal. 

Para construir una red neuronal con este tipo de neuronas sería suficiente con que la salida de cada neurona fuera la entrada de otras neuronas para así construir información compleja que se fuera propagando hacia delante, como se puede observar en la siguiente imagen. Las capas podrían ser de entrada ( _input_ ), ocultas o en el medio ( _hidden_ ) y de salida ( _output_ ) 



38 

**Módulo. Introducción a la Inteligencia Artificial** 

Estas primeras neuronas matemáticas o perceptrones fueron simuladas en una computadora de IBM llamada IBM 704, una de las primeras computadoras capaces de realizar cálculos complejos. 

Marvin Minsky, constructor de la primera máquina de IA basada en neuronas artificiales estuvo en contra de esta propuesta desde el principio.  Minsky y Rosenblatt se conocieron durante la adolescencia, y fueron protagonistas de uno de los mayores debates en el campo de la IA en el S XX. Tanto fue así que Minsky escribió un libro directamente dirigido a Frank Rosenblatt titulado “ _Perceptrons_ ”. La idea original del libro era analizar los perceptrones desde un punto de vista matemático, evaluando sus puntos fuertes, así como los débiles. Sin embargo, posteriormente se ha analizado que los postulados de Minsky en su libro estaban claramente sesgados para desmontar la teoría del perceptrón, afirmando que las redes neuronales de perceptrones serían incapaces de resolver una serie de problemas básicos como el reconocimiento de patrones, para lo que empleaban directamente la portada de su libro tratando de demostrar que “hasta para un ser humano ciertos reconocimientos son complejos”. En definitiva, criticaba la aproximación biológica a la IA, considerando un gran error basarse en la estructura de nuestro cerebro para tratar de enseñar a realizar tareas complejas a máquinas que nada tenían que ver con nuestras estructuras. Más adelante comprobaremos los efectos devastadores del pesimismo de Minsky en el desarrollo de la IA en las últimas décadas de siglo. 

El compañero de Minsky en la conferencia de Dartmouth, John McCarthy, desarrolló durante la época de los 50 el primer lenguaje de programación orientado a la IA llamado Lisp. Fue presentado en **1958** y en el artículo en el que se describe McCarthy propuso un sistema de IA completo con la habilidad de aprender de la experiencia tal y como lo hacen los humanos. Lisp es el segundo lenguaje de programación con mayor antigüedad, solo por detrás de FORTRAN. 

En **1959** , Allen Newell, Herbert Simon y J.C. Shaw desarrollaron el GPS, _General Problem Solver,_ que trataba de resolver problemas de igual forma que los humanos, un objetivo recurrente en estos primeros años de investigación de IA. 

39 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

En la presentación, Newell y Simon afirmaron con gran optimismo que “en diez años de distancia una computadora digital será la campeona mundial de ajedrez”. Serían necesarios casi 40 para que esta predicción se convirtiera en una realidad. 

En este mismo año, John McCarthy y Marvin Minsky iniciaron el Proyecto Inteligencia Artificial en el MIT, que sigue operativo a día de hoy con el objetivo de centralizar las actividades de investigación y desarrollo en el campo del razonamiento artificial y la Inteligencia Artificial en Estados unidos. 

Durante las décadas de 1940 y 1950, en resumen, la IA comenzó a tomar forma más allá de la teoría, y comenzó a dar frutos, aunque su utilidad todavía no quedaba clara. Se definió y perfiló el campo de estudio específico y se dieron los primeros pasos hacia modelos de autoaprendizaje y solución inteligente de problemas. 

#### **_Dato importante_** 

**_1943_** _– Primera propuesta de neurona artificial por Pitts y McCulloch_ 

**_1950_** _– Minsky presenta el SNARC, primera máquina basada en redes neuronales con capacidad de resolución de problemas_ 

_1952 – El primer jugador de ajedrez artificial con nivel amateur, con posibilidad de mejorar su desempeño por medio de autoaprendizaje_ 

**_1956_** _– Nace oficialmente la IA en la conferencia llamada “Dartmouth Summer Research Project on Artificial Intelligence”_ 

**_1958_** _– Rosenblatt propone los perceptrones y los prueba en una máquina de IBM_ 

_John McCarthy presenta LISP, primer lenguaje de programación para IA y segundo en el mundo_ 

**_1959_** _– Se presenta el General Problem Solver_ 

_McCarthy y Minsky fundan el Proyecto de IA en el MIT_ 

40 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

### **Etapa 2. El primer invierno de la IA 1960 – 1979** 

Las siguientes dos décadas comenzarían con el optimismo con el que terminó el periodo anterior, pero con unas posibilidades de financiación mucho mayores. 

Gracias a la creación de ARPA ( _Advanced Research Project Agency_ ) que sería la creadora de Internet, posteriormente conocida como DARPA, la financiación que recibieron las universidades americanas para proyectos de investigación tecnológica creció cifras como los 2,2 millones de dólares que recibió el MIT. Esto dio un empuje económico al grupo de McCarthy y Minsky en 1959, pero también permitió que McCarthy emprendiera nuevos proyectos para seguir investigando y desarrollando IA. 

A principios de década, en **1961** , James Slagle, desarrolla SAINT ( _Symbolic Automatic INTegrator_ ) un programa informático basado en heurísticas para resolver integrales sencillas en el campo del cálculo. En el momento de su presentación se estimó que las capacidades de SAINT igualaban a las de un estudiante preuniversitario. Se considera SAINT como el primer sistema experto de la historia, marcando el comienzo de una serie de desarrollos en las décadas posteriores que marcarían el camino de la IA. 

En **1963** , McCarthy sale del MIT y funda el _Stanford AI Project_ , el laboratorio principal de investigación de IA en Stanford que sigue funcionando a día de hoy bajo el mando del profesor Chris Manning. Dos años más tarde, Donald Michie fundó el laboratorio de IA en la universidad de Edimburgo. Estos laboratorios serían el centro de investigación y desarrollo de IA durante muchos años, y siguen activos a día de hoy. 

En el laboratorio de IA en el MIT se desarrolló gracias a esta financiación en **1964** el primer programa informático de NLP (Natural Language Processing), es decir, de procesamiento del lenguaje natural. Lo bautizaron ELIZA. 

ELIZA era capaz de mantener conversaciones con seres humanos simulando, por ejemplo, ser un tipo de psicoterapeuta bastante particular con su modo DOCTOR en el que era capaz de mantener conversaciones trascendentales sobre el ser humano y su existencia. Aunque en una primera instancia podía parecer que esta máquina era, en efecto, capaz de comprender el lenguaje humano, la realidad es fue creada para tratar de demostrar la simpleza y superficialidad de la comunicación entre humanos, y, por tanto, sus respuestas eran una ilusión que sencillamente reordenaba las preguntas del interlocutor y cambiaban ligeramente la sintaxis para que pareciera que había comprensión. La realidad es que su software estaba meramente basado en un reconocimiento de patrones básico en el que se identificaban palabras clave y contextos básicos para ser capaz de responder de forma mínimamente coherente. Aunque el propósito no fuera ese, gran cantidad de gente consideró a ELIZA una máquina inteligente y capaz de comprender conversaciones, aunque su creador, Joseph Weizenbaum insistía en lo contrario. 

41 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

En futuros módulos exploraremos el campo del NLP, que comenzó con un intento de crítica por parte de Weizenbaum y actualmente se ha convertido en uno de los campos más destacados dentro de la Inteligencia Artificial. 

Este mismo año, **1964** , el ingeniero informático Daniel Bobrow presentó STUDENT. Este programa, igual que SAINT, podría resolver problemas de álgebra y cálculo sencillos pero su gran avance consitió en incorporar procesamiento del lenguaje natural ya que era capaz de comprender enunciados escritos en libros de texto de álgebra y proporcionar directamente un número como resultado. En este caso también estamos frente a un sistema experto, que se considera como el primer sistema exitoso de procesamiento del lenguaje natural en el campo de la IA. 

Dos años más tarde, en **1966** , se propuso el primer sistema primitivo para el reconocimiento facial. Woody Bledsoe, Helen Chan Wolf y Charles Bisson trabajaron en poder emplear un computador para conseguir reconocer caras de seres humanos. Este primer proyecto pionero para reconocimiento facial era un sistema mixto, es decir, no era totalmente autónomo (en terminología científica esto es denominado un sistema “man-machine”). Este sistema requería que las coordenadas de las características faciales clave como la boca, los ojos, la nariz, las cejas, las orejas, etc, fueran introducidas manualmente por un ser humano a través de un computador. Con una tableta gráfica, el operador tenía que seleccionar las coordenadas de cada una de estas características para poder generar un perfil numérico de las características de esta cara. Gracias a estas coordenadas, el sistema calculaba más de veinte distancias entre ellas, por ejemplo el ancho de la boca, el de los ojos o la distancia entre las orejas. Gracias a este sistema un operador humano podía llegar a procesar hasta cuarenta imágenes faciales en una hora, o que permitió crear la primera base de datos masiva orientada al reconocimiento facial de criminales reincidentes. La tarea del ordenador era, una vez marcadas las coordenadas y calculadas las distancias de interés, poder determinar si la fotografía tenía suficiente similitud con otra de su base de datos como para afirmar que esa persona era exactamente un humano previamente registrado. Con este trabajo se inició la era del reconocimiento facial, hoy en día extendido por aeropuertos, sistemas de vigilancia incluso para las etiquetas automáticas en Facebook. No obstante, aún quedarían algunas décadas hasta que estos sistemas pudieran ser real y totalmente autónomos, sin necesidad de interacción humana para su funcionamiento. 

En **1969** se presentó DENDRAL. Este programa, del que ya hemos hablado en la unidad anterior, fue el primer ejemplo de agente experto que se comercializó e implantó con éxito, ya que sus predecesores SAINT y STUDENT fueron meras curiosidades académicas sin aplicación empresarial real. Fue un gran éxito a pesar de que contaba con numerosas limitaciones como la falta de capacidad para aprender de la experiencia y la aplicación excesivamente estricta de la lógica formal. Fue este momento en el que comenzó la era dorada de los agentes expertos que, por sorprendente que parezca, siguen vigentes a día de hoy en forma de algunos agentes conversacionales en sitios web, y para la resolución de cálculos mecánicos en los que no hay incertidumbre ni necesidad de actualizar el comportamiento en cada experimento. 

42 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Hasta este momento, el dinero procedente de ARPA no tenía excesivo seguimiento ni control, y se concedía a aquellas mentes consideradas como las más aptas para el desarrollo tecnológico sin realizar una medición de retorno de la inversión ni de impacto de las investigaciones. 

Sin embargo, en **1966** comenzó un cabio de opinión gubernamental que acabaría provocando, por una serie de factores que serán analizados a continuación, el denominado “Invierno de la IA”. En este año el Comité para el Asesoramiento del Procesamiento de Lenguaje Automático (ALPAC) llamó la atención del gobierno de los Estados Unidos sobre la falta de avances reales en el campo de la investigación de la traducción automática entre idiomas. El gobierno de los Estados Unidos decidió cerrar las líneas de financiación pública destinadas a la investigación de la traducción automática, lo que causaría un dominó de decisiones en los años siguientes. 

A finales de la década de los sesenta el optimismo relativo al futuro y posibilidades de la IA se encontró con la realidad del desarrollo tecnológico del momento. Como hemos visto en la sección anterior, en 1970 todavía no se había presentado si quiera el primer microprocesador. La investigación de la Inteligencia Artificial iba más rápido que el desarrollo en ingeniería de computadores. Y esto pasó factura a las expectativas que el mundo había puesto en esta tecnología. 

El ejemplo más sonado fue Shakey el Robot, presentado en sociedad en **1969** . Shakey pretendía ser el primer robot desplazable de propósito general, con capacidad para tomar decisiones acerca de las acciones que debía realizar en base a un análisis pormenorizado de su entorno por medio de un gran número de sensores. Gracias a estos sensores, Shakey era capaz de construir un mapa espacial de lo que veía, para así poder tomar decisiones acerca de sus futuros movimientos. El mapa debía actualizarse a cada paso que daba lo que, debido a las capacidades computacionales de esta época, tomaba más tiempo del deseado por un robot. Aun así, era capaz de realizar movimientos si el entorno era estable y sencillo. Sin embargo, en cuanto un objeto se movía en su campo de visión, la cantidad de cálculos que debía realizar para tomar una decisión acerca de la dirección en la que moverse llevaba tanto tiempo que Shakey podía llegar a estar parado durante horas mientras planeaba su próximo movimiento. 

Este fracaso hizo patentes las limitaciones de la IA a finales de los sesenta, y llevó a numerosas voces a criticar las expectativas con las que se había presentado este robot y la escasa utilidad que podría llegar a tener en el mundo real, por muy controlado que estuviera el entorno. 

43 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 



A la izquierda una fotografía de Shakey el robot. A la derecha, un pantallazo de una conversación con ELIZA. 

La limitación de la capacidad de cómputo de unos ordenadores sin microprocesadores o con microprocesadores primitivos impedía la ejecución de algoritmos complejos que, por otro lado, llevaban planteados años en la teoría. El cuello de botella era la capacidad de los procesadores de esta época para ejecutar cálculos complejos. En aquel momento el supercomputador más potente del momento poseía la capacidad de realizar cerca de 100 operaciones por segundo, mientras que actualmente una aplicación de IA básica requiere cerca de 10000 operaciones por segundo (MIPS). La capacidad de cómputo era mil veces inferior que la requerida para que la IA pudiera convertirse en una realidad plausible. 

Por otro lado, en este momento la capacidad de almacenamiento de estos computadores originales era tremendamente limitada. Como hemos comentado y veremos en detalle más adelante, la Inteligencia Artificial necesita una gran cantidad de datos para funcionar correctamente y comprender el mundo, abstrayendo el conocimiento complejo y generando modelos flexibles y genéricos. Por tanto, no solo eran necesarios procesadores con capacidades de miles de operaciones por segundo, sino también soportes de almacenamiento que permitieran contener la información necesaria y suficiente para que la IA pudiera aprender de su experiencia. De hecho, no existían si quiera programas de gestión de bases de datos ni gestores de archivos como Windows o MacOS, por lo que, de nuevo, era la capacidad técnica la que frenaba el potencial desarrollo de la IA. 

Por último, como ya hemos mencionado en la unidad anterior, en este momento del desarrollo de la IA los investigadores empleaban principalmente sistemas basados en lógica formal. Como ya hemos mencionado, esto implicaba que estos sistemas no tienen en cuenta la realidad en conjunto de un problema, ya que solo reciben reglas de razonamiento e información a priori por lo que no son capaces de computar la incertidumbre ni de representar la realidad compleja que les rodea. 

44 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

No ayudó a la confianza de los gobiernos la publicación del libro Perceptrons de Marvin Minsky en **1969** en el que criticaba ferozmente las posibilidades de los perceptrones de Rosenblatt para cumplir objetivos como comprender imágenes o traducir idiomas. A partir de la publicación de este libro no se publicó ningún artículo sobre redes neuronales artificiales hasta más allá de una década. Teniendo en cuenta que esta es actualmente la tecnología base del Deep Learning no es aventurado afirmar que el libro de Minsky supuso un freno en seco al desarrollo de la IA durante una década. 

Pero las discrepancias no eran unidireccionales. Minsky, por su parte, estaba centrado en el desarrollo de la IA “ _scruffy_ ” o “desaliñada”. Esta aproximación está basada en una aproximación totalmente opuesta a la lógica formal en la que se asume que no es posible definir un problema de manera estricta y formal de igual manera que los seres humanos no lo hacemos así. ELIZA era un programa “scruffy” así como otros procesadores del lenguaje natural como SHRDLU. Estos sistemas trataban de definir los problemas de forma compleja y en algunos casos desordenada, tratando de imitar la manera en la que la mente humana almacena información y la procesa posteriormente. No tratan de definir el mundo con conceptos sino con cualquier sistema que funcione para que su agente inteligente realice correctamente su trabajo. Podría resumirse como una IA sin reglas frente a la IA formal o “ _neat_ ”. Esta aproximación fue también ampliamente criticada por los sectores centrados en la lógica formal y en descripciones exactas y precisas de la realidad como el laboratorio de Standford de McCarthy. 

Todos estos problemas y críticas cruzadas resultaron en una serie de informes devastadores de los principales gobiernos del mundo que frenaron el desarrollo de la IA durante un prolongado periodo de tiempo. Más allá del informe de ALPAC en 1966, el gobierno británico publicó en **1973** un informe denominado “Lighthill report” en el que analizaba el estado del arte de la IA en aquel momento concluyendo que los objetivos grandiosos que se habían propuesto los investigadores de este campo estaban fallando y que el optimismo de las décadas anteriores había demostrado ser exagerado y equivocado. Esto supuso una serie de graves recortes en la financiación de la IA por parte del gobierno británico. Durante este año y el siguiente DARPA decidió cancelar las becas destinadas a investigación de Inteligencia Artificial con una duración indeterminada debido a la falta de resultados concluyentes por parte de sus investigadores en el MIT y Standford entre otros.  A partir de **1974** comenzó el denominado como “El primer invierno de la IA” ya que era prácticamente imposible hallar fondos para investigar en esta disciplina. 

En **1972** surgió una de las pocas contribuciones duraderas a la IA durante esta década. El grupo de los desarrolladores de IA basada en razonamientos formales o “neat” liderados por McCarthy en el MIT y Kowalsky en Edimburgo obtuvo su primera victoria. Kowalsky en asociación con los investigadores de la universidad de Marsella Alain Colmerauer y Philippe Roussel presentó el lenguaje de programación PROLOG. Este lenguaje de programación fue el primer lenguaje declarativo del mundo y a día de hoy es el lenguaje declarativo más usado por los desarrolladores informáticos, principalmente empleado para el desarrollo de agentes expertos basados en lógica formal, que aún siguen vigentes en casos de uso que ya hemos comentado previamente. 

45 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Un lenguaje de programación declarativo funciona mediante una base de conocimiento que posteriormente se opera. La lógica se expresa en términos de relaciones y hechos entre distintas variables o términos, y una ejecución se inicia realizando una consulta a este conjunto de relaciones. 

Por ejemplo, en PROLOG se pueden definir entidades de tipo “animal” y de tipo “pájaro” e indicar al programa que “pájaro” es parte del conjunto “animal”. Por otro lado, podríamos indicar que “Piolín” es una instancia del tipo “pájaro”. Al preguntarle a PROLOG si “Piolín” es un animal, PROLOG responderá que SI. 

Este tipo de razonamientos sencillos pueden ser complicados todo lo necesario hasta conseguir obtener complejas bases de conocimiento sobre las que efectuar razonamientos y tomar decisiones, que serían la base de los sistemas inteligentes desarrollados por los grupos de IA “ _neat_ ”. No obstante, este tipo de recolección de relaciones lógicas entre las entidades de un sistema complejo y su posterior introducción en comandos de PROLOG para que este pueda razonar sobre ellos requiere una cantidad ingente de tiempo por parte de los desarrolladores. Además, como ya hemos comentado varias veces respecto a este tipo de IA, el gran problema que presenta es su falta de flexibilidad. PROLOG no genera conocimiento nuevo. Necesita conocer todas y cada una de las entidades de su mundo, así como las relaciones entre ellas, para poder operar. Si en el mundo real, por cualquier motivo, alguna de estas entidades o relaciones varía, entonces el código desarrollado perderá vigencia y habrá que actualizar el conocimiento manualmente. Como veremos, en las décadas posteriores se trató de solucionar este problema mediante el desarrollo de sistemas inteligentes con capacidad de aprendizaje y actualización autónoma de su representación interna del mundo. Sin embargo, en la década de los setenta este sería el estado del arte de la programación de sistemas inteligentes, permitiendo en los años posteriores desarrollos muy relevantes en esta disciplina. 

A parte de esta contribución al desarrollo de los lenguajes declarativos y de su impacto en el futuro de la IA, los últimos años de la década de los setenta no produjeron ningún avance significativo digno de mención en la investigación de la IA por los motivos ya expuestos. Los pocos grupos que sobrevivieron trataron de mantener un perfil mínimo mientras la tecnología de computadores avanzaba hasta que volviera a permitirles tratar de ejecutar sus ideas sobre un hardware renovado y más potente. Intel presentaría el microprocesador en 1971, IBM el disquete en el mismo año y su unidad de disco en 1973. Por su parte, Apple presentó en 1977 su nuevo canon de computadora, el Apple II; y Microsoft presentó su sistema operativo DOS en 1981. Todos los avances en arquitectura de computadores, así como en microprocesadores y sistemas de almacenamiento permitirían que en los años posteriores el desarrollo de la IA volviera a tener un importante impulso. 

46 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

#### **_Dato importante_** 

**_1961_** _– Primer sistema experto, SAINT, dedicado a la resolución automática de integrales sencillas al nivel de un pre-universitario_ 

**_1963_** _- McCarthy abandona el MIT y funda el Stanford AI Project especializándose en el estudio de la lógica formal._ 

**_1964_** _- Se presenta ELIZA, el primer algoritmo de NLP de la historia con diseño “scruffy” en el laboratorio de Minksy en el MIT_ 

_Bobrow crea STUDENT, un programa escrito en LISP que es capaz de solucionar problemas de álgebra enunciados en texto, uno de los primeros procesadores de lenguaje con utilidad y éxito reales._ 

**_1965_** _– Año de comienzo de operaciones del grupo de IA de la Universidad de Edimburgo_ 

**_1966_** _- Informe ALPAC sobre la escasez de resultados en el campo de la traducción automática poniendo alerta al gobierno de los Estados Unidos_ 

**_1969_** _- DENDRAL es el primer agente experto con éxito del mercado, basado en lógica formal o “neat” pero muestra numerosas limitaciones, principalmente por la falta de aprendizaje automático_ 

_Shakey el robot se convierte en un fracaso histórico que aumenta las sospechas de los gobiernos sobre las posibilidades reales de la IA_ 

_Minsky publica Perceptrons criticando las ideas de Rosenblatt, consiguiendo que los perceptrones so sean estudiados en la próxima década_ 

**_1972_** _- El grupo de IA de Edimburgo presenta la versión de PROLOG junto a la Universidad de Marsella, el primer lenguaje de programación declarativo destinado a sistemas de IA_ 

**_1973_** _– Un informe devastador en Reino Unido aparece advirtiendo de los pocos resultados de la IA y de su excesivo optimismo en el pasado: El Lighthill Report_ 

**_1974_** _- Se cancela la gran mayoría de becas para IA y comienza el denominado como “Primer Invierno de la IA”._ 

_No habrá avances hasta principios de la década siguiente mientras la tecnología de la computación avanza para permitir a la IA continuar su desarrollo._ 

47 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 

### **Etapa 3. Los primeros éxitos, vuelta de la financiación 1980 – 1987** 

A pesar de la gran caída de fuentes de financiación por parte de la administración pública y hacia los distintos laboratorios de investigación de IA en el mundo, los avances en tecnología de computadores hicieron que algunas grandes corporaciones trataran de crear sistemas inteligentes por sus propios medios. 

En **1980** , nada más empezar la década, Digital Equipment Corporations (DEC), una de las mayores empresas en la industria de los computadores en Estados Unidos durante la segunda mitad de S XX, presentó un sistema experto en el que llevaba trabajando un par de años. Como ya se ha expuesto previamente, los sistemas expertos son programas informáticos de IA que emplean reglas lógicas _a priori_ introducidas por expertos en un cierto dominio de negocio. Estos programas pueden resolver problemas y responder preguntas acerca de un dominio muy específico. 

El sistema de DEC se llamó R1, aunque internamente se le otorgó el nombre de XCON por _eXpert CONfigurer_ . Este agente experto ayudaba a los clientes de DEC a seleccionar el computador que mejor se adaptaba a sus requisitos de compra y fue un éxito rotundo, Por primera vez, un sistema de IA era realmente útil. Cumplía una función que desempeñaba con éxito y mejoraba la experiencia de los clientes de DEC. Los cálculos resultaron en un total de 40 millones de dólares ahorrados por la compañía anualmente. 

A raíz de este éxito, corporaciones de todo el mundo comenzaron a desarrollar sistemas expertos por medio de sus propios departamentos de IA, no siendo ya imprescindibles los distintos laboratorios universitarios a lo largo del mundo. 

En este mismo año Stanford mostró al mundo el primer ejemplo de vehículo autónomo, consiguiendo mejorar notablemente los resultados obtenidos por el fracaso de Shakey the robot. The Stanford Cart, un robot con cámara de vídeo incorporada y capacidad para evitar objetos y calcular el lugar hacia el que debía dirigirse consiguió atravesar una sala llena de sillas en “tan solo” cinco horas sin llegar a pararse del todo hasta que hubo atravesado todo su camino, sin ningún tipo de interacción humana. 



The Stanford Cart, tras conseguir atravesar la sala de su reto 

48 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 

En **1981** , el Primer Invierno de la IA pasaría a la historia. El Ministerio Japonés de Industria y Comercio Internacional destinó la cifra de 850 millones de dólares a un ambicioso programa llamado Fifth Generation Computer Systems. Este programa perseguía la construcción de supercomputadores que pudieran proporcionar a los sistemas de Inteligencia Artificial la capacidad de cómputo necesaria para ejecutar sus complejos programas. Por otro lado, trataba de incentivar la investigación en campos como el NLP, la traducción automática entre idiomas, la visión artificial y la interpretación de dibujos, y los programas capaces de “pensar como humanos”. Para el desarrollo de este proyecto se seleccionó el lenguaje PROLOG como el prioritario en todos los proyectos. 

Varios gobiernos respondieron a este plan con los suyos propios, comenzando a desbloquear la financiación alrededor del mundo. En **1983** DARPA presenta en Estados Unidos su _Strategic Computing Initiative_ para desarrollar en los próximos diez años supercomputadores americanos y proyectos de inteligencia artificial tal y como harían los japoneses. Su misión era, en palabras de DARPA “el desarrollo de supercomputadores capaces de ejecutar diez mil millones de instrucciones por segundo para así conseguir ver, escuchar, hablar y pensar tal y como lo hace un ser humano. El grado de integración requerido implica mejorar las capacidades del cerebro humano, que es el instrumento más complejo conocido por la humanidad”. Los efectos prácticos de este programa supusieron una inversión media de 100 millones de dólares al año. 

Un año más tarde, en **1984** , el Reino Unido presentó el programa Alvey. John Alvey era un directivo en British Telecom que recibió el encargo del gobierno de diseñar un programa de financiación que pudiera rivalizar con los ya presentados por Estados Unidos y Japón. A diferencia de los dos anteriores, este programa no estaba centrado en la IA, sino que buscaba mejorar las capacidades de los ingenieros británicos en una serie de ámbitos que fueron: 

- Microelectrónica avanzada y VLSI (Integración a Muy Gran Escala) 

- Sistemas Expertos e Inteligencia Artificial 

- Ingeniería del Software 

- Traducción automática y Procesamiento del Lenguaje Natural (NLP) 

En cuanto a avances en investigación, uno de los más importantes de la década de los ochenta fue publicado en **1982** por el físico americano John Joseph Hopfield. Su invención, ahora llamada Hopfield network fue la primera red neuronal asociativa y recurrente en la historia. La idea de una red neuronal recurrente llegará hasta nuestros días para ser empleada en numeras aplicaciones en campos como el reconocimiento de lenguaje, como veremos más adelante, siendo uno de los tipos de red neuronal artificial más usados en la actualidad por investigaciones y corporaciones de todo el mundo. Tan recientemente como en 2020, se publicó el artículo científico llamado _“Hopfield Networks is All You Need”_ sosteniendo la vigencia de este tipo de redes neuronales para problemas actuales con tan solo alguna ligera mejora para adaptarla a los tiempos actuales. 

49 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Una red neuronal recurrente (RNN por sus siglas en inglés _Recurrent Neural Network_ ) parte de la idea de que la información no tiene que pasar necesariamente en una única dirección, que hasta el momento era hacia delate, sino que el cómputo que realiza una neurona puede ser la entrada del cómputo de otras neuronas de su mismo nivel en pasos subsecuentes del cálculo, o incluso de sí misma. Dicho de otra forma, la información generada por las propias neuronas puede volver hacia atrás, lo que permite a la red neuronal tener un cierto tipo de memoria o de concepto de tiempo, ya que la información que computa en un momento dado se tiene en cuenta para el cómputo en momentos posteriores, generando así una lógica temporal que las redes neuronales iniciales no planteaban. Profundizaremos en este tema más adelante, pero es esencial comprender la relevancia de este descubrimiento para aplicaciones actuales como generación automática de texto en tiempo real, o el análisis de sentimiento en una conversación humana. En cualquier secuencia temporal de eventos, como una frase o un vídeo, recordar lo que se acaba de procesar es una habilidad esencial, y las RNN abrieron la posibilidad a que esto sucediera en la disciplina de la IA. 

En la siguiente figura podemos observar a la izquierda el comportamiento de una red neuronal recurrente en las que el cómputo de salida de una neurona puede formar parte de la entrada en siguientes pasos. A la derecha vemos una red neuronal de alimentación hacia delante o “ _feed-forward”_ (FFNN), que era el único tipo de red neuronal empleada hasta el momento, en la que la información pasa una única vez por cada capa de neuronas y jamás vuelve hacia atrás, haciendo imposible un cálculo que tenga en cuenta estados anteriores tal y como se precisa hacer para analizar una frase escrita palabra por palabra. 



A la izquierda, una red neuronal recurrente (RNN). A la derecha, una red neuronal FFNN 

En torno al mismo momento en el que Hopfield publicaba sus desarrollos sobre redes neuronales recurrentes, una de las grandes mentes del campo de la IA hasta el momento actual, Geoffrey Hinton, publicó un artículo que sería esencial para que los sistemas inteligentes basados en redes neuronales fueran capaces de aprender por sí mismos. 

50 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Recordemos que este objetivo llevaba vigente desde la creación de la disciplina y derivado de la incapacidad de los agentes expertos de actualizar su conocimiento en función de cambios en el entorno. 

Geoffrey Hinton es un psicólogo cognitivo e ingeniero informático nacido en Londres que desarrolló su doctorado en el ya conocido grupo de IA de la Universidad de Edimburgo y posteriormente desarrollaría la mayoría de su carrera profesional en Canadá. Junto a sus compañeros David Rumelhart y Ronald J. Williams, escribió un artículo con miles de citaciones en investigaciones posteriores sobre un método que denominaron “backpropagation” en español “retro propagación”. Volveremos a hablar de Hinton a lo largo de toda la historia de la IA a partir de este momento, pero este, su primer descubrimiento, fue uno de los más importantes para el futuro del _Deep Learning._ 

El algoritmo de _backpropagation_ surgió para dar respuesta a la necesidad de un método para entrenar modelos de redes neuronales (por el término train empleado ampliamente en el proceso de aprendizaje de las redes neuronales en inglés). Hinton y sus compañeros tuvieron la intuición de que lo que una red neuronal almacenaba realmente en cada una de sus neuronas y de las capas de neuronas eran representaciones internas de información abstracta sobre el problema para el que estaba entrenada. Es decir, los pesos que cada neurona asignaba a cada una de sus entradas eran una forma de representación de información compleja. 

La idea de este algoritmo consistía en conseguir que una red neuronal multicapa pudiera generar correctamente estas representaciones internas de forma automática, para así permitir que aprendiera cualquier mapeado entre su entrada y la salida esperada de forma óptima. En lugar de asignar de forma manual los pesos de cada entrada, estos serían asignados aleatoriamente en el rango de valores posibles (entre cero y uno). La red neuronal, por tanto, comenzaría sin ningún tipo de información relevante contenida, ya que sus pesos serían fruto del azar. Gracias al algoritmo de _backpropagation_ a medida que la red neuronal fuera analizando ejemplos, se revisarían los resultados y se tratarían de propagar hacia atrás los errores y aciertos para ajustar los pesos según los resultados. 

Profundizaremos en el funcionamiento de este algoritmo en módulos anteriores ya que en esta unidad lo esencial es comprender la enorme importancia que tuvo este descubrimiento para el futuro de las redes neuronales. A partir de este momento, existía un algoritmo que permitía a las redes neuronales aprender efectivamente de forma automática, y por tanto les otorgaba el potencial de resolver prácticamente cualquier problema. 

51 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 



Visualización gráfica de la retropropagación de los errores en una red neuronal para la actualización de los pesos 

A partir de **1985** las compañías privadas invierten más de mil millones de dólares anuales en el desarrollo e implantación de sistemas expertos y surge una nueva industria que crecerá exponencialmente en torno a las máquinas Lisp. Estas máquinas eran ordenadores específicamente diseñados para la ejecución de programas informáticos escritos en Lisp, el lenguaje de programación para IA que presentara John McCarthy en 1958. En el ya mencionado AI Lab en el MIT se desarrolló un hardware específico para hacer ciertas operaciones en Lisp mucho más eficientes que un software convencional, lo que aceleraría enormemente los tiempos de cómputo y por tanto la usabilidad de los sistemas inteligentes de la época. En torno a la fabricación de este nuevo tipo de super computador surgirían empresas con gran éxito como Lisp Machines Inc, una spin-off del MIT y Symbolics, también procedente del MIT, que como curiosidad registró el primer dominio .com para su página web en 1985 para la venta de máquinas Lisp. También surgieron compañías dedicadas a la programación de software en Lisp como IntelliCorp y Aion, que se dedicaron enteramente al desarrollo de sistemas expertos empresariales ambas desde California recolectando grandes éxitos y ganancias gracias al hardware específico que les proporcionaban las máquinas Lisp para instalar en sus respectivos clientes. 

En **1986** , la empresa de automóviles Mercedes-Benz construyó y publicó un sistema de cámaras y sensores llamado PROMETHEUS (Programme for a European Traffic of Highest Efficiency and Unprecedented Safety) que permitía que una furgoneta condujera de manera autónoma por una carretera sin ningún otro vehículo ni obstáculo. De hecho, la demostración se realizó en el parking de una universidad. Los ordenadores necesarios para ejecutar todos los algoritmos de detección de líneas, profundidad y manejo de los mandos ocupaban todo el interior de la furgoneta. Aún con todas las limitaciones mencionadas, fue el primer ejemplo de vehículo real adaptado para una conducción autónoma, y un absoluto adelantado a su tiempo. 

52 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

El éxito del mercado de máquinas Lisp fue más fugaz de lo esperado dada la gran velocidad con la que surgía nuevo hardware generalista, cada vez con mayores capacidades y un menor precio, convirtiendo a las máquinas Lisp en sistemas caros con menos potencia comparada con otros sistemas. Esto supuso el colapso del mercado de fabricantes de máquinas Lisp en **1987** , por la feroz competencia que ejercían Apple e IBM con sus computadores de propósito general orientados a inundar el mercado. Los investigadores de IA más experimentados empezaron a temer que la gran acogida y explosión de los sistemas expertos en las empresas se hubiera convertido en una burbuja que hubiera acabado fuera de control y que, junto al colapso de la fabricación de hardware específico, el campo de la IA pudiera sufrir otro nuevo revés. 

En **1987** el computólogo y filósofo americano Judea Pearl publicó su libro “ _Probabilistic Reasoning in Intelligent Systems._ ” En el que presentó un nuevo tipo de redes denominadas “ _Bayesian networks_ ” o redes bayesianas. Este tipo de modelo estadístico, empleado a día de hoy en implementaciones de proyectos reales con _Machine Learning_ , es capaz de analizar un evento que ha sucedido y analizar las posibles causas de dicho evento asociando una probabilidad a cada una de ellas. Por ejemplo, las redes bayesianas se emplean para encontrar relaciones entre síntomas y enfermedades. Dados una serie de síntomas, una red bayesiana puede tratar de estimar las probabilidades de que sean causados por otra enfermedad. En definitiva, las redes bayesianas son una forma de aplicar el teorema de Bayes de forma automática para problemas complejos. 

En este mismo año, Rollo Carpenter, un ingeniero británico, creó un chatbot que se convirtió inmediatamente en el estado del arte de la simulación de conversación con humanos, lo llamó Jabberwacky. La intención de Carpenter era comenzar a trabajar hacia un sistema que fuera capaz de superar un test de Turing, aunque la realidad sería que aún faltarían más de veinticinco años para que esto sucediera. Jabberwacky estaba enfocado de manera distinta a sus antecesores, ya que trataba de aprender en base a la interacción constante con los humanos. Esto implica que no tenía una base de conocimiento formal y a priori como los sistemas expertos, sino que era capaz de obtener nuevas capacidades a través de la experiencia. Tiene una base de datos masiva en la que almacena todas las conversaciones que ha tenido con humanos y emplea como respuestas frases que previamente ha leído de un interlocutor humano, a las que asigna una probabilidad de encajar en la conversación que está manteniendo. Sería necesario esperar a múltiples avances de la computación como internet y los navegadores web para que Jabberwacky estuviera a disposición de todo el mundo, y a día de hoy su página web sigue activa para poder experimentar de primera mano el método de aprendizaje que aplicaba: http://www.jab- <u>berwacky.com/</u> 

Ejemplo de una conversación online con Jabberwacky, en la que trata de aprender de las res- 

53 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 



puestas en naranja claro que son las proporcionadas por el interlocutor humano. Las respuestas en negrita están generadas automáticamente por el algoritmo. 

Los sistemas expertos, a pesar de su utilidad en ciertos casos de uso muy específicos, tenían numerosos problemas que ya hemos ido conociendo en las etapas que hemos analizado hasta el momento. Su mantenimiento era notablemente costoso, ya que la representación del conocimiento que tenían era muy extensa y compleja. Además, carecían de la capacidad de aprender de la experiencia, como sí parecía que fueran capaces las redes neuronales de última generación gracias a las innovaciones como las Redes Neuronales Recurrentes (RNN) de Hopfield y los algoritmos de aprendizaje como el algoritmo de retropropagación ( _backpropagation_ ) de Hinton, mediante los cuales los algoritmos eran capaces de actualizar su propia representación interna de la realidad en base a la experiencia. 

En cuanto el contexto en el que se empleaban los agentes expertos cambiaba mínimamente, sufrían fallos terminales que impedían que fueran sistemas flexibles y escalables. Y, por último, requerían una gran capacidad de cómputo por su escasa eficiencia de cálculo. Si bien habían cumplido con los objetivos iniciales que se les había propuesto, el mundo comenzó a verlos como sistemas anticuados que no podrían seguir el ritmo de los avances tecnológicos. En paralelo, a pesar de que los avances relativos a las redes neuronales parecían prometedores, la capacidad de cómputo que requerían sus algoritmos estaba fuera de toda posibilidad con el hardware de este momento, lo que los convertía en algoritmos prometedores pero limitados totalmente por el avance de la capacidad de computación. Y estas dos situaciones unidas, en un breve lapso de tiempo, supondrían de manera irremediable el comienzo del temido “Segundo Invierno de la IA” con nuevas limitaciones presupuestarias y falta de confianza de la sociedad en general. 

54 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

#### **_Dato importante_** 

**1980** _– El primer agente experto con éxito comercial, denominado XCON, ayuda a los clientes a seleccionar el producto que más se adecua a sus necesidades convirtiéndose en un gran aliado._ 

**1981** _– El gobierno japonés lanza un ambicioso plan de impulso de la IA con una gran inversión denominado el plan de “Fifth Generation Computers”._ 

**1982** _- Hopfield presenta la primera red neuronal recurrente en la que la información fluye hacia atrás, dotando de memoria a las redes neuronales artificiales._ 

_Hinton publica el algoritmo clave de backpropagation, gracias al cual las redes neuronales pueden ser entrenadas para resolver problemas, es decir, consiguen tener capacidad de aprendizaje._ 

**1983** _– La agencia estadounidense DARPA presenta el plan Strategic Computing Initiative para construir sus propios supercomputadores y modelos de inteligencia artificial._ 

**1984** _– El Reino Unido lanza el programa Alvey para tratar de mejorar sus competencias tecnológicas, siendo la IA una de las disciplinas más destacadas en las que pretenden invertir._ 

**1985** _– La industria en torno a las Lisp Machines de McCarthy tiene una grana acogida y el mercado de los agentes expertos crece exponencialmente en un breve periodo de tiempo._ 

**1986** _– Mercedes-Benz presenta el primer ejemplo de vehículo autónomo completo en forma de una furgoneta._ 

**1987** _– Se publica el primer artículo con una propuesta de redes bayesianas, que infieren causas a partir de efectos, aplicando el teorema de Bayes de forma totalmente automática._ 

_Se publica Jabberwacky, un chatbot con gran capacidad de aprendizaje en base a las interacciones reales con humanos._ 

_Colapsa el mercado de las máquinas Lisp por la competencia de los nuevos computadores, más potentes y versátiles, que han aparecido recientemente en el mercado._ 

55 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 

### **Etapa 4. El Segundo Invierno de la IA 1988 – 1993** 

La fascinación del mundo empresarial por los sistemas inteligentes creció y cayó de forma abrupta a lo largo de los años 80. El colapso de los fabricantes de hardware específico para estos sistemas dio la impresión al mundo de que la IA había vuelto a poner demasiadas esperanzas y optimismo en todo lo que podía lograr, y volvió a muchos reticentes acerca de las capacidades reales de esta tecnología. Sin embargo, numerosos investigadores en este campo continuaron con su labor presentando avances y novedades mientras los fondos disponibles y el interés de la comunidad económica no paraban de crecer. 

Cuando en **1987** el mercado de máquinas Lisp colapsó, la iniciativa de DARPA _Strategic Computing Initiative_ cortó de golpe todos los fondos destinados a la investigación de la IA siguiendo una tendencia social creciente. Los nuevos directores de la agencia consideraban que la IA no sería relevante tecnológicamente en los próximos años por lo que desviaron los fondos destinados originalmente a la investigación de esta tecnología a otras mejor aceptadas por la sociedad y por las empresas, otras tecnologías capaces de producir resultados más inmediatos y con un tiempo a mercado mucho mejor. 

Por otro lado, ninguno de todos los objetivos marcados por Japón en su Fifth Generation Project había sido cumplido. De nuevo, la expectativa por los posibles avances de la IA había sido notablemente superior a su potencial real. De nuevo, hubo una oleada de indiferencia y reducción de la financiación en todos los países desarrollados. 

Hubo sin embargo investigadores que resistieron, tanto en universidades como en empresas privadas, que permitieron que el campo siguiera avanzando, aunque a menor velocidad que en los años anteriores. 

En **1988** , miembros del Watson Research Center de IBM publicaron un artículo titulado “ _A statistical approach to language translation_ ”. En él, presentaban un novedoso método para afrontar la traducción automática. Proponían abandonar las reglas de la lógica formal de los sistemas de las décadas anteriores para pasar a sistemas basados en probabilidades más similares a los sistemas de _Machine Learning_ con los que contamos hoy en día. Ya no se trataba de proporcionar a la máquina a priori toda la información necesaria para la resolución de un problema, como exigían los sistemas expertos, sino que bastaba con tratar de computar las probabilidades de cada tipo de traducción para una frase y elegir la mejor. No se buscaba definir toda la comprensión y conocimiento relativos a cada par de idiomas y sus relaciones para efectuar una traducción, sino mostrarle al algoritmo tantos ejemplos como fuera posible, para que en futuras ocasiones pudiera seleccionar la mejor de entre sus opciones basada en la experiencia. Era un enfoque que caminaba hacia máquinas capaces de aprender, aunque no necesitaran comprender para ello. 

También en **1988** aparecería uno de los mayores avances en _Deep Learning_ y visión artificial que se han dado hasta el momento en la IA. Fue gracias a Yann LeCun, un ingeniero informático de origen francés experto en Inteligencia Artificial. En 2018 recibió el premio 

56 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Turing, considerado como el Nobel de la informática, junto a Hinton. LeCun es el padre de un tipo de red neuronal que desde su nacimiento hasta nuestros días ha sido esencial para el desarrollo de la IA y en concreto de la visión artificial: Las Redes Neuronales Convolucionales. Durante su trabajo en los laboratorios de AT&T Bell en Nueva Jersey tuvo la inspiración de emplear modelos biológicos complejos del cerebro humano para mejorar las redes neuronales convolucionales. 

En 1959, casi tres décadas atrás, David Hubel y Torsten Wiesel, neuropsicólogos, describieron que en la visión humana participaban dos tipos de neuronas en el cerebro, las células “simples” y las células “complejas”. Las células simples eran aquellas que se excitaban ante cierto tipo de bordes y patrones según las orientaciones y posiciones de estos. Es decir, hay neuronas simples que reaccionan a los bordes lineales con dirección horizontal, otras que reaccionan a las manchas redondas en posiciones superiores de nuestro campo de visión y otras que reaccionan a los ángulos rectos cuyas líneas están dispuestas en diagonal. Las células complejas pueden reaccionar a un mismo patrón independientemente de su orientación, por lo que son capaces detectar cualquier borde lineal independientemente de su orientación, cualquier mancha redonda o cualquier ángulo recto independientemente de la dirección de las líneas que lo conforman. Esto se denominó “invariabilidad espacial”. Tres años más tarde descubrieron que las neuronas complejas eran capaces de detectar el mismo patrón en distintas orientaciones y lugares de una imagen porque recibían la información individual de cada neurona simple y “resumían” la información de estas. Una red neuronal biológica en la que unas células iniciales reaccionan a estímulos muy concretos, y posteriormente ciertas neuronas resumen esa información para que podamos comprender y procesar lo que vemos. 



Explicación visual del comportamiento de las células simples frente a las células complejas 

57 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Décadas más tarde, LeCun unió dos conceptos que serían clave para el futuro de la IA. Por una parte, imaginó una red neuronal organizada de manera similar a la visión humana para el reconocimiento de patrones. Una serie de neuronas iniciales que estuvieran especializadas en la detección de un borde, brillo, color o sombra complejo. Y más tarde, una serie de capas más profundas – este es el origen del término aprendizaje profundo o _Deep Learning_ – que convirtieran esta información individual en conocimiento abstracto y perceptible. Por otro lado, aprovechó el algoritmo de _backpropagation_ de Hinton como método para el entrenamiento de estas redes neuronales, de tal forma que los pesos de entrada de cada neurona se ajustaran automáticamente a medida que la red neuronal fuera observando ejemplos. En su artículo “B _ackpropagation Applied to Handwritten Zip Code Recognition_ ” LeCun y su equipo propusieron la primera Red Neuronal Convolucional (CNN por sus siglas en inglés) de la historia. Además, más allá del trabajo teórico, en este artículo publicaron un modelo específico destinado a leer automáticamente dígitos manuscritos en cheques de banco para automatizar el reconocimiento de códigos postales de los mismos. Para poder entrenarla por medio de la retropropagación, crearon la base de datos MNIST ( _Modified National Instituto f Standards and Technology_ ) que a día de hoy sigue siendo empleada para poner a prueba nuevos modelos de CNNs. Esta base de datos fue construida gracias a numerosos empleados de la Oficina del Censo de Estados Unidos que rellenaron una tarjeta con dígitos manuscritos del 0 al 9. 

Una vez construida esta base de datos de imágenes etiquetadas – es decir, cada imagen tiene el valor real del dígito que contiene asociado – se entrenó la CNN propuesta por LeCun. Este proceso basado en retropropagación comienza con una inicialización aleatoria de los pesos de las neuronas. Después, las imágenes de MNIST van pasando una a una por la red neuronal, que inicialmente devolverá valores aleatorios. Sin embargo, a medida que los errores que comete se van propagando hacia atrás, actualizando los pesos de las neuronas para corregir estos errores, la red neuronal va aprendiendo. Esta red neuronal se denominó LeNet, y se puede observar una visualización de su funcionamiento en la siguiente figura 



Arquitectura de la CNN LeNet para la detección de dígitos manuscritos 

58 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

En la actualidad hay Redes Neuronales Convolucionales capaces de inferir el dígito que se encuentra detrás de un papel manuscrito con mejor precisión de la que lo hacen los humanos. La arquitectura propuesta por LeCun tenía un problema principal: La capacidad de cómputo que requería para ejecutar todos los cálculos dentro de cada una de las neuronas de cada capa hacía que el proceso no fuera del todo eficiente en términos temporales y que la propuesta de LeCun fuera aplaudida en círculos académicos, pero no tan bien acogida por el entorno económico industrial. No obstante, en la década de los 90 el 10% de las cartas de Estados Unidos se clasificaban automáticamente empleado una versión optimizada de esta primera arquitectura de CNN que llegaría hasta nuestros días. 

En torno a la misma época, en **1989** el sistema inteligente _Deep Thought_ vencería por primera vez a jugadores humanos maestros de ajedrez. Este programa, desarrollado por IBM y llamado así en homenaje a la novela de ciencia ficción “Guía del autoestopista galáctico”, en la que salía un ordenador con el mismo nombre, no porque usara redes neuronales profundas. De hecho, sus algoritmos eran funciones de evaluación bastante simples en las que se calculaban las probabilidades de los distintos posibles movimientos del rival y se elegía aquella con mayores probabilidades de llevar a la máquina a la victoria. 

En un artículo de **1990** titulado “ _Elephants Don’t Play Chess_ ” el experto en robótica Rodney Brooks afirmaba que el enfoque de la IA a través de lenguajes formales y simbólicos como el que se emplea para definir jugadas de ajedrez no era suficiente si se pretendía que la IA llegara a solucionar problemas del mundo real. Brooks sostenía en su artículo que el enfoque de tratar de darle a los algoritmos todo el conocimiento del mundo “a priori” en un lenguaje formal no era correcto, ya que la neurociencia había demostrado que los cerebros biológicos no eran así como funcionaban. Generalmente un cerebro está compuesto de varios módulos especializados en percibir una cierta parte del mundo, y estos módulos siempre están actualizados ya que continuamente se ajustan a la experiencia y aprenden de lo experimentado. En definitiva, un algoritmo inteligente necesitaba tener propiocepción y capacidad de aprendizaje. No era suficiente con seguir reglas fijas para solucionar problemas concretos como hicieron en su momento los sistemas expertos. Esta nueva visión impulsó todavía más al campo del aprendizaje profundo y de las redes neuronales, ya que el artículo de Brooks tuvo una gran acogida en la comunidad científica. 

Como hemos podido ver durante esta etapa los avances relativos a la Inteligencia Artificial fueron escasos, pero gracias a la invención de las CNN y a expertos que afirmaban que la IA no debe estar basada en reglas simbólicas, junto a las invenciones pasadas de las RNN y de los algoritmos de retropropagación se estaba generando una base perfecta para lo que vendría después. Con los sistemas expertos dando las últimas alegrías a los investigadores de sistemas inteligentes, se hacía cada vez más patente la necesidad de encontrar un tipo de algoritmo que sustituyera a estos en el camino hacia modelos con capacidades realmente inteligentes. Las redes neuronales parecían el camino a seguir, pero aún existía una gran limitación tecnológica que impedía el entrenamiento y la ejecución en tiempo real de estos modelos, que seguían mostrando grandes resultados sobre el papel, pero 

59 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

era imposible implantar de forma práctica en el mercado. La siguiente etapa, hasta el año 2011, sería una etapa de expansión, en la que el mundo de esta disciplina aguardaba la llegada de la potencia de cómputo necesaria para poder ejecutar los modelos de redes neuronales artificiales de una vez por todas. 

#### **_Dato importante_** 

**_1988_** _- “A statistical approach to language translation, primera vez que se aplican técnicas similares al machine learning para problemas de traducción automática_ 

_Yann LeCun publica por primera vez un artículo en el que propone las Redes Neuronales Convolucionales basadas en la visión humana. Entrena un modelo para una base de datos de códigos postales manuscritos (MNIST) dando comienzo a la era del Deep Learning. Esta tecnología será clave en el desarrollo futuro de la IA, y marcará un antes y un después._ 

_1989 – El Sistema de IBM “Deep Thought” vence por primera vez a jugadores de ajedrez humanos de gran nivel, pero emplea una serie de algoritmos de probabilidad sencillos sin capacidad para el aprendizaje. Todavía no se ha conseguido vencer a grandes maestros con estos algoritmos basados en lógica simbólica._ 

**_1989_** _– Brooks publica “Elephants don’t play chess” que ayuda a la comunidad internacional a inclinarse por el Deep Learning, criticando el enfoque determinista y formal de los trabajos anteriores, entre los que destacan los agentes expertos._ 

### **Etapa 5. La gran expansión 1994 – 2011** 

Tras casi medio siglo con el campo de la IA delimitado y en crecimiento, a principios de los 90 se empezaron a conseguir viejos objetivos perseguidos tanto por la rama académica como por la empresarial con un mínimo éxito. Después de unas épocas turbulentas en las que la IA pasaba de ser la tecnología del momento a un puro sueño de algunos utópicos, a partir de la última década de S. XX esto cambiaría radicalmente. Tras los lentos pero continuos avances producidos en distintas corporaciones y universidades a lo largo del mundo, pero principalmente en Estados Unidos, Reino Unido, Canadá, Francia y Japón, la IA había conseguido demostrar lo que en ciertos momentos de la historia parecía imposible: que tenía la capacidad de resultar útil al mismo tiempo que realmente inteligente. 

60 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

No solo los desarrollos de décadas posteriores sustentaron este aumento de confianza durante los noventa. Si bien es cierto que la definición de las neuronas artificiales y los perceptrones, las primeras Redes Neuronales y la creación de algoritmos de entrenamiento y el primer diseño de Redes Neuronales Convolucionales fueron grandes hitos, nada podría haberse conseguido sin una mejora exponencial en la capacidad de cómputo de los computadores a lo largo del mundo. 

El surgimiento de Linux, un sistema operativo compatible UNIX junto a la creación de la programación orientada a objetos (que incorporaría la idea de herencia a partir de los primeros sistemas de lógica formal y de símbolos en lenguajes como PROLOG) y la mejora constante de la capacidad de cómputo junto a los sistemas operativos de Windows y Mac OS permitieron que los algoritmos a implementar por parte de los investigadores de IA pudieran ser más costosos computacionalmente, y también que su trabajo se desarrollara de forma más eficiente y conectada gracias a los nuevos sistemas operativos, navegadores web y sistemas de correo electrónico. 

Si bien la confianza de las empresas en la IA como valor añadido todavía era escaso, al menos ya no parecía que la IA fuera un campo convertido en una burbuja hinchada a base de optimismo, sino que empezó a verse como una rama científica con potencial real para solucionar problemas concretos y con capacidades suficientes. Dado que en los últimos años se había abandonado la idea de una IA basada en lógica formal y que pudiera realizar razonamientos complejos como los humanos, algo así como una AGI, las empresas empezaron a centrarse en sistemas para resolver problemas específicos, pero, a diferencia de los agentes expertos, que tuvieran la capacidad de aprender de la gran cantidad de datos que se empezaron a generar y almacenar durante esta década. Incluso hubo una serie de empresas e investigadores que evitaron mencionar el término “Inteligencia Artificial” durante unos años para diferenciarse de la IA optimista del pasado empleando en cambio términos como “informática”, “sistemas basados en el conocimiento”, “sistemas cognitivos” o “inteligencia computacional” entre otros, de tal forma que los programas de financiación no rechazaran sus propuestas por posibles similitudes con los grandes fracasos de otras épocas. 

Con grandes expectativas, pero, en esta ocasión, un realismo moderado en lugar de un optimismo desenfrenado comenzó el fin del Segundo Invierno de la IA, en un crecimiento exponencial que, ya sí, llegaría ininterrumpido hasta nuestros días. 

En **1994** , Daimler-Benz volvería a probar suerte con el vehículo autónomo por medio de los sistemas VaMP y Vita-2. Gracias a los avances realizados en capacidad de cómputo y en visión artificial, así como en los sensores empleados por estos sistemas como cámaras estereoscópicas para comprender la información de profundidad, fueron capaces de recorrer más de mil kilómetros por autopistas de París con tráfico real alcanzando velocidades de hasta 130 km/h con escasa interacción humana en los mandos principales del vehículo. Fueron capaces de que el vehículo cambiara automáticamente de carril, circulara detrás de otros vehículos por su carril y circulara sin tráfico. El resto de situaciones de tráfico debían ser todavía gestionadas por humanos. 

61 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Un año más tarde, en **1995** , el proyecto _Navlab_ de la Universidad Carnegie Mellon fue capaz de recorrer cinco mil kilómetros de carretera en su vehículo autónomo. En este caso, el 98,2% del tiempo de conducción el volante se movió solo. Este vehículo solo tenía controlado por IA el volante, gracias a una red neuronal que analizaba lo que capturaba una cámara a color y decidía si el volante debía girarse a derecha o a izquierda y en qué ángulo. Los pedales de aceleración y freno, así como el embrague y las marchas eran controlados por operadores humanos. 

El surgimiento de la web y de los navegadores web durante la década de los noventa201 permitieron a Richard Wallace desarrollar en **1995** su chatbot A.L.I.C.E (Artificial Linguistic Internet Computer Entity), que se inspiró en ELIZA, pero supo aprovechar el gran potencial de los millones de conversaciones y artículos almacenados en la web para recoger gran parte de ellos y entrenar con esta ingente fuente de información a su sistema. Es un programa mecanicista, teniendo una serie de respuestas preconstruidas y empleando heurísticas para elegir entre ellas la más adecuada. Si bien una conversación con ALICE puede ser divertida es obvio rápidamente que es una máquina que jamás pasaría el Test de Turing ya que se comprende su funcionamiento interno más pronto que tarde. Para probar a hablar con Alice se puede buscar en Google “pandorabots alice” y emplear el primer resultado, ya que aún se guarda una versión en funcionamiento para experimentar la conversación con un chatbot de hace casi treinta años. Esta fue la primera vez que un sistema empleaba las posibilidades de la recopilación de grandes cantidades de datos como fuente de entrenamiento, pero seguí empleando la decadente perspectiva de los sistemas formales de décadas pasadas. 

En **1997** la perspectiva formal consiguió otro gran logro ampliamente esperado por los investigadores originales de IA que, aunque ya relegado de la tendencia del momento por su poca aplicación práctica, causó un gran revuelo en la sociedad. IBM desarrolló un supercomputador con el único objetivo de jugar al ajedrez mejor que un ser humano y lo bautizó Deep Blue como continuación de su primer gran éxito, Deep Thought. Deep Blue fue el primer ordenador de la historia en ganar a un campeón del mundo de ajedrez con las mismas reglas y controles de tiempo que los participantes humanos. Un año antes, Deep Blue se había enfrentado a Garry Kasparov, campeón del mundo, y había perdido 4-2. En un año, IBM puso todos sus esfuerzos por mejorar las capacidades de su supercomputador inteligente y, finalmente, se alzó con la victoria por primera vez en la historia. Se considera uno de los últimos ejemplos de éxito de la actualmente denominada GOFAI _(Good Old-Fashioned Artificial Intelligence_ ), es decir, la de IA del pasado. Su inteligencia residía en la fuerza bruta que le proporcionaba su hardware, específicamente diseñado y desarrollado para este objetivo. En cada movimiento, analizaba partidas anteriores que tenía registradas con rasgos similares a la situación en la que se encontraba, y hacía una búsqueda para encontrar el movimiento óptimo. La única inteligencia que tenía era la capacidad de analizar hasta veinte movimientos de profundidad en juegos similares para poder analizar el mejor movimiento en cada caso. 

62 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Si bien la sociedad se sorprendió enormemente por la victoria de Deep Blue, los investigadores del campo de la IA sencillamente vieron una demostración de fuerza bruta sin ningún añadido a la tecnología existente, con la capacidad de resolver complejas simulaciones en un problema con reglas muy claras y un ámbito muy conciso, por lo que lo consideraron un hito de la supercomputación, pero no un paso adelante en la búsqueda de sistemas realmente inteligentes, ni de sistemas capaces de aprender de su propia experiencia y generar una representación propia de su entorno. Este tipo de sistema pertenecía a una categoría de IA llamada a día de hoy GOFAI, por _Good Old Fashioned Artificial_ Intelligence. Tecnología que ya se consideraba de otros tiempos. 

En contraste con los cada vez menos empleados sistemas expertos y basados en fuerza bruta, el campo del aprendizaje automático y de las redes neuronales cada vez tomaba más protagonismo en el mundo de la IA desde que Hilton propusiera el algoritmo de _backpropagation_ , Hopfield sus redes neuronales y Yann LeCun publicara las bases teóricas de las Redes Neuronales Convolucionales y las aplicara a la búsqueda visual de códigos postales. 

Un hito esencial en el campo del aprendizaje profundo se dio también en **1997** cuando Sepp Hochreiter y Jürgen Schmidhuber presentaron las redes LSTM ( _Long Short Term Memory_ ), un tipo específico de Red Neuronal Recurrente (RNN) tal y como lo eran las redes de Hopfield. Recordemos que una RNN consiste en que la salida computada de una neurona puede volver a ser su propia entrada junto a otras, o ser la entrada de otras neuronas en su misma capa, es decir, son redes neuronales con bucles. 

La arquitectura de las LSTM solucionaba el principal problema de las RNN hasta el momento, el algoritmo de _backpropagation_ no terminaba de funcionar bien para conseguir que las redes aprendieran. Debido a los bucles en las neuronas de las redes, el algoritmo no era capaz de propagar hacia atrás correctamente los errores y por tanto no era capaz de actualizar los pesos para minimizar estos errores. En concreto, este problema se daba cuando los errores habían pasado hacía un cierto periodo de tiempo, por ejemplo, analizando la primera palabra de una frase muy larga. El error se “desvanecía” y por tanto se decía que las RNN tenían memoria a muy corto plazo. La arquitectura LSTM creó “autopistas” dentro de la propia red neuronal para poder saltarse neuronas en el camino hacia atrás de los errores y de esta forma poder aumentar la capacidad de memoria de la red neuronal, que era capaz de solucionar correctamente problemas que requerían tener en cuenta información procesada en el pasado lejano. 

Esto ha llevado a las LSTM a ser la arquitectura más empleada a día de hoy para el procesamiento de flujos de datos o series de datos que requieren un seguimiento de la información a lo largo del tiempo como por ejemplo evaluar acciones humanas en un vídeo, predecir el tráfico en autopistas, o detección de anomalías en conversaciones empresariales. 

63 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 



Comparación entre una red neuronal no recurrente, una red neuronal recurrente estándar y una red LSTM 

A comienzos de S. XXI, el campo de los sistemas inteligentes viró hacia la investigación y el desarrollo de sistemas autónomos. Si bien la IA estaba comenzando a probar que podía resultar de ayuda real en ciertos casos de uso empresariales, hasta el momento solo habían triunfado ciertos sistemas expertos y algunos agentes conversacionales, pero en ningún caso se había desarrollado un sistema tangible con una utilidad real y posibilidad de llegar a mercado. Uno de los campos que más interés suscitó fue el de la robótica, en el que la IA y la sensórica se unieron para dar lugar a sistemas inteligentes capaces de interactuar físicamente con su entorno, en una continuación de trabajos como Shakey, The Stanford Cart y la furgoneta autónoma de Mercedes Benz. Esta situación supuso que los avances más destacados en el campo de la IA durante los primeros años de siglo estén relacionados con sistemas inteligentes con movimiento autónomo, o lo que podríamos definir como “robots inteligentes”. 



En el año **2000** , la Doctora Cynthia Breazeal, experta en informática afectiva del MIT, mostró al mundo un robot capaz de reconocer emociones humanas y de simularlas llamado Kismet. Kismet, como se puede ver en la imagen, es un robot que solo tiene cabeza, y en esta se representan los ojos, los labios, las pestañas, cejas y orejas. Para ser capaz de realizar esta tarea, Kismet necesitó poseer sistemas de procesamiento de sonido a texto, de lenguaje natural, de visión artificial y de propiocepción artificial. Gracias a sus cámaras y micrófonos era capaz de recoger sonidos e imágenes con los que realizaba tareas como el seguimiento de ojos, la detección de movimiento y el reconocimiento de rasgos faciales básicos. Tiene un conjunto de cámaras estereoscópicas, formadas por dos 

64 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 

lentes a una distancia conocida, que le permiten estimar distancias a los objetos que tiene en su campo de visión. Con toda esta información, un conjunto de algoritmos de clasificación permite identificar dónde está la persona con la que se interactúa, qué tono y volumen de voz tiene y la intención de la frase. Es decir, no hay un procesamiento del lenguaje natural ya que en ningún momento se pasa del audio que escucha Kismet a un texto que se procesa para comprender el significado. La interacción es más cercana a la que realiza un animal, basándose en nuestros rasgos faciales y en el tono y el volumen de nuestra voz para actuar en consecuencia. Kismet tenía una serie de frases previamente grabadas, y mediante el algoritmo de clasificación era capaz de seleccionar la frase más adecuada a cada contexto que detectaba. Aunque la utilidad de Kismet era realmente reducida, marcaba una serie de estándares que se implantarían en breve en la industria como el uso de cámaras y cámaras estereoscópicas para analizar el campo de visión y poder tomar decisiones al respecto. 

En **2001** se dio un gran salto hacia delante en la tecnología IA para el reconocimiento facial. En este año, Paul Viola y Michael Jones proponen su marco conceptual para la detección de objetos en tiempo real, llamado Viola-Jones. A pesar de que soportaba diversos tipos de detección de objetos, su motivación principal y el objetivo en el que alcanzó gran repercusión fue la detección facial en tiempo real en vídeos. Para hacerlo, empleaban un método denominado _Haar Features_ , que son características fáciles de identificar en una imagen como las que se muestran en la siguiente figura. Una vez identificadas manualmente estas características en imágenes de caras frontales, se entrena un algoritmo de clasificación para detectar estas características de forma automática y poder decidir dónde está una cara. 



Las haar features permiten detectar partes concretas de una cara por los contrastes de luz y oscuridad que siempre se dan en rostros humanos 

65 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Uno de los primeros usos comerciales de la tecnología de IA para la navegación robótica autónoma fue el que a su vez fue el primer robot que entró en las casas de muchos ciudadanos estadounidenses en **2002** , el aspirador inteligente Roomba de i-Robot. i-Robot es, como en tantas ocasiones, una spin-off procedente del MIT, fundada por robotistas y expertos en sistemas autónomos de esta universidad. Sus primeros diseños fueron los pequeños Micro Rovers para las primeras exploraciones espaciales de la NASA, y otros tipos de robots para la detección de minas y explosivos. Todos ellos eran operados por un humano en remoto hasta la llegada de Roomba. Este robot doméstico fue el primero en convencer a los consumidores de emplear un robot totalmente autónomo. Gracias a una cámara estereoscópica de infrarrojos, es capaz de analizar el espacio que le rodea y decidir la mejor ruta a través de los obstáculos de una habitación para recorrer todo el suelo de la misma de forma eficiente. Las cámaras estereoscópicas de infrarrojos tienen un emisor de infrarrojos que dibuja un patrón invisible al ojo humano en el entorno que les rodea. Este patrón se deforma al impactar contra diversos objetos a distintas distancias. Dado que la cámara tiene dos sensores, es capaz de percibir las sutiles diferencias percibidas por una cámara y otra debido a su posición, y triangular la distancia de cada punto que observa. Esta tecnología junto con un sistema autónomo para evitar obstáculos y un decisor de rutas, conforman un robot sencillo pero que cumple su utilidad y lleva la automatización por primera vez a los hogares estadounidenses y, posteriormente, del mundo. 

Continuando con el auge de los sistemas autónomos con propiocepción, sensórica y capacidad de movimiento, en **2004** los rovers de exploración de la NASA “Spirit” y “Opportunity” navegaron por la superficie humana sin necesidad de intervención humana. En este caso, de nuevo gracias a un sistema estéreo, un algoritmo de reconocimiento visual de patrones, dentro de lo que podríamos considerar como técnicas clásicas de visión artificial – profundizaremos en estas en el módulo dedicado a la visión artificial – analiza el terreno y es capaz detectar elementos de peligro, baches, rocas y otras complicaciones, para así trazar la ruta más segura por el terreno marciano. Para ello, el algoritmo busca el camino hacia un punto de ruta que obtenga la mejor puntuación dentro de sus reglas heurísticas. Este algoritmo es denominado GESTALT, Grid-based Estimation of Surface Traversability Applied to Local Terrain. Las imágenes estereoscópicas además permiten a los rovers conocer su propia posición por comparación de lo que perciben sus cámaras en los distintos momentos. A pesar de que los algoritmos empleados en estos pequeños rovers no eran extremadamente complejos ni novedosos, el hecho de ser capaces de ejecutarlos de forma autónoma, en remoto y en un pequeño ordenador alimentado por baterías solares abrió numerosas vías de investigación en el campo del vehículo autónomo que serían exploradas en los años venideros. 

Sumándose a esta tendencia por los vehículos y robots autónomos, la agencia americana DARPA, a la que hemos ido siguiendo a lo largo de los años, creó un certamen de coches autónomos denominado DARPA Grand Challenge en **2004** , con un premio en metálico de un millón de dólares para incentivar el desarrollo de tecnología americana en este campo. En la primera edición se propuso un circuito que recorría 240km a lo largo de una 

66 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

autopista en California, la Interstate 15. El equipo que más lejos llegó fue capaz de recorrer 11,78km hasta que se atascó al encontrarse una piedra que le hizo terminar dándose la vuelta. No hubo ganador y por tanto la competición se repitió al año siguiente, **2005** , con un cambio de superficie; se pasaría de la carretera a las pistas de tierra, y de 240 km se redujo la distancia hasta 212 km. En esta edición se pudo comprobar el vertiginoso ritmo de avance en esta tecnología ya que todos los competidores, menos uno, fueron capaces de superar la marca de 11,78 km del año anterior. El ganador fue el vehículo autónomo STANLEY, diseñado por la Universidad de Stanford y que completó el circuito en seis largas horas y cincuenta y cuatro minutos; seguido de cerca por Sandstorm de la Universidad Carnegie Mellon en Pensilvania, que tardaría once minutos más en completar el trazado. 

El Stanley era una versión modificada de un Volkswagen Tuareg que era conducido por un ordenador instalado dentro del coche y que procesaba las señales de los sensores colocados en el exterior del coche para guiarlo a través de las pistas de tierra. Para navegar en este caso no se emplearon cámaras estereoscópicas, sino un sistema mucho más preciso basado en láser llamado LIDAR, que permite construir un mapa de profundidad detallado del entorno, junto con posicionamiento por GPS y una cámara a color que junto a la información del LIDAR permitía la ejecución de un algoritmo de _machine Learning_ de detección de objetos, sombras y bordes para la navegación. En este caso, el algoritmo era verdaderamente inteligente ya que era capaz de realizar un aprendizaje automático en base a numerosos ejemplos de conducción de humanos que se le proporcionaron. 

En el caso de Sandstorm el vehículo también contaba con LIDAR, pero sumaron tecnología de radar y un par de cámaras estereoscópicas para contar con la mayor información posible, pero carecía de un sistema de autoaprendizaje y aunque en el primer tramo, más sencillo, fue capaz de avanzar más rápido que Stanley, acabó atascado en un tramo con dificultad para diferenciar objetos por culpa de las sombras y terminó en segundo lugar. 

En vista de los grandes y rápidos avances del campo de la IA, que recordemos había decidido esconder estas siglas bajo denominaciones más específicas como en este caso, el vehículo autónomo, el ejército de los Estados Unidos comenzó a invertir en diversas firmas para impulsar aún más el desarrollo de robots y vehículos autónomos dentro de sus fronteras. 

En **2005** , la empresa _Boston Dynamics_ una spin-off más procedente del MIT, fundada en 1992, fue la encargada de construir un robot para DARPA con fines militares que se convertiría en su primer cuadrúpedo autónomo. Construido con ayuda del mismo departamento de la NASA que creó los primeros rovers autónomos un año antes, “ _BigDog_ ” fue concebido como una mula de carga que acompañara a los soldados en terrenos complejos en los que no era posible desplegar vehículos estándar. Continuando con los desarrollos hasta el momento, equipaba una cámara estereoscópica, LIDAR, GPS y una serie de sensores de posición que le permitían correr hasta a 6,4 km/h en terreno accidentado. Su algoritmo de aprendizaje automático permitía que mejorara su comportamiento con la experiencia, lo que agradó enormemente a DARPA, pero sin embargo el motor mono 

67 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

cilíndrico de gas que movía las cuatro patas del robot era tan ruidoso que en 2015 el proyecto se descontinuó porque resultaba imposible desplegar a “ _BigDog_ ” en un combate real. Su novedad principal residía en el empleo de algoritmos de visión artificial para el seguimiento de objetos, conocido como _Object Tracking_ , que le permitía seguir a un humano allá por donde este transitara. 

Durante el año **2006** se menciona por primera vez el término “ _machine reading_ ” definido como la habilidad de una máquina de comprender texto escrito de forma autónoma tal y como lo hace un ser humano. En su artículo “Machine Reading” sostenían que el campo del NLP había llegado a conseguir analizar sintáctica y semánticamente diversas frases pero que nunca había conseguido una auténtica comprensión acerca de lo que estaba leyendo. Para ello, era necesario que las máquinas comprendieran el contexto y pudieran inferir información omitida en un texto de igual manera que lo hacemos nosotros. Como ejemplo decían que la frase “Se fue del restaurante después de disfrutar la comida” no especifica que el cliente pagó la comida, pero que por omisión un ser humano asume que lo hizo. El gran reto del _machine reading_ era obtener esta capacidad de forma no-supervisada, ya que no habría forma de etiquetar este tipo de conocimiento a diferencia de otras tareas en NLP que permitían conocer el resultado antes de la ejecución y entrenamiento de un algoritmo. A partir de este momento, el _machine reading_ se convertiría en uno de los objetivos principales del campo del NLP. 

En el año **2007** el campo de la visión artificial experimenta un salto de gigante con la publicación de ImageNet, una base de imágenes anotadas con el propósito de poder entrenar y evaluar cualquier algoritmo propuesto para la detección de objetos. Su impulsora, la profesora de Princeton Fei-Fei Lei, justificaba su creación en base a la escasa cantidad de bases de imágenes etiquetadas disponibles para la comunidad científica para poner a prueba sus nuevas ideas de arquitecturas para algoritmos de visión artificial. ImageNet, igual que la antigua MNIST, es un conjunto de imágenes accesible por cualquier persona con sus etiquetas, es decir, con un archivo para cada una de ellas que indica el objeto que contienen. En este caso, en vez de enfocarse en dígitos manuscritos de códigos postales del cero al nueve, ImageNet se enfoca en “imágenes naturales” e imágenes del mundo que están etiquetadas con una gran variedad de etiquetas como “anfibio”, “mueble” o “persona”. Las etiquetas se consiguieron gracias a un gran esfuerzo humano, es decir, por medio de etiquetado manual. Para este propósito emplearon una herramienta que pone a disposición de cualquiera AWS, el departamento de cloud de Amazon, llamado Amazon Mechanical Turk. Este servicio permite a cualquier persona proponer tareas sencillas en internet para que cualquiera, a cambio de una pequeña contribución económica, pueda realizarlas. De esta forma, ImageNet fue etiquetado por personas de todo el mundo. En total, hay más de 14 millones de imágenes y más de 20.000 categorías de imágenes. Estas categorías están anidadas, es decir, hay categorías que pertenecen a otras más grandes y así recursivamente. Como veremos posteriormente ImageNet fue uno de los ingredientes clave para el despegue del Deep Learning como tecnología clave de Inteligencia Artificial. 

68 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 



Visualización de algunas de las clases anidades de ImageNet 

En **2008** Google protagonizó uno de los mayores eventos de la década en tecnología de NLP. Hasta el momento, y aunque el NLP había sido un objetivo claro desde los comienzos, los resultados obtenidos habían sido bastante desesperanzadores. En ningún caso, tras décadas de inversión e investigación, ningún grupo de investigación ni corporación había conseguido superar un 80% de acierto en el reconocimiento de discurso ( _speech recognition_ ) lo que limitaba enormemente las aplicaciones reales de esta tecnología. Google desarrolló un método novedoso para implementar esta tecnología. Aprovechando las capacidades de los computadores de última generación y de las novedades en computación paralela, desplegaron miles de computadores que, ejecutando entre todos complejas redes neuronales, fueron aprendiendo a reconocer patrones gracias a la enorme cantidad de datos que Google había recopilado de sus propios usuarios hablando. Tras completar varios ciclos de entrenamiento, Google afirmó que su algoritmo había logrado alcanzar un 92% de precisión. Tal fue el revuelo que causó el desarrollo de este algoritmo, que en noviembre de este mismo año Apple anunció que incorporaría este algoritmo en su reciente iPhone para poder realizar búsquedas en Google por medio de comandos de voz. En ningún caso la respuesta era devuelta en forma de conversación, como si lo harían futuros asistentes conversacionales, sino que se devolvían las búsquedas de Google como si se hubieran realizado por escrito. Con este sistema, Google desbancó otros intentos de competidores como Microsoft Tellme, que buscaba direcciones y números de teléfono, y Yahoo! oneSearch, que permitía hacer búsquedas por voz con una precisión muy limitada. Gracias a este gran adelanto, el campo del NLP volvió a ser reconocido como una tecnología con posibilidades de implementación eral, y empezó a recibir tanto interés como fondos para investigación. 

69 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

En **2009** un investigador de visión artificial llamado Alex Berg sugirió a Fei-Fei Li, creadora de ImageNet, ir un paso más allá y no solo almacenar información acerca del tipo de imagen que era cada una de las almacenadas en la base de datos, sino también la localización exacta de cada objeto. La base de datos original estaba orientada a la clasificación de objetos, es decir, para algoritmos de visión artificial que a partir de una imagen devuelven una clase a la que creen que esta pertenece, como “perro” o “barco”. Si se añadiera información de localización, se podría emplear ImageNet para entrenar y valorar algoritmos de detección de objetos, que no solo clasifican objetos, sino que dicen “perro en las coordenadas X, Y” y que tienen muchas más aplicaciones empresariales reales. Fei-Fei Li consideró oportuna esta adición y junto a Berg publicó cinco artículos científicos explorando cómo procesar esta vasta cantidad de imágenes de forma automática. A partir de esta colaboración surgió el que a día de hoy sigue siendo uno de los retos más importantes en el mundo de la visión artificial, el ImageNet Large Scale Visual Recognition Challenge (ILSVRC). Este reto, abierto a cualquiera que quiera poner a prueba sus algoritmos de clasificación y detección de objetos, tiene tres modalidades. 

Por un lado, está la modalidad original de clasificación de objetos, por otro la localización de un único objeto – por ejemplo, encontrar dónde está el único gato de una imagen – y por otro la detección de objetos – detectar todos los gatos y todos los perros de una imagen – esta última sería la más relevante a partir de 2012 como veremos algo más adelante. 

Con los años, a partir de 2011 la ILSVRC se convirtió en uno de los _benchmarks_ más empleados en el mundo de la investigación de visión artificial, empleado para comparar diversas arquitecturas propuestas por los distintos grupos de investigación para determinar cuál de todas ellas era la que mejor generalizaba un problema de visión artificial específico. 

En **2010** Microsoft lanza el sistema Kinect inicialmente para su consola Xbox 360. A pesar de su lanzamiento original con el entretenimiento como objetivo, Kinect se convertiría en uno de los dispositivos para la estimación de la pose humana en 3D preferidos por los investigadores de visión artificial. La estimación de la pose humana, es decir, de la posición de cada una de sus extremidades, articulaciones, torso, cabeza y extremidades, es un objetivo que ha perseguido el campo de la visión artificial en las últimas décadas ya que proporciona información muy valiosa acerca de las posibles acciones que está realizando un ser humano en un determinado momento. El hardware de Kinnect no era distinto del empleado por los vehículos autónomos de principios de siglo en los que se empleaban cámaras a color RGB y sensores de infrarrojos con cámaras estereoscópicas. El gran avance de Microsoft fue un algoritmo patentado que permitía capturar el movimiento de todo el cuerpo en 3D, pero también el reconocimiento facial gracias a puntos de interés (KPI) de la cara de cada persona y el reconocimiento de voz. 

70 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

En **2011** , tras haber superado exitosamente el desafío de jugar al ajedrez, IBM se embarcó en un desafío mucho más complejo. Se propuso lanzar al mundo un algoritmo de IA que fuera capaz de competir (y ganar) en el concurso estadounidense “Jeopardy!” en el que los participantes reciben preguntas sobre diversos temas como historia, literatura, arte, ciencia, geografía…  El gran reto no era tener almacenadas las respuestas a todas estas preguntas, ya que la tecnología de almacenamiento para el año 2011 era más que suficiente como para tener grabada toda la información precisa. El gran reto era comprender las preguntas que lanzaba el presentador, que estaban formuladas en un lenguaje natural, lleno de expresiones ambiguas, coloquialismos e interjecciones. Para solucionar este problema IBM desarrolló durante años el algoritmo _DeepQA por Questions and Answers_ – Preguntas y Respuestas- basado en numerosas técnicas IA que ya habían sido previamente probadas para NLP previamente. Gracias a la capacidad de cómputo del procesador principal, se podían ejecutar en paralelo varias técnicas y obtener la mejor respuesta posible en el menor tiempo. Watson ganó a sus dos oponentes humanos y se convirtió en un hito en el avance de la IA para el gran público. 

Este mismo año, dos años después de que Google permitiera realizar búsquedas por voz, Apple demostró la velocidad con la que era capaz de mejorar los algoritmos existentes con la presentación en **2011** de Siri, un asistente virtual en iOS basado en Inteligencia Artificial. Apple no ha liberado el código ni lógica subyacente bajo Siri, por lo que los investigadores se limitan a afirmar que los comandos de voz que Siri recibe se convierten a texto y posteriormente se analizan con un motor de NLP para comprender el contenido y el contexto de la petición, lo que desencadena una acción por parte de Siri bien hablada o bien con respecto a otra aplicación. 

También en **2011** , se batió el récord de precisión para la base de datos de dígitos manuscritos MNIST. Un grupo de investigación en Suiza, en concreto en el centro de investigación IDSIA desarrollaron un modelo de Red Neuronal Convolucional que tras ser entrenado con imágenes etiquetadas de MNIST fue capaz de alcanzar una precisión del 99,73% en la identificación de estos dígitos. En este momento, las CNN de reconocimiento de dígitos eran superiores a las habilidades de un ser humano medio, ya que en algunas ocasiones los humanos fallaban a la hora de diferenciar dígitos en escrituras manuales más complejas de lo habitual. 

Por último, este mismo año una Red Neuronal Convolucional alemana superó la habilidad de los seres humanos para reconocer señales de tráfico con un 99,46% de acierto frente al 99,22% humano. Esto supondría un gran paso adelante en la industria del vehículo autónomo ya que por el momento numerosos experimentos habían triunfado en el objetivo de mantener el automóvil dentro de un camino o entre las dos líneas de un carril, pero una de las mayores dificultades de estos sistemas era el cumplimiento de las normas de circulación, por lo que este tipo de avances permitía imaginar vehículos realmente autónomos que pudieran tomar los mandos por completo sin interacción humana. 

71 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

El principio de la segunda década de S.XX, como se puede observar, apuntaba alto en cuanto al uso de las redes neuronales para la automatización de diversos problemas, principalmente relacionados con el lenguaje y la visión artificial. El gran contratiempo de este tipo de algoritmos residía en su gran coste computacional, como llevaba siendo habitual las décadas anteriores. Una CNN requiere analizar todos los píxeles de una imagen una y otra vez para ser entrenada, siendo este proceso lento y, en algunos casos, imposible por las limitaciones de RAM y de potencia de las CPUs de los computadores. Esto cambiaría radicalmente, a partir de 2012 gracias a una innovación que abriría las puertas de la era del _Deep Learning._ Estos algoritmos llevaban existiendo casi tres décadas, pero no habían terminado de despegar por los enormes tiempos de espera que requerían los procesos tanto de entrenamiento como de inferencia de las redes neuronales. Tendría que volver a aparecer Geoffrey Hinton, uno de los padres de la Inteligencia Artificial, para mostrar el camino y abrir una nueva era de la IA, en la que nos encontramos inmersos en la actualidad. 

#### **_Dato importante_** 

**1995** _- Se presenta ALICE, uno de los primero chatbots con capacidad de aprender de cada 1995 conversación que mantiene gracias a los avances en procesamiento y almacenamiento de datos._ 

**1997** _- Deep Blue, uno de los últimos éxitos de los sistemas por fuerza bruta pasados en reglas a priori, vence al campeón del mundo de ajedrez Kasparov, completando un objetivo que perseguía la IA desde sus inicios._ 

_Se publican las LSTM, un nuevo tipo de Red Neuronal Recurrente capaz de aprender de series de datos largas para objetivos en los que la memoria sea importante (conversaciones, seguimiento de objetos en video, etc.)_ 

**2000** _- Se presenta Kismet, el primer robot capaz de reconocer y simular emociones humanas gracias a sistemas muy básicos de NLP y de visión artificial alimentados por micrófonos y cámaras estereoscópicas_ 

**2001** _- Viola y Jones solucionan el problema del reconocimiento facial en tiempo real gracias a su método para el reconocimiento de objetos basado en Haar features_ 

**2002** _- El primer robot doméstico llega al mercado: Roomba limpia el suelo de una vivienda de forma autónoma gracias a sus sensores y algoritmos de guiado_ 

72 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

#### **_Dato importante_** 

**2004** _- La NASA despliega en Marte dos rovers autónomos que emplean visión artificial para seleccionar los caminos menos accidentados hacia un destino concreto._ 

**2007** _- Fei-Fei Lei publica la base de imágenes etiquetas más grande del mundo, llamada ImageNet. Permitirá a numerosos investigadores entrenar y evaluar sus modelos de clasificación y detección de objetos dentro de la visión artificial_ 

**2008** _- Google lanza su aplicación de speech to text en los dispositivos iPhone, obteniendo por primera vez en la historia una precisión mayor del 80% en esta tarea_ 

**2010** _- Microsoft lanza Kinect, con la capacidad de estimar la pose humana mediante un algoritmo novedoso basado en cámaras a color, infrarrojos y micrófonos. Será el estándar del “pose estimation” durante años._ 

**2011** _- La IA de IBM llamada Watson consigue vencer en un concurso de televisión llamado Jeopardy! ejecutando redes neuronales de NLP para comprender las preguntas y buscar las respuestas_ 

_Apple presenta Siri, un asistente virtual basado en IA que se puede instalar en cualquier dispositivo iOS, mejorando los procesos de speech to text, NLP y text to speech conocidos hasta el momento. Nunca se liberó el algoritmo._ 

### **Etapa 6. La era del Big Data y el Deep Learning: desde 2012** 

Ya hemos mencionado la tecnología de Deep Learning múltiples ocasiones a lo largo de esta cronología de la IA, pero en ningún momento hemos llegado a definir con precisión su alcance y significado, que serán detallados en siguientes unidades y módulos pero que nos ayudarán a situar contextualmente los últimos años de desarrollo de la tecnología de sistemas inteligentes. La tecnología de Deep Learning o aprendizaje profundo en español es un subcampo del Machine Learning que se basa en algoritmos inspirados por la estructura del cerebro humano y que tratan de simularlo denominados redes neuronales artificiales. El nombre de aprendizaje profundo proviene de las diversas capas de las que está compuesta una red neuronal. Como ya hemos analizado anteriormente, una red neuronal artificial es un conjunto de neuronas artificiales, también llamadas perceptrones, dispuestas en capas. Cada capa ocupa un orden en el procesamiento de la entrada de una red 

73 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

neuronal, recibiendo datos de la capa anterior y escribiendo datos en la capa siguiente. Originalmente, las capas de una red neuronal se dividen entre capa de entrada ( _input_ ), capas ocultas o intermedias ( _hidden_ ) y capas de salida ( _output_ ). Esta profundidad de capas dentro de un algoritmo es la que da el nombre de profundo, Deep, a todo lo relacionado con entrenamientos y despliegues de redes neuronales dentro de la IA. 

Las redes neuronales, como hemos estudiado, fueron propuestas y desarrolladas a lo largo del S. XX y, además de encontrar cierta resistencia de algunos críticos como Minsky, estuvieron limitadas principalmente por la capacidad de cómputo de las máquinas del siglo pasado. Una red neuronal es un algoritmo que requiere de una gran cantidad de recursos computacionales para poder ejecutar un algoritmo de entrenamiento como el _backpropagation_ ya que requiere analizar y corregir uno a uno todos los millones de parámetros que tiene, lo que requiere una gran cantidad de tiempo y de cálculos que los ordenadores del siglo XX no podían realizar. Fue por ello que, a pesar de conocer los algoritmos desde años atrás, los investigadores de IA no pudieron avanzar en este tipo de tecnología ya que el _hardware_ no los acompañaba. 

No obstante, a día de hoy podemos afirmar que las redes neuronales artificiales como parte del Deep Learning están generando una nueva revolución industrial en la práctica totalidad de sectores económicos. Y todo es gracias a una idea que surgió en 2012 que lo cambió todo. 

Remontando atrás algunos años, en el año 2007, Nvidia era el mayor fabricante de GPUs del mundo. Una GPU ( _Graphics Process Unit_ ) es un componente electrónico, en concreto un procesador, que está diseñado específicamente para poder procesar en paralelo el renderizado de gráficos 3D como los que se emplean, por ejemplo, en los videojuegos. Básicamente son capaces de procesar una gran cantidad de datos matriciales en paralelo, por lo que son de gran ayuda en edición de video y películas y en el diseño y ejecución de juegos con renderizados complejos. Los ingenieros de NVIDIA comenzaron a analizar si esta capacidad de cómputo en paralelo podría usarse para otros fines que no fuera el renderizado 3D, y decidieron publicar un marco de desarrollo o framework denominado CUDA ( _Compute Unified Device Architecture_ ). Esto permitía a los desarrolladores programar sistemas que ejecutaran cualquier tipo de cálculo matricial sobre una GPU permitiendo acelerar enormemente algunos tipos de cálculo muy concretos en procesos con coste computacional alto. A partir de este momento hubo alguna tímida aproximación al empleo de las GPUs de NVIDIA para el diseño, entrenamiento y despliegue de redes neuronales artificiales, como las primeras propuestas iniciales del profesor de Standford y fundador de Coursera Andrew NG en los últimos años de la primera década de S. XX. 

Sin embargo, el gran hito que marcó el comienzo de la era del Deep Learning gracias a la aceleración por hardware habilitada por medio de una GPU fue una Red Neuronal Convolucional (CNN) denominada Alexnet. 

74 

**Módulo. Introducción a la Inteligencia Artificial** 

En el año **2012** , Geoffrey Hinton, padre del algoritmo de backpropagation y su doctorando Alex Krizhevsky de la Universidad de Toronto presentaron en el ImageNet Challenge una red neuronal que había sido diseñada y desarrollada para permitir que su entrenamiento, es decir, que la ejecución de la retropropagación, se produjera sobre una GPU. El resultado fue espectacular, ya que Alexnet fue capaz de acertar correctamente la clase del 84,7% de imágenes. Si bien a día de hoy este puede parecer un número poco espectacular, la siguiente arquitectura clasificada, que se ejecutaba sobre CPUs, solo fue capaz de procesar un 73,3% de imágenes correctamente. En palabras de The Economist en reacción a este hallazgo, “ _De repente la gente ha empezado a prestar atención al Deep Learning, no solo la comunidad de desarrollo de Inteligencia Artificial, sino la industria tecnológica en su conjunto. “_ 

Alexnet sigue siendo una referencia a día de hoy tanto como punto de partida para evaluar y mejorar posibles modelos de CNN aplicadas a visión artificial, como para que alumnos de cursos de Inteligencia Artificial de todo el mundo comprendan el funcionamiento básico de estos algoritmos. A día de hoy, el artículo en el que se presentó esta arquitectura ha sido citado casi 39.000 veces desde entonces. Poco después de conseguir la victoria en el concurso de ImageNet, Alex vendió todos los derechos de su CNN y del método que había empleado a Google, y siguió trabajando allí durante los siguientes cinco años. Gracias a esta adquisición, Google pudo convertirse en el gran impulsor del campo del aprendizaje profundo que es hoy, liderando la investigación y los resultados de la misma desde entonces, aplicando las ventajas que ofrece el _Deep Learning_ a la gran mayoría de sus procesos de negocio 

No solo Alexnet fue una revolución por su precisión a la hora de categorizar imágenes, sino por la velocidad que lograron alcanzar en términos del entrenamiento de una CNN, hasta seis veces más rápido que con algunos de los procesadores más potentes en el mercado. Esto permitía una implantación más fácil en casos de uso reales, ya que hacía viable la inferencia en tiempo real y el entrenamiento en cuestión de horas y no de semanas como había sido hasta el momento, lo que incrementó notablemente el interés de empresas y corporaciones. A modo de ejemplo, en la siguiente imagen se puede observar una comparación de entrenar una CNN para la base de datos de MNIST en una GPU de NVIDIA y en distintos tipos de CPU empleados previamente para esta tarea. 



Comparación de entrenamientos GPU -CPU 

75 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Fue también en el año **2012** cuando Andrew NG, uno de los primeros investigadores en proponer el uso de GPUs para el entrenamiento de CNN, lideró un proyecto que planteó explorar las posibilidades del aprendizaje no supervisado. Hasta el momento, para poder entrenar una red neuronal artificial o cualquier otro algoritmo de Inteligencia Artificial, era necesario proporcionar conocimiento _a priori._ Bien fueran reglas de lógica formal para tratar de razonar, o imágenes de dígitos manuscritos con una etiqueta asociada como en MNIST, los algoritmos necesitaban saber cuál era la respuesta correcta para poder terminar por producir ellos esta respuesta de manera automática eventualmente. Sin embargo, el equipo de Andrew NG decidió cambiar de perspectiva. 

Diseñaron una red neuronal a la que mostraron diez millones de miniaturas de videos de YouTube como conjunto de entrenamiento ( _training set_ ). En aquel año Andrew trabajaba en el laboratorio X de Google, que había adquirido YouTube recientemente, y le proporcionó toda la capacidad computacional que pudiera necesitar. Por ello, diseñó con su equipo una red neuronal a la que no pidieron un resultado concreto, solo le mostraron imágenes sin etiqueta. Una vez hubo pasado por los diez millones de imágenes, comenzaron a tratar de averiguar qué había aprendido la red. Para ello, seleccionaron una serie de imágenes asociadas a conceptos muy concretos. Después, al mostrarle a la red las imágenes, evaluaban si había alguna neurona a lo largo de la red que respondía única y exclusivamente a estímulos de un tipo, lo que implicaría que la red había aprendido por sí sola a clasificar imágenes.  Cuando el equipo de investigación le mostró a la red neuronal imágenes de gatos, una neurona muy concreta se excitaba digitalmente cada vez que en la miniatura había un gato, pero nunca se excitaba ante cualquier otro estímulo. Lo mismo sucedió con el conjunto de caras humanas, que despertaba la actividad de una neurona concreta de esta red neuronal. 

Gracias a este experimento, el interés en el aprendizaje no reforzado, es decir, con poco contexto y guía, comenzó a crecer en el mundo de la IA. 

También en **2012** , el _Dynamic Design Lab_ de Standford presentó _Shelley_ junto al ResearchLab de Volkswagen. Shelley fue el nombre que el equipo le dio a un Audi TTS blanco que equipó con numerosas cámaras a lo largo de la carrocería y con un ordenador central que ejecutaba algoritmos de visión artificial en tiempo real. La principal diferencia de Shelley con otros intentos de conducción autónoma es que era un coche de carreras, corría a tiempos récord en un circuito cerrado. El reto no era que el coche fuera capaz de recorrer el circuito, cosa que se daba por sentada en este momento, sino que reaccionara a eventos imprevistos para mejorar la seguridad vial de los vehículos autónomos. En algunas ocasiones se dejaba al coche sin alguno de sus frenos o se cambiaba forzosamente de trazada para que los algoritmos aprendieran a reaccionar a condiciones no tan idóneas. Esto permitiría futuros desarrollos que facilitarían la legislación del coche autónomo. 

76 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 

En **2013** , un equipo de desarrollo de la Universidad Carnegie Mellon publicó el Never Ending Image Learner, llamado NEIL. El propósito de este algoritmo de visión artificial era “obtener conocimiento común sobre las relaciones que se dan en el día a día”. Con un objetivo tan amplio, el algoritmo empezó a bucear por internet y sigue haciéndolo a día de hoy. Para encontrar dichas relaciones emplea imágenes que extrae arbitrariamente de internet. De nuevo, estamos ante uno de los primeros casos exitosos de aprendizaje no supervisado en el que no se informa a la máquina del dato que está observando, sino que se le presenta una infinidad de datos que debe tratar de comprender. Por ejemplo, NEIL aprendió que los escolares llevan uniforme, que los perros tienen dueños y que los ukeleles se asocian a la playa. Gracias al trabajo de NEIL se pueden generar motores de búsqueda de relaciones visuales que pueden ser útiles para industrias como el entretenimiento y la salud, entre otras. 

En vista del gran interés que sus productos suscitaban en la industria de la Inteligencia Artificial, NVIDIA estuvo desde la presentación de Alexnet desarrollando un sistema de instrucciones primitivas para facilitar el uso de sus tarjetas gráficas para el entrenamiento y despliegue de Redes Neuronales Convolucionales. En **2014** publicó la librería cuDNN, que incorporaba funciones para optimizar funciones como la retropropagación o las convoluciones. La intención era que los desarrolladores de _frameworks_ para el diseño e implementación de _Deep Learning_ como Tensorflow, Caffe o PyTorch pudieran aprovechar las ventajas que ofrecía un hardware de paralelización tan potente sin necesidad de conocer las instrucciones de bajo nivel necesarias como para gestionar los distintos núcleos y la memoria de la GPU. No todos los investigadores se mostraron conformes con las capacidades de cuDNN, pero la realidad es que a día de hoy las últimas versiones de los ya mencionados _frameworks_ de desarrollo se basan en cuDNN para la aceleración de procesos gracias a GPUs y NVIDIA ha logrado convertirse en el fabricante mundial de referencia de tarjetas gráficas orientadas específicamente al tratamiento de algoritmos de aprendizaje profundo. 

En **2014** la competición de ImageNet volvió a tener una gran repercusión en el mundo de la IA cuando la ganadora fue VGGNet, una nueva red neuronal convolucional que aprovechaba el desarrollo de nuevas tarjetas gráficas más potentes y los nuevos marcos de desarrollo para emplear una arquitectura con una cantidad de capas convolucionales muchísimo mayor que las que tenía AlexNet. VGGNet, desarrollada por la Universidad de Oxford, fue la vencedora en el modelo de localización de objetos a diferencia de Alexnet que venció en el reto de clasificación. Por primera vez desde que la competición comenzó a celebrarse, una red neuronal fue capaz de obtener menos de un 10% de errores, lo que tan solo tres años antes era impensable. 

77 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 



En este mismo año, el coche autónomo de Google, que llevaba siendo desarrollado en el laboratorio X desde el año 2009, pasó un examen de conducir oficial en Nevada, Estados Unidos. Si bien no fue puesto a prueba en rotondas, zonas escolares o cruces de pasos a nivel, este vehículo autónomo completó satisfactoriamente todas las pruebas requeridas por el estado de Nevada para obtener una licencia de conducir. Cuando se presentó al examen, el coche de Google, construido sobre un Toyota Prius, había recorrido ya un millón de kilómetros de pruebas antes de poder presentarse al examen. Fue capaz de circular entre el tráfico habitual, detenerse ante la presencia de peatones cruzando la calzada y de ser, en palabras de los examinadores “tremendamente cauto”. 

Este hito en el desarrollo del vehículo autónomo marcó un antes y un después en el terreno legal, ya que el poder legislativo de los distintos estados y países no estaba preparado para tener una regulación que marcara los límites y responsabilidades en la conducción sin conductor. Este hecho sirvió para abrir el debate en numerosas naciones, permitiendo a otras muchas empresas emprender el camino de la investigación para el vehículo autónomo. 

**2014** también fue un año destacado para los sistemas de NLP basados en asistentes virtuales. Después de la presentación de Siri por parte de iOS años antes, las grandes tecnológicas no quisieron quedarse atrás y destinaron numerosos recursos humanos y económicos para la construcción de sus propios asistentes virtuales. Por un lado, Microsoft lanzó Cortana, un asistente virtual orientado a su Sistema Operativo de escritorio Microsoft que llevaba desarrollando desde el año 2009, aunque posteriormente sería ejecutable sobre otras plataformas como Android y finalmente sobre iOS. A diferencia de Siri, que funcionaba en dispositivos móviles, Cortana debía ser capaz originalmente de ayudar a un usuario a configurar su PC, buscar archivos en el mundo y ejecutar comandos y búsquedas en Bing, el buscador de Microsoft, como consultas sobre el estado del tiempo o del tráfico. 

78 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Fue Amazon quien revolucionó la idea de asistente virtual cuando presentó Alexa, un asistente desvinculado de sistemas operativos y dispositivos móviles, un asistente virtual doméstico contenido en un altavoz llamado Amazon Echo. Inicialmente Alexa solo podía completar compras en Amazon, pero con el paso del tiempo acabó siendo un asistente domótico completo basado en el procesamiento y comprensión del lenguaje natural, permitiendo controlar aspectos como la iluminación de una casa o el volumen de un equipo de música. El nombre no fue casual, ya que al contener el fonema “x” era más sencillo conseguir que el sistema siempre reconociera su nombre al ser una consonante fuerte que no suele perderse en ningún idioma. No obstante Amazon trató de convencer al público de que el nombre proviene de la librería de Alejandría ( _Alexandria_ en inglés). 

Sesenta y cuatro años más tarde de que Alan Turing publicara su idea de un test que pudiera demostrar si una máquina es inteligente en base a la forma en la que interactúa con un humano a través de una conversación, es decir, en **2014** , una máquina fue capaz de superar este test por primera vez. Este hito fue conseguido por un chatbot de nombre Eugene Goostman, que simula ser un niño ucraniano con trece años, lo que facilita que el interlocutor pueda confundirlo con un humano debido a su escasa edad. Turing predijo que en el año 2000 las máquinas serían capaces de engañar a un 30% de humanos, y tan solo catorce años más tarde Eugene lo consiguió con un 33% de los jueces que le realizaron la prueba. 

La gran mayoría de expertos en IA, sin embargo, no se mostraron especialmente emocionados por este hito, ya que sostenían que Eugene había sido entrenado única y exclusivamente para pasar el Test de Turing, que llevaba años sin considerarse válido por motivos que ya hemos discutido. Por ello, Eugene generó un gran revuelo mediático y se viralizó en cuestión de días, pero no se considera que aportara ningún avance relevante a la investigación del procesamiento del lenguaje natural. 

Sí que fue, sin embargo, un gran éxito el anuncio de la primera versión del sistema _Auto Pilot_ de Tesla, que fue anunciado en octubre de **2014** para el modelo Model S. Estos coches eran capaces, gracias a tecnología de visión artificial alimentada por cámaras, sensores de proximidad y LIDAR, de mantenerse en el carril con manejo automático del volante, de acelerar y frenar para adaptarse a la velocidad del tráfico o, en ausencia de este, a la velocidad de la vía y del reconocimiento automático de señales de tráfico para informar al conductor y tratar de cumplirlas. Esta primera versión no era realmente autónoma, ya que exigía al conductor siempre tener las extremidades sobre los controles y no perder de vista el coche, porque había numerosos imprevistos que podían desconectar el modo _Auto Pilot_ devolviendo el control manual del vehículo a su piloto. No obstante, los Model S estaban preparados para recibir futuras actualizaciones de software que mejorarían las capacidades de este algoritmo, que en el momento de su lanzamiento ya era capaz de buscar sitio de aparcamiento por sí mismo. 

79 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

En **2014** surgió una de las tecnologías más novedosas de los últimos años, proponiendo un uso totalmente revolucionario de las Redes Neuronales: generar contenido que no existe. Por el momento las aplicaciones del aprendizaje profundo se habían limitado a procesar datos del mundo real, bien fueran imágenes, video, sonido o datos, y generar una salida en consecuencia. Sin embargo, Ian Goodfellow, bajo la dirección de Yoshua Bengio, propuso al finalizar su tesis doctoral un tipo de Red Neuronal totalmente nuevo, las Redes Generativas Adversarias o GAN (Generative Adversarial Networks). Profundizaremos en el funcionamiento de este tipo de red neuronal en futuros módulos, pero la intuición básica es importante para conocer el devenir de la IA hasta nuestros días. Dos redes neuronales participan en un juego de suma cero, es decir, lo que gana una, lo pierde la otra. Una de ellas se especializa en reconocer imágenes de un tipo, por ejemplo, paisajes nevados. Esta es una CNN de clasificación de objetos como otras que ya hemos mencionado, dedicada a diferenciar si una imagen es de un tipo u otro. Es el otro participante en el juego el que es novedoso, ya que está dedicado a generar imágenes inexistentes de una tipología específica (caras, animales, paisajes nevados) que puedan pasar el examen de su contrincante. De esta forma, las imágenes que genera la red Generativa pasan a la red Adversaria, que decide si la imagen cumple con los requisitos del tipo de imagen exigido o no. Este análisis será el motor de la retropropagación de la red Generativa, que aprenderá cada vez a engañar mejor a su rival y por tanto a generar imágenes más reales cada vez. La perfección de las imágenes dependerá de lo bien entrenada que esté la red Adversaria, es decir, de lo perfeccionista que esta sea. Como veremos, las GAN se fueron popularizando con los años hasta ser aplicada en ámbitos tan dispares como la generación de imágenes artísticas, de texturas para videojuegos o los conocidos DeepFakes en los que se generan videos con caras de personas que no están realmente en dicho video. 

En el año **2015** , ante la rápida expansión que claramente estaba viviendo la IA y las capacidades que esta podían ofrecer al mundo, un grupo de investigadores en los campos de robótica, visión artificial e IA, grandes directivos de empresa, fundadores de startups y expertos en nuevas tecnologías firmaron una carta abierta para expresar una de sus mayores preocupaciones relativas a la IA. Durante el congreso internacional más importante de inteligencia artificial, el IJCAI ( _International Joint Conferences on Artificial Intelligence_ ) grandes nombres como Elon Musk, fundador de Space X y Tesla; Steve Wozniak de Apple y el físico y divulgador Stephen Hawking entre otros tres mil nombres pidieron la creación de un tratado internacional para evitar la proliferación de las armas automáticas basadas en inteligencia artificial con propósitos de hacer la guerra. 

Las armas autónomas, que sin una investigación totalmente abierta habían sido investigadas durante décadas por los diferentes ejércitos de las naciones, son armas capaces de seleccionar objetivos y atacar a los mismos sin ningún tipo de intervención por parte de un ser humano. Llegados al punto en el que un coche puede conducir entre el tráfico y aprobar un examen de conducir, en el que un asistente doméstico puede apagar las luces de casa cuando la abandonamos, y en el que una red neuronal aprende automáticamente a diferenciar humanos, en el año 2015 la tecnología estaba más que suficientemente ma- 

80 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

dura como para permitir un desarrollo y fabricación masivos de este tipo de armas. La preocupación de los firmantes de esta carta no estaba limitada a los ejércitos de cada país, que podrían pretender fabricarlas, pero firmar tratados de no uso, sino que el mero hecho de desarrollar estas armas y fabricarlas posteriormente podría implicar que dichas armas cayeran en manos de grupos paramilitares, dictaduras autoritarias o terroristas a través del mercado negro. 

La carta cerraba, no obstante, con un párrafo optimista que se transcribe traducido al español a continuación _“creemos firmemente que la Inteligencia Artificial posee un enorme potencial para beneficiar a la humanidad de múltiples formas, y que la finalidad de este campo de estudio debería ser hacer esto realidad. El inicio de una carrera armamentista en la que se vean implicadas Inteligencias Artificiales militares es una idea terrible, y debe ser evitado por medio de la prohibición de las armas ofensivas autónomas que escapen del control humano.”_ 

En el mismo **2015** , se logró por primera vez que un vehículo autónomo completara un viaje de costa a costa por Estados Unidos, en concreto desde Nueva York hasta San Francisco requiriendo solo de un 1% de intervención humana en todo el viaje de 5.500 km de longitud. Este hito fue alcanzado por la empresa Delphi Automotive. El vehículo fue guiado por numerosas condiciones de terreno, de asfalto a pistas de tierra, así como climatológicas, que no habrían sido posibles poner a prueba en un laboratorio. Es importante recordar que la tecnología de captura de información seguía siendo la misma que a principios de siglo e incluso antes: cámaras a color, cámaras estereoscópicas, LIDAR y radar, en este caso montados sobre el modelo Q5 de la marca Audi. Esto implica que las mejoras exponenciales que se estaban viviendo en el mundo del vehículo autónomo estaban principalmente motivadas por mejoras constantes en los algoritmos de Redes Neuronales que procesaban la entrada de estos sensores y eran capaces de seleccionar las mejores acciones posteriormente gracias a una gran velocidad de cómputo en base a los nuevos dispositivos hardware embarcados en los vehículos, como GPUs dedicadas. 

Poco después, Tesla Motors habilitó la versión número 7 de su software _Auto Pilot_ , inicialmente en los Estados Unidos, por una actualización telemática a todos los Model S que ya estaban circulando por las calles que mejoraba notablemente las capacidades de conducción en situaciones reales, pero que todavía no era capaz de detectar peatones ni ciclistas en tiempo real por lo que requería la atención completa del conductor en todo momento, preparado para actuar si fuera necesario, lo que todavía limitaba en gran medida las ventajas teóricas de un vehículo autónomo. Sin embargo, a partir de este momento, los vehículos de Tesla fueron los primeros en acercarse al nivel 3 de autonomía de la escala del NHTSA, todo un hito para la conducción autónoma en condiciones reales. 

La clasificación de los vehículos autónomos es, de forma muy resumida, la siguiente: 

81 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 

- Nivel 0. Sin automatización. Todos los controles y decisiones están supeditados a las decisiones del piloto humano, incluso si hay sistemas de avisos inteligentes como lectura de señales o avisos de cambio de carril. 

- Nivel 1. Asistencia al conductor. El algoritmo es capaz de decidir sobre el ángulo del volante o sobre la aceleración/deceleración del vehículo, siendo el humano responsable de los mandos del control no automatizado y de la monitorización del entorno para detectar posibles peligros en el mismo. El algoritmo necesita confiar en la intervención humana ante imprevistos. 

- Nivel 2. Automatización parcial. El algoritmo toma decisiones tanto sobre el ángulo del volante como de la velocidad del coche, por lo que el humano solo debe estar atento ante cualquier imprevisto, pero en situaciones normales no necesita manipular los mandos del vehículo. En este caso, el algoritmo carece de la capacidad de reaccionar ante estímulos anormales, pero es autónomo en situaciones estables. 

Hasta el Nivel 2 es el humano el que monitoriza el entorno, en busca de posibles peligros que requieran una actuación de emergencia. Desde el Nivel 3 en adelante es el sistema autónomo el que monitoriza constantemente el entorno, aunque no siempre sea capaz de actuar en consecuencia. 

- Nivel 3. Automatización condicional. El algoritmo de conducción autónoma se encarga de absolutamente todos los mandos y controles del vehículo, siendo capaz de reconocer peligros como peatones, animales u otros vehículos pequeños, pero en algunas ocasiones sin capacidad para reaccionar a tiempo, necesitando que el humano pueda reaccionar tomando el control solamente cuando el vehículo lo requiera. 

- Nivel 4. Alta automatización. En este caso el vehículo autónomo puede no ser capaz de tomar la mejor decisión ante un peligro inesperado en el entorno, pero siempre debe de ser capaz de, incluso si el humano no responde cuando se le requiere, parar de forma segura el vehículo y apagar el motor para evitar daños mayores 

- Nivel 5. Automatización completa. En este nivel de automatización el vehículo no necesitará nunca intervención humana, siendo siempre capaz de responder a tiempo y adecuadamente a cualquier imprevisto que suceda dentro o fuera del coche. 

Es por esta clasificación que en **2015** Tesla causó tal revuelo con un sistema que rozaba el nivel 3 de automatización, porque por fin parecía posible que un vehículo circulara sin necesidad de un humano pendiente en todo momento. 

En noviembre de **2015** Google liberó la que sería, como veremos, una de sus mayores contribuciones al desarrollo de _Machine Learning_ y en concreto del _Deep Learning._ Desde hacía cuatro años, el departamento de _Google Brain_ había estado desarrollando un 

82 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

sistema propietario de Machine Learning centrado en Deep Learning. Numerosas empresas dentro de Alphabet, la matriz, empezaron a usar este sistema denominado DistBelief. Gracias a la contribución de algunas de las mentes más brillantes del campo de la IA como Jeff Dean y el ya mencionado Geoffrey Hinton, Google modificó este sistema para que fuera capaz de ser ejecutado en múltiples CPUs y GPUs al mismo tiempo, siendo así capaz de ejecutar el algoritmo de retropropagación de Hinton y aumentando notablemente la precisión de los modelos. Esta nueva versión cambió de nombre, y se presentó al mundo bajo el nombre de Tensorflow en 2015. A diferencia de su antecesor, Tensorflow era un sistema de código abierto gratis, por lo que cualquiera podía emplear sus librerías y funciones para construir modelos de redes neuronales. Entre sus múltiples ventajas, Tensorflow puede ser usado en una gran variedad de lenguajes de programación: Python, JavaScript, C++ y Java, lo que permitió que se expandiera rápidamente entre la comunidad de desarrolladores a lo largo del mundo. Además, aprovechaba las capacidades de la librería CUDA de NVIDIA para optimizar sus librerías cuando estas se ejecutaban en tarjetas gráficas de esta compañía. 

Tensorflow proporciona a los desabolladores la capacidad de diseñar sus redes neuronales desde el punto que quieran. Estos pueden seleccionar capas de neuronas predefinidas para construir redes neuronales “por piezas”, o bajar al nivel de detalle de cada neurona y modificar sus parámetros como se desee. Estas funciones están optimizadas por ingenieros en Google, así como todos los algoritmos de aprendizaje disponibles. En menos de un año desde su lanzamiento, más de 1.500 repositorios de GitHub habían hecho referencia a las librerías de Tensorflow, algo considerado todo un éxito por parte de Google. 

En **2015** se presentó el que sería, y a día de hoy sigue siendo, uno de los algoritmos de detección de objetos más importantes para todos los investigadores de visión artificial, YOLO (You Only Look Once). Hasta este momento, los algoritmos de detección de objetos contaban con dos redes neuronales diferenciadas. Por un lado, ejecutaban una Red Neuronal Recurrente (RNN) para generar recuadros en torno a objetos, de tal forma que pudieran separar unos de otros. Posteriormente, estos recuadros pasaban por una Red Neuronal Convolucional (CNN) de clasificación, para así conocer la tipología de los objetos recuadrados. La filosofía de YOLO cambió esta perspectiva con su novedosa aproximación de “mirar solo una vez”. Para ello, diseñaron una única CNN que en una única pasada fuera capaz de generar los recuadros y las clases asociadas a los mismos. Para ello, dividía la imagen en una cuadrícula y en cada casilla trataba de detectar la clase asociada a la misma, así como los posibles márgenes de objetos. Después, superponiendo esta información, obtenía una clasificación de objetos que superaba con creces la precisión de modelos anteriores, pero que también reducía enormemente el tiempo de cómputo hasta permitir una detección en tiempo real sobre GPUs de NVIDIA que hacían posible el procesado en continuo de señales de video hasta 25 fps. Posteriores versiones de YOLO mejorarían la precisión y velocidad del algoritmo, convirtiéndolo en uno de los más empleados a día de hoy en sus últimas versiones, como veremos próximamente. En la siguiente imagen se puede observar la táctica que sigue YOLO para detectar objetos. 

83 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 



Por último, en este prolífico año para la IA, el algoritmo de Viola-Jones fue capaz de ser implementado y ejecutado en tiempo real sobre dispositivos móviles y sistemas embarcados, así como navegadores web permitiendo que se empleara este algoritmo en cámaras digitales para detectar caras, en teléfonos móviles, pero también en video-llamadas para girar la cámara hacia el hablante y en interfaces de usuario. En esta década todos los algoritmos que habían sido desarrollados durante los últimos cuarenta años comenzaban a encontrar su hueco en el mercado gracias a esta nueva capacidad de cómputo sin precedentes, así como al creciente número de investigadores dedicados a este campo de estudio. 

En **2016** , Deep Mind, empresa parte del conglomerado Alphabet, matriz de Google, devolvió al mundo de la IA uno de los retos más longevos en el campo: derrotar a maestros humanos en juegos de mesa complejos. Desde que en 1997 Deep Blue venciera al campeón mundial de ajedrez, numerosos algoritmos de fuerza bruta habían ido perfeccionándose y ejecutándose en tiempo real en más dispositivos gracias al constante crecimiento de MIPS en el _hardware_ comercial. Sin embargo, había un juego de mesa que aún se resistía a este tipo de sistemas clásicos basados en el cálculo de movimientos y selección por probabilidad de ventaja en base a grandes bases de datos de partidas jugadas: el Go. El Go es un juego que se originó en China hace más de tres mil años. En él, dos jugadores que usan cada uno piezas blancas y negras respectivamente, se turnan para colocar sus piezas en el tablero. El objetivo es rodear y capturar las piezas del oponente para convertirlas en propias. Una vez todos los movimientos posibles de la partida han sido ejecutados, se cuentan las piezas de cada color y el más alto gana. 

84 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

A pesar de lo complejo de sus reglas, el Go es uno de los juegos más complejos jugado por el ser humano, con 10¹⁷⁰ posibilidades en una sola partida, más que átomos hay en el universo. Esto convierte al Go en un juego googol veces más complejo (googol = 10¹⁰⁰) que el ajedrez. Por este motivo, un sistema basado en un cálculo de los distintos movimientos posibles jamás es capaz de superar más que a un jugador amateur, porque el Go no permite que el juego sea puramente matemático. La intuición y la estrategia son piezas tan importantes si no más para hacerse con la victoria. 

Para capturar este componente intuitivo del Go, Deep Mind presentó Alpha Go, un sistema que combina árboles de búsqueda con redes neuronales profundas. Una de estas redes neuronales, denominada “policy network” selecciona el siguiente movimiento a ejecutar empleando la situación del tablero como entrada. Otra red neuronal, “value network”, predice el ganador de la partida. Inicialmente AlphaGo jugó contra jugadores aficionados hasta que alcanzó un nivel suficiente como para vencerles en todas las ocasiones. A partir de este momento jugó miles de partidas contra sí mismo, aprendiendo de sus errores en cada ocasión. 

Cuando sus desarrolladores consideraron que estaba preparado, le enfrentaron al considerado como el mejor jugador de Go, el jugador coreano Lee Sedol en el Hotel Four Seasons de Seúl. El resultado fue de 4-1, otorgando la victoria a AlphaGo, que fue definido como “creativo” e “intuitivo” por los comentaristas en la retransmisión en directo de la partida. A pesar de su derrota, Lee Sedol fue el único ser humano capaz de vencer a AlphaGo. Para ejecutar los algoritmos de AlphaGo eran necesarias 1920 CPUs y 280 GPUs que estaban alojadas en servidores en la nube de Google en Estados Unidos. 

Este proceso de aprendizaje por medio del refuerzo positivo en caso de ganar, y por medio del refuerzo negativo en caso de perder, es denominado Reinforcement Learning. 

La victoria de AlphaGo sobre Lee Sedol y la cercanía del Auto Pilot de Tesla a un vehículo autónomo completo, entre otros hitos de la IA en los últimos años, ejercieron un efecto novedoso para los investigadores más longevos en el campo de la IA. Si durante las últimas décadas de S. XX el campo de la IA había tenido que rechazar sus tesis más optimistas para evitar ser olvidados por los organismos financiadores, en este momento el efecto contrario se estaba dando. Fruto de la cautela que produjeron los dos inviernos de la IA, muchos investigadores consideraban que la humanidad todavía estaba lejos de conseguir máquinas que condujeran por sí mismas o que ganaran a los juegos más complejos. Estas victorias de los sistemas inteligentes les empujaron hacia recuperar un optimismo perdido; por primera vez la realidad superaba las expectativas. 

**2016** fue el año en el que la IA y, en concreto, el Deep Learning, se democratizaron a nivel global. Hasta este momento cualquier investigador o empresa que quisiera desplegar un sistema de aprendizaje profundo necesitaba realizar una inversión inicial en servidores con potentes CPUs y GPUs además de cantidades de memoria mayores a las de un servidor empresarial estándar, lo que suponía una barrera de entrada derivada del coste que 

85 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

impedía a pequeñas universidades y empresas sumarse a la ola expansiva de la IA. Para tratar de cubrir este nicho en el mercado, los grandes proveedores de cloud, denominados _hyperscalers_ como AWS (proveedor de cloud propiedad de Amazon), Google Cloud e IBM desplegaron un nuevo tipo de servicio a demanda basado en Inteligencia Artificial 

En mayo de **_2016_** IBM lanzó su servicio Watson Visual Recognition. Con un nombre heredado de la IA que ganó “Jeopardy!” cinco años atrás, este servicio funcionaba como un SaaS ( _Software as a Service_ ) basado en la nube. Watson Visual Recognition es un servicio que permitía a las distintas empresas analizar y comprender automáticamente el contenido de una imagen empleando un modelo de visión artificial estándar, o incluso entrenar su propio modelo de visión artificial para reconocer objetos específicos de su dominio de negocio. Los clientes pueden contratar este servicio a través de una página de IBM y lanzar los entrenamientos de sus propios modelos de clasificación y detección de objetos directamente desde el navegador web. La facturación se realiza por uso, es decir, a final de mes el cliente abonará a IBM una determinada cantidad por cada entrenamiento realizado y por cada imagen analizada automáticamente. De esta forma, ya no era necesario adquirir un servidor con una inversión inicial, sino que por una cantidad realmente asequible todo el mundo podía usar modelos de visión artificial para optimizar sus procesos de negocio. 

De igual forma que IBM democratiza en mayo el acceso a modelos de visión artificial, Google hizo lo propio con modelos de NLP (Procesamiento del Lenguaje Natural) en julio de **2016** . Introdujo en su catálogo de Google Cloud APIs para el uso de sistemas de comprensión del lenguaje natural y de paso de texto a audio y viceversa. Los modelos que Google llevaba años desarrollando para sus productos internos estaban de repente disponibles para cualquiera por medio de una API, una interfaz de mensajes para ejecutar aplicaciones de forma remota. Inicialmente los servicios de NLP de Google Cloud estaban disponibles para inglés, español y japonés. Entre otras funcionalidades, se encontraban las siguientes. 

- Análisis de Sentimiento: Esta API recibe un texto completo y, tras procesarlo, devuelve una etiqueta de sentimiento general detectado en el texto. Estas etiquetas pueden ser, entre otras, optimista, formal, dubitativo, molesto, decepcionado… 

- Reconocimiento de entidades: A partir de un texto completo, un sistema de reconocimiento de entidades es capaz de identificar y reconocer los conceptos más relevantes para cada bloque de texto, y etiquetarlos por tipos como personas, organizaciones, ubicaciones, eventos, productos, marcas, media… 

- Análisis de sintaxis: Gracias a este módulo, Google ofrece la capacidad de identificar las distintas partes del discurso para así poder crear árboles de dependencia en cada oración, pudiendo así revelar la estructura del texto y, lo que es más importante, su contenido. 

86 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

- Categorías: Este último módulo permite clasificar un texto en diversas categorías de contenido como pueden ser: Arte, Animales, Cultura, Deportes, Tecnología, Ciencia… 

Entre otros usos Google ofrecía como ejemplos la revisión automática de productos vendidos a través de plataformas online y el análisis de sentimiento de llamadas en centros de llamadas masivos para telemarketing. Google proporciona a todos sus potenciales clientes la capacidad de poner a prueba las capacidades de su API de lenguaje natural mediante una demo que puede accederse en el <u>siguiente link alojado en los servidores de</u> Google Cloud. 

En la siguiente imagen se puede observar el resultado de una consulta de descubrimiento de entidades sobre un artículo de periódico relativo a descubrimientos sobre la ley de la relatividad de Einstein en 2021, en las que Google marca en rojo los nombres de personas, en amarillo los eventos, en verde las ubicaciones, y en gris otros conceptos. 



87 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Por otro lado, Google presentó en el mismo formato su API de Speech to Text (STT) accesible igualmente desde su cloud. Esta API es capaz de convertir voz humana a texto para emplearla en casos de uso como generación de subtítulos en tiempo real, permitir a usuarios interactuar con cualquier sistema a partir de la voz hablada y convertir interlocuciones habladas a texto para poder procesarlas posteriormente con un algoritmo de NLP como los que el propio Google ya hemos visto que ofrecía. En paralelo, surgió la opción contraria, denominada Text to Speech (TTS), que hacía exactamente lo opuesto, es decir, generar un archivo de audio en el que una IA pronuncia las frases que recibe como entrada. Gracias a esto, se puede completar el flujo de interacción auditiva con usuarios de cualquier interfaz y personalizar las comunicaciones hacia estos. 

Estos servicios serían posteriormente ofrecidos por otros proveedores de cloud como IBM por medio de Watson Speech to Text (cuya demo puede consultarse aquí) o AWS Polly, el servicio de Amazon para convertir texto en habla verosímil. Un ejemplo de AWS Polly es accesible desde <u>este enlace.</u> 

En mayo de **2016** , Google anunció un nuevo tipo de unidad de procesamiento, distinto de las CPUs y de las GPUs que se habían usado hasta el momento para la ejecución y entrenamiento de algoritmos de Deep Learning. La nueva unidad de procesamiento de Google recibió el nombre de Unidad de Procesamiento de Tensores (TPU), un circuito integrado diseñado específicamente para la ejecución de redes neuronales y en concreto las convolucionales. Gracias a las TPUs y a la optimización de Tensorflow para ejecutar sus modelos sobre estas, el despliegue de redes neuronales para casos de uso industriales en los que la inferencia en tiempo real es crítica amplió enormemente sus posibilidades. 

También en **2016** , la empresa Hanson Robotics con base en Hong Kong usó la tecnología de texto a voz de Google Cloud para desarrollar el primer robot de la historia en conseguir la nacionalidad de un país. Este robot, llamado Sophia por ser la traducción de “sabiduría” en griego. Sofía es un robot humanoide con capacidad de escuchar y comprender lo que le dicen los seres humanos – gracias al Speech to Text de Google cloud – así como de procesar mínimamente lo que percibe por medio de las cámaras a color que posee. Su IA mezcla una gran cantidad de algoritmos de todas las épocas, desde redes neuronales a NLP pasando por sistemas expertos. Gracias a la visión artificial, Sophia puede clasificar las caras de los seres humanos que la rodean en distintos estados anímicos gracias a una CNN de clasificación de objetos, así como simular emociones mediante los servomotores de su cara artificial para simular empatía con los seres humanos. La realidad es que numerosas interacciones de Sophia están moduladas en tiempo real, por lo que hay investigadores de IA que consideran que se le presta más atención de la debida a este robot humanoide. Sea como sea, Arabia Saudí concedió la ciudadanía a este robot “inteligente”, siendo así el primer país del mundo en hacer algo similar a esto. 

88 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

También en **2016** la comunidad científica presenció lo que algunos consideraron como una advertencia acerca de los límites de la IA mientras que otros sencillamente lo consideraron una divertida anécdota. En este año Microsoft desarrolló un chatbot, o bot conversacional, diseñado para operar en la red social Twitter. Originalmente Tay fue diseñada para imitar con la mayor precisión posible la interacción de una mujer estadounidense joven, pero con capacidad de aprender de la experiencia de las distintas conversaciones mantenidas con los usuarios de Twitter. En cuanto comenzó a hablar con diversas personas, una gran mayoría de ellas comenzó a hacerle preguntas políticas y a darle respuestas exaltadas y exageradas sobre la realidad. En este caso, el conjunto de entrenamiento fue el comportamiento del usuario medio de Twitter. El resultado no se hizo esperar y a las dieciséis horas de su lanzamiento, ocurrió el desastre para Microsoft. Tay comenzó a hacer comentarios racistas, extremadamente sexuales y antisemitas como resultado de su proceso de aprendizaje. Parte de los algoritmos de Tay, de los que se conocen pocos detalles, estaban diseñados para que Tay repitiera y parafraseara respuestas que ya había recibido, un comportamiento que ya se conocía con ELIZA muchas décadas antes. Microsoft apagó este chatbot tan pronto como tuvo constancia de estos comentarios y prometió que “investigaría lo sucedido para poder traer a Tay de vuelta una vez tuviera la capacidad de identificar comportamientos abiertamente malintencionados.”. No obstante, cuando unas semanas después volvieron a activar a Tay, esta publicó tweets acerca de drogarse delante de la policía y Microsoft decidió abandonar el proyecto definitivamente 

En **2016** , siguiendo la tendencia marcada por sus competidores, Google sacó al mercado Google Home, un altavoz inteligente con funcionalidades muy similares a Alexa que empleaba sus librerías de NLP para poder interactuar con los habitantes de una casa y así actuar como un asistente personal para ayudar a los usuarios a recordar tareas, crear reuniones, consultar búsquedas en Google por medio de su voz e interactuar con los diferentes aparatos IoT (Internet of Things) en su casa como bombillas inteligentes o electrodomésticos conectados. Gracias a esta solución, Google comenzó a recopilar innumerables comandos de voz de sus usuarios que pudo emplear para someter a sus librerías de NLP a una mejora constante por medio de reentrenamientos periódicos para mejorar la precisión de las mismas. 

AWS respondió al lanzamiento de APIs de _Machine Learning_ de sus competidores con el lanzamiento de Amazon _Rekognition_ , su servicio de análisis de imágenes en cloud. De forma similar a Watson Visual Recognition, el sistema de AWS permite identificar no solo objetos, sino también objetos y realiza una funcionalidad tan interesante como controvertida, el reconocimiento facial. Con _Rekognition_ se pueden comparar rostros para conocer la similitud entre ellos y de esta forma reconocer personas en imágenes o videos. Igual que en el resto de servicios cloud, en AWS _Rekognition_ solo se paga por el uso que se haga del servicio, evitando tener que invertir en la infraestructura subyacente. En la siguiente figura se puede observar el resultado de un análisis de _Rekognition_ sobre una fotografía de stock. 

89 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 



Resultado obtenido tras la consulta de una imagen de stock a AWS Rekognition 

En **2017** Libratus, diseñado por la Universidad Carnegie Mellon, ganó a los cuatro mejores jugadores de Texas Hold‘em póker. Para el entrenamiento de Libratus se aprovecharon las capacidades de computación que ofrece el supercomputador del Pittsburgh _Supercomputing Center_ en el que se entrenaron los modelos basados en teoría de juegos computacional que consiguieron vencer en un juego más que se consideraba demasiado complicado para las máquinas. En este caso, la complejidad del póker reside en la falta de información a la que se enfrenta un jugador a la hora de tomar decisiones, a diferencia del ajedrez o del Go en los que toda la información se puede capturar observando el tablero y las piezas que se encuentran sobre el mismo. Libratus huía de la aproximación de la IA tradicional, como la de Deep Blue, y trataba de emplear técnicas menos habituales. En su cálculo del mejor movimiento no solo tenía en cuenta la información que disponía, sino la incertidumbre sobre la situación del contrincante y, lo que fue más innovador, la información que debía tratar de ocultar a su contrincante por medio de las acciones a realizar. Cada partida que jugaba contra sus rivales o contra sí mismo era capaz de ajustar su algoritmo de teoría de juegos (GTO) para tener una estrategia más depurada. Tras esta victoria, el investigador principal, Tuomas Sandholm, fundó una empresa denominada Strategy Robot que fue subcontratada por el ejército de los Estados Unidos para emplear las capacidades estratégicas de Libratus en pos de un despliegue optimizado de tropas sobre el terreno de combate. La carta contra las armas de IA de hacía dos años estaba cada vez más de actualidad. 

Ya en **2017** , el equipo que desarrolló inicialmente el sistema de AlphaGo en Deep Mind, parte de Google, publicó en Nature un artículo científico en el que presentaban a la comunidad su nueva versión AlphaGo Zero. En esta nueva versión del modelo, los desarrolladores decidieron prescindir de la información generada por humanos para el entrenamiento del algoritmo. En vez de entrenar al algoritmo por medio de partidas jugadas contra otros aficionados al Go, afrontaron el problema con una perspectiva novedosa: La máquina jugaría única y exclusivamente contra sí misma. Sencillamente conociendo las reglas del juego, comenzarían partidas entre dos instancias del algoritmo, que mediante el ya explicado _Reinforcement Learning_ , sería capaz de ir seleccionando los mejores comportamientos que pudieran llevarle a la victoria y eliminando aquellos que le hacían 

90 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

perder contra sí misma. Esta versión fue capaz de ganar a la versión original de AlphaGo que derrotó a Lee en tres días, con un apabullante resultado de cien victorias frente a cero de su antecesora. En tan solo cuarenta días de juego fue capaz de superar a ningún otro algoritmo de Go, así como a ningún otro humano, siendo el mejor jugador de Go conocido de todos los tiempos. Para tener una referencia, en un solo día de jugar desde cero, era capaz de ser un mejor jugador de Go que ningún otro ser humano conocido. Llegados a este punto, la información generada por la IA en ciertos casos de uso parecía ser incluso más valiosa y precisa que la generada por humanos, incluso cuando la IA no sabía ejecutar un cierto problema con unas reglas conocidas. Esto hizo cambiar la perspectiva de muchos teóricos de la Inteligencia Artificial porque, si esto era así, ¿cuál era el papel residual del ser humano? 

En este mismo año el _Facebook Artificial Intelligence Research Lab_ , fundado por Yann LeCun, desarrolló y publicó dos chatbots con esta misma aproximación. En lugar de mejorar sus capacidades por medio de un aprendizaje supervisado generado mediante interacciones reales con humanos, se plantearon qué sucedería si, una vez un chatbot era capaz de mantener una conversación, su aprendizaje se producía por medio de una conversación con otro chatbot. Después de la experiencia del bot xenófobo de Microsoft, los investigadores de NLP estaban preocupados por la posible influencia que pudiera tener la situación coyuntural en un momento determinado en las capacidades de su agente conversacional en el futuro. El resultado, sin embargo, excedió las expectativas de todos los investigadores involucrados en el proyecto. Para poner a prueba estas capacidades diseñaron un sistema de negociación entre los agentes inteligentes. Cada uno de ellos debía conseguir una serie de objetos virtuales que había en disputa con el otro, para lo que tenía que ser capaz de negociar, hacer concesiones y aplicar teoría de juegos como hiciera Libratus en este mismo año. En la siguiente imagen puede verse un diagrama de flujo aplicado por los agentes para negociar entre ellos por objetos cotidianos, como libros o sombreros. 



91 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Información como la mostrada en la imagen anterior es proporcionada a los agentes conversacionales con anterioridad a su conversación, de tal forma que tengan ambos un punto de partida para comenzar a negociar. La dificultad de este propósito negociador es que Facebook, a diferencia que DeepMind con el Go, no había elegido un juego con las reglas claras a priori. Todo lo contrario, la negociación es un arte basado en la intuición y no hay reglas ni estrategias más válidas que otras. El objetivo final de los chatbots, en definitiva, no era aprender a comprender el inglés y hablar con soltura en este idioma, sino lograr el máximo beneficio dentro de una negociación, para lo que el idioma en el que se comunicaran era indiferente. Por tanto, los dos sistemas inteligentes empezaron a deshacerse de las partes del inglés que su algoritmo de aprendizaje por refuerzo no consideraba importantes, y comenzaron a quedarse solo con partes de frases que afectaban a la negociación como “necesito”, o “quiero”. Si un humano hubiera sido la contraparte de uno de estos chatbots, esto no habría ocurrido porque habría sido imprescindible emplear un lenguaje correcto para poder comunicarse. Al dejar a la simulación de la IA todo el trabajo del entrenamiento, se descubrió que esta perspectiva no era siempre la más adecuada, y se terminó el proyecto. Es importante recalcar que los sistemas inteligentes cumplieron su cometido, ya que acabaron siendo unos expertos negociadores. Eso sí, al final, como se puede comprobar en el siguiente extracto de conversación entre ellos, solo se entendían entre ellos dos, haciendo imposible un uso comercial de sus habilidades. A la izquierda se puede observar una conversación inicial, y a le derecha otra una de las últimas conversaciones que mantuvieron. 



En **2017** se empleó la tecnología de las GAN, desarrollado por Ian Goodfellow para generar por primera vez caras de seres humanos que jamás han existido, sencillamente siendo capaz de engañar a su red adversaria de detección de humanos. Este desarrolló se realizó bajo el paraguas de un proyecto llamado “This person does not exist” (esta persona no existe). Entrenando una red capaz de generar caras de seres humanos tan reales como las de aquellos que existen, se empleó como forma de llamar la atención acerca de las enormes posibilidades de la IA, pero también del riesgo que esta puede suponer si no se emplea adecuadamente. Una de las propuestas de su creador, Phillip Wang, era generar identidades falsas en páginas web de dudosa confianza para evitar ofrecer nuestra fotografía a las mismas. Sin embargo, no es difícil imaginar posibles usos maliciosos de esta tecnología. Se puede ejecutar el algoritmo en tiempo real en la <u>página web, que tiene una</u> versión actualizada del algoritmo en la que cada vez que se recarga la página se genera 

92 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

la fotografía de un ser humano que jamás ha existido. Es sencillamente un conjunto de píxeles que nuestro cerebro, igual que la red adversaria, reconoce como un ser humano perfectamente formado y válido. Es importante recordar que en ningún caso se trata de mezclar imágenes previamente conocidas, sino que cada pixel de las imágenes que se crean ha sido producido por un algoritmo de Inteligencia Artificial ejecutado sobre una potente GPU. 

Ya en enero de **2018** , la carrera por ser el primero en diseñar y entrenar un modelo de IA que resolviera un problema perseguido desde hace tiempo se desplazó desde los juegos de mesa hacia la comprensión lectora. En una carrera que se resolvió con menos de 24h de diferencia, el gigante tecnológico chico Alibaba y Microsoft desarrollaron sistemas inteligentes específicamente diseñados para examinarse de un examen de comprensión lectora realizado por la Universidad de Stanford llamado SQuAD. Este examen consiste en una batería de cien mil preguntas acerca del contenido de más de quinientos artículos de Wikipedia, que deben ser respondidas con precisión. Los temas son de lo más variados, desde deportes (“¿Dónde se celebró la edición número cincuenta de la Super Bowl?”), hasta literatura y ficción (“¿De qué planeta viene Doctor Who?”). La nota promedio de un ser humano es de 82,3/100, mientras que la IA de Alibaba consiguió un 82,4 tan solo un día antes de que el sistema de Microsoft la superara por tan solo dos décimas marcando el récord en 82,6 puntos. Tanto Alibaba como Microsoft comenzaron a aplicar sus sistemas diseñados en este reto para hacerse cargo de diversas llamadas al servicio de atención al cliente de cada una de las compañías, con resultados muy positivos. 

En este año, el gobierno de China se comprometió con la industria de la Inteligencia Artificial para tratar de encontrar un hueco en un mercado que, hasta el momento, estaba saturado de actores occidentales. Para ello, lazó un plan de ciento cincuenta billones de dólares americanos para el desarrollo de esta tecnología junto a empresas nacionales como Alibaba o Tencent. 

En el primer mes de **2018** también, Facebook publicó su librería Detectron. Si bien hemos mencionado con anterioridad la presentación por parte de Google de un _framework_ de desarrollo para Deep Learning denominado Tensorflow, Facebook también presentó el suyo con notable menos éxito, al que denominó Caffe2. Sobre este _framework_ , que tenía funcionalidades muy similares a las de Tensorflow permitiendo a los desarrolladores publicar y poner a prueba sus redes neuronales de una manera sencilla, construyó la plataforma Detectron. Esta plataforma contenía una serie de algoritmos esenciales en visión artificial, en concreto para la clasificación y detección de objetos, que cualquiera podía reaprovechar y entrenar para sus propios propósitos sin tener que desarrollar los algoritmos de redes neuronales desde cero. Pero la gran innovación por parte de Facebook fue la incorporación de un objetivo de la visión artificial que, hasta el momento y por limitaciones técnicas, no había sido posible llevar al gran público; la segmentación de objetos. 

93 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 



La segmentación de objetos, como se puede observar en la figura anterior, consiste en identificar cada pixel de los objetos detectados, en lugar de sencillamente dibujar un rectángulo que los contenga. Este objetivo es más complejo que la detección de objetos porque implica que la CNN reconozca los bordes precisos de un objeto. Gracias a la plataforma Detectron, los investigadores del grupo FAIR (Facebook Artificial Intelligence Research) publicaron Mask-RCNN, una red neuronal recurrente destinada la segmentación de objetos que se ejecuta sobre una GPU de Nvidia con soporte para CUDA. El código, desarrollado en Python, fue liberado por Facebook con el objetivo de permitir acelerar la investigación en todos los laboratorios que desearan aprovechar las capacidades de esta plataforma, de tal forma que puedan construir sus proyectos sobre bases sólidas y así ahorrar en tiempo y recursos, pudiendo enfocarlos en las particularidades de sus investigaciones. 

En marzo de **2018** , el primer autobús totalmente autónomo con licencia para circular en una línea estándar con pasajeros consiguió el permiso para hacerlo en una pequeña ciudad en Suiza llamada Neuhausen Rheinfall. Hasta el momento se habían propuesto numerosos prototipos de autobús autónomo, pero ninguno había escalado hasta la misma posición que uno conducido por conductores humanos hasta que el pequeño bus eléctrico de la compañía CNN Supercharged consiguió ser el primero. Denominado “Trapizio”, prescinde totalmente de pedales o volante, ya que al tener un nivel 5 de autonomía en la teoría, en ningún caso hay un conductor humano analizando el entorno. No obstante, este vehículo no es un vehículo de propósito general, ya que siempre realiza la misma ruta, saliendo del mismo punto y llegando al mismo destino, con las mismas paradas previamente establecidas de por medio. Esto permite a los ingenieros que lo desarrollaron entrenar el algoritmo específicamente para esta ruta, por lo que la variabilidad de situaciones a las que se puede ver expuesto se reduce notablemente. Además, su velocidad máxima está limitada a 25 km/h, pero en su homologación pudo demostrar un mejor tiempo de res- 

94 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

puesta que cualquier humano a cualquier tipo de imprevisto en la carretera. La realidad es que el gobierno municipal exige a un operador estar en el autobús para poder pararlo en cualquier momento, pero la tecnología de “Trapizio” es la primera en operar de forma rutinaria en una ciudad bulliciosa tan solo mediante sensores y algoritmos de visión artificial. 

En junio de **2018** , la Inteligencia Artificial viajó al espacio por primera vez de mano de CIMON, el primer robot con IA en subir a la Estación Espacial Internacional. Este robot diseñado en conjunto por Airbus e IBM se diseño para ser un asistente inteligente que ayudara a los astronautas de la EEI con sus experimentos y también en su día a día. Físicamente era una esfera de plástico con una pantalla para interactuar con ella, y CIMON (Crew Interactive Mobile CompanioN) flotaba en el vacío en torno a sus compañeros humanos. Gracias a sus cámaras a color que alimentaban un algoritmo de visión artificial para reconocimiento facial basado en CNN, era capaz de distinguir a los distintos astronautas y comunicarse con cada uno de ellos para los objetivos que tuvieran definidos. Los astronautas podían pedirle instrucciones en directo para realizar un experimento determinado, así como grabar notas de experimentos dictadas de viva voz, como si de un cerebro flotante se tratara. Para procesar la información de entrada por medio de lenguaje natural, así como para generar las respuestas en texto y leerlas en voz alta, CIMON aprovechaba los desarrollos de IBM realizados durante los años anteriores en su plataforma Watson – que primero ganó Jeopardy y posteriormente fue ofrecida como una API a cualquier cliente en el mundo – adaptados al dominio de negocio de las misiones espaciales y los experimentos que en estas se realizan. 

En junio de **2018** se publicó un trabajo que revolucionó el campo de NLP y que sigue haciéndolo a día de hoy con sus sucesivas versiones, el denominado Generative Pre.Trained Transformer Model o, en su forma abreviada, GPT. Este modelo fue desarrollado y explotado por OpenAI, una compañía sin ánimo de lucro centrada en la investigación y desarrollo en el campo de la IA con el objetivo de obtener beneficios para la humanidad a través de esta. Entre sus fundadores se encuentran Elon Musk y Sam Altman, firmantes entre otros de la carta de aviso a los gobiernos sobre armas autónomas tres años atrás. 

Hasta la publicación de GPT, todos los modelos de NLP basados en aprendizaje profundo estaban entrenados para un objetivo concreto, como pueden ser la detección de emociones en textos, o el análisis semántico de los mismos. Estos entrenamientos se realizaban por medio del ya mencionado aprendizaje supervisado, es decir, etiquetando un gran conjunto de datos y usándolos para que el algoritmo obtuviera conocimiento abstracto de la tarea que se espera de él. Esto suponía una gran limitación para el potencial de los modelos de NLP, ya que eran necesarias cantidades ingentes de datos etiquetados para obtener modelos suficientemente buenos, que además no eran capaces de generalizar la comprensión y generación del lenguaje humano ya que tenían un objetivo demasiado específico como para poder hacer esto. En su artículo “Improving Language Understanding by Generative Pre-training”, OpenAI proponía cambiar de enfoque y aplicar el aprendizaje no supervisado, de igual forma que aquel algoritmo que aprendió a reconocer gatos 

95 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

mediante miniaturas de YouTube. Una vez que el algoritmo hubiera reconocido una serie de conceptos iniciales por sí mismo, proponían aplicar aprendizaje supervisado, de tal forma que fueran necesarios menos datos etiquetados para obtener resultados igual de buenos. En resumen, el entrenamiento se dividía en dos fases. En una primera fase, se permitía a la máquina estudiar una serie de setecientos libros para tratar de modelar por sí misma el lenguaje humano. En una segunda fase, se le proporcionaba texto etiquetado para la realización de distintas funciones como clasificar textos o resumirlos. 

Una vez entrenada, la primera versión de GPT fue capaz de superar al mejor modelo del momento en nueve de los doce test de NLP que pasó, convirtiéndose en el primer algoritmo capaz de mejorar la precisión de sus antecesores generalizando la información necesaria para las distintas tareas estipuladas. Este éxito mostró el camino a seguir para entrenar modelos generalistas de lenguaje natural: el entrenamiento previo no supervisado. 

En el mimo terreno de lenguaje natural, Google publicó en noviembre de **2018** su sistema BERT (Bidirectional Encoder Representations from Transformers). La motivación para la investigación y el desarrollo de este algoritmo fue la misma que la de GPT, la escasez de datos etiquetados de lenguaje natural, tan necesarios en el _Deep Learning_ para poder aplicar procesos de entrenamiento a las redes neuronales profundas. Según los cálculos de Google, para poder obtener resultados suficientes con un algoritmo de aprendizaje profundo únicamente basado en aprendizaje supervisado, serían necesarios billones de documentos escritos con etiquetas asociadas a cada uno de los objetivos del NLP ya mencionados. Modelos como GPT ya habían propuesto el concepto de preentrenamiento, una fase previa de aprendizaje no supervisado para tratar de emplear los datos anotados al final del proceso, donde se sacaría más provecho de los mismos. La gran innovación de Google con BERT fue la inclusión del contexto en este proceso. GPT se entrenaba por medio de numerosos libros sin contexto, leía sin saber el campo del que leía. Sin embargo, BERT trataba de comprender el contexto, no solo el texto y las palabras que lo contenían. En un símil biológico podríamos decir que sucede de igual forma que en un cerebro humano, el mismo cúmulo de neuronas se excita al procesar conceptos como “tarjeta de crédito”, “contable, “cuenta corriente”, o “fondo de inversiones”, aunque las definiciones de estas palabras sean distantes y sin aparente relación. Esto se conseguía con una técnica novedosa: La bidireccionalidad. Todas las redes neuronales para NLP, y en concreto GPT, habían propuesto una arquitectura unidireccional. La información pasaba a través de las capas de neuronas hasta llegar a la capa de salida, sin mirar atrás. BERT introdujo la bidireccionalidad, pudiendo así relacionar familias de palabras entre sí cuando descubría que siempre aparecían en el mismo contexto. En la siguiente figura, publicada en el artículo científico que presentó Google en este año, se puede comprobar cómo la información fluye en ambas direcciones en BERT, mientras que solo fluye hacia delante en el modelo 

96 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 



Comparación creada por Google entre el modelo de BERT y GPT de OpenAI 

En el examen de Stanford SQuAD, BERT obtuvo una puntuación de 87,43, desbancando a la IA que presentó Microsoft a principios de año en tan solo unos meses. Además de convertirse en el mejor sistema de procesamiento del lenguaje natural del momento, BERT era un modelo extremadamente eficiente, y podía entrenarse en media hora empleando los TPUs de Google que ya hemos mencionado, y en tan solo unas horas en un sistema con GPUs. 

En diciembre de **2018** Facebook incorporó un nuevo algoritmo de visión artificial mediante Redes Neuronales Convolucionales en todas sus redes sociales para la detección de material explícito en fotografías y vídeos. Para entrenarlo emplearon un dataset controvertido con todas las imágenes que habían sido retiradas manualmente por medio de denuncias de otros usuarios de las redes sociales, para que la red neuronal fuera capaz de diferenciar estas fotografías de otras permitidas. Durante los primeros meses de funcionamiento, el algoritmo se hizo popular por la gran cantidad de falsos positivos que arrojó, esto es, marcó una gran cantidad de fotografías como explícitas que no lo eran, como diversas obras de arte o incluso imágenes muy distantes a un desnudo explícito. Gracias a la capacidad de los algoritmos de redes neuronales de ser reentrenados tantas veces como sea necesario, este algoritmo fue mejorando con el tiempo y a día de hoy su precisión es mejor que la de un revisor humano según afirman desde Facebook. 

También en este último mes de **2018** , la empresa Waymo, perteneciente a Alphabet, matriz de Google, lanzó en la ciudad estadounidense de Phoenix su servicio de vehículos sin conductor Waymo One. Tras acumular más de diez millones de kilómetros y obtener su carnet de conducir, el algoritmo de Waymo obtuvo el permiso de la localidad de Phoenix para implementar un servicio similar a un taxi, pero sin conductor. Inicialmente el servicio se limitó a cuatrocientos usuarios de pruebas para este sistema. Igual que el primer autobús eléctrico autónomo, inicialmente todos los vehículos debían llevar por normativa 

97 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

un operador entrenado para tomar los mandos del vehículo en caso de una emergencia que este no pudiera resolver. Desde 2021 el servicio se amplió a cualquier usuario que firmara previamente un acuerdo de exención de responsabilidad, pero todavía se mantiene el conductor humano para evitar accidentes, lo que no permite a Waymo afirmar tener un vehículo con autonomía nivel 5. De hecho, las cifras de la propia empresa muestran que tan solo un 10% de los viajes realizados en 2020 se completaron de principio a fin sin interacción humana, lo que demuestra que a esta subsidiaria de Google todavía le queda un camino de pruebas y mejoras hasta obtener su deseada flota totalmente autónoma. 

A principios de **2019** , un grupo de investigadores en DeepMind, recordemos que parte de Google, presentó la que sería un equivalente de las GAN en visión artificial – capaces de generar imágenes y videos a raíz de una única imagen de una persona – solo que en esta ocasión se centrarían en el audio. Desde el lanzamiento años atrás de los múltiples asistentes virtuales de los distintos proveedores de cloud con sistemas como Siri, Alexa, Google Assistant o Cortana, el campo de la síntesis de voz había llegado a niveles sorprendentes de realismo y naturalidad. Sin embargo, estas voces eran únicas, cada modelo de síntesis de voz tenía la suya propia, con un timbre y un tono que habían sido entrenados a propósito tras estudios por parte de las distintas corporaciones. 

Para esta nueva iteración en la tecnología de síntesis de voz, Google diseñó un modelo generativo que, una vez entrenado, es capaz de clonar cualquier voz en cinco minutos. Para entrenar este modelo, se empleó una base de datos con numerosos hablantes para tratar de que la red neuronal fuera capaz de adaptarse a las condiciones concretas de la voz de cada uno de ellos en su proceso de síntesis. Una vez entrenado, el modelo es capaz de escuchar cinco segundos de una persona hablando y adaptar los parámetros de su red neuronal para generar cualquier frase dicha por esta persona. Además, es capaz de generar hablantes aleatorios que no existen, es decir, de ajustar sus parámetros para inventar voces que no pertenecen a ninguna persona real. Si bien la investigación es un gran avance en la generación de síntesis, permitiendo a pequeñas empresas contar con su propio asistente por voz mediante un esfuerzo pequeño de desarrollo, en parte de la comunidad científica esto levantó la duda de hasta qué punto la unión entre este tipo de tecnología y de las Redes Adversarias Generativas podrían acabar haciendo imposible la distinción entre un vídeo de una persona afirmando algo de viva voz generado por Inteligencia Artificial o totalmente real. 

En **2019** OpenAI dio otro paso más hacia el objetivo de necesitar la menor cantidad de datos etiquetados para poder entrenar algoritmos de aprendizaje profundo, en este caso relacionado con la interacción física con el mundo real y la visión artificial, en lugar de con el procesamiento del lenguaje natural. En este caso, el algoritmo, denominado Dactyl, controla una mano robótica. La entrada de la red neuronal son imágenes procedentes de una cámara RGB, y la salida son los movimientos que debe realizar cada dedo. El objetivo de Dactyl era en origen ser capaz de manipular un cubo y de cambiarlo a la posición deseada. Teniendo en cuenta que Dactyl jamás había manejado una mano robótica previa- 

98 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

mente, la opción más cabal parecía ser aportarle información de movimientos diseñados por un ingeniero mecánico para mover el cubo en distintas direcciones. Sin embargo, OpenAI optó por una aproximación innovadora al permitir a Dactyl sencillamente experimentar con la mano y numerosos cubos. Es decir, aprender por sí mismo, o como ya hemos visto, aprendizaje no supervisado. El algoritmo que empleaba Dactyl para decidir su siguiente movimiento era una red de tipo LSTM ya que necesitaba recordar los últimos movimientos que había realizado para poder estimar los siguientes a realizar. Las estimaciones de OpenAI fueron que el sistema necesitaría cientos de años de práctica antes de llegar a ser capaz de manipular correctamente el cubo, por lo que las primeras iteraciones las realizaron en un entorno simulado, en el que Dactyl interactuaba con una mano robótica virtual y con un cubo virtual. Con 50 horas de entrenamiento simulado en un despliegue de 8 GPUs de NVIDIA trabajando en paralelo, fueron capaces de acumular la experiencia necesaria como para transferir este movimiento al mundo real. 

Por otro lado, Dactyl empleaba una Red Neuronal Convolucional (CNN) para estimar la posición del cubo a partir de sus cámaras RGB. De esta forma, el resultado de la CNN alimentaba la LSTM y Dactyl producía un movimiento. Tras el entrenamiento, fue capaz de identificar seis formas de agarrar y manipular un objeto que nadie le había enseñado jamás, y que descubrió por su propia cuenta a base de experimentación. Se pueden observar en la siguiente figura del artículo publicado por OpenAI llamado “Learning Dexterous In-Hand Manipulation”. 

Tras este éxito, OpenAI se propuso que Dactyl aprendiera a resolver un cubo de Rubik, y descubrieron que la forma más óptima para que el aprendizaje no supervisado por refuerzo diera resultados era proponer al algoritmo problemas de una dificultad creciente, 

exactamente igual que cuando los humanos aprendemos una nueva habilidad. Con su sistema de ADR (Automatic Domain Randomization) generaban problemas simulados con cubos de Rubik cada vez más difíciles de resolver, hasta que ambas redes neuronales fueron capaces de resolver un cubo de Rubik hasta el un 60% de los casos, lo cual teniendo en cuenta que el algoritmo no empleó datos etiquetados en ningún momento, se consideró un éxito rotundo. 



Distintas formas de coger un cubo que aprendió Dactyl por sí mismo 

99 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

En febrero de **2019** OpenAI continuó con un prolífico año, presentando la segunda versión de su algoritmo GPT para el procesamiento del lenguaje natural. GPT-2 incorporaba una función que sería la que daría a conocer GPT al público general; la capacidad de generar texto automáticamente a partir de una frase de “inspiración”. Pero no solo esto, sino que GPT-2 fue un modelo tan completo que además de improvisar textos, era capaz de responder preguntas complejas en modo conversacional, traducir entre distintos idiomas y analizar el discurso de un ser humano. 

El modelo tiene más de mil millones de parámetros y fue el primero en generar párrafos completos y con sentido, como por ejemplo pequeños titulares de noticias o reseñas de libros o productos. Sin embargo, a pesar de su estructura con memoria similar a una LSTM, el algoritmo pierde el hilo en la generación de textos más largos, los que comienzan a perder el sentido a medida que avanza la escritura dada la limitada capacidad de recordar de este tipo de arquitecturas de redes neuronales. Para entrenarlo se emplearon en este caso los textos de más de cuarenta y cinco millones de páginas web, de los que era capaz de resumir y responder preguntas automáticamente después de analizarlos todos. Frente a su antecesor, no necesitó una fase de ajuste posterior a este entrenamiento no supervisado para alcanzar grandes resultados, lo que suponía un paso más allá hacia el objetivo de no necesitar datos etiquetados para obtener modelos funcionales. GTP-2 fue muy sonado en los medios generalistas debido a una controvertida decisión de OpenAI de no publicar el modelo por temor a los posibles usos maliciosos que pudieran realizarse con su algoritmo. Esta decisión vino dada porque durante el periodo de pruebas identificaron que GPT2 tiene una gran capacidad para escribir noticias falsas a partir de un titular escrito por un humano, y que hasta es capaz de inventar fuentes para sus afirmaciones de tal forma que sería realmente sencillo generar bulos de forma automática. La realidad es que los textos generados solo eran convincentes un 50% de las ocasiones, mientras que en la otra mitad se escribían auténticos disparates como incendios bajo el agua o unicornios con cuatro cuernos. A pesar de ello, OpenAI consideró el riesgo demasiado elevado y solo publicó parte del algoritmo y de la arquitectura que diseñaron para GPT-2 como medida de protección. No obstante, ciertas compañías ligadas a la IA como NVIDIA consideraron esta decisión como errónea, ya que, afirmaron, contribuía a que la población general temiera a las capacidades Inteligencia Artificial en vez de comprender lo que podía aportarnos. Además, dudaban de las capacidades reales de este algoritmo, afirmando que la decisión de no publicarlo respondía a una finalidad publicitaria y no de protección, como se afirmaba desde OpenAI. 

En marzo de **2019** la Asociación de Máquinas de Cómputo (ACM por sus siglas en inglés) nombró a Yoshua Bengio, Geoffrey Hinton y Yann LeCun como los ganadores del premio Alan Turing, considerado como el Premio Nobel de la informática. La ACM consideró que estos tres grandes nombres merecían el premio por las innovaciones tanto teóricas como en el campo de la ingeniería que habían llevado a cabo, las que habían permitido convertir las redes neuronales profundas en un componente esencial del mundo computacional. El presidente de la ACM, Cherri M. Pancake afirmó que “La Inteligencia Artificial es una de 

100 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

las áreas con un crecimiento más rápido entre todas las áreas que componen la ciencia, así como uno de los temas más discutidos en la sociedad. Este crecimiento y el interés asociado son debidos en gran medida a los avances propuestos en el aprendizaje profundo por los equipos de Bengio, Hinton y LeCun, a los que consideramos fundadores de este campo. Estas tecnologías son usadas a día de hoy por miles de millones de personas”. En su trabajo, tanto conjunto como por separado, hemos visto que se desarrollaron los conceptos fundacionales del Deep Learning, como la definición de las redes neuronales convolucionales (LeCun, en la década de los 80), el algoritmo de backpropagation (Hinton, en la misma década), el primer empleo de las GPU para el entrenamiento de redes neuronales (Hinton junto a Alex Krizhevsky, en 2012), y las primeras GAN (Bengio junto a Ian Goodfellow, en 2014), entre otros muchos avances. Este reconocimiento internacional tiene asociado un premio en metálico de un millón de dólares destinados a mejorar las capacidades de investigación de cada premiado, financiados íntegramente por Google Inc. 

En mayo de **2019** , un equipo multidisciplinar compuesto por ingenieros de Google y sanitarios del Langone Medical Center en Estados Unidos, desarrollaron y entrenaron un algoritmo de Deep Learning basado en Redes Neuronales Convolucionales para reconocer indicios de cáncer de pulmón en imágenes capturadas por tomografía computarizada. Los médicos seleccionaban las imágenes en las que había riesgo de cáncer de pulmón y las diferenciaban de aquellas de pacientes sanos. Estos dos conjuntos de imágenes se mezclaban y se proporcionaban a la red neuronal como set de entrenamiento. Tras unas cuantas épocas de entrenamiento – veremos este concepto en profundidad más adelante – los resultados fueron mejores de lo esperado. Para valorar al algoritmo, se le comparó con las decisiones tomadas por seis radiólogos distintos sobre un set de evaluación de imágenes de escáner por TC. El sistema inteligente de soporte al diagnóstico obtuvo una mejor métrica de precisión que todos los radiólogos, obteniendo un 94% de precisión en la detección temprana de cáncer, así como una notable reducción del tiempo necesario para la detección del mismo. 

En este mismo mes, investigadores de la empresa Samsung, en concreto del Centro de IA de Moscú, en colaboración con el Instituto Skolkovo, publicaron un novedoso desarrollo basado en las Redes Generativas Antagónicas (GAN) que propusiera Ian Goodfellow un lustro atrás. Si bien hasta ahora las GAN habían sido empleadas para la generación de imágenes estáticas de objetos inexistentes (desde personas a animales, habitaciones o cuadros), desde Samsung se propuso un caso de uso inédito, consistente en generar una animación a partir de una fotografía de un rostro. En la animación, el rostro se mueve mientras habla, dando la impresión de dar vida a las imágenes. Hasta el momento, para hacer tal cosa era necesario un estudio 3D de la cara de la persona, además de precisar de varias imágenes para poder generar un video creíble. Si bien Samsung afirmó que esta nueva tecnología podría ser de gran ayuda tanto en la industria de los videojuegos como en todo el entorno relativo a las videollamadas, la comunidad científica alertó de un riesgo que conllevan asociados este tipo de algoritmos, los denominados deep fakes. Un _deep fake_ consiste en generar un vídeo creíble de una persona en la que esta hace, o dice, algo que jamás hizo o dijo. Las implicaciones que podría conllevar el mal uso de esta tecnología son sencillas de imaginar. 

101 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Este algoritmo de Samsung realizaba un entrenamiento para cada fotografía que se le ofrecía. Es decir, el modelo no es estático, sino que parte de un modelo previamente entrenado que requiere un último ajuste fino (o _fine tuning_ ) para la cara de cada sujeto que se le presenta. Una vez realizado este entrenamiento, que es notablemente rápido, se pueden generar infinitos videos de esta persona con solo indicarle a la GAN dónde se desean los puntos de referencia de la cara en cada _frame_ , como los ojos, la nariz o la boca. A finales de 2018, el Centro Americano para una Nueva Seguridad (CNAS por sus siglas en inglés) alertó de que en 2023 los _deep fakes_ podrían llegar a ser tan creíbles que fueran indistinguibles de la realidad, lo que unido a la capacidad amplificadora de las redes sociales podría suponer una inundación de vídeos generados artificialmente de personalidades afirmando consignas peligrosas e incluso ilegales. 

Recordemos otra de las grandes preocupaciones del mundo investigador en el campo de la IA acerca de uno de los usos más peligrosos que consideran que se puede dar a la misma; la guerra. Como ya hemos analizado, en 2015 un gran grupo de ellos firmó una carta solicitando a los gobernantes del mundo evitar el uso de esta tecnología para la fabricación de armas autónomas. Sin embargo, este aviso no evitó que numerosas corporaciones consideraran esta tecnología como una gran oportunidad armamentística, y en octubre de **2019** , se presentó el primer tanque autónomo con capacidad de combate real por parte de la empresa _Textron Systems._ Lo denominaron _Ripsaw M5 Autonomous Battle Tank._ Este tanque eléctrico totalmente autónomo, que no necesita interacción humana en absoluto, fue presentado en la exposición de la Asociación de Armas de EEUU en Washington DC. Según sus creadores es el carro de combate más inteligente diseñado hasta el momento, con múltiples capacidades de programación incluyendo una torreta automática con reconocimiento de personas y capacidad para evaluar un área de 260 grados de forma autónoma, evaluando el entorno en busca de potenciales enemigos gracias a los mismos sistemas que emplean los vehículos autónomos civiles. Es capaz de circular hasta a 110 km/h sin ningún tipo de supervisión por cualquier terreno, por lo que la funcionalidad de este carro de combate es completa. 

En octubre de **2019** , el grupo de investigación de Inteligencia Artificial de Facebook (FAIR) presentó la segunda versión de su plataforma de visión artificial a la que denominaron Detectron2. Aceptando el declive de su propio _framework_ de desarrollo de Redes Neuronales, que recordemos que se denominaba Caffe2, decidieron buscar otro marco de desarrollo para esta segunda versión. El más empleado del mundo era, por desgracia, mantenido y publicado por la competencia, Google. Es por ello que optaron por desarrollar el que ahora es el segundo _framework_ más empleado después de Tensorflow, al que denominaron PyTorch. Esta biblioteca de código abierto basada en Python permite realizar las mismas operaciones y construcciones de redes neuronales que su competidor, y ha sido empleada para desarrollar los sistemas de conducción autónoma tanto de Tesla como de Uber. 

102 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Detectron 2 incorpora todos los modelos que incorporaba originalmente la primera versión, pero incluye un nuevo tipo de algoritmos para un objetivo de visión artificial que hasta el momento se resistía a despegar; la estimación de pose. La estimación de pose trata de estimar la posición de cada miembro, articulación y extremidad de un ser humano a partir de una única foto a color, para reconstruir su esqueleto digitalmente y poder comprender las acciones que realiza un ser humano, analizar sus movimientos y las relaciones entre los distintos elementos de su esqueleto. Gracias a Detectron 2, cualquier laboratorio interesado en estudiar la pose humana puede implementar, entrenar y desplegar de forma relativamente sencilla un modelo de pose estimación denominado _DensePose-RCNN,_ basado en Redes Neuronales Convolucionales Recurrentes, tan solo con poseer un equipo con una GPU de Nvidia que soporte directivas CUDA. Entre otros usos, Facebook empleó esta tecnología para iniciar el camino hacia el cambio de fondo en tiempo real durante una videollamada, así como para el análisis del comportamiento durante las mismas. En la siguiente imagen se puede observar la diferencia entre la segmentación semántica de una imagen, en la que cada pixel tiene asociada una clase de interés, y la estimación de pose de los seres humanos, en la que se observan el tronco, la cabeza y las extremidades delimitadas. 



Comparación entre la segmentación de objetos (izquierda) y la estimación de pose humana (derecha) 

En febrero de **2020** , Microsoft lanzó su algoritmo T-NLG, Turing – Natural Language Generation, con la intención de convertirse en el estado del arte en la gran mayoría de objetivos de NLP. Para ello, diseñó un modelo con más parámetros que ninguno antes, diecisiete mil millones de parámetros, más de diez veces más que BERT o GPT-2. Para desarrollarlo, emplearon PyTorch, de Facebook. Microsoft sostiene que para el caso de un modelo generalista de NLP que sea capaz de escribir texto libre, responder preguntas, mantener conversaciones y ofrecer apoyo a la escritura, cuanto más grande el modelo este siempre funcionará mejor que uno más pequeño. Estos modelos generativos son asimilables a las GAN en visión artificial, ya que generan contenido realista que no existía hasta el momento. Dado que un modelo con tantos parámetros es imposible de entrenar en una única GPU, el equipo encargado del entrenamiento de este modelo tuvo que emplear 256 GPUS de NVIDIA funcionando en paralelo. Yann LeCun participó en el 

103 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

diseño y entrenamiento de este modelo como consultor para el grupo de investigación de Microsoft, aportando sus más de tres décadas de experiencia en el campo. Empleando la misma aproximación basada en aprendizaje no supervisado, T-NLG superó con creces las métricas arrojadas por Google BERT y OpenAI GPT-2, demostrando la certeza de que cuanto mayor el modelo, mejor su rendimiento. 

En mayo de **2020** , se publicó la cuarta versión del algoritmo YOLO, que ya hemos mencionado cuando cinco años atrás, apareció para cambiar la perspectiva de las CNN de detección de objetos. En las dos versiones entre la original y la cuarta, el equipo encargado de YOLO se centró en mejorar la detección de objetos pequeños y en movimiento con grandes resultados. Pero fue la cuarta versión la que supondría un gran cambio desde el punto de vista de la implementación. Hasta el momento, como hemos estado observando, los modelos de aprendizaje profundo eran cada vez más profundos, lo que implica una gran cantidad de parámetros y en definitiva una capacidad de cómputo espectacular tanto para entrenar el modelo como para realizar la inferencia. YOLO v4 se centró en solucionar este problema mientras seguía mejorando las capacidades de su algoritmo. Los resultados fueron mejores de lo esperado. YOLO v4 superó a todas las redes de detección de objetos existentes en grandes bases de datos de imágenes como ImageNet, incluyendo los modelos de Google y Facebook. Pero, además, fue la primera CNN en años que era posible entrenar en una única GPU en menos de un día, y esta GPU no tenía que ser necesariamente de alta gama, ya que hasta una NVIDIA 1080 Ti permitía realizar el entrenamiento a cualquiera. Esto permitió aún más la democratización de las redes neuronales de detección de objetos, ya que cualquiera con una GPU de capacidad media podía entrenar y desplegar este modelo, que por si esto no fuera suficiente, se había convertido en el estado del arte superando la precisión de todas sus antecesoras. Además, era capaz de procesar hasta sesenta y cinco imágenes por segundo, lo que hacía posible procesar en tiempo real un vídeo para detectar objetos en el mismo, con el consecuente impulso a la implantación real de este tipo de algoritmos en la industria. 

Como respuesta a la publicación de T-NGL por parte de Microsoft, tan solo cuatro meses más tarde, en junio de **2020** , OpenAI lanzó la última versión disponible por el momento de GPT, denominada GPT-3. En connivencia con Microsoft respecto al aumento del número de parámetros, OpenAI subió la apuesta a un modelo compuesto por ciento setenta y cinco millones de parámetros, diez veces más que T-NLG y cien veces más que su antecesor GPT-2. GPT-3 no solo es capaz de escribir textos de forma autónoma partiendo de una frase, sino que tiene capacidades espectaculares como escribir el código fuente de páginas web, pero también partituras de música en base a un concepto dado. En este caso, OpenAI publicó una demo accesible a cualquiera previo registro, que funcionaba vía API, es decir, el usuario manda una frase “semilla” a través de la red y recibe de vuelta su texto, web, partitura o artículo. Para el entrenamiento de esta nueva iteración de GPT también se subió la apuesta, y el algoritmo leyó todos los libros de dominio público disponibles, todos y cada uno de los artículos de Wikipedia, todos los artículos científicos disponibles en abierto y millones de páginas web aleatorias. Según OpenAI, ha absorbido la capacidad 

104 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

de comunicarse de todos los seres humanos que han publicado en la web, aunque esta afirmación no puede ser demostrada. El modelo ocupa 700 GB, y fue necesario emplear 48 GPUs de NVIDIA para completar su entrenamiento. El uso más novedoso de GPT-3 fue encontrado por los programadores de distintos lenguajes de programación y plataformas de prototipado, que descubrieron que pidiéndole a GPT-3 “Quiero una aplicación que permita ver las fotos de la galería en mi móvil” es capaz de escribir el código necesario para una aplicación funcional. Por primera vez una IA parecía tener la capacidad de escribir código funcional, en el mismo lenguaje de programación que ella ha sido creada. 

En la misma línea de investigación, en la que se trata de que una IA desarrolle código por sí misma, una de las últimas en el campo de los sistemas inteligentes, en junio de **2020** un grupo de investigadores franceses procedentes del grupo de IA de Facebook, FAIR, presentaron un novedoso algoritmo capaz de traducir de un lenguaje de programación a otra de forma no supervisada. Hasta el momento, todos los programas empleados para pasar de código en un lenguaje a otro, por ejemplo, de C++ a Python o para actualizar de una versión de un lenguaje a la siguiente, seguían reglas básicas aplicadas mediante un árbol de decisiones, es decir, según la definición de sistema inteligente que empleemos, no eran inteligentes. En ocasiones anteriores, había habido intentos de aplicar redes neuronales artificiales a la resolución de este problema, pero, como en tantas ocasiones relacionadas con el lenguaje, la muestra era escasa. Era muy difícil encontrar ejemplos paralelos de un mismo programa funcionando en dos lenguajes de programación distintos. Como tantas veces hasta el comienzo de esta segunda década de S.XXI, la gran limitación del _Deep Learning_ era la falta de una muestra etiquetada con suficiente tamaño como para permitir a los algoritmos generalizar problemas. Pero, igual que hicieran OpenAI y Microsoft, en esta ocasión Facebook optó por el aprendizaje no supervisado. Para ello, como ya hemos visto, alimentaron al algoritmo con tantos archivos de código fuente como pudieron. Para ello, recurrieron al repositorio de código más empleado actualmente, GitHub, y usaron todos sus repositorios de código en abierto para alimentar el algoritmo de traducción. Al fin y al cabo, afirman los líderes de este proyecto, es un ejercicio de traducción asimilable al que realizamos entre lenguajes humanos, que no tendría por qué mostrar mayores dificultades. Para aprender a traducir entre idiomas, el modelo nunca vio ejemplos de algoritmos traducidos, solo millones de líneas de código en cada uno de los lenguajes de programación que participaron en este estudio (C++, Java y Python). Una vez entrenado, se pone a prueba con traducciones de código ya conocidas, y los resultados mostraron que la aproximación de aprendizaje profundo no supervisado superaba con creces las habilidades y precisión de todos los sistemas comerciales hasta el momento. Si bien los resultados no son perfectos, y por tanto necesitan de la interacción humana para la resolución de pequeños errores, los autores afirman que se puede ahorrar una gran cantidad de tiempo empleando su algoritmo para hacer una primera traducción, de la que solo haya que corregir los errores. Una vez más, el momento en el que la IA sea capaz de programar se vislumbra, aunque aún quede lejos de los avances técnicos actuales. 

105 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 

En julio de **2020** , seis meses después del estallido de la pandemia de Covid-19 causada por el virus SARS-Cov-2, científicos de la Universidad de Oxford diseñaron un grupo de investigadores franceses el sistema CurialAI, el primer sistema de IA capaz de detectar potenciales enfermos de Covid-19 en menos de una hora. Este equipo de desarrollo entrenó una red neuronal que, en base a datos históricos de pacientes confirmados fue capaz de extrapolar las características claves de un paciente de Covid-19. Para ello, solo necesitaba un análisis de sangre y una serie de constantes vitales del paciente como el ritmo cardíaco y la saturación de oxígeno en sangre. En tan solo unos segundos era capaz de proporcionar un resultado que superaba el 90% de precisión. El gran reto para este modelo era diferenciar entre distintos tipos de enfermedades respiratorias, y consiguió solucionarlo con una precisión final equiparable a la de una prueba PCR, considerado el estándar de la detección de esta infección, con la gran ventaja de que no era necesario esperar 48 horas para obtener un resultado. El sistema nacional de salud del Reino Unido (NHS) comenzó a emplear este algoritmo en los pacientes llegados a las salas de urgencias, para acelerar el proceso de diagnóstico y detección, y tratar de aliviar la saturación a la que estaban sometidos los equipos sanitarios. 

Este mismo mes, un experimento de Facebook junto a la Universidad de Southern California mostró el camino a recorrer hacia el fin de la sensórica 3D para sustituirla con redes neuronales profundas que ofrezcan resultados similares. Diez años atrás, Microsoft había presentado Kinect, el primer sistema de reconocimiento 3d del cuerpo humano basado en infrarrojos que se convirtió en el estándar de la industria durante los años siguientes. No obstante, era un sensor relativamente costoso, y que implicaba la necesidad de realizar un despliegue específico para poder observar la tridimensionalidad de las personas en cualquier proyecto comercial. Para evitar esto, este experimento trató de obtener una reconstrucción 3d de personas únicamente a partir de una imagen a color en dos dimensiones. Gracias a este algoritmo fueron capaces de reconstruir a una persona tanto por delante como por detrás, con detalles como el pelo, la ropa o los dedos que incluso a sensores de infrarrojos les resulta complicado capturar. Gracias a este tipo de sistemas, podría ser mucho más sencillo tratar con esqueletos tridimensionales lo que, unido a las tecnologías de estimación de pose aporta una gran cantidad de información desde una simple imagen a color. 



Varios ejemplos de reconstrucción 3d publicados en el artículo original 

106 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

En octubre de **2020** , el servicio de Waymo One de transporte autónomo sin conductor en las calles de Phoenix abrió al público en general tras varios años en pruebas limitadas. A partir de este momento, gracias al permiso del estado de Arizona, los taxis autónomos de Waymo ya no necesitaban llevan en ellos a un operador de seguridad, por lo que en los asientos traseros del vehículo viaja el pasajero, y no hay nadie a los mandos del vehículo. No obstante, algunos de los vehículos aún viajan con este conductor de emergencia para ayudar a seguir mejorando los algoritmos de Waymo. Esto es debido a el nivel de autonomía de estos vehículos es 4, lo que quiere decir que pueden reaccionar a cualquier imprevisto, pero ante aquellos de más compleja resolución el vehículo sencillamente se apartará a un lado de la carretera y apagará el motor, lo que puede suponer un gran inconveniente para los usuarios de este servicio. Esto supone que, a día de hoy, solo el 48% de la población con posibilidad de usar este servicio se sienta tranquila empleando este servicio por preocupaciones relacionadas con su seguridad. De los 47 accidentes leves que ha tenido Waymo, la empresa afirma que la gran mayoría de ellos han sido culpa de otro ser humano conduciendo otro vehículo, ya que en muchos casos es el vehículo autónomo el que es embestido por detrás o por un lado, aunque no haya sido capaz de evitar el contacto gracias a sus sensores. Otra parte de la población trata de evitar el uso de este servicio por miedo a estar quitando trabajo real a sus vecinos, por lo que prefieren optar por vehículos con conductor. Sea por el motivo que sea, Waymo, igual que otras empresas dedicadas al vehículo autónomo, empieza a afirmar que la limitación para el crecimiento exponencial de su negocio ya no es técnica ni tecnológica, sino que el próximo objetivo de la industria del vehículo autónomo es ganarse la confianza del usuario medio. En la gran mayoría del territorio estadounidense todavía es necesario que los vehículos autónomos nivel 4 conduzcan con un humano preparado para tomar los mandos si el algoritmo lo requiere, por lo que tendrán que esperar para ver este servicio en otras localidades del país. 

En noviembre de **2020** DeepMind presentó la que fue una de las mayores revoluciones científicas, no solo en el campo de la IA, del año 2020, su algoritmo AlphaFold para la predicción del plegado de las proteínas y su estructura en 3D solamente conociendo su secuencia de aminoácidos. Las proteínas están formadas por cadenas de unas pequeñas moléculas denominadas aminoácidos, que están a su vez formadas por carbono, oxígeno, nitrógeno e hidrógeno. La forma o estructura tridimensional que adopta una proteína depende directamente de la lista de aminoácidos que la componen y del orden concreto en el que estos se encuentren. Hasta el momento, no hay un algoritmo directamente aplicable para obtener la estructura, por lo que en los laboratorios de todo el mundo se usa la técnica de la cristalografía de rayos X para conocer la estructura de una proteína. Sin embargo, este método requiere de equipamiento muy específico, de técnicos de laboratorios formados en el mismo y, además, de mucho tiempo. Cada vez que un equipo de investigación descubre la estructura de una nueva proteína, publican la lista de aminoácidos que la contienen, así como su estructura geométrica. El conjunto de todos estos hallazgos limpiados y ordenados, han dado como resultado la competición anual CASP ( _Critical Assessment of Protein Structure Prediction_ ), de la que se celebró su decimocuarta edición en 2020 y que fue ganada por un amplio margen por AlphaFold. Hasta la irrupción del 

107 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

_Deep Learning_ en este problema, los algoritmos propuestos por diversos grupos de investigación para estimar la estructura de las proteínas solo alcanzaban un 40% de acierto en los conjuntos de evaluación, lo que en la práctica implicaba que no era posible aplicarlos a la investigación real. Ya en 2018, DeepMind trabajó en una primera versión de AlphaFold que obtuvo grandes resultados en un primer conjunto de proteínas inicial, aunque no era capaz de extrapolar este conocimiento a cualquier cadena de aminoácidos. Fue en 2020 cuando la segunda versión obtuvo una precisión comparable a las técnicas de cristalografía por rayos x, evitando tener que usar costoso equipamiento y ejecutar tediosos procesos. El entrenamiento de AlphaFold se basó en el procesado de ciento setenta mil proteínas conocidas en un proceso sobre doscientas GPUs y que tardó varias semanas en completarse. Para solucionar el problema, los investigadores de DeepMind optaron por une red neuronal de atención, basada en la separación de un problema en distintas fases para posteriormente ponerlas en común y obtener un resultado general. 

Estos resultados fueron recibidos con gran excitación en la comunidad científica, llegando a afirmar Venki Ramakrishnan, un biólogo ganador del Premio Nobel de Química que “cambiaría de forma fundamental la investigación biológica”. Sin embargo, desde el campo de la IA se criticó la falta de transparencia de DeepMind que no ha dado a día de hoy más detalles acerca de su algoritmo, por lo que no se podrá aplicar directamente por los investigadores que puedan requerirlo, ni adaptarlo a problemas concretos al no conocer el código detrás de estos grandes resultados. Desde la Universidad de Oxford se critica que la base de datos empleada para entrenar AlphaFold está construida con fondos públicos y que es de dominio público, y consideran que por tanto los resultados deberían serlo también ya que han implicado el trabajo de numerosos investigadores fuera de la matriz de Alphabet. 

Entre otras aplicaciones clave en el mundo de la salud, los resultados de AlphaFold pueden ser directamente aplicados a la creación y validación de nuevos fármacos como una fase previa a los ensayos en animales y posteriores ensayos clínicos, además de conocer mejor el funcionamiento de diversas estructuras del cuerpo humano. Entre otros usos que ya se han aplicado a este algoritmo están la determinación de la estructura de las proteínas del virus SARS-CoV-2, lo que permitió conocer su mecanismo principal de infección y comenzar a desarrollar posibles antivirales para combatir la misma. 

En la misma línea de actuación, Baidu, el motor de búsqueda más usado en China, lanzó en **2020** un algoritmo llamado LinearFold, para tratar de ayudar al desarrollo de una vacuna contra el SARS-Cov-2 en los primeros compases de la pandemia. Debido a su estructura, este virus tiene la capacidad de mutar rápidamente, complicando la tarea de secuenciar la estructura de su ARN y por tanto el análisis del virus para poder desarrollar vacunas y antivirales que lo contrarresten. Este algoritmo, similar a AlphaFold, se centra en la predicción del plegado de cadenas de ARN compuestas por nucleótidos en lugar de aminoácidos en el caso de las proteínas. Gracias a este algoritmo de Baidu, la secuenciación de la estructura de un virus pasa de requerir 55 minutos con técnicas tradicionales a menos de medio minuto con esta tecnología, es decir, casi ciento veinte veces más rápido. 

108 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Tras la aparición de enormes modelos de aprendizaje no supervisado como GPT-3 y T- NGL, junto al crecimiento exponencial de la capacidad de cómputo del hardware comercial, parecía haberse instaurado una dinámica de “cuanto más grande mejor” en el mundo de la IA, que incrementaba el tamaño de sus modelos sin parar. No obstante, algunos investigadores comenzaron a optar por lo contrario durante **2020** , tratando de encontrar los modelos más pequeños posibles que pudieran realizar las mismas tareas que los gigantes ya publicados. Investigadores del MIT junto al IST de Austria trataron de encontrar un modelo lo más pequeño posible para proporcionar el giro de volante en un coche autónomo mediante una serie de cámaras en el salpicadero. Para hacerlo, se basaron en el estudio del cerebro de un pequeño gusano, el C. elegans que, a pesar de contar con un número de neuronas increíblemente pequeño, es capaz de navegar por el mundo gracias a su vista. Tras estudiar el sistema nervioso de este nematodo, diseñaron una Red Neuronal Recurrente (RNN) con tan solo diecinueve neuronas, en un viaje al pasado de más de medio siglo. Gracias a esta aproximación, los tiempos de entrenamiento, el coste computacional de la inferencia y la muestra necesaria, es mucho más efectivo en coste implementar este sistema en cualquier vehículo privado comercial. Los resultados de este experimento mostraron los mismos niveles de precisión que otras RNN más complejas para el manejo del volante, por lo que se consideró un éxito. 

En enero de **2021** la Swinburne University Of Technology Australia presentó un nuevo tipo de procesador para IA denominado Neuromorphic Processor o procesador neuromórfico. Este nuevo procesador demostró ser una unidad más veloz del mundo con capacidad de realizar hasta 10 TeraOps/s (operaciones por segundo). Con esta velocidad, superaron la velocidad inidividual de los TPU (Tensor Processing Unit) lanzados al mercado por Google pocos años atrás. Si bien los TPU son capaces de alcanzar velocidades hasta diez veces más altas funcionando en paralelo, esta cifra es la más alta conseguida hasta el momento por un único procesador. Este nuevo tipo de procesador está basado en la estructura biológica del córtex prefrontal del cerebro humano, siguiendo la última tendencia de volver a observar a la naturaleza y el resultado de la evolución de los cerebros para tratar de imitar los aspectos más relevantes de los mismos. Gracias a su estructura formada por conjuntos de láseres infrarrojos, los investigadores de IA pueden entrenar modelos de redes neuronales complejas en un único procesador, evitando así las dificultades inherentes a la computación en paralelo que se han tenido que emplear hasta el momento tanto con GPUs como con TPUs para cualquier modelo de aprendizaje profundo. 

Un mes más tarde, en febrero de **2021** , Microsoft se unió a NVIDIA para mejorar su modelo Turing Natural Language Generation (T-NGL) gracias a la capacidad de cómputo de las GPUs de última generación de NVIDIA. Como cada vez que se publica un nuevo modelo de generación automática de lenguaje, este tenía notablemente más parámetros que los modelos anteriores, marcando un número récord de 530 mil millones de parámetros. Este modelo está basado en las redes neuronales de Transformers, que explicaremos en la próxima unidad brevemente, y en futuros módulos en profundidad. En la siguiente gráfica podemos observar cómo, cada año que pasa, el número de parámetros de los modelos de generación de lenguaje crece siguiendo una tendencia lineal. 

109 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 



Comparación del número de parámetros de los modelos de generación de texto a lo largo de los años 

Para entrenar este modelo se emplearon clústers de supercomputadores como el NVIDIA Selene y el Microsoft Azure NDv4. Al tener tal cantidad de parámetros, ni siquiera un único supercomputador es capaz de entrenar el modelo en su conjunto, por lo que se debe paralelizar la tarea entre distintos supercomputadores con grandes stacks de GPUs en cada uno de ellos. En total se emplearon miles de GPUs modelo A100 de NVIDIA funcionando en paralelo. Para el entrenamiento en este caso se emplearon casi un terabyte de textos en inglés recopilados específicamente para el entrenamiento de modelos de generación de texto mediante aprendizaje no supervisado. El modelo es capaz de autocompletar frases y textos, de responder preguntas acerca de un texto que acaba de leer, de generar un conjunto de datos generales acerca de un tema a base de leer sobre él en distintas fuentes, y de comprender la polisemia de ciertas palabras y elegir con qué acepción procesarlas en función del contexto en el que se encuentre. 

En junio de **2021** , OpenAI marcó el último gran avance en Inteligencia Artificial que sabe programar junto a GitHub, el repositorio de código más usado en el mundo. Basada por supuesto en los resultados del modelo GPT-3 de OpenAI, este modelo llamado Copilot se entrenó posteriormente para obtener la capacidad de generar código fuente válido, para lo que se emplearon todos los repositorios de GitHub tanto privados como públicos. Si bien se considera que el 40% del código que genera contiene algún error de programación, GitHub afirma que más de un tercio de los nuevos repositorios que se suben a su plataforma han hecho uso de esta nueva tecnología. Hasta el momento los desarrollado- 

110 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

res informáticos no se muestran preocupados por copilot, ya que este actúa más como un asistente que como un sustituto. Gracias a este sistema, los desarrolladores pueden generar automáticamente los bloques y funciones de su código, y revisarlo de forma manual para que cumpla con las funcionalidades esperadas. De una forma muy similar en la que los servicios modernos de correo electrónico tratan de autocompletar los mensajes que escribimos, o los teclados inteligentes que tratan de estimar la siguiente palabra que vamos a escribir, Copilot recomienda a los programadores cuál debería ser el código que escriban a continuación, y estos pueden aceptarlo o rechazarlo. Por el momento escribe código en Javascript, Go, Python y Ruby, y es capaz de ser ejecutado en los entornos de desarrollo de Visual Studio Code, Neovim y JetBrains. 

En diciembre de **2021** Mercedes-Benz recibió la primera aprobación a nivel mundial de un sistema de conducción autónoma de nivel 3. Esta condición, considerada en a norma UN-R157 de la Organización de las Naciones Unidas, trata de estandarizar los niveles de automatización para evitar que los fabricantes tengan que buscar esta aprobación a nivel estatal o incluso municipal, como fue el caso de Tesla o de Waymo en los Estados Unidos. Esta tecnología, llamada DRIVE PILOT, está disponible en los modelos de la clase S de la marca, y permite al conductor realizar tareas varias mientras el algoritmo conduce como comprar online, leer emails o mandar mensajes. El sistema está basado en un sensor LiDAR, una cámara trasera y una serie de micrófonos diseñados para reaccionar ante vehículos de emergencia entre otras cosas. El sistema recibe información acerca de la geometría de la carretera, el perfil de la ruta, las señales reconocidas mediante CNN de detección de objetos y la detección de eventos inusuales como accidentes, obras o peatones inesperados, lo que le otorga este nivel 3 de autonomía. Este hito abre la puerta al resto de fabricantes de vehículos a tratar de conseguir este tipo de certificación, dando un paso más hacia la llegada real del vehículo autónomo a las calles de todos los países del mundo. 

Actualmente, estamos todavía en una fase de crecimiento exponencial de _Deep Learning._ Como se puede observar, los avances de los últimos diez años son más numerosos que todos los avances juntos de las décadas anteriores. Sin embargo, ninguno de estos avances tecnológicos habría sido posible sin las bases que sentaron los investigadores durante la segunda mitad de siglo XX y la primera década del actual. 

El crecimiento de la capacidad de cómputo de las unidades de procesamiento, tanto CPUs, GPUs como TPUs sigue una ley exponencial denominada la ley de Moore, que afirma que cada dos años el número de transistores en un procesador se duplica, por lo que el crecimiento. Hasta el momento, esta ley se ha cumplido de manera casi perfecta, y estos avances junto a la innovación procedente de mentes de todo el mundo han hecho posible que acabemos siendo capaces de entrar modelos que hace tan solo diez años no eran ni remotamente imaginables, como MT-NGL de Microsoft y NVIDIA. Si bien el propio Gordon Moore, creador de esta ley, afirma que durante la década actual el crecimiento se estancará debido al límite físico de tamaño con el que podemos trabajar, no parece que a día de hoy hayamos llegado al final del camino de la mejora de capacidad computacional en los sistemas con los que trabajamos. 

111 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Esto implica que podremos contar con modelos de _Deep Learning_ con todavía más neuronas y parámetros que permitan generalizar aún más conocimiento de una forma todavía más precisa. Pero como hemos visto, también existen voces que abogan por la simplificación de los modelos para asegurar su supervivencia. De igual manera que cuando Deep Blue ganó el campeonato mundial de ajedrez se criticó que su capacidad estaba únicamente basada en la fuerza bruta, modelos de casi medio billón de parámetros pueden acabar siguiendo el mismo camino hacia la obsolescencia. 

Es por ello que numerosos investigadores y compañías están tratando de aligerar la carga de los modelos de aprendizaje profundo en la actualidad, con redes neuronales artificiales que pueden ejecutarse en navegadores web, dispositivos móviles e incluso relojes inteligentes. Según las predicciones de la consultora PwC, la tendencia en el mercado actual es creciente, con cada vez más empresas usando la IA para sus procesos diarios, en concreto con modelos de _Deep Learning_ , y este crecimiento no parece tener visos de revertirse. Los próximos modelos serán más potentes, livianos y precisos, y quizá ya no dependan de grandes requisitos de hardware, lo que permitirá que la IA esté prácticamente en todas partes. 

#### **_Dato importante_** 

**_2012_** _– Hinton y Krizhevsky presentan Alexnet, la primera CNN capaz de entrenarse y ejecutarse sobre una GPU. Se convierte inmediatamente en el estado del arte y da comienzo a la era del Deep Learning_ 

**_2014_** _– VGGNet, una CNN que mejora notablemente las capacidades de Alexnet, consigue por primera vez una precisión superior al 90% en ImageNet._ 

_Microsoft presenta Cortana y Amazon presenta Alexa, sus asistentes virtuales basados en NLP_ 

_Se supera por primera vez el Test de Turing, aunque no se considera un gran hito en el campo de la IA por considerar este Test algo del pasado_ 

_Tesla presenta AutoPilot, disponible para su Model S_ 

_Ian Goodfellow junto a Yoshua Bengio propone las GAN, redes neuronales capaces de generar contenido que jamás ha existido, como personas que no existen._ 

112 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

#### **_Dato importante_** (continuación) 

**_2015_** _– Tesla actualiza AutoPilot con el nivel de autonomía más alto jamás alcanzado, rozando el nivel 3._ 

_Google publica Tensorflow, un framework abierto para el desarrollo de modelos de Machine Learning_ 

_Se publica la primera versión de YOLO, un novedoso algoritmo de detección de objetos basado en CNN que se convierte inmediatamente en el estado del arte_ 

**_2016_** _– AlphaGo, basado en redes neuronales de DeepMind, vence a un gran maestro del Go por primera vez en la historia_ 

_IBM, Google y AWS lanzan servicios de IA en la nube basados en visión artificial y NLP para que cualquiera pueda emplear sus algoritmos de forma escalable_ 

**_2017_** _– AlphaGo Zero aprende a jugar al Go por sí misma mediante Reinforcement Learning en tan solo unas horas de simulación_ 

_Dos bots de Facebook son desconectados por haber llegado a un lenguaje propio de negociación_ 

_Se publica “This person does not exist”, antecesor de los deep fake_ 

**_2018_** _– Microsoft y Alibababa presentan los modelos más avanzados de NLP hasta el momento, superando la habilidad humana de comprensión de texto y resolución de preguntas en el reto SQuAD de Standford._ 

_Facebook publica la primera versión de Detectron, un conjunto de modelos de visión artificial de acceso libre, con algoritmos en el estado del arte de la clasificación, detección y segmentación de objetos_ 

_El primer autobús sin conductor recibe permiso para circular por las calles de Suiza_ 

113 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

#### **_Dato importante_** (continuación) 

_Se presenta la primera versión de GPT, un modelo de NLP que ha aprendido  a comunicarse a base de únicamente leer libros, gracias al Reinforcement learning._ 

_Google publica BERT, su sistema de NLP más complejo hasta la fecha, capaz de comprender el contexto de lo que lee. Lo empleará en su motor de búsqueda._ 

_Waymo comienza pruebas en Phoenix para un sistema de taxis autónomos_ 

**2019** _– Google es capaz de clonar cualquier voz en cinco minutos_ 

_OpenAI consigue que una IA aprenda a resolver un cubo de Rubik por sí misma, mediante simulaciones y un sistema de aprendizaje por refuerzo_ 

_También OpenAI presenta GPT-2, una versión mejorada en la que el modelo es capaz de generar textos breves automáticamente a partir de una frase de inspiración. No publican el modelo por miedo a su posible uso para generar bulos y fake news._ 

_Hinton, Bengio y LeCun reciben el premio Alan Turing en reconocimiento a su contribución al mundo de la IA mediante los algoritmos de Deep Learning._ 

_Facebook presenta Detectron 2. En esta versión se incorpora la detección de pose humana a partir de imágenes planas, además de mejoras en todos los algoritmos._ 

_Microsoft presenta T-NLG, un generador de lenguaje natural con 17 mil millones de parámetros, superando a todos los modelos anteriores en comprensión y generación de texto_ 

**2020** _– Se publica la cuarta versión del algoritmo YOLO con notables mejoras de detección de objetos pequeños y en movimiento que le convierten en el nuevo estado del arte._ 

_OpenAI lanza GPT-3, el modelo más completo de NLP hasta la fecha actual. Es capaz no solo de generar texto, sino también canciones e incluso de programar en distintos lenguajes de programación. Todo ello se consigue mediante aprendizaje por refuerzo._ 

114 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

#### **_Dato importante_** (continuación) 

_Waymo One, el servicio de taxis sin conductor de Phoenix sale de la fase de pruebas y se convierte en el primer servicio de taxi autónomo del mundo_ 

_DeepMind presenta AlphaFold, capaz de predecir la estructura de proteínas en 3d solo con conocer los aminoácidos que las conforman._ 

_2021 – Microsoft y Nvidia publican el modelo de generación de texto más grande por el momento, empleando varios supercomputadores en paralelo para su entrenamiento_ 

_OpenAI presenta Copilot junto a GitHub, una herramienta para asistir de forma autónoma a los desarrolladores a la hora de escribir código._ 

_Mercedes Benz obtiene la primera licencia a nivel mundial para la venta de un vehículo autónomo de nivel 3._ 

Hemos podido comprobar a lo largo de las décadas el paso del lento crecimiento inicial de la Inteligencia Artificial a una explosión exponencial en los últimos años. En las décadas iniciales surgirían las primeras propuestas y el optimismo excesivo de sus fundadores llevaría este campo a sendos “inviernos” en los que tanto las entidades de financiación como la sociedad general perderían el interés y la confianza en la IA. A partir de la década de los noventa, sin embargo, empezaron a surgir numerosos usos comerciales y tecnologías avanzadas que permitieron la materialización de objetivos perseguidos desde hacía décadas como los agentes conversacionales básicos, la traducción automática correcta y los robots con algún grado de autonomía. Estos primeros años de éxitos empezaron a acelerar con la entrada de las grandes corporaciones estadounidenses en el desarrollo de los últimos modelos, lo que supondría el surgimiento de motores de búsqueda, asistentes virtuales y herramientas de visión artificial que comenzaron a llegar a numerosas industrias en el mundo. No obstante, a pesar de que la capacidad de cómputo del hardware de la primera década de S XXI había mejorado notablemente, los algoritmos más complejos como las redes neuronales profundas aún tenían una limitación relativa a la eficiencia y al tiempo necesario para entrenarlas y ejecutarlas. Por suerte, en 2012 todo cambió cuando se empleó una GPU por primera vez para entrenar y ejecutar una Red Neuronal Convolucional. A partir de este momento surgieron más avances cada año, principalmente relacionados con los campos de la visión artificial, la generación automática de texto y el procesamiento del lenguaje natural. Objetivos que parecían imposibles años atrás comenzaron a convertirse en realidades, como los vehículos totalmente autónomos, los modelos de IA que escribían código fuente y los algoritmos que escribían texto libre con coherencia y precisión. 

115 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

A lo largo de toda la historia de esta disciplina se repiten una serie de conceptos. Desde protagonistas humanos, los fundadores, impulsores y mayores innovadores que a lo largo de las décadas han facilitado a la comunidad científica las últimas ideas y tecnologías que han permitido el desarrollo de este campo desde el principio. Todos estos investigadores han precisado del apoyo de una serie de instituciones que han contribuido en una gran medida a sus éxitos, gracias a su financiación y apoyo a lo largo de las décadas. Y, por último, en conjunto investigadores y entidades parecen haber perseguido a lo largo de los años los mismos objetivos, que siguen vigentes a día de hoy y aún tienen un gran camino por recorrer todos y cada uno de ellos. Para cerrar esta unidad de historia de la Inteligencia Artificial, vamos a repasar las instituciones, protagonistas y objetivos clave a lo largo de las décadas. 

#### **Las instituciones de la IA** 

- Stanford University - USA 

- Massachusetts Institute of Technology (MIT) -USA 

- Carnegie Mellon University - USA 

- Edimburgh University - UK 

- Princeton Unversity - USA 

- Oxford University - UK 

- IBM - USA 

- Google - USA 

- Facebook - USA 

- Microsoft - USA 

- Amazon - USA 

- Alibaba - China 

- OpenAI - USA 

- DeepMind – USA 

- NVIDIA - USA 

116 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

#### **Los protagonistas de la IA** 

- **Marvin Minsky** : Fundador del laboratorio de IA del MIT, escribió el libro “Perceptrons”, abogó por la IA “scruffy”, desaparecida hoy en día 

- **John McCarthy:** Creador del concepto de IA, ganó el premio Turing en 1971. Inventó LISP. 

- **John Searle** : Propuso la definición de ANI, AGI y ASI para diferenciar los tipos de IA según su inteligencia comparada con la de los seres humanos. 

- **Frank Rosenblatt:** Propuso la idea de los perceptrones por primera vez, lo que sería la semilla del Deep Learning. 

- **John Hopfield:** Inventor de la primera Red Neuronal Recurrente (RNN), aún empleada hoy en día 

- **Yann LeCun:** Creador de las Redes Neuronales Convolucionales (CNN) en la década de los ochenta, que aún a día de hoy son el estado de arte en visión artificial 

- **Geoffrey Hilton:** Padre del algoritmo de la retropropagación gracias al cual las redes neuronales profundas pueden aprender a realizar las tareas necesarias. 

- **Jeff Dean:** Director del proyecto Tensorflow, que democratizaría el acceso al ML 

- **Ian Goodfellow:** Investigador en IA que presentó como tesis doctoral uno de los mayores avances en la última década, las Redes Generativas Adversarias (GAN) para la generación de contenido automática basada en visión artificial. 

#### **Los temas de la IA** 

- Comprender el lenguaje natural humano escrito y poder generar conversaciones e interacciones coherentes (NLP) 

- Convertir el audio de una persona hablando en un texto (transcripción), y poder generar un archivo de audio a partir de un texto proporcionado (generación de discurso) 

- Traducir automáticamente entre dos idiomas con la misma calidad que un ser humano (machine translation) 

- Analizar la escritura manuscrita para obtener texto digital de la misma (reconocimiento de texto) 

- Reconocer humanos y rasgos en los humanos para su identificación general (rango de edad, estado de ánimo, actitud) o específica (reconocimiento facial o biométrico) 

117 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

- Reconocer patrones de interés en imágenes que suelen ser reconocidos por expertos en un ámbito mediante la observación manual, bien sea mediante la clasificación, detección o segmentación de objetos (visión artificial). 

- Realizar recomendaciones de consumo a clientes (de los sistemas expertos al clustering del machine Learning) 

- Desarrollar sistemas inteligentes que jueguen a diversos juegos de mesa que el ser humano considera complicados y para los que hace falta intuición y capacidad de aprendizaje como ajedrez, póker o Go. 

- Robots y vehículos autónomos que son capaces de moverse, conducir, navegar, evitar obstáculos y cumplir las normas de circulación sin interacción humana (visión artificial) 

- Generar imágenes de objetos que no existen inspirados por otros que sí (GAN) 

- Generación automática de texto a partir de una frase inicial para construir textos completos (modelos generativos de texto) 

- Detectar la pose humana para comprender su posición espacial en 3D conociendo sus extremidades, articulaciones, torso y cabeza (desde Kinect hasta la estimación de pose por Deep Learning) 

- Programación automática y ayuda a la programación mediante modelos de aprendizaje no supervisado. 

En la actualidad todos estos objetivos históricos de la IA se consideran cumplidos. El reto actual es descubrir hasta dónde puede llevar el ser humano a la IA, y tratar de descubrir las arquitecturas y algoritmos que permitan hacerlo. 

118 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

## **3. Métodos y tecnologías fundacionales** 

la IA que implica grandes cantidades de datos, se llama _Machine Learning_ . La IA que implica grandes cantidades de datos y redes neuronales se llama _Deep Learning_ . 

Tal y como hemos observado en la unidad anterior, las tecnologías más extendidas en el mundo actualmente relativas a la IA son el aprendizaje automático o Machine Learning, y el aprendizaje profundo o Deep Learning. Pero la IA surgió mucho antes que estos dos conceptos, por lo que, ¿Es toda la IA aprendizaje automático? ¿Es todo el aprendizaje profundo aprendizaje automático? ¿Es todo el aprendizaje IA? Para responder a estas preguntas, lo más sencillo es observar la siguiente imagen. 

Como podemos ver, la Inteligencia Artificial es un campo muy amplio, que contiene un subconjunto de técnicas denominadas _Machine Learning._ Dentro de todas las técnicas 



llamadas _Machine Learning,_ encontramos algunas de ellas que están relacionadas con redes neuronales profundas, y a las que denominamos _Deep Learning._ Por último, la ciencia de datos o data science tiene entre sus objetivos el _Machine Learning_ y el Deep Learning, por lo que los alimenta, pero tiene otros objetivos que no son el objetivo de este máster. Dicho de otra forma, la IA que implica grandes cantidades de datos, se llama _Machine Learning_ . La IA que implica grandes cantidades de datos y redes neuronales se llama _Deep Learning_ . Pero ¿dónde queda la IA que no implica _data science_ ? 

119 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Este IA es la que hemos visto en los comienzos de la historia de esta disciplina, hasta los años ochenta en los que empiezan a aparecer proposiciones aplicables de redes neuronales con capacidad de aprendizaje automático. Esta IA es denominada actualmente GOFAI o _Good Old Fashioned Artificial Intelligence_ , término que ya hemos mencionado y que hace referencia a los algoritmos empleados en el campo de la IA de forma previa a la aparición del aprendizaje automático. 

Aunque no suponga revelaciones con gran impacto mediático, la GOFAI sigue existiendo a día de hoy, y cumple principalmente dos funciones. 

1. La GOFAI puede suplementar un producto basado en aprendizaje automático (ML) para crear un producto completo que resuelva una necesidad real. 

2. La GOFAI puede producir una solución completa por sí misma, sin ningún tipo de ML, cumpliendo con los requerimientos del cliente. 

_El concepto de_ **_GOFAI_** _engloba todos los sistemas con_ **_conocimiento a priori_** _y basados en r_ **_azonamiento formal_** _en los que no hay una fase de aprendizaje. Estos algoritmos, como sucedía mayoritariamente hace medio siglo, estaban íntegramente programados y “enseñados” por humanos._ 

En definitiva, el desarrollador trataba de darle todo el conocimiento y reglas lógicas al programa para resolver un problema muy concreto, recordemos Dendral o Deep Blue, cada uno con su caso de uso específico. 

En el caso de complementar modelos de ML, la realidad es que en la actualidad todos los sistemas de ML tienen de alguna forma conocimiento incorporado por parte de los humanos que lo desarrollan. O bien el lenguaje fonético empleado para el procesamiento de lenguaje natural, o la interpretación que se debe hacer de cada señal de tráfico que detecta un coche autónomo. Estas no son cosas que aprenda el algoritmo por su cuenta, sino que es el desarrollador el que debe incorporarlas al código fuente. Gracias a esto, la GOFAI puede ayudar a la Inteligencia Actual en el estado del arte a realizar sus funciones más rápido gracias a las asunciones previas que proporciona el ser humano al algoritmo. Esta influencia de los desarrolladores en el modelo obtenido tras el entrenamiento se denomina en inglés _inductive bias_ , y modula el comportamiento de un algoritmo automático para adecuarse lo más rápido posible a las necesidades de sus creadores. 

Por otro lado, hay sistemas con IA puramente formal o _a priori_ . Aunque actualmente la sensación que ofrece el mundo investigador, las publicaciones y los nuevos descubrimientos, así como las nuevas tecnologías de cómputo como las GPUs y las TPUs es de que estamos rodeados de redes neuronales, lo cual es relativamente cierto, aún quedan ciertos casos de uso en los que las empresas desarrollan sistemas de GOFAI puro con gran éxito. Estas empresas suelen ser compañías de desarrollo especializadas en este tipo 

120 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

de proyectos. Por ejemplo, a pesar de los enormes avances en el campo del procesamiento del lenguaje natural, hay empresas que actualmente programan chatbots basados en reglas lógicas, como los primeros ELIZA de hace décadas. De hecho, hay un mayor número de bots sin capacidad de aprendizaje en la web que viceversa. 

En definitiva, la GOFAI, o más formalmente la Inteligencia Artificial Simbólica, hace referencia a todas las herramientas desarrolladas para la generación de agentes inteligentes sin el uso de grandes cantidades de datos ni la capacidad de aprender. Estos sistemas están basados en programación lógica (como PROLOG), reglas anidadas, heurísticas, razonamiento formal y representación del conocimiento. Esta tecnología fue la predominante desde el surgimiento de la IA en los años 50 hasta finales de la década de los años 90, con su mayor exponente en los sistemas expertos, los chatbots simbólicos y los agentes de juego “por fuerza bruta” como Deep Blue. 

A partir del surgimiento de los desarrollos relativos a sistemas capaces de aprender de datos y, por tanto, en la conjunción de la ciencia de datos con la Inteligencia Artificial, surge el denominado aprendizaje automático o Machine Learning. 

_El_ **_Machine Learning_** _es un subconjunto de la Inteligencia Artificial en el que los algoritmos tratan de establecer sus propias reglas mediante el_ **_aprendizaje_** _a partir de grandes cantidades de_ **_datos_** _._ 

Por tanto, los algoritmos de _Machine Learning_ son aquellos que permiten obtener conclusiones de un cierto conjunto de datos, para posteriormente poder hacer predicciones sobre los mismos o incluso generar datos nuevos. Como veremos más adelante, el _Deep Learning_ es un subconjunto del _Machine Learning_ . 

Para poder realizar este proceso, es imprescindible ejecutar una serie de procesos que son comunes a todos los sistemas de aprendizaje automático, y por tanto también del profundo. Son las siguientes: 

1. **Definición** del problema. Aunque pueda parecer obvio, no es posible diseñar un buen modelo de ML sin una definición formal del problema y con una comprensión del dominio de negocio. La mejor aproximación es tratar de hacer una descripción numérica del problema siempre que sea posible. 

2. **Recolección** de datos. Para aprender es imprescindible tener una base de información de la cual absorber conocimiento. Para ello, todo proyecto de ML implica un esfuerzo en la recolección de datos. Estos pueden ser tendencias de acciones en bolsa, imágenes de animales o comandos por voz dictados por humanos. Serán aquello para lo que querremos que el modelo infiera o genere. 

121 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

3. **Preparación** de datos. En muchas ocasiones, los datos provienen de numerosas fuentes y, por desgracia, no suelen estar estandarizados. Es por ello que, gracias a la ciencia de datos, se convierte en imprescindible la limpieza y normalización de estos datos. El modelo requerirá una entrada de datos coherente para poder obtener los mejores resultados posibles. 

4. **Anotación** de los datos. Una vez normalizados los datos, es necesario etiquetarlos. A este proceso se le llama generación de _ground truth_ , la verdad absoluta que queremos proporcionar al modelo con la información precisa que queremos que conozca. Por ejemplo, en una fotografía podemos recuadrar los gatos, en un texto el sujeto y el predicado y en un modelo para detección de enfermedades, aquellos análisis de sangre que resultaron ser de personas enfermas. Del total de los datos tendremos que generar dos, y en ocasiones tres, conjuntos diferentes. Por un lado la gran mayoría de los datos – entre un 70% y un 80% - irán al conjunto de entrenamiento, es decir, a los datos que empleará el modelo para aprender. El porcentaje restante irá a uno o dos conjuntos según el protocolo que se decida seguir. En el más exigente, uno de los conjuntos será el de validación, que es usado durante el entrenamiento para comprobar que el modelo está cumpliendo con sus objetivos. Este conjunto es opcional. El que es obligatorio es el conjunto de evaluación que, tras finalizar el entrenamiento, usaremos para comprobar los resultados que hemos obtenido para no emplear los mismos datos con los que entrenamos para evaluar nuestro modelo. 

5. **Selección** e implementación del algoritmo. Como veremos brevemente a continuación, y en profundidad en próximos módulos, la elección del algoritmo a emplear en ML no es, en absoluto, trivial. Existen numerosos tipos de aprendizaje, y un sinfín de posibilidades dentro de cada uno de ellos en función del tipo de problema que queramos resolver. Por suerte, hay una serie de reglas a seguir que podrán ayudarnos a seleccionar un algoritmo en concreto. Siempre será esencial que, ante la duda, se implementen y evalúen varios modelos para seleccionar el que mejores métricas de precisión arroje al finalizar el proyecto. 

6. **Entrenamiento** del algoritmo. En la fase de _training_ , el algoritmo pasará un número determinado de veces por todos los datos etiquetados en el conjunto de entrenamiento para conseguir ajustarse de lo que se espera de él, lo que se denomina _fit_ en terminología específica. Según el algoritmo este proceso será más rápido o lento, pero al final del mismo acabaremos teniendo un modelo entrenado listo para su evaluación. En los casos en los que se emplea, en cada pasada por el conjunto de entrenamiento, el modelo se pone a prueba contra el conjunto de validación para poder decidir cuándo parar el entrenamiento. 

7. **Evaluación** del modelo. Una vez el algoritmo ha sido entrenado y hemos obtenido un modelo con conocimiento adquirido, lo ponemos a prueba contra el set de evaluación. En este set hay datos que el modelo no ha procesado nunca, por lo que nos ayudará a conocer cómo será su desempeño en el mundo real cuando se enfrente a situaciones que no ha experimentado hasta el momento. 

122 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

8. **Fine tuning** . El proceso de ajuste fino o _fine tuning_ consiste en identificar las debilidades del modelo una vez ejecutado el proceso de evaluación. Gracias a este proceso, se puede realizar un segundo entrenamiento focalizado en los puntos débiles del modelo, para incrementar su precisión. 

9. **Despliegue** del modelo. Una vez finalizado el proceso, el modelo puede ser desplegado para su puesta en producción. En este momento, el modelo estará preparado para recibir datos e inferir resultados ya sean predicciones o datos generados automáticamente. 

En la selección del algoritmo a emplear hay una decisión inicial que hemos ido vislumbrando a lo largo de los ejemplos e hitos de la IA a lo largo de la historia, que determinará una lógica específica en cada caso, por lo que es esencial poder diferenciarlos desde el principio. Hasta el momento ya hemos mencionado los tres tipos de aprendizaje que existen dentro del _Machine Learning_ , y es el momento de definirlos formalmente. 

_Existen tres tipos de_ **_aprendizaje automático_** _:_ 

- **_Aprendizaje supervisado_** 

- **_Aprendizaje no supervisado_** 

- **_Aprendizaje por refuerzo_** 

El **aprendizaje supervisado** parte de la premisa de que se cuenta con un conjunto de datos etiquetados del que se espera que el modelo aprenda a responder una serie de preguntas. Las etiquetas son la respuesta a estas preguntas, conocidas previamente y marcadas por un humano de forma manual, para tratar de que en el futuro el algoritmo sea capaz de hacerlo de forma automática. El algoritmo pasará por estos datos de forma iterativa tratando de ser capaz de acertar la respuesta para cada ítem mediante el proceso de entrenamiento. Una vez entrenado, será capaz de inferir la respuesta de forma automática. 

Hay dos tipos principales de aprendizaje supervisado. 

- a. **Clasificación** . En un problema de clasificación el algoritmo responde a la pregunta “¿de qué clase es este tipo de dato?”. Para cada ítem de entrada, como puede ser una imagen, dará una respuesta dentro de una lista de clases cerradas. Por ejemplo, un algoritmo capaz de identificar la especie de una planta a través de una foto es un algoritmo de clasificación, igual que un algoritmo que tome la decisión de conceder un préstamo no a un cliente bancario – en este caso las clases serían la positiva y la negativa -. En definitiva, es un problema matemático discreto, con una serie de valores válidos como salida. 

123 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

- b. **Regresión** . En este tipo de algoritmo se busca una estimación numérica continua, es decir, un valor dentro de un rango. Por ejemplo, tratar de estimar la temperatura que va a hacer la próxima semana, o cuánto va a tardar un vehículo en llegar a un destino fijado en una aplicación de mapas. 



Comparación visual entre un objetivo de clasificación y otro de regresión 

En el **aprendizaje no supervisado** no contamos con datos etiquetados, sino con ingentes cantidades de datos a procesar sin _ground truth_ asociado. Este es el ejemplo de los últimos modelos de generación de lenguaje como GPT-3 o MT-NGL. En este tipo de casos de uso se pretende que el algoritmo descubra relaciones entre los datos de forma automática sin intervención humana. Conocemos únicamente los datos de entrada, pero no exigimos unos datos de salida específicos, más allá de la estructura que deberán tener. En definitiva, su objetivo principal es la exploración. Principalmente se mencionan dos tipos de algoritmo de aprendizaje no supervisado, aunque existe una gran variedad de ellos en la que profundizaremos en futuros módulos. 

- a. Algoritmos de **_clustering_** . Los algoritmos de clustering o agrupación son capaces de encontrar grupos de datos similares sencillamente procesándolos todos. Este tipo de algoritmos son los que usan para hacer perfiles automáticos de tipos de cliente en plataformas online como Spotify o Netflix. En base a una gran cantidad de datos acerca de determinadas variables, estos algoritmos generarán un número predeterminado de grupos a petición del desarrollador. 

- b. Algoritmos de **asociación** y reducción de dimensiones. Estos algoritmos encuentran relaciones entre datos a la par que los simplifican para hacer más sencillo su análisis cualitativo. Ayudan a conocer qué sucesos pueden predecir la ocurrencia de otros sucesos, para así encontrar relaciones que por mera observación sería complejo obtener. Este carácter exploratorio puede ser usado en numerosos sectores y casos de uso, ya que ayuda a comprender de una manera más precisa cómo se comportan una serie de variables respecto a otras de forma automática. 

124 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Por último, nos encontramos con el **aprendizaje por refuerzo.** En este caso la principal diferencia es que no hay una pregunta a resolver, ni un nuevo conocimiento que generar, sino **una acción que tomar** . En el aprendizaje por refuerzo se trata de que un agente aprenda por sí mismo una serie de reglas o políticas que le ayuden a tomar las mejores decisiones para un problema específico. 

En este caso, en lugar de proporcionar datos al algoritmo, sean etiquetados o no, se pone a este frente al problema real desde el primer momento, normalmente por medio de una simulación, y se le permite experimentar. Para que esta experimentación no sea en vano, los desarrolladores diseñan un sistema de recompensas inspirada en la forma en un tipo de aprendizaje que soportan los cerebros reales de los animales, que buscan recompensar las acciones positivas para el objetivo marcado. Para cada resultado obtenido en positivo, el agente inteligente recibirá una recompensa. Para cada resultado negativo, un castigo. De esta forma, el agente explora todas las posibles formas de actuar frente a un problema, pero acaba quedándose con aquellas que le aseguran una recompensa mayor en conjunto y a largo plazo, de forma que, teóricamente, terminará por encontrar la solución óptima para el problema que se le ha planteado. En definitiva, es un método de aprendizaje basado en prueba y error, en el que se parte sin ningún tipo de directiva y se termina con un proceso optimizado de resolución de problemas. 

Un ejemplo habitual de este tipo de algoritmo son los robots que aprenden a andar sin ningún tipo de información más allá de cómo mover sus extremidades mecánicas en un mundo simulado. En 2017, DeepMind consiguió que un sistema de IA aprendiera a andar, correr, saltar y trepar sin ningún tipo de información previa. A cada paso que daba, salto que ejecutaba o escalón que subía, el algoritmo era recompensado. Cada vez que se caía, era penalizado. Aunque sus movimientos distaban de ser humanos, en este video se puede comprobar cómo al final el algoritmo fue capaz de encontrar una solución que en la gran mayoría de los casos solucionaba su objetivo de una forma solvente. 

En definitiva, tenemos tres tipos de aprendizaje, en función de dos factores: 

- a. Si vamos a esperar que el modelo aprenda a realizar acciones en un entorno determinado (aprendizaje por refuerzo) o si bien esperaremos que el modelo pueda responder a preguntas sobre los datos o que genere infomación totalmente nueva (aprendizaje supervisado y no supervisado) 

- b. Si tenemos un problema para el cual conozcamos la pregunta y podamos obtener un conjunto de datos etiquetado de forma manual para enseñar al modelo a responderla (aprendizaje supervisado), o si bien tenemos una gran cantidad de datos que queremos explorar y conocer mejor para comprender la realidad de un caso de uso por medio de la IA (aprendizaje no supervisado) 

125 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 



Por último, queda por responder la pregunta ¿dónde encaja aquí el _Deep Learning_ ? Hemos comentado que el _Deep Learning_ es un subconjunto del _Machine Learning_ . ¿Por qué se remarca siempre frente al resto de posibles algoritmos de ML? La atención que recibe este campo se debe única y exclusivamente a las capacidades que ha demostrado poseer a la hora de resolver problemas que hasta el momento no se creía que fueran capaces de ser resueltos, en concreto desde 2012. 

Dentro de la jerarquía de los algoritmos del aprendizaje automático, desde una perspectiva lógica, está al mismo nivel que otros tantos algoritmos como pueden ser los algoritmos bayesianos, los árboles de decisión, los algoritmos de agrupación y los de reducción dimensional. No hay ningún motivo formal que diferencie el _Deep Learing_ del resto, no obstante tiene que tener alguna característica como para haberse convertido en el tipo de _Machine Learning_ que más impacto tiene en la economía actual. 

Existen varios ejemplos de algoritmos de decisión que tratan de ayudar al desarrollador a decidir qué algoritmo de ML es el mejor para solucionar un determinado problema. En este tipo de árboles de decisión veremos que las redes neuronales, es decir, el Deep Learning, son una opción más a tener en cuenta entre otros tantos. En la siguiente hoja de ruta diseñada por Microsoft Azure ML, la librería de ML que ofrece Microsoft en su cloud, podemos comprobarlo. Las redes neuronales (que son, en definitiva, el aprendizaje profundo o _Deep Learning_ ) aparecen en dos ramas de este árbol de decisión. Por un lado, se recomiendan usar cuando tenemos un conjunto de datos etiquetados que queremos aprender a clasificar automáticamente – es decir, un objetivo de clasificación - , y nuestra prioridad es la precisión frente a la velocidad el entrenamiento y la inferencia. Por otro lado, también se recomiendan en casos de predicción numérica – es decir, regresión – cuando, de nuevo, el objetivo prioritario es ser precisos a la hora de dar una respuesta correcta. Como se puede observar las redes neuronales están mezcladas con todos los demás tipos de algoritmos de Machine Learning, que iremos descubriendo a lo largo de este máster. 

126 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 



Ayuda para la decisión de qué algoritmo usar en problemas de ML según sus características 

_El_ **_Deep Learning_** _es un subconjunto del Machine Learning basado en algoritmos que tratan de imitar la forma de aprender del cerebro humano denominados Redes Neuronales Artificiales (ANN). Están basadas en unidades lógicas denominadas neuronas o perceptrones, que reciben una serie de señales de entrada y se activan o no por medio de una función de activación._ 

Como hemos visto con anterioridad, a lo largo de la historia se han propuesto numerosos tipos de Red Neuronal Artificial (ANN) según el propósito y el tipo de dato con el que se pretende tratar. Dentro del aprendizaje profundo, como se puede intuir, solo se incluyen las Redes Neuronales Profundas (DNN o _Deep Neural Networks_ ), que a efectos prácticos son la inmensa mayoría de las redes neuronales actuales – excepto sonados casos como aquel en el que, inspirados por un gusano, los investigadores consiguieron desarrollar un algoritmo para conducir un vehículo con tan solo 19 neuronas – compuestas por varias capas de neuronas entre la capa de entrada y la capa de salida. Todas las DNN constan de una serie de elementos comunes: neuronas, sinapsis, pesos ( _weights_ ) y funciones de activación. 

A pesar de haber innumerables variaciones, la siguiente podría ser una clasificación inicial de los tipos de ANN más empleados en la actualidad, que nos resultarán familiares: 

127 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

- **Redes Neuronales de Alimentación Hacia Delante (FFNN)** . Este es el tipo más sencillo de red neuronal profunda. Consisten en una capa de entrada, que procesa directamente los datos, y un determinado número de capas intermedias que están entrecruzadas para compartir información entre las distintas capas. Una capa solo se comunica con la siguiente, hasta que se llega a la capa de salida en la que se computa el resultado final. Funcionan muy bien para predicciones numéricas en casos de regresión para aprendizaje supervisado, pero fallan de forma notable cuando se trata que trabajen con imágenes, texto o sonido. 

- **Redes Neuronales Convolucionales (CNN).** Las CNN surgieron para tratar de extraer de forma automática las características más relevantes de una imagen y de esta forma ser capaz de detectar, clasificar y segmentar objetos en las mismas. Inventadas por Yann LeCun y popularizadas por Hinton en 2012, son el algoritmo más empleado para procesamiento de imágenes a día de hoy, y cada día son más precisas y obtienen mejoras. Son algoritmos como YOLO, VGG, Resnet, Inception… 

- **Redes Neuronales Recurrentes (RNN).** Las RNN parten de la premisa de que el conocimiento puede fluir en dirección contraria a la esperada, pudiendo usar la salida de una neurona como entrada de una neurona de su misma capa. Gracias a este comportamiento es posible tener algún tipo de estructura temporal en la que se comprenden mejor que con las FFNN conceptos temporales como vídeos o pequeños fragmentos de texto. 

- **Redes Neuronales con Memoria a Corto y Largo Plazo (LSTM).** Las redes LSTM son una subclase de las RNN que tratan de mejorar la memoria de estas, incrementando su fiabilidad en tareas que requieran una memoria a largo plazo como comprender textos complejos o traducir de un idioma a otro. 

- **Redes Neuronales basadas en Transformers.** Este tipo de red neuronal se ha convertido en el estado del arte para la gran mayoría de problemas de procesamiento y generación de lenguaje natural, y están basadas en mecanismos inspirados en la atención humana. En vez de generar sistemas recurrentes, en los que la propia red se retroalimenta, lo que aumenta enormemente la complejidad de un algoritmo, estas redes neuronales tratan de proporcionar las mismas ventajas, pero de forma secuencial. El ejemplo más sonado de una red de Transformes es el éxito que ya hemos comentado del modelo GPT-3 de OpenAI para la generación automática de texto. Actualmente hay numerosos grupos de investigación tratando de estudiar si este tipo de red neuronal también pudiera ser aplicable al terreno de la visión artificial, desplazando por tanto a las CNN de una posición de liderazgo de la que llevan gozando dos décadas. 

128 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

- **Redes Neuronales Generativas Adversarias (GAN)** . Este tipo de redes neuronales presentadas en 2012 por primera vez, permiten generar datos que no existían previamente gracias a una competición entre una red que genera contenido y otra que valora su calidad, como ya hemos explicado con anterioridad. Gracias a este tipo de redes neuronales, que en ocasiones están formadas por redes neuronales de otros tipos en función del objetivo que se persiga, somos capaces de crear contenido totalmente nuevo que se parezca a otro contenido visto con anterioridad. Por ejemplo, en esta demo de Nvidia para su modelo GauGAN2, podemos generar un paisaje con aspecto realista con tan solo dibujar con un pincel los bloques más importantes del mismo. 



- **Autoencoders.** Los Autoencoders son un tipo de red neuronal focalizadas en el aprendizaje no supervisado. Su objetivo es similar al de las GAN, pero tienen una aproximación algo diferente. Su tarea se divide en dos fases. Por un lado, tratan de entender los datos que se le muestran – recordemos que sin etiquetar al ser aprendizaje no supervisado – y codificarlos mediante una representación interna que se genera automáticamente. Por otro lado, a partir de esta representación interna, tratan de recuperar con exactitud la entrada original. Para la primera parte del proceso se emplea un algoritmo llamado _encoder_ que es el encargado de la codificación de los datos. Por otro lado, se ejecuta el _decoder_ que trata de devolver estos datos codificados a un formato comprensible por un humano. Las aplicaciones más habituales para los Autoencoders son la detección de anomalías, ya que son capaces de detectar cuando una representación interna sigue un patrón notablemente distinto de los habituales y por tanto no será capaz de recuperar los datos como debería. Por otro lado, se usan para comprimir imágenes, quitar ruido de imágenes y mejorar la resolución de las mismas. 

129 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

Una de las características más importantes de los modelos de Deep Learning es la infraestructura específica que requieren para su entrenamiento y despliegue. Dado que los modelos actuales cuentan con miles de neuronas repartidas en decenas de capas, esto implica que tienen millones de parámetros. Estos parámetros, que no son más que los pesos de entrada que cada neurona artificial, deben ser ejecutados uno a uno para cada dato de entrada que recibe la red neuronal. Además, durante el proceso de entrenamiento deben ser recalculados y ajustados por medio de algoritmos como la retropropagación que vimos en la Unidad 2. Ambos procesos implican unas necesidades computacionales extremas incluso para los sistemas actuales. Como ya hemos estudiado, a partir de 2012 se generalizó el uso de las tarjetas gráficas o GPUs para el entrenamiento e inferencia de estas redes neuronales, lo que aceleró enormemente su desarrollo. Sin embargo, es importante tener en cuenta que el _Deep Learning_ no es siempre la solución a todos los problemas de Inteligencia Artificial. En muchos casos, el caso de uso requerirá de una infraestructura menos costosa, de una capacidad de ofrecer resultados en menos tiempo o, lo más habitual, no habrá suficientes datos para poder entrenar el modelo. 

Porque esta es la mayor desventaja de los modelos de aprendizaje profundo. Sin una cantidad suficiente de datos, no serán capaces de generalizar el conocimiento y, por tanto, fracasarán. Otros algoritmos de _Machine Learning_ como los árboles de decisión, las máquinas de soporte de vectores (SVM) o la lógica bayesiana, necesitan infinitamente menos datos para obtener un resultado aceptable, como veremos en módulos futuros. Es por tanto muy importante que el decisor del tipo de algoritmo conozca con detalle las restricciones, ventajas y desventajas de cada tipo de IA para poder poner en marcha siempre el sistema óptimo para cada caso de uso. Si bien a día de hoy la gran mayoría de sistemas de IA para imágenes, video y lenguaje están basados en redes neuronales, iremos descubriendo a lo largo de los distintos módulos que estas no son siempre la solución más adecuada, y que es esencial conocer otras opciones para poder sopesar cada una de ellas. 

En definitiva, hemos visto que la Inteligencia Artificial está compuesta por un sinfín de algoritmos que pueden ser inicialmente parte del aprendizaje automático (ML) o no, en cuyo caso se denomina IA simbólica o, según la fuente, _Good Old Fashioned Artificial Intelligence._ Estos sistemas, como los sistemas expertos, pueden ser de gran ayuda en casos de uso muy específicos, aunque habitualmente son un complemento necesario de los algoritmos de aprendizaje profundo. Por su parte, el Machine Learning está dividido en tres tipos de aprendizaje – supervisado, no supervisado y por refuerzo – en función del tipo de datos de entrada y del objetivo de cada uno. Por último, hemos descubierto que el aprendizaje profundo o _Deep Learning_ es tan solo un subconjunto del _Machine Learning_ en el que se implementan Redes Neuronales Artificiales Profundas , eso sí, con gran éxito. 

130 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

## **4. Aplicaciones e impacto en el mundo real** 

_Un sinfín de empresas de pequeño y mediano tamaño tienen un negocio basado en la implantación real de la IA en casos de uso concretos para sectores muy específicos. Este tipo de empresa suele beber de conocimiento en abierto que tanto universidades como grandes empresas generan, y ser capaz de implantarlo en sus clientes de forma óptima y eficiente._ 

Como ya hemos visto en la Unidad 2, durante toda la historia de la IA ha habido una serie de objetivos que han perseguido los investigadores de este campo dentro de las distintas subdisciplinas. Desde reconocer caras y comprender la pose de un humano en visión artificial, a traducir textos automáticamente o escribir artículos en el caso del procesamiento del lenguaje natural. No obstante, la investigación tecnológica precisa de un paso esencial para su empleo en el mundo real, la transferencia tecnológica. La transferencia tecnológica es el proceso por el cual las instituciones de investigación como centros de investigación gubernamentales o universidades, son capaces de transferir el conocimiento, habilidades y tecnologías al sector privado para que este pueda explotar las últimas investigaciones de tal forma que lleguen al consumidor y que puedan seguir desarrollándose por un cauce comercial. Básicamente, es el proceso por el cual una nueva tecnología acaba pasando desde un centro investigador a una empresa, porque se encuentra un caso de uso para la misma. 

En el caso de la Inteligencia Artificial este proceso cuenta con dos anomalías que es importante recalcar para comprender las discrepancias entre el mundo de la investigación teórica y el sector privado. Por un lado, es un sector en el que, como hemos podido comprobar, hay un número creciente de empresas dedicadas a la investigación que posteriormente publican en abierto sus resultados. Por nombrar algunos ejemplos, podemos contar con FAIR (Facebook Artificial Intelligente Research), DeepMind, OpenAI o Google, entre muchos otros. Este caso es poco común, ya que las divisiones de empresas privadas publican en abierto los resultados de sus investigaciones como si se tratara de una universidad, permitiendo a otras empresas privadas seguir desarrollando soluciones desde donde ellos terminaron. Esto puede plantear una serie de problemas de funcionamiento de la investigación en IA, porque en el caso de estos grupos de investigación, la motivación última está guiada por las necesidades empresariales de sus matrices, ya que son las que financian la investigación, y esto puede cortar caminos de investigación en 

131 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

los que la aplicación de una cierta tecnología no sea fácilmente demostrable. Por suerte, numerosas universidades por todo el mundo siguen investigando estas tecnologías con mayor libertad investigadora, lo que les permite tener un margen mayor de investigación puramente teórica sin la presión de lo aplicable que pueda llegar a ser en un futuro. Estas universidades son, por ejemplo, el MIT, Standford, Princeton, Oxford, Edimburgh, Carnegie Mellon, Berkeley, Cambridge. 

Por otro lado, y directamente relacionado con esto, hay numerosas investigaciones sobre IA que no tienen una aplicación comercial directa, ni parece que vayan a tenerla. El ejemplo más actual de esto es el empleo de las Redes Adversarias Generativas o GANS, que hemos visto dos unidades atrás. Aunque los resultados de este tipo de redes neuronales son impresionantes, y suelen cautivar al público general además de al propio mundo investigador por su complejidad y capacidades, es difícil encontrar casos de uso comerciales a una red neuronal que transforma fotografías en cuadros de Monet más allá de la creación de un filtro en alguna aplicación de fotografía móvil. Esto sucede también con la tecnología de estimación de pose en tres dimensiones, que si bien permite conocer datos realmente sorprendentes del movimiento del cuerpo humano, solo es aplicable en casos muy concretos de entrenamiento deportivo de alto nivel o de prevención de riesgos laborales, y sin embargo a día de hoy hay cientos de grupos de investigación centrados en mejorar esta tecnología. Por el contrario, las aplicaciones más primitivas de la IA como la detección de objetos, la resolución de problemas mediante el razonamiento o la traducción entre diversos idiomas son las que más implementadas están en el mundo que nos rodea, y las que mayor cantidad de beneficios siguen proporcionando a las empresas de cualquier tamaño que las implantan. No es de extrañar, por tanto, que Google, Facebook, Amazon, Microsoft e IBM estén centrados en mejorar sus sistemas de visión artificial para la detección de objetos, de texto y de reconocimiento facial; y también de mejorar sus algoritmos de lenguaje natural para mejorar sus asistentes, sus buscadores web y su escritura automática de páginas web y aplicaciones. 

Pero no todo el sector de la IA son estas cinco grandes empresas. Un sinfín de empresas de pequeño y mediano tamaño tienen un negocio basado en la implantación real de la IA en casos de uso concretos para sectores muy específicos. Este tipo de empresa suele beber de conocimiento en abierto que tanto universidades como grandes empresas generan, y ser capaz de implantarlo en sus clientes de forma óptima y eficiente. Son este tipo de casos de uso en los que nos vamos a centrar en esta unidad. Si bien habrá un módulo en este máster para comprender de forma completa el proceso de captura de requisitos, definición e implantación de Inteligencia Artificial en proyectos del mundo real, es relevante completar esta introducción a la IA conociendo una serie de casos de uso seleccionados para esta tecnología, más allá de los grandes hitos de la historia. Si bien estos hitos han marcado el camino a seguir, son los pequeños proyectos de estas empresas los que hacen que la IA esté cada día en más sectores, en más países y, por tanto, que llegue a más gente. Por tanto, veremos una lista de algunos de los miles de casos de uso de la IA y, en concreto, del _Machine Learning_ y el _Deep Learning_ , que pueden ayudar a que comprendamos mejor las posibilidades infinitas que nos brinda esta tecnología. 

132 

**Módulo. Introducción a la Inteligencia Artificial** 

#### a. **Descubrimiento de fármacos y toxicología** 

Un gran número de los fármacos que se intentan desarrollar por parte de los laboratorios farmacéuticos fallan por una serie de razones entre las que se incluyen falta de eficacia, mal perfil de seguridad, interacciones con otros fármacos o dificultades para la fabricación. Gracias al desarrollo e implementación de modelos de aprendizaje profundo, es posible predecir los efectos de un medicamento sin necesidad de realizar ensayos clínicos sencillamente conociendo la composición molecular del mismo. Un ejemplo de este tipo de caso de uso es AtomNet, una red neuronal que es capaz de proponer medicamentos para tratar un patógeno concreto una vez conoce el genoma del mismo, así como posibles características clave del mismo. También se han empleado GANs (Redes Generativas Adversarias) fuera del ámbito de la visión artificial para tratar de proponer nuevas moléculas para tratar ciertas enfermedades, con una eficacia superior a la esperada. Entre este tipo de sistemas y los que ya hemos comentado que ayudan a la identificación de la estruc0tura tridimensional de proteínas y ARN, los laboratorios farmacéuticos comienzan a contar con asistentes que les permiten conocer los patógenos y diseñar medicamentos y vacunas de forma notablemente más rápida y eficaz que mediante experimentos reales desde el momento inicial. 

#### b. **Soporte al diagnóstico de imagen médica** 

También en el ámbito de la salud, peo en este caso desde el punto de vista del diagnóstico, la IA ha contribuido notablemente en los últimos años. En base a tecnologías de visión artificial como la detección y la segmentación de objetos, los científicos han sido capaces de detectar elementos anómalos en todo tipo de capturas médicas como radiografías, TC, TAC, resonancias magnéticas, imágenes de fondo de ojo… para el soporte al diagnóstico de enfermedades como el cáncer, las lesiones internas en órganos vitales o complicaciones de la diabetes en el fondo del ojo. En el ámbito del _Machine Learning_ general, existen modelos que permiten un análisis rápido y certero de ECG (Electrocardiogramas), Encéfalogramas y análisis de sangre y orina, para detectar en un tiempo muy reducido y sin saturar los servicios médicos enfermedades que de otra manera podrían pasar desaparecidas. 

#### c. **Bioinformática** 

Por último, como ejemplo en el caso de la comprensión del cuerpo humano y los procesos de la vida, la Inteligencia Artificial ha sido una pieza clave en el campo de la bioinformática. En este campo, los científicos de la vida tratan de comprender grandes conjuntos de datos relacionados con la biología para obtener conclusiones a gran escala. Uno de los ejemplos más sonados es la secuenciación del genoma humano, o la identificación de genes específicos que pueden desencadenar enfermedades en los seres humanos. Algoritmos como AlphaFold permiten a los científicos conocer y predecir aspectos de diversas moléculas con gran preci- 

133 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

sión. También se emplean algoritmos de aprendizaje profundo en el campo de la evolución, proponiendo automáticamente relaciones entre los distintos ancestros conocidos de una especie, para ayudarnos a trazar con mayor precisión todos los resquicios del árbol de la evolución. 

#### d. **Gestión de la relación con el cliente** 

En un ámbito más puramente empresarial, hay una gran cantidad de sistemas comerciales basados en aprendizaje profundo para el soporte en las empresas a la gestión de sus clientes. Entre otras cosas, estos sistemas tratan de calcular el retorno de la inversión (ROI) que puede llegar a arrojar una acción específica de relación con clientes o relaciones públicas, incluso a recomendar acciones específicas dadas las condiciones del entorno. Estas acciones se realizan mediante redes neuronales que reciben información acerca del mercado, los productos, las ventas y los clientes de una empresa, y que son capaces de ofrecer como salida un vector de acciones con una probabilidad de éxito recomendada para cada cliente. De igual forma, existen sistemas de estimación del ciclo de vida de los clientes y los productos, que reciben información comercial y tratan de estimar el número de años que estos podrán ser valiosos para una empresa. Estos algoritmos tienden a estar integrados en los paquetes de CRM (Customer Relationship Management), siendo módulos opcionales de los mismos que pueden ayudar enormemente a los directores comerciales y de márketing a tomar las mejores decisiones posibles. 

#### e. **Sistemas de recomendación** 

La gran mayoría de plataformas VoD (Video a Demanda), de compra online y de _streaming_ de música tienen una sección adaptada a cada usuario en la que le recomiendan qué es lo próximo que puede ver, comprar o escuchar. Estos algoritmos están basados en redes neuronales profundas que emplean los datos de millones de clientes y sus gustos para efectuar un proceso conocido como clustering en el que profundizaremos en otras unidades. Este proceso trata de crear de forma no supervisada perfiles de clientes que permitan agruparlos en un número finito de categorías. Según el perfil al que pertenezca un usuario, recibirá unas recomendaciones u otras en función de su comportamiento pasado y la contrastación del mismo con el del resto de usuarios de la plataforma. Estos algoritmos han permitido a estas plataformas basadas en internet generar contenido específico para nichos de mercado muy concretos, ya que ha arrojado luz sobre los tipos de clientes que tienen y las preferencias de los mismos. 

#### f. **Publicidad inteligente** 

Muy relacionado con los casos anteriores se encuentra el caso de la publicidad inteligente. El machine Learning aporta al mundo de la publicidad una serie de ventajas principales frente a aquellos que no lo emplean, que son: 

134 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

1. Mejor personalización 

Tal y como hacen las plataformas con sus propios usuarios al proporcionarles recomendaciones de hacia dónde ir en cada momento, los anunciantes tratan también de adecuar el mensaje al receptor de tal forma que se maximice la inversión. Para hacerlo, se emplean modelos de aprendizaje automático que, en base a las características que son capaces de estimar del consumidor por su comportamiento online, proponen un tipo de anuncios u otros. Estos modelos no cuentan con la información real del cliente potencial, como sí hacen los sistemas de recomendación, sino que la clave de su éxito es la capacidad de estimar características clave de una persona como sexo, edad, estado civil, o rango salarial sencillamente por su comportamiento online, para posteriormente, ya sí, hacer recomendaciones sobre él. 

2. Mejor toma de decisiones sobre publicidad 

En la actualidad, más del 65% de las empresas que se anuncian en internet emplean algún tipo de soporte basado en la IA para la toma de decisiones estratégicas de publicidad. El algoritmo en este caso, tiene en cuenta los datos del contexto en un momento determinado y la audiencia objetivo, para así poder proponer un tipo de campaña publicitaria u otra en función de una gran cantidad de datos. Habitualmente la toma de decisiones se tomaba en base a datos, pero nuestra capacidad de encontrar relaciones entre diversas variables es ínfimamente inferior de la de un modelo de ML, y es por esto que las empresas confían en los algoritmos para las decisiones más importantes de su estrategia publicitaria. 

3. Interacciones y conversaciones más personales 

Gracias a los avances de procesamiento del lenguaje natural y a la generación de texto, las empresas pueden crear herramientas de marketing conversacionales, en las que mantener una experiencia personal e individual con un “agente” de la marca de tal forma que no sea una actividad meramente pasiva. En la actualidad están empezando a aparecer banners con anuncios en los que se puede interactuar y conversar con el anuncio, en un intento más de acercarse al potencial cliente lo máximo posible. 

4. Mejor creatividad basada en datos 

De la misma manera en la que en el campo de los labortatorios farmacéuticos se emplean algoritmos de IA para tratar de predecir la eficacia y toxicidad de un medicamento teórico, en el momento actual existen numerosas herramientas que tratan de predecir el éxito de una campaña publicitaria por medio de modelos de aprendizaje automático. Además, existen algorit- 

135 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

mos que tratan de mejorar el proceso creativo proponiendo colores, mensajes e imágenes que pueden encajar en el anuncio según el público objetivo, tratando así de reducir la incertidumbre de los equipos creativos ante el éxito de sus campañas. 

5. Alcanzar los mejores medios para llegar al público objetivo 

Por último, la IA es capaz de recomendar canales en los que publicar una campaña para que genere el mayor impacto posible dentro del público objetivo. Una vez determinado el mensaje y el público objetivo, los algoritmos, previamente entrenados, ofrecerán una serie de alternativas entre los distintos canales, páginas web, influencers y otras opciones para ofrecer las mejores soluciones en función de las características concretas del lanzamiento. 

Tanto IBM, como Google, Amazon y Microsoft tienen disponibles servicios de recomendación y mejora de la publicidad online a través de sus servicios Cloud. 

- g. **Restauración de imágenes** 

Uno de los usos más visuales de la IA es el de la restauración de videos e imágenes de otras épocas. Mediante una mezcla tanto de CNN como de GAN, se han publicado modelos que colorean fotografías en blanco y negro de forma automática, así como otros que eliminan el ruido y la distorsión de las imágenes, aumentan las imágenes por segundo de un video o la resolución de una imagen. En la mayoría de casos, estos retos se han tratado se ha tratado como un problema de aprendizaje supervisado. Para entrenar una CNN que colorea imágenes, es suficiente con generar un conjunto de prueba en el que la entrada son imágenes artificialmente convertidas a blanco y negro, y la inferencia esperada el correspondiente color real de estas imágenes. De igual forma, se puede reducir la resolución de una imagen de forma artificial para emplearla en el entrenamiento de una red neuronal, y emplear su pareja de resolución completa como solución al problema. Con los vídeos se aplica la misma lógica. Si se convierte un vídeo de 60 fps a otro de 30fps habrá un frame extra entre cada par de frames que habrá desaparecido. Si la red neuronal es capaz de inferir estos frames con éxitos para un banco de videos lo suficientemente extenso, será capaz de inferir frames en videos nuevos que no hayan formado parte de su entrenamiento. Este tipo de aplicaciones no tienen un uso comercial directo, pero generan contenido audiovisual interesante tanto para las redes sociales como, en algunas ocasiones, para exposiciones sobre momentos pasados de la historia. Por ejemplo, en este video se puede ver una grabación de Nueva York en el año 1911 en el que han actuado tres modelos distintos. Por un lado, se han pasado las imágenes originales a 4k, posteriormente se han inferido todos los frames necesarios para que el video tenga 60 fps y por último se han coloreado de forma totalmente automática. Aunque el resultado dista de ser perfecto, es posible conocer el Nueva York de hace más de un siglo de una forma más cercana y realista. Uno 

136 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

de los artículos más recientes de “upscaling” fue publicado en 2021 y es capaz de ampliar la resolución de una fotografía de un rostro ocho veces, manteniendo las proporciones faciales, como se puede comprobar en el siguiente ejemplo. 



#### h. **Detección del fraude financiero y predicción de mercados financieros.** 

Otro uso para el que se ha empleado el aprendizaje profundo ampliamente es la detección de la evasión fiscal, el lavado de dinero y el fraude en general. Para conseguir modelos que lancen alertas precisas sobre este tipo de comportamientos, es suficiente con seguir los pasos básicos del _Deep Learning_ . Es necesario contar con una base de datos etiquetada, en este caso las características que nos interesen serán características financieras de determinadas personas. Ingresos, origen de los ingresos, gastos, declaración de la renta, movimientos bancarios y ubicación de las cuentas, por ejemplo. La etiqueta será si dicha persona cometía algún tipo de fraude, y cual. Una vez se ha reunido una base de datos suficientemente amplia, se puede tratar de encontrar un modelo óptimo para que clasifique a individuos de interés. Otros modelos optan por el aprendizaje no supervisado. En este caso, los modelos procesan toda la información financiera de todas las personas posibles, para comprender que es un estado financiero habitual. Una vez comprendido, pueden detectar anomalías que no encajen en el modelo general financiero que han alcanzado, y de esta forma dar la voz de alarma. 

#### i. **Revisión automática de campos de cultivo y control de calidad alimentario** 

Gracias a la tecnología actual de visión artificial, entre otras a la conjunción de imagen hiperespectral y de aprendizaje automático, el sector de la alimentación está viviendo una revolución en todas las partes de su cadena. La imagen hiperespectral, como veremos en detalle en unidades futuras, permite observar con detalle la parte de la luz que no es visible al ojo humano y que permite, redes neuronales mediante, conocer detalles críticos de los objetos que observa a nivel molecular. Cada material y estado de la materia reflejan la luz de forma distinta, lo que genera 

137 

**Centro Europeo de Postgrado                                                             Módulo. Introducción a la Inteligencia Artificial** 

para cada uno de ellos una marca específica que se llama “huella espectral”. Si un modelo es capaz de diferenciar huellas espectrales gracias a un proceso de aprendizaje supervisado, entonces puede distinguir moléculas, materiales complejos y estados de la materia con tan solo recibir una imagen en una banda espectral fuera del rango visible. 

En el caso de la agricultura, el procesamiento mediante _Machine Learning_ de las imágenes hiperespectrales de campos permite detectar problemas antes de las plantas sufran sus consecuencias. Gracias a pequeños drones que sobrevuelan las superficies de cultivo, posteriormente los científicos de datos pueden determinar si el nivel de irrigación de un campo es óptimo, o si un campo sufre una plaga en concreto. Una vez el fruto está cosechado, la imagen hiperespectral ayuda a clasificar de forma objetiva el punto de maduración del mismo por la formación de azúcares en su superficie, así como a separarlo de objetos no deseados como piedras o cáscaras. 

Una vez en la cadena de producción y envasado, modelos entrenados específicamente para esta finalidad son capaces de determinar el nivel de grasa y de proteína de los alimentos, sus niveles de humedad y su frescura, para así realizar un control de calidad completo y no invasivo en sus líneas de producción. 



#### j. **Astronomía** 

Como en otros campos de la ciencia, la astronomía se ha visto muy beneficiada de los avances en aprendizaje profundo para acelerar, optimizar y aumentar la productividad y precisión de muchos de sus procesos. En el caso del aprendizaje supervisado, los astrónomos han entrenado modelos de Machine Learning para ser capaces de clasificar automáticamente información recibida por los telescopios en diferentes tipos de estrellas o quásares. También se emplean para calcular la distancia de distintos cuerpos en el espacio en función de la información que se captura de ellos sin necesidad de interacción humana. 

138 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

Por otro lado, se ha aplicado el aprendizaje no supervisado a descubrir posible información que se encuentra en datos ya capturados pero que, al carecer de un método de detección, no han sido clasificados. Por ejemplo, hay modelos que han encontrado grupos de planetas donde hasta el momento solo se había visto ruido, gracias a una revisión concienzuda de todos los datos almacenados hasta el momento. 

#### k. **Seguros y banca** 

En el ámbito de los seguros se emplean modelos de ML para la predicción del riesgo de los clientes. Las compañías de seguros llevan años desarrollando algoritmos para analizar las probabilidades de que cada uno de sus clientes sufran un contratiempo para el que estén asegurados. Gracias al aprendizaje no supervisado, las compañías de seguros han sido capaces de identificar cuáles son los factores más relevantes a la hora de predecir si un cliente va a causar un accidente o va a sufrir una determinada enfermedad. En el caso específico de la banca, se han desarrollado numerosos modelos privados para predecir el riesgo crediticio. A la hora de decidir si conceder un préstamo a uno de sus clientes, los bancos emplean estos modelos en base a una serie de variables como el salario, la liquidez, la rentabilidad del préstamo… para tomar una decisión objetiva acerca de sus potenciales clientes. Gracias a estos modelos, la banca reduce el nivel de incertidumbre, e incluso algunas corporaciones en concreto han comenzado a operar con operaciones automáticas, en las que si el algoritmo considera que una operación debe realizarse, se ejecuta sin necesidad de la aprobación posterior de un gestor. 

139 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 

## **Bibliografía** 

- “What Is Artificial Intelligence?” John McCarthy, Stanford University, 2004 

- “Minds, Brains, and Programs”, John Searle, Behavioral and Brain Sciences, 1980 

- “Computing Machinery and Intelligence”, Allan M. Turing, Mind, 1950 

- “What to Think About Machines That Think: Today’s Leading Thinkers on the Age of Machine Intelligence”, John Brockman, Paperback, 2015 

- “Superintelligence: Paths, Dangers, Strategies.”, Nick Bostrom, Oxford University Press, 2014 

- “DENDRAL: A Case Study of the First Expert System for Scientific Hypothesis Formation”, Lindsay, Robert K., Bruce G. Buchanan, E. A. Feigenbaum, and Joshua Lederberg, Artificial Intelligence 61, 1993 

- “The Master Algorithm: How the Quest for the Ultimate Learning Machine Will Remake Our World”, Pedro Domingos, Penguin Books, 2015 

- “Broad band: the untold story of the women who made the Internet”. Claire L Evans, 2018 

- “La quimera del autómata matemático. Del calculador medieval a la máquina analítica de Babbage”, Guijarro, V.; González, L, Cátedra, (2010). 

- “Intelligent Machinery”, Allan M. Turing, The Turing Archive, 1948 

- “AI: The Tumultuous Search for Artificial Intelligence”, Daniel Crevier, BasicBooks, 1993 

- “The Chinese Room Argument”, David Cole, The Stanford Encyclopedia of Philosophy, 2004 

- “A Logical Calculus of the Ideas Immanent in Nervous Activity”, Walter Pitts, Bulletin of Mathematical Biophysics, 1943 

- “Machines Who Think (2 ed.)”, Pamela McCorduck, A. K. Peters, 2004 

- “AI Past, Present, Future”, Meg Houston, Dartmouth College AI@50, 2006 

- “Strategic Computing: DARPA and the Quest for Machine Intelligence”, Alex Roland and Phillip Shiman, Cambdrige Mass, 2002. 

140 

**Centro Europeo de Postgrado                                                               Módulo. Introducción a la Inteligencia Artificial** 

- “Neural Networks: A Systematic Introduction”, R. Rojas, Springer, 1996 

- “How the backpropagation algorithm works”, Michael A Nielsen, Neural Networks and Deep Learning, 2015 

- “Backpropagation Applied to Handwritten Zip Code Recognition”, LeCun, B. Boser, J. S. Denker, D. Henderson, R. E. Howard, W. Hubbard, L. D. Jackel; AT&T Bell Laboratories, 1986 

- “Gradient-based learning applied to document recognition”; LeCun, Yann; Bottou, Léon; Bengio, Yoshua; Haffner, Patrick; Proceedings of the IEEE., 1988 

- “The Summers and Winters of Artificial Intelligence”, Tad Gonsalves, Mehdi, 2017 

- “Behind Deep Blue: Building the Computer that Defeated the World Chess Champion”, Feng-hsiung Hsu, Princeton University Press, 2002 

- “SURFACE NAVIGATION AND MOBILITY INTELLIGENCE ON THE MARS EXPLORATION ROVERS” Mark Maimone, Jeffrey Biesiadecki, Edward Tunstel, Yang Cheng, Chris Leger NASA Jet Propulsion Laboratory, 2004 

- “The Athena SDM rover: A testbed for Mars rover mobility”, J. Biesiadecki, M. Maimone, and J. Morrison, Proc. Intl. Symp. on Artificial Intelligence, Robotics and Automation in Space, 2001. 

- “Say Hello to Stanley”, Joshua Davis, Wired, 2006 

- “BigDog Overview”, Boston Dynamics, Press Release, 2008 

- “The Face Detection Algorithm Set to Revolutionize Image Search”, MIT Technology Review, 2015 

- “Who is who at different cameras: people re-identification using depth cameras”; Albiol, A., Albiol, A., Oliver, J., Mossi, J.M Computer Vision, IET. Vol 6(5), 2012 

- “Our Biometric Future: Facial Recognition Technology and the Culture of Surveillance”, Kelly Gates, NYU Press, 2011 

- “NEIL: Extracting Visual Knowledge from Web Data”, Xinlei Chen, Abhinav Shrivastava, Abhinav Gupta; International Conference on Computer Vision (ICCV), 2013 

- “Mastering the game of Go with deep neural networks and tree search”, Silver, David; Huang, Aja et al, Nature, 2016 

- “Generative Adversarial Networks in Computer Vision: A Survey and Taxonomy”. 

141 

**Módulo. Introducción a la Inteligencia Artificial** 

**Centro Europeo de Postgrado** 

Wang, Zhengwei; She, Qi; Ward, Tomas E., arXiv, 2019 

- “Language Models are Few-Shot Learners”, Tom B. Brown et al, arXiv, (2020), 

- “Artificial intelligence driven assessment of routinely collected healthcare data is an effective screening test for COVID-19 in patients presenting to hospital”, Andrew AS Soltan et al, The Lancet, 2020 

- “How Baidu is bringing AI to the fight against coronavirus”, Baidu, MIT Technology Review, 2020 

- “YOLOv4: Optimal Speed and Accuracy of Object Detection”, Alexey Bochkovskiy et al, arXiv, 2020 

- “MACHINE LEARNING IN ASTRONOMY: A PRACTICAL OVERVIEW”, Dalya Baron, arXiv, 2019 

- “A Very Brief Introduction to Machine Learning with Applications to Communication Systems”, Simeone, O; Universidad de Cornell, 2018 

- “Artificial Intelligence: A Modern Approach”, Tercera Edición, Stuart Russel y Peter Norvig, Pearson, 2016 

- “Progress in digital integrated electronics”, G. E. Moore, IEDM Technical Digest, 1975 

- “AI Predictions 2021”, Price Waterhouse Cooper, 2021 

142 







**CEUPE** Centro Europeo de Postgrado 

**Web** 

www.ceupe.com 

**E-mail** info@ceupe.com 

