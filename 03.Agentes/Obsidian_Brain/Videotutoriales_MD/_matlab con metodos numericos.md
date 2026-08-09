---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\Rotura_Presa_HEC_RAS_e_IBER_y_Model_Flujo_No_Permantente_\06. Rotura Presa HEC-RAS e IBER y Model. Flujo No Permantente\DATA\Flujo No Permanente\02 Bibliografia\_matlab con metodos numericos.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]

# Invitación al Análisis Numérico 

Carlos Enrique Mejía Salazar Universidad Nacional de Colombia, Medellín Escuela de Matemáticas 

Julio 2002 

2 

# Contenido 

|Prefac|io<br>7|
|---|---|
|1 Pre|sentación y repaso<br>9|
|1.1|Motivación . . . . . . . . . . . . . . . . . . . . . . . . .<br>9|
|1.2|Bosquejo del contenido . . . . . . . . . . . . . . . . . .<br>10|
|1.3|Repaso: Normas en espacios vectoriales . . . . . . . . .<br>11|
||1.3.1 Normas de vectores . . . . . . . . . . . . . . . .<br>12|
||1.3.2 Normas de matrices . . . . . . . . . . . . . . . .<br>13|
|2 Pri|meros pasos en MATLAB<br>15|
|2.1|La línea de comandos . . . . . . . . . . . . . . . . . . .<br>16|
|2.2|Los M-archivos . . . . . . . . . . . . . . . . . . . . . .<br>17|
|2.3|Ejercicios . . . . . . . . . . . . . . . . . . . . . . . . .<br>20|
|2.4|Procesamiento de información y visualización . . . . .<br>22|
|2.5|Ejercicios . . . . . . . . . . . . . . . . . . . . . . . . .<br>28|
|3 Ecu|aciones no lineales<br>31|
|3.1|Método de bisección . . . . . . . . . . . . . . . . . . .<br>31|
|3.2|Método de Newton . . . . . . . . . . . . . . . . . . . .<br>35|
||3.2.1 Ejercicios . . . . . . . . . . . . . . . . . . . . .<br>38|
||3.2.2 Análisis de Convergencia Local . . . . . . . . .<br>38|
|3.3|Iteraciones de punto …jo . . . . . . . . . . . . . . . . .<br>40|
|3.4|Ejercicio . . . . . . . . . . . . . . . . . . . . . . . . . .<br>44|
|3.5|Análisis de convergencia local . . . . . . . . . . . . . .<br>45|
|3.6|Ejemplos . . . . . . . . . . . . . . . . . . . . . . . . . .<br>47|
|3.7|Ejercicios suplementarios . . . . . . . . . . . . . . . . .<br>50|
|3.8|Examen de entrenamiento . . . . . . . . . . . . . . . .<br>52|



|4<br>||Contenido<br>|
|---|---|---|
|4 Inte|rpolación|55|
|4.1|Tablas . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>55|
|4.2|Teorema fundamental . . . . . . . . . . . . . . .|. . . .<br>57|
||4.2.1 Intento 1 . . . . . . . . . . . . . . . . . .|. . . .<br>57|
||4.2.2 Intento 2 . . . . . . . . . . . . . . . . . .|. . . .<br>59|
||4.2.3 Cálculo de coe…cientes . . . . . . . . . .|. . . .<br>62|
|4.3|Forma de Newton . . . . . . . . . . . . . . . . .|. . . .<br>63|
|4.4|Forma de Lagrange . . . . . . . . . . . . . . . .|. . . .<br>66|
|4.5|Ejercicios . . . . . . . . . . . . . . . . . . . . .|. . . .<br>67|
|4.6|Error al interpolar . . . . . . . . . . . . . . . .|. . . .<br>68|
|4.7|Ejercicios suplementarios . . . . . . . . . . . . .|. . . .<br>69|
|4.8|Examen de entrenamiento . . . . . . . . . . . .|. . . .<br>71|
|5 Inte|gración numérica|73|
|5.1|Fórmulas básicas . . . . . . . . . . . . . . . . .|. . . .<br>74|
||5.1.1 Ejercicio . . . . . . . . . . . . . . . . . .|. . . .<br>76|
||5.1.2 Cambio de intervalo . . . . . . . . . . .|. . . .<br>76|
|5.2|Error en la cuadratura . . . . . . . . . . . . . .|. . . .<br>77|
|5.3|Cuadraturas compuestas . . . . . . . . . . . . .|. . . .<br>78|
|5.4|Ejercicios . . . . . . . . . . . . . . . . . . . . .|. . . .<br>79|
|5.5|Cuadraturas de Newton-Cotes . . . . . . . . . .|. . . .<br>80|
|5.6|Método de coe…cientes indeterminados . . . . .|. . . .<br>81|
|5.7|Cuadratura de Gauss . . . . . . . . . . . . . . .|. . . .<br>82|
|5.8|Ejercicios . . . . . . . . . . . . . . . . . . . . .|. . . .<br>84|
|5.9|Polinomios ortogonales . . . . . . . . . . . . . .|. . . .<br>84|
|5.10|Fórmula de recurrencia de tres términos . . . .|. . . .<br>86|
|5.11|Cuadratura gaussiana y polinomios ortogonales|. . . .<br>87|
|5.12|Ejercicios . . . . . . . . . . . . . . . . . . . . .|. . . .<br>90|
|5.13|Ejercicios suplementarios . . . . . . . . . . . . .|. . . .<br>91|
|5.14|Examen de entrenamiento . . . . . . . . . . . .|. . . .<br>93|
|6 Ecu|aciones diferenciales ordinarias|95|
|6.1|Problemas de valor inicial . . . . . . . . . . . .|. . . .<br>95|
|6.2|Problemas lineales y no lineales . . . . . . . . .|. . . .<br>96|
|6.3|Soluciones de los ejemplos . . . . . . . . . . . .|. . . .<br>97|
|6.4|Análisis del Método de Euler . . . . . . . . . . .|. . . . 101|
|6.5|Existencia y unicidad . . . . . . . . . . . . . . .|. . . . 101|



|Contenid<br>|o<br>|5<br>|
|---|---|---|
|6.6|Solución numérica . . . . . . . . . . . . . . . . . . . . .|102|
|6.7|Método de Euler . . . . . . . . . . . . . . . . . . . . .|103|
||6.7.1 Análisis de error . . . . . . . . . . . . . . . . .|108|
||6.7.2 Consistencia . . . . . . . . . . . . . . . . . . . .|110|
||6.7.3 Estabilidad . . . . . . . . . . . . . . . . . . . .|111|
||6.7.4 Errores de redondeo . . . . . . . . . . . . . . .|112|
||6.7.5 Estabilidad absoluta . . . . . . . . . . . . . . .|113|
|6.8|Métodos de Taylor . . . . . . . . . . . . . . . . . . . .|114|
|6.9|Métodos de Runge-Kutta . . . . . . . . . . . . . . . . .|115|
|6.10|Ejercicios . . . . . . . . . . . . . . . . . . . . . . . . .|115|
|6.11|Problemas con valores en la frontera . . . . . . . . . .|116|
|6.12|Diferencias …nitas y método de colocación para PVFs .|118|
|6.13|Existencia y unicidad . . . . . . . . . . . . . . . . . . .|118|
|6.14|Diferencias …nitas . . . . . . . . . . . . . . . . . . . . .|118|
|6.15|Método de Newton . . . . . . . . . . . . . . . . . . . .|119|
|6.16|Ejercicios . . . . . . . . . . . . . . . . . . . . . . . . .|123|
|6.17|Método de colocación . . . . . . . . . . . . . . . . . . .|123|
|6.18|Ejercicios suplementarios . . . . . . . . . . . . . . . . .|129|
|6.19|Examen de entrenamiento . . . . . . . . . . . . . . . .|131|
|7 Ecu|aciones diferenciales parciales|133|
|7.1|Diferencias …nitas para problemas parabólicos . . . . .|133|
|7.2|Ecuaciones de tipo parabólico . . . . . . . . . . . . . .|134|
|7.3|Diferencias …nitas . . . . . . . . . . . . . . . . . . . . .|134|
||7.3.1 Métodos más comunes . . . . . . . . . . . . . .|135|
||7.3.2 Ejercicios . . . . . . . . . . . . . . . . . . . . .|137|
|7.4|Ecuaciones no lineales . . . . . . . . . . . . . . . . . .|138|
|7.5|Ejercicio . . . . . . . . . . . . . . . . . . . . . . . . . .|142|
|7.6|Otras condiciones de borde . . . . . . . . . . . . . . . .|143|
|7.7|Consistencia, estabilidad y convergencia . . . . . . . .|145|
|7.8|Análisis Matricial de Estabilidad . . . . . . . . . . . .|147|
|7.9|Ejercicios . . . . . . . . . . . . . . . . . . . . . . . . .|148|
|7.10|Dos dimensiones . . . . . . . . . . . . . . . . . . . . . .|149|
||7.10.1 Métodos ADI . . . . . . . . . . . . . . . . . . .|150|
||7.10.2 Ejercicio . . . . . . . . . . . . . . . . . . . . . .|154|
|7.11|Ejercicios suplementarios . . . . . . . . . . . . . . . . .|154|
|7.12|Examen de entrenamiento . . . . . . . . . . . . . . . .|156|



|6||Contenido|
|---|---|---|
|8 Ma|terial de interés|157|
|8.1|Referencias generales . . . . . . . . . .|. . . . . . . . . 157|
|8.2|LAPACK . . . . . . . . . . . . . . . .|. . . . . . . . . 158|
|8.3|Templates y otras colecciones . . . . .|. . . . . . . . . 159|
|8.4|MATLAB y otros . . . . . . . . . . . .|. . . . . . . . . 160|
|Ref|erencias|161|



# Prefacio 

En estas notas ofrecemos una variedad de temas del análisis numérico, que pueden servir de motivación y de guía a estudiantes de nuestra Universidad y a otros interesados. Se pueden considerar como unas notas de clase, pero, para la selección de temas y enfoques, no se siguió un programa de curso dado. 

Los más de 100 ejercicios están repartidos en pequeñas listas en medio de la exposición, ejercicios suplementarios y exámenes de entrenamiento. Hay cerca de 30 ejemplos resueltos en detalle, que casi siempre aparecen con su rutina MATLAB acompañante. Dichas rutinas se presentan únicamente con …nes didácticos y no sustituyen software de calidad. 

Pretendemos publicar estas notas en la WEB y mantenerlas en evolución. Por eso los aportes de usuarios son muy importantes. Comentarios, correcciones y sugerencias son bienvenidos en la dirección electrónica 

cemejia@perseus:unalmed:edu:co: 

Expresamos nuestro reconocimiento a la Universidad Nacional de Colombia, por habernos concedido el año sabático durante el cual escribimos estas notas. 

Parte de este documento se utilizará como guía en un cursillo de la XIII Escuela Latinoamericana de Matemáticas, que se reunirá en Cartagena, Colombia de julio 29 a agosto 3 de 2002. 

Medellín, julio 15 de 2002 

8 Contenido 

# 1 

# Presentación y repaso 

Motivación Bosquejo del contenido Repaso 

## 1.1 Motivación 

Los métodos numéricos son parte importante de la interacción entre matemáticas, ingeniería e industria. Se estudian cada día más, en gran parte debido a que la necesidad de modelamiento matemático en la ciencia y la técnica crece de forma vertiginosa. 

Es común escuchar que los métodos numéricos se utilizan por no disponer de soluciones analíticas para la mayoría de los problemas de la matemática aplicada. Por supuesto ésto es verdad, pero es importante tener en cuenta que casi siempre las soluciones analíticas se utilizan discretizadas y/o truncadas. Generalmente es una pérdida de tiempo resolver un problema analíticamente para después obtener una aproxi­ mación de tal solución, en lugar de optar desde el principio por una solución numérica. 

De…nir el análisis numérico no es tarea fácil y sobre esta materia existen todavía discrepancias, descritas por Trefethen en el Apéndice a su libro Trefethen y Bau (1997) [34]. La de…nición que propone Tre­ fethen, muy cercana a la propuesta por Henrici desde 1964 en Henrici (1964) [15], es la siguiente: El análisis numérico es el estudio de algo­ ritmos para la solución de problemas de la matemática continua. Por matemática continua, Trefethen se re…ere al análisis, real y complejo. Utiliza esta palabra como opuesta a discreta. 

Por su parte, la computación cientí…ca, puede de…nirse como el di­ seño e implementación de algoritmos numéricos para problemas de ciencias e ingeniería. De manera que podemos decir que el análisis 

10 

1. Presentación y repaso 

numérico es un pre-requisito para la computación cientí…ca. En estas notas, hacemos de cuenta que el problema matemático a resolver ya ha sido de…nido. No nos ocupamos del problema físico o de ingeniería directamente. Aquí nos concentramos en algoritmos y uso de software. Además, es en medio de ejemplos concretos que presentamos las no­ ciones de estabilidad y error, indispensables para evaluar la calidad de un método numérico. Para compensar por las obligatorias omisiones, ofrecemos bibliografía que permita profundizar en los temas a los in­ teresados. 

Frecuentemente, los métodos numéricos, muy en especial los que sir­ ven para resolver ecuaciones diferenciales, conducen a problemas de álgebra lineal en los que las matrices tienen alguna estructura y la mayoría de sus elementos son nulos. Para estos problemas, el álgebra lineal numérica ofrece métodos especiales, en los que se está traba­ jando intensamente desde hace varios años. Basta ver, por ejemplo, las Memorias de Copper Mountain Conference del año 2000 [35], que con­ tienen 6 artículos sobre precondicionamiento, 6 sobre cálculo de valores propios y 3 sobre métodos multigrid. Esta es una conferencia organi­ zada anualmente por University of Colorado en cooperación con SIAM (Society for Industrial and Applied Mathematics), que trata cada dos años sobre métodos multigrid y en el año intermedio sobre métodos iterativos en general. 

Los temas del álgebra lineal numérica son de gran importancia den­ tro del análisis numérico. Dentro de estas notas veremos problemas que al discretizarlos se convierten en problemas de álgebra lineal que aquí resolvemos utilizando a MATLAB. Pero este tema es tan importante, que amerita consideración especial. Esperamos en un futuro cercano complementar estas notas con unas acerca de álgebra lineal numérica. Lo único que haremos, por ahora, es que al …nal de estas notas, comen­ tamos brevemente sobre software especializado que invitamos a conocer a los interesados. 

## 1.2 Bosquejo del contenido 

La organización de estas notas es la siguiente: Enseguida, en este mismo capítulo, presentamos una sección de repaso que hasta ahora solo con­ 

11 

1.3. Repaso: Normas en espacios vectoriales 

tiene material sobre normas en espacios vectoriales. Vislumbramos que la sección de repaso crecerá un poco posteriormente. En el próximo capítulo introducimos el software MATLAB, que es el que escogimos para ejemplos y ejercicios en estas notas. En el capítulo siguiente se presenta la solución de ecuaciones no lineales por varios métodos, in­ cluyendo el método de Newton. En los dos capítulos que siguen nos ocupamos de interpolación y de integración numérica y en los dos si­ guientes nos concentramos en la solución numérica de ecuaciones dife­ renciales. Este tema lo iniciamos con métodos de un paso para proble­ mas de valor inicial para ecuaciones diferenciales ordinarias. Enseguida continuamos con métodos numéricos para problemas con valores en la frontera para ecuaciones diferenciales ordinarias. Más tarde, hace­ mos una revisión de métodos numéricos para la solución de ecuaciones diferenciales parciales de tipo parabólico. En la parte …nal, hacemos re­ ferencia a software de álgebra lineal numérica, con énfasis en métodos iterativos no estacionarios para la solución de sistemas de ecuaciones lineales. 

Al …nal de los capítulos que tratan sobre métodos numéricos, in­ cluimos una lista de ejercicios suplementarios y un examen de entre­ namiento. La mayoría de los problemas en estas secciones …nales están basados en problemas y ejemplos de las referencias Cheney y Kincaid (1980) [8], Golub y Ortega (1993) [12] y Johnson y Riess (1982) [19]. 

## 1.3 Repaso: Normas en espacios vectoriales 

Existen nociones topológicas y geométricas que son indispensables para estudiar análisis numérico. Posiblemente la más importante sea la idea de norma, que logra generalizar a espacios abstractos los conceptos escalares de valor absoluto y módulo. 

De…nición 1 Sea V un espacio vectorial no vacío, real o complejo. Una norma en V es una función N : V ! R que cumple las siguientes condiciones: 

- a. N (x) ¸ 0 para todo x 2 V y N(x) = 0 si y solo si x = 0: b. N (®x) = j®j N (x) para todo x 2 V y todo escalar ®: c. N (x + y) · N (x) + N (y) para todo x; y 2 V: 

12 

1. Presentación y repaso 

A la norma N (x) generalmente se le denota kxk : Se le agrega un subíndice si hay lugar a confusión. 

### 1.3.1 Normas de vectores 

Para el espacio vectorial R<sup>n</sup> , las siguientes son las normas más uti­ lizadas: 

Sea x 2 R<sup>n</sup> con componentes xj; j = 1; 2;:::;n: 1. Norma in…nito o norma uniforme: kxk1 = max j =1;2;:::;n<sup>j</sup> xjj : 



Las mismas de…niciones son válidas en el espacio vectorial C<sup>n</sup> de vec­ tores de n componentes complejas. En este caso, jxjj signi…ca módulo del número complejo xj. 

Ejemplo 2 El vector x = [1 2 3 4]<sup>0</sup> tiene kxk1 = 4; kxk1 = 10 y kxk2 = ~~p~~ 30: Las bolas de centro en el origen y radio 1; en las normas 2 y 1; aparecen en la siguiente …gura. 



<!-- Start of picture text -->
Bola Unitaria en Norma 2<br><!-- End of picture text -->



<!-- Start of picture text -->
1<br>0.5<br>0<br>-0.5<br>-1<br>-1 -0.5  0  0.5  1<br><!-- End of picture text -->



<!-- Start of picture text -->
Bola Unitaria en Norma 1<br>1<br>0.5<br>0<br>-0.5<br>-1<br>-1 -0.5  0  0.5  1<br><!-- End of picture text -->

13 

1.3. Repaso: Normas en espacios vectoriales 

Estas …guras fueron generadas con el siguiente M-archivo. El nombre M-archivo es debido a que los programas en lenguaje MATLAB se denominan en inglés M-…les. Los nombres de archivos de programas en este lenguaje siempre tienen la letra m como extensión y son archivos de texto plano que se pueden abrir en procesadores de texto sin formato como Bloc de Notas en WINDOWS. MATLAB proporciona su propio editor de archivos en las versiones más recientes. 

% normas.m Herramienta didactica, Carlos E. Mejia, 2002 % bolas unitarias con normas 1 y 2 t = 0:pi/20:2*pi; subplot(121) plot(sin(t),cos(t),’r’) axis([-1 1 -1 1]);axis square; title(’Bola Unitaria en Norma 2’); x=-1:.1:1;y=1-abs(x); subplot(122) plot(x,y,’r’,x,-y,’r’) axis([-1 1 -1 1]);axis square title(’Bola Unitaria en Norma 1’); print -deps2 .nfignnormas.eps 

### 1.3.2 Normas de matrices 

Para el espacio vectorial R<sup>n£n</sup> de matrices cuadradas n £ n con ele­ mentos reales, también se requiere el concepto de norma. La notación que se usa es la misma, pero, además de las propiedades a., b. y c. de la de…nición 1, se pide que se cumplan las siguientes dos condiciones: 

d. kABk · kAk kBk ; para toda A; B 2 R<sup>n£n</sup> 

e. Toda norma matricial debe ser compatible con alguna norma vec­ torial, es decir, kAxk · kAk kxk ; para toda A 2 R<sup>n£n</sup> ; x2R<sup>n</sup> : 

Las condiciones para una norma en el espacio matricial C<sup>n£n</sup> son análogas a las de arriba y no las precisaremos aquí. 

Un concepto necesario para la de…nición de una de las normas ma­ triciales más utilizadas es el de radio espectral. 

De…nición 3 Sea B 2 R<sup>n£n</sup> con L = f¸1; ¸2; :::; ¸rg su espectro, es decir, el conjunto de sus valores propios distintos. El radio espectral de 

14 



Ejemplo 4 La matriz 



tiene radio espectral ½ (A) = 6; pues sus valores propios son ¡3 y ¡6: Las normas matriciales más utilizadas son las siguientes: Sea A = [aij] 2 R<sup>n£n</sup> (de…niciones análogas para A 2 C<sup>n£n</sup> :) 



in…nito vectorial). 



norma 2 vectorial). 

Ejemplo 5 La matriz 



tiene kAk1 = 18; kAk1 = 18; kAk2 = ½ (A) = 13:4833 y kAkF = p184: 

En este ejemplo la norma 2 de A es igual a su radio espectral por ser A una matriz simétrica. Esto no es cierto en general, como puede verse con matrices sencillas como 



para la cual kAk2 = 1 pero ½ (A) = 0: 

# 2 

# Primeros pasos en MATLAB 

La línea de comandos Los M-archivos 

Procesamiento de información y visualización 

Según la empresa fabricante de MATLAB, llamada The Mathworks, MATLAB es un lenguaje de alto rendimiento para la computación téc­ nica. Es que MATLAB posee herramientas de calidad que facilitan el trabajo en diferentes fases de la computación cientí…ca, como proce­ samiento de información, modelamiento, desarrollo de algoritmos, com­ putación y simulación. Basta dar un vistazo a su página 

http : ==www:mathworks:com= 

para con…rmarlo. 

En esta corta introducción, ayudamos a la familiarización con este software de los que aún no lo están. Lo hacemos con unos cuantos ejemplos sencillos que sugieren la amplia gama de posibilidades que tiene este software y que preparan el camino para leer sin di…cultad las rutinas de los capítulos posteriores. En todo el documento se trabajó con MATLAB 5.3, Release 11. Versiones posteriores podrían requerir pequeños cambios a las instrucciones dadas aquí para operación del software. 

En Internet hay un gran número de guías para estudiar MATLAB y métodos numéricos con MATLAB. La amplia documentación en línea que trae el software es, por supuesto, una referencia obligada. Otra referencia útil y de aparición reciente es Higham y Higham (2000) [16]. Pero MATLAB es un software comercial. Aquellos que no tengan acceso a él, de todas maneras pueden seguir en gran medida las rutinas de estas notas, utilizando un paquete de software no comercial con sintaxis similar a la de MATLAB. Un tal paquete es OCTAVE, que se puede conseguir en su dirección 

http : ==www:octave:org=: 

16 

2. Primeros pasos en MATLAB 

## 2.1 La línea de comandos 

La línea de la pantalla donde MATLAB espera comandos, empieza por el símbolo >>. A la línea se le llama línea de comandos. Para …nalizar trabajo con MATLAB, se puede escoger la opción Exit MATLAB del menú File o entrar la palabra quit en la línea de comandos. Si lo que desea es abortar los cálculos que está haciendo, presione CTRL-C. La tecla de la ‡echa " sirve para recordar las expresiones que se han escrito antes en la línea de comandos. 

Hay cuatro sistemas de ayuda en línea: help, lookfor, helpwin y helpdesk. El último es el sistema más completo de todos, está en formato html, es apto para cualquier explorador de internet y posee enlaces para gran cantidad de archivos con formato PDF. El primero, help, lo explicamos por medio de un ejemplo: en la línea de comandos escriba help linspace. La respuesta del sistema es mostrar las primeras líneas precedidas por % del M-archivo linspace.m que listamos a con­ tinuación: 

function y = linspace(d1, d2, n) %LINSPACE Linearly spaced vector. % LINSPACE(x1, x2) generates a row vector of 100 linearly % equally spaced points between x1 and x2. % % LINSPACE(x1, x2, N) generates N points between x1 and x2. % % See also LOGSPACE, :. % Copyright (c) 1984-98 by The MathWorks, Inc. % $Revision: 5.6 $ $Date: 1997/11/21 23:29:09 $ if nargin == 2 n = 100; end if n~=1 y = d1:(d2-d1)/(n-1):d2; else y = d2; end 

Si el M-archivo por el que se pide ayuda (help) fue creado por un usuario y tiene líneas de comentarios en la primera parte, también las 

17 

2.2. Los M-archivos 

mostrará. Así que la recomendación es incluir líneas de comentario en la parte de arriba de todo M-archivo que se cree. Es una costumbre que le ahorra tiempo y esfuerzo hasta a uno mismo. 

Para conocer las variables que hay en un momento dado en el espa­ cio de trabajo, hay dos comandos: who y whos. Ensáyelos y note la diferencia. Por cierto, también es bueno notar que en MATLAB todas las variables representan matrices. Los escalares son matrices 1 £ 1: De hecho la palabra MATLAB es una sigla que signi…ca Matrix Laboratory. 

Finalmente, antes de considerar M-archivos, advertimos que el núcleo básico de MATLAB es para cálculo numérico y no simbólico. Por tanto, si a=5 y b=7+a, entonces b=12 y sigue siendo 12 aunque el valor de a cambie. MATLAB administra el cálculo simbólico a través de una de sus cajas de herramientas, que debe comprarse por aparte. 

## 2.2 Los M-archivos 

La línea de comandos deja de ser práctica cuando se desea hacer un pro­ ceso con varias órdenes o comandos. Se requiere entonces crear archivos con los comandos MATLAB que se requieren para cada tarea. Se les llama M-archivos (M-…les en inglés.) Son de texto plano (ASCII) y MATLAB proporciona un editor con una agradable codi…cación de colores que ayuda mucho en el proceso de creación y depuración de dichos archivos. Los M-archivos que requieren argumentos de entrada y entregan valores de salida, se llaman funciones. Los que no tienen ni argumentos de entrada ni valores de salida se llaman guiones ( script en inglés.) El M-archivo normas.m del ejemplo 2, que consideramos en la sección 1.3, es un guión. 

Los M-archivos están en directorios. Para que MATLAB los encuen­ tre, se debe cumplir al menos una de las siguientes condiciones: 

i. El directorio en el que están los archivos pertenece al search path de MATLAB. 

ii. El directorio en el que están los archivos es el directorio actual de MATLAB. 

Para saber cúal es su directorio actual, use el comando pwd. Para hacer que el directorio c:nmet sea su directorio actual, escriba la orden cd c:nmet. 

El search path se puede ver y actualizar por medio de la opción Set 

18 

2. Primeros pasos en MATLAB 

path, del menú File. 

Ejemplo 6 Este es un ejemplo de M-archivo de tipo guión. 

% exa1.m Herramienta didactica, Carlos E. Mejia 2002 xx=-1:.01:1; y=sin(pi*xx);z=sin(9*pi*xx); plot(xx,y,’k--’,xx,z,’r’); set(gca,’XTick’,-1:.25:1) grid on title (’ Sen(pi*x) y sen(9pi*x) coinciden en esta malla ’); print -deps2 .nfignexa1.eps 



<!-- Start of picture text -->
Sen(pi*x) y sen(9pi*x) coinciden en esta malla<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>-0.2<br>-0.4<br>-0.6<br>-0.8<br>-1<br>-1  -0.75  -0.5  -0.25  0  0.25  0.5  0.75  1<br><!-- End of picture text -->

De este sencillo ejemplo, destacamos que las funciones matemáticas elementales se pueden aplicar a vectores. La coincidencia de dos fun­ ciones distintas en los puntos de una malla, es un fenómeno que puede conducir a errores. En inglés se llama aliasing. Sobre todo lo que se quiera conocer mejor, la recomendación es acudir a la ayuda en línea. 

Ejemplo 7 El primer M-archivo de este ejemplo, es de tipo función y se ocupa de calcular, de forma ingenua, el n-ésimo término de la sucesión de Fibonacci. El segundo es de tipo guión y sirve para construir árboles binarios en los que las ramas se consiguen, parcialmente, de forma aleatoria. Utiliza la rutina rand.m que trae MATLAB. 

19 

2.2. Los M-archivos 19 function x=fib(n); % Herramienta didactica, Carlos E. Mejia 2002 % sucesion de Fibonacci, n<1477 % uso: x=fib(n) x=ones(1,n); for j=3:n x(j)=x(j-1)+x(j-2); end Al ejecutar x=…b(10) se obtiene x = 1 1 2 3 5 8 13 21 34 55 Miremos ahora el generador de árboles: % tree1.m, Herramienta didactica, Carlos E. Mejia, 2002 % generacion aleatoria de numeros para construir un arbol clf hold on x=[0;0];y=[0;rand];line(x,y) % a lo más 10 niveles de ramas n=rand*10 for i=1:n, [m,longi]=size(x); angu1=(pi/2)*rand(1,longi); angu2=(pi/2)*rand(1,longi)+angu1; x=[x(2,:),x(2,:);x(2,:)+(2/i)*rand*cos(angu1),... x(2,:)+(3/i)*rand*cos(angu2)]; y=[y(2,:),y(2,:);y(2,:)+(2/i)*rand*sin(angu1),... y(2,:)+(3/i)*rand*sin(angu2)]; line(x,y); end title(’Arbol con 10 niveles de ramas’) print -deps2 .nfigntree1.eps Uno de los árboles que pueden obtenerse con esta rutina, aparece en la siguiente …gura. 

20 

2. Primeros pasos en MATLAB 



<!-- Start of picture text -->
Arbol con 10 niveles de ramas<br>5<br>4.5<br>4<br>3.5<br>3<br>2.5<br>2<br>1.5<br>1<br>0.5<br>0<br>-1.5  -1  -0.5  0  0.5  1  1.5<br><!-- End of picture text -->

Ahora es un buen momento para reposar y asimilar los comandos MATLAB que se han utilizado. También es buen momento para estu­ diar algunos otros por medio de la ayuda en línea y experimentación directa. Los siguientes ejercicios pueden servir de guía para estas tareas. 

## 2.3 Ejercicios 

1. Use el sistema de ayudas de MATLAB para encontrar información sobre las siguientes constantes especiales: realmin, realmax, inf, NaN, pi, eps. 

2. Repase los M-archivos vistos hasta ahora y obtenga más informa­ ción sobre los comandos utilizados en ellos, por medio de los sistemas de ayuda de MATLAB. En particular, consulte sobre for, if, end, tres puntos (...), hold y line. 

3. Intentemos calcular de forma ingenua lim r (x) ;donde x!0 



5 El resultado exacto es ; se puede obtener por Regla de L’Hopital. ¡24 

21 

#### 2.3. Ejercicios 

Ensaye el siguiente intento de aproximar este límite: 

% exa2.m, Herramienta didactica, Carlos E. Mejia, 2002 % resultados exacto y numerico de limite complicado format short e x=(10.^(-(1:9)))’; % x es una sucesión decreciente de numeros positivos res=x.^(-3).*(log(1-x)+x.*exp(x/2)); disp(’Resultado numérico = ’);disp(res); 

Genera los siguientes resultados: Resultado numérico = -2.3341e-001 

-2.1064e-001 

-2.0856e-001 -2.0835e-001 

-1.6282e-001 

-2.8964e+001 5.2635e+004 

-5.0248e+007 

2.8282e+010 

La discrepancia es enorme, de…nitivamente con este archivo no se puede aproximar ese límite. ¿Cómo explica esta discrepancia y qué estrategia recomienda para poder obtener resultados correctos? Sugerencia: Como estrategia para hacer bien los cálculos, utilice expansiones en serie de Taylor para log (1 ¡ x) y x exp alrededor ³ x 2 ´ de x = 0: Con ellas, construya la serie de Taylor para r (x) que resulta 5 11 379 ser + x x ::: donde el factor entre paréntesis es ¡ 24 ¡ 48 ¡ 1920 ¡ µ ¶ una serie que no requerimos en más detalle. 

Como explicación de la discrepancia, piense en error de redondeo, sustracción de cantidades casi iguales y en el cociente de dos cantidades cercanas a cero. Re‡exione sobre estas fuentes de error y observe que en este ejemplo aparecen juntas. 

4. Use el sistema de ayuda en línea de MATLAB para estudiar so­ bre las siguientes formas de generar matrices: linspace, zeros, eye y rand. Practique con todos. 

22 

2. Primeros pasos en MATLAB 

5. Escriba un M-archivo de tipo función que tenga como argumento de entrada, un número entero positivo n y como resultado, el promedio aritmético de las componentes de un vector n £ 1 generado aleatoria­ mente. 

6. Utilice el sistema de ayuda en línea de MATLAB para estudiar sobre los comandos num2str, clf, clear y disp. Practique con ellos. 

## 2.4 Procesamiento de información y visualización 

En esta sección damos un vistazo a distintas formas que tiene MAT­ LAB de ayudar en pre y pos-procesamiento de información. Hacemos énfasis en las herramientas grá…cas y en la capacidad de MATLAB de leer y almacenar información en archivos que pueden ser binarios, con extensión mat, o de texto plano, con la extensión que se desee. 

Empezamos con el procesamiento de un archivo binario de datos llamado seamount.mat que trae MATLAB como ejemplo. Para ésto, preparamos el siguiente M-archivo: 

% exa3.m, Herramienta didactica, Carlos E. Mejia, 2002 % Referencia: ’’Using MATLAB Version 5’’, p. 5-21 % Datos de una montaña submarina en archivo seamount.mat clear all; load seamount; subplot(1,2,1); plot(x,y,’k.’,’markersize’,15) %xlabel(’Longitud’);ylabel(’Latitud’); title(’ Localizacion’); grid on subplot(1,2,2); [xi,yi]=meshgrid(210.8:.01:211.8,-48.5:.01:-47.9); zi=griddata(x,y,z,xi,yi,’cubic’); [c,h]=contour(xi,yi,zi,’k-’); set(gca,’XTick’,[210.8 211.3 211.8]) clabel(c,h,’manual’); title(’ Curvas de nivel’); %xlabel(’Longitud’);ylabel(’Latitud’); print -deps2 .nfignexa3-1.eps 

23 

2.4. Procesamiento de información y visualización 

figure subplot(2,1,1); surface(zi);shading interp; title(’ Montaña submarina’); xlabel(’Longitud’);ylabel(’Latitud’); colorbar(’vert’); subplot(2,1,2); surf(zi); shading interp xlabel(’Longitud’);ylabel(’Latitud’); zlabel(’Altura’); grid on print -deps2 .nfignexa3-2.eps 

La primera …gura, que incluye puntos de medición y curvas de nivel, es: 



<!-- Start of picture text -->
Localizacion  Curvas de nivel<br>-47.95  -47.9<br>-48<br>-48<br>-48.05<br>-48.1<br>-48.1<br>-48.15<br>-48.2  -48.2<br>-48.25<br>-48.3<br>-48.3<br>-48.35<br>-48.4<br>-48.4<br>-48.45  -48.5<br>210.5  211  211.5  212  210.8  211.3  211.8<br>-3000<br>-4000<br>-3500<br>-2000<br><!-- End of picture text -->

La segunda …gura trae dos representaciones tri-dimensionales pero una de ellas se proyecta sobre un plano. 

24 

2. Primeros pasos en MATLAB 



El siguiente ejemplo se basa en un archivo de datos generado con un M-archivo. Dicho archivo contiene cinco columnas x, y, z, r, v que representan coordenada x, coordenada y, profundidad, transmisividad óptica y velocidad respectivamente. Los números son todos …cticios, pero tienen cierto parecido con los que pueden medirse en un sector costero con aparatos especializados. 

function exa4(k); 

% Herramienta didactica, Carlos E. Mejia, 2002 

% Datos generados por gen1 y grabados en mar1.dat % columna 1: coordenada x, columna 2: coordenada y 

% columna 3: profundidad (z) 

% columna 4: transmisividad optica (r) 

% columna 5: velocidad (v) 

- % se simulan mediciones de z, r, v en nodos de una 

- % cuadricula que cubre un rectangulo cerca de la costa 

- % todos los numeros en mar1.dat son ficticios 

% k parametro de discretizacion % uso exa4(k) gen1 load mar1.dat; 

2.4. Procesamiento de información y visualización 

25 

% ahora tenemos una nueva variable mar1 que es una matriz 

% con 5 columnas y tantas filas como filas tenga mar1.dat x=mar1(:,1);y=mar1(:,2);z=mar1(:,3);nr=mar1(:,4);nv=mar1(:,5); mx = min(x); Mx = max(x); my = min(y); My = max(y); [xi,yi]=meshgrid(linspace(mx,Mx,k),linspace(my,My,k)); % se prepara malla 2-D zi=griddata(x,y,z,xi,yi,’cubic’); % Interpolacion de datos a nueva malla figure; subplot(2,1,1); surface(xi,yi,zi) % Visualizacion title([’Organizacion y visualizacion’,’ k: ’,num2str(k)]); xlabel(’Eje X’); ylabel(’Eje Y’); shading interp; subplot(2,1,2); surf(zi); xlabel(’Eje X’); ylabel(’Eje Y’); zlabel(’Profundidad’);colormap(copper) colorbar(’vert’); print -deps2 .nfignexa4-1.eps figure; subplot(1,2,1) plot(nr,z,’k’);title(’Transmisividad óptica’); subplot(1,2,2) plot(nv,z,’k’);title(’Velocidad’); print -deps2 .nfignexa4-2.eps La primera …gura trae representaciones tri-dimensionales del “área de estudio”. 

26 

2. Primeros pasos en MATLAB 



La segunda …gura muestra los per…les de transmisividad óptica y velocidad con respecto a la profundidad. 



<!-- Start of picture text -->
Transmisividad óptica  Velocidad<br>0  0<br>-1  -1<br>-2  -2<br>-3  -3<br>-4  -4<br>-5  -5<br>-6  -6<br>-7  -7<br>-8  -8<br>40  60  80  100  0  50  100 150<br><!-- End of picture text -->

Para que el ejemplo quede completo, incluímos también el M-archivo gen1.m. En ninguna forma pretendemos que esta forma de generar datos …cticios sea la mejor. Aquí presta un buen servicio didáctico y promueve la consulta de la ayuda en línea para aclarar de…niciones y usos de comandos que se incluyen ahora por primera vez. 

% gen1.m Herramienta didactica, Carlos E. Mejia, 2002 

2.4. Procesamiento de información y visualización 

27 

% genera datos ficticios para procesamiento de informacion % se piensa en sector rectangular cercano a la costa % x: coordenada x, y: coordenada y % z: profundidad, % v: velocidad del agua, r: transmisividad optica fi1=fopen(’mar1.dat’,’w’); % transmisividad optica A=40;B=80;step=.4; r=A+step:step:B;lr=length(r); p=linspace(-8,0,lr); %profundidad, variable z s=rand(size(r)); nr=2*log(r-A)+0.1; C=nr(1);D=nr(lr); c1=(A-B)/(C-D);c2=(B*C-A*D)/(C-D); nr=c1*nr+c2; nr=nr+3*round(rand)*s; % velocidad v0=40;vf=140; v=linspace(v0+1,vf,lr); nv=3*log(v-v0)+2*rand; cv=nv(1);dv=nv(lr); d1=(v0-vf)/(cv-dv);d2=(vf*cv-v0*dv)/(cv-dv); nv=d1*nv+d2; s=rand(size(r)); nv=nv+6*round(rand)*s; x=linspace(0,5000,10);y=linspace(0,3000,10); l10=floor(lr/10); nx=linspace(0,5000,lr);ny=linspace(0,3000,lr); for j=1:lr-1 m=mod(j,l10);q=(j-m)/l10; % j=l10*q+m if mod(j,l10)==0 nx(j)=x(j-q*l10+1); else nx(j)=x(j-q*l10); end ny(j)=q*300; 

28 

2. Primeros pasos en MATLAB 

end for i=1:lr out=[nx(i) ny(i) p(i) nr(i) nv(i)]; fprintf(fi1,’%8.2f %8.2f %8.2f %8.2f %8.2fnn’,out); end fclose(’all’); 

2.5 Ejercicios 

1. Revise la ayuda en línea de MATLAB para saber más acerca de los comandos de visualización grá…ca que hemos utilizado hasta ahora. Algunos de ellos son: …gure, plot, subplot, griddata, meshgrid, shading y surf. 

2. Por medio de la ayuda en línea, consulte acerca de los comandos mod, round y ‡oor. 

3. De nuevo, utilice la ayuda en línea para conocer más acerca del manejo de archivos en MATLAB. En particular, consulte sobre fopen, fclose, load, save y diary. 

4. A continuación presentamos un M-archivo para jugar Punto y Fama. Es rudimentario pues el usuario debe entrar los números en forma de vectores pero es correcto desde el punto de vista lógico. Tam­ bién incluímos la salida en pantalla que proporcionó en un juego especí…co. Se consiguió al invocar el comando diary pyf.dat. 

% punto y fama pyf1.m 

% Herramienta didactica, Carlos E. Mejia, 2002 res=1; while res ==1 nro=randperm(10); nro=rem(nro(1:4),10); nfa=0; % disp([’ El numero oculto es: ’]); disp(nro); cont=0; disp([’ Se trata de adivinar los 4 digitos distintos ’]); disp([’ de un vector en el orden correcto ’]); disp([’ Se da una fama por cada digito correctamente situado ’]); 

29 

2.5. Ejercicios 29 disp([’ y un punto por cada digito incorrectamente situado ’]); while nfa~=4 x=input(’ Entre un vector con cuatro digitos: ’); fa=find(nro-x==0); nfa=size(fa,2); npu=0; for i=1:4 for j=1:4 if nro(i)==x(j) & i~=j npu=npu+1; end end end disp([’ Famas: ’, num2str(nfa),’ Puntos: ’,num2str(npu)]); cont=cont+1; end disp([ ’ Buen trabajo, felicitaciones! ’]); disp([’ Lo hizo en ’, num2str(cont),’ intentos ’]); res=input(’ Entre 1 si desea seguir jugando y... otro numero en caso contrario: ’); end pyf1 Se trata de adivinar los 4 digitos distintos de un vector en el orden correcto Se da una fama por cada digito correctamente situado y un punto por cada digito incorrectamente situado Entre un vector con cuatro digitos: [0 1 2 3] Famas: 1 Puntos: 1 Entre un vector con cuatro digitos: [4 5 6 7] Famas: 1 Puntos: 1 Entre un vector con cuatro digitos: [4 5 2 0] Famas: 0 Puntos: 2 Entre un vector con cuatro digitos: [5 0 3 7] Famas: 0 Puntos: 0 Entre un vector con cuatro digitos: [2 1 6 4] Famas: 4 Puntos: 0 

30 

2. Primeros pasos en MATLAB 

Buen trabajo, felicitaciones! Lo hizo en 5 intentos 

Entre 1 para jugar mas y otro numero en caso contrario: 4 

El ejercicio consiste en comprender el programa proporcionado y en tratar de mejorarlo para que su operación sea más sencilla para el usuario. En particular, MATLAB tiene la posibilidad de utilizar menús, botones, ventanas, etc. Nosotros no exploramos esas posibilidades en estas notas. 

# 3 

# Ecuaciones no lineales 

Método de bisección Método de Newton Iteración de Punto Fijo 

Las ecuaciones no lineales de la forma f (x) = 0 aparecen frecuente­ mente en la computación cientí…ca y la mayoría exigen tratamiento numérico. El método más importante para su solución es el de New­ ton, que puede enunciarse para ecuaciones escalares o vectoriales. Para las primeras, lo estudiamos en la sección 3.2 y para las segundas lo presentamos en la sección 6.15 y lo utilizamos varias veces en estas notas. 

Además del método de Newton, comentamos también un poco so­ bre el método de bisección, que aunque lento, tiene asegurada su con­ vergencia en intervalos cerrados que contienen zeros de la función f: Además, también presentamos las iteraciones de punto …jo, de las cuales el método de Newton es un importante caso particular. 

Sobre ecuaciones no lineales hay capítulos en los principales libros de análisis numérico. En estas notas seguimos a Stewart, 1996 [29], Atkinson, 1978 [4] y Kincaid y Cheney, 1994 [21]. Sin embargo, creemos que estas notas se pueden utilizar junto con cualquier otro libro de texto de análisis numérico. 

## 3.1 Método de bisección 

Uno de los problemas más sencillos de enunciar que más motivan el estudio de los métodos numéricos, es el de encontrar los números reales x que satisfagan una ecuación de la forma 

f (x) = 0: 

32 

3. Ecuaciones no lineales 

Por ejemplo, resolver en los números reales las ecuaciones 



Las grá…cas siguientes ilustran mejor la situación. Indican que un pro­ blema con enunciado tan simple puede ser difícil de resolver: 



<!-- Start of picture text -->
3<br>x -1  sin(x)-x  tan(x)-x<br>4  4  1<br>2  2  0.5<br>0  0  0<br>-2  -2  -0.5<br>-4  -4  -1<br>-4 -2  0 2 4 -4 -2  0 2 4 -1  0  1<br><!-- End of picture text -->

La primera grá…ca sugiere que hay un único cero, precisamente donde ese cero está y las otras dos indican que hay alguno en cada caso, pero nada más. En realidad, sen(x) y x se encuentran en un único punto, x = 0; pero en cambio tan(x) y x se encuentran en un número in…nito de puntos. Ciertamente se requiere disponer de herramientas teóricas (teoremas) y prácticas (algoritmos) para resolver problemas de esta clase. 

Una de las herramientas teóricas más importantes, que sirve de base teórica al método de bisección, es el Teorema del Valor Intermedio, que enunciamos enseguida. 

Teorema 8 (Valor Intermedio) Sea f una función continua de…nida en un intervalo cerrado [a;b] y sean 



Entonces, para cada s 2 [m;M ] ; existe al menos un c 2 [a; b] tal que f (c) = s: 

El siguiente código en lenguaje de MATLAB sirve para resolver numéricamente, por el método de bisección, ecuaciones escalares de la forma f(x) = 0: En la iteración basada en la instrucción while de 

3.1. Método de bisección 33 

esta rutina, puede apreciarse la idea central del método. Más detalles pueden encontrarse en un libro de texto. 

function m1(fun,a,b) % Herramienta didactica, Carlos E. Mejia, 2002 % Uso m1(’fun’,a,b) % Se encuentra un cero de la funcion fun en el intervalo [a,b] % por el Metodo de Biseccion fprintf(’Método de Bisección nnnn’); epsi=input(’Valor para epsilon: ’); Nuit=input(’valor para número maximo de iteraciones: ’); k=1; fa=feval(fun,a); fb=feval(fun,b); if sign(fa)==sign(fb) % chequeo inicial disp(’No se cumple condición f(a)*f(b)<0’); break; end % empieza búsqueda binaria while (abs(b-a)>epsi & k < Nuit) c = (a+b)/2; if (c==a j c==b) fprintf(’Epsilon es demasiado pequeño. ’); break; end fc = feval(fun,c); if (fc==0) a = c; b = c; fa =fc; fb = fc; break; end if (sign(fc)~= sign(fb)) a = c; fa = fc; else b = c; fb = fc; end k = k + 1; end disp([’La raiz encontrada es ’,num2str(c)]); 

34 

3. Ecuaciones no lineales 

disp([’Se requirieron ’,num2str(k),’ iteraciones’]); 

Un archivo con las funciones mencionadas arriba y una más con la que se trabajará más adelante, tiene la siguiente forma: 

function y = f1(x) y = x^3-1; % y = sin(x)-x; % y = tan(x)-x; % y = cos(x)*cosh(x) +1; % y = x*exp(x)-exp(x)+1; % y = x^2-2; 

Note el símbolo de comentario % delante de las de…niciones que no se utilizan en un determinado momento. 

Para usar m1.m con este archivo, se invoca el siguiente comando en la línea de comandos de MATLAB: m1(’f1’, a, b), donde a y b son los extremos de intervalo y deben ser números reales. 

Todo ésto parece sencillo pero se requiere tener mucho cuidado. No siempre es fácil determinar un intervalo en el que la función f es con­ tinua y tiene un cero. Además, cuando f tiene varios ceros en el mismo intervalo o cuando tiene uno que es una raiz múltiple de f , también se presentan di…cultades. 

Veamos otro ejemplo: 

Encontrar las primeras cuatro raíces positivas de 

f(x) = cos(x) cosh(x) + 1: 

La siguiente grá…ca ayuda a encontrar intervalos apropiados para lla­ 

35 

3.2. Método de Newton 

mar la rutina de bisección: 



<!-- Start of picture text -->
4<br>x 10<br>2 25  500  7<br>20  400  6<br>1.5<br>15<br>300  5<br>1  10<br>200  4<br>5<br>0.5  100  3<br>0<br>0  2<br>0  -5<br>-100  1<br>-10<br>-0.5<br>-15  - 200  0<br>-1  -20  - 300  -1<br>1  1.5  2 4  4.5  5 7  7.5  8 10  11  12<br><!-- End of picture text -->

Las cuatro raíces pedidas son, aproximadamente, 1.8751, 4.6941, 7.8548 y 10.9955. Posiblemente ya notó que esta función oscila y su am­ plitud crece mucho. Funciones como ésta no delatan su comportamiento cuando se gra…can en intervalos extensos. Utilice un computador para convencerse. 

## 3.2 Método de Newton 

En esta segunda sección sobre ecuaciones no lineales de la forma f (x) = 0, comentamos acerca del Método de Newton, su convergencia cuadrática (en muchos casos, no en todos desafortunadamente) y su derivación del Teorema de Taylor. El método en efecto, se debe a Newton (1642-1727), a quien se debe también, junto con Leibniz (1646-1716), la invención del cálculo. 

Según el Teorema de Taylor, para f dos veces continuamente dife­ 

3. Ecuaciones no lineales 

36 

renciable en un intervalo que contiene a x y x0, 



donde ¹ está entre x y x0: 

Supongamos que x ¹ es tal que f (¹x) = 0: Si x0 está cerca de x ¹ y jf<sup>00</sup> (x0)j no es demasiado grande, entonces la función 



es una buena aproximación de f (x) en una vecindad de x: ¹ A f<sup>¹</sup> (x) se le llama linealización de f (x) en x0; pues es la ecuación de la recta tangente a la curva y = f (x) en el punto (x0; f (x0)). 

Finalmente, sería bueno que x ¹ se pudiera aproximar por medio de la solución de f<sup>¹</sup> (x) = 0; que es muy fácil de obtener, siempre que f<sup>0</sup> (x0) sea no nula. Dicha solución es simplemente, 



Afortunadamente, este razonamiento conduce a un efectivo método ite­ rativo para obtener soluciones de la ecuación f (x) = 0: El método se llama de Newton o de Newton - Raphson y se de…ne asi: 



El siguiente M-archivo sirve para resolver ecuaciones de la forma f (x) = 0 por el método de Newton. 

function out = m2(fun,fprima,x0) 

- % Herramienta didactica, Carlos E. Mejia, 2002 

- % Uso z = m2(’fun’,’fprima’,x0); 

- % Se aproxima un cero de f por el Metodo de Newton 

- % Las funciones f y f’ estan dadas por los M-archivos fun 

y 

- % fprima respectivamente. x0 es la primera aproximacion fprintf(’Método de Newton nnnn’); 

3.2. Método de Newton 37 epsi=input(’Valor para epsilon: ’); Nuit=input(’Valor para número maximo de iteraciones: ’); v=feval(fun,x0);vp=feval(fprima,x0); disp(’ k x f(x) ’); out=[0,x0,v]; fprintf(’%4.0f %8.3e %8.3enn’,out); for k=1:Nuit x1=x0-v/vp; v=feval(fun,x1);vp=feval(fprima,x1); out=[k,x1,v]; fprintf(’%4.0f %8.3e %8.3enn’,out); if (abs(x1-x0)<epsi j abs(v)<epsi) break end x0=x1; end 

Para ejecutar este archivo con cada una de las funciones de…nidas en el M-archivo f1.m, se requiere de otro M-archivo f2.m con las derivadas. El archivo f1.m que proponemos como ejemplo, lo listamos arriba en la sección 3.1. Nótese que utilizamos el signo de comentario % para inhabilitar las funciones que no se requieren en cada experimento. 

El archivo de derivadas correspondiente a f1.m es 

function y = f2(x) % Derivadas de funciones en M-archivo f1.m y = 3*x^2; % y = cos(x)-1; % y = sec(x)^2-1; % y = cos(x)*sinh(x) - sin(x)*cosh(x); % y = x*exp(x)+exp(x)-exp(x); % y = 2*x; 

Supongamos que queremos aproximar uno de los ceros de la función f (x) = cos(x) cosh(x) + 1: Entonces ponemos los signos de comentario % donde corresponden en f1.m y f2.m e invocamos z = m2(’f1’,’f2’,8); en la línea de comandos de MATLAB. Si proponemos una tolerancia epsi = 1.e-8 y un número máximo de iteraciones = 30, obtenemos: 

38 

3. Ecuaciones no lineales 

|k xk|f (xk)|
|---|---|
|0 8.00000000e+000|-2.15864768e+002|
|1 7.87238132e+000|-2.31372508e+001|
|2 7.85506067e+000|-3.91280475e-001|
|3 7.85475753e+000|-1.18472167e-004|
|4 7.85475744e+000|-1.03985709e-011|



### 3.2.1 Ejercicios 

Trate de practicar con estas rutinas o con otras parecidas para resolver los siguientes ejercicios: 

1. Resuelva el problema anterior con x0 = 7: Obtiene lo que espera? Es correcto el resultado que obtiene? 

2. Busque ceros de la función f(x) = tan(x) ¡ x que sean cercanos a 

100: 

Respuesta: Los más cercanos son, aproximadamente, 98.9500628 y 102.091966. Trate de no usar esta información para que experimente en condiciones normales. 

### 3.2.2 Análisis de Convergencia Local 

Si la primera aproximación x0 es su…cientemente cercana al cero x ¹ de f y si f<sup>0</sup> (¹x) = 0; entonces el método de Newton converge. La primera condición es la que nos obliga a decir que el análisis que presentamos es de caracter local. La segunda condición es válida únicamente para raíces simples de f; es decir, para raíces cuya multiplicidad algebraica es 1: 

Para simpli…car el análisis de convergencia, suponemos que f tiene derivadas de todos los órdenes. Sea 



Entonces 



La función g es la función de iteración del método de Newton. Cumple 



39 

3.2. Método de Newton 

Por tal motivo, se dice que x¹ es un punto …jo de g y que el método de Newton es un método de punto …jo. Posteriormente diremos más sobre iteraciones de punto …jo. 

De…nimos 



Este es el error cometido al aproximar al cero exacto con el iterado xk: La convergencia se da cuando 



Además, en algunos casos, como el que nos ocupa, por ejemplo, se puede decir qué tan rápida es dicha convergencia. De (3.1) y (3.2), 



y por Teorema de Taylor, 



con ¯ k<sup>un número entre xk y x:¹Es decir,</sup> 

De otro lado, 



pero como f (¹x) = 0 y f<sup>0</sup> (¹x) = 0; entonces g<sup>0</sup> (¹x) = 0: Por continuidad de g<sup>0</sup> en x; ¹ para todo 0 < C < 1; existe ± > 0 tal que si 0 < jx ¡ x¹j < ± entonces jg<sup>0</sup> (x) ¡ g<sup>0</sup> (¹x)j = jg<sup>0</sup> (x)j · C < 1: Por tanto, debemos escoger x0 que cumpla jx0 ¡ x¹j < ±: Como ¯ 0<sup>está entre x</sup> 0<sup>y</sup> x;<sup>¹</sup> entonces 



¹ De aqui, jx1 ¡ xj < ±; lo que indica que este argumento se puede repetir. Llegamos a 



40 

3. Ecuaciones no lineales 

Por inducción, 



Para saber qué tan rápida es esta convergencia, usamos Teorema de Taylor para g; teniendo en cuenta que g<sup>0</sup> (¹x) = 0: Es decir, 



donde ´ k<sup>está entre xk y x: ¹Esto lo reescribimos asi:</sup> 



De aqui encontramos que 



Un proceso iterativo en el que la sucesión de errores cumple 



se dice que es cuadráticamente convergente. 

## 3.3 Iteraciones de punto …jo 

En esta tercera parte sobre ecuaciones no lineales de la forma f (x) = 0, exponemos algunas ideas y proponemos algunos ejemplos sobre itera­ ciones de punto …jo. Tales iteraciones fueron brevemente introduci­ das a través del Método de Newton, que es un método de punto …jo. Recordemos que si 



entonces 



41 

3.3. Iteraciones de punto …jo 

es la presentación como iteración de punto …jo del método de Newton. Muchas veces, un problema de la forma f (x) = 0 se puede enunciar como un problema de punto …jo de la forma x = g(x): Con un ejemplo sencillo se comprende mejor. 

Ejemplo 9 Se quieren encontrar los ceros de los polinomios p (x) = x2 ¡ 5x + 6 y q (x) = x<sup>3</sup> ¡ 13x + 18 resolviendo un problema de punto …jo asociado. 

Para el polinomio p; se proponen las siguientes: 



Note que x = gj (x) si y solo si p (x) = 0: 

El siguiente M-archivo ofrece la posibilidad de ensayar estas cuatro funciones de iteración. 

function out = m3(f_fun,g_fun,s,x0) % Herramienta didactica, Carlos E. Mejia, 2002 % Uso z = m3(’f_fun’,’g_fun’,s,x0); % Se aproxima el cero s de f_fun por medio de una % iteracion de punto fijo con funcion de iteracion g_fun % x0 es la primera aproximacion % El cero s es conocido pero no se utiliza en el proceso % iterativo. Solo se usa para listar las dos ultimas % columnas de la tabla de resultados fprintf(’Método de Punto Fijo nnnn’); epsi=input(’Valor para epsilon: ’); Nuit=input(’Valor para número maximo de iteraciones: ’); v=feval(f_fun,x0);e0=s-x0; disp(’ k x_k f(x_k) e_k e_k)/e_(k-1))’); out=[0,x0,v,e0]; fprintf(’%4.0f %8.3e %8.3e %8.3enn’,out); for k=1:Nuit x1=feval(g_fun,x0); 

42 3. Ecuaciones no lineales v=feval(f_fun,x1); e1=s-x1; out=[k,x1,v,e1,e1/e0]; fprintf(’%4.0f %8.3e %8.3e %8.3e %8.3enn’,out); if (abs(x1-x0)<epsi abs(v)j <epsi) break end x0=x1;e0=e1; end Las funciones f y gj están dadas en M-archivos como los siguientes: function z = f(x); % Funcion f_fun iteracion de punto fijo % z=x^2-5*x+6; z=x^3-13*x+18; function z = g(x); % funcion g_fun de iteracion de punto fijo % z = x^2-4*x+6; % z = 5-6/x; % z = (5*x-6)^(1/2); % z = (x^2+6)/5; % % z = x^3-12*x+18; % z = (x^3+18)/13; % z = (13*x-18)^(1/3); z = (13*x-18)/x^2; 

Para aproximar el cero s = 2 del primer polinomio, utilizamos el M-archivo propuesto. Siempre utilizamos una tolerancia epsi = 10<sup>¡8</sup> : Para la función g1 con un máximo de 10 iteraciones, los resultados son: 

43 

3.3. Iteraciones de punto …jo 

|k|xk|f (xk)|ek|ek=ek<br>1<br>¡|
|---|---|---|---|---|
|0|0.00e+000|6.00e+000|2.00e+000||
|1|6.00e+000|1.20e+001|-4.00e+000|-2.00e+000|
|2|1.80e+001|2.40e+002|-1.60e+001|4.00e+000|
|3|2.58e+002|6.53e+004|-2.56e+002|1.60e+001|
|4|6.55e+004|4.29e+009|-6.55e+004|2.56e+002|
|5|4.29e+009|1.84e+019|-4.29e+009|6.55e+004|
|6|1.84e+019|3.40e+038|-1.84e+019|4.29e+009|
|7|3.40e+038|1.16e+077|-3.40e+038|1.84e+019|
|8|1.16e+077|1.34e+154|-1.16e+077|3.40e+038|
|9|1.34e+154|Inf|-1.34e+154|1.16e+077|
|10|Inf|NaN|-Inf|Inf|



Ciertamente no hay convergencia. Para la función g2 con un máximo de 20 iteraciones, se encuentra: 

|k|xk|f (xk)|ek|ek=ek<br>1<br>¡|
|---|---|---|---|---|
|0|0.00e+000|6.00e+000|2.00e+000||
|1|-Inf|Inf|Inf|Inf|
|2|5.00e+000|6.00e+000|-3.00e+000|0.00e+000|
|.|...|...|...|...|
|10|3.03e+000|2.74e-002|-1.03e+000|9.87e-001|
|.|...|...|...|...|
|15|3.00e+000|3.45e-003|-1.00e+000|9.98e-001|
|.|...|...|...|...|
|20|3.00e+000|4.52e-004|-1.00e+000|1.00e+000|



Es decir, hay convergencia, pero a otro cero de p: Otro ensayo con g2<sup>y un máximo de 10 iteraciones:</sup> 

|k|xk|f (xk)|ek|ek=ek<br>1<br>¡|
|---|---|---|---|---|
|0|1.99e+000|1.01e-002|1.00e-002||
|4|1.95e+000|5.56e-002|5.28e-002|1.53e+000|
|8|1.66e+000|4.56e-001|3.40e-001|1.67e+000|
|10|6.69e-001|3.10e+000|1.33e+000|2.17e+000|



44 

3. Ecuaciones no lineales 

De…nitivamente, aproximar el cero s = 2 por este medio no parece fácil. Tratemos con g3 y un máximo de 10 iteraciones: 

|k|xk|f (xk)|ek|ek=ek<br>1<br>¡|
|---|---|---|---|---|
|0|0.00e+000|6.00e+000|2.00e+000||
|4|3.58e+000|-2.11e+000|-1.58e+000|8.17e-001|
|8|3.43e+000|4.21e-001|-1.43e+000|9.16e-001|
|10|3.29e+000|3.13e-001|-1.29e+000|9.43e-001|



Tampoco se ve promisorio. Finalmente, con g4 y un máximo de 30 iteraciones, se obtiene: 

|k|xk|f (xk)|ek|ek=ek<br>1<br>¡|
|---|---|---|---|---|
|0|0.00e+000|6.00e+000|2.00e+000||
|5|1.81e+000|2.33e-001|1.95e-001|7.48e-001|
|10|1.95e+000|5.75e-002|5.45e-002|7.86e-001|
|20|1.99e+000|5.55e-003|5.52e-003|7.99e-001|
|25|2.00e+000|1.80e-003|1.80e-003|8.00e-001|
|30|2.00e+000|5.89e-004|5.89e-004|8.00e-001|



Aqui se observa convergencia. 

Este ejemplo simple nos invita a re‡exionar acerca de condiciones su…cientes para convergencia de una iteración de punto …jo y también acerca del cociente de errores consecutivos presentado en la última columna, que nos sugiere tendencia a ser constante en caso de haber convergencia. Todo ésto lo aclararemos próximamente, pero antes pro­ ponemos el siguiente ejercicio: 

## 3.4 Ejercicio 

¡ Para el polinomio q (x) = x<sup>3</sup> 13x +18 presentado antes, considere las siguientes funciones de iteración de punto …jo y decida cuáles permiten 

45 

3.5. Análisis de convergencia local 

aproximar el cero s = 2: Realice 5 iteraciones de punto …jo con cada una de las funciones admisibles. 



## 3.5 Análisis de convergencia local 

En esta sección sobre ecuaciones no lineales de la forma f (x) = 0, exponemos teoría de convergencia local para iteraciones de punto …jo. Recordemos que los ejemplos presentados antes, nos invitan a re‡exionar acerca de condiciones su…cientes para convergencia de una iteración de punto …jo y también acerca del cociente de errores consecutivos pre­ sentado en la última columna, que nos sugiere tendencia a ser constante en caso de haber convergencia lineal. 

En lugar de empezar con una ecuación de la forma f (x) = 0; lo hacemos con una función g que tiene un punto …jo s: Es decir, tal que s = g (s) : Nos preguntamos cuándo y cómo converge la iteración 



Para nadie es sorpresa que es la derivada de g en el punto …jo la que determina si hay o no convergencia. Para hacer el análisis más sencillo, suponemos que g tiene un número su…ciente de derivadas continuas. El resultado central es el siguiente: 

Teorema 10 (Teorema de Convergencia Local) Si jg<sup>0</sup> (s)j < 1; entonces hay un intervalo I± = [s ¡ ±; s + ±] tal que la iteración (3.4) converge a s siempre que x0 2 I±: Si g<sup>0</sup> (s) = 0; entonces la convergen­ cia es lineal con rata de convergencia g<sup>0</sup> (s): Si 



entonces la convergencia es de orden p: 

dem: 

46 

3. Ecuaciones no lineales 

No es sorprendente que el argumento presentado para demostrar la convergencia del Método de Newton, que es un método de Punto Fijo, nos sea útil de nuevo aquí. Lo repetimos por considerarlo de interés. De…nimos ek = xk ¡ s: Por Teorema de Taylor, 



donde ¹ k<sup>está entre xk y s: Por tanto,</sup> 



Sea C una constante positiva tal que jg<sup>0</sup> (s)j < C < 1: Por continuidad ¡ de g<sup>0</sup> ; para " = C jg<sup>0</sup> (s)j ; existe ± tal que jg<sup>0</sup> (x) ¡ g<sup>0</sup> (s)j · " siempre que 0 < jx ¡ sj < ±: De aqui obtenemos jg<sup>0</sup> (x)j · " + jg<sup>0</sup> (s)j = C < 1 para todo x 2 I±: 

Sea I± = [s ¡ ±; s + ±] : Veamos que si x0 2 I±; la iteración de punto …jo xk+1 = g(xk) es convergente. Por (3.6), 



Como ¹ 0<sup>está entre x0 y s; entonces está en I±: Luego</sup> 



Esto indica que x1 2 I±: Similarmente, 



con ¹ 1<sup>entre x1 y s; o sea en I±: Luego de (3.7),</sup> 

je2j · C je1j · C<sup>2</sup> je0j < C<sup>2</sup> ± < ±: 

Esto indica que x2 2 I±: Con este procedimiento, llegamos a que 



y por tanto 



o sea, la iteración es convergente. Más aun, si g<sup>0</sup> (s) = 0; hay una vecindad de s en la que g<sup>0</sup> no se anula. Sin pérdida de generalidad, 

47 

3.6. Ejemplos 

podemos suponer que tal vecindad es el intervalo I± con el que hemos venido trabajando. Entonces podemos escribir 



para algún ¹ k entre xk y s: Por convergencia, lim ¹ k = s y de nuevo k!1 por continuidad de g<sup>0</sup> ; lim g<sup>0</sup> (¹ k<sup>)= g0 (s) : Por tanto</sup> k!1 



Qué pasa si existe p > 1 tal que 



De nuevo, invocamos el Teorema de Taylor para obtener 



con ¹ k<sup>entre xk y s: Con el procedimiento que usamos arriba, vemos</sup> que 



Es decir, la convergencia es de orden p: 

## 3.6 Ejemplos 

La iteración de Newton para raíces simples tiene convergencia al menos, cuadrática. 

En efecto, si s es una raíz simple de f; entonces f (s) = 0 pero f<sup>0</sup> (s) 6= 0: Sea 



Entonces, 



48 

3. Ecuaciones no lineales 

De aqui se concluye que el orden de convergencia es 2 si f<sup>(2)</sup> (s) = 0 y es más de 2 si f<sup>(2)</sup> (s) = 0: El M-archivo m4.m contiene el cálculo de errores y cocientes de errores consecutivos para la iteración de Newton. Es una modi…cación menor del M-archivo m2.m. 

function out = m4(f_fun,f_prima,s,x0) % Herramienta didactica, Carlos E. Mejia, 2002 % Uso z = m4(’f_fun’,’f_prima’,s,x0); % Se aproxima el cero s de f_fun por medio de la % iteracion de punto fijo con funcion de % iteracion dada por Metodo de Newton % x0 es la primera aproximacion % El cero s es conocido pero no se utiliza en el proceso % iterativo. Solo se usa para listar las dos ultimas % columnas de la tabla de resultados % ultima columna ilustra la convergencia cuadratica fprintf(’Método de Newton y convergencia cuadraticannnn’); epsi=input(’Valor para epsilon: ’); Nuit=input(’Valor para número maximo de iteraciones: ’); v=feval(f_fun,x0);vp=feval(f_prima,x0);e0=s-x0; disp(’ k x_k f(x_k) e_k e_k/(e_(k-1)) e_k/(e_(k-1))^2’); out=[0,x0,v,e0]; fprintf(’%4.0f %8.4e %8.4e %8.4enn’,out); for k=1:Nuit x1=x0-v/vp; v=feval(f_fun,x1);vp=feval(f_prima,x1); e1=s-x1; out=[k,x1,v,e1,e1/e0,e1/e0^2]; fprintf(’%4.0f %8.4e %8.4e %8.4e %8.4e %8.4enn’,out); if (abs(x1-x0)<epsi abs(v)j <epsi) break end x0=x1;e0=e1; end 

Veamos su ejecución para tres ejemplos de los listados en el M-archivo f1.m. En todos los casos, usamos 1.e-6 como valor de epsilon y un 

49 

3.6. Ejemplos 

máximo de 20 iteraciones. 

> 2 ¡ 1. Aproximación del cero s =<sup>~~p~~</sup> 2 de la función f(x) = x 2 por el Método de Newton. 

|k|xk|f (xk)|ek|ek=ek<br>1<br>¡|ek= (ek<br>1<sup>)2 </sup><br>¡|
|---|---|---|---|---|---|
|0|50|2.5e+003|-4.9e+001|||
|1|25.0200|6.2e+002|-2.4e+001|4.9e-001|-1.0e-002|
|2|12.5500|1.6e+002|-1.1e+001|4.7e-001|-2.0e-002|
|3|6.3547|3.8e+001|-4.9e+000|4.4e-001|-4.0e-002|
|4|3.3347|9.1e+000|-1.9e+000|3.9e-001|-7.9e-002|
|5|1.9672|1.9e+000|-5.5e-001|2.9e-001|-1.5e-001|
|6|1.4919|2.3e-001|-7.8e-002|1.4e-001|-2.5e-001|
|7|1.4162|5.7e-003|-2.0e-003|2.6e-002|-3.4e-001|
|8|1.4142|4.1e-006|-1.4e-006|7.1e-004|-3.5e-001|
|9|1.4142|2.1e-012|-7.4e-013|5.1e-007|-3.5e-001|



La última columna sugiere convergencia cuadrática. Pero solamente el análisis teórico puede asegurarla. 

¡ 2. Aproximación del cero s = 0 de la función f (x) = xe<sup>x</sup> e<sup>x</sup> + 1: Nótese que s = 0 es un cero de multiplicidad 2 y que no debemos esperar convergencia cuadrática. 

|k|xk|f (xk)|ek|ek=ek<br>1<br>¡|ek= (ek<br>1<sup>)2 </sup><br>¡|
|---|---|---|---|---|---|
|0|2.0000|8.4e+000|-2.0e+000|||
|1|1.4323|2.8e+000|-1.4e+000|7.2e-001|-3.6e-001|
|2|0.9638|9.1e-001|-9.6e-001|6.7e-001|-4.7e-001|
|.|...|...|...|...|...|
|8|0.0276|3.9e-004|-2.8e-002|5.1e-001|-9.4e+000|
|9|0.0139|9.8e-005|-1.4e-002|5.0e-001|-1.8e+001|
|10|0.0070|2.5e-005|-7.0e-003|5.0e-001|-3.6e+001|
|11|0.0035|6.1e-006|-3.5e-003|5.0e-001|-7.2e+001|
|12|0.0018|1.5e-006|-1.8e-003|5.0e-001|-1.4e+002|
|13|0.0009|3.8e-007|-8.8e-004|5.0e-001|-2.9e+002|



50 

3. Ecuaciones no lineales 

La penúltima columna sugiere convergencia lineal. La última no invita a pensar en convergencia cuadrática. De todas maneras, como lo dijimos antes, los experimentos nunca son la última palabra. 

Estos dos ejemplos sugieren la preparación de tablas con cocientes de errores consecutivos para tratar de encontrar patrones que después conduzcan a a…rmaciones matemáticas generales. Tales patrones no siempre se encuentran, como en el siguiente caso: 

3. Aproximar el cero s = 1 de la función x 3 ¡ 1: 

|k xk|f (xk)|ek|ek=ek<br>1<br>¡|ek= (ek<br>1<sup>)2 </sup><br>¡|
|---|---|---|---|---|
|0 3.0000|2.6e+001|-2.0e+000|||
|1 2.0370|7.5e+000|-1.0e+000|5.2e-001|-2.6e-001|
|2 1.4384|2.0e+000|-4.4e-001|4.2e-001|-4.1e-001|
|3 1.1200|4.1e-001|-1.2e-001|2.7e-001|-6.2e-001|
|4 1.0124|3.8e-002|-1.2e-002|1.0e-001|-8.6e-001|
|5 1.0002|4.5e-004|-1.5e-004|1.2e-002|-9.8e-001|
|6 1.0000|6.9e-008|-2.3e-008|1.5e-004|-1.0e+000|



Ninguna de las dos últimas columnas ofrece mayor información como para buscar un orden dado de convergencia. En este caso, la conver­ gencia es cuadrática, pues se trata de un cero simple. 

## 3.7 Ejercicios suplementarios 

1. Trate de encontrar todos los ceros de f (x) = cos (x) ¡ cos (3x) por un procedimiento grá…co o analítico. Enseguida utilice un método numérico para aproximar los ceros que se encuentran en ¡ 

el intervalo [ 2¼; 2¼] : 

2. Argumente por medios grá…cos que la ecuación x = tan (x) tiene in…nitas soluciones. Conjeture el valor de dos de esas soluciones y con…rme su conjetura con un método numérico. 



51 

#### 3.7. Ejercicios suplementarios 

raíz. Después, por un procedimiento analítico, demuestre que, en efecto, puede haber a lo más una. Finalmente, con un procedi­ miento grá…co o un método numérico, aproxime la raíz. En este caso, el siguiente teorema puede servir como el procedimiento analítico requerido: 

Teorema: Sea f una función continuamente diferenciable en (a; b) : Si f<sup>0</sup> (x) > 0 para todo x 2 (a; b) ; entonces f tiene a lo más un cero en el intervalo (a; b) : 

Este teorema es una consecuencia del Teorema del Valor Medio para Derivadas. Trate de demostrarlo. 

4. Encuentre el punto de corte de las grá…cas y = 3x y y = ex: 

5. Utilice medios grá…cos para aproximar la localización de los ceros de la función log (1 + x) + tan (2x) : Utilice un método numérico para aproximar dos de esos ceros. 

6. Escriba el método de Newton para determinar el recíproco de la raíz cuadrada de un número positivo. Realice dos iteraciones del método para aproximar 1=§ ~~p~~ 4 empezando en x0 = 1 y x0 = ¡1: Sugerencia: Enuncie el método de Newton para encontrar los 1 

ceros de f (x) = x<sup>2</sup> y simplifíquelo. ¡ 4 

- 4 ¡ 

- 7. Dos de los ceros de x + 2x<sup>3</sup> 7x<sup>2</sup> + 3 son positivos. Aproxímelos por el método de Newton. 

8. La ecuación x ¡ Rx<sup>¡1</sup> = 0 tiene a x = §R<sup>1=2</sup> como solución. Establezca el método de Newton para esta ecuación, simplifíquelo y calcule los primeros 5 iterados para R = 25 y x0 = 1: 

9. ¿Cuál es la recta y = ax + b que más se aproxima a sen (x) cerca de x = ¼=4? ¿Por qué está relacionada esta pregunta con el método de New­ ton? 

Sugerencia: Considere la expansión en serie de Taylor de sen (x) alrededor de x = ¼=4: 

10. Utilice dos métodos numéricos diferentes para aproximar log (2) : ¡ 

Sugerencia: Piense en la ecuación e<sup>x</sup> 2 = 0: 

52 

3. Ecuaciones no lineales 

11. Considere la ecuación x ¡ 2sen (x) = 0: a. Muestre grá…camente que esta ecuación tiene exactamente tres raíces en el intervalo (¡2; 2): Son 0 y una en cada uno de los in­ tervalos (¼=2; 2) y (¡2; ¡¼=2) : 

b. Muestre que la iteración de punto …jo xn+1 = 2sen (xn) con­ verge a la raíz en (¼=2; 2) para cualquier x0: c. Utilice el método de Newton para aproximar este mismo cero. Compare la rapidez de convergencia en las partes a. y b. 

- 2 ¡ 

- 12. Considere la ecuación x 2x + 2 = 0: Por medio de ensayos con varios valores x0; estudie el comportamiento del método de Newton ante esta igualdad. Comentario: Como x2 ¡ 2x + 2 = (x ¡ 1)<sup>2</sup> + 1 > 0; no hay un número real que cumpla esta igualdad. 

## 3.8 Examen de entrenamiento 

Resuelva estos ejercicios sin consultar libros ni notas de clase para darse una idea del nivel de preparación que ha obtenido hasta ahora. Una calculadora sencilla es lo mínimo que debe tener a disposición y es su…ciente para poder responder todos los ejercicios del examen. Claro que es preferible si dispone de una calculadora gra…cadora o un computador. 

1. Considere la función f (x) = e 2x + 3x + 2: 

   - a. Demuestre que f tiene una raíz en [¡2; 0] : 

   - b. Demuestre que este es el único cero de f: Sugerencia: Utilice el teorema que se sugirió en el Ejercicio Su­ plementario número 3. 

   - ¡ 

   - c. Con x = 1 como primera aproximación, calcule los primeros tres iterados del método de bisección y del método de Newton para aproximar la raíz de f: 

2. Sea f (x) = (x ¡ 1)<sup>2</sup> : Muestre que la derivada de f en 1 es 0; pero los iterados del método de Newton convergen a 1: ¿Qué puede decir de la rata de convergencia? 

53 

3.8. Examen de entrenamiento 





Sugerencia: Sea x0 = 0 y considere g (x) =<sup>~~p~~</sup> 3 6 + x: El número s es un punto …jo de la función g: 

4. Como un caso extremo de una función para la cual el método de Newton converge lentamente, considere f (x) = (x ¡ a)<sup>n</sup> ; para n un entero positivo y a un número real. Muestre que el método de Newton genera la sucesión 



y que dos errores consecutivos satisfacen la relación 



¿Por qué motivo esta relación sugiere que la convergencia es lenta? 

54 3. Ecuaciones no lineales 

# 4 

# Interpolación 

Tablas Teorema fundamental Forma de Newton (Diferencias divididas) Forma de Lagrange 

## 4.1 Tablas 

Uno de los procedimientos más útiles en el procesamiento de infor­ mación es el de construir curvas con base en unos cuantos puntos de referencia Pj con coordenadas (xj; yj) dados en una tabla de la forma 

|j|0|1|¢ ¢ ¢|n||
|---|---|---|---|---|---|
|xj|x0|x1|¢ ¢ ¢|xn|(4.1)|
|yj|y0|y1|¢ ¢ ¢|yn||



Las curvas obtenidas representan y aproximan la información puntual y con las debidas precauciones, se usan frecuentemente en lugar de los datos originales. Si la curva que se construye pasa por todos los puntos de la tabla, se denomina una interpolación. Si la curva no tiene que pasar por los puntos pero satisface un cierto criterio de cercanía, se denomina una aproximación a los datos de la tabla. Los criterios de cercanía son procedimientos de optimización entre los cuales el más común es posiblemente el de mínimos cuadrados. 

Ejemplo 11 El Departamento Nacional de Estadística de la República de Colombia, DANE, publica en su página <http://www.dane.gov.co>, que el total de exportaciones del país, en millones de dólares, entre 1996 y 2000, está dado por la siguiente tabla: 

|Año|1996|1997|1998|1999|2000|
|---|---|---|---|---|---|
|Total|10648|11549|10866|11617|13115|



56 

4. Interpolación 

Tres diferentes interpolaciones obtenidas por medio del M-archivo m5.m, están dadas en la siguiente …gura: 



<!-- Start of picture text -->
x 10  4  Exportaciones de Colombia 1996-2000<br>1.35<br>1.3<br>1.25<br>1.2<br>1.15<br>1.1<br>1.05<br>0  5  10  15  20  25  30  35  40  45<br><!-- End of picture text -->

Por su parte, el M-archivo m5.m es: 

% Herramienta didactica, Carlos E. Mejia, 2002 % uso: m5 

% tres clases de interpolacion ofrecidas por MATLAB x=1996:2000;xp=1996:.1:2000; y=[10648 11549 10866 11617 13115]; y1=interp1(x,y,xp,’linear’); grid on;hold on; plot(y1,’k+’); title(’Exportaciones de Colombia 1996-2000’); y2=interp1(x,y,xp,’cubic’); plot(y2,’k’); y3=interp1(x,y,xp,’spline’); plot(y3,’k--’); print -deps2 .nfignm5.eps 

57 

4.2. Teorema fundamental 

Los tres métodos de interpolación utilizados son: linear, que signi…ca que los puntos se unen por medio de rectas, cubic, que construye un polinomio cúbico que pasa por los puntos y spline, que es una interpo­ lación cúbica segmentaria. Cada segmento es un polinomio cúbico que se une suavemente con el vecino, o sea que su valor y los de sus dos primeras derivadas en el punto de encuentro, concuerdan con los del vecino. 

## 4.2 Teorema fundamental 

Pasamos ahora a considerar algunas ideas teóricas sobre interpolación, encabezadas por el teorema fundamental de interpolación polinómica que garantiza existencia y unicidad del polinomio interpolante. Cualquier libro de texto de análisis numérico incluye este material. Aquí seguimos a Stewart, 1996 [29], Atkinson, 1978 [4] y Kincaid y Cheney, 1994 [21]. 

La idea de aproximar es central en el modelamiento matemático. Aquí queremos presentar una aproximación particular que es interpo­ latoria de una tabla dada, es decir, la función resultante satisface la tabla. Pero antes veamos que hay aproximaciones no interpolatorias y que en muchas ocasiones son las únicas disponibles. 

Consideremos la siguiente tabla: 

|j 0|1|2|3||
|---|---|---|---|---|
|xj 1|2|3|4|(4.2)|
|yj 1|1/2|1/3|1/4||



entonces podemos pretender conseguir funciones de muy diversas clases para aproximarla. 

### 4.2.1 Intento 1 

Una recta, llamada recta de regresión, que se consigue por aproximación de mínimos cuadrados. 

Nótese que buscar interpolación con una recta es imposible, pues tal recta debería ser de la forma f (x) = ax + b con f (xj) = yj para 

58 

4. Interpolación 

j = 0; 1; 2; 3: Esto lleva al sistema 

ax0 + b = y0 ax1 + b = y1 ax2 + b = y2 ax3 + b = y3 

que es contradictorio. 

3 Se busca entonces una recta f (x) = ax+b tal que<sup>P</sup> [f (xj ) ¡ yj ]2 sea j=0 mínimo. Esta recta se consigue con el siguiente M-archivo, que produce la …gura que se incluye a continuación. 

% Herramienta didactica, Carlos E. Mejia, 2002 

% sistema redundante % uso: redun A=[1 1; 2 1;3 1; 4 1]; y=[1; 1/2;1/3; 1/4]; x=Any p=x’ % en forma de polinomio z=1:3/100:4; plot(z,1./z,’r’,z,polyval(p,z),’k--’); title(’Curva 1/x y recta de regresión, x=1:4’); print -deps2 .nfignredun.eps 



<!-- Start of picture text -->
Curva 1/x y recta de regresión, x=1:4<br>1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>1  1.5  2 2.5  3 3.5  4<br><!-- End of picture text -->

59 

4.2. Teorema fundamental 

Digno de mencionarse es que, para MATLAB, un polinomio es un vector …la, el vector de sus coe…cientes. Las operaciones entre poli­ nomios, están de…nidas en MATLAB con esa convención. Por ejemplo, la instrucción polyval que se usa en el M-archivo de arriba, sirve para evaluar un polinomio en los elementos de un vector. También es im­ portante saber más de la instrucción x = Any: Cuando los tamaños de las matrices involucradas son compatibles, esta instrucción entrega la solución del sistema lineal 

Ax = y; 

ya sea la única, en caso de haber una sola o la de mínimos cuadrados. La simplicidad de esta instrucción y la calidad de las rutinas MATLAB que la respaldan, son dos de las razones para que este software sea tan exitoso. La ayuda en línea de MATLAB puede ayudar a completar esta información. 

### 4.2.2 Intento 2 

Un polinomio de grado mínimo, en este caso 3, que sea interpolante. El grado está determinado por el número de parejas de datos disponibles. Como hay 4, se busca un polinomio de grado 3 que tiene 4 coe…cientes por encontrar. Más precisamente: 

Queremos hallar a; b; c; d tales que el polinomio 

p(x) = a + b(x ¡ 1) + c(x ¡ 1)(x ¡ 2) + d(x ¡ 1)(x ¡ 2)(x ¡ 3) (4.3) 

sea tal que p(xj) = yj ; j = 0; 1; 2; 3: La escritura del polinomio inter­ polante en esta forma es cómoda para evaluaciones y es la que después llamaremos forma de Newton. Para resolver a mano este problema, acudimos al método de los coe…cientes indeterminados. Consiste en utilizar evaluaciones del polinomio (4.3) en las abscisas de la tabla para formar un sistema de ecuaciones en el que las incógnitas son los coe…cientes a; b; c; d: Veamos el uso del método para el polinomio 

60 

4. Interpolación 

interpolante de la tabla (4.2). 



Para resolver el problema con MATLAB, preparamos el M-archivo pol3.m, que incluimos a continuación junto con la grá…ca que produce. 

% pol3, Herramienta didactica, Carlos E. Mejia, 2002 z=1:3/100:4; x=[1 2 3 4]’;y=1./x; polin=interp1(x,y,z,’cubic’); plot(z,1./z,’k’,z,polin,’k--’); set(gca,’XTick’,x’),grid on axis([1 4 0 1]), set(gca,’YTick’,[1/4 1/3 1/2 1]), title(’1/x (-) y cúbico interpolante (--)’); print -deps2 .nfignpol3.eps 

61 

4.2. Teorema fundamental 



<!-- Start of picture text -->
1/x (-) y cúbico interpolante (--)<br>1<br>0.5<br>0.3333<br>0.25<br>1 2 3 4<br><!-- End of picture text -->

La interpolación polinomial esta respaldada por el siguiente teorema de existencia y unicidad. 

Teorema 12 Dada una tabla con abscisas xj (todas diferentes) y or­ denadas yj; j = 0; 1; 2; :::; n; existe un único polinomio p de grado a lo más n tal que 



dem: 

Unicidad 

Supongamos que hay dos polinomios q y r que satisfacen (7.2). El polinomio q ¡ r es tal que (q ¡ r)(xj) = 0 para j = 0; 1; :::; n: Es decir, tiene grado a lo más n y sin embargo cuenta con n + 1 raíces. Esto obliga a que sea el polinomio nulo o sea que q = r: 

Existencia 

Inducción sobre n : 

n = 0 : La función x0 ! y0 se interpola con el polinomio constante p(x) = y0: 

Supongamos que hay polinomio interpolante pk¡1<sup>de gradok</sup> ¡ 1 ¡ para los datos (xj ;yj); j = 0; 1; :::; k ¡ 1: Es decir, pk 1<sup>(x</sup> j<sup>)=</sup> yj ; j = 0; 1; :::; k ¡ 1: 

62 

4. Interpolación 

Consideremos el polinomio 



Por supuesto es interpolante de los datos hasta k ¡ 1; pues pk¡1<sup>lo es.</sup> Para que también interpole en xk; pedimos que 



lo cual proporciona un único valor para c: El despeje de c se puede hacer pues los xj son todos distintos por hipótesis. 

### 4.2.3 Cálculo de coeficientes 

La idea en la demostración de existencia nos lleva a considerar el si­ guiente procedimiento recurrente: 



m con la convención Q (x ¡ xs) = 1 si m < 0: s=0 Para evaluar los pk y por tanto, para calcular los ck; se usa la multi­ 

63 

4.3. Forma de Newton 

plicación anidada. El algoritmo es como sigue: 



Continuamos considerando la tabla del teorema anterior, es decir, 



en la que todos los nodos xj son distintos. Supondremos además que yj<sup>=f(x</sup> j<sup>); donde f es la función que se quiere interpolar. Según el</sup> teorema anterior, hay un único polinomio, de grado a lo más n; que interpola esta tabla. A continuación presentamos dos maneras de con­ seguirlo que son muy comunes. 

## 4.3 Forma de Newton 

Volvamos a la idea de la demostración del teorema fundamental de la interpolación. Recordemos que se trata de una demostración por inducción en la que se van construyendo los polinomios de acuerdo con la siguiente estrategia: 

64 

4. Interpolación 



Esta es la forma de Newton del polinomio interpolante de la tabla dada. Los coe…cientes ck; que se consiguen con el algoritmo visto antes, se conocen como diferencias divididas. Para ellos se utiliza generalmente la siguiente notación, que viene acompañada de la forma de obtenerlos por recurrencia: 



En general, 

En resumen, la forma de Newton del polinomio interpolante de la tabla dada es 



65 

4.3. Forma de Newton 

Las diferencias divididas se presentan generalmente en tablas como la siguiente: 

x0 f [x0] f [x0; x1] ¢ ¢ ¢ f [x0; ¢ ¢ ¢ ; xn¡1<sup>] f[x</sup> 0<sup>; x</sup> 1<sup>;</sup> ¢ ¢¢ xn] x1 f [x1] f [x1; x2] ¢ ¢ ¢ f [x1; ¢ ¢ ¢ ; xn] . x2 f [x2]<sup>.</sup> . . . . . . . xn¡1<sup>f[x</sup> n¡1<sup>] f[x</sup> n¡1<sup>;x</sup> n<sup>]</sup> xn f [xn] 

Cuando las tablas de diferencias divididas se organizan de esta ma­ nera, los coe…cientes del polinomio interpolante quedan situados en la primera …la. 

Note también que la diferencia dividida (4.6) se encuentra en la …la k y la columna j de la matriz (n +1) £ (n +1) indizada de 0 a n en las dos direcciones, que se obtiene de la tabla de diferencias descartando la columna de las xj. El numerador de (4.6) se consigue por substracción de los elementos (k +1; j ¡ 1) y (k; j ¡ 1) de esta matriz y el numerador se obtiene por substracción de xk+j y xk: 

El siguiente M-archivo lo presentamos con el ánimo de mostrar el procedimiento de construcción de tablas de diferencias divididas. Ad­ vertimos que dista mucho de ser útil, por la cantidad de información que debe entrarse con el teclado. Como dijimos al principio, las rutinas presentadas en estas notas son solamente ejemplos de clase que no pre­ tenden sustituir rutinas hechas por profesionales que son las que deben usarse siempre que estén disponibles. 

% Herramienta didactica, Carlos E. Mejia, 2002 

% uso: difdiv 

% diferencias divididas n=input(’ Entre numero de abscisas: ’); x=input(’ Entre vector de abscisas: ’); y=input(’ Entre vector de ordenadas: ’); d=zeros(n); 

d(:,1)=y(:); for j=2:n 

for i=1:n-j+1 

66 

4. Interpolación 

d(i,j)=(d(i+1,j-1)-d(i,j-1))/(x(i+j-1)-x(i)); end 

end d 

Veamos unos resultados obtenidos con esta rutina. Ofrecemos los datos correspondientes al polinomio x 3 en una tabla con 4 abscisas. Los resultados son: 

» difdiv Entre numero de abscisas: 4 Entre vector de abscisas: [1 2 4 6] Entre vector de ordenadas: [1 8 64 216] d = 



El resultado que ofrece difdiv.m es que el polinomio interpolante, que tiene que ser el propio x 3 por unicidad, está dado por 



Es decir, se obtiene el resultado correcto. 

## 4.4 Forma de Lagrange 

Hay una expresión equivalente para el polinomio interpolante de grado a lo más n que interpola la tabla (4.5). Se conoce como la forma de Lagrange. Está dada por 

donde 



67 

4.5. Ejercicios 

A los polinomios lk se les llama polinomios básicos de Lagrange o funciones cardinales. Estos polinomios son de grado n y entonces el polinomio interpolante se consigue como una suma ponderada de poli­ nomios de grado n: 

Mencionamos esta forma porque es de interés teórico. Nos será de utilidad en la sección 5.5 sobre cuadraturas de Newton-Cotes y en la sección 5.11 sobre polinomios ortogonales y cuadratura gaussiana. 

Una de las propiedades que utilizaremos más adelante, es 



que es una consecuencia directa de (4.8). Aquí ± kj es el delta de Kro­ necker, que toma el valor 1 si k = j y el valor 0 si k = j: 

Con riesgo de sonar repetitivo, volvemos a insistir en que se recurra a software de calidad siempre que esté disponible. En particular, los cál­ culos con la forma de Lagrange, son más susceptibles de ser inestables numéricamente que los cálculos con diferencias divididas. 

## 4.5 Ejercicios 

1. De acuerdo con la revista Newsweek de junio 17 de 2002, pag. 27, el porcentaje de sillas vacías en la primera fase del Mundial de Fútbol, está dado por la siguiente tabla: 

|Año|1990 1994|1998|
|---|---|---|
|Porcentaje|18<br>8.7|10|



a. Construya el polinomio interpolante de esta tabla de grado a lo más 2, utilizando diferencias divididas. 

b. Evalúe este polinomio en 2002. Quisiéramos llamar a este número, el porcentaje correspondiente al Mundial de 2002. Esta clase de evalu­ ación se llama extrapolación. No tiene que ofrecer resultados correctos, a menos que haya razones adicionales para tener en cuenta. 

c. La misma revista informa que el porcentaje de sillas vacías en la primera fase del Mundial del 2002, es 22%. ¿Qué tan bueno fue el estimado obtenido en b.? 

d. Aumente la tabla con la información para el año 2002. Construya el polinomio interpolante de esta tabla de grado a lo más 3, utilizando 

68 

4. Interpolación 

diferencias divididas. Note que sólo tiene que completar el trabajo que ya hizo en la parte a., no necesita empezar desde el principio. 

2. Use el método de coe…cientes indeterminados para encontrar un polinomio cuadrático p (x) tal que p (1) = 0; p<sup>0</sup> (1) = 7 y p (2) = 10: (Note la evaluación de la derivada.) La interpolación polinomial que incluye información sobre derivadas, es importante pero no hace parte de estas notas. Sugerimos a los interesados que estudien interpolación de Hermite, para darse una idea sobre el tema. 

3. Una función spline de grado k con nodos x0; x1; :::; xn es una función S que cumple: 

¡ a. En cada intervalo [xj 1<sup>; x</sup> j<sup>);S es un polinomio de grado · k:</sup> b. S tiene derivadas continuas hasta de orden k ¡ 1 en [x0;xn] : 

Ejemplos: Los splines de grado 0 son funciones constantes a trozos, los de grado 1 son funciones continuas lineales a trozos y los de grado 2 son continuas, con primera derivada continua y de…nidos en cada subintervalo por un polinomio cuadrático. 

Determine los valores de a; b; c y d para que la función 



sea un spline cúbico con nodos 0; 1 y 2: 

Los ejercicios 2. y 3. abren un espacio para temas no tratados en detalle en estas notas. Sugerimos consultar Kincaid y Cheney (1994), cap. 6. 

## 4.6 Error al interpolar 

Si la función f que se está interpolando es su…cientemente suave, las diferencias divididas están relacionadas con las derivadas de f y es posible acotar el error cometido al interpolar. Más precisamente, el teorema siguiente a…rma que la diferencia dividida de f en n +1 puntos distintos, se puede obtener por evaluación de f<sup>(n)</sup> en un cierto punto. 

Teorema 13 Si f 2 C<sup>n</sup> [a; b] y si x0; x1; :::; xn son n + 1 puntos dis­ tintos de [a; b]; entonces existe un punto z 2 (a; b) tal que 



69 

4.7. Ejercicios suplementarios 

El error al interpolar también puede expresarse en términos de deri­ vadas de f cuando f es su…cientemente suave. 

Teorema 14 Sean f 2 C<sup>n+1</sup> [a; b] y pn un polinomio de grado · n que interpola a f en n + 1 puntos distintos x0; x1;:::;xn de [a; b]: Para cada x 2 [a; b]; corresponde un punto zx 2 (a; b) tal que 



En particular, si x no es uno de los nodos xj; j = 0; 1; :::; n; el error al interpolar también puede escribirse así: 



## 4.7 Ejercicios suplementarios 

1. Encuentre los polinomios interpolantes de grado mínimo (a lo más 3), que interpolan las siguientes tablas. Utilice forma de La­ grange para la primera tabla, forma de Newton en la segunda y repita los cálculos de ambas tablas por el método de coe…cientes indeterminados. 



2. Encuentre el polinomio de grado a lo más 4, que satisface la siguiente tabla: 



3. Forme una tabla de diferencias divididas para los datos siguientes y explique lo que pasa. 



70 

   4. Interpolación 

4. Veri…que directamente que si x1; x2; x3 son puntos distintos, en­ tonces 

f [x1;x2; x3] = f [x3; x1; x2] = f [x2;x3; x1] : 

5. Encuentre el polinomio de grado a lo más 4, que satisface la siguiente tabla: 

x 0 1 3 2 5 <u>y</u> 2 1 5 6 -183 

6. La función cos (x) se puede aproximar con un polinomio inter­ polante de grado n usando n +1 nodos igualmente espaciados en el intervalo [0; 1] : Exprese un estimado del error que se comete en términos de n: ¿Para qué valores de n es este error menor que 10<sup>¡7</sup> ? 

7. (Continuación) Realice el mismo experimento del ejercicio ante­ rior usando como nodos, los llamados nodos de Chebyshev, que son xj = 5 cos (j¼=20) ; j = 0; 1; :::; 20: 

8. Encuentre un polinomio interpolante de grado 15 para la función f (x) = arcsen (x) en el intervalo £ ¡1= ~~p~~ 2; 1= ~~p~~ 2¤ : A…rme si con­ sidera que esta aproximación es buena o no con justi…caciones. 

9. Suponga que estamos hallando un polinomio interpolante para una función en [0; 1] ; usando solamente dos puntos x0 y x1: ¿Cuáles deben ser x0 y x1 para que el factor (x ¡ x0) (x ¡ x1) del error al interpolar sea mínimo? 

10. Se propone encontrar un polinomio interpolante de la función ¡ 

f (x) = (1 + 25x<sup>2</sup> )¡1 en el intervalo [ 1; 1] ; de las siguientes for­ mas: a. Utilizando los puntos xjn = ¡1 + 2j=n; j = 0; 1;:::;n; para n = 5; 10; 25: 

: b. Utilizando los puntos xjn = cos µ2n j¼ ¶ 

Haga grá…cas de las funciones de error f (x) ¡ p (x) en todos los casos. Comente sus resultados. 

71 

4.8. Examen de entrenamiento 

### 11. Para la tabla 



se construyó su tabla de diferencias divididas 

|-2|-39|40|-20|7|-1|1 0|
|---|---|---|---|---|---|---|
|-1|1|0|1|3|4|1|
|0|1|2|10|19|9||
|1|3|22|67|55|||
|2|25|156|232||||
|3|181|620|||||
|4|801||||||



Utilice esta tabla para construir el polinomio interpolante de f (x) en cada uno de los siguientes conjuntos de nodos: f¡1; 0; 1g ; f¡1; 0; 1; 2g ; f¡1; 0; 1; 2; 3g ; f0; 1g y f0; 1; 2; 3; 4g : 

## 4.8 Examen de entrenamiento 

Resuelva estos ejercicios sin consultar libros ni notas de clase para darse una idea del nivel de preparación que ha obtenido hasta ahora. Una calculadora sencilla es lo mínimo que debe tener a disposición y es su…ciente para poder responder todos los ejercicios del examen. Claro que es preferible si dispone de una calculadora gra…cadora o un computador. 

1. Calcule el polinomio p de grado 2 que satisface la tabla 



utilizando los tres métodos estudiados, es decir, la forma de La­ grange, la forma de Newton y el método de coe…cientes indeter­ minados. 

2. Sea f (x) = sen y sea p el polinomio p del ejercicio anterior ³ ¼x 2 ´ que coincide con f en los puntos 0, 1 y 2. Calcule una cota para el error jf (x) ¡ p (x)j en [0; 2] : Compare esta cota con el error verdadero en los puntos x = 1=4 y x = 3=4: 

72 

   4. Interpolación 

3. Encuentre el polinomio p de grado 3 que interpola a<sup>~~p~~</sup> x en los nodos 0; 1; 3; y 4: Compare p (2) con<sup>~~p~~</sup> 2 = 1:414216: 

4. Sea p el polinomio que satisface la tabla 



¿Qué puede decir del grado de p? 

# 5 

# Integración numérica 

Fórmulas básicas Error en la cuadratura Cuadraturas compuestas Fórmulas de Newton-Cotes Coe…cientes indeterminados Cuadratura de Gauss Polinomios ortogonales 

La integral de…nida R ab f (x) dx es un número y el proceso de calcu­ larlo, con base en valores de la función f; se conoce como integración numérica o cuadratura. (Esta última palabra se re…ere a encontrar un cuadrado cuya área sea igual al área bajo una curva.) Más precisamente, toda fórmula de integración numérica para la integral R ab f (x) dx es una suma de la forma 

n 



Las formas de escoger los xj y los Aj; generan los distintos tipos de cuadratura. 

Tal como dijimos al principio de estas notas, frecuentemente lo que se requiere para cálculos numéricos son aproximaciones numéricas en lugar de soluciones analíticas. En este caso, podemos decir que uti­ lizar integración numérica es tan importante cuando no se conoce an­ tiderivada para la función como cuando se conoce. 

Para presentar la integración numérica, seguimos a Stewart (1996) [29] y Kincaid y Cheney (1994) [21]. Nos dedicamos únicamente a integrales unidimensionales de…nidas en intervalos cerrados. No con­ sideramos otros dominios de integración ni funciones con singularida­ des. Para tratamiento avanzado del tema, sugerimos Isaacson y Keller (1994) [17] y el libro especializado Davis y Rabinowitz (1984) [9]. 

74 

5. Integración numérica 

## 5.1 Fórmulas básicas 

Una fórmula típica es la Regla de Simpson: 



El símbolo =<sup>»</sup> se lee: es aproximadamente igual a. Empecemos usando esta regla y la más elemental de las rutinas de cuadratura que ofrece MATLAB. 

Ejemplo 15 Utilizar la rutina básica de cuadratura proporcionada por MATLAB, llamada quad, y la regla de Simpson básica para aproximar las integrales entre 0 y 1 de las siguientes funciones: f (x) = jsin (2¼x)j ; 2 f (x) = ~~p~~ ¼ exp (¡x<sup>2</sup> ) y f (x) = x (x ¡ 0:5) (x ¡ 1) + 5: 

Solución: Las soluciones exactas se conocen. En el segundo ejemplo no existe antiderivada, pero la función de error 



está tabulada. Las tablas para erf y muchas otras funciones de…nidas en términos de integrales, son indicativo de lo importante que es tener buenas rutinas para integración numérica. Dichas tablas se pueden con­ sultar, por ejemplo, en la compilación Abramowitz y Stegun (1970) [1]. Preparamos el siguiente M-archivo para hacer los cálculos: 

function simpson(fun,a,b) 

% Herramienta didactica, Carlos E. Mejia, 2002 

% uso de quad, la integracion numerica de bajo orden 

% que ofrece MATLAB junto con regla de Simpson 

% quad esta basada en Simpson y es adaptativa 

% fun: integrando, a, b: limites de integracion % Uso: simpson(’fun’,a,b), fun puede ser fsim.m i1=quad(fun,0,1); c=(b-a)/6; fa=feval(fun,a); f2=feval(fun,(a+b)/2); 

75 

5.1. Fórmulas básicas 

fb=feval(fun,b); i2=c*(fa+4*f2+fb); disp([’Resultado quad: ’,num2str(i1)]); disp([’Resultado Simpson básico: ’,num2str(i2)]); 

Los resultados obtenidos se comparan con los exactos en la siguiente tabla: 

|Int<br>|egral<br>|quad.m|Simpson|Exacto|
|---|---|---|---|---|
|~~R ~~1<br>0<br>|<br> <sup>jsin(2¼x)j dx</sup><br>|0:6366|1:2246£10<sup>¡16</sup>|0:6366|
|~~Z ~~1<br>0<br>|<br> <br>2<br>~~p~~¼exp <sup>¡</sup>¡x<br>2<sup>¢</sup>dx<br>|0:8427|0:8431|0:8427|
|~~R ~~1<br>0|<br> <sup>(x (x</sup><br>0:5) (x<br>¡<br>¡1)+ 5)dx|5<br>|5|5|



El fracaso de la regla de Simpson en la aproximación de la primera integral se debe a que en x = 0; 0:5 y 1; el valor del integrando es cero. La rutina quad.m acierta en los tres ejemplos. La regla de Simpson no fracasa en la segunda integral, simplemente ofrece una aproximación menos buena que quad.m. El éxito de ambas rutinas en el tercer ejemplo es obligatorio, pues el integrando es un polinomio de grado 3 y la regla de Simpson es exacta para polinomios hasta de grado 3, como veremos enseguida. 

Otra fórmula básica es la regla trapezoidal, de…nida así: 



Si f es una función no negativa, la regla trapezoidal consiste en apro­ ximar el área bajo la curva por el área del trapecio con bases f (0) y 2 f (1) y altura 1: Para la función ~~p~~ ¼ exp (¡x 2) ; las dos áreas se pueden 

76 

5. Integración numérica 

ver en la siguiente grá…ca: 



<!-- Start of picture text -->
Regla trapezoidal<br>1.4<br>1.2<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>-1  0  1  2<br><!-- End of picture text -->

### 5.1.1 Ejercicio 

Repetir el ejemplo 15 con la regla trapezoidal en lugar de la regla de Simpson. Comentar acerca de los resultados obtenidos. 

### 5.1.2 Cambio de intervalo 

Las dos fórmulas básicas que hemos presentado fueron dadas para el intervalo [0; 1] pero el M-archivo simpson.m, lo escribimos con base en un intervalo genérico [a; b] : Los cambios de intervalo son tan fáciles de hacer, que a menudo se presentan las fórmulas únicamente para [0; 1] : Para cambiar de intervalo, basta escribir la variable x como función lineal de otra variable y, así: 



Enseguida pedimos x = a cuando y = 0 y x = b cuando y = 1, lo cual exige tomar p = a y q = b ¡ a: La expresión anterior se cambia por 



y además, también escribimos 



5.2. Error en la cuadratura 77 

Finalmente, dx = (b ¡ a)dy y la integral<sup>R</sup> ab f (x) dx la podemos evaluar así: 



Como 



entonces en el intervalo [a; b] la regla de Simpson es 



y la regla trapezoidal es 



## 5.2 Error en la cuadratura 

Sean 

y 



Si f tiene su…cientes derivadas, los errores en cada una de estas cuadraturas están dados por 



y 



donde ¿ y ´ están entre a y b: La justi…cación de estas igualdades puede verse en Kincaid y Cheney (1994) [21]. 

78 

5. Integración numérica 

Una consecuencia de estas fórmulas de error, es que la regla de Simp­ son es exacta para polinomios hasta de grado 3 y que la regla trape­ zoidal es exacta para polinomios hasta de grado 1. En efecto, la cuarta derivada de un polinomio de grado 3 o menor, es cero y la segunda derivada de un polinomio de grado 1 es cero. Estas ideas se generalizan en la sección 5.5 sobre cuadraturas de Newton-Cotes. 

Otra consecuencia de estas fórmulas, es que sobre intervalos grandes, es prácticamente imposible obtener buenos resultados con estas cuadra­ turas. Por eso se recurre a las cuadraturas compuestas, que se conside­ ran en la siguiente sección. 

## 5.3 Cuadraturas compuestas 

Las cuadraturas trapezoidal y de Simpson normalmente se aplican sobre intervalos pequeños que conforman uno grande, pues de esa ma­ nera se obtienen errores menores. Supongamos que queremos aproximar I = R a b f (x) dx: Entonces dividimos el intervalo [a; b] en n subinterva­ los, cada uno de longitud h = b<sup>¡</sup> a : Sean xj = a + jh; j = 0; 1; :::; n: n Sabemos que 



y al sumar todas estas aproximaciones, obtenemos una aproximación para I: Tal suma la denotamos CT (f; a; b) y la llamamos regla trape­ zoidal compuesta. Su valor es 



Si f es su…cientemente suave, el error para esta cuadratura es 



79 

5.4. Ejercicios 

donde ¿ 2 (a;b) : El factor h<sup>2</sup> es muy importante. Indica que si el número de puntos se duplica, el nuevo error es del mismo orden de magnitud que el anterior error dividido por 4. 

De forma análoga se de…ne la regla de Simpson compuesta. Requiere para su de…nición que el número n de subintervalos sea par. Los detalles pueden verse en un libro de análisis numérico, por ejemplo, Kincaid y Cheney (1994) [21]. 

## 5.4 Ejercicios 

Las integrales de Fresnel de tipo coseno se de…nen asi: 



Tales integrales y las de tipo seno que se de…nen análogamente, apare­ cen tabuladas en una gran variedad de colecciones de funciones, por ejemplo en Abramowitz y Stegun (1970) [1]. 

1. Construya una tabla de los valores de la función C(z) para todo z de la forma z = 0:05k; donde k = 1; 2;:::; 20: Necesariamente debe utilizar alguna rutina para integración numérica. Dicha rutina puede crearla usted o tomarla de alguna fuente. 

2. Repita el ejercicio 1. para la función 



Estas son las integrales de Fresnel de tipo seno. 

3. Establezca la fórmula de cuadratura compuesta de Simpson que denotaremos CS (f; a; b) : Puede hacerlo por deducción directa o con­ sultando un libro de análisis numérico. Enseguida, vuelva al ejemplo 15. Repita los cálculos para las tres funciones, utilizando las fórmu­ las compuestas de cuadratura CT (f;a;b) y CS (f; a; b), para n = 2<sup>k</sup> ; k = 0; 1;:::; 4: 

4. Calcule C (1) y S (1) por medio de las fórmulas compuestas de cuadratura CT (f; a; b) y CS (f; a; b), para n = 4: 

80 

5. Integración numérica 

## 5.5 Cuadraturas de Newton-Cotes 

Buscamos una cuadratura para<sup>R</sup> ab f (x) dx de la forma<sup>P</sup> n Ajf (xj) ; j=0 

donde x0; x1; :::; xn son puntos distintos del intervalo [a;b] : Queremos además que sea exacta para polinomios hasta de grado n: ¿Será posible encontrar A0; A1; :::; An tales que para todo polinomio p de grado a lo más n; la igualdad 



es cierta? La respuesta es a…rmativa y la escribimos en forma de teo­ rema. 

Teorema 16 (Cuadratura de Newton-Cotes) Sean lj ; j = 0; 1;:::;n los polinomios básicos de Lagrange sobre x0; x1; :::; xn: Entonces 



son los únicos coe…cientes tales que 



dem: 

Puesto que los polinomios de Lagrange tienen grado n; para ellos debe cumplirse el lado derecho de (5.2), es decir, 



La última igualdad se debe a (4.9). De manera que el único posible valor para cada Aj es el propuesto en (5.1). 

Tomemos ahora un polinomio p de grado a lo más n: De (4.7), 



81 

5.6. Método de coe…cientes indeterminados 

Por tanto, 



Es apropiado observar que para cada n y cada colección de n + 1 puntos, hay una cuadratura de Newton-Cotes. 

Ejemplo 17 La regla trapezoidal es la cuadratura de Newton-Cotes sobre [a; b] con n = 1; x0 = a y x1 = b: 

Sin pérdida de generalidad, trabajamos en [0; 1] : Es fácil ver que 



para k = 0; 1: Es decir, para aproximar R 01 f (x) dx; la cuadratura de Newton-Cotes sobre [0; 1] con n = 1; x0 = 0 y x1 = 1 es 



que es T (f; 0; 1) : 

Normalmente, esta no es la forma de encontrar los factores de pon­ deración Aj en una cuadratura de Newton-Cotes. Lo que se hace es recurrir al método de coe…cientes indeterminados, que convierte el pro­ blema en la solución de un sistema de ecuaciones lineales. 

## 5.6 Método de coe…cientes indeterminados 

Explicamos el método por medio de la solución del siguiente ejemplo. 

Ejemplo 18 Encontrar la cuadratura de Newton-Cotes sobre [0; 1] con n = 2; x0 = 0; x1 = 0:5 y x2 = 1: 

Buscamos una cuadratura para R 01 f (x) dx que sea de la forma 



82 

5. Integración numérica 

y que sea exacta para polinomios de grado a lo más 2: Los coe…cientes que encontremos, serán los de la cuadratura de Newton-Cotes pedida, es decir, los dados en (5.1). 

Escogemos 1; x y x<sup>2</sup> como los polinomios de grados 0; 1 y 2 res­ pectivamente, que nos permitan enunciar un sistema por medio del cual encontramos los coe…cientes Aj de la cuadratura. Evaluamos el polinomio y la cuadratura para cada uno de los polinomios, así: 



1 y 6 

Este sistema tine una única solución dada por A0 = A2 = y 6 2 A1 = : Estamos ante la cuadratura de Newton-Cotes sobre [0; 1] con 3 n = 2; x0 = 0; x1 = 0:5 y x2 = 1 y no es más que la regla de Simpson. 

Esta cuadratura tiene otra particularidad, que ya conocemos desde que vimos los errores en la sección 5.2. Para x3; la ecuación que resulta es 



y en efecto, los valores encontrados antes para A1 y A2; también satis­ facen esta ecuación. Esto signi…ca que la regla de Simpson también es exacta para polinomios de grado 3: 

Nótese que la regla de Simpson no es una cuadratura de NewtonCotes para n = 3; pues no se utilizan 4 puntos en su formulación. 

## 5.7 Cuadratura de Gauss 

Para el cálculo aproximado de la integral R ab f (x) dx, tenemos cuadra­ turas 



83 

5.7. Cuadratura de Gauss 

con n + 1 nodos y n + 1 coe…cientes de ponderación que son exactas para polinomios de grado a lo más n: Hasta ahora, los nodos están …jos de antemano y hay n + 1 coe…cientes de ponderación Aj por deter­ minar, tantos como coe…cientes tiene un polinomio de grado n: Ahora intentamos algo más: considerar nodos y coe…cientes de ponderación como incógnitas, un total de 2n +2 incógnitas. Veremos que existe una fórmula de cuadratura (5.3) que es exacta para polinomios de grado a lo más 2n + 1. Dicha cuadratura se conoce como cuadratura de Gauss o gaussiana. 

Empecemos como antes, con el método de coe…cientes indetermina­ dos y un ejemplo similar al ejemplo 17. 

Ejemplo 19 Utilizar el método de coe…cientes indeterminados para hallar el sistema de ecuaciones correspondiente a la cuadratura gaus­ siana para n = 1 en [0; 1] : 

Nuestras 2n + 2 incógnitas son x0; x1; A0 y A1: Escogemos los poli­ nomios 1; x; x 2 y x 3 para las evaluaciones. 



Lo primero que salta a la vista es que el sistema al que llegamos es no lineal. Para resolverlo, podemos hacer algunas manipulaciones algebraicas o recurrir al método de Newton, que en estas notas aparece en la sección 6.15. Pero la no linealidad no es el único problema que este sistema tiene, pues es sabido que padece de inestabilidad numérica, es decir, un pequeño error en un paso puede conducir a soluciones lejanas a las verdaderas. 

Los dos inconvenientes, no linealidad e inestabilidad numérica, están presentes en todos los sistemas a los que se llega si se intenta el método de coe…cientes indeterminados para conseguir cuadraturas gaussianas. 

5. Integración numérica 

84 

¿Qué hacer entonces? Lo mismo que hizo Gauss (1777-1855) hace cerca de 200 años: utilizar polinomios ortogonales, que es lo que haremos en la sección 5.9. 

## 5.8 Ejercicios 

1. Resuelva exactamente el sistema de ecuaciones (5.4) y obtenga una fórmula de cuadratura gaussiana sobre [0; 1] que es exacta para poli­ nomios de grado a lo más 3. 

2. Utilice la cuadratura gaussiana que acaba de deducir para calcular las integrales del ejemplo 15. 

3. Calcule C (1) y S (1) ; las integrales de Fresnel para z = 1; por medio de esta cuadratura gaussiana. Las integrales de Fresnel fueron de…nidas en la sección de ejercicios 5.4. 

## 5.9 Polinomios ortogonales 

La cuadratura de Gauss que buscamos es bastante más general que la presentada antes. Sea w (x) una función positiva y continua en [a; b] que llamaremos función de ponderación (en inglés weight). Queremos aproximar la integral 





por medio de una combinación lineal de valores de la función 



De…nición 20 Dos funciones f y g se dice que son ortogonales con respecto a w en el intervalo [a;b] si 



En realidad, si nos concentramos a trabajar en el espacio vecto­ rial de funciones continuas en [a; b] ; denotado C ([a; b]) ; la expresión R a b f (x) g (x) w (x) dx de…ne un producto interno en C ([a; b]) : En estas 

85 

5.9. Polinomios ortogonales 

condiciones, la expresión (5.5) dice que el producto interno de las fun­ ciones f y g es cero. Eso es lo que se llama ortogonalidad en espacios vectoriales. 

De…nición 21 Una sucesión de polinomios ortogonales es una suce­ sión de polinomios fpj g1j=0 en la que grad(pj ) = j para cada j y tal que 



Como la ortogonalidad no se altera por multiplicación por escalares no nulos, normalizamos los polinomios pj de manera que los coe…cientes de los términos de mayor grado x<sup>j</sup> sean 1: A los polinomios con esa característica, se les llama mónicos. 

De ahora en adelante trabajamos con sucesiones de polinomios orto­ gonales mónicos. El primer resultado que mencionamos es que, de haber una tal sucesión de polinomios ortogonales fpjg1j =0, todo polinomio de grado n se puede escribir de forma única como una combinación lineal con p0; p1; :::; pn: 

Teorema 22 Sea fpjg<sup>1</sup> j=0<sup>una sucesión de polinomios ortogonales móni­</sup> n cos (ver de…nición 21.) Si q (x) = P aj x<sup>j</sup> es un polinomio de grado a j =0 lo más n; entonces existen escalares bj tales que 



n n Además, si q = P bjpj = P cjpj; entonces bj = cj para cada j: j=0 j=0 

La demostración de este resultado es una inducción sobre n: Puede verse, por ejemplo, en Stewart (1996), [29]. 

El segundo resultado que nos interesa es un corolario del anterior. Consiste en notar que pn+1 es ortogonal a cualquier polinomio q de grado n o menor, pues lo que hacemos es escribir a q como en el teorema 

86 

5. Integración numérica 



anterior y multiplicar. Más precisamente: Si q =<sup>P</sup> bjpj; entonces 

j=0 



La igualdad a cero se da por la ortogonalidad de la sucesión de poli­ nomios. Hemos probado 

Corolario 23 El polinomio pn+1 es ortogonal a cualquier polinomio de grado n o menor. 

## 5.10 Fórmula de recurrencia de tres términos 

La existencia de sucesiones de polinomios ortogonales mónicos, no ha sido establecida aún. Intentemos su construcción. 

Por ser todos mónicos, obligatoriamente p0 es el polinomio constante ¡ 1 y p1 (x) = x d1: ¿Podremos identi…car a d1? La respuesta es a…rmativa, lo hacemos por ortogonalidad. Como 



entonces 



La re-escritura propuesta para d1 se verá lógica en un momento, cuando encontremos una expresión general para dn+1: Además, el denominador es no nulo pues el integrando es continuo y positivo. 

La idea es buscar a pn+1 en la forma 



utilizando apropiadamente la ortogonalidad de la sucesión. Para dn+1; 

87 

5.11. Cuadratura gaussiana y polinomios ortogonales 

imitamos lo hecho para d1; es decir, 



¡dn+1 R a b p2 n (x) w (x) dx ¡en+1 R a b pn (x) pn¡1<sup>(x) w (x) dx</sup> ¡ ::: 

En el lado derecho, los términos después del segundo son cero por ortogonalidad. Luego 



De nuevo, el denominador es no nulo pues el integrando es continuo y positivo. 

Similarmente, usando ortogonalidad, se encuentra que 



y que los demás coe…cientes en (24) son cero. Para los detalles puede verse Stewart (1996) [29]. 

Encontramos pues una fórmula de recurrencia de tres términos que genera una sucesión de polinomios ortogonales y mónicos asociada con el intervalo [a;b] y la función de ponderación w (x) : Es la siguiente: 



Ya estamos listos para relacionar cuadratura de Newton-Cotes, cua­ dratura de Gauss y polinomios ortogonales. 

## 5.11 Cuadratura gaussiana y polinomios ortogonales 

Empezamos con un teorema sobre los ceros de pn+1: Estos n + 1 ceros serán los nodos para la cuadratura de Gauss, de allí la importancia de este resultado. 

5. Integración numérica 

88 

Teorema 24 Los ceros de pn+1 son reales, simples y pertenecen a [a;b] : 

La demostración puede consultarse en Stewart (1996) [29]. Este teorema establece que los ceros de pn+1 son una colección de n + 1 puntos distintos del intervalo [a; b] : Queremos utilizar estos puntos como nodos para una cuadratura de Newton-Cotes asociada con el intervalo [a;b] y la función de ponderación w (x) : Esta cuadratura aproxima<sup>R</sup> ab f (x) w (x) dx por una combinación lineal de valores de f de la forma 



Los coe…cientes Aj de la cuadratura, se consiguen de forma similar a la que se usa en el teorema 5.2, a saber, de…nimos 



Esta cuadratura de Newton-Cotes para R ab f (x) w (x) dx es exacta para polinomios de grado hasta n; o sea que 



Resulta que, debido a los nodos que estamos usando, esta cuadratura cumple mucho más que ésto. Demostremos que 



Sea g un polinomio de grado a lo más 2n + 1: Dividimos g por pn+1 y obtenemos 



89 

5.11. Cuadratura gaussiana y polinomios ortogonales 

con grad(q) · n y grad(r) · n: Luego 





Para un intervalo [a; b] y una función de ponderación w 2 C ([a; b]) ; concluímos que: 

1. Hay una sucesión de polinomios ortogonales y mónicos fpj g<sup>1</sup> j=0 con grad(pj) = j para cada j: (Ver sección 5.10.) 

2. Dado n entero positivo, el polinomio pn+1 tiene n + 1 ceros dis­ tintos en el intervalo [a; b] : (Ver teorema 24.) 

3. Con los ceros de pn+1 como nodos, se puede construir la corres­ pondiente cuadratura de Newton-Cotes para aproximar la inte­ gral R ab f (x) w (x) dx. A dicha cuadratura se le llama cuadratura de Gauss. Esta cuadratura es exacta para polinomios de grado hasta 2n + 1: Está dada por la combinación lineal 



con 



Aquí los lj son los polinomios básicos de Lagrange asociados con los n + 1 nodos x0; x1; :::; xn: 

90 

5. Integración numérica 

También podemos demostrar que los coe…cientes Aj en la cuadratura de Gauss son positivos. En efecto, es claro que 



y grad<sup>¡</sup> l<sup>2</sup> j<sup>¢</sup> = 2n: Por tanto, la cuadratura de Gauss es exacta para l<sup>2</sup> j<sup>(x) y</sup> 



por (4.9). 

Notamos G (f;a;b;w; n) la cuadratura gaussiana sobre [a;b] ; con función de ponderación w (x) y con n + 1 nodos que aproxima 



Si f es su…cientemente suave, el error cometido al utilizar esta cuadra­ tura es 



para algún ¿ 2 (a;b) : Una demostración de esta igualdad puede en­ contrarse en Kincaid y Cheney (1994) [21], sección 7.3. 

## 5.12 Ejercicios 



2. Para intervalos y funciones de ponderación particulares, las cua­ draturas de Gauss toman distintos nombres. Una de las más famosas es la cuadratura de Gauss-Legendre, que se hace con el intervalo [¡1; 1] y con la función de ponderación w (x) = 1: Los polinomios ortogona­ les correspondientes, se conocen como polinomios de Legendre. Para todas las cuadraturas de Gauss más utilizadas, los nodos y los coe…cientes aparecen tabulados en Abramowitz y Stegun (1970) [1] y en compendios similares. Calcule las integrales del ejemplo 15 utilizando 

91 

5.13. Ejercicios suplementarios 

las cuadraturas de Gauss-Legendre de 2 y 4 nodos, correspondientes a n = 1 y n = 3: Esta es la cuadratura que investigó Gauss originalmente. ¡ 3. Para el intervalo [ 1; 1] y la función de ponderación w (x) = (1 ¡ x<sup>2</sup> )<sup>¡1=2</sup> ; la cuadratura se conoce como de Gauss-Chebyshev y a los polinomios ortogonales se les conoce como polinomios de Chebyshev. Demuestre que los coe…cientes de la cuadratura de Gauss-Chebyshev son todos iguales. Encuentre el valor de ellos. 

Sugerencia: Consulte Johnson y Riess (1982) [19], pag. 329. 

4. Sea 



con 0 · c < 1: Se sabe que para c = 0:5; el valor de K es 1:6858: Compruebe este hecho utilizando dos cuadraturas de Gauss distintas. 

## 5.13 Ejercicios suplementarios 

1. Aplique regla trapezoidal y de Simpson para aproximar Si(1) ; donde 



Utilice h = 2<sup>¡k</sup> ; con k = 1; 2; 3: 

2. Encuentre aproximaciones al valor de la integral 



por medio de reglas compuestas trapezoidal y de Simpson, regla del rectángulo (ver ejercicio siguiente) y dos cuadraturas gaus­ sianas diferentes. Utilice un computador o una buena calculadora. 





92 

5. Integración numérica 

Cuando f es positiva, corresponde a aproximar la integral con la suma de las áreas de rectángulos de altura f (xj) : Encuentre una expresión para el error al aproximar I con la regla del rectángulo. 

4. ¿Qué tan grande debe ser n para que se cometa un error menor a 10<sup>¡6</sup> al aproximar<sup>R</sup> 02 e¡x2dx con la regla trapezoidal? 

5. Regla de Simpson 3/8: Otro esquema de integración numérica es la regla de Simpson 3/8, de…nida sobre tres subintervalos de la siguiente manera: 



Frecuentemente se dice que la regla de Simpson opaca a la regla de Simpson 3/8. Explique la lógica de esta opinión generalizada, probando que la regla de Simpson 3/8 es exacta para polinomios de grado 3 o menor, que es lo mismo que se logra con la regla de Simpson a un costo menor en evaluaciones de funciones. 

6. Encuentre aproximaciones de R 01 (1 + x2)¡1 dx utilizando regla de Simpson con h = 2<sup>¡k</sup> ; k = 1; 2: Calcule el error que comete en cada caso. Compare con las cotas de error que da la teoría. 

7. Construya una regla de cuadratura de la forma 



que es exacta para polinomios de grado 2 o menor. 

8. Construya la cuadratura de Gauss de la forma 



que es exacta para polinomios del más alto grado posible. 

9. Aproxime a ¼ por integración numérica de una integral de la forma 



93 

5.14. Examen de entrenamiento 

10. Aproxime a log (2) por integración numérica de una integral de la forma 



## 5.14 Examen de entrenamiento 

Resuelva estos ejercicios sin consultar libros ni notas de clase para darse una idea del nivel de preparación que ha obtenido hasta ahora. Una calculadora sencilla es lo mínimo que debe tener a disposición y es su…ciente para poder responder todos los ejercicios del examen. Claro que es preferible si dispone de una calculadora gra…cadora o un computador. 

- ¡ 

- 1. Considere la función f (x) = jxj en el intervalo [ 1; 1] : Utilice h = 2<sup>k</sup> ; k = ¡1; 0 para aproximar R ¡11<sup>f (x) dx por regla de Simpson.</sup> Compare con la solución verdadera. 

2. Se quiere estimar R 0 ¼ sen (x) dx por regla trapezoidal con n subdi­ visiones del intervalo y se desea tener un error menor que 10<sup>¡12</sup> : ¿Qué tan grande debe ser n de acuerdo con la teoría? 

3. Utilice la cuadratura gaussiana 



para aproximar las integrales 



94 5. Integración numérica 

# 6 

# Ecuaciones diferenciales ordinarias 

Problemas de valor inicial Existencia y unicidad de PVIs Método de Euler Análisis de Error Consistencia, estabilidad, errores de redondeo, estabilidad absoluta Métodos de Taylor y método clásico de Runge-Kutta 

## 6.1 Problemas de valor inicial 

Los primeros problemas que consideramos son los de valor inicial, es decir, resolver numéricamente una ecuación diferencial ordinaria de primer orden para la que se conoce un punto de su curva solución. Más precisamente, sean 



Queremos encontrar una función y : R ! R<sup>n</sup> tal que 



96 

6. Ecuaciones diferenciales ordinarias 

La notación acostumbrada para la función incógnita y es 



Resolver numéricamente problemas de valor inicial (PVI, de ahora en adelante), es uno de los temas en la mayoría de los libros de análisis numérico. Excelentes presentaciones del tema pueden encontrarse, por ejemplo, en Stoer y Bulirsch (1992) [30], Kincaid y Cheney (1994) [21] y Johnson y Riess (1982) [19]. Los libros Gear (1971) [11] y Henrici (1962) [14] son dos de los primeros que se han escrito sobre el tema y se consideran clásicos. 

## 6.2 Problemas lineales y no lineales 

Si cada componente fk de f es de la forma 



con akj : R ! R; k = 1; :::; n; j = 0; 1;:::;n; decimos que (6.1) es un problema lineal. En otro caso, decimos que el problema (6.1) es no lineal. Si ak0 es la función nula para todo k; decimos que (6.1) es un problema homogéneo. En otro caso, decimos que es un problema no homogéneo. 

Los siguientes ejemplos resueltos sirven como motivación para cono­ cer herramientas modernas de solución disponibles en MATLAB. Es­ tas herramientas utilizan tamaños de paso adaptable y métodos de alto orden. Como se verá después, nuestra pretensión en estas notas es considerar en detalle solamente los métodos más elementales. Sin embargo, con…amos en que quienes se sientan inclinados por el tema, puedan basarse en este material y en las referencias que incluimos para analizar métodos más complicados. 



Este es un problema lineal homogéneo y su solución exacta es fácil de obtener. Pero también es interesante resolverlo numéricamente. 2. Encontrar y : R ! R<sup>2</sup> tal que 



Aqui, g y b son constantes positivas. Este es un problema no lineal ho­ mogéneo que sirve de modelo para un péndulo plano. 

3. Especies en competencia: Sean y1 (t) y y2 (t) las cantidades de animales en el tiempo t de dos especies que compiten por el mismo alimento. Se supone que la natalidad de cada especie es proporcional al número de animales de esa especie pero la mortalidad de cada especie depende de la población de ambas especies. Un sistema de este tipo es el siguiente: 



Si se sabe que la población inicial de cada especie es de 10000, cuál será la solución de este sistema para t 2 [0; 4]? 

Este es otro ejemplo de problema no lineal homogéneo. 

## 6.3 Soluciones de los ejemplos 

1. Para el primer ejemplo, usamos el método de Euler por medio del M-archivo ode3.m. 

% ode3, Herramienta didactica, Carlos E. Mejia, 2002 % uso: ode3 

98 6. Ecuaciones diferenciales ordinarias % solucion numerica de PVI, metodo de Euler % rhs3: m-archivo con lado derecho en el pvi % inte: intervalo [to,tfin] % ci: condicion inicial y(to) clear all inte=[0 4];ci=[2;1]; t=linspace(inte(1),inte(2),800); y=zeros(length(t),2);h=(inte(2)-inte(1))/length(t); y(1,:)=ci(:)’; for j=1:length(t)-1 y(j+1,:)=y(j,:)+h*feval(’rhs3’,t,y(j,:)’)’; end y1=y(:,1); y2=y(:,2); subplot(2,1,1); plot(t,y1,’k*’,t,y2,’k’); %set(gca,’XTick’,[0 1/2 1 3/2]) axis([0 3/2 0 2]);ylabel(’Y(1) y Y(2)’) title(’Ecuacion yprime=Ay’); subplot(2,1,2); plot(y1,y2,’r’);xlabel(’Y(1)’);ylabel(’Y(2)’); xlabel(’Diagrama de fase Y_1 VS Y_2’); print -deps2 .nfignode3.eps 

99 

6.3. Soluciones de los ejemplos 

Las grá…cas generadas son: 



<!-- Start of picture text -->
Ecuacion yprime=Ay<br>2<br>1.5<br>1<br>0.5<br>0<br>0  0.5  1  1.5<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>0  0.2  0.4  0.6  0.8  1  1.2  1.4  1.6  1.8  2<br>Diagrama de fase Y  1 VS Y 2<br><!-- End of picture text -->

2. El segundo ejemplo se resuelve con una herramienta profesional de MATLAB, llamada ODE45. Esta es la más poderosa entre todas las rutinas de uso general que ofrece MATLAB, para la solución de PVIs. El M-archivo que utilizamos es éste: 

% ode1, Herramienta didactica, Carlos E. Mejia, 2002 % Referencia D. Higham y N. Higham, Matlab Guide % SIAM, p. 151 tspan=[0,10]; yazero=[1;1];ybzero=[-5;2];yczero=[5;-2]; [ta,ya]=ode45(’rhs1’,tspan,yazero); [tb,yb]=ode45(’rhs1’,tspan,ybzero); [tc,yc]=ode45(’rhs1’,tspan,yczero); [y1,y2]=meshgrid(-5:.5:5,-3:.5:3); Dy1Dt=y2;Dy2Dt=-sin(y1); quiver(y1,y2,Dy1Dt,Dy2Dt,’k’) hold on plot(ya(:,1),ya(:,2),’k’,... yb(:,1),yb(:,2),’k’,yc(:,1),yc(:,2),’k’) 

100 

6. Ecuaciones diferenciales ordinarias 

axis equal,axis([-5 5 -3 3]) title(’Pendulo simple’) xlabel (’Diagrama de fase, y_1 VS y_2’), hold off print -deps2 .nfignode1.eps 

Con este M-archivo generamos la siguiente grá…ca: 



<!-- Start of picture text -->
Pendulo simple<br>3<br>2<br>1<br>0<br>-1<br>-2<br>-3<br>-5 -4 -3 -2 -1 0 1 2 3 4 5<br>Diagrama de fase, y 1  VS y 2<br><!-- End of picture text -->

3. Con un M-archivo como el anterior, generamos esta grá…ca para el ejemplo 3. 



<!-- Start of picture text -->
x 10 4 Especies en competencia<br>2<br>1.8<br>1.6<br>1.4<br>1.2<br>1<br>0.8<br>0 2000 4000 6000 8000 10000<br>Diagrama de fase, y 1  VS y 2<br><!-- End of picture text -->

La grá…ca sugiere la tendencia a desaparecer de la población 1 y a estabilizarse en 20.000 la otra población. Para demostrar un hecho 

101 

6.4. Análisis del Método de Euler 

como éste, se recurre al estudio de equilibrios para el sistema dinámico (6.2). 

## 6.4 Análisis del Método de Euler 

Al método de Euler lo escogimos para hacerle un análisis detallado por ser el más sencillo y porque dicho análisis contiene muchas de las ideas utilizadas para el análisis de métodos menos sencillos. La sección la iniciamos con un teorema de existencia y unicidad para PVIs seguido por ejemplos ilustrativos. Después nos concentramos en el algoritmo de Euler y exponemos las de…niciones y estimados básicos para el análi­ sis de error del método. Terminamos con la presentación esquemática de otros métodos de diferencias …nitas. Por razones metodológicas, el análisis lo realizamos para ecuaciones escalares, pero casi siempre la generalización al caso vectorial es prácticamente una repetición del mismo análisis. 

## 6.5 Existencia y unicidad 

Empezamos con el Teorema Fundamental de Existencia y Unicidad de Soluciones. 

Teorema 26 Sea f de…nida y continua en la franja 



a; b …nitos. Además, supongamos que existe una constante L tal que 



para todo t 2 [a; b] y todo u;v 2 R<sup>n</sup> (condición de Lipschitz). Entonces para todo t0 2 [a;b] y todo y0 2 R<sup>n</sup> existe exactamente una función y (t) tal que 

a. y (t) es continua y continuamente diferenciable para t 2 [a; b] ; b. y<sup>0</sup> (t) = f (t;y (t)) para t 2 [a;b]; 

c. y (t0) = y0: 

Dos ejemplos unidimensionales son apropiados en este momento. 

102 

6. Ecuaciones diferenciales ordinarias 

Ejemplo 27 1. El PVI 



tiene una única solución y (t) = exp (t) : Las hipótesis del teorema an­ terior se satisfacen en cualquier franja S que contenga al eje y en el plano cartesiano R £ R: 2. El PVI 



<u>1</u> tiene una única solución y (t) = 1¡t<sup>; de…nida únicamente para t< 1:</sup> Esta asíntota vertical no sorprende, pues de (6.3) vemos que la función solución del PVI debe ser positiva con derivada positiva y creciente. En este caso, la existencia y unicidad de la solución no se puede obtener del Teorema 26. Recomendamos un libro especializado como Henrici (1962) [14] para más detalles teóricos. 

## 6.6 Solución numérica 

Los métodos de diferencias …nitas para el PVI (6.1), o simplemente, métodos de diferencias, consisten en encontrar aproximaciones de la solución y (t) en un conjunto de puntos 



no necesariamente igualmente espaciados. Denotemos por 



a las correspondientes aproximaciones. Los cálculos para hallar Yk se basan en una o varias de las aproximaciones previamente encontradas Y0; Y1; :::; Yk¡1<sup>:</sup> 

Al número de aproximaciones previas que se requieren en un método dado, se le llama el número de pasos del método. 

Si un método numérico contempla la posibilidad de cambiar de tamaño de paso de acuerdo con los resultados que va obteniendo, se dice que se trata de un método adaptativo. La mayoría de los métodos de di­ ferencias programados como comandos en los principales paquetes de 

103 

6.7. Método de Euler 

software, son adaptativos. Varios de los que utiliza MATLAB son de la familia de métodos llamados de Runge-Kutta-Fehlberg. Sugerimos con­ sultar Kincaid y Cheney (1994) [21] a quien desee conocer más detalles sobre estos métodos. 

## 6.7 Método de Euler 

Como la de…nición de métodos de diferencias …nitas es esencialmente independiente del número n de funciones incógnitas, en adelante nos limitamos a presentar la teoría para una sola ecuación con una sola función incógnita. En los ejemplos, consideramos tanto ecuaciones es­ calares como sistemas. 

Sea f : R £ R ! R: Queremos encontrar una función y : R ! R tal que 



Para las consideraciones siguientes, supondremos que este PVI tiene una única solución su…cientemente suave, es decir, que es única y tiene todas las derivadas que se requieran para el análisis. Aunque parezca muy restrictiva, esta condición únicamente facilita el enunciado de los métodos numéricos de interés y no se requiere a la hora de hacer cálculos especí…cos. 

Los métodos de diferencias …nitas que estudiamos a continuación son de un paso y trabajan con una malla igualmente espaciada, o sea tj<sup>= t</sup> 0<sup>+ jh; para todo j = 1; 2; :::; donde h es un número real no nulo.</sup> El primero que consideramos es el más sencillo de todos y se obtiene de la expansión de Taylor de primer orden 



donde » está entre t y t + h y recordamos que y<sup>0</sup> (t) = f (t; y (t)) : Si 0 < jhj, una primera aproximación para y (t + h) es y (t)+ hf (t; y (t)) : Esto da origen al método de Euler para aproximar la solución de (6.4) 

6. Ecuaciones diferenciales ordinarias 

104 

que se de…ne así: 



Nótese que cada iteración se obtiene de la anterior agregando un término corrector de la forma hG (tj; Yj; h; f) : En el caso del método de Euler que acabamos de de…nir, G es independiente de h; pues es f (t;Y ) : En general, los métodos de un paso se de…nen así: 



Al …nal de la sección vemos algunos otros métodos de un paso. 

Ejemplo 28 Resolvamos el PVI 



por el método de Euler. Interesa aproximar el valor exp(¡10) = y (1) : 

Veamos algunas aproximaciones obtenidas con distintos valores de h: La solución exacta es la línea continua y la otra es la solución aproxi­ mada. 

105 

6.7. Método de Euler 



<!-- Start of picture text -->
yprima = -10y, n = 2 yprima = -10y, n = 4<br>1  4<br>0<br>2<br>-1<br>0<br>-2<br>-2<br>-3<br>-4  -4<br>0 0.5  1 0  0.5  1<br>yprima = -10y, n = 8  yprima = -10y, n = 16<br>1  1<br>0.8<br>0.5<br>0.6<br>0.4<br>0<br>0.2<br>-0.5  0<br>0  0.5  1 0  0.5  1<br><!-- End of picture text -->



<!-- Start of picture text -->
yprima = -10y, n = 32 yprima = -10y, n = 64<br>1  1<br>0.8  0.8<br>0.6  0.6<br>0.4  0.4<br>0.2  0.2<br>0 0<br>0 0.5  1 0  0.5  1<br>yprima = -10y, n = 128  yprima = -10y, n = 256<br>1  1<br>0.8  0.8<br>0.6  0.6<br>0.4  0.4<br>0.2  0.2<br>0  0<br>0  0.5  1 0  0.5  1<br><!-- End of picture text -->

106 

6. Ecuaciones diferenciales ordinarias 

La siguiente tabla corrobora lo observado en las grá…cas. 

||Tabla 1: Mét|odo de Euler, y<sup>0</sup>|= 10y; y (0)= 1<br>¡|
|---|---|---|---|
|r|<br>h|exp (¡10)¡Yn|(exp (¡10)¡Yn) =h|
|1|5.0000e-001|4.0000e+000|8.0001|
|2|2.5000e-001|3.3750e+000|13.5002|
|3|1.2500e-001|1.0644e-004|0.0009|
|4|6.2500e-002|4.4992e-005|0.0007|
|5|3.1250e-002|3.6375e-005|0.0012|
|6|1.5625e-002|2.2937e-005|0.0015|
|7|7.8125e-003|1.2790e-005|0.0016|
|8|3.9063e-003|6.7400e-006|0.0017|



Notamos que hay valores de h para los cuales la aproximación es inaceptable y que la última columna de la tabla tiende a estabilizarse. Lo primero indica que h debe ser su…cientemente pequeña y lo segundo sugiere que el orden del método es 1: Pero estas son solo observaciones que más tarde precisamos con claridad. Por ahora, consideramos un ejemplo muy parecido al anterior. 

### Ejemplo 29 Resolver y<sup>0</sup> = 5y; y(0) = 1. 

La tabla 2 contiene resultados para este ejemplo, que fueron obtenidos con un M-archivo muy similar al del ejemplo 28. Esta tabla contiene una columna de error relativo debido a lo difícil que es, en general, entender la calidad de una aproximación con el error absoluto como único estimado. 

||Tabla|2: Método de|Euler, y<sup>0</sup>= 5y|; y (0)= 1|
|---|---|---|---|---|
|r|<br>h|Er. absoluto|Er. relativo|(exp (¡10)¡Yn) =h|
|1|5.0000e-001|144.9132|0.9764|289.8263|
|2|2.5000e-001|137.0225|0.9233|548.0901|
|3|1.2500e-001|118.4923|0.7984|947.9387|
|4|6.2500e-002|89.3265|0.6019|1429.2235|
|5|3.1250e-002|58.3382|0.3931|1866.8221|
|6|1.5625e-002|34.0847|0.2297|2181.4207|
|7|7.8125e-003|18.5481|0.1250|2374.1591|
|8|3.9063e-003|9.6934|0.0653|2481.5193|



107 

6.7. Método de Euler 

Las correspondientes …guras ilustran mejor lo que está pasando: como la solución exacta estalla, o sea, tiende a in…nito, también debe hacerlo la solución aproximada. Se observa de nuevo que h debe ser su…cientemente pequeño y se sigue la misma convención: La línea a trozos identi…ca la solución aproximada y la continua es la exacta. 



<!-- Start of picture text -->
yprima = 5y, n = 2  yprima = 5y, n = 4<br>150  150<br>100  100<br>50  50<br>0  0<br>0  0.5  1  0  0.5  1<br>yprima = 5y, n = 8  yprima = 5y, n = 16<br>150  150<br>100  100<br>50  50<br>0  0<br>0  0.5  1  0  0.5  1<br>yprima = 5y, n = 32  yprima = 5y, n = 64<br>150  150<br>100  100<br>50  50<br>0  0<br>0  0.5  1  0  0.5  1<br>yprima = 5y, n = 128  yprima = 5y, n = 256<br>150  150<br>100  100<br>50  50<br>0  0<br>0  0.5  1 0  0.5  1<br><!-- End of picture text -->

108 

6. Ecuaciones diferenciales ordinarias 

### 6.7.1 Análisis de error 

El análisis de error para métodos de un paso, y muy en especial, para el método de Euler, es nuestro siguiente punto a tratar. Los ejemplos an­ teriores, aunque sencillos, plantean inquietudes con respecto al tamaño de h; que aparecen también en ejemplos complejos y en otros métodos de solución. 

Sea y (t) alguna solución de y<sup>0</sup> = f (t; y) y sean t<sup>¤</sup> y h …jos. De…nimos el error de truncación local en t<sup>¤</sup> , denotado ¿<sup>¤</sup> ; por la ecuación 



La discrepancia entre y (t<sup>¤</sup> + h) y y (t<sup>¤</sup> )+hG (t<sup>¤</sup> ; y (t<sup>¤</sup> ) ; h; f ) está dada por el término h¿<sup>¤</sup> : Esta última expresión corresponde a la fórmula de avance que propone el método numérico (6.6): 

En el caso del método de Euler, la correspondiente expresión (6.7) es 



Por teorema de Taylor, 



<u>1</u> 

donde ¾ está entre t<sup>¤</sup> y t<sup>¤</sup> + h: Es decir, ¿ e = 21 hy<sup>00</sup> (¾) : 

En este punto es conveniente introducir la notación O; que se lee O grande. 

De…nición 30 Si F (t; h) es una función de…nida para t0 · t · b y para todo h su…cientemente pequeño, entonces la notación 



para algún r > 0 signi…ca que hay una constante c tal que 



La notación O grande se usa especialmente para comparar funciones o sucesiones. Podemos decir que si 



109 

6.7. Método de Euler 

entonces F (t; h) converge a 0 cuando h ! 0 al menos tan rápido como h<sup>r</sup> : Entre sucesiones también es útil. Por ejemplo, puesto que n + 1 2 · 2 ; entonces n µ n1 ¶ 



n + 1 Esto implica que converge a 0 cuando n ! 1 al menos tan n<sup>2</sup> 1 rápido como : 

n 

De acuerdo con la de…nición anterior y recordando la suposición sobre y de tener un número su…ciente de derivadas, podemos decir que el error de truncación local en el método de Euler cumple ¿ e = O (h) : 

En general para métodos de un paso, si ¿ = O (h<sup>p</sup> ) ; se dice que el método es de orden p: 

Nótese que esta clasi…cación depende de la suavidad de las soluciones para y<sup>0</sup> = f (t; y) : Puede suceder que un método de orden p para un problema y<sup>0</sup> = g (t; y) no se comporte como tal por ser g una función sin la suavidad requerida. Algo análogo sucede con el método de Newton para resolver numéricamente ecuaciones de la forma F (x) = 0: Aunque el método se clasi…ca como de convergencia cuadrática, no siempre exhibe esa clase de convergencia. 

Volvamos al análisis de error del método de un paso (6.6). Denotemos ej = y (tj) ¡ Yj el error global en tj y para h = b<sup>¡ t0</sup> , sea ¿ = n j =1max ;2;:::;n<sup>j</sup> ¿ j j ; donde ¿ j es el error de truncación local en tj = t0 + jh; j = 1; 2; :::; n: 

Teorema 31 Supongamos que G satisface la condición de Lipschitz 



para todo h que cumple 0 < h · b ¡ t0; para todo t 2 [t0; b] y para todo u; v; ¡1 < u; v < 1: Entonces 

6. Ecuaciones diferenciales ordinarias 

110 

Una demostración detallada de este teorema puede encontrarse en Johnson y Riess (1982) [19]. 

La cota del lado derecho es en general imposible de conocer por la di…cultad para aproximar a ¿ y K: Además, a menudo no es pequeña, a no ser que h sea demasiado pequeña. Por tanto, la información que proporciona este teorema es eminentemente cualitativa y no es muy útil a la hora del cálculo numérico. 

Nótese que en el ejemplo 28, K = 10 y ¿ · 50h: El teorema anterior asegura que 



lo cual no dice mucho. 

### 6.7.2 Consistencia 

Para continuar con el análisis de error, consideremos de nuevo el Teo­ rema 31. Allí se a…rma que un método de un paso es convergente si se cumple la condición de consistencia, que dice simplemente 



Pero hay otra forma de enunciar la condición de consistencia: de (6.7) vemos que 



donde h¿ j es el error de truncación local en tj: Esta expresión la re­ escribimos así: 



Como y<sup>0</sup> (tj) = f (tj; y (tj)) ; vemos que, tomando límites, la condición de consistencia se puede expresar simplemente como 



Volveremos a considerar consistencia al …nal de la sección, cuando veamos otros métodos de diferencias. Por ahora continuemos con el análisis. 

111 

6.7. Método de Euler 

### 6.7.3 Estabilidad 

Pasemos ahora, basados en Atkinson (1978) [4], a enunciar un estimado de estabilidad para el método de Euler. En pocas palabras podemos decir que estabilidad es continuidad con respecto a los datos. 

De…nición 32 Consideramos un PVI 



y una perturbación del mismo dada por 



donde j"j · ½ y k±k1 · ½; para algún ½: Decimos que el método de un paso con fórmula de avance 



es estable, si las soluciones Y y Z de (6.10) y 

Zj+1<sup>= Z</sup> j<sup>+ hG (t</sup> j<sup>; Z</sup> j<sup>; h; f (t</sup> j<sup>; Z</sup> j<sup>) + ± (t</sup> j<sup>)) con Z</sup> 0<sup>= y</sup> 0<sup>+ "</sup> respectivamente, cumplen 



Debe advertirse que hay varias clases de estabilidad. Para el método de Euler, chequear que se cumple esta de…nición es bastante rápido. Las fórmulas de avance del método de Euler son, respectivamente, 



y 



donde 



Sea ej = Zj ¡ Yj . Esta diferencia satisface el siguiente estimado: 



Claramente, si ½ ! 0; entonces ej ! 0 para todo j; es decir, el método de Euler es estable. 

112 

6. Ecuaciones diferenciales ordinarias 

### 6.7.4 Errores de redondeo 

Otra cosa es propagación de error de redondeo. Cómo se comporta el método de Euler al respecto? Continuamos siguiendo a Atkinson (1978) [4]. Supongamos que y0 se conoce exactamente. Teniendo en cuenta errores de redondeo, el método de Euler para (6.4) tiene la forma 

Uj+1 = Uj + hf (tj; Uj ) + " j<sup>;</sup> 

donde U0 = y0 y j = 0; 1; :::; N: Recordemos que el error de truncación en cada paso se de…ne por la ecuación 



y denotemos Ej = Uj ¡ y (tj ) el error total cometido en el paso j: Si 



entonces el error Ej satisface 



que, de acuerdo con (6.8) y con la hipótesis de su…ciente suavidad para y, tiene la forma 



con C1 y C2 constantes positivas. Muy frecuentemente, la grá…ca del lado derecho de (6.11) tiene la siguiente forma: 



<!-- Start of picture text -->
Error c*h + epsil/h<br>1.4<br>1.2<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>0 0.05  0.1  0.15  0.2  0.25<br>h<br><!-- End of picture text -->

113 

6.7. Método de Euler 

En esta grá…ca se condensa una de las precauciones más importantes que se deben tener en el uso de métodos numéricos: Se quiere h pequeño " para que ¿ sea pequeño pero no muy pequeño para que no sea deh masiado grande. Situaciones como ésta se presentan siempre que se re­ suelve un problema en un computador. Tomar a h demasiado pequeño obliga a hacer muchas iteraciones que invitan al error de redondeo a ser protagonista en los cálculos. 

### 6.7.5 Estabilidad absoluta 

Muy relacionado con lo que estamos tratando es el concepto de estabi­ lidad absoluta, que en pocas palabras, signi…ca que el método numérico no aumenta errores pasados. Para estudiar la estabilidad absoluta se recurre a la ecuación de prueba 



El método de Euler aplicado a esta ecuación tiene la forma 



lo cual lleva por iteración, a la ecuación 



Es decir, de la única manera que el método de Euler no aumenta errores iniciales es pidiendo 



Al intervalo más grande de la forma (a; 0) tal que si h¸ 2 (a; 0) entonces se cumple (6.13), se le llama intervalo de estabilidad absoluta. Para el método de Euler, es, por supuesto, (¡2; 0) : Terminamos con unos comentarios: 

1. El método de Euler no puede ser absolutamente estable cuando ¸ ¸ 0: 

2 2. Si ¸ < 0; entonces 0 < h < : Pero de acuerdo con el apartado ¡ ¸ anterior, h no puede tomarse demasiado pequeño. Por consiguiente, 

114 

6. Ecuaciones diferenciales ordinarias 

existe un intervalo de valores positivos en el que h debe situarse para obtener la mejor aproximación por medio del método numérico. Este es un enunciado de tipo práctico. Los enunciados teóricos exigen con­ siderar h ! 0: 

3. Los problemas escalares del tipo (6.12) son el caso 1 £ 1 de los problemas lineales 



donde A es una matriz. Estos problemas tienen interés por si mismos pero además, surgen cada que se quiere considerar la linearización de problemas no lineales, que es una herramienta muy valiosa a la hora de estudiar equilibrios de sistemas dinámicos. Sugerimos Hale y Kocak (1991) [13] para profundizar sobre el tema. 

Terminamos esta sección con la forma de construir otros métodos de Taylor y con la de…nición del método clásico de Runge-Kutta. 

## 6.8 Métodos de Taylor 

Los métodos de un paso para la solución de (6.4) se de…nieron en (6.6). Hay muchos métodos de un paso, por ejemplo, a partir del teorema de Taylor, se pueden de…nir otros si la expansión (6.5) se reemplaza por una de más alto orden. 

La expansión de Taylor de orden 2 es 



donde ´ está entre t y t + h: Para la escritura de y<sup>00</sup> en términos de f; se utiliza la regla de la cadena. De aquí se deduce el método de un paso conocido como método de Taylor de orden 2; que se de…ne como en (6.6) con 



Los subíndices t y y indican derivadas parciales con respecto a la primera y la segunda variables de f respectivamente. 

115 

6.9. Métodos de Runge-Kutta 

El inconveniente principal que tienen los métodos de Taylor, es la necesidad de evaluar a f y a varias de sus derivadas parciales en cada iteración. Actualmente esa es una tarea menos dispendiosa gracias a los paquetes de software que permiten computación simbólica. Pero todavía el tiempo para hacer un cálculo numérico es considerablemente menor que el de hacer el mismo cómputo con cálculo simbólico. 

## 6.9 Métodos de Runge-Kutta 

Los métodos de Runge-Kutta son métodos de un paso que en lugar de requerir evaluaciones de derivadas parciales de f; lo que requieren es evaluaciones de f en puntos cuidadosamente escogidos. El más famoso de todos los métodos de Runge-Kutta es llamado clásico. Se de…ne por medio de (6.6) con 



donde 



La deducción de métodos de Runge-Kutta que requieren únicamente dos evaluaciones de la función f; es un ejercicio que recomendamos. Aparece en muchos libros, por ejemplo, Kincaid y Cheney (1994) [21] o Stoer y Bulirsch (1992) [30]. 

## 6.10 Ejercicios 

1. Comprobar que el método de Taylor orden 2 y el método RungeKutta clásico satisfacen la condición de consistencia (6.9). 

116 

6. Ecuaciones diferenciales ordinarias 

2. Demostrar que si f satisface la condición de Lipschitz del Teorema 26, entonces las funciones G de los métodos mencionados en el ejercicio anterior satisfacen la condición de Lipschitz del Teorema 31. 

## 6.11 Problemas con valores en la frontera 

Los problemas con valores en la frontera en dos puntos, PVF en lo sucesivo, son más complicados que los problemas de valor inicial, entre otras cosas porque los teoremas de existencia y unicidad son más elabo­ rados y menos generales. Entre los investigadores del tema, destacamos a Keller, quien ha propuesto varios resultados importantes, muchos de los cuales están consignados en su libro Keller (1990) [20]. Un compen­ dio actualizado hasta …nes de los 80’s es Ascher, Mattheij y Russell (1995) [3] que también recomendamos a quienes deseen profundizar en el tema. 

Un PVF se de…ne así: Encontrar una solución y (t) de un sistema de n ecuaciones diferenciales ordinarias, 



que satisfacen una condición de borde de una de las siguientes clases: 



en la que la función r puede ser no lineal en una o ambas de sus dos componentes, 



donde A y B son matrices de orden n y c 2 R<sup>n</sup> o …nalmente, 



donde A1 y A2 son matrices de n columnas y c1; c2 son vectores con el mismo número de …las de A1 y A2 respectivamente. A las condiciones de borde (6.14) se les llama separadas. En todos los casos, ¡1 < a < b < 1: 

117 

6.11. Problemas con valores en la frontera 

En estas notas, consideramos únicamente funciones y y f de valor real y condiciones de borde separadas. Es decir, nos restringimos a trabajar con ecuaciones diferenciales ordinarias de segundo orden de la forma 



junto con condiciones de borde 



donde A y B son constantes. La función f puede depender de forma lineal o no lineal de su segunda variable. 

Lo primero que hacemos es una ilustración de las di…cultades que se pueden presentar en cuanto a existencia y unicidad. Dos ejemplos sencillos de PVF con la forma (6.15) - (6.16) son: 



y 



En el primer caso, la única solución es 



donde las constantes C1 y C2 son las componentes del vector solución del sistema 



En el segundo caso, no siempre hay solución y cuando hay, no es única, pues las soluciones son de la forma 



pero al aplicar condiciones de borde, se llega a A = C2 = ¡B y no aparecen restricciones para C1: Por tanto, las soluciones de (6.17) con A = ¡B; son 



con C1 cualquier constante y si A 6= ¡ B no hay solución. 

118 

6. Ecuaciones diferenciales ordinarias 

## 6.12 Diferencias …nitas y método de colocación para PVFs 

Existencia y unicidad Diferencias …nitas Método de Newton Colocación 

En esta sección presentamos un teorema de existencia y unicidad, debido a Keller, y explicamos los métodos numéricos más sencillos para la solución de PVFs. La exposición la basamos en Kincaid y Cheney (1994) [21] y Stoer y Bulirsch (1992) [30]. Además, en algunos apartes, sobre todo en lo que tiene que ver con M-archivos y ejemplos, seguimos a López (2000) [22]. 

## 6.13 Existencia y unicidad 

Decimos que el PVF (6.15) - (6.16) es de clase M si la función f (t; y) cumple las siguientes condiciones: 

a. f (t; y) está de…nida y es continua en la franja [a; b] £ R: 

b. (Condición de Lipschitz) Existe una constante L tal que para todo t 2 [a; b] y cualquier par de números u1 y u2; 



c. fy (t; y) es continua y no negativa en la franja [a; b] £ R: 

Teorema 33 (Keller) Todo PVF de clase M tiene una única solución. 

Nótese que las condiciones a. y b. de arriba son las mismas que se requieren en el teorema fundamental de existencia y unicidad de los PVI que estudiamos antes. 

## 6.14 Diferencias …nitas 

Una posible discretización de diferencias …nitas para este problema es como sigue: Se genera una subdivisión del intervalo [a;b]; en n + 1 subintervalos de igual longitud h = b<sup>¡</sup> a ; de manera que los nodos n + 1 

119 

6.15. Método de Newton 

de la malla sean tj = a + jh; con j = 0; 1;:::;n + 1: Enseguida para j = 1; 2; :::; n; aproximamos la segunda derivada y<sup>00</sup> (tj) por el cociente 



y entonces resulta natural querer resolver el sistema 



con v0 = A; vn+1 = B y para j = 1;:::;n; vj son las aproximaciones de los valores y(tj) utilizados para los cálculos: Tenemos entonces un sistema, en general no lineal, de n ecuaciones con n incógnitas v1; v2; :::; vn, que generalmente se resuelve por un método iterativo de tipo Newton. Expandido, el sistema es el siguiente: 



Suponemos que este sistema tiene solución para preservar sencilla esta exposición. Advertimos, sin embargo, que estudiar condiciones su…cientes o necesarias para existencia de soluciones de sistemas no lin­ eales, es un tema de investigación actual que está lleno de sutilezas y di…cultades. 

## 6.15 Método de Newton 

El método de Newton para nuestro sistema se enuncia más fácilmente con notación vectorial. Denotamos por V al vector columna cuyas com­ ponentes son v1; v2; :: : ; vn y de…nimos una función de variable y valor vectorial G de la siguiente manera: 



con la componente j¡ ésima de GV igual al lado izquierdo de la ecuación j¡ ésima en (6.18). De esta forma, el sistema que nos ocupa se puede 

6. Ecuaciones diferenciales ordinarias 

120 

denotar simplemente como GV = 0: Su solución por el método itera­ tivo de Newton exige en cada iteración, la solución de un sistema lineal de ecuaciones. Más precisamente, se procede así: 



donde el superíndice indica orden de iteración y W es la solución del sistema de ecuaciones 



donde la matriz J es el jacobiano de G en el punto V<sup>(k)</sup> = (v1; v2; : : :; vn)<sup>T</sup> , en el cual omitimos los superíndices para no recargar la exposición. Para cada iteración, J es la matriz tridiagonal dada por 



para i = 1; 2;: : :; n y haciendo v0 = A y vn+1 = B: 

El algoritmo numérico debe incluir un número máximo de iteraciones como criterio de parada y algún otro criterio de parada basado en lo cercanos que son los iterados consecutivos, utilizando alguna de las normas que de…nimos al principio. 

En resumen: el método de diferencias …nitas para PVF lleva a un sistema de ecuaciones, posiblemente no lineal, que generalmente debe tratarse por un método iterativo para su solución. Cuando se enuncia un método de Newton, que es uno de los más comunes y poderosos, se ve la necesidad de resolver, en cada iteración un sistema tridiagonal de ecuaciones lineales. 

El siguiente ejemplo sirve para a…rmar las ideas expresadas arriba. 

Ejemplo 34 Resolver el PVF y<sup>00</sup> = t (y<sup>0</sup> )<sup>2</sup> en [0; 2] ; con y(0) =<sup>¼</sup> y 2 ¼ y(2) = : La solución exacta es y (t) = arccot y la usamos para 4 2 µ t ¶ comparación con la solución obtenida por diferencias …nitas. 

El siguiente M-archivo es tomado de López 2000 [22]. 

function pvfDFnl(fun,gun,hun,p1,p2,v1,v2,n,m,tol,wun) 

6.15. Método de Newton 121 % Solución numérica de P.V.F no lineal % y’’=f(x,y,y’) a<= x <=b % y(a)=v1 y(b)=v2 % por el método de diferencia finita. % pvfDFnl(’fun’,’gun’,’hun’,p1,p2,v1,v2,n,m,tol,’wun’) % fun= f(x,y,y’). % gun= derivada con respecto a y de f(x,y,y’). % hun= derivada con respecto a y’ de f(x,y,y’). % wun= solución exacta del P.V.F. % p1=a p2=b % n= número de subintervalos % m= número máximo de iteraciones % tol= tolerancia a=zeros(n-1,1);b=zeros(n-2,1);c=zeros(n-2,1); d=zeros(n-1,1); h=(p2-p1)/n;k=1;pe=(v2-v1)/(p2-p1); x=p1:h:p2;w=feval(wun,x’); y=v1+pe*(x’-p1); while k<=m for i=1:n-1 t(i)=(y(i+2)-y(i))/(2*h); a(i)=2+(h^2)*feval(gun,x(i+1),y(i+1),t(i)); d(i)=y(i)-2*y(i+1)+y(i+2)-(h^2)*feval(fun,x(i+1),y(i+1),t(i)); end for i=1:n-2 b(i)=-1+(h/2)*feval(hun,x(i+1),y(i+1),t(i)); c(i)=-1-(h/2)*feval(hun,x(i+2),y(i+2),t(i+1)); end J=diag(a)+diag(b,1)+diag(c,-1); v=Jnd; y=y+[0;v;0]; if norm(v)<tol disp([x’,w,y]); disp([k,norm(y-w)]); disp(’ éxito’);break end k=k+1; 

122 

6. Ecuaciones diferenciales ordinarias 

end if k>m disp(’excede # iteraciones’); end % Las siguientes instrucciones muestran una gráfica de la solución % con las aproximaciones obtenidas subplot(1,2,1); plot(x,y,’r’); xlabel(’Tiempo’); title(’PVF no lineal’) hold on fplot(wun,[p1 p2],’k*’); zoom hold off subplot(1,2,2); % Gráfica de los errores ee=w-y; plot(x,ee,’k’); title(’Error’); print -deps2 .nfignpvfDFnl.eps 

Con este archivo generamos las siguientes …guras: 



<!-- Start of picture text -->
PVF no lineal  -5  Error<br>x 10<br>1.6  6<br>1.5<br>1.4<br>1.3  4<br>1.2<br>1.1<br>1  2<br>0.9<br>0.8<br>0.7  0<br>0 0.5  1 1.5  2  0 0.5  1 1.5  2<br>t t<br><!-- End of picture text -->

123 

6.16. Ejercicios 

## 6.16 Ejercicios 

1. Repita el procedimiento de diferencias …nitas explicado arriba para el PVF 



con condiciones de borde 



2. Escriba un M-archivo que se encargue de resolver un PVF de la forma (6.19)-(6.20). Aplique este programa para resolver numérica­ mente los siguientes casos concretos: 

a. y<sup>00</sup> + 2y<sup>0</sup> + 10t = 0; y(0) b. y<sup>00</sup> = ¡y; y(0) = 3; y = 7: ³ ¼ 2<sup>=</sup> ´<sup>1; y(1) = 2:</sup> 

c. y<sup>00</sup> = 2e<sup>t</sup> ¡ y; y(0) = 2; y(1) = e + cos (1) : 

3. Para los tres ejemplos propuestos en el numeral anterior, encuentre la solución exacta y repita 2. calculando, además de la solución, la distribución del error en los puntos de la malla. Calcule además la norma 2 del error. 

4. En 2. utilice mallas uniformes de tamaño de paso 2<sup>¡k</sup> ; k = 2; 3; :::; 10: Gra…que k VS Norma 2 del error. 

## 6.17 Método de colocación 

La solución numérica que se obtiene con diferencias …nitas es una lista de números fv0; v1; :::; vn; vn+1g : El primero y el último son valores de frontera no calculados y los otros n se obtienen como solución de un sistema de ecuaciones. Con este resultado, podemos construir una función discreta 



6. Ecuaciones diferenciales ordinarias 

124 

con asignación tj ¡! vj; j = 0; 1; :::; n; n+1: A esta función la podemos extender a todo el intervalo con una regla sencilla como la siguiente: 



Además, esta función se puede pensar como una combinación lineal de B-splines de grado cero. Para ésto, nos conviene pensar que la malla de los tj hace parte de la malla de…nida para todos los reales 



Los B-splines de grado cero se de…nen así 



Estas funciones satisfacen 



y además, tienen soporte compacto. Para una descripción de los B- splines, recomendamos Kincaid y Cheney (1994) [21]. 

La función F se representa 



Esta es apenas una de las posibles extensiones de F: Pudimos pre­ tender, por ejemplo, una extensión continua y lineal a trozos o muchas otras. La idea es que para muchas de esas extensiones F; se encuentre una colección de funciones, digamos<sup>©</sup> Áj ª ; para la que se cumple una igualdad de la forma (6.21), es decir, 



El método de colocación, consiste en considerar estas ideas en orden inverso, es decir, dada una colección de funciones<sup>©</sup> Áj ª ; obtener una 

125 

6.17. Método de colocación 

función F; dada por (6.22), que aproxima la solución del PVF (6.15) - (6.16). En los casos en que el PVF es lineal, el análisis es sencillo. El problema consiste en identi…car los coe…cientes vj por medio de la solución de un sistema lineal de ecuaciones. La matriz de este sistema es dada por bandas cuando las funciones Áj tienen soporte compacto. 

Los B-splines se usan frecuentemente por tener soporte compacto y también son muy comunes las funciones trigonométricas. En este último caso, se habla de métodos espectrales para la solución de ecuaciones diferenciales. Tienen la ventaja de ser rápidos en el computador pues generalmente el procedimiento numérico está basado en transformadas rápidas de Fourier. El libro Trefethen (2000) [33] es una reciente y útil referencia para métodos espectrales. El mismo autor ofrece en Internet Trefethen (1996) [32], que es un moderno libro inconcluso sobre solución numérica de ecuaciones diferenciales que también se re…ere al tema de los métodos espectrales. 

Presentamos las ideas del método de colocación para el PVF 



Aquí, las funciones p; q y w se supone que son continuas en [0; 1] y la función incógnita u es un elemento del espacio 



Para la de…nición del método, nos basamos en el operador lineal 



Escogemos un conjunto de funciones de V; digamos 



y un conjunto de puntos, llamados de colocación o interpolación, 



Queremos encontrar una función 



126 

6. Ecuaciones diferenciales ordinarias 

tal que 

Lv (ti) = w (ti) ; i = 1; :::; n: 

A tal función la encontramos, gracias a la linealidad de L; por medio de la solución del sistema lineal de ecuaciones 



en el que las aj conforman el vector de incógnitas. 

La importancia del método de colocación es tal, que en MATLAB 6, release 12, hay un M-archivo llamado bvp4c.m, que sirve para resolver PVFs por un método de colocación. Por su parte, Trefethen (2000) [33], trae un poderoso método llamado de colocación espectral, que permite resolver PVFs, lineales y no lineales, de forma rápida y con gran precisión. Para este método, los puntos de colocación son los ceros de los polinomios de Chebyshev. 

Concluimos esta subsección con un ejemplo recomendado por Kin­ caid y Cheney [21] en sección 8.10. 

Ejemplo 35 Resolver por el método de colocación el PVF y<sup>00</sup> + 4y = cos (t) en ; con y (0) = y = 0; utilizando las funciones de h0;<sup>¼</sup> 4<sup>i</sup> ³ ¼4 ´ k t : prueba vjk (t) = t<sup>j ³¼</sup> 4<sup>¡</sup> ´ 

Debido a la necesidad de tomar derivadas hasta de orden 2, opta­ mos por utilizar exponentes j y k de 3 en adelante. Para resolver este ejemplo preparamos un sencillo M-archivo que permite trabajar hasta con 25 puntos de colocación solamente. Mejorar esta rutina tal vez no se justi…ca, por las razones expuestas a continuación. La rutina es: 

function u=pvf1(a,b,n) 

% pvf1.m, metodo de colocacion 

- % Herramienta didactica, Carlos E. Mejia, 2002 

- % problema general: Ly=y’’+py’+qy = w 

- % basado en Kincaid y Cheney seccion 8.10 

% a, b: limites del intervalo % n: numero de nodos de colocacion y de funciones de prueba h = (b-a)/(n+1);t = a+h:h:b-h; 

6.17. Método de colocación 

127 

% coeficientes q=4*ones(size(t));w=cos(t)’;p=zeros(size(t)); for m=1:n [j k]=poten(m); lv = j*(j-1)*vf(j-2,k,t)-2*j*k*vf(j-1,k-1,t)+k*(k-1)*vf(j,k-2,t); lv = lv + p.*(j*vf(j-1,k,t)-k*vf(j,k-1,t)) + q.*vf(j,k,t); ma(:,m)=lv’; end %c=manw; c=bicgstab(ma,w,1e-4,50); up=cell(size(c));u=zeros(size(c)); for m=1:n [j k]=poten(m); up{m}=vf(j,k,t)’; u=u+c(m).*up{m}; end ex=exaf(t);er=u-ex’; er2=sqrt((1/(n+2))*sum(er.^2)) ee2=norm(er) T=[0 t pi/4];ex=[0; ex’; 0];u=[0; u; 0]; plot(T,u,’r’,T,ex,’k--’) axis([0 pi/4 -.4 .4]) title(’Método de Colocación’) xlabel t, print -deps2 .nfigncol2.eps Los polinomios básicos se generan por medio de la función vf.m y la solución exacta está en exaf.m. La rutina poten.m se ocupa de asignar exponentes j y k a cada índice m: La incluimos por completez: function [j,k]=poten(m) if m>=1 & m<6 j=3+m-1;k=3; elseif m>=6 & m<11 j=3+m-6;k=4; elseif m>=11 & m<16 j=3+m-11;k=5; elseif m>=16 & m<21 j=3+m-16;k=6; 

128 

6. Ecuaciones diferenciales ordinarias 

elseif m>=21 & m<26 

j=3+m-21;k=7; 

end 

Al invocar u=pvf1(0,pi/4,7), obtuvimos la siguiente grá…ca: 



<!-- Start of picture text -->
Método de Colocación<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>-0.1<br>-0.2<br>-0.3<br>-0.4<br>0 0.1  0.2  0.3  0.4  0.5  0.6  0.7<br>t<br><!-- End of picture text -->

Para poder resolver el sistema lineal, tuvimos que acudir a un so…sticado método iterativo para la solución del sistema de ecuaciones (6.24). Se trata de BI-CGSTAB, publicado por primera vez por H. A. van der Vorst en 1992. Se trata de un método de gradiente conjugado con biortogonalización, que además posee un caracter estabilizador. MAT­ LAB incluye este método en la rutina bicgstab.m. Para saber más sobre este método recomendamos Trefethen y Bau (1997) [34]. 

Los resultados son de inferior calidad a los obtenidos antes por dife­ rencias …nitas para un problema no lineal. Hay una razón numérica de peso para esperar pobres resultados. Se trata de los polinomios escogi­ dos como funciones básicas, que no se escogieron en ninguna familia de polinomios ortogonales. Los polinomios escogidos generan sistemas lineales muy mal condicionados. 

Un caso análogo y muy famoso, es el de tratar de usar los poli­ nomios x<sup>j</sup> ; como funciones básicas para construir el polinomio que sea la mejor aproximación de una función dada en el sentido de los mínimos cuadrados. Con la función constante 1 como función de ponderación, el sistema lineal al que se llega es uno de los más mal condicionados de 

129 

6.18. Ejercicios suplementarios 

los que se tenga noticia, pues la matriz del sistema es la temida matriz 1 de Hilbert Hn; cuyo elemento (i; j) es : A medida que crece i + j + 1 n; el tamaño de la matriz, también aumenta el número de condición de Hn: Más detalles de este interesante ejemplo pueden verse en Atkinson, 1978 [4], sección 4.3. 

## 6.18 Ejercicios suplementarios 

1. El problema de calcular la integral de f se puede pensar como la solución del PVI 



cuya solución es 



Muestre que el método de Euler aplicado a (6.25) es equivalente a la regla del rectángulo para (6.26) y si se aplica a (6.25) el método clásico de Runge-Kutta de cuarto orden, es lo mismo que aplicar la regla de Simpson compuesta a (6.26). 

2. Aplique el método de Euler y el método clásico de Runge-Kutta al PVI 

   - y<sup>0</sup> = t<sup>2</sup> + (y (t))<sup>2</sup> ; y (0) = 1; t ¸ 0: 

Compare los dos resultados. Tenga en cuenta que la solución de este PVI no existe para todo t: 

3. Intente resolver, por el método de Euler, los ejemplos 2. y 3. de la sección de ejemplos 25. Puede haber di…cultades, debe tratar varios valores de h: 

4. Considere este otro problema de especies en competencia. 





con condición inicial y1 (0) = 80 y y2 (0) = 30: Utilice un método de alto orden, por ejemplo ode45 de MATLAB, para resolver 

130 

6. Ecuaciones diferenciales ordinarias 

este problema y gra…car su diagrama de fase. Enseguida, use el método de Euler para el mismo problema con diferentes valores de h; digamos h = 1; 0:5; 0:25 y 0:125: Probablemente los nuevos diagramas de fase no concuerdan con el que ya obtuvo por el método de alto orden. Explique motivos para esta discrepancia. 

5. (Continuación) En el problema anterior, cambie la condición ini­ cial por cada una de las siguientes: (81; 30) ; (80; 31) ; (79; 30) y (80; 29) : Este es un test de estabilidad, determina qué tan grandes son los cambios en la solución del PVI cuando ocurren pequeños cambios en la condición inicial. 

6. Considere el PVI 



cuya solución exacta es y (t) = e<sup>¡100t</sup> +1: Este es un problema de los llamados sti¤. Es claro que la solución decrece rápidamente de 2 a casi 1 y después se queda prácticamente horizontal. Com­ pruebe que esta situación hace difícil resolver este problema por el método de Euler. Trate varios valores de h para convencerse. Una alternativa bastante buena es utilizar el método de Euler hacia atrás, de…nido por la ecuación en diferencias 



Este es un método implícito que permite resolver este problema sti¤ sin mayores contratiempos. Compruébelo! Sugerencia: En el método de Euler, los iterados son 



y en el método de Euler hacia atrás, son 



7. Considere el PVF 



131 

6.19. Examen de entrenamiento 

a. Aproxime la solución del PVF con un polinomio de grado 3 que satisface los valores v (0) ; v (1) ; v<sup>00</sup> (0) y v<sup>00</sup> (1) : b. Aproxime la solución del PVF por medio del método de dife­ rencias …nitas. 

## 6.19 Examen de entrenamiento 

Resuelva estos ejercicios sin consultar libros ni notas de clase para darse una idea del nivel de preparación que ha obtenido hasta ahora. Una calculadora sencilla es lo mínimo que debe tener a disposición y es su…ciente para poder responder todos los ejercicios del examen. Claro que es preferible si dispone de una calculadora gra…cadora o un computador. 

1. Determine las constantes de Lipschitz para las siguientes fun­ ¡ 

ciones en [ 1; 1]: 

a. f (t; y) = t<sup>2</sup> y: 

- b. f (t; y) = t exp (¡y<sup>2</sup> ) : 



¿Qué solución de este PVI será la que aproxima el método de Euler? 

3. Resuelva por el método de Euler con h = 0:25; el siguiente PVI: y0 = 2ty; y (0) = 1; 0 · t · 1: 

4. Convierta los PVIs siguientes, dados en términos de ecuaciones escalares de grado 2, a PVIs con variable vectorial. 

   - a. y<sup>00</sup> = ¡sen (y) ; y (0) = ¼=2; y<sup>0</sup> (0) = 0: 

   - b. y<sup>00</sup> ¡ y = t; y(0) = 1; y<sup>0</sup> (0) = 1: 

132 6. Ecuaciones diferenciales ordinarias 

# 7 

# Ecuaciones diferenciales parciales 

Ecuaciones de tipo parabólico Diferencias …nitas con condiciones de borde de tipo Dirichlet Ecuaciones no lineales y otras condiciones de borde Consistencia, estabilidad y convergencia Dos dimensiones Métodos ADI 

## 7.1 Diferencias …nitas para problemas parabólicos 

En esta sección nos referimos brevemente a la solución de ecuaciones diferenciales parciales por diferencias …nitas. Para la exposición, nos basamos en Smith (1978) [28] y Kincaid y Cheney (1994) [21] pero re­ comendamos consultar también referencias más completas como Strik­ werda (1989) [31] y el libro clásico Richtmyer y Morton (1967) [27]. El objetivo es motivar el estudio a partir de ejemplos sencillos de dis­ cretizaciones de diferencias …nitas de problemas de tipo parabólico. 

A partir de MATLAB 6, release 12, hay una rutina especial para re­ solver una amplia gama de ecuaciones unidimensionales de tipo parabólico o elíptico. Se trata de pdepe.m. Además, desde hace varios años, ex­ iste una caja de herramientas especializada en ecuaciones diferenciales parciales. Aquí no nos referimos a ninguna de estas alternativas que ofrece MATLAB. Quedan como temas llamativos para cuando estas notas crezcan en esta dirección. 

134 

7. Ecuaciones diferenciales parciales 

## 7.2 Ecuaciones de tipo parabólico 

La ecuación diferencial parcial de tipo parabólico más sencilla es la ecuación unidimensional 



La variable espacial x se toma en un intervalo [a; b] y la variable tem­ poral t se toma en el intervalo semi-in…nito [0; 1): Las condiciones de borde se de…nen para x = a y x = b y para todo t: La condición inicial se de…ne para x 2 (a; b) y t = 0: La ecuación (7.1) tiene validez en (a; b) £ (0; 1) : Esta ecuación da cuenta de procesos difusivos lineales, por ejemplo, la conducción de calor. Debido a ésto, muy frecuentemente nos referimos a la variable dependiente como temperatura, aunque este modelo se puede utilizar en muchos otros procesos. 

Consideremos discretizaciones uniformes en espacio y tiempo dadas por 



donde h y k son los tamaños de paso en las direcciones de espacio y tiempo respectivamente. Ambos son reales positivos. Es conveniente de…nir también 



## 7.3 Diferencias …nitas 

En todas las aproximaciones de diferencias …nitas utilizamos la varia­ ble discreta Vij para representar la aproximación de u en el punto de la malla (xi;tj ) que se calcula por medio del método numérico. Sea h = b<sup>¡</sup> a y supongamos que tenemos condiciones de borde de tipo n + 1 Dirichlet para x = a = x0 y x = b = xn+1; es decir, los elementos V0 j y Vnj +1<sup>son conocidos para todo j: Además, de…nimos la variable</sup> discreta vectorial V<sup>j</sup> = £V1 j; V2 j; :::; Vn j<sup>¤</sup> para representar el vector de aproximaciones en el nivel temporal j: Nótese que una condición inicial signi…ca que el vector V<sup>0</sup> es conocido. Posteriormente consideramos otras condiciones de borde. 

135 

7.3. Diferencias …nitas 

### 7.3.1 Métodos más comunes 

Distinguimos varias expresiones de diferencias …nitas que aproximan (7.1).Veamos algunas: 

1. Método explícito, es decir, la temperatura Vi<sup>j+1</sup> se escribe en tér­ minos de temperaturas en niveles anteriores en la escala temporal. 



que conduce a 



¡ Sea A = trid (r; 1 2r; r) la matriz tridiagonal de orden n con elemen­ ¡ tos diagonales 1 2r y elementos super y sub diagonales iguales a r: La igualdad (7.2) se puede escribir 



lo que indica que 



Los iterados consecutivos se consiguen por aplicación de potencias de A a la condición inicial. 

2. Método implícito, es decir, la temperatura Vi<sup>j+1</sup> se escribe en tér­ minos de temperaturas en el mismo nivel y en niveles anteriores de la escala temporal, 



que se puede escribir 



¡ Sea A = trid (¡r; 1 + 2r; r) la matriz tridiagonal de orden n con elementos diagonales 1 +2r y elementos super y sub diagonales iguales ¡ a r: La igualdad (7.5) se puede escribir 



136 

7. Ecuaciones diferenciales parciales 

Es decir, en cada paso temporal, se debe resolver un sistema de ecua­ ciones lineales con matriz simétrica, tridiagonal y diagonalmente dom­ inante (por tanto no singular). 

3. Métodos mixtos dependientes de un parámetro ® 2 [0; 1] : 



Los dos métodos anteriores son casos particulares de éste, basta hacer ® = 0 y 1 respectivamente. El más importante de los métodos mixtos 1 es el que corresponde a ® = que se llama de Crank-Nicolson. Está 2 dado por la igualdad 



que también podemos escribir 



Sean A = trid (¡r; 2 (1 + r) ¡ r) y B = trid (r; 2 (1 ¡ r) ; r) matrices de orden n: La ecuación (7.7) se escribe como el sistema 



con V<sup>j+1</sup> como incógnita. Este es el sistema que debe resolverse para cada iteración temporal. 



La solución exacta es u (x;t) = exp sen : Preparamos ¡ 4 ³ ¼x 2 ´ µ ¼<sup>2</sup> t<sup>¶</sup> 

un M-archivo para resolver el problema con diferentes valores para r y n: La calidad o falta de calidad de los resultados, sugieren que r debe cumplir algún requisito para obtener resultados útiles. Esto lo con…rmamos más adelante en la subsección 7.8. 

137 

7.3. Diferencias …nitas 

||Métodos explícito e<br>|implícito<br>|
|---|---|---|
|n r|Error(explícito)|Error(Implícito)|
|10 0.5|4.1813e-002|3.0735e-002|
|10 0.8|2.1062e-002|4.4402e-003|
|20 0.5|1.1529e-002|8.6889e-003|
|20 0.8|5.6956e-003|1.2394e-003|
|30 0.5|5.2961e-003|4.0122e-003|
|30 0.8|8.7532e-003|6.6802e-003|
|40 0.5|3.0288e-003|2.2990e-003|
|40 0.8|3.6016e+001|1.4966e-003|
|50 0.5|1.9578e-003|1.4874e-003|
|50 0.8|2.6821e+011|1.7249e-003|
|60 0.5|1.3687e-003|1.0403e-003|
|60 0.8|4.7197e+022|1.2066e-003|



Estos resultados indican que el método implícito tiende a ofrecer mejores resultados y que el método explícito ofrece algunos totalmente inaceptables. Estos últimos se obtienen siempre para r = 0:8 pero no para n < 40: Posteriormente le daremos total sentido a esta tabla. Advertimos que los malos resultados están asociados con falta de es­ tabilidad y que en términos coloquiales, estabilidad signi…ca que los resultados no estallan. La razón por la que los resultados malos empe­ oran a medida que crece n; es porque hay que hacer más cálculos y por tanto hay más ocasión de propagar y agrandar los errores. 

### 7.3.2 Ejercicios 

1. Consideremos el problema 



para x 2 [0; 1] con condición inicial, condiciones de borde y solución exacta dadas por 



7. Ecuaciones diferenciales parciales 

138 

Utilice los tres métodos propuestos en la subsección 7.3.1 y obtenga la solución para t = 0:1: Trabaje con varios valores de h y k de manera que r tome los valores 0:1n; con n = 1; 2; :::; 8: 

2. Se trata de resolver el problema 



para x 2 [¡1; 1] con solución exacta y condiciones de borde dadas por 



y con condición inicial 



1 Encuentre la solución para t utilizando los tres métodos pro­ = 2 puestos en la subsección 7.3.1: Utilice varios valores de h y k de manera que r tome los valores 0:1n; con n = 1; 2; :::; 8: 

## 7.4 Ecuaciones no lineales 

Tal como vimos al principio de estas notas, el método de Newton es un recurso importante cuando se trata de afrontar un problema no lineal. Veamos un ejemplo sencillo que aparece como Ejemplo 2.7 en [28]. La temperatura u satisface la ecuación no lineal 



con condición inicial u (x) = 4x (1 ¡ x) ; 0 < x < 1; t = 0 y las condiciones de borde u = 0 para x = 0 y x = 1, t ¸ 0: Para estudiar el método de Newton aplicado a este problema, consideremos el siguiente M-archivo que se encarga de implementarlo: 

139 

7.4. Ecuaciones no lineales 139 function vnew=smith27ci(tfin,n); % Herramienta didactica, Carlos E. Mejia, 2002 % ecuacion parabolica no lineal en 1-D % ejemplo 2-7 de Smith % metodo de Newton para hallar ceros de F(x)=0 % tfin: tiempo final % n: numero de subintervalos en [0,1], n>2 % h: tamaño de paso en espacio % k: tamaño de paso en tiempo h=1/n; k=.5*h^2; % k puede definirse en otras formas si se desea p=h^2/k; % x: dominio espacial, xa: dominio espacial ampliado x=(h:h:1-h)’;xa=[0;x;1]; % vold: condicion inicial vold=4.*x.*(1-x); vnew=vold; t=0; while t<tfin va=[0;vnew;0]; plot(xa,va,’r’); title(’Difusion no lineal’); xlabel(’Espacio’) hold on; count=floor(t/k)+1; % condiciones de borde son homogeneas % diferencias finitas tomadas en ih y (j+1/2)k % g: parte de F(v), depende de v en tiempo anterior % fv: parte de F(v) que depende de v en tiempo actual % jf: matriz jacobiana de F in2=1;it=1; while in2>1.e-8 & it<10 g=zeros(n-1,1);fv=g;jf=zeros(n-1); g(1)=vold(2)^2-2*(vold(1)^2-p*vold(1));% 1 fv(1)=vnew(2)^2-2*(vnew(1)^2+p*vnew(1))+g(1); jf(1,1)=-4*vnew(1)-2*p; jf(1,2)=2*vnew(2); 

140 7. Ecuaciones diferenciales parciales g(n-1)=-2*(vold(n-1)^2-p*vold(n-1))+vold(n-2)^2;% 2 fv(n-1)=-2*(vnew(n-1)^2+p*vnew(n-1))+vnew(n-2)^2+g(n-1); jf(n-1,n-2)=2*vnew(n-2); jf(n-1,n-1)=-4*vnew(n-1)-2*p; for i=2:n-2 g(i)=vold(i+1)^2-2*(vold(i)^2-p*vold(i))+vold(i-1)^2;% 3 fv(i)=vnew(i+1)^2-2*(vnew(i)^2+p*vnew(i))+vnew(i-1)^2+g(i); jf(i,i-1)=2*vnew(i-1); jf(i,i)=-4*vnew(i)-2*p; jf(i,i+1)=2*vnew(i+1); end % solucion sistema lineal asociado con metodo de Newton in=jfn-fv; in2=norm(in); % actualizacion de vold y vnew vnew=vnew+in;it=it+1; end t=t+k;vold=vnew; end Explicamos ahora el método de diferencias utilizado. En el punto ih; j + k la aproximación de diferencias es 2 <u>µ</u> µ 1<sup>¶¶</sup> 1 2 2 2 2 2 2 ¡ ¡ (Vi;j+1 ¡ Vi;j) =<sup>1 ¡</sup> Vi¡1;j +1 2Vi;j+1 + Vi+1;j +1 + Vi 1;j<sup>¡ 2V</sup> i;j<sup>+ V</sup> i+1;j¢ k 2h<sup>2</sup> en donde las incógnitas se distinguen por el subíndice j + 1: Esta es la igualdad que de…ne la expresión no lineal que debemos resolver por el h<sup>2</sup> método de Newton. Hacemos p = y de…nimos las i¡ ésimas …las de k los vectores g (V ) y f (V ) ; de la siguiente manera 2 2 2 [g (V )]i = Vi¡1;j<sup>¡ 2</sup> ¡Vi;j ¡ pVi;j ¢ + Vi+1;j 2 2 2 [f (V )]i = Vi¡1;j+1<sup>¡ 2</sup> ¡Vi;j+1 + pVi;j+1¢ + Vi+1;j+1 

donde en g se reune lo conocido y f reune las incógnitas. Para i = 1 e i = n¡1 hay expresiones ligeramente diferentes debido a las condiciones homogéneas en el borde (Ver líneas marcadas % 1 y % 2 en el M-archivo de arriba. Para la expresión general, ver línea % 3.) La matriz jacobiana 

141 

7.4. Ecuaciones no lineales 

es jf y puede verse que también requiere de armado especial en las …las extremas por las condiciones de borde. 

En las grá…cas que adjuntamos, es clara la difusión, la tendencia de las temperaturas calculadas es hacia la temperatura nula. Al invocar smith27ci(0.5,10), se obtiene la grá…ca 



<!-- Start of picture text -->
Difusion no lineal<br>1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>Espacio<br><!-- End of picture text -->

y al invocar smith27ci(2,10), se consigue la siguiente: 



<!-- Start of picture text -->
Difusion no lineal<br>1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br>Espacio<br><!-- End of picture text -->

7. Ecuaciones diferenciales parciales 

142 

Naturalmente sabemos que esta presentación es apenas una invitación a consultar más acerca de cómo resolver problemas parabólicos no lin­ eales. En Richtmyer y Morton (1967) [27], pag. 201, hay un método para resolver 



que es fácilmente generalizable a la ecuación 



Los cálculos que presentan los autores para ilustrar su método, fueron realizados por ellos mismos en un computador Univac en el año 1954. Eran los primeros intentos por resolver problemas no lineales por dife­ rencias …nitas. 

## 7.5 Ejercicio 

Considere el problema 



y suponga que la solución u satisface la ecuación no lineal 



para todo t y x: 

a. Utilizando el método de Newton para ecuaciones no lineales, obtenga a partir de (7.9) la condición inicial, las condiciones de borde y la solu­ ción para t = 0:5. 

b. Utilice el método de Newton y el método de diferencias …nitas descrito antes para aproximar la solución de (7.8) en t = 0:5: Los resultados para t = 0:5 en las partes a. y b. deben coincidir. 

143 

7.6. Otras condiciones de borde 

## 7.6 Otras condiciones de borde 

En muchas circunstancias las condiciones de borde se expresan por medio de derivadas. Por ejemplo, la rata a la cual se trans…ere calor por radiación de una super…cie externa a temperatura u hacia el medio que la rodea que está a temperatura v; es proporcional a u ¡ v: Más aun, Fourier descubrió que tal rata es igual a 



donde K es la conductividad térmica del material. Todo ésto da lugar a una condición de borde de la forma 



donde H es una constante de proporcionalidad que se conoce como el coe…ciente de transmisión de calor. 

Para indicar el tratamiento de estas condiciones de borde por el método de diferencias …nitas, presentamos el ejemplo 2.3 de Smith (1978) [28]. Nótese que las derivadas en la dirección normal, se con­ vierten en este caso en derivadas con respecto a x: 

Ejemplo 37 Resolver por el método explícito (7.2) la ecuación 



que satisface la condición inicial 



y las condiciones de borde 



144 

7. Ecuaciones diferenciales parciales 

Recordamos que el método de diferencias que deseamos utilizar está dado por la igualdad 



k donde r = : En x = 0 y x = 1 optamos por utilizar nodos virtuales h<sup>2</sup> no pertenecientes a la malla para realizar los cálculos, en la siguiente forma: En x = 0; 



y la condición de borde, discretizada con diferencias centrales, nos lleva a 



Al eliminar lo correspondiente al nodo virtual i = ¡1 de estas dos ecuaciones, llegamos a 



Similarmente para x = 1 tenemos 



y la condición de borde, discretizada por diferencias centrales, nos da 



Por tanto para i = n + 1; la ecuación en diferencias es 



De (7.10) se obtienen n ecuaciones, correspondientes a i = 1; :::; n: De (7.11) se obtiene una más, correspondiente a i = 0 y …nalmente de (7.12) se consigue la ecuación que corresponde a i = n+1: El sistema de estas n +2 ecuaciones nos da la solución al ejemplo propuesto, siempre y cuando se respeten otras condiciones con respecto al valor de r; que son el tema de la sección siguiente. 

145 

7.7. Consistencia, estabilidad y convergencia 

## 7.7 Consistencia, estabilidad y convergencia 

Para esta subsección adoptamos la siguiente convención: 

L (u) = f representa la ecuación diferencial parcial en las variables independientes x y t con solución exacta u: El operador L es lineal e incluye implícitamente las condiciones de borde. 

Fh (V ) = f representa la aproximación de diferencias …nitas con solución exacta V: Implícitamente queda establecida la dependencia k = rh<sup>2</sup> y por tanto k ! 0 si y solo si h ! 0: 

v es una función continua de x y t con un número su…ciente de derivadas continuas de manera que L (v) se pueda evaluar en el punto (ih;jk) : 

La notación vij signi…ca la evaluación de v en (ih;jk) : Similarmente 

para la solución exacta u: 

Ti;j (v) = Fh ¡vij¢ ¡ L ¡vij¢ es el error de truncación en el punto (ih;jk) : j ei;j = ui ¡ Vi<sup>j</sup> es el error de discretización en el punto (ih; jk) : Si Ti;j (v) ! 0 cuando h ! 0; se dice que la ecuación en diferencias es consistente o compatible con la ecuación diferencial parcial. En todas las situaciones que nos interesan, Ti;j (v) = O (h<sup>s</sup> ) con s > 0: Si en el lugar de v escribimos la solución u; la cual restringimos a los puntos de la subdivisión, obtenemos 



La solución V de la ecuación en diferencias no es la que se obtiene en el computador, debido a los inevitables errores en los datos y de redondeo. Digamos que la que se obtiene es la solución numérica N: Al error V ¡ N se le denomina error de redondeo. El error total en el punto (ih; jk) está dado por 



Si uij ¡ Nij ! 0 cuando h ! 0, se dice que V converge a u: El error total se compone de dos partes, dadas por los dos sumandos en el lado derecho de (7.13). El primer sumando está asociado con la consistencia, como vimos antes. El segundo es más complicado pues tiene que ver con redondeo y no podemos pedir simplemente que tienda a cero cuando 

146 

7. Ecuaciones diferenciales parciales 

h ! 0; pues eso no ha de funcionar, como lo vimos con claridad en el análisis de estabilidad para PVI. Aquí también, estamos ante grá…cas como la presentada allá que repetimos por completez. 



<!-- Start of picture text -->
Error c*h + epsil/h<br>1.4<br>1.2<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>0  0.05  0.1  0.15  0.2  0.25<br>h<br><!-- End of picture text -->

La estabilidad la de…nimos así: Un método de diferencias …nitas es estable si el segundo sumando del lado derecho de (7.13) no crece sin límite. 

El teorema de equivalencia de Lax a…rma que para aproximaciones consistentes de diferencias …nitas, estabilidad es necesaria y su…ciente para convergencia. Como se ha visto ya, la consistencia está regida por la aproximación discreta elegida y por tanto se tiene completo control a este respecto. Pero con la estabilidad no hay reglas generales, ni límites a cero. La estabilidad depende, entre otros, de los datos, de las ecuaciones y del computador. Es la propiedad más difícil de alcanzar pero cuando se alcanza, se consigue todo, pues es equivalente a convergencia en presencia de consistencia. Recomendamos Richtmyer y Morton (1967) [27] para una presentación formal de este importante teorema. 

147 

7.8. Análisis Matricial de Estabilidad 

## 7.8 Análisis Matricial de Estabilidad 

Volvamos al método explícito (7.10) aplicado a la ecuación 



con condiciones homogéneas en el borde y una condición inicial u0 (x) : Supongamos que hay errores en la condición inicial y no los hay en el procedimiento de cálculo. Esta es una simpli…cación que hace más claro el análisis de estabilidad. Tenemos una nueva condición inicial discreta N 0 que origina nuevos iterados N j en el proceso. 

De acuerdo con (7.4), 



Por tanto el error en el paso j está dado, gracias a la linealidad, por 



que lleva a 



y para que este error no crezca sin límite, que es lo que llamamos estabilidad, requerimos que kA<sup>j</sup> k sea acotada cuando j ! 1. 

Recurrimos a un conocido teorema del álgebra lineal numérica que aquí citamos de Ortega (1990) [26], pag. 25. Antes vemos la siguiente de…nición. 

De…nición 38 Una matriz A es de clase M si para todos los valores propios ¸ tales que j¸j = ½ (A) ; se cumple que todos los bloques de Jordan asociados con ¸ son 1 £ 1: 

Teorema 39 kA<sup>j</sup> k es acotada cuando j ! 1 si y solo si ½ (A) < 1 o ½ (A) = 1 y A es de clase M. 

En el caso del método explícito (7.10), estamos ante la matriz 

A = trid (r; 1 ¡ 2r; r) 

148 



de la que se sabe que tiene n valores propios distintos, por tanto es diagonalizable y en particular, es de clase M. 

Los n valores propios distintos de A son 



y queremos 



Nótese que 



1 y esta última desigualdad es cierta si y solo si r · 2 : 

Los métodos de diferencias que son estables para todos los valores de r se llaman incondicionalmente estables. Los demás, como el método explícito que acabamos de considerar, se denominan condicionalmente estables. 

## 7.9 Ejercicios 

Considere los métodos de diferencias de…nidos en la subsección 7.3.1. 

1. Compruebe que son consistentes con la ecuación diferencial. 

2. Compruebe que los valores propios de la matriz A asociada con el método (7.2) son los listados arriba. 

3. Realice un análisis matricial de estabilidad para el método implíc­ ito (7.5) y para el método de Crank-Nicolson. Demuestre que ambos son incondicionalmente estables. 

4. Para el método explícito (7.2) aplicado a la ecuación 



con condiciones homogéneas en el borde y una condición inicial u0 (x) ; 1 demuestre directamente que la condición 0 < r · 2 es su…ciente para 

149 

7.10. Dos dimensiones 

estabilidad, probando que lleva a soluciones acotadas para la ecuación en diferencias. 



j Después haga W<sup>j</sup> = max i ¯¯Vi ¯¯ y concluya que 



lo que implica 



## 7.10 Dos dimensiones 

La más sencilla de las ecuaciones parabólicas en dos dimensiones es 



con condición inicial dada en el rectángulo cuando t = 0 y condiciones de borde en los cuatro lados del rectángulo. 

Los métodos vistos antes se pueden extender para este problema de forma completamente natural, sin embargo, la solución en el com­ putador es laboriosa y no recomendable. Trabajamos con la siguiente convención: Los parámetros de discretización espacial son h1 y h2; co­ rrespondientes a las direcciones x y y respectivamente, los puntos en el eje x son a + ih1; los puntos en el eje y son c + jh2; el espaciamiento en tiempo está regido por el parámetro k como antes y la variable disc­ reta de la ecuación en diferencias es de nuevo V . Un punto de la malla espacio-temporal está dado por (a + ih1; c + jh2; sk) ; donde i; j; s son enteros. 

150 

7. Ecuaciones diferenciales parciales 

Para escribir de forma compacta las ecuaciones en diferencias que corresponden a (7.14), utilizamos la siguiente convención: 

I es el operador de diferencias correspondiente a la identidad. D<sup>2</sup> i<sup>es el operador de diferencias correspondiente a la segunda derivada</sup> en la dirección de x si i = 1 y y si i = 2: Entonces, por ejemplo, D12 se de…ne por la igualdad 



La extensión del método explícito (7.10) para (7.14) es 



La validez de este método está dada por la condición de estabilidad, que es 



Esta condición obliga a trabajar con un parámetro k exageradamente pequeño, lo cual no es deseable. De manera que no es recomendable utilizar este método. 

De forma similar se pueden generalizar a la ecuación (7.14) el método implícito y el método de Crank-Nicolson. Este último es 



El método de Crank-Nicolson para (7.14) es incondicionalmente estable, lo cual es conveniente, pero no es recomendable porque para cada paso en el sentido temporal, o sea de nivel s a nivel s + 1; el esfuerzo computacional que se requiere es grande. 

### 7.10.1 Métodos ADI 

En esta sección introducimos brevemente los métodos ADI, llamados así por la sigla en inglés que corresponde a Alternating Direction Im­ plicit. Estos métodos fueron desarrollados a partir de 1955 por Peaceman, Rachford y Douglas, a quienes en la década de los sesenta se 

151 

7.10. Dos dimensiones 

unieron otros investigadores, entre los cuales mencionamos a Hubbard, D’Yakonov, Mitchell y Fairweather. Se trata de métodos potentes, espe­ cialmente si la ecuación está de…nida en un rectángulo, que mejoraron en gran medida la velocidad y exactitud de los cálculos y se usan inten­ samente desde antes de conocerse con precisión las condiciones para su validez. Sobre rectángulos y con condiciones de borde sencillas, estos métodos son incondicionalmente estables. 

Uno de los métodos ADI más utilizados es conocido en la liter­ atura como de Peaceman y Rachford y utiliza la importante estrategia predictor-corrector. Al resultado del paso predictor se le denota con 1 el superíndice s + pero no signi…ca que corresponda a los valores 2 de la temperatura buscada en los puntos con coordenada temporal s + k: 2 µ 1<sup>¶</sup> 

Este método se de…ne así: 



Cada uno de los pasos consiste en la solución de un sistema lineal de ecuaciones con matriz tridiagonal. Terminamos con un ejemplo tra­ bajado en detalle y un ejercicio del mismo estilo del ejemplo pero que debe trabajarse con coordenadas cilíndricas para volverlo un problema unidimensional. 

Ejemplo 40 (Johnson y Riess, 1982, ejemplo 8.4) Una placa cuadrada determinada por el producto de intervalos [¡1; 1]£ [¡1; 1] se encuentra a temperatura 0 cuando t = 0 y se sumerge en un medio de temperatura 1: Encuentre la distribución de temperatura de la placa en los tiempos 0:5; 1 y 1:8: 

Solución. No tenemos solución analítica pero el sentido común dice que la placa, eventualmente, debe adquirir la temperatura del medio. Preparamos el siguiente M-archivo para la solución de este ejercicio por el método ADI. 

152 

7. Ecuaciones diferenciales parciales 

function vnew= edp2dadi3(n,tfin) % Herramienta didactica, Carlos E. Mejia, 2002 % ecuacion u_t=u_xx+u_yy % Johnson y Riess, ejemplo 8.4 % edp2dadi3 % dominio: cuadrado [-1,1]x[-1,1] % es 0 cuando t=0, rodeado de medio a temperatura 1 % n: numero de subdivisiones en x e y % tfin: tiempo en el que se pide la solucion % metodo adi de Peaceman y Rachford rh=zeros(n,1); h=2/(n+1); k=h/2;r=k/h^2;ro=2/r; vold=zeros(n);vnew=vold;vint=vold; % I-(k/2)D_2 sub=-ones(n-1,1); d=(ro+2)*ones(n,1); id2=diag(sub,-1)+diag(d)+diag(sub,1); % I-(k/2)D_1 (distinto al anterior si espaciamiento en % x es diferente de espaciamiento en y) sub=-ones(n-1,1); d=(ro+2)*ones(n,1); id1=diag(sub,-1)+diag(d)+diag(sub,1); t=0; while t<=tfin % metodo adi % lado derecho predictor for j=1:n if j==1 rh(:)=1+(ro-2)*vold(:,1)+vold(:,2); elseif j==n rh(:)=vold(:,n-1)+(ro-2)*vold(:,n)+1; else rh(:)=vold(:,j-1)+(ro-2)*vold(:,j)+vold(:,j+1); end % solucion predictor rh(1)=rh(1)+1;rh(n)=rh(n)+1; 

153 

7.10. Dos dimensiones v=id1nrh; vint(:,j)=v(:); end % lado derecho corrector for i=1:n if i==1 rh(:)=1+(ro-2)*vint(1,:)+vint(2,:); elseif i==n rh(:)=vint(n-1,:)+(ro-2)*vint(n,:)+1; else rh(:)=vint(i-1,:)+(ro-2)*vint(i,:)+vint(i+1,:); end % solucion corrector rh(1)=rh(1)+1;rh(n)=rh(n)+1; v=id2nrh; vnew(i,:)=v(:)’; end % t=t+k;vold=vnew; end 

La siguiente es una copia de los resultados que este programa entrega en pantalla. >> vnew=edp2dadi3(8,1.8) vnew = 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 0.9999 0.9999 0.9999 0.9999 0.9999 0.9999 1.0000 1.0000 0.9999 0.9999 0.9999 0.9999 0.9999 0.9999 1.0000 1.0000 0.9999 0.9999 0.9999 0.9999 0.9999 0.9999 1.0000 1.0000 0.9999 0.9999 0.9999 0.9999 0.9999 0.9999 1.0000 1.0000 0.9999 0.9999 0.9999 0.9999 0.9999 0.9999 1.0000 1.0000 0.9999 0.9999 0.9999 0.9999 0.9999 0.9999 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 1.0000 

Este resultado es evidencia de la capacidad del método para resolver el problema. Debe tenerse cuidado con n o t grandes, pues el exceso de cálculos puede llevar a resultados anómalos mayores de 1 en algunos nodos y todo el proceso fracasa. 

154 

7. Ecuaciones diferenciales parciales 

### 7.10.2 Ejercicio 

Se tiene una esfera con centro 0 y radio 1 que en el tiempo t = 0 tiene temperatura 0: La esfera se sumerge en un medio de temperatura 1: Encuentre la distribución de temperatura en la esfera para t = 0:5; 1 y 1:8: 

Sugerencia: Utilice coordenadas cilíndricas y suponga que la tem­ peratura depende solamente de la distancia del punto al centro o sea que no depende ni de z ni de µ: Esta suposición se conoce como simetría @u circular, que también implica que = 0: @r ¯¯¯¯r=0 

La ecuación que nos ocupa es 



y por simetría circular, se convierte simplemente en 



Esta ecuación tiene una singularidad cuando r = 0: Pero como = 0; esta singularidad no ofrece di…cultades pues, la expansión @r @u<sup>¯¯</sup> ¯¯r=0 1 @u de Taylor de<sup>@u</sup> en torno a r = 0; nos permite concluir que = @r r @r ¯¯¯¯r=0 @<sup>2</sup> u @r<sup>2</sup> : ¯¯¯¯r=0 

Más detalles sobre ésto pueden encontrarse en Smith, 1978 [28], pag. 40. 

## 7.11 Ejercicios suplementarios 

1. Utilice el método explícito, el método implícito y el método de Crank-Nicolson para resolver el problema 



para x 2 [0; 1] con condición inicial, condiciones de borde y solu­ ción exacta dadas por 

u (t;x) = x 2 e¡t: 

7.11. Ejercicios suplementarios 



2. Modi…que los programas de computador que usó en el ejercicio anterior para que sirvan para el siguiente problema que incluye condiciones de borde con derivadas. 



para x 2 [0; 1] con condición inicial y solución exacta dadas por 

u (t; x) = [sen (¼x) + cos (¼x)] exp<sup>¡</sup> ¡¼<sup>2</sup> t¢ 

y con condiciones de borde 



3. Resuelva el problema parabólico no lineal 



con condiciones de borde homogéneas y condición inicial u (0; x) = sen (¼x) : 

4. Utilice el método ADI para resolver el problema 



para 0 < x < 2; 0 < y < 1; con 





Sugerencia: La solución exacta es 

¡ u (t;x; y) = exp ¡ 5¼<sup>2</sup> t¢ sen (2¼x) sen (¼y) : 

156 

7. Ecuaciones diferenciales parciales 

## 7.12 Examen de entrenamiento 

Resuelva este ejercicio sin consultar libros ni notas de clase para darse una idea del nivel de preparación que ha obtenido hasta ahora. Una calculadora sencilla es lo mínimo que debe tener a disposición y es su…ciente para poder responder el ejercicio. Claro que es preferible si dispone de una calculadora programable o un computador. 

Enuncie en el mayor detalle posible, el método de Crank-Nicolson para resolver el siguiente problema: 



con condiciones de borde y condición inicial dadas por 



Debe especi…car el sistema lineal al que se llega y sería muy bueno si lo puede resolver, aunque sea solamente con matrices pequeñas. 

# 8 

# Material de interés 

Referencias generales LAPACK Templates y otras colecciones de software MATLAB y otros 

## 8.1 Referencias generales 

Entre los libros de Métodos Numéricos que conocemos, mencionamos Stewart (1996) [29], Kincaid y Cheney (1994) [21], Mathews y Fink (2000) [23], Burden y Faires (1998) [6], Chapra y Canale (1999) [7] y James, Smith y Wolford (1985) [18] como libros básicos y los libros Isaacson y Keller (1994) [17], Atkinson (1978) [4] y Stoer y Bulirsch (1992) [30] como más avanzados. 

Para el tema de Algebra Lineal Numérica especí…camente, están, por ejemplo, Noble y Daniel (1989) [25], Trefethen y Bau (1997) [34] y Demmel (1997) [10]. Libros que se ocupan de computación cientí…ca son también referencias importantes. Entre ellos están Golub y Ortega (1993) [12] y el libro inconcluso Trefethen (1996) [32]. 

Enseguida nos referimos a herramientas computacionales que se justi…ca tener en cuenta a la hora de enfrentar los problemas de álgebra lineal numérica que se originan en la solución numérica de ecuaciones diferenciales. Las herramientas son de dos clases: las que se encargan de problemas generales o cajas negras, en las que el usuario confía aunque no entienda los algoritmos en los que están basadas y las que son hechas a la medida, con alto nivel de intervención por parte del usuario. 

Todas las herramientas mencionadas aquí son de alta calidad, todas trabajan en ambiente UNIX o LINUX y la mayoría también trabajan en ambiente WINDOWS, pero ese no es su ambiente nativo y a menudo hay que hacer muchos ajustes para lograr que funcionen bien en esas 

158 

8. Material de interés 

plataformas. 

## 8.2 LAPACK 

Entre las herramientas para problemas generales, destacamos a LA­ PACK (Linear Algebra Package) que es una colección de subrutinas escritas en FORTRAN 77 para resolver los problemas matemáticos más comunes que surgen a partir del modelamiento y que se enmarcan en el campo del álgebra lineal numérica. El desarrollo de LAPACK es una tarea que se empezó antes de 1980 y aun no termina. Al principio hubo dos colecciones de software, LINPACK que se ocupaba principalmente de la solución de sistemas lineales y de la descomposición en valores singulares y EISPACK, que se dedicaba a los problemas de va­ lores propios. LAPACK es el sucesor de ambos y a LAPACK le siguen otras colecciones, como ScaLAPACK, por ejemplo, de manera que el esfuerzo por dotar a la comunidad de herramientas computacionales de primer nivel y de dominio público, continúa. 

En Mejía, Restrepo y Tre¤tz [24], tuvimos la oportunidad de presen­ tar a LAPACK a un público general y aquí reproducimos algunas de las ideas que expusimos allá. La colección LAPACK, descrita en LA­ PACK Users’ Guide [2], se puede obtener libremente en NETLIB en la dirección 

< http : ==www:netlib:org=lapack= > : 

Allá también se puede obtener la mejor documentación disponible sobre LAPACK, incluyendo la Guía mencionada arriba. Las subrutinas de LAPACK se basan en llamadas a unas subrutinas más sencillas que se conocen por la sigla BLAS (Basic Linear Algebra Subprograms). Hasta el momento se dispone de subprogramas BLAS de tres niveles: Nivel 1, publicado en 1979, que se encarga de operaciones de vector con vector. Nivel 2, publicado en 1988, que se ocupa de operaciones de matriz con vector. Nivel 3, publicado en 1990, que se dedica a operaciones entre matrices. 

La construcción de LAPACK con base en los subprogramas BLAS genera un alto nivel de estandarización, proporciona gran rapidez de cálculo y hace más fácil hacer un seguimiento cuando se presentan di…cultades. La utilización de LAPACK es universal, no solo directa­ 

159 

8.3. Templates y otras colecciones 

mente, sino también como motor de cálculo en software con interfase grá…ca como OCTAVE, <http://www.octave.org>, desarrollado en la Universidad de Wisconsin. 

LAPACK incluye rutinas para resolver sistemas de ecuaciones lin­ eales, sistemas de ecuaciones lineales por mínimos cuadrados, proble­ mas de valores propios y problemas de valores singulares. 

## 8.3 Templates y otras colecciones 

Los autores de Templates for the Solution of Linear Systems: Build­ ing Blocks for Iterative Methods [5], algunos de los cuales participan también del proyecto LAPACK, se orientan hacia la descripción de al­ goritmos y ofrecen programas fuente en diversos formatos, entre ellos FORTRAN, C y lenguaje MATLAB. Ellos consideran su colección de rutinas como de las hechas a la medida, pues proporcionan los medios para que el usuario adapte las rutinas a sus necesidades. 

La preocupación de los autores es explicar los detalles, en ocasiones nada triviales, de los métodos iterativos más importantes en años re­ cientes. Aunque incluyen métodos estacionarios, ellos están ahí solo por completez. Los temas principales del libro y por tanto los objetivos de los principales templates, son los métodos iterativos no estaciona­ rios basados en subespacios de Krylov y diversas técnicas de precondi­ cionamiento. Tanto el libro como las rutinas en los diferentes formatos, se pueden obtener en NETLIB, en la dirección 

< http : =www:netlib:org=templates= > : 

Mencionamos …nalmente otras colecciones importantes que no están en el dominio público. 

La colección IMSL, ofrecida por Visual Numerics, con dirección in­ ternet 

< http : ==www:vni:com=products=imsl= > : 

Las colecciones ofrecidas por NAG, Numerical Algorithms Group, con dirección internet 

< http : ==www:nag:co:uk= > : 

160 

8. Material de interés 

Numerical Recipes, con dirección internet 

< http : ==www:nr:com= >; 

las cuales están respaldadas por un grupo de libros muy bien escritos en los que se explican en detalle los algoritmos. Los libros se pueden conseguir en Internet libres de costo o se pueden comprar, junto con el software, a precio moderado. 

## 8.4 MATLAB y otros 

Los paquetes de software que integran una ágil interfase con algorit­ mos de calidad para una gran cantidad de problemas matemáticos, aparecieron hacia …nes de los ochentas y mantienen su ascenso desde entonces. Para muchas tareas, estos paquetes son hoy la alternativa más económica en materia de tiempo pero no siempre en asuntos de dinero. Lo más importante que ofrecen es la capacidad de manipulación simbólica, la cual promete seguir siendo por un tiempo largo, esencial en la computación cientí…ca. 

Entre estos paquetes, mencionamos a MATLAB, MATHEMATICA, MAPLE y MUPAD entre los de carácter comercial, con direcciones internet 

< http : ==www:mathworks:com= >; 

< http : ==www:wolfram:com= >; < http : ==www:maplesoft:com=flash=index:html > y < http : ==www:mupad:de= > 

respectivamente. 

Entre los paquetes de dominio público que por cierto, utilizan a LA­ PACK como base para sus rutinas de cálculo, están SCILAB y OC­ TAVE, con direcciones internet 

< http : ==www ¡ rocq:inria:fr=scilab= > y < http : ==www:octave:org > : 

# Referencias 

- [1] M. Abramowitz and I. A. Stegun, eds., Handbook of Mathe­ matical Functions, Dover, 1970. 

- [2] E. Anderson, Z. Bai, C. Bischof, J. Demmel, J. Don­ garra, J. DuCroz, A. Greenbaum, S. Hammarling, A. McKenney, S. Ostrouchov, and D. Sorensen, LAPACK User’s Guide, SIAM, 1992. 

- [3] U. M. Ascher, R. M. M. Mattheij, and R. D. Russell, Nu­ merical Solution of Boundary Value Problems for Ordinary Dif­ ferential Equations, SIAM, 1995. 

- [4] K. E. Atkinson, An Introduction to Numerical Analysis, Wiley, 1978. 

- [5] R. Barrett, M. Berry, T. Chan, J. Demmel, J. Donato, J. Dongarra, V. Eijkhoui, R. Pozo, C. Romine, and H. van der Vorst, Templates for the Solution of Linear Sys­ tems: Building Blocks for Iterative Methods, SIAM, 1993. 

- [6] R. L. Burden and J. D. Faires, Análisis Numérico, Interna­ tional Thomson, sexta ed., 1998. 

- [7] S. C. Chapra and R. P. Canale, Métodos Numéricos para Ingenieros, McGraw Hill, tercera ed., 1999. 

- [8] W. Cheney and D. Kincaid, Numerical Mathematics and Com­ puting, Brooks/Cole Publishing Co., 1980. 

- [9] P. J. Davis and P. Rabinowitz, Methods of Numerical Inte­ gration, Academic Press, segunda ed., 1984. 

- [10] J. W. Demmel, Applied Numerical Linear Algebra, SIAM, 1997. 

162 

Referencias 

- [11] C. W. Gear, Numerical Initial Value Problems in Ordinary Dif­ ferential Equations, Prentice-Hall, 1971. 

- [12] G. Golub and J. M. Ortega, Scienti…c Computing, An Intro­ duction with Parallel Computing, Academic Press, 1993. 

- [13] J. Hale and H. Kocak, Dynamics and Bifurcations, SpringerVerlag, 1991. 

- [14] P. Henrici, Discrete Variable Methods in Ordinary Di¤erential Equations, John Wiley, 1962. 

- [15] ~~,~~ Elements of Numerical Analysis, Wiley, 1964. 

- [16] D. J. Higham and N. J. Higham, MATLAB Guide, SIAM, 2000. 

- [17] E. Isaacson and H. B. Keller, Analysis of Numerical Meth­ ods, Dover, 1994. 

- [18] M. L. James, G. M. Smith, and J. C. Wolford, Applied Nu­ merical Methods for Digital Computation, Harper and Row, ter­ cera ed., 1985. 

- [19] L. W. Johnson and R. D. Riess, Numerical Analysis, AddisonWesley, segunda ed., 1982. 

- [20] H. B. Keller, Numerical Solution of Two Point Boundary Value Problems, SIAM, 1990. 

- [21] D. Kincaid and W. Cheney, Análisis Numérico, AddisonWesley Iberoamericana, 1994. 

- [22] B. López, Solución numérica de problemas con valores en la fron­ tera en dos puntos, Trabajo de grado, carrera de Matemáticas, Universidad Nacional de Colombia, Medellín, 2000. 

- [23] J. H. Mathews and K. D. Fink, Métodos Numéricos con MAT­ LAB, Prentice Hall, tercera ed., 2000. 

163 

Referencias 

- [24] C. E. Mejía, T. Restrepo, and C. Trefftz, Lapack una colección de rutinas para resolver problemas de algebra lineal numérica, Revista Universidad EAFIT, 123 (2001), pp. 73–80. 

- [25] B. Noble and J. W. Daniel, Algebra Lineal Aplicada, Prentice Hall, tercera ed., 1989. 

- [26] J. M. Ortega, Numerical Analysis, a second course, SIAM, 1990. 

- [27] R. D. Richtmyer and K. W. Morton, Di¤erence Methods for Initial-Value Problems, Interscience Publishers, segunda ed., 1967. 

- [28] G. D. Smith, Numerical Solution of Partial Di¤erential Equa­ tions: Finite Di¤erence Methods, Oxford University Press, se­ gunda ed., 1978. 

- [29] G. W. Stewart, Afternotes on Numerical Analysis, SIAM, 1996. 

- [30] J. Stoer and R. Bulirsch, Introduction to Numerical Analysis, Springer Verlag, segunda ed., 1992. 

- [31] J. C. Strikwerda, Finite Di¤erence Schemes and Partial Dif­ ferential Equations, Wadsworth y Brooks/Cole, 1989. 

- [32] L. N. Trefethen, Finite Di¤erence and Spectral Methods for Ordinary and Partial Di¤erential Equations, disponible en http://web.comlab.ox.ac.uk/oucl/work/nick.trefethen/pdetext.html, 1996. 

- [33] ~~,~~ Spectral Methods in MATLAB, SIAM, 2000. 

- [34] L. N. Trefethen and D. Bau, Numerical Linear Algebra, SIAM, 1997. 

- [35] H. van der Vorst, ed., Copper Mountain Conference Proceed­ ings, SIAM, 2001. Publicadas como Vol. 23, No. 2 de SIAM Jour­ nal of Scienti…c Computing. 

