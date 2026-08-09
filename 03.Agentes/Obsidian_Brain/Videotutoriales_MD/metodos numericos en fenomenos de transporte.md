---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\Rotura_Presa_HEC_RAS_e_IBER_y_Model_Flujo_No_Permantente_\06. Rotura Presa HEC-RAS e IBER y Model. Flujo No Permantente\DATA\Flujo No Permanente\02 Bibliografia\metodos numericos en fenomenos de transporte.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]

### **M´etodos Num´ericos en Fen´omenos de Transporte.** 

**Norberto Nigro** `<nnigro@intec.unl.edu.ar>` **Mario Storti** `<mstorti@intec.unl.edu.ar>` 

_www:_ _`http://www.cimec.org.ar/cfd` Centro Internacional de M´etodos Computacionales en Ingenier´ıa_ _`http://www.cimec.org.ar`_ 

```
(Documentversion:curso-0.3.0)
(Date:2005/05/2300:03:21UTC)
```

# **´Indice general** 

|**1.**<br>**Mo**|**delos i**|**fis´ıcos y matem´aticos**|**9**|
|---|---|---|---|
|1.1.|Conce|ptos introductorios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>9|
||1.1.1.|Postulado del continuo<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>9|
||1.1.2.|Tipos de flujo<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>10|
||1.1.3.|La soluci´on a los problemas de mec´anica de fluidos<br>. . . . . . . . . . .|. . . .<br>11|
||1.1.4.|Unidades . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>12|
||1.1.5.|Propiedades de los fluidos. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>13|
|1.2.|Cinem|´atica de fluidos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>15|
||1.2.1.|El vol´umen material . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>15|
||1.2.2.|El principio de conservaci´on de la cantidad de movimiento lineal<br>. . . .|. . . .<br>15|
|1.3.|TP.I.-|Trabajo Pr´actico #1<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>37|
|**2.**<br>**Ni**|**veles d**|**in´amicos de aproximaci´on**|**40**|
||2.0.1.|Introducci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>40|
|2.1.|Las e|cuaciones de Navier-Stokes . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>41|
||2.1.1.|Modelo de fluido incompresible. . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>42|
||2.1.2.|Las ecuaciones de Navier-Stokes promediadas<br>. . . . . . . . . . . . . .|. . . .<br>43|
||2.1.3.|Aproximaci´on ”Thin shear layer” (TSL)<br>. . . . . . . . . . . . . . . . .|. . . .<br>44|
||2.1.4.|Aproximaci´on Navier-Stokes parabolizada. . . . . . . . . . . . . . . . .|. . . .<br>45|
||2.1.5.|Aproximaci´on de capa l´ımite . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>46|
|2.2.|Mode|lo de flujo inv´ıscido . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>46|
||2.2.1.|Propiedades de las soluciones discontinuas<br>. . . . . . . . . . . . . . . .|. . . .<br>47|
|2.3.|Flujo|potencial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>49|
||2.3.1.|Aproximaci´on de peque˜nas pertubaciones<br>. . . . . . . . . . . . . . . .|. . . .<br>51|
||2.3.2.|Flujo potencial linealizado<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>51|
|**3. Nat**|**uralez**|**a matem´atica de las ecuaciones**|**52**|
|3.1.|Introd|ucci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>52|
|3.2.|Superi|ficies caracter´ısticas. Soluciones del tipo ondas . . . . . . . . . . . . . . .|. . . .<br>55|
|3.3.|Ecuac|iones diferenciales parciales de segundo ´orden<br>. . . . . . . . . . . . . . .|. . . .<br>55|
|3.4.|Defini|ici´on general de superficie caracter´ıstica . . . . . . . . . . . . . . . . . . .|. . . .<br>58|
|3.5.|Domi|nio de dependencia - zona de influencia . . . . . . . . . . . . . . . . . . .|. . . .<br>60|
|3.6.|Condi|ciones de contorno e iniciales. . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>61|



1 

´INDICE GENERAL _´INDICE GENERAL_ 

||3.6.1.|Introducci´on<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>62|
|---|---|---|---|
||3.6.2.|MatLab como software de aplicaci´on . . . . . . . . . . . . . . . . . . . . . . .|.<br>63|
|**4. M´e**|**todo d**|**e diferencias finitas**|**73**|
|4.1.|Difere|ncias finitas en 1D . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>73|
||4.1.1.|Desarrollo en Serie de Taylor . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>73|
||4.1.2.|Aproximaciones de mayor orden<br>. . . . . . . . . . . . . . . . . . . . . . . . .|.<br>75|
||4.1.3.|Aproximaci´on de derivadas de orden superior . . . . . . . . . . . . . . . . . .|.<br>75|
||4.1.4.|N´umero de puntos requeridos . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>76|
||4.1.5.|Soluci´on de la ecuaci´on diferencial por el m´etodo de diferencias finitas . . . .|.<br>76|
||4.1.6.|Ejemplo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>78|
||4.1.7.|An´alisis de error. Teorema de Lax<br>. . . . . . . . . . . . . . . . . . . . . . . .|.<br>79|
||4.1.8.|Condiciones de contorno tipo Neumann (“flujo impuesto”). . . . . . . . . . .|.<br>80|
|4.2.|Proble|l<br>mas no-lineales<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>84|
||4.2.1.|Ejemplo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>87|
||4.2.2.|M´etodo secante . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>88|
||4.2.3.|M´etodo tangente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>89|
|4.3.|Precisi|´on y n´umero de puntos en el esquema de diferencias finitas . . . . . . . . . . .|.<br>90|
|4.4.|M´etod|o de diferencias finitas en m´as de una dimensi´on . . . . . . . . . . . . . . . . .|.<br>92|
|4.5.|Aprox|imaci´on en diferencias finitas para derivadas parciales . . . . . . . . . . . . . .|.<br>93|
||4.5.1.|i<br>Stencil del operador discreto<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>95|
|4.6.|Resolu|ci´on del sistema de ecuaciones . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>96|
||4.6.1.|Estructura banda . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>96|
||4.6.2.|Requerimientos de memoria y tiempo de procesamiento para matrices banda|.<br>97|
||4.6.3.|Ancho de banda y numeraci´on de nodos . . . . . . . . . . . . . . . . . . . . .|.<br>99|
|4.7.|Domin|ios de forma irregular . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>100|
||4.7.1.|Inmersi´on del dominio irregular en una malla homog´enea<br>. . . . . . . . . . .|.<br>101|
||4.7.2.|Mapeo del dominio de integraci´on<br>. . . . . . . . . . . . . . . . . . . . . . . .|.<br>104|
||4.7.3.|Coordenadas curvil´ıneas ortogonales . . . . . . . . . . . . . . . . . . . . . . .|.<br>105|
||4.7.4.|Ejemplo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>105|
||4.7.5.|Mallas generadas por transformaci´on conforme . . . . . . . . . . . . . . . . .|.<br>106|
|4.8.|La ecu|aci´on de convecci´on-reacci´on-difusi´on . . . . . . . . . . . . . . . . . . . . . . .|.<br>112|
||4.8.1.|Interpretaci´on de los diferentes t´erminos . . . . . . . . . . . . . . . . . . . . .|.<br>113|
||4.8.2.|Discretizaci´on de la ecuaci´on de advecci´on-difusi´on . . . . . . . . . . . . . . .|.<br>118|
||4.8.3.|Desacoplamiento de las ecuaciones . . . . . . . . . . . . . . . . . . . . . . . .|.<br>119|
||4.8.4.|Esquemas de diferencias contracorriente (upwinded) . . . . . . . . . . . . . .|.<br>119|
||4.8.5.|El caso 2D<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>121|
||4.8.6.|Resoluci´on de las ecuaciones temporales . . . . . . . . . . . . . . . . . . . . .|.<br>123|
|4.9.|Condu|cci´on del calor con generaci´on en un cuadrado . . . . . . . . . . . . . . . . . .|.<br>124|
|**5. T´ec**|**nicas d**|**e discretizaci´on**|**126**|
|5.1.|M´eto|do de los residuos ponderados<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>126|
||5.1.1.|Introducci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>126|
||5.1.2.|Aproximaci´on por residuos ponderados . . . . . . . . . . . . . . . . . . . . .|.<br>129|



[Document version: curso-0.3.0. File version: $Id: curso.tex,v 1.36 2005/05/23 18:38:32 mstorti Exp $] 

**2** 

´INDICE GENERAL _´INDICE GENERAL_ 

||5.1.3.|Residuos ponderados para la resoluci´on de ecuaciones diferenciales . . . . . . .|131|
|---|---|---|---|
||5.1.4.|Condiciones de contorno naturales . . . . . . . . . . . . . . . . . . . . . . . . .|138|
||5.1.5.|M´etodos de soluci´on del contorno<br>. . . . . . . . . . . . . . . . . . . . . . . . .|139|
||5.1.6.|Sistema de ecuaciones diferenciales<br>. . . . . . . . . . . . . . . . . . . . . . . .|140|
||5.1.7.|Problemas no lineales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>|141|
||5.1.8.|Conclusiones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|145|
||5.1.9.|TP.chapV– Trabajo Pr´actico #2 . . . . . . . . . . . . . . . . . . . . . . . . . .|146|
|**6.**<br>**M´e**|**todo d**|**e los elementos finitos**|**150**|
|6.1.|Introd|ucci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|150|
|6.2.|Funci|ones de forma locales de soporte compacto . . . . . . . . . . . . . . . . . . . . .|152|
|6.3.|Aprox|imaci´on a soluciones de ecuaciones diferenciales. Requisitos sobre la continuidad||
||de las|funciones de forma<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|155|
|6.4.|Form|ulaci´on d´ebil y el m´etodo de Galerkin . . . . . . . . . . . . . . . . . . . . . . . .|156|
|6.5.|Aspec|tos computacionales del m´etodo de los elementos finitos<br>. . . . . . . . . . . . .|156|
||6.5.1.|Ejemplo 1<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|157|
||6.5.2.|Ejemplo 2<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|162|
||6.5.3.|Ejemplo 3<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|162|
|6.6.|Interp|olaci´on de mayor orden en 1D . . . . . . . . . . . . . . . . . . . . . . . . . . . .|163|
||6.6.1.|Grado de las funciones de prueba y velocidad de convergencia<br>. . . . . . . . .|164|
||6.6.2.|Funciones de forma de alto orden standard de la clase _C_<sup>0</sup><br>. . . . . . . . . . .|165|
|6.7.|Probl|emas con advecci´on dominante - M´etodo de Petrov-Galerkin . . . . . . . . . . .|166|
|6.8.|El cas|o multidimensional . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|169|
||6.8.1.|Introducci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|169|
||6.8.2.|Elemento triangular . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|170|
||6.8.3.|Elemento cuadrangular . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|172|
||6.8.4.|Transformaci´on de coordenadas<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|174|
||6.8.5.|Integraci´on num´erica<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|176|
|6.9.|Probl|emas dependientes del tiempo<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|177|
||6.9.1.|Discretizaci´on parcial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|177|
||6.9.2.|Discretizaci´on espacio-temporal por elementos finitos<br>. . . . . . . . . . . . . .|179|
|6.10.|El m´e|todo de los elementos finitos aplicado a las leyes de conservaci´on . . . . . . . . .|182|
|6.11.|TP.VI|- Trabajo Pr´actico . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|185|
|**7.**<br>**M´e**|**todo d**|**e los vol´umenes finitos**|**188**|
|7.1.|Introd|ucci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|188|
|7.2.|Form|ulaci´on del m´etodo de los vol´umenes finitos<br>. . . . . . . . . . . . . . . . . . . .|191|
||7.2.1.|Mallas y vol´umenes de control . . . . . . . . . . . . . . . . . . . . . . . . . . .|192|
|7.3.|El m´e|todo de los vol´umenes finitos en 2D . . . . . . . . . . . . . . . . . . . . . . . . .|193|
||7.3.1.|Evaluaci´on de los flujos convectivos . . . . . . . . . . . . . . . . . . . . . . . .|193|
||7.3.2.|F´ormulas generales de integraci´on . . . . . . . . . . . . . . . . . . . . . . . . .|197|
|7.4.|El m´e|todo de los vol´umenes finitos en 3D . . . . . . . . . . . . . . . . . . . . . . . . .|199|
||7.4.1.|Evaluaci´on del area de las caras de la celda . . . . . . . . . . . . . . . . . . . .|199|
||7.4.2.|Evaluaci´on del vol´umen de la celda de control<br>. . . . . . . . . . . . . . . . . .|200|



[Document version: curso-0.3.0. File version: $Id: curso.tex,v 1.36 2005/05/23 18:38:32 mstorti Exp $] 

**3** 

´INDICE GENERAL _´INDICE GENERAL_ 

|7.5.|TP.VI|I.- Trabajo Pr´actico . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>203|
|---|---|---|---|
|**8.**<br>**An**|**´alisis d**|**e esquemas num´ericos**|**206**|
|8.1.|Intro|ducci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>206|
|8.2.|Defini|iciones b´asicas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>206|
|8.3.|Consi|stencia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>209|
|8.4.|Estab|ilidad . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>211|
|8.5.|El m´e|todo de Von Neumann . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>212|
||8.5.1.|Factor de amplificaci´on . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>214|
||8.5.2.|Extensi´on al caso de sistema de ecuaciones . . . . . . . . . . . . . . .|. . . . .<br>215|
||8.5.3.|An´alisis espectral del error num´erico<br>. . . . . . . . . . . . . . . . . .|. . . . .<br>219|
||8.5.4.|Extensi´on a esquemas de tres niveles<br>. . . . . . . . . . . . . . . . . .|. . . . .<br>223|
||8.5.5.|El concepto de velocidad de grupo . . . . . . . . . . . . . . . . . . . .|. . . . .<br>223|
||8.5.6.|An´alisis de Von Neumann multidimensional<br>. . . . . . . . . . . . . .|. . . . .<br>224|
|8.6.|Conv|ergencia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>224|
|8.7.|TP. Tr|abajo Pr´actico . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>226|
|**9. M´e**|**todos i**|**terativos para la resoluci´on de ecuaciones lineales**|**229**|
|9.1.|Conce|ptos b´asicos de m´etodos iterativos estacionarios<br>. . . . . . . . . . . . .|. . . . .<br>229|
||9.1.1.|Notaci´on y repaso<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>229|
||9.1.2.|El lema de Banach . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>234|
||9.1.3.|Radio espectral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>237|
||9.1.4.|Saturaci´on del error debido a los errores de redondeo.<br>. . . . . . . . .|. . . . .<br>239|
||9.1.5.|M´etodos iterativos estacionarios cl´asicos . . . . . . . . . . . . . . . . .|. . . . .<br>240|
|9.2.|M´etod|o de Gradientes Conjugados . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>245|
||9.2.1.|M´etodos de Krylov y propiedad de minimizaci´on . . . . . . . . . . . .|. . . . .<br>245|
||9.2.2.|Consecuencias de la propiedad de minimizaci´on. . . . . . . . . . . . .|. . . . .<br>247|
||9.2.3.|Criterio de detenci´on del proceso iterativo.<br>. . . . . . . . . . . . . . .|. . . . .<br>251|
||9.2.4.|Implementaci´on de gradientes conjugados . . . . . . . . . . . . . . . .|. . . . .<br>255|
||9.2.5.|Los “verdaderos residuos”.. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>260|
||9.2.6.|M´etodos CGNR y CGNE . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>266|
|9.3.|El m´et|odo GMRES . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>266|
||9.3.1.|La propiedad de minimizaci´on para GMRES y consecuencias . . . . .|. . . . .<br>266|
||9.3.2.|Criterio de detenci´on:<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>270|
||9.3.3.|Precondicionamiento . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>271|
||9.3.4.|Implementaci´on b´asica de GMRES . . . . . . . . . . . . . . . . . . . .|. . . . .<br>272|
||9.3.5.|Implementaci´on en una base ortogonal . . . . . . . . . . . . . . . . . .|. . . . .<br>273|
||9.3.6.|El algoritmo de Gram-Schmidt modificado. . . . . . . . . . . . . . . .|. . . . .<br>275|
||9.3.7.|i<br>Implementaci´on eficiente . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>275|
||9.3.8.|i<br>Estrategias de reortogonalizaci´on . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>276|
||9.3.9.|Restart<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>276|
||9.3.10.|Otros m´etodos para matrices no-sim´etricas<br>. . . . . . . . . . . . . . .|. . . . .<br>276|
||9.3.11.|Gu´ıa Nro 3. GMRES . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>279|
|9.4.|Desco|mposici´on de dominios.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . .<br>281|



[Document version: curso-0.3.0. File version: $Id: curso.tex,v 1.36 2005/05/23 18:38:32 mstorti Exp $] 

**4** 

´INDICE GENERAL _´INDICE GENERAL_ 

|9.4.1.<br>Condicionamiento del problema de interfase. An´alisis de Fourier. . . . .|. . . .<br>282|
|---|---|
|**10.Flujo incompresible**|**287**|
|10.1. Definici´on de flujo incompresible<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>287|
|10.2. Ecuaciones de Navier-Stokes incompresible. . . . . . . . . . . . . . . . . . . . .|. . . .<br>288|
|10.3. Formulaci´on vorticidad-funci´on de corriente . . . . . . . . . . . . . . . . . . . .|. . . .<br>288|
|10.4. Discretizaci´on en variables primitivas . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>290|
|10.5. Uso de mallas staggered . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>292|
|10.6. Discretizaci´on por elementos finitos . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>293|
|10.7. El test de la parcela<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>295|
|10.8. La condici´on de Brezzi-Babuska . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>297|
|10.9. M´etodos FEM estabilizados . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>298|



**5** 

[Document version: curso-0.3.0. File version: $Id: curso.tex,v 1.36 2005/05/23 18:38:32 mstorti Exp $] 

# **Introducci´on. Contenidos del curso** 

Este curso b´asico sobre _CFD_ siguiendo los lineamientos del libro de C. Hirsch [Hirsch] se divide en 2 partes: 

1. Fundamentos y t´ecnicas generales aplicables a los fen´omenos de transporte en general y al flujo de calor y de fluidos en particular 

   - _a_ ) MODELOS FISICOS Y MATEMATICOS EN CFD 

   - _b_ ) APROXIMACIONES DINAMICAS 

   - _c_ ) NATURALEZA MATEMATICA DE LAS ECUACIONES 

   - _d_ ) TECNICAS DE DISCRETIZACION GLOBAL 

   - _e_ ) METODOS ESPECTRALES 

   - _f_ ) TECNICAS DE DISCRETIZACION LOCAL 

   - _g_ ) METODOS DE ELEMENTOS FINITOS 

   - _h_ ) TECNICAS DE DISCRETIZACION LOCAL 

   - _i_ ) METODOS DE VOLUMENES FINITOS 

   - _j_ ) ANALISIS NUMERICO DE ESQUEMAS DISCRETOS 

   - _k_ ) RESOLUCION DE ECUACIONES DISCRETIZADAS 

   - _l_ ) APLICACIONES 

2. T´ecnicas espec´ıficas aplicables a problemas de mec´anica de fluidos y transferencia de calor. 

   - _a_ ) FLUJO INVISCIDO COMPRESIBLE 

   - _b_ ) FLUJO VISCOSO COMPRESIBLE 

   - _c_ ) FLUJO VISCOSO INCOMPRESIBLE 

   - _d_ ) TOPICOS ESPECIALES 

La _primera parte_ del curso consiste en presentar los principios generales sobre los que se apoyan los modelos f´ısicos que interpretan muchas de las situaciones experimentales en mec´anica de fluidos y transferencia de calor. Mediante una visi´on del material propia de la mec´anica del continuo se obtiene posteriormente un modelo matem´atico que en general consiste de un conjunto de ecuaciones a derivadas parciales con o sin restricciones y con sus respectivos valores de contorno e iniciales que completan 

6 

´INDICE GENERAL _´INDICE GENERAL_ 

su definici´on. Dada la complejidad matem´atica de estos modelos, salvo en situaciones muy particulares en las cuales se pueden obtener soluciones anal´ıticas, requieren de su resoluci´on num´erica con lo cual se hace necesario presentar las diferentes t´ecnicas de discretizaci´on habitualmente empleadas en problemas de transporte de calor y momento. Debido al diferente car´acter de las ecuaciones diferenciales, tanto en su visi´on continua como en su contraparte discreta y a la presencia de ecuaciones adicionales en los contornos, tambien discretizadas, se requiere un minucioso an´alisis de los esquemas num´ericos empleados previo a su resoluci´on, con el fin de poder interpretar las t´ecnicas num´ericas desde el punto de vista de la precisi´on, la convergencia, la consistencia y la estabilidad. A continuaci´on se aborda el tema de la resoluci´on num´erica delsistema algebraico/diferencial de ecuaciones que surge de la discretizaci´on empleada. Este t´opico tiene alta incidencia en la factibilidad de resolver problemas num´ericos ya que de acuerdo al problema en mano y a los recursos computacionales disponibles muestra las diferentes alternativas para su resoluci´on. Esta primera parte finaliza con una serie de aplicaciones de los conceptos adquiridos a la resoluci´on de las ecuaciones de convecci´on difusi´on tanto en su version estacionaria como transiente, desde el simple caso unidimensional al multidimensional, considerando el caso lineal como el no lineal representado por la ecuaci´on de B¨urgers. Este modelo sencillo tiene especial inter´es dada la similitud que presenta con la estructura de las ecuaciones que conforman la mayoria de los modelos matem´aticos mas frecuentemente usados en mec´anica de fluidos y transferencia de calor. En esta primera parte del curso se introducir´an en forma de trabajos pr´acticos y cuando la explicaci´on te´orica lo requiera algunos ejemplos a resolver tanto anal´ıtica como num´ericamente. dado que esta parte es introductoria se ver´an modelos simplificados de aquellos com´unmente empleados en _CFD_ pero que contienen muchas de las caracter´ısticas matem´atico/num´ericas propias de aquellos y que lo hacen atractivos en pos de ir incorporando conceptos, necesarios para abordar la segunda parte, en forma gradual. Paralelamente con el curso te´orico se desarrollar´an talleres sobre los aspectos pr´acticos a cubrir en esta primera parte. Debido a que el enfoque del curso est´a orientado hacia los fundamentos y el aprendizaje de las t´ecnicas que est´an impl´ıcitas en todo c´odigo computacional se hace necesario programar por uno mismo algunas aplicaciones vistas en la secci´on te´orica. Ya que esto dif´ıcilmente se encuentra en un paquete comercial y dado que el grado de avance que actualmente existe en el area de software educativo est´a bastante lejos de poder contar con herramientas aptas para la ense˜nanza se hace necesario elegir alg´un entorno que sea ameno para el usuario y potente para el ambicioso plan de aprender m´etodos num´ericos desde cero. En este sentido consideramos que el uso de MatLab puede ser muy beneficioso por varias razones, a saber: 

1. cuenta con muchas rutinas de alto nivel y otras de bajo nivel que permite ubicarse muchas veces en diferentes niveles o jerarquias con lo cual cada uno puede optar por el rol que mas le gusta, 

2. es un lenguaje de programaci´on, por lo tanto crear rutinas muy espec´ıficas, 

3. gran y eficiente interacci´on entre c´alculo y gr´aficos, 

4. posibilidad de debugear aplicaciones en forma interactiva. 

No obstante, por razones de eficiencia y para cuando la necesidad lo requiera es necesario contar con conocimientos de lenguajes de programaci´on m´as orientados a simulaciones de gran escala, como por ejemplo el Fortran y el C o C++. Sin entrar en detalles acerca de la programaci´on el curso incluye el manejo de un programa de elementos finitos para la resoluci´on de algunos de los problemas incluidos 

**7** 

[Document version: curso-0.3.0. File version: $Id: tema0.tex,v 1.3 2003/04/21 17:14:13 mstorti Exp $] 

´INDICE GENERAL _´INDICE GENERAL_ 

en la primera parte del curso. Este software ser´a utilizado en la segunda parte del curso para resolver problemas de flujos compresibles e incompresibles que requieren mucha mayor potencia de c´alculo. 

La _segunda parte_ del curso trata acerca de las t´ecnicas espec´ıficas empleadas en la resoluci´on de problemas de mec´anica de fluidos. B´asicamente se tomar´a en primera instancia el caso de flujo inv´ıscido compresible representado por el modelo de las ecuaciones de Euler y posteriormente se tratar´a el caso viscoso tanto compresible como incompresible modelado por las ecuaciones de Navier-Stokes. En cada uno de estos cap´ıtulos se volcar´an los conceptos aprendidos en la primera parte del curso para dise˜nar y analizar esquemas num´ericos que permitan resolver estos casos particulares. Dada la complejidad del problema surgen naturalmente restricciones muy severas en cuanto a la resoluci´on num´erica de las ecuaciones lo cual hace necesario explorar t´ecnicas iterativas espec´ıficasa tal fin. Como las soluciones num´ericas en los problemas de flujos de fluidos son altamente dependiente de la malla se hace necesario introducir nociones b´asicas sobre generaci´on de mallas en _CFD_ . Este tema forma parte del grupo de t´opicos especiales. Otro de los temas especiales a tratar es el modelado de la turbulencia. Es bien sabido que la mayor´ıa de los problemas de inter´es son gobernados por condiciones de flujo turbulento. Se ver´a a modo de introducci´on algunos modelos algebraicos t´ıpicos en los casos de flujos internos y externos asi como algunos modelos basados en ecuaciones a derivadas parciales como el caso del bien popular m´etodo _κ − ϵ_ . Finalmente cierra esta secci´on de t´opicos especiales el tratamiento de problemas con dominios variables en el tiempo. 

**8** 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

## **Cap´ıtulo 1** 

# **Modelos fis´ıcos y matem´aticos** 

En este cap´ıtulo se presentan los principios o leyes f´ısicas que gobiernan el flujo de fluidos, las reglas que definen el comportamiento de los materiales involcucrados, los relaciones termodin´amicas entre las variables que caracterizan el fen´omeno y finalmente los modelos matem´aticos conformados por sistemas de ecuaciones diferenciales que ser´an el punto de partida hacia la b´usqueda de soluciones a diversos problemas de mec´anica de fluidos y transferencia de calor. 

#### **1.1. Conceptos introductorios** 

En esta secci´on mencionaremos algunos conceptos b´asicos necesarios para conformar el marco te´orico para el tratamiento de los problemas a resolver. 

##### **1.1.1. Postulado del continuo** 

Partiendo de una descripci´on molecular de la materia podemos poner atenci´on en el movimiento de ellas en forma individual o formar un _cluster_ que agrupe a muchas de ellas y estudiar el movimiento del mismo. La idea del cluster equivale a una especie de promediaci´on estad´ıstica que tiene sentido si las escalas de inter´es a ser resueltas son mucho mayores que el camino libre medio de las mol´eculas. Esta visi´on _fenomenol´ogica_ hace que el medio sea interpretado como un continuo a diferencia de la visi´on _microsc´opica_ que mira al material desde una aproximaci´on a las part´ıculas. Desde la ´optica del continuo las variables a resolver se asumen variar en forma continua respecto a las coordenadas espaciales y al tiempo. En la aproximaci´on del continuo la operaci´on de promediaci´on antecede a la aplicaci´on del principios termomec´anicos. En la aproximaci´on de part´ıcula se suelen plantear las leyes f´ısicas a la escala microsc´opica y estudiar los fen´omenos que ocurren a esa escala. Si realiz´aramos la promediaci´on despu´es de aplicar los principios termomec´anicos deber´ımos encontrar el mismo resultado que aquel que surge de la mec´anica del continuo. De todos modos esto ´ultimo no es muy pr´actico ya que a menudo la informaci´on microsc´opica que se dispone es muy escasa como para poder plantear un modelo a tan peque˜na escala para despu´es saltar mediante la promediaci´on a la macroescala, de real inter´es a los fines ingenieriles. 

9 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.1. Conceptos introductorios_ 

##### **1.1.2. Tipos de flujo** 

**Compresible e incompresible** Un fluido se considera incompresible si su densidad experimenta cambios despreciables frente a cambios apreciables en la temperatura y la presi´on. Despreciable es un t´ermino ambiguo y debe ser interpretado de acuerdo a la experiencia. Por ejemplo si un fluido var´ıa su densidad un 5 % para un salto t´ermico de ∆ _T ≈_ 100<sup>_◦_</sup> _C_ o en un 1 % para un salto de presi´on de ∆ _p ≈_ 100 _atm_ uno se inclinar´ıa pensar que el fluido es incompresible. En realidad lo que interesa es el flujo que se establece con total independencia del fluido que lo experimenta. No importa si es agua o aire lo importante es en que medida es la compresibilidad del medio un factor importante por considerar. Un ejemplo es la convecci´on natural en un medio como el agua. Este fen´omeno es manejado por diferencia de densidades muchas veces producidas por gradientes t´ermicos. Si bien la densidad del agua tiene un comportamiento tal que podr´ıa pensarse como incompresible, es su compresibilidad la que permite poner en movimiento al sistema formando corrientes convectivas que describen por si mismas el fen´omeno. No obstante este problema puede ser tratado como uno de flujo incompresible introduciendo efectos forzantes proporcionales al gradiente t´ermico mediante una aproximaci´on debida a _Boussinesq_ . En general el caso de flujo compresible es reservado para gases a alta velocidad, pr´oximas o superior a las del sonido en donde los fen´omenos ondulatorios son muy apreciables. No obstante el agua, un fluido qu a priori podr´ıa ser tildado como incompresible, al circular por una ca˜ner´ıa y al experimentar el cierre abrupto de una v´alvula desarrolla ondas de presi´on que pueden ser analizadas por t´ecnicas de flujos compresible. Resumiendo, la divisi´on entre compresible e incompresible debe ser analizada en t´ermino del flujo que produce y no del fluido que lo experimenta. 



<!-- Start of picture text -->
Convection<br>Stable Unstable<br>Laminar Turbulence<br>Infinitesimal Finite<br>amplitude<br>Instability Transition<br>Undisturbed<br>Developed<br>Disturbed Developing<br>Flujo laminar y turbulento<br><!-- End of picture text -->

**Laminar y turbulento** Mientras que el flujo laminar es caracterizado por un movimiento suave y determin´ıstico de una l´amina de fluido sobre otra, el turbulento es un movimiento aleatorio superpuesto sobre un movimiento medio del fluido. El humo de un cigarrillo es un experimento interesante que permite visualizar como el aire alrededor del mismo al calentarse se pone en movimiento de forma 

**10** 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.1. Conceptos introductorios_ 

laminar. En direcci´on ascendente pronto se ve como esa corriente ordenada empieza a inestabilizarse formando remolinos de gran escala que se returcen hasta que el des´orden se amplifica y los remolinos se afinan en tama˜no y crecen en cantidad retorci´endose m´as y mas alcanzando un r´egimen plenamente turbulento. Este fen´omeno es visible a nuestros ojos por un efecto similar al utilizado en la t´ecnica Schlieren en el que se hace atravezar rayos luminosos en un medio con densidad variable. De los muchos experimentos que se podr´ıan mencionar acerca de flujos turbulentos no podemos dejar de mencionar aquel que hizo historia y que se debi´o al propio Reynolds. El pudo observar como el flujo que atravezaba un tubo de secci´on circular a medida que iba cambiando la velocidad de entrada experimentaba cambios despreciables en su patr´on fluidodin´amico hasta que al atravezar cierto valor l´ımite se produc´ıa un cambio significativo en el r´egimen fluidodin´amico. Ese valor cr´ıtico puede ser establecido mediante t´ecnicas de an´alisis dimensional, que dan cuenta que cuando el n´umero de Reynolds supera un valor pr´oximo a los 2100 el flujo se transiciona y luego se transforma en turbulento. La transici´on se manifiesta porque se crea un movimiento vorticoso peri´odico que al crecer el Reynolds se desordena a´un mas alcanzando un r´egimen turbulento. La figura 1.1.2 muestra a modo de esquema los diferentes reg´ımenes que se presentan en un flujo desde uno laminar estable, pasando por inestabilidades hasta uno turbulento. El tema de la inestabilidad de flujos es toda un area de investigaci´on aparte que merece mucha atenci´on y que por razones de complejidad y espacio no ser´a tratada en este curso. Aquellos interesados en el tema pueden recurrir a libros como Batchelor [Ba], Dreizin & Reid [DR] y a los trabajos de Taylor entre otros. 

**Estacionario y transiente** En el caso laminar la diferencia entre un flujo estacionario y otro transiente es obvia, en el primero las variables de interes son independientes del tiempo mientras que en el ´ultimo _p_ = _p_ ( _t_ ) y **v** = **v** ( _t_ ). Si el flujo es turbulento, por ser este siempre transiente, la diferencia debe establecerse sobre los valores medios, o sea _<u>p̸</u>_ = _<u>p</u>_ <u>(</u> _t_ ) implica que el flujo es estacionario, siendo _<u>p</u>_ = _T_<sup><u>1</u></sup> �0 _T_<sup>_p_(</sup><sup>_t_)</sup><sup>_dt_elpromediotemporaldelapresi´onenunper´ıododeduraci´on</sup><sup>_T_.</sup> 

**Unidimensional y multidimensional** En el punto anterior tratamos la dependencia o no de las variables dependientes sobre una variable independiente en particular, el tiempo, estableciendo las diferencias entre un movimiento estacionario y otro transiente. Ahora tomaremos otra variable independiente, las coordenadas espaciales y supongamos que las variables dependientes, la presi´on y la velocidad por ejemplo, s´olo dependen de una de las coordenadas espaciales. En ese caso el movimiento es unidimensional siendo esta situaci´on muy ventajosa a la hora de un tratamiento anal´ıtico. Lamentablemente estas situaciones dif´ıcilmente se encuentren en la realidad, siendo al menos 2D la clase de problemas que merecen atenci´on. En estos casos como en el 3D los problemas deben ser generalmente abordados en forma num´erica. 

##### **1.1.3. La soluci´on a los problemas de mec´anica de fluidos** 

El formalismo necesario para resolver problemas de mec´anica de fluidos requiere de establecer los postulados fundamentales que gobiernan el movimiento de los mismos. Sin entrar en demasiado detalle en este tema podemos decir que la mayor´ıa de los estudiantes aprenden en los cursos universitarios las leyes de Newton del movimiento y la aplican para resolver problemas de est´atica y din´amica en forma casi natural. Parecer´ıa natural que ellas deban incluirse como leyes o postulados fundamentales para 

**11** 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.1. Conceptos introductorios_ 

tratar problemas de movimiento de fluidos. Sin embargo y desde el punto de vista de la mec´anica del continuo son m´as adecuadas las dos leyes de Euler que dicen: 

- 1.- la variaci´on temporal de la cantidad de movimiento de un cuerpo es igual a la fuerza resultante actuando sobre el mismo. 

- 2.- la variaci´on temporal del momento de la cantidad de movimiento de un cuerpo es igual al torque resultante actuando sobre el mismo, considerando que tanto el momento angular como el torque son medidos respecto del mismo punto. 

La primera ley de Euler es una generalizaci´on de la segunda ley de Newton mientras que la segunda ley de Euler es independiente de la primera ya que no solo incluye las fuerzas de vol´umen sino tambi´en las fuerzas de superficie. Estas dos leyes son conocidas como el _principio del momento lineal (1)_ y el _principio del momento angular (2)_ . Ambas, junto con los _principios de conservaci´on de la masa y la energ´ıa_ forman las leyes fundamentales necesarias para definir el modelo f´ısico utilizado en la mayor´ıa de los fen´omenos de transporte. Es m´as, los principios del momento lineal y angular pueden ser considerados como principios de conservaci´on considerando que la variaci´on temporal de la cantidad de movimiento lineal o angular son igualadas por la velocidad a la cual dicha cantidad de movimiento lineal o angular se suminstra al _cuerpo_ mediante una fuerza o un torque respectivamente. 

En lo anterior la palabra _cuerpo_ se utiliza como una cantidad fija de material, un cuerpo siempre contiene la misma masa y algunas veces es referido como sistema. Considerando los 4 principios de conservaci´on anteriores, cantidad de movimiento lineal y angular, masa y energ´ıa podemos ver que los dos primeros son principios sobre propiedades vectoriales mientras que los dos ´ultimos son establecidos sobre cantidades escalares. Establecer los principios fundamentales es solo el comienzo de un largo camino en pos de obtener soluciones a problemas de mec´anica de los fluidos. A continuaci´on se requiere un detallado an´alisis matem´atico para transformar lo establecido por los principios f´ısicos en ecuaciones matem´aticas ´utiles. A posteriori se necesita introducir reglas sobre el comportamiento del material tanto desde un punto de vista mec´anico como termodin´amico ambas basadas en las observaciones o quiz´as en algunos casos deducibles de principios o leyes f´ısicas aplicables a escalas mucho mas peque˜nas. Finalmente es la intuici´on la que restringe a´un m´as los modelos en pos de hacerlos tratables. 

##### **1.1.4. Unidades** 

En pos de normalizar el tratamiento tomaremos como unidades aquellas que surgen del sistema internacional de medidas y que se expresan en funci´on de las siguientes magnitudes b´asicas o primarias: 



con lo cual las cantidades cinem´aticas como posici´on, velocidad y aceleraci´on surgen de combinar distancias y tiempos en distintas potencias. La fuerza, como magnitud din´amica surge de aplicar el 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

**12** 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.1. Conceptos introductorios_ 

principio de conservaci´on de la cantidad de movimiento lineal , entonces 



##### **1.1.5. Propiedades de los fluidos** 

Para el caso de flujo incompresible a una fase solo se requiere conocer la densidad y la viscosidad si el fluido es newtoniano. En el caso que el fluido sea no newtoniano o si los efectos compresibles son importantes existen otras magnitudes a tener en cuenta. 

**Compresibilidad** Con dos coeficientes tendremos en cuenta el efecto de la presi´on y la temperatura sobre la densidad. El primero se define como: 



mientras que el coeficiente de expansi´on _β_ se define como: 



En el caso de los l´ıquidos estos dos coeficientes son en general peque˜nos, especialmente _κ_ . El coeficiente de expansi´on puede adquirir cierta importancia en el caso de fen´omenos como la convecci´on natural. En el caso de gases, un ejemplo es el caso de los gases ideales cuya ley de comportamiento viene com´unmente expresada por 



En el caso de los gases reales el comportamiento es diferente especialmente cerca de los puntos cr´ıticos y se debe recurrir a la experiencia para poder determinar las leyes de comportamiento. 

**Viscosidad** A diferencia de los materiales s´olidos que ante un esfuerzo sufren una deformaci´on en general independiente del tiempo, los fluidos no soportan determinados esfuerzos y se deforman continuamente. Esto muchas veces est´a asociado a la fluidez del medio. Un contraejemplo de los dicho en el caso de s´olidos es el fen´omeno de _creep_ o fluencia lenta. En el caso de los s´olidos la deformaci´on es la variable cinem´atica de inter´es, definida como la variaci´on relativa de la distancia entre dos puntos del cuerpo material. En los fluidos su an´alogo es la tasa o velocidad de deformaci´on, o sea la variaci´on relativa de la velocidad de dos puntos dentro del vol´umen material. Lo que suele ser de inter´es es establecer cierta relaci´on entre causa y efecto, o sea entre tensi´on y deformaci´on en mec´anica de s´olidos 

**13** 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.1. Conceptos introductorios_ 

o entre tensi´on y velocidad de deformaci´on en fluidos. Esta funcionalidad puede asumir un rango lineal y luego uno no lineal, dependiendo del material el punto de corte entre uno y otro comportamiento. En s´olidos es el m´odulo de Young el que vincula tensi´on con deformaci´on mientras que en mec´anica de fluidos es la viscosidad la que juega semejante rol. La _reolog´ıa_ es la ciencia que se encarga de establecer relaciones de este tipo v´alidas para ciertos materiales o fluidos. A su vez una vez establecido el ensayo de laboratorio aparecen los te´oricos tratando de traducir los valores experimentales en alguna teor´ıa que los explique. Entre estas teor´ıas una de las m´as citadas es la de considerar al fluido como Newtoniano, con eso queremos decir que la viscosidad es independiente del estado de deformaci´on del fluido. La viscosidad puede variar con la posici´on y el tiempo pero por otras causas, por ejemplo calentamiento, pero no var´ıa por su estado de deformaci´on. Con el viscos´ımetro se pueden determinar valores para la viscosidad. En el caso m´as general la viscosidad puede depender del estado de deformaci´on y en este caso el fluido exhibe un comportamiento no newtoniano. La figura 1.1.5 muestra 4 curvas tensi´on vs velocidad de deformaci´on que muestran el caso newtoniano (recta por el or´ıgen), el flujo de Bingham (recta desfasada del or´ıgen), y dos casos de fluido no newtoniano, el caso dilatante con viscosidad proporcional a la deformaci´on y el caso pseudo-pl´astico cuando la viscosidad disminuye cuanto m´as se deforma el fluido. 



<!-- Start of picture text -->
Comportamiento reol´ogico de los fluidos<br>Bingham model<br>Pseudo plastic Newtonian<br>Dilatant<br><!-- End of picture text -->

Existe un modelo muy usado llamado _modelo de la ley de potencia_ o modelo de Ostwald-de Wael el cual trata de unificar el tratamiento definiendo una viscosidad aparente del tipo 



con _µ_ 0 una viscosidad de referencia y _n_ una potencia. En este caso el escurrimiento se piensa del tipo flujo paralelo. 

**Tensi´on superficial** Esta aparece en general cuando existen interfaces entre dos o m´as fluidos o un fluido y un s´olido y a veces suelen ser tan importantes que su omisi´on en las ecuaciones pone en peligro el realismo de la soluci´on. Esta en general es funci´on de la curvatura de la interface y de alg´un coeficiente de capilaridad. Su complejidad escapa los alcances de estas notas. 

Presi´on de vapor 

En algunas aplicaciones la presi´on local suele descender demasiado alcanzando la presi´on de saturaci´on del vapor con lo cual aparece el fen´omeno de _cavitaci´on_ . Este fen´omeno es muy importante en 

**14** 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

el funcionamiento de m´aquinas hidr´aulicas como bombas y turbinas pero su tratamientoe escapa los alcances de estas notas. 

#### **1.2. Cinem´atica de fluidos** 

En esta secci´on se presentan algunas definiciones necesarias para describir el movimiento de los fluidos y se muestran algunas reglas muy ´utiles que permiten manipular matem´aticamente las ecuaciones de conservaci´on, pudiendo expresarlas de varias formas segun el tratamiento que se desee emplear. Empezaremos con la definici´on de los diferentes vol´umenes de control com´unmente empleados en la descripci´on de las ecuaciones de movimiento y expresaremos en forma matem´atica el principio de conservaci´on del momento lineal. Posteriormente trabajaremos sobre la cinem´atica del movimiento, el lado izquierdo de la ecuaci´on, usaremos el teorema de la divergencia para poder transformar integrales de vol´umen en integrales de area y viceversa, una ayuda para poder formular los problemas desde el punto de vista integral o diferencial, microsc´opico o macrosc´opico y finalmente se presenta el teorema del transporte para poder manipular vol´umenes de control variables con el tiempo. De esta forma se arriba a las ecuaciones de conservaci´on. 

##### **1.2.1. El vol´umen material** 

Por lo previamente establecido el principio de momento lineal involucra la definici´on de _cuerpo_ , diciendo que la variaci´on temporal de la cantidad de movimiento de un cuerpo es igual a la fuerza resultante actuando sobre el mismo. Como cuerpo queremos decir un sistema con una cantidad fija de material. Debido a que los principios de conservaci´on se aplican a los cuerpos y si consideramos el principio de conservaci´on de la masa entonces se deduce que la masa de un vol´umen material es constante. Al basar nuestro an´alisis en la mec´anica del continuo y al asumir que nuestra escala de inter´es es mucho mayor que la del propio movimiento molecular, entonces, tiene sentido considerar que el vol´umen material cambia de forma y posici´on con el tiempo de una manera continua sin intercambiar masa con el medio ambiente. Designaremos al vol´umen material y a su respectiva area material como _Vm_ y _Am_ . En breve surgir´a la necesidad de trabajar con vol´umenes de control fijos en el espacio y a estos como a su respectiva area los designaremos sencillamente por _V_ y _A_ . Finalmente presentamos una tercera posibilidad, aquella en la que el vol´umen de control se mueve pero ya no siguiendo al sistema o cuerpo sino de una manera arbitraria y a estos y su respectiva area la simbolizamos como _Va_ y _Aa_ . 

##### **1.2.2. El principio de conservaci´on de la cantidad de movimiento lineal** 

Consideremos un vol´umen diferencial de fluido _dV_ como el mostrado en la figura 1.2.2. La masa contenida en el mismo es _dM_ = _ρdV_ y la cantidad de movimiento del mismo es **v** _dM_ = _ρ_ **v** _dV_ . Por definici´on la cantidad de movimiento del vol´umen material se define como: 



**15** 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 



<!-- Start of picture text -->
w ̸  = u<br>volumen<br>arbitrario w = u<br>volumen<br>u<br>material<br>volumen<br>fijo<br>w = 0<br><!-- End of picture text -->

###### Distintas definiciones de vol´umenes de control 

con lo cual el principio de la conservaci´on de la cantidad de movimiento lineal puede escribirse como: 



La derivada _DtD_<sup>esllamadala</sup><sup>_derivadamaterial_yenbreveser´asometidaaan´alisisjuntoconlas</sup> otras dos derivadas temporales a considerar, la _derivada total_ y la _derivada parcial_ . Aqu´ı simplemente lo que queremos indicar es que estamos tomando la variaci´on temporal de una propiedad de un vol´umen material. Del lado izquierdo de la anterior ecuaci´on participa la cinem´atica del movimiento mientras que del derecho se hallan las causas del movimiento o fuerzas externas aplicadas al cuerpo. Estas pueden ser: 

- a.- fuerzas de cuerpo o vol´umen 

- b.- fuerzas de superficie. 

Mientras que las primeras act´uan sobre la masa del sistema (fuerzas gravitatorias, electrost´aticas, etc) las otras lo hacen sobre el contorno del sistema. Introduciendo estas dos fuerzas en la expresi´on anterior arribamos al principio de conservaci´on de la cantidad de movimiento lineal, expresado como: 



donde **g** es la fuerza de cuerpo por unidad de masa y **t** ( **n** ) es el vector tensi´on en el contorno. Casos simples 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

**16** 

- Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 



<!-- Start of picture text -->
#�$&%'()*,+.-(0/'1()2 345(<br>+63"7'8+698-;:/<:=)(>#@?<br>�

<br>

 "!<br>A@BDCECFCGHI<br>C0K6IE5L8F.CG JMON CPCG Q MSR<br>TVUXWZY<[]\@^6_`abcdafehgbije6_<br><!-- End of picture text -->

- Vol´umen material 

En la mayor´ıa de los cursos de mec´anica de los fluidos de la carrera de de Ingenier´ıa se hace especial ´enfasis entre otros temas a la resoluci´on de problemas asociados con la est´atica de fluidos y el flujo en tubos y canales. 

- La est´atica de fluidos 

El primer caso corresponde al caso particular de un flujo en reposo (estacionario) donde el t´ermino izquierdo de la expresi´on (1.6) se anula quedando una igualdad del tipo: 



Si adem´as se acepta la definici´on que dice: _un fluido se deformar´a continuamente bajo la aplicaci´on de un esfuerzo de corte_ entonces, las ´unicas fuerzas de superficie posibles deben actuar en forma normal a la misma. Adem´as se puede probar que el tensor de tensiones asociado a un fluido en reposo es isotr´opico y por lo tanto permanecer´a invariante con la direcci´on. Con todo esto las ecuaciones se simplifican demasiado y si asumimos cierta continuidad en los integrandos podemos cambiar a la forma diferencial del problema y arribar a la bien conocida expresi´on: 



donde hemos usado notaci´on de Gibbs en la primera l´ınea, notaci´on indicial en la segunda y la definici´on del operador gradiente en la tercera. Esta expresi´ıon es muy familiar para los estudiantes de ingenier´ıa ya que muchos problemas cl´asicos se resuelven con ella, a saber: 

1. a.-bar´ometros 

- [Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 



Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

2. b.-man´ometros 

3. c.-fuerzas sobre cuerpos planos sumergidos 

4. d.-fuerzas sobre cuerpos curvos sumergidos 

5. e.-fuerzas de flotaci´on 

6. f.-hidr´ometros, etc 

En la parte I de la pr´actica 1 se presentan algunos problemas opcionales a resolver para aquellos que quieran ejercitarse sobre temas que no son centrales al curso pero que son necesarios conocer para poder analizar problemas de mec´anica de fluidos. Opcionales significa que aquellos que se sientan confiados en que conocen la forma de resolverlos no est´an obligados a hacerlo. 

Flujo laminar unidimensional 

En este problema el fluido no esta en reposo pero si consideramos el caso de flujo laminar y l´ıneas de corriente rectas entonces nuevamente el miembro izquierdo de (1.6) se anula. Esto tiene su explicaci´on si tomamos un vol´umen material como el de la figura 1.2.2, 



- Flujo laminar unidimensional, definici´on del vol´umen material 

all´ı su cantidad de movimiento es constante ya que la densidad es constante por tratarse de un flujo incompresible y la velocidad en ese vol´umen de control es constante ya que la misma depende solamente del radio. Un ejemplo de flujo unidimensional que no tiene l´ıneas de corriente rectas y por ende no anula el miembro izquierdo es el de flujo Couette entre dos cil´ındricos conc´entrico de longitud infinita. La raz´on es que all´ı existe una aceleraci´on centr´ıpeta necesaria para mantener el flujo en un movimiento circular. Nuevamente tomamos la expresi´on (1.7) pero en este caso por estar el fluido en movimiento no podemos despreciar los esfuerzos cortantes. Por lo tanto las fuerzas de superficie actuar´an en la direcci´on normal (la presi´on) y en la direcci´on tangencial (la tensi´on de corte). Por la forma que tiene el vol´umen material y debido a que el movimiento tiene una sola componente de velocidad seg´un la direcci´on _z_ entonces las fuerzas normales a las superficies solo pueden actuar sobre aquellas superficies cuya normal est´a alineada con el eje _z_ . Como no existe flujo en la secci´on transversal del tubo los esfuerzos de corte en los mismos es nulo y solo puede haber esfuerzos de corte en los planos cuya normal coincide con la direcci´on radial como se muestra en la figura. Por lo tanto, si por el momento no consideramos las fuerzas de cuerpo la expresi´on (1.7) queda 



> [Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

 ! � "#$&% 

**18** 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

Haciendo un poco de ´algebra y tomando l´ımites cuando ∆ _r →_ 0 y ∆ _z →_ 0 conduce a la siguiente expresi´on diferencial: 



Esta ecuaci´on se la conoce con el nombre de ecuaci´on de tensi´on del movimiento porque viene expresada en t´erminos de las componentes del tensor de tensiones. Si queremos expresar esta ecuaci´on en t´ermino de las variables cinem´aticas debemos usar alguna relaci´on constitutiva. En este caso recurrimos a la ley de Newton de la viscosidad en la cual 



con lo cual si consideramos que la viscosidad es constante la (1.10) se transforma en 



Este flujo es denominado _flujo plano Couette_ y representa uno de los casos simples con soluci´on anal´ıtica y que ha tenido gran inter´es desde el punto de vista de las aplicaciones. Nosotros aqu´ı solo lo hemos planteado, dejamos la resoluci´on del mismo como parte de los trabajos pr´acticos. 

Cinem´atica de fluidos en los casos generales 

En la secci´on anterior nos volcamos hacia la resoluci´on de dos casos muy particulares que permiten independizarse completamente del miembro izquierdo de la expresi´on (1.6) del principio de conservaci´on de la cantidad de movimiento lineal . Ahora nos detendremos a analizar las variables que componen este miembro izquierdo de forma de adquirir las nociones elementales necesarias para su tratamiento. Este t´ermino expresa la cinem´atica del movimiento y como tal incluye la variaci´on temporal de propiedades que se hallan distribuidas en el espacio de alguna manera continua. Por lo tanto aparece la necesidad de tratar a las dos variables independientes m´as importantes que incluyen los principios de conservaci´on, las coordenadas espaciales y el tiempo. El objetivo est´a en conducir por una lados hacia la formulaci´on diferencial de los principios de conservaci´on con el prop´osito de analizarlos desde un punto de vista macrosc´opico local y por otro manipular la formulaci´on integral para poder llevar a cabo balance 

s macrosco´opico globales, muy ´utiles por varias razones. Estos balances macrosc´opico globales permiten chequear soluciones obtenidas num´ericamente mediante balances locales y por otro han sido de amplia difusi´on en la profesi´on del ingeniero para el c´alculo y dise˜no de equipos e instalaciones. 

Coordenadas espaciales y materiales 

En esta secci´on pretendemos desarrollar las nociones b´asicas sobre lo que se entiende por _coordenadas materiales_ y su relaci´on con las _coordenadas espaciales_ en pos de describir adecuadamente el movimiento de un fluido. El t´ermino coordenadas espaciales se refiere a un sistema de coordenadas fijo donde todos los puntos del espacio pueden ser localizados. Hay dos formas posibles de localizar o identificar una part´ıcula de fluido que pertenece a un vol´umen material diferencial _dVm_ ( _t_ ). Una forma ser´ıa designar su posici´on mediante sus coordenadas espaciales _x, y, z_ . Asumiendo que a un dado tiempo de referencia _t_ = 0 las coordenadas espaciales se hallan localizadas en 



[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

**19** 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

Para un tiempo _t >_ 0 la posici´on se puede expresar mediante 



Compactando las tres expresiones anteriores en una sola mediante 



entonces, **r** representa el vector posici´on espacial mientras que **R** es llamado el vector posici´on material. Este ´ultimo identifica una part´ıcula del sistema o cuerpo y en algun sentido la impone una marca al tiempo de referencia. Este conjunto espec´ıfico de coordenadas no representa ning´un sistema de coordenadas que se mueve y se deforma con el cuerpo. De alguna manera las coordenadas espaciales se pueden expresar en funci´on de las coordenadas materiales y el tiempo, 



Una descripci´on _Lagrangiana_ del movimiento es aquella expresada en t´ermino de las coordenadas materiales mientras que una descripci´on _Euleriana_ se expresa seg´un las coordenadas espaciales. 

La derivada temporal del vector posici´on espacial para una part´ıcula de fluido en particular es la velocidad de la misma. Ya que la derivada se eval´ua con las coordenadas materiales fijas esta derivada es llamada _derivada material_ , 



###### Derivadas temporales 

Sea _S_ = _S_ ( _x, y, z, t_ ) una funci´on escalar, entonces su derivada temporal se define como: 



Si _S_ fuera solo funci´on del tiempo esta definici´on es directa mientras que si _S_ depende de las coordenadas espaciales existe una ambiguedad respecto al punto que se toma en el instante _t_ y en _t_ + ∆ _t_ . Para comenzar consideremos el movimiento de una part´ıcula _p_ de un sistema o cuerpo, acorde a (1.18) tenemos que la componente _x_ de la velocidad de la misma ser´a: 



Imaginemos que la medici´on la llevamos a cabo con un observador montado sobre la part´ıcula, entonces para el observador las coordenadas materiales no cambian y por ende (1.18) se vuelve 



[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 



Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

Supongamos que queremos medir la temperatura de un flujo y como es habitual la medici´on la llevamos a cabo en una ubicaci´on fija del laboratorio, entonces lo que medimos como derivada temporal de la temperatura es: 



y a esta derivada se la suele llamar _derivada parcial_ efectuada fijando las coordenadas espaciales del punto de medici´on en lugar de las coordenadas materiales como en (1.20). 

Un tercer caso ser´ıa el de efectuar la medici´on montado sobre un dispositivo que se mueva de una forma arbitraria no manteniendo ni las coordenadas espaciales ni las materiales fijas. Esta derivada se la llama _derivada total_ asumiendo que la velocidad del sistema de medici´on es **w** _̸_ = **v** . 

La figura 1.2.2 muestra una descripci´on de lo que acabamos de presentar como las tres derivadas temporales a utilizar en el resto del curso. 



<!-- Start of picture text -->
RTS<br>RVU<br>JLK<br>JNM<br>89:!;<=9�>@?'9:!9�ABCD4E5FHGE5C7I<br>! "$#%"'& )(!*,+-".0/21435/76<br>O2P<br>OQ<br>�
�
��<br>z<br>y<br>x<br><!-- End of picture text -->



<!-- Start of picture text -->
Definici´on de las derivadas temporales<br><!-- End of picture text -->

Para interpretar lo anterior pero desde un punto de vista matem´atico asumamos que tenemos cierta funci´on escalar como la temperatura definida como: 



Si las coordenadas materiales se mantiene fijas, entonces podemos expresar las coordenadas espaciales en t´erminos de las materiales y el tiempo como 



- [Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 



Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

manteniendo **R** constante y diferenciando 



Por definici´on las derivadas de las coordenadas espaciales mantieniendo las coordenadas materiales **R** fijas son las componentes de la velocidad del fluido **v** , mientras que la derivada manteniendo las coordenadas espaciales **r** fijas es la derivada parcial, entonces (1.24) se transforma en: 



mientras que en notaci´on de Gibbs es 



y en notaci´on indicial: 



En el caso en que la medici´on la efectuemos sobre un dispositivo que tiene su propio movimiento entonces ya las coordenadas materiales no son fijas y las derivadas totales de las coordenadas espaciales respecto al tiempo representan las componentes de la velocidad del dispositivo **w** , 



en notaci´on de Gibbs: 



y en notaci´on indicial: 



Como vemos comparando (1.21) e (1.27) con (1.30) vemos que esta ´ultima es la m´as general ya que (1.21) corresponde al caso **w** = **0** mientras que como (1.27) ser´ıa cuando **w** = **v** . 

Hasta aqu´ı hemos analizado el caso de una funci´on escalar y en particular hemos mencionado por razones de ´ındole pr´actica el caso de la temperatura. A continuaci´on veremos que sucede cuando la funci´on a derivar es una cantidad vectorial. Tomemos como ejemplo el caso del vector velocidad cuya derivada temporal representa el vector aceleraci´on. Por definici´on, 



Haciendo el mismo an´alisis que con el caso escalar arribamos a que para un observador con coordenadas espaciales fijas este mide como aceleraci´on 



[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 



Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

siendo la relaci´on entre ambas 



en notaci´on indicial 



Aqu´ı vemos que la aceleraci´on consiste de dos t´erminos, uno es llamado la _aceleraci´on local_ y representa la variaci´on temporal de la velocidad en un punto fijo en el espacio. La segunda es llamada la _aceleraci´on convectiva_ y depende tanto de la magnitud de la velocidad como de su gradiente. De la expresi´on anterior surge que aunque el flujo sea estacionario la aceleraci´on puede no ser nula dependiendo de su componente convectiva. Un ejemplo de esto lo vemos en el caso del flujo entrando a un tubo desde un dep´osito. Hasta que se desarrolla el flujo experimenta una aceleraci´on debido al t´ermino convectivo aun cuando para un observador ubicado justo enfrente de dicha entrada las condiciones parecen no variar. Sin embargo otro observador viajando con el fluido experimentar´a la aceleraci´on convectiva. 

###### Teorema de la divergencia 

Esta herramienta matem´atica es muy ´util en la discusi´on que sigue a continuaci´on en este cap´ıtulo. Con ella podemos formular balances macrosc´opicos o desarrollar ecuaciones diferenciales a partir de los principios de conservaci´on expresados en forma integral como por ejemplo el (1.6) . 

Este teorema, conocido por aquellos alumnos que han tomado un curso de C´alculo de varias variables se puede expresar de la siguiente forma: 



Nuestro objetivo no es mostrar una demostraci´on del mismo, solamente presentarlo y tratar de aplicarlo en las secciones que siguen a esta. Para poder aplicarlo al caso de un campo escalar expresemos el campo vectorial anterior como **G** = _S_ **b** donde _S_ es un escalar y **b** es un vector constante. Entonces se puede demostrar que 



###### Teorema del transporte 

Hasta el momento hemos presentado diferentes formas de derivar temporalmente una funci´on tanto escalar como vectorial y a su vez hemos mencionado las dos formas de localizar un punto del cuerpo, mediante sus coordenadas espaciales o sus coordenadas materiales. 

El objetivo de esta secci´on es desarrollar una expresi´on general para la derivada temporal de una integral de vol´umen bajo condiciones tales que los puntos que pertenecen a la superficie del vol´umen se mueven con una velocidad arbitraria **w** . De acuerdo a lo ya presentado este vol´umen arbitrario lo hemos denominado como _Va_ ( _t_ ). Si la velocidad del mismo la fijamos igual a la velocidad de fluido **v** entonces el vol´umen se transforma en un vol´umen material _Vm_ ( _t_ ) y bajo estas condiciones nos referiremos al _teorema del transporte de Reynolds_ . 

**23** 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

Considerando el vol´umen arbitrario _Va_ ( _t_ ) como aquel ilustrado en la parte izquierda de la figura 1.1. Deseamos determinar la integral de vol´umen de una cantidad escalar _S_ , a saber: 



Para visualizar el teorema debemos pensar que el vol´umen bajo consideraci´on se mueve a trav´es del espacio de forma tal que los puntos de su superficie se mueven con velocidad **w** . Esta velocidad puede variar con el tiempo (aceleraci´on) y con las coordenadas espaciales (deformaci´on). En cada instante de tiempo la integral es evaluada y deseamos medir cual es la variaci´on de esta medici´on. Observando la figura vemos que en un instante ∆ _t_ el nuevo vol´umen barrido por la superficie m´ovil es designado _dVaII_ mientras que el viejo vol´umen dejado atr´as por su movimiento se designa por _dVaI_ . 



<!-- Start of picture text -->
n V a(t + ∆t)<br>Superficie al tiempo t<br>Va ( t ) dV = w  ·  n∆t dA<br>n<br>n<br>w dA(t + ∆t)<br>dAcs<br>dA(t)<br>dV = w  ·  n∆t dA<br><!-- End of picture text -->

Figura 1.1: Teorema del transporte 

El area de este vol´umen arbitario _Aa_ ( _t_ ) se puede dividir en dos partes: _AaI_ ( _t_ ) y _AaII_ ( _t_ ) mediante una curva cerrada sobre la superficie tal que **n** _·_ **w** = 0. Sin entrar en demasiados detalles para su demostraci´on, suponiendo que tal curva existe, entonces 



lo cual nos permite escribir la integral en (1.37) como 



[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 



Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

Cambiando el orden de integraci´on con el proceso l´ımite en el primer t´ermino obtenemos 



A continuaci´on analizamos de que forma cambiar las integrales de vol´umen por integrales de superficie. Para ello consideremos nuevamente la figura 1.1 que en su parte derecha analiza lo que ocurre localizadamente sobre un diferencial de superficie del vol´umen que se est´a moviendo. Este diferencial de vol´umen al moverse una distancia _L_ barre un cilindro oblicuo con respecto a la normal a la superficie siendo esta distancia 



con _w_ la magnitud del vector **w** que define la velocidad con que se mueve el vol´umen arbitrario, siendo su versor direcci´on representado en la figura mediante **_λ_** , entonces 



El vol´umen barrido es 



La relaci´on entre la orientaci´on del diferencial de area sobre la superficie con aquel generado por el barrido es: 







Entonces 



y aplicando este resultado a los dos vol´umenes que aparecen en la expresi´on (1.41) obtenemos lo siguiente: 



cuya sustituci´on en (1.41) produce 



[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 



Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

Tomando el l´ımite vemos que _AaI_ ( _t_ )+ _AaII_ ( _t_ ) = _Aa_ ( _t_ ) obteniendo finalmente el **Teorema general del transporte** : 



En el caso de un vol´umen fijo en el espacio tenemos que _Va_ ( _t_ ) = _V_ y **w** = 0 con lo que lo anterior se simplifa a 



El uso m´as frecuente del teorema general del transporte es cuando se lo aplica a un vol´umen material en cuyo caso este resultado se lo conoce como el _Teorema del transporte de Reynolds_ , cuya expresi´on viene dada como: 



La extensi´on de los resultados anteriores al caso de una funci´on vectorial es directa, simplemente podemos aplicarlo a cada componente, luego multiplicarlo por su respectivo versor direcci´on y luego sumar, con lo que (1.50) aplicado por ejemplo al campo de velocidades produce el siguiente resultado: 



Conservaci´on de la masa 

Hasta este punto hemos tratado de obtener las herramientas necesarias para manipular el miembro izquierdo del principio de conservaci´on de la cantidad de movimiento lineal con lo cual en pos de generalizar su uso deber´ıamos a esta altura completarlo con el manejo del miembro derecho, aquel representado por las fuerzas de vol´umen y las de superficie. Antes de ello y en pos de ir conduciendo al estudiante hacia la utilizaci´on m´as importante de todos los conceptos hasta aqu´ı presentados vamos a considerar el caso particular de la conservaci´on de la masa, ya que este no presenta miembro derecho. Definamos la propiedad a medir, la masa de un vol´umen material como: 



Ya que el principio de conservaci´on requiere que la misma se mantenga constante, entonces: 



Aplicando el teorema del transporte a la derivada material de la integral obtenemos: 



que surge de reemplazar _S_ = _ρ_ en (1.52) . 

De esta forma fue posible introducir el operador derivada dentro de la integral. Ahora a continuaci´on el teorema de la divergencia nos ayudar´a para transformar la integral de area en una de vol´umen 

**26** 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

con el fin de poder juntar todos los t´erminos bajo un mismo signo integral y de esta forma pasar de la formulaci´on integral a una diferencial. Esto produce finalmente: 



Asumiendo continuidad en los integrandos podemos deshacernos de la integral y obtener la tan ansiada forma diferencial del principio de conservaci´on de la masa 



Existen algunas otras formas de expresar el mismo principio de conservaci´on, como por ejemplo si aplicamos la definici´on de derivada material y alguna manipulaci´on algebraica b´asica llegamos a: 



Otra forma particular de la ecuaci´on de continuidad se obtiene si consideramos el caso de un flujo incompresible. Como la densidad es constante de (1.59) surge que 



Una forma particular del teorema del transporte de Reynolds se puede lograr si expresamos la propiedad escalar _S_ como producto de la densidad por su propiedad espec´ıfica, 



En ese caso aplicando todo lo visto hasta aqu´ı se puede arribar a la siguiente igualdad, llamada **forma especial del teorema del transporte de Reynolds** 



Una forma alternativa de obtener la ecuaci´on de continuidad mucho m´as pr´actica y con menos manipuleo matem´atico es posible mediante el concepto de balance de flujos. 

En general para un diferencial de vol´umen como el mostrado en la figura 1.2.2 podemos expresar el siguiente principio de conservaci´on de la masa de la siguiente forma: 



El t´ermino _flujo_ es muy frecuentemente usado en referencia al transporte de masa, momento y energ´ıa y significa una especie de caudal de alguna propiedad en la unidad de tiempo. Aplicando el caudal m´asico, por tratarse en este caso del balance de masa, a cada cara del cubo elemental y 

**27** 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 



<!-- Start of picture text -->
ρvz|z+∆z<br>ρvy|y+∆y<br>∆ z<br>ρv x|x ρvx|x<br>z<br>ρvy|y<br>ρvz|z<br>y<br>x<br><!-- End of picture text -->

Balance de masa 

asumiendo una variaci´on continua de las propiedades encontramos que: 

_∂ ∂t_<sup>(</sup><sup>_ρ_∆</sup><sup>_x_∆</sup><sup>_y_∆</sup><sup>_z_) =</sup> 



caudal m´asico a trav´es de la superficie orientada seg´un _z_ (1.64) 

Dividiendo por el vol´umen del cubo y tomando l´ımites cuando las dimensiones tienden a cero arribamos a una expresi´on id´entica a (1.58) . Como vemos en lo anterior solo hemos usado un concepto de balance de flujos a trav´es de la superficie con t´erminos de incremento de la propiedad en el vol´umen considerando a ´este fijo en el espacio por lo que aparece la derivada temporal parcial. 

Lineas de corriente, lineas de camino, trazas y funci´on de corriente 

Este importante tema perteneciente a la cinem´atica de fluidos por razones de espacio y por no estar dentro de los objetivos del curso ser´a dejado al lector para su estudio. En general la mayor´ıa de los libros introductorios de mec´anica de fluidos lo tratan en forma extensiva. Sugerimos a aquellos interesados en el tema los libros de Whitaker [Wi], Batchelor [Ba] y White [Wh] entre otros. Por razones de completitud de las presentes notas en un futuro est´a previsto incluirlo al tema en esta secci´on. 

Fuerzas de superficie en un fluido 

Volvamos por un momento a la expresi´on del principio de conservaci´on de la cantidad de movi- 

**28** 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

miento lineal , ecuaci´on (1.6), 



En la secci´on anterior hemos tratado la cinem´atica de los fluidos en el caso general, o sea el miembro izquierdo de la ecuaci´on (1.6) y hemos hecho una menci´on aparte dentro de esta al caso especial de la est´atica de los fluidos. Nosotros ahora volcamos nuestra atenci´on al miembro derecho, o sea a las causas del movimiento y en especial al t´ermino de las fuerzas de superficie ya que las fuerzas de cuerpo o de masa en general no presentan mayor dificultad. 

Vector tensi´on y tensor de tensiones 

A continuaci´on trataremos al vector tensi´on a pesar de que ya lo hemos presentado cuando tratamos el caso particular de la est´atica de los fluidos o el caso simple de flujo desarrollado en un tubo (movimiento unidimensional). Como antes consideramos la hip´otesis del continuo, o sea asumimos que el vector tensi´on var´ıa en forma continua con las variables independientes del problema, al igual que las otras variables incluidas en el problema. No obstante en el caso del vector tensi´on tambi´en debemos agregar que var´ıa en forma suave o continua con la orientaci´on en la cual est´a calculado, **n** . Sin entrar en detalles acerca de la prueba de esto [Wi] establecemos las siguientes hip´otesis: 

1. 1.- el vector tensi´on actuando sobre lados opuestos de la misma superficie en un dado punto es igual en magnitud y opuesto en direcci´on, **t** ( **n** ) = _−_ **t** ( **n** ). 

2. 2.- el vector tensi´on puede escribirse en t´erminos del tensor de tensiones del cual proviene como **t** ( **n** ) = **n** _·_ **T** . 

3. 3.- el tensor de tensiones es sim´etrico, o sea _Tij_ = _Tji_ 

El primer punto se demuestra planteando el principio de conservaci´on de la cantidad de movimiento lineal , el teorema del valor medio y un procedimiento de ir al l´ımite cuando la longitud caracter´ıstica tiende a cero. El segundo punto requiere plantear el equilibrio de un vol´umen tetra´edrico sobre el cual el vector tensi´on actuando sobre un plano puede descomponerse o formarse seg´un aquellos pertenecientes a los otros tres planos orientados seg´un los ejes cartesianos. Los tres vectores tensi´on actuando sobre los tres planos cartesianos son: 



**29** 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

siendo el vector tensi´on expresado seg´un estos tres vectores tensi´on: 



con lo cual se alcanza el resultado esperado 



donde el tensor de tensiones est´a compuesto de t´erminos **it** ( **i** ) que no representan ni un producto escalar ni uno vectorial, este producto es a menudo llamado _producto di´adico_ , base del algebra tensorial. Entonces surge que el vector tensi´on (tensor de primer orden) es la contracci´on del tensor de tensiones (tensor de segundo orden) en la direcci´on normal. Este resultado no es tan obvio para aquellos no familiarizados con el algebra tensorial y se recomienda volcar la atenci´on a este tema para aquellos que pretender lograr un mejor entendimientos de las ecuaciones de movimiento que m´as adelante se definen. En res´umen, el tensor de tensiones en tres dimensiones expresado por simplicidad seg´un las coordenadas cartesianas es: 

Las nueve componentes escalares en (1.65) representan o caracterizan al tensor de tensiones, que en notaci´on matricial puede escribirse como: 



El primer ´ındice representa la orientaci´on del plano sobre el cual la tensi´on act´ua mientras que el segundo ´ındice est´a relacionada con la direcci´on en la cual la tensi´on est´a actuando. 

En notaci´on indicial (1.67) puede escribirse como: 



La forma de arribar al tercer punto, la simetr´ıa del tensor, es mediante el principio de conservaci´on del momento de la cantidad de movimiento lineal aplicado a un vol´umen diferencial. Esta simetr´ıa a su vez conduce al siguiente resultado: 



Ecuaciones de movimiento expresada seg´un el tensor de tensiones 

El objetivo es plantear las ecuaciones de movimiento en t´ermino del tensor de tensiones siendo esta forma una herramienta muy ´util para plantear un anal´ısis macrosc´opico global de la mec´anica de los fluidos o incluso como paso previo a la formulaci´on diferencial del problema permitiendo cerrar el an´alisis mediante la introducci´on de las ecuaciones constitutivas del material, siendo esta forma bastante general. Comenzamos planteando el principio de conservaci´on de la cantidad de movimiento lineal , 



[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 



Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

La idea es encontrar la formulaci´on diferencial al problema tal como hicimos previamente al tratar la conservaci´on de la masa. All´ı usamos el teorema de la divergencia sobre un integrando formado por el producto escalar del vector velocidad con la normal. Aqu´ı la dificultad est´a en que el integrando tiene al vector tensi´on y a´un no presentamos como aplicar el teorema de la divergencia a un integrando vectorial que no puede ser considerado constante. Para salvar esta dificultad Whitaker multiplica la anterior ecuaci´on escalarmente por un vector constante **b** y por ser constante puede ser introducida sin dificultad dentro del s´ımbolo diferencial: 



y mediante el teorema del transporte de Reynolds y algunas manipulaciones algrebraica simples llegamos a: 



como ( **T** _·_ **b** ) es un vector se puede aplicar el teorema de la divergencia tal como lo vimos anteriormente y obtener 



Otra vez, al ser los l´ımites de integraci´on arbitrarios podemos removerlos y el integrando se satisface en todo punto del dominio. La eliminaci´on del vector constante **b** es trivial en los dos primeros t´erminos. En cuanto al tercero una forma de resolverlo es recurrir o a la notaci´on indicial o sino a la definici´on matricial del tensor (1.68) 



de esta forma surge que la integral de superficie del vector tensi´on se transforma en la integral de vol´umen de la divergencia del tensor de tensiones, una generalizaci´on del teorema de la divergencia. Por lo tanto la ecuaci´on de movimiento (1.6) se transforma en: 



Entonces partiendo de la formulaci´on integral o macrosc´opica global arribamos a la formulaci´on diferencial o macrosc´opica local del principio de conservaci´on de la cantidad de movimiento lineal . Esta expresi´on tiene la ventaja que el miembro izquierdo es expresado en las variables dependientes del problema mientras que el miembro derecho contienen los flujos de estas variables o su cantidades 

**31** 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

duales. Incorporando las ecuaciones constitutivas del material es como transformamos esta ecuaci´on en otra equivalente pero expresada solo en las variables de estado. 

###### Ecuaciones diferenciales de movimiento de un fluido 

En la secci´on anterior derivamos la ecuaci´on vectorial de movimiento expresada seg´un el tensor de tensiones y junto al principio de conservaci´on de la masa forman un sistema de 4 ecuaciones en 3D con 9 inc´ognitas, las tres componentes del vector velocidad y los 6 coeficientes del tensor de tensiones sim´etrico. Para salvar esta indeterminaci´on introducimos informaci´on adicional via las ecuaciones constitutivas del material que relacionan las componentes del tensor de tensiones con la presi´on y los gradientes del vector velocidad llegando finalmente a expresar las anteriores 4 ecuaciones en funci´on de las 4 inc´ognitas, la presi´on y el vector velocidad. 



###### Tensor de tensiones viscoso 

En la secci´on 2 hemos visto que en el caso de la est´atica de fluidos no pod´ıan existir esfuerzos cortantes y que los ´unicos esfuerzos que el fluido es capaz de resistir son aquellos normales. Hab´ımos mencionado que estos eran isotr´opicos y que en definitiva estaban caracterizados por la presi´on: 



Analizando la anterior vemos que para el caso de un fluido en reposo el tensor de tensiones se reduce a un escalar, en realidad asumiendo que la isotrop´ıa se manifiesta mediante un tensor m´ultiplo de la identidad podemos extender lo anterior diciendo que **T** = _−p_ **I** . En general podemos dividir al tensor de tensiones en dos partes, una isotr´opica como la anterior y una no isotr´opica, denominada muchas veces _deviat´orica_ y que corresponde al tensor viscoso, 



siendo **_τ_** = 0 para el caso particular de la est´atica de fluidos. Ya que **T** e **I** son sim´etricos, entonces **_τ_** es sim´etrico y dado que el t´ermino isotr´opico es un tensor diagonal, entonces se satisface que: 



Reemplazando en las 4 ecuaciones arriba planteadas (1.76,1.58) se obtiene: 



donde solo se requiere establecer ecuaciones para las componentes del tensor viscoso en t´ermino de las velocidades o mas generalmente en t´erminos del tensor velocidad de deformaci´on **d** . Si suponemos que el material se comporta como un fluido newtoniano entonces es muy habitual usar la siguiente ley: 



[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

**32** 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

expresada en notaci´on de Gibbs e indicial y en t´ermino de dos coeficientes de viscosidad, _µ_ y _κ_ . 

En pos de poder entender mejor la forma en la que surgen las ecuaciones constitutivas es necesario introducir varios conceptos relacionados con la deformaci´on y la velocidad de deformaci´on de un fluido. No obstante esto es dejado para futuras versiones de estas notas debido a lo extenso del an´alisis, aquellos interesados pueden consultar la bibliografia b´asica del tema [Wi],[Ba]. Por el momento nuestro an´alisis lo enfocamos hacia derivar las ecuaciones diferenciales de movimiento que ser´an la que posteriormente resolveremos via m´etodos num´ericos. Para ello nos conformamos con la definici´on de alguna ley constitutiva. Ya que por lo general siempre se comienza por los casos m´as simples o m´as observados experimentalmente recurrimos a la hip´otesis newtoniana, con la definici´on (1.82), que reemplazada en (1.81) nos da: 



donde _∇_<sup>_T_</sup> **v** es el gradiente del vector velocidad traspuesto, un tensor de segundo orden. Casos particulares como el de flujo incompresible donde la ecuaci´on de continuidad seg´un (1.60) equivale a _∇·_ **v** = 0 simplifica la anterior a: 



Si la viscosidad fuera constante sale fuera del s´ımbolo divergencia y entonces la anterior se simplifica 

a: 



Formulaci´on vorticidad-funci´on de corriente Definimos la vorticidad como: 



Si tomamos la ecuaci´on de conservaci´on del momento lineal para el caso incompresible a viscosidad constante y si le aplicamos el rotor a la misma obtenemos 



donde _∇∧_ **g** representa el rotor del campo de fuerzas de vol´umen en general, ya sea fuerzas gravitatorias como de flotaci´on t´ermica o electromagn´eticas, etc. El t´ermino **_ω_** _·∇_ **v** representa matem´aticamente un t´ermino fuente proporcional a la vorticidad y f´ısicamente est´a asociado a la deformaci´on por contracci´on o elongaci´on del vol´umen material. Como se alcanza a ver en el caso bidimensional este t´ermino no existe porque la vorticidad es un vector orientado en la direcci´on normal al plano del movimiento y el producto escalar con ella es nulo. Solo existe en el escurrimiento 3D. En el caso 2D la vorticidad 

**33** 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

puede tratarse como un escalar ya que su orientaci´on permanecer´a fija y apuntando en la normal al plano del movimiento. Si consideramos ausencia de fuerzas de vol´umen la anterior se simplifica a: 



Introduciendo la definici´on de funci´on de corriente, 



y reemplaz´andola en la definici´on de la vorticidad llegamos a 



Resumiendo la formulaci´on vorticidad-funci´on de corriente en 2D se puede escribir como: 



donde 



El planteamiento de las condiciones de contorno en esta formulaci´on merece un tratamiento cuidadoso y algunos detalles de los mismos se incluyen en el cap´ıtulo de las aplicaciones. 

Flujo compresible 

Hasta el momento hemos hecho bastante hincapi´e en el caso de flujo incompresible en el cual asumimos que la densidad es constante. En esta secci´on trataremos de extender el tratamiento para incluir algunos conceptos introductorios acerca del flujo compresible. En el caso compresible la densidad aparece como una inc´ognita a resolver y en general a partir de argumentos termodin´amicos est´a ligada a otras variables, por ejemplo a la presi´on y temperatura a trav´es de la ecuaci´on de estado. 



Con todo esto es posible cerrar el sistema. Al respecto presentaremos la ecuaci´on de conservaci´on de energ´ıa que debe ser acoplada al resto de las ecuaciones de conservaci´on para luego hacer algunos comentarios acerca de la entrop´ıa. 

Conservaci´on de la energ´ıa 

El postulado fundamental de la conservaci´on de la energ´ıa establece: 



[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 



Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

donde el t´ermino a la izquierda representa la variaci´on temporal de la energ´ıa interna y la cin´etica dentro del vol´umen material o cuerpo, el primer t´ermino de la derecha y el segundo representan trabajos por unidad de tiempo de las fuerzas de gravedad y las de superficie, mientras que el tercer t´ermino contiene el calor intercambiado. De alguna forma esta versi´on integral equivale al primer principio de la termodin´amica aplicado a sistemas cerrados que en general se expresa en forma diferencial o en diferencias: 



Usando la igualdad derivada anteriormente (forma especial del teorema del transporte de Reynolds) (1.62) 



y expresando el vector tensi´on como la contracci´on del tensor de tensiones en la direcci´on normal llegamos a: 



y aplicando el teorema de la divergencia sobre las dos integrales de area para llevarlas a formas equivalentes sobre integrales de vol´umen lo anterior se puede escribir como: 



y si expresamos las fuerzas gravitatorias como conservativas y provenientes del gradiente de un potencial ( _∇φ_ ), podemos simplificar lo anterior a: 



donde hemos agrupado la energia interna, la cin´etica y la potencial en el miembro izquierdo y si aplicamos el balance de masa se llega a: 



En general es com´un a partir de esta expresi´on plantear el balance en un vol´umen de control arbitrario que se mueve a una velocidad distinta a la del fluido y de esta forma obtener el balance macrosc´opico global. Tambi´en es habitual extender lo anterior al caso de sistemas abiertos donde es usual definir la entalp´ıa y plantear el balance en t´erminos de esta funci´on. 

Ecuaci´on de la energ´ıa t´ermica 

Una forma de poner la anterior expresi´on en t´erminos de la energ´ıa t´ermica es remover de (1.97) la ecuaci´on correspondiente al balance de energ´ıa mec´anica. Este se puede hallar tomando las ecuaciones de movimiento y multiplicarla escalarmente por la velocidad, 



[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 



Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.2. Cinem´atica de fluidos_ 

Restando de (1.95) hallamos 



Separando **T** = _−p_ **I** + **_τ_** en su componente normal y en la deviat´orica y pasando a la versi´on diferencia mediante el teorema de la divergencia encontramos : 



- Φ representa la disipaci´on viscosa que aumenta la energ´ıa interna y por ende la temperatura. Ecuaci´on de la entropia 

Partiendo de las funciones caracter´ısticas de la termodin´amica encontramos la relaci´on entre energ´ıa interna, entrop´ıa y densidad, 



Tomando la derivada material y multiplicando por la densidad 



y escribiendo la ecuaci´on de continuidad en la forma 



y usando la igualdad (1.97) llegamos a 



Haciendo el proceso inverso, desde la formulaci´on diferencial llegar a la integral implica en este caso obtener: 



De este balance integral de la entrop´ıa surge que si un proceso es isentr´opico entonces la entrop´ıa del vol´umen material o cuerpo debe permanecer constante y esta condici´on se cumple si: 

1. 1.- **q** _·_ **n** = 0 sobre la superficie, o sea es adiab´atico, 

2. 2.- _∇T_ = 0 sobre el sistema, proceso reversible, 

3. 2.- Φ = 0 sobre el sistema, efectos de fricci´on despreciables. 

[Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

**36** 



<!-- Start of picture text -->
Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos<br>Secci´on 1.3. TP.I.- Trabajo Pr´actico #1<br><!-- End of picture text -->

#### **1.3. TP.I.- Trabajo Pr´actico #1** 

1. Demostrar que para un fluido en reposo (est´atica de fluidos) el tensor de tensiones es isotr´opico. _Ayuda:_ Considere un tetraedro diferencial sumergido en un fluido en reposo. 

2. Dado el man´ometro de la figura encuentre la expresi´on que relaciona la presi´on relativa del interior del tanque respecto a la atmosf´erica en funci´on de las alturas de las columnas usando el principio de conservaci´on de la cantidad de movimiento lineal . 



<!-- Start of picture text -->
Abierto a la atmósfera<br><!-- End of picture text -->



<!-- Start of picture text -->
Abierto a la atmósfera<br>z=h3<br>Tanque de presión z=h2<br>z=h1<br><!-- End of picture text -->



<!-- Start of picture text -->
ρ 2<br>ρ 1<br><!-- End of picture text -->



<!-- Start of picture text -->
z=0<br><!-- End of picture text -->



<!-- Start of picture text -->
Man´ometro<br><!-- End of picture text -->



<!-- Start of picture text -->
3. Calcule la fuerza y el torque aplicado sobre la placa plana de la siguiente figura:<br>+(,*-<br>!#" $<br>&('*)<br><!-- End of picture text -->



<!-- Start of picture text -->
Fuerza sobre un cuerpo plano sumergido<br><!-- End of picture text -->

4. Calcule la fuerza a la que se halla sometida una esfera sumergida sobre la que act´ua un desnivel como el de la siguiente figura: 

- [Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 



<!-- Start of picture text -->
37<br><!-- End of picture text -->

- Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.3. TP.I.- Trabajo Pr´actico_ _<u>#1</u>_ 





<!-- Start of picture text -->
I&JLKNM<br>SUTWV<br><!-- End of picture text -->



<!-- Start of picture text -->
X&YZ<br>#%'1* 2")3%*#4#.5*6#.798#;:4),6<#=%' 7>0#0%*#<br><!-- End of picture text -->



<!-- Start of picture text -->
! "$#&%' ("$#%*),+.-0/<br>#%'1* 2")3%*#4#.5*6#.798#;:4),6<#=%' 7>0#0%*#<br><!-- End of picture text -->

         - Fuerza sobre un cuerpo curvo sumergido 

5. Deduzca la expresi´on de un flujo Couette plano laminar y calcule: (a) la velocidad m´axima y la velocidad promedio en la secci´on transversal al flujo 

      - (b) el caudal en funci´on de la caida de presi´on 

6. Deduzca la expresi´on de un flujo Couette plano laminar pero ahora utilizando una ley de viscosidad no newtoniana. Para ello tome aquella del modelo de fluido de ley de potencia: 

            - _τyx_ = _µ_ 0 _|_<sup>d</sup> d<sup>_v_</sup> _y_<sup>_x|n−_1d</sup> d<sup>_v_</sup> _y_<sup>_x_</sup> 

   - y considere: (a) el caso de un fluido pseudopl´astico ( _n <_ 1) 

      - (b) el caso de un fluido dilatante ( _n >_ 1) 

7. Deduzca la expresi´on de un flujo Couette laminar para un escurrimiento longitudinal a lo largo de un tubo anular donde el radio interior es _r_ 1 y el exterior es _r_ 2. 

8. Repita el Ej 7 pero utilizando un fluido no newtoniano con una ley como la presentada en el ej 6 y calculo la relaci´on entre el caudal y la caida de presi´on. 

9. Partiendo de la definici´on vectorial del teorema de la divergencia demostrar la versi´on escalar del mismo. _Ayuda:_ Un campo escalar puede ser definido por uno vectorial con una orientaci´on fija del campo. 

10. Aplique el teorema de la divergencia a la expresi´on del principio de conseraci´on de cantidad de movimiento lineal (1.6) para el caso de est´atica de los fluidos para obtener la expresi´on diferencial (1.8). 

11. A partir del teorema del transporte de Reynolds (1.52) aplicado a una funci´on escalar del tipo _S_ = _ρs_ hallar la forma especial del teorema expresado por (1.62). _Ayuda: utilice el principio de conservaci´on de la masa para alcanzar el resultado_ 

- [Document version: curso-0.3.0. File version: $Id: tema1.tex,v 1.11 2005/05/22 23:05:10 mstorti Exp $] 

O&PLQR 

**38** 

Cap´ıtulo 1. Modelos fis´ıcos y matem´aticos _Secci´on 1.3. TP.I.- Trabajo Pr´actico_ _<u>#1</u>_ 

12. Probar que si **w** es independiente de las coordenadas espaciales, entonces 



13. Si la velocidad de un fluido viene dada por: 



obtener una expresi´on para la derivada material de la velocidad<sup>_<u>D</u>_</sup> _Dt_<sup>**<u>v</u>**en t´ermino de los coeficientes</sup> _a, b, c_ y _u_ 0. 

**39** 

[Document version: curso-0.3.0. File version: $Id: tema2.tex,v 1.6 2003/05/21 03:02:41 mstorti Exp $] 

## **Cap´ıtulo 2** 

# **Niveles din´amicos de aproximaci´on** 

##### **2.0.1. Introducci´on** 

las ecuaciones de Navier-Stokes 

la dependencia de la viscosidad y la conductividad t´ermica con otras variables 

- leyes constitutivas 

describen completamente el fen´omeno fluidodin´amico en r´egimen laminar. 

No obstante en casi todas las situaciones reales en la naturaleza y en la tecnolog´ıa existe una particular forma de inestabilidad conocida con el nombre de _turbulencia_ . Esta ocurre cuando en ciertas situaciones un n´umero adimensional llamado n´umero de _Reynolds_ , definido por _Re_ = _ρU_ c _harL/µ_ , alcanza o supera determinado valor que depende del problema en particular. _L_ representa una longitud caracter´ıstica y _U_ c _har_ una velocidad caracter´ıstica. Este fen´omeno se caracteriza por la presencia de fluctuaciones estad´ısticas en todas las variables del flujo que se agregan a los valores medios, llegando en algunos casos a alcanzar valores de hasta el 10 % del promedio. 

Dado que la escala que imponen los fen´omenos turbulentos est´an fuera de los alcances de los recursos computacionales actuales, es la tarea de estos tiempos tratar de resolver las ecuaciones de Navier-Stokes en su versi´on promediada y suplementada por alguna descripci´on externa de las tensiones de Reynolds. Esta informaci´on es suministrada por los modelos de turbulencia, cubriendo ellos un rango muy amplio, desde los m´as simples basados en definir una longitud de mezcla y una viscosidad para los _eddies_ hasta aquellos que plantean un balance para el transporte de cantidades como la energ´ıa cin´etica turbulenta y la disipaci´on, modelo denominado _k − ϵ_ , o formas m´as complicadas de calcular las componentes del tensor de Reynolds. A continuaci´on presentamos en forma resumida cuales ser´ıan los distintos niveles de aproximaci´on que se pueden plantear sobre la base de los efectos din´amicos presentes. 

###### **Navier-Stokes tridimensional laminar** 

###### **Navier-Stokes tridimensional turbulento** 

- En el caso de no existir extensas regiones viscosas podemos plantearnos _Thin shear layer_ (TSL). Esta aproximaci´on desprecia los fen´omenos de difusi´on molecular y turbulenta en la direcci´on de transporte reduciendo el n´umero de t´erminos de tensi´on viscosa a calcular. 

40 

Cap´ıtulo 2. Niveles din´amicos de aproximaci´on _Secci´on 2.1. Las ecuaciones de Navier-Stokes_ 

- **Navier-Stokes parabolizado:** En esta aproximaci´on el car´acter el´ıptico de las ecuaciones es responsabilidad de la presi´on mientras que el resto de las variables se parabolizan, reduciendo los fen´omenos de difusi´on a la direcci´on transversal. 

- **Capa l´ımite** Para altos Re podemos introducir una suerte de separaci´on de los efectos viscosos e inv´ıscidos, desacoplando la presi´on de los efectos viscosos y confinando ´estos a una regi´on cercana a los cuerpos mientras que lejos el flujo se comporta como inv´ıscido. 

- **Aproximaci´on inv´ıscida (ecuaciones de Euler)** . Aqu´ı despreciamos todos los efectos viscosos y nos acercamos a los cuerpos tanto como el espesor de la capa l´ımite, no resolviendo lo que sucede dentro de ellas. 

- **Modelo de p´erdidas distribuidas** Es un modelo usado en problemas de flujo interno, en especial en turbom´aquinas. Se ubica en un nivel intermedio entre los modelos total o parcialmente viscosos y aquellos puramente inv´ıscidos. Debido a la existencia de filas de ´alabes las capas l´ımites y las estelas que deja una fila de ellas se mezclan y son vista por la siguiente como una fuerza de fricci´on distribuida. 

- **Modelo de flujo potencial** Este est´a asociado a flujo irrotacional y por su car´acter isoentr´opico presenta problemas de unicidad cuando aparecen discontinuidades debiendo imponerse las condiciones de Rankine-Hugoniot para evitarlas. 

#### **2.1. Las ecuaciones de Navier-Stokes** 



donde _Wf_ = _ρ⃗fe ·⃗v_ . Estas forman un sistema de 5 ecuaciones en el caso 3D expresado aqu´ı en variables conservativas _U_ definidas como: 



No debe confundirse lo que se llama una forma conservativa de lo que son las variables conservativas. La matriz de los vectores flujos _⃗F_ tiene dimensi´on (5 _×_ 3) 



y puede dividirse en tres vectores columnas ( _f, g, h_ ) de 5 componentes cada uno. 

**41** 

[Document version: curso-0.3.0. File version: $Id: tema2.tex,v 1.6 2003/05/21 03:02:41 mstorti Exp $] 

Cap´ıtulo 2. Niveles din´amicos de aproximaci´on _Secci´on 2.1. Las ecuaciones de Navier-Stokes_ 

El lado derecho contiene los t´erminos fuentes, _Q_ , un vector de (5 _×_ 1) 



De esta forma podemos arribar a una forma condensada de las ecuaciones que suele ser muy ´util en ciertas situaciones 



que expresada en sus tres coordenadas cartesianas da lugar a 



Las ecuaciones de Navier-Stokes deben ser suplementadas por leyes constitutivas y por la definici´on del tensor de tensiones viscosas en funci´on de otras variables del flujo. Consideraremos las hip´otesis Newtonianas ya vistas. Las leyes termodin´amicas definen la relaci´on entre la energ´ıa o la entalp´ıa y otras variables termodin´amicas, tales como la temperatura, la densidad o la presi´on. 



Adem´as deben especificarse leyes de dependencia de la viscosidad y la conductividad t´ermica con otras variables del flujo como la temperatura o eventualmente la presi´on. En particular es muy usual en gases expresar la dependencia de la viscosidad con la temperatura a partir de la ley de Sutherland 



Para la conductividad t´ermica puede plantearse algo similar conociendo la relaci´on que vincula _Cp_ = _Cp_ ( _T_ ). En el caso de l´ıquidos _k_ es asumida como constante. 

Muchas veces se usa la hip´otesis de gases perfectos que plantea una expresi´on particular de (2.7), como _e_ = _CvT_ y una relaci´on para las tres variables termodin´amicas a trav´es de la ecuaci´on de estado de los gases 



donde _R_ g _as_ es la constante universal de los gases. 

##### **2.1.1. Modelo de fluido incompresible** 

Las ecuaciones de Navier-Stokes se simplifican considerablemente para el caso de fluidos incompresibles para el cual se asume que la densidad permanece invariable tanto en la coordenada espacial como en el tiempo. Si adem´as el flujo permanece isot´ermico esto separa la ecuaci´on de energ´ıa del resto y el sistema se reduce en una ecuaci´on. En el caso de flujos que involucren variaciones de temperatura el acoplamiento entre la temperatura y el movimiento ocurre a trav´es de : 

variaci´on de la viscosidad con T 

**42** 

[Document version: curso-0.3.0. File version: $Id: tema2.tex,v 1.6 2003/05/21 03:02:41 mstorti Exp $] 

Cap´ıtulo 2. Niveles din´amicos de aproximaci´on _Secci´on 2.1. Las ecuaciones de Navier-Stokes_ 

variaci´on de la conductividad con T 

- fuerzas de flotaci´on 

fuentes de calor de or´ıgen mec´anico, qu´ımico o el´ectrico 

entre otras. 

En el caso incompresible la ecuaci´on de masa se transforma en: 



que aparece como una especie de restricci´on a la ecuaci´on del movimiento que en forma no conservativa se puede escribir como: 



La ecuaci´on de vorticidad de Helmholtz, presentada previamente, se transforma en 



Para flujos donde la densidad no se estratifica el t´ermino en presi´on desaparece de las ecuaciones y el primer t´ermino del lado derecho se anula si el flujo es plano. 

El caso incompresible presenta una situaci´on muy particular, una de las 5 inc´ognitas, la presi´on, no tiene una forma dependiente del tiempo debido al car´acter no evolutivo de la ecuaci´on de continuidad. Esto redunda en una dificultad num´erica que ha dado y continua dando lugar a muchas especulaciones. 

Una ecuaci´on para la presi´on puede obtenerse tomando la divergencia de las ecuaciones de momento y asumiendo un campo de velocidades _solenoidal_ , conduce a: 



que puede ser considerada como una ecuaci´on de Poisson para la presi´on cuando el campo de velocidades es especificado. El t´ermino derecho contiene solo derivadas de primer ´orden para la velocidad. 

##### **2.1.2. Las ecuaciones de Navier-Stokes promediadas** 

El proceso de promediaci´on en el tiempo para un flujo turbulento se introduce para alcanzar las leyes de movimiento para las cantidades medias. La promediaci´on temporal se define de forma de remover la influencia de las fluctuaciones turbulentas sin destruir la dependencia temporal con otros fen´omenos no estacionarios con escala de tiempo diferente a aquellas asociadas con la turbulencia. 

La promediaci´on se define como: 





[Document version: curso-0.3.0. File version: $Id: tema2.tex,v 1.6 2003/05/21 03:02:41 mstorti Exp $] 

Cap´ıtulo 2. Niveles din´amicos de aproximaci´on _Secci´on 2.1. Las ecuaciones de Navier-Stokes_ 

donde _T_ se define como un tiempo suficientemente largo comparado con la escala de sucesos de la turbulencia pero peque˜no comparado a la escala temporal del problema no estacionario. En flujos compresibles este proceso de promediaci´on conduce a productos de fluctuaciones entre cantidades como la densidad y otras variables como la velocidad y la energ´ıa interna. Para evitarlas se recurre a un promedio pesado con la densidad. 



De esta forma se remueven todos los productos necesarios de las fluctuaciones de la densidad con las fluctuaciones de las otras variables. Por ejemplo, la ecuaci´on de continuidad se transforma en 



Aplicada a las ecuaciones de momento llegamos a: 



donde las tensiones de Reynolds se definen como: 



y se agregan a las tensiones viscosas promediadas _<u>τ</u>_<sup>_~~v~~_</sup> . En coordenadas cartesianas tenemos que 



La relaci´on entre las tensiones de Reynolds y las variables debe ser especificada en forma externa y se realiza a trav´es de modelos que contienen una dosis de especulaci´on te´orica combinada con evidencias experimentales. 

##### **2.1.3. Aproximaci´on ”Thin shear layer” (TSL)** 

A elevados n´umeros de Reynolds las capas de corte pr´oximas a las paredes y las que se producen en las estelas ser´an de un tama˜no limitado y si la extensi´on de las zonas viscosas permanece limitada durante la evoluci´on del flujo entonces la influencia dominantes de estas capas estar´a dada por los gradientes en la direcci´on transversal a la corriente fluida. Entonces, la aproximaci´on ”Thin shear layers” consiste en despreciar las derivadas en las direcciones de la superficie que delimitan estas capas de corte y considerar solo las derivadas en la direcci´on normal a ellas. Esta aproximaci´on se sustenta a´un m´as si hechamos un vistazo a las mallas discretas que se confeccionan para flujos con _Re >_ 10<sup>4</sup> que son muy densas en la direcci´on normal a los cuerpos y son muy gruesas en el plano tangente al cuerpo, alcanz´andose muy baja precisi´on en las direcciones contenidas en el plano tangente. 

**44** 

[Document version: curso-0.3.0. File version: $Id: tema2.tex,v 1.6 2003/05/21 03:02:41 mstorti Exp $] 

Cap´ıtulo 2. Niveles din´amicos de aproximaci´on _Secci´on 2.1. Las ecuaciones de Navier-Stokes_ 

La forma condensada de las ecuaciones de Navier-Stokes (2.5) permanecen inalteradas pero el vector flujos _⃗F_ se simplifica por el hecho que 



Entonces si tomamos los flujos en cada una de las tres direcciones locales (tangente, normal y binormal) vemos que 



Como vemos esta aproximaci´on asume flujo inv´ıscido para las direcciones del plano tangente y flujo viscoso s´olo en la direcci´on normal. A diferencia de la aproximaci´on de capa l´ımite, TSL no asume que la presi´on sea constante dentro de la capa l´ımite, con lo cual representa una aproximaci´on tipo capa l´ımite de mayor ´orden. 

##### **2.1.4. Aproximaci´on Navier-Stokes parabolizada** 

Esta aproximaci´on se basa sobre consideraciones similares a TSL pero se aplica solamente al caso estacionario. Esta aproximaci´on va dirigida hacia aquellas situaciones donde existe una direcci´on predominante como ser´ıa el caso de flujo en canales. Adem´as se supone que las regiones viscosas cerca de bordes s´olidos son dominadas por gradientes en el plano normal y por lo tanto la difusi´on de momento y energ´ıa en la direcci´on principal se desprecian. Esta aproximaci´on es solo v´alida mientras no existan zonas con variaciones importantes tal como recirculaciones. Analizando la ecuaci´on de momento en la direcci´on principal (asumimos la x) ser´ıa : 



Esta ecuaci´on por haber perdido el t´ermino de derivada segunda seg´un la direcci´on _x_ cambi´o de tipo el´ıptico a parab´olico ya que seg´un ”x” la derivada primera es la de mayor ´orden. Entonces la 

**45** 

[Document version: curso-0.3.0. File version: $Id: tema2.tex,v 1.6 2003/05/21 03:02:41 mstorti Exp $] 

Cap´ıtulo 2. Niveles din´amicos de aproximaci´on _Secci´on 2.2. Modelo de flujo inv´ıscido_ 

variable ”x” puede ser vista como un pseudo tiempo y se resuelven problemas en 2D avanzando de a capas en ”x”. Similarmente la ecuaci´on de energ´ıa parabolizada se vuelve 



##### **2.1.5. Aproximaci´on de capa l´ımite** 

Fue un gran descubrimiento alcanzado por Prandtl quien reconoci´o que a altos Re las regiones viscosas permanecen acotadas a una extensi´on _δ_ ( del ´orden de _δ/L ≃_ � _ν/UL_ para un cuerpo de longitud L ) a lo largo de cuerpos s´olidos o superficies inmersas o limitando el flujo. En estos casos el c´alculo de la presi´on puede separarse de aquel del campo de velocidades. Comparando esta aproximaci´on con la TSL se puede decir que aqu´ı adem´as de las suposiciones hechas con la TSL se agrega aquella que la velocidad en la direcci´on normal a la superficie se desprecia por lo cual no se produce caida de presi´on en esa direcci´on. De esta forma la presi´on en la capa l´ımite se asume igual a la externa _pe_ ( _x, y_ ) computada a partir de una aproximaci´on inv´ıscida. 

Si bien uno puede separar el c´omputo de la zona o regi´on inv´ıscida del de la capa l´ımite existe muchas situaciones donde existe interacci´on entre ambas y deben resolverse en forma iterativa. Este tipo de aproximaci´on cae dentro de lo que suele llamarse _interacci´on viscosa-inv´ıscisa_ 

#### **2.2. Modelo de flujo inv´ıscido** 

La configuraci´on de flujo m´as general para el caso no viscoso donde se desprecian los efectos de conducci´on del calor se describen mediante las ecuaciones de Euler, obtenidas a partir de las ecuaciones de Navier-Stokes despreciando todos los t´erminos de tensiones viscosas y los de conducci´on del calor. Esta aproximaci´on vale para flujos a elevados n´umero de Reynolds y fuera de las regiones donde se concentran los efectos viscosos. Este modelo respecto al de Navier-Stokes introduce un cambio importante en el conjunto de ecuaciones, el sistema de segundo ´orden se transforma en uno de primer ´orden, modificando no solo la aproximaci´on f´ısica y num´erica sino tambien la especificaci´on de las condiciones de contorno. Las ecuaciones de Euler no estacionarias tienen una forma condensada similar a aquella presentada en (2.5) 

###### _∂U_<sup>_⃗_</sup> 



para el caso de Navier-Stokes , con la modificaci´on puesta en la forma de definir el vector flujo _⃗F_ En este caso los flujos se definen como 



Una consideraci´on importante le cabe a la entrop´ıa. Ya que el modelo de Euler asume la no existencia de conducci´on del calor ni de esfuerzos viscosos, si tomamos la ecuaci´on (2.6.f) 



[Document version: curso-0.3.0. File version: $Id: tema2.tex,v 1.6 2003/05/21 03:02:41 mstorti Exp $] 



Cap´ıtulo 2. Niveles din´amicos de aproximaci´on _Secci´on 2.2. Modelo de flujo inv´ıscido_ 

vemos que el segundo miembro es nulo, por lo cual ´esta se reduce a: 



expresando que la entrop´ıa es constante a lo largo de las l´ıneas de corriente. Por lo tanto las ecs. de Euler describen flujos isentr´opicos en ausencia de discontinuidades. No obstante la entrop´ıa puede variar de una l´ınea de corriente a otra y esto es visto por una forma especial atribuida a Crocco de describir las ecuaciones de momento , cuando se la aplica al caso inv´ıscido y estacionario en ausencia de fuerzas externas. Esta se expresa como: 



Si por un momento asumimos un campo uniforme de entalp´ıas vemos que la derivada normal de la entrop´ıa (en el plano tangente no var´ıa) equivale a la componente normal en la terna de Frenet del producto vectorial entre la velocidad y la vorticidad y que es equivalente al producto de la componente binormal de la vorticidad con la velocidad normal, o sea 



Por lo tanto gradientes de entropia y vorticidad est´an directamente vinculados. Las ecuaciones de Euler tambi´en permiten discontinuidades en capas vorticosas, en ondas de choque o del tipo discontinuidades de contacto, pero ellas deben obtenerse usando la forma integral del las ecuaciones ya que la forma diferencial asume continuidad de la soluci´on. 

##### **2.2.1. Propiedades de las soluciones discontinuas** 

Si dentro de un vol´umen V existe una superficie Σ que se mueve con una velocidad _⃗C_ donde la soluci´on presenta una discontinuidad debemos recurrir a la forma integral de las ecuaciones de Euler, que en ausencia de t´erminos fuentes se puede escribir como: 



Ya que debemos seguir el movimiento de la superficie para poder estudiar su evoluci´on, debemos aplicar el teorema del transporte de Reynolds sobre el t´ermino temporal, que dice: 

Para cualquier funci´on _f_ ( _⃗x, t_ ) tenemos que 



Entonces usando (2.30) con _f_ = 1 y el teorema de la divergencia sobre (2.29) produce lo siguiente: 



[Document version: curso-0.3.0. File version: $Id: tema2.tex,v 1.6 2003/05/21 03:02:41 mstorti Exp $] 



Cap´ıtulo 2. Niveles din´amicos de aproximaci´on _Secci´on 2.2. Modelo de flujo inv´ıscido_ 

Asumiendo que el vol´umen tiende a cero el t´ermino del flujo puede ponerse como: 



donde _d⃗_ Σ es la normal a la superficie de la discontinuidad Σ y donde definimos el salto de una variable que cruza una discontinuidad _A_ como � � 



Combinando (2.29) con (2.32) llegamos a 



que conduce a la forma local de las leyes de conservaci´on sobre una discontinuidad, llamadas las relaciones de _Rankine-Hugoniot_ : 



Si Σ( _⃗x, t_ ) = 0 define la superficie de discontinuidad, entonces 



y si definimos la normal a la superficie como 

entonces, reemplazando en (2.34) obtenemos 



###### **Distintas formas de discontinuidad** 

_shocks:_ todas las variables del flujo son discontinuas 

_de contacto y capas vorticosas (”slip lines”):_ 

- no ha transferencia de masa a trav´es de ellas 

- densidad y velocidad tangencial discontinuas 

- presi´on y velocidad normal continuas 

Si vemos las propiedades del sistema desde una terna que se mueve junto a la discontinuidad, las relaciones de Rankine Hugoniot para las ecuaciones de Euler se transforman en: 



**48** 

[Document version: curso-0.3.0. File version: $Id: tema2.tex,v 1.6 2003/05/21 03:02:41 mstorti Exp $] 

Cap´ıtulo 2. Niveles din´amicos de aproximaci´on _Secci´on 2.3. Flujo_ _<u>potencial</u>_ 

_Discontinuidad de contacto_ Al no haber transporte de masa a trav´es de ellas 



y de (2.36) surge que 

y en general 



_Capas vorticosas (”Slip lines”)_ Como antes 



permitiendo saltos en la velocidad tangencial y en la densidad 



_Ondas de choque_ Ellas permiten el transporte de masa a trav´es y por lo tanto la velocidad normal y la presi´on pueden ser discontinuas mientras que la velocidad tangencial permanece continua. Entonces 



La llamada _condici´on de entrop´ıa_ da la informaci´on necesaria para poder filtrar de todas las posibles soluciones aquellas que no tengan sentido f´ısico. Esto est´a fuera de los alcances de este curso. Del mismo modo no ser´a tratado aqu´ıa el tema de la formulaci´on de flujo inv´ıscido rotacional mediante la representaci´on de _Clebsch_ que permite una descripci´on m´as econ´omica en t´ermino de c´omputo pero m´as compleja en cuanto a su interpretaci´on. 

#### **2.3. Flujo potencial** 

Si a la hip´otesis del flujo inv´ıscido le agregamos la _irrotacional_ lo cual matem´aticamente podemos expresar como: 



el campo tridimensional de velocidades puede ser descripto por una ´unica funci´on escalar _φ_ , llamada funci´on potencial y definida por: 

**49** 

[Document version: curso-0.3.0. File version: $Id: tema2.tex,v 1.6 2003/05/21 03:02:41 mstorti Exp $] 

Cap´ıtulo 2. Niveles din´amicos de aproximaci´on _Secci´on 2.3. Flujo_ _<u>potencial</u>_ 



lo cual reduce notoriamente el c´alculo. Si las condiciones iniciales son compatibles con un campo de entrop´ıa uniforme, luego para flujos continuos la entrop´ıa ser´a constante en todo el dominio y las ecuaciones de momento se transforman en 



o 



donde la constante _H_ 0 es la entalp´ıa de todas las l´ıneas de corriente. De esta forma la ecuaci´on de energ´ıa ya no ser´a independiente del resto. La ecuaci´on para flujo potencial surge de la ecuaci´on de continuidad tomando en cuenta la hip´otesis de flujo isoentr´opico para poder expresar la densidad como una funci´on de la velocidad, o sea del gradiente del potencial. 

En forma de conservaci´on tenemos 



que junto con la relaci´on entre densidad y funci´on potencial 



completan el modelo. _ρA_ y _hA_ son valores de referencia para la densidad y la entalp´ıa que a menudo corresponden con las condiciones de estancamiento. _Caso estacionario_ 



y 



surgen como el modelo a resolver. 

Algunos temas a agregar m´as adelante son: 

_Flujo irrotacional con circulaci´on - condici´on de Kutta-Joukowski Limitaciones del modelo de flujo potencial para flujos trans´onicos_ 

**50** 

[Document version: curso-0.3.0. File version: $Id: tema2.tex,v 1.6 2003/05/21 03:02:41 mstorti Exp $] 

Cap´ıtulo 2. Niveles din´amicos de aproximaci´on _Secci´on 2.3. Flujo_ _<u>potencial</u>_ 

##### **2.3.1. Aproximaci´on de peque˜nas pertubaciones** 

En flujos estacionarios o no estacionarios alrededor de perfiles alares con un espesor mucho menor que su cuerda se puede asumir que las velocidades en el plano normal son despreciables simplificando a´un m´as el modelo. Asi surge el modelo de _peque˜nas perturbaciones_ que matem´aticamente se escribe como: 



##### **2.3.2. Flujo potencial linealizado** 

Si el flujo es incompresible hemos visto que la ecuaci´on de continuidad se expresa como 



y por la hip´otesis del modelo potencial _⃗v_ = _⃗ ∇φ_ entonces (2.45) se transforma en 



la ecuaci´on de Laplace. 

Otra forma de linealizar el problema es usando superposici´on de flujos simples, como fuentes, sumideros y v´ortices calibrando los coeficientes con que cada uno participa de forma de ajustar la condici´on de contorno de velocidad normal nula sobre cuerpos s´olidos. 

Los m´etodos basados en singularidad provienen de plantear el problema en forma integral, usar n´ucleos (“ kernels “) que representen la influencia espacial y resolver num´ericamente. Estos m´etodos son llamados singulares porque casualmente producen integrales singulares cuyo tratamiento no es trivial y est´a fuera del alcance del curso. M´etodos como el de los _paneles_ o el m´etodo de los _elementos de borde_ son los m´aximos representantes de ´esta t´ecnica. 

**51** 

[Document version: curso-0.3.0. File version: $Id: tema3.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

## **Cap´ıtulo 3** 

# **Naturaleza matem´atica de las ecuaciones de la mec´anica de fluidos** 

#### **3.1. Introducci´on** 

Para comenzar resumimos las varias aproximaciones vistas en el cap´ıtulo anterior de forma tal de mostrar las ecuaciones que surgen de los modelos vistos. 

En general las leyes de conservaci´on plantean una ecuaci´on del tipo 



que expresada en sus tres coordenadas cartesianas dan lugar a 



Las ecuaciones de Navier-Stokes se pueden expresar en su forma general como 



En el caso incompresible se transforman en 





donde es muy com´un desacoplar el problema en una soluci´on para la velocidad y otra para la presi´on. Para esta ´ultima surge 



52 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.1. Introducci´on_ 

En la aproximaci´on _”Thin shear layer (TSL)”_ hemos visto 



mientras que en el caso parabolizado cambia solamente la ecuaci´on de momento seg´un la direcci´on preferencial del flujo por otra del tipo 



y la de energ´ıa por la siguiente 

En el modelo inv´ıscido 

y en flujo potencial tenemos el caso general 



junto con la relaci´on entre densidad y funci´on potencial 



y los casos de peque˜nas perturbaciones 

[Document version: curso-0.3.0. File version: $Id: tema3.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.1. Introducci´on_ 

o el caso linealizado con 



Examinando las anteriores ecuaciones provenientes de los modelos f´ısicos asumiendo distintos niveles de aproximaci´on din´amica podemos decir que todas se representan por un conjunto de ecuaciones a derivadas parciales cuasi-lineales de primer o a lo sumo segundo ´orden. 

Por lo visto al comienzo el modelo matem´atico refleja un balance entre flujos convectivos, difusivos y diversas fuentes internas y externas que surgen a partir del modelo planteado por la f´ısica. 

Los _flujos difusivos_ aparecen con operadores de segundo ´orden como una consecuencia de la ley generalizada de Fick, con una tendencia a suavizar gradientes. 

Los _flujos convectivos_ aparecen con operadores de primer ´orden y expresan el transporte de la propiedad. 

Por lo tanto la competencia entre ellos influenciar´a sobre la naturaleza matem´atica de las ecuaciones, desde las ecuaciones el´ıpticas, parab´olicas hasta las hiperb´olicas. Del mismo modo es la persona que modela la que al introducir una aproximaci´on est´a forzando sobre el tipo de ecuaci´on con que se enfrentar´a. 

Tomemos a modo de ejemplo de esto la componente _x_ de la ecuaci´on de momento de las ecuaciones de Navier-Stokes asumiendo flujo laminar e incompresible. 



Adimensionalizar estas ecuaciones es un modo de ver mejor aquello de la competencia. Para ello tomemos una longitud de referencia _L_ , un tiempo caracter´ıstico _T_ , una escala de velocidades _V_ y una de presiones _ρV_<sup>2</sup> . Reemplazando como es habitual en (4.1.1) surge 



donde _Re_ =<sup>_<u>ρV L</u>_</sup> _µ_ =<sup>_<u>V L</u>_</sup> _ν_ es el n´umero de Reynolds y todas las variables, las independientes como las dependientes, se expresan en la versi´on adimensionalizada. 

Para _Re →_ 0, flujos fuertemente viscosos, denominados reptantes, el t´ermino convectivo y no lineal es despreciable y surgen las ecuaciones de _Stokes_ 



Asumimos que el gradiente de presi´on est´a fijado para poder reducir este caso ejemplificatorio al caso de una ecuaci´on y no entar en las complejidades que presupone un sistema de ecuaciones con varias inc´ognitas. Asi como est´an escritas son de naturaleza parab´olica debido a la existencia de un operador de primer ´orden para una de las variables independientes, el tiempo, y uno de segundo ´orden para la otra, la coordenada _x_ . Si agregamos la hip´otesis de flujo estacionario entonces desaparece el t´ermino temporal y la ecuaci´on se transforma en el´ıptica _(ec. de Poisson)_ 

Si _Re →∞_ y si nos ubicamos fuera de la capa l´ımite, los t´erminos viscosos tendr´an muy poca influencia haciendo que el flujo sea dominado por los t´erminos convectivos (ecs. de Euler). 



[Document version: curso-0.3.0. File version: $Id: tema3.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.2. Superficies caracter´ısticas. Soluciones del tipo ondas_ 

Si reducimos el problema al caso unidimensional la anterior se vuelve 



que es una ecuaci´on hiperb´olica que describe un fen´omeno de propagaci´on. 

Es de gran importancia la distinci´on entre fen´omenos de difusi´on (el´ıpticos) y de propagaci´on (hiperb´olicos), ya que en los primeros la informaci´on se propaga en todas direcciones mientras que en los ´ultimos existe una direcci´on preferencial y la informaci´on se propaga solo a determinadas regiones. Entre ambos existen las ecuaciones parab´olicas que amortiguan en el tiempo los efectos difusivos. Las ecuaciones de Navier-Stokes son de car´acter parab´olicas en el espacio y en el tiempo y cambian de tipo al caso el´ıptico en el estado estacionario. De todas maneras es importante resaltar que la ecuaci´on de continuidad al no contar con difusi´on es de car´acter hiperb´olico lo cual hace que, estrictamente hablando, las ecuaciones de Navier-Stokes sean incompletamente parab´olicas. 

#### **3.2. Superficies caracter´ısticas. Soluciones del tipo ondas** 

Las ecuaciones a derivadas parciales que describen los niveles de aproximaci´on vistos en el cap´ıtulo anterior son cuasi-lineales y a lo sumo de segundo ´orden. No obstante se sabe que en muchos casos existe una forma no degenerada de llevar un sistema de segundo ´orden a otro de primer ´orden. Asumimos que contamos con la transformaci´on necesaria y que tenemos entre manos un sistema cuasi-lineal de primer ´orden. La clasificaci´on de las ecuaciones est´a ´ıntimamente relacionada con el concepto de _caracter´ısticas_ , definida como hipersuperficies a lo largo de la cual ciertas propiedades del flujo permanecen invariables o ciertas derivadas pueden volverse discontinuas. 

Un sistema de ecuaciones a derivadas parciales de primer ´orden se dice hiperb´olico si su parte homog´enea admite soluci´on del tipo ondulatoria. Ya veremos que esto est´a asociado con el hecho que los autovalores del sistema son reales. Por otro lado si el sistema admite soluci´on del tipo ondas amortiguadas (evanescentes) el sistema ser´a parab´olico y si no admite soluci´on del tipo ondulatorio ser´a el´ıptico y dominado por difusi´on. 

#### **3.3. Ecuaciones diferenciales parciales de segundo ´orden** 

Sea el siguiente operador cuasi-lineal de segundo ´orden 





[Document version: curso-0.3.0. File version: $Id: tema3.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.3. Ecuaciones diferenciales_ _<u>parciales</u> de segundo ´orden_ 

que en forma matricial se escribe como 



Si la soluci´on es expresable como una onda plana que se propaga en la direcci´on _⃗n_ , ´esta tendr´a la forma 

_U_ = _Ue_<sup>ˆ</sup><sup>_I_(</sup><sup>_⃗n·⃗x_)</sup> = _Ue_<sup>ˆ</sup><sup>_I_(</sup><sup>_nxx_+</sup><sup>_nyy_)</sup> (3.11) 

con _I_ =<sup>_√_</sup> _−_ 1. 

Reemplazando la soluci´on(4.2.3) en (4.2.2) y tomando la parte homog´enea nos queda 



que admitir´a soluci´on no trivial solo si el determinante del sistema es nulo, 



O sea que las raices de 



nos dar´an la respuesta a si la soluci´on es expresable como una onda, o sea si es hiperb´olica o si se trata de una onda pero amortiguada (parab´olica) o si no existe soluci´on real en cuyo caso es el´ıptica. Resolviendo, 

_b_<sup>2</sup> _− ac >_ 0 dos soluciones reales, dos ondas (hiperb´olico) 



_b_<sup>2</sup> _− ac <_ 0 dos soluciones complejas conjugadas, (el´ıptico) 

En lo anterior hemos asumido una soluci´on del tipo onda plana. Esto puede generalizarse a hipersuperficies generales con una representaci´on no lineal de la onda. Esta consiste en definir una superficie que funciona como frente de onda _S_ ( _x, y_ ) y la soluci´on se representa por una onda general del tipo 



A partir de aqu´ı la operatoria es la misma que en el caso de onda plana. Un sistema es hiperb´olico si (4.2.7) es una soluci´on para valores reales de _S_ ( _x, y_ ) Esto se logra calculando 



donde _Sx, Sy_ son las derivadas de la superficie respecto a las direcciones que caen sobre ella. 

Las superficies _S_ ( _x, y_ ) que hacen el anterior determinante nulo son superficies caracter´ısticas con una normal que apunta segun _⃗ ∇S_ . 

**56** 

[Document version: curso-0.3.0. File version: $Id: tema3.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.3. Ecuaciones diferenciales_ _<u>parciales</u> de segundo ´orden_ 

_Ejemplo 1: Flujo potencial estacionario_ Llamemos _c_ a la velocidad del sonido. Si tomamos la ecuaci´on del modelo de flujo potencial y trabajamos algebraicamente sobre la relaci´on entre densidad y funci´on potencial asumiendo transformaciones isoentr´opicas llegamos a 



que en el caso 2D estacionario se simplifica a 



que bajo la forma de una ecuaci´on general de segundo ´orden (4.2.2) posee los siguientes coeficientes: 



Entonces el discriminante _b_<sup>2</sup> _−_ 4 _ac_ se vuelve 



lo cual es negativo (el´ıptico) en el caso subs´onico y positivo (hiperb´olico) en el caso supers´onico. En el caso trans´onico el problema se transforma en parab´olico. Como vemos el problema potencial tiene una naturaleza bastante variada dependiendo del r´egimen de velocidades que estemos resolviendo. Una complicaci´on adicional a esto aparece por el hecho que en el caso trans´onico y supers´onico pueden aparecen discontinuidades como ondas de choque con un tratamiento num´erico bien particular. 

_Ejemplo 2: La ecuaci´on potencial en peque˜nas perturbaciones_ Como hemos visto si la componente transversal al flujo del vector velocidad es despreciable, la ecuaci´on potencial estacionaria se reduce a 



entonces las raices de la ecuaci´on (4.2.6) son 



que definen las normales a las dos caracter´ısticas para flujos supers´onicos. Estas se obtienen como 



Estas caracter´ısticas son id´enticas a las l´ıneas de Mach que se hallan a un ´angulo _µ_ respecto a la direcci´on del vector velocidad, con 



**57** 

[Document version: curso-0.3.0. File version: $Id: tema3.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.4. Definici´on_ _<u>general</u> de superficie caracter´ıstica_ 

#### **3.4. Definici´on general de superficie caracter´ıstica** 

Sea un sistema de _n_ ecuaciones diferenciales parciales de primer ´orden para las _n_ inc´ognitas _u_<sup>_i_</sup> _, i_ = 1 _, . . . , n_ en el espacio _m_ dimensional _x_<sup>_k_</sup> _, k_ = 1 _, . . . , m_ incluyendo eventualmente la variable tiempo. Escrita en forma de conservaci´on y usando la convenci´on de suma sobre ´ındices repetidos tenemos 



El an´alisis de las propiedades del sistema recae sobre la forma cuasi-lineal obtenida despu´es de introducir las matrices jacobianas _A_<sup>_k_</sup> definidas por 



Por lo tanto el sistema (4.5.1) toma la forma cuasi-lineal 



que en forma condensada se escribe como 



donde el vector columna _U_ es de ( _n ×_ 1) y contiene las inc´ognitas _u_<sup>_j_</sup> , mientras que _A_<sup>_k_</sup> son matrices de _n × n_ y _Q_ un vector de t´erminos fuentes. Las matrices _A_<sup>_k_</sup> y el vector _Q_ pueden depender de _x_<sup>_k_</sup> y de _U_ pero no del gradiente de _U_ . 

Una soluci´on expresada como una onda plana de la forma (4.2.3) o en general (4.2.7) existir´a si el sistema homog´eneo 



admite soluciones no triviales, lo cual como antes redunda en que 



Esta ecuaci´on tiene a los sumo _n_ soluciones, las _n_ superficies caracter´ısticas. El sistema se dice _hiperb´olico_ si todas las caracter´ısticas son reales y si las soluciones son linealmente independientes. Si todas son complejas es _el´ıptico_ y si hay de ambas es h´ıbrido. Adem´as si el rango de _A_<sup>_k_</sup> _nk_ no es completo el sistema se dice _parab´olico_ . Esto ocurrir´a cuando al menos una de las variables no posea derivadas respecto a alguna de las coordenadas espaciales. 

_Ejemplo 3 : Sistema de 2 ecs de primer ´orden en 2D_ Sea el siguiente sistema de ecuaciones en 2D 



[Document version: curso-0.3.0. File version: $Id: tema3.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.4. Definici´on_ _<u>general</u> de superficie caracter´ıstica_ 

que en forma matricial se puede escribir como 



donde 



Planteando el determinante e igualando a cero conduce a las raices: 



Si _cd/ab >_ 0 el sistema es hiperb´olico, por ejemplo tomemos _a_ = _b_ = _c_ = _d_ = 1, en este caso el sistema de ecuaciones es la conocida _ecuaci´on de las ondas_ que escrita como una ecuaci´on de segundo ´orden luce como 



Si _cd/ab <_ 0 el sistema es el´ıptico, por ejemplo tomemos _a_ = _b_ = 1 ; _c_ = _−d_ = _−_ 1, en este caso el sistema de ecuaciones es la conocida _ecuaci´on de difusi´on o de Laplace_ 



Finalmente si _b_ = 0 existe una sola caracter´ıstica y el sistema es parab´olico. Con _a_ = 1 ; _b_ = 0 ; _c_ = _−d_ = _−_ 1 ; _f_ 1 = 0 ; _f_ 2 = _v_ obtenemos la conocida _ecuaci´on del calor_ 



_Ejemplo 4: Ecuaciones en aguas poco profundas estacionaria_ Este sistema, conocido como _”shallow water equations”_ , describe la distribuci´on espacial de las alturas de la superficie libre de una corriente de agua que posee un campo de velocidades ( _u, v_ ). Si llamamos _g_ a la aceleraci´on de la gravedad, entonces: 



Introduciendo el vector de inc´ognitas 



**59** 

[Document version: curso-0.3.0. File version: $Id: tema3.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.5. Dominio de dependencia - zona de influencia_ 

el sistema se puede escribir en forma matricial como 



o en forma compacta 



Las tres superficies caracter´ısticas se obtienen como la soluci´on de plantear el siguiente determinante nulo, con _λ_ = _nx/ny_ 



Trabajando sobre el determinante conduce a las soluciones : 

Como vemos<sup>_√_</sup> _gh_ juega el mismo rol que la velocidad del sonido en el caso de las ecuaciones de flujo compresible, y como all´ı , existe un valor cr´ıtico donde el sistema cambia de tipo. Este valor se llama velocidad supercr´ıtica y en el caso que _⃗v_<sup>2</sup> = _u_<sup>2</sup> + _v_<sup>2</sup> _> gh_ el sistema se vuelve _hiperb´olico_ . 

En el caso de velocidades subcr´ıtico el sistema es _h´ıbrido_ ya que habr´a 2 soluciones complejas conjugadas y _λ_<sup>(1)</sup> que siempre es real. La superficie caracter´ıstica asociada con _λ_<sup>(1)</sup> es la l´ınea de corriente, ya que _nx_<sup>(1)</sup> = _−v_ ; _n_<sup>(1)</sup> _y_ = _u_ . 

#### **3.5. Dominio de dependencia - zona de influencia** 

Las propiedades de propagaci´on de los problemas hiperb´olicos tiene importantes consecuencias respecto a la forma en que la informaci´on se propaga o transmite por todo el dominio. 

Si consideramos el caso escalar bidimensional presentado en (4.2.1) este generar´a dos caracter´ısticas en el caso hiperb´olico donde cada una se representa por una familia de curvas. Si tomamos 1 miembro de cada familia y tomamos un punto _P_ donde se intersectan, vemos que ambas caracter´ısticas dejan una regi´on aguas arriba que afectar´a la soluci´on en el punto _P_ y una zona aguas abajo que depender´a del valor de la funci´on en el punto _P_ . Mir´andolo desde el punto _P_ , la primera se llama _zona de dependencia_ del punto P y la segunda _zona de influencia_ del punto P. Este hecho es muy importante y tiene muchas consecuencias matem´aticas, f´ısicas y num´ericas. (figura 3.5) 

En el caso de problemas parab´olicos ambas caracter´ısticas degeneran en una (el rango del sistema no es completo) y en este caso la zona de dependencia cae sobre la caracter´ıstica mientras que la de influencia es la regi´on completa aguas abajo de la caracter´ıstica. 

En el caso el´ıptico no existe superficie caracter´ıstica que separe el dominio en zonas de dependencia e influencia. Esto produce que la zona de influencia, la de dependencia y el dominio coincidan y la informaci´on se propaga en todas direcciones. 

**60** 

[Document version: curso-0.3.0. File version: $Id: tema3.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.6. Condiciones de contorno e iniciales_ 



<!-- Start of picture text -->
características<br>P<br>Γ<br>A<br>B<br>Región de dependencia de P<br>C<br>Zona de influencia de P<br><!-- End of picture text -->

Dominio de dependencia e influencia 

#### **3.6. Condiciones de contorno e iniciales** 

Para que los anteriores sistemas de ecuaciones que surgen del modelo f´ısico est´en finalmente bien planteados en el sentido matem´atico es necesario que se impongan ciertas condiciones sobre los datos. Si alguna de las variables independientes del problema es el tiempo es necesario establecer una condici´on a tiempo _t_ = 0 _∀⃗x_ , problema llamado _de Cauchy_ o de _valores iniciales_ . Cuando la variable espacial _x_ est´a acotado en el espacio por un borde o contorno, el problema suele llamarse de _valores de frontera e iniciales_ . 

Sin entrar en detalles acerca del tema podemos decir que la correcta especificaci´on de las condiciones de contorno e iniciales requiere de un detallado estudio que incluye a las autofunciones del sistema. 

De todos modos este es un tema abierto ya que en la mayor´ıa de los casos que trata la mec´anica de fluidos no existen resultados contundentes acerca de como tratar estas condiciones. 

Sin ir tan lejos terminamos esta secci´on diciendo que en los problemas independientes del tiempo de car´acter el´ıptico es usual imponer algunos valores sobre algunos nodos _(Dirichlet)_ o sobre su derivada _(Neumann)_ . En el primer caso puede tratarse de imponer el vector velocidad sobre una pared s´olida o la temperatura, mientras que en el caso Neumann estamos hablando de imponer que el flujo t´ermico asuma alguna ley de transferencia en el contorno (convecci´on, radiaci´on,etc). 

En casos donde el sistema se transforma en primer ´orden (Euler), la velocidad no puede ser fijada en un contorno s´olido, recurriendo a fijar solo la componente normal, dejando la tangencial como parte del c´alculo (condici´on slip). En el caso de superficies libres es usual establecer la continuidad de las tensiones normales y tangenciales. 

**61** 

[Document version: curso-0.3.0. File version: $Id: tp2.tex,v 1.2 2003/04/20 10:14:34 mstorti Exp $] 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.6. Condiciones de contorno e iniciales_ 

#### **INTRODUCCION AL USO DE MATLAB** 

**Objetivos:** Aprender el uso del lenguaje _MatLab_ muy poderoso en cuanto a sus posibilidades de uso como herramienta de c´alculo num´erico y visualizaci´on gr´afica asi como de programar en este entorno extendiendo su aplicaci´on al an´alisis num´erico y simulaci´on en Ingenier´ıa. 

##### **3.6.1. Introducci´on** 

**MatLab** es un lenguaje de programaci´on interpretado de bajo nivel que a diferencia de los lenguajes compilados permite gran flexibilidad para programar, debuggear y correr peque˜nas aplicaciones respecto a los tradicionalmente r´apidos pero muy r´ıgidos lenguajes compilados. Adem´as es un software de aplicaci´on y como su nombre lo indica es un laboratorio de matrices (Mat=Matrices / Lab =Laboratorio). Otra de las importantes caracter´ısticas es que incluye poderosas facilidades gr´aficas que se pueden correr run-time, mientras que en el caso de los lenguajes compilados uno debe o bien generar un software gr´afico completo o sino adaptar algunas rutinas para los casos particulares de aplicaci´on, lo cual lo transforma en una gran complicaci´on. Adem´as el hecho que los c´alculos y las gr´aficas se vayan generando en tiempo de ejecuci´on lo hace muy flexible. Otras de la caracter´ısticas interesantes de este lenguaje interpretado es que equivale a un entorno en s´ı mismo, o sea permite ejecutar comandos en forma muy interactiva lo cual lo hace apto para ir avanzando en lo que uno est´a haciendo, viendo resultados en pantalla de lo que uno est´a obteniendo, corrigiendo rumbos, etc. Adem´as cuenta con una enorme biblioteca de rutinas de c´alculo que lo transforma en un lenguaje de bajo nivel sin necesidad de tener que programar demasiado, salvo aplicaciones especiales. Hemos dicho al comienzo que una de las principales diferencias entre un lenguaje compilado y uno interpretado es la velocidad de procesamiento de datos, especialmente para grandes problemas. El programa compilado arma un ejecutable habiendo interpretado cada sentencia previamente en la etapa de compilaci´on y genera un archivo binario optimizado. En cambio el lenguaje interpretado realiza la interpretaci´on de cada sentencia a medida que corre lo cual lo hace lento. Por ejemplo si uno realiza un loop de 1000 iteraciones el int´erprete debe trabajar 1000 veces haciendo lo mismo. MatLab soporta vectorizaci´on lo cual hace que en lugar de manejar escalares e interpretar operaciones entre escalares pueda manejar vectores e interpretar vectores. Por ejemplo si tenemos un vector de 1000 elementos y queremos hacer c´alculos con cada uno de sus coeficientes, en lugar de hacer un loop de 1000 iteraciones podemos invocar directamente la operaci´on sobre todo el vector. Por ejemplo, si tenemos una matriz _A_ de (1000 _×_ 2), donde cada columna representa un vector de 1000 elementos y queremos calcular la suma de ellos podemos hacer: 

###### `for k=1:1000,` 

```
c(k)=A(k,1)+A(k,2);
```

```
end
```

o sencillamente 

###### `c = A(:,1)+A(:,2);` 

Todo esto y muchas cosas m´as que surgen cuando uno lo utiliza hacen a MatLab una muy interesante herramienta para la investigaci´on en torno a los m´etodos num´ericos. 

**62** 

[Document version: curso-0.3.0. File version: $Id: tp2.tex,v 1.2 2003/04/20 10:14:34 mstorti Exp $] 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.6. Condiciones de contorno e iniciales_ 

MatLab cuenta con muchas rutinas propias llamadas _built in functions_ , solo basta con recorrer el help para ver la enorme cantidad de ellas. Adem´as cuenta con lo que se llaman _Toolkits_ que son paquetes de rutinas para aplicaciones particulares. Aqu´ı˜no entraremos en detalle sobre estas ´ultimas sino que s´olo mencionamos su existencia para aquellos curiosos que puedan interesarse. A grandes rasgos podemos decir que MatLab es un lenguaje de programaci´on integrado con un software de aplicaci´on. Entonces podemos hacer una divisi´on inicial en: 



A continuaci´on planeamos hacer un peque˜no _tour_ por las galer´ıas de MatLab tratando de tocar s´olo algunos de sus puntos con el objetivo de motivar a los turistas a volver a ellos en el futuro. 

##### **3.6.2. MatLab como software de aplicaci´on** 

En esta parte de la visita a MatLab investigaremos sus capacidades como software de aplicaci´on, sin entrar por ahora en detalles de programaci´on. Como fue dicho en la introducci´on este software es un _laboratorio de matrices_ y como tal debemos saber como definir matrices, vectores como un caso particular de una matriz, recordar algunos aspectos del ´algebra de espacios vectoriales para poderlas utilizar en forma coherente y finalmente ver las potencialidades que tiene esto. Yendo m´as all´a en cuanto a aplicaciones hemos mencionado las capacidades gr´aficas del software. A este respecto debemos primero saber como convertir matrices en mapas redefiniendo el ´algebra y viendo como de esta forma es posible visualizar funciones en varias variables y hacer distintos tipos de gr´aficos muy ´utiles en general. 

###### **(1) Manejo standard de matrices, vectores y escalares** 

Una matriz es el ´atomo de este software, es algo asi como la menor porci´on divisible del c´alculo, siendo los escalares y los vectores s´olo casos particulares. Por ejemplo para ingresar la matriz 



debemos ingresar sus coeficientes como una lista de n´umeros separados por un blanco al menos que corresponden a los elementos de cada fila, separando las filas entre si con un ; o simplemente con `<Enter>` , o sea 



El `;` despues del `]` finaliza la sentencia sin mostrar por pantalla lo ingresado. Si uno quiere ver lo que ingresa hay que remover el `;` . Su uso es muy importante cuando las matrices son muy grandes ya que la salida por pantalla puede tomar bastante tiempo. 

[Document version: curso-0.3.0. File version: $Id: tp2.tex,v 1.2 2003/04/20 10:14:34 mstorti Exp $] 

**63** 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.6. Condiciones de contorno e iniciales_ 

Un vector es un caso particular de lo anterior, este puede ser un vector fila o un vector columna. Sean 



En estos casos el ingreso es 





o simplemente podemos definir 



```
c=b’;
```

donde el s´ımbolo `’` significa la transpuesta, de un vector como en este caso pero su uso es en general para cualquier matriz. 

Todas los c´alculos que se van haciendo si se asignan a variables permanecen en la memoria de trabajo, sino se asignan son eliminadas permaneciendo solo en memoria el ´ultimo resultado almacenado en una variable denominada `ans` . Por ejemplo la instrucci´on siguiente genera un vector fila pero al no estar asignado solo queda en memoria bajo la variable `ans` . 



Si a continuaci´on emito otra instrucci´on pierdo el resultado anterior, salvo que previamente lo haya almacenado en una variable, como por ejemplo 

###### `b = ans` 

Si hacemos `who` podemos ver las variables en memoria hasta el momento almacenadas y si hacemos `whos` podemos ver m´as detalles de las mismas. 

Como es sabido del algebra lineal una matriz puede generarse como el producto tensorial de vectores. Por ejemplo si en el caso anterior hacemos 

###### `A1 = c*b` 

el resultado es una matriz de 3 _×_ 3 porque es el producto de un vector de 3 _×_ 1 por otro de 1 _×_ 3. En este caso el resultado ser´a: 



**64** 

[Document version: curso-0.3.0. File version: $Id: tp2.tex,v 1.2 2003/04/20 10:14:34 mstorti Exp $] 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.6. Condiciones de contorno e iniciales_ 

Del mismo modo podemos definir el producto interno entre vectores de una forma trivial. La definici´on de producto interno es: 



En este caso si hacemos 

```
b*c
```

obtenemos el producto interno anterior y tal como hemos definido la instrucci´on no est´a alojado en ninguna variable por lo cual corre peligro de ser destruido despu´es de la pr´oxima instrucci´on. 

Otro aspecto importante es que existen formas de generar matrices muy especiales. Por ejemplo 

- `ones(10)` genera una matriz de (10 _×_ 10) con elementos unitarios. 

- `ones(10,3)` genera una matriz de (10 _×_ 3) con elementos unitarios. 

- `zeros(5,3)` genera una matriz de (5 _×_ 3) con elementos nulos. 

- `(-3:2:15)` genera un vector fila cuyo primer elemento es _−_ 3, generando el resto avanzando de a 2 y no supera el valor 15. 

Otra forma ser´ıa 

###### `kron((1:3)’,(2:5))` 

que produce el producto tensorial del vector columna `(1:3)’` con el vector fila `(2:5)` , lo cual arroja la siguiente matriz como resultado 



Existen muchas otras formas, por ejemplo: 

- `rand(4)` produce una matriz de (4 _×_ 4) con n´umeros aleatorios 

- `eye(5)` produce la matriz identidad de (5 _×_ 5) 

- `diag(v,idiag)` produce una matriz poniendo el vector `v` en la codiagonal `idiag` , determinando el tama˜no de la matriz la longitud del vector v y la codiagonal en la cual se ubica, ya que debe entrar el vector entero en ella. Por ejemplo si el vector es de (5 _×_ 1) y lo queremos ubicar en la segunda codiagonal entonces la matriz ser´a de (7 _×_ 7) y tendr´a la siguiente forma: 

```
>>diag(ones(5,1),2)
```

```
ans=
```



**65** 

[Document version: curso-0.3.0. File version: $Id: tp2.tex,v 1.2 2003/04/20 10:14:34 mstorti Exp $] 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.6. Condiciones de contorno e iniciales_ 

|`0`|`0`|`0`|`0`|`1`|`0`|`0`|
|---|---|---|---|---|---|---|
|`0`|`0`|`0`|`0`|`0`|`1`|`0`|
|`0`|`0`|`0`|`0`|`0`|`0`|`1`|
|`0`|`0`|`0`|`0`|`0`|`0`|`0`|
|`0`|`0`|`0`|`0`|`0`|`0`|`0`|



Si no especificamos la codiagonal asume un valor cero lo cual significa la propia diagonal y si especificamos un valor negativo asume las codiagonales inferiores en lugar de las superiores. Es importante resaltar que si el argumento del comando `diag` es una matriz entonces devuelve la diagonal o la codiagonal de la misma como un vector. Vea el help ( `help diag` ). 

A esta altura debemos asegurarnos de salvar lo hecho por si ocurriera alg´un imprevisto o por si tuvi´eramos que detener temporariamente nuestro trabajo. El comando `save` salva las variables en memoria en un archivo. Si omitimos el nombre (solo invocamos el comando `save` ) guarda el contenido de la memoria en un archivo llamado `matlab.mat` , caso contrario, si especificamos el nombre , por ejemplo `save tempo` , guarda la memoria entera en el archivo `tempo.mat` Tambien podemos guardar parte de la memoria, para ello debemos invocar `save <filename> variables` . 

Cuando uno desea continuar con el trabajo interrumpido y quiere recuperar la memoria salvada con el comando `save` debe ejecutar `load <filename>` o simplemente `load` si salv´o las variables sin especificar el fichero. 

Con `clear` se limpia todo el espacio de trabajo (memoria) y con `clear variables` aquellas variables que uno desea. 

Con `size(<arreglo>)` o `length(<arreglo>)` se puede obtener la dimensi´on del arreglo. El primer caso es general y devuelve dos valores mientras que el segundo es exclusivamente para vectores y devuelve solo un valor. 

El software contiene una serie de operadores de matrices tal como suma, resta, producto, potencia, divisi´on por derecha e izquierda, etc. Todos estos operadores se definen tal como lo establece el ´algebra de los espacios vectoriales. Una aclaraci´on va con la divisi´on. 

Que significa dividir matrices para MatLab? 

Sean _A, B_ dos matrices de ( _m × m_ ), entonces 



Como vemos la divisi´on involucra matrices inversas, pero especial cuidado hay que tener cuando tratamos grandes matrices ya que el tiempo de c´alculo se achica mucho en estos casos con los comandos de divisi´on comparado al comando de inversi´on `inv(A)` o _A_<sup>_−_1</sup> 

Otro detalle interesante en el manipuleo de matrices es que uno puede extraer submatrices de otras matrices o armar matrices con bloques de otras submatrices. Por ejemplo, 

```
>>A=eye(4);
>>B=ones(4,2);
>>C=zeros(2,4);
>>D=eye(2);
```

```
>>E=[AB;CD]
```

[Document version: curso-0.3.0. File version: $Id: tp2.tex,v 1.2 2003/04/20 10:14:34 mstorti Exp $] 

**66** 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.6. Condiciones de contorno e iniciales_ 

###### `ans =` 

|`1`|`0`|`0`|`0`|`1`|`1`|
|---|---|---|---|---|---|
|`0`|`1`|`0`|`0`|`1`|`1`|
|`0`|`0`|`1`|`0`|`1`|`1`|
|`0`|`0`|`0`|`1`|`1`|`1`|
|`0`|`0`|`0`|`0`|`1`|`0`|
|`0`|`0`|`0`|`0`|`0`|`1`|



Del mismo modo podemos tomar un bloque de la matriz _E_ , por ejemplo el de las filas 1,3,5 con las columnas 2,3 haciendo: 

###### `E([1;3;5],[2;3])` 

En cuanto a las capacidades de c´alculo adem´as de existir toda una gama de funciones standard para escalares existen otras m´as para vectores y matrices. Por ejemplo es muy com´un hablar del seno trigonom´etrico de un n´umero real. Como se calcula el seno de una matriz? 

Bueno existen varias formas de calcularlo pero hay que tener cuidado al hacerlo con MatLab. 

Si nosotros definimos por ejemplo una matriz _A_ de (3 _×_ 3) y ejecutamos la instrucci´on `sin(A)` el resultado ser´a diferente a si nosotros usamos la definici´on de una funci´on aplicada a una matriz 



donde _V_ es la matriz de autovectores y Λ es la matriz diagonal con los autovalores en la diagonal. En este caso 



###### Donde est´a la diferencia? 

La diferencia est´a en que MatLab soporta otro tipo de operadores adem´as de los standard para matrices, llamados operadores de arreglos. Sin entrar por ahora en detalles porque lo abordaremos m´as adelante, un operador de arreglo realiza una operaci´on sobre cada elemento del arreglo como si fuera una lista de elementos. Entonces si a MatLab le decimos `B = sin(A)` ´el entiende: 



Conclusi´on, cuando queremos realizar una funci´on especial sobre una matriz debemos o realizar la descomposici´on en autovalores y autovectores utilizando la funci´on de MatLab `eig(A)` o sino usar otra funci´on llamada `funm` que en este caso se usa de la siguiente forma : `funm(A,’sin’)` . 

MatLab soporta muchas funciones para matrices, por ejemplo: 

c´alculo de determinantes _→_ `det` 

c´alculo de autovalores _→_ `eig` 

c´alculo de la traza _→_ `trace` 

c´alculo del n´umero de condici´on _→_ `cond` 

**67** 

[Document version: curso-0.3.0. File version: $Id: tp2.tex,v 1.2 2003/04/20 10:14:34 mstorti Exp $] 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.6. Condiciones de contorno e iniciales_ 

- c´alculo de la norma _→_ `norm` 

- c´alculo del rango _→_ `rank` 

- factorizaci´on Choleski _→_ `chol` 

- factorizaci´on LU _→_ `lu` 

- ortogonalizaci´on _→_ `orth` 

entre otras. 

_Consulte el help de matrices._ 

###### **Matrices como listas y tablas** 

Las matrices tambi´en pueden ser interpretadas como listas o tablas de datos. Reci´en hab´ıamos mencionado que hay que tener cuidado en el uso de MatLab cuando se aplican funciones a matrices porque su resultado puede ser diferente al esperado. Esto se debe a que como dijimos una matriz puede ser una matriz en el sentido estricto o una lista o una tabla. En el caso de listas son como elementos independientes sobre los cuales se pueden aplicar operaciones individualmente con el fin de obtener alg´un resultado espec´ıfico. Por ejemplo, una matriz puede representar la distribuci´on de temperatura en un dominio rectangular o mapeable a un rect´angulo, donde cada elemento de la matriz puede equivaler a un punto de esa grilla rectangular. Entonces planteando operaciones sobre ellos podemos lograr efectos interesantes. 

Por ejemplo sea una matriz _A_ de ( _m × n_ ) elementos. Haciendo: 

`diff A` _⇒ Bi,j_ = _Ai,j_ +1 _− Ai,j_ 

_<u>∂A</u>_ `gradient A` _⇒_ � _∂x_<sup>_,_</sup><sup>_<u>∂A</u>_</sup> _∂y_ � 

`interp2 A` interpolaci´on de datos en 2D 

Del mismo modo dado un conjunto de datos en forma de lista en 1,2 o 3 dimensiones, podemos aplicarle ciertas operaciones e incluso visualizar usando instrucciones gr´aficas. 

En el caso de tablas se puede pensar a una matriz como una planilla de c´alculo y realizar toda una serie de an´alisis estad´ısticos sobre los mismos y calcular promedios, dispersiones, histogramas, sumas y productos acumulados, medianas, etc. 

Es importante a esta altura resaltar que existen operaciones sobre arreglos del mismo modo que existen operaciones sobre matrices. Por ejemplo para multiplicar matrices simplemente invocamos el s´ımbolo del producto. Si queremos multiplicar arreglos esto se entiende como un producto elemento a elemento en forma individual. Por ejemplo, sean _A_ y _B_ dos arreglos, entonces el producto de arreglo se define como: 



Para poder diferenciar esto de la habitual multiplicaci´on de matrices MatLab soporta las operaciones precedidas por un punto. 

Por ejemplo 

**68** 

[Document version: curso-0.3.0. File version: $Id: tp2.tex,v 1.2 2003/04/20 10:14:34 mstorti Exp $] 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.6. Condiciones de contorno e iniciales_ 

- `.*` equivale al producto de arreglos 

- `./` equivale al cociente de arreglos 

- `.^n` equivale a elevar todos los coeficientes del arreglo a una potencia `n` 

###### **Visualizaci´on gr´afica** 

El hecho de permitir un manejo de matrices como si fuera una lista de datos ordenados seg´un la estructura de la matriz o como una tabla de valores permite altas facilidades de graficaci´on. 

Visite el help de los comandos `plot` , `mesh` , `surf` , etc para ver todas las capacidades gr´aficas que ofrece MatLab. 

###### **Programaci´on** 

Finalmente cerramos este breve paseo con otra facilidad muy importante a la hora de pretender ir un poco m´as alla de lo que ofrece MatLab. Programando en MatLab es posible generar programas de prop´ositos particulares o generales, como por ejemplo construir un generador de mallas, mejores formas de visualizar soluciones, visualizar mallas de elementos finitos, generar un programa de alg´un m´etodo num´erico, etc. Aqu´ı˜no entraremos en detalle de los aspectos de programaci´on. Para aquellos intersados visitar el help o la bibliograf´ıa especializada. 

- **[Ejercicio 1.]** Dadas las grandes capacidades que tiene Matlab para el tratamiento de matrices uno de los principales objetivos es aprender como manipularlas. Existen muchas formas de ingresar matrices. En este ejemplo se pretende que Ud explore diferentes formas de hacerlo. Por ejemplo, dada la siguiente matriz de (10 _×_ 10) con los siguientes elementos: 

||<br>2|_−_1|0|0|0|0|0|0|0|0<br>||
|---|---|---|---|---|---|---|---|---|---|---|---|
||<br>_−_1|2|_−_1|0|0|0|0|0|0|0<br><br>||
||<br><br><br>0|_−_1|2|_−_1|0|0|0|0|0|0<br><br><br><br>||
||<br><br><br>0|0|_−_1|2|_−_1|0|0|0|0|0<br><br><br><br>||
|**A**=<br><br><br>|<br><br><br>0|0|0|_−_1|2|_−_1|0|0|0|0<br><br><br>|(333)|
|<br><br><br>|<br><br><br>0|0|0|0|_−_1|2|_−_1|0|0|0<br><br><br>|.|
||<br><br><br>0|0|0|0|0|_−_1|2|_−_1|0|0<br><br><br>||
||<br><br><br>0|0|0|0|0|0|_−_1|2|_−_1|0<br><br><br>||
||<br><br>0|0|0|0|0|0|0|_−_1|2|_−_1<br><br>||
||0|0|0|0|0|0|0|0|_−_1|1<br>||



explique una forma sencilla de cargarla sin necesidad de entrar cada uno de los 100 coeficientes que la conforman. 

A continuaci´on calcule: 

- 1.- la traspuesta 

- 2.- el producto consigo misma 

- 3.- su raiz cuadrada 

[Document version: curso-0.3.0. File version: $Id: tp2.tex,v 1.2 2003/04/20 10:14:34 mstorti Exp $] 

**69** 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.6. Condiciones de contorno e iniciales_ 

- 4.- sume la matriz identidad del mismo orden 

**[Ejercicio 2.]** A continuaci´on se desea armar una matriz como la siguiente: 



donde **A** es la matriz del ejemplo anterior. Muestre una forma sencilla de hacerlo. 

- **[Ejercicio 3.]** Tome la matriz del ejemplo 2 y arme una nueva matriz de 3 _×_ 2 que contenga los elementos de las filas 1,3,5 y columnas 2,4 de la matriz **B** . 

- **[Ejercicio 4.]** Se sabe de la necesidad de contar con un buen manipulador de matrices a la hora de resolver problemas de ´algebra lineal. Un ejemplo de ello es la resoluci´on de sistemas de ecuaciones. Sea la matriz del ejemplo 1 y un vector miembro derecho **b** que representa la funci´on _sin_ ( _π/_ 2 _∗ x_ ) donde _x_ es un vector de 10 componentes cuyos valores var´ıan entre 0 y 1. Resolver el sistema **Au** = **b** . Grafique la soluci´on **u** y el vector **b** en la misma figura. 

- **[Ejercicio 5.]** Calcule el determinante de la matriz anterior **A** del ejemplo 1 y sus autovalores. A continuaci´on grafique los autovalores en el plano complejo. Posteriormente ingrese la matriz 



calcule el determinante y sus autovalores y muestre su distribuci´on en el plano complejo. Use el comando `spy(A)` y `spy(C)` y explique que es lo que hace. 

- **[Ejercicio 6.]** Para las matrices **A** y **C** de los ejemplos anteriores calcule la soluci´on del sistema lineal ( **A** + **C** ) **u** = **b** con el miembro derecho similar al usado en el Ej. 4. Grafique la soluci´on. A continuaci´on resuelva el sistema( **A** + 10 **C** ) **u** = **b** y grafique la soluci´on. 

- **[Ejercicio 7.]** Dada las matrices 



**70** 

[Document version: curso-0.3.0. File version: $Id: tp2.tex,v 1.2 2003/04/20 10:14:34 mstorti Exp $] 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.6. Condiciones de contorno e iniciales_ 

generar con Matlab la matriz 



y extraiga de la matriz _C_ aquella correspondiente a las filas 2 y 3 y columnas 5,8,11,12 y muestre su estructura. 

- **[Ejercicio 8.]** Dado el vector _x_ = _j_<sup>2</sup> _, j_ = 1 _, . . . ,_ 10 y el vector _y_ = _j_<sup>3</sup> _, j_ = _−_ 3 _, . . . ,_ 3, calcule el producto tensorial de ambos vectores y muestre la matriz obtenida con el producto tensorial en forma gr´afica. _Ayuda:_ La matriz es tal que sus elementos se calculan de la siguiente forma: 



y una forma de graficarla es mediante el comando `mesh` 

A continuaci´on genere una grilla en 2D con _x ∈_ ( _−_ 2 _,_ 2) y _y ∈_ (0 _,_ 3) y calcule la funci´on _z_ = _x_<sup>2</sup> +<sup>_√_</sup> _<u>y</u>_ y grafique la soluci´on. _Ayuda:_ Explore el comando `meshgrid` 

- **[Ejercicio 9.]** Confeccione un programa en Matlab que realice el producto vectorial de vectores en tres dimensiones. Pru´ebelo con un ejemplo no trivial. Exti´endalo al caso de varios vectores. Para esto utilice primero un archivo tipo script y luego uno tipo funci´on. Si no recuerda las diferencias entre ambos revise las notas entregadas (Primer de Matlab). 

- **[Ejercicio 10.]** Confeccione un programa en Matlab que resuelva la siguiente ecuaci´on diferencial ordinaria usando la funci´on `ode23` y `ode45` , 





**[Ejercicio 11.]** Resuelve el siguiente sistema no lineal de ecuaciones 





usando como estimaci´on inicial 







utilizando la funci´on de Matlab `fsolve` o `fsolve2` 

**[Ejercicio 12.]** Construya un polinomio de cuarto orden 



y encuentre las raices del mismo usando un conjunto de coeficientes _ai_ a elecci´on. Grafique el polinomio en el rango donde se hallan todas sus raices. 

**71** 

[Document version: curso-0.3.0. File version: $Id: tp2.tex,v 1.2 2003/04/20 10:14:34 mstorti Exp $] 

Cap´ıtulo 3. Naturaleza matem´atica de las ecuaciones _Secci´on 3.6. Condiciones de contorno e iniciales_ 

- **[Ejercicio 13.]** Utilice las rutinas del proyecto sobre sistemas din´amicos masa resorte amortiguador para el caso de 1 grado de libertad lineal y verifique el valor del amortiguamiento cr´ıtico del sistema. 

- **[Ejercicio 14.]** Genere una aplicaci´on para resolver el ejemplo del p´endulo doble y trate de animar el movimiento del sistema 

**72** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

## **Cap´ıtulo 4** 

# **M´etodo de diferencias finitas** 

#### **4.1. Diferencias finitas en 1D** 

Queremos resolver el campo de temperaturas a trav´es de una pared de material ( _−∞≤ y, z ≤_ + _∞_ , 0 _≤ x ≤ Lx_ ). La temperatura en _x_ = 0 _, Lx_ es mantenida a _φ_<sup>¯</sup> 0, _φ_<sup>¯</sup> _Lx_ y hay una fuente de calor repartida _Q_ ( _x_ ): 



Dividimos el intervalo en _L_ segmentos de longitud ∆ _x_ = _Lx/L_ y llamaremos _“nodos”_ o _“puntos de la grilla”_ a los extremos de los segmentos: 



##### **4.1.1. Desarrollo en Serie de Taylor** 

Si bien la ecuaci´on que debemos resolver es de segundo orden, empezaremos, por simplicidad, por desarrollar aproximaciones en diferencias para la derivada de primer orden, 



Indicando _fl_ = _f_ ( _xl_ ) para cualquier funci´on _f_ ( _x_ ), tenemos: 



Donde el sub´ındice _l_ + _θ_ 1 es una extensi´on de la notaci´on que indica evaluaci´on en ( _l_ + _θ_ 1)∆ _x_ . Despejando la derivada de primer orden: 



73 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.1. Diferencias finitas en 1D_ 



<!-- Start of picture text -->
C<br>φ l+1 B<br>φ l<br>D A<br>φ l-1<br>xl-1 xl xl+1<br>xl-1 xl xl+1<br><!-- End of picture text -->

Figura 4.1: Interpretaci´on geom´etrica de las diferentes aproximaciones por diferencias finitas a la derivada. 

A esta aproximaci´on para la derivada de primer orden la llamamos _“por diferencia hacia adelante”_ ( _forward difference_ ): 



V´ease la figura 4.1 para una interpretaci´on gr´afica de esta aproximaci´on. Hemos aproximado la derivada en el punto _xl_ por la pendiente de la secante a la curva que pasa por los puntos _xl_ y _xl_ +1 (segmento _AC_ ). El error de esta aproximaci´on es: 



Similarmente, la aproximaci´on hacia atr´as ( _“backward difference”_ )da: 



[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.1. Diferencias finitas en 1D_ 

que corresponde a la pendiente del segmento _DA_ en la figura. 

##### **4.1.2. Aproximaciones de mayor orden** 

Haciendo desarrollos de mayor orden: 



de donde: 



que corresponde al segmento _DC_ de la figura 4.1. La correspondiente estimaci´on del error es: 



A esta la llamamos una _“aproximaci´on centrada”_ , ya que involucra a los dos nodos vecinos del nodo _l_ . Notar que, al contrario de las otras, esta es sim´etrica con respecto al punto en cuesti´on. Notar tambi´en que el error resulta ser un orden mayor. Con lo cual en principio se pueden obtener mejores aproximaciones con menos puntos usando un aproximaci´on de mayor orden como esta. Pero, como veremos m´as adelante, en la secci´on _§_ 4.1.7, el hecho de que la aproximaci´on sea de un mayor orden no es una condici´on _“suficiente”_ para obtener un orden de convergencia mayor. 

##### **4.1.3. Aproximaci´on de derivadas de orden superior** 

Para obtener una estimaci´on de la derivada segunda comenzamos haciendo una expansi´on hasta cuarto orden de _φl±_ 1: 

de donde: 



o sea que: 





Esta es una _“aproximaci´on centrada”_ . 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

**75** 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.1. Diferencias finitas en 1D_ 

##### **4.1.4. N´umero de puntos requeridos** 

Nos cuestionamos cuantos puntos son necesarios para obtener una aproximaci´on de un dado orden (digamos _O_ (∆ _x_ )) para una derivada de orden _k_ . Por ejemplo para obtener una aproximaci´on a la derivada primera es obvio que necesitamos al menos dos puntos ya que por dos puntos pasa una recta y la recta es el polinomio de bajo orden que posee una derivada de primer orden no nula. El mismo razonamiento nos dice que se necesitan tres puntos para aproximar una derivada segunda. Por otra parte, parece tambi´en obvio que si queremos una aproximaci´on de mayor orden entonces necesitaremos m´as puntos. La expresi´on que relaciona 

- _N_ el n´umero de puntos, 

- _p_ la precisi´on del m´etodo y 

- _k_ el orden de la derivada a aproximar, 

es 





Es decir, con _N_ puntos o m´as podemos desarrollar una aproximaci´on de orden _p_ (es decir _|E| ≤ C_ ∆ _x_<sup>_p_</sup> ) para �d<sup>_k_</sup> _φ/_ d _x_<sup>_k_�</sup> . Verificamos esto en los desarrollos anteriores, 

|**Tipo de aproximaci´on**|(precisi´on)|(orden de la deriva-<br>da)|Nro. de puntos utili-<br>zados|(nro. de puntos re-|queridos de acuerdo|a (4.17))|
|---|---|---|---|---|---|---|
|hacia atr´as/adelante|1|1|2||2||
|centrada|2|1|3||3||
|centrada|2|2|3||4||



Cuadro 4.1: Tabla N´umero de puntos utilizados en las diferentes aproximaciones por diferencias utilizadas. 

##### **4.1.5. Soluci´on de la ecuaci´on diferencial por el m´etodo de diferencias finitas** 

Consideremos primero, por simplicidad, el caso de condiciones Dirichlet _φ_ (0) = _φ_<sup>¯</sup> 0, _φ_ ( _Lx_ ) = _φ_<sup>¯</sup> _Lx_ . Evaluando la ecuaci´on diferencial en _xl_ : 



y aproximando la derivada segunda por diferencias finitas de segundo orden centradas: 



[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.1. Diferencias finitas en 1D_ 

hay una ecuaci´on para cada _l_ = 1 _,_ 2 _, . . . , L −_ 1, que son los _puntos interiores_ . Concretamente, las ecuaciones resultan ser: 



Definiendo un vector de inc´ognitas **_φ_** , que contiene s´olo los nodos interiores: 



Tenemos el siguiente sistema de ecuaciones: 

###### **K** **_φ_** = **f** 



con: 



N´otese la analog´ıa: 



El operador del continuo �d<sup>2</sup> _/_ d _x_<sup>2�</sup> es reemplazado por la matriz **K** , el campo del continuo _φ_ es reemplazado por el conjunto de valores nodales **_φ_** y, finalmente, la fuente interna _Q_ ( _x_ ) es reemplazada 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

**77** 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.1. Diferencias finitas en 1D_ 



Figura 4.2: Problema unidimensional con condiciones de contorno Dirichlet en ambos extremos 

por el vector miembro derecho **f** . A su vez, la condiciones de contorno tipo Dirichlet tambi´en generan un t´ermino en el miembro derecho. 

La matriz **K** es sim´etrica ( _Kij_ = _Kji_ para todos _i, j_ ) y definida postitiva ( **v**<sup>_T_</sup> **Kv** _>_ 0 para todo **v** _∈_ IR<sup>_L−_1</sup> ). Esto tiene mucha importancia: se puede demostrar la existencia y unicidad de la soluci´on discreta y adem´as tiene importancia pr´actica ya que permite el desarrollo de rutinas de resoluci´on especialmente dise˜nadas. 

##### **4.1.6. Ejemplo** 

Resolver: 



Usaremos ∆ _x_ =<sup>1</sup> _/_ 3 (ver figura 4.2). Tenemos 4 valores nodales _φ_ 0, _φ_ 1, _φ_ 2 y _φ_ 3, de los cuales _φ_ 0 y _φ_ 3 son conocidos de las condiciones de contorno y s´olo restan dos inc´ognitas _φ_ 1 y _φ_ 2. La ecuaci´on en los nodos interiores es: 



para: 



pero _φ_ 0 = 0 por la condici´on de contorno, de manera que la ecuaci´on resultante es: 



Para _l_ = 2 la ecuaci´on resultante es: 



Resolviendo el sistema (4.29-4.30) obtenemos: 



La soluci´on exacta a este problema puede ser encontrada f´acilmente. Proponiendo soluciones de la forma _e_<sup>_−αx_</sup> , se obtiene la ecuaci´on caracter´ıstica _α_<sup>2</sup> = 1 de donde _α_ = _±_ 1. Proponemos entonces 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

**78** 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.1. Diferencias finitas en 1D_ 

||Exacta||∆_x_= 1_/_3||∆_x_= 1_/_6|
|---|---|---|---|---|---|
|_x_|_φ_|_φ_|Error|_φ_|Error|
|1/3.|0.28892|0.28929|3_,_6_×_10<sup>_−_4</sup> (0.12 %)|0.28901|9_,_2_×_10<sup>_−_5</sup> (0.032 %)|
|2/3|0.61024|0.61071|4_,_7_×_10<sup>_−_4</sup> (0.077 %)|0.61036|1_,_2_×_10<sup>_−_4</sup> (0.019 %)|



Cuadro 4.2: Tabla : Errores para _φ_<sup>_′′_</sup> _− φ_ = 0 _, φ_ (0) = 0 _, φ_ (1) = 1, para ∆ _x_ =<sup>1</sup> _/_ 3 _,_<sup>1</sup> _/_ 6 

soluciones de la forma _φ_ = _ae_<sup>_x_</sup> + _be_<sup>_−x_</sup> . _a_ y _b_ se obtienen de imponer las condiciones de contorno, y resulta ser: 



Los resultados num´ericos y exactos son comparados en la tabla 4.2, se incluyen tambi´en los resultados obtenidos para ∆ _x_ =<sup>1</sup> _/_ 6: 

N´otese que tanto en _x_ =<sup>1</sup> _/_ 3 como en _x_ =<sup>2</sup> _/_ 3 el error ha bajado en un factor<sup>1</sup> _/_ 4 al reducir el paso de la malla en un factor<sup>1</sup> _/_ 2. Primero vemos que, cualitativamente, el esquema de discretizaci´on es _convergente_ , es decir el error, en alguna norma predeterminada, se reduce, al reducir el paso de la malla. Cuantitativamente, podemos decir que el error tiene un comportamiento _∝_ ∆ _x_<sup>2</sup> . Tambien se dice que el _“orden de convergencia”_ es _∝ h_<sup>2</sup> , donde _h_ representa el paso de la malla (∆ _x_ en nuestro caso). Esto es consistente con el error de truncamiento que encontramos en el desarrollo de Taylor usado. 

##### **4.1.7. An´alisis de error. Teorema de Lax** 

Si denotamos por **_φ_** ex los valores nodales de la soluci´on exacta, es decir 



entonces **_φ_** ex satisface (4.19) pero con un error de truncamiento, es decir 



donde _E_ trunc _,l_ es el error correspondiente a la ecuaci´on _l_ -´esima. Sabemos que el error de truncamiento es _O_ (∆ _x_ )<sup>2</sup> , y tenemos, en forma matricial 



Restando (4.22) de (4.35) obtnemos una ecuaci´on para el error **E** _φ_ = **_φ_** _−_ **_φ_** ex en los valores nodales 



y entonces, 



Al hecho de que el error de truncamiento _E_ trunc _,i →_ 0 para ∆ _x →_ 0 lo llamamos _“consistencia”_ del m´etodo. Queremos saber bajo que condiciones, el esquema es _“convergente”_ , es decir _∥_ **E** _φ∥→_ 0 para 

**79** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.1. Diferencias finitas en 1D_ 

∆ _x →_ 0. Por lo que vemos, esto est´a relacionado con alguna propiedad de **K** , es decir que de alguna forma la inversa de **K** “se mantenga acotada”, para ∆ _x →_ 0. 

Tomando normas 



Recordemos que la norma (Eucl´ıdea) de un vector est´a definida como 



y la norma de una matriz est´a definida como el m´aximo autovalor de la misma. Puede verse entonces que _∥_ **K**<sup>_−_1</sup> _∥_ es la inversa del m´ınimo autovalor de **K** , y usando (4.12) 



de manera que 



EL miembro izquierdo de esta ecuaci´on representa el _“error cuadr´atico medio”_ de la soluci´on num´erica. Esta expresi´on nos dice que este error es del mismo orden que el error de truncamiento, con la condici´on de que _λ_ min se mantenga acotado (es decir, que no tienda a cero) cuando ∆ _x_ tiende a cero. Si se cumple esta condici´on decimos que la discretizaci´on es _“estable”_ . Entonces, la condici´on para la convergencia es 

Consistencia + Estabilidad = _⇒_ Convergencia (4.44) 

Este resultado es conocido como _Teorema de Lax_ y es la base del an´alisis de error para el m´etodo de diferencias finitas. 

##### **4.1.8. Condiciones de contorno tipo Neumann (“flujo impuesto”)** 

El problema a resolver es: 







[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

**80** 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.1. Diferencias finitas en 1D_ 

||Exacta|∆|_x_= 1_/_3|∆|_x_= 1_/_6|
|---|---|---|---|---|---|
|_x_|_φ_|_φ_|Error|_φ_|Error|
|1/3|0.2200|0.2477|0.0277 (12 %)|0.2340|0.0140 (6 %)|
|2/3|0.4648|0.5229|0.0582 (12 %)|0.4942|0.0294 (6 %)|
|1|0.7616|0.8563|0.0947 (12 %)|0.8097|0.0481 (6 %)|



Cuadro 4.3: Tabla : Errores para _φ_<sup>_′′_</sup> _− φ_ = 0 _, φ_ (0) = 0 _, φ_<sup>_′_</sup> (1) = 1, para ∆ _x_ =<sup>1</sup> _/_ 3 _,_<sup>1</sup> _/_ 6 

Ahora _φL_ pasa a ser una inc´ognita m´as: 



Para determinar esta inc´ognitas tenemos _L −_ 1 ecuaciones que provienen de aproximar el operador diferencial por diferencias finitas de segundo orden en puntos interiores como en la ecuaci´on (4.19). Para dar cuenta de la condici´on de contorno tipo Neumann en _Lx_ agregamos la siguiente aproximaci´on: 



Ahora s´ı, tenemos _L_ ecuaciones en _L_ inc´ognitas. Volviendo al ejemplo anterior del problema (4.26), pero ahora con condici´on de tipo Neumann en _x_ = 1: _φ_<sup>_′_</sup> (1) = 1 el sistema resultante es: 



Resolviendo el sistema, se encuentran los valores discretos que pueden observarse en la tabla 4.3. (se incluyen tambi´en los resultados obtenidos para ∆ _x_ =<sup>1</sup> _/_ 6): 

La soluci´on exacta puede obtenerse de la misma forma que en el caso Dirichlet y resulta ser: 



Notamos que los errores resultan ser notablemente mayores que en el caso Dirichlet puro, concretamente son dos ´ordenes de magnitud mayores. Un indicio de la causa del problema la da el hecho de que, al reducir el paso de la malla a la mitad, el error no ha bajado en un factor<sup>1</sup> _/_ 4 como antes, sino que apenas ha bajado un factor<sup>1</sup> _/_ 2, exhibiendo una convergencia _∝_ ∆ _x_ . La causa es que hemos usado una expansi´on orden _O_ (∆ _x_ ) para la condicion de Neumann, ecuaci´on (), si bien la expansi´on en los nodos interiores es _O_ (∆ _x_<sup>2</sup> ). Podemos deducir una regla muy importante que es que _el orden de convergencia est´a dictado por el m´as bajo orden de las expansiones utilizadas, tanto para el interior del dominio como para las condiciones de contorno_ . 

**81** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.1. Diferencias finitas en 1D_ 



<!-- Start of picture text -->
x=0 x=L<br>nodo ficticio<br>dominio "real"<br>x1 x2 x3 xL-1 xL xL+1<br><!-- End of picture text -->

Figura 4.3: Inclusi´on de un nodo ficticio para obtener una discretizaci´on m´as precisa de la condici´on de contorno tipo Neumann. 

En consecuencia, si queremos recuperar el orden de convergencia _∝_ ∆ _x_<sup>2</sup> , necesariamente debemos desarrollar una aproximaci´on _O_ (∆ _x_<sup>2</sup> ) para la condici´on tipo Neumann. Una forma de hacer esto es introduciendo un _“nodo ficticio”_ (ver figura 4.3) _xL_ +1 y aproximando la condici´on de contorno como: 



Pero hemos introducido una inc´ognita m´as: _φL_ +1, de manera que agregamos la ecuaci´on para nodos interiores en el nodo de contorno _L_ : 



El sistema es: 





[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

**82** 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.1. Diferencias finitas en 1D_ 



Figura 4.4: Malla 1D con ∆ _x_ =<sup>1</sup> _//_ 3 _._ y un nodo ficticio. 

||Exacta||∆_x_= 1_/_3||∆_x_= 1_/_6|
|---|---|---|---|---|---|
|_x_|_φ_|_φ_|Error|_φ_|Error|
|1/3|0.2200|0.2168|0.0033 (1.5 %)|0.2192|0.0008 (0.4 %)|
|2/3|0.4648|0.4576|0.0071 (1.5 %)|0.4629|0.0018 (0.4 %)|
||0.7616|0.7493|0.0123 (1.6 %)|0.7585|0.0031 (0.4 %)|



Cuadro 4.4: Tabla : _Errores para φ_<sup>_′′_</sup> _− φ_ = 0 _, φ_ (0) = 0 _, φ_<sup>_′_</sup> (1) = 1 _, para_ ∆ _x_ =<sup>1</sup> _/_ 3 _,_<sup>1</sup> _/_ 6 _, con esquema O_ (∆ _x_<sup>2</sup> ) 

Volviendo al ejemplo de la ecuaci´on _φ_<sup>_′′_</sup> _− φ_ = 0 con condiciones _φ_ (0) = 0, _φ_<sup>_′_</sup> (1) = 1 y discretizado con ∆ _x_ =<sup>1</sup> _/_ 3 (ver figura 4.4), los resultados con este nuevo m´etodo pueden observarse en la tabla 4.4. 

El error es ahora un orden de magnitud menor y se recupera la convergencia cuadr´atica. Sin embargo el sistema ha dejado de ser sim´etrico. Para recuperar la simetr´ıa de la matriz del sistema, podemos obtener una ecuaci´on para _φL_ y _φL−_ 1, eliminando _φL_ +1 de las dos ´ultimas ecuaciones: 



N´otese que esta ecuaci´on es la misma que la (4.49) pero con el agregado del t´ermino ∆ _x_<sup>2</sup> _QL/_ 2 _k_ en el miembro derecho. De hecho, esta misma ecuaci´on puede obtenerse planteando un balance de energ´ıa en el intervalo [ _L −_ 1 _/_ 2 _, L_ ]∆ _x_ . El sistema total es: 



[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

**83** 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.2. Problemas no-lineales_ 



#### **4.2. Problemas no-lineales** 

Consideremos el siguiente problema uni-dimensional, no-lineal debido a la dependencia de _k_ con la temperatura: 



Mencionaremos a continuaci´on algunos otros problemas de la mec´anica del continuo que presentan no-linealidad: 

- _Material hiper´elastico: E_ = _E_ ( _ϵ_ ), _G_ = _G_ ( _ϵ_ ), coeficientes el´asticos dependientes de las deformaciones 

- _Flujo potencial subs´onico (compresible)_ : _∇·_ [ _ρ_ ( _|∇φ|_ ) _∇φ_ ] = 0, donde _φ_ es el potencial **v** = _∇φ_ , **v** =velocidad, _ρ_ =densidad. Aqu´ı _ρ_ juega el papel de la conductividad en el problema t´ermico. En contraste con ´aquel, _ρ_ depende de las derivadas de _φ_ , y no del valor de _φ_ . 

La regla en estos casos es diferenciar en forma _conservativa_ . Llamando _ψ_ al flujo: 



La ecuaci´on de balance para el nodo _l_ , puede ser escrita a segundo orden como: 



donde _ψl_ +1 _/_ 2 indica el valor de _ψ_ en nodos ubicados en el punto medio entre los nodos reales: _xl_ +1 _/_ 2 = ( _xl_ + _xl_ +1) _/_ 2. Una aproximaci´on de segundo orden para los flujos es: 



La ecuaci´on resultante para nodos interiores es: 



[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.2. Problemas no-lineales_ 

_x=0 x=L_ 



Figura 4.5: Balance global de calor para el problema unidimensional. 

Sumando sobre las ecuaciones sobre _l_ obtenemos un _principio de conservaci´on discreta_ : 



de all´ı viene el nombre de _“esquema conservativo”_ , ya que reproduce el balance de energ´ıa que satisface la ecuaci´on del continuo (ver figura 4.5): 



Esto es muy importante en problemas donde puede llegarse a esperar variaciones abruptas de las variables en intervalos muy peque˜nos, como es el caso de las _ondas de choque_ ( _“shock waves”_ ) en fluidos compresibles. 

El sistema de ecuaciones es ahora no-lineal: 



y no puede resolverse, en general, en forma cerrada, pero puede resolverse en forma aproximada generando una sucesi´on de valores **_φ_**<sup>0</sup> , **_φ_**<sup>1</sup> , _. . ._ , **_φ_**<sup>_n_</sup> , _. . ._ de tal forma que converja a la soluci´on exacta del sistema (4.69): 



Una forma apropiada de generar estas sucesiones es llevando el sistema anterior a una forma de _“punto fijo”_ : 



donde **O** es un mapeo de IR<sup>_L−_1</sup> en s´ı mismo, f´acilmente evaluable. Adem´as, debe elegirse un vector de inicializaci´on **_φ_**<sup>0</sup> y la secuencia se genera recursivamente como: 



En la pr´actica, esta forma de recurrencia es ejecutada un n´umero finito de iteraciones _N_ , de tal manera que **_φ_**<sup>_N_</sup> est´e suficientemente cerca de **_φ_** . Obviamente, como no conocemos **_φ_** , el criterio para detener el proceso iterativo, no puede basarse en una evaluaci´on directa de _∥_ **_φ_**<sup>_N_</sup> _−_ **_φ_** _∥_ . Aqu´ı, _∥_ **v** _∥_ = <u>�</u> _ni_ =1<sup>_v_</sup> _i_<sup>2</sup> ~~�~~ es la norma _L_ 2 del vector. Una posibilidad es analizar la diferencia entre dos iteraciones consecutivas de la sucesi´on: 



[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] **85** 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.2. Problemas no-lineales_ 

donde _ϵ_ es la _“tolerancia”_ deseada. Este criterio puede hacerse adimensional poniendo: 



Este criterio puede ser enga˜noso, por ejemplo, si la sucesi´on est´a convergiendo muy lentamente. Un criterio m´as robusto se basa en el _residuo_ del sistema de ecuaciones: 



donde el residuo **R** se define como: 



y el factor _∥_ **f** _∥_ en el denominador ha sido agregado para hacer el criterio adimensional. El valor de la tolerancia _ϵ_ , en ambos casos, depende de m´ultiples factores: 

- Obviamente, cuanto menor sea la tolerancia mayor es el costo computacional. La mayor´ıa de los m´etodos exhiben _convergencia lineal_ , de manera que veremos que el costo computacional es proporcional a log _ϵ_ . 

- Debido a errores de redondeo, es de esperarse que, ambos criterios no puedan bajar m´as all´a de un cierto valor _ϵ_ mach. Con esto queremos decir que _∥_ **R** ( **_φ_**<sup>_n_</sup> ) _∥ > ϵ_ mach para _n →∞_ , en vez de tender a cero, como ser´ıa en una m´aquina de precisi´on infinita. Para problemas bien condicionados, y si el criterio ha sido convenientemente adimensionalizado la precisi´on de la m´aquina est´a en _ϵ_ mach = 10<sup>_−_13</sup> _,_ 10<sup>_−_16</sup> , si todos los c´aculos se hacen en doble precisi´on. Si los c´aculos se hacen en simple precisi´on entonces la precisi´on cae a: _ϵ_ mach = 10<sup>_−_6</sup> _,_ 10<sup>_−_8</sup> . 

- Debe recordarse siempre que **_φ_** (la soluci´on exacta al problema discreto) posee un error debido a la discretizaci´on. Llamando **_φ_**<sup>_∗_</sup> a los valores nodales de la soluci´on del continuo, tenemos que: 



El error que interesa es el miembro izquierdo de esta desigualdad, es decir, el error con respecto a al soluci´on del continuo. El primer t´ermino del miembro derecho es el _error en la resoluci´on del sistema no-lineal_ , mientras que el segundo es el _error de discretizaci´on_ . A medida que se itera, el error de resoluci´on se va reduciendo, hasta anularse, en el l´ımite: 



Este expresi´on quiere decir que, por m´as que se itere, el error con respecto a la soluci´on exacta no va a bajar del error propio de discretizaci´on. De poder estimarse, el error de discretizaci´on, puede fijarse la tolerancia en una fracci´on (digamos<sup>1</sup> _/_ 10) del error de discretizaci´on. Poner una tolerancia m´as baja, aumenta el costo sin mejorar notablemente la soluci´on. 

**86** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.2. Problemas no-lineales_ 



<!-- Start of picture text -->
n = 0.3<br>f<br>0<br>x5x4 x3 x2 x1 x0 x<br>x6<br>0<br><!-- End of picture text -->

Figura 4.6: El esquema de punto fijo (4.79) aplicado a un problema undimensional con _k_ ( _φ_ ) = _φ_<sup>_−_0</sup><sup>_,_7</sup> . 

##### **4.2.1. Ejemplo** 

El esquema de iteraci´on puede ponerse simplemente como: 



La implementaci´on es muy simple. En la figura 4.6 vemos el esquema aplicado a la resoluci´on de una ecuaci´on unidimensional _k_ ( _φ_ ) _φ_ = _f_ , con _k_ ( _φ_ ) = _φ_<sup>_m_</sup> , _m_ = _−_ 0 _,_ 7 y _f_ = 1. N´otese que el esquema puede ser tambi´en puesto de la forma: 



Dado el valor de _φ_<sup>_j_</sup> , se puede obtener una pendiente aproximada entre el punto _Pj_ = ( _φ_<sup>_j_</sup> _, k_ ( _φ_<sup>_j_</sup> ) _φ_<sup>_j_</sup> ) y el origen _O_ . La intersecci´on de esta recta con _y_ = _f_ marca el nuevo punto _φ_<sup>_j_+1</sup> . El esquema es convergente si _k_ ( _φ_ ) _φ_ es mon´otona creciente. En caso contrario es divergente (ver figura 4.7, para el caso _m_ = _−_ 1 _,_ 5. Esta condici´on se cumple en muchos casos f´ısicos, ya que est´a asociado a una _condici´on de estabilidad_ del sistema. Pensemos por ejemplo en un resorte no-lineal, para el cual _k_ es la constante del resorte, _φ_ la elongaci´on y _f_ la fuerza aplicada. Entonces _k_ ( _φ_ ) _φ_ creciente quiere decir: _a mayor elongaci´on, mayor fuerza_ , lo cual coincide con el criterio de estabilidad. Sin embargo, la convergencia puede ser muy lenta, como por ejemplo en la figura 4.8, que corresponde a _m_ = _−_ 0 _,_ 9, _f_ = 1, _φ_ 0 = 3. 

**87** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.2. Problemas no-lineales_ 



<!-- Start of picture text -->
n =- 0.5<br>f<br>0<br>x0 x1 x2 x3 x<br>0<br><!-- End of picture text -->

Figura 4.7: Idem, para _k_ ( _φ_ ) = _φ_<sup>_−_1</sup><sup>_,_5</sup> . 

##### **4.2.2. M´etodo secante** 

Consideremos por simplicidad un problema de un s´olo grado de libertad: 



Supongamos que _φ_<sup>_j_</sup> est´a suficientemente cerca de la soluci´on _φ_ , de maner que podemos hacer un desarrollo de Taylor alrededor de _φ_ : 



pero _φ_ es un punto fijo de _O_ , de manera que _O_ ( _φ_ ) = _φ_ . Reemplazando en (4.81): 



Si _|O_<sup>_′_</sup> _| <_ 1 entonces podemos _φ_<sup>_j_+1</sup> estar´a todav´ıa m´as cerca de la soluci´on y podremos despreciar el t´ermino cuadr´atico para todo los _j_ . 



con _C_ = _|O_<sup>_′_</sup> _|_ . A este tipo de convergencia se le llama, “convergencia lineal”. Usando en forma recursiva esta relaci´on: 



[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.2. Problemas no-lineales_ 



<!-- Start of picture text -->
n = 0.1<br>f<br>0<br>x6x5 x4 x3 x2 x1 x0x<br>0<br><!-- End of picture text -->

Figura 4.8: Idem, para _k_ ( _φ_ ) = _φ_<sup>_−_0</sup><sup>_,_9</sup> . 

Adem´as, podemos poner: 



De manera que (4.85) puede ponerse como: 



Es com´un graficar log _|R|_ en funci´on de _j_ : 



De manera que, asint´oticamente, es una recta de pendiente log _C_ . Cuanto m´as peque˜no es _C_ , m´as empinada es la pendiente y se llega a una dada precisi´on con menos iteraciones. 

##### **4.2.3. M´etodo tangente** 

El sistema puede ser tambi´en puesto en forma de punto fijo como: 





[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.3. Precisi´on_ _<u>y</u> n´umero de_ _<u>puntos</u> en el esquema de diferencias finitas_ 

donde _J_ ( _φ_ ) se definir´a m´as adelante. La constante _C_ es, en este caso: 



En _φ_ vale que _R_ ( _φ_ ) = 0, de manera que: 



Si _J_ se parece mucho a _R_<sup>_′_</sup> entonces _C_ es muy peque˜no y la tasa de convergencia es muy alta. El caso ´optimo es poner _J_ = _R_<sup>_′_</sup> , en cuyo caso la convergencia deja de ser lineal y pasa a ser _“cuadr´atica”_ : 



La estimaci´on correspondiente para residuos es: 



Usando esta estimaci´on en forma recursiva: 













Esto es una exponencial cuando se grafica como log _R_ en funci´on de _j_ (ver figura 4.9). 

#### **4.3. Precisi´on y n´umero de puntos en el esquema de diferencias finitas** 

Ahora veremos como generar esquemas en diferencias de una forma general. Veremos que para una aproximaci´on para un cierto orden de derivaci´on se requiere un n´umero m´ınimo de puntos y que cada vez que querramos aumentar el orden de aproximaci´on, deberemos incrementar el n´umero de puntos en el stencil. 

Consideremos _N_ puntos arbitrarios _{xl}_<sup>_N_</sup> _l_ =1<sup>,yexpandamoslosvaloresde</sup><sup>_φl_=</sup><sup>_φ_(</sup><sup>_xl_)alrededorde</sup> un cierto punto _x_ 0 (que no necesariamente debe coincidir con uno de los _xl_ , _l ≥_ 1). 



[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.3. Precisi´on_ _<u>y</u> n´umero de_ _<u>puntos</u> en el esquema de diferencias finitas_ 



<!-- Start of picture text -->
convergencia lineal<br>convergencia cuadrática<br>n (iteraciones)<br>|Residuo|<br><!-- End of picture text -->

Figura 4.9: Tipos de convergencia lineal y cuadr´atico. 

Ahora suponemos que el stencil se va reduciendo, hacia el punto _x_ 0 pero manteniendo las distancias relativas invariantes, es decir: 



con _ξl_ =cte y _ϵ →_ 0. Poniendo el sistema anterior en forma matricial: 



donde: 



**91** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.4. M´etodo de diferencias finitas en m´as de una dimensi´on_ 



y **e** es un vector que depende en principio de _ϵ_ pero cuyas componentes se mantienen acotadas al hacer tender _ϵ →_ 0. Resolviendo el sistema lineal, podemos obtener una expresion para cualquiera de las derivadas, digamos, por ejemplo, la _k−_ ´esima: 



Ahora bien, **A** no depende de _ϵ_ de manera que tampoco dependen los coeficientes de su inversa _ckl_ , de manera que: 



De manera que llegamos a la siguiente regla simple que vincula la el orden de la derivada _k_ , el n´umero de puntos del stencil _N_ y el orden de la aproximaci´on _p_ : 



En particular, si se quiere aproximar una derivada _k_ -´esima, entonces es necesario al menos _k_ +1 puntos para que la aproximaci´on sea “convergente” es decir _p ≥_ 1. Por ejemplo, podemos obtener la derivada de primer orden _k_ = 1 con precisi´on _O_ (∆ _x_ )<sup>2</sup> ( _p_ = 2), con _N_ = 3 puntos. Por el contrario, para la derivada segunda ( _k_ = 2) s´olo podemos esperar una precisi´on _O_ (∆ _x_ ) ( _p_ = 1) con _N_ = 3 puntos. En el caso de una malla de paso constante, y con diferencias centradas se puede obtener una precisi´on un orden mayor por cuestiones de simetr´ıa. 

#### **4.4. M´etodo de diferencias finitas en m´as de una dimensi´on** 

Empecemos por un dominio rectangular con condiciones Dirichlet (ver figura 4.10): 









Generamos una malla de paso constante ∆ _x_ , ∆ _y_ (ver figura 4.11): 



llamamos _“nodo lm”_ al punto de coordenadas: 



[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

**92** 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.5. Aproximaci´on en diferencias finitas_ _<u>para</u> derivadas_ _<u>parciales</u>_ 



<!-- Start of picture text -->
y<br>_<br>Lx<br>_ Ω _<br>0 x<br>_<br>0 Lx<br><!-- End of picture text -->

Figura 4.10: Problema bidimensional de conducci´on del calor rect´angulo. 

#### **4.5. Aproximaci´on en diferencias finitas para derivadas parciales** 

Consideramos una expansi´on en _x_ de la forma (ver figura 4.12): 





Igual que en 1D, se obtienen expresiones aproximadas para las derivadas de primer y segundo orden: 







y expresiones similares en _y_ . 

La discretizaci´on se hace remplazando las derivadas segundas por diferencias de segundo orden para los nodos interiores: 



**93** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.5. Aproximaci´on en diferencias finitas_ _<u>para</u> derivadas_ _<u>parciales</u>_ 



Figura 4.11: Malla homo´genea de diferencias finitas. 

y las condiciones de contorno: 



El sistema es, como siempre: 

**K** **_φ_** = **f** 



donde **K** es ahora una matriz tri-diagonal por bloques: 



siendo **K**<sup>¯</sup> : 



[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

**94** 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.5. Aproximaci´on en diferencias finitas_ _<u>para</u> derivadas_ _<u>parciales</u>_ 



<!-- Start of picture text -->
m+1<br>(l,m)<br>m<br>m-1<br>l-1 l l+1<br><!-- End of picture text -->

Figura 4.12: Nodo t´ıpico en una malla estructurada bidimensional. 

(esto es para el caso especial ∆ _x_ = ∆ _y_ ). El vector de inc´ognitas es: 



que corresponde a haber numerado las inc´ognitas primero seg´un _y_ y despu´es seg´un _x_ (ver figura 4.13). 

##### **4.5.1. Stencil del operador discreto** 

Consideremos la fila de la matriz correspondiente a la ecuaci´on para el nodo _lm_ . De todos los coeficientes s´olo cinco son no nulos, correspondiente al nodo en cuesti´on y los cuatro vecinos. Estos coeficientes son los mismos para todos los nodos de la malla, y entonces podemos caracterizar el 

**95** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.6. Resoluci´on del sistema de ecuaciones_ 



<!-- Start of picture text -->
y<br>yM<br>M-1 2(M-1) (M-1)(L-1)<br>yM-1<br>2 M+1<br>y2<br>y1 1 M<br>y0<br>x<br>x0 x1 x2 xL-1 xL<br><!-- End of picture text -->

Figura 4.13: Orden de numeraci´on de los grados de libertad en el sistema lineal. 

operador discreto por una sola de las l´ıneas. Para ser m´as grafico a´un, podemos poner los coeficientes en los nodos asociados. A esto se le llama el _stencil_ o _estrella_ del operador discreto. Para el caso de la ecuaci´on de Poisson que estamos tratando, con ∆ _x_ = ∆ _y_ , el stencil obtenido consta de 5 puntos involucrados y tiene como coeficientes 4 para el nodo central y -1 para todos los otros (ver figura 4.14) 

#### **4.6. Resoluci´on del sistema de ecuaciones** 

##### **4.6.1. Estructura banda** 

Consideremos el caso _Lx_ = 3, _L_ = 3, _Ly_ = 5, _M_ = 5, ∆ _x_ = ∆ _y_ , por simplicidad (ver figura 4.15). La matriz es: 



vemos que los elementos no nulos se encuentran s´olo sobre la diagonal y sus cuatro codiagonales superiores e inferiores, es decir (ver figura 4.16): 



con _a_ = 4. Toda matriz que satisface (4.130) para alg´un _a_ es llamada una _matriz banda_ y _a_ el _ancho de banda_ de la matriz. Obviamente, el inter´es surge cuando _a_ es mucho menor que la dimensi´on _N_ de la matriz, que es el caso para las matrices de elementos finitos. Veremos que en ese caso se 

**96** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.6. Resoluci´on del sistema de ecuaciones_ 



<!-- Start of picture text -->
-1<br>m+1<br>-1 4 -1<br>m<br>-1<br>m-1<br>l-1 l l+1<br><!-- End of picture text -->

Figura 4.14: Stencil de 5 puntos para el operador de Laplace en 2D. 

puede ganar mucho tanto en requerimientos de memoria para factorizar la matriz, como en tiempo de procesamiento. Podemos ver que en el caso que nos ocupa _a_ = _M −_ 1. 

##### **4.6.2. Requerimientos de memoria y tiempo de procesamiento para matrices banda** 

Consideremos una matriz sim´etrica de _N × N_ , con ancho de banda _a_ . Puede verse que al factorizar la matriz los elementos fuera de la diagonal no se “llenan”, esto es, siguen siendo nulos despu´es del proceso de factorizaci´on. Mediante algoritmos especialmente dise˜nados, se puede trabajar s´olo sobre las diagonales activas de manera que s´olo se requieren almacenar _N_ +( _N −_ 1)+( _N −_ 2)+ _· · ·_ +( _N −a_ ) _≈ Na_ elementos, contra los _N_ ( _N_ + 1) _/_ 2 elementos que hace falta almacenar, si no se tiene en cuenta la estructura banda de la matriz. El factor de ganancia en memoria es: 



Consideremos ahora el costo computacional del m´etodo de eliminaci´on de Gauss para una matriz llena. Para eliminar la primera columna, debemos hacer _N −_ 1 operaciones de fila, cada una de las cuales tiene _N_ elementos, lo cual requiere _N_ ( _N −_ 1) _e_ operaciones, donde _e_ es el n´umero de operaciones necesarios para eliminar un elemento. Usualmente se necesita una suma y una multiplicaci´on, de manera que _e_ = 2, sin embargo, dependiendo de la m´aquina y de detalles de implementaci´on, debe tenerse en cuenta las operaciones de traer los elementos desde la RAM el procesador y de incrementar los contadores. Para eliminar la segunda columna, debemos realizar _N −_ 2 operaciones de _N −_ 1 

**97** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.6. Resoluci´on del sistema de ecuaciones_ 



Figura 4.15: Malla de diferencias finitas para un problema con condiciones Dirichlet. 

elementos, es decir ( _N −_ 1)( _N −_ 2) _e_ operaciones. El n´umero total de operaciones es de: 

(Costo computacional matriz llena) = 



Si la matriz es banda, entonces en la primera columna solo hay _a_ + 1 elementos no nulos. Por lo tanto, solo debemos hacer _a_ operaciones de fila. Adem´as, en cada una de las filas s´olo los 2 _a_ primeros elementos est´an dentro de la banda, de manera que deben efectuarse 2 _ea_<sup>2</sup> operaciones para eliminar la primera columna. Para las otras columnas, ocurre algo parecido y el costo total es: 



La relaci´on de costos es: 



Para fijar ideas, consideremos el caso de una malla de _L_ = _M_ = 200 nodos. El n´umero total de grados de libertad es _N_ = ( _L −_ 1) _×_ ( _M −_ 1) _≈ LM_ = 40000. El n´umero total de elementos a almacenar como matriz llena es _≈ N_<sup>2</sup> _/_ 2 = 8 _,_ 0 _×_ 10<sup>8</sup> elementos. En el caso de utilizar doble precisi´on esto equivale a 12.8Gbytes de memoria RAM. Utilizando almacenamiento banda tenemos _a_ = 200 y el n´umero de elementos a almacenar es _Na_ = 200 _×_ 40000 = 8000000, 64.0Mbyte de memoria en doble precisi´on. 

Con respecto al costo computacional, para la matriz llena es 40000<sup>3</sup> _/_ 3 _e ≈_ 2 _,_ 1 _×_ 10<sup>13</sup> _e_ operaciones, mientras que para matriz banda es de s´olo 2 _×_ 200<sup>2</sup> _×_ 40000 _e_ = 3 _,_ 2 _×_ 10<sup>9</sup> _e_ operaciones. Considerando 

**98** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.6. Resoluci´on del sistema de ecuaciones_ 



<!-- Start of picture text -->
Kij=0<br>N<br>2a<br>Kij=0<br>N<br><!-- End of picture text -->

Figura 4.16: Definici´on del ancho de banda de una matriz. 

_e_ = 2 y una velocidad de procesamiento de 40Mflops (1 Mflop=10<sup>6</sup> operaciones de punto flotante por segundo) los tiempos de procesamiento resultan ser de: 



##### **4.6.3. Ancho de banda y numeraci´on de nodos** 

El ancho de banda es altamente dependiente de la _numeraci´on de los nodos_ , esto es, del orden en que las inco´gnitas son puestas en el vector **_φ_** . Por ejemplo si la numeraci´on se hace primero en _y_ y 

**99** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.7. Dominios de forma irregular_ 



<!-- Start of picture text -->
y<br>yM<br>(L-1)(M-1)<br>yM-1<br>L L+1 L+2 2(L-1)<br>y2<br>y1 1 2 3 4 5 L-3 L-2 L-1<br>y0<br>x<br>x0 x1 x2 xL-1 xL<br><!-- End of picture text -->

Figura 4.17: Numeraci´on alternativa para reducir el ancho de banda. 

despu´es en _x_ (ver figura 4.17): 



entonces el ancho de banda pasa a ser de _a_ = _L −_ 1. La regla es, entonces, _numerar siempre primero en aquella direcci´on en la cual hay menos nodos_ . 

#### **4.7. Dominios de forma irregular** 

El m´etodo de diferencias finitas ser´ıa de muy poca utilidad si s´olo pudiera aplicarse a dominios de forma rectangular. Existen b´asicamente dos posibilidades para extender el m´etodo a un dominio de forma arbitraria como en la figura 4.18. (�, � indican ventajas y desventajas del m´etodo, respectivamente): 

- Considerar al dominio _inmerso en una malla homog´enea_ (ver figura 4.18). En este caso el esquema para los nodos interiores es el mismo como el que consideramos hasta ahora. 

   - La generaci´on de la malla es muy sencilla (�) 

**100** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.7. Dominios de forma irregular_ 



<!-- Start of picture text -->
Ω<br>Ω<br>∆ y<br>∆ x<br><!-- End of picture text -->

Figura 4.18: El dominio de resoluci´on de resoluci´on Ωes “embebido” en una malla homog´enea. 

   - Deben generarse ecuaciones especiales para los nodos en el contorno (�) 

   - En principio no hay posibilidad de _“refinar”_ la malla en ciertas partes (�) 

- _Ajuste del contorno (“boundary fitting”)_ (ver figura 4.19): La idea es encontrar una transfor- 

- maci´on de coordenadas que lleve el dominio irregular en cuesti´on a un rect´angulo. La ecuaci´on original es transformada siguiendo las reglas cl´asicas y finalmente se resuelven las ecuaciones transformadas en el dominio transformado. 

   - La generaci´on de la malla es relativamente compleja, incluso para dominios relativamente simples (�) 

   - Los esquemas en diferencias, tanto para nodos interiores como nodos de contorno se obtienen f´acilmente por los m´etodos est´andar (�) 

   - La malla suele estar m´as densa en ciertas partes que en otras. Esto puede ser una ventaja o desventaja dependiendo de si el lugar donde la malla est´a mas densa es un punto donde se necesita mayor precisi´on o no (��?) 

   - Admite cierto grado de refinamiento (�) 

##### **4.7.1. Inmersi´on del dominio irregular en una malla homog´enea** 

Como se mencionara, aqu´ı el punto delicado es el hallar f´ormulas en diferencias para los nodos en contacto con el contorno. Consideremos por ejemplo la figura 4.18.. Haciendo un zoom de una regi´on cerca del contorno, tenemos una disposici´on como en la figura 4.20. Suponiendo que la condici´on de 

**101** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.7. Dominios de forma irregular_ 



<!-- Start of picture text -->
η y<br>Ω<br>Ω′<br>ξ x<br><!-- End of picture text -->

Figura 4.19: La malla es generada por mapeo de una malla homog´enea sobre un rect´angulo al dominio Ω. 

contorno es de tipo Dirichlet, debemos encontrar ecuaciones en diferencias para un nodo como el _P_ . Considerando que la malla es homog´enea ( _PT_ = _PS_ = ∆ _x_ , _PQ_ = _PR_ = ∆ _y_ ) y definiendo: 



podemos hacer un desarrollo de Taylor para _φT_ y _φV_ : 



con 



La derivada de primer orden se puede obtener, a orden ∆ _x_<sup>2</sup> , haciendo una combinaci´on lineal de _φT_ y _φV_ de forma de que se cancelen los t´erminos que contienen la derivada segunda. 



de manera que: 



[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

**102** 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.7. Dominios de forma irregular_ 



<!-- Start of picture text -->
∆ y<br>Q<br>U<br>λ∆ y<br>S V P T<br>µ∆ x<br>R<br>∆ x<br><!-- End of picture text -->

Figura 4.20: Diagrama general de los nodos sobre la malla regular en la zona cercana al contorno del dominio de resoluci´on. F´rmulas especiales en diferencias deben ser desarrolladas para los nodos como el _P_ 

La derivada segunda se puede aproximar de: 







de donde: 



N´otese que para _µ_ = 1 ( _PV_ = _PS_ ) se recupera la f´ormula centrada de segundo orden. Por el contrario, la expresi´on anterior es de primer orden y, de hecho _es imposible generar una aproximaci´on de segundo orden para la derivada segunda con 3 puntos en una malla irregular_ (Confi´erase a la secci´on anterior donde se explica la relaci´on entre precisi´on, n´umero de puntos y orden de la derivada). 

Finalmente, el sistema de ecuaciones se halla planteando las ecuaciones en diferencias para los puntos interiores sobre una malla regular, mientras que para los puntos como el _P_ sobre el contorno, las ecuaciones son de tipo: 



[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.7. Dominios de forma irregular_ 

Debe recordarse que esta expresi´on es _O_ (∆ _x_ ) de manera que s´olo puede esperarse una tal convergencia. 

Para condiciones de tipo Neumann, el problema es a´un m´as complicado. 

##### **4.7.2. Mapeo del dominio de integraci´on** 

Consideremos, por ejemplo, resolver el problema: 



En notaci´on tensorial: 



Como fue adelantado, aqu´ı se trata de encontrar una transformaci´onnn de coordenadas: 



de tal forma que en la variable **_η_** , el dominio de integraci´on sea un ret´angulo. La transformaci´on de las ecuaciones se hace por la _“regla de la cadena”_ : 



donde **J** denota la matriz del jacobiano de la transformaci´on y _∇η_ es el operador gradiente con respecto a las coordenadas **_η_** . Usando c´aculo tensorial, podemos plantear la ecuaci´on diferencial en t´erminos de: 

derivadas de las inc´ognitas y los datos (propiedades del material) con respecto a las coordenadas transformadas, e.g.: ( _∂φ/∂ηj_ ), etc... 

- propiedades de la transformaci´on como: jacobianos, tensores m´etricos, factores de escala, (conocidos). 

Continuando con la ecuaci´on de Poisson, su transformaci´on es: 



donde: 



La ecuaci´on transformada puede ser reescrita como una ecuaci´on quasi-´armonica con una conductividad anisotr´opica: 



[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.7. Dominios de forma irregular_ 

donde: 



##### **4.7.3. Coordenadas curvil´ıneas ortogonales** 

Un caso particular es cuando la transformaci´on es tal que las superficies _ηi_ =cte son ortogonales entre s´ı en el sistema _xi_ . Puede verse que la condici´on para que esto ocurra es que el tensor m´etrico de la transformaci´on satisfaga: 



_hi_ es llamado el _factor de escala_ de la coordenada transformada _ηi_ . Se desprende que _g_ 1 _/_ 2 = _h_ 1 _h_ 2 _h_ 3. La ecuaci´on del calor en coordenadas c´urvilineas ortogonales es: 



##### **4.7.4. Ejemplo** 

Sea resolver la ecuaci´on del calor en una c´ascara esf´erica: 



con condiciones de frontera Dirichlet en la c´ascara exterior e interior: 



donde las coordenadas esf´ericas est´an dadas por la transformaci´on usual: 





Los factores de escala son: 







de manera que la ecuaci´on transformada es: 



[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.7. Dominios de forma irregular_ 

Se contruye una malla homog´enea en coordenadas transformadas, dada por una serie de ( _I_ + 1) _×_ ( _J_ + 1) _×_ ( _K_ + 1) puntos _Pijk_ cuyas coordenadas ( _ri, θj, φk_ ) est´an dadas por: 



donde 0 _≤ ϵθ ≪ π_ tiene el fin de evitar la singularidad en los polos _θ_ = _±π/_ 2. La ecuaci´on para el nodo _ijk_ es: 



donde: 



y 



La ecuaciones (4.170-4.172) son conservativas y precisas de segundo orden. 

##### **4.7.5. Mallas generadas por transformaci´on conforme** 

Una clase especial de transformaciones pueden generarse mediante la teor´ıa de variable compleja llamada _transformaci´on conforme_ . Si bien est´a es v´alida s´olo para 2D, puede combinarse con otras transformaciones para generar mallas tridimensionales. 

Una transformaci´on conforme ( _x, y_ ) _→_ ( _ξ, η_ ), se basa en definir dos variables complejas _z_ = _x_ + _iy_ y _w_ = _ξ_ + _iη_ y poner la transformaci´on en forma de una funci´on anal´ıtica: _w_ = _f_ ( _z_ ) con _f_ anal´ıtica. Las transformaciones conformes son un subconjuto de las transfomaciones obtenidas por coordenadas curv´ılineas ortogonales. No s´olo las lineas _ξ_ =cte, _η_ =cte son ortogonales entre s´ı, sino que los factores de escala son iguales _hξ_ = _hη_ . Esto significa que un elemento rectangular _e_ en coordenadas _ξ, η_ (ver figura 4.21) es mapeado por la transformaci´on en otro _e_<sup>_′_</sup> de forma aproximadamente rectangular con ´angulos interiores _α, βγδ ≈_ 90<sup>_◦_</sup> ) y con, aproximadamente, la misma relaci´on de aspecto ( _BB_<sup>_′_</sup> _/AA_<sup>_′_</sup> _≈_ ∆ _η/_ ∆ _ξ_ ). 

Por ejemplo, la transformaci´on de coordenadas _z_ = exp( _w_ ), equivale a la transformaci´on: 



**106** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.7. Dominios de forma irregular_ 



<!-- Start of picture text -->
β A’<br>B’<br>γ<br>∆η e e’<br>α<br>B<br>δ<br>η ∆ξ y A<br>x<br>ξ<br><!-- End of picture text -->

Figura 4.21: Transformaci´on de un “elemento” de volumen ∆ _ξ_ , ∆ _η_ por una transformaci´on conforme. No s´olo los ´angulos interiores permanecen aproximadamente rectos, sino que la relaci´on de aspecto permanece inalterado. 

y es muy similar al cambio de coordenadas de cartesianas a polares. Por ejemplo, un dominio rectangular como el _ABCDEF_ (ver figura 4.22) es transformado en una corona circular. N´otese que el ∆ _r_ entre sucesivas capas de nodos va diminuyendo con el radio. Lo interesante es que esta variaci´on es tal que la relaci´on de aspecto se mantiene constante, como fue mencionado en un marco m´as general. 

Las transformaciones conformes pueden ser concatenadas de forma de poder obtener dominios bastantes m´as complicados. Por ejemplo, a la transformaci´on (4.173) se puede aplicar una transformaci´on lineal para correr el centro del c´ırculo interior _O_ de _z_ ( _O_ ) = 0 a _z_ 1( _O_ ) = 1 + _e_ , manteniendo el punto _B_ en _z_ = 1 (ver figura 4.24). La transformaci´on es: 



A continuaci´on una _“transformaci´on de Joukowski”_ lleva la corona circular al exterior de un perfil aerodin´amico (ver figura 4.23): 



La circunferencia interior _ABC_ es transformada sobre el contorno del perfil, mientras que el c´ırculo exterior _DEF_ es transformado en una curva cercana a una circunferencia. Usualmente, se supone que sobre esta circunferencia el flujo no est´a perturbado para poder imponer las condiciones de contorno apropiadas. El punto _B_ en _z_ 1 = 1 es transformado en el borde de fuga ( _TE_ = _“trailing edge”_ , mientras que el punto _A ≡ C_ es transformado en el borde de ataque _LE_ ( _“Leading Edge”_ ). 

Otro ejemplo de transformaci´on podemos observarlo en las figuras 4.25, 4.26, donde el dominio rectangular _ABCDEF_ en el plano _w_ es mapeado por la transformaci´on _z_ = _w_ 3 _/_ 2 en el dominio indicado en la figura 4.26. 

**107** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.7. Dominios de forma irregular_ 



<!-- Start of picture text -->
w π r=e z<br>F E D<br>1<br>O r=1 E<br>0<br>A ≡ C B<br>0 D ≡ F<br>A B C<br>− π<br>− π 0 π − π 0 π<br>iw<br>z=e<br><!-- End of picture text -->

Figura 4.22: Un rect´angulo es transformado en una corona circular usando la transformaci´on exponencial _z_ = _e_<sup>_w_</sup> . 

**108** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.7. Dominios de forma irregular_ 



<!-- Start of picture text -->
z<br>2<br>1<br>0 D ≡ F<br>E<br>A ≡ C=L.E. B=T.E.<br>-1 0 1<br><!-- End of picture text -->

Figura 4.23: Transformaci´on de Joukowski. El c´ı rculo interior es mapeado sobre el perfil mientras que el exterior es mapeado sobre un cuasi-c´ırculo al infinito. 

**109** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.7. Dominios de forma irregular_ 



<!-- Start of picture text -->
z<br>1<br>1<br>D ≡ F<br>A ≡ C O B<br>0<br>E<br>0 1<br><!-- End of picture text -->

Figura 4.24: Transformaci´on intermedia para correr el centro del c´ırculo, manteniendo el punto _z_ = 1 fijo. 

**110** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.7. Dominios de forma irregular_ 



<!-- Start of picture text -->
w<br>F E D<br>1<br>0<br>A B C<br>-1 0 1<br><!-- End of picture text -->

Figura 4.25: Dominio rectangular en el plano _w_ . 



<!-- Start of picture text -->
D<br>1.5 z<br>z=w<br>1<br>E<br>C<br>0<br>B<br>F<br>A<br>-1<br>-1 0 1<br><!-- End of picture text -->

Figura 4.26: Dominio transformado en el plano _z_ = _w_ 3 _//_ 2 _._ . 

**111** 

[Document version: curso-0.3.0. File version: $Id: diffin.tex,v 1.9 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.8. La ecuaci´on de convecci´on-reacci´on-difusi´on_ 

#### **4.8. La ecuaci´on de convecci´on-reacci´on-difusi´on** 

Consideremos el transporte de una sustancia de concentraci´on _φ_ en un medio fluido con campo de velocidades **v** y difusividad _k >_ 0. Adem´as consideramos que _φ_ s consume con una reacci´on qu´ımica de cin´etica de primer orden, con constante _c >_ 0 y que hay una producci´on de _φ_ dada por una densidad de producci´on _g_ 



con condiciones de contorno 





Los t´erminos involucrados en (4.176) se denominan 



Tanto **v** como _c_ , _g_ y _k_ pueden ser funciones de la posici´on y del tiempo **v** = **v** ( **x** _, t_ ), etc... Las dimensiones de las costantes es 



**112** 

[Document version: curso-0.3.0. File version: $Id: diffcrd.tex,v 1.14 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.8. La ecuaci´on de convecci´on-reacci´on-difusi´on_ 

##### **4.8.1. Interpretaci´on de los diferentes t´erminos** 

Los t´erminos de reacci´on y producci´on pueden agruparse como _−c_ ( _φ − φ_ eq), donde _φ_ eq = _g/c_ es la concentraci´on de _φ_ que esta en _“equilibrio local”_ con la producci´on. En estado estacionario y con condiciones homog´eneas tal que _φ_ no depende de _x_ entonces _φ → φ_ eq. (Nota: si _g_ = _f_ ( _φ_ ) entonces los zeros de _f_ son puntos de equilibrio. ) 

Para entender mejor el significado de los diferentes t´erminos involucrados vamos a considerar algunos casos particulares. 

**No hay dependencia espacial.** Si consideramos que _φ_ no depende de **x** ( _φ̸_ = _φ_ ( **x** )) entonces los t´erminos convectivo y difusivo son nulos y llegamos a una ODE para el valor de _φ_ (constante en todo el dominio) 



cuya soluci´on es 



y vemos que _φ_ decae exponencialmente hacia _φ_ eq. Podemos deducir de esto que en zonas donde los gradientes son bajos _φ_ tiende a aproximarse a _φ_ eq. 



<!-- Start of picture text -->
1<br>φ<br>0.8 θ=1<br>0.6<br>θ=3<br>0.4<br>0.2<br>θ=10<br>θ=30<br>θ=100<br>0<br>0 0.2 0.4 0.6 0.8 x/L 1<br><!-- End of picture text -->

Figura 4.27: Concentraci´on para diferentes valores del mdulo<sup>´</sup> de Thiele 

**113** 

[Document version: curso-0.3.0. File version: $Id: diffcrd.tex,v 1.14 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.8. La ecuaci´on de convecci´on-reacci´on-difusi´on_ 

**Reacci´on difusi´on.** Ahora, si incluimos la difusi´on, pero estacionario y con **v** = 0, entonces la ecuaci´on es 



Si _φ_ eq = cte, pero la condici´on de contorno es _φw̸_ = _φ_ eq entonces _φ_ va a tratar de estar cerca de _φ_ eq en el interior del dominio, yendo suavemente hacia _φw_ en los contornos. La rapidez con la cual el valor interior empalma con la condici´on de contorno depender´a de la importancia relativa entre _c_ y _k_ . Consideremos, para fijar ideas, el siguiente problema 





entonces la soluci´on es 



donde _θ_ es el _“m´odulo de Thiele”_ o _“n´umero de reacci´on”_ . La soluci´on se observa en la figura 4.27 y vemos que para n´umeros de Thiele altos la soluci´on se pega al valor de equilibrio en el interior del dominio y empalma con la condici´on de contorno en una capa l´ımite de esperor ~~�~~ _k/c_ = _L/θ_ . Estas capas l´ımites representan grandes gradientes para la soluci´on y pueden aparejar problemas (falta de convergencia) para los m´etodos num´ericos. 

En el caso t´ermico _φ_ es la temperatura, _k_ la difusividad t´ermica y _g_ una fuente de calor distribuida. _c_ puede provenir de una reacci´on endot´ermica proporcional a la temperatura. Tambien en el caso 2D el t´erino _−c_ ( _φ − φ_ eq) puede pensarse como un t´ermino de enfriamiento Newtoniano. 

Notar que si **v** = 0, los restantes t´erminos s´olo contienen derivadas espaciales de orden par (0 ´o 2) y por lo tanto son invariantes ante inversi´on de coordenadas ( _x →−x_ ). Esto dar´a lugar despu´es a que las matrices de los m´etodos num´ericos resulten sim´etricas. 

**114** 

[Document version: curso-0.3.0. File version: $Id: diffcrd.tex,v 1.14 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.8. La ecuaci´on de convecci´on-reacci´on-difusi´on_ 

**Advecci´on difusi´on.** En el caso estacionario (( _∂φ/∂t_ ) = 0) y si no hay reacci´on ni producci´on ( _c, g_ = 0) queda la _“ecuacio´n de advecci´on-difusi´on”_ . Consideremos el caso 1D en un intervalo de longitud _L_ con condiciones Dirichlet 



Esto representa el transporte de temperatura _φ_ por un fluido con difusividad _k_ y velocidad _v_ . La soluci´on puede encontrarse por m´etodos operacionales est´andar, proponiendo soluciones de la forma e<sup>_λx_</sup> , resolviendo el polinomio caracter´ıstico en _λ_ y buscando la combinaci´on lineal que satisface las condiciones de contorno. La soluci´on resulta ser 



(ver figura 4.28). Para valores de _v_ muy peque˜nos la souci´on se aparta poco de la soluci´on de conducci´on pura 



A medida que _v_ aumenta las temperaturas bajan ya que el movimiento del fluido tiende a contrarrestar el efecto de la condici´on de contorno en _x_ = _L_ y refrigera m´as que cuando el fluido est´a quieto. La importancia relativa de ambos t´erminos (difusivo y convectivo) se puede cuantificar a trav´es del _“n´umero de P`eclet”_ Pe dado por (4.186). A medida que el Pe aumenta, el gradiente de _φ_ se concentra m´as y m´as cerca de la pared _x_ = 1, formando una capa l´ımite de espesor 



De nuevo, estos altos gradientes son una fuente de problemas para los m´etodos num´ericos. Si la velocidad se invierte entonces la discontinuidad se produce en _x_ = 0 que es la nueva salida ( _x_ = _L_ es la entrada). 

Una forma diferente de ver este fen´omeno es considerar que, a medida que _k →_ 0, el problema se hace cada vez m´as advectivo (Pe _→∞_ ). Ahora bien, para el problema advectivo puro la ecuaci´on es de primer orden y por lo tanto requiere de una sola condici´on de contorno. La teor´ıa de sistemas hiperb´olicos indica que la condici´on de contorno debe aplicarse donde las l´ıneas caracter´ısticas entran. El valor de la variable en un contorno donde las caracter´ısticas salen resulta de la integraci´on de la ecuaci´on dentro del dominio. Si se pretende imponer un valor diferente como condici´on de contorno Dirichlet, la diferencia se absorbe en una capa l´ımite. 

Debido a que la ecuaci´on de advecci´on pura propaga los valores a lo largo de las caracter´ısticas, tambi´en se pueden producir altos gradientes en el interior del dominio. Por ejemplo consideremos advecci´on pura en u dominio rectangular _ADD_<sup>_′_</sup> _A_<sup>_′_</sup> como se muestra en la figura 4.30. El flujo entra por el lado _AA_<sup>_′_</sup> y sale por _DD_<sup>_′_</sup> . La condici´on a la entrada es _φ_ = _φ_<sup>¯</sup> donde _φ_<sup>¯</sup> contiene un salto cerca del punto _W_ . El transporte convectivo tiende a propagar esta discontinuidad a lo largo de la caracter´ıstica _WW_<sup>_′_</sup> , pero debido a la difusi´on la discontinuidad se va suavizando y termina en un escal´on suavizado a la salida _DD_<sup>_′_</sup> . 

**115** 

[Document version: curso-0.3.0. File version: $Id: diffcrd.tex,v 1.14 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.8. La ecuaci´on de convecci´on-reacci´on-difusi´on_ 



<!-- Start of picture text -->
1<br>0.8<br>Pe=−10<br>0.6<br>0.4 Pe=0<br>Pe=1<br>0.2<br>Pe=30<br>Pe=3<br>Pe=10 Pe=100<br>0<br>0 0.2 0.4 0.6 0.8 1<br><!-- End of picture text -->

Figura 4.28: Soluci´on al problema de advecci´on pura 1D con coeficientes constantes 



<!-- Start of picture text -->
C<br>φ<br>contorno de salida<br>B<br>contorno de entrada<br>A<br>capa líimite<br>φ<br>solución invíscida<br>A B distancia a lo largo de la característica C<br>capa líimite<br>solución invíscida<br>característica<br><!-- End of picture text -->

Figura 4.29: Sistem´as fuertemente advectivos en 2D 

**116** 

[Document version: curso-0.3.0. File version: $Id: diffcrd.tex,v 1.14 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.8. La ecuaci´on de convecci´on-reacci´on-difusi´on_ 



<!-- Start of picture text -->
φ A’<br>B’<br>W<br>x<br>C’<br>A<br>D’<br>y<br>B<br>W’<br>C<br>D<br><!-- End of picture text -->

Figura 4.30: Discontinuidad interna propagada desde la condici´on de en un sistema fuertemente advectivo 

**117** 

[Document version: curso-0.3.0. File version: $Id: diffcrd.tex,v 1.14 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.8. La ecuaci´on de convecci´on-reacci´on-difusi´on_ 

##### **4.8.2. Discretizaci´on de la ecuaci´on de advecci´on-difusi´on** 



<!-- Start of picture text -->
1<br>φ<br>0.8<br>v=1 v=10<br>0.6<br>v=3<br>0.4 v=20<br>v=40<br>0.2<br>v=100<br>0 v=500<br>−0.2<br>−0.4<br>−0.6<br>−0.8<br>−1<br>0 0.2 0.4 0.6 0.8 1<br>x/L<br><!-- End of picture text -->

Figura 4.31: Soluci´on num´erica al problema de advecci´on difusi´on con un esquema centrado 

Consideremos el problema 1D de advecci´on difusi´on a coeficientes constantes (4.185). Consideremos una malla uniforme de _N_ segmentos de longitud ∆ _x_ = _L/N_ . Los nodos son _xj_ = ( _j −_ 1)∆ _x_ , para _j_ = 1 _, . . . , N_ + 1. Una discretizaci´on centrada de segundo orden es 



Notar que la derivada de primer orden introuce un t´ermino antisim´etrico. Este esquema funciona bien mientras la velocidad se mantenga por debajo de un cierto l´ımite, que resulta ser _v_ crit = 2 _k/_ ∆ _x_ (En la figura _k_ = 1 y el n´umero de puntos es _N_ = 20, de manera que ∆ _x_ = 0 _,_ 05 y _v_ crit = 40). Para velocidades mayores la soluci´on num´erica se vuelve oscilatoria y para velocidades mucho m´as grandes que la cr´ıtica las oscilaciones contaminan todo el dominio. N´otese que la velocidad cr´ıtica se produce cuando el P`eclet de la malla es 



Estas oscilaciones pueden asociarse a un falta de estabilidad del esquema num´erico, sin embargo el esquema es estable, estrictamente hablando, ya que si refinamos suficientemente entonces Pe∆ _x_ pasar´a a ser menor que uno y se recupera la convergencia _O_ (∆ _x_<sup>2</sup> ). Sin embargo vemos que si tomamos la estimaci´on de error est´andar 



la constante _C_ depende de Pe. O sea, no existe un _C_ independiente de Pe tal que (4.191) valga para todo ∆ _x_ y Pe, es decir _no se puede obtener una cota de error uniforme sobe Pe_ . Bajo esta definici´on de estabilidad m´as estricta el esquema es inestable. 

**118** 

[Document version: curso-0.3.0. File version: $Id: diffcrd.tex,v 1.14 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.8. La ecuaci´on de convecci´on-reacci´on-difusi´on_ 

##### **4.8.3. Desacoplamiento de las ecuaciones** 

Si consideramos las ecuaciones discretas del esquema centrado (4.189) para Pe _→∞_ , es decir _k_ = 0, obtenemos 



Esta ecuaci´on dice que 





Entonces, si _N_ es impar existe una soluci´on que es 



y por otro lado no existe soluci´on si _N_ es par. 

Se dice que hay un _“desacoplamiento”_ de las ecuaciones para los nodos pares e impares, lo cual es asociado normalmente a una falta de estabilidad del esquema num´erico. 

##### **4.8.4. Esquemas de diferencias contracorriente (upwinded)** 



<!-- Start of picture text -->
1.1<br>1<br>sign(x)<br>0.8<br>f 3(x)<br>0.6<br>0.4<br>0.2<br>0<br>f 1(x)<br>−0.2<br>−0.4<br>−0.6<br>−0.8<br>−1<br>−1.1<br>−20 −15 −10 −5 0 5 10 15 20<br><!-- End of picture text -->

Figura 4.32: Diferentes propuestas para el par´ametro de estabilidad 

Notemos que, en el caso de advecci´on pura (Pe = _∞_ ) la soluci´on num´erica deber´ıa ser 



**119** 

[Document version: curso-0.3.0. File version: $Id: diffcrd.tex,v 1.14 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.8. La ecuaci´on de convecci´on-reacci´on-difusi´on_ 

y esto se lograr´ıa si reemplazamos la derivada centrada en (4.192) por una derivada lateral a izquierda (tambi´en llamada _“contracorriente”_ o _“upwinded”_ ) 



Pero esto se puede reescribir como 



o, poniendo _k_ num = _v_ ∆ _x/_ 2, 



donde _k_ num es una difusi´on _“num´erica artificial”_ que _“estabiliza”_ el esquema. Notar que, si _v <_ 0, entonces el esquema debe estar decentrado a derecha 



y entonces debe ser _k_ num = _−v_ ∆ _x/_ 2, de manera que, en general 



Ahora bien, para Pe _< ∞_ podemos tomar 



Este esquema no presenta m´as inestabilidades y para Pe _≫_ 1 se aproxima al upwindado pero para Pe peque˜nos sigue agregando difusi´on, incluso para Pe∆ _x <_ 1 cuando sabemos que el esquema es estable, resultando en un esquema demasiado difusivo. Entonces surge la idea de tratar de reducir la difusi´on num´erica para valores de Pe∆ _x_ peque˜nos. Notemos que (4.200) puede reescribirse como 



con 



de manera que podr´ıamos reemplazar la _“funci´on de upwinding”_ sign() por otra que anule la difusi´on num´erica para _|_ Pe∆ _x| <_ = 1, por ejemplo podemos usar 



con 



[Document version: curso-0.3.0. File version: $Id: diffcrd.tex,v 1.14 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.8. La ecuaci´on de convecci´on-reacci´on-difusi´on_ 

o tambi´en, para hacerlo m´as continuo 



Puede demostrarse que, si elegimos _f_ ( _x_ ), como la siguiente _“funci´on m´agica”_ 



entonces, en este caso simple se obtiene la soluci´on exacta (4.186) (de ah´ı el nombre de funci´on m´agica). Sin embargo, esto s´olo vale mientras el problema sea 1D, con coeficientes constantes, paso de la malla constante y sin t´ermino fuente. De todas formas es una funci´on de upwinding interesante, ya que en forma muy suave satisface todos los l´ımites necesarios. 

Como (d _α/_ d _x_ ) _|x_ =0 =<sup>1</sup> _/_ 3 otra funci´on comunmente utilizada es 



##### **4.8.5. El caso 2D** 

El primer intento por extender el esquema upwindado a 2D (o 3D) es agregar una viscosidad num´erica seg´un cada una de las direcciones principales de la malla. Sea un dominio rectangular 0 _≤ x ≤ Lx_ , 0 _≤ y ≤ Ly_ , dividido en _Nx_ , _Ny_ intervalos de longitud ∆ _x_ = _Lx/Nx_ , ∆ _y_ = _Ly/Ny_ . Los puntos de la malla est´an ubicados en _xjk_ = (( _j −_ 1)∆ _x,_ ( _k −_ 1)∆ _y_ ) y sea _φ_ ( _xjk_ ) _≈ φj,k_ . Ademas, consideremos **v** = ( _vx, vy_ ) = cte, 



donde 



Este esquema resulta ser estable. Si el flujo esta alineado con la malla, es decir _vx_ = 0 o _vy_ = 0, entonces el esquema reproduce exactamente sus virtudes en el caso 1D. En general la viscosidad num´erica es _“anisotr´opica”_ , por ejemplo, si **v** = ( _v,_ 0) entonces 



o, en forma tensorial 



[Document version: curso-0.3.0. File version: $Id: diffcrd.tex,v 1.14 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.8. La ecuaci´on de convecci´on-reacci´on-difusi´on_ 

y, en general, **k** num es un tensor anisotr´opico, con ejes principales a lo largo de los ejes principales de la malla. 

Si consideramos una velocidad cruzada con la malla, entonces el esquema resulta ser demasiado disipativo. Por ejemplo, consideremos **v** = _v_ (1 _,_ 1) _/√_ 2, y ∆ _x_ = ∆ _y_ = _h_ . Entonces 



es decir que el tensor de difusi´on num´erica es escalar 



donde **I** 2 _×_ 2 es el tensor identidad de 2 por 2. Ahora bien, si consideramos un sistema de coordenadas alineado con la velocidad, es decir _x_<sup>_′_</sup> _∥_ **v** e _y_<sup>_′_</sup> _⊥_ **v** , entonces el tensor difusividad num´erica sigue siendo 



mientras que lo deseable ser´ıa tener una difusividad seg´un _x_<sup>_′_</sup> pero no seg´un _y_<sup>_′_</sup> 



con 



donde el sub´ındice _s_ indica valores seg´un la l´ınea de corriente, as´ı por ejemplo 



Antitransformando el tensor (4.216) a los ejes _x − y_ obtenemos 



donde ˆ **s** = **v** _/v_ es el versor seg´un la l´ınea de corriente. 

Finalmente el esquema es 



[Document version: curso-0.3.0. File version: $Id: diffcrd.tex,v 1.14 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.8. La ecuaci´on de convecci´on-reacci´on-difusi´on_ 



<!-- Start of picture text -->
u<br>B<br>O<br>A<br><!-- End of picture text -->

Figura 4.33: Definici´on del tama˜no de la celda seg´un la l´ınea de corriente 

Notar la expresi´on en diferencias de la ´ultima fila que es una aproximaci´on _O_ (∆ _x_ ∆ _y_ ) para � _∂_<sup>2</sup> _φ/∂x∂y_ �. 

Falta definir la expresi´on general para _hs_ en funci´on del ´angulo que forma **v** con la malla. Existen varias propuestas para esto, no siendo ninguna de ellas totalmente satisfactoria. La m´as simple podr´ıa ser tomar alguna media de los par´ametros de la malla _h_ = (∆ _x_ + ∆ _y_ ) _/_ 2 o _h_ =<sup>_√_</sup> ∆ _x_ ∆ _y_ . Notar que en realidad estas definiciones no son _“seg´un la l´ınea de corriente”_ . Consecuentemente, es de esperarse que puedan ser muy sobre- o sub-difusivas en ciertos casos. Una posibilidad mejor es tomar la mayor distancia dentro de la celda a lo largo de una direcci´on paralela a **v** como el segmento _AB_ en la figura 4.33. La expresi´on resulta ser 



##### **4.8.6. Resoluci´on de las ecuaciones temporales** 

Hasta ahora vimos como discretizar las ecuaciones espacialmente para obtener un estado estacionario. Consideremos ahora un problema no estacionario. La idea es primero discretizar en el espacio, tal cual como se ha hecho hasta ahora. Por ejemplo consideremos la ecuaci´on de advecci´on-reacci´ondifusi´on lineal 1D, 



entonces un esquema estabilizado posible es 



donde _φ_<sup>˙</sup> significa la derivada temporal de _φ_ . Estas ecuaciones representan un _“sistema de ecuaciones diferenciales ordinarias”_ (ODE’s) acoplado 



Al mismo puede aplicarse una serie de esquemas de integraci´on temporal, por ejemplo 



[Document version: curso-0.3.0. File version: $Id: diffcrd.tex,v 1.14 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.9. Conducci´on del calor con_ _<u>generaci´on</u> en un cuadrado_ 

El m´etodo de forward Euler permite avanzar un paso de tiempo con un costo en tiempo de procesamiento y memoria de almacenamiento muy bajos, ya que no necesita resolver ning´un sistema lineal. Por el contrario, en los otros dos casos s´ı se necesita resolver un sistema. Si el problema es lineal, entonces podemos notar que la matriz del sistema **K** es constante (no var´ıa con el tiempo) de manera que podemos factorizarla una vez y posteriormen hacer solamente una retrosustituci´on. De todas formas el tiempo y memoria necesarios para avanzar un paso de tiempo en el backward Euler es mucho mayor que para el forward. Pero el forward tiene la limitaci´on de que, para pasos de tiempo grandes la soluci´on se hace inestable y diverge. El paso de tiempo cr´ıtico viene dado por 



Notar que estos criterios pueden ponerse como 



donde Co, Fo son los n´umeros adimensionales de Courant y Fourier. 

#### **4.9. Soluci´on exacta al problema de conducci´on del calor con generaci´on constante en un cuadrado** 

Ecuaciones de gobierno 



Proponemos un desarrollo 



Este desarrollo satisface las condiciones de contorno y representa una base completa. Por simetr´ıa podemos descartar los t´erminos para _j, k_ pares, ya que involucrar´ıan funciones antisim´etricas con respecto a _x, y_ = 12. Aplicando el operador de Laplace obtenemos 



Multiplicamos miembro a miembro por sin( _lπx_ ) sin( _mπy_ ) e integrando sobre el cuadrado. Usando que 



De manera que 



[Document version: curso-0.3.0. File version: $Id: solex.tex,v 1.2 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 4. M´etodo de diferencias finitas _Secci´on 4.9. Conducci´on del calor con_ _<u>generaci´on</u> en un cuadrado_ 

Es decir que 



Pero 



De manera que el valor m´aximo de _φ_ , que ocurre en el centro del cuadrado, es 



**125** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

## **Cap´ıtulo 5** 

# **T´ecnicas de discretizaci´on** 

Habiendo presentado en la primera parte los modelos matem´aticos que rigen el movimiento de los fluidos y estableciendo el conjunto de ecuaciones que gobiernan el caso general y algunos otros particulares ahora estamos en condiciones de pasar a tratar algunos aspectos num´ericos relacionados con el dise˜no de los esquemas m´as com´unmente empleados en fluidodin´amica computacional. Una de las t´ecnicas m´as empleadas en fluidodin´amica computacionalha sido la de diferencias finitas. Esta fue una de las primeras en aparecer y conserva vigencia a pesar de algunas restricciones propias de la t´ecnica. Su alta eficiencia para la resoluci´on de problemas definidos en geometr´ıas sencillas lo hace muy atractivo y es muchas veces la mejor opci´on cuando existe la posibilidad de mapear el dominio real en otro completamente regular y estructurado. Su definici´on se basa en aproximar los operadores diferenciales por otros denominados _operadores en diferencias_ que se aplican a un vector de datos que representa la soluci´on en un conjunto finito de puntos en el dominio. Esta forma de discretizar un operador diferencial es una alternativa y no la ´unica para tal fin. Desventajas claras del m´etodo como su dif´ıcil implementaci´on en problemas gobernados por geometr´ıas arbitrarias hizo que en los ´ultimos a˜nos gran cantidad de investigaci´on en el area de fluidodin´amica computacionalse volcase al uso de otras t´ecnicas alternativas. La mayor´ıa de las mismas se pueden presentar bajo un m´etodo general conocido como el _m´etodo de los residuos ponderados_ (WRM). 

#### **5.1. M´etodo de los residuos ponderados** 

##### **5.1.1. Introducci´on** 

Este m´etodo es conceptualmente diferente a aquel empleado en diferencias finitas ya que asume que la soluci´on a un problema planteado puede ser anal´ıticamente representable mediante una expansi´on del tipo: 



donde en general _am_ forman un conjunto finito de coeficientes con _M_ la dimensi´on del espacio finito dimensional empleado y _Nm_ las funciones anal´ıticas conocidas y elegidas para representar o expandir a la soluci´on del problema. Estas funciones son com´unmente denominadas _soluciones de prueba_ y su 

126 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

elecci´on hace a la diferencia entre una vasta cantidad de m´etodos num´ericos, como veremos en breve. La funci´on _ψ_ es introducida con el prop´osito de satisfacer las condiciones de contorno del problema. Sea Γ el contorno del dominio Ωdel problema, entonces la elecci´on de la funci´on _ψ_ es tal que 



De la elecci´on de _ψ_ y _Nm_ depender´a la calidad de la soluci´on y la convergencia del m´etodo num´erico a medida que se refina la discretizaci´on, o sea que _M →∞_ . Este requisito denominado _completitud_ est´a sustentado fuertemente en bases matem´aticas con lo que a diferencia del m´etodo de las diferencias finitas esta clase de t´ecnica goza con el apoyo de s´olidos conceptos matem´aticos de teor´ıa de operadores, an´alisis funcional y an´alisis num´erico. Si bien nuestra aplicaci´on ser´a la de obtener soluciones a ecuaciones a derivadas parciales un buen ejercicio para introducir los conceptos de aproximaci´on es el caso simple de aproximar una funci´on conocida a priori con una expansi´on del tipo (5.1) . 

###### **Aproximaci´on puntual de funciones** 

Este caso simple consiste en dada una funci´on _φ_ aproximarla por _φ_<sup>ˆ</sup> bajo el requisito que ambas coincidan en _M_ puntos distintos elegidos arbitrariamente sobre Ω. Este requisito conduce a un sistema de ecuaciones algebraicas lineales en el conjunto de par´ametros inc´ognita _{am_ ; _m_ = 1 _,_ 2 _, . . . , M }_ . 

Para graficar la explicaci´on supongamos una funci´on a aproximar como 

_φ_ = sin( _−_ 1 _,_ 8 _πx_ ) + _x_ graficada en la parte superior izquierda de la figura 5.1 en trazo lleno. 

En la misma figura se muestra la funci´on lineal _ψ_ que satisface las condiciones de contorno, o sea 



La rutina Ej ~~2~~ 0.m permite definir una aproximaci´on a _φ_ usando una cantidad _M_ de t´erminos a elecci´on del alumno. En la figura 5.1 se grafica en la parte superior izquierda en linea de puntos la soluci´on num´erica obtenida con 2 t´erminos y a su derecha el valor absoluto del error donde como vemos este vale cero en un conjunto de puntos equidistribuidos cuya cantidad coincide con _M_ . Las dos gr´aficas del medio corresponden a _M_ = 3 mientras que las dos de abajo representan solamente el error que se comete cuando _M_ = 4 y _M_ = 9. 

La forma de construir el sistema de ecuaciones algebraicas a resolver es bastante simple. Se debe reemplazar (5.1) para los _M_ puntos interiores al dominio e igualarlos a los valores de la funci´on _φ_ en esos nodos. Esto, para el caso de _M_ = 2 genera lo siguiente: 



**127** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 



<!-- Start of picture text -->
|e| = 0.07486<br>2 0.3<br>1.5 0.25<br>1 ψ 0.2<br>0.5 0.15<br>0 0.1<br>-0.5 φ 0.05<br>φ<br>-1 0<br>0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1<br>|e| = 0.05065<br>2 0.14<br>1.5 0.12<br>0.1<br>1<br>0.08<br>0.5<br>0.06<br>0<br>0.04<br>-0.5<br>0.02<br>-1 0<br>0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1<br>0.02 5 |e| = 0.00429 2 x 10 -5 |e| = 2.199e-006<br>0.02<br>0.01 5<br>1<br>0.01<br>0.00 5<br>0 0<br>0 0.2 0.4 0.6 0.8 1 0 0.2 0.4 0.6 0.8 1<br><!-- End of picture text -->

###### Figura 5.1: Aproximaci´on de una funci´on por ajuste puntual 

**128** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

La figura 5.2 muestra como var´ıa el error en un gr´afico semilogar´ıtmico siendo su convergencia del tipo espectral. En general el error en la aproximaci´on se puede escribir como: 



por lo que la pendiente en el gr´afico nos da una idea de la convergencia en funci´on de la discretizaci´on. 



<!-- Start of picture text -->
Convergencia<br>-1<br>10<br>-2<br>10<br>-3<br>10<br>-4<br>10<br>-5<br>10<br>-6<br>10<br>-1 0<br>10 10<br>log(M)<br>log(|E|)<br><!-- End of picture text -->

Figura 5.2: Convergencia de la aproximaci´on 

###### **Aproximaci´on por series de Fourier** 

Usando la teor´ıa de series de Fourier es posible aproximar una funci´on _φ_ arbitraria siempre que esta cuente con un n´umero finito de discontinuidades y de extremos locales, cosa que casi siempre ocurre en las aplicaciones. Entonces la aproximaci´on se escribe como: 



La inherente completitud de que gozan las series de Fourier le confiere la propiedad que al incrementar la dimensi´on del espacio de trabajo la precisi´on mejora. 

##### **5.1.2. Aproximaci´on por residuos ponderados** 

A continuaci´on se presenta un m´etodo general que permite hallar los coeficientes de (5.1) siendo las dos formas anteriores casos particulares del mismo. Definamos el error o residuo _R_ Ω en la aproximaci´on como: 



[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 



Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

siendo ´esta una funci´on de la posici´on en el dominio Ω. En la figura chapV-1 hemos presentado funciones de este tipo. La idea es que en lugar de pedir que esta funci´on _R_ Ω sea id´enticamente nula en todo el dominio le pedimos que integrada mediante alguna funci´on de peso esta sea nula, es decir: 



con _Wl_ un conjunto de funciones de peso independientes. Entonces en lugar de pedir que _φ_<sup>ˆ</sup> _→ φ_ como _M →∞_ le pedimos que chapV-7 se satisfaga para todo _l_ como _M →∞_ . De alguna manera se puede verificar que esto ´ultimo equivale a asumir que _R_ Ω _→_ 0 en todo el dominio. Reemplazando _φ_<sup>ˆ</sup> de (5.1) en (5.7) obtenemos un conjunto o sistema de ecuaciones algebraicas lineales para los coeficientes inc´ognitas _am_ que puede ser escrito en forma gen´erica como: 



Una vez que la funci´on _φ_ se conoce la aproximaci´on se define mediante la elecci´on de _ψ_ y las funciones de peso _Wl_ y de prueba _Nm_ . Diferentes funciones de peso dan or´ıgen a diferentes m´etodos, todos del tipo de residuos ponderados. 

###### **M´etodo de colocaci´on puntual** 

En este m´etodo las funciones de peso son de la forma: 



con _δ_ ( _x − xl_ ) la funci´on delta de Dirac. Esto equivale a anular el residuo en un conjunto finito de puntos _xl_ , o sea es similar a la aproximaci´on por ajuste puntual. La matriz **K** y el vector derecho se calculan como: 



###### **M´etodo de colocaci´on por subdominios** 



donde en este caso se requiere que el error integrado sobre cada una de estas subregiones sea nulo. 



**130** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

###### **M´etodo de Galerkin** 

Es uno de los m´as populares m´etodos y se basa en elegir 



con lo cual el sistema a resolver est´a formado por: 



Este m´etodo goza con la ventaja de que la matriz del sistema es sim´etrica Si elegimos como funciones de prueba y de peso aquellas que conforman la base de un desarrollo en series de Fourier se puede demostrar que el sistema queda reducido a una simple expresi´on para los coeficientes _am_ ya que la matriz del sistema es diagonal. Esta caracter´ıstica tan particular se debe a que la base elegida es _ortogonal_ con lo que �Ω<sup>_NlNmd_Ω= 0</sup><sup>_l̸_=</sup><sup>_m_.</sup> 

###### **Otros pesos** 

En general existen muchas posibles elecciones de la funci´on de peso. Entre las m´as conocidas a´un no presentadas podemos mencionar el _m´etodo de los momentos_ donde _Wl_ = _x_<sup>_l−_1</sup> donde se requiere que no solo la integral del error sea nula sino algunos de sus momentos. Otro m´etodo del estilo de los presentados bajo el m´etodo de los residuos ponderados es el _m´etodo de los cuadrados m´ınimos_ . Com´unmente definido como la minimizaci´on de un funcional formado como: 



la idea es hallar un extremo de dicho funcional mediante _∂a∂Il_<sup>=0,quealintroducirlaen(5.16)</sup> produce que 



habiendo usado el hecho que<sup>_∂φ_ˆ</sup> _∂zl_<sup>=</sup><sup>_Nl_apartirde(5.1).</sup> (5.17) equivale al m´etodo de Galerkin y es un caso particular del mismo. 

##### **5.1.3. Residuos ponderados para la resoluci´on de ecuaciones diferenciales** 

En la secci´on anterior hemos visto como utilizar el m´etodo de los residuos ponderados para aproximar funciones conocidas anal´ıticamente o aquellas en donde conocemos su evaluaci´on en un conjunto discreto de puntos. En esos casos el residuo estaba asociado a la diferencia entre la funci´on a aproximar y la aproximante. En esta secci´on trataremos el caso de la resoluci´on de ecuaciones diferenciales, en donde el residuo viene dado por la diferencia entre un operador diferencial aplicado a la funci´on a aproximar y el mismo operador aplicado a la aproximante. En el primer cap´ıtulo hemos hecho un repaso a los modelos f´ısicos y matem´aticos que gobiernan muchos de los problemas de inter´es en fluidodin´amica computacional. Para comenzar con un caso simple tomemos un operador diferencial sencillo como la ecuaci´on de Poisson, 

**131** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

###### **Funciones de prueba que satisfacen las condiciones de contorno** 

En esta secci´on trataremos el caso de funciones aproximantes que satisfacen exactamente las condiciones de contorno a trav´es de la elecci´on apropiada de las funciones de prueba. Sea el problema de Poisson: 



donde _κ_ puede ser la conductividad t´ermica de un material y _Q_ el flujo de calor aportado por una fuente y en este caso _φ_ ser´ıa la temperatura. En el caso lineal _κ_ y _Q_ son independientes de _φ_ . En general un problema de valores de contorno como ´este para estar bien planteado requiere definir las condiciones de frontera. Estas en general pueden ser escritas como otro operador diferencial, del tipo: 



En general existen diferentes tipos de condiciones de frontera. Las m´as conocidas son del tipo: 



Aproximando la soluci´on mediante funciones del tipo (5.1) y eligiendo 





entonces _φ_<sup>ˆ</sup> autom´aticamente satisface las condiciones de borde chapV-19 para todos los valores de _am_ . Aplicando el operador diferencial a la funci´on aproximante (5.1) y asumiendo que las funciones de prueba y sus derivadas son continuas tenemos: 



Aqu´ı se requiere que hasta la segunda derivada sea continua. Cuando en las pr´oximas secciones analicemos el m´etodo de los elementos finitos veremos como estas restricciones ser´an debilitadas. La forma en la cual hemos construido la aproximaci´on garantiza el cumplimiento de las condiciones de borde 

**132** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

y entonces nos queda que _φ_<sup>ˆ</sup> debe satisfacer solo la ecuaci´on diferencial en el interior del dominio. Sustituyendo _φ_<sup>ˆ</sup> en (5.18) : 



obtenemos el residuo de la misma con _L_ asumido un operador lineal. Una vez definido el residuo aplicamos el m´etodo de los residuos ponderados 



Esta ecuaci´on contiene _M_ inc´ognitas, entonces aplicando esta misma ecuaci´on para _l_ = 1 _,_ 2 _, . . . , M_ se obtiene un sistema de ecuaciones algebraicas que pueden ser escritas en forma compacta como: 



El procedimiento requiere calcular los coeficientes de las matriz y del miembro derecho y luego invertir el sistema para calcular los coeficientes con los cuales se obtiene la soluci´on aproximada al operador diferencial de (5.18). Ya que las funciones de prueba elegidas para aproximar la soluci´on tienen soporte global entonces la matriz de coeficientes ser´a llena y no tendr´a estructura de banda, t´ıpica de los m´etodos de diferencias finitas y elementos finitos. Adem´as, en lo anterior nada se ha dicho acerca de la elecci´on de las funciones de peso con lo cual uno puede aplicar todo lo anterior a las distintas alternativas mostradas en secciones anteriores. 

A modo de ejemplo calcularemos la soluci´on al siguiente problema de valores de contorno unidimensional: 

**Ejemplo 1D** Hallar _φ_<sup>ˆ</sup> soluci´on aproximada de la siguiente ecuaci´on diferencial 



De acuerdo a las definiciones generales presentadas antes las condiciones de borde y las funciones de prueba elegidas son: 



[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 



Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

La elecci´on de _ψ_ y _Nm_ es arbitraria, existen muchas otras posibles alternativas a estas pero aqu´ı usaremos la base trigonom´etrica. Aplicando el m´etodo de los residuos ponderados y la definici´on de los coeficientes de la matriz y el vector del miembro derecho tenemos: 



Si tomamos _M_ = 2 dos t´erminos en la expansi´on y si aplicamos el m´etodo de colocaci´on puntual obtenemos la siguiente matriz: 



mientras que si aplicamos Galerkin en virtud de la ortogonalidad de las funciones de prueba, 



tenemos: 



La soluci´on num´erica del sistema de ecuaciones resultante da: 



La soluci´on exacta a este problema es del tipo 



La rutina Ej ~~2 1~~ contiene la resoluci´on de este ejemplo. 

La figura (5.3) muestra a la derecha la solucion exacta, la aproximada por Galerkin y la de colocaci´on a la cual se le ha removido la funci´on _ψ_ = _x_ para poder notar mejor las diferencias. A la izquierda vemos una distribuci´on puntual del error donde se alcanza a notar, para este ejemplo, una mejor aproximaci´on obtenida mediante el m´etodo de Galerkin. 

**134** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

**Ejemplo 2D** La ecuaci´on que gobierna la torsi´on el´astica de barras prism´aticas es: 



donde _G_ es el m´odulo el´astico de torsi´on, _θ_ es el ´angulo que se gira la secci´on y _φ_ equivale a una funci´on tensi´on que de acuerdo a la teor´ıa es nula en todo el contorno. Detalles acerca de la forma que se obtiene esta ecuaci´on pueden verse en libros sobre teor´ıa de la elasticidad, como por ejemplo Timoschenko [Ti]. Esta ecuaci´on tiene la estructura de una ecuaci´on de Poisson y analog´ıas con otros experimentos gobernados por la misma ecuaci´on pueden hacerse. Por ejemplo la anterior tambi´en surgur´ıa si queremos resolver un problema de conducci´on del calor con una fuente aplicada en todo el vol´umen del material asumiendo que en la direcci´on _z_ la barra es infinita y la temperatura del contorno est´a fija a un valor de referencia. 

Supongamos que en este ejemplo _Gθ_ = 1, con lo cual la ecuaci´on a resolver se transforma en: 



Aqu´ı apelamos a la intuici´on. Siendo el problema sim´etrico respecto a los ejes _x_ e _y_ deber´ıamos elegir funciones de prueba que tengan esta propiedad y satisfagan las condiciones de contorno. Por ejemplo, si tomamos _ψ_ = 0 y usamos 3 t´erminos una elecci´on posible ser´ıa: 



La rutina Ej ~~2~~ 2 muestra el aspecto que tienen estas tres funciones donde se alcanza a apreciar la paridad deseada. 

De esta forma aplicando la aproximaci´on (5.1), comparando (5.18) con (5.34) y usando la definici´on de la matriz y el vector derecho del sistema algebraico (5.9) que permite calcular los coeficientes _am_ tenemos: 



Como vemos, ahora las integrales a calcular son bidimensionales por lo que debe estimarse con m´as detalle la forma de realizar el c´alculo. Nosotros aqu´ı solo deseamos mostrar la metodolog´ıa a usar y en este caso estas integrales las realizaremos a mano. Cuando se pretende volcar estos conceptos en un programa para fines de c´alculo intensivo deben adoptarse m´etodos m´as eficientes y generales para tal fin, como por ejemplo la integraci´on num´erica, tema que veremos m´as adelante cuando abordemos el estudio del m´etodo de los elementos finitos . Analizando (5.37) vemos que la derivada segunda de funciones tipo cosenos generan funciones cosenos, y considerando la ortogonalidad de estas bases las integrales en (5.37) se simplifican notablemente. 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

**135** 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

La rutina Ej ~~2~~ 2 contiene el c´alculo de este ejemplo donde se puede apreciar la forma de calcular la matriz (diagonal) y el miembro derecho del sistema. En este caso se ha empleado una resolucion anal´ıtica de las integrales. La rutina mejorada Ej ~~2 2~~ b muestra como puede emplearse una rutina de integraci´on num´erica con el fin de evitar tediosos calculos. 

La figura (5.4) muestra en la parte superior la soluci´on obtenida con la mencionada rutina en la cual se incluye el valor de la tensi´on m´axima que es de 3.103, cercano al te´orico de 2.96 5 % de error. 

Para terminar esta secci´on mencionamos que el m´etodo de los cuadrados m´ınimos aplicado a la resolucion de ecuaciones a derivadas parciales no es equivalente al m´etodo de los residuos ponderados de Galerkin. Para ver esto tomemos como antes el funcional definido como: 







o sea la funci´on de peso que surge del m´etodo de los cuadrados m´ınimoses equivalente al operador diferencial del problema aplicado a las funciones de prueba. En algunas circumstancias este tipo de aproximaci´on es deseable mientras que en algunos casos no. 

###### **Funciones de prueba que no satisfacen las condiciones de contorno** 

Hasta aqu´ı hemos considerado aproximaciones elegidas de forma tal de satisfacer las condiciones de contorno. Esto muchas veces puede ser dificultoso y antes esto es preciso relajar tal requisito. Para poder elegir las funciones de prueba independientemente de las condiciones de contorno postulamos una expansi´on del tipo: 



que no satisface las condiciones de contorno. Entonces el residuo en el interior del dominio ( _R_ Ω) es suplementado por otro en el borde ( _R_ Γ): 



En este caso el m´etodo de los residuos ponderados consiste en escribir: 



[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 



Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

con _Wl_ y _Wl_ elegidas en forma arbitraria e independiente. Reemplazando (5.40) en (5.41) llegamos a la definici´on del siguiente sistema de ecuaciones: 



Para ilustrar el procedimiento tomaremos el ejemplo 1D anteriormente presentado. 

**Ejemplo 1D (chapV-26) versi´on 2** Aqu´ı resolveremos el mismo problema presentado en (5.26) con la diferencia que usaremos como funciones de prueba la base _Nm_ = _x_<sup>_m−_1</sup> _, m_ = 1 _,_ 2 _, . . ._ 

En este caso simple la integral de borde en (5.41) se reduce a la evaluaci´on del integrando en los dos puntos extremos de este dominio definido por el intervalo [0 _,_ 1]. Entonces 



En este ejemplo usaremos para el <u>peso</u> en el interior del dominio el m´etodo de Galerkin _Wl_ = _Nl_ mientras que para el peso en el borde _Wl_ = _−Nl|_ Γ, entonces: 



Si usamos una expasi´on en tres t´erminos se llega a la siguiente matriz: 



La soluci´on a este problema es: 



**Ejemplo 2D - versi´on 2** Usando como aproximaci´on la siguiente 



es obvio ver que la misma satisface las condiciones de contorno en _y_ = _±_ 2, mientras que la condici´on _x_ = _±_ 3 debe incluirse en el c´alculo. 

Tomando (5.40) y (5.42) y reemplazando la anterior expresi´on vemos que: 



[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

Usando _Wl_ = _Nl_ y _Wl_ = _Nl|_ Γ se llega a armar el sistema de ecuaciones. La rutina Ej ~~2 3~~ muestra una forma de resolver este problema apelando a las capacidades de c´alculo simb´olico de MatLab. Se recomienda editar y leer esta rutina para entender la metodolog´ıa que es extensible a otros ejemplos utilizando diferentes funciones de base. 

La figura (5.4) en la parte inferior muestra la soluci´on num´erica obtenida donde se alcanza a ver que la condici´on de contorno en _y_ = _±_ 2 se satisface exactamente pero aquella en _x_ = _±_ 3 se cumple solo aproximadamente. Esta es una de las diferencias entre las dos metodolog´ıas propuestas. Adem´as la tensi´on m´axima es un poco superior a la obtenida con la primera metodolog´ıa alej´andose un poco m´as del valor te´orico. La figura chapV-4 en la parte inferior derecha muestra la variaci´on de la tensi´on a lo largo del contorno _x_ = _±_ 3 en funci´on de la coordenada _y_ . 

##### **5.1.4. Condiciones de contorno naturales** 

Como hemos visto en la secci´on anterior es posible facilitar la selecci´on de las funciones de prueba sin necesidad de que satisfagan las condiciones de contorno a expensas de un trabajo algebraico mayor y de una degradaci´on en la calidad de la soluci´on. El primer item est´a relacionado con la resoluci´on de las integrales que permiten el c´alculo de los coeficientes. En (5.42) vemos que adem´as de las integrales en el interior tenemos la necesidad de evaluar integrales en el contorno del dominio, las cuales pueden contener operadores diferenciales que complican a´un m´as la situaci´on. Aqu´ı veremos que existen ciertas condiciones de contorno las cuales surgen como las naturales al problema, en el sentido que permiten cierta cancelaci´on de t´erminos cuando el problema se expresa en su forma d´ebil. Supongamos que aplicamos el m´etodo de los residuos ponderados al problema definido en (5.18) . 



La _forma d´ebil_ de la anterior formulaci´on integral se obtiene mediante la integraci´on por partes que en su versi´on general puede escribirse como: 



donde _C, D, E_ son operadores diferenciales lineales involucrando ´ordenes de derivaci´on inferiores a la del operadores _L_ . Usando (5.40) y (5.49) en (5.41) se llega a: 



donde lo que se pretende es anular las contribuciones al contorno del miembro izquierdo , o sea: 



Un ejemplo de condiciones de contorno natural que com´unmente se tiene en las aplicaciones es la especificaci´on de un flujo impuesto en el contorno. Pensando en el problema t´ermico podemos 

**138** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

imaginar que extraemos calor del contorno de una pieza con una magnitud _<u>q</u>_ especificada. En esos casos la condici´on de contorno viene expresada como: 



Si hechamos un vistazo a (5.40) vemos que _M_ = _∂n∂_<sup>ysiloqueestamosresolviendoeslaecuaci´on</sup> de conducci´on t´ermica en ese caso el operador _E_ = _∂n∂_<sup>=</sup><sup>_M_,porlocual</sup> _Wl_ = _−Wl_ satisface (5.51) simplificando (5.50) a: 



En lo anterior hemos utilizado el teorema de Green o su equivalente, la f´ormula de integraci´on por partes. Una versi´on un poco m´as detallada del mismo aplicada a un caso sencillo expresa que: 



con _α_ y _β_ funciones escalares. A pesar que (5.54) incluye solo derivadas de primer ´orden, la t´ecnica es bien general como lo expresa chapV-46 e incluso se extiende al caso de funciones vectoriales. No obstante en la mayor´ıa de las aplicaciones los operadores que se trabajan son de relativo bajo ´orden. 

##### **5.1.5. M´etodos de soluci´on del contorno** 

Hasta aqu´ı los m´etodos empleados resolv´ıan el problema en el interior del dominio pudiendo trabajar con funciones de prueba que satisfagan o no las condiciones de contorno . Si en lugar de elegir funciones de prueba que satisfagan las condiciones de contorno elegimos aquellas que satisfacen el operador diferencial en el interior del dominio el problema se reduce a resolver solo el residuo en el contorno. Este tipo de estrategia di´o lugar al _m´etodo de los paneles_ y al _m´etodo de los elementos de contorno_ . De esta forma como las funciones de prueba satisfacen el operador diferencial en el interior entonces: 



con lo cual la definici´on del m´etodo de los residuos ponderados (chapV-38) se reduce simplemente a: 



Un solo conjunto de funciones de prueba _Wl_ , definidas solamente sobre el borde del dominio deben definirse. Adem´as como el problema se plantea sobre el contorno la dimensi´on espacial se reduce en una unidad con lo cual problemas en 3D se transforman en bidimensionales y aquellos en 2D en unidimensionales. Estas ventajas tiene su contracara en la dificultad de elegir funciones de prueba que satisfagan el operador diferencial en el interior del dominio. Este es el principal limitante de esta t´ecnica que se muestra atractiva por todo lo que implica reducir la dimensi´on espacial. Una de las aplicaciones m´as divulgadas de esta t´ecnica es la resoluci´on de problemas gobernados por la ecuaci´on de Laplace, por ejemplo: conducci´on del calor, flujo potencial, elasticidad lineal, y otros. La raz´on es que 

**139** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

si pensamos en funciones anal´ıticas de variable compleja _z_ = _x_ + _iy_ , estas satisfacen autom´aticamente la ecuaci´on de Laplace. Supongamos una funci´on anal´ıtica del tipo: 



luego, 







Por ejemplo tomando la funci´on anal´ıtica 



Todas las funciones _u_ y _v_ que surgen de (5.59) satisfacen la ecuaci´on de Laplace siendo todas ellas candidatas para integrar las funciones de prueba con las cuales armar una funci´on aproximante que satisfaga este problema en particular en el interior del contorno. El siguiente ejemplo muestra una aplicacion del m´etodo de los elementos de contorno al problema de la torsi´on de una viga. 

##### **5.1.6. Sistema de ecuaciones diferenciales** 

El m´etodo de los residuos ponderados en cualquiera de sus versiones puede ser extendido para tratar el caso de sistemas de ecuaciones diferenciales . Un sistema de ecuaciones diferenciales surge cuando en el modelo matem´atico se pretende resolver campos vectoriales en una o varias dimensiones espaciales o cuando se pretenden acoplar varios campos escalares y/o vectoriales tanto en una como en varias dimensiones espaciales. En esos casos la soluci´on a obtener viene representada por un vector 



que debe satisfacer ciertas ecuaciones diferenciales, una por cada componente del vector inc´ognita 



la cual en forma compacta puede escribirse como 



[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 



Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

Del mismo modo con las ecuaciones en el contorno 



Para cada componente del vector necesitamos definir una aproximaci´on del tipo (5.1) , que escrita en forma compacta se expresa como: 



donde **N** _m_ es una matriz diagonal donde en cada t´ermino de la diagonal se halla la funci´on de prueba de cada componente del vector inc´ognita. Del mismo modo las funciones de peso, tanto para la integral sobre el interior del dominio como para la del contorno son tambi´en matrices diagonales. De esta forma la extensi´on del m´etodo de los residuos ponderados escalar aplicado al caso vectorial es directa. 



La mayor´ıa de los casos de inter´es tanto en la industria como en la ciencia involucran sistemas de ecuaciones diferenciales . 



Los problemas de elasticidad bidimensional est´an generalmente formulados en dos variables, los desplazamientos _u, v_ seg´un las componentes _x_ e _y_ respectivamente. Los problemas de flujo viscoso incompresible tridimensional vienen muchas veces expresados en t´ermino de las variables primitivas del problema, las tres componentes de la velocidad y la presi´on. No obstante en 2D muchos prefieren la formulaci´on vorticidad _ω_ , funci´on de corriente _ψ_ que desde el punto de vista computacional tiene una implementaci´on m´as f´acil y no requiere un tratamiento especial de la incompresibilidad como lo necesita la formulaci´on en variables primitivas. El caso de flujo compresible 3D tiene un vector inc´ognita con 5 componentes. Esta es solo una breve descripci´on de algunos de los casos t´ıpicos donde se necesita resolver un sistemas de ecuaciones diferenciales . El agregado de modelos adicionales, por ej. turbulencia u otros, muchas veces tambi´en agrega componentes al vector inc´ognita. Por ´ultimo en pos de reducir el ´orden de una ecuaci´on diferencial se puede transformar la misma en un sistemas de ecuaciones diferenciales donde el orden se ha reducido completamente equivalente al original. 

##### **5.1.7. Problemas no lineales** 

Muchos problemas pr´acticos modelados f´ısicamente producen tanto ecuaciones diferenciales como condiciones de contorno que son no lineales. Esta no linealidad se expresa porque existe una dependencia de los operadores, tanto el del interior como el del contorno, con la variable de estado o funci´on 

**141** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

inc´ognita. Dado que en todas las secciones anteriores hemos considerado la aplicaci´on del m´etodo de los residuos ponderados al caso lineal se hace necesario hacer algunos comentarios respecto al caso no lineal. El m´etodo de los residuos ponderados es completamente aplicable al caso no lineal. Supongamos que queremos resolver un problema de conducci´on del calor donde la conductividad depende de la misma temperatura. La ecuaci´on de gobierno puede escribirse como: 



Planteando una aproximaci´on del tipo (5.1) , introduciendo la misma en la formulaci´on por residuos ponderados de (5.67) produce un sistema de ecuaciones algebraico no lineales del tipo: 



que puede resolverse iterativamente en la forma: 



Adem´as del caso de la ecuaci´on de conducci´on no lineal existen muchos otros problemas de inter´es a mencionar como el caso de la ec. de B¨urgers, el caso de la ecuaci´on de flujo viscoso incompresible expresada en una formulaci´on _ψ − ω_ donde la nolinealidad se halla en las condiciones de contorno. Obviamente las ecuaciones de flujo compresible e incompresible expresada en las variables primitivas o conservativas son tambi´en ejemplos claros de sistemas de ecuaciones diferenciales no lineales. 

**142** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 



<!-- Start of picture text -->
1<br>0.8<br>0.6<br>e_Gal = 0.001596<br>0.4<br>e_Col = 0.004067<br>0.2<br>0<br>0.01 0.008 0.006 0.004 0.002 0<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>0.07 0.06 0.05 0.04 0.03 0.02 0.01 0<br><!-- End of picture text -->

Figura 5.3: Soluci´on aproximada a una ODE mediante residuos ponderados 

**143** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 



<!-- Start of picture text -->
max(|tau|) = 3.103<br>4<br>3<br>2<br>1<br>0<br>2<br>4<br>0 2<br>0<br>−2<br>−2 −4<br><!-- End of picture text -->

Funciones de prueba que satisfacen las condiciones de contorno 



<!-- Start of picture text -->
max(|tau|) = 3.217<br>φ 0.2<br>4 0.1<br>3<br>0<br>2<br>−0.1<br>1<br>−0.2<br>0<br>−1 −0.3<br>−2 −1 0 1 2<br>2<br>5<br>0<br>0 y<br>−2 −5<br>Solucion en x=3<br><!-- End of picture text -->

Funciones de prueba que no satisfacen las condiciones de contorno 

Figura 5.4: Torsi´on de una barra prism´atica 

**144** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

##### **5.1.8. Conclusiones** 

En esta primera parte de este cap´ıtulo que trata acerca de diferentes t´ecnicas num´ericas de discretizaci´on hemos presentado el caso del m´etodo de los residuos ponderados aplicado a la resoluci´on de ecuaciones a derivadas parciales utilizando para aproximar un conjunto de funciones de prueba definidas globalmente, satisfaciendo o no las condiciones de contorno, de f´acil extensi´on al caso de sistemas de ecuaciones diferenciales y al caso no lineal. No obstante, como se desprende de los ejemplos incluidos la elecci´on de dichas funciones no es tarea f´acil, incluso no es extensible al caso de geometr´ıas arbitrarias si uno requiere que dichas funciones satisfagan las condiciones de contorno exactamente. Adem´as, a medida que se aumenta el grado de la aproximaci´on el condicionamiento del sistema lineal a resolver se vuelve cr´ıtico salvo que se usen funciones base con mayor grado de ortogonalidad. Esto se logra mediante el uso de polinomios de Legendre o de Chebyshev. En realidad estos son muy frecuentemente utilizados en el contexto de los _m´etodos espectrales_ el cual en forma indirecta ha sido el tema de esta secci´on (5.1) . Este tema dar´ıa para una secci´on aparte pero por el momento diferimos un tratamiento m´as detallado para futuras versiones de estas notas. En las pr´oximas secciones trataremos de relajar algunas de las limitaciones de esta t´ecnica, en especial aquella relacionada con el tratamiento de dominios de forma arbitraria, presentando primero el m´etodo de los elementos finitos y posteriormente el m´etodo de los vol´umenes finitos . 

**145** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

##### **5.1.9. TP.chapV– Trabajo Pr´actico #2** 

1. Tome la rutina Ej ~~2 0~~ .m y transf´ormela para ser usada con funciones de prueba del tipo _Nm_ = sin( _mπx_ ). Comience con _M_ = 2 y ref´ınelo para testear la convergencia de la aproximaci´on. 

2. Demuestre que la aproximaci´on por residuos ponderados del tipo Galerkin, tomando como funciones de prueba la base _Nm_ = sin( _mπx/Lx_ ) conduce a un sistema de ecuaciones con una matriz diagonal. 

3. Un ensayo experimental sobre la deflecci´on _u_ ( _x, y_ ) de una placa cuadrada de lado unitario con todo su contorno empotrado dio como resultado los valores que se muestran en la figura. 



<!-- Start of picture text -->
X X X<br>X X X<br>∆x<br>X X X<br>y∆<br><!-- End of picture text -->

Figura 5.5: Ej. 3 Torsi´on de una barra 

Aproximar la deflecci´on mediante 



y usando el m´etodo de los residuos ponderados estimar los coeficientes _alm_ . _Ayuda: las integrales que aparecen del c´alculo de los coeficientes pueden resolverse mediante integraci´on num´erica usando regla del trapecio bidimensional_ 

4. Mediante el uso de un adecuado conjunto de funciones de prueba aproxime la funci´on _φ_ = 1 + sin( _πx/_ 2) en el rango 0 _≤ x ≤_ 1. Utilice colocaci´on puntual, colocaci´on por subdominios y el m´etodo de Galerkin e investigue num´ericamente la convergencia de las sucesivas aproximaciones. 

5. La rutina Ej ~~2~~ 1 contiene la resoluci´on del problema de valores de contorno presentado en las 

**146** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

notas te´oricas: 



El mismo se ha usado con _M_ = 2 t´erminos en la expansi´on. Pruebe de modificar la cantidad de t´erminos y trace una curva donde se muestre la convergencia de cada uno de los m´etodos. 

6. Resuelva el ejercicio anterior pero utilizando como conjunto de funciones de prueba la base _Nm_ = _x_<sup>_m_</sup> (1 _− x_ ). Construya una rutina en base a la Ej ~~2 1~~ para resolver este problema y muestre la convergencia de la misma. Saque conclusiones respecto a los obtenido en este ejercico y el anterior. 

7. Utilizando como base la rutina Ej ~~2 2~~ realice las modificaciones necesarias para realizar un estudio de convergencia de la aproximaci´on. Tenga en cuenta de mantener la simetr´ıa en la elecci´on de las funciones de prueba y utilice las propiedades de ortogonalidad para calcular la matriz de coeficientes. 

8. Utilice el m´etodo de los residuos ponderados aplicado al residuo en el dominio interior y agregado el proveniente del contorno para resolver el problema de la torsi´on de la barra definido en la teor´ıa. Utilice una expansi´on del tipo 



que satisface la condici´on de contorno en _y_ = _±_ 2 pero no satisface aquella en _x_ = _±_ 3. Elija _Wl_ = _Nl_ y _Wl_ = _Nl|_ Γ y obtenga el sistema de ecuaciones a resolver y la soluci´on. Estudie la convergencia dl residuo al tomar diferente cantidad de t´erminos en la expansi´on arriba presentada. _Sugerencia: Realice un programa del tipo Ej_ _~~2 2~~ para el mismo y para resolver las integrales use integraci´on num´erica_ 

9. **Condiciones de contorno naturales** Resolver el problema de conducci´on t´ermica estacionaria 



usando como funci´on aproximante 



Utilice la rutina Ej 2 ~~3~~ para este fin. 

**147** 

[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 

Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

10. **M´etodo de los elementos de contorno - Torsi´on de una viga.** 

El problema de la torsi´on de una viga definido en la teor´ıa 



puede ser transformado a una ecuaci´on de Laplace mediante la siguiente igualdad: 



Usando el m´etodo de los residuos ponderados aplicado solo al contorno y la siguiente base de funciones 



hallar la soluci´on aproximada _φ_<sup>ˆ</sup> y compararla con la obtenida por el m´etodo de los residuos ponderados aplicado al interior. 

11. **Sistema de ecuaciones diferenciales** 

El problema de conducci´on t´ermica 



puede descomponerse en un sistema de dos ecuaciones diferenciales de primer orden del tipo: 



siendo el vector inc´ognita **_φ_** = . Usando la aproximaci´on: � _φq_ � 



calcular la soluci´on a este problema usando dos t´erminos. 

12. **Ejemplo : Problemas no lineales** 

Resolver la ecuaci´on no lineal 



[Document version: curso-0.3.0. File version: $Id: tema4.tex,v 1.12 2005/05/22 23:57:06 mstorti Exp $] 



Cap´ıtulo 5. T´ecnicas de discretizaci´on _Secci´on 5.1. M´etodo de los residuos_ _<u>ponderados</u>_ 

usando como funciones de prueba la base _Nm_ = _x_<sup>_m_</sup> (1 _− x_ ) con dos t´erminos mediante un m´etodo de los residuos ponderados por colocaci´on puntual. 

**149** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

## **Cap´ıtulo 6** 

# **M´etodo de los elementos finitos** 

#### **6.1. Introducci´on** 

El m´etodo de los residuos ponderados presentado en el cap´ıtulo anterior sirvi´o como una teor´ıa unificadora de una gran cantidad de m´etodos num´ericos a la vez que en s´ı mismo puede concebirse como una t´ecnica num´erica en particular. Esa t´ecnica com´unmente denominada _m´etodo espectral_ goza de ciertas ventajas siendo su principal desventaja la de estar muy restringida a dominios con geometr´ıas muy simples como zonas rectangulares, paralelep´ıpidos u otras mapeables a las anteriores. Este no es el caso que m´as interesa a los ingenieros de las ´ultimas d´ecadas los cuales requieren herramientas computacionales de c´alculo que permitan tratar dominios arbitrarios. Si bien en el procedimiento antes empleado uno planteaba la aproximaci´on de forma tal de satisfacer las condiciones de contorno, hemos visto que existe la posibilidad de elegir funciones m´as generales que no satisfacen las condiciones de contorno y para las cuales un m´etodo de los residuos ponderados que incluya el residuo en el contorno debe plantearse. Esto provocaba la aparici´on de integrales adicionales sobre el contorno de dif´ıcil tratamiento anal´ıtico. En los m´etodos empleados en el cap´ıtulo anterior trabajamos en el espacio transformado en lugar que en el espacio f´ısico y esto puede verse de inmediato si pensamos que el vector de inc´ognitas **a** = _{a_ 1 _, a_ 2 _, . . . , aM }_ representan las amplitudes de diferentes componentes ondulatorias de la soluci´on y no el valor de la inc´ognita del problema en cada posici´on de la malla. Una idea explorada en los ´ultimos tiempos es la de trabajar con m´etodos espectrales pero en el dominio f´ısico del problema. Entonces para poder aplicar todo lo anterior es necesario hacer una transformaci´on al dominio de la frecuencia para luego volver al dominio f´ısico con la soluci´on del problema. Trabajar en el dominio f´ısico del problema permite descomponer espacialmente el problema asi como el m´etodo espectral lo descompone en el espacio de las frecuencias. Esta descomposici´on del dominio en pedazos (elementos, vol´umenes, celdas, etc) de tama˜no finito le confiere el nombre al m´etodo. Aqu´ı esta la _gran idea_ en torno a estas t´ecnicas las cuales no requieren demasiado trabajo para especificar las funciones de prueba ya que al ser de soporte compacto aproximan bien la mayor´ıa de las funciones a´un siendo de bajo orden. A su vez las integrales a calcular para obtener los coeficientes de la matriz y del vector miembro derecho son integrales sobre elementos que tienen una forma completamente mapeable a un cuadrado o cualquier otra figura geom´etrica simple (tri´angulos) lo cual permite su c´alculo en forma muy sencilla, tanto anal´ıticamente como mediante cuadratura num´erica. En cuanto a las condiciones de contorno estas presentan un tratamiento mucho m´as simple debido a que las 

150 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.1. Introducci´on_ 

variables sobre las cuales se especifican coinciden con las variables a calcular. Diferente era el caso de los m´etodos espectrales en los cuales las condiciones de contorno se especifican sobre las variables del problema siendo la inc´ognita las amplitudes de su descomposici´on espectral. Esto motivaba tener que elegir adecuadamente a priori las funciones de prueba antes de realizar el c´alculo. No obstante esto, la selecci´on de una t´ecnica num´erica no es una cosa obvia. Los m´etodos espectrales sirven y son insuperables para algunas aplicaciones donde el fen´omeno f´ısico requiere alto orden de precisi´on y la geometr´ıa no presenta dificultades, mientras que los m´etodos localizados son m´as aplicables a los casos donde no interesa entrar en demasiado detalle de la soluci´on pero el dominio del problema es muy complicado. 

Resumiendo, vimos que el m´etodo de los residuos ponderados consiste en aproximar la soluci´on mediante 



definida a lo largo de todo el dominio Ωy las integrales 



se eval´uan mediante una sola operaci´on y sobre todo el dominio. La ida alternativa consiste en dividir la regi´on Ωen un n´umero de subdominios o elementos Ω<sup>_e_</sup> sin solapamiento y que cubran todo el dominio, de forma que la aproximaci´on _φ_<sup>ˆ</sup> se construya _a pedazos_ o _a trozos_ sobre cada subdominio. Expresando matem´aticamente lo anterior, 



De esta forma las integrales IV.38 se pueden calcular agregando la contribuci´on a la integral proveniente de cada elemento, 



donde Γ<sup>_e_</sup> es el borde del elemento que cae sobre alg´un borde del dominio Γ y es tal que _∪e_ Γ<sup>_e_</sup> = Γ. _E_ denota la cantidad total de elementos en la partici´on. Si se usan elementos de forma simple y si la definici´on de las funciones de forma permite un c´alculo de manera repetitiva entonces es posible tratar dominios con formas completamente arbitrarias con facilidad. Es de notar que el m´etodo de los residuos ponderados al estilo del presentado en el cap´ıtulo anterior equivale a hacer lo mismo pero sobre un solo elemento que coincide con el dominio Ω. La definici´on a trozos de la aproximaci´on introduce ciertas discontinuidades en la soluci´on o en alguna de sus derivadas. Cierto grado de discontinuidad es permisible y esto limita fuertemente la formulaci´on a emplear. Por otro lado el hecho de que las funciones de prueba se elijan a trozos provoca un beneficio computacional importante respecto a la 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

**151** 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.2. Funciones de forma locales de soporte compacto_ 

estructura de la matriz resultante. Un funci´on a trozos en general tiene un soporte compacto, o sea esta no es nula solo en una regi´on peque˜na del dominio abarcando algunos pocos elementos del mismo. Esto produce matrices con estructura de banda lo cual tratada convenientemente puede reducir much´ıismo el costo computacional de obtener una soluci´on. Esto lo veremos en m´as detalle m´as adelante al tratar el problema de la resoluci´on num´erica del sistema de ecuaciones. Nosotros ya hemos pasado por una situaci´on similar al resolver el sistema de ecuaciones para calcular los coeficientes **a** en el cap´ıtulo anterior. All´ı˜no hemos tenido mayor dificultad tanto porque los sistemas eran de un tama˜no chico y adem´as porque la matriz era completamente llena en cuyo caso recurr´ımos directamente a una especie de eliminaci´on gaussiana. Ya veremos que esto no es admisible en especial en problema con gran n´umero de inc´ognitas (sistemas de ecuaciones en 3D). Esta es otra de las grandes diferencias entre los m´etodos locales y aquellos globales, la resoluci´on del sistema de ecuaciones. 

#### **6.2. Funciones de forma locales de soporte compacto** 

Para ilustrar lo anterior consideremos la aproximaci´on de una funci´on _φ_ ( _x_ ) en el espacio unidimensional definido por Ω= [0 _, Lx_ ]. 

###### Figura 6.1: Aproximaci´on por funciones a trozos 

La divisi´on de Ωen _E_ (= _Mn −_ 1) subregiones no solapadas se determina estableciendo un adecuado conjunto de puntos _{xl_ ; _l_ = 1 _,_ 2 _, . . . , Mn}_ en Ωcon _xl_ = 0 y _xMn_ = _Lx_ definiendo el elemento Ω<sup>_e_</sup> como el intervalo _xe ≤ x ≤ xe_ +1. Como vemos la funci´on a trozos usada para aproximar la funci´on _φ_ es constante a trozos, constante dentro de cada elemento coincidiendo su valor con el de la funci´on _φ_ en el centro de cada elemento, lo cual equivale a hacer colocaci´on en esos puntos, com´unmente llamados los nodos. En este ejemplo tan sencillo la numeraci´on es obvia. Siendo la funci´on aproximante constante a trozos la funci´on de prueba que da or´ıgen a la misma es una funci´on que vale: 



A nivel global la funci´on aproximante que resulta es: 



De esta forma la aproximaci´on se escribe como: 



donde _φm_ es el valor de la funci´on en cada nodo _m_ de la malla (el centro del elemento) y reemplazaa _am_ la amplitud de cada componente espectral en el m´etodo de los residuos ponderados presentado en el cap´ıtulo anterior. Esto ya fue comentado previamente y tiene la ventaja que en este caso los 

**152** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.2. Funciones de forma locales de soporte compacto_ 

coeficientes a calcular tienen un significado f´ısico m´as directo con el problema. La funci´on _ψ_ ha sido omitida por lo que la aproximante no coincidir´a con el valor especificado en el borde aunque por un proceso de refinamiento se puede llegar tan cerca como se quiera a satisfacer los mismos. Sobre cualquier elemento _e_ la aproximaci´on global puede expresarse en t´erminos del valor _φe_ y de la funci´on de forma del elemento _N_<sup>_e_</sup> como: 



Otro tipo de aproximaci´on de frecuente uso y que mejora la anterior es la que surge de emplear funciones de forma lineales. Estas funciones de forma desde el punto de vista global asumen 



con una variaci´on lineal entre los valores mencionados. Esto puede construirse a nivel elemental si por cada elemento definimos dos funciones de forma, una por cada nodo del elemento. Ahora el concepto de nodo ya no coincide como antes con el centro del mismo sino que ahora se ubican en los extremos del intervalo que define al elemento. Estos son ahora los puntos de colocaci´on. La figura 6.2 muestra graficamente lo que recien se acaba de mencionar. 

Figura 6.2: Aproximaci´on por funciones a trozos 

La aproximaci´on global para este caso es: 



donde a diferencia del caso anterior la suma se extiende a _Mn_ puntos, los nodos de esta malla. Es de remarcar que esta aproximaci´on satisfar´a autom´aticamente los valores en el contorno _x_ = 0 _, x_ = _Lx_ sin necesidad de agregar una funci´on _ψ_ ya que ahora los puntos de colocaci´on est´an justamente sobre los extremos de los elementos y para el caso del primer y ´ultimo elemento estos coinciden con los extremos del dominio donde se agregan las condiciones de contorno . Sobre cualquier elemento _e_ con nodos _i, j_ la aproximaci´on toma el valor: 



siendo la variaci´on en el interior del elemento lineal por ser lineales las funciones de prueba _Ni, Nj_ . Los dos conjutnos de funciones de prueba usados, aquellos constantes a trozos y los lineales a trozos forman un conjunto completo en el sentido que refinando la partici’on se obtienen soluciones con cada vez mayor precisi´on. A su vez estas funciones son generalizables a varias dimensiones como puede verse en la figura 6.3. 

**153** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.2. Funciones de forma locales de soporte compacto_ 

Figura 6.3: Funciones a trozos en varias dimensiones 

**154** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.3. Aproximaci´on a soluciones de ecuaciones diferenciales. Requisitos sobre la continuidad de las funciones de forma_ 

A su vez es posible tanto aplicar un m´etodo de los residuos ponderados de colocaci´on como uno tipo Galerkin. En el primer caso las integrales se pesan con distribuciones tipo _delta de dirac_ en los nodos, ya sea en el centro del elemento como en sus extremos. En el caso de la formulaci´on de Galerkin las funciones de peso coinciden con las de interpolaci´on dando resultados distintos pero equivalentes. Al igual que en el cap´ıtulo anterior el m´etodo de los residuos ponderados puede aplicarse para aproximar una funci´on como para resolver una ecuaci´on diferencial. El primero es un caso particular del segundo donde el operador _L_ es la identidad. Los detalles del procedimiento incluido en el m´etodo de los elementos finitos se ver´an en pr´oximas secciones cuando resolvamos algunos ejemoplos en particular. 

#### **6.3. Aproximaci´on a soluciones de ecuaciones diferenciales. Requisitos sobre la continuidad de las funciones de forma** 

El m´etodo de los residuos ponderados aplicado a la resoluci´on de una ecuaci´on diferencial del tipo: 



con condiciones de contorno 



se escribe como 



con 



La idea de usar un m´etodo num´erico basado en aproximar una soluci´on mediante funciones de forma locales plantea el interrogante de si es posible su uso sabiendo que tanto la funci´on como alguna de sus derivadas pueden ser discontinuas. 

###### Figura 6.4: Continuidad de las funciones de forma 

Para ilustrar la explicaci´on observemos la figura 6.4 donde se presentan tres tipos de funciones, la de la izquierda es discontinua con derivada puntualmente no acotada, la del centro continua con derivada primera discontinua y derivada segunda puntualmente no acotada y aquella de la derecha que es continua y tiene primera derivada continua, segunda derivada discontinua y tercera derivada puntualmente no acotada. Pensemos que estas funciones pueden ser posibles candidatos a ser usados como funciones de forma para nuestro m´etodo num´erico. El hecho que alguna de las derivadas presente una singularidad puede provocar problemas en el c´omputo de las matrices por lo cual se debe evitar su uso. Para ello si los operadores involucrados en el c´alculo de las matrices contienen derivadas de orden _s_ entonces debemos garantizarnos que las funciones de forma tengan _s −_ 1 derivadas continuas o sea las funciones deben pertenecer a la clase _C_<sup>_s−_1</sup> . Un ejemplo concreto lo tenemos si observamos de 

**155** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.4. Formulaci´on d´ebil_ _<u>y</u> el m´etodo de Galerkin_ 

la secci´on anterior que la forma d´ebil del problema de conducci´on t´ermica contiene a lo sumo primeras derivadas. En esa caso _s_ = 1 y necesitamos que las funciones de forma sean _C_<sup>0</sup> , o sea funciones continuas, como aquella ubicada en el centro de la figura 6.4. Una observaci´on a hacer es que no debe confundirse la continuidad de una funci´on con el grado del polinomio que la aproxima localmente. Por ejemplo una funci´on de forma que usa polinomios de segundo ´orden en el interior de los elementos no necesariamente tiene mayor continuidad que una lineal. La continuidad depende de como se pegan las funciones elemento a elemento y no de como se interpola en su interior. Los elementos de la clase _Lagrange_ , los m´as standard en m´etodo de los elementos finitos pertenecen a la clase _C_<sup>0</sup> mientras que aquellos del tipo _Hermite_ son _C_<sup>1</sup> . Mientras los primeros requieren que las funciones se peguen en forma continua entre los elementos los ´ultimos son m´as estrictos y requieren que la primera derivada tambi´en sea continua, independientemente de lo que suceda adentro. La figura 6.5 pretende ilustrar una funci´on de forma hermitiana para un elemento unidimensional de dos nodos. 

###### Figura 6.5: Funciones de forma de mayor orden 

Los requisitos de continuidad que estuvimos tratando tambi´en se aplican a las funciones de peso. En estos casos una sutileza debe remarcarse. Cuando hablamos del m´etodo de colocaci´on hemos empleado la funci´on _delta de Dirac_ para tal fin. Esto solo es factible si se garantiza que el residuo sea finito. 

#### **6.4. Formulaci´on d´ebil y el m´etodo de Galerkin** 

En el cap´ıtulo anterior vimos como un t´ermino como el siguiente 



con _L_ un operador diferencial lineal puede ser reemplazado por otro como 



donde los operadores lineales _C, DE_ tienen un orden de diferenciaci´on estrictamente inferior al de _L_ . Tal reformulaci´on es muy ventajosa cuando se usan funciones de forma definidas localmente debido a que esto disminuye el grado de continuidad a ser demandado sobre las mismas. Uno de los operadores que frecuentemente aparecen es el de segundo orden que cuando se lo somete a la debilitaci´on (6.16,6.17) da or´ıgen a dos operadores de primer orden, uno aplicado a la funci´on de peso y el otro a la interpolaci´on. Esto pone de manifiesto que la elecci´on de la misma clase de funciones para _W_ como para _N_ , base del m´etodo de Galerkin, posee muchas ventajas. Adem´as de equiparar el grado de continuidad queda garantizada la simetr´ıa del operador. 

#### **6.5. Aspectos computacionales del m´etodo de los elementos finitos** 

En esta secci´on tomaremos algunos ejemplos muy simples que servir´an para explicar la metodolog´ıa empleada en el m´etodo de los elementos finitos . Estos ejemplos consisten de dominios unidimensionales, con una partici´on muy gruesa (pocos elementos empleados) y con funciones de prueba sencillas. 

**156** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.5. Aspectos computacionales del m´etodo de los elementos finitos_ 

No obstante esto el procedimiento es bien general y puede extenderse tanto a mallas muy finas como al caso multidimensional y con funciones de alto orden. 

##### **6.5.1. Ejemplo 1** 

Este primer ejemplo consiste en resolver: 



**Paso 1: Elecci´on de la funciones de forma y formulaci´on del problema** Teniendo en cuenta las consideraciones acerca del grado de continuidad de las funciones de forma relativa al orden de diferenciaci´on del operador involucrado en este ejemplo vemos de inmediato que funciones de la clase _C_<sup>0</sup> son suficientes para resolver este problema. Esto permite usar funciones lineales a trozos aunque si se desea tambi´en puede aumentarse el grado del polinomio interpolante, como por ejemplo usar elementos cuadr´aticos o de mayor orden. No obstante esto involucra en general un mayor costo computacional muchas veces innecesario para la precisi´on requerida. Entonces la aproximaci´on se escribe como: 



Al establecer el m´etodo de los residuos ponderados sobre este problema tenemos 



donde el ´ultimo t´ermino representa la contribuci´on del residuo en el borde porque la aproximaci´on elegida no necesariamente satisface las condiciones de borde. No obstante este t´ermino puede omitirse si uno elije funciones de peso que se anulen sobre la parte del contorno donde se prescriben condiciones tipo Dirichlet. Entonces si lo anulamos y si debilitamos la integral sobre el interior del dominio para poder usar funciones con menores requisitos de continuidad llegamos a: 



Usando el m´etodo de Galerkin _Wl_ = _Nl_ surge obviamente la necesidad de emplear funciones clase _C_<sup>0</sup> . 

**Paso 2: discretizacion de las variables independientes generacion de la malla** Esto consiste en subdividir el dominio en elementos tales que 



**157** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.5. Aspectos computacionales del m´etodo de los elementos finitos_ 

En este caso simple la partici´on es trivial, el dominio es un segmento de recta y la partici´on consiste en dividir este segmento en intervalos que satisfagan (6.22). La situaci´on unidimensional es muy particular y simple ya que (6.22) se puede alcanzar en forma exacta. En varias dimensiones esto se obtiene en general en forma aproximada. Para simplificar los pasos siguientes dividamos el dominio Ω= [0 _,_ 1] en 3 elementos (4 nodos) como se muestra en la figura 6.6. 

De esta forma quedan definidas las coordenadas de los nodos 



y las conectividades de los elementos (los nodos asociados a cada elemento) 



En lo que siguen definimos el tama˜no del elemento como _h_<sup>_e_</sup> = _|xj − xi|_ con _i, j_ los nodos que lo definen. 



<!-- Start of picture text -->
e=1 e=2 e=3<br>I=1 2 3 4<br>1 2 3 4<br>1<br>2<br>3<br>4<br><!-- End of picture text -->

Figura 6.6: Malla del ejemplo 1 

A continuaci´on presentamos una transformaci´on de coordenadas que facilita mucho la tarea a nivel computacional. Esta se define como: 



donde _xk_ son las coordenadas del elemento en el dominio real del problema y _ξk_ son las correspondientes en un elemento denominado _master_ . En una dimensi´on este elemento m´aster se define 

**158** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.5. Aspectos computacionales del m´etodo de los elementos finitos_ 

como: 



La idea es transformar el elemento real en otro muy simple, por ejemplo pensemos simplemente en una cuadr´angulo en 2D completamente distorsionado y su mapeo a un cuadrado con sus aristas paralelas a los ejes coordenados. Realizar c´alculos de derivadas e integrales en el primero suele ser mucho m´as trabajoso que en el elemento de forma simple. Si bien este tema presentado en el caso unidimensional parece de poca importancia en varias dimensiones este mapeo es clave para poder facilitar los c´alculos. Este tema ser´a presentando con m´as detalle m´as adelante en el contexto del m´etodo de los elementos finitos en varias dimensiones. 

**Paso 3: Definici´on de las funciones de forma** Este paso es una consecuencia de los dos anteriores. Habiendo elegido el tipo de funciones de forma necesarios para satisfacer los requerimentos de continuidad que plantea el operador diferencial a resolver y habiendo realizado la discretizaci´on de las variables independientes surge de su combinaci´on la definici´on de las funciones de forma. Estas se pueden escribir como: 



donde se asume que _xi < xj_ y tiene un valor unitario en el nodo cayendo linealmente hasta ser nula en el otro nodo del mismo elemento. 

Esta definici´on es muy ad-hoc para el caso unidimensional y no usa la idea de mapeo al elemento master definida anteriormente. La siguiente si presenta esa idea y la incluimos porque ser´a la que en definitiva usaremos al momento de calcular las integrales. 



Esta definici´on como vemos satisface la definici´on de la funci´on, en el nodo _i_ , _ξ_ = _−_ 1 _⇒ Ni_ = 1 y _Nj_ = 0 mientras que en el nodo _j_ , _ξ_ = 1 _⇒ Ni_ = 0 y _Nj_ = 1. Una definici´on equivalente a la anterior que suele unificar la anterior y es v´alida para los dos nodos es la siguiente: 



donde _l_ representa la numeraci´on local de los nodos, a nivel del elemento. Esta tiene la ventaja que permite operar algebraicamente con m´as flexilibidad. 

Ensambl´andola sobre todo el conjunto de elementos produce una funci´on que tiene la forma de un sombrero como fue mostrada en la figura 6.2. 

**159** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.5. Aspectos computacionales del m´etodo de los elementos finitos_ 

**Paso 4: C´alculo de la matriz del sistema y del miembro derecho** Como hemos visto en el primer paso (6.21) la formulaci´on del problema contiene el c´alculo de varias integrales, una por cada nodo de la malla. Reemplazando en ella la aproximaci´on (6.19), la definici´on de la funci´on de peso que para este ejemplo coincide con la de interpolaci´on (Galerkin) y la definici´on de las funciones de forma (6.27), entonces el c´alculo de estas integrales se puede escribir como: 



Estas integrales definidas sobre todo el dominio Ω= [0 _,_ 1] pueden descomponerse aditivamente por una de las propiedades de la integraci´on en varias integrales, una por cada elemento. Entonces, calcular las integrales a nivel del elemento y luego ensamblarlas o agregarlas cada una de sus contribuciones es equivalente a integrar sobre todo el dominio. Esto es as´ı porque las funciones que aproximan a la soluci´on fueron definidas elemento a elemento. Por lo tanto lo dicho equivale a: 





Reemplazando por sus valores 



Esta expresi´on contiene dos juegos de´ındices, unos sin primas que representan la numeraci´on global de la matriz y est´a asociado a la numeraci´on global de la malla y otros ´ındices primados que tienen la numeraci´on local dentro del elemento. Hay una relaci´on entre ambos y viene expresada por la tabla de conectividades definida antes (6.24). Para el el elemento ´e-simo, fila _e_ del arreglo IX se satisface que 

con lo cual el ´algebra anterior se pudo compactar bastante. Nosotros para simplificar la notaci´on y expresar este cambio de numeraci´on en la expresi´on (6.31) usamos Υ<sup>_lm_</sup> _l_<sup>_′_</sup> _m_<sup>_′_.</sup> 

**160** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.5. Aspectos computacionales del m´etodo de los elementos finitos_ 

Esta relaci´on entre numeraciones es la que permite el ensamble de contribuciones elementales en globales. Esto significa que 



con _A_ el operador de ensamblaje. Esto se ilustra en la figura 6.6. 

Si bien todo el c´alculo ha sido llevado a cabo manualmente esto tiene un alto grado de automatizaci´on debido a lo simple que resultan las funciones de forma y sus derivadas en el elemento master. 

**Paso 5: Resoluci´on del sistema de ecuaciones** Con el miembro derecho el procedimiento es similar y finalmente se alcanza el siguiente sistema de ecuaciones lineales a resolver: 





Dado que las condiciones de contorno definidas inicialmente implicaban imponer el valor de _φ_ ( _x_ = 0) = 0 y _φ_ ( _x_ = 1) = 1, esto implica primero reemplazar dichos valores en el vector inc´ognita y pasar para el miembro derecho todos aquellos t´erminos que dichos valores generan para luego remover las filas y las columnas correspondientes a estas variables impuestas. 

Por lo tanto el sistema (6.34) se transforman en otro m´as reducido: 



La resoluci´on de este sistema es inmediata obteniendo los valores del arreglo **_φ_** , soluci´on a nuestro problema. Con ellos es posible estimar las derivadas en los extremos reemplazando simplemente el vector soluci´on en (6.34) y despejando el valor de<sup>dˆ</sup> d<sup>_<u>φ</u>_</sup> _x_ ��� _x_ =0 _,_ 1<sup>.</sup> 

**Comentarios finales** Para terminar con este ejemplo haremos dos comentarios, uno acerca del c´alculo de las integrales elementales y otro acerca de la resoluci´on del sistema algebraico. Respecto al primero es de destacar que si bien aqu´ı hemos recurrido a la integraci´on anal´ıtica en general se trabaja utilizando integraci´on num´erica con lo cual solo se necesita evaluar el integrando en determinados puntos del dominio y sumar las contribuciones, como es el caso de integraci´on por cuadratura num´erica. Con esto es posible extender el tratamiento a operadores de diferente tipo, incluso con coeficientes variables dentro del elemento, etc. El tema de la integraci´on num´erica ser´a abordado m´as adelante. 

**161** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.5. Aspectos computacionales del m´etodo de los elementos finitos_ 

Respecto a la resoluci´on del sistema se debe evaluar el m´etodo a seguir seg´un el tipo de problema a resolver, lineal o no lineal, estacionario o transiente, 2D o 3D y fundamentalmente teniendo en cuenta los recursos computacionales disponibles. Este tema que hoy en dia es un area en si misma ser´a tratada en un pr´oximo cap´ıtulo. 

##### **6.5.2. Ejemplo 2** 

Este ejemplo es similar al anterior salvo en el tipo de condiciones de contorno impuesta. En este caso las mismas son: _φ|x_ =0 = 0 y<sup>d</sup> d<sup>_<u>φ</u>_</sup> _x_<sup>_|x_=1= 1</sup> 

La formulaci´on del m´etodo de los residuos ponderados para este problema es la siguiente: 



Ya que la integral sobre el dominio no ha cambiado y los t´erminos de contorno no influyen sobre la matriz del sistema, esta ´ultima queda igual que en la del ejemplo anterior. Por el cambio en el tipo de derivada solo se modifica el miembro derecho con lo que el sistema a resolver se transforma en uno id´entico a (6.34) con un miembro derecho 



Lo restante es todo similar a lo ya visto. 

##### **6.5.3. Ejemplo 3** 

Este ejemplo muestra como tratar un sistema de ecuaciones diferenciales e incluso para darle cierta generalidad usaremos una formulaci´on mixta. 

El problema a resolver es el de conducci´on del calor con fuente (ec. de Poisson) reemplazado por una formulaci´on mixta del tipo: 



Escribiendo para cada variable inc´ognita su aproximaci´on en la forma: 



**162** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.6. Interpolaci´on de mayor orden en 1D_ 

El m´etodo de los residuos ponderados aplicado a la anterior se puede escribir como: 



Aqu´ı hay varias alternativas para elegir las funciones de forma. La primera que vamos a adoptar es aquella en la que ambas variables se aproximan con funciones lineales a trozos con los pesos coincidentes entre si y coincidente a las funciones de interpolaci´on. O sea _Nl,_ 1 = _Nl,_ 2 = _Nl_ Por cada elemento hay 4 inc´ognitas, 2 nodos con 2 grados de libertad por nodo. 

Las expresi´on para el c´alculo de las matrices elementales ahora contienen a su vez una matriz, o sea que al agregar la contribuci´on de cada uno de los nodos del elemento contra todos los otros nodos del mismo elemento (en 1D, 2 _×_ 2) se llega a: 



lo cual produce la siguiente matriz elemental 



Lo que sigue es simplemente calcular las integrales y resolver el sistema. Otra alternativa para (6.40) es debilitar la segunda ecuaci´on y cambiarla de signo: 



y por haber disminuido el orden de diferenciaci´on sobre _q_ podemos usar funciones de forma constantes a trozo tanto para interpolar esta funci´on como para pesar la misma ( _Nl,_ 1 = _Nm,_ 1 constantes a trozos ). De esta forma en cada elemento la cantidad de grados de libertad se reduce de 4 a 3, los dos valores de _φ_ en los nodos y el valor de _q_ en el centro del elemento. La contribuci´on elemental se escribe como: 



#### **6.6. Interpolaci´on de mayor orden en 1D** 

Tanto en el cap´ıtulo anterior como en las secciones anteriores del prsente hemos introducido el concepto de aproximaci´on mediante el uso de funciones de prueba con cierta suavidad aplicada a todo 

**163** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.6. Interpolaci´on de mayor orden en 1D_ 

el dominio _m´etodos globales_ o aquellas definidas elemento a elemento _m´etodos locales_ con interpolaci´on constante o lineal por elemento. Esta ´ultima alternativa condujo a la forma m´as simple de definir el m´etodo de los elementos finitos . La motivaci´on de mejorar la aproximaci´on a la soluci´on del problema conduce a varias clases de refinamiento, entre ellas las m´as usuales son: 

- 1.- usar una interpolaci´on de bajo orden y refinar la malla _tipo h_ , 

- 2.- usar una malla fija y una interpolaci´on de mayor orden _tipo p_ , 

- 3.- una combinaci´on de las dos anteriores _tipo h-p_ . 

Desde el punto de vista pr´actico la mejor soluci´on es la alcanzar la mayor precisi´on al menor costo posible. Si bien la elecci´on es muy dependiente del problema es cierto que en muchas aplicaciones refinar en el polinomio de aproximaci´on es el camino ´optimo. No obstante, en ciertas aplicaciones la definici´on de las funciones de interpolaci´on est´a muy restringida por la formulaci´on del problema. Ejemplos de este caso lo tenemos en las formulaciones aplicadas a la resoluci´on de flujo compresible e incompresible. El tratamiento de la compresibilidad pone una fuerte restricci´on en la elecci´on de los espacios funcionales. No todas las combinaciones posibles para aproximar la velocidad y la presi´on son permisibles, existiendo un criterio a satisfacer ( _critero de inf-sup_ ) para los espacios funcionales. Por otro lado la advecci´on dominante requiere la estabilizaci´on num´erica del problema que se hace cada vez m´as complicada de definir a medida crece el orden de los polinomios interpolantes. Estas son las principales causas por las cuales en el tratamiento num´erico de modelos f´ısicos m´as complicados se prefiere el uso de funciones de interpolaci´on de bajo orden y se refina sobre el tama˜no de la malla. De todos modos nosotros aqu´ı presentaremos algunos detalles acerca de la interpolaci´on de mayor orden restringida al caso unidimensional, aunque la extensi´on a muchas dimensiones es tan directa como la del caso lineal. Dado un grado polinomial, existen muchas formas para generar funciones de forma que tengan ese orden de aproximaci´on. La m´as standard es la de utilizar una base de Lagrange en la cual cada grado polinomial diferente se alcanza con un juego de bases diferentes. No obstante existen otros m´etodos que son aditivos en el sentido que dada una funci´on de forma de grado _n_ se puede generar aquella de orden _n_ + 1 usando la de grado _n_ y agregandole alguna funci´on adicional. Este m´etodo es denominado _formas jer´arquicas_ de aproximaci´on y son computacionalmente muy eficientes aunque su uso no ha sido muy difundido a´un. 

##### **6.6.1. Grado de las funciones de prueba y velocidad de convergencia** 

La discusi´on acerca de la estimaci´on del error y la convergencia de una aproximaci´on en general es algo complicado de tratar y anteriormente solo mencionamos que la convergencia se alcanzar´a si la aproximaci´on es _completa_ . Esta forma vaga de definirla se deb´ıa a la generalidad de la elecci´on de las funciones de prueba. Si nos limitamos a una interpolaci´on polinomial el tratamiento se simplifica mucho. 

Consideremos un dominio Ωsubdividido en elementos Ω<sup>_e_</sup> de tama˜no _h_ y tomemos funciones de prueba interpoladas mediante un polinomio completo de grado _p_ . Es claro que si la soluci´on exacta del problema es un polinomio de grado menor o igual a _p_ la soluci´on num´erica ser´a exacta (sin tener en cuenta errores de redondeo) independientemente del peso utilizado. Obviamente que la soluci´on en 

**164** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.6. Interpolaci´on de mayor orden en 1D_ 

general no ser´a polinomial, no obstante, si no contiene singularidades (en la funci´on o en alguna de sus derivadas) puede ser bien aproximada por una expansi´on en series de Taylor. 



donde la serie de Taylor se ha tomado alrededor del punto _O_ . Entonces al usar funciones de prueba polinomiales de grado _p_ estamos aproximando exactamente los primeros _p_ + 1 t´ermino en (6.45) y el error de la aproximaci´on se vuelve _O_ ( _h_<sup>_p_+1</sup> . Es de notar que la aproximaci´on a la primera derivada ser´a _O_ ( _h_<sup>_p_</sup> ) y aquella correspondiente a la derivada _d_ -´esima ser´a _O_ ( _h_<sup>_p_+1</sup><sup>_−d_</sup> ) 

Volviendo a la formulaci´on general del m´etodo de los residuos ponderados o a aquella del m´etodo de los elementos finitos vimos que estaban involucrados dos operadores diferenciales _L_ y _M_ . Estos operadores contienen derivadas y supongamos que la m´axima derivada sea _d_ , es claro que el menor orden para la aproximaci´on de la soluci´on debe ser tal que la representaci´on del operador diferencial de la soluci´on sea _O_ ( _h_ ) por razones de completitud. Entonces se requiere que: 



Este requisito de completitud pone de manifiesto la utilidad de la formulaci´on d´ebil presentada anteriormente. Hab´ımos visto oportunamente que al debilitar la formulaci´on disminu´ıan los requisitos de continuidad de la aproximaci´on. Ahora se pone de manifiesta una segunda ventaja de la debilitaci´on, reducir el orden de diferenciaci´on del operador diferencial disminuye el orden de la m´ınima interpolaci´on necesaria para garantizar convergencia en malla. Como ejemplo a esto podemos mencionar el caso del operador involucrado en un problema de conducci´on del calor. Este contiene como m´aximo segundas derivadas, al debilitarlo usando el m´etodo de Galerkin las mayores derivadas son de primer orden con lo cual se requieren funciones _C_<sup>0</sup> para satisfacer continuidad entre elementos y como m´ınimo funciones lineales para obtener convergencia en malla. 

##### **6.6.2. Funciones de forma de alto orden standard de la clase** _C_<sup>0</sup> 

Sea el conjunto de elementos unidimensionales como el ilustrado en la figura 6.7 y tomamos un elemento _e_ de la malla con sus nodos extremos numerados como 0 y 1. La aproximaci´on lineal mostrada en la parte superior de la figura asegura que la aproximaci´on es lineal sobre todo el elemento y que los par´ametros asociados a los nodos corresponden a los valores nodales en los mismos nodos. Adem´as de esta forma se garantiza la continuidad _C_<sup>0</sup> . Usando la idea de mapeo al elemento de referencia las funciones de forma se escriben como: 



La extensi´on al caso cuadr´atico se logra definiendo un nodo intermedio y tomando ahora tres funciones, una por cada nodo, con la condici´on de ser cuadr´atica dentro del elemento y valer uno en 

**165** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.7. Problemas con advecci´on dominante - M´etodo de Petrov-Galerkin_ 

el nodo asociado y cero en los otros dos, o sea: 



Extendiendo lo anterior la caso c´ubico y luego generalizando es posible definir cada una de estas funciones resolviendo un sistema lineal para los coeficientes de cada funci´on de forma asociada con cada nodo. En general, si el grado del polinomio es _p_ , entonces habr´a _p_ + 1 nodos en el elemento y 





De esta forma surgen las funciones de prueba para el caso cuadr´atico: 



y para el caso c´ubico 



Figura 6.7: Aproximaciones de mayor orden 

#### **6.7. Problemas con advecci´on dominante - M´etodo de PetrovGalerkin** 

Como ya hemos visto al introducir los m´etodo de los residuos ponderados estos m´etodos se basan en definir funciones de peso diferentes a las elegidas para interpolar la soluci´on, lo cual da or´ıgen a una gran variedad de posibilidades. Lo que se pretende aqu´ı es introducir este tema que inmediatamente encontrar´a su utilidad cuando se pretenda resolver problemas dominados por advecci´on, naturalmente hallados en problemas de mec´anica de fluidos. 

**166** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.7. Problemas con advecci´on dominante - M´etodo de Petrov-Galerkin_ 

Nuestro inter´es por este tema surge de la gran popularidad que ha tomado este tipo de formulaciones en el ´area de la mec´anica de fluidos, especialmente el m´etodo denominado SUPG. Si bien no es nuestro inter´es aqu´ı hacer historia sobre este tema podemos mencionar que la idea del m´etodo SUPG fue tratar de buscar el efecto producido por las ya conocidas y efectivas t´ecnicas de _upwinding_ para evitar oscilaciones num´ericas producidas cuando en las ecuaciones de transporte dominan los t´erminos convectivos sobre los restantes. La siguiente es un ejemplo t´ıpico de una ecuaci´on de transporte donde el miembro izquierdo representa la convecci´on y es proporcional a la velocidad con que se mueve el fluido mientras que el miembro derecho es el t´ermino difusivo, si _φ_ es la temperatura equivale a la conducci´on del calor. 



Entonces adimensionalizando la ecuaci´on anterior surge el n´umero de Peclet, 



relaci´on entre la convecci´on y la difusi´on, con _L_ una dimensi´on caracter´ıstica del problema. Si barremos el valor de Peclet desde 0 _→∞_ vemos que la ecuaci´on cambia de tipo, de ser una el´ıptica pasa a ser hiperb´olica y este cambio depende sobre la competencia entre los t´erminos convectivos y los difusivos. Al resolver el problema por diferencias finitas centradas aparecen oscilaciones cuando el Peclet de la grilla supera un valor pr´oximo a la unidad. La t´ecnica del upwindind surgi´o en el ´area de las diferencias finitas como intento de evitar las mencionadas oscilaciones y fue planteada sobre la base de aplicar una aproximaci´on en diferencias decentrada a la derivada primera. El decentraje deb´ıa hacerse aguas arriba considerando la orientaci´on del flujo y esto pudo explicarse desde muchos puntos de vista. Uno de los m´as importantes es aquel ligado al concepto de error de truncamiento explic´andose la aparici´on de las oscilaciones del hecho que al truncar la aproximaci´on centrada esta introduce una especie de difusi´on num´erica negativa que compite con la f´ısica. Existe un cierto valor del n´umero de Peclet para el cual la difusi´on num´erica supera a la f´ısica y de acuerdo a argumentos termodin´amicos se viola el segundo principio y el problema pasa a estar mal planteado. Para ver mejor esto recurrimos nuevamente a la ecuaci´on de advecci´on-difusi´on en 1D y la discretizamos por diferencias finitas centradas, lo cual es completamente equivalente a haberlo hecho por m´etodo de los elementos finitos . El esquema resultante es: 



con _Pe_ = _a_ ∆ _x_ 2 _k_ es el n´umero de Peclet del elemento y aqu´ı hemos asumido coeficientes constantes y malla uniforme. La soluci´on exacta a este problema es del tipo: 



que reemplazada en la ecuaci´on produce la siguiente ecuaci´on algebraica de segundo grado: 



[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 



Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.7. Problemas con advecci´on dominante - M´etodo de Petrov-Galerkin_ 

la cual produce las siguientes ra´ıces: 



Vemos que si _Pe_ = 1 la ecuaci´on degenera en una de primer grado con la soluci´on _ξ_ = 1 o sea _φ_ = constante. Si _Pe <_ 1 las dos ra´ıces son positivas lo cual genera soluciones positivas, combinaciones de la soluci´on constante y otra del tipo _φ_ =<sup><u>1+</u></sup> 1 _−_<sup>_<u>Pe</u>_</sup> _Pe i_ . El problema surge cuando _Pe >_ 1 ya que en este caso una de las ra´ıces es negativa y genera soluciones del tipo _φ_ = ( _−_ 1)<sup>_i_</sup><sup><u>1+</u></sup><sup>_<u>Pe</u>_</sup> _i_ . Esta soluci´on contiene una _|_ 1 _−Pe|_ oscilaci´on num´erica que puede arreglarse refinando el elemento siempre que exista algo de difusi´on en el problema, o sea que el _Pe̸_ = _∞_ . Extrapolando al caso de mec´anica de fluidos esta situaci´on se presenta en el caso de flujo viscoso (Navier-Stokes) cuando el Reynolds del elemento supera un valor cr´ıtico, del ´orden de la unidad. Una situaci´on extrema ocurre en el caso de los modelos inv´ıscidos. All´ı la difusi´on f´ısica es nula y por m´as que refinemos el _Pe →∞_ , generando las raices _ξ_ = _±_ 1 , lo cual implica una oscilaci´on irremediable. Usando diferencias finitas descentradas aguas arriba equivale a que la raiz negativa introducida por el t´ermino cuadr´atico, o sea el nodo aguas abajo, sea removida. Es por ello que es usual aproximar la primera derivada con una diferencia hacia atr´as, de forma de que ahora el esquema es: 



El caso de _Pe →∞_ transforma la ecuaci´on de segundo grado en otra de primer grado, lo cual genera una ´unica soluci´on (constante) lo cual tiene sentido f´ısico ya que el operador diferencial tambi´en cambia de tipo (´orden) cuando sucede esto. 

El _upwind_ puede verse como el agregado de viscosidad artificial o difusi´on artificial en pos de contrarestar la difusi´on negativa que introduce la discretizaci´on. Controlar esta difusi´on agregada artificialmente es importante ya que si nos excedemos la soluci´on es sobredifusiva y estamos resolviendo un problema con mayor difusi´on que la real, y por el lado contrario si no introducimos la suficiente aparecer´an oscilaciones no f´ısicas. Para ver esto se puede partir de la ecuaci´on discreta centrada (6.55) y restarle la reci´en obtenida (6.59), lo cual pone en evidencia el t´ermino introducido artificialmente: 



con<sup>_<u>a</u>_</sup><sup><u>∆</u></sup> 2<sup>_<u>x</u>_</sup> funcionando como una especie de difusi´on artificial. 

Lo anterior se lo conoce como la t´ecnica de _full upwind_ . Se sabe que esto es correcto solo cuando _Pe →∞_ y que cuando _Pe_ asume valores pr´oximos al valor cr´ıtico la difusi´on introducida debe ser corregida para evitar soluciones muy suavizadas. Para ello se ha recurrido al caso unidimensional lineal el cual tiene soluci´on exacta y se ha demostrado que la forma de corregir es introducir una funci´on denominada _m´agica_ del tipo: 



**168** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.8. El caso multidimensional_ 

En el contexto del m´etodo de los elementos finitos el mismo efecto puede lograrse de varias formas, por ejemplo mediante el uso del m´etodo de los residuos ponderados Petrov-Galerkin. Tomando la ecuaci´on (6.53). 



y definiendo a la funci´on de peso como: 



donde el primer t´ermino reproduce el m´etodo de Galerkin mientras que el segundo es una perturbaci´on cuyo efecto en la matriz es tal que al ser aplicado a un t´ermino proporcional a<sup>d</sup> d<sup>_<u>φ</u>_</sup> _x_<sup>produceun</sup> t´ermino similar a uno difusivo. El par´ametro _τ_ debe ajustarse en funci´on de la cantidad de perturbaci´on (difusi´on artificial) a agregar. De todos modos existen muchos trabajos que dan cuenta de la buena confiabilidad de la definici´on: 



donde _||_ d<sup>d</sup> _x_<sup>_<u>ξ</u>u||_equivalealvectorvelocidadtransformadoalelementom´asterylafunci´on</sup><sup>_ψ_(</sup><sup>_Pe_)es</sup> la llamada funci´on m´agica definida m´as arriba. 

Un aspecto de importancia es la continuidad de las funciones de peso. Seg´un la definici´on _Nl ∈ C_<sup>0</sup> , luego _Wl ∈ C_<sup>_−_1</sup> con lo cual se plantea una dificultad matem´atica que ha sido muy bien estudiada. Sin entrar en detalles las conclusiones han sido que el problema se suscita en los bordes entre elementos y que la formulaci´on variacional que surge del planteamiento de la forma d´ebil del m´etodo de los residuos ponderados arroja la satisfacci´on de las ecuaciones en el interior de los elementos y de los flujos en los bordes. 

Su extensi´on al caso multidimensional di´o or´ıgen a los m´etodos denominados _Streamline diffusion_ ya que introducen la difusi´on seg´un las l´ıneas de corriente. Estos m´etodos han mostrado ser muy robustos y eficientes a la hora de resolver problemas de flujo de fluidos no obstante, a diferencia del caso unidimensional, ahora no se cuenta con una soluci´on que permita controlar la cantidad de difusi´on a agregar y esta debe ser introducida acorde a criterios ad-hoc. 

La extensi´on al caso de sistemas de ecuaciones, tal como ocurre con los modelos de Navier-Stokes y Euler requieren un estudio un poco m´as detallado del tema y ser´a abordado en futuros cap´ıtulos. 

#### **6.8. El caso multidimensional** 

##### **6.8.1. Introducci´on** 

En esta secci´on por su simplicidad presentaremos el caso 2D siendo directa la extensi´on a 3D. En cuanto a las funciones de interpolaci´on existe mucha bibliograf´ıa en la cual se puede hallar las expresiones de las mismas tanto para funciones de diferente grado de continuidad como de diferente orden polinomial. Nosotros aqu´ı solo trataremos el caso de funciones de prueba de clase _C_<sup>0</sup> multilineales sobre elementos de forma triangular o cuadrangular. Dado que en el caso multidimensional se presentan 

**169** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.8. El caso multidimensional_ 

situaciones geom´etricas completamente arbitrarias lo mejor para ordenar el tratamiento del tema es introducir las funciones de forma en el elemento master y luego mencionar los detalles del mapeo que transforma las coordenadas reales en las del elemento de referencia. 

##### **6.8.2. Elemento triangular** 

El tri´angulo es una forma particularmente muy ´util porque permite representar con bastante precisi´on dominios de forma arbitraria. Para un tri´angulo t´ıpico _e_ con nodos numerados en sentido antihorario _i, j, k_ y ubicados en los v´ertices del mismo como se muestra en la figura 6.3 buscamos una funciones de forma elemental _Ni_<sup>_e_(</sup><sup>_x, y_)talque,</sup> 



con _Si_<sup>_e_elconjuntodeelementosquecontienenalnodo</sup><sup>_i_.</sup> 

El mapeo de cualquier tri´angulo al elemento master puede verse en la figura 6.8, donde los nodos _i, j, k_ se posicionan en 1 _,_ 2 _,_ 3 respectivamente. 



<!-- Start of picture text -->
k<br>η<br>y (0,1)<br>3<br>j<br>i<br>x ξ<br>2<br>1<br>(0,0) (1,0)<br><!-- End of picture text -->

Figura 6.8: Mapeo para elementos triangulares 

Las funciones de interpolaci´on lineales que satisfacen lo anterior son: 



**170** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.8. El caso multidimensional_ 

Como se puede apreciar geom´etricamente con 3 puntos definimos exactamente un plano y por lo tanto el gradiente de cualquier funci´on _φ_ definida como combinaci´on lineal de sus tres valores nodales ser´a constante dentro del elemento. Calcularemos primero el mapeo. 









De lo cual surge que dado un par ( _ξ,_<sup>¯</sup> ¯ _η_ ) podemos calcular inmediatamente su correspondiente (¯ _x,_ ¯ _y_ ) y viceversa. Retomando lo dicho antes con la aproximaci´on de la soluci´on tenemos 



Entonces 



donde 



con _φ_ = _x, y, u_ 

Lo mismo vale para los elementos del jacobiano y su inversa 



con el determinante del jacobiano expresado como 





[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.8. El caso multidimensional_ 

Con toda esta informaci´on es posible reemplazar en las integrales que surgen al aplicar el m´etodo de los residuos ponderados y obtener tanto la matriz del sistema como el vector miembro derecho. La ventaja del uso de elementos triangulares radica en que al ser los gradientes constantes permiten simples reglas de integraci´on. No obstante m´as adelante veremos que en pos dee generalizar el tratamiento introduciremos la integraci´on num´erica como medio para evaluar las mismas. Una vez que las contribuciones elementales han sido computadas se deben agregar a la matriz global. Este procedimiento puede visualizarse en la figura 6.9 donde se muestra un ejemplo 2D discretizado mediante elementos triangulares lineales. La forma en que se hace la numeraci´on de la malla influye notablemente en la posici´on de los elementos no nulos de la malla y esto influye directamente sobre la definici´on del ancho de banda de la matriz, un par´ametro que afecta el costo de resolver el sistema en forma dr´astica. Visualizando el elemento _e_ = 1 si por un momento alteramos la numeraci´on intercambiando aquella del nodo 4 con la del nodo 17, entonces la matriz ser´a llena y el ancho de banda coincide con la dimensi´on completa de la matriz. 

##### **6.8.3. Elemento cuadrangular** 

Los elementos cuadrangulares si bien poseen menos posibilidades de representar con precisi´on un dominio de forma arbitraria tienen como ventaja su buena performance en aplicaciones de mec´anica de fluidos. En el caso de elementos cuadrangulares la transformaci´on al elemento m´aster se ilustra en la figura 6.10. 

Figura 6.9: Ensamble para mallas triangulares 

**172** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.8. El caso multidimensional_ 

Las funciones de interpolaci´on se calculan como el producto cartesiano de las funciones de prueba unidimensionales (funciones bilineales) y pueden escribirse como: 



Esto origina un polinomio incompleto de segundo grado. De la misma forma que en el caso triangular el mapeo se logra interpolando cada coordenada seg´un: 



Entonces dado ( _ξ,_<sup>¯</sup> ¯ _η_ ) podemos calcular inmediatamente su correspondiente (¯ _x,_ ¯ _y_ ) pero no podemos plantear la correspondencia inversa ya que el sistema es incompletamente cuadr´atico. 

En estos casos ni los gradientes ni los jacobianos son constantes por elemento sino que dependen de la posici´on. Esto agrega complicaci´on algebraica al c´alculo de las integrales y es aqu´ı donde m´as r´edito se obtiene de emplear integraci´on num´erica. 



<!-- Start of picture text -->
y η<br>l<br>k<br>(1,1)<br>4 3<br>i ξ<br>j<br>x 1 2<br>(−1,−1)<br><!-- End of picture text -->

Figura 6.10: Mapeo elemento cuadrangular 

**173** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.8. El caso multidimensional_ 

##### **6.8.4. Transformaci´on de coordenadas** 

Tanto los m´etodos globales como los locales de alto ´orden requieren realizar integrales sobre porciones extendidas del dominio, incluso sobre la totalidad del mismo, los cuales dif´ıcilmente pueden ser representados por elementos de forma simple. La complejidad de los dominios de c´alculo hace necesaria una transformaci´on de coordenadas de forma de poder llevar un dominio arbitrario Ω( _x, y_ ) a otro mucho m´as simple Ω(<sup>ˆ</sup> _ξ, η_ ) donde realizar las operaciones tales como la integraci´on para el c´alculo del sistema algebraico a resolver. 

Por transformaci´on de coordenadas o _mapeo_ del ingl´es _mapping_ entendemos una transformaci´on un´ıvoca entre ( _ξ, η_ ) y ( _x, y_ ). Para entrar en tema consideremos la familiar transformaci´on de coordenadas cil´ındricas polares a cartesianas, donde 



En la figura **??** vemos detalles bien conocidos de esta transformaci´on. Supongamos que un mapeo en general se describa mediante funciones 





con _ndm_ el n´umero de dimensiones del dominio o n´umero de variables independientes espaciales. Una vez que se conocen las coordenadas en el dominio f´ısico de cada uno de los elementos de la malla ( _x_<sup>_e_</sup> _, y_<sup>_e_</sup> ) _∈_ Ω<sup>_e_</sup> _⊂_ Ωy elegido el tipo de mapeo a realizar _fk_ ( _ξj_ ) se pueden escribir las funciones de forma y sus derivadas sobre el elemento de referencia _master_ (Ω) de tal forma de poder realizar las integraciones<sup>ˆ</sup> propias del m´etodo sobre este dominio sencillo apelando a t´ecnicas standard de c´alculo num´erico como la integraci´on por cuadratura gaussiana u otras. Los requisitos de continuidad de las funciones en los contornos entre elementos se garantiza eligiendo apropiadamente las funciones de forma. En las aplicaciones standard del m´etodo de los elementos finitos se usan funciones de forma del tipo _C_<sup>0</sup> , o sea continuas con todas sus derivadas discontinuas. No obstante eligiendo apropiadamente estas funciones se podr´ıan obtener aproximaciones con mayor suavidad. Cuando presentamos las diferentes t´ecnicas num´ericas aplicadas a los modelos vimos que existe la necesidad de derivar las funciones de forma respecto a las variables independientes, tanto las coordenadas espaciales en el dominio global como el 

**174** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.8. El caso multidimensional_ 

tiempo. Con respecto a las derivadas especiales es necesario aplicar la regla de la cadena: 



donde **J** es el _jacobiano_ de la transformaci´on, una medida de la deformaci´on que se requiere para llevar un diferencial de elemento en el dominio local a otro en el global. Como se alcanza a ver para que la transformaci´on exista se requiere que el jacobiano sea inversible. Para ver como se transforma el area tomamos: 



De esta forma tenemos todos los elementos necesarios para realizar cualquier integraci´on que surge de la aplicaci´on del m´etodo de los elementos finitos . Supongamos que tomamos la siguiente integral proveniente de un problema de conducci´on t´ermica sobre un dominio mapeable en un cuadrado: 



###### **Mapeo param´etrico** 

Una forma ´util de definir un mapeo de entre muchas posibles alternativas es utilizando la misma clase de funciones utilizadas para interpolar la o las variables dependientes de un problema _φ_ . En este caso cada una de las coordenadas espaciales pueden tratarse como si fueran una funci´on m´as a aproximar: 



Si elegimos las mismas funciones de forma para las variables dependientes e independientes, entonces la aproximaci´on se denomina _isoparam´etrica_ . Ya que las funciones de forma son continuas el mapeo param´etrico ser´a continuo. De todas formas es posible aproximar a distinto orden las variables 

**175** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.8. El caso multidimensional_ 

independientes y las dependientes aunque no es lo usual. Con el mapeo se simplifica mucho el an´alisis y la programaci´on de los esquemas num´ericos. 

##### **6.8.5. Integraci´on num´erica** 

El c´alculo de las contribuciones elementales tanto de la matriz como del vector miembro derecho requiere resolver integrales sobre el dominio ocupado por cada elemento con un integrando que contiene al operador diferencial discreto pesado con alguna funci´on de prueba. Tanto la forma del elemento en principio arbitraria como el grado de las funciones de forma pueden complicar demasiado la evaluaci´on anal´ıtica del problema haciendo este procedimiento completamente dependiente de la aplicaci´on. Para ganar en generalidad e incluso para facilitar la tarea se recurre a integrar num´ericamente. Esto consiste en reemplazar la integral por una suma donde cada t´ermino de la misma es el producto del integrando evaluado en cada punto de muestreo pesado con un valor correspondiente a cada uno de esos mismos puntos. Por ejemplo en 1D 



donde _ξpg, wpg_ son las coordenadas de cada punto de muestreo y su correspondiente peso. La forma en que se deducen las coordenadas y los pesos en los puntos de muestreo diferencian a un m´etodo de otro. Sin entrar en detalles t´ecnicos acerca de este tema el cual es ampliamente tratado en cursos regulares de c´alculo num´erico podemos decir que en el contexto de m´etodo de los elementos finitos es muy usual el m´etodo de la cuadratura gaussiana. Este procedimiento define la posici´on de los puntos de muestreo en el interior del dominio de forma de aproximar exactamente la integral de una funci´on aproximada por un polinomio de grado _≤ p_ . Sea la funci´on 



cuya integral evaluada num´ericamente mediante (6.81) nos da: 



Comparando la integral exacta 



con la num´erica (6.83) se establece un sistema de _p_ + 1 ecuaciones con 2( _Npg_ + 1) inc´ognitas y la soluci´on solo es posible cuando 



y ya que _Npg_ es un entero _p_ ser´a siempre un n´umero impar. 



[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.9. Problemas dependientes del tiempo_ 

|_n_+ 1|_p_|
|---|---|
|1|1|
|2|3|
|3|5|
|4|4|



Cuadro 6.1: Precisi´on de la integraci´on por Puntos de Gauss 

Comparando este m´etodo de cuadratura de Gauss-Legendre con el m´etodo de Newton-Cotes vemos que este permite con 3 evaluaciones aproximar un integrando de 5to orden mientras que el de Newton-Cotes con 3 evaluaciones solo permite aproximar exactamente una funci´on de tercer orden. Las coordenadas de los puntos de muestreo y sus pesos correspondientes tanto para el caso 1D como para el multidimensional pueden consultarse en la abundante bibliograf´ıa del tema. 

#### **6.9. Problemas dependientes del tiempo** 

En esta clase de problemas el tiempo aparece como una variable independiente adicional y lo que se busca es la evoluci´on temporal de la soluci´on que a su vez es variable en el espacio. Estos problemas, denominados _de valores iniciales_ ocurren muy frecuentemente en las aplicaciones, en problemas de difusi´on transiente, en propagaci´on de ondas, en problemas de inestabilidad de flujos, etc. En el caso estacionario la discretizaci´on de las variables independientes (en este caso las espaciales) conduc´ıa a un sistema de ecuaciones algebraicas. Ahora, discretizando en una primera etapa las variables espaciales se alcanza un sistema de ecuaciones diferenciales ordinarias que puede ser resuelto tal como est´a aplicando t´ecnicas ad-hoc para tal fin. Este m´etodo se lo conoce como de _semidiscretizaci´on parcial_ . La otra alternativa es en una segunda etapa discretizar la variable independiente tiempo mediante alguna t´ecnica, m´etodo de los elementos finitos o m´etodo de las diferencias finitas , conduciendo nuevamente a un sistemas de ecuaciones algebraicas . 

##### **6.9.1. Discretizaci´on parcial** 

Si bien este m´etodo fue presentado como para desacoplar el tratamiento de las variables espaciales respecto a la temporal tambi´en puede ser aplicado al caso estacionario cuando queremos discretizar solo algunas de las variables espaciales y no todas. Supongamos que _φ_ = _φ_ ( _x, y, z_ ) sea una funci´on a encontrar dependiente de las tres coordenadas espaciales. Podemos aproximar esta funci´on de la forma habitual 



Reemplazando la anterior en el problema diferencial produce que todas las derivadas respecto a _y_ permanecer´an tal cual y las restantes derivadas asumir´an su versi´on discreta, llegando finalmente al 

**177** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.9. Problemas dependientes del tiempo_ 

sistema de ecuaciones diferenciales ordinarias siguiente: 



con el orden de la ecuaci´on diferencial ordinaria determinado por el m´aximo orden de derivaci´on respecto a _y_ . Este tipo de soluci´on prueba ser ´util cuando el dominio es prism´atico en _y_ , o sea no depende de _y_ . 

En general podemos decir que si el problema f´ısico viene gobernado por la ecuaci´on diferencial 



entonces si la aproximaci´on planteada es del tipo 



entonces el sistemas de ecuaciones diferenciales ordinarias resultante se puede escribir como: 





Adecuadas condiciones de borde sobre Γ para todo instante _t_ junto con valores iniciales para **a** ( _t_ = 0) y para<sup><u>d</u></sup> d<sup>**<u>a</u>**</sup> _t_<sup>(</sup><sup>_t_= 0)si</sup><sup>_β̸_= 0debensuministrarseparaunbuenplanteamientodelproblema.</sup> Ejemplos t´ıpicos de las ecuaciones anteriores son: 



Posponemos para cap´ıtulos posteriores la resoluci´on de algunos problemas no estacionarios. 

**178** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.9. Problemas dependientes del tiempo_ 

##### **6.9.2. Discretizaci´on espacio-temporal por elementos finitos** 

La resoluci´on del sistema de ecuaciones diferenciales ordinarias que fue presentado en la secci´on anterior requiere de utilizar algoritmos num´ericos que permitan integrar en el tiempo a las mismas. La otra alternativa posible es la de discretizar el operador temporal de alguna forma para convertir el sistema de ecuaciones diferenciales ordinarias en un sistemas de ecuaciones algebraicas que puede resolverse de la misma forma que hemos visto para problemas en estado estacionario. La discretizaci´on de la variable independiente tiempo se puede efectuar de muchas formas, entre ellas la m´as usual es recurrir a esquemas simples en diferencias finitas. Esto consiste en discretizar la o las derivadas temporales mediante esquemas en diferencias y este tema ser´a tratado con mayor grado de detalle m´as adelante. Por el momento solo ejemplificamos como se podr´ıa efectuar esta discretizaci´on para el caso de una ecuaci´on como la (6.90). 



donde vemos que existen tres niveles de tiempo _t_<sup>_n−_1</sup> = _t_<sup>_n_</sup> _−_ ∆ _t_ = ( _n −_ 1)∆ _t_ , _t_<sup>_n_</sup> = _n_ ∆ _t_ y _t_<sup>_n_+1</sup> = _t_<sup>_n_</sup> +∆ _t_ = ( _n_ +1)∆ _t_ y adem´as hemos empleado operadores en diferencias centradas. La forma de llevar a cabo el c´alculo da oria gen a dos clases de m´etodos, los _expl´ıcitos_ y los _impl´ıcitos_ . En los primeros no se requiere invertir ninguna matriz y el valor de la soluci´on en un instante de tiempo se puede despejar directamente a partir de aquellos valores de la soluci´on evaluada en tiempos anteriores. En el caso impl´ıcito esto no es factible y se requiere invertir un sistema. Este tema ser´a profundizado m´as adelante. 

La segunda alternativa que exploraremos con m´as detalle a continuaci´on es la de usar funciones de prueba dependientes del tiempo. El hecho de que no sea esta una forma general de trabajo se debe a que: 

- 1.- problemas con tiempos caracter´ısticos largos involucran un excesivo vol´umen de c´alculo, 

- 2.- las matrices resultan en general no sim´etricas aun usando el m´etodo de Galerkin, 

- 3.- la simple topolog´ıa que existe en el dominio temporal ofrece poco atractivo para usar discretizaci´on irregulares en el tiempo. 

En los ´ultimos tiempos ha habido un gran inter´es por el uso de formulaciones espacio-temporales para tratar problemas con dominios variables en el tiempo. 

Por su mayor grado de aplicaci´on en el area de la mec´anica de fluidos en la secci´on que sigue trataremos exclusivamente el caso de ecuaciones de primer orden. 

**179** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.9. Problemas dependientes del tiempo_ 

###### **Ecuaciones de primer orden** 

Tomando el caso de _β_ = 0 en (6.88) llegamos al siguiente sistema de ecuaciones diferenciales ordinarias 



Las condiciones iniciales implican conocer el valor de _φ_ ( _t_ = 0) lo cual en forma discreta equivale a conocer **a** ( _t_ = 0) = **a**<sup>0</sup> . De acuerdo a (6.89) vemos que el problema espacial y el temporal est´an desacoplados por lo que una posterior aproximaci´on, ahora exclusivamente en el tiempo, para la inc´ognita **a** se puede plantear. Entonces, 



con **a**<sup>_m_</sup> = **a** ( _t_ = _tm_ ). Consideremos un elemento _n_ el tiempo con sus nodos extremos _t_ = _tn_ y _t_ = _tn_ +1 como se muestra en la figura 6.8. 

Por lo tanto 



Aplicando el m´etodo de los residuos ponderados a (6.93) llegamos a: 



Si las funciones de peso elegidas satisfacen que 



(6.96) se escribe como: 



mientras que (6.94) se escribe como: 



la cual reemplazada en (6.98) produce 



[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

**180** 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.9. Problemas dependientes del tiempo_ 

Estas funciones de peso equivalen a funciones constantes a trozos por elemento. Si las matrices **C** y **K** fueran independientes del tiempo entonces: 



(6.101) es v´alida para cada elemento _n_ de la discretizaci´on temporal o sea que permite para cada _n_ obtener los valores de la inc´ognita **a**<sup>1</sup> _,_ **a**<sup>2</sup> _,_ **a**<sup>3</sup> _. . ._ comenzando con el valor **a**<sup>0</sup> . Este tipo de esquema de marcha temporal se lo denomina de _dos niveles_ ya que cada c´alculo involucra solo dos instantes de tiempo, el actual y el anterior. Existen extensiones a esto que involucran varios niveles de tiempo pero no ser´an abordados por el momento. 

Para generalizar el tratamiento la expresi´on (6.101) puede reescribirse para ser usada con cualuquier funci´on de peso de la siguiente forma: 



y ya que la funci´on **f** en general var´ıan suavemente en el tiempo es algunas veces conveniente interpolarla mediante: 



Reemplazando (6.103) en (6.102) llegamos a: 



con lo cual (6.102) se escribe como: 



Si **f** no fuera una funci´on suave entonces (6.102) debe ser evaluado exactamente. 

###### **Algunos esquemas en particular** 

**Colocaci´on** Tomemos el caso del m´etodo de los residuos ponderados utilizando como func´on de peso la colocaci´on puntual. En este caso lo de puntual debe reinterpretarse como su equivalente temporal, o sea evaluada no en un punto en el espacio sino en un instante de tiempo. Si _Wn_ = _δ_ ( _T − θ_ ) _, n_ = 0 _,_ 1 _,_ 2 _, . . ._ , entonces de (6.102) surge que 





[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.10. El m´etodo de los elementos finitos aplicado a las leyes de conservaci´on_ 

la cual reemplazada en (6.105) nos da el bien conocido _m´etodo theta_ que se escribe como: 



Este m´etodo sirve como un marco te´orico general ya que de ´el se derivan muchos de los esquemas frecuentemente usado en la pr´actica. Algunos de los ejemplos m´as citados son: 

- 1.- _Esquema Forward Euler, θ_ = 0, 

- 2.- _Esquema Backward Euler, θ_ = 1, 

- 3.- _Crank-Nicolson, θ_ =<sup>1</sup> _/_ 2 

**Galerkin** Si en lugar de usar colocaci´on aplicamos el m´etodo de Galerkin ( _Wn_ = _Nn_ ) y si tomamos funciones de prueba de la clase _C_<sup>0</sup> satisfaciendo que: 



al reemplazar en (6.98) se obtiene el siguiente esquema: 



que es un esquema de tres niveles de tiempo. De esta forma hemos visto que el tratamiento empleado sobre la discretizaci´on espacial puede ser extendido a la temporal en forma directa donde los esquemas multipasos tienen su correspondencia con la aproximaci´on de mayor orden en el tiempo. Detalles acerca de la forma de resolver la semidiscretizaci´on asi como la discretizaci´on completa se posponen para un pr´oximo cap´ıtulo. 

#### **6.10. El m´etodo de los elementos finitos aplicado a las leyes de conservaci´on** 

En esta secci´on presentamos una aplicaci´on del m´etodo de los elementos finitos a un sistema de leyes de conservaci´on, t´ıpica en la modelizaci´on matem´atica de problemas de mec´anica de fluidos. Hasta aqu´ı hab´ıamos considerado casi exclusivamente el caso escalar y lineal. Las leyes de conservaci´on tal como fueron presentadas al comienzo forman un sistema de ecuaciones no lineales. Su tratamiento no difiere a lo visto para el caso escalar y tampoco respecto a lo dicho sobre sistemas en el caso de la aplicaci´on del m´etodo de los residuos ponderados con aproximaciones globales. Por lo tanto y por no abundar en detalles pasamos directamente a la aplicaci´on del m´etodo de los elementos finitos a las ecuaciones de conservaci´on. 

Consideremos las leyes de conservaci´on de la forma: 



**182** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.10. El m´etodo de los elementos finitos aplicado a las leyes de conservaci´on_ 

siendo **F** el vector de flujos. Supongamos por un momento que solo incluimos los flujos convectivos dentro de ´este y que aplicamos las siguientes condiciones iniciales sobre el dominio Ωy sobre el contorno Γ = Γ0 _∪_ Γ1: 



Definiendo una forma d´ebil con **W** = **0** sobre Γ0 llegamos a 



que seguido a una integraci´on por partes conduce a 



Interpolando la soluci´on 



y debido a que el flujo es generalmente una funci´on no lineal de **U** es preferible una representaci´on separada para los flujos 



Usando el m´etodo de Galerkin ( **W** = **N** ), la ecuaci´on para el nodo _j_ es: 



donde Ω _j_ es el subdominio formado por todos los elementos que contienen al nodo _j_ y la suma sobre _m_ cubre todos los nodos de Ω _j_ . 

La matriz de masa se define como: 



mientas que la de rigidez es 



que como se alcanza a ver es no sim´etrica. Lo anterior conduce a: 



[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 



Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.10. El m´etodo de los elementos finitos aplicado a las leyes de conservaci´on_ 

Si tuvi´eramos difusi´on f´ısica entonces la discretizaci´on se lleva a cabo conforme a lo ya visto anteriormente y queda solo un comentario acerca del tratamiento de la matriz de masa. En diferencias finitas es usual una aproximaci´on a<sup>d</sup> d<sup>**U**</sup> _t_<sup>_<u>j</u>_que conduce a una matriz diagonal mientras que en elementos</sup> finitos usando un m´etodo tipo Galerkin la misma no es diagonal _masa consistente_ . En las aplicaciones habituales los sistemas a resolver son enormes en tama˜no por lo que es casi imprescindible muchas veces recurrir a m´etodos de resoluci´on expl´ıcitos. Estos requieren que la matriz asociada al miembro izquierdo de la ecuaci´on algebraica sea diagonal por lo que en el caso del m´etodo de los elementos finitos lo que se suele hacer es _concentrar_ los t´erminos en la diagonal, t´ecnica conocida con el nombre de _lumping_ , 



**184** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.11. TP.VI- Trabajo Pr´actico_ 

#### **6.11. TP.VI- Trabajo Pr´actico** 

###### **m´etodo de los elementos finitos en 1D** 

1. Dada una malla unidimensional formada por 5 nodos equiespaciados y numerados consecutivamente de izquierda a derecha, con el extremo izquierdo en _z_ = 0 y el derecho en _x_ = 1. Calcular la matriz 



usando 

a.- funciones de prueba lineales a trozo definidas como 



variando linealmente dentro de cada elemento. 

- b.- usando funciones del tipo _Ni_ = _x_<sup>_i_</sup> . Compare con la matriz obtenida en (a) 

- c.- Repita (a) pero usando la siguiente numeraci´on: 



Compare con (a) 

2. Eval´ue que tipo de funciones de forma utilizar para resolver las ecuaciones diferenciales que abajo se muestran si se adopta el m´etodo de Galerkin. Fundamentar la selecci´on hecha. 



[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

**185** 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.11. TP.VI- Trabajo Pr´actico_ 

3. Resolver la ecuac´on<sup>_d_2</sup><sup>_<u>φ</u>_</sup> _dx_<sup>2+</sup><sup>_φ_= 0con</sup><sup>_φ_(</sup><sup>_x_= 0) = 1y</sup><sup>_φ_(</sup><sup>_x_= 1) = 0usandoelm´etododeGalerkin</sup> 

con 4 elementos lineales de igual tama˜no. Tome la ecuaci´on del nodo central y eval´ue el orden de precisi´on del esquema. _Ayuda: Expandir usando series de Taylor la ecuaci´on del nodo_ 

4. (Uso del _FemCode_ en 1D) 

Usando el programa _FemCode_ resolver la ecuaci´on 



usando 4,8,16,32 y 64 elementos lineales. 

   - a.- Calcule la soluci´on exacta de este problema. 

   - b.- Trazar la curva de error vs tama˜no de elemento en forma logar´ıtmica y estimar el orden de convergencia de la aproximaci´on. 

   - c.- Compare lo obtenido con lo te´orico. 

5. (Uso del _FemCode_ en 1D) 

Usando el _FemCode_ resolver el problema unidimensional 



utilizando elementos cuadr´aticos y c´ubicos. Hacer un estudio del orden de convergencia de cada uno de ellos. 

6. (Mapeo) 

Un elemento de 4 nodos se muestra en la figura siguiente. Construya un mapeo isoparam´etrico entre este y un elemento bilineal cuadrado sobre _−_ 1 _≤ ξ, η ≤_ 1. 

Figura 6.11: Mapeo isoparam´etrico 

7. (Mapeo) 

Encuentre el mapeo isoparam´etrico a un elemento serend´ıpido de 8 nodos del elemento de la figura, con el borde curvo descripto por la funci´on _y_<sup>4</sup> = 5 _x_ . 

**186** 

[Document version: curso-0.3.0. File version: $Id: tema5.tex,v 1.11 2005/05/22 23:14:26 mstorti Exp $] 

Cap´ıtulo 6. M´etodo de los elementos finitos _Secci´on 6.11. TP.VI- Trabajo Pr´actico_ 

Figura 6.12: Mapeo isoparam´etrico 

8. (Integraci´on num´erica) 

En el c´omputo por elementos finitos es muy usual evaluar integrales del tipo 

- �Ω<sup>_e_</sup><sup>_<u>∂N</u>_</sup> _∂xk_<sup>_<u>i</u>_</sup> _∂N∂xlj_<sup>_dxkdxl_</sup> 

- y �Ω<sup>_e NiNjdxkdxl_.</sup> 

Determine el n´umero de puntos de Gauss que se necesitan tomar si requerimos que ambas integrales se eval´uen exactamente usando elementos : 

   - (a) triangulares 

   - (b) cuadrangulares de 4 nodos 

   - (c) cuadrangulares de 9 nodos 

9. (Uso del _FemCode_ en 2D) 

Resolver para una geometr´ıa plana anular con _ri_ = 0 _,_ 1 y _re_ = 1 un problema de conducci´on t´ermica con conductividad constante _κ_ = 1 imponiendo la temperatura sobre la pared circular interior a un valor nulo. Sobre la pared circular exterior la misma est´a aislada salvo en la porci´on 0 _< θ < π/_ 2 donde el flujo t´ermico alcanza un valor unitario. Determinar el campo de temperaturas resultante _T_ = _T_ ( _r, theta_ ) y mostrar las isotermas. 

10. (Upwind) 

Resolver la ecuaci´on de transporte 



usando el programa _FemCode_ para una malla bidimensional compuesta por 10 _×_ 10 elementos tomando: 

- a.- **v** = [10<sup>_−_3</sup> _,_ 0] sin upwind, 

- b.- **v** = [1 _,_ 0] sin upwind, 

- c.- **v** = [1 _,_ 0] con upwind, 

Sacar algunas conclusiones de acuerdo a los resultados obtenidos. 

11. Repita el ejemplo anterior usando una velocidad no alineada con la malla. Tome lo mismo que antes con una velocidad orientada a 30 grados respecto al eje horizontal. 

**187** 

[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

## **Cap´ıtulo 7** 

# **M´etodo de los vol´umenes finitos** 

#### **7.1. Introducci´on** 

Continuando con la presentaci´on de los diferentes m´etodos que surgen a partir del m´etodo de los residuos ponderados ahora trataremos el caso del m´etodo de los vol´umenes finitos . A modo de res´umen de lo visto antes la aplicaci´on del m´etodo de los residuos ponderados a las ecuaciones de conservaci´on fue escrita como: 



Los m´etodos de colocaci´on, tanto el caso puntual como el de subdominios, usan la ecuaci´on residual sin integraci´on parcial sobre la funci´on de peso quedando el problema en forma diferencial. Si a cada nodo _j_ del dominio le asignamos un subdominio Ω _j_ y si tomamos una funci´on de peso definida como: 



que aplicada a (7.1) nos da: 



que equivale a la misma ley de conservaci´on aplicada a cada subdominio. La idea detr´as del m´etodo de los vol´umenes finitos es discretizar cada integral siendo esta la principal diferencia del m´etodo respecto a muchos otros que llevan el problema a una formulaci´on diferencial. Para poder arribar a la forma m´as conveniente del m´etodo de los vol´umenes finitos debemos aplicar a (7.3) el teorema de Gauss-Green o de la divergencia y transformar la integral de vol´umen en otra de superficie, 



(7.4) es la ecuaci´on b´asica del m´etodo de los vol´umenes finitos que tiene como una de sus principales ventajas la de trabajar con el t´ermino de los flujos sobre el contorno del dominio, con lo cual si el costo computacional es dominado por esta operaci´on la reducci´on del mismo puede ser notable. A 

188 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.1. Introducci´on_ 

partir de (7.4) se necesita discretizar las integrales de alguna forma y lograr el sistema discreto final a resolver. Ya que el m´etodo es planteado sobre la forma integral de las leyes de conservaci´on es de notar que al satisfacer las mismas sobre cada subdominio implica satisfacerlas sobre el dominio global. Por ejemplo, si planteamos las leyes de conservaci´on sobre los 3 dominios de la figura 7.1 llegamos a: 



<!-- Start of picture text -->
B<br>C<br>Ω1<br>D Ω2<br>Ω3<br>A E<br><!-- End of picture text -->

Figura 7.1: Leyes de conservaci´on para subdominios del dominio Ω 



que sumados producen el mismo resultado que si lo hubi´eramos aplicado a todo el dominio. Esto se explica ya que dos subdominios vecinos por una cara o arista comparten los t´erminos de flujo, con la diferencia que debido a la orientaci´on de la normal exterior a cada uno, los mismos se deben balancear, 



Esta propiedad debe ser satisfecha si se requiere que el esquema sea _conservativo_ , caso contrario pueden aparecer contribuciones internas produciendo esquemas no conservativos. 

Como para ilustrar la diferencia entre un esquema conservativo y otro que no lo es planteamos el caso de una ley de conservaci´on en un dominio unidimensional que solo cuenta con un t´ermino de flujo convectivo, 



En la figura 7.2 se muestra la discretizaci´on espacial adoptada. 





[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.1. Introducci´on_ 



Figura 7.2: Grilla unidimensional 

Este esquema sencillo, similar a aquel obtenido por diferencias finitas equivale a haber tomado como vol´umen la longitud de cada segmento que representa cada celda, con el valor de la variable en cada nodo de la grilla, la fuente evaluada tambi´en en cada nodo de la misma y los flujos evaluados en los puntos medios entre los nodos. Lo anterior tambien es equivalente a haber tomado los flujos en los nodos y tanto la variable como la fuente en el centro de cada celda. 

Si aplicamos (7.8) para los nodos _i_ + 1 e _i −_ 1 y sumamos llegamos a: 



Esto es posible ya que los flujos en los puntos intermedios se van cancelando por una propiedad denominada _telesc´opica_ . Este esquema es _conservativo_ . Veamos para este mismo problema como llegamos a un esquema _no conservativo_ . Supongamos que _f_ = _f_ ( _u_ ) como sucede en el flujo convectivo de la ecuaci´on del momento lineal, entonces: 



donde _a_ ( _u_ ) es conocido como el jacobiano del flujo convectivo. Pensando nuevamente en la ecuaci´on de momento podemos tomar el caso de _f_ = _u_<sup>2</sup> _/_ 2 donde en este caso _a_ ( _u_ ) = _u_ , entonces la forma matem´aticamente equivalente a (7.7) expresada en t´erminos de este jacobiano es 



Discretizando la (7.11) 



Obteniendo similares expresiones para los nodos _i −_ 1 e _i_ + 1 y sumando llegamos a: 





[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.2. Formulaci´on del m´etodo de los vol´umenes finitos_ 

Si hubi´eramos discretizado (7.11) sobre un solo subdominio AB en lugar de agregar las contribuciones de 3 subdominios equivalentes hubi´eramos obtenido solo el miembro izquierdo de (7.13) , con lo cual el miembro derecho equivale a una fuente interna num´erica que no representa la f´ısica del problema. Haciendo un an´alisis num´erico sobre el esquema no conservativo mediante expansi´on en series de Taylor se puede ver que la importancia de estas fuentes internas es similar al error de truncamiento con lo cual en principio parecer´ıa ser despreciable. No obstante, lo anterior no es v´alido en el caso de existir fuertes gradientes en la soluci´on tal el caso de flujo trans´onico con ondas de choque, bastante citado en la bibliograf´ıa. 

La expresi´on formal de una discretizaci´on conservativa a (7.7) puede escribirse como: 



donde _f_<sup>_∗_</sup> es llamado el _flujo num´erico_ y es una funci´on de los valores de _u_ en los puntos vecinos, 



La consistencia de (7.14) requiere que cuando la soluci´on _u_ es constante el flujo num´erico sea igual al del continuo, 



Una consecuencia interesante de lo anterior la establece el siguiente teorema: 

**Teorema de Lax y Wendroff** (1960) _Si la soluci´on ui de (7.14) converge acotadamente en casi todo punto a alguna funci´on u_ ( _x, t_ ) _cuando_ ∆ _x,_ ∆ _t →_ 0 _, luego u_ ( _x, t_ ) _es una soluci´on d´ebil de (7.7) ._ 

#### **7.2. Formulaci´on del m´etodo de los vol´umenes finitos** 

Hemos visto que las leyes de conservaci´on escritas en forma integral y aplicadas a un vol´umen discreto Ω _j_ pueden escribirse como en (7.4) . La forma discreta de esta se escribe como: 



donde la suma de los flujos se refiere a todos los contornos externos de la celda de control Ω _j_ . La figura 7.3 muestra en su parte superior un ejemplo de grilla aplicable a vol´umenes finitos. Tomando la celda 1 identificada por los ´ındice ( _i, j_ ) entonces **U** _j_ = _Uij_ , Ω _j_ = area ( _ABCD_ ) y los t´erminos de flujo se obtienen como suma sobre los 4 lados _AB, BC, CD, DA_ . Asimismo en la figura inferior Ω _j_ est´a representada por el area sombreada formada por los tri´angulos que tienen como nodo com´un al nodo _j_ y los flujos se obtienen sumando sobre los lados 12 _,_ 23 _,_ 34 _,_ 45 _,_ 56 _,_ 61. Esta es la formulaci´on general del m´etodo de los vol´umenes finitos , y el usuario tiene que definir para un vol´umen Ω _j_ seleccionado c´omo estimar´a el vol´umeny las caras de la celda y c´omo aproximar´a los flujos sobre estas caras. Esto en diferencias finitas equivale a elegir la aproximaci´on en diferencias para las derivadas. Para definir una formulaci´on conservativa se requiere: 

**191** 

[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.2. Formulaci´on del m´etodo de los vol´umenes finitos_ 

- 1.-<sup>�</sup> _j_<sup>Ω</sup><sup>_j_= Ω,</sup> 

- 2.- _∩_ Ω _j̸_ = _∅_ , pueden solaparse pero solo si los contornos internos que surgen del solapamiento son comunes entre dos celdas, 

- 3.- los flujos en las superficies de las celdas deben calcularse con independencia de a cual celda le corresponde. 

(2) significa que todos los contornos de las celdas deben pertenecer a lo sumo a dos celdas y solo aquellos que est´an en el contorno exterior del dominio pueden no satisfacer este requisito. La condici´on (3) garantiza la conservatividad. 

A continuaci´on y tomando como referencia la figura 7.3 mencionaremos algunas diferencias entre el m´etodo de los vol´umenes finitos con el m´etodo de las diferencias finitas y el m´etodo de los elementos finitos . 

- 1.- Las coordenadas del nodo _j_ que es la precisa ubicaci´on de la variable **U** dentro de la celda Ω _j_ no aparece explicitamente. Consecuentemente **U** _j_ no est´a asociada con ning´un punto fijo del dominio y puede considerarse como un _valor promedio_ de la variable de flujo **U** sobre la celda. Esta interpretaci´on surge inmediatamente inspeccionando la figura superior de la gr´afica 7.3. 

- 2.- Las coordenadas de la malla aparecen solamente para definir el vol´umen de la celda y las areas de las caras, por ejemplo en la misma figura superior las coordenadas _A, B, C, D_ son suficientes. 

- 3.- En problemas estacionarios sin fuentes el ´unico t´ermino que permanece es el de la suma de los flujos sobre las caras con lo cual el m´etodo puede programarse para barrer estas caras e ir descargando los flujos sobre las dos celdas al mismo tiempo considerando la diferencia en signo. 

- 4.- El m´etodo de los vol´umenes finitos permite una f´acil introducci´on de las condiciones de contorno, especialmente aquellas que vienen expresadas en t´ermino de los flujos que pueden ser directamente impuestos en el respectivo t´ermino. 

##### **7.2.1. Mallas y vol´umenes de control** 

En cuanto a las mallas que puede manipular el m´etodo de los vol´umenes finitos este cuenta con la misma flexibilidad que el m´etodo de los elementos finitos pero restringido a elementos con lados rectas o caras planas. Entre las mallas posibles podemos hacer una divisi´on entre: 

- 1.- _mallas estructuradas_ , son aquellas en las cuales cualquier nodo puede ser ubicable en t´ermino de dos ´ındices ( _i, j_ ) en 2D o tres ´ındices ( _i, j, k_ ) en 3D. Estas mallas son muy com´unmente denominadas mallas de diferencias finitas. 

- 2.- _mallas no estructuradas_ , son aquellas com´unmente empleadas por el m´etodo de los elementos finitos y donde no es posible encontrar una expresi´on de 2 o 3 ´ındices que permita ubicar un nodo. 

Una vez que la malla se ha construido el usuario debe decidir entre 2 opciones propias del m´etodo de los vol´umenes finitos : 

**192** 

[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.3. El m´etodo de los vol´umenes finitos en 2D_ 



<!-- Start of picture text -->
3 2<br>i,j+1 9<br>C<br>4 B F<br>1<br>i−1,j<br>i,j 8<br>D<br>i+1,j<br>A<br>5 6 E<br>i,j−1 7<br>G<br>H K<br><!-- End of picture text -->

Figura 7.3: Grillas bidimensionales 

- 1.- _centrado en las celdas_ , las variables de flujo representan un promedio de los valores de la misma sobre la celda y est´an asociadas a la celda. (ver figura 7.3 (a) y (c)) 

- 2.- _centrado en los v´ertices_ , en este caso las variables de flujo representan los valores en los v´ertices o los puntos de la malla. (ver figura 7.3 (b) y (d)) 

#### **7.3. El m´etodo de los vol´umenes finitos en 2D** 

Cconsideremos la ecuaci´on (7.4) aplicada al vol´umen de control ABCD de la figura 7.3 (a), 



donde la derivada temporal pudo ser extraida de la integral siempre que consideremos el caso de dominio y malla fija. _f_ y _g_ representan las dos componentes cartesianas del vector flujo **F** . Al discretizar estas integrales llegamos a la siguiente expresi´on: 



##### **7.3.1. Evaluaci´on de los flujos convectivos** 

La evaluaci´on de los flujos _fAB_ y _gAB_ depende del esquema elegido tambien como de la localizaci´on de las variables de flujo con respecto a la malla. Como es habitual en m´etodos num´ericos en mec´anica de fluidos podemos distinguir entre _esquemas centrados_ y aquellos que tienen _upwinding_ . Los primeros requieren estimaciones locales del flujo mientras que los ´ultimos determinan los flujos acorde 

**193** 

[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.3. El m´etodo de los vol´umenes finitos en 2D_ 

con la direcci´on de propagaci´on de las componentes ondulatorias. Ahora exploraremos las distintas posibilidades. 

###### **Esquema central - centrado en la celda** 

- 1.- Promedio de flujos 



- 2.- El flujo de los promedios 



3.- Otro promedio de flujos 



con 







Tanto (7.21) como (7.22) son aproximaciones directas al flujo _fAB_ . En especial esta ´ultima equivale a integrar el flujo sobre cada cara usando la regla del trapecio � _AB_<sup>_fdy_=(</sup><sup>_fA_+</sup><sup>_fB_)(</sup><sup>_yB−yA_)</sup><sup>_/_2.</sup> Sumando sobre todas las caras llegamos a: 



lo cual equivale al m´etodo de Galerkin sobre elementos triangulares o cuadrangulares. 

Para el m´etodo de los vol´umenes finitos centrado en las celdas usando esquemas upwind el flujo convectivo es evaluado como una funci´on de la direcci´on de propagaci´on de la asociada velocidad convectiva. Si pensamos en el caso escalar bidimensional esto ´ultimo puede expresarse como: 



Considerando la figura 7.3 en su parte superior (centrado en las celdas), se podr´ıa definir: 



**194** 

[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.3. El m´etodo de los vol´umenes finitos en 2D_ 

mientras que para el caso de centrado en los v´ertices (figura (b)) tenemos: 



La desventaja de esta t´ecnica est´a en que se aumenta bastante el soporte de informaci´on en forma innecesaria ya que est´an involucrados los v´ertices ( _i −_ 2 _, j_ ) e ( _i, j −_ 2). 

###### **Esquema central sobre una malla cartesiana** 

Si bien el m´etodo de los vol´umenes finitos es tan general como el m´etodo de los elementos finitos y puede ser aplicado a mallas completamente no estructuradas en esta secci´on trataremos el caso de una grilla uniforme y demostraremos que el mismo es completamente equivalente a un esquema obtenido por el m´etodo de las diferencias finitas . Si miramos la malla superior de la figura 7.3 y si por un momento la rectificamos un poco de forma de alinear los lados con los ejes cartesianos y planteamos las integrales de contorno sobre la curva ABCD encontramos: 

LADO AB 



LADO BC 









**195** 

[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.3. El m´etodo de los vol´umenes finitos en 2D_ 

Reemplazando lo anterior en (7.19) llegamos a 





Ahora tenemos que especificar como definir los flujos en los centros de los lados _fi±_ 1 _/_ 2 _,j±_ 1 _/_ 2 _Caso (a) Aplicando (7.20) a un esquema centrado en las celdas_ 



_Caso (b) Aplicando (7.24) a un esquema centrado en las celdas_ 



**Comentarios:** 

- 1.- Se puede demostrar que estos esquemas son de segundo orden de precisi´on, 

- 2.- no dependen de los valores de los flujos _fij, gij_ , 

- 3.- (7.28) puede generar oscilaciones debido al desacoplamiento de las ecuaciones correspondientes a ( _i_ + _j_ ) par de aquellas donde ( _i_ + _j_ ) es impar. (7.29) no contiene este inconveniente. 

Id´entico tratamiento puede hacerse con el caso de formulaciones centradas en los v´ertices pero esto es dejado como ejercicio pr´actico. 

###### **Esquemas upwind en mallas cartesianas** 

Supongamos la ecuaci´on de advecci´on pura lineal en 2D, 



sobre una malla similar a la representada en la parte superior de la figura 7.3 pero rectificada de forma de lograr alinearla con los ejes coordenados cartesianos. Si _f_ = _aU_ y _g_ = _bU_ entonces, 





[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.3. El m´etodo de los vol´umenes finitos en 2D_ 

que reemplazada en la (7.19) aplicada a este problema nos da: 



###### **Mallas no uniformes** 

Garantizar la precisi´on de segundo orden de algunos esquemas cuando las mallas involucradas son no uniformes no es tarea f´acil. No entraremos en detalles aqu´ı por ser un tema demasiado espec´ıfico pero hacer promedios sobre mallas no uniformes es muy dependiente del problema, de la discretizaci´on usada, etc. Por el momento nos conformamos con lo ya visto y debemos cuidar que las mallas no tengan fuertes gradientes, o sea que sean suaves. Esto hace que la generaci´on de mallas para el m´etodo de los vol´umenes finitos sea bastante restrictiva. 

##### **7.3.2. F´ormulas generales de integraci´on** 

A diferencia de los problemas convectivos donde los flujos son funciones homog´eneas de primer orden en las variables de estado, los problemas con difusi´on contienen en general flujos difusivos que son dependientes tanto de la variable a resolver como de su gradiente. En esto casos se hace necesario promediar derivadas de las variables en lugar de las variables en si misma. Un ejemplo t´ıpico de esto son las ecuaciones de Navier-Stokes que contienen **F** _d_ = **F** _d_ ( **U** _, ∇_ **U** ) . Una forma bastante general de resolver esto es apelando al teorema de la divergencia y a la integraci´on por partes. Supongamos que tenemos integrales de flujo y la queremos aproximar por el valor promedio del integrando multiplicado por la medida del dominio de integraci´on. Entonces, aplicando el teorema de la divergencia, 



**197** 

[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.3. El m´etodo de los vol´umenes finitos en 2D_ 

Aplicando la regla de integraci´on del trapecio llegamos a: 





donde la suma se extiende a todos los v´ertices desde 1 hasta 6 que rodean al nodo _j_ en la figura 7.3 con _U_ 0 = _U_ 6 y _U_ 7 = _U_ 1. 

La misma expresi´on se puede aplicar para el c´alculo del area de las celdas, 



Si las celdas fueras cuadrangulares se puede hallar una forma interesante y particular de la anterior tomando la tercera de las ecuaciones (7.37,7.38,7.39) y agrupando por valores en los nodos opuestos. Esto queda para la pr´actica. 

###### **Ejemplo: Ecuaci´on de difusi´on en 2D** 

Tomemos la ecuaci´on 





[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.4. El m´etodo de los vol´umenes finitos en 3D_ 

considerando _κ_ constante las componentes del flujo son: 



Considerando (7.19) llegamos a una ecuaci´on para cada celda, siendo la de ( _i, j_ ) escrita como: 



El flujo _fA_ se toma como valor promedio entre las celdas 1678 y de manera similar con _fB_ sobre las celdas 1893 con lo cual se escriben como: 



Tomando _fAB_ =<sup>1</sup> _/_ 2( _fA_ + _fB_ ), multiplicando por ∆ _y_ y haciendo lo mismo con las restantes 3 caras se obtiene una expresi´on sencilla si consideramos ∆ _x_ = ∆ _y_ , 



Si en su lugar usamos 



esta conduce a la standard forma del operador de Laplace en el m´etodo de las diferencias finitas 



#### **7.4. El m´etodo de los vol´umenes finitos en 3D** 

En el caso 3D los vol´umenes finitos m´as com´unmente utilizados son los tetraedros y los hexaedros. Con los primeros se tiene la ventaja de que son muy generales ya que cualquier dominio tridimensional puede ser mallado con tetraedros, mientras que con hexaedros el problema no es tan sencillo existiendo algunas restricciones. No obstante en lo que sigue pensaremos en vol´umenes independientemente de su forma geom´etrica para aplicar algunos conceptos particulares al caso 3D. 

##### **7.4.1. Evaluaci´on del area de las caras de la celda** 

Una importante propiedad del vector area asociado con cada celda se puede derivar a trav´es del teorema de la divergencia. Por ejemplo si en (7.36) usamos _U_ = 1 entonces 



[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.4. El m´etodo de los vol´umenes finitos en 3D_ 

mostrando que el vector superficie de una dada cara contenida en una superficie cerrada _S_ y orientado en la direcci´on saliente 



depende solamente del propio contorno de la cara. Tomemos la figura 7.4 donde se muestra el vector superficie exterior para algunas de las caras del hexaedro. Si por ejemplo tomamos la cara _ABCD_ vemos que entre las muchas alternativas para evaluar el vector area podemos citar a: 

- 1.- _usando las diagonales_ 



- 2.- _usando las aristas_ 



No obstante ambas expresiones conducen a id´enticos resultados aun en el caso general en el que la cara no sea coplanar, siendo la (7.49) la m´as econ´omica desde el punto de vista de la cantidad de operaciones involucradas. 



<!-- Start of picture text -->
G<br>SDCGH<br>C<br>H<br>F<br>B<br>E D<br>SABCD<br>SADHE<br>A<br><!-- End of picture text -->

Figura 7.4: Volumen finito hexa´edrico en 3D 

##### **7.4.2. Evaluaci´on del vol´umen de la celda de control** 

En la figura 7.5 vemos una forma de calcular el vol´umen de un hexaedro mediante divisi´on en tetraedros o pir´amides. Para calcular el vol´umen de un tetraedro podemos apelar a las siguientes 

**200** 

[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.4. El m´etodo de los vol´umenes finitos en 3D_ 

identidades: 



<!-- Start of picture text -->
∇·  a d Ω= A  · d S<br>�Ω � S<br>en 2D tomando a  =  x  ⇒∇·  x  = 2<br>2Ω= x  · d S  = ( xdy − ydx )<br>(7.51)<br>� S � S<br>en 3D tomando a  =  x  ⇒∇·  x  = 3<br>3Ω PABC = x  · d S  = � x  ·  S faces<br>� PABC<br>faces<br>P<br>G<br>C<br>H<br>D D<br>F<br>C<br>A E B<br>B<br>A<br>(a) G<br>C (b)<br>H<br>D<br>F<br>E B<br>A<br>(c)<br><!-- End of picture text -->

Figura 7.5: Calculo del vol´umen de una celda en 3D 

La ´ultima expresi´on en (7.51) es equivalente a 



con **x** ( _P_ ) el vector posici´on respecto al punto _P_ . Este punto es arbitrario pero por comodidad conviene que coincida con uno de los v´ertices del tetraedro. Ya que el punto _P_ pertenece a todas las 

**201** 

[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.4. El m´etodo de los vol´umenes finitos en 3D_ 

caras excepto a la cara _ABC_ solo con ella el producto escalar es no nulo. Si recurrimos a la expresi´on (7.49) para evaluar el area de las caras de la celda y la reemplazamos en (7.52) hallamos: 



que puede escribirse tambi´en como un determinante : 



Se debe tener cuidado con la numeraci´on dada al tetraedro ya que de esta depender´a el signo de algunas contribuciones. Una regla general podr´ıa ser utilizar la regla de la mano derecha partiendo de la cara y tomando el cuarto nodo en el sentido que indica el pulgar. Otra recomendaci´on importante es que cuando partimos una malla de hexaedros en tetraedros se debe tomar la precauci´on de que las caras hexa´edricas comunes a dos celdas tengan diagonal coincidente. Estas diagonales surgen al hacer la partici´on. 

En el caso de una partici´on del hexaedro en pir´amides esta puede dividirse en dos tetraedros y el c´alculo del vol´umen y las areas se reduce a lo visto anteriormente. 

Como caso de inter´es se puede demostrar que si alguna de las caras de la celda hexa edrica no es coplanar entonces las dos ´unicas particiones del hexaedro en 5 tetraedros no producen el mismo valor de vol´umen. Si tomamos un promedio de los dos valores obtenidos este equivale a hacer una transformaci´on isoparam´etrica trilineal al estilo m´etodo de los elementos finitos e integrarla con 2 _×_ 2 _×_ 2 puntos de Gauss. 

**202** 

[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.5. TP.VII.- Trabajo Pr´actico_ 

#### **7.5. TP.VII.- Trabajo Pr´actico** 

**m´etodo de los vol´umenes finitos en 1D** 

Muestre que la ley de conservaci´on integral sobre un dominio unidimensional _a ≤ x ≤ b_ aplicada a 



se reduce a que 



es constante en el tiempo. Aplique esta condici´on a la variable espacial discretizada con una distribuci´on arbitraria de puntos en la malla y muestre que la anterior condici´on se reduce a: 



_Ayuda: Aplique la regla del trapecio para evaluar la integral ∂t∂_ � _ab_<sup>_udx_=0</sup><sup>_yreescribalasuma_</sup> _aislando los t´erminos en ui._ 

Escriba un programa en MatLab para resolver la ecuaci´on de advecci´on difusi´on 1D no estacionaria utilizando una formulaci´on 

- 1.- centrada en la celda, 

- 2.- centrada en los v´ertices 

Tenga en cuenta la necesidad de ingresar una condici´on inicial, condiciones de contorno del tipo Dirichlet y Neumann y como datos del problema f´ısico la velocidad de transporte y el coeficiente de difusi´on. 

###### **m´etodo de los vol´umenes finitos en 2D** 

Hemos visto algunas formas de evaluar los flujos convectivos como las expresiones (7.20) y (7.22), entre otras. Su aplicaci´on al caso del m´etodo de los vol´umenes finitos centrado en las celdas produjo las ecuaciones (7.31) y (7.32) respectivamente. Obtenga las expresiones equivalentes al m´etodo de los vol´umenes finitos centrado en los v´ertices. 

- Tome una celda cuadrangular y partiendo de las terceras expresiones de (7.37,7.38,7.39) obtenga una expresi´on para el promedio de las derivadas y otra para el vol´umen de la celda tratando de que la expresi´on final quede expresada como diferencia entre valores opuestos por cada diagonal. 

**203** 

[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.5. TP.VII.- Trabajo Pr´actico_ 

Considere la ecuaci´on de difusi´on bidimensional 



y escriba la formulaci´on centrada en la celda para una malla estructurada considerando que los coeficientes de difusi´on son variables con la posic´on y se definen en los v´ertices de la celda, siendo el valor en el centro de cada arista aquel que surge como promedio de los valores en los v´ertices extremos de cada arista. 

De la figura 7.6 surgen algunas alternativas para definir las celdas en 2D para el m´etodo de los vol´umenes finitos . Tome la mostrada a la izquierda ((a) Mc Donald-1971), aplique la definici´on del m´etodo de los vol´umenes finitos (7.17) a la celda _ACDEGH_ 



y derive el esquema para el nodo ( _i, j_ ) usando como definici´on de flujos por cara aquella definida como el promedio de los flujos en los puntos extremos, es decir, _fAC_ =<sup>1</sup> _/_ 2( _fA_ + _fC_ ) y compare con la expresi´on (7.57) 



<!-- Start of picture text -->
∂Uij + 1 2 ( fi +1 ,j − fi− 1 ,j ) + ( fi +1 ,j +1  − fi− 1 ,j +1) + ( fi +1 ,j− 1  − fi− 1 ,j− 1) +<br>∂t 4 � 2∆ x 2∆ x 2∆ x �<br>(7.57)<br>1 2 ( gi,j +1  − fi,j− 1) + ( gi +1 ,j +1  − fi +1 ,j− 1) + ( gi− 1 ,j +1  − fi− 1 ,j− 1) =  Qij<br>4 � 2∆ y 2∆ y 2∆ y �<br>F E F E<br>D D<br>G C G C<br>B B<br>A A<br>H H<br><!-- End of picture text -->

Figura 7.6: Vol´umenes de control centrado en los v´ertices 

**204** 

[Document version: curso-0.3.0. File version: $Id: tema6.tex,v 1.11 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 7. M´etodo de los vol´umenes finitos _Secci´on 7.5. TP.VII.- Trabajo Pr´actico_ 

**m´etodo de los vol´umenes finitos en 3D** Mostrar que las expresiones 



o 



utilizadas para evaluar el area de las caras de la celda de control en 3D son equivalente a la expresi´on: 



Tome un hexaedro con al menos una cara no coplanar. Realice las dos ´unicas posibles particiones en 5 tetraedros cada una y calcule el vol´umen de cada partici´on utilizando la expresi´on del determinante: 



- (a) Qu´e valores de vol´umenes obtuvo ?, 

- (b) son coincidentes ?. 

- (c) Tome su promedio. 

- (d) Demostrar que el promedio coincide con el vol´umen obtenido mediante el c´alculo por el m´etodo de los elementos finitos usando una transformaci´on isoparam´etrica trilineal integrada con 2 _×_ 2 _×_ 2 puntos de Gauss. 

**205** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

## **Cap´ıtulo 8** 

# **An´alisis de esquemas num´ericos** 

#### **8.1. Introducci´on** 

De acuerdo a lo establecido en los cap´ıtulos precedentes vimos que la discretizaci´on de las variables independientes y de las ecuaciones conducen a un esquema num´erico particularmente dependiente del m´etodo usado. Un esquema num´erico en general se lo representa mediante un _stencil_ o _estrella_ del operador discreto que permite vincular la soluci´on entre los nodos de la malla. Si bien en el continuo el dominio de dependencia e influencia de un operador abarca regiones extensas del dominio espacial en el caso discreto este se restringe a una zona m´as acotada y que depender´a del orden y tipo de aproximaci´on utilizado. Uno de los pasos que anteceden a la aplicaci´on pr´actica de los esquemas num´ericos es llevar a cabo un an´alisis del mismo para tener una idea de lo que puede esperarse del mismo. El an´alisis m´as cl´asico incluye t´opicos como _consistencia, precisi´on, estabilidad y convergencia_ . 

Existe una gran variedad de m´etodos de an´alisis desde aquellos que estudian el comportamiento del operador discreto en un medio infinito, otros que incluyen el tratamiento del contorno y algunos otros que dan cuenta de la influencia de las no linealidades. Antes de pasar a tratar los m´as importantes m´etodos de an´alisis introduciremos al lector en los conceptos b´asicos de los 4 t´opicos antes mencionados. 

#### **8.2. Definiciones b´asicas** 

Consideraremos una de las ecuaciones m´as representativas de los modelos matem´aticos que aparecen en mec´anica de fluidos, la ecuaci´on hiperb´olica de advecci´on pura no estacionaria, que en su versi´on unidimensional se escribe como: 



donde _a_ es la velocidad de propagaci´on de la onda cuya amplitud es _u_ . Reescribimos la anterior usando sub´ındices para referirnos a las derivadas, entoces: 



206 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.2. Definiciones b´asicas_ 

Consideremos un problema de valores iniciales de frontera, entonces para poder resolver la (8.2) necesitamos especificar : 



Supongamos que aplicamos un esquema en diferencias finitas centradas de segundo ´orden para la primera derivada espacial o uno de vol´umenes finitos equivalente, entonces el esquema semidiscreto nos queda 



Este es com´unmente referenciado como el _m´etodo de las l´ıneas_ . 

El pr´oximo paso es definir una discretizaci´on para el tiempo. Esto implica el reemplazo de la derivada temporal por una forma discreta y adem´as involucra tomar la decisi´on de elegir el nivel de tiempo en el cual evaluar el lado derecho. 

_Esquema expl´ıcito_ Eligiendo una forma en diferencias hacia adelante, el esquema m´as simple que se obtendr´ıa ser´ıa evaluar el lado derecho en el tiempo anterior. Este esquema se denomina _forward Euler_ y se escribe como: 



Surge por inspecci´on directa que la soluci´on se obtiene despejando directamente 



_Esquema impl´ıcito_ 

Si en cambio evaluamos el lado derecho en el tiempo posterior y si usamos diferencias hacia atr´as para la forma discreta de la derivada temporal tenemos el esquema _backward Euler_ : 



Como vemos aqu´ı la soluci´on se obtiene invirtiendo un sistema de ecuaciones de la forma 



donde la matriz que representa el sistema es tridiagonal debido a que la estrella es centrada y fue generada mediante la combinaci´on de tres nodos. 

**207** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.2. Definiciones b´asicas_ 

Estos esquemas producen aproximaciones con una precisi´on de segundo ´orden en el espacio y primer ´orden en el tiempo. Usando esquemas de primer ´orden en el espacio surgen los siguientes dos esquemas: 





Analizando lo que ocurre con los esquemas (8.5-8.10) se puede comprobar que los dos primeros son incondicionalmente inestables mientras que el tercero es condicionalmente estables y el cuarto es incondicionalmente estable. Esto significa que los dos primeros producen un error que crece en amplitud con el paso de tiempo (divergen) mientras que en el tercer esquema debemos elegir una relaci´on entre el paso de tiempo y el de la malla acorde a un criterio de estabilidad. Como veremos m´as adelante en problemas de advecci´on pura el par´ametro que gobierna la estabilidad de un esquema num´erico es el n´umero de _Courant_ . Este se define como: 



El cuarto esquema (8.10) converge sin restricciones pero tiene una precisi´on baja (primer ´orden). 

**Problema:** Usando Matlab implementar los 4 esquemas (8.5-8.10) para una funci´on _f_ ( _x_ ) 



con _a_ = 1 _,_ ∆ _x_ = 1 _, g_ ( _x_ = _−_ 5) = 0 _, L_ = 10. Tome distintos valores del n´umero de Courant, desde _σ_ = 0 _,_ 1 hasta valores superiores a _σ_ = 1. 

Este ejemplo simple muestra la importancia del an´alisis antes de realizar cualquier experimento num´erico. Podemos formularnos las siguientes preguntas a la hora de analizar un esquema: 

Qu´e condiciones imponer para una aproximaci´on aceptable ? 

- C´omo predecir los l´ımites de estabilidad del esquema ? 

- C´omo obtener informaci´on cuantitativa de la precisi´on ? 

Para responder estas preguntas recurrimos a los conceptos de: 

**consistencia** Esta define una relaci´on entre la ecuaci´on diferencial y la formulaci´on discreta. 

- **estabilidad** Establece una relaci´on entre la soluci´on calculada y la soluci´on exacta de las ecuaciones discretas 

**208** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.3. Consistencia_ 

**convergencia** Conecta la soluci´on calculada con la soluci´on exacta de la ecuaci´on diferencial. 

En la figura 8.1 vemos un cuadro sin´optico con la relaci´on entre los operadores, sus soluciones y los t´opicos de an´alisis. A continuaci´on entraremos m´as en detalle en ellos. 

Figura 8.1: Definici´on de consistencia - convergencia - estabilidad 

#### **8.3. Consistencia** 

Un esquema es consistente si la ecuaci´on discreta tiende al operador diferencial cuando todos los incrementos de las variables independientes tienden a cero. Esto se puede expresar como: 



con ∆ _xj_ representando los pasos de la malla en todas las direcciones. Como vemos ambos operadores se aplican a la soluci´on exacta del problema. 

Apliquemos la definici´on al caso (8.2). Para ello desarrollemos en series de Taylor alrededor del punto _u_<sup>_n_</sup> _i_<sup>todaslosvaloresnodalesqueest´anincluidosenelesquemanum´erico(8.5).</sup> 





Para los esquemas de primer ´orden como el aplicado a la derivada temporal hemos cortado el desarrollo en el t´ermino _O_ (∆ _t_<sup>2</sup> ) mientras que en las aproximaciones espaciales centradas, que son de segundo ´orden hemos extendido el desarrollo un t´ermino m´as. Reemplazando (8.14) en el esquema (8.5) y usando la definici´on (8.13) vemos que 



Se ve claramente que si ∆ _x ,_ ∆ _t →_ 0 el segundo miembro se anula y el esquema es, por la definici´on, _consistente_ . 

La _precisi´on_ del esquema puede verse en los t´erminos que lideran el segundo miembro. Este esquema es de primer ´orden en el tiempo y de segundo ´orden en el espacio. No obstante la precisi´on global podr´ıa alterarse si alguna relaci´on entre ∆ _x_ y ∆ _t_ se establece, por ejemplo si se fija que ∆∆ _xt_<sup>sea</sup> constante, entonces ser´a globalmente de primer ´orden, mientras que si se fija la relaci´on ∆∆ _xt_<sup>2constante</sup> ser´a globalmente de segundo ´orden. 

**209** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.3. Consistencia_ 

Otra forma interesante de interpretar la consistencia es la siguiente: Supongamos que _u_ ¯<sup>_n_</sup> _i_<sup>es la soluci´on exacta del esquema num´erico, o sea las</sup><sup>_u_¯</sup><sup>_n_</sup> _i_<sup>son tales que satisfacen</sup> exactamente (8.5). Al reemplazarlas en el operador diferencial arrojan la siguiente identidad: 



mostrando que la soluci´on exacta de una formulaci´on discreta no satisface exactamente la ecuaci´on diferencial para valores finitos del paso de tiempo y el incremento de la malla. No obstante la soluci´on exacta de la ecuaci´on en diferencias satisface una ecuaci´on diferencial equivalente, llamada _modificada_ , que difiere de la original en el error de truncamiento, representado por los t´erminos del lado derecho. En este ejemplo 



que puede ser expresado en forma equivalente aplicando la ecuaci´on diferencial sobre ´el para eliminar la derivada temporal, 



con lo cual el error de truncamiento puede ser escrito como 



lo cual equivale finalmente a resolver una ecuaci´on diferencial modificada 



Esto muestra porqu´e el esquema es inestable. Tal como mencion´aramos anteriormente el esquema num´erico (8.5) genera un error de truncamiento equivalente a una difusi´on negativa, con un coeficiente _−_<sup><u>∆</u></sup> 2<sup>_<u>t</u>a_2</sup> 

Finalmente la consistencia y el ´orden de precisi´on de un esquema lo dictamina el error de truncamiento, en el primer caso tendiendo a cero con los incrementos espaciales y temporales y en el segundo caso a trav´es de las potencias con las cuales se va a cero. 

Concluyendo, si 



la _consistencia_ exige _p >_ 0 _, q >_ 0 

la _precisi´on_ est´a asociada con los valores de _p , q_ 

**210** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.4. Estabilidad_ 

#### **8.4. Estabilidad** 

La definici´on de estabilidad ha sufrido bastantes cambios desde que fue por primera vez introducida por O’Brien en 1950. Sin entrar en detalles hist´oricos saltamos hasta 1956 cuando Lax y Richtmyer introdujeron el concepto de estabilidad basado en la evoluci´on temporal de la soluci´on. Posteriormente, en 1967, Ritchmyer y Morton desarrollaron esta idea que se basa en definir en forma matricial la influencia del operador discreto. Asi como un operador diferencial acepta una descomposici´on espectral sobre un espacio de dimensi´on infinita, el operador discreto acepta una equivalente pero en un espacio de dimensi´on finita, o sea representable por matrices. Supongamos que expresamos todas las inc´ognitas en cada punto del espacio y del tiempo (variables nodales) en un arreglo, que al tiempo _n_ ∆ _t_ se puede expresar como: 



El esquema num´erico puede ser escrito en forma de operador _C_ : IR<sup>_N_</sup> _→_ IR<sup>_N_</sup> como: 



con _C_ = _C_ (∆ _x,_ ∆ _t_ ) 

A modo de ejemplo tomemos el esquema num´erico (8.5) y veamos que forma toma el operador. Una ecuaci´on t´ıpica de aquel esquema es 





Si tomamos en cambio el esquema (8.7,8.8) por su car´acter de impl´ıcito debemos previamente 

**211** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.5. El m´etodo de Von Neumann_ 

definir un operador _B_ sobre _U_<sup>_n_+1</sup> para luego generar el operador _C_ sobre _U_<sup>_n_</sup> . 





**Problema:** Calcular el operador discreto _C_ del esquema (8.9) y el operador discreto _B_ del esquema (8.10). 

La condici´on de estabilidad se establece del siguiente modo: Dada una soluci´on inicial _U_<sup>0</sup> a tiempo _t_ = 0 la acci´on repetida de _C_ sobre ella produce que 



Para que todas las soluciones _U_<sup>_n_</sup> permanezcan acotadas y el esquema definido por _C_ sea estable el operador _C_ tiene que ser uniformemente acotado. Esto es, existe una constante _K_ tal que 



para valores fijos de _τ, T_ y _∀n_ . A continuaci´on presentamos el m´etodo de _Von Neumann_ , uno de los m´etodos m´as conocidos para el an´alisis de estabilidad. 

#### **8.5. El m´etodo de Von Neumann** 

Este m´etodo es bien popular y simple de aplicar, pero como tal tiene algunas limitaciones relacionadas con: _•_ v´alido solamente para operadores lineales 

- v´alido solamente para coeficientes constantes 

- v´alido solamente para problemas peri´odicos 

Como vimos en la figura 8.1 el an´alisis de estabilidad se basa en la relaci´on que existe entre la soluci´on computada _u_<sup>_n_</sup> _i_<sup>ylasoluci´onexactadelaecuaci´ondiscretizada</sup><sup>_u_¯</sup><sup>_n_</sup> _i_<sup>.Entreellasexisteuna</sup> diferencia que viene dada por los errores de redondeo y los errores en los valores iniciales. Por lo tanto 



**212** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.5. El m´etodo de Von Neumann_ 

Aplicando el esquema (8.5) sobre la soluci´on exacta de la ecuaci´on discreta vemos que por (8.27) 



Ya que _u_ ¯<sup>_n_</sup> _i_<sup>satisfaceexactamentelaecuaci´on(8.5)entoncesnosquedaunaecuaci´onparaelerror</sup> 



que es id´entica al esquema original. Por lo tanto, seg´un una visi´on lineal los errores evolucionan con el tiempo en la misma forma que la soluci´on. Del mismo modo podemos plantear algo equivalente aplicando una visi´on de operadores, como presentamos en (8.23), llegando a que 



con _e_<sup>_n_</sup> un vector equivalente al definido en (8.22) pero conteniendo a los errores en lugar de los valores nodales. Si las condiciones de borde son peri´odicas entonces podemos descomponer al error en series de Fourier para la variable espacial en cada paso de tiempo. Ya que el dominio tiene longitud finita la representaci´on de Fourier ser´a discreta y sumada sobre un conjunto finito de arm´onicas. 

Sea un dominio de longitud L, la representaci´on compleja de Fourier refleja la regi´on (0 _, L_ ) en ( _−L, L_ ) con un rango de frecuencias y longitudes de onda ( _k_ = 2 _π/λ_ ) como el siguiente: 



La figura 8.2 muestra los dos modos extremos, uno que cubre todo el dominio 2 _L_ (ondas largas) y el otro que abarca la menor regi´on en la cual se puede representar una onda, 2∆ _x_ . 

Por lo tanto estableciendo que ∆ _x_ = _L/N_ , con _N_ el n´umero de nodos en una grilla definida como el conjunto de puntos de coordenadas _xi_ = _i_ ∆ _x_ podemos representar todas las arm´onicas visibles por la grilla como 



La descomposici´on en series de Fourier del error es: 



donde _I_ =<sup>_√_</sup> _−_ 1 y _Ej_<sup>_n_eslaamplituddelaj-´esimaarm´onica.</sup> Definimos la fase como 



que cubre el dominio ( _−π, π_ ) en pasos de _π/N_ . La regi´on alrededor de _φ_ = 0 corresponden a las bajas frecuencias mientras que las cercanas a _φ_ = _π_ est´an asociadas a las altas frecuencias. Por la linealidad del operador no solamente el error satisface (8.30) sino cada arm´onica. 

**213** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.5. El m´etodo de Von Neumann_ 

Figura 8.2: Representaci´on de Fourier del error num´erico 

##### **8.5.1. Factor de amplificaci´on** 

El hecho que cada arm´onica satisfaga (8.30) implica que existe un desacoplamiento de los modos y cada uno de ellos puede tratarse por separado. Consideremos una de ellas, _Ej_<sup>_neIiφ_,introduci´endola</sup> en el esquema (8.29), introduciendo el n´umero de Courant _σ_ y sacando factor com´un _e_<sup>_Iiφ_</sup> llegamos a una ecuaci´on del tipo: 



La condici´on de estabilidad (8.26) se satisface si las amplitudes del error no crecen con el tiempo, o sea si 



La cantidad _G_ (∆ _t,_ ∆ _x, k_ ) =<sup>_<u>E</u>_</sup> _E_<sup>_n_+1</sup><sup>_<u>n</u>_</sup> se la define como el factor de amplificaci´on. Para el esquema presentado llegamos a que el factor de amplificaci´on es 



lo cual indica que su m´odulo ser´a siempre mayor que uno y por lo tanto _incondicionalmente inestable_ . 

Hab´ıamos visto anteriormente sin demostraci´on evidente que el esquema (8.9) era _condicionalmente estable_ . Tratemos de justificarlo con las herramientas reci´en presentadas. Para ello tomemos una arm´onica como la anterior, ingres´emosla en el esquema (8.9) 



aplicado al error y saquemos factor com´un _E_<sup>_n_</sup> _e_<sup>_Iiφ_</sup> , entonces arribamos a la siguiente expresi´on para el factor de amplificaci´on: 



Esto se representa gr´aficamente por un c´ırculo centrado en 1 _− σ_ de radio _σ_ , como lo muestra la figura 8.3. 

Figura 8.3: Factor de amplificaci´on para un esquema con upwind. 

La versi´on geom´etrica de la condici´on de estabilidad (8.26) es que el factor de amplificaci´on de todas las arm´onicas deben ubicarse dentro de un c´ırculo centrado en el or´ıgen de radio unitario. En el caso del esquema (8.9) esto se cumple solo si 





[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.5. El m´etodo de Von Neumann_ 

La condici´on (8.39) es muy conocida y denominada _condici´on de Courant-Friedrichs-Lewy (CFL)_ 

Otra forma de ver esta condici´on es mediante teor´ıa de caracter´ısticas. Si trazamos las caracter´ısticas a partir de un punto de la malla se debe elegir la relaci´on entre el paso espacial y el temporal de forma tal de satisfacer que _el dominio de dependencia de la ecuaci´on diferencial debe estar contenido en el dominio de dependencia de las ecuaciones discretizadas_ . La figura 8.4 muestra lo que reci´en comentamos. Es la discretizaci´on empleada capaz de capturar el dominio de dependencia de las caracter´ısticas del problema ? 

###### Figura 8.4: Interpretaci´on geom´etrica de la condici´on CFL 

Finalmente si tomamos un esquema como el (8.10) 



vemos que este tiene una _estabilidad incondicional_ . Esto se puede demostrar siguiendo los mismos pasos que en los casos anteriores, llegando finalmente a que el factor de amplificaci´on tiene una expresi´on como: 



lo cual implica que su m´odulo ser´a siempre menor que la unidad. 

##### **8.5.2. Extensi´on al caso de sistema de ecuaciones** 

Consideremos que un esquema num´erico es construido en dos pasos: 

(1) Aplicaci´on de la discretizaci´on espacial 



donde el t´ermino _qi_ contiene eventuales fuentes y las contribuciones del contorno. La representaci´on matricial de lo anterior se transforma en 



(2) Aplicaci´on de un esquema de integraci´on temporal. 



que en forma matricial se escribe como 





[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.5. El m´etodo de Von Neumann_ 

En estos casos _C_ = 1 + ∆ _tS_ . Esto corresponde al caso de un esquema de dos niveles expl´ıcitos. El caso impl´ıcito adopta la forma 



donde el operador discreto se define como _C_ = _B_ 1<sup>_−_1</sup><sup>_B_0.</sup> 

En el caso del esquema de integraci´on temporal del tipo Forward Euler el operador _C_ = _I_ + ∆ _tS_ . En el caso de varias ecuaciones el factor de amplificaci´on se transforma en la matriz de amplificaci´on. Existe una relaci´on entre el concepto de matriz de amplificaci´on _G_ y el operador _C_ . Mientras el primero habita en el espacio de las frecuencias el segundo lo hace en el dominio espacial. En general _G_ ( _φ_ ) o _G_ ( _k_ ) se puede ver como el equivalente de Fourier discreto del operador de discretizaci´on _C_ , con una relaci´on como: 



La anterior nos dice que la matriz de amplificaci´on se puede obtener reemplazando el argumento de la matriz _C_ , que en general est´a asociado con el operador de desplazamientos _E_ por _e_<sup>_Iφ_</sup> . Si recordamos que _φ_ est´a definido desde ( _−π, π_ ) en pasos de _π/N_ , entonces existe una equivalencia entre _E_ y _e_<sup>_Iφ_</sup> . El primero desplaza en la malla y el segundo en el espacio de las frecuencias. 

Habiendo establecido una forma de calcular la matriz de amplificaci´on queda por ver como establecer un criterio de estabilidad general. El concepto de m´odulo del factor de amplificaci´on cambia por el de norma de la matriz de amplificaci´on. Definiendo ´esta como: 



y considerando el hecho que 



donde _ρ_ ( _G_ ) = m´ax _j_ =1 _,p |λj|_ es el radio espectral de la matriz _G_ de _p × p_ y _λ_ sus autovalores. Entonces una condici´on suficiente de estabilidad es que 



La posibilidad que el radio espectral sea mayor que uno surge en considerar algunos problemas donde la soluci´on exacta crece exponencialmente, no obstante una condici´on estricta del tipo 



puede ser necesaria para evitar que algunos modos num´ericos crezcan m´as r´apidamente que sus correspondientes modos f´ısicos. Por ejemplo cuando la matriz de amplificaci´on tiene autovalores de valor 1 con multiplicidad mayor que uno. Estas condiciones suficientes de estabilidad (b) son v´alidas tambi´en para el caso de matrices normales donde _G_ conmuta con su hermitiana conjugada y el radio espectral coincide con la norma. 

**216** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.5. El m´etodo de Von Neumann_ 

###### **Propiedades de la matriz de amplificaci´on** 

1. Si la matriz de amplificaci´on puede expresarse como un polinomio de la matriz _A_ , _G_ = _P_ ( _A_ ), luego el teorema del mapeo espectral es v´alido y establece que: 



Por ejemplo, si _G_ = 1 _− IαA_ + _βA_<sup>2</sup> , entonces 



2. Si _G_ puede expresarse como una funci´on de varias matrices que conmutan entre si, esto es: 



entonces, _A, B_ tienen el mismo conjunto de autovectores y 



Esta condici´on deja de ser v´alida cuando las matrices no conmutan como es el caso de las ecuaciones de movimiento fluido en varias dimensiones. 

_Ejemplo: Ecuaciones de shallow water_ 

Las ecuaciones de _shallow water (aguas poco profundas)_ son un importante modelo para tratar la hidrodin´amica de zonas costeras, algunos rios y lagos donde la profundidad es mucho menor que las restantes dos direcciones coordenadas. El modelo se puede escribir como: 



El modelo unidimensional linealizado alrededor de un estado de referencia **U** 0 = _{h_ 0 ; _v_ 0 _}_ , expresado en forma diferencial se puede escribir como: 





[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.5. El m´etodo de Von Neumann_ 

Un esquema espacialmente centrado se escribe como: 



En cuanto a la discretizaci´on temporal primero consideraremos el caso de una integraci´on temporal siguiendo el esquema de Euler y luego tomaremos el caso del esquema de Lax-Friedrichs. 

_Esquema Euler_ 



donde ∆representa el operador de corrimientos espaciales y si llevamos a cabo el ensamblaje de la matriz _C_ esta se expresa como: 



Por otro lado podemos arribar a la matriz de amplificaci´on reemplazando (8.54) en (8.55), 





Comparando (8.55) y (8.57) vemos que 



Aplicando la primera propiedad de la matriz de amplificaci´on tenemos que 





[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.5. El m´etodo de Von Neumann_ 

o sea los autovalores de la matriz **A** se transforman conforme a 8.59) 

Los autovalores de la matriz **A** se calculan en forma directa como: 



Por lo tanto los autovalores de la matriz de amplificaci´on ser´an: 



Este esquema es a simple vista inestable. En el caso en que los autovalores fueran de dificultosa evaluaci´on podemos recurrir a una resoluci´on num´erica. 

_Esquema Lax-Friedrichs_ 

En 1954 Lax sugiri´o una forma de estabilizar el esquema anterior conservando la discretizaci´on espacial centrada. Este esquema bien popular en estos dias se puede escribir como: 



Realizando un procedimiento similar al caso del integrador Euler hacia adelante llegamos a que existe una condici´on tipo CFL aqu´ı del tipo, 



##### **8.5.3. An´alisis espectral del error num´erico** 

Hab´ımos visto que una forma de caracterizar la evoluci´on temporal del error en un esquema num´erico era mediante la definici´on de la matriz de amplificaci´on o en el caso de modelos escalares simplemente del factor de amplificaci´on. Surgi´o que dicha evoluci´on estaba regida por una expresi´on del tipo: 



Descomponiendo temporalmente a la soluci´on num´erica en arm´onicas podemos ver que 



con _ω_ = _ω_ ( _k_ ) una funci´on compleja del n´umero de onda que representa la dispersi´on num´erica. Relacionando (8.64) con (8.65) vemos que existe una relaci´on directa entre el factor o matriz de amplificaci´on y esta dispersi´on num´erica, 





[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.5. El m´etodo de Von Neumann_ 

Entonces, la representaci´on de la soluci´on num´erica en t´ermino de arm´onicas simples se puede escribir como: 



Del mismo modo la soluci´on exacta acepta una descomposici´on similar obteniendo: 



con su correspondiente funci´on de amplificaci´on exacta 



Para poder estudiar el espectro de los errores num´ericos dividiremos la dispersion _ω_ en su parte real y su parte imaginaria, 



de forma tal que si reemplazamos (8.70) en (8.69) tenemos 





Del mismo modo con la soluci´on exacta podemos obtener 



Si comparamos ambos m´odulos y ambas fases entre si llegamos a la definici´on de dos par´ametros de error muy importantes: 



La definici´on del error de dispersi´on dada en (8.73) es adecuada en problemas parab´olicos sin t´erminos convectivos (Φ = 0),<sup>˜</sup> caso contrario esta puede cambiarse por 



mejor adecuada en aquellos problemas dominados por convecci´on. 

**220** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.5. El m´etodo de Von Neumann_ 

###### **An´alisis de error en problemas parab´olicos** 

Tomemos la ecuaci´on del calor discretizada en el espacio en forma centrada y en el tiempo con un esquema expl´ıcito. El esquema se puede escribir como: 



El factor de amplificaci´on se obtiene mediante el procedimento presentado oportunamente y este se expresa como: 





El factor de dispersi´on del continuo se obtiene reemplazando la representaci´on espectral de la soluci´on exacta en el operador diferencial, 



y el error de disipaci´on se obtiene como: 



que si lo expandimos en series de potencias en _φ_ se obtiene despu´es de algo de algebra 



Este esquema produce errores num´ericos bajos para modos de baja frecuencia pero para aquellos de alta frecuencia estos pueden ser inaceptables, especialmente para aquellos _β ≤_<sup>1</sup> _/_ 2 pr´oximos a la cota superior. No obstante para _β_ = 1 _/_ 6 los dos ´ultimos t´erminos se cancelan y este esquema presenta un alto orden _O_ (∆ _t_<sup>2</sup> _,_ ∆ _x_<sup>4</sup> ). Adem´as ya que _G_ es real no existe error en phase por lo tanto no presenta dispersi´on num´erica. 

###### **An´alisis de error en problemas hiperb´olicos** 

Tomemos como ejemplo t´ıpico de una ecuaci´on hiperb´olica la ecuaci´on de advecci´on pura: 



F´ısicamente el transporte por convecci´on se puede ejemploficar colocando inicialmente en el dominio una onda y viendo que esta viaja en una determinada direcci´on guiada por el campo de velocidades 

**221** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.5. El m´etodo de Von Neumann_ 

sin modificarse, o sea sin amortiguarse ni dispersarse. Si como hicimos para el caso parab´olico reemplazamos una arm´onica del tipo _u_ = _e_<sup>_−I_˜</sup><sup>_ωt_</sup> _e_<sup>_Ikx_</sup> en el operador diferencial encontramos que: 



Figura 8.5: Error de disipaci´on del m´etodo expl´ıcito con upwind para la ec. de advecci´on pura. 

Como vemos a diferencia del caso parab´olico aqu´ı el coeficiente de dispersi´on num´erica es un n´umero real lo que le da un car´acter ondulatorio a la soluci´on y sin amortiguamiento. Entonces, de acuerdo a la definici´on (8.73) el error por disipaci´on y por dispersi´on vienen dados por: 



Entonces, _∥ G ∥_ es la amortiguaci´on num´erica del esquema mientras que _ϵφ_ es el error por dispersi´on. Si _ϵφ >_ 1 la soluci´on num´erica viaja m´as r´apido que la exacta mientras que si es _ϵφ <_ 1 viaja m´as lento. 

_Esquema expl´ıcito con upwind_ 

A modo de ilustraci´on tomemos el caso de un esquema expl´ıcito con upwind para resolver la ecuaci´on de advecci´on pura no estacionaria (8.80). Este esquema ya lo hemos tratado a la hora de calcular el factor de amplificaci´on y hab´ıamos obtenido una expresi´on para el mismo (8.38) 



O sea que de acuerdo a (8.82) el amortiguamiento num´erico lo podemos apreciar graficando la expresi´on (8.83). La figura 8.5 muestra el error de disipaci´on para un esquema expl´ıcito de primer orden estabilizado espacialmente mediante la introducci´on de _upwind_ . 

El error de dispersi´on se calcula a partir de la relaci´on entre las velocidades de fase num´erica y la exacta. La primera se calcula mediante su definici´on (8.66) y finalmente el error de dispersi´on se escribe como: 



La figura 8.6 muestra como es el error de dispersi´on para diferentes n´umeros de Courant, fundamentalmente para _σ_ =<sup>1</sup> _/_ 2 que da dispersi´on nula y para _σ_ = 1 _/_ 4 y 3 _/_ 4 que son casos representativos de ondas num´ericas que viajan m´as lentas y m´as r´apido que las exactas respectivamente. 

**222** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.5. El m´etodo de Von Neumann_ 

Figura 8.6: Error de dispersi´on del m´etodo expl´ıcito con upwind para la ec. de advecci´on pura. 

##### **8.5.4. Extensi´on a esquemas de tres niveles** 

Una forma muy simple de ver un esquema de tres niveles es mediante la introducci´on de una ecuaci´on adicional. De esta forma el problema queda definido mediante dos ecuaciones de 2 niveles y es completamente an´alogo al caso de tratar con sistema de ecuaciones. De esta forma la matriz de amplificaci´on que surge requiere un c´alculo de autovalores para poder identificar los errores de disipaci´on y dispersi´on. Dejamos como ejemplos dos casos interesantes. 

_El esquema leapfrog para la ecuaci´on de convecci´on_ 



_El esquema Du Fort-Frankel para la ecuaci´on de difusi´on_ 



##### **8.5.5. El concepto de velocidad de grupo** 

Un paquete de ondas contiene en general arm´onicas con varias frecuencias. En ese caso la velocidad de grupo representa la velocidad a la cual la energ´ıa de la onda se propaga. En el caso de una onda unidimensional la definici´on matem´atica de la velocidad de grupo de la soluci´on exacta es: 



Su contraparte num´erica la definimos como 



Un ejemplo lo tenemos con el esquema _leapfrog_ que tiene una relaci´on de dispersi´on num´erica expresada como: 



y aplicando (8.88) se llega a que: 



Para bajas frecuencias la velocidad de grupo es similar a la velocidad de transporte _a_ pero a altas frecuencias _φ ≈ π_ esta tiende a _−a_ o sea en contrafase con la exacta. 

**223** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.6. Convergencia_ 

##### **8.5.6. An´alisis de Von Neumann multidimensional** 

Para extender lo visto en las secciones anteriores al caso multidimensional introducimos el vector n´umero de onda **k** , de forma que una soluci´on descompuesta en arm´onicas puede escribirse como: 



El producto escalar en su versi´on discretizada se escribe como: 



donde cada n´umero de fase en cada direcci´on espacial barre el rango [ _−π, π_ ]. El resto del an´alisis permanece id´entico al caso unidimensional. Para ejemplificar tomemos la ecuaci´on del calor, un ejemplo de una ecuaci´on del tipo parab´olica. 



Si usamos un esquema centrado en las variables espaciales y expl´ıcito de primer ´orden en el tiempo la versi´on discreta se escribe como: 



Una descomposici´on de Fourier discreta se define por: 



Definiendo la matriz de amplificaci´on en forma similar al caso unidimensional _v_<sup>_n_+1</sup> = _Gv_<sup>_n_</sup> e introduci´endola junto con (8.95) en (8.94) se llega a: 



con _β_ el n´umero de Fourier antes definido. Otra vez, haciendo que el factor de amplificaci´on se mantenga en m´odulo menor que la unidad se llega a dos condiciones similares al caso 1D apenas m´as restrictivas, 



#### **8.6. Convergencia** 

La convergencia puede ser establecida siguiendo a Richtmyer y Morton de la siguiente forma: 





[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.6. Convergencia_ 

###### para _n_ ∆ _t_ fijo. 

Siguiendo el _teorema de equivalencia de Lax_ podemos decir que: 

_para un problema de valores iniciales bien planteado y una discretizaci´on consistente, la estabilidad es condici´on necesaria y suficiente para la convergencia_ 

Con esto concluimos diciendo que los dos pasos necesarios del an´alisis son: 

- (1) La consistencia conduce a la determinaci´on del ´orden de precisi´on del esquema y su error de truncaci´on 

- (2) la estabilidad nos brinda informaci´on detallada de la distribuci´on en frecuencias del error como funci´on del contenido en frecuencia de la soluci´on calculada. 

De esta forma la convergencia queda definida sin necesitar an´alisis. 

**225** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.7. TP. Trabajo Pr´actico_ 

#### **8.7. TP. Trabajo Pr´actico** 

1. Escriba un programa en MatLab que grafique el factor de amplificaci´on para la ecuaci´on de adveccci´on-difusi´on discretizada en el espacio en forma central y en el tiempo usando un esquema expl´ıcito _Forward Euler_ para diferentes n´umeros de Peclet. Considere al menos lo que sucede cuando el Peclet de la malla es: 

a.- _Pe_<sup>_h_</sup> _<<_ 1 

- b.- _Pe_<sup>_h_</sup> _<_ 1 

- c.- _Pe_<sup>_h_</sup> = 1 

d.- _Pe_<sup>_h_</sup> _>_ 1 

   - e.- _Pe_<sup>_h_</sup> _>>_ 1 

2. Obtener la matriz de amplificaci´on para el modelo unidimensional linealizado de _shallow water_ usando un esquema centrado espacialmente y un integrador temporal tipo Lax-Friedrichs, 



3. Calcule la matriz de amplificaci´on para la ecuaci´on de las ondas unidimensional de segundo orden: 



usando el siguiente esquema de discretizaci´on basado en una descomposici´on del operador de segundo orden en 2 ecuaciones de primer orden: 



- a.- Encuentre la condici´on de estabilidad de este esquema. 

- b.- Es este esquema adecuado para resolver una ecuaci´on el´ıptica del tipo 



4. Calcule el error por disipaci´on y por dispersi´on para la ecuaci´on de advecci´on pura discretizada espacialmente en forma centrada y temporalmente mediante un esquema del tipo Lax-Friedrichs. 

**226** 

[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.7. TP. Trabajo Pr´actico_ 

5. Obtenga el esquema num´erico de Lax-Wendroff. Este se puede escribir partiendo de una expansi´on en series de Taylor como la siguiente: 



reemplazando la ecuaci´on diferencial<sup>_<u>∂u</u>_</sup> _∂t_<sup>+</sup><sup>_a_</sup><sup>_<u>∂u</u>_</sup> _∂x_<sup>= 0 y una versi´on que surge de derivar esta ´ultima</sup> nuevamente respecto al tiempo e intercambiar ´ındices de derivaciones. 

A continuaci´on calcule el error por disipaci´on y por dispersi´on para la ecuaci´on de advecci´on pura discretizada espacialmente en forma centrada y temporalmente mediante el esquema de Lax-Wendroff. 

6. Programe los siguientes esquemas aplicados a la ecuaci´on de advecci´on pura: 

   - a.- expl´ıcito con upwind, 

   - b.- centrado y Lax-Friedrichs, 

   - c.- centrado y Lax-Wendroff, 

y ensayar su comportamiento para las siguientes condiciones iniciales: 

- 1.- una soluci´on constante pero discontinua en el centro del dominio, 

- 2.- una onda senoidal con fase _φ_ = _π/_ 10, 

- 3.- una onda senoidal con fase _φ_ = _π/_ 5. 

Analice el comportamiento bajo diferentes n´umeros de Courant ( _σ_ ) y saque conclusiones. 

7. El esquema _leapfrog_ aplicado a la ecuaci´on de advecci´on no estacionaria _ut_ + _aux_ = 0 se puede escribir como: 



Programe un esquema de este tipo e inicialice la soluci´on con: 







Estime la velocidad de grupo y analice la soluci´on num´erica obtenida compar´andola con la te´orica. 



[Document version: curso-0.3.0. File version: $Id: tema7.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 8. An´alisis de esquemas num´ericos _Secci´on 8.7. TP. Trabajo Pr´actico_ 

8. Analice el esquema _leapfrog_ en combinaci´on con una discretizaci´on espacial con upwind para resolver la ecuaci´on de advecci´on pura no estacionaria en 1D. Calcule la matriz de amplificaci´on y muestre que el esquema es inestable. 

9. Aplique una discretizaci´on espacial con _full upwind_ en ambas direcciones a la ecuaci´on de convecci´on pura no estacionaria en 2D 

_ut_ + _aux_ + _buy_ = 0 

usando un esquema expl´ıcito de primer order para integrarla en el tiempo. Realice un an´alisis de estabilidad de von Neumann y compare la condici´on de estabilidad con aquella del caso 1D. 

10. Escriba un programa para analizar la estabilidad de von Neumann del esquema de Lax-Wendroff aplicado a una discretizaci´on espacial centrada en 2D para resolver la ecuaci´on de advecci´on pura. Grafique el factor de amplificaci´on en funci´on de la fase para diferentes n´umeros de Courant. Compare con el caso 1D. 

**228** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

## **Cap´ıtulo 9** 

# **M´etodos iterativos para la resoluci´on de ecuaciones lineales** 

#### **9.1. Conceptos b´asicos de m´etodos iterativos estacionarios** 

##### **9.1.1. Notaci´on y repaso** 

Denotamos a un sistema lineal como 



con _A_ no-singular de _N × N_ y _b ∈ R_<sup>_N_</sup> . La soluci´on del sistema la denotamos como _x_<sup>_∗_</sup> = _A_<sup>_−_1</sup> _b ∈ R_<sup>_N_</sup> , mientras que _x_ representa una soluci´on potencial. 

Los m´etodos iterativos se basan en encontrar una secuencia _{xk}_<sup>_∞_</sup> _k_ =0<sup>talque</sup> 



Debemos asegurar la convergencia del m´etodo iterativo y si es posible determinar la _tasa de convergencia_ , es decir como se comporta el error _∥x − xk∥_ para _k →∞_ . 

###### **Normas inducidas** 

Dada una norma para vectores _∥ . ∥_ , denotamos por _∥A∥_ la norma de _A_ inducida por _∥ . ∥_ , definida 

por 



Las normas inducidas tienen la importante propiedad de que 



y tambi´en: 



229 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 

ya que 



Obviamente _∥I∥_ = 1 y _∥_ 0 _∥_ = 0. Diferentes normas utilizadas son 



**Norma inducida** _L_ 2 **de una matriz.** Sea _B_ = _A_<sup>_T_</sup> _A_ entonces _B_ es sim´etrica y definida positiva. Sean _{vj, λj}_<sup>_N_</sup> _j_ =1<sup>losautovaloresde</sup><sup>_B_,</sup><sup>_v_</sup> _j_<sup>_Tvk_=</sup><sup>_δjk_,entonces</sup> 





[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 

de manera que _∥A∥_ 2 = m´ax _|_ **Norma infinito inducida de una matriz.** Por definici´on 





y entonces, la norma inducida es 





Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 

###### **Norma inducida 1 de una matriz.** 

Por definici´on, 



y entonces, 



y entonces 



Sea _v_ tal que ( _v_ ) _i_ = _δij_ con _j_ = argmax _k_ � _i_<sup>_|aik|_,entonces</sup> 



y como 



entonces 



y por definici´on de norma inducida 



y entonces, de (9.38) y (9.42) se deduce que 



**Normas no inducidas.** Es f´acil demostrar que existen normas que no son inducidas, es decir que satisfacen 









[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 

pero no provienen de ninguna norma para vectores. Por ejemplo, si definimos la norma _∥ . ∥∗_ como 



con _c >_ 0 _, c̸_ = 1, entonces es claro que es una norma pero _∥I∥∗_ = _c̸_ = 1 y por lo tanto no es inducida. 

###### **N´umero de condici´on** 

El n´umero de condici´on de una matriz no-singular en la norma _∥ . ∥_ es 



Podemos ver que 



Si _A_ es singular tomamos como que _κ_ ( _A_ ) = _∞_ . 

###### **Criterios de convergencia de los m´etodos iterativos** 

Desar´ıamos _“detener”_ un m´etodo iterativo cuando _∥ek∥_ = _∥x − xk∥ <_ tol, pero como no conocemos _x_<sup>_∗_</sup> esto es imposible en los casos pr´acticos. Pero s´ı podemos calcular el residuo de la ecuaci´on para la iteraci´on _k_ como 



Si _∥rk∥_ es suficientemente peque˜no esperamos que _∥ek∥_ sea peque˜no y podemos poner como criterio de detenci´on 



El siguiente lema nos permite relacionar ambos criterios de detenci´on 

**Lema 1.1.1.** Dados _b, x, x_ 0 _∈_ IR<sup>_N_</sup> , _A_ no-singular y _x_<sup>_∗_</sup> = _A_<sup>_−_1</sup> _b_ , entonces 



###### **Demostraci´on.** 



entonces 



y 



Por lo tanto 



La divisi´on por _∥e_ 0 _∥_ y _∥r_ 0 _∥_ es para _adimensionalizar_ el problema. Por ejemlo, si consideramos un problema t´ermico, entonces _x_ puede representar temperaturas nodales y por lo tanto tendr´a dimensiones de temperatura (<sup>_◦_</sup> C), el miembro derecho _q_ tendr´a dimensiones de potencia (Watts) y los coeficientes 

**233** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 

[ _Aij_ ] = W _/_<sup>_◦_</sup> C, pero lo importante es que el residuo tendr´a las mismas dimensiones que _b_ es decir potencia (Watts). Ahora si hacemos un cambio de unidades tomando como unidad de potencia a cal _/_ s entonces el criterio de parada _∥r∥ <_ tol es completamente diferente, mientras que _∥r∥ / ∥r_ 0 _∥_ es el mismo en los dos sistemas de unidades. Por otra parte, este criterio depende de la soluci´on inicial _x_ 0 lo cual puede llevar a iterar demasiado en el caso en que partimos de una buena soluci´on ( _∥r_ 0 _∥_ muy peque˜no). Otra posibilidad es 



Ambos coinciden si _x_ 0 = 0. 

##### **9.1.2. El lema de Banach** 

La forma m´as directa de obtener (y posteriormente analizar) un m´etodo iterativo es reescribir (9.1) como un problema de iteraci´on de punto fijo. Una forma de hacer esto es reescribir la ecuaci´on como 



lo cual induce el siguiente m´etodo iterativo de Richardson 



El an´alisis de tales secuencias recursivas es m´as general y vamos a estudiar la convergencia de relaciones recursivas generales de la forma 



donde _M_ es la llamada _matriz de iteraci´on_ o _matriz de amplificaci´on_ . Estos m´etodos son llamados m´etodos iterativos estacionarios porque la transici´on de _xk_ a _xk_ +1 no depende de la historia anterior: 

**M´etodos estacionarios:** _xk_ +1 = _f_ ( _xk_ ) 

**M´etodos no estacionarios:** _xk_ +1 = _f_ ( _xk, xk−_ 1 _, xk−_ 2 _, . . ._ ) 

Los m´etodos de Krylov que discutiremos m´as adelante _no son m´etodos estacionarios_ . Es interesante tambi´en ver que el esquema de Richardson puede ponerse de la forma 



N´otese que _rk_ act´ua como una peque˜na correcci´on a la iteraci´on _k_ para obtener la siguiente _k_ + 1. Si estamos suficientemente cerca de la soluci´on _x_<sup>_∗_</sup> entonces _rk_ ser´a peque˜no y la correcci´on ser´a peque˜na. Aplicando recursivamente (9.60) obtenemos una expresi´on general para la iteraci´on _xk_ . Asumamos por simplicidad que _x_ 0 = 0, entonces 



[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

**234** 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 

Es claro que la convergencia del m´etodo est´a ligada a la convergencia de la suma de _M_<sup>_j_</sup> . **Lemma 1.2.1.** Si _M ∈_ IR<sup>_N×N_</sup> satisface _∥M ∥ <_ 1 entonces _I − M_ es no-singular y 



**Demostraci´on.** Veremos que la serie converge a (1 _− M_ )<sup>_−_1</sup> . Sea _Sk_ =<sup>�</sup><sup>_k_</sup> _l_ =0<sup>_Ml_. Mostraremos que</sup> es una secuencia de Cauchy 





para _m, k →∞_ . Entonces _Sk → S_ para alg´un _S_ . Pero entonces tomando el l´ımite en la relaci´on de recurrencia 



obtenemos 



Por lo tanto 



de donde _I − M_ es no-singular y _S_ = ( _I − M_ )<sup>_−_1</sup> . Por otra parte 



**Matrices diagonalizables bajo la norma 2.** En el caso en que _M_ es diagonalizable y consideramos la norma _∥M ∥_ 2 es m´as f´acil de visualizar las implicancias del lema. Sean _S_ no-singular y Λ diagonal las matrices que dan la descomposici´on diagonal de _M_ 



**235** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 

Como _∥M ∥_ = m´ax _j |λj| <_ 1 esto quiere decir que todos los autovalores _λj_ de _M_ , que son reales ya que _M_ es sim´etrica, est´an estrictamente contenidos en el intervalo _−_ 1 _< λj <_ 1. Por otra parte 







**Corolario 1.2.1.** Si _∥M ∥ <_ 1 entonces la iteraci´on (9.60) converge a _x_ = ( _I − M_ )<sup>_−_1</sup> _c_ para cualquier punto inicial _x_ 0. 

**Demostraci´on.** Si _x_ = _x_ 0 ya est´a demostrado. Si _x̸_ = _x_ 0 haciendo el cambio de variables _x_<sup>_′_</sup> _k_<sup>=</sup> _xk − x_ 0 llegamos al esquema recursivo 





El cual converge y converge a ( _I − M_ )<sup>_−_1</sup> _c_<sup>_′_</sup> , por lo tanto _xk_ converge a 





Una consecuencia del corolario es que la iteraci´on de Richardson (1.6) converge si _∥I − A∥ <_ 1. A veces podemos precondicionar el sistema de ecuaciones multiplicando ambos miembros de (9.1) por una matriz _B_ 



de manera que la convergencia del m´etodo iterativo es mejorada. En el contexto de la iteraci´on de Richardson las matrices _B_ tales que permiten aplicar el Lema de Banach y su corolario se llaman _inversas aproximadas_ 

**Definici´on 1.2.1.** _B_ es una inversa aproximada de _A_ si _∥I − BA∥ <_ 1. 

El siguiente teorema es llamado com´unmente _Lema de Banach_ . 

**Teorema 1.2.1.** Si _A_ y _B ∈_ IR<sup>_N×N_</sup> y _B_ es una inversa paroximada de _A_ , entonces _A_ y _B_ son no singulares y 



y 



**Demostraci´on.** Sea _M_ = _I − BA_ , entonces _I − M_ = _BA_ es no singular y por lo tanto _B_ y _A_ son no-singulares y 



[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 

y 



Por otra parte, 



La demostraci´on de las otras desigualdades es similar. � 

Notar que hay una cierta simetr´ıa en el rol jugado por _A_ y _B_ . De hecho deber´ıamos definir inversa aproximada _por derecha_ y _por izquierda_ y _B_ ser´ıa la inversa aproximada por derecha de _A_ . La iteraci´on de Richardson, precondicionada aproximadamente, tiene la forma 



Si _∥I − BA∥≪_ 1 las iteraciones convergen r´apido y adem´as, (por el Lema 1.2.1) las decisiones basadas en el residuo precondicionado _∥B_ ( _b − A x_ ) _∥_ reflejar´an muy bien el error cometido. 

##### **9.1.3. Radio espectral** 

El an´alisis de _§_ 9.1.2 relacion´o la convergencia del esquema iterativo (9.60) a la norma de la matriz _M_ . Sin embargo la norma de _M_ puede ser peque˜na en alguna norma y grande en otras. De aqu´ı que la performance de la iteraci´on no sea completamente descripta por _∥M ∥_ . El concepto de _radio espectral_ da una descripci´on completa. Sea _σ_ ( _A_ ) el conjunto de autovalores de _A_ . 

**Definici´on 1.3.1.** El radio espectral de _A_ es 



El radio espectral de _A_ es independiente de la norma particular de _M_ . De hecho 



ya que, si _Av_ = _λ_ max _v_ , entonces 



Siempre que _∥ . ∥_ sea una norma inducida. En realidad puede demostrarse algo as´ı como que _ρ_ ( _A_ ) es el ´ınfimo de todas las normas de _A_ . Esto es el enunciado del siguiente teorema (que no demostraremos aqu´ı). 

**Teorema 1.3.1.** Sea _A ∈_ IR<sup>_N×N_</sup> . Para cada _ϵ >_ 0 existe una norma inducida _∥ . ∥_ tal que _ρ_ ( _A_ ) _> ∥A∥− ϵ_ . 

Puede verse que, si _ρ_ ( _M_ ) _≥_ 1 entonces existen _x_ 0 y _c_ tales que (9.60) diverge. Efectivamente, sea _v_ el autovalor tal que _Mv_ = _λv_ y _|λ|_ = _ρ_ ( _M_ ) _≥_ 1. Tomemos _x_ 0 = _v_ , _c_ = 0, entonces 



es claro que no converge. 

**237** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 



<!-- Start of picture text -->
k<br><!-- End of picture text -->

Figura 9.1: Historia de convergencia t´ıpica 

**Teorema 1.3.2.** Sea _M ∈_ IR<sup>_N×N_</sup> . La iteraci´on (9.60) converge para todos _x_ 0 _, c ∈_ IR<sup>_N×N_</sup> sy y solo si _ρ_ ( _M_ ) _<_ 1. 

**Demostraci´on.** Si _ρ_ ( _M_ ) _>_ 1 entonces en cualquier norma tal que _∥M ∥ >_ 1 la iteraci´on no converge por el p´arrafo anterior. Por otra parte, si _ρ_ ( _M_ ) _<_ 1 entonces, tomando _ϵ_ = (1 _− ρ_ ( _M_ )) _/_ 2, existe una norma tal que 



y por lo tanto converge. � 

**Tasa de convergencia de m´etodos estacionarios.** Para un esquema convergente de la forma 



podemos estimar la tasa de convergencia como, 





y por lo tanto 







Es usual visualizar la convergencia del m´etodo graficando _∥rk∥_ versus _k_ . Como _∥rk∥_ 2 puede reducirse en varios ´ordenes de magnitud durante la iteraci´on, es usual usuar ejes logar´ıtmicos para _∥rk∥_ 2. Por otra parte (9.103) no s´olo es una estimaci´on de la tasa de convergencia sino que, de hecho, muchas veces el residuo de la ecuaci´on termina comport´andose de esta forma, despu´es de un cierto transitorio inicial (ver figura) es decir 



**238** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 



<!-- Start of picture text -->
k<br><!-- End of picture text -->

Figura 9.2: Estimaci´on de la tasa de convergencia 

Este tipo de comportamiento se refleja en una recta de pendiente log _γ_ en el gr´afico. Un ´ındice de la velocidad de convergencia es el n´umero de iteraciones _n_ necesario para bajar el residuo un factor 10, 







para problemas muy mal condicionados 



y entonces, 



A veces podemos calcular la tasa de convergencia “experimentalmente” conociendo el valor del residuo _∥rk∥_ para dos iteraciones _k_ 1, _k_ 2. Asumiendo que en el intervalo _k_ 1 _≤ k ≤ k_ 2 la tasa de convergencia es constante como en (9.105) (ver figura 9.2), entonces 



de donde 



y entonces, 





##### **9.1.4. Saturaci´on del error debido a los errores de redondeo.** 

A medida que vamos iterando el residuo va bajando en magnitud. Cuando el valor del residuo pasa por debajo de cierto valor umbral dependiendo de la precisi´on de la m´aquina ( _∼_ 10<sup>_−_15</sup> en Octave, 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

**239** 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 



<!-- Start of picture text -->
1<br>máquina de<br>precisión finita<br>1e-10<br>máquina de<br>precisión infinita<br>1e-20<br>0 2000 4000 6000 8000 10000<br>iter<br><!-- End of picture text -->

Figura 9.3: Saturaci´on del error por errores de redondeo. 

Fortran ( `real *8` ) o C (tipo `double` )) se produce, debido a errores de redondeo, un efecto de _saturaci´on_ (ver figura 9.3). Es decir, al momento de calcular (9.50), es claro que incluso reemplazando _xk_ por la soluci´on exacta _x_<sup>_∗_</sup> el residuo (calculado en una m´aquina de precisi´on finita) dara un valor no nulo del orden de la precisi´on de la m´aquina. Por supuesto este umbral de saturaci´on es relativo a la norma de cada uno de los t´erminos intervinientes y adem´as para sistemas mal condicionados, el umbral se alcanza antes por un factor _κ_ ( _A_ ), es decir que 



##### **9.1.5. M´etodos iterativos estacionarios cl´asicos** 

Hay otras formas alternativas a (9.58) de llevar _Ax_ = _b_ a un problema de punto fijo. Los m´etodos como Jacobi, Gauss-Seidel y relajaciones sucesivas se basan en descomposiciones de _A_ ( _“splittings”_ ) de la forma, 



con _A_ 1 no-singular y f´acil de factorizar. El nuevo problema de punto fijo es 



El an´alisis del m´etodo se basa en estimar el radio espectral de _M_ = _−A_<sup>_−_</sup> 1<sup>1</sup><sup>_A_2.</sup> 

**Iteraci´on de Jacobi.** Corresponde a tomar 







[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 

donde _L, U, D_ son las partes triangular inferior, superior y diagonal de _A_ = _L_ + _U_ + _D_ . El esquema iterativo es 



Notar que _A_ 1 es diagonal y, por lo tanto, trivial de invertir. La matriz de iteraci´on correspondiente es 



**Teorema 1.4.1.** Sea _A ∈_ IR<sup>_N×N_</sup> y asumamos que para cualquier 1 _≤ i ≤ N_ 



entonces _A_ es no-singular y Jacobi converge. 

**Demostraci´on.** Veamos que 



Entonces, 



Por lo tanto la iteraci´on converge a la soluci´on de 





entonces _Ax_ = _b_ y _I − M_ = _D_<sup>_−_1</sup> _A_ es no-singular y _A_ es no-singular. 

**Iteraci´on de Gauss-Seidel.** En este esquema se reemplaza la soluci´on aproximada con el nuevo valor tan pronto como ´este es calculado, 



que puede escribirse como 



El split correspondiente es 



y la matriz de iteraci´on 



_A_ 1 es triangular inferior y por lo tanto _A_<sup>_−_</sup> 1<sup>1</sup> es f´acil de calcular. Notar tambi´en que a diferencia de Jacobi, depende del ordenamiento de las inc´ognitas. Tambi´en podemo hacer un “backward GaussSeidel” con el splitting 





[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 

La iteraci´on es 



y la matriz de iteraci´on 



**Gauss-Seidel sim´etrico.** Podemos combinar alternando una iteraci´on de forward GS con una de backward GS poniendo 





La matriz de iteraci´on es 

_M_ SGS = _M_ BGS _M_ GS = ( _D_ + _U_ )<sup>_−_1</sup> _L_ ( _D_ + _L_ )<sup>_−_1</sup> _U_ (9.135) 

Si _A_ es sim´etrica, entonces _U_ = _L_<sup>_T_</sup> y 



Queremos escribir estos esquemas como una iteraci´on de Richardson precondicionada, es decir que queremos encontrar _B_ tal que _M_ = _I − BA_ y usar _B_ como inversa aproximada. Para la iteraci´on de Jacobi, 



y para Gauss-Seidel sim´etrico 



**Verificaci´on.** Debemos demostrar que _M_ SGS = _I − B_ SGS _A_ . Efectivamente, 











**Sobrerelajaci´on.** Consideremos iteraci´on simple de Richardson 



Si vemos que _xk_ se acerca mon´otonamente y lentamente a _x_<sup>_∗_</sup> podemos pensar en “acelerarlo” (ver figura 9.4) diciendo que el m´etodo iterativo en realidad nos predice un estado intermedio _<u>xk</u>_ +1, y buscamos el vector de iteraci´on _xk_ +1 sobre la recta que une _xk_ con _<u>xk</u>_ +1 





[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 



Figura 9.4: Aceleraci´on de la convergencia por sobre-relajaci´on 

Veremos m´as adelante que el valor ´optimo de _ω_ est´a relacionado con la distribuci´on de autovalores de la matriz de iteraci´on en el plano complejo. Mientras tanto podemos ver intuitivamente que 

_ω_ = 1 deja el esquema inalterado 

_ω >_ 1 tiende a acelerar la convergencia si el esquema converge lenta y mon´otonamente 

_ω <_ 1 tiende a desacelerar la convergencia si el esquema se hace inestable. 

**Esquema iterativo de Richardson con relajaci´on para matrices spd.** Aplicando el m´etodo de relajaci´on a la iteraci´on b´asica de Richardson obtenemos el esquema 



que puede reescribirse como 



de manera que la matriz de iteraci´on es 



Asumiendo que _A_ es spd, el espectro de _M_ SR esta dado por 



pero como _A_ es spd, los autovalores _λ ∈ σ_ ( _A_ ) son reales y positivos. Asumamos que est´an ordenados _λ_ 1 _≥ λ_ 2 _≥ . . . ≥ λN_ . Tambi´en denotaremos _λ_ min = _λN_ , _λ_ max = _λ_ 1. Los autovalores de _M_ SR se comportan en funci´on de _ω_ como se observa en la figura 9.5. Para un dado _ω_ todos los autovalores de _M_ SR est´an comprendidos entre los autovalores correspondientes a _λ_ min y _λ_ max (la regi´on rayada de la figura). Para _ω_ suficientemente chico todos los autovalores se concentran cerca de la unidad. Para un cierto valor _ω_ crit el autovalor correspondiente a _λ_ max se pasa de _−_ 1 con lo cual la iteraci´on no converge. El valor de _ω_ crit est´a dado entonces por 



La tasa de convergencia est´a dada por _γ_ = m´ax _j |_ 1 _− ωλj|_ , y queremos buscar el _ω_ que da la mejor tasa de convergencia, es decir el m´ınimo _γ_ . Como los 1 _− ωλj_ est´an comprendidos en el intervalo 1 _− ωλ_ min _,_ 1 _− ωλ_ max, se cumple que 



[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.1. Conceptos b´asicos de m´etodos iterativos estacionarios_ 

Ahora bien, para un cierto intervalo de valores 0 _< ω < ω_ opt el m´aximo corresponde a 1 _− ωλ_ min y _γ_ decrece al crecer _ω_ , mientras que para _ω_ opt _< ω < ω_ crit el m´aximo est´a dado por _−_ 1 + _ωλ_ max y crece con _ω_ . Para _ω_ = _ω_ opt ambos valores coinciden y entonces 



de donde 



Adem´as es f´acil ver que _γ_ es m´ınimo para _ω_ = _ω_ opt, de ah´ı el nombre de _coeficiente de relajaci´on ´optimo_ . 

Podemos ver tambi´en que, para n´umeros de condici´on muy altos el valor ´optimo se encuentra muy cerca del valor cr´ıtico, 



La tasa de convergencia que se obtiene para _ω_ opt es de 





que para sistemas mal condicionados ( _κ ≫_ 1) es 



**M´etodo de relajaciones sucesivas.** La combinaci´on de Gauss-Seidel puede mejorarse dram´aticamente con sobre-relajaci´on para una cierta elecci´on apropiada del par´ametro de relajaci´on. Este m´etodo es muy popular y se llama SSOR por _“Successive Standard Over-Relaxation”_ . Partiendo de (9.127) y reescribi´endolo como 



y combinando con la sobre-relajaci´on est´andar (9.148) 



llegamos a 





de manera que la matriz de iteraci´on es 



**244** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 



<!-- Start of picture text -->
C<br>B<br>A<br><!-- End of picture text -->

Figura 9.5: Comportamiento de los autovalores de la matriz de iteraci´on en funci´on del par´ametro de relajaci´on 

#### **9.2. M´etodo de Gradientes Conjugados** 

##### **9.2.1. M´etodos de Krylov y propiedad de minimizaci´on** 

Los m´etodos de Krylov (a diferencia de los m´etodos estacionarios que vimos hasta ahora), no tienen una matriz de iteraci´on. Los que describiremos m´as en profundidad son Gradientes Conjugados y GMRES. Ambos se basan en que la _k_ -´esima iteraci´on minimiza alguna medida del error en el espacio af´ın 



donde _x_ 0 es la iteraci´on inicial y el subespacio de Krylov _Kk_ es 



**Nota:** El papel de _x_ 0 y _b_ puede intercambiarse, lo importante es _r_ 0 (esto vale pr´acticamente para todos los m´etodos iterativos). De hecho, el esquema es invariante ante translaciones del origen, es decir las iteraciones para los dos sistemas siguientes 





con 







son equivalentes (es decir, _x_<sup>_′_</sup> _k_<sup>=</sup><sup>_xk −x_¯),yaque</sup> 





[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 

de manera que el espacio de Krylov es el mismo. Entonces podemos, o bien eliminar _b_ haciendo _x_ ¯ = _x_<sup>_∗_</sup> o eliminar _x_ 0 haciendo _x_ ¯ = _x_ 0. 

El residuo es _r_ = _b − Ax_ , de manera que _{rk}_ para _k ≥_ 0 denota la secuencia de residuos _rk_ = _b − Axk_ . Como antes, _x_<sup>_∗_</sup> = _A_<sup>_−_1</sup> _b_ , es la soluci´on del sistema. El m´etodo de GC es en realidad un m´etodo directo, en el sentido de que llega a la soluci´on en un n´umero finito de pasos, de hecho veremos m´as adelante que converge en _N_ (o menos) iteraciones, es decir que 



GC es un m´etodo que sirve en principio s´olo para matrices sim´etricas y definidas positivas (spd). Recordemos que _A_ es sim´etrica si _A_ = _A_<sup>_T_</sup> y definida positiva si 



Luego veremos que podemos extender cualquier sistema (no sim´etrico ni definido positivo) a un sistema spd. Como _A_ es spd. podemos definir una norma como 



es la llamada _“norma A”_ o _“norma energ´ıa”_ ya que en muchos problemas pr´acticos el escalar resultante ( _∥x∥_<sup>2</sup> _A_<sup>)representalaenerg´ıacontenidaenelcamporepresentadoporelvector</sup><sup>_x_.</sup> El esquema a seguir ser´a 

Descripci´on formal del m´etodo y consecuencias de la propiedad de minimizaci´on 

Criterio de terminaci´on, performance, precondicionamiento 

Implementaci´on 

La _k_ -´esima iteraci´on de GC _xk_ minimiza el funcional cuadr´atico 



en _x_ 0 + _Kk_ . 

Notemos que si hacemos el m´ınimo sobre todo IR<sup>_N_</sup> , entonces si 



vale que 



**Lema 2.1.1.** Sea _S ∈_ IR<sup>_N_</sup> , si _xk_ minimiza _φ_ sobre _S_ , entonces tambi´en minimiza _∥x_<sup>_∗_</sup> _− x∥A_ = _∥r∥A−_ 1 sobre _S_ . 

**Demostraci´on.** Notemos que 



[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] **246** 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 

pero _A_ = _A_<sup>_T_</sup> , entonces _x_<sup>_∗T_</sup> _A x_ = _x_<sup>_T_</sup> _A_<sup>_T_</sup> _x_<sup>_∗_</sup> = _x_<sup>_T_</sup> _A x_<sup>_∗_</sup> y _Ax_<sup>_∗_</sup> = _b_ , de manera que 



Pero _x_<sup>_∗T_</sup> _A x_<sup>_∗_</sup> =cte de manera que _xk_ minimiza _∥x − x_<sup>_∗_</sup> _∥A_ . Sea _e_ = _x − x_<sup>_∗_</sup> , entonces, 









Usaremos este lema para el caso _S_ = _x_ 0 + _Kk_ . 

##### **9.2.2. Consecuencias de la propiedad de minimizaci´on.** 

El lema 2.1.1 implica que, como _xk_ minimiza _φ_ sobre _x_ 0 + _Kk_ , 



para todo _w ∈ x_ 0 + _Kk_ . Como _w ∈ x_ 0 + _Kk_ puede ser escrito como 



para ciertos coeficientes _{γj}_ , podemos expresar _x_<sup>_∗_</sup> _− w_ como 



Pero 



entonces 





donde el polinomio 



tiene grado _k_ y satisface _p_ (0) = 1. Entonces, 



[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 

_Pk_ denota el conjunto de los polinomios de grado _k_ . El teorema espectral para matrices spd afirma que existe una base de autovectores _{ui}_<sup>_N_</sup> _i_ =1<sup>conautovalores</sup><sup>_{λi}_</sup> 



con _ui_ , _λi_ reales, _λi >_ 0 y los _ui_ ortogonales entre s´ı, es decir que 



Adem´as formamos las matrices 



La descomposici´on diagonal de _A_ es 



Adem´as y Definamos y notemos que 

Entonces, para todo _x ∈_ IR<sup>_N_</sup> 

y volviendo a (9.199) 

donde _σ_ ( _A_ ) es el conjunto de autovalores de _A_ . 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

**248** 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 



Figura 9.6: GC con tasa de convergencia muy lenta. 

**Corolario 2.2.1.** Sea _A_ spd y _{xk}_ las iteraciones de GC. Sea _p_ ¯ _k_ cualquier polinomio de grado _k_ tal que _p_ ¯ _k_ (0) = 1, entonces 



Los polinomios que satisfacen _p_ ¯ _k_ (0) = 1 se llaman polinomios residuales. 

**Definici´on 2.2.1.** El conjunto de polinomios residuales de orden _k_ es 



La forma de estimar la convergencia de GC es construir secuencias de polinomios residuales basados en la informaci´on de como est´an distribuidos los autovalores de _A_ (es decir de _σ_ ( _A_ )). Un primer resultado es ver que GC es un m´etodo directo 

**Teorema 2.2.1.** Sea _A_ spd. Entonces GC converge antes de las _N_ iteraciones. **Demostraci´on.** Sea _{λi}_<sup>_N_</sup> _i_ =1<sup>losautovaloresde</sup><sup>_A_.Tomemoscomopolinomioresidual</sup> 



Pero _p_ ¯ _∈PN_ ya que tiene grado _N_ y _p_ ¯(0) = 1. Entonces, de la estimaci´on de error (9.215) 



ya que, por construcci´on, _p_ ¯( _z_ ) = 0 para todos los _z ∈ σ_ ( _A_ ). �. 

Sin embargo, desde el punto de vista pr´actico esto no es tan bueno como suena. Veremos que, bajo ciertas condiciones, la convergencia puede ser muy lenta y desde el punto de vista pr´actica haya que esperar hasta _N_ iteraciones para que el residuo baje de la tolerancia aceptable. 

Es decir, si evaluamos a GC como un m´etodo iterativo, entonces debemos poder evaluar la tasa de convergencia para _k < N_ (la pendiente de la curva de convergencia). 

**249** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 

**Teorema 2.2.2.** Sea _A_ spd con autovalores _{ui}_<sup>_N_</sup> _i_ =1<sup>.Sea</sup><sup>_b_unacombinaci´onlinealde</sup><sup>_k_delos</sup> autovectores de _A_ . Por simplicidad asumiremos que los autovectores de _A_ est´an ordenados de manera que estos autovectores son los primeros _k_ 



Entonces la iteraci´on de GC para _Ax_ = _b_ con _x_ 0 = 0 termina en, a lo sumo, _k_ iteraciones **Demostraci´on.** Por el teorema espectral 



ya que 



Usamos el polinomio residual 



y puede verse que _p_ ¯ _∈Pk_ y _p_ ¯( _λl_ ) = 0 para 1 _≤ l ≤ k_ y 



De manera que, por (9.199) y _x_ 0 = 0 se deduce que 



**Teorema 2.2.3.** Sea _A_ spd y supongamos que hay exactamente _k ≤ N_ autovalores distintos de _A_ . Entonces GC termina en, a lo sumo, _k_ iteraciones **Demostraci´on.** Usar el polinomio residual 



**250** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 



<!-- Start of picture text -->
N<br>k<br>máquina de precisión finita<br>precisión de la máquina<br>máquina de precisión infinita<br><!-- End of picture text -->

Figura 9.7: Comportamiento del residuo en m´aquinas de precisi´on finita. 

##### **9.2.3. Criterio de detenci´on del proceso iterativo.** 

En una m´aquina de precisi´on infinita debemos ver que el residuo desciende bruscamente a cero en la iteraci´on _N_ (puede ser antes bajo ciertas condiciones, como hemos visto en algunos casos especiales), pero en la pr´actica no se itera GC hasta encontrar la soluci´on exacta sino hasta que cierto criterio sobre el residuo (por ejemplo _∥rk∥ <_ 10<sup>_−_6</sup> ) es alcanzado. De hecho, debido a errores de redondeo, ocurre que no se puede bajar de un cierto nivel de residuo relacionado con la precisi´on de la m´aquina (10<sup>_−_15</sup> en Fortran doble precisi´on y tambi´en en Octave) y el n´umero de operaciones necesarias para calcular el residuo. Entonces, si ese nivel de residuo est´a por encima del valor del residuo que obtendr´ıamos en la iteraci´on _N −_ 1 (ver figura 9.7), no veremos el efecto de la convergencia en _N_ iteraciones, sino que GC se comporta como un m´etodo iterativo, de manera que lo importante es la tasa de convergencia media del m´etodo. 

En la pr´actica se usa usualmente como criterio de detenci´on del proceso iterativo 



Sin embargo, las estimaciones de error basadas en la propiedad de minimizaci´on est´an expresadas en la norma energ´ıa del error 



El siguiente lema relaciona la norma eucl´ıdea del error con la norma energ´ıa del error **Lema 2.3.1.** Sea _A_ spd, con autovalores _λ_ 1 _≥ λ_ 2 _≥ . . . ≥ λN_ . Entonces para todo _z ∈_ IR<sup>_N_</sup> 



y 



###### **Demostraci´on.** 



[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 

Sean _{ui, λi}_ los autovectores, autovalores de _A_ , con _u_<sup>_T_</sup> _i_<sup>_uj_=</sup><sup>_δij_.Entonces,</sup> 



Entonces, 



###### **Lema 2.3.2.** 



Recordemos que en la norma _L_ 2 para matrices spd. vale que 







Usando (9.230) y (9.231) 



Consideremos un ejemplo simple 



Por lo tanto _k_ 2 = 1 _,_ 22 (relativamente peque˜no). Tomemos el polinomio (ver figura 9.8) 



Como vemos en la figura todos los polinomios se anulan en _z_ = 10 la mitad del intervalo donde se encuentran los autovalores. Esta regi´on est´a sombreada en la figura. El m´aximo valor de _p_ ¯ _k_ ( _z_ ) sobre el intervalo se alcanza en los extremos del intervalo 





[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 



<!-- Start of picture text -->
1<br>9 11 z<br><!-- End of picture text -->

Figura 9.8: Polinomio residual apropiado para el caso (9.243) 



<!-- Start of picture text -->
1<br><!-- End of picture text -->





<!-- Start of picture text -->
z<br><!-- End of picture text -->

Figura 9.9: Polinomio residual basado en los polinomios de Tchebyshev 

lo cual implica que la tasa de convergencia es _γ_ = 1 _/_ 10 y el n´umero de iteraciones por orden de magnitud es 



Mientras tanto, para los residuos 







Para obtener la mejor estimaci´on basada solamente en la informaci´on del autovalor m´aximo y m´ınimo debemos construir un polinomio de tal forma que tome los valores m´as bajos posibles en el intervalo _λ_ 1 _≤ z ≤ λn_ (ver figura 9.9). Estos polinomios pueden construirse en base a los _polinomios_ 

**253** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 

_de Tchebyshev_ . Efectivamente, hagamos el cambio de variable 



de manera que _θ_ = 0 en _z_ = _λN_ y _θ_ = _π_ en _z_ = _λ_ 1. Los polinomios de Tchebyshev _Tn_ ( _x_ ) se definen como 



Por ejemplo 







Por construcci´on vemos que _|Tn| ≤_ 1 en _|x| ≤_ 1, o sea _λn ≤ z ≤ λ_ 1. Entonces tomamos _pk_ ( _z_ ) = _Tn_ ( _x_ ( _z_ )) _/Tn_ ( _x_ ( _z_ = 0)). Como _x_ ( _z_ = 0) cae fuera del intervalo _|x| ≤_ 1 y _Tn_ crece fuertemente (como _x_<sup>_n_</sup> ) fuera del mismo, es de esperar que _Tn_ ( _x_ ( _z_ = 0)) _≫_ 1 y entonces _|pk_ ( _z_ ) _| ≪_ 1 en _λn ≤ z ≤ λ_ 1. Mediante estimaciones apropiadas para el valor de _Tn_ ( _x_ ( _z_ = 0)) puede demostrarse que 



Podemos ver que, si _κ ≫_ 1, entonces podemos aproximar 



y entonces 



que debe ser comparada con _n ≈_ 1 _,_ 15 _κ_ para Richardson con _ω_ = _ω_ opt. La ventaja es clara, teniendo en cuenta que (como veremos despu´es) el costo (n´umero de operaciones) de una iteraci´on de gradientes conjugados es similar al de una iteraci´on de Richardson. 

Sin embargo, la convergencia puede ser mucho mejor que la dada por la estimaci´on anterior, dependiendo de la distribuci´on de los autovalores. Por ejemplo, asumamos que los autovalores est´an distribuidos en (ver figura 9.10) 



Entonces _κ_ = 400 y la estimaci´on anterior (basada s´olo en el n´umero de condici´on) da 



mientras que si tomamos el polinomio residual de la forma 



[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 



<!-- Start of picture text -->
1<br>1 .5<br>1  399 400 z<br><!-- End of picture text -->

Figura 9.10: Polinomio residual apropiado para un espectro con dos clusters de autovalores 

Entonces debemos estimar 



y 





Por lo tanto, 







que representa una tasa de convergencia 5 veces m´as rapida que la predicha s´olo en base al n´umero de condici´on de _A_ . 

En el contexto de GC la convergencia se puede mejorar tratando de encontrar precondicionamientos que disminuyan el n´umero de condici´on o bien que los autovalores est´an agrupados en peque˜nos _“clusters”_ (ver figura 9.11). 

##### **9.2.4. Implementaci´on de gradientes conjugados** 

La implementaci´on de GC se basa en que conociendo _xk_ pueden ocurrir dos situaciones. O bien _xk_ +1 = _xk_ = _x_<sup>_∗_</sup> , o bien 



donde _pk_ +1 _̸_ = 0 es una _direcci´on de b´usqueda_ que puede obtenerse en forma sencilla y _αk_ +1 es un escalar que se obtiene minimizando el funcional de GC sobre la recta, 



[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 











_z_ 

_Agrupar autovalores en pequeños clusters (GC)_ 

Figura 9.11: Posibles estrategias de precondicionamiento 

Recordar que el funcional estaba definido como 



Entonces 





de donde 



Si _xk_ +1 = _xk_ entonces _α_ = 0, pero esto s´olo ocurre si _xk_ es la soluci´on. **Lema.** _rl ∈Kk_ para todo _l < k_ 

**Demostraci´on.** Lo haremos por inducci´on en _k_ . Para _k_ = 1 _Kk_ = span _{r_ 0 _}_ y obviamente se verifica que _r_ 0 _∈Kk_ . Ahora asumiendo que es v´alido para _k_ lo demostraremos para _k_ + 1. Para _l < k_ , se cumple que _rl ∈Kk ⊂Kk_ +1, por lo tanto s´olo resta demostrarlo para _rk_ . Pero 



y entonces, 







**Lema 2.4.1.** Sea _A_ spd. y _{xk}_ las iteraciones de GC, entonces 



[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 

**Demostraci´on.** Como _xk_ minimiza _φ_ en _x_ 0 + _Kk_ , entonces para todo _ξ ∈Kk_ 



pero _∇φ_ = _−r_ , entonces 



Ahora bien, si _xk_ +1 = _xk_ entonces _rk_ = _rk_ +1 y 



por lo tanto _xk_ = _x_<sup>_∗_</sup> .De paso esto permite ver tambi´en que GC converge en _N_ iteraciones (cosa que ya hemos demostrado bas´andonos en la propiedad de minimizaci´on.) Efectivamente, supongamos que _rk̸_ = 0 entonces 



Pero para _k_ = _N_ dim _Kk_ = _N_ entonces _rk_ +1 = 0. 

**Lema 2.4.2.** Si _xk̸_ = _x_<sup>_∗_</sup> entonces _xk_ +1 = _xk_ + _αk_ +1 _pk_ +1 donde _pk_ +1 est´a determinado (a menos de una constante multiplicatva) por 



**Demostraci´on.** Como _Kk ⊂Kk_ +1 





pero _Axk − b_ = _rk ⊥ ξ_ para todo _ξ ∈Kk_ de manera que 



y como dim _Kk_ +1 = dim _Kk_ + 1, esto define ´unicamente a _pk_ +1. 

Esta propiedad se llama que _pk_ +1 es _“conjugado”_ a _Kk_ . Ahora bien, tomando _rk_ y ortogonaliz´andolo con respecto a _Kk_ podemos obtener _pk_ +1. Entonces, 



**Teorema 2.4.1.** Sea _A_ spd. y asumamos que _rk̸_ = 0. Sea _p_ 0 = 0. Entonces _pk_ +1 = _rk_ + _βk_ +1 _pk_ para alg´un escalar _βk_ +1 y _k ≥_ 0. **Demostraci´on.** ver libro. 

**Lema 2.4.3.** Las siguientes f´ormulas son tambi´en v´alidas para obtener los _αk_ y _βk_ . 



**Demostraci´on.** Ver libro. 

**Algoritmo 2.4.1.** `cg(` _x, b, A, ϵ, k_ max `)` 

**257** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 

1. _r_ = _b − Ax_ , _ρ_ 0 = _∥r∥_<sup>2</sup> 2<sup>,</sup><sup>_k_= 1</sup> 

2. Do while<sup>_√_</sup> _<u>ρk−</u>_ 1 _> ϵ ∥b∥_ 2 y _k < K_ max a. If _k_ = 1 then 

_p_ = _r_ else _β_ = _ρk−_ 1 _/ρk−_ 2 _p_ = _r_ + _βp_ endif b. _w_ = _Ap_ c. _α_ = _ρk−_ 1 _/_ ( _p_<sup>_T_</sup> _w_ ) d. _x_ = _x_ + _αp_ e. _r_ = _r − αw_ f. _ρk_ = _∥rk∥_ 2 g. _k_ = _k_ + 1 

Notar que no es necesario formar expl´ıcitamente la matriz _A_ (ni siquiera en forma “sparse”, es decir, la lista de _{i, j, aij}_ ), sino que solo es necesario definir una rutina que, dado _x_ calcule _Ax_ . Esto se llama una _operaci´on matriz-vector_ . Debido a esta propiedad de no necesitar tener la matriz almacenada, GC es llamado un m´etodo _m´atrix free_ . 

**Costo de GC.** Las variables que se deben mantener almacenadas durante la iteraci´on son _x, w, p, r_ o sea 4 _N_ elementos. En cuanto al n´umero de operaciones, 

- 1 producto matriz vector (paso 2.b) 

- 2 productos escalares (pasos 2.c y 2.f) 

- 3 “axpys” (pasos 2.a, 2.d y 2.e). 

Una operaci´on “axpy” es aquella de la forma _y ← αx_ + _y_ , es decir adicionar a un vector _x_ un m´ultiplo escalar de otro vector _y_ . (El nombre proviene de que la rutina de la librer´ıa BLAS que realiza esta operaci´on y que a su vez es una descripci´on mnemot´ecnica de la operaci´on que se realiza.). De todos, el que requiere m´as operaciones es generalmente el producto matriz vector, sobre todo en la versi´on _matrix free_ y sobre todo cuanto m´as compleja es la f´ısica del problema. Por ejemplo, si _x_ representa el vector de potenciales nodales guardados por columnas para una malla homog´enea de paso _h_ (como en la funci´on `laplacian.m` usada en la Gu´ıa 1), entonces la implementaci´on de _Ax_ es 

```
phi=reshape(phi,n-1,n-1);
```

- `% range of indices of internal nodes II=(2:n); JJ=II;` 

- `% Include the boundary nodes Phi=zeros(n+1);` 

**258** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 

```
Phi((2:n),(2:n))=phi;
```

```
%Usethestandard5pointformula
lap_phi=((-Phi(II+1,JJ)...
```

```
-Phi(II-1,JJ)...
-Phi(II,JJ+1)...
-Phi(II,JJ-1)...
+4*Phi(II,JJ))/h^2);
```

```
lap_phi=lap_phi(:);
```

donde vemos que b´asicamente el n´umero de operaciones necesario es _O_ (5 _N_ ), ya que 5 es el n´umero de puntos involucrados en el stencil de Poisson. Sin embargo, si la complejidad de la representaci´on aumenta el c´omputo se mantiene en general _O_ ( _N_ ) pero con cada vez m´as operaciones por nodo. Por ejemplo, si la malla est´a refinada hacia los lados, es decir si el _h_ no es constante, entonces hay que multiplicar cada fila por un _h_ distinto. Si adem´as permitimos que las l´ıneas de la malla no sean paralelas a los ejes, entonces habr´a que calcular los _coeficientes m´etricos_ de la malla. Si consideramos el uso de mallas no estructuradas con el m´etodo de los elementos finitos el c´alculo de las matrices de cada elemento aumentar´a todav´ıa m´as el n´umero de operaciones por nodo. 

**Costo de GC como m´etodo directo.** Si bien el m´etodo de GC se usa raramente como m´etodo directo, por razones que veremos m´as adelante, vamos a estimar el n´umero de operaciones necesarios y compararlo con eliminaci´on de Gauss. Considerando un cuadrado de _N_ = _n × n_ nodos en 2D y un cubo de _N_ = _n × n × n_ en 3D, tenemos que, 

Ancho de banda de la matriz: _m_ = _n_ en 2D, _m_ = _n_<sup>2</sup> en 3D. 

- N´umero total de inc´ognitas: _N_ = _n_<sup>2</sup> en 2D, _N_ = _n_<sup>3</sup> en 3D. 

- N´umero de op. Gauss: _N_<sup>2</sup> en 2D, _N_<sup>2</sup><sup>_,_33</sup> en 3D 

- N´umero de op. GC/directo: _N_<sup>2</sup> en 2D, _N_<sup>2</sup> en 3D 

Hemos hecho uso de que el n´umero de operaciones para eliminaci´on de Gauss es _Nm_<sup>2</sup> . Para GC hemos usado 

n´umero de op. = _O_ (n´umero de iter. _×_ nro. de op. por iter.) (9.287) = _O_ ( _N_<sup>2</sup> ) (9.288) 

Vemos que, incluso como m´etodo directo, GC llega a ser m´as competitivo en 3D. De todas formas, como ya hemos mencionado, por el problema de precisi´on finita (ver figura 9.7) en general para problemas grandes se llega a la precisi´on de la m´aquina antes de las _N_ iteraciones. 

En cuanto a la capacidad de almacenamiento, GC obviamente requiere mucho menos memoria ( _O_ ( _N_ ) para GC contra _O_ ( _N_<sup>1</sup><sup>_,_5</sup> ) en 2D y _O_ ( _N_<sup>1</sup><sup>_,_33</sup> ) en 3D para Gauss). 

**259** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 



<!-- Start of picture text -->
1e+10<br>1<br>1e-10<br>residuos verdaderos<br>1e-20<br>1e-30<br>1e-40<br>1e-50<br>residuos calculados<br>1e-60 de la relacion en diferencias<br>1e-70<br>0 100 200 300 400 500 600 700<br><!-- End of picture text -->

Figura 9.12: Gradientes Conjugados y los residuos verdaderos. 

**Comparaci´on como m´etodo iterativo con Richardson.** Tanto para Richardson como para GC el costo para bajar el error un order de magnitud es, b´asicamente 



Donde _n_ es el n´umero de iteraciones necesario para bajar el error un orden de magnitud. Asumiendo que el costo de las iteraciones es pr´acticamene el mismo para los dos m´etodos (lo cual es v´alido si hacemos una implementaci´on _matrix free_ con una formulaci´on relativamente compleja, por ejemplo FEM), entonces los costos relativos est´an dados por las tasas de convergencia y, usando que en 3D _κ ∼ n_<sup>2</sup> = _N_<sup>2</sup><sup>_/_3</sup> . 



con lo cual la ganancia es evidente. 

##### **9.2.5. Los “verdaderos residuos”.** 

El algoritmo `cg(...)` (ver p´ag. 257) descripto m´as arriba tiene la particularidad de que los residuos no son calculados directamente usando (9.50) sino que son calculados en el paso (2e). Si bien las expresiones coinciden en una m´aquina de precisi´on infinita, debido a errores de redondeo los valores num´ericos obtenidos con uno u otro m´etodo pueden diferir en una m´aquina de precisi´on finita. En la figura 9.12 vemos los residuos calculados en un experimento calculados de las dos formas. El comportamiento de los verdaderos residuos es similar al observado para Richardson en _§_ 9.1.4. Sin embargo, es 

**260** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 

todav´ıa peor para GC. El residuo no s´olo no baja de el umbral _∥r∥_ sat de saturaci´on sino que empieza a crecer lentamente. Esto es muy peligroso desde el punta de vista pr´actico, ya que en el caso de Richardson el efecto de saturaci´on s´olo ocasiona un gasto de tiempo de c´alculo innecesario, pero en el caso de GC puede ocasionar una p´erdida de precisi´on. Podemos decir que Richardson es un m´etodo _estable_ ante errores de redondeo, mientras que GC es _inestable_ . Esta inestabilidad de GC se debe al hecho de que asume que los residuos van formando una base ortogonal y las direcciones de b´usqueda van siendo conjugadas (ec. (9.281)), y estas propiedades se van perdiendo por errores de redondeo. Esta inestabilidad es compartida por todos los m´etodos que se basan en estas propiedades de conjugaci´on, por ejemplo GMRES y los m´etodos que veremos despu´es. Para peor los residuos calculados por la expresi´on recursiva (2e) tienden a seguir descendiendo, de manera que si el usuario no verifica el verdadero valor del residuo, puede creer que realmente el error ha bajado (despu´es de 600 iteraciones) hasta 2 _×_ 10<sup>_−_64</sup> , mientras que el error verdadero est´a en el orden de 3 _×_ 10<sup>_−_3</sup> . 

Cuando calculamos los residuos directamente a partir de (9.50) decimos que se trata de los _verdaderos residuos_ . El porqu´e los residuos calculados seg´un el algoritmo `cg(...)` (ver p´ag. 257) tienden a bajar, en vez de _rebotar_ como lo hacen los verdeaderos residuos, puede entenderse m´as f´acilmente en el algoritmo de Richardson. Efectivamente, puede demostrarse simplemente que los residuos tambi´en satisfacen una relaci´on como la (9.101) a saber 



De manera que tambi´en podr´ıamos calcular los residuos utilizando recursivamente esta relaci´on. Pero esta relaci´on no involucra diferencias entre magnitudes grandes como en (9.50) y por lo tanto _∥rk∥_ calculado por esta expresi´on sigue descendiendo, independientemente de la precisi´on de la m´aquina. 

Una forma de corregir el el algoritmo `cg(...)` (ver p´ag. 257) es agregar una l´ınea en cada iteraci´on que calcule el verdadero residuo, _s´olo a los efectos de chequear convergencia_ , sin embargo esto involucra un producto matriz vector adicional por iteraci´on, es decir pr´acticamente duplica el costo del m´etodo. 

**Precondicionamiento.** Asumamos que tenemos una matriz _M_ f´acil de invertir y tal que _κ_ ( _MA_ ) _≪ κ_ ( _A_ ) o tal que los autovalores est´an agrupados en clusters. Entonces podemos tratar de resolver 



en vez del sistema original, ya que este est´a bien condicionado. Sin embargo, incluso si _M_ es spd. el producto de dos matrices spd. no es necesariamente spd. Basta con ver el ejemplo, 



_A_ y _M_ son spd. pero 



no es sim´etrica. Una posibilidad es buscar _M_ = _S_<sup>2</sup> y entonces redefinir 



[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

**261** 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 

y una vea obtenido _y_ obtener _x_ = _Sy_ . Como _SAS_ es equivalente a _S_<sup>2</sup> _A_ = _MA_ tienen la misma distribuci´on de autovalores y _SAS_ s´ı es spd. Pero falta resolver el problema de hallar _S_ , lo cual puede ser m´as complicado que hallar _M_ y por otra parte el c´alculo de _SAS_ por un vector involucra el c´alculo de dos productos matriz-vector adicionales, contra uno s´olo si precondicionamos de la forma (9.293). La soluci´on pasa por reproducir el algoritmo de Gradiente Conjugado pero reemplazando el producto escalar por _x_<sup>_T_</sup> _Mx_ y finalmente resulta en el siguiente algoritmo de GC precondicionado, 

Algoritmo 2.4.1. `pcg(` _x, b, A, M, ϵ, k_ max `)` 

1. _r_ = _b − Ax_ , _τ_ 0 = _r_<sup>_T_</sup> _Mr_ , _ρ_ 0 = _∥r∥_ 2, _k_ = 1 

2. Do while<sup>_√_</sup> _<u>ρk−</u>_ 1 _> ϵ ∥b∥_ 2 y _k < K_ max a. If _k_ = 1 then _z_ = _Mr_ else _β_ = _ρk−_ 1 _/ρk−_ 2 _p_ = _Mr_ + _βp_ endif b. _w_ = _αp_ c. _α_ = _ρk−_ 1 _/_ ( _p_<sup>_T_</sup> _w_ ) d. _x_ = _x_ + _αp_ e. _r_ = _r − αw_ f. _ρk_ = _∥rk∥_<sup>2</sup> 2<sup>,</sup><sup>_τk_=</sup><sup>_r_</sup> _k_<sup>_TMr_</sup> g. _k_ = _k_ + 1 

La modificaci´on principal del algoritmo pasa por reemplazar _p_ por _Mp_ en las definiciones de los _p_ y reemplazar los productos escalares _x_<sup>_T_</sup> _y_ por la forma cuadr´atica _x_<sup>_T_</sup> _My_ . Adem´as, ahora calculamos escalares _τk_ para el c´alculo de las direcciones _pk_ y escalares _ρk_ para chequear la convergencia. (Mientras que en la versi´on no precondicionada, _ρk_ = _τk_ ). 

El costo adicional m´as importante para el esquema precondicionado es un producto matriz-vector adicional con la matriz precondicionada. El costo del producto matriz-vector para el precondicionamiento puede variar mucho y depende de la complejidad del precondicionamiento. Por ejemplo, si tomamos _M_ como la inversa de la parte diagonal de _A_ (precondicionamiento Jacobi), entonces el costo es ´ınfimo, pero en el otro extremo podemos tomar _M_ = _A_<sup>_−_1</sup> . Entonces GC converge en una iteraci´on pero el costo de calcular _Mx_ es el costo de invertir _A_ !! Tenemos entonces que 



Cuanto m´as complejo es el precondicionador el _n_ tiende a disminuir pero el n´umero de operaciones tiende a aumentar debido al costo del c´alculo del precondicionamiento. Lo importante entonces, al evaluar la efectividad de un precondicionador es no s´olo evaluar c´omo aumenta la tasa de convergencia sino _tambi´en tener en cuenta el costo de evaluar Mx._ 

**Precondicionadores.** Existen una variedad de precondicionadores propuestos para diferentes problemas. Algunos son muy espec´ıficos para ciertas aplicaciones otros son puramente algebraicos, es decir su aplicaci´on es general para toda clase de problema (tal vez no su efectividad!). En el contexto de la resoluci´on de sistemas lineales provenientes de la discretizaci´on de ecuaciones en derivadas parciales por diferencias finitas o vol´umenes finitos podemos mencionar los siguientes 

**262** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 

Intr´ınsecos al problema 

- Resolvedores r´apidos de Poisson 

- Multigrilla 

- Descomposici´on de dominios 

- ADI 

De tipo general 

- Jacobi 

- Factorizaci´on incompleta 

- Precondicionamiento polinomial 

A continuaci´on haremos una breve descripci´on de los mismos 

**Resolvedores r´apidos de Poisson.** Si consideramos la ecuaci´on de Poisson 1D con condiciones de contorno peri´odicas la matriz resulta ser 



Sea _x_ de la forma 



donde i es la unidad imaginaria. Puede verse que ( _x_ ) _i_ es un autovector de _A_ . Esto vale, no s´olo para la matriz del laplaciano 1D, sino tambi´en para cualquier operador homog´eneo (que no depende de _x_ ) discretizado sobre una malla homog´enea. En este caso las filas de la matriz _A_ son las mismas, s´olo que se van corriendo una posici´on hacia la derecha a medida que bajamos una fila, es decir: 



donde _A_<sup>ˆ</sup> _µ_ es c´ıclico en _p_ de per´ıodo _N_ , es decir _A_<sup>ˆ</sup> _p_ + _N_ = _A_<sup>ˆ</sup> _p_ . Pero los _x_ de la forma (9.300) son la base que induce la transformada de Fourier, de manera que si _F_ es la matriz que tiene como columnas estos autovectores, vale que 



donde fft( _z_ ) indica el operador de transformada de Fourier tal como est´a definido en Matlab. Como las columnas de _F_ son autovectores de _A_ , entonces _F_<sup>_−_1</sup> _AF_ es diagonal y podemos tomar como precondicionamiento 



**263** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 

_<mark>malla fina</mark>_ 

###### _<mark>malla gruesa</mark>_ 

Figura 9.13: Mallas fina y gruesa para las t´ecnicas de multigrilla. 

por lo visto, para matrices peri´odicas, _M_ = _A_<sup>_−_1</sup> y entonces GC converger´a en una iteraci´on. La idea es que (9.303) puede ser un buen precondicionamiento incluso en condiciones m´as generales, por ejemplo cuando la matriz no es peri´odica o cuando la malla no es homog´enea. En cuanto al costo del precondicionamiento, multiplicar por _F_ y<sup>_−_1</sup> es equivalente a aplicar transformadas y antitransformadas de Fourier (aplicar las operaciones `fft( )` y `ifft( )` de Matlab. Estas requieren _O_ ( _N_ log2( _N_ )) operaciones y la inversi´on de la parte diagonal de _A_ s´olo requiere _O_ ( _N_ ) operaciones. La idea puede extenderse f´acilmente a 2D y 3D. 

**Multigrilla.** Si hacemos una descomposici´on modal del error, puede verse que el error en las componentes correspondientes a los autovalores m´as peque˜nos converge en general mucho m´as lentamente que para los autovalores m´as altos. Esto es m´as evidente para el m´etodo de Richardson, donde los factores de amplificaci´on 1 _− ωλi_ son muy cercanos a 1 para los autovalores m´as peque˜nos. A su vez, como ya hemos visto en los ejemplos, los autovalores altos est´an asociados a frecuencias altas (funciones que son muy oscilatorias espacialmente) mientras que los autovalores bajos est´an asociados a autofunciones suaves. Esto significa que despu´es de un cierto n´umero de iteraciones el error para las frecuencias altas se debe haber reducido mucho mientras que el grueso del error est´a en las componentes de baja frecuencia. Como las funciones suaves pueden ser restringidas a una malla m´as gruesa sin perder informaci´on, esto sugiere la idea de proyectar el problema a una malla m´as gruesa (digamos con _h_<sup>_′_</sup> = 2 _h_ y por lo tanto con la mitad de nodos, ver figura 9.13) y realizar una serie de iteraciones sobre esta malla para obtener una correcci´on. Una vez obtenida ´esta se interpola sobre la malla original y se agrega al vector de iteraci´on. La idea es que la correcci´on va a ser tan buena como si hubi´eramos iterado sobre la malla original pero a un costo igual a la 1 _/_ 2<sup>_nd_</sup> ya que la malla gruesa tiene la mitad de nodos. Esta idea puede ser aplicar recursivamente, ya que al iterar en la malla gruesa va a volver a ocurrir que despues de una serie de iteraciones va a quedar una fuerte componente del error en las frecuencias bajas y estas las podemos corregir iterando sobre una malla _h_<sup>_′′_</sup> = 2 _h_<sup>_′_</sup> = 4 _h_ y as´ı siguiendo. De esta manera, multigrilla se basa en resolver el problema en una serie de mallas con paso de malla _h,_ 2 _h,_ 4 _h, . . . ,_ 2<sup>_m_</sup> _h_ , haciendo una serie de iteraciones en la malla fina seguida de iteraciones sobre la malla m´as gruesa y as´ı siguiendo. 

**Descomposici´on de dominios.** Ver _§_ 9.4.1 

**Precondicionamiento Jacobi.** Consiste en simplemente tomar _M_ = diag _A_<sup>_−_1</sup> . Como la matriz a invertir es diagonal el costo de invertirla es muy bajo ( _O_ ( _N_ ) opeaciones). Este precondicionamiento no aporta nada en situaciones donde los elementos de la diagonal son aproximadamente constantes (precondicionar con un m´ultiplo escalar de la identidad no puede nunca mejorar el n´umero de condici´on). Esto ocurre por ejemplo para el Laplaciano (tanto en 1D como en m´as dimensiones) cuando el paso de la malla es constante. Cuando la malla no es homog´enea (ver figura- 9.14) entonces el n´umero 

**264** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.2. M´etodo de Gradientes Conjugados_ 



Figura 9.14: Malla refinada hacia una esquina. 

de condici´on es 



donde _h_ min es el m´ınimo _h_ sobre toda la malla y entonces puede ser bastante peor que _O_ ( _n_<sup>2</sup> ) donde _n_ es el n´umero de elementos en una direcci´on caracter´ıstica. Los elementos diagonales de _A_ son _∝ h_<sup>_−_</sup> _x_<sup>2+</sup> _h_<sup>_−_</sup> _y_<sup>2</sup> = _O_ (m´ın( _hx, hy_ )<sup>_−_2</sup> ) y puede verse que este precondicionamiento corrige el mal condicionamiento producido por el refinamiento de manera que 



**Factorizaci´on incompleta.** Consideremos la factorizaci´on Cholesky _A_ , _A_ = _BB_<sup>_T_</sup> . Entonces este precondicionamiento consiste en descartar elementos de _B_ de manera de reducir su ancho de banda. En la implementaci´on pr´actica el descarte se va haciendo a medida de que se va factorizando la matriz, bas´andose en el valor absoluto del elemento _Bij_ que se est´a evaluando y su distancia a la diagonal _|i − j|_ . Por supuesto se trata de descartar aquellos elementos que tienen un menor valor absoluto y que se encuentran m´as alejados de la diagonal. 

**Precondicionamiento polinomial.** Consiste en encontrar un polinomio _p_ ( _z_ ) tal que _M_ = _p_ ( _A_ ) _≈ A_<sup>_−_1</sup> . El criterio para construir el polinomio en cuesti´on es similar al utilizado para construir los polinomios residuales que permiten obtener la estimaci´on de convergencia (9.255) en base a los polinomios de Tchebyshev. El costo de un tal precondicionmiento es evaluar _Mx_ = _p_ ( _A_ ) _x_ que involucra _m_ productos matriz-vector, donde _m_ es el orden del polinomio de Tchebyshev. Como es usual en la evaluaci´on de polinomios, se utiliza la forma anidada, tambi´en llamada de H¨orner, como en el siguiente script 

```
y=0;
```

```
fork=0:m
```

```
y=p(k)*x+A*y;
```

```
end
```

donde (usando la notaci´on de Octave) _p_ ( _x_ ) = _p_ 1 _x_<sup>_m_</sup> + _p_ 2 _x_<sup>_m−_1</sup> + _. . ._ + _pm_ +1 y los coeficientes _pi_ est´an almacenados en un vector de longitud _m_ + 1. En la versi´on _matrix free_ , el producto _Ax_ est´a definido por medio de una rutina. Sea `w=prodvec(x)` la rutina que retorna _w_ = _Ax_ cuando se le pasa _x_ entonces el algoritmo se escribe como 

**265** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 

```
y=0;
```

```
fork=0:m
y=p(k)*x+prodvec(y);
```

```
end
```

##### **9.2.6. M´etodos CGNR y CGNE** 

Si _A_ es nosim´etrica o no definida positiva, entonces podemos considerar resolver 



en el cual aparece la matriz _A_<sup>_T_</sup> _A_ que es sim´etrica y definida positiva si _A_ es no singular. Notar que en cada iteraci´on de GC sobre este sistema estamos minimizando 





de ah´ı el nombre de _“Conjugate Gradient on the Normal Equations to minimize the Residual”_ (CGNR). Otra posibilidad es hacer el cambio de variable _x_ = _A_<sup>_T_</sup> _y_ y resolver 



para _y_ . Una vez encontrado _y_ , _x_ se obtiene con una operaci´on matriz vector adicional _x_ = _A_<sup>_T_</sup> _y_ . La norma que se minimiza es en este caso 



- de ah´ı el nombre de _“Conjugate Gradient on the Normal Equations to minimize the Error”_ (CGNE). Observaciones 

   - En general ocurre que _κ_ ( _A_<sup>_T_</sup> _A_ ) _∼ κ_ ( _A_ )<sup>2</sup> , lo cual augura muy bajas tasas de convergencia si el _κ_ ( _A_ ) es grande. 

Se necesitan 2 productos matriz vector por iteraci´on 

- En la versi´on _matrix free_ hay que programar no s´olo una rutina que calcule _Ax_ sino tambi´en una que calcule _A_<sup>_T_</sup> _x_ . Para problemas provenientes de discretizaciones por FEM o FDM de PDE’s, esto puede resultar bastante complicado. 

#### **9.3. El m´etodo GMRES** 

##### **9.3.1. La propiedad de minimizaci´on para GMRES y consecuencias** 

GMRES (por _“Generalized Minimum RESidual”_ fue popuesto en 1986 por Y. Saad y m. Schulz como un m´etodo iterativo por subespacios de Krylov para sustemas no-sim´etricos. En contraposici´on 

**266** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 

con CGNR o CGNE _no_ requiere el c´alculo de productos de _A_<sup>_T_</sup> con un vector, lo cual es una gran ventaja en muchos casos. pero es necesario guardar una base de _Kk_ lo cual requiere un costo de almacenamiento adicional a medidad que la iteraci´on progresa. 

La iteraci´on _k_ -´esima ( _k ≥_ 1) es 



N´otese que esta propiedad de minimizaci´on es muy similar con la de Gradientes Conjugados, con la diferencia que en GC se aplica al funcional (9.181). Como aqu´ı estamos contemplando la posibilidad que _A_ no sea sim´etrica o definida positiva, entonces no podemos tomar este funcional. Si consideramos que minimizar _∥b − A x∥_ 2 es equivalente a minimizar _∥b − A x∥_<sup>2</sup> 2<sup>el cual contiene en la forma cuadr´atica</sup> _A_<sup>_T_</sup> _A_ , entonces vemos que GMRES es equivalente a CGNR con la salvedad de que con GMRES no debemos calcular productos _A_<sup>_T_</sup> -vector pero en contraparte debemos mantener una base del espacio de Krylov. 

Como _x ∈ x_ 0 + _Kk_ puede ponerse de la forma 



entonces 







donde _p_ ¯ _∈Pk_ es un polinomio residual. 

**Teorema 3.1.1.** Sea _A_ no-singular y _xk_ la _k_ -´esima iteraci´on de GMRES. Entonces para todo _p_ ¯ _∈Pk_ 



**Corolario 3.1.1.** Sea _A_ no-singular, entonces 



**Teorema 3.1.2.** Sea _A_ no-singular. Entonces GMRES encuentra la soluci´on dentro de las _N_ iteraciones 

**Demostraci´on.** Usar _p_ ¯( _z_ ) = _p_ ( _z_ ) _/p_ (0), donde _p_ ( _z_ ) = det( _A − zI_ ) es el polinomio caracter´ıstico. � 

Para GC hemos usado el teorema espectral para encontrar estimaciones de la tasa de convergencia. Esto no puede asumirse en general si _A_ no es sim´etrica. Sin embargo podemos restringir el an´alisis al caso de que _A_ sea diagonalizable aunque los autovalores y autovectores pueden ser ahora comlejos. 

**Nota sobre la condici´on de diagonalizabilidad de matrices.** Recordemos que 

**267** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 

- _A_ es diagonalizable si _A_ = _V_ Λ _V_<sup>_−_1</sup> con Λ diagonal. Cuando _A_ es real y sim´etrica Λ es real y podemos elegir a _V_ como real. Cuando _A_ es no-sim´etrica tando Λ como _V_ pueden ser complejos. 

- En ´algebra compleja muchos conceptos pueden extenderse f´acilmente si reemplazamos la “tranpuesta” de _A_ por la “transpuesta conjugada” de _A_ que denotaremos como _A_<sup>_H_</sup> . 

- El producto escalar de dos vectores pertenecientes a _C_<sup>_N_</sup> se define como _x_<sup>_H_</sup> _y_ =<sup>�</sup><sup>_n_</sup> _k_ =1 ( _x_ ) _k_ ( _y_ ) _k_ . 

- _V_ es _unitaria_ si _V_<sup>_H_</sup> _V_ = _I_ (es la extensi´on del concepto de matriz ortogonal a complejos). 

- _A_ es _normal_ si es diagonalizable y si la matriz de cambio de base correspondiente _V_ es unitaria. Puede verse que si _A_ conmuta con su transpuesta conjugada (es decir _A_<sup>_H_</sup> _A_ = _A A_<sup>_H_</sup> ) entonces _A_ es normal. 

Es obvio que si _A_ es herm´ıtica (sim´etrica en el caso real) entonces _A_ es normal 

**Teorema 3.1.3.** para todo _p_ ¯ _− k ∈Pk_ 



**Demostraci´on.** Basta con ver que 



No est´a claro como puede estimarse el _κ_ 2( _V_ ), si existe. Si _A_ es normal, entonces _V_ es unitaria, preserva la norma y entonces _∥V ∥_ 2 = �� _V −_ 1��2<sup>=</sup><sup>_κ_2(</sup><sup>_V_) = 1</sup> 









y similarmente para _V_<sup>_−_1</sup> . Por otra parte, si _A_ se aproxima a una matriz no diagonalizable, entonces _κA_ () _→∞_ . Esto puede verse con un ejemplo simple. La matriz 



es un _bloque de Jordan_ y es claramente no diagonalizable. Perturbando ligeramente uno de los elementos diagonales de la forma 



[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 

con _ϵ_ muy peque˜no la matriz pasa a ser diagonalizable, ya que tiene dos autovalores distintos ( _λ_ = 1 _, ϵ_ ). Sin embargo podemos ver que la matriz de cambio de base _V_ correspondiente tiene un n´umero de condici´on que crece como 2 _/ϵ_ : 

```
octave>a=[01;01e-5]
```

```
a=
0.000001.00000
0.000000.00001
octave>[v,d]=eig(a)
v=
1.000001.00000
0.000000.00001
d=
0.0000e+000.0000e+00
0.0000e+001.0000e-05
octave>cond(v)
ans=2.0000e+05
octave>
```

Ahora consideremos que ocurre si utilizamos una rutina num´erica de diagonalizaci´on (como el `eig( )` de Octave) sobre una matriz que no es diagonalizable. Lo deseable ser´ıa que la rutina num´erica nos mostrara un mensaje de eror diciendo que la matriz no es diagonalizable. Sin embargo, debido a los errores de redondeo, la matriz aparece ser como diagonalizable desde el punto de vista num´erico y entonces la forma efectiva de verificar _“cu´an diagonalizable es una matriz”_ es chequear _κ_ 2( _V_ ). Cuanto m´as grande es este n´umero _“menos diagonalizable”_ es la matriz. 

```
octave>a=[01;00]
a=
```

```
01
00
```

```
octave>[v,d]=eig(a)
v=
```

```
1.00000-1.00000
0.000000.00000
```

```
d=
00
00
```

```
octave>cond(v)
ans=1.9958e+292
```

**269** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 

Esto es similar a cuando nos preguntamos si una matriz es inversible o no. Si calculamos el determinante de la matriz, por errores de redondeo este n´umero siempre resulta ser diferente de cero. Adem´as, la misma matriz multiplicada por una factor _a <_ 1 tiene un determinante que es un factor _a_<sup>_N_</sup> veces menor. Para matrices grandes (digamos _N_ = 100) un peque˜no factor 0 _,_ 1 puede representar un cambio en la magnitud del determinante por un factor 10<sup>_−_100</sup> . Todo esto indica que el determinante no es un buen indicador de _“cuan singular es una matriz”_ y un an´alisis m´as detallado muestra que el indicador correcto es el n´umero de condici´on de la matriz: cuanto m´as alto es el n´umero de condici´on _“m´as singular es la matriz”_ . 

Los siguientes Teoremas reproducen los resultados ya obtenidos para GC. Su demostraci´on se basa nuevamente en la construcci´on de polinomios residuales apropiados que se anulan en los autovalores de la matriz. 

**Teorema 3.1.4.** Sia _A_ tienen autovalores distintos entonces GMRES converge en _k_ iteraciones. **Teorema 3.1.5.** Si _r_ 0 es una combinaci´on lineal de _k_ autovectores de _A_ entonces GMRES converge dentro de las _k_ iteraciones. 

##### **9.3.2. Criterio de detenci´on:** 

Pensando a GMRES como un m´etodo iterativo las estimaciones de la tasa de convergencia son similares a las de GC. Como en GC el criterio de detenci´on es 



Una estimaci´on bastante cruda de la tasa de convergencia se puede obtener asumiendo que existe un _ω_ tal que _∥I − ωA∥_ 2 = _ρ <_ 1. Tomando el polinomio de _p_ ¯ _k_ ( _x_ ) = (1 _− ωz_ )<sup>_k_</sup> podemos obtener la estimaci´on de convergencia 



Esta estimaci´on de convergencia tiene algunos puntos en com´un con las estimaciones de convergencia que hemos obtenido para el m´etodo de Richardson. Notemos que bajoe estas mismas condiciones el m´etodo de Richardson predice la misma tasa de convergencia. Sin embargo la diferencia fundamental est´a en que con GMRES no es necesario conocer el valor de _ω_ , de hecho, como (9.329) es v´alido para cualquier _ω_ es v´alido para aquel que minimize _∥I − ωA∥_ 2, es decir que su convergencia es mejor que la de Richardson sobre-relajado con el mejor valor del par´ametro de relajaci´on que pudi´eramos obtener, sin necesidad de conocer ning´una norma ni estimaci´on de los autovalores de _A_ . Por otra parte, GMRES tiene en su contra que debe guardar la base del espacio de Krylov. Pero si hacemos la estrategia del “restart” que veremos m´as adelante, seg´un la cual se realizan un cierto n´umero _m_ (bajo) de iteraciones de GMRES y obtenido el _xm_ se vuelve a iterar GMRES de cero desde _xm_ , entonces este GMRES con restart tendr´ıa una tasa de convergencia mejor que la mejor que podr´ıamos obtener con el mejor par´ametro de relajaci´on _ω_ , a un costo similar por iteraci´on y con un requerimiento de capacidad de almacenamiento no demasiado alto. 

Como esta estimaci´on no depende de una diagonalizaci´on de _A_ podr´ıamos esperar que nos de alguna estimaci´on de la convergencia en el caso en que _A_ no es diagonalizable. Deafortunadamente, 

**270** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 

puede verificarse que para un bloque de Jordan de la forma 



vale que _∥I − ωA∥_ 2 _>_ 1 para todo _ω_ , es decir que no hay _ω_ que haga convergente a Richardson y, a la vez, nos permita obtener una estimaci´on de la tasa de convergencia para GMRES. Too esto har´ıa pensar que si la matriz no es diagonalizable (o _“casi no diagonalizable’_ ) entonces GMRES no converger´a. Pero si la forma de Jordan de una Matriz incluye un peque˜no bloque de Jordan de dimension _kJ_ y el resto es diagonalizable, entonces basta con tomar polinomios residuales de la forma 



para _k > kJ_ , donde _λJ_ es el autovalor correspondiente al bloque de Jordan y _q_ es un polinomio apropiado para estimar una buena convergencia sobre el espectro de autovalores restantes. Por ejemplo, si el resto de los autovalores es real y positivo, entonces podr´ıamos usar los polinomios de Tchebyshev usados para estimar la tasa de convergencia de GC. 

##### **9.3.3. Precondicionamiento** 

La forma de implementar el precondicionamiento en GMRES difiere con GC en cuanto a que para GMRES no es necesario que el sistema precondicionado 



sea ni sim´etrico ni definido positivo. Entonces basta con encontrar un precondicionamiento _M_ tal que _∥I − MA∥_ 2 _<_ 1 y se resuelve directamente el sistema precondicionado. Debido a esto, la rutina de GMRES no incluye nada en especial en cuanto al precondicionamiento, sino que directamente se pasa _Mb_ como miembro derecho, y la rutina que calcula el producto matriz vector retorna ( _MA_ ) _x_ en vez de _A x_ . 

Por otra parte se pueden usar _precondicionadores por derecha_ y _por izquierda_ . El precondicionamiento por izquierda es como fue expuesto en el p´arrafo anterior mientras que el precondicionamiento po derecha consiste en encontrar un _M_ tal que _∥I − AM ∥_ 2 _<_ 1 y entonces hacer el cambio de variable _x_ = _My_ , resolver con GMRES el sistema 



y finalmente, una vez encontrado _y_ obtener _x_ de _x_ = _My_ . 

En cuanto a las ideas para desarrollar precondicionadores son similares a las utilizadas con GC. 

**271** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 

##### **9.3.4. Implementaci´on b´asica de GMRES** 

Recordemos que _xk_ se obtiene del problema de minimizaci´on (9.313). Sea _Vk_ una matriz que contiene los vectores que expanden _Kk_ es decir 



Entonces _x − x_ 0 es una combinaci´on lineal de las columnas de _Vk_ , es decir 



Entonces _y_ debe ser tal que minimize 



Sea ahora 



entonces el cuadrado de la norma se escribe como 



que alcanza su m´ınimo cuando 



lo cual ocurre cuando 



Esto puede implementarse en Octave con el comando 

###### `y=(B’*B)\B*r0` 

pero a´un m´as simplemente 

###### `y=B\r0` 

hace lo mismo ya que para matrices rectangulares el operador `\` se interpreta como resolver el sistema de m´ınimos cuadrados asociado. 

En cuanto a la implementaci´on pr´actica, notemos que el vector 



**272** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 

de donde vemos que en cada iteraci´on s´olo necesitamos calcular el ´ultimo elemento del vector, lo cual involucra _O_ ( _N_ ) operaciones. Algo similar ocurre con el c´alculo de la matriz _Hk_ = _Bk_<sup>_TBk_ainvertir.</sup> 







con lo cual s´olo es necesario calcular la ´ultima columna y el elemento diagonal. La ´ultima fila es igual a la transpuesta de la ´ultima columna ya que _Hk_ es sim´etrica y definida positiva por construcci´on. El c´alculo de esta ´ultima columna requiere de _O_ ( _kN_ ) operaciones. Finalmente la inversi´on del sistema cuya matriz es _Hk_ requiere _O_ ( _k_<sup>3</sup> ) operaciones. Mientras mantengamos _k ≪ N_ (m´as estrictamente es _k_<sup>2</sup> _≪ N_ ) este costo es despreciable contra las _k_<sup>_N_</sup> operaciones. 

##### **9.3.5. Implementaci´on en una base ortogonal** 

En la pr´actica es muy com´un ir cosntruyendo una base ortogonal de _Kk_ mediante el _proceso de ortogonalizaci´on de Gram-Schmidt_ . El algoritmo es el siguiente 

1. _r_ 0 = _b − Ax_ 0, _v_ 1 = _r_ 0 _/ ∥r_ 0 _∥_ 2 





Si en alg´un _i_ sucede que _w_ = 0 entonces decimos que el algoritmo _falla_ o _colapsa_ ( _“breakdown”_ ). Asumiendo que los _r_ 0 _, Ar_ 0 _, . . . , A_<sup>_k−_1</sup> _r_ 0 son linealmente independientes (o sea que: dim _Kk_ = _k_ ), entonces podemos que 

El algoritmo no falla. 



Esto se puede demostrar por inducci´on en _i_ . Para _i_ = 1 es obvio, ya que _v_ 1 es igual a _r_ 0 normalizado. Para demostrarlo para _i_ + 1, observemos que _w_ es otogonal a todos los _vj_ para _j ≤ i_ 







Ahora bien _Avi_ pertenece a _Ki_ +1 y los _vl_ para _l_ = 1 _, . . . , i_ pertenecen a _Ki_ . Si _w̸_ = 0 entonces podemos normalizar _w_ apra obtener _vi_ +1 y _{vl}_<sup>_i_</sup> _l_ =1<sup>+1es un conjunto de vectores ortonormales en</sup><sup>_Ki_+1. Como</sup><sup>_Ki_=1</sup> 

**273** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 

es de dimensi´on a lo sumo _i_ + 1, _vi_ +1 y _{vl}_<sup>_i_</sup> _l_ =1<sup>+1esunabaseortogonal.S´olofaltademostrarentonces</sup> que bajo las hip´otesis asumida el algoritmo no falla. 

Ahora bien, por inducci´on podemos asumir que 



Pero si el algoritmo falla, entonces quiere decir que _Avi_ es una combinaci´on lineal de los _{vl}l_ = 1<sup>_i_</sup> y eso implicar´ıa que _A_<sup>_i_</sup> _r_ 0 es una combinaci´on lineal de los mismos e indicar´ıa que los _{A_<sup>_j−_1</sup> _r_ 0 _}_<sup>_i_</sup> _j_ =1<sup>son</sup> linealmente dependientes. 

###### **Colapso de GMRES (Breakdown)** 

Puede ocurrir que _w_ = 0 para alg´un _i_ , en cuyo caso (por lo visto en el p´arrafo anterior) indicar´ıa que _{A_<sup>_j−_1</sup> _r_ 0 _}_<sup>_i_</sup> _j_ =1<sup>sonlinealmentedependientes.Podemosverqueestoocurresi</sup><sup>_x∗−x_0</sup><sup>_∈Kk_.</sup> **Lemma 3.4.1.** Si _wi_ +1 = 0 entonces _x_<sup>_∗_</sup> = _A_<sup>_−_1</sup> _b ∈Ki_ 

**Demostraci´on.** Si _w_ = 0 para alg´un _i_ entonces eso implica 



Por construcci´on _Avj ∈Ki_ para _j < i_ , con lo que resulta que _AKi ⊂Ki_ . Pero como 



es una base de _Ki_ entonces 



para una cierta matriz _H_ de _i × i_ . La columna _j_ -´esima de _H_ son los coeficientes de la expansi´on de _Avj_ en t´ermino de los _{vl}_<sup>_j_</sup> _l_ =1<sup>+1.</sup><sup>_H_esnosingularyaque</sup><sup>_A_noloes.Efeectivamentesi</sup><sup>_z̸_== 0,</sup><sup>_z∈_IR</sup><sup>_i_</sup> es tal que _Hz_ = 0, entonces _Viz_ es un vector no nulo y 



Consideremos ahora el residuo en la _i_ -´esima iteraci´on 



con _y ∈_ IR<sup>_i_</sup> ya que _xi − x_ 0 _∈Ki_ . Adem´as _r_ 0 por construcci´on es proporcional a _v_ 1 la primera columna de _Vi_ lo cual puede escribirse como 



con _e_<sup>_T_</sup> 1<sup>= [10</sup><sup>_. . ._0].Como</sup><sup>_Vi_esortogonal,preservalanorma</sup> 





Pero basta con tomar _y_ = _βH_<sup>_−_1</sup> _e_ 1 para el cual _∥ri∥_ 2 = 0 y GMRES ha convergido. 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

**274** 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 

##### **9.3.6. El algoritmo de Gram-Schmidt modificado** 

Uno de los principales problemas de GMRES es que por errores de redondeo se va perdiendo la ortogonalidad de los vectores _vi_ , por lo cual debe prestarse especial atenci´on al proceso de ortogonalizaci´on. Una primera observaci´on es que la siguiente versi´on modificada del proceso de ortogonalizaci´on de Gram-Schmidt resulta ser mucho m´as estable ante errores de redondeo 

_vk_ +1 = _Avk_ for _j_ = 1 _, . . . , k vk_ +1 = _vk_ +1 _−_ ( _vk_<sup>_T_</sup> +1<sup>_vj_)</sup><sup>_vj_</sup> 

##### **9.3.7. Implementaci´on eficiente** 

La matriz _H_ que contiene los coeficientes que expanden _Avi_ en t´ermino de los _vl_ tiene una estructura particular que permite una implementaci´on m´as eficiente del algoritmo. Consideremos la expresi´on 



Esto quiere decir que _Avi_ es una combinaci´on lineal de los _{vj}_<sup>_i_</sup> _j_<sup>+1</sup> =1<sup>.Comolacolumna</sup><sup>_j_-´esimade</sup><sup>_Hk_</sup> son los coeficientes de la expansi´on de _Avj_ en t´ermino de los _{vl}_<sup>_j_</sup> _l_ =1<sup>+1</sup> 



vemos los _hlj_ deben ser de la forma _hlj_ = 0 para _l > j_ + 1. Es decir 



Este tipo de matriz se llama _Hessenberg superior_ ( _upper Hessenberg_ ). 

El residuo se puede escribir como 





y como _Vk_ es ortogonal 



Para resolver este problema se recurre a una estrategia similar a la anterior. Es decir, en Octave `y=beta*H\e1` si usamos la soluci´on por m´ınimos cuadrados interna de Octave, o `y=beta*(H’*H)\H*e1` si lo resolvemos expl´ıcitamente. Finalmente, existen algoritmos especiales que permiten factorizar la matriz con un algoritmo _QR_ en forma m´as eficiente usando la estructura Hessenberg superior de _Hk_ . Independientemente de la implementaci´on de la resoluci´on del problema de cuadrados m´ınimos, el algoritmo de GMRES es 

**275** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 

Algoritmo `gmresb(` _x, b, A, ϵ, k_ max _, ρ_ `)` 

1. _r_ = _b − Ax_ , _v_ 1 = _r/ ∥r∥_ 2, _ρ_ = _∥r∥_ 2, _β_ = _ρ_ , _k_ = 0 2. While _ρ > ϵ ∥b∥_ 2 y _k < k_ max (a) _k_ = _k_ + 1 (b) _vk_ +1 = _Avk_ . Para _j_ = 1 _, . . . , k_ (i) _hjk_ = _vk_<sup>_T_</sup> +1<sup>_v −j_</sup> (ii) _vk_ +1 = _vk_ +1 _− hjk vj_ (c) _hk_ +1 _,k_ = _∥vk_ +1 _∥_ 2 (d) _vk_ +1 = _vk_ +1 _/ ∥vk_ +1 _∥_ 2 (e) _e_ 1 = [1 0 0 _. . ._ 0]<sup>_T_</sup> _yk_ = argmin _y∈_ IR _k_ �� _βe_ 1 _− Hkyk_ ��2 (f) _ρ_ = �� _βe_ 1 _− Hk yk_ ��2 3. _xk_ = _x_ 0 + _Vk y_<sup>_k_</sup> 

##### **9.3.8. Estrategias de reortogonalizaci´on** 

Se puede perder ortogonalidad por errores de redondeo. Una soluci´on es hacer un segundo paso de ortogonalizaci´on sea entodas las iyeraciones, sea cuando alg´un indicador de p´erdida de ortogonalidad se activa. 

##### **9.3.9. Restart** 

Como debemos almacenar una base para _Kk_ esto requiere _kN_ reales lo cual va creciendo con _k_ y eventualmente excede la memoria de la m´aquina. Entonces la idea es iterar GMRES _m_ iteraciones y empezar de nuevo a partir de la ´ultima iteraci´on, es decir aplicar GMRES inicializando con _x_ 0 _← xm_ . El siguiente algoritmo `gmresm` refleja esto, 

Algoritmo `gmresm` ( _x, b, A, ϵ, k_ max _, m, ρ_ ) 

1. `gmres` ( _x, b, A, ϵ, m, ρ_ ) 

2. _k_ = _m_ 3. While _ρ > ϵ ∥b∥_ 2 y _k < k_ max (a) `gmres` ( _x, b, A, ϵ, m, ρ_ ) (b) _k_ = _k_ + _m_ 

##### **9.3.10. Otros m´etodos para matrices no-sim´etricas** 

GMRES, CGNE y CGNR comparten las siguientes (buenas) caracter´ısticas 

Son f´aciles de implementar 

Se analizan con residuos polinomiales 

Por otra parte los CGN* tienen la desventaja de que necesitan un producto _A_<sup>_T_</sup> _x_ y su tasa de convergencia est´a regida por _κ_ ( _A_<sup>_T_</sup> _A_ ) _∼ κ_ ( _A_ )<sup>2</sup> , mientras que GMRES s´olo necesita calcular _A x_ y la convergencia est´a basada en _κ_ ( _A_ ), pero es necesario guardar una base de _Kk_ , lo cual representa una 

**276** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 

capacidad de almacenamiento que va creciendo con las iteraciones. Como esto es virtualmente imposible para grandes sistemas desde el punto de vista pr´actico se utiliza el GMRESm, lo cual puede involucrar un serio deterioro de la convergencia. 

El m´etodo ideal deber´ıa ser como CG: 

- S´olo necesitar calcular _A x_ (no _A_<sup>_T_</sup> _x_ ) 

- Estar basado en una propiedad de minimizaci´on o conjugaci´on 

Requerir baja capacidad de almacenamiento. (Sobre todo que no crezca con las iteraciones). 

Converger en _N_ iteraciones. 

En esta secci´on describiremos algunos m´etodos que tratan de aproximarse a estos requerimientos con menor o mayor ´exito. 

**Bi-CG:** (por _Biconjugate Gradient Squared_ ) No se basa en una propiedad de minimizaci´on sino de ortogonalidad 



donde _Kk_ 



es el _espacio de Krylov conjugado_ . _r_ ˆ0 es un vector que debe ser provisto por el usuario, pero lo m´as usual es tomar _r_ ˆ0 = _r_ 0. El algoritmo genera secuencias de residuos y direcciones de b´usqueda _{rk, pk}_ y sus correspondientes conjugados _{r_ ˆ _k,_ ˆ _pk}_ tales que hay biortogonalidad entre los residuos 



y de bi-conjugaci´on entre las direcciones de b´usqueda 



Si _A_ es sim´etrica y definida positiva y _r_ ˆ0 = _r_ 0, entonces Bi-CG es equivalente a GC (pero computa todo el doble, es decir que tiene el doble de costo por iteraci´on). Bi-CG necesita un c´alculo _A_<sup>_T_</sup> _x_ , pero la ventaja con respecto a los CGN* es que su tasa de convergencia est´a basada en _κ_ ( _A_ ) no en _κ_ ( _A_<sup>_T_</sup> _A_ ). Es muy ´util si _A_ es aproximadamente spd, es decir si los autovalores de _A_ est´an cerca de la recta real. 

Podemos comparar Bi-CG con GMRES en cuanto a la tasa de convergencia si consideramos que resulta ser que 



con _p_ ¯ _k_ un polinomio residual, y entonces por la propiedad de minimizaci´on de GMRES 



pero debe recordarse que Bi-CG comparado con GMRES no necesita un espacio de almacenamiento creciente. Adem´as una iteraci´on de Bi-CG requiere dos productos matriz vector, pero el costo de GMRES tambi´en crece con las iteraciones. 

**277** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 

**CGS** (por _Conjugate Gradient Squared_ ). Este m´etodo trata de ser una extensi´on de Bi-CG pero tal que no necesita calcular _A_<sup>_T_</sup> _x_ . Puede verse que en la iteraci´on _k_ 



entonces el factor _rk_<sup>_Tr_ˆ</sup><sup>_k_(quejuegaelpapelde</sup><sup>_ρk_enGC,(verelalgoritmo</sup><sup>`cg(...)`enp´ag.257),</sup> puede reescribirse de la forma 





en el cual no es necesario calcular _A_<sup>_T_</sup> _x_ . Con manipulaciones similares se puede llegar a transformar todos las expresiones donde aparece _A_<sup>_T_</sup> , pero el algoritmo resulta modificado, es decir las iteraciones de Bi-CG _no son las mismas_ que para CGS. 

**Bi-CGstab** (por Biconjugate Gradient Squared stabilized). Trata de mejorar CGS reemplazando 



donde 



donde _ωi_ se selecciona para minimizar 



como funci´on de _ωi_ , esto es usualmente conocido como _line-searching_ . Sea 









de manera que 



y el valor que minimiza es 



Bi-CGstab entonces no necesita del c´alculo de _A_<sup>_T_</sup> _x_ como CGS pero tiende a tener una tasa de convergencia mejor. El costo computacional involucrado por iteraci´on es 

Almacenamiento para 7 vectores 

- 4 productos escalares 

- 2 productos matriz-vector ( _Ax_ ) 

**278** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 



Figura 9.15: Descomposici´on de dominios 

##### **9.3.11. Gu´ıa Nro 3. GMRES** 

Consideremos la ec. de _advecci´on-difusi´on_ 





donde 

_φ_ = temperatura del fluido 

_k_ = conductividad t´ermica del fluido 

_a_ = velocidad del fluido (puede ser positiva o negativa) 

La soluci´on exacta es 



donde 



Aqu´ı _L_ = 1. En la figura 9.16 vemos Para _a →_ 0 el problema se acerca a la ec. de Laplace y la soluci´on tiende a ser una recta que une los valores de contorno, mientras que para Pe grandes y positivos el fluido va en la direcci´on + _x_ y arrastra el valor de la condici´on _aguas arriba_ una cierta longitud hasta que a una distancia peque˜na _δ_ sube r´apidamente para tomar el valor dado por la condici´on en _x_ = 1. 

La discretizaci´on num´erica pasa por reemplazar las derivadas por diferencias num´ericas 



[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] **279** 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.3. El m´etodo GMRES_ 



<!-- Start of picture text -->
x<br><!-- End of picture text -->

Figura 9.16: Soluci´on para el problema de advecci´on difusi´on, en los l´ımites dominado por difusi´on y por advecci´on 

###### y 



Lamentablemente, esta discretizaci´on falla cuando el Pe _≫_ 1, en el sentido de que produce fuertes oscilaciones num´ericas. La soluci´on usual es agregar una cierta cantidad de _difusi´on num´erica_ , es decir que se modifica la ecuaci´on original a 



donde 



Realizar las siguientes tareas: 

1. Calcular la matriz para Pe _h_ = 0 _,_ 01, 1 y 100 

2. Calcular los autovalores. Ver la distribuci´on en el plano complejo. 

3. Verificar que la matriz no es sim´etrica. Ver que la parte correspondiente a _φ_<sup>_′′_</sup> es sim´etrica mientras que la que corresponde a _φ_<sup>_′_</sup> es antisim´etrica. 

4. Ver a que tiende la matriz para _k →_ 0. Es diagonalizable? 

5. Resolver por GMRES y CGNE. 

6. Pensar como se podr´ıa hacer para calcular _A_<sup>_T_</sup> _x_ sin construir _A_ . 

**280** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.4. Descomposici´on de dominios._ 

#### **9.4. Descomposici´on de dominios.** 

Consideremos la soluci´on de una ecuaci´on en derivadas parciales en un dominio como muestra la figura 9.15. Descomponemos el problema en dos dominios de manera que podemos separar las inc´ognitas en _x_ en tres grupos, aquellos que est´an estrictamente contenidos en el dominio de la izquierda _x_ 1, los estricatamente contenidos en el dominio de la derecha _x_ 3 y los que est´an sobre la interfase _x_ 2. La ecuaci´on se descompone en bloques de la siguiente forma 



La descomposici´on en bloques refleja el hecho de que como los grados de libertad contenidos en _x_ 1 y _x_ 3 no est´an compartidos por ning´un elemento, los bloques correspondientes _A_ 13 y _A_ 31 son nulos. Podemos eliminar _x_ 1 y _x_ 3 de la primera y ´ultima l´ınea de ecuaciones y obtener una ecuaci´on para los grados de libertad de interfase _x_ 2 



Ahora consideremos resolver este sistema por GC. En cada iteraci´on debemos calcular el producto de la matriz entre par´entesis por un vector _x_ 2. Para los t´erminos primero y tercero de la matriz es necesario factorizar y resolver un sistema lineal con las matrices _A_ 33 y _A_ 11. Esto corresponde a resolver problemas independientes sobre cada uno de los dominios con condiciones Dirichlet sobre la interfase, por lo tanto estos problemas pueden ser resueltos en procesadores independientes lo cual implica un alto grado de paralelizaci´on del problema. Esto se puede extender a m´as procesadores, y en el l´ımite podemos lograr que en cada procesador se resuelva un sistema lineal lo suficientemente peque˜no como para ser resuelto en forma directa. La eficiencia del m´etodo puede ser mejorada a´un m´as encontrando un buen precondicionamiento. 

Si separamos la matriz _S_ que aparece en el sistema (9.397) en la contribuci´on por el dominio de la izquierda _SL_ y de la derecha _SR_ 







Entonces podemos poner como precondicionamiento 



Es _M_ un buen precondicionamiento? O mejor dicho: Porqu´e habr´ıa _M_ de parecerse a _S_<sup>_−_1</sup> ? Bien, si el operador es sim´etrico (el laplaciano lo es) y los dominios son iguales y la malla es sim´etrica, entonces puede verse que _SL_ = _SR_ y entonces _M_ y _S_<sup>_−_1</sup> coinciden 





[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.4. Descomposici´on de dominios._ 



Figura 9.17: Descomposici´on de dominios. Problema del continuo. 

Por otra parte resolver _x_ = _My_ es equivalente a resolver 



y despu´es 



y el punto es que ambos sistemas (9.403) y (9.404) equivale a resolver problemas _independientes_ con condiciones tipo Neumann sobre la interfase. De nuevo, el hecho de que ambos problemas sobre cada dominio sean independientes favorece la paralelizaci´on del algoritmo. 

##### **9.4.1. Condicionamiento del problema de interfase. An´alisis de Fourier.** 

Obviamente la aplicabilidad de la descomposici´on de dominios descripta depende del n´umero de iteraciones necesarias para resolver el problema de interfase y por lo tanto del n´umero de condici´on de la matriz complemento de Schur _S_ o de su precondicionada _MS_ . Para hacer una estimaci´on de estos n´umeros de condici´on nos basaremos en un an´alisis de Fourier del problema del continuo para la ecuaci´on de Laplace. Las ecuaciones de gobierno son 







**282** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.4. Descomposici´on de dominios._ 

Consideremos la soluci´on en dos dominios Ω1, Ω2. La restricci´on de _φ_ a cada uno de los dominios debe satisfacer 

y 

|∆_φ_1 =_−f_ en Ω1|(9.409)|
|---|---|
|_φ_1 = <sup>¯</sup>_φ_1 en Γ1|(9.410)<br>(9.411)|
|∆_φ_2 =_−f_ en Ω2|(9.412)|
|_φ_2 = <sup>¯</sup>_φ_2 en Γ2|(9.413)|
||(9.414)|



y la continuidad de _φ_ y su derivada normal a trav´es de Γ _I_ 



Ahora consideremos una descomposici´on _φ_ = _ψ_ + _φ_<sup>˜</sup> , de manera que _ψ_ = 0 en Γ _I_ , es decir 

|∆_ψ_1 =_−f_ en Ω1|(9.417)|
|---|---|
|_ψ_1 = <sup>¯</sup>_ψ_1 en Γ1|(9.418)|
|_ψ_1 = 0 en Γ_I_|(9.419)|



y 

|∆_ψ_2 =_−f_ en Ω2|(9.420)|
|---|---|
|_ψ_2 = <sup>¯</sup>_φ_2 en Γ2|(9.421)|
|_ψ_2 = 0 en Γ_I_|(9.422)|



y por lo tanto falta hallar _φ_<sup>˜</sup> definido por 

|∆<sup>˜</sup>_φ_1 = 0 en Ω1||
|---|---|
|˜_φ_1 = 0 en Γ1||
|˜_φ_1 =_u_ en Γ_I_|(9.423)|



y 

|∆<sup>˜</sup>_φ_2 = 0 en Ω2||
|---|---|
|˜_φ_2 = 0 en Γ2||
|˜_φ_2 =_u_ en Γ_I_|(9.424)|



**283** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.4. Descomposici´on de dominios._ 

donde _u_ es una inc´ognita del problema y debe ser tal que 



donde 



Definimos ahora el operador de _Stekhlov-Poincar´e S_ 1 del dominio Ω1 como 



donde<sup>_∂φ_</sup><sup><u>1</u></sup> _∂n_<sup>denotaladerivadanormaltomandolanormalexterioraldominioencuesti´on,queparael</sup> dominio Ω1 coincide con la direcci´on de + _x_ , y _φ_ 1 es la soluci´on de (9.423), para el correspondiente _u_ . An´alogamente se puede definir _S_ 2 por 



donde _φ_ 2 est´a definido en funci´on de _u_ por (9.424) y el signo _−_ viene de que la normal exterior a Ω2 sobre Γ _I_ va ahora seg´un la direcci´on _−x_ . Entonces 



donde _S_ = _S_ 1 + _S_ 2. 

Ec. (9.429) es la versi´on del continuo de (9.397). Calcularemos el n´umero de condici´on de _S_ a partir del c´alculo de autovalores de _S_ . 

Cada uno de los operadores de Stekhlov-Poincar´e act´ua sobre el espacio de funciones definidas sobre Γ _I_ . Podemos mostrar que las funciones de la forma 



son autofunciones de estos operadores. La soluci´on _φ_<sup>˜</sup> 1 que es soluci´on de (9.423) correspondiente a _u_ = _um_ es de la forma 



Reemplazando en las ecuaciones que definen (9.423), la primera de las ecuaciones resulta ser 



de donde 



y de las condiciones de contorno en _x_ = 0, _L_ 1 resulta ser 





[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.4. Descomposici´on de dominios._ 

la derivada normal en Γ _I_ es entonces 



de manera que 



Vemos entonces, que _um_ es una autofunci´on de _S_ 1 con autovalor 



An´alogamente, el operador _S_ 2 tiene autovalores 



El operador _S_ tiene autovalores 



Ahora bien, dijimos que estimar´ıamos el n´umero de condici´on de la matriz _S_ a partir de los autovalores de _S_ . En el continuo _S_ tiene infinitos autovalores y los _λm_ van a infinito para _m →∞_ , de manera que el n´umero de condici´on de _S_ va a infinito. Obtendremos una estimaci´on para el n´umero de condici´on de _S_ asumiendo que los autovalores de _S_ se aproximan a los primeros _NI_ autovalores de _S_ , donde _NI_ es la dimensi´on de _S_ . El autovalor m´as bajo es 



si _L_ 1 = _L_ 2 = _L/_ 2, entonces 



El autovalor m´aximo se obtiene para _m_ = _NI_ y asumiendo que _NI ≫_ 1 y _L_ 1 _/L, L_ 2 _/L_ no son demasiado peque˜nos, entonces _kmL_ 1 = _NI πL_ 1 _/L ≫_ 1 y tanh _kmL_ 1 _≈_ 1 y similarmente tanh _kmL_ 2 _≈_ 1 y por lo tanto 



y el n´umero de condici´on es 



Notar que _κ_ ( _S_ ) va como 1 _/h_ al refinar, mientras que recordemos que el n´umero de condici´on de _A_ (la matriz del sistema) va como 1 _/h_<sup>2</sup> (Gu´ıa de ejercicios Nro. 1). 

Otro punto interesante a notar es que, para _m →∞_ los autovalores tienden a hacerse independientes de las longitudes de los dominios en la direcci´on normal a la interfase. Por ejemplo, para los autovalores _λ_<sup>1</sup> _m_<sup>de</sup><sup>_S_1,</sup><sup>_L_1apareceenelargumentodelatangentehiperb´olicayestatiendea1para</sup> 

**285** 

[Document version: curso-0.3.0. File version: $Id: itera1.tex,v 1.7 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 9. M´etodos iterativos para la resoluci´on de ecuaciones lineales _Secci´on 9.4. Descomposici´on de dominios._ 

_m →∞_ , independientemente del valor de _L_ 1. Incluso puede verse que para _m →∞_ los autovalores se hacen independientes del tipo de condici´on de contorno sobre el borde opuesto (es decir sobre _x_ = 0). Esta observaci´on se basa en el hecho de que el operador de Laplace es muy _local_ . Si _u_ es de la forma sin _mπy/L_ sobre Γ _I_ , entonces la longitud de onda es _β_ = 2 _L/m_ la cual se va achicando a medida que _m →∞_ . Las perturbaciones inducidas decaen como _e_<sup>_−n/β_</sup> donde _n_ es una coordenada en la direcci´on normal a Γ _I_ y si _β_ es muy peque˜no la perturbaci´on no llega al contorno opuesto. 

Ahora consideremos los autovalores del problema precondicionado. Como todos las _um_ de la forma (9.430) son autofunciones de los operadores _S_ 1, _S_ 2 y _S_ , entonces los autovalores de _MS_ son aproximadamente los primeros _NI_ autovalores de (1 _/_ 4)( _S_ 1<sup>_−_1</sup> + _S_ 2<sup>_−_1)(</sup><sup>_S_1 +</sup><sup>_S_2),esdecir</sup> 



Como mencionamos previamente (ver p´ag. 281), si el problema es sim´etrico (en el caso del continuo basta con _L_ 1 = _L_ 2, en el caso del discreto adem´as la malla tambi´en tiene que ser sim´etrica alrededor de _x_ = 1 _/_ 2), entonces _M_ = _S_<sup>_−_1</sup> . En el caso del continuo ocurre lo mismo ya que si los dos dominios son iguales, entonces 



y por lo tanto _λm_<sup>prec</sup> = 1 para todo _m_ . Si _L_ 1 _̸_ = _L_ 2, entonces puede verse que para _m_ grandes _λ_ 1 _≈ λ_ 2 ya que ambos se hacen independientes de _L_ 1 _,_ 2 y de la condici´on de contorno en el contorno opuesto y por lo tanto 



Pero entonces esto quiere decir que _κ_ ( _MS_ ) se hace independiente de _NI_ para _m_ suficientemente grandes. Este resultado es muy importante desde el punto de vista pr´actico, _el n´umero de condici´on del problema precondicionado no se deteriora bajo refinamiento para el precondicionamiento Dirichletto-Neumann._ 

**286** 

[Document version: curso-0.3.0. File version: $Id: incomp.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

## **Cap´ıtulo 10** 

# **Flujo incompresible** 

#### **10.1. Definici´on de flujo incompresible** 

Un flujo incompresible es ´aquel donde el fluido no se comprime, como es t´ıpicamente el caso de los l´ıquidos, pero tambi´en puede pasar que bajo ciertas condiciones un fluido que es compresible (como los gases en general) no manifiesta efectos de compresibilidad para un patr´on o r´egimen de flujo en particular. En ese caso se le asigna a la propiedad de flujo compresible o incompresible al patr´on de flujo. Para los fluidos compresibles, puede demostrarse que los efectos compresibles van con el n’umero de Mach al cuadrado, es decir que la variaci´on relativa de la densidad 



donde 



es el n´umero de Mach, _u_ es la velocidad del fluido y _c_ es la velocidad del sonido. Podemos decir entonces que el flujo es compresible si el n´umero de Mach es menor que un cierto valor, digamos 0.1. Por ejemplo, un auto a 100 Km/h en atm´osfera est´andar posee un Mach de approx. 0.1, con lo cual en esas condiciones podemos considerar que el flujo es incompresible. 

Es de notar que si las variaciones de densidad son provocadas por otros efectos que no sean la presi´on mec´anica como la dilataci´on t´ermica, expansi´on solutal (p.ej. salinidad), etc... entonces el patr´on de flujo puede considerarse (con respecto a los efectos sobre los algoritmos num´ericos) incompresible, a´un si la densidad resulta no ser constante ni espacialmente ni en el tiempo. El t´ermino compresible/incompresible se aplica a las variaciones de densidad producidad exclusivamente por efecto de la presi´on. 

Si bien en principio uno podr´ıa pensar que la incompresibilidad es una ventaja, ya que permite eliminar (en muchos casos) una variable (la densidad), desde el punto de vista num´erico suele traer m´as problemas que soluciones. 

287 

Cap´ıtulo 10. Flujo incompresible _Secci´on 10.2. Ecuaciones de Navier-Stokes incompresible_ 

#### **10.2. Ecuaciones de Navier-Stokes incompresible** 

Las ecuaciones de Navier-Stokes incompresibles son 





La primera es la _“ecuaci´on de momento”_ , mientras que la segunda es la _“ecuaci´on de continuidad”_ o _“balance de masa”_ . Es importante notar que en el l´ımite de _“flujo reptante”_ o _“flujo de Stokes”_ (es decir, despreciando el t´ermino convectivo), las ecuaciones resultantes son exactamente iguales a las de elasticidad lineal incompresible isotr´opica, si reemplazamos el vector de velocidad por el de desplazamiento y la viscosidad por el m´odulo de elasticidad. 

Las siguientes observaciones nos permiten adelantar el problema ocasionado por la incompresibilidad: 

- **La condici´on de incompresibilidad no tiene un t´ermino temporal:** Esto quiere decir que “la presi´on no tiene historia”. El estado del fluido s´olo st´a dado por la velocidad. Tambi´en podemos decir que la ecuaci´on de continuidad aparece como una restricci´on, m´as que como una ecuaci´on de evoluci´on. La presi´on, pasa a ser el multiplicador de Lagrange asociado. 

- **Las ecuaciones son no locales:** Esto es m´as f´acil de ver en el caso de elasticidad. Se sabe bien que en el caso de elasticidad compresible el problema es el´ıptico, de manera que hay una cierta localidad de los efectos. Esto se pierde en el caso incompresible. Por ejemplo, consideremos un s´olido incompresible que ocupa una regi´on Ω(ver figura 10.1). Las condiciones son de desplazamiento nulo en toda la frontera, menos en una cierta parte Γ1 donde se aplica un cierto desplazamiento uniforme, y otra cierta parte Γ2 donde las condiciones son libres, es decir tracci´on nula. En el caso compresible, el operador es el´ıptico, local, y la influencia del desplazamiento impuesto sobre el dominio Γ1 en el dominio Γ2 depender´a de la distancia entre ambas regiones, sus tama˜nos relativos, etc... Si el tama˜no de ambas regiones es similar y muy peque˜nos con respecto a la distancia que los separa, entonces los desplazamientos en Γ2 ser´an despreciables. Por el contrario, en el caso incompresible, el cambio de volumen total en Γ2 debe ser igual al impuesto en Γ1, por lo tanto los desplazamientos en Γ2 ser´an del mismo orden que aquellos impuestos en Γ1 (asumiendo que ambas regiones de la frontera tienen dimensiones similares). 

- **Cambia el c´aracter matem´atico de las ecuaciones:** Tambi´en en el caso el´astico, estacionario las ecuaciones dejan de ser el´ıpticas al pasar al caso incompresible. Esto se debe a que la ecuaci´on de continuidad _“no tiene t´ermino en derivadas segundas”_ . 

- **La ecuaci´on de la energ´ıa se desacopla de la de momento y continuidad:** El campo de temperaturas se puede obtener a posteriori a partir de el campo de velocidades obtenido. 

#### **10.3. Formulaci´on vorticidad-funci´on de corriente** 

La vorticidad se define como 



[Document version: curso-0.3.0. File version: $Id: incomp.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 



Cap´ıtulo 10. Flujo incompresible _Secci´on 10.3. Formulaci´on vorticidad-funci´on de corriente_ 



<!-- Start of picture text -->
L<br><!-- End of picture text -->

Figura 10.1: No localidad en elasticidad incompresible. 

el cual, para un flujo bidimensional se reduce a 



En 2D se puede encontrar una funci´on de corriente _ψ_ tal que 





Tomando rotor de (10.3) se llega, despues de un cierto trabajo algebraico, a 



pero (s´olo en 2D!) el tercer t´ermino es nulo, ya que _∇_ **u** debe estar en el plano y **Ω** est´a fuera del plano, de manera que la ecuaci´on se reduce a una ecuaci´on de advecci´on difusi´on para la vorticidad 



Por otra parte, recombinando (10.6) con (10.7) se llega a una ecuaci´on de Poisson para la funci´on de corriente: 



La _“formulaci´on vorticidad/funci´on de corriente”_ consiste en resolver (10.10) y (10.11) en forma acoplada. 

Las ventajas y desventajas de la formulaci´on, con respecto a la formulaci´on en variables primitivas (10.3-10.4) son 

**289** 

[Document version: curso-0.3.0. File version: $Id: incomp.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 10. Flujo incompresible _Secci´on 10.4. Discretizaci´on en variables_ _<u>primitivas</u>_ 

La extensi´on a 3D de la formulaci´on vorticidad/funci´on de corriente es muy compleja. 

- La formulaci´on vorticidad/funci´on de corriente tiene un grado de libertad menos por nodo. 

- Las condiciones de contorno para la presi´on son desconocidas para la formulaci´on en variables primitivas. 

- Las condiciones de contorno para la vorticidad son desconocidas para la formulaci´on vorticidad/funci´on de corriente . 

- La formulaci´on vorticidad/funci´on de corriente requiere de cierto cuidado en cuanto a la discretizaci´on. 

#### **10.4. Discretizaci´on en variables primitivas** 



<!-- Start of picture text -->
pressure node<br>u velocity node<br>v velocity node<br>j+1<br>j<br>j−1<br>i−1 i i+1<br><!-- End of picture text -->

Figura 10.2: Grilla est´andar (no staggered) usada para flujo incompresible en variables primitivas. 

Si despreciamos el t´ermino convectivo (problema de Stokes) y consideramos el caso estacionario en una malla de paso homog´eneo _h_ , la siguiente discretizaci´on (espacial) de segundo orden parece ser un buen punto de partida (ver figura 10.2) : 



donde ∆ _h_ reresenta el operador de Laplace discreto est´andar de 5 puntos 





[Document version: curso-0.3.0. File version: $Id: incomp.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 10. Flujo incompresible _Secci´on 10.4. Discretizaci´on en variables_ _<u>primitivas</u>_ 



<!-- Start of picture text -->
j+1<br>j<br>j−1<br>i−1 i i+1<br><!-- End of picture text -->

Figura 10.3: Grilla no staggered. Stencil para la ecuaci´on de momento seg´un _x_ 



<!-- Start of picture text -->
j+1<br>j<br>j−1<br>i−1 i i+1<br><!-- End of picture text -->

Figura 10.4: Grilla no staggered. Stencil para la ecuaci´on de momento seg´un _y_ 

En las figuras 10.3, 10.4 y 10.5 pueden verse los stenciles usados para cada una de las ecuaciones. Pero resulta ser que las presiones en los nodos impares se desacopla de los pares dando lugar a modos _“checkerboard”_ en la presi´on. Las formas des resolver esto es 

- Resolver una ecuaci´on alternativa para la presi´on llamada PPE (Poisson Pressure Equation). Usar mallas “staggered” (en espa˜nol “desparramadas” (???)) 

- Usar m´etodos de compresibilidad artificial. 

Discutiremos a continuaci´on el uso de mallas staggered. 

**291** 

[Document version: curso-0.3.0. File version: $Id: incomp.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 10. Flujo incompresible _Secci´on 10.5. Uso de mallas staggered_ 



<!-- Start of picture text -->
j+1<br>j<br>j−1<br>i−1 i i+1<br><!-- End of picture text -->

Figura 10.5: Grilla no staggered. Stencil para la ecuaci´on de continuidad 

#### **10.5. Uso de mallas staggered** 

Si consideramos la ecuaci´on de momento seg´un _x_ , entonces vemos que lo ideal ser´ıa tener una malla para los nodos de velocidad _x_ desplazada en _h/_ 2 con respecto a la malla de los nodos de presi´on, en ese caso podr´ıamos tener una ecuaci´on de la forma (ver figura 10.7) 



Similarmente, para la ecuaci´on de momento seg´un _y_ tenemos (ver figura 10.8) 



Esto evita el desacoplamiento de las presiones entre nodos pares e impares. Entonces tenemos 3 redes “staggered” a saber (ver figura 10.6) 

Los nodos de presi´on: _pij ≈ p_ ( _ih, jh_ ) 

Los nodos de velocidad _x_ : _ui_ +1 _/_ 2 _,j ≈ u_ (( _i_ +<sup>1</sup> _/_ 2) _h, jh_ ) 

Los nodos de velocidad _y_ : _vi,j_ +1 _/_ 2 _≈ v_ ( _ih,_ ( _j_ +<sup>1</sup> _/_ 2) _h_ ) 

con _i, j_ enteros. Por otra parte, la ecuaci´on de continuidad tambi´en queda en un stencil m´as compacto, si lo imponemos sobre los nodos de presi´on (ver figura 10.9) 



Por otra parte, las condiciones de contorno tambi´en se simplifican algo, en cuanto a las condiciones sobre la presi´on, ya que utilizando s´olo contornos que coinciden con lineas semienteras ( _i, j_ =entero+<sup>1</sup> _/_ 2). 

El m´etodo de mallas staggered es probablemente el m´as robusto y prolijo para tratar flujo incompresible por diferencias finitas. 



[Document version: curso-0.3.0. File version: $Id: incomp.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 10. Flujo incompresible _Secci´on 10.6. Discretizaci´on_ _<u>por</u> elementos finitos_ 



<!-- Start of picture text -->
j+1<br>j+1/2<br>j<br>j−1/2<br>j−1<br>i−1 i i+1<br>i−1/2 i+1/2<br><!-- End of picture text -->

Figura 10.6: Grilla staggered usada para flujo incompresible en variables primitivas. 

#### **10.6. Discretizaci´on por elementos finitos** 

Considerando el caso estacionario, flujo reptante, un t´ermino forzante **f** y condiciones de contorno Dirichlet, las ecuaciones de gobierno son 







y espacios de interpolaci´on 





La formulaci´on d´ebil Galerkin se obtiene pesando la ecuaci´on de momento por una funci´on de interpolaci´on de velocidad y pesando la ecuaci´on de continuidad con las funciones de interpolaci´on de presi´on. 



Notar que, como no aparecen derivadas de _p_ ni _φ_ entonces es posible utilizar aproximaciones discontinuas para _p_ . 



[Document version: curso-0.3.0. File version: $Id: incomp.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 10. Flujo incompresible _Secci´on 10.6. Discretizaci´on_ _<u>por</u> elementos finitos_ 



<!-- Start of picture text -->
punto alrededor del<br>j+1 cual se hace la aproximación<br>j+1/2<br>j<br>j−1/2<br>j−1<br>i−1 i i+1<br>i−1/2 i+1/2<br><!-- End of picture text -->

Figura 10.7: Grilla staggered. Stencil para la ecuaci´on de momento seg´un _x_ 

El sistema al que se llega es; 



o 



donde 







**294** 

[Document version: curso-0.3.0. File version: $Id: incomp.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 10. Flujo incompresible _Secci´on 10.7. El test de la_ _<u>parcela</u>_ 



<!-- Start of picture text -->
punto alrededor del<br>j+1 cual se hace la aproximación<br>j+1/2<br>j<br>j−1/2<br>j−1<br>i−1 i i+1<br>i−1/2 i+1/2<br><!-- End of picture text -->

Figura 10.8: Grilla staggered. Stencil para la ecuaci´on de momento seg´un _y_ 

N´otese que la matriz **K** es sim´etrica y definida positiva, mientras que la matriz total **A** s´olo es sim´etrica y de hecho no puede ser definida positiva ya que tiene elementos diagonales (en el bloque **0** ) nulos. 

Como _K_ es no-singular podemos eliminar **U** de la ecuaci´on de momento e insertarla en la ecuaci´on de continuidad obteniendo una ecuaci´on para **P** de la forma 



La matriz **H** es sim´etrica y semidefinida positiva. Para que el problema este bien planteado debemos al menos exigir que la matriz sea no-singular. Podemos ver que esto ocurre si y s´olo si **Q** tiene rango de filas (el n´umero de filas linealmente independiente) _Np_ (el n´umero de grados de libertad de presi´on). Efectivamente, si **Q** tiene rango menor que _Np_ entonces existe algun vector **P** tal que **QP** = **0** y entonces **HP** = 0. Por otra parte, si **Q** tiene rango igual a _Np_ entonces para todo **P** _̸_ = **0** vale que **u** = **QP** _̸_ = 0 y entonces 



con lo cual **H** resulta ser definida positiva y por lo tanto no-singular. 

#### **10.7. El test de la parcela** 

Ahora bien **Q** es de dimensi´on _Nu × Np_ , de manera que, para que **Q** sea no singular debemos pedir que al menos _Nu ≥ Np_ . Si bien esto parece un requerimiento bastante simple, en realidad sirve para descartar toda una serie de familias de interpolaci´on y da lugar al famoso _“test de la parcela”_ ( _“patch test”_ ). 

Consideremos por ejemplo la interpolaci´on m´as simple que se nos pueda ocurrir es _P_ 1 _/P_ 0 para tri´angulos, es decir velocidades lineales continuas y presiones constantes por elemento (ver figura 10.10). (La convenci´on aqu´ı es poner primero el espacio de interpolaci´on para velocidades y despu´es 

**295** 

[Document version: curso-0.3.0. File version: $Id: incomp.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 10. Flujo incompresible _Secci´on 10.7. El test de la_ _<u>parcela</u>_ 



<!-- Start of picture text -->
punto alrededor del<br>j+1 cual se hace la aproximación<br>j+1/2<br>j<br>j−1/2<br>j−1<br>i−1 i i+1<br>i−1/2 i+1/2<br><!-- End of picture text -->

Figura 10.9: Grilla staggered. Stencil para la ecuaci´on de continuidad. 

el que se usa para presiones. En general, a menos que se mencione lo contrario el espacio para velocidades se asume continuo y el de presiones discontinuo. _Pn_ denota el espacio de funciones que es polinomial de grado _n_ por elemento, mientras que _Qn_ denota el espacio de funciones bilineales (trilineales en 3D) de grado _n_ .) En una malla estructurada de cuadr´angulos, donde dividimos cada cuadr´angulo en dos tri´angulos, tenemos (para una malla suficientmente grande) _Np_ =2 grados de libertad de presi´on por cada cuadr´angulo y un nodo de velocidad (es decir _Nu_ = 2), por lo tanto no se satisface el test de la parcela y la aproximaci´on es inestable. Si tomamos parcelas m´as peque˜nas la situaci´on es peor, ya que el _Nu_ es mayor o igual al _Nu_ asint´otico pero imponiendo las condiciones de contorno _“m´as inestables posibles”_ , es decir todo el contorno de la parcela con velocidades impuestas el _Nu_ resulta ser 



Entonces, si bien el test de la parcela asint´otico permite descartar una serie de familias de interpolaci´on, el test aplicado sobre parcelas m´as peque˜no resulta ser m´as restrictivo. Por ejemplo para la interpolaci´on _Q_ 1 _/P_ 0 el an´alisis asint´otico da _Nu_ por celda = 2, _Np_ por celda = 1 lo cual en principio est´a bien, pero cuando vamos a una parcela de 2 _×_ 2 = 4 elementos cuadrangulares tenemos _Nu_ = 2 (s´olo el nodo de velocidad del medio est´a libre), _Np_ = 3 (uno de los nodos de presi´on siempre est´a restingido) lo cual est´a mal. 

Sin embargo, puede verse que un macroelemento triangular formado por 3 elementos _Q_ 1 _/P_ 0 es estable. 

La relaci´on asint´otica m´as apropiada parece ser _Nu_ = 2 _Np_ . 

**296** 

[Document version: curso-0.3.0. File version: $Id: incomp.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 10. Flujo incompresible _Secci´on 10.8. La condici´on de Brezzi-Babuska_ 





<!-- Start of picture text -->
Q1/P0 Q2/P1 Q2/Q1<br>inestable estable inestable<br>Q2(s)/Q1 Q2(s)/P1 Q2(s)/P0<br>inestable inestable estable<br>P1/P0 P2/P1 P2/P0<br>inestable inestable estable<br>nodo de presión<br>nodo de velocidad<br>P2+/P1<br>estable<br><!-- End of picture text -->

Figura 10.10: Combinaciones de espacios de interpolaci ’on de elementos finitos. Velocidades continuas, presiones discontinuas. 

#### **10.8. La condici´on de Brezzi-Babuska** 

Si bien el test de la parcela es muy ´util para descartar posibles familias de interpolaci´on, no es suficiente para asegurar la convrgencia. R´ıos de tinta han corrido en cuanto a cual es la condici´on para asegurar convergencia en problemas de este tipo y la respuesta es la conocida _“condici´on de Brezzi-Bab_<sup>_.._</sup> _.uska”_ tambien conocida como condicion _“inf-sup”_ . 



Trabajando un poco esta ecuaci´on puede llegarse a la conclusi´on de que 



donde _Mp_ es la _“matriz de masa”_ de las funciones de presi´on es decir 



Como _Mp_ es una “matriz de masa”, tiene un n´umero de condici´on muy bajo y no afecta mucho la expresi´on anterior, de manera que podemos tomar tambi´en 





[Document version: curso-0.3.0. File version: $Id: incomp.tex,v 1.5 2005/05/22 03:40:47 mstorti Exp $] 

Cap´ıtulo 10. Flujo incompresible _Secci´on 10.9. M´etodos FEM estabilizados_ 



#### _Q1/P0_ 

Figura 10.11: Parcela de 2 _×_ 2 elementos cuadrangulares. Nodos pintados de negro indican grados de libertad restringidos. 

Notemos que la matriz en cuesti´on es la misma que se obtiene si condensamos el sistema total en el vector de presiones, ec. (10.33). De manera que el criterio de BB parece relacionar la convergencia del espacio de interpolaci´on con el comportamiento de los autovalores para _h →_ 0. 

#### **10.9. M´etodos FEM estabilizados** 

Podemos modificar el sistema de ecuaciones a resolver si agregamos a la ecuaci´on de momento un t´ermino de estabilizaci´on que proviene de tomar el gradiente de la ecuaci´on de continuidad y otro proporcional a la divergencia de la ecuaci´on de momento a la ecuaci´on de continuidad. El sistema modificado es 





El sistema de ecuaciones es 



donde 





son aproximaciones a los operadores de Laplace (vectorial) y _“grad-div”_ . 

Notar que con el agregado de estos t´erminos de estabilizaci´on ahora el bloque que antes era nulo ya no lo es. Por otra parte el sistema es ahora el´ıptico, con lo cual deber´ıan imponerse tambi´en condiciones de contorno sobre la presi´on. (Lo cual no es trivial). En la pr´actica _“se deja la presi´on libre”_ lo cual es equivalente a imponer derivada normal de la presi´on nula ( _∂n_<sup>_∂p_=0)locual</sup><sup>**noescierto**perose</sup> absorbe en una capa l´ımite de espesor _h_ . 

**298** 

[Document version: curso-0.3.0. File version: ] 

# **´Indice alfab´etico** 

ajuste del contorno, 101 alto orden esquemas en dif. fin. de , 90 backward difference, _v´ease_ diferencia hacia atr´as banda ancho de, 99 matriz, 96 centrada diferencia, 75 choque ondas de, 85 compresible flujo potencial subs´onico c., 84 conservativo esquema, 85 consistencia, 79 contravariante tensor m´etrico, 104 convariante tensor m´etrico, 104 convecci´on, 112 convecci´on-reacci´on-difusi´on, 112 convergencia lineal, 88 convergencia cuadr´atica, 90 definida positiva matriz, 78 diferencia hacia adelante, 74 diferencia hacia atr´as, 74 diferencias finitas m´etodo de, 73 sistema de ecuaciones, 77 

difusi´on, 112 Dirichlet condici´on de contorno tipo, 76 escala, factores de, 105 esf´ericas coordenadas, 105 estabilidad, 80 ficticio nodo, 82 forward difference, _v´ease_ diferencia hacia adelante Gauss m´et. de eliminaci´on de, 97 hiper´elastico material, 84 irregular dominios de forma, 100 Lax, Teorema de Lax, 80 mapeo del dominio de integraci´on, 104 multidimensional m´et. de d.f. m., 92 

Neumann condici´on de contorno tipo, 80 no-lineales problemas, 84 nodos, 73 numeraci´on de nodos, 99 orden de convergencia, 79 ortogonales 

299 

´INDICE ALFAB´ETICO _´INDICE ALFAB´ETICO_ 

coordenadas curvil´ıneas, 105 precisi´on de la m´aquina, 86 punto fijo, m´etodo de, 85 reacci´on, 112 residuo de un sistema no-lineal de ecs., 86 secante m´etodo, 87 sim´etrica matriz, 78, 97 stencil, 90, 95 tangente m´etodo, 89 Taylor serie de T. para aprox. en diferencias, 73 tensor m´etrico contravariante, 104 tolerancia, 86 tolerancia para la resol. de un sistema no-lin., 86 transformaci´on conforme, 106 tri-diagonal matriz, 94 

**300** 

[Document version: curso-0.3.0. File version: ] 

