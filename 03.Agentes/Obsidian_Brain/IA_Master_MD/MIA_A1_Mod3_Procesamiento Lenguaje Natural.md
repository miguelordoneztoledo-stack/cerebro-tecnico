---
tags:
  - master_ia
  - teoria
source: MIA_A1_Mod3_Procesamiento Lenguaje Natural.pdf
---

# **Módulo Procesamiento del Lenguaje Natural (NLP)** 



# **Módulo Procesamiento del Lenguaje Natual (NLP)** 

|**1. INTRODUCCIÓN AL PROCESAMIENTO DEL LENGUAJE NATURAL (NLP) ..........04**<br>1.1. QUÉ ES EL PROCESAMIENTO DEL LENGUAJE NATURAL ..................................04<br>|
|---|
|1.2. OBJETIVOS Y ARQUITECTURA BÁSICA DE UN SISTEMA NLP ...........................06|
|1.3. ANTECEDENTES DEL NLP ACTUAL ..................................................................10|
|**2. PREPROCESAMIENTO DE TEXTOS: EL PRIMER PASO EN EL NLP ......................15**<br>|
|2.1. LAS EXPRESIONES REGULARES Y LA SEGMENTACIÓN DE PALABRAS Y|
|FRASES ..................................................................................................................15<br>|
|2.2. QUÉ ES UNA PALABRA ...................................................................................17|
|2.3. NORMALIZACIÓN DEL TEXTO .........................................................................18|
|2.3.1. TOKENIZACIÓN .......................................................................................19|
|2.3.2. NORMALIZACIÓN DEL FORMATO DE LAS PALABRAS ..............................25|
|2.3.3. SEGMENTACIÓN DE FRASES Y ORACIONES ............................................32|
|**3. CATEGORIZACIÓN, AUTOCORRECCIÓN Y AUTOCOMPLETADO DE TEXTO .....36**|
|3.1. AUTOCORRECCIÓN Y ALGORITMOS DE ESTIMACIÓN DE DISTANCIA .............36|
|3.1.1. ESTIMACIÓN DE LA DISTANCIA ENTRE PALABRAS...................................37<br>|
|3.1.2. FILTRADO DE CANDIDATOS Y ESTIMACIÓN DE PROBABILIDAD ...............41|
|3.2. CATEGORIZACIÓN DE PALABRAS (PART OF SPEECH TAGGING) ......................43|
|3.2.1. HIDDEN MARKOV CHAINS Y EL ALGORITMO VITERBI .............................45|
|3.3. N-GRAMS – AUTOCOMPLETADO DE TEXTO ...................................................58|
|3.3.1. MATRIZ DE RECUENTO (COUNT MATRIX) ................................................63|
|3.3.2. APLICAR UN MODELO DE LENGUAJE BASADO EN N-GRAM ...................64|
|3.3.3. EVALUACIÓN DE MODELOS DE LENGUAJE: PERPLEJIDAD (PERPLEXITY) ..64|
|**4. NLP CON MACHINE LEARNING. REPRESENTACIÓN DE PALABRAS,**<br>**SEMÁNTICA, DISTANCIA Y RELACIÓN ENTRE PALABRAS .....................................66**|
|4.1. VECTORS AND WORD EMBEDDINGS ..............................................................66|
|4.1.1. MATRIZ DE CO-OCURRENCIA: CO-OCURRENCE MATRIX ........................69|
|4.1.2. MEDICIÓN DE DISTANCIA ENTRE PALABRAS: LA DISTANCIA DEL<br>COSENO ...........................................................................................................72|
|4.1.3. TF – IDF: TERM FREQUENCY – INVERSE DOCUMENT FREQUENCY Y<br>PPMI .................................................................................................................75|
|4.2. WORD2VEC ...................................................................................................80|
|4.2.1. SKIP-GRAM WITH NEGATIVE SAMPLING (SGNS) .....................................81|
|4.2.2. CONTINUOUS BAG OF WORDS (CBOW) .................................................84|
|**5. PROCESAMIENTO DEL LENGUAJE NATURAL CON DEEP LEARNING ..............101**|
|5.1. RECURRENT NEURAL NETWORKS (RNN) .......................................................102|
|5.2. LONG SHORT-TERM MEMORY (LSTM) ..........................................................111|
|5.2.1. LSTM PARA LA CLASIFICACIÓN DE TEXTOS: UN EJEMPLO ....................118|
|5.2.2. APLICACIÓN DE UNA RED LSTM EN NLP: NAMED ENTITY|
|RECOGNITION (NER) .......................................................................................125|
|5.2.3. OTRAS APLICACIONES DE LA ARQUITECTURA LSTM ............................129|



|**6. NLP BASADO EN MECANISMOS DE ATENCIÓN. TRANSFORMERS .................130**|
|---|
|6.1. SELF-ATTENTION LAYER ................................................................................131|
|6.2. TRANSFORMER BLOCK .................................................................................136|
|6.3. TRADUCCIÓN SEQ2SEQ CON MECANISMOS DE ATENCIÓN .........................136|
|6.4. TRANSFORMERS PARA GENERAR MODELOS DE LENGUAJE Y GENERACIÓN|
|DE TEXTO ............................................................................................................141|
|6.5. BIDIRECTIONAL ENCODER REPRESENTATIONS FROM TRANSFORMERS (BERT) 142|
|6.6. GENERATIVE PRE-TRAINED TRANSFORMERS (GPT-2 Y GPT-3) ........................143|
|**BIBLIOGRAFÍA ........................................................................................................145**|



**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

## **1. Introducción al Procesamiento del Lenguaje Natural (NLP)** 

_“El lenguaje natural, en las disciplinas de la neuropsicología, la lingüística y la filosofía del lenguaje, es un lenguaje que ha evolucionado de forma natural entre seres humanos a través de la repetición, sin ningún tipo de planificación ni premeditación.”_ 

### **1.1. Qué es el Procesamiento del Lenguaje Natural** 

Hasta este momento hemos estudiado en este máster diversas áreas de la Inteligencia Artificial, desde puntos de vista tanto teóricos como prácticos. Hemos analizado los tipos de IA, su historia, los modelos más conocidos de _Deep Learning y Machine Learning_ . También hemos aprendido cómo funciona la Visión Artificial, así como los dispositivos de cómputo que soportan la ejecución de este tipo de modelos y su posible despliegue en cloud. 

De entre las habilidades principales que se esperan de un sistema inteligente, en esta asignatura trataremos el lenguaje humano. Recordemos que el primer test que trató de determinar si un sistema era verdaderamente inteligente, el test de Turing, se basaba exclusivamente en la capacidad de responder preguntas en lenguaje natural. Así sucede también con un experimento más evolucionado, la habitación china, en la que se trata de demostrar que sólo si el sistema inteligente comprende el significado detrás de la gramática y sintaxis es cuando realmente se puede determinar que ciertamente tiene inteligencia. 

Como sucede en todos los ámbitos, estas discusiones de carácter teórico no influyen en el desarrollo real de la tecnología. La tecnología de procesamiento y comprensión del lenguaje natural está en constante evolución y crecimiento, aportando soluciones a diversos retos presentes en la totalidad de los sectores económicos y revolucionando la forma de atender clientes, extraer información de interacciones y de procesar datos no estructurados en busca de datos agregados para mejorar la calidad de vida de la población. En definitiva, la primera idea que debe quedarnos es que **el NLP transforma información no estructurada procedente de lenguaje natural en información estructurada** . 

04 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

La primera pregunta que puede surgir a la hora de abordar esta disciplina es ¿qué es el lenguaje natural? El lenguaje natural, en las disciplinas de la neuropsicología, la lingüística y la filosofía del lenguaje, es un lenguaje que ha evolucionado de forma natural entre seres humanos a través de la repetición, sin ningún tipo de planificación ni premeditación. El lenguaje natural está presente en diversas formas, como puede ser el lenguaje hablado – discurso – o los símbolos – texto escrito – entre otros. 

El concepto de lenguaje natural surge en contraposición a los lenguajes construidos, aquellos que sí que han sido planificados con antelación. Por ejemplo, los lenguajes de programación informáticos como Python, son lenguajes artificiales. Cumplen perfectamente la función de comunicación del lenguaje, permitiendo al desarrollador indicar a la máquina las instrucciones que debe realizar. Sin embargo, estos lenguajes no evolucionan de forma natural. En caso de ser modificados, estos cambios surgirán de un diseño previo por parte de los responsables de mantener el lenguaje de programación. 

Ocurre lo mismo con otros lenguajes artificiales como el de la lógica formal o incluso de algún intento de lenguaje humano completo como el esperanto. 

Para procesar un lenguaje artificial no es necesario contar con un sistema inteligente. Estos lenguajes tienen normas gramaticales estrictas, sintaxis limitadas y, en definitiva, una estructura predecible y procesable. 

El proceso de convertir un código fuente escrito en C++ a lenguaje de ensamblador – instrucciones de bajo nivel – y en última instancia a código máquina – binario – es un proceso determinista. Para el procesamiento de este tipo de lenguajes se emplean los conocidos como Procesadores de Lenguaje (LP) que no debemos confundir con los Procesadores de Lenguaje Natural. 

Los Procesadores de Lenguaje no son parte por tanto de la Inteligencia Artificial, y quedan fuera del alcance de este máster. Basta con saber que están basados en la Teoría de Autómatas y Lenguajes Formales, definida por diversos tipos de gramáticas y autómatas que parten de las investigaciones de Allan Turing a lo largo de su vida. 

Estos lenguajes artificiales son relativamente sencillos de procesar por un computador. Sencillamente es necesario recopilar todas las reglas lógicas que definen el funcionamiento de dicho lenguaje, y codificarlas para obtener un Procesador de Lenguaje. En un lenguaje de programación no podemos cambiar el orden de las palabras, ya que, si lo hiciéramos, no podríamos compilar nuestro programa y el Procesador de Lenguaje arrojaría un error de compilación. 

05 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Por ejemplo, en Java no podemos emplear una variable antes de usarla, como en este ejemplo: 



Sin embargo, en lenguaje humano podemos expresar perfectamente que “el número a tiene un valor de 150000 y es un entero”, sin que nadie tenga un problema para comprenderlo. 

Este pequeño ejemplo es, en esencia, la explicación de la gran complejidad que tiene el paso de un Procesador de Lenguaje (LP) a un Procesador de Lenguaje Natural (NLP), y la explicación de por qué el primero no es considerado un sistema inteligente, pero el segundo requiere de técnicas de Inteligencia Artificial avanzadas para realmente conseguir comprender un lenguaje natural. 

### **1.2. Objetivos y arquitectura básica de un sistema NLP** 

Comprender el lenguaje natural es solo uno de los objetivos en los que se puede aplicar el conocimiento del lenguaje natural. En este sentido, partimos de lenguaje natural ya construido por un hablante de dicho humano, y nos proponemos comprenderlo. Veremos a lo largo de esta unidad y las siguientes **qué significa comprender el lenguaje** . Por ahora, es suficiente con que comprendamos que este es uno de los dos sentidos en los que podemos aplicar el conocimiento del lenguaje. Este fue el comienzo del procesamiento del lenguaje natural, como estudiaremos en breve. 

Sin embargo, actualmente los esfuerzos del mundo investigador están centrados en el sentido contrario. En **generar contenido en lenguaje natural** para que un humano pueda comprenderlo como si hubiera sido creado por un hablante nativo de dicho lenguaje. 

El conjunto de ambos sentidos consigue que un sistema inteligente artificial pueda comunicarse con un sistema inteligente biológico o, dicho de otra forma, un humano. El ejemplo más lejano de esta doble comunicación se remonta a los primeros chatbots como ELIZA, pero veremos que no ha sido hasta descubrimientos recientes que los sistemas inteligentes no han sido capaces realmente de generar contenido desde cero que pueda ser interpretado como válido completamente. 

Podríamos hacer una analogía con la visión artificial de la siguiente manera. La comprensión del lenguaje natural sigue un proceso de captura (texto o audio), procesamiento (extracción del contenido semántico) y acción. Esto es lo que hacen la mayoría de modelos de clasificación, detección, segmentación de objetos… Capturan imágenes o vídeos, los procesan y toman decisiones según los objetos encontrados. 

06 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Por otro lado, tenemos las GAN en visión artificial. Estos modelos generativos crean contenido visual válido a partir de inputs de pequeño tamaño, dando lugar a un contenido de nueva creación producido por un sistema inteligente. 

Los modelos generativos de lenguaje tienen el mismo funcionamiento. A partir de un breve input, son capaces de escribir historias, artículos, reseñas e incluso programas informáticos, como veremos a lo largo de la asignatura. 

En la siguiente figura podemos ver de forma esquemática los dos sentidos en los que se puede aplicar el Procesamiento del Lenguaje Natural para la interacción entre un sistema y un usuario humano. 



En según qué referencias encontraremos estas dos orientaciones del NLP diferenciadas en dos conceptos separados: Comprensión del Lenguaje Natural (NLU) y Generación de Lenguaje Natural (NLG). 

- **_Natural Language Understanding_ (NLU)** . Este subconjunto del NLP hace referencia a las técnicas de Procesamiento del Lenguaje Natural que emplean un análisis sintáctico y semántico del texto o el discurso para tratar de comprender el significado de una oración. La sintaxis hace referencia a la estructura gramatical de la oración, mientras que la semántica estudia el significado de cada una de sus palabras y en última instancia de la oración completa. Estos modelos tratan de encontrar entidades reconocibles y las relaciones que en el texto se establecen entre ellas, de igual forma que lo hacemos los seres humanos a lo largo de una conversación. A lo largo de esta asignatura estudiaremos diversas aplicaciones del NLU como parte del NLP, como pueden ser el análisis de sentimientos o la autocorrección de palabras durante la escritura. 

07 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

- **_Natural Language Generation_ (NLG)** . En este caso, las técnicas de NLG hacen referencia a todos los modelos generativos de lenguaje. En lugar de comprender oraciones, se generan conformando un texto completo en base a una determinada entrada. Uno de los usos más extendidos del NLG más allá de la creación de textos completos es la generación automática de resúmenes de conversaciones transcritas o artículos científicos. Por descontado, los modelos de NLG tienen que comprender la sintaxis y semántica del lenguaje, para así poder planificar los textos y oraciones que se generan en base a la entrada dada. 

Ambos subconjuntos tienen una serie de técnicas determinadas, que estudiaremos a lo largo de la asignatura, desde las más sencillas como la conocida como “N-gram” hasta los métodos más complejos e innovadores como los Transformers basados en mecanismos de atención. 

En el NLP actual nos encontramos con una serie de objetivos que trabajaremos a lo largo de la asignatura, entre los cuales destacan: 

- **Preprocesado del texto:** Todo sistema de NLP requiere de un previo procesado del texto de entrada para poder trabajar con él de forma estructurada. Veremos diversas técnicas que nos permitirán normalizar los textos para facilitar la labor de nuestros algoritmos de lenguaje. 

- **_Parts-of-Speech tagging (POS)_** . Este tipo de objetivo trata de realizar una clasificación sintáctica de las palabras de cada una de las oraciones de nuestros textos. Si un algoritmo e NER clasifica las palabras en entidades, un algoritmo de POS las clasifica por la función que desempeñan en una frase. De esta forma, todas las palabras son clasificadas en alguno de los tipos: “nombre”, “verbo”, “adverbio”, “preposición”, “conjunción”… Para posteriormente poder analizar el significado semántico de la frase una vez desentrañada su estructura sintáctica gramatical. 

- **Vectorización:** **_Word Embedding._** Estos procesos son una parte esencial en el NLP, y consisten en convertir todas las palabras u oraciones de un corpus en un conjunto de vectores formados por números reales. En definitiva, se trata de generar un espacio vectorial numérico que represente las diferentes palabras que contiene un texto, para posteriormente realizar sobre dichos vectores o bien un análisis gramatical - o sintáctico – o bien un análisis de contenido – o semántico – para comprender el texto de entrada. 

08 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

- **Autocorrección y autocompletado.** Muchos modelos de NLP actuales están centrados en la ayuda al ser humano cuando este escribe textos. Prácticamente todos los procesadores de texto, las herramientas de correo electrónico y los teclados en nuestros dispositivos inteligentes cuentan con sistemas que permiten detectar errores en la escritura tanto sintácticos como semánticos, así como para el autocompletado de las frases haciendo más rápida la tarea de escribir y facilitando este proceso a personas con dificultades de visión u otras condiciones de salud. Veremos diversas formas de predecir palabras dada una frase incompleta, así como de medir la distancia entre dos palabras para poder seleccionar aquella que más se acerque a una palabra incorrecta o incluso a una palabra correcta pero que no tenga sentido dado el contexto del conjunto de la frase o el texto con el que estemos trabajando. 

- **Identificación de lengua:** Este objetivo trata de reconocer automáticamente el idioma en el que está escrito un texto. Si bien no es un paso esencial para el NLP -ya que el desarrollador siempre puede indicarlo de antemano – sí que es interesante para casos de uso relativamente inciertos o multilenguaje. 

- **_Named-Entity Recognition (NER)._** Este es uno de los objetivos más extendidos del NLP desde hace años. Su tarea es sencilla, clasificar todas las palabras que sea posible dentro de una serie de entidades previamente definidas. Podríamos considerarlo como un objetivo similar a la clasificación de objetos en visión artificial. Por ejemplo, podríamos tener entidades como “ubicación”, “nombre de persona”, “fecha y hora”, “divisa”, “organización”, “disciplina”… Un algoritmo de NER clasificará todas las palabras de nuestro corpus que pertenezcan a alguna de las entidades para las que ha sido entrenado. 

- **Análisis de sentimientos** **_(Sentiment Analysis)_** . Los modelos de análisis de sentimientos tratan de identificar cualidades subjetivas de un texto, como pueden ser el tono general, emociones específicas (enfado, alegría, tristeza, miedo), sarcasmo, ironía, confusión, duda… Así como opiniones expresadas por el hablante. Son algoritmos muy interesantes para extraer opiniones generalizadas de grandes cantidades de datos, como puede ser el análisis de reseñas de un producto a la venta en internet. 

- **Traducción automática.** Modelos capaces de convertir el texto de un lenguaje a otro manteniendo el significado y respetando la sintaxis gramatical del lenguaje de destino. Este fue uno de los primeros objetivos que se planteó el mundo del Procesamiento del Lenguaje Natural en sus inicios a mitad de siglo XX, como veremos a continuación. 

09 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

- **_Word-Sense Disambiguation (WSD)_** . En ocasiones los algoritmos de NLP se encuentran con palabras que tienen más de una acepción en el diccionario, es decir, que tienen varios significados. Es vital contar con métodos capaces de realizar una desambiguación de estas palabras para poder comprender realmente el significado de un texto. 

- **Correferencia o coindexación** **_(Co-reference resolution)_** . La correferencia es un fenómeno en el que en una oración se hace referencia a una entidad que ha aparecido previamente en la misma. Por ejemplo, en la oración “No pude ayudar a Juan, lo perdí de vista rápidamente”, a quien perdí de vista fue a Juan, y esto está implícito en el correcto uso de un pronombre como  “lo”. En ocasiones este fenómeno no es trivial, y es esencial conseguir que nuestros sistemas inteligentes distingan la correferencia en los textos para no perder gran parte del significado de las oraciones al no poder trabajar con este fenómeno lingüístico. 

- **Resumen de documentos y descubrimiento de temas** **_(Topic Discovery)._** A partir de un documento completo o un texto complejo, estos modelos aprenden a devolver una sinopsis del mismo, resumiendo su contenido más importante y priorizando los conceptos que en dicho texto se muestran. Son muy empleados para hacer minería de datos en internet, ya que consiguen facilitar el procesamiento de grandes cantidades de información. Los algoritmos de topic Discovery no tratan de resumir un texto en lenguaje natural, sino que persiguen extraer una serie de temas que se han tratado en el texto, por lo que son modelos más sencillos que aquellos que también aplican generación del lenguaje natural para la producción de resúmenes. 

### **1.3. Antecedentes del NLP actual** 

Tal y como hemos procedido a hacer en otras asignaturas, vamos a tratar de comprender de forma breve el camino que ha recorrido el campo del Procesamiento del Lenguaje Natural desde las primeras aproximaciones formales al lenguaje humano hasta las últimas tendencias. 

Siete años después de que Alan Turing propusiera su test para diferenciar una máquina de un ser humano, surgió, en 1957, uno de los hitos considerados como puntos iniciales de la disciplina del NLP. 

En este año, el reconocido lingüista estadounidense Noam Chomsky identificó uno de los mayores retos a los que deberían enfrentarse los sistemas que trataran de superar el test de Turing, escribiendo su libro “Estructuras sintácticas”, que sería considerado por la revista Time como uno de los 100 libros más importantes de la historia. En este ensayo Chomsky trataba de demostrar la problemática que suponen las frases gramaticalmente correctas, pero sin sentido aparente. 

10 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Para ilustrarlo empleó una célebre frase en inglés: “ _Colorless green ideas sleep furiously_ ”, que traducido al español sería “Las ideas verdes incoloras duermen furiosamente”. Usando esta frase como ejemplo mostró que los sistemas que pretendieran cumplir con las pruebas del test de Turing, o dicho de otra forma, los primeros sistemas de NLP, tendrían que tener más capacidades que la mera comprobación de la corrección gramatical de una oración. Las consecuencias de esta afirmación serían esenciales para distinguir dos grandes bloques de actuación de los sistemas de NLP que siguen vigentes en la actualidad. 

En definitiva, Chomsky sostenía que la sintaxis (la corrección estructural de una oración según una gramática) y la semántica (el significado de dicha oración en función de los significados individuales de cada palabra y el conjunto de todas ellas) son independientes. 

La sintaxis es un aspecto del lenguaje que se puede estudiar desde una perspectiva meramente formal, es decir, en base a un conjunto de reglas y símbolos como son los de la lógica formal. Por ello, una gramática puede ser expresada como un conjunto de normas y símbolos que pueden ser unidos en base a unos ciertos criterios que pueden formalizarse. Chomsky sostenía que una lengua es “un conjunto de frases que tienen una longitud determinada y que han sido formadas a base de un conjunto finito de elementos”. Este enfoque resultaría enormemente interesante a todos aquellos interesados en construir sistemas capaces de comprender y generar lenguaje natural. 

De esta forma, podemos, al menos teóricamente, desarrollar un programa informático que genere oraciones gramaticalmente correctas, así como un programa que compruebe que determinada oración en gramaticalmente correcta. 

En la siguiente imagen podemos observar el ejemplo de un análisis sintáctico de una oración sencilla. 



11 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Sin embargo, ¿comprende el lenguaje un algoritmo capaz de generar oraciones aleatorias en base a una gramática? Según el ensayo de Chomsky, este tipo de algoritmos podría generar una frase como “Los colores huelen a espacio vectorial”. Esta frase es totalmente correcta desde el punto de vista gramatical, pero carece de todo sentido. 

Es por ello que, si la sintaxis es independiente de la semántica, ¿qué rol juega la semántica en la comprensión del lenguaje? Chomsky no construyó teorías semánticas independientes, sencillamente se limitó a sostener que es posible analizar formalmente una gramática desde la perspectiva sintáctica sin que la semántica afecte a la calidad de la teoría. Serían necesarias más investigaciones y numerosos ensayos para tratar de acercarse a la problemática de la semántica, notablemente más compleja que la de la sintaxis, como veremos a lo largo de la asignatura. 

El trabajo de Chomsky acerca de las gramáticas no es solo relevante para el campo del NLP ya que contribuyó también enormemente al desarrollo de los primeros lenguajes de programación y a los procesadores de dichos lenguajes que los convertían a código en ensamblador y posteriormente en código máquina. Sin embargo, estas implicaciones de las gramáticas de Chomsky quedan fuera del alcance de esta asignatura, si bien son esenciales para el desarrollo de los lenguajes de programación tal y como los conocemos en la actualidad. 

A partir de esta publicación el campo del NLP se vio dividido en dos corrientes principales: los simbólicos y los estocásticos. Aquellos que pertenecían al primer grupo trataban de generar algoritmos única y exclusivamente basados en la producción de oraciones en base a gramáticas formales y reglas previamente definidas. Este fue el enfoque que se empleó en el _experimento de Georgetown_ en 1954 cuando un sistema informático fue capaz de traducir por primera vez más de sesenta oraciones en ruso al inglés. Esta traducción automática, que sería el primer objetivo de los investigadores de NLP por motivos bélicos, estaba basada en reglas que marcaban la correspondencia entre determinadas estructuras sintácticas en ruso y sus correspondientes en inglés, para posteriormente traducir palabra por palabra el contenido. Surgió en esta época también ELIZA (1964), del que hablamos en profundidad en la primera asignatura de este máster, que estaba basado en el empleo de las frases de entrada para, modificando su estructura sintáctica basada en transformaciones gramaticales formales, responder a un humano que interactuaba con el sistema. En este mismo año se crea en Estados Unidos el ALPAC ( _Automatic Language Processing Advisory Commitee_ ), que tenía como misión evaluar los avances y promesas de la disciplina del NLP. 

Tan solo dos años después de la creación del ALPAC, se dio el objetivo de traducción automática por imposible y se recortó al máximo la inversión en Procesamiento del Lenguaje Natural ya que en ningún momento se había obtenido un sistema eficiente y eficaz para la traducción automática, ni tampoco un sistema solvente para mantener una conversación con un humano. La disciplina del NLP se consideró prácticamente extinta en este momento, aunque hubo investigadores que continuaron con su labor a pesar de la falta extrema de fondos. 

12 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Estos pocos investigadores desarrollaron en 1970 una gran variedad de ontologías conceptuales, que trataban de estructurar desde un punto de vista formal la definición, propiedades y relaciones entre los conceptos y entidades de un determinado subconjunto de una lengua. Este esfuerzo trataba de dar respuesta a la necesidad de comprensión del contenido de las oraciones, más allá de su corrección sintáctica. Algunos ejemplos de ontologías desarrolladas durante estos años son MARGIE (1975), TaleSpin (1976), SAM (1978) o Politics (1979). Cada una de ellas trataba de recopilar todas las entidades posibles y las relaciones entre ellas dentro de un pequeño ámbito de la realidad. Es intuitivo imaginar que esta tarea es realmente compleja, ya que es prácticamente imposible recopilar todas las entidades y relaciones por muy pequeña que sea la realidad que desea modelarse. No obstante, esta era la mejor opción de los todavía simbólicos investigadores de NLP que perseguían definir todo el mundo lingüístico a base de reglas formales. Esta opción implicaba que toda oración era segmentada en palabras y signos de puntuación. Cada una de las palabras era asociada con un concepto de la ontología, y así se podían conocer sus relaciones con otros conceptos y entidades. Sin embargo, esta aproximación mostraba muchas limitaciones y debilidades ya que requería que los desarrolladores de la ontología hubieran tenido en cuenta todas las posibles entidades y relaciones entre las mismas en un universo. Por muy acotado que fuera un universo, siempre podía haber conceptos nuevos, relaciones no tenidas en cuenta o palabras sin una correspondencia con los elementos de la ontología. Por tanto, aunque como ejercicio teórico fuera un gran avance en el intento de formalizar el conocimiento humano y la semántica dentro del lenguaje natural, las ontologías cayeron rápidamente en desuso debido a su poca flexibilidad, a su dependencia de las decisiones de desarrollo y a su dificultad para representar realidades complejas y universos más amplios. 

En la siguiente figura podemos observar un ejemplo de ontología realmente reducida, y que a pesar de ello tiene una enorme cantidad de entidades que no han sido incluidas, así como de relaciones entre ellas, lo que haría a efectos prácticos de esta ontología un ejercicio estéril para la implantación de un modelo real de NLP para cualquier caso de uso. 



13 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Durante los primeros años de la década de 1980, se continuó con el esfuerzo por parte de los investigadores de tratar de modelar la realidad en base a un lenguaje formal. A pesar de que la tarea cada vez se antojara más compleja y le meta se vislumbrara más lejana, a principios de esta década hubo ciertos avances dentro del NLP simbólico, que sin embargo vivía sus últimos años de vigencia. 

Uno de los más sonados fue la creación del algoritmo de Lesk en 1986. Este algoritmo trataba de mejorar la comprensión de los primitivos sistemas de NLP del significado de las oraciones (semántica) gracias al contexto. En concreto, este algoritmo trataba de encontrar la desambiguación entre dos palabras. Este algoritmo se basa en que una palabra tendrá un significado u otro en función de las palabras que la rodean, lo cual a priori parece intuitivo. Sin embargo, la implementación fue relativamente ruda, ya que se trataba de encontrar en las distintas acepciones de una palabra en el diccionario apariciones textuales de otras palabras que la rodeaban. De esta forma, si ninguna de las palabras “vecinas” de la palabra ambigua aparecía en el diccionario, el algoritmo fallaba. No obstante, variaciones y mejoras de este algoritmo han llegado hasta nuestros días en algoritmos como WordNet. 

Otro artículo con gran repercusión fue el titulado _Rhetorical structure theory_ , publicado en 1988, con la intención de mejorar la comprensión de la relación que guardan distintas partes de un texto entre sí. En los años venideros se emplearía esta teoría para los primeros resúmenes automáticos de textos, antes de la llegada de las redes neuronales a la disciplina del NLP. Para analizar la jerarquía de las distintas oraciones dentro de un texto, RST genera un árbol en el texto en el que trata de estimar qué oración está subordinada a qué otra, para así encontrar los contenidos principales y aquellos que son secundarios, o la relación entre la condición y el efecto, o la causa y la consecuencia. 

A pesar de estos avances, la segunda corriente de NLP se impondría a partir de el final de esta década: el NLP estadístico. Los modelos estadísticos de NLP tenían una orientación completamente distinta a los modelos basados en reglas escritas a mano de los algoritmos simbólicos. Por el contrario, se comenzó a introducir la estadística en forma de _machine learning_ para procesar el lenguaje. Gracias al ya conocido aumento de la capacidad de cómputo de los computadores en torno a esta época y a un progresivo cambio de enfoque comenzaron a surgir los primeros modelos que anticiparían el NLP actual. 

En este momento se retomó el objetivo de la traducción automática, ya desde una perspectiva estadística. Para generar estos modelos se empleó información de documentos oficiales de países con más de una lengua oficial en la que todas las frases estaban relacionadas entre sí. 

14 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

## **2. Preprocesamiento de textos: el primer paso en el NLP** 

_“Un regex es una expresión que puede ser verdadera o falsa. Se emplean para buscar patrones en el texto, y así identificar determinadas palabras. No solo se emplean en el mundo del Procesamiento del Lenguaje Natural, ya que tienen numerosas aplicaciones en un gran número de casos de uso de desarrollo informático.”_ 

### **2.1. Las expresiones regulares y la segmentación de palabras y frases** 

Los primeros agentes conversacionales que hemos visto en la asignatura de Introducción a la Inteligencia Artificial, así como la inmensa mayoría de los primeros procesadores de lenguajes estaban basados en una herramienta informática clave para el NLP denominada “expresiones regulares”, o _regex_ por su concatenación en inglés. 

Un _regex_ es una expresión que puede ser verdadera o falsa. Se emplean para buscar patrones en el texto, y así identificar determinadas palabras. No solo se emplean en el mundo del Procesamiento del Lenguaje Natural, ya que tienen numerosas aplicaciones en un gran número de casos de uso de desarrollo informático. 

Un _regex_ es, en definitiva, una condición acerca de una palabra. Podemos, por ejemplo, querer buscar palabras que contengan la letra ‘b’. Para ello, construiremos un _regex_ que compruebe esta condición. Acto seguido, ejecutaremos este _regex_ a lo largo de un corpus y observaremos los resultados. 

El caso más sencillo de un _regex_ es la búsqueda de una palabra completa. La expresión regular /perro/ busca todas las ocurrencias de la palabra “perro” en un texto. Teniendo en cuenta que las expresiones regulares tienen en cuenta las mayúsculas y las minúsculas (case sensitive, en inglés), la palabra “Perro” no cumplirá la condición de la expresión regular /perro/. 

Para tener en cuenta ambas palabras, podemos incorporar en la expresión regular el operador [], que permite que un carácter tome distintos valores. Si construimos por tanto la expresión regular / **[** pP **]** erro/, cualquiera de las dos palabras anteriores sería válida para este _regex_ . 

En ocasiones queremos indicar intervalos de letras o números. Para ello podemos usar el operador -, por ejemplo / **[** 1-5 **]** / buscará cualquier dígito que esté entre el 1 y el 5. 

15 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

También puede que queramos buscar todas las ocurrencias de perro tanto en singular como en plural. En este caso, si generamos un regex que sea / **[** pP **]** erros/ solo buscaremos la aparición en plural. Necesitamos un operador que nos permita poner caracteres opcionales. Este operador es “?”. La expresión regular / **[** pP **]** erros **?** / indica que buscamos palabras que empiecen por p o por P seguidas de “erro” y con un carácter opcional que es “s”. Es decir, que coincidirá con perro, Perro, perros y Perros. 

Uno de los usos más extendidos de las expresiones regulares es la búsqueda de archivos. Imaginemos que tenemos una carpeta con imágenes nombradas de la siguiente forma: _lugar_fecha_autor._ Podríamos encontrar imágenes como las que se muestran en la siguiente lista a modo de ejemplo: 

- Argentina_Mayo22_Damián 

- Perú_Abr21_Rosa 

- Argentina_Feb20_Sara 

- Italia_Oct19_Pedro 

- … 

Si quisiéramos buscar todas las fotografías realizadas por Rosa en Perú conoceríamos el comienzo y el final de nuestro regex, pero no el contenido intermedio. Para indicar “cualquier número de caracteres intermedios” se usa el operador “.”. En este caso, para resolver la búsqueda construiríamos una expresión regular de la forma /Perú.Rosa/ 

¿Y si queremos las fotografías que ha realizado Rosa tanto en Perú como en Francia independientemente de la fecha? Seguimos necesitando más operadores. En este caso, un operador de alternativa, representado por el operador “|”. /perro **|** gato/ indica que el regex buscará tanto la palabra perro como la palabra gato. 

En el caso de las fotografías necesitamos indicar en el regex que solo dudamos de la primera palabra, para lo que necesitaremos paréntesis. Si construimos la expresión regular correctamente tendremos que / **(** Perú **|** Francia **)** .Rosa/ devuelve todas las palabras que empiezan por Perú o por Francia, que después tienen un número indeterminado de caracteres, y que terminan con Rosa. 

Además, podemos indicar a las expresiones regulares si queremos buscar palabras al principio de una línea “^”, al final de una línea “$” o como palabras aisladas “/b”. De esta forma, podemos recopilar los operadores básicos de las expresiones regulares que hemos estudiado hasta este momento en la siguiente tabla. 

16 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

|**Operador**|**Función**|
|---|---|
|[]|/**[**vV**]**aca/ encontrará Vaca y vaca|
|-|/Brooklyn9**[**7-9**]**/ encontrará Brooklyn97, Brooklyn 98 y Brooklyn99|
|?|/h**?**ola/ encontrará tanto hola como ola|
|.|/ca.lla/ encontrará tanto caballa como canalla como casilla|
|||/uno**|**dos/ encontrará tanto uno como dos|
|^|Principio de línea|
|$|Fin de línea|
|/b|Palabra aislada|



### **2.2. Qué es una palabra** 

Con las expresiones regulares hemos descubierto la posibilidad de realizar determinadas búsquedas más o menos complejas en un texto o un conjunto de ellos para extraer información relevante para nuestros sistemas. 

Todos los idiomas están estructurados en unidades básicas de significado que conocemos como palabras. El texto escrito de forma premeditada suele contener únicamente palabras y signos de puntuación. Por ello, podríamos sentirnos tentados de definir una palabra como todo conjunto de caracteres rodeado por espacios o signos de puntación. 

Sin embargo, cuando trabajemos con transcripciones de conversaciones humanas, el mayor exponente del lenguaje natural al que podemos enfrentarnos, nos encontraremos con situaciones como la siguiente. 

“Ehhhh bueno, yo vivo en-en Sidney y esto… no-no me llega a convencer la cantidad de gente que hay .” 

¿Son “eeeh”, el primer “en”, “esto…” y  el primer “no”, palabras? ¿aportan contenido y significado a la oración? Siempre dependerá del objetivo de nuestro sistema de NLP, pero cabe pensar que habrá situaciones en las que haya que filtrar este tipo de palabras para trabajar con determinadas entradas. Por otro lado, ¿consideramos la misma palabra si esta comienza con mayúscula? ¿y si está en plural? ¿Son la misma palabra “gato”, “Gato”, “gatos” y “Gatos” o son palabras totalmente distintas? 

17 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Habitualmente en la disciplina del Procesamiento del Lenguaje Natural distinguimos dos conceptos básicos a la hora de analizar palabras en un corpus, que son: 

- Tipos ( _types_ ). El número de tipos de palabras es la cantidad de palabras diferentes que podemos encontrar en un texto. 

- Tokens ( _tokens_ ). Los tokens son el número total de palabras que encontramos en un texto. 

Hay numerosas palabras que se repiten en un idioma como son los artículos o las preposiciones. Esto implica que en todo texto siempre habrá notablemente más tokens (unidades individuales de palabras) que tipos (palabras distintas). La decisión de qué es una palabra y qué no lo es dependerá del caso de uso del sistema que estemos desarrollando, pero es una decisión que deberemos tomar en las primeras etapas de diseño de nuestros sistemas de NLP para poder avanzar con seguridad hacia las siguientes. 

La tokenización consiste, por tanto, en encontrar todas las palabras – es decir que cumplan con **nuestra** definición de palabras – y el análisis de tipos de encontrar el conjunto de palabras únicas que se emplean en un texto. Cada uno de estos resultados será una entrada interesante a según que modelos de NLP, como podremos observar en secciones futuras de esta asignatura. 

### **2.3. Normalización del texto** 

Para poder procesar cualquier texto con un sistema de NLP necesitaremos previamente ejecutar un proceso sobre el mismo que se conoce como normalización del texto o _Text Normalization_ . Este proceso nos ayudará a estandarizar el contenido de nuestro texto de tal forma que facilitemos el proceso posterior de cualquier algoritmo que deseemos ejecutar para cualquier caso de uso. Esta estandarización persigue encontrar los distintos componentes de nuestro texto y aplicarles una serie de procesos que nos permitan obtener una salida homogénea. En definitiva, es un preprocesado, igual que el que realizamos a las imágenes en visión artificial. Si bien en la visión artificial manipulamos elementos como el contraste, el _gamma_ , filtramos la imagen y eliminamos ruido, en el caso del lenguaje trataremos de limpiar el contenido – por ejemplo, extrayendo las palabras originales de formas acortadas de las palabras – para un funcionamiento óptimo de los algoritmos posteriores. 

Este proceso implica tres subprocesos esenciales que deben realizarse por orden, y que vamos a analizar por separado. 

1. Tokenización 

2. Normalización del formato de las palabras 

3. Segmentación de frases y oraciones 

18 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **2.3.1. Tokenización** 

La **tokenización es el proceso de encontrar los elementos básicos individuales de un texto, habitualmente las palabras** . Buscaremos todas y cada una de las palabras para comenzar con nuestra normalización. 

Para realizar la **tokenización** podríamos optar por métodos realmente básicos. Intuitivamente podríamos pensar que, si empleamos los espacios y los signos de puntuación como elementos separadores, seríamos capaces de extraer todas las palabras de un texto. Por ejemplo, para la frase “Ninguna ciencia, en cuanto a ciencia, engaña; el engaño está en quien no la sabe” si usáramos el criterio de los signos de puntuación, obtendríamos los siguientes tokens: 



La salida de la práctica mayoría de los algoritmos de tokenización es similar a la que hemos mostrado en este ejemplo. Cada token se indica en una línea distinta. Sin embargo, esto complica la lectura de la salida y ocupa demasiado espacio en el manual de la asignatura, por lo que emplearemos la convención del símbolo <⌴> para denotar los espacios entre tokens sin ocupar una cantidad de espacio tan elevada.  Además, identificaremos cada token unitario entre los símbolos <>. Por tanto, la tokenización de un texto con N tokens tendrá la forma < `token1` >⌴< `token2` >…< `tokenN` > 

Esto significa que para el ejemplo anterior tenemos 15 tokens. Es importante notar también que tenemos un total de 13 tipos (recordemos, palabras distintas que aparecen a lo largo del texto). Parece que la tokenización ha surtido efecto. No obstante, si queremos tokenizar la frase “El día 20/07/1969 el Apolo 11 llegó a la Luna a las 20:17, con N. Amstrong de capitán”, nuestro método empleado hasta el momento devolvería la siguiente división de tokens: 

19 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



Nuestro texto no ha sido correctamente tokenizado. La fecha, la hora y el nombre compuesto han sido divididos en distintos tokens, dificultando enormemente el trabajo futuro de un modelo de semántica que trate de comprender esta frase. Otros ejemplos de tokens que no podrían funcionar con una aproximación tan básica como la separación por espacios y signos de puntuación son las direcciones de recursos en internet o URLS (https:// <u>nytimes.com devolvería tres tokens) o las direcciones IPv4 o IPv6, por ejemplo.</u> 

Para hacer las cosas más complicadas todavía para nuestro modelo simple de tokenización, hay lenguas como el inglés o el francés en el que se producen acortamientos de determinados conjuntos de palabras mediante el uso de apóstrofes. Construcciones como “You’re young” o “J’aime le gâteau” requieren de la capacidad de distinguir dos tokens donde aparentemente solo hay uno, infiriendo el contenido de una palabra que ha sido acortada en el proceso. 



o, en el caso de la oración en francés: 



Veremos diferentes aproximaciones para solucionar este problema dentro de la categoría del objetivo del NLP conocido como Named Entity Recognition (NER) en el que se trata de reconocer como unidad diversas fechas, horas, nombres propios organizaciones… Que nos ayudarán con este tipo de problemáticas desde una perspectiva más avanzada. Será en la Unidad relativa al NLP con Deep Learning. 

No obstante, y por ahora, es suficiente con que comprendamos estas limitaciones a las que se enfrenta una lógica formal que persigue tokenizar palabras en cualquier idioma, como hemos podido comprobar a lo largo de los distintos ejemplos. 

Uno de los algoritmos de tokenización más extendidos en la actualidad se conoce como **Penn Treebank** , y es el que vamos a poner a prueba en nuestro siguiente ejemplo. Los algoritmos de tokenización son el primer elemento que se ejecuta en un proceso de NLP y por tanto deben ser tanto precisos como rápidos, lo cual supone un verdadero reto para sus diseñadores y desarrolladores. Es por estos motivos que la inmensa mayoría de los algoritmos tokenizadores están basados en expresiones regulares como las que hemos analizado en la sección anterior, que tratan de identificar diferentes formatos de palabra (siglas, acrónimos, fechas, horas, coordenadas, direcciones, URLS...) gracias a la ejecución de diversos _regex_ deterministas. 

20 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Esto implica que los algoritmos de tokenización forman parte de la programación estructurada clásica, siendo simbólicos y no estadísticos por motivos de eficiencia. Si bien hay algoritmos basados en _machine learning_ para tokenizar textos, vamos a centrarnos en los más usados a día de hoy, que se basan en expresiones regulares para segmentar todas las palabras de un texto. 

**Para ejecutar los ejemplos de esta asignatura vamos a emplear la misma herramienta que usamos durante la asignatura de Visión Artificial: Google Colab. Para recordar cómo poner en marcha un entorno de Google Colab, recomendamos acudir al manual de Visión Artificial.** 

#### **Ejemplo de tokenización** 

Para este ejemplo vamos a emplear por primera vez una librería de NLP. En este caso, usaremos una de las librerías más extendidas en la actualidad para el tratamiento y procesado automático de textos, que es NLTK, de Python. 

NLTK es una librería que, además de numerosos métodos de NLP que probaremos a lo largo de la asignatura, nos da acceso a grandes corpus de texto para poder ejecutar diversos métodos sobre ello. Esto nos permite no tener que descargar obras literarias o entrevistas para probar nuestros ejemplos. Sencillamente descargaremos uno de los 50 recursos que ofrece esta librería, y veremos el funcionamiento de la misma en tiempo real. 

En estos primeros ejemplos emplearemos pequeños textos en español, para poder analizar desde el conocimiento de una lengua materna los retos a los que se enfrentan los algoritmos actuales de NLP. Sin embargo, a medida que vayamos necesitando mayores cantidades de texto, emplearemos en ocasiones los recursos de NLTK, que se encuentran en lengua inglesa. 

En este primer ejemplo vamos a emplear el algoritmo de tokenización”Treebank” para tratar de segmentar las palabras de una frase corta en español. 

Para hacerlo, vamos a crear un nuevo cuaderno de Google Colab, tal y como lo hicimos durante la asignatura de Visión Artificial. 

En la primera celda introduciremos el siguiente fragmento de código 

21 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



El resultado de la ejecución de esta primera celda deberá ser el siguiente: 



Como podemos ver, el método tokenize nos ha devuelto una lista de tokens, que no son más que objetos del tipo string en Python. Los signos de puntuación han sido almacenados como tokens, pero es relevante notar que la hora no ha sido alterada, ya que este método de tokenización es capaz de reconocer estructuras como fechas y horas, a diferencia de nuestro método básico del principio de esta sección. 

Uno de los problemas que presenta el español frente a otros idiomas respecto a la tokenización es que cuenta con signos de puntuación de apertura. Tanto las interrogaciones como las exclamaciones en español cuentan con un primer signo que no existe en la gran mayoría de idiomas occidentales. Para comprender las implicaciones de esto, vamos a hacer una segunda prueba, sustituyendo nuestra variable “frase” por la siguiente “¿Qué hora es? ¡Ya se ha hecho de noche!”, y ejecutando la misma celda de nuevo. Podemos ver este cambio en la siguiente imagen: 



22 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Vemos que nuestro algoritmo de tokenización ahora ha cometido errores. Tanto el símbolo “¿” como el símbolo “¡” han sido incluidos en el token de la palabra inmediatamente después. Es por esto que en español en ocasiones hay que usar otros algoritmos de tokenización, o hacer una combinación de algoritmos. 

Por ejemplo, NLTK ofrece un algoritmo tokenizador más sencillo llamado WordPunct que sencillamente separa las palabras por espacios y signos de puntuación. Ya hemos comentado las limitaciones de esta aproximación a la tokenización, pero vamos a probarla de primera mano. 

Crearemos una segunda celda de código, y en este caso importaremos el tokenizador WordPunct. Además, usaremos la frase “¿Qué hora es? ¡Ya se ha hecho de noche! Son las 21:43” Para poner a prueba las mencionadas limitaciones y ventajas. 

Introduciremos el siguiente código en la segunda celda de nuestro cuaderno 



El resultado será el siguiente 



Como vemos, en esta ocasión hemos sido capaces de tokenizar por separado los símbolos “¿” y “¡”, pero sin embargo hemos separado las horas de los minutos por culpa del símbolo “:”. 

Gracias a este primer ejemplo hemos podido comprobar cómo los tokenizadores tienen que enfrentarse a una gran variedad de situaciones, que en ocasiones superan las capacidades de las expresiones regulares que rigen su funcionamiento. En concreto, el español es un idioma complejo para los tokenizadores, y requiere de un mayor esfuerzo que otros como pueden ser el inglés y el francés. 

23 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

La tokenización se enfrenta a un último reto que tendremos que tratar de solucionar, y son las palabras desconocidas. Los modelos de NLP basados en aprendizaje profundo y aprendizaje automático, que son la gran mayoría, aprender a procesar el texto a través de un conjunto de entrenamiento etiquetado, y posteriormente se aplican a otros ejemplos del mundo real en su aplicación. 

Esto implica que estos modelos pueden no llegar a conocer todas las palabras de un idioma, por lo que debemos encontrar una forma de detectar palabras que nuestros modelos no hayan procesado previamente y tokenizarlas. 

Para solucionar este problema los tokenizadores modernos emplean un concepto denominado _subwords_ (subpalabras) que permiten detectar palabras que no han sido nunca procesadas. Por ejemplo, si nuestro corpus de entrenamiento cuenta con la palabra “acuático” pero no “subacuático”, necesitamos una forma de detectar subacuático como una palabra con significado por sí misma. Para hacer esto, los tokenizadores basados en subpalabras primero extraen un vocabulario de un corpus de entrenamiento sin más información acerca del vocabulario de un idioma. 

Uno de los algoritmos más conocidos se denomina byte-pair encoding (BPE), y surgió en 2016. Este algoritmo primero segmenta todos y cada uno de los caracteres del texto y analiza aquellos que aparecen uno junto al otro la mayor parte de las veces. Por ejemplo, “ar”, “er” o “ir”. Una vez detectadas estas estructuras, sustituye estos dos tokens por el token construido por el conjunto de dos caracteres. Este proceso se repite recursivamente hasta alcanzar un máximo llamado k, que es un parámetro del algoritmo. De esta forma el vocabulario de nuestro tokenizador será un conjunto de todos los caracteres más tantos conjuntos de caracteres como permita el parámetro _k_ . 

El funcionamiento de este algoritmo es más sencillo si se observa en un **ejemplo** como el siguiente 

Pongamos que tenemos el siguiente corpus de texto 

```
escribir, estructura, partir, partición, dormir
```

El algoritmo de BPE tomaría como vocabulario todos los caracteres que aparecen en el corpus 

```
e, s, c, r, i, b, t, u, a, p, o, d, m
```

Ahora, buscará el conjunto de caracteres que más se repite a lo largo del corpus, que es ir_ (porque es el final de la palabra). 

El vocabulario entonces pasará a ser 

```
e, s, c, r, i, b, t, u, a, p, o, d, m, ir_
```

24 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

El siguiente conjunto de caracteres que más aparece en conjunto es <es>, por lo que el tokenizador lo añadirá a su vocabulario, siendo este 

```
e, s, c, r, i, b, t, u, a, p, o, d, m, ir_, _es
```

Y quedando por tanto nuestro corpus de la siguiente manera 

<_es>⌴<c>⌴<r>⌴<i>⌴<b>⌴<ir_>⌴<,>⌴<_es>⌴<t>⌴<r>⌴<u>⌴<c>⌴ <t>⌴<u>⌴<r>⌴<a>⌴<,>⌴<p>⌴<a>⌴<r>⌴<t>⌴<ir_>⌴<,>⌴<p>⌴<a >⌴<r>⌴<t>⌴<i>⌴<c>⌴<i>⌴<ó>⌴<n>⌴<,>⌴<d>⌴<o>⌴<r>⌴<m>⌴ <ir_> 

Si siguiéramos ejecutando el algoritmo, veríamos que el conjunto “part” aparece también dos veces en el corpus, por lo que lo añadiríamos al vocabulario 

```
e, s, c, r, i, b, t, u, a, p, o, d, m, ir_, _es, _part
```

Y nuestro corpus sería, tras la tokenización: 

<_es>⌴<c>⌴<r>⌴<i>⌴<b>⌴<ir_>⌴<,>⌴<_es>⌴<t>⌴<r>⌴<u>⌴<c>⌴ <t>⌴<u>⌴<r>⌴<a>⌴<,>⌴<_part><ir_>⌴<,>⌴<_part>⌴<i>⌴<c>⌴<i> ⌴<ó>⌴<n>⌴<,>⌴<d>⌴<o>⌴<r>⌴<m>⌴<ir_> 

Este proceso continuaría hasta llegar a la iteración definida por el parámetro k. En este momento el tokenizador considera que el vocabulario ha sido completado, y será el que aplique en la tokenización de futuros corpus de test. 

En un corpus tan escaso como el que hemos usado en este ejemplo el vocabulario que puede resultar de este proceso es tan escaso que no funcionará en otros textos. Sin embargo, este tipo de modelos se entrenan con grandes cantidades de texto por lo que su salida más habitual es un vocabulario formado por tantas palabras como existen en el texto junto a una serie de subpalabras (que suelen coincidir con prefijos, sufijos, lexemas y terminaciones verbales). Esto ayuda a detectar nuevas palabras compuestas, formas verbales, variaciones de palabras conocidas… 

### **2.3.2. Normalización del formato de las palabras** 

Como hemos visto, el primer proceso para convertir un cuerpo de texto en un conjunto de datos procesables es convertir los caracteres que lo componen en una serie de tokens que formen parte de un vocabulario definido, habitualmente construido en base a un proceso iterativo sobre el texto a tratar. 

Estos tokens tratan de separar palabras de signos de puntuación, para posteriormente construir frases y analizar la sintaxis y la semántica de las mismas. 

25 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Uno de los retos que encuentra el NLP a la hora de procesar estos aspectos del texto es la normalización. En el lenguaje natural nos encontramos con múltiples formas de expresar el mismo concepto o palabra, y es imprescindible que nuestros sistemas conozcan todas estas formas de expresar un concepto, y que las agrupen bajo un mismo token. Por ejemplo, podemos haber encontrado en un texto las palabras “monitor”, “Monitor” y “MONITOR”. Nuestro tokenizador habrá generado un token para cada una de ellas que, hasta el momento, apuntan a distintas palabras de nuestro vocabulario. 

Para normalizar estas palabras se emplea un método de normalización basado en mayúsculas y minúsculas denominado **_Case folding_** . Este método persigue básicamente convertir todas las letras de nuestros textos en minúsculas, de tal forma que todos los tokens con variaciones de mayúsculas y minúsculas apunten al mismo concepto de nuestro vocabulario (reduciendo así los tipos que tenemos en nuestro vocabulario). 

Pero esto no es suficiente si queremos reducir el contenido de nuestro texto a su mínima expresión y por tanto el número de tipos de nuestro vocabulario. Para hacer esto emplearemos métodos como la radicalización o **_stemming_** y la lematización o **_lemmatization_** . 

A lo largo de un texto extenso, es probable que encontremos numerosas derivaciones de una misma palabra como pueden ser “democracia”, “democrático”, “demócrata” o “democráticamente”. En función del caso de uso al que estemos aplicando el Procesamiento del Lenguaje Natural, es posible que deseemos unificar todos estos tokens bajo un mismo concepto, que podría ser “democracia”. 

Para hacer esto podemos recurrir en primera instancia al _stemming_ . Este es el método más simple de normalización de palabras basadas en su significado. Este proceso se basa en eliminar las terminaciones derivativas más comunes de las palabras para tratar de obtener únicamente la raíz de las mismas. Esto implica que, obviamente, el _stemming_ es un método heurístico que depende del conocimiento de un idioma concreto y que solo funcionará para este idioma. Dependerá del desarrollador del método decidir qué terminaciones se tienen en cuenta en el método para así aplicarlo a los tokens una vez estos han sido encontrados. 

Uno de los algoritmos de _stemming_ más conocido y empleado en la lengua inglesa es el algoritmo de Porter (1980). Este algoritmo se aplica a las palabras con un determinado número de sílabas mayor que un parámetro m dado. Para todas estas palabras se aplican una serie de reglas que tratan de radicalizar la palabra. Dado que estos algoritmos son heurísticos, están compuestos por una gran cantidad de reglas de aplicación directa, por lo que no sería valioso exponer todas en este manual. Sin embargo, a efectos de ejemplo, podemos analizar algunas reglas y ejemplos de su aplicación, de tal forma que comprendamos de primera mano la aplicación de un algoritmo de _stemming_ . 

26 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

ATIONAL  ATE : conversational  conversate 

SSES  SS: classes  class IES  I: homies  homi 

ING  doing  do 

Como podemos ver, el algoritmo de Porter aplica una serie de reglas predefinidas a todos y cada uno de los tokens, tratando de eliminar las distintas derivaciones de las palabras para quedarse con la forma más cercana a la raíz posible. Estos métodos, si bien son sencillos y muy poco costosos computacionalmente, son métodos con altas tasas de fallo ya que es complejo definir una lista de reglas que permitan que de cualquier variación de cualquier palabra de un idioma consigamos llegar a la raíz de la misma. 

Vamos a probar en Python dos stemmers distintos. Por un lado, el _stemmer_ de Porter que ya hemos analizado, y por otro lado el _stemmer_ “Snowball” a un texto en español. Este _stemmer_ es una variación del de Porter que soporta un gran número de idiomas, entre otros árabe, alemán, francés, finlandés, ruso, sueco… Y por suerte el español se encuentra entre ellos. 

#### **Ejemplo de stemmers** 

Crearemos un nuevo cuaderno de Google Collab y en la primera celda incorporaremos el siguiente código 



27 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Como podemos ver, hemos incluido una serie de palabras en inglés que todas están derivadas de la raíz “program” para poner a prueba el _stemmer_ de Porter. El resultado debería ser similar al siguiente, en el que podemos comprobar que el algoritmo de Porter ha logrado dar con la raíz exacta de cada una de las palabras de la lista. Podemos imaginar las diversas reglas que han sido aplicadas en este caso tras una detección de ciertos conjuntos de caracteres por medio de un _regex_ , como pueden ser ING  o ER  que son terminaciones que en inglés denotan un gerundio en el primer caso y una profesión en el segundo. El conjunto de reglas que hay que desarrollar para obtener un stemmer completo para una lengua hacen que estos estén en constante cambio y crecimiento, generando nuevos _regexi_ y tratando de encontrar formas más óptimas para encontrar determinadas cadenas de caracteres sin generar solapes que puedan poner en compromiso la robustez y flexibilidad del algoritmo. 

Observamos en la siguiente imagen el resultado del procesado. 



Probemos ahora el mismo proceso, pero con palabras en español de tal forma que comprobemos la adecuación de las reglas lógicas de Snowball para nuestro idioma. Para ello, creamos una lista de palabras en español relacionadas con la raíz “programa” y observamos el resultado de Snowball. 



28 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Recordemos que estos algoritmos funcionan en base a reglas lógicas. Por tanto, para que Snowball funcione con nuestras palabras tendrá que tener incluidas reglas como 

S  

ADOR  

AR  

ACIÓN  

ES  

Y ejecutarlas iterativamente sobre todos los tokens que le hemos pasado. En efecto, si ejecutamos la segunda celda veremos que el resultado es el siguiente, y que por tanto hemos conseguido **normalizar todos los tokens** para permitir un Procesado del Lenguaje Natural unificado en siguientes fases de nuestro caso de uso. 



La aproximación de los _stemmers_ funciona en el caso de que los tokens compartan la misma raíz y **esta esté presente en la palabra** . Non son más que métodos de recorte, que buscan por medio de expresiones regulares una serie de conjuntos de caracteres y realizan sustituciones anidadas. Existe una gran limitación para esta aproximación, y podemos comprenderla fácilmente analizando el ejemplo de las palabras “fui”, “irán” y “vamos”. Estas tres palabras son formas conjugadas del verbo “ir”, en diversas personas y tiempos. Un _stemmer_ solo sería capaz de detectar que irán es una forma derivada de la raíz “ir”, pero no podría hacer lo mismo con los otros dos ejemplos ya que la raíz no existe de forma explícita entre los caracteres de la palabra. 

Para tratar de dar solución, aunque sea de forma parcial, a este problema, surgen los algoritmos basados en la lematización o _lemmatization_ . Es un proceso más complejo que el _stemming_ ya que hace un análisis real de los morfemas que componen cada token, y trata de ir más allá que las meras reglas heurísticas que ya hemos visto. 

29 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Un morfema está definido como “La unidad más pequeña de la lengua que tiene significado léxico o gramatical y no puede dividirse en unidades significativas menores.”. Ejemplos de morfemas son los prefijos, los infijos y los sufijos con los que construimos palabras en base a otras. 

El análisis de morfemas llevado a cabo en la lematización trata de descubrir las partes en las que una palabra puede ser dividida que aportan significados a la misma. Por ejemplo, la palabra “submarino” está compuesto por el morfema prefijo “sub” (debajo de), del morfema raíz “mar”, y del morfema sufijo “ino” (perteneciente a). Como podemos comprobar el análisis de morfemas podrá ayudarnos enormemente en futuras fases del NLP en las que estemos interesados en comprender el significado de palabras que no existen en nuestro vocabulario. 

Este análisis es más complejo y costoso computacionalmente que la ejecución de una serie de reglas heurísticas. De hecho, es un proceso que puede ser asimilable al de la tokenización, que podríamos definir como la tokenización de un token, es decir, ser capaz de segmentar en morfemas una palabra que previamente fue segmentada de un texto completo. Para hacer esto, igual que en la tokenización, necesitaremos de un diccionario o vocabulario en el que poder basarnos a la hora de relacionar morfemas con palabras y con familias de palabras. Este proceso no sería viable hacerlo de forma heurística, ya que el número de morfemas de un idioma es prácticamente inabarcable. Para generarlos se emplean grandes bases de datos de textos en un determinado idioma, y un modelo estadístico que, de igual forma que en su momento hemos detectado el vocabulario de tokens a base de encontrar los caracteres que más aparecen juntos, trata de buscar los morfemas más habituales y de hallar las raíces de las palabras. 

NLTK nos ofrece, entre otros, un algoritmo de lematización llamado “WordNetLemmatizer” que funciona para palabras en inglés. Vamos a tratar de ponerlo a prueba para comprender su funcionamiento, y la diferencia con el _stemming_ . 

30 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

#### **Ejemplo lematización** 

En el mismo cuaderno de Google Colab que empleamos en el ejemplo anterior, vamos a crear una tercera celda en la que introduciremos el siguiente código. Vamos a tratar de comprender el resultado de la lematización en tres casos: sustantivo, verbo y adverbio. Los algoritmos lematizadores suelen necesitar conocer la tipología de palabra con la que van a tratar para ejecutar una serie de transformaciones u otras con precisión. 



Veremos como el resultado consiste en la extracción de la raíz original de cada una de estas palabras: 



Este resultado es mucho más completo y autocontenido que el resultado que puede ofrecer un stemmer, ya que los resultados son palabras con sentido (y que por tanto forman parte del vocabulario real de la lengua en la que se está trabajando). 

En definitiva, tras aplicar un algoritmo de tokenización y otro de normalización – bien sea _stemmming o lemmatizer_ – tendremos todos y cada uno de los conceptos diferenciales (habitualmente palabras) de nuestro texto identificados y normalizados. Nos quedará un paso para tener nuestro corpus preparado para la ejecución de un algoritmo de NLP. 

31 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **2.3.3. Segmentación de frases y oraciones** 

Por ahora hemos ejecutado algoritmos de tokenización y de normalización. Ambos tipos de algoritmos nos han ayudado a comenzar a estructurar un texto que, a prioriu para nuestro sistema inteligente estaba únicamente conformado por caracteres. Gracias a la tokenización hemos podido extraer lñas distintas palabras que componen nuestro texto, así como generar un vocabulario en base al mismo. 

Además, mediante los algoritmos de _stemming y lemmatization_ , hemos conseguido que las palabras derivadas de una isma raíz tengan el mismo significado para nuestro algoritmo, siempre que esto sea adecuado en el caso de uso. 

En definitiva, por el momento hemos trabajado a nivel de palabras, e incluso hemos llegado a analizar los diversos morfemas que componen cada una de estas palabras. 

El último paso en nuestro proceso de estandarización y preprocesado de un texto es la segmentación de frases y oraciones. Todos los idiomas se construyen en torno a las palabras y las oraciones. La Real Academia Española define una oración en su acepción gramatical como “Estructura gramatical formada por la unión de un sujeto y un predicado.” Las oraciones pueden ser absolutamente sencillas como “yo como”, o complicadas en el caso de múltiples subordinaciones como “Marcos cayó en la cuenta de que era el mismo día del año que aquel en el que su abuelo descubrió un agujero en la pared de la iglesia”. Si las palabras son la unidad mínima de un lenguaje, las oraciones son las estructuras completas con significado y estructura, por lo que es de vital importancia tener capacidad para identificar todas y cada una de las oraciones de un texto, indicando su principio y su final. 

El objetivo de un algoritmo de _sentence segmentation_ es agrupar todos los tokens hallados en una jerarquía de nivel superior, creando agrupaciones de tokens por cada una de las oraciones detectadas. Como en todos los casos que hemos analizados hasta ahora, este trabajo puede realizarse mediante métodos realmente sencillos que serán rápidos de ejecutar, pero complejos de generalizar, o mediante métodos más complejos de NLP que requerirán una mayor capacidad de cómputo, pero tendrán una mayor robustez y flexibilidad. 

Uno de los segmentadores de oraciones más básicos que podemos construir es un detector de puntos. Cada vez que nos encontremos un token compuesto por un punto <.> agruparemos todos los tokens hasta este en una nueva oración, y crearemos una nueva a partir del token siguiente. Pronto descubriríamos que necesitamos incluir también los signos de cierre de pregunta <?> y de cierre de exclamación <!>, ya que estos son empleados como sustitución de un punto para cerrar una oración. Sin embargo, si solo empleáramos este tipo de segmentación, perderíamos una gran cantidad de información en nuestras oraciones, ya que en el lenguaje natural no se aplican siempre las convenciones exactas de la gramática, y este es un hecho con el que los modelos deben trabajar sin problemas. 

32 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Por ejemplo, los dos textos siguientes tienen el mismo significado, a pesar el cambio en la puntuación. 

- a. “Esto es una frase. Esto es otra frase.” 

- b. “Esto es una frase; esto es otra frase.” 

Si nuestro objetivo posterior al preprocesado es la comprensión del lenguaje, deberíamos ser capaces de normalizar la segmentación de estas dos frases de tal forma que el resultado sea idéntico. Otro ejemplo podría ser el uso de oraciones explicativas dentro de una oración, como en el siguiente ejemplo: 

“Juan Pablo se acercó a la mesa del salón – la mesa era una reliquia familiar que nadie osaba criticar – y desplegó un mapa sobre ella.” 

En este caso, nos encontramos con dos oraciones, una de ella incrustada dentro de la otra. Si tan solo usáramos la lógica de los caracteres, segmentaríamos tres oraciones distintas, mientras que realmente hay solamente dos. 

Esta realidad implica, como en otros tantos casos, que las soluciones basadas en reglas encontrarán numerosos problemas para dar con un conjunto de reglas suficientemente amplio como para poder funcionar con todos los posibles casos que pueden darse en un idioma, sin por ello perder calidad. Es por esto que a medida que la disciplina del Procesamiento del Lenguaje Natural fue creciendo a principios de siglo XXI, surgieron numerosos métodos basados en _machine learning_ que trataron de automatizar el proceso de aprender a segmentar oraciones. En algunos casos nos encontraremos con métodos de aprendizaje supervisado y en otros no supervisado. Recordemos que la diferencia entre estos dos tipos de aprendizaje automático reside en la existencia de etiquetas generadas por un ser humano o no. En el caso del aprendizaje supervisado, un humano debe separar de forma manual todas las oraciones de un texto, para que el modelo de _machine learning_ pueda aprender a segmentar las oraciones. 

Un algoritmo de aprendizaje no supervisado ( _unsupervised learning_ ) tratará de encontrar patrones en el texto y de agrupar los tokens sin ningún tipo de información previa ni de reglas conocidas. 

Sorprendentemente, este último enfoque es el que mejores resultados ha dado a la hora de desarrollar algoritmos de segmentación de oraciones. De hecho, uno de los métodos más empleados en la actualidad para segmentar oraciones es el método conocido como Punkt, publicado en 2006, cuyo artículo tenía por nombre “ _Unsupervised Multilingual Sentence Boundary Detection_ ”. La gran ventaja de este método no supervisado es que puede ser reentrenado para cualquier fragmento de texto, haciendo de este algoritmo uno de los más flexibles dado que siempre tiene la capacidad de adaptarse a cualquier nuevo corpus con el que deseemos trabajar. 

33 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Vamos a ver un ejemplo del funcionamiento del algoritmo de Punkt, que por suerte viene incorporado entre todos los módulos que nos ofrece NLTK, por lo que podremos ver su funcionamiento en tiempo real gracias a un cuaderno de Google Colab. 

#### **Ejemplo de** **_sentence segmentation_** 

Crearemos un nuevo cuaderno de Google Collab para probar la segmentación de oraciones en NLTK . 

En la primera celda del cuaderno introduciremos el siguiente fragmento de código, y lo ejecutaremos 



La salida de la ejecución será similar a la siguiente: 



Si analizamos la salida de nuestro ejemplo veremos que Punkt ha sido capaz de segmentar bien todas las oraciones menos la última, que ha sido unificada con la anterior. 

Para mejorar este comportamiento podríamos buscar un texto en el que esta situación se diera lo suficientemente a menudo como para ser estadísticamente representativa, y podríamos reentrenar el algoritmo. 

34 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Tras ejecutar los tres procesos de preprocesado de un texto para el uso de algoritmos de Procesamiento del Lenguaje, hemos conseguido pasar de un conjunto de caracteres a un vocabulario propio que viene marcado por una serie de tokens, que normalizaremos para evitar múltiples formas de denominar un mismo concepto, y por último agruparemos en oraciones. 

Una vez realizados estos tres procesos, el texto estará listo para aplicar algoritmos de Procesamiento del Lenguaje Natural más avanzados. Es importante notar que habitualmente estos procesos vienen incorporados en muchos de los algoritmos más avanzados de NLP. Sin embargo, es esencial conocer su funcionamiento y el motivo de su existencia, ya que son los cimientos sobre los que construiremos todos los algoritmos que vamos a analizar en esta asignatura. Por muy elaborado que sea un algoritmo de análisis de emociones, si la tokenización y la normalización no tienen la calidad suficiente, sus resultados serán insuficientes y el algoritmo quedará descartado cuando quizá sencillamente había que seleccionar un tokenizador mejor, aplicar lematización, o reentrenar el modelo de segmentación de oraciones antes de desechar por completo un nuevo algoritmo. 

En la próxima unidad analizaremos los primeros pasos que podemos dar una vez un texto está preparado para ser tratado. Estudiaremos cómo podemos usar la distancia entre palabras para desarrollar algoritmos de autocompletado de texto, así como modelos de predicción de palabras para, entre otras cosas, desarrollar sistemas de autocompletado. Categorizaremos palabras para aumentar nuestro conocimiento acerca del contenido de un texto, y estudiaremos métodos ampliamente implantados en la actualidad como son el Bag of Words y los modelos de _Word2Vec_ . 

35 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

## **3. Categorización, autocorrección y autocompletado de texto** 

_“La autocorrección es una aplicación que transforma palabras incorrectamente escritas en la versión correcta de dichas palabras. Lo encontramos a diario en los teclados de muestros dispositivos móviles, de nuestros editores de texto e incluso de nuestros editores de email.”_ 

### **3.1. Autocorrección y algoritmos de estimación de distancia** 

Uno de los casos de uso más sencillos dentro del Procesamiento del Lenguaje Natural y que nos puede ayudar a comprender conceptos y algoritmos complejos de NLP aplicándolos a un caso de uso real y que a día de hoy está presente en prácticamente todos los sistemas de mensajería y edición de textos disponibles: la autocorrección de textos. 

La autocorrección es una aplicación que transforma palabras incorrectamente escritas en la versión correcta de dichas palabras. Lo encontramos a diario en los teclados de muestros dispositivos móviles, de nuestros editores de texto e incluso de nuestros editores de email. El proceso de la autocorrección tiene cuatro pasos principales: 

1. El proceso comienza con la identificación de una palabra que no pertenece al vocabulario estipulado. Para la detección de palabras incorrectamente escritas, podemos aplicar un sencillo algoritmo que busque cada una de las palabras escritas en un vocabulario previamente definido, y en el caso de aquellas palabras que estén fuera, iniciar el proceso. 

2. Una vez detectada una palabra con errores ortográficos, se trata de encontrar las palabras más cercanas dentro del vocabulario conocido. En la siguiente sección analizaremos cómo realizar este proceso. 

3. Una vez identificadas estas palabras cercanas, se sustituye la palabra errónea por cada una de las palabras encontradas a una distancia determinada. 

4. Se calculan las probabilidades de cada una de las palabras en función de contexto de la oración en la que se encontrara la palabra incialmente mal escrita. Finalmente, se sugiere la sustitución de la palabra errónea por la palabra que el algoritmo interpreta que se deseaba escribir en un primer momento, que será aquella que haya obtenido una mayor probabilidad en esta etapa del proceso. 

36 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **3.1.1. Estimación de la distancia entre palabras** 

Para medir la distancia entre dos palabras a la hora de la autocorreción, en NLP se emplea la denominada distancia de edición o _edit distance_ . 

La distancia de edición mide el número de cambios mínimos que deben realizarse sobre una palabra inicial hasta llegar a una palabra final. Por ejemplo, para pasar de la palabra “amarillo” a la palabra “amarilla” hay que realizar un único cambio. Para pasar de la palabra “bruja” a la palabra “oruga” hay que realizar dos cambios. 

Denominaremos ediciones a estos cambios ejecutados sobre una palabra en búsqueda de otra. 

Diferenciaremos entre los siguientes tipos de edición: 

- Inserción ( _insert_ ): Añadir una o varias letras en una palabra. La palabra “cuarto” se convierte en “cuartos” con la inserción de una “s” final. 

- Borrado ( _delete_ ): Eliminar una o varias letras de una palabra. Por ejemplo, la palabra “tres” se convierte en la palabra “res” si editamos su primera letra mediante un borrado. 

- Intercambio ( _switch_ ): Cambiar una letra por una de las letras que la rodean. Por ejemplo “caso” se convierte en “caos” haciendo un cambio de la “o” por la “s” inmediatamente anterior. 

- Sustitución ( _replace_ ): Sustituir una letra por cualquier otra letra del abecedario. Por ejemplo, “mato” se convierte en “pato” sustituyendo la “m” por la “p”. 

Cualquier palabra puede convertirse en otra palabra por medio de un número finito de ediciones. En el caso de la autocorrección, trataremos de encontrar aquellas palabras con menos cantidad de ediciones grente a nuestra palabra original mal escrita. 

Para buscar la palabra o palabras que menor distancia de edición tengan con una determinada palabra dada, necesitamos un algoritmo llamado _Minimum Edit Distance_ (MED). Este algoritmo, como indica su nombre, trata de encontrar la distancia de edición mínima entre dos palabras. Esto es importante porque para pasar de “amarillo” a “amarilla” podemos hacer una única edición, o podemos hacer tantas como queramos: 

amarillo  ramarillo  remarillo  ermarillo  ermarilla  armarilla  amarilla 

Es por esto que la distancia que será realmente relevante a efectos prácticos será la **mínima distancia de edición (MED)** . El algoritmo MED fue descubierto simultáneamente por numerosos grupos de investigación durante los años 70, pero fue nombrado específicamente por los investigadores Wagner y Fischer en el año 1974. 

37 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Este algoritmo, en definitiva, nos ayuda a conocer la semejanza entre dos palabras. Cuantas menos ediciones sean necesarias para pasar de una palabra a otra, más similares serán estas dos palabras entre sí. 

El algoritmo de _Minimum Edit Distance_ asocia un coste a cada una de las ediciones que se pueden realizar. La versión más empleada es la definitiva por Levenshtein, y es por tanto la que vamos a estudiar. 

Para simplificar el algoritmo, se omiten las ediciones de intercambio, ya que son poco frecuentes, y se emplea una tabla de costes como la siguiente: 

|**Tipo de edición**|**Coste**|
|---|---|
|Inserción|1|
|Borrado|1|
|Sustitución|2|



Este coste es relativamente intuitivo, ya que una sustitución no es más que un borrado seguido de una inserción. 

Por ejemplo, para pasar de la palabra “casa” a la palabra “osa”, tenemos que hacer las siguientes ediciones: 

- borrado de c: “asa” 

- sustitución a  o: “osa” 

Esto implica una distancia de edición de 1 (borrado ) + 2 (sustitución) = 3. Las palabras “casa” y “osa” tienen una distancia de edición de 3. 

Vamos a ver en un ejemplo diversos cálculos de la distancia mínima de edición gracias al módulo NLTK de Python. 

38 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

#### **_Ejemplo Minimum Edit Distance_** 

En este ejemplo primero vamos a ejecutar el método “edit_distance” de NLTK, lo que supondrán muy pocas líneas de código. Crearemos un nuevo cuaderno de Google Collab e introduciremos lo siguiente. 



La distancia de edición mínima entre las palabras “estrella” y “destreza” es de 4 ediciones. 



```
Una inserción (destrella), una eliminación (destrela), y una susti-
tución (destreza) = 4.
```

Podemos tratar de desarrollar un algoritmo de autocorrección altamente simplificado para comprender cómo funcionan este tipo de algoritmos en la realidad. Para ello, recordemos que necesitamos un algoritmo de medición de distancias (en este caso usaremos el algoritmo edit_distance de NLTK) y un vocabulario. Podemos definir un vocabulario relacionado con materiales, como puede ser 

Usaremos cuatro palabras de test, que el alumno podrá modificar tanto como desee para hacer diversas pruebas. Cada una de las palabras de test serán evaluadas contra el vocabulario. En caso de no encontrarse en el vocabulario, se calcularán las distancias a todas las palabras correctas, para seleccionar la palabra más cercana y autocorregir el error de escritura. 

Creamos una segunda celda de código y **la ejecutamos después de la primera** . Esto es importante, porque si la primera celda no ha sido ejecutada, la librería “edit_distance” no estará importada y tendremos errores en la ejecución del código. 

39 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



Si hemos mantenido las cuatro palabras de test sugeridas, veremos que la salida de nuestro script será similar a la siguiente, que merece la pena analizar. 

40 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



En los dos primeros casos nos encontramos con palabras mal escritas por una letra. En el caso de “ardilla” podemos comprobar que se encuentra a solo 2 de distancia de “arcilla” (debido a una sustitución), por lo que esta es la seleccionada. 

En el segundo caso “mdera” está a tan solo una inserción de “madera”, por lo que esta es la palabra más cercana. 

En el tercer caso podemos ver como “asfalto” es una palabra correctamente escrita y por tanto no se ejecutan más pasos del algoritmo de autocorrección. 

Por último, tenemos la palabra “pájaro”, realmente lejana de todas las palabras de nuestro vocabulario. Por pura casualidad, la palabra más cercana es “pladur”. Sin embargo, en este caso nuestra autocorrección seguramente no hubiera complido con su cometido. Esto es debido a que estamos trabajando con un vocabulario realmente reducido a efectos de ejemplo, y por tanto hay muchas posibilidades de que suceda algo así. 

### **3.1.2. Filtrado de candidatos y estimación de probabilidad** 

Una vez tenemos una serie de palabras previamente filtradas para que pertenezcan a nuestro vocabulario, tendremos que tomar la decisión de cuál es la palabra que mejor sustituye a aquella que estamos tratando de autocorregir. En el ejemplo anterior sencillamente escogíamos la palabra con menor distancia a la que habíamos escrito erróneamente, ya que nuestro vocabulario era realmente reducido. Sin embargo, en un vocabulario completo encontraremos en múltiples ocasiones en las que hay numerosas palabras a la misma distancia mínima. Por ejemplo, si en español escribimos “osa”, tendremos entre otras a las palabras “cosa”, “rosa”, “posa”, “osas”, “losa” y “sosa” a la misma distancia. ¿Con cuál debería quedarse un algoritmo de autocorrección? Si bien podría parecer que lo más relevante sería el contexto de la frase, recordemos que estos procesos requieren de una gran velocidad y baja necesidad de capacidad de cómputo, por lo que no sería práctico aplicar un modelo semántico de NLP que comprenda el significado deseado de la frase con una palabra mal escrita para decidir por qué palabra corregirla. 

41 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Para tener una solución eficiente en coste y tiempo, vamos a definir un estadístico que nos ayude a calcular la probabilidad de que una palabra aparezca en un determinado corpus sin necesidad de comprender el contexto de cada una de las oraciones con las que trabajamos. 

Para tener una solución eficiente en coste y tiempo, vamos a definir un estadístico que nos ayude a calcular la probabilidad de que una palabra aparezca en un determinado corpus sin necesidad de comprender el contexto de cada una de las oraciones con las que trabajamos. 

Denominemos para ello _P(w)_ a la probabilidad de que una palabra aparezca en un corpus. El cálculo de _P(w)_ surge de la división del número de veces que esa palabra aparece en nuestro texto, denominado _C(w)_ , entre el número total de palabras que aparecen en nuestro corpus, que denominaremos V. 

#### De esta forma, _P(w) = C(w)/V_ 

Gracias a este sencillo estadístico, podemos estimar la probabilidad de que cada una de las palabras con mínima distancia de edición que hemos encontrado en la fase anterior aparezcan en un texto. 

Seleccionaremos por tanto la palabra con una mayor probabilidad y esta será la elegida para proponer autocorrección. 

Si bien hemos estudiado el algoritmo de _Minimum Edit Distance_ para tratar el caso de uso específico de la autocorrección, es un algoritmo que tiene muchas más aplicaciones dentro del campo del NLP. Entre otras destacan el análisis de similitud entre documentos, por ejemplo, para la detección de plagio; la traducción automática, para dar con las mejores palabras a la hora de traducir una oración; e incluso en biología computacional para ayudar a los biólogos a secuenciar el ADN, que está compuesto por cuatro letras que forman un vocabulario realmente extenso. 

Hasta el momento, hemos visto en esta asignatura la tokenización de un texto, la normalización de estos tokens para estandarizarlos, la segmentación de oraciones y, por último, el análisis de la distancia entre dos palabras para tratar de encontrar las más semejantes entre todo un vocabulario. 

El siguiente paso será categorizar estas palabras, para poder así comprender la tipología de cada una de ellas y que esto aumente nuestro conocimiento acerca del contenido de los diversos textos y corpus que nos encontremos. Recordaremos las distintas categorías léxicas y cómo emplearlas para diversos casos de uso en Procesamiento de Lenguaje Natural. También trataremos de entender cómo realizar el proceso de categorización léxica de palabras en Python de forma automática por medio de ejemplos y de una serie de algoritmos incorporados. Comprenderemos, en definitva, cómo la categorización de palabras, llamada _Part of Speech Tagging_ es habitualmente el primer paso hacia la comprensión de la estructura y contenido de cualquier oración, texto o corpus que deseemos procesar. 

42 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **3.2. Categorización de palabras (Part of Speech Tagging)** 

El proceso de clasificar palabras en las distintas **partes del discurso** es conocido formalmente como **etiquetado de partes de discurso** o, más habitualmente, por su nombre en inglés **_Part of Speech Tagging (POS-tagging)_** . Estas partes del discurso no son más que las distintas clases a las que puede pertenecer una palabra, también conocidas como categorías léxicas. El objetivo del _Part of Speech Tagging_ es generar automáticamente una etiqueta para cada token encontrado. Continuando con la similitud con los algoritmos de visión artificial, podríamos afirmar que el POS tagging es similar a la clasificación de objetos. Contaremos con una serie de clases entre las que trataremos de clasificar una palabra. 

Las **categorías léxicas** se denominan en la disciplina del NLP _open classes_ ya que están en constante cambio y crecimiento, y pueden surgir nuevas palabras pertenecientes a estas clases en cualquier momento: 

- Sustantivo: “Palabras cuyos referentes son clases de entidades fijas”, es decir, que hacen referencia a un concepto concreto y lo nombran. Desde el punto de vista sintáctico serán una de las posibilidades para representar al sujeto en una oración. El tagging de estas palabras permitirá a nuestros algoritmos identificar a los sujetos de la acción, así como las entidades principales presentes en oraciones y textos. 

- Adjetivo: “Palabras que acompañan al sustantivo para expresar una cualidad de la cosa designada por él o para determinar o limitar la extensión del mismo.”, nos permiten por tanto conocer detalles acerca de los sustantivos que hayamos identificado, por lo que serán de gran relevancia a la hora de comprender el tono y emoción de un determinado corpus. 

- Verbo: “Palabras que expresan acciones, procesos, estados o existencia que afectan a los sustantivos”, en definitiva, nos indican qué están haciendo y cómo se encuentran los sustantivos que hemos identificado previamente. 

- Adverbio: “Palabras que modifican a un verbo, a un adjetivo, a otro adverbio en lugar, tiempo, modo, cantidad y otros matices”. En definitiva, afinan el significado y connotación de estas palabras, aportando por tanto una gran carga semántica que nuestros sistemas inteligentes tendrán que comprender. 

Además, encontramos otro tipo de palabras denominadas **categorías funcionales** , que en NLP reciben el nombre de _closed classes_ ya que no existe la posibilidad de que surjan nuevas palabras de estos tipos. Entre ellas encontramos los pronombres, las preposiciones, las conjunciones, los determinantes y las interjecciones. También podremos clasificar elementos como los signos de puntuación y otros símbolos como pueden ser las divisas o los símbolos matemáticos. 

43 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Parte del trabajo de un algoritmo de POS tagging es la desambiguación de las categorías. Hay palabras que solo pueden pertenecer a una categoría y bastará con tener un gran diccionario para resolverlas, por ejemplo “y”, que es una conjunción y no puede ser nada más. Pero veamos otros ejemplos en los que necesitaríamos resolver una cierta ambigüedad: 

- “bajo” puede ser una preposición (se encuentra bajo el cielo) o un adjetivo (vive en un piso bajo) 

- “ante” puede ser una preposición (se presentó ante él) o un sustantivo (no compra prendas de ante por respeto a la naturaleza). 

Como vemos, el proceso de categorización de las partes del discurso no es trivial en absoluto. Sin embargo, veremos que en la actualidad los algoritmos de POS tagging tienen la misma precisión que los seres humanos realizando la misma tarea, que es ligeramente superior del 97%. En el caso del inglés existen un 85% de palabras que no tienen ningún tipo de ambigüedad, es decir, que bastaría con usar un diccionario para resolver su categoría. Eso nos deja con un 15% de palabras ambiguas. La mala noticia para nuestros algoritmos de POS tagging es que las palabras ambiguas son las más comunes con diferencia, y aparecen en torno a un 60% de las veces en un texto estándar. 

Vamos a ver varios algoritmos que realizan esta tarea, pero hay un concepto que será compartido entre todos ellos medir su capacidad de lograr su objetivo. El objetivo de todos estos algoritmos será superar el método de la clase más frecuente, o **_Most Frequent Class Baseline._** Este es un algoritmo trivial que a la hora de realizar la desambiguación entre clases, siempre elegirá aquella más probable. Partiendo de un corpus etiquetado podemos conocer el número de veces que la palabra “ante” es clasificada como una preposición y cuantas por un nombre. Si empleamos el método de _Most Frequent Class_ , cada vez que encontremos la palabra “ante” en futuros textos le asociaremos la clase más repetida en el corpus de entrenamiento. 

La comprobación es que para que un algoritmo sea válido tiene que acertar un mayor número de veces en la clasificación de palabras que un algoritmo trivial que aplique siempre la clase más probable a una palabra, porque de lo contrario no estará aportando valor. 

Es decir, mediremos la utilidad de nuestros algoritmos de POS tagging contra un algoritmo que lo único que hace es asignar siempre a las palabras su categoría más frecuente en el idioma en el que se trabaje. De esta forma, nos aseguraremos de que los algoritmos son más precisos que un simple modelo estadístico basado en frecuencias acumuladas. Sorprendentemente estos modelos tienen un 92% de precisión a la hora de hacer el POS tagging, por lo que es un 5% lo que tienen que mejorar los algoritmos. El primer algoritmo que estudiaremos está basado en un concepto denominado “cadenas de Markov”. 

44 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **3.2.1. Hidden Markov Chains y el algoritmo Viterbi** 

Las **cadenas de Markov** son un sistema de representación de estados y transiciones entre ellos que se usa tanto en reconocimiento del discurso como para POS tagging dentro del NLP, pero que tiene numerosas aplicaciones computacionales además de estas que hemos mencionado. **El objetivo de una cadena de Markov es tratar de modelar situaciones en las que es necesario predecir la probabilidad de pasar de un estado a otro en un sistema dado.** 

Por ejemplo, podemos usar una cadena de Markov para tratar de predecir las probabilidades de que un determinado día llueva o no en función de las condiciones meteorológicas del día actual. O, por ejemplo, el tiempo que va a hacer por la tarde dado el tiempo que hace por la mañana. Los estados de una cadena de Markov se representan como círculos en cuyo interior se escribe el nombre de cada uno de los estados. De cada uno de estos círculos salen flechas que simbolizan la transición hacia otro estado, y en cada una de ellas hay una probabilidad, que será la de transitar desde el estado del que parte hasta el estado al que llega. 

Si una flecha con el valor 0,2 transita desde el estado “soleado” hasta el estado “lluvioso”, esto quiere decir que hay un 20% de probabilidades de que, si hoy ha sido un día soleado, mañana sea un día lluvioso. Podemos ver un ejemplo sencillo de cadena de Markov aplicado a una predicción meteorológica rudimentaria en la siguiente imagen. 



Esta cadena de Markov nos indica que si hoy, por ejemplo, ha hecho un día “nublado”, es decir que partimos de ese estado, hay un 20% de probabilidad de que mañana transitemos hacia el estado “soleado”. Hay también un 30% de probabilidad de que mañana nos quedemos en el mismo estado “nublado” y un 50% de probabilidad de que mañana hayamos transitado hasta el estado “lluvioso”. 

45 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

En el caso del NLP y más concretamente del POS tagging, los estados con los que trabajaremos serán la categoría léxica de una palabra (su etiqueta) y la de la siguiente palabra en una frase. Es decir, trataremos de decidir si en una frase la última palabra que hemos procesado es un “verbo”, qué probabilidad hay de que la siguiente sea un “nombre”, un “adjetivo”, un “adverbio” o cualquier categoría. Es decir, la probabilidad de transitar de un estado a otro conociendo el estado – en este caso la categoría de una palabra – inicial. 

Por ejemplo, en la frase “La única persona que puede hacer eso es … “ podríamos asumir que la siguiente palabra que va a aparecer en esta frase va a ser un nombre, o un pronombre. Podríamos, por tanto, generar una norma que indique que después de un estado “verbo” en una frase es probable que transitemos hacia un estado “nombre”; es decir, que normalmente después de un verbo encontraremos un nombre. Para representar esto emplearemos la representación gráfica que hemos visto anteriormente, que será la que representará el estado actual de nuestra frase en cada momento, o lo que es lo mismo, en cada palabra de nuestra frase. 

En definitiva, en una cadena de Markov para POS tagging definiremos **la probabilidad de transición desde una categoría de palabra hasta otra** . Podemos ver un ejemplo de una cadena de Markov para POS tagging simplificada en la siguiente imagen. 

En cada uno de los estados vemos la categoría en la que estamos, y las probabilidades de que la siguiente palabra pertenezca a una categoría u otra. De esta forma, si nos encontramos con una palabra de la categoría “verbo”, como en la frase que hemos empleado anteriormente de ejemplo, tendremos un 40% de probabilidades de que la siguiente palabra pertenezca a la categoría “nombre”. Tendremos un 30% de probabilidades de que sea un “verbo” de nuevo, y el mismo 30% de que sea un “adjetivo”. 



Con un modelo de cadena de Markov como el de la imagen podemos construir una matriz de probabilidades sencilla, que resume de forma clara el conocimiento almacenado en esta cadena de Markov concreta. 

46 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

En esta matriz situaremos en las filas el estado actual, y en las diferentes columnas los estados hacia los que puedo transitar. El cruce de cada una de las filas y columnas representará la probabilidad de transitar desde el estado de la fila hasta el estado de la columna. Observemos en la tabla que en caso de encontrarnos con un “nombre” la probabilidad de transitar hacia un “adjetivo” es del 0,6. Esto quiere decir que cuando una palabra en una frase pertenece a la categoría “nombre” con un 60% de certeza podemos afirmar que la siguiente palabra será un adjetivo. 

||**Verbo**|**Adjetivo**|**Nombre**|
|---|---|---|---|
|**Verbo**|0.3|0.3|0.4|
|**Adjetivo**|0.3|0.1|0.6|
|**Nombre**|0.2|0.6|0.2|



Recordemos que en esta sección estamos tratando de implementar un algoritmo para clasificar partes del discurso, o lo que es lo mismo, un POS tagger. Esto significa que nuestro algoritmo trabajará con palabras a las que tendrá que asociar clases léxicas. En el ejemplo inmediatamente anterior hemos trabajado con estas clases directamente, asumiendo que conocemos la clase de la palabra en la que nos encontramos en un momento dado. 

Sin embargo, en el caso de uso real, no conoceremos las clases de las palabras (este es, de hecho, nuestro objetivo), sencillamente conoceremos la palabra, y tendremos que ser capaces de asociarle una determinada clase. 

Cuando el estado en el que se encuentra una cadena de Markov no es directamente observable, se trabaja con modelos algo más complejos llamados **_Hidden Markov Models_** . Este nombre deriva del hecho de que la máquina no conoce el estado en el que se encuentra. Tendremos por tanto dos tipos de estado, los estados observables y los estados no observables. Esto aplicado a nuestro problema es sencillo de comprender. Cuando un sistema de POS tagging lee un texto se encuentra con palabras de las que desconoce las etiquetas. Por tanto, no puede saber en el estado en el que se encuentra a priori. 

Los estados observables, los que el sistema sí ve, serán todas las palabras de nuestro corpus. Por otro lado, tendremos estados no observables, que son las categorías del part of speech (nombres, verbos, adjetivos, adverbios…), dado que no se pueden conocer sencillamente observando la palabra. Esto complica las cosas, ya que si tenemos dos tipos de estado tendremos dos tipos de probabilidad a la que prestar atención. 

47 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

En un _HMM (Hidden Markov Model)_ trabajaremos por tanto con dos matrices de probabilidades. Por un lado, tendremos la matriz con las probabilidades de **transición** , que definen la probabilidad de pasar **de un estado no observable a otro estado no observable** . Por ejemplo, podríamos preguntarnos la probabilidad de que, dado un “adjetivo”, la siguiente palabra sea un “nombre”. Esta es la matriz que hemos calculado anteriormente para el ejemplo de cadena de Markov aplicado a categorías de palabras. 

Por otro lado, encontraremos la matriz con las probabilidades de **emisión** , que son las probabilidades de que **desde un estado oculto se pase a un estado visible** , es decir, el paso de una categoría léxica hacia una palabra concreta. Por ejemplo, la probabilidad de que, si estamos en un estado oculto “adjetivo”, pasemos a un estado visible “malicioso”. 

Esta segunda tabla de probabilidades es menos intuitiva, ya que transita desde las etiquetas concretas (nombre, verbo, adjetivo…) en las filas hacia las palabras específicas en las columnas. Podemos imaginar un ejemplo de tabla de emisión con la siguiente tabla. Habrá tantas columnas como palabras existan en nuestro vocabulario. 

||**Comer**|**Sencillo**|**Mirando**|**…**|
|---|---|---|---|---|
|**Verbo**|0.4|0.1|0.4|…|
|**Adjetivo**|0.2|0.6|0.1|…|
|**Nombre**|0.1|0.3|0.2|…|



Dado un corpus de entrenamiento con el que deseemos generar nuestro algoritmo de POS tagging, tendremos que calcular la matriz de emisión y la matriz de transición de dicho corpus para generar entonces un _Hidden Markov Model_ que represente nuestro corpus y sus categorías léxicas y palabras. Para ello habitualmente nos basaremos en un gran corpus de muestra previamente etiquetado. Esto quiere decir que cada una de las palabras del corpus estará etiquetada previamente con la categoría de discurso a la que pertenece. 

48 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Emplearemos un ejemplo para comprender el método de generación de estas matrices de forma teórica, para lo que imaginemos un texto corto para ayudarnos a comprender el proceso, aunque los corpus reales para el entrenamiento tengan miles de palabras. Si tenemos un texto etiquetado de la siguiente forma: 

“Hoy [ADV] ha [VER] muerto [VER] mamá [NOM]. O [CONJ] quizá [ADV] ayer [ADV]. No [ADV] lo [PRON] sé [VER]. Recibí [VER] un [DET] telegrama [NOM] del [PREP][ART] asilo[NOM]” 

Primero trataremos de calcular la matriz de transición. La probabilidad de transición de ADV (adverbio)  VER (verbo) será el resultado de sumar la cantidad de veces que sucede la transición ADV  VER y dividirla entre el total de transiciones que existen partiendo del estado ADV hacia cualquier otro en nuestro corpus. 

En este caso tenemos 1 transición ADV  VER de entre 4 transiciones que parten de adverbios, por lo que la probabilidad ADV  VER será: 

#### **_P(ADV,VER)= 1/4 = 0,25._** 

Podemos calcular también la probabilidad de transición ADV  ADV. Tenemos 2 ejemplos de esta transición, por lo que: 

#### **_P(ADV,ADV)= 2/4 = 0, 5._** 

La última transición con la que contamos es 1 muestra de ADV  PRON, que termina de completar la probabilidad de transición de los adverbios. Todas las demás transiciones, según nuestro corpus, tendrán una probabilidad 0. 

#### **_P(ADV,PRON)= 1/4 = 0,25._** 

Si realizamos este proceso para todas las posibles transiciones desde cualquier categoría hasta cualquier categoría, tendremos la tabla de probabilidades de transición, que recordemos que indica la probabilidad de pasar de un estado no observable hasta otro estado no observable. 

Para poder aplicar este algoritmo necesitamos definir un estado inicial como un estado no observable nuevo, que será desde el que parta nuestro algoritmo. Para ello, emplearemos la primera palabra de cada párrafo de nuestro corpus y estimaremos las probabilidades de la misma manera. 

Si calculamos la matriz de transición de nuestro pequeño corpus obtendremos la siguiente matriz. Por supuesto es una matriz con poca utilidad, ya que nuestro corpus era demasiado limitado como para poder comprender estadísticamente la probabilidad de transitar desde un estado oculto hasta otro, pero al menos nos ha ayudado a comprender el proceso de construir esta tabla de probabilidades. 

49 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

La última transición con la que contamos es 1 muestra de ADV  PRON, que termina de completar la probabilidad de transición de los adverbios. Todas las demás transiciones, según nuestro corpus, tendrán una probabilidad 0. 

#### **_P(ADV,PRON)= 1/4 = 0,25._** 

Si realizamos este proceso para todas las posibles transiciones desde cualquier categoría hasta cualquier categoría, tendremos la tabla de probabilidades de transición, que recordemos que indica la probabilidad de pasar de un estado no observable hasta otro estado no observable. 

Para poder aplicar este algoritmo necesitamos definir un estado inicial como un estado no observable nuevo, que será desde el que parta nuestro algoritmo. Para ello, emplearemos la primera palabra de cada párrafo de nuestro corpus y estimaremos las probabilidades de la misma manera. 

Si calculamos la matriz de transición de nuestro pequeño corpus obtendremos la siguiente matriz. Por supuesto es una matriz con poca utilidad, ya que nuestro corpus era demasiado limitado como para poder comprender estadísticamente la probabilidad de transitar desde un estado oculto hasta otro, pero al menos nos ha ayudado a comprender el proceso de construir esta tabla de probabilidades. 

||**NOM**|**VER**|**ADV**|**ADJ**|**PRON**|**CONJ**|**ART**|**DET**|
|---|---|---|---|---|---|---|---|---|
|**NOM**||||||0,5||0,5|
|**VER**|0,25|0,5||||||0,25|
|**ADV**||0,25|0,5||0,25||||
|**PRON**||1|||||||
|**CONJ**|||1||||||
|**ART**|1||||||||
|**DET**|1||||||||



La siguiente matriz que vamos a tratar de calcular es la matriz de emisión, que es la que representa las probabilidades de pasar desde un estado oculto (categoría de palabra) hacia un estado visible (una palabra concreta). 

Para hacer esto, volvamos a nuestra frase estudiada anteriormente. En las filas de nuestra matriz volverán a estar todas las categorías de palabras. Pero ahora en las columnas tendremos cada palabra de nuestro corpus. Para calcular la probabilidad de emisión desde el estado oculto NOM hasta la palabra concreta “mamá”, tendremos que ver cuántas veces una etiqueta “nombre” tiene como palabra asociada “mamá” y dividirlo entre el total de las palabras etiquetadas como nombre. 

50 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

En este caso es muy sencillo ya que tenemos 3 nombres y solo 1 de ellos es la palabra “mamá”. Lo mismo sucede con ”telegrama” y con “asilo”. Por tanto, la probabilidad de emisión será: 

#### **_C(NOM, ”mamá”)= 1/3 = 0, 33_** 

**_C(NOM, ”asilo”)= 1/3 = 0, 33._** 

#### **_C(NOM, ”telegrama”)= 1/3 = 0, 33._** 

Esto nos indica que cuando nuestro sistema esté en un estado oculto “NOM” tiene la misma probabilidad de emitir a un estado visible “mamá” que a “telegrama” que a “asilo”. 

De nuevo, empleando un corpus tan pequeño es difícil obtener resultados con sentido, ya que para completar estas dos matrices necesitaríamos enormes corpus en español. 

Sin embargo, este pequeño corpus nos ha ayudado a comprender cómo pasar de un corpus etiquetado a una matriz de transición y a una matriz de emisión, que son las dos partes críticas para representar un sistema de _Parts of Speech Tagging_ mediante un _Hidden Markov Model_ . 

Hasta el momento hemos construido dos matrices de probabilidades que definen un modelo oculto de Markov. Conocemos la probabilidad de pasar de una categoría de palabra a otra (estados ocultos) y la probabilidad de pasar de una categoría de palabra a una palabra específica (estado visible). Ahora bien, ¿cómo construimos un algoritmo para clasificar palabras basándonos en esto? Es para responder esta pregunta que surge el **algoritmo de Viterbi.** 

**El algoritmo de Viterbi** es un algoritmo de grafo que trabaja con _Hidden Markov Models_ y trata de encontrar la secuencia más probable de estados ocultos, lo que denominamos **camino de Viterbi** . En nuestro caso, por tanto, trata de estimar la secuencia más probable de categorías de palabras dada una frase. 

El funcionamiento del algoritmo de Viterbi es el siguiente: En cada estado multiplica la probabilidad de pasar del estado actual a cualquiera de los estados ocultos que pueden llegar a emitir el estado visible. Hecho esto, seleccionará el estado oculto futuro que más probabilidad alcance. 

#### Formalmente esto es 

_P(estado_actual, estado_futuro) x C(estado_futuro, estado_visible)_ 

51 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

O aplicado a nuestro caso: la probabilidad de que desde una categoría de palabra pasemos a otra multiplicada por la probabilidad de que la siguiente palabra de la frase pertenezca a esta nueva categoría. 

Vamos a tratar de ejemplificar su funcionamiento para comprender cómo, partiendo de nuestras dos matrices de probabilidades podemos estimar las categorías de las palabras de una frase. Recordemos que vamos a trabajar de la siguiente manera: Conoceremos el estado en el que estamos (la categoría de la palabra anterior de la frase) y la palabra actual. Tendremos que encontrar el estado futuro (es decir, la categoría de la palabra actual) en base a nuestras dos matrices de probabilidades que han sido extraídas de un corpus empleando un _Hidden Markov Model_ (HMM) o un Modelo Oculto de Markov. 

||**NOM**|**VERB**|**ADJ**|**ADV**|**PREP**|
|---|---|---|---|---|---|
|**Estado 0**|0,5|0,1|0,1|0,2|0,1|
|**NOM**|0,1|0,3|0,4|0,1|0,1|
|**VERB**|0,1|0,1|0,05|0,3|0,4|
|**ADJ**|0,2|0,3|0,01|0,1|0,3|
|**ADV**|0,3|0,4|0,2|0,2|0,1|
|**PREP**|0,6|0,4|0|0,1|0|



||**coto**|**privado**|**de**|**caza**|
|---|---|---|---|---|
|**NOM**|0,2|0,3|0,2|0,3|
|**VERB**|0|0,1|0|0,2|
|**ADJ**|0|0,7|0|0|
|**ADV**|0|0,1|0|0|
|**PREP**|0|0|0,7|0|



Empezaremos por la primera palabra de “coto privado de caza”. Estamos en el “estado 0” (acabamos de empezar) y hay opciones de transitar hacia [NOM], [ADJ], [ADV] y [PREP] (ver primera tabla). 

Nuestra primera palabra es “coto”, y puede ser emitida únicamente por la categoría [NOM]. Por tanto, tendremos que calcular la siguiente probabilidad, tal y como hemos indicado anteriormente: 

_P(estado_0, NOM) x C(NOM, ”coto”)= 0,5 x 1 = 0,5_ 

52 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Hemos calculado la probabilidad de que el primer tag sea [NOM] y de que este [NOM] emita nuestra palabra, “coto”. Como podemos ver, la mayor probabilidad ha sido asignada a [NOM], ya que no había más opciones. Este será el tag que marquemos como inicio de nuestro **camino de Viterbi** . 



Ahora estamos en un estado [NOM] y conocemos el siguiente estado visible, que es la palabra “privado”. Para calcular el siguiente movimiento, es decir, el siguiente estado oculto, debemos mirar las probabilidades de pasar desde un estado [NOM] hasta cualquiera de los estados ocultos asociados a la palabra “privado”. 

Para esto primero miramos a la **matriz de emisión** y vemos que “privado” puede ser emitido por palabras con las categorías [NOM], [VER], [ADJ] y [ADV] con probabilidades 30%, 10%, 70% y 10% respectivamente. 

En este momento, el algoritmo de Viterbi multiplica la probabilidad de pasar desde [NOM] hasta cada una de las categorías seleccionadas por la probabilidad de que “privado” sea emitido por alguna de estas categorías. Esto significa: 

**_P(NOM, NOM) x C(NOM, ”privado”)= 0,1 x 0,3 = 0,03_** 

**_P(NOM, VER) x C(VER, ”privado”)= 0,3 x 0,1 = 0,03_** 

**_P(NOM, ADJ) x C(ADJ, ”privado”)= 0,4 x 0,7 = 0,28_** 

**_P(NOM, ADV) x C(ADV, ”privado”)= 0,1 x 0,1 = 0,01_** 

Como podemos ver, la probabilidad mayor indica que, de todas las posibilidades, la más alta es que “privado” sea una palabra que dado el contexto de la frase pertenezca a la categoría de adjetivo, [ADJ], por lo que el algoritmo de Viterbi avanzará un estado, hasta la palabra “de” en el estado [ADJ], como podemos ver en el siguiente diagrama. 

Además, para computar la probabilidad absoluta de cada una de estas ramas del posible camino óptimo, tenemos que multiplicar la probabilidad del tag anterior por la de cada uno de estos caminos. Recordemos que la probabilidad de que el primer tag fuera [NOM] es del 0,5. Por tanto, multiplicaremos todas las probabilidades de este estado _por la probabilidad acumulada en el camino que llevamos hasta ahora._ 

53 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

**_P(estado_0, NOM, NOM)= 0,03 x 0,5 = 0,015 P(estado_0, NOM, VER) = 0,03 x 0,5 = 0,015 P(estado_0, NOM, ADJ) =  0,28 x 0,5 = 0,14_** 

#### **_P( estado_0, NOM, ADV) = 0,01 x 0,5 = 0,0015_** 

El estado de nuestro algoritmo de Viterbi hasta ahora es, por tanto, el que podemos observar en el siguiente diagrama. En cada uno de los tags se encuentra la probabilidad de que un determinado camino llegue hasta ellos. 

Parece que la probabilidad mayor de nuestro camino por ahora pasa por [ADJ]. Sin embargo, no vamos a abandonar el resto de ramas posibles todavía. ¿Por qué? Porque no sabemos qué viene después, por lo que, aunque ahora el tag [ADJ] tenga la mayor probabilidad, no podemos descartar que las siguientes palabras de nuestra frase cambien estas probabilidades. Vamos a ver esto en nuestro ejemplo a continuación. 



En el siguiente paso el algoritmo de Viterbi comienza a tener más trabajo. La palabra “de” puede ser un nombre (la cuarta letra del alfabeto) o una preposición. Para que el algoritmo de Viterbi pueda elegir el mejor camino deberá computar ocho nuevas ramas. Son las que van desde [NOM]  [NOM], [NOM]  [PREP], [VER]  [NOM], [VER]  [PREP], y así sucesivamente hasta llegar a [ADV]  [PREP]. 

El proceso será exactamente el mismo. Primero calcularemos la probabilidad de que estando en  [NOM] el siguiente estado oculto sea [NOM] (probabilidad de transmisión) y la multiplicaremos por la probabilidad de que el siguiente estado oculto sea [NOM] y emita la palabra “de”, además, la multiplicaremos por la probabilidad de la rama completa del camino que la precede, que en este caso es 0,015. 

54 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Lo vemos en el siguiente cálculo 

#### **_P(NOM, NOM) x C(NOM, ”de”)= 0,1 x 0,2 = 0,02_** 

#### **_P(estado_0, NOM, NOM, NOM) = 0,02 x 0,015 = 0,0003_** 

Por poner otro ejemplo, podemos calcular la rama del camino que va desde [ADJ]  [PREP]. Para ello calculamos la probabilidad de transición P(ADJ,PREP) y la probabilidad de emisión C(PREP, “de”) y las multiplicamos. Además, multiplicamos esta probabilidad por la de la rama que la precede que es P(estado_0, NOM, ADJ) y hallaremos definitivamente la probabilidad de esta rama que es la P(estado_0, NOM, ADJ, PREP). Lo vemos en el ejemplo 

#### **_P(ADJ, PREP) x C(PREP, ”de”)= 0,3 x 0,7 = 0,21_** 

#### **_P(estado_0, NOM, ADJ, PREP) = 0,21 x 0,14 = 0,0294_** 

Para ahorrar espacio, vamos a representar el resto de cálculos necesarios en una tabla como la siguiente: 

|**anterior**|**futuro**|**p. transición**|**p. emisión**|**p. rama anterior**|**p. rama**|
|---|---|---|---|---|---|
|**NOM**|NOM|0,1|0,2|0,015|**0,0003**|
|**NOM**|PREP|0,1|0,7|0,015|**0,00105**|
|**VER**|NOM|0,1|0,2|0,015|**0,0003**|
|**VER**|PREP|0,4|0,7|0,015|**0,0042**|
|**ADJ**|NOM|0,2|0,2|0,14|**0,0056**|
|**ADJ**|PREP|0,3|0,7|0,14|**0,0294**|
|**ADV**|NOM|0,3|0,2|0,0015|**0,00009**|
|**ADV**|PREP|0,1|0,7|0,0015|**0,000105**|



Que podemos representar en nuestro diagrama a su vez de la siguiente manera 



55 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Es este momento en el que el algoritmo de Viterbi muestra su capacidad de optimización. En el estado anterior, cuando analizábamos la palabra “privado”, teníamos cuatro posibles estados futuros y cada uno de ellos tenía una única rama. Esto implica que no podemos “podar” ninguna rama ya que quizá e el futuro la rama más prometedora no fuera la más correcta. 

Sin embargo, en este estado, analizando la palabra “de”, tenemos dos posibles estados futuros a cada uno de los cuales llegan **cuatro ramas** distintas. Aquí podemos asumir que, pase lo que pase en el futuro, la rama más probable siempre tendrá que ser la que pase por la rama que maximiza la probabilidad en cada nodo. No vamos a quitar posibles estados futuros, pero sí que vamos a podar todas las ramas que llegan a estos nodos excepto aquella con una mayor probabilidad. En definitiva, asignaremos a cada estado la probabilidad del camino más probable que llega hasta él, olvidando los demás. Esto podríamos representarlo de la siguiente manera: 



Llegamos por tanto a la última palabra, “caza”. Repetiremos el proceso de cálculo de probabilidades de transición y emisión con los resultados que podemos observar en la siguiente tabla. 

|**anterior**|**futuro**|**transición**|**emisión**|**rama anterior**|**probabilidad rama**|
|---|---|---|---|---|---|
|NOM|NOM|0,1|0,3|0,0056|0,000168|
|NOM|VER|0,3|0,2|0,0056|0,000336|
|PREP|NOM|0,6|0,3|0,0294|0,005292|
|PREP|VER|0,4|0,2|0,0294|0,002352|



56 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Como vemos, la rama más probable es aquella que transita desde [PREP] hasta [NOM]. Nos quedaremos de nuevo con la mayor de las probabilidades de cada nodo, por lo que nuestro camino de Viterbi quedará como vemos en el siguiente diagrama. 

Ahora que hemos procesado todas las palabras de la frase, podemos decidir cuál es nuestro camino de Viterbi. Cuál es el camino que, transitando por todos los posibles estados ocultos, da una mayor probabilidad si aplicamos el _Hidden Markov Model_ del que hemos partido al comienzo de este ejemplo. 

El algoritmo de Viterbi tiene la gran ventaja de tener la capacidad de abandonar caminos cuando estos no permiten obtener mayores probabilidades en el futuro. En nuestro diagrama son todas las flechas y probabilidades en rojo. Gracias a este comportamiento, reducimos enormemente la carga computacional de este algoritmo ya que si usáramos un algoritmo de fuerza bruta que computara todos los caminos posibles la complejidad sería exponencial y el tiempo de cómputo sería demasiado elevado para frases complejas con un gran número de palabras. 



57 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **3.3. N-Grams – Autocompletado de texto** 

Hasta este momento hemos visto cómo podemos preprocesar un texto y posteriormente comprender la tipología de palabras que lo componen (POS tagging). Es decir, hemos hecho un análisis exploratorio de un texto, con el objetivo de conocerlo mejor y poder extraer información relevante del mismo. 

Pongamos ahora otro objetivo que destaca dentro del mundo del NLP: la capacidad para predecir. Hablamos de poder inferir la siguiente palabra que va a aparecer en un texto o frase únicamente conociendo las palabras que la preceden. Esto es exactamente lo que hacen los teclados predictivos a los que nos hemos acostumbrado dentro de nuestros dispositivos inteligentes. 

Por ejemplo, podríamos querer completar la frase “El árbol se inclinó debido a una ráfaga de …”. Como hispanohablantes sabemos que la palabra que con mayor probabilidad continuará esta frase es “viento” y no “madera” o “piedras”. Pero, ¿cómo conseguir un modelo predictivo que sea capaz de hacer este ejercicio por nosotros? Esto nos ayudaría no solo a crear predictores para un usuario final, sino para corregir automáticamente errores gramaticales o sugerir cambios en documentos, e incluso para mejorar la calidad de la traducción automática entre dos idiomas. Esta tecnología de autocompletado tiene una gran relevancia en el campo de los sistemas de comunicación alternativos o AAC por sus siglas en inglés, sistemas diseñados para personas con ciertas limitaciones en el habla debido a distintos tipos de condiciones que ayudan a estas personas a poder comunicarse por medio de un selector de palabras que tienen este tipo de modelos de lenguaje. 

El modelo de lenguaje (LM por sus siglas en inglés) más sencillo que vamos a analizar es un modelo denominado **n-gram** . Un **n-gram es una secuencia de n palabras** . Por tanto, un 3-gram podría ser “salió el sol”, y un 5-gram “salió el sol por la mañana”. 

Los modelos n-gram nos ayudarán a asignar distintas probabilidades a cada una de las posibles secuencias que puede generar cada uno de ellos según el valor de su n. Si bien existen otros métodos de predicción del lenguaje más avanzados como son las Redes Neuronales Recurrentes (RNN) y los Transformers, los modelos n-gram son una tecnología crítica en el campo del NLP y es esencial conocerlos y entender su funcionamiento para poder progresar en el estudio del modelado del lenguaje. 

El caso más sencillo que podemos proponernos es calcular la probabilidad de que dada una frase “s” el siguiente token sea la palabra “w”. Denominemos a esta probabilidad condicionada P(w|s). 

58 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Si tenemos una frase s=”La mesa del salón está” y queremos computar la probabilidad de que w=”rota” podemos acudir, como siempre, a un mecanismo de fuerza bruta. Si tuviéramos un corpus suficientemente grande en español como para que la frase “La mesa del salón está” apareciera suficientes veces, podríamos calcular la probabilidad de cualquier w mirando sencillamente a nuestro corpus. Si en nuestro corpus “rota” aparece 2 veces de las 100 que encontramos nuestra frase, entonces P(w|s) = 0,2. Sin embargo, se antoja improbable que, por muy grande que sea cualquier corpus que podamos conseguir, seamos capaces de encontrar todas y cada una de las posibles frases que pueden ser creadas en español un número suficiente de veces como para que esto sea estadísticamente significativo. Ni siquiera empleando toda la web podríamos cubrir todas las posibles frases en español y todas las posibles palabras que pueden aparecer detrás de las mismas. 

Recordemos que este era el caso más sencillo. Si en lugar de querer estimar la probabilidad de una única palabra queremos estimar un conjunto de palabras, pongamos 3, como puede ser “rota por debajo”, el cómputo de esta probabilidad y las opciones de que aparezca en nuestro corpus empiezan a ser prácticamente imposibles. 

Por ello tenemos que simplificar los cálculos, y los modelos n-gram consiguen hacer esto reduciendo el número de palabras en los que se centran para realizar la predicción. Por ejemplo, un modelo 2-gram solo emplea la última palabra de la frase para predecir la siguiente palabra. En nuestro ejemplo, en lugar de calcular P(rota | La mesa del salón está), un modelo 2-gram habría tratado de calcular la probabilidad P(rota | está). 

Para calcular esta probabilidad un modelo 2-gram buscará en nuestro corpus todas las apariciones de la palabra “está” y registrará todos los 2-grams (llamados bigramas) que se generan siendo la palabra “está” la primera de las dos palabras. 

De igual forma, un modelo 3-gram buscará todas las apariciones de la palabra está y sus dos palabras posteriores, creando así 3-grams (o trigramas). 

Para calcular las probabilidades de cada uno de los bigramas o trigramas emplearemos la frecuencia relativa de todos ellos en relación con el conjunto de nuestro corpus. Vamos a verlo en un sencillo ejemplo. 

59 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Pongamos que tenemos un corpus formado por tres frases. 

```
1. “La casa de mis padres está muy lejos de la ciudad”
```

```
2. “La motocicleta de Manuel está rota desde el año pasado, no es ca-
paz de encender el motor”
```

`3.  “El tiempo está muy inestable, ayer hizo sol y hoy está nublado”` Para construir un modelo de 2-gram veremos que tenemos 2 apariciones del bigrama (está, muy), 1 aparición del bigrama (está, rota) y una aparición del bigrama (está, nublado) 

Teniendo en cuenta que la palabra “está” aparece un total de 4 veces, las probabilidades de nuestro pequeño modelo 2-gram serían las siguientes: 

P(muy | está) = 2/4 = 1/2 

P(rota | está) = 1/4 

P(nublado | está) = 1/4 

Si queremos construir un modelo 3-gram nuestras probabilidades cambiarán, ya que tenemos 1 aparición del trigrama (está, muy, lejos), 1 aparición del trigrama (está, rota, desde), 1 aparición del diagrama (está, muy, inestable) y 1 aparición del diagrama (está, nublado, .), por lo que tendremos ¼ de probabilidades de cada una de ellas en nuestro modelo 3-gram. 

Para construir cualquier modelo con una n superior, como pueden ser 4-gram o 5-gram podríamos seguir exactamente el mismo método. 

Gracias a esta aproximación podemos tratar de estimar la probabilidad de que una determinada palabra suceda al final de una determinada frase. Por ahora esto no nos aporta demasiada información, pero sienta una base para ejecutar operaciones más complejas. Vamos a centrarnos ahora en estimar la probabilidad de una frase, o lo que es lo mismo, una secuencia de palabras. 

Para ello, tenemos que hacer un comentario rápido sobre el funcionamiento de la probabilidad encadenada, o la llamada “regla de la cadena”. Esta regla establece que para calcular la probabilidad conjunta de dos variables aleatorias A y B, podemos calcular la probabilidad de  que suceda B dado el suceso A y multiplicarla por la probabilidad de que suceda B. Esto se puede expresar de la siguiente manera: 

#### **P(A,B) = P(B|A) x P(A)** 

60 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Por ejemplo, para saber la probabilidad de que mañana haga calor y esté soleado P(calor, soleado), podemos calcular la probabilidad de que haciendo calor esté soleado P(soleado | calor) y multiplicarla por la probabilidad de que haga calor P(calor), lo que nos quedaría como 

P(calor, soleado) = P(soleado | calor) x P(calor) 

Podemos aplicar esta regla a tantos sucesos como deseemos, por ejemplo, para cuatro sucesos aleatorios A, B, C y D, la regla de la cadena sería como sigue: 

#### **P(A, B, C, D) = P(A) x P(B|A) x P(C|A,B) x P(D|A,B,C)** 

Y, ¿cómo podemos aplicar esto a nuestro objetivo de obtener modelos de lenguaje predictivos dentro del campo del Procesamiento del Lenguaje Natural? 

Recordemos que estamos tratando de obtener predicciones para frases enteras. Por ejemplo, supongamos que queremos calcular la probabilidad de la frase “hoy compré dos pantalones” suceda en nuestro modelo de lenguaje. Para hacer esto, deberemos aplicar la cadena de probabilidad: 

P(hoy, compré, dos, pantalones) = P(hoy) x P(compré | hoy) x P(dos | hoy compré) x P(pantalones | hoy compré dos) 

Con un ejemplo como esta frase se comprende mucho mejor la regla de la cadena. Básicamente buscamos los n-gramas necesarios para cada palabra según su posición en la frase, y calculamos su probabilidad. El n-grama más grande que tenemos es la frase completa, que es un tetragrama formado por las palabras (hoy, compré, dos, pantalones). Para obtener cada una de estas probabilidades, un algoritmo de n-gram buscará en nuestro corpus cuantas veces aparece la palabra “hoy” entre todas las palabras del corpus y dividirá este valor entre el número total de palabras del corpus. Esta será P(hoy). 

Después, buscará cuántas veces la palabra “compré” aparece después de la palabra “hoy”, lo dividirá entre todas las ocurrencias de la palabra hoy, y esto será P(compré | hoy).  De igual forma calculará las probabilidades del siguiente trigrama y del siguiente tetragrama para obtener la probabilidad completa de la frase. 

En este caso estamos dando por sentado que todos estos n-gramas aparecen en nuestro corpus con una relevancia estadística suficiente. Sin embargo, como ya sabemos, esto es altamente improbable, y lo más habitual será que nuestros modelos de lenguaje se encuentren con frases que no aparecen en nuestro corpus. Es aquí cuando las nociones de los 2-grams que hemos estudiado antes cobran sentido. En lugar de calcular la probabilidad de la frase completa, podemos calcular la probabilidad de los distintos bigramas que la componen, de igual manera que anteriormente solo mirábamos a la palabra anterior para predecir una palabra en lugar de a toda la frase precedente. 

61 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Gracias a esta técnica podemos aproximar la regla de la cadena de una forma más sencilla, que sigue siendo relevante a nivel lingüístico y estadístico. Si aplicamos esta aproximación basada en bigramas, la fórmula anterior para el cálculo de P(hoy, compré, dos, pantalones) quedaría de la siguiente manera: 

P(hoy, compré, dos, pantalones) = P(hoy) x P(compré | hoy) x P(dos | compré) x P(pantalones | dos) 

Tomemos un momento para comparar ambas fórmulas. En la fórmula anterior teníamos un tetragrama, lo que implicaba que en nuestro corpus necesitamos que aparezca este tetragrama para poder calcular su probabilidad, lo cual era muy improbable. Sin embargo, con la simplificación que acabamos de realizar toda nuestra fórmula está compuesta por bigramas – además de la palabra inicial – lo que aumenta exponencialmente las probabilidades de encontrar dichos bigramas en nuestro corpus para poder computar estas probabilidades. Esta aproximación en la que solo consideramos relevante la última palabra que encontramos en nuestra frase se denomina **Markov assumption** o “suposición de Markov” mediante la cual simplificamos el cálculo de probabilidades para la predicción de una frase empleando únicamente las probabilidades de los bigramas que componen nuestra frase y multiplicándolos entre sí. 

Si empleamos esta suposición estaremos trabajando con bigramas excepto en dos casos muy concretos para nuestras frases, el comienzo y el final de las mismas. 

Para poder trabajar en estas dos situaciones específicas definiremos dos símbolos artificiales para que nuestros modelos puedan trabajar con ellos: 

- Símbolo de comienzo de frase <s> 

- Símbolo de fin de frase </s> 

La probabilidad de nuestra primera palabra será por tanto P(hoy | <s>) y podremos trabajarla como la probabilidad de un bigrama. 

Haremos lo mismo para el final de la frase. Esto será muy interesante porque nos ayudará a estimar la probabilidad de que una frase acabe con una determinada palabra, en lugar de predecir otra palabra que continúe la frase. Esto quiere decir, que en nuestro ejemplo anterior añadiremos al final una última probabilidad que desearemos calcular, que será P(</s> | pantalones). Esta será la probabilidad de que nuestra frase de ejemplo concreta acabe con la palabra “pantalones”. 

Gracias a la inclusión de los símbolos de principio y final de frase, nuestros modelos de lenguaje pueden estimar las probabilidades de frases completas teniendo en cuenta la probabilidad de que la frase **comience** con una palabra determinada y también que **termine** con una palabra determinada. 

62 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **3.3.1. Matriz de recuento (count matrix)** 

La probabilidad de conteo nos permite conocer la probabilidad de que cada una de las palabras de un corpus vaya seguida de cualquiera de las otras palabras de nuestro corpus. En definitiva, relaciona todas las palabras de nuestro vocabulario con todas las palabras de nuestro vocabulario para permitir a nuestros modelos generar frases y predecir palabras de forma automática. 

Vamos a ver el procedimiento por el que los modelos de lenguaje de NLP generan estas matrices de conteo, llamadas _count matrix_ , ya que son la base de todos los modelos de lenguaje basados en N-gram. 

#### **Paso 1. Matriz de recuento.** 

El primer paso que ejecuta todo modelo de lenguaje dado un corpus es generar la matriz de recuento o conteo. Este concepto es relativamente sencillo, ya que se trata de generar una matriz de frecuencias acumuladas. Cada vez que en el corpus aparece un bigrama determinado, se suma 1 en la celda correspondiente a la fila de la palabra 1 y la columna de la palabra 2. 

Por ejemplo, para la frase “tengo mucho frío” sumaríamos 1 unidad al recuento de la celda que se encuentra en la fila “tengo” y en la columna “mucho”, y también 1 unidad al recuento de la celda que se encuentra en la fila “mucho” y en la fila “frío”. Si tuviéramos un corpus compuesto por una única frase como la siguiente “tengo mucho frio y mucho miedo, pero no tengo hambre”, la matriz de recuento quedaría como sigue. Como podemos ver el símbolo de principio de frase sólo lo ponemos en las filas porque solo puede comenzar un bigrama, mientras que el símbolo de cierre de frase solo lo ponemos en las columnas porque solo puede ser el segundo elemento de un bigrama. 

Las matrices de recuento en corpus muy grandes suelen ser muy dispersas, ya que la gran mayoría de las palabras de un corpus no tendrán correspondencia con la gran mayoría del resto de palabras del corpus. Incluso con una única frase podemos ver esta dispersión. 

||</s>|tengo|mucho|frío|y|miedo|pero|no|hambre|
|---|---|---|---|---|---|---|---|---|---|
|<s>|0|1|0|0|0|0|0|0|0|
|tengo|0|0|1|0|0|0|0|0|1|
|mucho|0|0|0|1|0|1|0|0|0|
|frío|0|0|0|0|1|0|0|0|0|
|y|0|0|1|0|0|0|0|0|0|
|miedo|0|0|0|0|0|0|1|0|0|
|pero|0|0|0|0|0|0|0|1|0|
|no|0|0|0|0|0|0|0|0|0|
|hambre|1|0|0|0|0|0|0|0|0|



63 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

#### **Paso 2. Matriz de probabilidad** 

La matriz de probabilidad sencillamente calcula las probabilidades de cada uno de los binomios en base a las frecuencias acumuladas. Como suele hacerse para normalizar, dividiremos el valor de cada celda entre la suma de todos los valores de su fila, es decir, dividiremos cada frecuencia entre el total de apariciones de una palabra en nuestro corpus. 

En la tabla de nuestro ejemplo, tendremos que la probabilidad del bigrama P(frío | mucho) = 0,5 y de igual forma P(miedo | hambre) será de 0,5 también. 

Esta matriz de probabilidad será la que alimente a nuestro modelo de lenguaje. 

### **3.3.2. Aplicar un modelo de lenguaje basado en N-gram** 

Nuestro modelo de lenguaje empleará la matriz de probabilidades para calcular la probabilidad de la siguiente palabra en cada momento de una frase para cumplir su objetivo. Sencillamente devolverá la palabra con la mayor probabilidad asociada según la matriz de probabilidad que hayamos construido. 

Podríamos usar esta misma funcionalidad para crear un algoritmo generativo de lenguaje, que, a partir de una única palabra seleccionada como principio de frase, construya una frase hasta que el token </s> sea seleccionado. Este sencillo modelo generativo podría ser empleado para crear frases sueltas, pero siempre llegaremos al mismo resultado con cada una de las palabras de inicio, a no ser que introduzcamos algún tipo de aleatoriedad en la selección de la palabra con mayor probabilidad. 

Por ejemplo, podríamos seleccionar una de las tres palabras con mayor probabilidad siempre que las probabilidades calculadas entre estas tres palabras difieran menos de un cierto valor dado. 

### **3.3.3. Evaluación de modelos de lenguaje: perplejidad (perplexity)** 

Para evaluar un modelo de lenguaje de NLP primero realizaremos el proceso necesario de preparación de los datos en cualquier sistema que queramos ajustar y evaluar, la división de los datos. Existen diversas ratios con los que podemos hacer esto. En función del tamaño de nuestro corpus emplearemos desde un 70% hasta un 98% del corpus para calcular la matriz de probabilidad. Este conjunto se denomina en el caso de los modelos de _machine Learning_ el set de entrenamiento o _training set_ . La parte restante del corpus que no hayamos empleado para entrenar nuestro modelo podremos usarlos para evaluar el modelo, empleando datos ajenos al entrenamiento de forma que el modelo se enfrente a un nuevo reto a la hora de ser evaluado. 

64 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

La métrica que se usa para evaluar los modelos de lenguaje se denomina “ _perplexity_ ” y es una medida de complejidad. Es una medida similar a la entropía. Que mide la variabilidad de nuestros datos. En concreto, en el caso de los modelos N-gram definiremos la métrica de _perplexity_ como la inversa de la probabilidad de nuestro set de evaluación. Si nuestro modelo de lenguaje otorga una probabilidad muy alta a las frases del conjunto de evaluación, querrá decir que ha comprendido correctamente las probabilidades de cada una de las palabras del lenguaje y por tanto será un buen modelo. En definitiva, es un proceso de evaluación que sigue la misma lógica que cualquier otro modelo predictivo. Si la predicción del modelo se asemeja en la mayor medida posible a la realidad del set de evaluación, este será considerado como un buen modelo. 

El único punto a destacar en el caso de los modelos de lenguaje basados en N-gram es el uso de la métrica de la perplejidad o _perplexity_ , como forma de evaluar la complejidad tanto del lenguaje como de nuestro modelo 

65 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

## **4. NLP con machine learning. Representación de palabras, semántica, distancia y relación entre palabras** 

_“Los word embeddings son, por tanto, representaciones numéricas de las palabras, generalmente en forma de un vector, que consiguen que palabras con significados similares tengan representaciones similares.”_ 

### **4.1. Vectors and Word embeddings** 

En la década de 1950 una serie de investigadores con independencia entre ellos plantearon la conocida como “hipótesis de la distribución” conocida en inglés como _distributional hypothesis_ . Esta teoría sostiene que las palabras que aparecen en contextos similares tienden a tener significados similares. O, dicho de otra forma, que las palabras que son sinónimos tienden a suceder en entornos similares, es decir, rodeadas de palabras comunes. De esta intuición podemos tratar de definir una medida de distancia entre palabras que implique medir la distancia entre sus entornos.  Medir la distancia entre palabras puede ayudarnos a comprender mejor el significado y tono de nuestros textos, así como a mejorar nuestros modelos de lenguaje como los que ya hemos visto. 

El campo del _vector semantics_ trata de estudiar el significado de las palabras mediante representaciones numéricas de las mismas, llamadas _embeddings_ , que derivan de la distribución de las palabras a lo largo de distintos textos y corpus. Esta técnica está basada en métodos de aprendizaje automático, por lo que será la primera técnica de _machine learning_ que veremos en esta asignatura. Son modelos que aprenden de forma autónoma a base de procesar una gran cantidad de textos en un determinado idioma. 

**Los** **_word embeddings_ son, por tanto, representaciones numéricas de las palabras, generalmente en forma de un vector, que consiguen que palabras con significados similares tengan representaciones similares.** 

66 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Para poder comenzar a comprender esta disciplina debemos comenzar por definir qué es el significado de una palabra. En la unidad anterior hemos visto como para un modelo N- gram una palabra es sencillamente un conjunto de caracteres que aparece en un texto con mayor o menos probabilidad antes o después de otro conjunto de caracteres (bien sea en forma de bigramas, trigramas, tetragramas…). 

Una de la forma más sencillas de apoyarnos en un sistema de aprendizaje automático para definir el significado de una palabra es basarnos en las relaciones que esta palabra puede tener con otras palabras. Podríamos analizar cómo hay determinadas palabras que se encuentran en el mismo dominio (océano, río), otras son sinónimos entre sí (médico, doctor) y otras son antónimos (frío, caliente), así como pueden tener distintas connotaciones e intenciones. Tratar de definir estas relaciones entre las palabras por medio de vectores que las representen en un espacio vectorial artificial será el objetivo que tendrá esta parte de la asignatura. 

Todas las palabras tienen una forma física, que no es más que es el conjunto de caracteres que las conforman. Por ejemplo, la palabra “ratón” es un conjunto de cinco caracteres que conforman una palabra r-a-t-o-n. Esta es su forma, conocida en la disciplina del NLP como **_word form_** . 

Por otro lado, es una palabra que puede tener varios significados, en el caso de la palabra “ratón” podemos estar hablando de un pequeño roedor, o de un dispositivo que controla el cursor en un PC. Estos distintos significados de esta _word form_ se denominan sentido de la palabra, que en inglés se conoce como **_word sense_** . Este fenómeno en el que una misma _word form_ tiene varios _word senses_ es conocido como polisemia, que se define como una palabra que posee varias acepciones correctas. 

En el extremo contrario nos encontramos con el fenómeno de los sinónimos. En este caso, tenemos una serie de diversas _word forms_ que comparten un mismo sentido, un word sense. Para considerar que dos palabras son sinónimos trataremos de probar que en caso de sustituir una por otra en cualquier tipo de frase u oración, el significado de esta no se ve alterado. 

Si bien en ningún caso esta regla se cumple completamente ya que no hay dos palabras iguales y existe siempre una connotación distinta para cada una de ellas, habitualmente consideraremos a los sinónimos como palabras con una relación muy fuerte que pueden ser intercambiadas desde un punto de vista semántico. Gracias a la representación en embeddings podremos medir numéricamente la distancia entre palabras para así descubrir la relación que hay entre ellas mediante un modelo de NLP 

Esta relación podremos medirla mediante la métrica de la **similitud,** que trata de estimar cómo de parecidas son dos palabras. Además, podemos usar la asociación o **relatedness** que estima si dos palabras pertenecen al mismo dominio, o aparecen habitualmente a la hora de hablar de ciertos temas en concreto. 

67 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Para comenzar a crear estas representaciones de las palabras que hemos llamado _embeddings_ podemos comenzar por seleccionar una serie de dimensiones de forma manual para categorizar el significado de nuestras palabras en función de estas dimensiones. Si seleccionamos una dimensión tendremos vectores unidimensionales. Por ejemplo, podemos clasificar las palabras por género, lo que implicaría tener un vector unidimensional en el que un 0 significa palabra masculina, y un 1 significa palabra femenina. Si bien este embedding no nos ayudaría a comprender la relación entre palabras, sería perfectamente válido desde un punto de vista matemático. 

Para comenzar a darle utilidad a los _embeddings_ podemos definir una dimensión que indique el tono de la palabra (positivo-negativo) y otra dimensión que indique lo concreta o abstracta que es una palabra (abstracta-concreta). Esto nos daría un espacio vectorial de dos dimensiones, aumentando la cantidad de información que se almacena en cada uno de los _embeddings_ que hemos empleado para definir nuestras palabras. Si empleáramos este sistema de dimensiones, podríamos clasificar una palabra como “parque de atracciones” en un valor muy alto tanto de positivismo como de concreción (5.00, 4.00), y una palabra como “silla” en un valor neutro de positivismo, pero en uno aún más alto de concreción (0.00, 5.00). 

Una vez tuviéramos dos palabras o más convertidas a este vector podríamos analizar la similitud entre cualquier par de palabras de nuestro vocabulario estimando la distancia entre los dos vectores que las conforman. De esta forma, podríamos intuir que las palabras “triste” y “enfadado” son palabras similares, ya que tendrían una puntuación muy baja tanto en positivismo (son palabras con una connotación negativa) como en concreción (las dos son palabras muy abstractas). 

Este sistema nos ayudaría a codificar y comparar el significado de cualquier palabra, pero exigiría realizar este proceso que estamos haciendo para todas y cada una de las palabras del diccionario. Además, estas dos dimensiones no reflejan la realidad de todos significados y connotaciones que puede tener una palabra, por lo que sería un modelo muy limitado. Nos obstante, nos ha ayudado a comprender el proceso para generar word embeddings. Recordemos no obstante que el objetivo es definir un método de aprendizaje automático que decida cuáles serán las dimensiones y por tanto el espacio vectorial en el que clasificaremos las palabras y que nunca lo haremos de forma manual, siendo estos ejemplos un mero recurso para realizar un acercamiento intuitivo al concepto de los vectores como representaciones de las palabras. 

En el proceso de generación de un universo de representaciones numéricas de palabras, o word embeddings, mediante un método de aprendizaje automático, siempre necesitaremos un **corpus** (como en cualquier tarea de NLP) y un **método de embedding** . Este método de embedding en nuestro caso ha sido asignar manualmente dos dimensiones a las palabras, pero veremos a continuación que existen numerosos métodos para conseguir una representación vectorial de todas las palabras de nuestro corpus asociada al significado y a la similitud entre las palabras del corpus. Analicemos cada uno de estos componentes por separado a continuación. 

68 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

El **corpus** puede ser un corpus genérico en el que tratemos de conocer los significados de todas las palabras de un idioma. Este tipo de corpus suelen proceder de grandes cantidades de libros y artículos e incluso de la descarga masiva de páginas web. De este tipo de corpus genérico obtendremos un conocimiento en conjunto de un idioma, sin sesgos por dominio de negocio. Por otro lado, podemos necesitar corpus especializados en caso de que estemos frente a un caso de NLP centrado en un dominio de negocio específico, para lo que trataremos de recopilar documentos técnicos, publicaciones científicas y especificaciones técnicas que permitan a nuestro modelo descubrir espacios vectoriales específicos para este dominio de negocio, así como categorizar adecuadamente las palabras del mismo. 

El **método de embedding** será un modelo de _Machine Learning_ que tratará de descubrir el mejor espacio vectorial para representar el significado de las palabras de nuestro conjunto de textos de entrenamiento. Este método tendrá una serie de parámetros que analizaremos más adelante como puede ser el tamaño del espacio vectorial o el tipo de aprendizaje. Vamos a estudiar dos métodos de word embedding principales, el **tf-idf** y el **word2vec con CBOW** , y analizaremos sus diferencias, fortalezas y debilidades. Hay métodos muy complejos de word-embedding como BERT (Google) y GPT (OpenAI) que están basados en _deep learning_ que dejaremos fuera del alcance de esta parte de la asignatura por ahora. 

### **4.1.1. Matriz de co-ocurrencia: co-ocurrence matrix** 

La gran mayoría de métodos de embedding están basados en el análisis de una matriz que denominaremos la matriz de co-ocurrencia, que trata de representar cómo las palabras tienden a aparecer juntas y en los mismos contextos dentro de un corpus. Hay dos matrices principales: la matriz de término-documento y la matriz término-término. 

#### **La matriz término-documento** 

En una matriz término-documento cada fila representa una palabra de nuestro vocabulario y cada columna representa un documento del corpus. En cada celda veremos la cantidad de veces que una palabra aparece en cada uno de los documentos. Podemos ver un ejemplo de una matriz término-documento, denominada en inglés _term-document_ a continuación. Imaginemos que tenemos un corpus compuesto por cuatro documentos – lo que sería un corpus demasiado reducido a efectos de aprendizaje automático, pero es suficiente para el objetivo didáctico del ejemplo – y que deseamos comprender las relaciones entre cuatro palabras en español: lucha, amor, bien y árbol. 

Para construir la matriz término-documento contaremos cuántas veces aparece cada una de las palabras en cada uno de los documentos y obtendremos una matriz como la que sigue. 

69 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

||**Documento 1**|**Documento 2**|**Documento 3**|**Documento 4**|
|---|---|---|---|---|
|lucha|1|0|24|11|
|amor|8|17|5|7|
|bien|19|21|3|2|
|árbol|0|0|8|12|



Esta matriz nos puede ayudar de forma muy directa a realizar una extracción de información rápida desde el punto de vista de los documentos, llamada en inglés **_information retrieval_** , gracias a la cual podemos identificar documentos con temáticas similares por la similitud que tienen sus columnas dentro de esta matriz de término documento. Es decir que si analizamos la tabla por columnas podremos ver, por ejemplo, que en nuestra matriz de ejemplo los documentos 3 y 4 parecen tratar temas relacionados con batallas en entornos naturales, por lo que podríamos emplear esta información para realizar una agrupación automática de documentos en base al tipo de palabras que aparecen en los mismos y la frecuencia con las que estas aparecen. 

En un ejemplo real, por supuesto, no tendríamos únicamente 4 palabras y 4 documentos, sino que tendríamos miles de filas, una por cada palabra del vocabulario de interés, y tantas columnas como documentos formaran parte de nuestro corpus. El objetivo del **_information retrieval_** es, en definitiva, dado un documento _d_ hallar de entre todo nuestro corpus los N documentos más similares al documento _d_ dado en base a la frecuencia con la que se repiten las mismas palabras en _d_ y en el resto de documentos del corpus. 

Si en lugar de mirar las columnas nos fijamos en las filas estaremos ante nuestros primeros **word embeddings** . Podríamos asociar a cada una de las palabras como vector de representación (embedding) sus apariciones en cada uno de los documentos. 

Es decir, la palabra árbol tendría un vector asociado [0,0,8,12]. De igual forma que documentos similares suelen compartir palabras, podemos afirmar que palabras similares aparecen en los mismos documentos. Por tanto, la matriz término-documento nos permite definir las palabras por su ocurrencia en cada uno de los documentos de nuestro corpus. 

Para que este método sea fiable y devuelva los resultados que esperamos, será necesario que contemos con un corpus suficientemente extenso y variado como para que la gran  mayoría de palabras de nuestro vocabulario estén suficientemente representadas a lo largo de los documentos del corpus. Si esto se cumple, tendremos una primera aproximación a la similitud entre palabras basada en su aparición en el mismo conjunto de documentos que otras palabras del vocabulario. 

70 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

#### **La matriz término-término** 

Esta matriz, también llamada matriz palabra-palabra o término-contexto es una matriz en la que tanto las filas como las columnas representan las diferentes palabras de nuestro vocabulario. En este caso cada celda representa el número de veces que la palabra de la fila ocurre en el mismo contexto que la palabra representada en la columna. 

Lo primero que deberemos hacer será definir qué es contexto. El contexto puede ser que dos palabras aparezcan en un mismo documento completo, en una misma frase completa o, lo que es más habitual, en una ventana en torno a la palabra. 

En el caso de la ventana, podemos considerar una coocurrencia si dos palabras aparecen en una ventana de un número determinado de palabras hacia delante y hacia detrás de la palabra que estamos analizando. Habitualmente esta ventana de coocurrencia se encuentra en el entorno de las 3, 4 o 5 palabras hacia delante y hacia detrás. 

En el siguiente ejemplo podemos ver una tabla de término-término que ha sido computada a través de un gran corpus extraído de Wikipedia para una serie de palabras muy concretas que nos puede ayudar a comprender la utilidad de esta matriz. 

||**tiburón**|**…**|**computador**|**dato**|**resultado**|**tarta**|**azúcar**|**…**|
|---|---|---|---|---|---|---|---|---|
|**cereza**|0|…|2|8|9|442|25|…|
|**fresa**|0|…|0|0|1|60|19|…|
|**digital**|0|…|1670|1683|85|5|4|…|
|**información**|0|…|3325|3982|378|5|13|…|



Como podemos observar, según la matriz término-término que hemos mostrado, las palabras cereza y fresa son palabras muy similares, mientras que las palabras digital e información son muy similares. No obstante, entre estas dos parejas de palabras hay una gran diferencia respecto al vector que las define. 

Uno de los principales problemas que nos encontraremos será que la gran mayoría de estos vectores serán muy dispersos, es decir, con una gran cantidad de palabras sucederá lo mismo que sucede con la palabra “tiburón”, no hará coocurrencia y el valor de la grandísima mayoría de las celdas será 0. Veremos más adelante métodos para reducir el tamaño de nuestros vectores y evitar almacenar tantos valores vacíos, que disminuyen notablemente la eficiencia de nuestros algoritmos de aprendizaje y el espacio requerido para almacenar esta matriz. 

71 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **4.1.2. Medición de distancia entre palabras: La distancia del coseno** 

Para poder medir la similitud entre dos palabras v y w necesitamos de algún tipo de métrica que, dados dos vectores de palabras ( _embeddings_ ) podamos computar una métrica de distancia entre ellas dadas todas sus dimensiones en un espacio vectorial obtenido por un determinado método de embedding. 

Actualmente el método más usado por excelencia en el campo del NLP es un algoritmo conocido como la distancia del coseno ( _cosine distance en inglés_ ) que mide el coseno del ángulo que forman ambos vectores entre sí. 

La medición del coseno está basada en el conocido como **_dot product_** o producto escalar, que es un operador del álgebra lineal para vectores. Si definición es sencilla: 

Dados dos vectores 

v=(v1, v2, v3, ..., vn) y w=(w1, w2, w3, …, wn) 

Su producto escalar es el resultado de la operación 

v·w = v1·w1 + v2·w2 + v3·w3 + … + vn·wn 

Es decir, la suma del producto individual de cada uno de los componentes en cada una de las dimensiones del espacio vectorial. Gracias a esta operación podemos obtener un único valor como el resultado del producto de dos vectores sea cual sea el número de dimensiones que estos tienen y por tanto independientemente del espacio vectorial en el que nuestro método de embedding haya terminado clasificando nuestras palabras. 

Debido a la propia definición de la operación, el producto escalar tiende a ser un número mayor cuando los dos vectores tienen valores altos en la misma dirección y valores bajos en la misma dirección dado que multiplicamos los componentes de la misma dimensión dos a dos. Sin embargo, el mayor problema de usar únicamente el producto escalara como una métrica de distancia es que es una métrica que favorece a los vectores largos, ya que cuantos más valores que no son 0, mayor acabará siendo el resultado del producto escalar. 

En nuestro caso de uso de NLP esto se traduce como que las palabras que son más frecuentes y que coocurren con más palabras como pueden ser artículos, preposiciones, determinantes… Serán palabras con vectores menos dispersos (habrá menos celdas a 0 en su matriz de coocurrencia) y por tanto darán altos valores de similitud con una gran cantidad de palabras sencillamente porque son palabras muy frecuentes en un idioma. 

Para tartar de solucionar esto se introduce la medida de longitud de un vector en la medida de la distancia del coseno, que veremos completa a continuación. 

72 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

La medición de la longitud de un vector se define como la raíz cuadrada de la suma de los cuadrados de todos los componentes de un vector. Esto se denomina módulo de un vector y matemáticamente se expresa de la siguiente manera. Veremos todos estos conceptos con un ejemplo concreto para terminar de asentarlos. 



Si dividimos el resultado del producto escalar por la multiplicación entre las longitudes de nuestras dos palabras estaremos normalizando el resultado del producto escalar, y por tanto seremos capaces de obtener una métrica de similitud independiente de la longitud de cada vector y por tanto de la frecuencia con la que cada palabra aparece en un corpus. La división del producto escalar de dos vectores entre la multiplicación de sus longitudes es específicamente el coseno del ángulo que conforman y es por esto que esta métrica de similitud se denomina distancia del coseno. 

A continuación, vemos la formulación de la distancia del coseno entre dos vectores que representan dos palabras v y w en un espacio vectorial dado por un método de embedding para conocer la similitud entre palabras de una forma automática y objetiva. 



Apliquemos la distancia del coseno a un ejemplo concreto para comprender definitivamente el funcionamiento de una de las métricas más importantes en el NLP en la actualidad. 

Dada una matriz de ocurrencia como la siguiente trataremos de calcular la distancia del coseno entre sus palabras para encontrar aquellas que son más similares entre sí. 

||**tarta**|**datos**|**ordenador**|
|---|---|---|---|
|**cereza**|442|8|2|
|**digital**|5|1683|1670|
|**información**|5|3982|3325|



73 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Esto nos dejaría con los siguientes embeddings si optáramos por aplicar directamente la matriz de coocurrencia para construir los embeddings. Veremos a continuación métodos de embedding para extraer vectores no dispersos, pero dado que nuestra tabla de ejemplo contiene solo tres dimensiones extraeremos estos vectores directamente. 

cereza = (442, 8, 2) 

digital = (5, 1683, 1670) 

información = (5, 3982, 3325) 

Calculemos la distancia del coseno entre ambos pares de palabras para analizar los resultados 



Como podemos observar, dada nuestra matriz de coocurrencia, los embeddings que hemos generado a partir de ella y el cálculo de la distancia del coseno podemos afirmar que las palabras digital e información son mucho más similares entre ellas que con la palabra cereza, con la que comparten muy poco. 

A continuación, vamos a estudiar dos métodos de generación de embeddings más complejos y elaborados de lo que han sido hasta ahora tanto el primer método manual en el que las dimensiones las hemos elegido de forma arbitraria, como este segundo en el que la representación vectorial de la palabra es directamente el resultado de su matriz de coocurrencia, que recordemos que genera vectores demasiado dispersos en casos de uso reales como para obtener algoritmos suficientemente eficientes. 

74 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **4.1.3. TF – IDF: Term Frequency – Inverse Document Frequency y PPMI** 

Tf-idf es un método de jerarquización de palabras que se basa en la frecuencia de cada término y en la frecuencia inversa de cada documento. Hemos visto cómo emplear la matriz de coocurrencia puede llevarnos a vectores realmente dispersos, pero este no es el único problema que plantea este método. Si empleamos únicamente la matriz de coocurrencia tendremos palabras con una gran cantidad de similitud con cualquier otra palabra, como pueden ser “un”, “el”, “con”, “de”… Lo que podría comprometer la precisión y utilidad de nuestro modelo. Tenemos por un lado la realidad de que las palabras que se repiten juntas con frecuencia son posiblemente palabras con un significado y realidad similares, pero sin embargo aquellas que se repiten “demasiado” pueden llegar a estropear el modelo. Esto es una paradoja que solo puede solucionarse tratando de encontrar un equilibrio entre ambas realidades. Es decir, jerarquizando las palabras para así poder descubrir cuáles de ellas son realmente relevantes y cuales de ellas son sencillamente palabras muy frecuentes en un corpus o en un idioma y que no deberemos usar para definir el significado semántico de nuestras palabras ni para calcular distancias entre distintas palabras. 

Existen dos algoritmos centrados en encontrar este equilibrio, en función de si la búsqueda que realizamos se basa en documentos o si se basa en palabras. Es decir, en función de si buscamos la relevancia de una palabra dentro de un documento dentro del objetivo de infromation retrieval y minería de textos, o si únicamente deseamos conocer la similitud entre dos palabras. Para el primer caso analizaremos y emplearemos el algoritmo TF-IDF y para el segundo el algoritmo PPMI, que veremos más tarde. 

TF-IDF está formado por dos intuiciones que componen su nombre: 

1. **Term Frequency** (frecuencia de término): La frecuencia de un término t en un documento _d_ es el número de veces que aparece en un documento. Para el algoritmo TF-IDF esta frecuencia se modula aplicando un logaritmo de base 10 a la frecuencia total y habitualmente se suma 1 para evitar tratar de calcular logaritmos de cero. En resumen, el término TF de nuestro algoritmo será, para un término _t_ en un documento _d_ , como sigue: 



75 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

2. **Inverse Document Frequency** o la frecuencia inversa del documento es el segundo término, que emplearemos para darle más peso a las palabras que aparecen con menor frecuencia en los documentos. Los términos que aparecen en pocos documentos son útiles para distinguir dichos documentos del conjunto de la colección, ya que son los aspectos diferenciales de los mismos. Por tanto, son términos más útiles que las palabras que, por ejemplo, se repiten a lo largo de todos los documentos que  componen un corpus. La frecuencia de documento de un término _t_ es sencillamente el número de documentos en los que aparece dicho término. Si un término aparece en tres documentos, su frecuencia de documento será 3. Para darle más valor a un término cuanto menor sea su frecuencia de documento recurrimos a la frecuencia inversa de documento. 

La primera intuición del inverse document frequency pasa por dividir el número total de documentos de nuestro corpus, que podemos llamar _N,_ entre la frecuencia de documento de nuestro término. Si en un corpus de 5600 documentos una palabra aparece tan solo en 6 de ellos, podríamos intuir que la inversa de la frecuencia de documento de dicha palabra será 5600/6. De esta forma, cuantas más veces aparezca una palabra en un corpus menor será el resultado de esta operación dado que el denominador crecerá, y conseguiremos nuestro objetivo de darle más valor a las palabras con menos frecuencia de documento. 

Para limitar los valores de esta función de nuevo se usa un logaritmo en base 10 de forma que podamos tener todos los valores acotados y bajo control. En definitiva, el cálculo de la frecuencia inversa de documento viene explicado por la siguiente fórmula para un término t en un corpus compuesto por _N_ documentos. 



Vamos a ver a efectos de ejemplificación los cálculos de la frecuencia de documento y la frecuencia inversa de documento de una serie de palabras en la obra de Shakespeare para comprender la gran relevancia que tiene la frecuencia inversa de documento. 

76 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

|**Palabra**|**df**|**idf**|
|---|---|---|
|Romeo|1|1.57|
|salad|2|1.27|
|Falstaff|4|0.967|
|forest|12|0.489|
|battle|21|0.246|
|wit|34|0.037|
|fool|36|0.012|
|good|37|0|
|sweet|37|0|



Como podemos ver, hay palabras que aparecen en todos los documentos de Shakespeare como pueden ser “good”, “fool” y “sweet” y que por tanto tienen un valor de idf de 0 ya que aparecen en prácticamente todas las obras de Shakespeare. Sin embargo, palabras como “Romeo” o “Falstaff” aparecen en una menor cantidad de obras por lo que su importancia específica para definir dichas obras es muy alta y por tanto el resultado del cálculo de idf es un valor más elevado. 

Con las dos métricas que hemos definido (tf e idf) podemos calcular un valor conjunto que categorice nuestras palabras, que es TF IDF. En definitiva, el cálculo de tf idf consiste en multiplicar ambos términos y almacenar el valor resultado. Dado un corpus de documentos _D_ , un documento específico _d_ y una palabra _w_ , la relevancia de la palabra w para definir y caracterizar el documento d se puede calcular como sigue: 



Cuanto mayor sea el valor de TF-IDF más relevante será la palabra para el documento d y por tanto podremos usarla para caracterizar este documento y generar información que pueda ayudar a posteriores modelos de minería de datos o de _information retrieval_ filtrando las palabras menos relevantes gracias a este equilibrio entre la frecuencia absoluta de una palabra y la rareza de dicha palabra en todo el conjunto del corpus que emplearemos para el entrenamiento de nuestros modelos. 

En cuanto a los word embeddings, TF-IDF es muy útil a la hora de generar vectores para representar palabras que nos puedan ayudar a comparar documentos. Si generar un vector para cada una de las palabras más relevantes de un documento estaremos ahorrando una gran cantidad de espacio y de tiempo de cómputo. 

77 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Emplearemos las N palabras más relevantes de un documento – es decir aquellas con una mayor puntuación en TF-IDF, y posteriormente aplicaremos la distancia del coseno entre ellas. 

Aquellos documentos que tengan un menor valor de distancia de coseno entre sus palabras más relevantes serán considerados similares y por tanto podremos agruparlos como documentos con la misma temática o que pertenecen al mismo dominio de negocio. 

El método de TF-IDF está orientado a la clasificación de palabras relevantes respecto a documentos. Si quisiéramos emplear un método para generar vectores en base a la matriz de coocurrencia o matriz de término-término tendríamos la opción de emplear el método Positive Pointwise Mutual Information o PPMI. 

El método de PPMI se basa en la intuición de que la mejor forma de medir la asociación y similitud entre dos palabras es tratar de definir cuánto **más** coocurren estas dos palabras en un corpus de lo que habríamos poder esperado a priori si fueran dos palabras al azar. 

El concepto de PMI o Pointwise Mutual Information es uno de los conceptos más importantes en NLP. Mide cómo de habitual es que dos eventos _x_ e _y_ ocurran en conjunto en comparación con lo que habríamos esperado si fueran independientes. Su definición procede de una publicación de 1961 y su definición dada una palabra objetivo _w_ y una palabra contextual _c_ mediante la siguiente fórmula matemática. 



El numerador indica cómo de probable es que observemos las dos palabras en conjunto. El denominador indica cómo de probable sería que ambas palabras sucedieran de forma independiente en el mismo suceso. En definitiva, compara la probabilidad de que ambas palabras sucedan en el mismo contexto con la probabilidad de que sucedan de forma independiente. Es una gran herramienta para tratar de definir si dos palabras tienen una asociación fuerte o no. Dado que el valor del PMI puede arrojar valores negativos y estos son difíciles de emplear para un algoritmo de NLP, se emplea la métrica de PPMI en la que todos los valores negativos se sustituyen por 0, por lo que la fórmula queda de la siguiente manera. 



Tratemos de ver esto por medio de un ejemplo para comprender cómo poner en práctica la métrica PPMI para un corpus concreto en base a una matriz de coocurrencia. 

78 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Usemos como ejemplo la siguiente tabla de término-término que ha sido computada en base a un gran corpus descargado de Wikipedia. 

||**ordenador**|**datos**|**resultado**|**tarta**|**azúcar**|**recuento (palabra)**|
|---|---|---|---|---|---|---|
|**cereza**|2|8|9|442|25|486|
|**fresa**|0|0|1|60|19|80|
|**digital**|1670|1683|85|5|4|3447|
|**información**|3325|3982|378|5|13|7703|
|**recuento**<br>**(contexto)**|4997|5673|473|512|61|11716|



Tratemos de computar el valor del Positive Pointwise Mutual Information (PPMI) para las palabras información y datos. Para ello tenemos que calcular las siguientes probabilidades 

P(información, datos) = 3982/11716 = 0,3399 

P(información) = 7703/11716 = 0,6575 

P(datos) = 5673/11716 = 0,4842 

PPMI(information, datos) = log2(0,3399/(0,6575 * 0,4842)) = 0,0944 

Realicemos la misma operación para las palabras fresa y datos 

P(fresa, datos) = 0/11716 = 0,00 

P(fresa) = 80/11716 = 0,0068 

PPMI(fresa, datos) = log2(0,00/(0,0068*0,4842)) = 0,00 

Como vemos el valor PPMI es 0 en el caso de las palabras fresa y datos, mientras que entre información y datos es notablemente mayor con un 0,0944. Esto indica que las palabras información y datos se encuentran cercanas mientras que las palabras fresa y datos no comparten ningún tipo de significado. 

Entre otros usos de la métrica de PPMI podemos ver la búsqueda de las 10 palabras más similares a una palabra dada w dentro de un corpus de entrenamiento para extrapolarlo al conjunto de un idioma posteriormente en un modelo de NLP. 

79 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **4.2. Word2Vec** 

Hemos visto hasta el momento la intuición detrás de tratar de representar palabras por medio de vectores llamados embeddings que pertenecen a un determinado espacio vectorial, así como diversas formas de analizar la distancia entre palabras en función de diversas métricas y medidas tanto para relacionar documentos entre sí como para relacionar palabras entre sí. 

En esta sección vamos a estudiar la técnica conocida como word2vec, que fue publicada en 2013 por un grupo de ingenieros de Google y es uno de los algoritmos más relevantes en NLP en la actualidad. Esta técnica emplea una red neuronal para encontrar asociaciones entre palabras en un gran corpus de texto. Una vez entrenado, un modelo de word2vec puede detectar automáticamente sinónimos en un texto, así como sugerir palabras para completar frases parciales. 

Este método de embedding genera vectores a partir de palabras, que posteriormente se pueden comparar mediante medidas como la distancia del coseno para analizar la similitud entre las palabras representadas. 

Las redes neuronales que veremos en esta sección son redes neuronales que **no son profundas** , es decir, **no estamos hablando de** **_deep learning_** ya que son redes neuronales con tan solo dos capas que están entrenadas para permitir al modelo reconstruir el contexto semántico de las palabras. Un modelo completo de word2vec recibe un gran corpus de texto y produce un espacio vectorial en el que se puede resumir cada una de las palabras del corpus para posteriores comparaciones entre ellas. Las palabras con significados similares se encontrarán próximas entre sí en este espacio vectorial creado por word2vec. 

Hay dos arquitecturas posibles para aplicar word2vec: CBOW o skip-grams. 

CBOW, llamado así por las siglas de continuous bag-of-words, es un modelo que asume que el orden de las palabras no influye en el conteto, mientras que en el caso de skipgrams sí que es algo tenido en cuenta, como veremos a continuación. Según los autores del artículo en el que se publicó word2vec, CBOW es una arquitectura más rápida mientras que skip-gram tiene una mayor precisión cuando trata con palabras menos frecuentes. En ambos casos word2vec genera vectores densos, es decir, no son vectores dispersos con muchos valores nulos, sino que tendremos vectores cuyas dimensiones estarán en su mayoría completas con números enteros positivos, mejorando así el rendimiento de métricas de similitud como puede ser la distancia del coseno o PPMI. 

80 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **4.2.1. Skip-gram with negative sampling (SGNS)** 

La primera opción para implementar word2vec es la arquitectura de SGNS, llamado habitualmente skip-gram. La intuición detrás de estos modelos de word2vec consiste en que en lugar de contar cuántas veces una palabra w aparece contextualmente cerca de otras palabras, trataremos de entrenar un modelo de _machine learning_ para clasificación – es decir, un modelo de aprendizaje supervisado – que pueda resolver la siguiente clasificación: “¿Es probable que la palabra w aparezca cerca de la palabra c?”. Las clases que devolverá el algoritmo serán SI o NO, por lo que es un algoritmo de clasificación binaria, siendo un modelo eficiente y rápido tanto de entrenar como de ejecutar. En el caso de las skip-grams no entrenaremos redes neuronales complejas, sino un método clasificador de regresión logística de _machine learning_ . Los pasos que seguiremos con este modelo de aprendizaje supervisado para cada par de palabras será el siguiente: 

1. Emplearemos la palabra objetivo (w) y la palabra contexto (c) como ejemplos positivos (respuesta SI) 

2. Emplearemos palabras aleatorias de todo nuestro corpus como ejemplos negativos (NO) 

3. Usaremos una regresión logística para entrenar un clasificador que trate de encontrar una línea que divida los ejemplos positivos y los negativos 

4. Emplearemos los pesos aprendidos por nuestro modelo de machine learning como las representaciones de nuestras palabras, nuestros embeddings. 

Imaginemos una frase como puede ser: 

“… aleación, [el motor diésel es eficiente], dadas las últimas novedades …” 

Siendo las palabras entre corchetes las palabras c1 (el), c2 (motor), c3 (es), c4(eficiente) el contexto de nuestra palabra w (diésel). El objetivo de nuestro modelo será, para un determinado par de w,c como puede ser (diésel, motor) tratar de estimar la probabilidad de que c (motor) sea una palabra de contexto real para diésel. 

Para tratar de estimar esta probabilidad un modelo de skip-gram se basa e la similitud entre los embeddings de ambas palabras. Cuanto más similares sean los embeddings de ambas palabras, más probable será que una de ellas aparezca como contexto de la otra. 

Para estimar la similitud entre los embeddings skip-gram emplea el producto escalar. Recordemos que la distancia del coseno es un producto escalar normalizado, pero en este caso solo emplearemos el producto escalar. 

El problema de emplear el producto escalar es que el rango de valores de dicha operación varía de entre - ∞ hasta + ∞ y una probabilidad debe estar entre 0 y 1. 

81 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Para solucionar este problema aplicamos una función matemática que nos permita constreñir cualquier conjunto de valores entre 0 y 1. Esta función será la misma función que hemos estudiado en asignaturas anteriores para la activación de una neurona artificial: la función logística o sigmoide. Una función logística es capaz de convertir cualquier rango de valores en un rango limitado entre 0 y 1, y si expresión matemática es la siguiente: 



Si estimamos que x es el producto escalar entre nuestra palabra original w y la palabra de contexto que deseamos estudiar c, nos quedará que la probabilidad de que la palabra c sea una palabra real de contexto para la palabra _w_ es de 



Recordemos que tanto c como w son los vectores que representan nuestras palabras, y no las palabras propiamente dichas como sucedía en los modelos más simples de N-gram. Para aplicar múltiples palabras de contexto a una única palabra objetivo (c1, c2, c3 y c4) a w skip-gram multiplica todas las probabilidades de cada una de las palabras de contexto para calcular la probabilidad final. Es decir 



La arquitectura de skip-gram almacena dos embeddings para cada palabra del vocabulario. Un embedding **W** que representa la palabra cuando es palabra objetivo y el embedding **C** , para cuando la palabra actúa como contextual. Pero, ¿cómo se calculan estos embeddings? 

#### **Algoritmo de aprendizaje de skip-gram** 

El algoritmo de aprendizaje de skip-gram parte de un corpus de texto que tiene un vocabulario de _N_ palabras. Comienza asignando un vector aleatorio a cada una de las palabras y a continuación itera a lo largo de cada palabra w para ajustar su embedding de forma que sea lo más similar posible a las palabras de las que tiende a encontrarse cerca en los textos del corpus, y sea lo más distinta posible a aquellas palabras con las que nunca coincide. 

82 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Para ello, empleará una serie de ejemplos positivos, que serán las palabras que efectivamente aparecen en el corpus en el mismo contexto que nuestra palabra objetivo. También extraerá del corpus una cantidad de ejemplos negativos, es decir, de palabras que no aparecen nunca en el mismo contexto que la palabra _w_ . La cantidad de ejemplos negativos viene definida por un parámetro _k_ que es configurable, y que indica el número de ejemplos negativos que el algoritmo extraerá por cada ejemplo positivo. 

Imaginemos la siguiente situación de entrenamiento de un algoritmo de skip-gram en el que el parámetro _k = 2_ , es decir, que por cada ejemplo positivo que encuentre el algoritmo, se generarán dos ejemplos negativos. Si empleamos nuestra frase anterior, en la que la _w = “diesel”_ , podríamos tener la siguiente tabla de ejemplos positivos y negativos: 

|**Ejemplos pos**|**itivos**|**Ejemplos ne**|**gativos**|
|---|---|---|---|
|diésel|el|diésel|manzana|
|||diésel|flor|
|diésel|motor|diésel|cuchillo|
|||diésel|entonces|
|diésel|es|diésel|donde|
|||diésel|interpolación|
|diésel|eficiente|diésel|suyos|
|||diésel|caminante|



Tenemos un total de 4 ejemplos positivos, y dado que _k=2_ tenemos 8 ejemplos negativos. Una vez tenemos esta serie de ejemplos el algoritmo de clasificación tendrá dos objetivos simultáneos que cumplir: 

1. Maximizar la similitud entre los embeddings de la palabra w y los ejemplos positivos 

2. Minimizar la similitud entre los embeddings de la palabra w y los ejemplos negativos 

O expresado en términos más formales, el objetivo es maximizar el producto escalar entre los vectores del primer conjunto mientras que se minimiza el producto escalar entre los pares de vectores que pertenecen al segundo conjunto. 

Para hacer esto se emplea un método de aprendizaje que **ya hemos estudiado previamente** en la asignatura de Visión Artificial denominado Descenso Estocástico del Gradiente, más conocido por su nombre en inglés Stochastic Gradient Descent (SGD). Recordemos que este método basado en la primera derivada trata de encontrar los puntos mínimos de un objetivo para un modelo de aprendizaje automático, que es exactamente lo que estamos tratando de hacer con nuestro modelo de skip-gram. 

83 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Gracias a SGD los embeddings aleatorios W y C van siendo modificados hasta que el algoritmo encuentra el punto mínimo en el que se optimiza el problema planteado hasta que obtenemos dos matrices definitivas para cada palabra objetivo _w_ y contexto _c_ . 

Un aspecto importante de skip-gram, además del parámetro _k_ , es el parámetro _L_ con el que controlamos la ventana de nuestro contexto. Como es de esperar, cuanto más grande sea _L_ , más palabras formarán ejemplos positivos para cada palabra, y encontraremos distintas representaciones para ellas en función de variaciones de este parámetro, con el que el desarrollador deberá experimentar hasta obtener el mejor modelo de embedding posible dado un problema concreto. 

En definitiva, skip-gram es una de las dos posibles arquitecturas con las que podemos hacer funcionar el algoritmo Word2Vec destinado a la generación de vectores que representen palabras en un corpus. Es un modelo basado en una regresión logística que aprende gracias al Stochastic Gradient Descent y que en esencia trata de maximizar el producto escalar entre los vectores de palabras que comparten contextos y que trata de minimizar el producto escalar entre los vectores de aquellas palabras que jamás comparten contexto. Esta aproximación es similar a la que podría derivarse de un algoritmo que trate de minimizar la distancia del coseno, que hemos visto anteriormente en esta unidad. 

Es posible que veamos referencias al método de skip-gram como un método basado en redes neuronales – nunca en _deep Learning_ – de aprendizaje semi-supervisado. Esto puede ser comprendido así si consideramos la función sigmoide o logística como la función de activación de una neurona, que devolverá sus pesos tras el entrenamiento como el embedding de cada una de las palabras. 

### **4.2.2. Continuous Bag Of Words (CBOW)** 

El proceso de CBOW para generar embeddings de las palabras de nuestro corpus puede explicarse de forma intuitiva de la siguiente manera. 

En este caso, el objetivo de CBOW será predecir una palabra central dada una serie de palabras de contexto. A diferencia de skip-gram, no conoceremos la palabra w y el objetivo del modelo será, dadas unas palabras de contexto _c1, c2, c3, c4_ , predecir la palabra que falta, es decir, _w_ . 

Por ejemplo, dada la frase “el pequeño ______ está ladrando”, si nuestro modelo tuviera suficiente muestra dentro del corpus, sería capaz de saber rellenar el vacío en la frase con la palabra “perro”, o “cachorro”, “terrier”… 

84 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Para generar datos que nos permitan entrenar nuestro modelo partiremos de un corpus que procesaremos de la siguiente manera. Para cada palabra de nuestro corpus almacenaremos todas sus palabras de contexto unidas, a diferencia de skip-gram que tomábamos una serie de ejemplos positivos aleatorios. El número de palabras que usemos vendrá definido por el parámetro _C_ , llamado _context halg-size_ , que hace referencia al número de palabras que tomamos antes y después de _w_ . Si C=3 tomaremos un total de 6 palabras que serán las 3 previas a _w_ y las 3 posteriores. 

Llamaremos ventana o _window_ al total de la suma de las palabras de contexto y de la palabra central, por lo que en el caso de C=3 tendremos una ventana de 3+1+3 = 7. 

Para entrenar nuestro modelo acabaremos teniendo una matriz como la siguiente, que se convertirá en nuestro training set. 

Pongamos que tenemos la frase “son las vías más seguras ya que entre otras razones no hay riesgos de colisión frontal”. Para generar la matriz de training set con esta frase debemos primero definir el valor de C. Pongamos un C=2 y por tanto una window=5. Para cada fila de la matriz iremos deslizando la ventana de 5 posiciones una posición a la derecha, hasta cubrir el total de la frase. De cada aplicación de la ventana, extraeremos la palabra frontal como etiqueta, es decir, como el resultado que debe dar nuestro modelo de CBOW una vez entrenado y contra el que calcularemos el error del entrenamiento. 

El resto de las palabras serán palabras de contexto, dos por delante y dos por detrás de nuestra palabra central. Nos quedaría por tanto una matriz similar a la siguiente: 

|**Palabras de contexto**|**Palabra central**|
|---|---|
|son, las, más, seguras|vías|
|las, vías, seguras, ya|más|
|vías, más, ya, que|seguras|
|más, seguras, que, entre|ya|
|seguras, ya, entre, otras|que|
|ya, que, otras, razones<br>…|entre<br>…|



Este funcionamiento viene definido en el paper de publicación de este modelo en 2013, recordemos que, de la mano de Google, mediante el siguiente diagrama. En la primera columna tenemos los inputs, que son las palabras de contexto a la izquierda de nuestra tabla. En el centro tenemos el procesado o “proyección”, que es el pequeño tramo formado por neuronas artificiales que aplicaremos en CBOW. Por último, tenemos la salida, el “output”, que consiste en la palabra central. 

85 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Las palabras de contexto se denominan w(t-2) y w(t-1) para las palabras que preceden a la central y w(t+1) y w(t+2) para las palabras que suceden a la central. Por último, la palabra central es denominada w(t). 

En definitiva, en un modelo CBOW trataremos de predecir la palabra central de una frase dadas una serie de palabras de contexto conocidas que vendrán definidas por un parámetro configurable llamado C. 

Para generar el training set, o set de entrenamiento, procesaremos un gran corpus con frases en el idioma deseado para generar un conjunto de inputs a nuestro modelo (las palabras de contexto) y un conjunto de etiquetas o valores de salida esperados (las palabras centrales) que serán las que nos permitirán entrenar el modelo, como veremos más adelante. 



En este punto, podemos volver por un momento al primer preprocesamiento del texto que analizamos en la primera unidad, la tokenización. Este preprocesado será el que automáticamente identifique las palabras de nuestro corpus y nos permita generar el set de entrenamiento de forma automática. 

86 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Para tokenizar nuestro corpus y extraer las palabras más significativas, deberemos tomar una serie de decisiones acerca de la tokenización que son importantes. Principalmente serán las siguientes: 

- Mayúsculas/minúsculas. Se recomienda convertir todas las palabras bien a mayúsculas o bien a minúsculas para que nuestro modelo no identifique diferente a una palabra si empieza una frase o si no. La decisión es poco relevante pero deberemos pensar si deseamos todos nuestros tokens en mayúsculas ( _upper case_ ) o en minúsculas ( _lower case_ ). 

- Puntuación. En este caso podemos optar por convertir todos los signos de puntuación a un mismo token, mantener su significado original o directamente eliminarlos. Habitualmente los signos de puntuación se eliminan, ya que no suelen cambiar el significado de las palabras de forma individual sino de las frases en sentido completo por lo que no cambiará la relación de una palabra con las palabras de su contexto. 

- Números. Dependiendo de si los números son relevantes para nuestro caso de uso o no, decidiremos si eliminar todos los números, si reemplazar todos los números por un token específico para números, o si mantenerlos íntegros. 

- Caracteres especiales. En este caso habitualmente se eliminan todos los caracteres especiales. 

- Palabras especiales. Las palabras especiales pueden ser emoticonos, hashtags, páginas web, URLS… Ya hemos hablado sobre esto en la sección de tokenización por lo que no profundizaremos en este aspecto. 

Lo importante en este caso es recordar que la política de tokenización que empleemos para procesar nuestro corpus, generar el training set y, en última instancia, entrenar el algoritmo de CBOW afectarán a sus resultados y al potencial que puede llegar a alcanzar, por lo que nunca deberíamos conformarnos con una sola política de tokenización y deberíamos buscar aquella que fuera más efectiva para nuestro caso de uso o problema concreto de NLP. 

Una vez tokenizado nuestro texto, vamos a tratar de extraer estas palabras del mismo. Vamos a ver un ejemplo en Python de cómo podemos extraer las palabras de contexto y centrales para un corpus de ejemplo, lo que sería extrapolable a un corpus completo de texto. 

87 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Supongamos que tenemos un corpus ya tokenizado, en el que todas las frases han sido procesadas y se encuentran en una lista de strings que representan nuestros tokens. 

Volvamos a la frase “son las vías más seguras ya que entre otras razones no hay riesgos de colisión frontal”. Tras un proceso de tokenizado (podemos emplear el código de ejemplos anteriores si deseamos comprobarlo) esta frase sería una lista en Python como la siguiente 

[“son”, “las”, “vías”, “más”, “seguras”, “ya”, “que”, “entre”, “otras”, “razones”, “no”, “hay”, “riesgos”, “de”, “colisión”, “frontal”] 

Vamos a necesitar una variable C, que para mantener la consistencia tendrá un valor de 2. Una vez conocido C tendremos que iterar a lo largo de la lista extrayendo siempre una palabra central y dos palabras de contexto de la misma. 

Como siempre querremos mirar hacia atrás 2 posiciones, no podremos empezar por la palabra inicial, sino por aquella que está en la posición C, de tal forma que siempre haya palabras por detrás. De igual forma, no podremos procesar todas las palabras, sino que tendremos que parar en la palabra que deje C palabras al final de la lista, para siempre tener suficientes palabras de contexto. 

Iteraremos por la lista de palabras extrayendo una palabra y sus dos predecesoras y antecesoras, y las escribiremos por pantalla para observar nuestro set de entrenamiento. Vamos primero a definir el método de extracción de datos y posteriormente lo probaremos con nuestra frase. 

88 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Creamos un nuevo cuaderno de Google Colab e introducimos el siguiente código que ejecuta las instrucciones que acabamos de comentar, y además incorpora comentarios para una mejor comprensión. 



En esta celda de código lo único que hemos hecho ha sido definir un método. Este método podrá ser llamado posteriormente desde cualquier otra celda, pero por ahora no producirá ningún resultado visible en nuestro cuaderno. No obstante, es esencial ejecutarlo para poder continuar con el ejemplo. 

Ahora, crearemos una variable en la que se encuentren almacenados todos los tokens de nuestra frase y seleccionaremos un valor para C. Recordemos que vamos a emplear el valor C de 2 para mantener la coherencia con el ejemplo manual que hemos mostrado anteriormente. Sin embargo, se anima al alumno a probar distintas frases **ya tokenizadas** y distintos valores para C de forma que pueda observar los diferentes resultados que se pueden obtener preparando los datos para entrenar un modelo de CBOW. 

89 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Creamos ahora una nueva celda de código en la que introducimos el siguiente fragmento y lo ejecutamos. 



Una vez ejecutado veremos por teminal una salida similar a la siguiente. En cada salida vemos la palabra central y debajo de la misma todas las palabras de contexto que ha extraído nuestro método para buscar palabras centrales y de contexto. Con este método podríamos generar un dataset para entrenar un modelo CBOW a partir de cualquier corpus ya tokenizado. 



90 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Una vez tenemos las palabras preparadas para entrenar nuestro modelo tenemos que dar un último paso esencial para que este pueda procesar las palabras. Actualmente nuestras palabras o tokens son strings, conjuntos de caracteres. Las redes neuronales actúan sobre vectores numéricos, por lo que tenemos que definir un método para transformar nuestras palabras en vectores. 

Primero transformaremos las palabras centrales en vectores. El primer paso será generar un vocabulario de nuestro corpus, que recordemos que no es más que la lista de todas las palabras diferentes que existen en nuestro corpus, tal y como vimos en la primera unidad. Una opción es transformar nuestras palabras en vectores one-hot. 

Un vector one-hot no es más que un vector en el que todos los números son 0 excepto uno de ellos, que es un 1. 

Si tuviéramos un vocabulario de cuatro palabras: vaca, pato, caballo, gato; su codificación en one-hot sería la siguiente 

vaca: 1000 

pato: 0100 

caballo: 0010 

gato: 0001 

Esto implica que nuestros vectores de palabras centrales (W) tendrán tantas posiciones como palabras existen en nuestro vocabulario. 

Recordemos que cada palabra tendrá dos vectores. Por un lado, W y por otro lado C. Para transformar las palabras de contexto en vectores emplearemos la media de todos los vectores one-hot individuales gracias al paso anterior. Es decir, sumaremos los vectores de sus N palabras de contexto y los dividiremos entre N. Esto implica que los vectores de contexto representan cuántas veces aparece cada una de las palabras de contexto próximas a la misma, por lo que cuanto más alto sea el valor en una posición, más cercana será la palabra de contexto correspondiente en el vector one-hot. 

Una vez tenemos nuestro corpus tokenizado, extraídas las palabras centrales y de contexto y convertidos ambos conjuntos de palabras a vectores procesables por una red neuronal, es el momento de tratar con redes neuronales poco profundas para definir nuestro modelo. 

91 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

El modelo de CBOW está compuesto por una capa de entrada a la red neuronal que denominaremos “input layer”. Esta capa recibirá los vectores de las palabras de contexto, que denominaremos X. La salida de nuestra red neuronal será la capa llamada “output layer”. Esta capa devolverá la palabra central predicha. Para ello, devolverá un one-hot vector en el que el resultado será un vector de 0s y un 1 en el caso de la palabra detectada. Esto implica que el tamaño de nuestro vector de salida será del número total de palabras que tenga nuestro vocabulario. 

La capa que hace todo el trabajo de nuestro modelo es la capa intermedia, llamada capa oculta o “Hidden layer”. Tendremos entre cientos y miles de neuronas. Podremos decidir el número de neuronas que deseamos que tenga nuestra capa intermedia, y es aquí cuando CBOW comienza a cobrar sentido. 

Recordemos que CBOW es un método de embedding, es decir, el objetivo definitivo es ser capaces de convertir todo el vocabulario de un corpus en una serie de vectores que sean lo más similares posibles cuanto más similares sean los significados de las palabras. Para ello emplearemos los pesos aprendidos por nuestra red neuronal. Es decir, el objetivo de predecir la palabra central de una frase es tan solo una “excusa” para poder enseñar a nuestro modelo a representar las palabras en un único embedding. Esta representación estará almacenada en los pesos de nuestras neuronas. 

El tamaño de N, es decir, el número de neuronas que decidamos que tenga nuestra capa intermedia, será el tamaño de los embeddings que devolverá nuestro modelo para las palabras de nuestro corpus y vocabulario. 

CBOW es una red neuronal de alimentación hacia delante, o _Fast Forward Feed Neural Network_ , cuya estructura vimos en la asignatura de Introducción a la IA. Estas redes neuronales poco profundas ( _shallow_ en inglés) están totalmente conectadas, igual que las últimas capas de las Redes Neuronales Convolucionales (CNN), es decir, todas las neuronas de una capa se conectan con todas las neuronas de la capa siguiente, lo que en inglés se denomina _dense connected  o fully connected network_ . 

Recordemos que las neuronas artificiales tienen una serie de entradas que se ponderan por medio de una serie de pesos. Las entradas ponderadas se suman a esta suma se le aplica una **función de activación** Esta función será la que genere el valor de salida de la neurona, que viajará entonces a todas las neuronas de la siguiente capa en caso de haberla. 

En este caso usaremos para nuestras neuronas de la capa de entrada la función conocida como Rectified Linear Unit Function, también llamada ReLU, una de las funciones de activación más significativas en el campo de las redes neuronales. 

Por otra parte, para la capa intermedia o “hidden layer” emplearemos la función softmax, que veremos a continuación. 

92 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



#### **Rectified Linear Unit (ReLu)** 

La función unitaria de rectificación lineal se aplica sobre el cómputo de la suma de todas las entradas de la neurona por todos sus pesos, como sucede en todas las neuronas artificiales. En este caso, las entradas serán cada una de las dimensiones de los vectores de entrada, que serán los vectores C de contexto. Recordemos que estos vectores tendrán la misma longitud que palabras tiene nuestro vocabulario, por lo que nuestras neuronas en la capa oculta ( _Hidden layer)_ tendrán tantas entradas como palabras tiene nuestro vocabulario y por tanto el mismo número de pesos. 

Llamemos C a todas las dimensiones de nuestros vectores, y W a todos los pesos de nuestras neuronas. Siendo así, el primer paso que realizará cada una de las neuronas será multiplicar cada dimensión del vector (c1, c2, c3, …, cN) por cada uno de los pesos correspondientes a sus entradas (w1, w2, w3, …, wn), y sumar todos estos valores. 

Además, las neuronas incorporan un sesgo, denominado _bias_ en inglés, que añade una cierta cantidad a la suma total, y que representaremos por b. 

Por tanto, el primer paso que realiza una neurona es 

Z = W * C + b 

La salida definitiva de la neurona, un número, vendrá determinada por la aplicación de su función de activación sobre Z. En el caso de las neuronas de la capa oculta de un modelo de CBOW, emplearemos la función ReLU. Por tanto, la salida definitiva de una de nuestras neuronas artificiales será la siguiente. 

output = ReLU(Z) 

93 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Trataremos a continuación de comprender la función ReLU, una de las funciones más relevantes no solo en el campo del NLP sino del campo de la Inteligencia Artificial en su conjunto. 

La función ReLU solo activa la neurona cuando Z es un número positivo. En caso de serlo, hace llegar este número a la siguiente neurona. Matemáticamente esto es 

#### ReLU(Z) = max(0, Z) 

En la siguiente imagen podemos visualizar el comportamiento de la función ReLU, que pondremos a prueba en un ejemplo más adelante. Como podemos ver, cualquier número de entrada (X) a la función que sea menor que cero es automáticamente convertido a 0, por lo que toda la parte izquierda de la gráfica es una línea constante en 0. 

A partir de este punto, todo número de entrada (X) que sea mayor que 0 se mantiene intacto, siendo por tanto una función y=x cuando x>0. Esta función nos ayuda a evitar valores negativos mientras que mantiene la linealidad de nuestras funciones en números positivos. 



#### **Softmax** 

En el caso de las neuronas de la capa de salida ( _output layer_ ) nos encontramos con el mismo funcionamiento básico. Cada una de las neuronas multiplica las entradas por sus pesos, añade un _bias_ y posteriormente aplica la función de activación. 

Las neuronas de la capa de salida emplean una función conocida como softmax para generar su salida definitiva. La salida de la función softmax devuelve un vector de números comprendidos entre 0 y 1 que suman 1 en total, por lo que habitualmente se toman como las probabilidades de diversos eventos independientes – ya que la suma de todas ellas es 1 – como en este caso. 

94 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

En concreto en CBOW cada una de las salidas de la función softmax representa la probabilidad de que cada una de las palabras que representa cada dimensión sean la palabra w que estamos buscando a partir de las palabras de contexto. 

La expresión matemática de softmax es más compleja e incluye aplicar la función exponencial de base e a cada uno de los elementos del vector Z de entrada. La expresión matemática es la siguiente, aunque no es necesario que la comprendamos inmediatamente ya que vamos a ver un ejemplo de su aplicación a continuación. 



Es decir, que para calcular cada uno de los componentes de nuestro vector softmax de salida tomaremos cada uno de los componentes de entrada y calcularemos la exponencial del componente, elevando el número e a dicho componente. 

Dividiremos el resultado entre la suma del número e elevado a cada uno de los componentes del vector, y este será el resultado del cálculo de softmax para esta posición. 

En la siguiente gráfica podemos comprobar cómo se aplica la función exponencial a cada uno de los componentes de nuestro vector. La función exponencial (e^x) devuelve valores notablemente más grandes para cada incremento de números enteros, por lo que ponderará notablemente más aquellos valores en nuestros vectores más distantes de 0, con un crecimiento exponencial frente al crecimiento lineal de la función ReLU. 



Veámoslo en un ejemplo en el que calcularemos tanto la función ReLU de la entrada de una neurona como la función softmax de entrada a una neurona de la capa de salida. 

95 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

#### **Ejemplo de ejecución de funciones de activación** 

#### 1 – ReLu 

Pongamos que tenemos una neurona con 4 entradas que tiene la función ReLU como función de activación, tal y como muestra la siguiente imagen. 

Recordemos que la neurona primero multiplica cada señal de entrada (c1, c2, c3 y c4) por cada uno de sus pesos correspondientes (w1, w2, w3, y w4) que son los que se modifican durante el aprendizaje y más importante todavía, los que serán el embedding de nuestro modelo final. Finalmente suma todas las multiplicaciones (c1*w1 + c2*w2 + c3*w3 + c4*w4), les añade un sesgo b y finalmente aplica la función ReLU a este número. Vamos a calcular manualmente estas operaciones para comprender de primera mano el funcionamiento de la función de activación conocida como Rectified Linear Unit, empleada en la capa intermedia de la red neuronal poco profunda de un modelo CBOW para embedding dentro del contexto del modelo word2vec, que fue publicado en 2013 por Google. 



Pongamos inicialmente los siguientes valores para nuestro ejemplo 

|c1|2|w1|0.1|
|---|---|---|---|
|c2|-1|w2|0.8|
|c3|4|w3|0.4|
|c4|-6|w4|0.9|



96 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Y supongamos un valor b = +2 

Siendo esto así, podemos calcular z como 

Z = 2*0.1 + -1*0.8 + 4*0.4 + 6*0.2 = 0.2 – 0.8 + 1.6 – 5.4 = -4.4 

A continuación, aplicaremos la función ReLU al Z resultante: 

ReLU(z) = max(0, -4.4) = 0 

Como hemos podido comprobar, la función ReLU devuelve un 0 en todos los casos en los que el cómputo de nuestra neurona acabe siendo un número negativo como en este caso. Cambiemos los pesos de la neurona para comprobar cuál sería el resultado en otra situación. 

|c1|2|w1|0.8|
|---|---|---|---|
|c2|-1|w2|0.1|
|c3|4|w3|0.6|
|c4|-6|w4|0.2|



Z = 2*0.8 + -1*0.1 + 4*0.6 + -6*0.2 = 1.6 -0.1 +2.4 – 1.2 = 2.7 

ReLU(z) = max(0, 2.7) = 2.7 

En efecto, hemos comprobado que la función ReLU mantiene los valores positivos cuando estos son el resultado del cómputo de nuestra neurona. Con este ejemplo hemos podido comprobar el funcionamiento de la función de activación de nuestras neuronas de la capa intermedia, aquellas que generarán los embeddings de nuestras palabras al final del proceso. 

#### 2 – Softmax 

Veamos ahora el funcionamiento de la función de activación de softmax. En este caso, la neurona no sumará las señales,  sino que las empleará como entrada de la función softmax para calcular un vector de salida. 

Imaginemos el siguiente vector de entrada a la función softmax 

Z = [3, 6, 5, 9, 7] 

Lo primero que hará un algoritmo de softmax será elevar el número e a cada uno de estos números, lo que se representa como exp(Z) 

exp(Z) = [exp(3), exp(6), exp(5), exp(9), exp(7)] = [20, 403, 148, 8103, 1097] 

97 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



Ahora, calcularemos la suma de todos estos números para tener el término sum_exp = 20 + 403 + 148 + 8103 + 1097 = 9771 

Por último, dividiremos cada valor exponencial entre esta suma para hallar el resultado de la aplicación de softmax 

softmax(Z) = [20/9771, 403/9771, 8103/9771, 1097/9771] = [0.002, 0.041, 0.829, 0.112] 

Esto quiere decir que la clase que más probable indica nuestro modelo que es la salida es la correspondiente a la tercera posición o dimensión de nuestro vector, ya que tiene una probabilidad de 0.829. Podemos comprobar que todas las probabilidades sumadas suman 1 (aproximadamente debido al redondeo de los decimales) por lo que hemos aplicado correctamente la función de softmax. 

Hasta ahora hemos comprendido como funciona nuestra red neuronal **hacia delante** , es decir, cómo aplicar cada una de las capas de la red neuronal para terminar prediciendo cuál es la palabra central que corresponde a las palabras de contexto dadas. En todo momento hemos afirmado que este modelo es un modelo de aprendizaje automático, y por tanto, capaz de aprender por sí mismo. 

No olvidemos que el objetivo final de este modelo de NLP es generar los embeddings de las palabras de nuestro vocabulario **a través de los pesos aprendidos en cada neurona de la capa oculta** , por lo que será necesario **realizar un entrenamiento de la red neuronal.** 

Ya hemos visto en asignaturas anteriores cómo se entrena una red neuronal por medio de la retropropagación o backpropagation, por lo que pasaremos de forma rápida por este proceso para el modelo concreto de CBOW. 

Una vez tenemos el training set con un conjunto de palabras de contexto asociadas a una etiqueta, que será su palabra central asociada, podemos comenzar el entrenamiento. 

El entrenamiento comienza inicializando de forma aleatoria todos los pesos de todas las neuronas de nuestras dos capas, la intermedia y la de salida. Una vez inicializados de forma aleatoria, pasaremos un primer lote de conjuntos de palabras de contexto y almacenaremos los resultados predichos por nuestra red neuronal que, en este momento, es un algoritmo aleatorio y no produce resultados de valor. 

98 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Una vez procesadas todas las palabras del primer lote, calcularemos el **error** cometido por nuestra red neuronal. Para ello, compararemos en cada caso la palabra que ha sido inferida por nuestra red neuronal en la capa de salida con la palabra central real que correspondía a las palabras de contexto que llegaron a la capa de entrada. 

Mediremos este error mediante una función de error que se denomina **cross-entropy loss** , y que es una de las funciones de error más empleada en modelos de clasificación con redes neuronales en las que la última capa aplica una función softmax. 

El algoritmo de entrenamiento calculará la media de todos los errores individuales, es decir, de la distancia entre la palabra inferida y la palabra. Recordemos que el algoritmo de retropropagación o backpropagation calcula las derivadas parciales de cada uno de los pesos (W) y sesgos o bias (b) de cada neurona, para encontrar el punto en el que el error se minimiza para cada uno de estos parámetros. 

Una vez nuestra red neuronal poco profunda ha llegado a un punto de entrenamiento óptimo para el conjunto de entrenamiento dado, es decir, las palabras de contexto extraídas de nuestro corpus y sus palabras centrales asociadas, tendremos una serie de neuronas (en función del tamaño N que hayamos decidido que tendrán nuestros embeddings, tendremos N neuronas en la capa intermedia). Recordemos que estos pesos aprendidos por las neuronas intermedias a través de la retropropagación son los que finalmente nos darán el espacio vectorial y la transformación de palabras a embeddings, que es nuestro objetivo final. Todo lo que hemos estudiado acerca de word2vec y CBOW hasta el momento tiene como objetivo poder convertir cualquier palabra del vocabulario de un corpus en un vector de tal forma que a vectores similares (comparados mediante su producto escalar) las palabras también tengan significados similares, lo que es uno de los mayores retos del NLP. 

Ahora que ya tenemos una red entrenada, trataremos de extraer los embeddings de nuestra red neuronal para las palabras de nuestro vocabulario. Tras entrenar nuestro modelo podremos extraer tres representaciones vectoriales o embeddings distintas para nuestras palabras. Veamos cuáles son una por una. 

La primera opción es considerar cada uno de los pesos de cada una de las entradas de las neuronas de la capa intermedia de nuestra red neuronal como los embeddings de nuestro vocabulario. Si construimos una matriz con todos los pesos de todas las neuronas de nuestra capa intermedia tendremos una matriz de tamaño V x N (el tamaño de la entrada a la capa intermedia, que son todas las palabras del vocabulario (V) por el número de salidas, que en este caso es N), siendo V el número de palabras de nuestro vocabulario y N el tamaño de nuestros embeddings. 

99 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Siendo esto así, si empleamos las columnas de esta matriz de pesos como embeddings tendríamos tantos vectores como palabras en nuestro vocabulario, pudiendo emplearlos directamente como los vectores que representan nuestras palabras. La relación entre la matriz de pesos y las palabras del vocabulario se determina por el orden en el que la red neuronal vio las palabras. 

Si tenemos un corpus de cinco palabras “estoy triste por tu pérdida”, la primera columna de pesos de la matriz W corresponderá a la palabra “estoy” y será su embedding, la segunda a la palabra “triste” y será su embedding, y así sucesivamente. 

La segunda opción que tenemos para extraer los embeddings de nuestro vocabulario es emplear los pesos de la capa de salida _output layer._ En este caso la matriz de pesos “ tiene como dimensiones N x V (el tamaño de su entrada x el tamaño de su salida) ya que recibe N señales desde la capa intermedia y produce un vector one-hot de V posiciones. 

En este caso emplearemos las filas de la matriz de pesos para extraer los embeddings de las palabras, respetando de nuevo el orden en el que la red neuronal procesó las palabras durante el entrenamiento. 

La última opción es calcular la media entre los dos vectores extraídos por los dos vectores anteriores, que es la forma más habitual de realizar esta tarea. 

Llegados a este punto, hemos conseguido tener un método de embedding basado en redes neuronales poco profundas que nos dan, como producto secundario, los embeddings de todas las palabras de nuestro vocabulario. Por el camino, hemos sido capaces además de entrenar un modelo que puede predecir una palabra conociendo sus palabras del contexto, aunque este no fuera nuestro objetivo principal. La capacidad de almacenar el **significado** de una palabra en un **vector** es una gran capacidad para un modelo de NLP, ya que significa pasar de un conjunto de letras a un conocimiento real sobre el significado de la palabra. Si bien el sistema inteligente no **comprende** las palabras, si que es capaz de dotarles de un significado abstracto que se relacionará de forma cercana con otras palabras con significados similares. Gracias a esto podremos extraer temas acerca de los que trata un texto, sugerir palabras similares en un teclado predictivo, o analizar cómo de similares son dos documentos o frases. 

100 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

## **5. Procesamiento del lenguaje natural con Deep Learning** 

_“El lenguaje es un fenómeno temporal en el que se añaden conceptos, entidades y acciones a medida que se desarrolla, y el procesamiento del mismo por parte del cerebro humano parte por una com-_ _<u>prensión temporal del mismo.”</u>_ 

Hasta el momento hemos analizado una gran cantidad de algoritmos y modelos de NLP basados en diversas tecnologías. Hemos visto algoritmos para autocorregir textos, para completar y predecir la siguiente palabra de una frase, para identificar el tipo de palabra que es cada palabra en una oración y para comprender la similitud y distancia entre palabras, así como para transformar estas en vectores comprensibles por algoritmos. 

Sin embargo, en ninguno de estos casos hemos analizado el lenguaje como el fenómeno temporal que es. En todos los casos hemos asumido que contábamos con toda la información en todo momento, y que podíamos generar ventanas en torno a una palabra central conociendo las palabras que la precedían y la sucedían. Sin embargo, no es así como el lenguaje suele construirse. El lenguaje es un fenómeno temporal en el que se añaden conceptos, entidades y acciones a medida que se desarrolla, y el procesamiento del mismo por parte del cerebro humano parte por una comprensión temporal del mismo. 

Además, todos los modelos vistos hasta el momento fallan a la hora de tener en cuenta el contexto. Los modelos N-gram solo miran tantas palabras atrás como les indique su N, y los modelos word2vec, en concreto aquellos basados en redes neuronales feed forward poco profundas solo ven las N palabras de contexto que hayamos definido, por lo que tienen una visibilidad escasa de lo que ha sucedido anteriormente de estas ventanas predefinidas. Todos estos aspectos de los que carecen los modelos vistos hasta ahora nos guían hacia la necesidad que justifica el diseño y desarrollo de algoritmos basados en redes neuronales más complejas que permitan que nuestros modelos de NLP tengan una percepción temporal del lenguaje a la vez que son capaces de procesar un contexto ilimitado respecto al mismo. A lo largo de las últimas unidades de esta asignatura vamos a centrarnos en **arquitecturas de deep learning orientadas al Procesamiento del Lenguaje Natural.** 

Vamos a hablar de tres tipos de redes neuronales: las redes neuronales recurrentes (RNN), las redes neuronales de memoria a corto y largo plazo (LSTM) y las últimas arquitecturas basadas en mecanismos de atención también conocidas como Transformers. 

101 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

En esta primera unidad dedicada a los algoritmos de Deep Learning para NLP veremos las dos primeras arquitecturas mencionadas: Las RNN y las LSTM aplicadas al lenguaje. 

Recordemos que uno de los objetivos principales de los modelos de NLP es la predicción de la siguiente palabra de una frase dado el comienzo de la misma. Para evaluar cómo de bueno es un modelo de NLP de este tipo los evaluaremos contra frases que no han visto durante el proceso de entrenamiento y compararemos su inferencia con la palabra real que debería haber sido predicha.  Veamos una de las primeras arquitecturas que vamos a estudiar en esta unidad a continuación: las Redes Neuronales Recurrentes (RNN) 

### **5.1. Recurrent Neural Networks (RNN)** 

Ya hemos estudiado el concepto de Red Neuronal Recurrente en la asignatura de Introducción a la Inteligencia Artificial. Estas redes neuronales se caracterizan por contener un ciclo dentro de sus conexiones neuronales. Esto quiere decir que el valor de una de las neuronas vuelve a la misma neurona convirtiéndose en uno de los inputs de la siguiente iteración del procesado “hacia delante” de la red neuronal. Este tipo de redes neuronales permiten a nuestros modelos poder tener un recuerdo de lo que han procesado en iteraciones previas. 



En la imagen anterior podemos observar la estructura de la RNN más simple posible. Si no fuera por el ciclo representado en azul, estaríamos frente a una red neuronal _feed forward_ como puede ser la que se emplea en los modelos de CBOW para generar embeddings. Tenemos una capa de entrada que tendrá una serie de inputs procedentes del texto a procesar. Estos inputs pasan a una capa intermedia o _hidden_ (h) que procesa la señal de la capa de entrada y hace llegar su salida a la última capa de la red (y). La gran diferencia con las redes que hemos visto hasta ahora es que la salida de la capa intermedia u oculta vuelve a convertirse en su entrada, uniéndose a la información que proporciona la entrada a la red neuronal. Esto implica que la red neuronal puede computar salidas para cada momento del procesamiento sin necesidad de tener un contexto de una longitud dada como en los modelos anteriores. 

Gracias a esta dimensión temporal en la que la información de cada pasada de la red neuronal vuelve a entrar a la red neuronal en la siguiente iteración no añade complejidad a la red ya que sencillamente añade una entrada a la capa intermedia. En un momento temporal dado la red se comporta como una red _feed forward_ y el efecto de la recurrencia solo se observa en las distintas pasadas por una frase, palabra a palabra. 

102 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Añadiremos un nuevo set de pesos llamado **U** que se añadirá a los pesos **W** que teníamos en las redes de alimentación hacia delante. Estos pesos determinarán la ponderación que dará la RNN al bucle que hemos añadido en esta arquitectura. Desde el punto de vista del entrenamiento nada cambia, ya que son pesos que se ajustan mediante una función de error que se retropropaga a los distintos pesos – indistintamente de si son U o W -  mediante una derivada de los mismos para encontrar el mínimo punto de error. 

En la siguiente imagen podemos comparar la estructura de una RNN comparada con la estructura de la _feed forward neural network_ que vimos en la unidad anterior. Vemos cómo la salida de la capa intermedia vuelve a entrar a sus neuronas aplicando unos pesos U y un _bias_ distinto, pero el funcionamiento es idéntico al de una neurona convencional. 



A efectos de inferencia, es decir, de un paso “hacia delante” en nuestra red neuronal solo tenemos que tener en cuenta que en el momento _t-1_ , es decir, en la inferencia inmediatamente anterior a la que deseamos realizar, deberemos haber almacenado en alguna variable el resultado del cómputo de la capa intermedia para poder emplearla como entrada de esta capa en la inferencia actual. 

Reflexionemos por un momento qué aporta la recurrencia en términos de lenguaje. En el modelo de CBOW teníamos una serie de palabras de contexto en una ventana de una longitud determinada. En el ejemplo concreto que vimos teníamos 2 palabras por delante y 2 palabras por detrás. Este es todo el contexto que ve una red de alimentación hacia delante. Sin embargo, con una RNN no necesitamos delimitar el contexto máximo ya que iremos almacenando el resultado del cómputo de cada iteración en esta variable temporal, que volverá a ser procesada en la siguiente iteración. Esto permite que la red neuronal tenga una suerte de memoria, en la que almacena el resultado de su cómputo en cada momento de la frase y lo emplea para computar el resultado de la siguiente iteración, permitiendo así que la RNN genere su propia representación del contexto que procesa. 

103 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Para el objetivo de autocompletado las redes recurrentes funcionan de una forma muy similar a como lo hacen los modelos N-gram o CBOW. Reciben un vector de embeddings de palabras (que previamente deberán haber sido generados por alguno de los modelos de embedding que ya hemos estudiado). 

La red entonces trata de predecir el embedding de la siguiente palabra de la frase, devolviendo así su primera inferencia. Además, almacena la salida de la capa oculta, que pasará a formar parte de la entrada de la propia capa oculta para predecir la siguiente palabra de la frase. Trabajaremos de forma idéntica a las redes más sencillas como CBOW, en las que el vocabulario está representado por un vector one-hot que representará la palabra predicha en base a la posición del vector en la que haya un 1 en la capa de salida de la red, que también usará una función softmax como último paso en el cómputo. 

Las RNN no solo se aplican a la predicción de palabras dado un contexto, sino que pueden ser aplicadas a objetivos de NLP que ya hemos visto desde una perspectiva más clásica y ahora podemos reeditar por medio del _deep learning_ . 

Uno de ellos es el **part of speech tagging** , en el que recordemos que el objetivo es clasificar sintácticamente cada una de las palabras de una frase en función del tipo de palabra que sean (nombre, verbo, artículo, determinante, preposición…). En este caso la entrada también serán los embeddings correspondientes a los tokens que hemos generado mediante un proceso de tokenización junto a otro posterior de embedding. Cada uno de estos embeddings tendrán una etiqueta correspondiente a la clase de palabra que son, que serán las que deba predecir la red. En este caso el vector one-hot de salida en lugar de indicar palabras dentro de un vocabulario indicará tipos de palabra. Por lo demás el funcionamiento es idéntico al caso de uso de predicción de palabras para casos como el autocompletado. Tendremos una serie de embeddings con una etiqueta asociada, y el proceso de aprendizaje tratará de minimizar el error entre la inferencia de la red y la etiqueta asociada en el _groundtruth_ de nuestro training set. Dado que en este caso también usamos softmax en nuestra última capa, emplearemos la función de _cross-entropy loss_ para el entrenamiento. La gran ventaja de clasificar palabras gracias a una RNN es que, como en todos los casos en los que usemos redes neuronales recurrentes, la red tendrá “memoria” del tipo de palabras que ha visto anteriormente gracias a la acumulación de conocimiento derivados del bucle en la capa intermedia, y obtendremos mejores resultados dado que puede comprender un contexto sin límite de tamaño ni complejidad, acercándose más a como comprende un humano el lenguaje natural. 

104 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Otro caso de uso de NLP al que se pueden aplicar las RNN simples es a la clasificación de secuencias. Un ejemplo de clasificación de secuencias es el análisis de tono y sentimientos. Si bien en el part of speech tagging clasificamos palabra a palabra, en este caso clasificamos secuencias completas, bien sean frases o textos completos. Para aprovechar al máximo el potencial de las RNN pasaremos el texto que deseemos clasificar palabra a palabra por la red. A medida que la capa intermedia acumula conocimiento palabra a palabra, en la última iteración tendremos una representación de la frase completa que podemos considerar como un resumen de la misma. A cada palabra que pasa los pesos de la capa intermedios actúan sobre la siguiente palabra de la frase y el texto, así como sobre el resumen de todas las palabras que han pasado anteriormente. De esta forma, podemos emplear la salida de la capa intermedia de la última palabra de nuestra secuencia – bien sea una frase o un texto completo – como el resumen definitivo de dicha secuencia. Aprovechando que esta secuencia es numérica y estructurada, es decir, puede ser procesada por una red neuronal, podemos pasar este “resumen” por una última capa con softmax (solo en la última iteración) que nos permita clasificar el tono o el sentimiento del texto gracias a este conocimiento comprimido que aúna los datos más relevantes del texto o frase. De esta forma el vector one-hot de salida representaría en cada posición una emoción o sentimiento. 

En el entrenamiento se deberá etiquetar manualmente el tono o sentimiento de cada una de las secuencias, que serán las que durante el proceso de entrenamiento definirán los cambios necesarios en los pesos y _bias_ para minimizar el error de la red a la hora de analizar sentimientos. 

Por último, podríamos aprovechar el potencial de las RNN para construir **modelos generativos de lenguaje** . Hasta este momento solo hemos hablado de realizar un análisis comprensivo del texto. Identificación de palabras y frases, autocorrección, autocompletado, clasificación sintáctica, procesamiento del significado de las palabras y la distancia entre las mismas… Pero no hemos hablado del NLG, conocido como _Natural Language Generation_ , es decir, modelos capaces de producir texto natural, coherente y comprensible a partir de un determinado input. Uno de los usos más intuitivos de la generación de lenguaje natural es como parte esencial de un asistente conversacional. Si bien todos los métodos que hemos estudiado hasta ahora son esenciales para que el asistente conversacional **comprenda** el mensaje que desea transmitir el humano, los modelos generativos son esenciales para **comunicar** al humano el resultado del procesamiento que nos ha solicitado, también a través de lenguaje natural. 

Ya hemos visto un comportamiento similar por medio de N-gram, en el que éramos capaces de estimar la probabilidad de que una palabra fuera el inicio de una frase y a partir de ahí comenzar a predecir palabras a base de bigramas, trigramas o n-gramas de mayor grado para tratar de construir frases con sentido. Gracias a las RNN podemos mejorar este proceso gracias a una técnica que se denomina **_autoregressive generation_** o generación auto regresiva. El proceso es como sigue: 

105 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

1. Empleando un modelo RNN de predicción de palabras como el que hemos visto en esta misma sección, introducir el token <s> y emplear la palabra que devuelva la red neuronal como comienzo de nuestra frase. 

2. Empleando el embedding de la palabra predicha por la RNN de autocompletado, la introducimos en la RNN, por supuesto manteniendo el bucle de la RNN para no perder la información del contexto. Es aquí donde este modelo generativo supera con creces el modelo N-gram, como en todos los casos. Gracias a la recurrencia, la red nunca pierde la perspectiva de las palabras que ha ido generando y por tanto, entrenada con un corpus suficientemente grande podrá generar frases largas con sentido y coherencia. Los modelos N-gram solo tienen en cuenta las últimas N palabras de la frase que están generando, lo que hace que a medida que la frase va siendo más larga, comienza a perder sentido ya que no hay ninguna relación entre las primeras palabras y las últimas. Esto es algo que no sucede con las frases generadas por una RNN de generación auto regresiva correctamente entrenada con una cantidad suficiente de datos. 

3. Seguir generando palabras hasta que la red devuelva un símbolo de fin de frase </ s> o hasta que se alcance una longitud máxima predeterminada por el desarrollador. 

Podemos ver gráficamente la lógica detrás de este proceso en el siguiente diagrama en el que generamos una frase de cuatro palabras hasta que la RNN devuelve el token de fin de frase </s>. En cada paso usamos la palabra que sale de la RNN como input de la siguiente etapa, pero también pasamos la salida de su capa intermedia a la siguiente etapa (flechas horizontales). En determinadas fuentes se refieren a esta representación de una RNN como una RNN desplegada o unfolded porque los distintos rectángulos blancos son la misma red que recibe la información de sí misma, pero se representan como distintos bloques a pesar de ser realmente el mismo. 



106 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

#### **Ejemplo RNN** 

Construir una RNN en Python es tremendamente sencillo gracias al módulo Keras de Tensorflow. Ya hemos usado Keras con anterioridad en la asignatura de Visión Artificial, por lo que no entraremos en detalles de su funcionamiento. 

Será suficiente con saber que en Keras hay una capa RNN integrada directamente en la librería bajo el nombre de keras.layers.SimpleRNN, que es una capa recurrente totalmente conectada en la que la salida de la iteración anterior pasa a formar parte de la entrada de la iteración actual, tal y como hemos estudiado en la teoría de estos modelos. Para construir una red neuronal en keras es suficiente con saber las capas que deseamos emplear y el número de neuronas que queremos emplear en cada una de ellas. Imaginemos que deseamos implementar una RNN para la generación automática de texto en la que emplearemos 32 neuronas en la capa recurrente y dos  capas totalmente conectadas al final para acabar generando el output final de la misma. 

Solo vamos a ver cómo construiríamos la RNN ya que para su entrenamiento necesitaríamos un gran corpus de texto etiquetado, y para esto existen los modelos preentrenados como algunos que veremos en ejemplos futuros para poder ejecutar directamente tareas de NLP sin necesidad de etiquetar toda la Wikipedia de nuevo. 

Podemos crear un cuaderno de Google Colab para comprobar que efectivamente el código funciona y es usable, pero no utilizaremos la red neuronal, sencillamente veremos cómo generar su estructura. 



En definitiva, estamos creando una capa con recurrencia de 32 neuronas activada por ReLU y posteriormente dos capas totalmente conectadas (Dense) que computan la salida definitiva de la red en el último paso. 

107 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Para ver la estructura que Keras ha construido sobre tensorflow de nuestra red podemos llamar a model.summary() que nos mostrará las capas y sus parámetros entrenables. En total, esta estructura de red que hemos generado tiene 1457 parámetros entrenables, lo que podríamos considerar un modelo bastante “pequeño” para hoy en día. 



Hasta ahora hemos analizado el funcionamiento de una RNN básica, lo que en el mundo del _deep learning_ se denomina una arquitectura de _vanilla Recurrent Neural Network_ , tratando de jugar con el concepto de que es el sabor “por defecto” de helados y postres. Cualquier tipo de arquitectura más compleja de una arquitectura _vanilla es_ aquella que incorpora alguna mejora frente a la idea original. 

Las RNN presentan un problema principal, y es su falta de memoria a largo plazo. Si bien hemos indicado anteriormente que mejoran notablemente la memoria de modelos como N-Gram o word2vec con CBOW, que tienen una capacidad de análisis de contexto limitada y predeterminada, las redes RNN muestran una tendencia al desvanecimiento del conocimiento distante en el tiempo. Es decir, si bien son capaces de codificar contenido temporal, lo cual es una gran ventaja para el lenguaje como ya hemos comentado, a medida que un suceso (o palabra) está más lejano en el tiempo, tiene menos relevancia en la salida de la capa intermedia en cada iteración, hasta que llegado un punto, se “desvanece” y deja de estar representado en el conocimiento que genera la red. Esto se denomina gradient vanishing. Podemos ver una representación visual del desvanecimiento de gradiente en la siguiente imagen. En ella podemos intuir como las RNN tienden a dar más peso a los últimos inputs que reciben frente a aquellos más antiguos, hasta que llegado un determinado momento estos inputs más antiguos acaban desapareciendo del resultado del cómputo de la capa oculta con bucle. Llamaremos al resultado del cómputo de la capa oculta el **estado oculto** de la RNN. 

108 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



La estrategia más básica para tratar de lidiar con este problema son las Puertas de Unidad Recurrente, más conocidas por su nombre en inglés: _Gated Recurrent Unit_ o sencillamente GRU. La intención principal de las GRUS es almacenar el contenido más relevante en las capas ocultas independientemente de lo distantes que se encuentren en el tiempo, para evitar el desvanecimiento. Este tipo de módulo se propuso en 2014 por Cho et al, y supondría un cambio sustancial a las capacidades de lenguaje de las redes neuronales profundas. 

Veamos un ejemplo para entender la problemática de una RNN en un contexto de comprensión y predicción de NLP frente a las capacidades que proporciona una GRU, y posteriormente analizaremos su lógica y funcionamiento. 

Si tuviéramos dos frases con una palabra por completar como pueden ser “Los árboles son las plantas más grandes. Además, ____ en peligro actualmente”, una RNN tendría problemas para completar esta palabra, ya que el token que indica el género y número del verbo a completar (árboles) se encuentra muy distante en la frase y es probable que genere cualquier persona y número del verbo estar o encontrarse, como puede ser “estoy en peligro actualmente”. 

Una GRU trata de codificar el contenido de la frase que más relevancia tiene, como puede ser en este caso el sujeto de la frase por lo que conoceríamos el género y el número del mismo. Para ello emplean dos vectores, llamados en el artículo en el que se publicaron **_update gate y reset gate_** . Son, en definitiva, los vectores que deciden qué información debe pasar hacia la siguiente capa. Su característica principal es que pueden ser entrenados para mantener información que ha aparecido hace tiempo, así como para descartar la información irrelevante de cara a la predicción de palabras o autocompletado. 

La **_update gate_** ayuda al modelo a decidir qué información de inferencias anteriores debe mantenerse hacia el futuro. Para ello emplea la salida de la capa oculta en el momento actual, y la salida de la GRU del momento anterior. Cada una de ellas las multiplica por una serie de pesos – que serán los que se modifiquen durante el entrenamiento – y posteriormente las suma. Una vez sumadas, aplica una función sigmoide para obtener un resultado entre 0 y 1. 

109 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Es decir, aplicamos una nueva capa de decisión entre la capa oculta de un momento y la del momento siguiente, ya que gracias a que la salida actual y la anterior están ponderadas, le daremos más o menos importancia a cada uno de los elementos en cada momento. 

La denominada como **_reset gate_** es la que indica al modelo la cantidad de información que debe olvidar del pasado, de tal forma que  no se mantenga información relevante. En términos matemáticos su aplicación es idéntica a la aplicación de una _update gate_ , y emplea como inputs tanto la salida del estado oculto de la ejecución anterior como el input actual de la red. 

La primera _gate_ que se aplica es la reset gate. Para hacerlo se decide la cantidad de información del estado anterior que se debe mantener, generando un nuevo estado de memoria intermedio en el que solo se mantienen ciertos element0os del estado anterior original en función del criterio de que la celda GRU ha aprendido a través del entrenamiento. 

Una vez hemos eliminado del estado oculto anterior la información “irrelevante”, la _update gate_ decide qué cantidad de información empleamos de este estado anterior de información y cuánta del estado actual de salida. De esta combinación saldrá el estado oculto de memoria definitivo. Para hacer esto, ambas _gates_ emplean una función sigmoide que mantiene la salida de la red neuronal entre 0 y 1. En definitiva, indican la cantidad de información que se debe emplear del estado anterior (reset) y cuánta información se debe emplear de la nueva computación de la capa oculta (update). Por tanto, se multiplicarán el estado oculto anterior y la salida actual por este vector, que se denomina **vector de relevancia** , y se obtendrá el siguiente estado oculto. Gracias a este cambio, conseguimos evitar el desvanecimiento de la información lejana, ya que gracias a esta celda nuestra red neuronal es capaz de aprender qué nueva información debe guardar y cuál debe descartar, así como qué información del pasado debe mantener y cuál debe descartar. No vamos a analizar en profundidad el funcionamiento de las puertas de GRU ya que no son la arquitectura más común en NLP actualmente. 

La opción de emplear este tipo de celdas GRU es una de las formas en las que podemos solucionar el problema que supone la poca memoria que muestran las arquitecturas de _vanilla_ RNNs, pero en la actualidad el modelo más empleado para el Procesamiento del Lenguaje Natural son las arquitecturas conocidas como Long-Short Term Memory, o para acortar LSTM. 

110 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **5.2. Long Short-Term Memory (LSTM)** 

Las arquitecturas LSTM son arquitecturas específicas basadas en Redes Neuronales Recurrentes (RNN) diseñadas para procesar secuencias completas de datos con el foco puesto en la capacidad de saber cuándo recordar y cuándo olvidar información, algo muy similar al objetivo de las GRUs. En resumen, son capaces de tratar secuencias de forma completa, en lugar de procesar cada punto de dicha secuencia de forma independiente como haría una _feed forward network_ . La gran diferencia con una RNN es que tienen mecanismos que modulan la información que se almacena en el estado oculto de salida para evitar el desvanecimiento del gradiente, manteniendo la información más relevante y olvidando la información que no se considera como tal. Su nombre indica que tienen dos mecanismos de memoria, una memoria a largo plazo que retiene información del conjunto de la secuencia temporal y una memoria a corto plazo que retiene información cercana en el tiempo. Recordemos que el lenguaje es un fenómeno esencialmente temporal, en el que las palabras fluyen unas detrás de otras y siempre hacen referencia a palabras y conceptos que han aparecido en el pasado. Dado que vamos a analizar un modelo orientado a procesar secuencias siempre daremos por sentado que vamos a procesar múltiples puntos temporales. Es por ello que haremos referencia a la iteración “actual” y a la iteración “anterior”. 

Por ejemplo, si estamos procesando una frase, la iteración “anterior” es aquella que resulta de llegar hasta la anterior palabra de aquella en la que nos encontramos, y la iteración “actual” es la que ejecutamos sobre la palabra en la que nos encontramos. Lo vemos en el siguiente diagrama. Si estamos procesando la siguiente frase y vamos por la palabra “en”, la iteración anterior es la correspondiente al resultado de procesar (Hoy > me > caí), y la iteración actual el resultado de incorporar “en” a la secuencia de procesado. 



En cada nueva iteración la red LSTM actualizará su memoria a corto y a largo plazo para almacenar la información histórica más relevante. De esta forma se irá modificando la memoria de la red en función de cada nuevo input de nuestra secuencia, pero no daremos necesariamente más peso a las entradas más nuevas como sí pasaba en una _vanilla_ RNN en el diagrama que hemos visto, sino que nuestra red aprenderá – gracias al proceso de entrenamiento – a priorizar los conceptos y palabras más importantes de nuestras frases de tal forma que nunca se pierda la información más relevante. 

111 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Una red LSTM tiene tres componentes principales: 

- Un estado de celda o “ _cell state_ ”. Contiene la memoria a largo plazo de la arquitectura. En ocasiones se la define como una cinta transportadora en la que la información fluye desde el inicio hacia el final de la unidad LSTM. 

- Un estado oculto o “ _hidden state_ ”. Contiene la salida de la capa oculta. Es decir, es el resultado del último cómputo. 

- Una serie de puertas o “ _gates_ ”. Son las encargadas de decidir la cantidad de información que pasa al siguiente estado, y la información que es descartada en cada paso hacia delante por la red.  En definitiva, deciden la información que pasa a formar parte de los estados, y la información que se elimina de los estados. Generalmente hay tres tipos de puertas en una LSTM. Por un lado tenemos la puerta de olvido o _forget gate_ , por otro la puerta de entrada o _input gate_ y por último la puerta de salida o _output gate_ . Las veremos todas en detalle a continuación para comprender su funcionamiento. 

Una unidad LSTM tiene, además, una entrada (que llamaremos x) y una salida (que llamaremos y). En cada procesado tendremos por tanto de inicio un _cell state_ de la iteración anterior (ct0), un _hidden state_ del estado anterior (ht0) y una entrada correspondiente a la iteración actual (xt1). Tras la ejecución de la celda LSTM tendremos un _cell state actual_ (ct1), un _hidden state actual (_ ht1) y una salida correspondiente a la iteración actual (yt1). Podemos ver esto en el siguiente diagrama. 



Veamos los tres tipos de puerta que existen en una LSTM por el orden en el que se ejecutan. En el siguiente diagrama vemos las tres puertas sin entrar en su funcionamiento. 

112 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



Comencemos con la primera puerta, la puerta de olvido o **_forget gate_** , que es la encargada de decidir qué información de la memoria de largo plazo de la red ( _cell state_ o c) se mantiene en la misma. 

Para ello se suman los vectores de entrada (x) y el estado oculto(h) y se pasan por una red neuronal de una única capa (representada como un círculo verde) activada por una función sigmoide, es decir, que devuelve una salida entre 0 y 1. Esta red neuronal ese entrena para que su salida sea cercana a 0 cuando la información contenida en el nuevo input se considera irrelevante y para que sea cercana a 1 cuando dicha información se considera relevante. Esta puerta funciona de una forma similar a una válvula. Cuanto más cercano sea el valor de salida a 0, la válvula estará más cerrada y dejará pasar menos información desde el nuevo input hacia la memoria a largo plazo. Cuanto más próximo a 1 sea el valor resultante de la función sigmoide, más abierta estará la válvula y una mayor cantidad de información del nuevo input pasará a la memoria a largo plazo. 

La salida de esta red neuronal es multiplicada mediante un producto escalar con el estado anterior de memoria a largo plazo o _cell state_ (c). Gracias a esta multiplicación los elementos del _cell state_ que coincidan con los marcados como irrelevantes serán multiplicados por valores próximos a 0, y por tanto tendrán una influencia menor en su peso específico a la hora de recordar ciertos eventos. De igual forma, los elementos identificados como relevantes en función del estado oculto anterior y de la nueva entrada serán multiplicados por un valor cercano a 1, y por tanto tendrán más importancia dentro de la memoria a largo plazo. Es por esto que se denomina forget gate, ya que el resultado de su aplicación afecta a la memoria a largo plazo dando más o menos importancia a determinados componentes en función de la composición de los vectores de entrada y del _hidden state_ . 

113 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



Al finalizar la ejecución de la _forget gate_ tendremos un vector _cell state_ modificado, mientras que los vectores _hidden state_ y el de entrada no han sido manipulados todavía, sencillamente se han usado para tomar decisiones acerca de la memoria a largo plazo. 

Veamos ahora el funcionamiento de la **_input gate_** que tendrá las mismas entradas que le _forget gate_ : el estado oculto de la ejecución anterior y el input de la ejecución actual. 

Si en la puerta anterior se tomaba la decisión de qué información del _cell state_ debía perder peso, es decir, ser olvidada, en este paso se decide qué información se añade a la _cell state_ , es decir, ampliamos el conocimiento acumulado en nuestra memoria a largo plazo tras “liberar espacio” de la misma gracias a la puerta de olvido. El funcionamiento de esta puerta se separa en dos partes. Una de ellas se denomina **_new memory network_** , y la otra es la **_input gate_** propiamente dicha. 

La red neuronal de nueva memoria o _new memory network_ es una red neuronal simple activada por la función tanh. Hasta el momento en esta asignatura hemos mencionado las funciones ReLU, softmax y sigmoide. La función tanh es una nueva función de activación que delimita la salida de nuestra red neuronal entre -1 y 1, a diferencia de la función sigmoide que limita la salida entre 0 y 1, como podemos comprobar en el siguiente gráfico. Esta red neuronal es la encargada de combinar el estado oculto (h) con el nuevo vector de entrada (x) para generar un vector de salida ponderado. 

La salida de esta red neuronal se llama **vector de actualización de memoria** o **_new memory update vector_** , y esencialmente contiene información acerca de cómo convertir en nueva memoria el conjunto de nuestro input (x) dado el estado oculto (h). Podríamos decir que “traduce” el input usando el estado oculto como contexto para prepararlo de tal forma que esté preparado para ser incorporado a la memoria a largo plazo de nuestra red. 

114 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

En este caso necesitamos que haya valores negativos ya que necesitamos poder reducir el peso de ciertos componentes de nuestros vectores de entrada en la nueva memoria a largo plazo, por lo que la importancia asociada a cada componente de los vectores de entrada podrá ser negativa, neutra o positiva, en función de la importancia que de la red neuronal de nueva memoria a cada uno de los componentes de entrada a sus neuronas. 



Con este nuevo vector para actualizar la memoria estamos preparados para ampliar el conocimiento acumulado en la memoria a largo plazo, pero ahora debemos decidir si esta nueva memoria realmente es suficientemente relevante como para ser incorporada a nuestra memoria a largo plazo. Para hacer esto emplearemos la misma estrategia que en la puerta de olvido. Usaremos los vectores de entrada (x) y de estado oculto (h) para procesarlos a través de una red neuronal de una única capa activada con una función sigmoide. Es decir, nuestra salida estará limitada entre 0 y 1. Esta será realmente la puerta de entrada o _input gate_ que será la que decida cuánta información nueva pasa a formar parte de nuestra memoria a largo plazo. De igual forma que en la puerta anterior, podemos entender este intervalo [0,1] como una válvula. En este caso cuanto menor sea el valor menos cantidad de información fluirá desde los componentes del **_new memory update vector_** hacia el **_cell state_** , y viceversa. 

En definitiva, al terminar la ejecución de esta puerta habremos terminado de manipular nuestra memoria a largo plazo, ya que hemos olvidado la información que no es relevante dada la nueva entrada, y hemos incorporado la información que sí es relevante de esta nueva entrada en nuestra memoria a largo plazo. 

El siguiente paso será computar la salida de esta iteración para obtener tanto la salida de la red como el nuevo estado oculto que nos permita volver a hacer la siguiente ejecución para el siguiente elemento de nuestra secuencia. Pero antes, veamos un diagrama del funcionamiento de la _input gate_ . A la izquierda vemos la red de nueva memoria en la que usamos una red simple activada por tanh para construir el nuevo vector de memoria. A la derecha vemos la i _nput gate_ , que decidirá hasta qué punto este nuevo vector de memoria fluirá hacia la memoria a largo plazo. Multiplicamos escalarmente la salida de ambas redes neuronales y sumamos el resultado a la memoria a largo plazo (c), para así incorporar esta nueva información a nuestra memoria a largo plazo, que queda completada definitivamente. 

115 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



Nos queda ahora por tanto computar la salida propiamente dicha de nuestra red. Para ello vamos a emplear la última de las puertas, la puerta de salida o **_output gate._** 

En este caso vamos a usar tres entradas. Las dos primeras son las mismas que en los casos anteriores, es decir, el estado oculto anterior y los nuevos datos de entrada o input. La tercera será la nueva memoria a largo plazo o _cell state_ . El objetivo de esta puerta es generar un nuevo estado oculto, que es la memoria a corto plazo de nuestra red neuronal. Para ello decidirá qué cantidad de memoria a largo plazo debe fluir hacia la memoria a corto plazo, así como la influencia del nuevo input en el nuevo estado oculto que debe generar. Para hacer esto volveremos a recurrir a una combinación de una red neuronal de una capa activada por tanh, y otra red neuronal de una capa activada por una función sigmoide. 

Lo primero que haremos será pasar la nueva memoria a largo plazo o _cell state_ por una red neuronal activada por tanh, que limite el resultado al intervalo [-1,1], generando así un vector que permita incorporar el conocimiento acumulado en el cell state nuevo dentro de nuestro _hidden state_ actualizado. Posteriormente pasaremos la suma del anterior estado oculto y de nuestro input por una red neuronal simple activada por una función sigmoide para de nuevo tener una válvula entre 0 y 1 que decida la cantidad de memoria largo plazo que pasará hacia el estado oculto. 

Multiplicando el vector obtenido en la primera red neuronal por la válvula o _output gate_ obtenemos el nuevo _hidden state_ actualizado. Por último, computaremos la salida de nuestra red neuronal, que será el resultado de esta computación concreta para la iteración en la que nos encontramos. 

116 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

El resumen del funcionamiento de una unidad LSTM podemos comprobarlo en el siguiente y último diagrama. 



Es importante recordar que una arquitectura LSTM está orientada al procesado de secuencias, como son las conversaciones, las frases e incluso los textos completos. Esto quiere decir que nunca procesaremos un único input, como puede hacer una CNN para detección de objetos con una fotografía, sino que es necesario que ejecutemos la inferencia de la red múltiples veces encadenadas para que su empleo tenga sentido. 

Esto implica que las salidas de una ejecución se convertirán en las entradas de la ejecución siguiente. En cada iteración estaremos generando una nueva memoria a largo plazo que habrá sido actualizada, así como un estado oculto. Ambos, denominados (c) y (h) se convertirán en las entradas de la siguiente iteración junto al siguiente elemento de la secuencia que estemos procesando. 

En la siguiente figura podemos ver cómo sería la ejecución 3 veces de una red LSTM para una secuencia de 3 elementos. Recordemos que no es que tengamos 3 redes distintas, sino que ejecutamos 3 veces la misma red. Gracias a eta arquitectura evitamos los problemas derivados de los ciclos simples presentes en las capas ocultas de las Redes Neuronales Recurrentes (RNN) de una forma tan efectiva que en la actualidad la práctica mayoría de redes neuronales con recurrencia empleadas en el Procesamiento del Lenguaje Natural se basan en LSTM. 

117 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



### **5.2.1. LSTM para la clasificación de textos: un ejemplo** 

Vamos a tratar de construir una red LSTM en Keras para clasificar reseñas de películas de cine. El objetivo es que dada una reseña de cine escrita nuestra red neuronal devuelva una puntuación numérica para la película. En definitiva, exploraremos al fin el objetivo de análisis de sentimientos en NLP. 

Para ello vamos a usar la base de datos abierta del laboratorio de Stanford AI denominada Large Movie Review Dataset. En ella se encuentran una gran cantidad de reseñas en IMDb en las que el sentimiento se clasifica como positivo o negativo en función del contenido textual de la reseña escrita. 

Lo primero que haremos será descargar la base de datos y descomprimirla. Este será el primer corpus real con el que trabajaremos. Para ello, crearemos un nuevo cuaderno de Google Colab, y en la primera celda introduciremos el siguiente código y lo ejecutaremos. Tardará un poco en descargar todas las reseñas, por lo que deberemos esperar hasta que aparezca un tick verde junto a la celda indicando que ha terminado su ejecución. 



Cuando hayamos terminado tendremos un gran corpus de texto compuesto de reseñas de películas que podemos explorar si lo deseamos con comandos de Linux en Google Colab escribiendo antes de los comandos el carácter “!” para que el intérprete de Google Colab los ejecute sobre el sistema operativo y no con el intérprete de Python. Podemos ejecutar por ejemplo el siguiente comando para ver la estructura de la carpeta que nos hemos descargado 



118 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

El siguiente paso será emplear la función de Tensorflow “text_dataset_from_directory” para convertir el corpus que nos hemos descargado en un objeto de tipo Dataset que nos permita trabajar directamente con los algoritmos de entrenamiento y evaluación de Tensorflow y Keras. Para hacer esto, crearemos una nueva celda de código e introduciremos y ejecutaremos el siguiente snippet de código. En esta celda eliminamos elcarácter </br> que es propio de HTML (las reseñas están descargadas de la web) y no queremos que pase a formar parte de nuestros tokens ni de nuestros embeddings. 



La salida nos informará de la cantidad de archivos y las clases que ha encontrado tensorflow. La salida deberá ser como la siguiente 



Ahora que tenemos los datos preparados comenzaremos generando un modelo completo de NLP. Vamos a tener que aplicar todos los conocimientos que hemos adquirido hasta el momento. Primero tendremos que tokenizar nuestro texto, posteriormente generaremos embeddings de las palabras, y por último entrenaremos una red neuronal con una unidad LSTM para tratar de predecir la salida de las reviews. 

Dado que la salida de nuestra red será un único número tenemos que poner al final de nuestro modelo dos capas totalmente conectadas hacia delante para acabar teniendo una salida de tamaño 1. Vayamos paso a paso. Primero declaramos un modelo secuecial de tensorflow que recibe una entrada de tamaño 1 en forma de string (la reseña). Creemos una celda y ejecutémosla. 



Ahora tenemos que añadir una capa que convierta las entradas de nuestra red en tokens, que es siempre el primer paso de un proyecto de NLP. Para ello emplearemos una capa de Tensorflow diseñada a tal efecto que se integra en la arquitectura de nuestra red, y que en cada procesado de una secuencia la tokeniza automáticamente. Además, antes de añadirla al modelo la adaptaremos a nuestro corpus concreto, para que los tokens estén optimizados para las palabras que aparecen en nuestro vocabulario. 

119 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Crearemos una nueva celda de código y la ejecutaremos como sigue: 



Una vez tokenizadas las palabras es el momento de convertirlas en embeddings. Esto es también un paso esencial en todo proyecto de NLP ya que consigue convertir las palabras en vectores estandarizados que mantienen su significado y que serán la entrada a nuestra red LSTM. 

Emplearemos una capa de Tensorflow prediseñada a tal efecto para que siempre que introduzcamos una frase en forma de string esta se tokenize y genere embeddings de forma automática. 

De nuevo, creamos una nueva celda de código y la ejecutamos: 



120 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Ahora añadiremos a nuestro modelo una capa de LSTM compuesta por 64 unidades que serán las que mantengan la memoria de lo que ha ocurrido previamente en nuestra frase para así, al procesar la secuencia completa, poder tomar una decisión acerca de si la reseña ha sido positiva o negativa. 



Detrás de la capa LSTM añadiremos a nuestro modelo las dos últimas capas. Estas dos últimas capas serán, como en casi todos los modelos, capas totalmente conectadas que computarán el resultado final. En este caso aplicaremos primero una capa totalmente conectada con una función de activación ReLU para convertir los valores devueltos por la capa de LSTM en valores sin números negativos. 

Posteriormente aplicamos una última capa totalmente conectada activada por una función sigmoide con una salida de un único valor comprendido entre 0 y 1, que será la salida definitiva de nuestra red. Recordemos que estamos tratando de definir si una reseña es positiva o negativa, por lo que este es el tipo de salida que necesitamos. 



Ahora que ya tenemos listo tanto nuestro modelo como los datos que vamos a emplear para entrenarlo es el momento de que aprenda a determinar si una reseña es positiva o negativa. Para ello vamos a compilar nuestro modelo, vamos a ver su estructura final, y vamos a entrenarlo durante 10 épocas (pasadas completas a los datos en distinto orden) para tratar de emplearlo posteriormente con reseñas propias y comprobar su funcionamiento. 

121 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

En una nueva celda de código introducimos y ejecutamos el siguiente código, que puede tardar varios minutos en completarse pero que nos dará en tiempo real la información acerca del error que comete nuestra red y de la precisión que alcanza en cada una de las 10 épocas. 



La visualización del modelo será la siguiente, con todas las capas que hemos incorporado y un total de 181761 parámetros. 



En cuanto al entrenamiento visualizaremos cada una de las épocas por separado en tiempo real. Es posible que un entorno estándar de Google Colab necesite en torno a 10 minutos para terminar el entrenamiento, ya que son muchos datos que procesar y una gran cantidad de parámetros que actualizar en cada lote de datos. 

Veremos como época a época el error va descendiendo y la precisión va subiendo, hasta posiblemente acabar en cifras cercanas al 90%, lo que no es una mala métrica teniendo en cuenta la simpleza de nuestro modelo. 

122 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

La salida tendrá un aspecto similar a la siguiente captura de pantalla. 



Cuando el modelo haya terminado de entrenar los pesos de las neuronas de todas las capas de nuestro modelo estarán optimizados para el corpus de entrenamiento que hemos usado. Si guardamos estos pesos y los cargamos en un modelo podremos usar nuestra red neuronal para predecir la positividad o negatividad de una reseña (en inglés) directamente partiendo de una frase en lenguaje natural. 

Para hacer esto, primero creamos una nueva celda de código y la ejecutamos con las siguientes dos líneas de código. 



Y por último trataremos de probar nuestro modelo. Introduciremos una reseña muy positiva acerca de cualquier película y posteriormente una reseña muy negativa. Si el modelo ha entrenado bien la tokenización, la generación de embeddings, la memoria a corto y largo plazo y los pesos de las capas totalmente conectadas, la primera de las reseñas deberá recibir una puntuación muy alta, cercana a 1, es decir, muy positiva. 

Por el contrario, la segunda reseña deberá arrojar un resultado muy próximo a cero, ya que es claramente negativa. 

123 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



En efecto, la salida de nuestra red neuronal para cada una de estas frases es la siguiente 



Hemos conseguido por tanto entrenar un modelo recurrente con memoria a corto y largo plazo que procesa pequeños textos en lenguaje natural y nos permite conocer si estos son positivos o negativos, en definitiva, realiza un análisis de sentimientos sobre las mismas. 

Ahora podemos probar con más reseñas de la misma forma en la que lo hemos hecho en la última celda, para seguir poniendo a prueba nuestro modelo. Podríamos complicar este modelo todo lo que quisiéramos, ya que solo estamos midiendo dos tipos de sentimiento. Además, solo tenemos una capa de LSTM mientras que podríamos haber usado varias para codificar el conocimiento de una forma más abstracta. Sin embargo, este ejemplo nos ha servido para comprender cómo encajan todas las piezas del puzle en un proyecto real de NLP, en el que deseamos pasar desde una frase escrita en lenguaje natural hasta un resultado numérico con el que podamos trabajar de forma estructurada. 

124 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **5.2.2. Aplicación de una red LSTM en NLP: Named Entity Recognition (NER)** 

Al comienzo de esta asignatura mencionamos un objetivo concreto del NLP conocido como reconocimiento de entidades o Named Entity Recognition como uno de los objetivos más habituales a la hora de procesar un texto completo con Procesamiento del Lenguaje Natural. 

Named Entity Recognition es un tipo de objetivo de NLP que trata de buscar de forma rápida y eficiente ciertos tipos de información a lo largo de un texto o fragmento del mismo. Su objetivo principal es localizar y extraer entidades predefinidas del texto de entrada a nuestros modelos. 

Una entidad, a la que ahora denominaremos “Named Entity” es cualquier tipo de cosa que pueda ser considerada un grupo concreto. Personas, lugares, organizaciones, fechas, horas, precios… El objetivo del NER es encontrar las palabras dentro de un texto que pertenecen a cada una de estas categorías predefinidas de forma automática. El siguiente fragmento es un ejemplo de lo que podría ser la salida de un NER tagger: 

Acerca de los precios del gas, **[ORG] United Airlines** sostuvo el **[TIME] viernes** que ha tenido que aumentar las tarifas en torno a **[MONEY] 6$** por viaje en algunos vuelos. El portavoz de la compañía, **[PER] Tim Wagner** dijo que la subida de precios tendría lugar a partir del **[TIME] sábado** en ciertos vuelos con origen en **[LOC] Chicago y [LOC] San Francisco.** 

Si bien hay entidades específicas en función de casos de uso concretos como pueden ser razas de perros, nombres de productos comerciales, artistas pictóricos o genes, hay 

una serie de categorías de entidades que todo sistema de NER suele incorporar tras su diseño y entrenamiento. En la siguiente tabla podemos observar algunas de ellas. 

|**Tipo**|**Tag**|**Categorías ejemplo**|
|---|---|---|
|People|PER|personas, personajes|
|Organization|ORG|empresas, clubs deportivos|
|Location|LOC|ríos, montañas, ciudades|
|Geo-Political Entity|GPE|países, estados|
|Money|MONEY|divisas, cantidades|
|Time|TIME|horas, minutos|
|Date|DATE|fechas, días, meses, años|



125 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

El procesado de Named Entity Recognition, también llamado Named Entity Tagging es muy útil en muchos procesos de NLP. Por ejemplo, para construir un bot que responde preguntas de clientes es necesario identificar el nombre del cliente, el nombre del producto, la fecha de compra, el lugar de compra, la franquicia… Todos estos datos serán más fáciles de encontrar si están categorizados por tipos de categorías. También ayudan a generar resúmenes automáticos y extracción de temas en textos por medio del estudio de las categorías más empleadas y de las distintas palabras que pertenecen a cada una de estas categorías. Ayudan a mejorar sistemas de recomendación de compras y anuncios, la eficiencia de motores de búsqueda en internet e incluso para tomar decisiones de internet a base de extraer información de artículos económicos de internet. 

Una de las mayores dificultades que enfrentan los modelos NER es la ambigüedad. Palabras como Washington pueden ser a la vez una persona, una ciudad, una organización o una entidad geo política. Para tratar de resolver esta ambigüedad los modelos de NER necesitan trabajar directamente con el contexto. Si bien hay modelos de NER que llevan desde los años 90 aproximando este problema con la misma perspectiva que los modelos de POS tagging que vimos al comienzo de esta asignatura estos modelos tienen el problema de que no son capaces de gestionar el contexto adecuadamente ya que emplean modelos secuenciales matemáticos como las cadenas ocultas de Markov que solo tienen información del estado en el que se encuentran, pero no tienen ningún tipo de memoria. Es aquí donde las redes LSTM surgieron como un gran cambio de las reglas del juego a la hora de identificar estas entidades en diversos textos y fuentes. 

Para entrenar un método de NER primero segmentaremos las oraciones con un método a tal efecto como los que ya hemos visto en la asignatura. Posteriormente, tokenizaremos todas las palabras y asignaremos manualmente – es decir, etiquetaremos – las clases de entidad que corresponden a cada palabra de nuestro conjunto de entrenamiento. Posteriormente, pasaremos estas frases tokenizadas por nuestro modelo de LSTM y usaremos las etiquetas para ajustar nuestro modelo. En este caso prestaremos atención a la salida (y) del modelo LSTM en cada palabra, ya que no estamos haciendo una predicción a nivel secuencia sino a nivel palabra. Gracias a que los modelos de LSTM muestran un buen comportamiento en tareas de NLP que requieran de una memoria de contexto, NER es una de las aplicaciones más habituales para estos modelos, obteniendo muy buenos resultados. 

Como en casi todas las ocasiones, existen modelos preentrenados para ejecutar sistemas de Named Entity Recognition en Python. Uno de ellos es spaCy. Este paquete para Python incorpora todos los tipos de procesamiento de NLP que hemos visto hasta el momento, incluido NER. Cuenta con tokenizadores, lematizadores, POS tagging, detección de oraciones y Named Entity Recognition. Vamos a ejecutar un ejemplo rápido en un cuaderno de Google Colab para ver en tiempo real cómo devuelve la salida de un NER una aplicación orientada al despliegue real. 

126 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

#### **Ejemplo NER** 

Crearemos un nuevo cuaderno de Google Colab e introduciremos el siguiente fragmento de código en la primera celda, que posteriormente ejecutaremos. 



Como podemos observar hemos cargado el modelo de inglés de spacy, hemos generado una oración en forma de string en la que tenemos una serie de entidades que deseamos reconocer mediante NER y hemos ejecutado sobre la misma el método nlp de spaCy. Este método ejecuta todo el flujo de NLP necesario hasta llegar al reconocimiento de entidades. Primero tokeniza las palabras, detecta frases y lematiza. Hecho hecho, aplica un algoritmo de embedding pre-entrenado para generar los vectores de cada uno de los tokens de tal forma que mantengan el significado de las palabras. Posteriormente pasa la frase por un algoritmo de POS tagging y una LSTM para Named Entity Recognition y almacena el resultado de cada uno de los tokens en varias variables a las que podemos acceder. 

Hemos accedido a las variables text (el contenido del texto del token), a la variable pos (que es el resultado del POS tagging y nos indicará el tipo de palabra que es cada una de la frase) y por último a la variable ent_type, que devuelve el tipo de entidad reconocido en cada uno de los casos. La salida de este ejemplo será como vemos en la siguiente imagen. 

Podemos comprobar que el algoritmo de POS tagging ha detectado tanto Mark como Zuckerberg como nombres propios (PROPN) y además los ha identificado como parte del nombre de una persona [PERSON]. Ciertas palabras genéricas no tienen una entidad asociada como puede ser “of” o “the”, pero ha reconocido Meta como una organización con un nomnre propio y el valor de Meta como una cantidad de dinero compuesta por el símbolo $ (SYM) y dos números (NUM) todos ellos de la categoría de entidad [MONEY]. 

127 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



Podemos imaginar fácilmente cómo sería el proceso para tener un algoritmo que rastree las redes sociales, los periódicos o los blogs en busca de determinados nombres de personas u organizaciones, de referencias a determinados países o de opiniones concretas gracias al conjunto del POS tagging y el NER. 

Habitualmente se emplea el NER para detectar los temas más relevantes acerca de los cuales trata un texto, y poder ofrecer de forma automatizada datos estructurados para el procesamiento estadístico partiendo de textos completos en lenguaje natural en los que se detectan categorías de palabras y entidades concretas con modelos como los que hemos estudiado a lo largo de toda la asignatura. 

128 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **5.2.3. Otras aplicaciones de la arquitectura LSTM** 

Además de los sistemas de Named Entity Recognition, existen una gran multitud de aplicaciones en las que se emplean modelos basados en redes LSTM en el campo del Procesamiento del Lenguaje Natura, como pueden ser, entre otras, las siguientes aplicaciones: 

- Predicción del siguiente carácter o la siguiente palabra en una frase  La entrada de la red (secuencial) es una frase parcial y la salida es una palabra inferida como la siguiente palabra más probable para esta frase codificada como un vector one-hot 

- Traducción automática entre dos idiomas  La entrada es una secuencia de texto y la salida es una secuencia de texto palabra a palabra. Para ello emplearemos la salida de la unidad LSTM en cada caso, y emplearemos la memoria a largo y corto plazo para mantener una constancia y coherencia en base al contexto. 

- Análisis de sentimiento  La entrada del modelo en este caso es un texto completo que se analiza de forma secuencial. Sin embargo, solo prestaremos atención a la última salida de todas las iteraciones de la red, ya que en este caso estamos trabajando a escala secuencia y solo queremos obtener una o varias clases de la secuencia completa, sin necesitar comprender la salida palabra a palabra de nuestro modelo. En el último paso de la red la salida codifica el sentimiento genérico del texto en un vector one-hot. 

129 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

## **6. NLP basado en mecanismos de atención. Transformers** 

_“Las capas self-attention permiten extraer y usar directamente información procedente de grandes contextos sin la necesidad de pasarla ni en bucle hacia detrás, como en una RNN, ni de actualizar estados ocultos y de memoria a largo plazo para siguientes iteraciones, como sucede en las redes LSTM”_ 

A lo largo de la asignatura hemos pasado por diversos modelos basados en redes neuronales para cumplir varios objetivos de NLP, a cada cual más complejo. Desde las redes neuronales poco profundas que emplea el modelo Word2Vec para generar vectores que contengan el significado de las palabras, pasando por los modelos generativos basados en RNNs básicas, así como modelos con memoria a corto y largo plazo que tratan de solucionar los “problemas de memoria” de las Redes Neuronales Recurrentes por medio de celdas de memoria que se aplican a objetivos como puede ser el Named Entity Recognition (NER). 

A pesar de la inclusión de estas redes con memoria, denominadas Long Short Term Memory, aún hay ocasiones en las que la información más distante dificulta el entrenamiento de estas redes neuronales y no llega a quedar almacenada en su memoria a largo plazo. Además, debido a su naturaleza secuencial, las LSTM no permiten ser computadas en paralelo, ya que cada una de las computaciones del algoritmo depende de la anterior para contar con su salida y emplearla como entrada. 

Tras alcanzar la máxima complejidad computacional con los modelos de NLP con compuestos de múltiples redes neuronales con diversas funciones de activación como las GRU o las unidades LSTM, el mundo investigador comenzó a cambiar el rumbo y a acercarse de nuevo a las redes neuronales más básicas, las redes neuronales feed forward, con la intención de cambiar el enfoque que se estaba aplicando hasta el momento en la disciplina del Procesamiento del Lenguaje Natural. 

130 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **6.1. Self-Attention Layer** 

Como resultado de este cambio de rumbo surgió un nuevo tipo de red neuronal que revolucionaría el campo del NLP por completo: los **Transformers** . Estas redes neuronales son modelos compuestos por los denominados _Transformer blocks_ . Dichos bloques son conjuntos de redes neuronales con múltiples capas que se construyen combinando capas lineales, capas de alimentación hacia delante y capas con atención, llamadas **self-attention layers** . Son estas capas las que suponen una gran innovación en estos modelos y las que determinan el éxito que han tenido y que siguen teniendo en la actualidad. 

Las capas _self-attention_ permiten extraer y usar directamente información procedente de grandes contextos sin la necesidad de pasarla ni en bucle hacia detrás, como en una RNN, ni de actualizar estados ocultos y de memoria a largo plazo para siguientes iteraciones, como sucede en las redes LSTM. Vamos a analizar cómo funciona este tipo de capas, y posteriormente analizaremos el papel que juegan dentro de un bloque completo de Transformer, que es la pieza básica para construir un modelo de _deep learning de_ **_Transformers_** con atención. 

El primer punto a tener en cuenta es que una _self-attention layer_ mapea los valores de una secuencia de entrada que podemos representar como X (x1, x2, …, xn) con los valores de un vector de salida de exactamente el mismo tamaño Y(y1, y2, …, yn). 

Además, es importante tener en cuenta que cuando esta capa procesa un elemento de la secuencia de entrada solo tiene acceso a dicho elemento y a los elementos previos de la secuencia. Esto quiere decir que solo tiene acceso al contexto de los elementos que **preceden** al elemento que está computando. Esto evita requerimientos como los de la predicción de palabras contextuales de CBOW, que necesita conocer palabras previas y posteriores a la palabra de contexto que desea predecir para ser capaz de hacerlo. 

Por tanto, gracias a esta estructura tendremos la posibilidad de usar los Transformers para generar modelos de lenguaje (como son ngram o word2vec) y también para desarrollar modelos generativos (como los modelos auto generativos con RNNs). 

Además, el cómputo de cada uno de los elementos de la entrada es independiente del cómputo de los demás elementos de la entrada, y por ello permite una paralelización tanto del entrenamiento como de la ejecución de los modelos, lo que aumenta notablemente la eficiencia de estos modelos en términos computacionales. 

131 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



En definitiva, en una capa _self-attention_ el modelo solo procesa el propio input y todos los inputs anteriores a este, generando una salida de la misma longitud de la entrada, mapeando los elementos uno a uno. 

El funcionamiento básico de una capa _self-attention_ está basado en la capacidad de comparar cada uno de los elementos de la entrada con el resto de elementos de la misma, de forma que puede extraer su relevancia en un determinado contexto. El resultado de esta comparación es el que se emplea para computar la salida dada la entrada. 

Por ejemplo, en la imagen superior, la salida y3 está basada en una serie de comparaciones que se realizan entre el elemento x3 y los elementos x1 y x2 que le preceden. Para realizar esta comparación se emplea un sistema de puntuación (score) que determina un valor para la comparación de cada par de inputs. Este sistema de comparación, como ya ha sucedido en otras ocasiones, es el producto escalar entre los dos vectores. La capa realizará por tanto la comparación entre x1 y x2, que será x1 · x2, la comparación entre x1 y x3, que será x1 · x3, y así sucesivamente. 

Por tanto, si nos encontramos en x3, tendré que calcular la distancia existente entre x3 y x1, entre x3 y x2 y entre x3 y x3 para generar una puntuación o _score_ – denotado α –   que indique la relevancia de cada uno de estos elementos de la entrada en la salida que estoy tratando de computar. 

Una vez calculada, emplearemos una función softmax para normalizar las puntuaciones α , pudiendo emplearlas para priorizar información y desarrollando así lo que denominaremos como un **mecanismo de atención** . Llamamos a esto mecanismo de atención porque permite que la red neuronal dote de más importancia a unos determinados inputs que a otros, de igual forma que hacía una LSTM por medio de sus puertas de olvido y de nueva memoria. La gran diferencia es que en este caso no necesitamos realizar ejecuciones iterativas a lo largo de la secuencia, y que con tan solo contar con los inputs previos al elemento que proceso puedo **prestar atención** a la información más relevante del contexto. 

El resultado de la relevancia o score de un elemento de nuestro input se denomina α , y dará un peso específico a cada elemento de la entrada. 

La capa de atención suma entonces todos los elementos que ha tenido en cuenta multiplicados por su α , y computa la salida yn en función de la entrada que ha recibido en cada momento. 

132 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

En resumen: Compararemos cada elemento de la entrada con todos los elementos anteriores, o lo que es lo mismo, con su contexto. Hecha esta comparación ponderaremos la importancia de cada uno de estos elementos del contexto, incluido el elemento que estamos procesando actualmente. Gracias a esta ponderación podemos calcular un valor de salida multiplicando cada elemento por su ponderación y sumándolos todos. Esta sencilla idea es la base de una capa de atención y, en definitiva, de los mecanismos basados en atención, que veremos que nos permitirán realizar operaciones complejas sobre secuencias de lenguaje como puede ser la traducción automática o la generación autónoma de texto. 

Las arquitecturas completas de Transformers nos permiten construir en base a esta idea sofisticados y complejos modelos que nos ayudan a comprender cómo las palabras pueden contribuir a representar secuencias de entrada largas. 

Vamos a ver como a lo largo del proceso de atención en este tipo de capas, cada uno de los inputs de la entrada llega a cumplir tres roles diferentes dentro del cálculo de la salida de la capa, que son los siguientes. En todos los casos el vector es el mismo, que será el embedding resultante de convertir la palabra de la secuencia de entrada en un vector según un determinado método de embedding. Sin embargo, dado que cumple estas tres funciones veremos como para cada una de ellas aplicaremos distintos caminos y operaciones hasta computar la salida definitiva. 

- Cuando lo comparamos con los inputs del pasado, se convierte en el foco de atención para la comparativa. Es el vector – y por tanto la palabra –  contra el que comparo todos los demás. En este rol, el input se denomina **query** (consulta), y servirá para determinar los elementos a los que debo prestar atención. 

- Es el input que precede al siguiente input, por lo que será usado para comparar contra él en el siguiente paso. En este caso, está cumpliendo el rol de **key** (clave), y solo se compara contra él una vez para determinar su importancia en el contexto a la hora de procesar una palabra dada de nuestra frase. 

- Por último, es un valor numérico que se emplea para computar la salida de la capa de atención cuando está siendo procesado por la misma. Una vez hayamos calculado su score por medio de la comparación, emplearemos el valor real del embedding para calcular el vector de salida. 

Veremos más claramente estos roles en un diagrama más adelante, al que podemos acudir en cualquier momento de esta lección para asentar los conocimientos que estamos adquiriendo acerca de las capas de atención. 

133 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Para poder emplear de forma diferenciada un mismo vector entre estos tres tipos de roles los transformes diferencian entre tres matrices de pesos de sus modelos, que son **W**<sup>**Q**</sup> **, W**<sup>**K**</sup> **y W**<sup>**V**</sup> . Multiplicando cada input por la matriz de pesos correspondiente obtendremos tres vectores distintos, que serán el valor del input en cada uno de sus roles posibles. El vector embedding de entrada es por tanto siempre el mismo, pero gracias a tener diversas matrices de pesos para cada uso, conseguimos que a la hora de entrenar el modelo podamos modificar las palabras de entrada de tres formas distintas y por tanto dotarlas de tres funcionalidades distintas sin modificar su significado original. 

Multiplicando cada uno de los inputs x de nuestra frase – recordemos que las x serán vectores numéricos que hemos obtenido gracias a un algoritmo como word2vec partiendo de nuestras palabras originales – por sus matrices de pesos tendremos por tanto los siguientes tres vectores que derivan de un mismo vector x: 

- q = x * **W**<sup>**Q**</sup>  Lo empleamos como query, será el foco de atención 

- k = x * **W**<sup>**k**</sup>  Lo empleamos como key, será el que se compare con los inputs futuros 

- v = x * **W**<sup>**v**</sup>  Lo usamos como value, será el que nos permita computar una salida numérica al final de la capa de atención 

Teniendo estos vectores calculados podemos calcular la distancia entre un input x1 y un input x2 de la siguiente manera 

score(x1, x2) = q2 · k1 

Es decir, calcularemos el producto escalar entre el vector del input x2 actuando como foco de atención, denominado query, y el vector del input x1 actuando como consulta o key. Este resultado será el que empleemos para aplicar una función de activación softmax y por tanto darle el peso específico a nuestro valor. Este peso específico será el resultado de aplicar softmax sobre esta puntuación o score y lo llamaremos **α** como ya hemos mencionado previamente. 

Una vez tenemos el peso específico de cada input presente y pasado en una iteración concreta, calcularemos la suma de todos los vectores en su rol numérico (v) multiplicados por su peso específico ( α ) para computar la salida de nuestra capa self-attention. Es decir, la salida la calculamos como 

#### **yn = ∑ α *v = α1 * v1 + α2 * v2 + … + αn * vn** 

Veamos en la siguiente imagen cómo calcula una capa _self-attention_ el valor de la salida y3 correspondiente a un input x3 en el que focaliza su atención, pero teniendo en cuenta contextualmente a sus predecesores x1 y x2. 

134 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



Por supuesto, todos los parámetros de una capa de atención serán aprendidos automáticamente durante el proceso de entrenamiento de una red neuronal basada en mecanismos de atención o Transformer. 

Dado que cada uno de los puntos de la salida puede ser computado de forma aislada de los demás, podemos ejecutar una capa de atención de forma paralela para todos los inputs a la vez, de tal forma que en una única ejecución en paralelo tendremos el resultado del cómputo para toda la secuencia de entrada, es decir, para la frase al completo. Esto permite una gran eficiencia computacional y unos tiempos de cómputo mucho menores que los necesarios por arquitecturas como las RNN y las LSTM que dependen de las ejecuciones sobre las palabras anteriores de una frase para poder ejecutar la siguiente ya que la memoria y los estados ocultos se construyen de forma secuencial e iterativa. 

Uno de los usos más directos de la capa de atención es la traducción automática. En la traducción automática tendremos que convertir cada una de las palabras de una frase de entrada en una serie de palabras de salida en un idioma objetivo. Para ello es necesario tener en cuenta el contexto de esta frase, y esto es justo lo que nos permite un modelo basado en atención. 

135 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **6.2. Transformer block** 

Si bien la capa de atención es el componente principal y más novedoso de un modelo basado en atención, estos modelos generalmente están construidos a base de la concatenación de unos bloques denominados _Transformer Block_ . Estos bloques incluyen, además de una capa de _self-attention_ , una capa de _feed forward_ y dos capas de normalización, así como dos conexiones residuales que permiten que la información fluya entre capas que no son contiguas. Esta técnica permite mejorar el aprendizaje evitando que todos los pesos estén relacionados únicamente con la capa anterior, y se ha demostrado que permite obtener mejores métricas de precisión. 

Las capas de normalización son muy habituales en modelos complejos de aprendizaje profundo y también están diseñadas para ayudar a mejorar las métricas del aprendizaje de nuestra red neuronal. La capa de normalización calcula la media y la desviación estándar de nuestros datos y posteriormente los normaliza, consiguiendo que la media de nuestro vector sea 0 y la desviación estándar sea 1. Este proceso, muy habitual en diversas aplicaciones estadísticas, permite un aprendizaje más homogéneo, por lo que se realiza para los vectores de salida de nuestras dos capas neuronales principales, la capa de atención y la capa estándar o de alimentación hacia delante. 

Podemos ver el orden de estas capas y las conexiones residuales en el siguiente diagrama que representa un bloque de transformer o _Transformer Block_ . 



### **6.3. Traducción seq2seq con mecanismos de atención** 

Los modelos “secuencia a secuencia”, habitualmente denominados como seq2seq son aquellos que reciben una secuencia de datos de entrada y devuelven otra secuencia de datos de salida. Ya hemos visto algunos de estos modelos, y los Transformer son un tipo más de modelos seq2seq. 

136 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Uno de los objetivos más habituales en el NLP actual es la traducción automática que es, en esencia, un objetivo para un modelo seq2seq. Tendremos una secuencia de entrada en un idioma determinado, bien sea una frase o un conjunto de frases. Tras el procesado, deberemos devolver una secuencia que tenga exactamente el mismo significado en otro idioma. Para ello en la actualidad se emplean ampliamente los últimos modelos de Transformer. Hay otras aproximaciones basadas en tablas de correlación, en RNN y en LSTM, pero son menos precisas que los resultados obtenidos por los sistemas basados en mecanismos de atención. Estos mecanismos de atención recordemos que procesan la frase como un completo, no palabra a palabra. Para hacerlo, emplean una arquitectura de encoder-decoder, como las que vimos en arquitecturas similares a las redes deconvolucionales en la asignatura de Visión Artificial. Por tanto, tenemos dos elementos en nuestro modelo de traducción que serán el encoder y el decoder. 

Un modelo seq2seq no tiene por qué devolver una frase de exactamente la misma longitud que tenía la frase de entrada, por lo que no podemos sencillamente usar una capa de atención y pretender que las salidas de dicha capa correspondan una a una a las palabras traducidas de la frase de entrada, ya que esto sería muy parecido a usar únicamente una tabla de vocabulario. Querremos traducir toda la frase a la vez, empleando toda la información de contexto posible, pero sin centrarnos en cada una de las palabras individualmente. 

#### **Encoder** 

El encoder toma como entrada los embeddings de cada una de las palabras de la frase, dado un método de embedding seleccionado que suele ser word2vec con CBOW. 

Una vez tenemos todas las palabras convertidas a vectores que mantienen su significado desde el punto de vista del espacio vectorial, el encoder aplica el mecanismo de atención de una _self-attention layer_ para procesar cada uno de los elementos del input, convirtiéndolos en una representación intermedia de los mismos. La diferencia entre el embedding inicial y la representación intermedia de salida del encoder será el cómputo que realiza la capa de atención gracias a comparar el elemento que está tratando con el resto de elementos de entrada de la frase, como ya hemos visto. 

Una vez están calculados todas las salidas para todos los vectores (que no olvidemos que son palabras, en definitiva) de entrada, el último paso es ponderar cada uno de los elementos para construir **una salida única** que contenga toda la información relevante para poder ejecutar la traducción automática. En definitiva, cada palabra es convertida a una representación basada en mecanismos de atención, y posteriormente se construirá un único vector que representará **todo el significado de la frase en un único vector.** 

137 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Este vector será el que llegará al decoder, que tratará de convertir de vuelta esta representación numérica de la frase de origen en las palabras correspondientes del idioma de destino. Recordemos que estos modelos tienen en cuenta el contexto, por lo que no es una traducción basada en las palabras, ya que las representaciones de las palabras que son producidas en el encoder ya llevan codificados los elementos anteriores gracias a la estructura de la capa _self-attention_ . Esto nos permite que el decoder tome mejores decisiones acerca de las palabras que debe usar en la traducción gracias a conocer de alguna forma el resto del contenido de la frase que debe traducir, así como a poder ponderar la importancia de cada uno de los elementos de la frase de entrada a la hora de construir el resultado. 

Imaginemos que tenemos la frase en inglés “This book is nice”. Tras haber convertido las palabras a vectores por medio de word2vec tendremos un vector de entrada X de cuatro elementos [x1, x2, x3, x4] 

El encoder habrá generado una salida para cada uno de ellos como hemos visto en la sección anterior Y [y1, y2, y3, y4] 

Además, habrá generado un vector compuesto por la suma ponderada de estos vectores, que denominaremos vector de contexto. En definitiva, el funcionamiento del encoder es el que podemos observar en el siguiente diagrama en el que los elementos de la frase son convertidos a embeddings (en verde) para posteriormente pasar por la capa de Transformers y ser convertidos en el vector de salida. Estos vectores de salida pasan por una suma ponderada que acaba resultando en el vector de contexto, que teóricamente contiene toda la información relevante de nuestra frase de entrada en su idioma original. 



138 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

#### **Decoder** 

El decoder procesará inicialmente la suma ponderada de los vectores de salida de la capa de atención, es decir, el vector de contexto, pero tendrá una capacidad que es la que permite que obtenga tan buenos resultados. Esta es que puede procesar elementos concretos de la salida del encoder para prestar atención a elementos concretos de la misma. Es decir, recordemos que el encoder ha generado una salida para cada palabra de la frase inicial, y que estas son las que contienen la información esencial de cada una de las palabras de entrada. Sin embargo, no podemos procesar directa y únicamente estos vectores de salida y1, y2, …, yn porque en nuestro modelo seq2seq devolveremos una secuencia con una longitud independiente de la longitud de la frase original, y si procesamos las palabras una a una estaríamos forzando a nuestro traductor a generar tantas palabras en el idioma de destino como tenía la frase en el idioma de origen, mejorando notablemente la calidad de la traducción. 

El mecanismo que resuelve esta encrucijada es la atención de nuevo. Un nuevo tipo de atención llamado **cross-atention** permite al decoder no solo procesar el vector de contexto, sino decidir qué elementos de la salida de cada procesado del encoder es relevante en cada momento, para incorporarlo en su cómputo. 

Este mecanismo es complejo, y se basa en comparar los estados intermedios del decoder con los estados intermedios del encoder. A medida que el decoder va generando la frase de salida en el idioma de destino, se comparan sus estados intermedios de salida con los del encoder para decidir a qué inputs se debe prestar más atención en cada momento dado del proceso de traducción. El decoder pasa sus estados intermedios o estados ocultos al mecanismo de atención, que es entonces el que decide qué inputs del encoder debe usar para centrar su atención en ellos (es decir, aumentar su ponderación en la suma que genera el vector de contexto). 

Para asimilar el comportamiento del modelo seq2seq a la capa de atención que ya hemos estudiado, es como si los estados intermedios del decoder fueran los vectores de consulta (query) y los inputs de nuestro encoder fueran los vectores de comparación o claves (keys) contra los que comparar. De esta forma, los inputs del encoder que sean más similares a cada una de las salidas de nuestro decoder serán los más puntuados y por tanto los que más se tendrán en cuenta en el siguiente paso de la traducción. 

139 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 



Google introdujo la arquitectura de encoder-decoder seq2seq basada en Transformers en su aplicación Google Translate desde principios de 2018, tras hacer diversas pruebas con otras arquitecturas como las RNNs e incluso las CNNs aunque estas sean típicamente arquitecturas destinadas a la visión artificial. La introducción de los Transformers en la traducción automática implicó una mejora sustancial en la calidad de las traducciones y desde este momento tanto el traductor de Google como el traductor de Meta emplean la tecnología de los mecanismos de atención para la traducción automática entre idiomas. 

En el siguiente gráfico podemos observar la mejora que supuso la introducción de la arquitectura Transformer en el traductor de Google, procedente del blog de IA de Google. 



140 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

### **6.4. Transformers para generar modelos de lenguaje y generación de texto** 

Ya hemos visto los componentes principales de la arquitectura de los Transformers, tanto la capa de atención como el bloque de Transformers completo. Ahora veremos cómo podemos emplearlos para generar modelos de lenguaje de igual forma que hicimos con las Redes Neuronales Recurrentes (RNN). 

Tendremos un corpus de texto que servirá para entrenar nuestros modelos, y el objetivo principal será dado un texto en lenguaje natural trataremos de predecir la siguiente palabra del mismo de forma secuencial. 

Para ello emplearemos un bloque de Transformers seguido de una capa de alimentación hacia delante, cuya salida pasará por una capa Softmax para acabar determinando la palabra más probable de nuestro vocabulario en cada paso de nuestra secuencia. Como ya hemos comentado, la gran ventaja de un modelo de transformer es que no depende de la recurrencia ni de los estados ocultos de redes como una LSTM, sino que procesa todos los inputs en un mismo momento. 

De esta forma, somos capaces de generar palabras de forma secuencial prestando atención a las palabras más relevantes sin necesidad de almacenar una memoria interna, sencillamente guardando el resultado de cada iteración para posteriormente emplearla como entrada de la siguiente etapa. Podemos verlo mejor en la siguiente imagen 



Como podemos comprobar la aproximación es realmente similar a la que empleamos en el caso de las RNN, la diferencia principal es el cambio del tipo de red central que empleamos, que en este caso es un Transformer block basado en una capa de atención _self-attention layer_ . 

141 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

De igual forma que hicimos con las RNN y los modelos auto regresivos de generación del lenguaje, podemos aprovechar estos modelos de lenguaje para tratar de generar textos completos, no solo una palabra detrás de una secuencia. Generalmente estos modelos parten de un contexto inicial llamado “prefijo” a partir del cual se continúa escribiendo. Esto nos permite que los mecanismos de atención tengan suficiente información desde los primeros pasos como para generar texto lo suficientemente coherente como para asemejarse al lenguaje natural. 

Una de las aplicaciones más habituales de la generación automática de texto mediante Transformers es el resumen de textos. Dado un artículo, por ejemplo, estos modelos deben ser capaces de generar un resumen lo suficientemente el artículo respetando su contenido esencial. Para entrenar estos modelos se parte de un set de artículos completos y sus resúmenes escritos de forma manual. Una de las formas más interesantes de emplear los Transformers con contexto para este objetivo es sencillamente añadir el resumen del artículo al final del mismo con un determinado carácter que lo señale. 

De esta forma, el artículo entero puede ser introducido en la red como el “prefijo” y el resumen será generado automáticamente por la red gracias a los mecanismos de atención tras el entrenamiento. Gracias a este descubrimiento, modelos como GPT3 pudieron ser entrenados automáticamente en base a millones de artículos en internet ya que en una gran cantidad de artículos escritos en inglés el autor incorpora al final del mismo un acrónimo “TLDR” (too long, didn’t read) tras el que suele haber un resumen del propio artículo. 

Los investigadores alimentaron a los Transformers con todos los textos de internet que pudieron previos a “TLDR” y emplearon el resto del artículo, que se asume que es el resumen, para entrenar el modelo. 

### **6.5. Bidirectional Encoder Representations from Transformers (BERT)** 

BERT es un modelo de machine learning orientado a NLP basado en Transformers que fue presentado en 2018 por Google. Tan solo un año después pasó a formar parte del motor de búsqueda del propio Google y a día de hoy se publican más de 150 artículos científicos al año basados en esta arquitectura para seguir mejorando y trabajando distintos modelos de lenguaje de NLP. 

Los objetivos de BERT son principalmente los mismos que los que hemos estudiado a lo largo de toda la asignatura. Por un lado, el modelado del lenguaje, es decir, el mismo objetivo que tiene N-gram, las RNN de lenguaje y los Transformer genéricos: poder predecir la siguiente secuencia de una palabra. Pero además tiene el objetivo de poder predecir la siguiente frase dada una secuencia de frases, es decir, aprovecha la aproximación generativa de los Transformers que acabamos de ver para generar frases completas dado un prefijo de texto que puede ser una secuencia de varias frases distintas. 

142 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

BERT no es un modelo seq2seq por lo que solo tiene un encoder, no necesita un decoder porque no estamos trabajado con modificación de secuencias, sino con predicción de palabras y frases completas. A priori no es un modelo diseñado para la generación de texto, sino para la estructuración del lenguaje natural no estructurado, lo que recordemos que es el objetivo primario de la disciplina del NLP. Esto cobra todavía más sentido si pensamos que un motor de búsqueda como Google necesita precisamente reconocer palabras, centrarse en las más importantes, reconocer entidades y partes del discurso… y es esto específicamente lo que BERT permite dentro de Google. 

Algunos de los usos de BERT más allá del NLP son la comprensión de preguntas por parte de usuarios para la generación de chatbots inteligentes e incluso la entrada a modelos generativos como DALL-e 2, que hemos visto y analizado en la asignatura de Visión Artificial para comprender qué desea generar el usuario. Recordemos que el input de este tipo de modelos es una entrada de texto en lenguaje natural, y para que la GAN que genera las imágenes comprenda lo que debe producir, un algoritmo de NLP debe reconocer las entidades y las relaciones entre ellas, tal y como hace BERT. 

### **6.6. Generative Pre-trained Transformers (GPT-2 y GPT-3)** 

Los modelos GPT por Transformers Generativos Pre-entrados, son modelos basados en mecanismos de atención que fueron propuestos por OpenAI en 2019. Estos modelos son capaces de traducir texto, responder preguntas, resumir textos y generar texto en función de un contexto como tareas principales dentro de la disciplina del NLP. 

Sin embargo, no han sido entrenados para realizar ninguna de estas tareas, sino que han sido capaces de realizarlas gracias a la representación interna que han sido capaces de generar de las diversas palabras y frases que han procesado a lo largo de su entrenamiento. 

Hasta la aparición de los modelos GPT, los modelos de NLP se entrenaban en base a corpus etiquetados manualmente, lo que implicaba un gran esfuerzo y coste y la imposibilidad de entrenar modelos en determinados lenguajes o contextos. La gran innovación de los sistemas GPT fue la introducción de una fase de pre-entrenamiento no supervisado en el que se trataba de generar un modelo de lenguaje genérico para obtener un primer set de pesos para las neuronas del modelo de Transformer. 

Posteriormente se realiza una fase de “fine-tuning” en la que el modelo puede ser adaptado a un objetivo concreto más allá del modelado del lenguaje (que recordemos que solemos definir como la capacidad para predecir la siguiente palabra de una secuencia dado un contexto). 

143 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

Gracias a la arquitectura de Transformers basada en atención los modelos GPT tienen una capacidad de memoria ampliada frente a otros modelos basados en recurrencia, por lo que la capacidad del modelo para pasar de un objetivo de NLP a otro es más robusta y muestra resultados mucho mejores. Para entrenar el modelo GPT-2 se empleó un corpus llamado BooksCorpus en el que se encuentran más de 7000 obras de ficción no publicadas de diversos géneros. De forma interesante, este corpus se tokenizó y se generaron sus embeddings con la librería spaCy, que hemos visto en el ejemplo dedicado al reconocimiento de entidades (NER) con LSTM. 

De igual forma que BERT la arquitectura de GPT solo emplea un encoder, que es el que genera el modelo de lenguaje, basado en una arquitectura de bloques Transformer como los que ya hemos estudiado. Uno de los usos más extendidos de GPT-2 es la generación de texto partiendo de un titular o resumen, que fue la funcionalidad que dio a este modelo la relevancia mediática que obtuvo. 

En 2020 OpenAI liberó GPT-3, la siguiente iteración de los modelos GPT. La gran diferencia con los modelos anteriores reside esencialmente en el número de parámetros que tiene el modelo, no en cambios sustanciales de arquitectura, que sigue siendo una arquitectura de un encoder basado en Transformers. En este caso emplearon múltiples fuentes como origen del entrenamiento como Wikipedia, Books2, Books1 o el dataset de Common Crawil. En definitiva, la API de GPT-3 permite cualquier tarea “text-in text-out” que se desee, permitiendo a los usuarios solicitar la generación de cualquier tipo de contenido, desde un artículo periodístico hasta el guión de una película. Entre otras aplicaciones ha sido empleado en sistemas de ayuda a la programación como GitHub Copilot, que a día de hoy es empleado por cientos de miles de desarrolladores en el mundo con una gran acogida para el desarrollo de funciones sencillas y relativamente repetitivas. 

144 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

## **Bibliografía** 

- Lesk, M. (1986). Automatic sense disambiguation using machine readable dictionaries: how to tell a pine cone from an ice cream cone. In SIGDOC ‘86: Proceedings of the 5th annual international conference on Systems documentation, pages 2426, New York, NY, USA. ACM. 

- Bayer, Samuel, John Aberdeen, John Burger, Lynette Hirschman, David Palmer, and Marc Vilain. 1998. Theoretical and computational linguistics: Toward a mutual understanding. in (Lawler and Dry, 1998) 

- Cutting, Doug, Julian Kupiec, Jan Pedersen, and Penelope Sibun. 1991. A practical part-of-speech tagger. In The 3rd Conference on Applied Natural Language Processing, Trento, Italy. 

- Nadeau, David; Sekine, Satoshi (2007). A survey of named entity recognition and classification, Lingvisticae Investigationes. 

- Kapetanios, Epaminondas; Tatar, Doina; Sacarea, Christian (2013-11-14). Natural Language Processing: Semantic Aspects. CRC Press 

- Tibor Kiss and Jan Strunk. (2006). Unsupervised Multilingual Sentence Boundary <u>Detection. Computational Linguistics, 32(4):485–525.</u> 

- Nothman, Joel; et al. (2013). “Learning multilingual named entity recognition from Wikipedia”. Artificial Intelligence. 194 

- Turian, J., Ratinov, L., & Bengio, Y. (2010). Word representations: a simple and general method for semi-supervised learning. In Proceeding of the 48th Annual Meeting of the Association for Computational Linguistics. 

- “POS tags”. <u>Sketch Engine. Lexical Computing. 2018-03-27. Retrieved 2018-04-06.</u> 

- DeRose, Steven J. 1988. “Grammatical category disambiguation by statistical optimization.” 

- Charniak, Eugene. 1997. “Statistical Techniques for Natural Language Parsing” 

- Mikolov, Tomas; et al. (2013). “Efficient Estimation of Word Representations in Vector Space”. arXiv:1301.3781 

- Mikolov, Tomas; Chen, Kai & Corrado, Gregory S. et al., “Computing numeric representations of words in a high-dimensional space”, published 2015 

145 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

- Mikolov, Tomas (2013). “Distributed representations of words and phrases and their compositionality”. Advances in Neural Information Processing Systems. 

- Le, Quoc; et al. (2014). “Distributed Representations of Sentences and Documents”. arXiv:1405.4053 

- Weinberger, K. Q.; Dasgupta A.; Langford J.; Smola A.; Attenberg, J. (2009). “Feature hashing for large scale multitask learning”. Proceedings of the 26th Annual International Conference on Machine Learning 

- Broder, Andrei Z.; Glassman, Steven C.; Manasse, Mark S.; Zweig, Geoffrey (1997). “Syntactic clustering of the web”. Computer Networks and ISDN Systems. 29 

- Alex Franz and Thorsten Brants (2006). “All Our N-gram are Belong to You”. Google Research Blog. 

- David Guthrie; et al. (2006). “A Closer Look at Skip-gram Modelling” 

- Frederick J. Damerau (1971), Markov Models and Linguistic Theory. Mouton. 

- Luhn, Hans Peter (1957). “A Statistical Approach to Mechanized Encoding and Searching of Literary Information”. IBM Journal of Research and Development. 1 

- Manning, C.D.; Raghavan, P.; Schutze, H. (2008). “Scoring, term weighting, and the vector space model” (PDF). Introduction to Information Retrieval. 

- Seki, Yohei. “Sentence Extraction by tf/idf and Position Weighting from Newspaper Articles”. National Institute of Informatics. 

- Abiodun, Oludare Isaac; Jantan, Aman; Omolara, Abiodun Esther; Dada, Kemi Victoria; Mohamed, Nachaat Abdelatif; Arshad, Humaira (2018-11-01). “State-of-the-art in artificial neural network applications: A survey”. Heliyon. 4 (11) 

- Li, Xiangang; Wu, Xihong (2014-10-15). “Constructing Long Short-Term Memory based Deep Recurrent Neural Networks for Large Vocabulary Speech Recognition”. arXiv:1410.4281 

- Hochreiter, Sepp; Schmidhuber, Jürgen (1997-11-01). “Long Short-Term Memory”. Neural Computation. 9 (8): 1735–1780 

- Sutskever, Ilya; Vinyals, Oriol; Le, Quoc V. (2014). “Sequence to Sequence Learning with Neural Networks”. Electronic Proceedings of the Neural Information Processing Systems Conference. 27 

- Schmidhuber, Jürgen (2015). “Deep Learning”. Scholarpedia. 10 (11) 

146 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

- Gers, Felix A.; Schmidhuber, Jürgen (November 2001). “LSTM recurrent networks learn simple context-free and context-sensitive languages. IEEE Transactions on Neural Networks. 12 

- Chung, Junyoung; Gulcehre, Caglar; Cho, KyungHyun; Bengio, Yoshua (2014). “Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling”. arXiv:1412.3555 

- Graves, A.; Liwicki, M.; Fernández, S.; Bertolami, R.; Bunke, H.; Schmidhuber, J. (May 2009). “A Novel Connectionist System for Unconstrained Handwriting Recognition”. IEEE Transactions on Pattern Analysis and Machine Intelligence. 31 

- Sak, Hasim; Senior, Andrew; Beaufays, Francoise (2014). “Long Short-Term Memory recurrent neural network architectures for large scale acoustic modeling” 

- Cho, Kyunghyun; van Merrienboer, Bart; Bahdanau, DZmitry; Bengio, Yoshua (2014). “On the Properties of Neural Machine Translation: Encoder-Decoder Approaches” 

- Ravanelli, Mirco; Brakel, Philemon; Omologo, Maurizio; Bengio, Yoshua (2018). “Light Gated Recurrent Units for Speech Recognition”. IEEE Transactions on Emerging Topics in Computational Intelligence. 2 

- Heck, Joel; Salem, Fathi M. (2017-01-12). “Simplified Minimal Gated Unit Variations for Recurrent Neural Networks”. arXiv:1701.03452 

- Graves, Alex; Wayne, Greg; Reynolds, Malcolm; Harley, Tim; Danihelka, Ivo; Grabska-Barwińska, Agnieszka; Colmenarejo, Sergio Gómez; Grefenstette, Edward; Ramalho, Tiago; Agapiou, John; Badia, Adrià Puigdomènech; Hermann, Karl Moritz; Zwols, Yori; Ostrovski, Georg; Cain, Adam; King, Helen; Summerfield, Christopher; Blunsom, Phil; Kavukcuoglu, Koray; Hassabis, Demis (2016-10-12). “Hybrid computing using a neural network with dynamic external memory”. Nature. 538 

- Vaswani, Ashish; Shazeer, Noam; Parmar, Niki; Uszkoreit, Jakob; Jones, Llion; Gomez, Aidan N.; Kaiser, Lukasz; Polosukhin, Illia (2017-12-05). “Attention Is All You Need”. arXiv:1706.03762 

- Luong, Minh-Thang (2015-09-20). “Effective Approaches to Attention-based Neural Machine Translation”. arXiv:1508.04025v5 

- “Open Sourcing BERT: State-of-the-Art Pre-training for Natural Language Processing”. Google AI Blog 

- Devlin, Jacob; Chang, Ming-Wei; Lee, Kenton; Toutanova, Kristina (11 October 2018). “BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding”. arXiv:1810.04805v2 

147 

**Módulo. Procesamiento del Lenguaje Natural (NLP)** 

**Centro Europeo de Postgrado** 

- Chiorrini, Andrea; Diamantini, Claudia; Mircoli, Alex; Potena, Domenico. “Emotion and sentiment analysis of tweets using BERT” (2021). Proceedings of Data Analytics solutions for Real-LIfe Applications 

- Howard, Jeremy; Ruder, Sebastian (18 January 2018). “Universal Language Model Fine-tuning for Text Classification”. arXiv:1801.06146v5 

- “Language Models are Unsupervised Multitask Learners” (2019). openai.com. 

148 







**CEUPE** Centro Europeo de Postgrado 

**Web** 

www.ceupe.com 

**E-mail** info@ceupe.com 

