---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\UCCI-especializaciónProy Investigación\MODULO 7.PORAT\PORAT-18-01-23\BAYESIAN VS NEURONAL español.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]

Machine Translated by Google 

Revista  de  tecnología  de  procesamiento  de  materiales  164–165  (2005)  1430–1435 

Modelado  de  procesos  de  fabricación  por  sistemas  de  aprendizaje: El  clasificador  bayesiano  ingenuo  versus  redes  neuronales  artificiales 

Marcin  Perzyk  �,  Robert  Biernacki,  Andrzej  Kochanski 

Instituto  de  Procesamiento  de  Materiales,  Universidad  Tecnológica  de  Varsovia,  Narbutta  85,  02­954  Warszawa,  Polonia 

# Resumen 

Se  comparan  las  capacidades  de  modelado  de  dos  tipos  de  sistemas  de  aprendizaje:  el  clasificador  bayesiano  ingenuo  (NBC)  y  las  redes  neuronales  artificiales (ANN),  en  función  de  sus  errores  de  predicción  y  factores  de  importancia  relativa  de  las  señales  de  entrada.  Se  utilizaron  datos  industriales  reales  y  simulados.  Se encontró  que  NBC  puede  ser  una  herramienta  efectiva  y,  en  algunas  aplicaciones,  mejor  que  ANN.  ©  2005  Elsevier  BV  Todos  los  derechos  reservados. 

Palabras  llave:  Modelado;  Proceso  de  manufactura;  Sistemas  de  aprendizaje;  Clasificador  bayesiano  ingenuo;  Redes  neuronales  artificiales 

# 1.  Introducción 

El  diseño  y  el  control  de  los  procesos  de  fabricación  pueden  verse  favorecidos por  el  uso  de  herramientas  matemáticas.  En  la  práctica,  muchas  veces  nos encontramos  con  procesos  del  tipo  “caja  negra”,  cuya  naturaleza  física  es desconocida  o  muy  compleja.  Los  procesos  de  modelado  de  este  tipo  consisten en  establecer  la  relación  entre  las  señales  de  entrada  y  de  salida  (es  decir,  el resultado)  a  partir  de  un  cierto  número  de  casos  observados  (problema  de regresión).  Recientemente,  han  sido  las  redes  neuronales  artificiales  (ANN)  las que  se  han  utilizado  comúnmente  para  este  propósito.  Sus  aplicaciones  incluyen, por  ejemplo: 

- predecir  propiedades  de  productos  o  materiales  sobre  la  base  de  los  parámetros 

del  proceso  tecnológico  involucrado;  •  predecir  fallas  de  equipos  sobre  la base  de  señales  seleccionadas 

- nales; 

- identificar  las  causas  que  conducen  a  la  aparición  del  hombre defectos  de  fabricación  en  los  productos; 

- diseño  basado  en  los  datos  específicos  que  fueron  recopilados  en  la  industria y  generalizados  por  las  RNA. 

A  pesar  de  los  grandes  éxitos,  las  ANN  tienen  varias  deficiencias,  como  un proceso  de  capacitación  complejo  y  lento. 

y  ambigüedad  de  los  resultados.  El  mismo  problema  puede  ser  resuelto  por redes  con  diferentes  arquitecturas  y  topología  de  conexiones.  Además,  para  una red  en  particular,  cada  aprendizaje  genera  diferentes  pesos  de  sinapsis relacionados  con  el  alcance  de  los  mínimos  locales  de  errores  de  red  [2,5,6]. 

Esta  falta  de  unicidad  de  predicción  no  aparece  en  el  modelado  con  la ayuda  de  otras  herramientas  matemáticas,  como  los  polinomios  o  el  ingenuo clasificador  bayesiano  (NBC)  [3] ,  un  sistema  de  aprendizaje  simple  que  hace uso  del  cálculo  de  probabilidades.  Los  autores  del  artículo  no  conocen  ninguna aplicación  de  NBC  para  el  modelado  de  procesos  industriales. 

El  presente  proyecto  de  investigación  se  ocupa  de  un  análisis  de  la aplicabilidad  de  la  NBC  a  los  problemas  de  modelado  de  procesos  de  fabricación, análisis  que  reside  en  la  comparación  de  los  errores  de  predicción  de  la  NBC  y los  de  las  ANN,  así  como  en  la  comparación  de  la  importancia  relativa  factores de  señales  de  entrada  para  los  datos  modelados  con  la  ayuda  de  ambos sistemas.  Básicamente,  las  ANN  se  utilizan  interrogándolas,  es  decir,  mediante el  simple  cálculo  de  valores  de  salida  para  valores  asumidos  de  entradas.  Sin embargo,  para  facilitar  la  realización  de  tareas  tales  como  la  identificación  de  las causas  de  los  defectos  en  los  productos,  o  los  factores  críticos  para  una  falla  del equipo,  un  análisis  de  la  importancia  relativa  de  las  señales  de  entrada  parece ser  de  gran  utilidad.  De  manera  similar,  encontrar  parámetros  de  producción, que  son  los  más  significativos  para  obtener  efectos  físicos  o  económicos particulares,  puede  ayudar  en  la  optimización  de  la  fabricación. 

Autor  correspondiente.  Tel.:  +48  22  8429347;  fax:  +48  22  8499797. 

Dirección  de  correo  electrónico:  m.perzyk@wip.pw.edu.pl  (M.  Perzyk). 

proceso. 

0924­0136/$  –  ver  portada  ©  2005  Elsevier  BV  Todos  los  derechos  reservados.  doi:10.1016/ j.jmatprotec.2005.02.043 

Machine Translated by Google 

1431 

M.  Perzyk  et  al. /  Revista  de  tecnología  de  procesamiento  de  materiales  164–165  (2005)  1430–1435 

2.  Sistemas  de  aprendizaje  que  utilizan  el  clasificador 

bayesiano  na¨ıve 

Los  sistemas  que  utilizan  métodos  probabilísticos  suelen  basarse  en el  teorema  y  la  ecuación  bayesianos  [1]. 

Incluyen  los  clasificadores  bayesianos  (el  clasificador  óptimo,  sin 

importancia  práctica,  y  el  NBC)  así  como  las  redes  bayesianas  [3]. 

El  teorema  bayesiano  es  aplicable  en  el  caso  de  eventos  con  resultados conocidos  cuya  ocurrencia  depende  de  factores  que  los  preceden. Calculamos  la  probabilidad  de  que  un  factor  dado  sea  la  causa  de  un evento  particular  (el  efecto).  El  uso  del  NBC  requiere  el  cálculo  de probabilidades  sobre  la  base  de  un  conjunto  de  datos  de  entrenamiento preparado  adecuadamente,  que  consiste  en  ejemplos  descritos  por  medio de  atributos  y  el  concepto  objetivo.  El  uso  del  NBC  consiste  en  lo  siguiente: 

- Establecimiento  de  los  llamados  atributos  (categorías)  para  las  cantidades de  entrada  y  las  categorías  de  la  cantidad  de  salida  (el  concepto objetivo).  Cabe  señalar  que  la  NBC  requiere  el  uso  de  cantidades  que son  nominales  o  en  serie,  pero  no  de  carácter  continuo.  El  “valor”  de un  atributo  o  del  concepto  objetivo  se  define  marcando  su  pertenencia a  una  categoría  particular,  que  a  su  vez  puede  identificarse  verbalmente. Por  ejemplo,  algo  puede  ser  “muy  pequeño”,  “pequeño”,  “mediano”, “grande”  y  “muy  grande” (cinco  categorías)  o  “bueno”  y  “malo” (dos categorías).  •  Crear  el  conjunto  de  datos  de  entrenamiento  que  consta de  registros  que  incluyen  los  valores  de  los  atributos  de  todas  las 

- cantidades  de  entrada,  así  como  el  valor  correspondiente  de  la  cantidad de  salida.  •  Sobre  la  base  del  conjunto  de  datos  de  entrenamiento,  se estiman  las  probabilidades  de  categorías  particulares  de  la  cantidad  de 

- salida,  así  como  las  probabilidades  de  valores  particulares  de  atributos (categorías)  de  todas  las  cantidades  de  entrada  para  categorías  de salida  particulares.  Esta  fase  se  conoce  como  el  entrenamiento  del clasificador. 

- Sobre  la  base  de  las  probabilidades  estimadas  obtenidas  en  la  fase  de entrenamiento  se  pueden  calcular  las  probabilidades  de  ocurrencia  de cada  categoría  de  la  cantidad  de  salida  para  cualquier  caso  dado (cualquier  vector  de  entrada).  La  solución  dada  por  NBC  es  el  valor  de la  categoría  de  cantidad  de  salida,  que  obtuvo  el  valor  de  probabilidad más  alto.  Si  las  categorías  de  salida  se  crearon  asignando  rangos particulares  de  valores  de  salida  continuos  a  los  números  que representan  las  categorías,  es  posible  cambiar  el  número  de  la categoría  calculada,  por  ejemplo,  en  un  valor  original  medio  de  dicho rango. 

el  último  tipo,  en  el  que  se  conocen  las  dependencias  de  entrada­salida, permite  una  mejor  evaluación  de  la  corrección  de  la  predicción  de  los sistemas  de  aprendizaje.  Estos  conjuntos  de  datos  simulados  se  crearon sobre  la  base  de  ecuaciones  simples  supuestas  del  tipo  Y  =  f(X1,  X2, ...) de  la  siguiente  manera:  todos  los  valores  de  entrada  se  establecieron originalmente  al  azar  entre  0  y  1,  luego  la  salida  put  y,  finalmente,  se añadió  ±20%  de  ruido  de  distribución  de  tipo  gaussiano  a  los  valores  de entrada  generados.  En  el  presente  trabajo  se  utilizaron  los  siguientes conjuntos  de  datos: 

- Datos  industriales  1.  Resistencia  de  la  fundición  dúctil  en  función  de  su composición  química  [4].  Además  del  subconjunto  de  entrenamiento que  contiene  700  registros,  también  se  creó  el  subconjunto  de verificación,  que  contenía  90  registros.  •  Datos  industriales  2.  Las 

- cantidades  de  entrada  aquí  son  los  parámetros  del  proceso  de  producción que  están  relacionados  con  el  molde  de  arena  verde  (12  parámetros). La  cantidad  de  salida  es  la  apariencia  del  defecto  de  porosidad  del  gas en  las  fundiciones  de  acero.  En  este  caso,  la  salida  original  era  de  tipo discreto  (categoría  “1”:  sin  defecto,  categoría  “2”:  defecto).  El  conjunto de  datos  de  entrenamiento  contenía  172  registros  y  no  había  ningún conjunto  de  verificación. Los  datos  en  cuestión  fueron  presentados  y  analizados  en  detalle  en  el trabajo  de  dos  de  los  presentes  autores  [5]. 

- Datos  simulados  1.  El  conjunto  se  obtuvo  de  acuerdo  con  la  siguiente ecuación:  Y  =  X1  +  2X2  +  3X3  +  4X4  +  5X5. El  conjunto  de  entrenamiento  contenía  1000  registros,  mientras  que el  de  verificación  contenía  200  registros.  •  Datos  simulados  2.  El 

- conjunto  se  obtuvo  de  acuerdo  con  la  siguiente  ecuación:  Y  =  (6X1) 3 +  (10−3X2)  3 +  ∙∙∙  + 

- (1X7)  3 +  ∙∙∙  +  (1X12)  3.  Los  valores  de  salida  de  este  conjunto  tienen un  carácter  continuo.  El  conjunto  de  entrenamiento  contiene  1000 registros,  mientras  que  el  de  verificación  contiene  200  registros.  •  Datos 

- simulados  3.  Los  valores  de  salida  Y  de  este  conjunto  tienen  un  carácter binario,  0  ó  1,  dependiendo  de  si  la  suma  anterior  supera  o  no  un determinado  valor  límite.  Los  valores  de  los  datos  de  entrada  en  este caso  eran  idénticos  a  los  valores  en  el  conjunto  de  datos  simulados  2. El  valor  límite  se  eligió  de  tal  manera  que  la  proporción  del  valor  Y  =  1 en  el  conjunto  fuera  de  alrededor  del  15  %.  El  número  de  registros  en el  conjunto  es  como  en  los  datos  simulados  3. 

- Datos  simulados  4.  El  conjunto  de  entrenamiento  es  del  mismo  tipo  que los  datos  simulados  3.  Sin  embargo,  esta  vez  el  número  de  registros  es 172  y  no  hay  un  conjunto  de  datos  de  verificación. 

Los  datos  simulados  2–4  se  diseñaron  de  manera  que  hicieran  posible un  análisis  comparativo  de  los  resultados  seleccionados  de  estos  conjuntos con  los  resultados  obtenidos  para  los  datos  industriales  2. 

# 3.2.  Redes  neuronales  artificiales 

# 3.  Metodología  de  la  investigación 

## 3.1.  Conjuntos  de  datos 

Los  conjuntos  de  datos  utilizados  en  el  presente  trabajo  difieren  en  el carácter  de  dependencia  entre  las  señales  de  entrada  y  salida. Incluyen  datos  industriales  y  simulados.  los  conjuntos  de 

Las  redes  tenían  una  arquitectura  de  tipo  MLP  con  una  capa  oculta que  tenía  un  número  de  neuronas  igual  al  número  de  entradas  de  la  red. Para  mejorar  los  resultados  de  aprendizaje,  se  ha  aplicado  el  método  de entrenamiento  denominado  'recocido  simulado',  combinado  con  el  método convencional  de  retropropagación.  El  método  de  recocido  simulado  se utilizó  para  una  mejor  selección  de  los  valores  iniciales  de  las  sinapsis mientras  que  el 

Machine Translated by Google 

1432 

M.  Perzyk  et  al. /  Revista  de  tecnología  de  procesamiento  de  materiales  164–165  (2005)  1430–1435 

La  fase  de  retropropagación  del  aprendizaje  disminuyó  el  error  de  red. Para  los  datos  que  incluían  conjuntos  de  verificación  (prueba),  el  proceso de  aprendizaje  finalizaba  automáticamente  cuando  el  error  calculado  para el  conjunto  de  verificación  comenzaba  a  crecer.  Para  los  conjuntos  de datos  sin  verificación,  el  criterio  para  finalizar  la  sesión  de  aprendizaje  fue el  cambio  del  error  cuadrático  medio  en  una  sola  iteración  inferior  a  5  × 10−6.  Cada  red  ha  sido  entrenada  10  veces. 

El  factor  de  importancia  relativa  de  las  señales  de  entrada  se  puede definir  de  varias  maneras.  En  general,  debe  reflejar  el  grado  máximo  de cambio  de  la  salida  del  sistema  debido  a  posibles  cambios  en  las  entradas. La  definición  asumida  en  el  presente  trabajo  se  basa  en  las  máximas diferencias  entre  los  valores  de  salida  que  se  pueden  obtener  cambiando 

la  entrada  considerada  (dentro  del  intervalo  de  entrenamiento),  mientras que  las  entradas  restantes  se  mantienen  en  valores  asumidos aleatoriamente.  Esto  se  repite  varias  veces  y  se  calcula  el  promedio  de  las diferencias  máximas  para  esa  entrada.  Los  valores  así  obtenidos  para cada  entrada  se  normalizan  entre  0  y  1,  de  modo  que  la  entrada  más significativa  obtenga  el  rango  igual  a  1  y  la  menos  significativa,  el  rango igual  a  0. 

# 3.3.  El  clasificador  bayesiano 

En  el  presente  trabajo,  las  variables  continuas  se  tradujeron  en  valores de  atributos  y  categorías  mediante  la  inclusión  de  una  variable  particular en  un  rango  apropiado  de  su  valor  original,  con  un  número  particular asignado  al  rango.  Para  cada  uno  de  los  conjuntos  anteriores,  se  realizaron pruebas  para  establecer  el  número  de  rangos  (categorías)  para  los  valores de  entrada  y  salida.  En  una  sesión  de  aprendizaje  en  particular,  se  utilizó el  mismo  número  de  rangos  para  todas  las  variables.  Todos  los  cálculos para  el  NBC  se  programaron  en  el  lenguaje  VBA  para  Excel  y  se representaron  en  una  hoja  de  cálculo.  Cabe  señalar  que  los  conjuntos  de verificación  no  son  necesarios  para  entrenar  el  NBC.  Solo  se  pueden  utilizar para  evaluar  la  capacidad  de  predicción  del  sistema  en  el  caso  de  nuevos datos. 

La  Fig.  1  representa  los  resultados  de  los  ensayos  de  división  de  los valores  de  datos  continuos  en  categorías.  Las  curvas  muestran  errores medios  relativos  de  los  resultados  del  modelado  para  conjuntos  con diferentes  características.  En  el  caso  de  los  datos  industriales  2  (así  como 

Fig.  1.  Errores  de  predicción  de  la  cantidad  de  salida  por  parte  del  NBC  para  conjuntos  de datos  seleccionados  en  función  del  número  de  categorías. 

La  medida  de  la  importancia  de  una  entrada  se  define  como  la diferencia  máxima  posible  de  los  valores  de  probabilidad  dados  por  (1) para  esa  entrada.  Estas  diferencias  máximas  se  calculan  (y)  para  cada categoría  de  la  salida  c  y luego  se  promedian  sobre  todas  las  categorías  de  salida  posibles.  Los  k factores  de  importancia relativa  se  obtienen  normalizando  esos  promedios  en  el  intervalo  0­1. 

# 4.  Comparación  de  errores  de  NBC  y  ANN 

Se  identificaron  los  errores  promedio  de  los  resultados  de  predicción del  valor  de  salida  obtenidos  de  la  NBC  y  las  ANN,  considerando  su proporción  en  los  rangos  de  valores  característicos.  La  Fig.  2  representa las  distribuciones  de  errores  de  predicción  para  los  datos  simulados  1.  Del diagrama  se  deduce  que  las  ANN  son  capaces  de  modelar  las  dependencias caracterizadas  por  un  conjunto  de  este  tipo  de  manera  mucho  más  precisa, es  decir,  un  conjunto 

los  datos  simulados  3,  que  no  están  representados  en  el  diagrama)  el  error se  definió  como  el  porcentaje  de  categorías  falsas. 

Las  distribuciones  de  errores  para  los  datos  de  entrenamiento  y  verificación son  similares.  Los  números  asumidos  de  categorías  fueron  aquellos  que dieron  los  errores  más  bajos  para  los  datos  de  verificación  (o  los  datos  de entrenamiento  en  ausencia  de  los  datos  de  verificación). 

El  factor  de  importancia  relativa  para  el  NBC  se  calcula  sobre  la  base de  los  elementos  del  sistema  entrenado.  Una  entrada  Xi  influye  en  la categoría  de  la  salida  Y  a  través  de  las  probabilidades  condicionales  de  la forma: 



Fig.  2.  La  comparación  de  los  errores  de  predicción  de  salida  obtenidos  de  NBC  y  ANN (errores  mínimos  de  10  sesiones  de  entrenamiento)  para  el  conjunto  de  datos  simulados  1. 

Machine Translated by Google 

1433 

M.  Perzyk  et  al. /  Revista  de  tecnología  de  procesamiento  de  materiales  164–165  (2005)  1430–1435 

Fig.  5.  La  comparación  de  los  errores  de  predicción  de  salida  obtenidos  del  NBC  y  las ANN  (errores  promedio  de  10  sesiones  de  entrenamiento)  para  los  datos  con  salida binaria. 

Fig.  3.  La  comparación  de  los  errores  de  predicción  de  salida  obtenidos  del  NBC  y  las ANN  (errores  mínimos  de  10  sesiones  de  entrenamiento)  para  el  conjunto  de  datos simulados  2. 

ing  set:  para  sets  pequeños  es  el  NBC  el  que  da  mejores  resultados. 

que  tiene  dependencias  "claras"  y  que  es  relativamente  numeroso 

rous 

La  Fig.  3  presenta  las  distribuciones  de  error  para  el  conjunto  de datos  simulados  imitando,  hasta  cierto  punto,  el  carácter  del  conjunto  de datos  industriales  2,  pero  con  una  salida  de  tipo  continuo. 

Las  predicciones  de  ambos  sistemas,  que  modelan  las  complejas relaciones,  exhiben  grandes  errores.  Cabe  destacar,  sin  embargo,  que las  RNA  cumplieron  un  poco  mejor  su  tarea,  ya  que  la  proporción  de pequeños  errores  es  mayor  en  el  caso  de  este  sistema. 

# 5.  Factores  de  importancia  relativa  de  las  señales  de  entrada 

higos.  6­9  muestran  los  gráficos  de  los  factores  de  importancia  de la  señal  de  entrada  estimados  por  medio  de  los  métodos  discutidos  en  la Sección  3.  En  el  caso  de  las  ANN,  el  diagrama  también  muestra  la dispersión  de  los  resultados  de  10  sesiones  de  entrenamiento.  Las dispersiones  se  definieron  por  rangos  de  los  valores  apropiados. 

En  el  caso  de  los  datos  industriales  1  –  los  datos  con  una  salida 

continua,  el  NBC  es  claramente  mejor  que  las  ANN  en  la  predicción  de los  valores  de  salida  (ver  Fig.  4). 

La  Fig.  5  representa  una  comparación  de  la  distribución  de  errores caracterizada  como  los  porcentajes  de  categorías  falsas  para  los conjuntos  de  entrenamiento  con  salidas  binarias.  Las  respuestas continuas  de  las  RNA  se  tradujeron  a  forma  binaria  de  la  siguiente manera:  a  los  valores  del  rango  0–0,5  se  les  asignó  la  categoría  “1”, mientras  que  a  los  valores  del  rango  0,5–1  se  les  asignó  la  categoría  “2 ”.  Se  puede  ver  fácilmente  que  las  ANN  son  mucho  mejores  que  las  NBC para  modelar  las  dependencias  caracterizadas  por  la  salida  de  tipo binario  para  los  datos  industriales  1.  Por  otro  lado,  en  el  caso  de  datos simulados  el  nivel  de  éxito  depende  de  la  tamaño  del  tren 

Fig.  4.  La  comparación  de  los  errores  de  predicción  de  salida  obtenidos  de  NBC  y  ANN (errores  mínimos  de  10  sesiones  de  entrenamiento)  para  el  conjunto  de  datos  industriales 1. 

Fig.  6.  Valores  del  factor  de  importancia  relativa  de  las  cantidades  de  entrada  para  NBC y  ANN,  para  los  datos  simulados  1  (las  dispersiones  de  valores  obtenidos  de  las  ANN están  marcadas  con  líneas  verticales  en  negrita);  Los  gráficos  a  y  b  se  obtienen  para  dos simulaciones  diferentes  de  conjuntos  de  datos. 

Machine Translated by Google 

1434 

M.  Perzyk  et  al. /  Revista  de  tecnología  de  procesamiento  de  materiales  164–165  (2005)  1430–1435 

Fig.  7.  Valores  del  factor  de  importancia  relativa  para  señales  de  entrada  para  el  conjunto  de  datos 2  simulados . 

En  los  casos  representados  en  las  Fig.  6a  yb,  los  valores  del  factor de  importancia  relativa  calculados  generalmente  concuerdan  con  las expectativas  (la  distribución  de  los  valores  del  factor  de  importancia relativa  refleja  el  papel  creciente  de  las  cantidades  de  entrada consecutivas,  de  1  a  5).  Sin  embargo,  las  ANN  pueden  predecir  la importancia  de  las  señales  de  entrada  con  mucha  más  precisión  que NBC.  Además,  este  sistema  resultó  ser  más  sensible  al  ruido  generado aleatoriamente  en  el  conjunto  de  entrenamiento. 

Ese  hecho  se  reflejó  en  los  valores  considerablemente  diferentes  para las  señales  de  baja  importancia  para  dos  conjuntos  simulados  de acuerdo  con  la  misma  ecuación. 

higos.  7  y  8  representan  la  distribución  de  los  valores  del  factor  de importancia  relativa  de  los  conjuntos  de  datos  simulados  que  tienen  la misma  estructura  de  señales  de  entrada  y  difieren  con  respecto  al  tipo de  datos  de  salida  (Fig.  7  ­  datos  simulados  2,  con  una  salida  continua Fig.  8  –  dato  simulado  3,  con  salida  binaria).  Ambos  conjuntos  de  datos pertenecen  a  una  situación  hipotética  en  la  que  tratamos  de  averiguar cuál  de  los  12  parámetros  del  proceso  de  producción  podría  ser  la causa  de  la  disminución  de  la  calidad  del  producto.  El  primer  conjunto asume  que  el  parámetro  de  calidad  de  salida  en  cuestión  es  una 

cantidad  continua;  podría  ser,  por  ejemplo,  la  rugosidad  de  la  superficie o  alguna  propiedad  del  material.  El  segundo  conjunto  imita  la  situación típica  en  la  que  los  productos  se  clasifican  como  buenos  o  defectuosos. En 

Fig.  9.  Importancia  relativa  de  los  factores  de  producción  y  parámetros  ambientales  relacionados con  el  molde  de  arena  para  la  aparición  del  defecto  de  porosidad  gaseosa  en  las  fundiciones  de acero  (fuente  de  los  datos  industriales  [5]);  1  –  tiempo  desde  el  moldeo  hasta  el  vertido,  2  –  orden de  vertido,  3  –  número  del  equipo  de  moldeo  4  –  número  del  equipo  de  montaje,  5  –  índice  de calidad  del  molde,  6  –  índice  de  calidad  del  vertido,  7  –  contenido  de  humedad  de  la  arena  de moldeo,  8  –  permeabilidad  de  la  arena  de  moldeo,  9  –  resistencia  a  la  tracción  de  la  arena  de moldeo,  10  –  temperatura  ambiente  antes  del  día  de  colada,  11  –  temperatura  ambiente  en  la colada,  12  –  humedad  del  aire. 

en  el  caso  de  ambos  conjuntos  de  datos  se  supuso  que  la  señal  decisiva es  X1,  pero  la  suma  de  los  efectos  de  las  otras  seis  señales seleccionadas  (de  X7  a  X12)  puede  dar  el  mismo  resultado.  Por  otro lado,  se  supuso  que  las  señales  de  X2  a  X6  no  tenían  prácticamente importancia. 

Los  factores  de  importancia  relativa  obtenidos  tanto  de  las  ANN como  de  la  NBC  para  el  equipo  con  salida  continua  confirman  el  efecto claramente  notorio  de  la  señal  X1 ,  así  como  valores  de  factor  de importancia  relativa  generalmente  ligeramente  más  altos  de  las  señales de  X7  a  X12,  en  comparación  con  las  señales  de  X2  a  X6. 

En  el  caso  de  las  salidas  del  tipo  binario,  se  puede  observar  un aumento  dramático  en  la  dispersión  de  los  resultados  para  una  sesión de  entrenamiento  ANN  particular,  en  comparación  con  lo  que  se presenta  en  la  Fig.  7.  Aunque  la  señal  X1  tiene  el  valor  de  importancia promedio  más  alto,  la  siguiente  las  señales  (X6  y  X11)  no  son  muy diferentes.  Teniendo  en  cuenta  las  enormes  dispersiones,  no  se  puede afirmar  que  la  red  neuronal  haya  encontrado  una  señal  con  una importancia  tan  predominante.  Por  otro  lado,  los  resultados  de  la clasificación  realizada  por  la  NBC  son  de  carácter  inequívoco.  Vale  la pena  enfatizar  que  la  ambigüedad  de  las  predicciones  de  las  ANNs, que  se  manifiesta,  entre  otras  cosas,  en  las  altas  dispersiones  de  los valores  de  los  factores  de  importancia  relativa,  parece  inevitable,  a pesar  de  todos  los  esfuerzos  encaminados  a  su  reducción  [7]. 

La  Fig.  9  es  el  gráfico  de  importancia  relativa  de  las  causas  del defecto  de  porosidad  gaseosa  en  fundiciones  de  acero.  El  cuadro  se elaboró  a  partir  de  los  datos  industriales  obtenidos  en  el  proyecto  de investigación  descrito  en  la  referencia  [5].  El  objetivo  de  ese  proyecto era  la  identificación  de  las  causas  de  los  defectos  en  una  de  las fundiciones  colaboradoras. 

Fig.  8.  Valores  del  factor  de  importancia  relativa  para  las  señales  de  entrada  para  el  conjunto  de datos  3  simulados . 

El  diagrama  muestra  grandes  dispersiones  de  los  resultados obtenidos  en  sucesivas  sesiones  de  entrenamiento  de  ANN,  así  como la  ausencia  de  una  importancia  claramente  notoria  del  conjunto  de parámetros  que  fueron  identificados  como  causantes  de  defectos, mediante  otros  métodos  de  análisis  [5]. .  Los  factores  relevantes  fueron siete  parámetros  que  influyeron  en  la  presión  de  vapor  en  el  molde. 

Machine Translated by Google 

1435 

M.  Perzyk  et  al. /  Revista  de  tecnología  de  procesamiento  de  materiales  164–165  (2005)  1430–1435 

en  el  momento  del  vertido:  la  humedad  de  la  arena  verde  en  el 

momento  del  moldeo,  su  permeabilidad,  la  resistencia  (el  factor  que indica  indirectamente  la  humedad),  la  temperatura  ambiente  antes  del vertido  del  proceso  de  producción,  la  temperatura  ambiente  durante  el vertido,  la  tiempo  desde  el  moldeado  hasta  el  vertido,  y  la  humedad  del aire  antes  del  tiempo  de  vertido. 

El  grupo  anterior  de  señales  no  surgió  de  ninguna  manera  conspicua también  en  el  caso  de  la  NBC.  La  Fig.  9  muestra  como  muy  importante la  señal  “índice  de  calidad  de  vertido”,  que  fue  indicada  por  ambos sistemas  y  que  también  podría  ser  la  causa  del  defecto. 

Los  resultados  que  se  muestran  en  la  Fig.  9  indican  que,  como  es  el caso  de  las  ANN  [5],  un  tema  muy  importante  es  el  desarrollo  de métodos  de  análisis  automatizado  de  los  resultados  de  NBC.  Esto facilitaría  encontrar  los  efectos  sinérgicos  de  un  grupo  arbitrario  de señales  de  entrada,  lo  que  parece  ser  un  problema  clave. 

resultados  en  el  caso  de  señales  con  menor  importancia.  Para  una salida  de  tipo  binario,  la  NBC  identificó  una  señal  claramente  visible  y, por  lo  tanto,  su  resultado  fue  mejor  que  el  obtenido  de  las  ANN. 

Aparentemente,  la  principal  ventaja  de  la  NBC  en  comparación  con las  ANN  es  su  singularidad,  así  como  la  simplicidad  de  su  uso.  También se  puede  suponer  que  el  NBC  es  menos  exigente  en  lo  que  respecta  al tamaño  del  conjunto  de  entrenamiento  (por  ejemplo,  el  entrenamiento no  requiere  el  uso  de  un  conjunto  de  verificación). 

Parece  que  la  NBC  puede  hacer  un  sistema  de  aprendizaje  útil  en aplicaciones  industriales  y  que,  en  algunos  casos,  puede  ser  mejor  que las  ANN.  Sin  embargo,  es  necesario  seguir  investigando,  especialmente para  ampliar  las  posibilidades  de  interpretación  de  los  resultados  de ambos  sistemas. 

# Referencias 

# 6.  Resumen  y  conclusiones 

- [1]  T.  Bayes,  Philos.  Trans.  Roy.  Soc.  Londres  53  (1763)  370–418. 

El  análisis  comparativo  discutido  en  el  presente  trabajo  lleva  a  la conclusión  de  que  los  errores  de  predicción  de  una  NBC  pueden  ser menores  o  mayores  que  los  errores  de  una  ANN.  Para  dos  conjuntos de  datos  simulados  idénticos  con  salida  binaria,  que  diferían  solo  con respecto  al  tamaño,  la  NBC  produjo  un  error  menor  (porcentaje  de categorías  falsas)  que  una  ANN. 

El  factor  de  importancia  relativa  de  las  cantidades  de  entrada  para  el 

NBC  en  su  forma  actual  conduce  a  un  bajo  grado  de  precisión  de 

- [2]  T.  Masters,  Recetas  prácticas  de  redes  neuronales  en  C++,  Academic Prensa,  1993. 

- [3]  TM  Mitchell,  Aprendizaje  automático,  McGraw­Hill,  1997.´ 

- [4]  M.  Perzyk,  A.  Kochanski,  J.  Mater.  Proceso.  Tecnología  109  (2001) 305–307. 

- [5]  M.  Perzyk,  A.  Kochanski,  J.  Eng.  Fabricación  217  (2003)  1279–1284.´ [6]  M.  Perzyk,  A.  Kochanski,  J.  Kozłowski,  Informatyka  w  Technologii  Materiałow  3  ´ (2003)  125–132. 

- [7]  MA  Yescas,  HKDH  Bhadeshia,  DJ  MacKay,  Mater.  ciencia  Ing.  A 311  (2001)  162–173. 

