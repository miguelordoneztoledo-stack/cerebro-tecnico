---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\PRE-MAESTRÍA UNI - HIDRAULICA\PRE-MAESTRÍA UNI - HIDRAULICA\MATEMÁTICA APLICADA\MATERIAL\ApunteSucesionesSeries.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]

# An´alisis Matem´atico III: Apunte sobre sucesiones y series num´ericas y de funciones 

Pablo Torres - Departamento de Matem´atica Escuela de Ciencias Exactas y Naturales Facultad de Ciencias Exactas, Ingenier´ıa y Agrimensura Universidad Nacional de Rosario 

## **1. Sucesiones num´ericas** 

### **1.1. Introducci´on** 

Una sucesi´on de n´umeros reales es una colecci´on ordenada de n´umeros reales. Al considerar una sucesi´on se conoce cu´al es el lugar que ocupa cada uno. Hay un primer elemento, al que podr´ıamos llamar _a_ 1, un segundo _a_ 2, un elemento _n_ -´esimo o general, _an_ , etc. 

Notaremos a las sucesiones por 



donde si bien utilizamos llaves, hacemos hincapi´e en que consideramos el orden en el que los elementos son presentados. 

**Nota 1.1.1.** _En ocasiones los valores de los ´ındices que indican el dominio de la sucesi´on pueden comenzar desde n_ = 0 _, sin que esto afecte a las definiciones que a ´estas involucren._ 

#### **Ejemplo 1.1.1.** 





_5. Sucesi´on de Fibonacci: f_ 1 = 1 _, f_ 2 = 2 _, fn_ +2 = _fn_ + _fn_ +1 _para n ∈_ N _._ 

Observemos en los ejemplos que a cada n´umero natural (posici´on en la sucesi´on) le corresponde un elemento de la sucesi´on, y s´olo uno, y que los elementos son, por definici´on, n´umeros reales. 

**Definici´on 1.1.1** (Sucesi´on num´erica) **.** 

_Una sucesi´on num´erica (real) es una funci´on cuyo dominio es el conjunto de los n´umeros naturales, y su codominio el de los n´umeros reales,_ 



1 

_1.2 Sucesiones Convergentes, Divergentes y Oscilantes_ An´alisis Matem´atico III 

Teniendo en vista esta definici´on, las sucesiones son funciones, todas con los mismos conjuntos dominio y codominio. Dos sucesiones ser´an iguales si sus respectivos t´erminos lo son. Esto es, 



La igualdad de sucesiones no debe confundirse con la igualdad de sus codominios. 

**Definici´on 1.1.2** (Sucesiones acotadas) **.** 

_Una sucesi´on {an}n se dice acotada superiormente, si existe un valor real M, tal que se verifica, para todo n,_ 



_y est´a acotada inferiormente, si existe m tal que_ 



_para cualquier n._ 

_Esto es, el recorrido de la sucesi´on es un subconjunto acotado_<sup>1</sup> _, superiormente o inferiormente, seg´un sea el caso._ 

#### **Ejemplo 1.1.2.** 

_1. {an}n_ = _{_ 1 _,_ 2 _,_ 3 _,_ 4 _,..., n,...}, est´a acotada inferiormente por 1, y no est´a acotada superiormente._ 

_2. {bn}n_ = _{−_ 2 _, −_ 4 _, −_ 6 _,..., −_ 2 _n,...}, no est´a acotada inferiormente, y est´a acotada superiormente por −_ 2 _._ 



### **1.2. Sucesiones Convergentes, Divergentes y Oscilantes** 

Considerando que una sucesi´on es un caso particular de una funci´on real, con dominio en N, en la cual se piensa a _an_ como la imagen de _n_ por esta funci´on, tienen sentido las siguientes definiciones de convergencia y divergencia. 

#### **Definici´on 1.2.1.** 

_Una sucesi´on num´erica {an} tiene l´ımite finito ℓ, si para cualquier n´umero positivo ε, existe un n´umero natural N ∈_ N _, tal que se verifica_ 



_Si este es el caso, decimos que la sucesi´on es convergente, o que la sucesi´on converge a ℓ y lo notaremos_ 



Gr´aficamente, si dado _ε >_ 0, es posible encontrar _N_ , tal que, todos los _an_ siguientes se encuentren en el entorno ( _ℓ − ε,ℓ_ + _ε_ ). 

> 1Un conjunto no vac´ıo _A ⊆_ R es acotado superiormente si existe _M ∈_ R tal que _∀a ∈ A_ , _a ≤ M_ . Al n´umero _M_ se lo denomina cota superior de _A_ . Es claro que si _M_ es cota superior de _A_ , entonces todo n´umero mayor que _M_ tambi´en es cota superior de _A_ . De manera an´aloga se define conjunto acotado inferiormente y cota inferior. 

2 

_1.2 Sucesiones Convergentes, Divergentes y Oscilantes_ 

An´alisis Matem´atico III 

**Definici´on 1.2.2** (Sucesiones divergentes y oscilantes) **.** 

_Se dice que una sucesi´on {an} diverge a_ +∞ _(resp. −_ ∞ _), si para cualquier M >_ 0 _, existe N ∈_ N _, donde_ 



_La sucesi´on diverge, si lo hace a_ +∞ _o a −_ ∞ _._ 

_Finalmente, una sucesi´on se dice oscilante si no es convergente ni divergente._ 

**Nota 1.2.1.** _Dado ε >_ 0 _, si un n´umero N_ 1 _es ´util en la condici´on de convergencia (o para un M >_ 0 _, en la de divergencia), entonces cualquier N > N_ 1 _tambi´en lo es. En efecto,_ 



_Adem´as, es ´ultil observar que_ 



_y lo mismo con ±_ ∞ _._ 

#### **Ejemplo 1.2.1.** 

_1. La sucesi´on {_<sup><u>1</u></sup> _n_<sup>_} es convergente a 0. En efecto, dado ε>_0</sup><sup>_, basta tomar un n´umero natural N >_</sup> _ε_<sup><u>1</u></sup> _(Propiedad Arquimedeana_<sup>2</sup> _), para obtener_ 





_5. Las sucesiones {n}, {_ 2 _n}, {n_<sup>2</sup> _}, etc., divergen a_ +∞ _._ 

_6. Las sucesiones {_ ( _−_ 1)<sup>_n_</sup> _} y {_ ( _−_ 1)<sup>_n_</sup> _n} son oscilantes. La primera est´a acotada, y la segunda no._ 

Se pueden afirmar los l´ımites del ejemplo anterior por medio de la siguiente observaci´on. 

#### **Nota 1.2.2.** 

_Sea f una funci´on real y {an} una sucesi´on tal que an_ = _f_ ( _n_ ) _._ 



#### **Ejercicio 1.2.1.** _Probar los siguientes l´ımites:_ 

> 2Propiedad Arquimedeana: Si _x >_ 0 e _y_ es un n´umero real arbitrario, entonces existe _n ∈_ N tal que _n.x > y_ . Para probar este resultado es ´util el Axioma del supremo: Todo conjunto no vac´ıo de n´umeros reales acotado superiormente tiene supremo en R. Vale aclarar aqu´ı la definici´on de supremo de un conjunto no vac´ıo _A ⊆_ R ( _s_ = sup( _A_ )): un n´umero real _s_ es supremo de _A_ si es cota superior de _A_ y toda otra cota superior de _A_ es mayor que _s_ , i.e. _s_ es la menor de las cotas superiores de _A_ . Equivalentemente, _s_ = sup( _A_ ) si para todo _h >_ 0 existe _a ∈ A_ tal que _s − h < a ≤ s_ . 

3 

_1.2 Sucesiones Convergentes, Divergentes y Oscilantes_ 

An´alisis Matem´atico III 









Agrupando resultados conocidos, enunciamos el siguiente resultado y proponemos la demostraci´on como ejercicio. 

**Teorema 1.2.1.** _Son v´alidas las siguientes afirmaciones:_ 

_1. El l´ımite de una sucesi´on num´erica, si existe, es ´unico._ 

_2. Si an → ℓ, entonces |an| →|ℓ|._ 

_3. Si an →_ 0 _, y {bn} est´a acotada, an · bn →_ 0 

_4. Si an → ℓ_ 1 _, bn → ℓ_ 2 _, y c ∈_ R _,_ 







_5. Si para n > N, an_ ≦ _bn_ ≦ _cn, y adem´as valen an → ℓ y cn → ℓ, entonces bn → ℓ._ 

El siguiente Lema permite probar varios l´ımites ´utiles. 

**Lema 1.2.1** (Desigualdad de Bernoulli) **.** _Si h > −_ 1 _y h̸_ = 0 _._ 



_para todo n ∈_ N _._ 

_Adem´as, la igualdad se verifica solo para n_ = 1 _._ 

_Demostraci´on._ Si _n_ = 1, se cumple por igualdad. 

A continuaci´on mostraremos, utilizando el Principio de Inducci´on, que para _n_ ≧ 2, 



Para _n_ = 2, (1 + _h_ )<sup>2</sup> = 1 + 2 _h_ + _h_<sup>2</sup> _>_ 1 + 2 _h ._ 

4 

_1.2 Sucesiones Convergentes, Divergentes y Oscilantes_ 

An´alisis Matem´atico III 

Si suponemos que para alg´un _n ∈_ N es (1 + _h_ )<sup>_n_</sup> _>_ 1 + _nh_ , como 1 + _h >_ 0, 



que completa el argumento de inducci´on. 

Observar que en el Lema anterior, si tomamos _h_ = 0, se verifica la igualdad para todo _n ∈_ N **Proposici´on 1.2.1.** _Dado p >_ 0 _,_ 



_Demostraci´on._ Si _p_ = 1, es inmediato. 

Si _p >_ 1, _p_ = 1 + _h_ , con _h >_ 0. En este caso, por la Desigualdad de Bernoulli, 



Observemos que 



ya que, dado _M >_ 0, por la Propiedad Arquimedeana, existe _N_ tal que _Nh > M −_ 1, y con esos elementos, ( _h >_ 0) 



Luego 







y en consecuencia, 



**Ejercicio 1.2.2.** _En este ejercicio queremos probar la siguiente convergencia:_ 



_Para ello, se propone como sugerencia, reemplanzando en el lado derecho de la igualdad_<sup><u>1</u></sup> 2<sup>_an_=</sup><sup>_an −_</sup> 21<sup>_an por la expresi´on como suma de an, arribar a la f´ormula_</sup> 



_y utilizar la Proposici´on 1.2.1._ 

5 

_1.3 Sucesiones Mon´otonas_ 

An´alisis Matem´atico III 

### **1.3. Sucesiones Mon´otonas** 

**Definici´on 1.3.1** (Sucesiones Mon´otonas) **.** _Una suceci´on {an} se dice_ 

_1. creciente, si an ≤ an_ +1 _, ∀n ∈_ N _,_ 

_2. decreciente, si an ≥ an_ +1 _, ∀n ∈_ N _._ 

_3. estrictamente creciente, si an < an_ +1 _, ∀n ∈_ N _,_ 

_4. estrictamente decreciente, si an > an_ +1 _, ∀n ∈_ N _._ 

_para todo ∈_ N _. Si una sucesi´on es creciente o decreciente, se dice que es mon´otona._ 

_Naturalmente adem´as, se definen las sucesiones no decrecientes y no crecientes._ 

- **Ejemplo 1.3.1.** _1. Si {an} es creciente (resp. decreciente) entonces {−an} es decreciente (resp. creciente)._ 

   _2. Si {an} es acotada superiormente (resp. inferiormente) entonces {−an} es acotada inferiormente (resp. superiormente)._ 

   _3. Una sucesi´on est´a acotada superiormente e inferiormente si y solo si existe T ∈_ R _tal que |an| ≤ T, ∀n ∈_ N _._ 

El siguiente resultado no es s´olo v´alido para sucesiones mon´otonas, pero su rec´ıproca s´ı, y por eso se incluye aqu´ı. 

**Teorema 1.3.1.** _Si una sucesi´on {an} es convergente, entonces est´a acotada (sup. e inferiormente)._ 

_Demostraci´on._ Sea _ℓ_ , tal que _an → ℓ_ . Entonces, dado _ε >_ 0, existe _N ∈_ N, de manera que, para _n > N_ , 



Luego, para _ε_ = 1, existe _N_ 1 _∈_ N tal que si _n ≥ N_ 1 entonces _|an| < |ℓ|_ + 1. 

Si ahora consideramos _T_ = m´ax _{|a_ 1 _|, |a_ 2 _|,..., |aN_ 1 _−_ 1 _|, |aN_ 1 _|, |ℓ|_ + 1 _}_ (m´aximo de una cantidad finita de n´umeros), entonces, 



y para todo _n_ , es _|an| ≤ T_ . 

**Nota 1.3.1.** _Si una sucesi´on est´a acotada, ¿es convergente?_ 

_Observemos que la sucesi´on {_ ( _−_ 1)<sup>_n_</sup> _} est´a acotada y no es convergente ya que es oscilante. ¿Qu´e ocurre si la sucesi´on es acotada y adem´as es mon´otona?_ 

#### **Teorema 1.3.2.** 

_Si una sucesi´on mon´otona {an} est´a acotada, entonces es convergente._ 

6 

_1.3 Sucesiones Mon´otonas_ 

An´alisis Matem´atico III 

_Demostraci´on._ Comencemos con el caso _{an}_ creciente, _an−_ 1 _< an_ , esto es, para todo _n_ . 

Como la sucesi´on _an_ est´a acotada, el conjunto _A_ = _{an_ : _n ∈_ N _}_ (pensado como el recorrido de la sucesi´on), es un subconjunto no vac´ıo y acotado superiormente de R, y por el Axioma del Supremo, existe _ℓ_ , supremo de este conjunto num´erico. Mostremos que _an → ℓ_ . Sea _ε >_ 0 cualquiera. Deseamos hallar _N ∈_ N tal que _n > N ⇒|an − ℓ| < ε_ . 

Por un lado, como _ℓ_ = sup( _A_ ), vale que 



para todo _n ∈_ N. 

Por otro lado, como _ℓ_ = sup( _A_ ), por el Teorema de Caracterizaci´on del supremo, dado _ε >_ 0, existe un elemento de _A_ , llam´emoslo _aN_ , tal que 



Observando que _aN ≤ an_ para todo _n > N_ , se tiene 



Combinando las desigualdades (1) y (2), para todo _n > N_ , 



Si _{an}_ es decreciente y acotada, entonces _{−an}_ es creciente y acotada, y por lo tanto convergente, lo que implica que sea tambi´en en este caso _{an}_ convergente. 

**Nota 1.3.2.** _Si una sucesi´on es acotada y adem´as es mon´otona a partir de un cierto sub´ındice n_ 0 _∈_ N _, entonces la sucesi´on es convergente._ 

#### **Corolario 1.3.1.** 

_Una sucesi´on creciente (decreciente), converge o diverge a_ +∞ _(−_ ∞ _)._ 

**Definici´on 1.3.2** (Subsucesi´on) **.** _Dada una sucesi´on num´erica {an}_<sup>∞</sup> _n_ =1<sup>_, se denomina subsucesi´on de {an}_∞</sup> _n_ =1 _a toda sucesi´on de la forma {ank}_<sup>∞</sup> _k_ =1<sup>=</sup><sup>_{an_</sup> 1<sup>_,an_</sup> 2<sup>_,...,an_</sup> _k_<sup>_,...},_</sup> 

_formada por elementos de la sucesi´on original {an}_<sup>∞</sup> _n_ =1<sup>_ytalqueseconservaelordenrelativodelos_</sup> _´ındices, i.e._ 



Enunciamos dos propiedades que relacionan los l´ımites de una sucesi´on y sus subsucesiones, cuyas demostraciones quedan como ejercicio. 

**Proposici´on 1.3.1.** _Una sucesi´on es convergente a un valor ℓ si y solo si todas sus subsucesiones son convergentes a ℓ._ 

**Proposici´on 1.3.2.** _Sea ℓ ∈_ R _. Si una sucesi´on es tal que toda subsucesi´on tiene una sub-subsucesi´on que converge a ℓ, entonces la sucesi´on original converge a ℓ._ 

7 

- _1.4 Principio del punto de acumulaci´on. Teorema de Bolzano-Weierstrass._ An´alisis Matem´atico III 

A continuaci´on definiremos las sucesiones num´ericas complejas, i.e. aquellas sucesiones con codominio C. 

**Definici´on 1.3.3** (Sucesi´on num´erica compleja) **.** 

_Una sucesi´on num´erica compleja es una funci´on cuyo dominio es el conjunto de los n´umeros naturales, y su codominio el de los n´umeros complejos,_ 





La definici´on de l´ımite de una sucesi´on num´erica compleja se define de manera natural considerando el m´odulo de un n´umero complejo. 

Una sucesi´on _{an}_ compleja puede descomponerse en su parte real e imaginaria, i.e. _an_ = _un_ + _i.vn_ , donde _un_ y _vn_ son sucesiones num´ericas reales. 

**Teorema 1.3.3.** _Una sucesi´on num´erica compleja es convergente si y solo si las sucesiones de su parte real e imaginaria son ambas convergentes._ 

### **1.4. Principio del punto de acumulaci´on. Teorema de Bolzano-Weierstrass.** 

**Definici´on 1.4.1** (Punto de acumulaci´on de una sucesi´on) **.** _Sea {an} una sucesi´on y α ∈_ R _. Decimos que α es un apunto de acumulaci´on de la sucesi´on {an} si, para todo ε >_ 0 _el conjunto_ 



_es infinito (no acotado superiormente)._ 

**Ejemplo 1.4.1.** _1. La sucesi´on {_ ( _−_ 1)<sup>_n_</sup> _} posee dos puntos de acumulaci´on α_ 1 = 1 _y α_ 2 = _−_ 1 _. Observar que esta sucesi´on es oscilante._ 

_2. La suceci´on { n_<sup><u>1</u></sup><sup>_}tieneaα_= 0</sup><sup>_como´unicopuntodeacumulaci´on.Observarqueestasucesi´on_</sup> _converge a_ 0 _._ 

_3. La sucesi´on {n} no tiene punto de acumulaci´on y es divergente a_ +∞ _._ 

_4. La sucesi´on definida como a_ 2 _n_ = _n y a_ 2 _n_ +1 = 0 _para n ∈_ N _tiene a α_ = 0 _como ´unico punto de acumulaci´on. Observar que esta suceci´on no es convergente._ 

**Proposici´on 1.4.1** (Principio del punto de acumulaci´on para sucesiones) **.** _Sea {xn} una sucesi´on acotada. Luego, {xn} tiene al menos un punto de acumulaci´on._ 

_Demostraci´on._ Como la sucesi´on est´a acotada, existen _a, b ∈_ R tal que _xn ∈_ [ _a, b_ ] para todo _n ∈_ N. Luego, el conjunto _{n ∈_ N : _xn ∈_ [ _a, b_ ] _}_ es infinito. 

Procederemos usando el M´etodo dicotomico. En este caso lo aplicaremos para obtener una sucesi´on de intervalos. 

Consideremos [ _a, b_ ] = [ _a_ 1 _, b_ 1]]. Obtenido el intervalo [ _an, bn_ ], construimos el intervalo [ _an_ +1 _, bn_ +1], tomando el punto medio _cn_ +1 de [ _an, bn_ ] (i.e. _cn_ +1 =<sup>_<u>an</u>_</sup><sup><u>+</u></sup> 2<sup>_<u>bn</u>_</sup> ), y tenemos que al menos uno de los conjuntos _{n ∈_ N : _xn ∈_ [ _an, cn_ +1] _}_ o _{n ∈_ N : _xn ∈_ [ _cn_ +1 _, bn_ ] _}_ es infinito. Si _{n ∈_ N : _xn ∈_ [ _an, cn_ +1] _}_ es infinito definimos [ _an_ +1 _, bn_ +1] = [ _an, cn_ +1], y en caso contrario definimos [ _an_ +1 _, bn_ +1] = [ _cn_ +1 _, bn_ ]. Observemos que ahora que el conjunto _{n ∈_ N : _xn ∈_ [ _an_ +1 _, bn_ +1] _}_ es infinito. 

De esta manera, considerando los extremos de los intervalos, se obtienen dos sucesiones _{an}_ y _{bn}_ tales que: 

8 

- _1.4 Principio del punto de acumulaci´on. Teorema de Bolzano-Weierstrass._ An´alisis Matem´atico III 

   1. _{an}_ es creciente y acotada superiormente por _b_ (luego, _{an}_ es convergente), 





Sea _n_ l´ım _→_ ∞<sup>_an_=</sup><sup>_ψ_. Adem´as, por´algebra de l´ımites,</sup> 



Veamos que _ψ_ es un punto de acumulaci´on de _{xn}_ . Sea _ε >_ 0. Por lo que acabamos de probar, existe _n ∈_ N tal que [ _an, bn_ ] _⊆_ ( _ψ − ε, ψ_ + _ε_ ). En consecuencia, el conjunto _{n ∈_ N : _|xn − ψ| < ε}_ es infinito, ya que 



Luego, _ψ_ es un punto de acumulaci´on de _{xn}_ como quer´ıamos probar. 

Los siguientes dos resultados y la Proposici´on 1.4.1 que acabamos de probar son equivalentes. 

**Teorema 1.4.1** (Teorema de Bolzano-Weierstrass) **.** _Toda sucesi´on num´erica real contiene una subsucesi´on convergente._ 

**Proposici´on 1.4.2** (Principio de los Intervalos Encajados) **.** _Sean {_ [ _an, bn_ ] _} una colecci´on de intervalos cerrados y acotados de_ R _, tales que , para todo n ∈_ N _,_ [ _an_ +1 _, bn_ +1] _⊆_ [ _an, bn_ ] _. Entonces,_ 



_Si adem´as n_ l´ım _→_ ∞<sup>_bnan_= 0</sup><sup>_entonces,_</sup> 



El siguiente resultado es una consecuencia inmediata de los resultados que acabamos de mencionar. 

**Corolario 1.4.1.** _Una sucesi´on acotada y con un ´unico punto de acumulaci´on es convergente (y converge a dicho punto de acumulaci´on)._ 

_Demostraci´on._ Ejercicio 

A continuaci´on consideraremos una clase (en principio) particular de sucesiones. 

**Definici´on 1.4.2** (Sucesiones de Cauchy) **.** _Una sucesi´on {an} es de Cauchy si para todo ε >_ 0 _existe N ∈_ N _tal que_ 



**Proposici´on 1.4.3.** _Toda sucesi´on convergente es de Cauchy._ 

_Demostraci´on._ Ejercicio 

Acabamos de ver que para una sucesi´on es condici´on necesaria ser de Cauchy para ser convergente. En lo que sigue veremos que, para una sucesi´on num´erica real ser de Cauchy tambi´en es condici´on suficiente para ser convergente. 

9 

- _1.4 Principio del punto de acumulaci´on. Teorema de Bolzano-Weierstrass._ An´alisis Matem´atico III 

**Teorema 1.4.2.** _Toda sucesi´on de Cauchy es acotada y posee ´unico punto de acumulaci´on. En conclusi´on toda sucesi´on de Cauchy es convergente._ 

_Demostraci´on._ Sea _{an}_ una sucesi´on de Cauchy. Luego, tomando _ε_ = 1, existe _N_ 0 _∈_ N tal que _n, m ≥ N_ 0 _⇒|an − am| <_ 1. 

Ergo, para todo _n ≥ N_ 0, _|an| <_ 1 + _|aN_ 0 _|_ . Sea _T_ = m´ax _{|a_ 1 _|,..., |aN_ 0 _−_ 1 _|,_ 1 + _|aN_ 0 _|}_ . Tenemos que para todo _n ∈_ N, _|an| ≤ T_ , i.e. _{an}_ est´a acotada. 

Aplicando ahora el Principio del punto de acumulaci´on para sucesiones (Proposici´on 1.4.1), tenemos que la sucesi´on _{an}_ tiene al menos un punto de acumulaci´on. 

Veamos que dicho punto de acumulaci´on es ´unico. Supongamos que existen _α, β ∈_ R puntos de acumulaci´on de _{an}_ con _α̸_ = _β_ . Sea _ε_ =<sup>_<u>|β</u>−_</sup> 3<sup>_α|_</sup> . Observemos que _ε >_ 0. Como _{an}_ es de Cauchy, existe _N ∈_ N tal que si _n, m ≥ N_ entonces _|an − am| < ε_ (*). 

Dado que _α_ y _β_ son puntos de acumulaci´on, los conjuntos _A_ = _{n ∈_ N : _|an − α| < ε}_ y _B_ = _{n ∈_ N : _|an − β | < ε}_ son ambos de cardinal infinito. Luego, existen _n_ 0 _∈ A_ y _m_ 0 _∈ B_ tales que _n_ 0 _≥ N_ y _m_ 0 _≥ N_ , i.e. _|α − an_ 0 _| < ε_ y _|am_ 0 _− β | < ε_ . 

Entonces, 



En consecuencia, 



Es decir, _|an_ 0 _− am_ 0 _| > ε_ , lo cual contradice (*). Esta contradicci´on proviene de suponer que existen dos puntos de acumulaci´on diferentes. En consecuencia el punto de acumulaci´on es ´unico y el teorema queda demostrado 

**Ejemplo 1.4.2.** _Sea a, b ∈_ R _. Consideremos la sucesi´on {an} definida como a_ 1 = _a, a_ 2 = _b, an_ =<sup>_an−_</sup><sup><u>1</u></sup><sup>_−_</sup> 2<sup>_an−_</sup><sup><u>2</u></sup> _si n ≥_ 3 _. Tenemos que_ [ _an_ +2 _, an_ +1] _⊂_ [ _an_ +1 _, an_ ] _. M´as a´un, para n ≥_ 3 _,_ 



_En consecuencia,_ 



_Esto implica que la sucesi´on {an} es de Cauchy en_ R _y por lo tanto es convergente. Observemos que determinamos que la sucesi´on es convergente, sin necesidad de conocer el valor al cual converge._ 

10 

An´alisis Matem´atico III 

## **2. Series num´ericas** 

### **2.1. Definici´on y ejemplos** 

Consideremos una secuencia num´erica _{an}_ real o compleja. Podemos formar la _sumas parciales_ 



La sucesi´on de sumas parciales _{sn}_ se denomina _serie infinita_ , o simplemente _serie_ , que tambi´en se nota: 



∞ Por ejemplo, la serie ∑ <u>1</u> _k_<sup>representa la sucesi´on</sup><sup>_{sn}_donde</sup> _k_ =1 



Si existe un n´umero real o complejo _S_ tal que 



decimos que la serie 



_converge_ y tiene suma _S_ , en cuyo caso escribimos 



Si _{sn}_ no converge, decimos que la serie no converge y no tiene suma. 

**Ejemplo 2.1.1.** 







11 

_2.2 Linealidad de series convergentes_ 

An´alisis Matem´atico III 

∞ **LA SERIE ARM ONICA.**<sup>**´**</sup> _Consideremos la serie arm´onica_ ∑ <u>1</u> _k_<sup>_. No es dif´ıcil ver que las sumas parcia-_</sup> _k_ =1 _les verifican_ 



∞ _Luego, como_ l´ım ∑ <u>1</u> _k_<sup>_no converge._</sup> _n→_ ∞<sup>ln(</sup><sup>_n_+1) = ∞</sup><sup>_, lo mismo ocurre con sn y por lo tanto la serie_</sup> _k_ =1 

### **2.2. Linealidad de series convergentes** 

A partir de las igualdades conocidas para suma de una cantidad finita de t´erminos 



surge la siguiente extensi´on de estas igualdades a series. 

**Teorema 2.2.1.** _Sean_ ∑<sup>∞</sup> _k_ =1<sup>_ak y_∑∞</sup> _k_ =1<sup>_bk series convergentes y α y βconstantes. Luego, la serie_∑∞</sup> _k_ =1<sup>(</sup><sup>_αak_+</sup> _β bk_ ) _converge y verifica_ 



_Demostraci´on._ Ejercicio 

**Corolario 2.2.1.** _Si_ ∑<sup>∞</sup> _k_ =1<sup>_akconverge y_∑∞</sup> _k_ =1<sup>_bkno converge, entonces_∑∞</sup> _k_ =1<sup>(</sup><sup>_ak_+</sup><sup>_bk_)</sup><sup>_no converge._</sup> 

_Demostraci´on._ Ejercicio. 

**Ejemplo 2.2.1.** _1. La serie_ ∑<sup>∞</sup> _k_ =1<sup>(</sup><sup><u>1</u></sup> _k_<sup>+</sup> 2<sup><u>1</u></sup><sup>_k_)</sup><sup>_no converge ya que_∑</sup> _k_<sup>∞</sup> =1 <u>1</u> _k_<sup>_no converge y_∑</sup> _k_<sup>∞</sup> =1 21<sup>_kconverge._</sup> _2. Si dos series no convergen, no necesariamente la serie suma no converge. Por ejemplo, las series_ ∑<sup>∞</sup> _k_ =1 <u>1</u> _k_<sup>_y_∑</sup> _k_<sup>∞</sup> =1<sup>_−_</sup><sup><u>1</u></sup> _k_<sup>_no convergen pero la serie_∑</sup> _k_<sup>∞</sup> =1<sup>(</sup><sup><u>1</u></sup> _k_<sup>+ (</sup><sup>_−_</sup><sup><u>1</u></sup> _k_<sup>))</sup><sup>_converge, m´as a´un su suma es_0</sup><sup>_ya_</sup> _que todos sus t´erminos son nulos._ 

### **2.3. Series telesc´opicas** 

Consideremos una sucesi´on _{bn}_ y observemos que las siguientes sumas parciales verifican 



Intentemos extender esta propiedad a series infinitas. Consideremos _an_ = _bn − bn_ +1 para _n ∈_ N. Luego, la serie ∑<sup>∞</sup> _k_ =1<sup>_ak_se denomina</sup><sup>_serie telesc´opica_.</sup> 

12 

_2.4 La serie geom´etrica_ 

An´alisis Matem´atico III 

**Teorema 2.3.1.** _Sean {an} y {bn} dos sucesiones tales que an_ = _bn − bn_ +1 _para n ∈_ N _. La serie_ ∑<sup>∞</sup> _k_ =1<sup>_ak_</sup> _converge si y solo si la sucesi´on {bn} converge. M´as a´un,_ 



_donde ℓ_ = _n_ l´ım _→_ ∞<sup>_bn._</sup> 

_Demostraci´on._ Ejercicio. 



_Considerando bn_ = _n_<sup><u>1</u></sup><sup>_en el teorema anterior, resulta_</sup> 





### **2.4. La serie geom´etrica** 

Consideremos las sumas parciales 



Si _x_ = 1, _sn_ = _n_ y como ya hemos visto, la serie no converge. Consideremos ahora _x̸_ = 1, luego 



Ergo, 



∞ En consecuencia, si _|x| <_ 1, _x_<sup>_n_</sup> _→_ 0. Por lo tanto, si _|x| <_ 1, ∑ _x_<sup>_k_</sup> = 1 _−_ <u>1</u> _x_<sup>.Adem´as,si</sup><sup>_|x| >_1,como</sup> _k_ =0 _|x_<sup>_n_</sup> _| →_ +∞, la sucesi´on no converge y entonces la serie no converge. En conclusi´on, tenemos el siguiente resultado 

∞ **Proposici´on 2.4.1.** _Sea x ∈_ C _. Luego,_ ∑ _x_<sup>_k_</sup> _converge si y solo si |x| <_ 1 _. k_ =0 

**Nota 2.4.1.** _1. Si reemplazamos en la serie geom´etrica x por x_<sup>2</sup> _, tenemos que si |x| <_ 1 _,_ 



13 

_2.5 Tests de convergencia_ 

An´alisis Matem´atico III 

_2. Multiplicando en la igualdad anterior ambos lados por x, se tiene que si |x| <_ 1 _,_ 



_3. Reemplazando x por −x en la serie geom´etrica, si |x| <_ 1 _resulta_ 



_4. Reemplazando en lo anterior x por x_<sup>2</sup> _, si |x| <_ 1 



_5. Multiplicando ambos lados de la igualdad anterior por x, si |x| <_ 1 _resulta_ 



_6. Sustituyendo x por_ 2 _x en la serie geom´etrica, tenemos que si |_ 2 _x| <_ 1 _, i.e. si |x| <_<sup><u>1</u></sup> 2<sup>_,_</sup> 



_7. Todas estas series tienen la forma general_ 



_donde para k ∈_ N0 _, ak son los coeficientes (reales o complejos). Este tipo de series se denominan_ series de potencias _._ 

### **2.5. Tests de convergencia** 

En esta secci´on veremos condiciones suficientes y/o necesarias para la convergencia de una serie. 



_Demostraci´on._ La demostraci´on sigue de observar que _an_ = _sn − sn−_ 1 y calcular el l´ımite para _n →_ ∞. 

**Nota 2.5.1.** _Observemos que la implicaci´on rec´ıproca del resultado anterior no es cierta, ya que {_<sup><u>1</u></sup> _n_<sup>_} es_</sup> _una sucesi´on convergente, pero la serie_ ∑ _n_<sup><u>1</u></sup><sup>_no converge, como ya hemos visto._</sup> 

**Teorema 2.5.2.** _[Test para series de t´erminos no negativos] Sea an ≥_ 0 _para todo n ∈_ N _. Luego, la serie_ ∑ _an converge si y solo si la sucesi´on de sumas parciales est´a acotada._ 

_Demostraci´on._ El resultado surge inmediatamente del Teorema 1.3.2 aplicado a la sucesi´on de sumas parciales. 

14 

_2.5 Tests de convergencia_ 

An´alisis Matem´atico III 

∞ **Ejemplo 2.5.1.** _Consideremos la serie_ ∑ _k_ <u>1!</u><sup>_. Observemos que si k ∈_N</sup><sup>_,_</sup> _k_<sup><u>1</u></sup> !<sup>_≤_</sup> 2<sup>_k_</sup> <u>1</u><sup>_−_1</sup><sup>_. Por lo tanto,_</sup> _k_ =1 



**Teorema 2.5.3.** _Sean an ≥_ 0 _y bn ≥_ 0 _para todo n ∈_ N _. Si existe una constante c >_ 0 _tal que an ≤ cbn para todo n ∈_ N _, entonces la convergencia de_ ∑ _bn implica la convergencia de la serie_ ∑ _an._ 

_Demostraci´on._ Sea _S_ = ∑ _bn_ . Luego, _sn_ = _a_ 1 + _a_ 2 + _···_ + _an ≤ cS_ para todo _n ∈_ N. Aplicando ahora el Teorema 2.5.2 a la sucesi´on de t´erminos no negativos ∑ _an_ surge que esta serie es convergente. 

**Teorema 2.5.4.** _[Test de comparaci´on de l´ımites] Sean an >_ 0 _y bn >_ 0 _para todo n ∈_ N _. Si_ 



_(se dice que estas sucesiones son asint´oticamente iguales) entonces_ ∑ _an converge si y solo si_ ∑ _bn converge._ 

_Demostraci´on._ Como _n_ l´ım _→_ ∞ _<u>abnn</u>_<sup>= 1,existe</sup><sup>_N_talquesi</sup><sup>_n ≥N_entonces</sup> 2<sup><u>1</u></sup><sup>_<_</sup><sup>_<u>a</u>_</sup> _b_<sup>_<u>n</u>_</sup> _n_<sup>_<_</sup> 2<sup><u>3</u>.Porlotanto,</sup><sup>_n ≥N_</sup> entonces _bn <_ 2 _an_ y _an <_ 2<sup><u>3</u></sup><sup>_bn_. Aplicando el Teorema 2.5.3 usando ambas desigualdades surge el resultado</sup> deseado. 

**Teorema 2.5.5.** _[Test de la integral] Sea f una funci´on positiva decreciente definida en_ [1 _,_ +∞) _. Para cada n ∈_ N _, sean_ 



_Luego, ambas sucesiones {sn} y {tn} son convergentes o ambas son divergentes a_ +∞ _._ 

_Demostraci´on._ Observemos que 



i.e. _sn − f_ (1) _≤ tn ≤ sn−_ 1. 

Como las sucesiones _{sn}_ y _{tn}_ son ambas crecientes, estas desigualdades implican que ambas son acotadas o ambas son no acotadas. Ergo, ambas sucesiones convergen o ambas divergen a +∞. 

**Ejemplo 2.5.2.** _Consideremos, dado s ∈_ R _, la serie_ 



_Si s ≤_ 0 _, la sucesi´on { n_<sup><u>1</u></sup><sup>_<u>s</u>} no converge a_0</sup><sup>_, y por lo tanto la serie no converge._</sup> 

15 

_2.5 Tests de convergencia_ 

An´alisis Matem´atico III 

_Tomemos f_ ( _x_ ) = _x_<sup>_−s_</sup> = _x_<sup><u>1</u></sup><sup>_<u>s</u>para x ≥_1</sup><sup>_y s >_0</sup><sup>_. Resulta_</sup> 



_Si s >_ 1 _, n_ l´ım _→_ ∞<sup>_n_1</sup><sup>_−s_= 0</sup><sup>_y por lo tanto la sucesi´on {tn} converge. Aplicando el test de la integral obtenemos_</sup> ∞ _que si s >_ 1 _la serie_ ∑ _k_ <u>1</u><sup>_<u>s</u>es convergente._</sup> _k_ =1 



**Teorema 2.5.6.** _[Test de la ra´ız] Sea_ ∑ _an una serie de t´erminos no negativos tal que_ 



_1. Si R <_ 1 _, entonces la serie_ ∑ _an converge._ 

_2. Si R >_ 1 _, entonces la serie_ ∑ _an no converge._ 

_3. Si R_ = 1 _, este criterio no determina la naturaleza de la serie_ ∑ _an._ 



_Demostraci´on._ 1. Supongamos _R <_ 1. Sea _x_ tal que _R < x <_ 1. Luego, dado que _n_ l´ım _→_ ∞<sup>_a_</sup> _nn_ = _R_ , existe _N ∈_ 

<u>1</u> N tal que si _n ≥ N_ entonces _ann < x_ , i.e. _an < xn_ . En consecuencia, aplicando el test de comparaci´on con la serie ∑ _x_<sup>_n_</sup> surge que la serie ∑ _an_ converge, ya que _x <_ 1. 

2. Si _R >_ 1, existe _N ∈_ N tal que si _n ≥ N_ entonces _an >_ 1. Por lo tanto la sucesi´on _{an}_ no converege a 0, lo que implica que la serie ∑ _an_ no converge. 

- <u>1</u> 

- 3. Si _R_ = 1, observemos que considerando _an_ =<sup><u>1</u></sup> _n_<sup>y</sup><sup>_an_=</sup> _n_<sup><u>12</u>, tenemos que en ambos casos</sup> _n_<sup>l´ım</sup> _→_ ∞<sup>_a_</sup> _nn_ = 1. Sin embargo, como ya hemos visto, la serie ∑ _n_<sup><u>1</u>no converge y la serie ∑</sup> _n_<sup><u>12</u>converge.</sup> 



∞ _Como_<sup><u>1</u></sup> _e_<sup>_<_1</sup><sup>_, del Test de la ra´ız surge que la serie_</sup> ∑ � _n_ + _<u>n</u>_ 1� _n_ 2 _es convergente. k_ =1 

**Teorema 2.5.7.** _[Test del cociente] Sea_ ∑ _an una serie de t´erminos positivos tal que_ 



_1. Si R <_ 1 _, entonces la serie_ ∑ _an converge._ 

_2. Si R >_ 1 _, entonces la serie_ ∑ _an no converge._ 

16 

_2.5 Tests de convergencia_ 

An´alisis Matem´atico III 

_3. Si R_ = 1 _, este criterio no determina la naturaleza de la serie_ ∑ _an._ 

_Demostraci´on._ 1. Supongamos _R <_ 1. Sea _x_ tal que _R < x <_ 1. Luego, dado que _n_ l´ım _→_ ∞ _aan_ <u>+</u> _n_ <u>1</u><sup>=</sup><sup>_R_, existe</sup> _N ∈_ N tal que si _n ≥ N_ entonces<sup>_a_</sup> _a_<sup>_<u>n</u>_</sup><sup><u>+</u></sup> _n_<sup><u>1</u></sup><sup>_< x_, dividiendo en ambos lados por</sup><sup>_xn_+1 resulta</sup><sup>_a_</sup> _x_<sup>_nn_++11</sup><sup>_<_</sup><sup>_<u>a</u>_</sup> _x_<sup>_<u>nn</u>_.</sup> Luego, la sucesi´on<sup>_<u>a</u>_</sup> _x_<sup>_<u>nn</u>_es decreciente para</sup><sup>_n ≥N_. Por lo tanto, si</sup><sup>_n ≥N_,</sup><sup>_<u>a</u>_</sup> _x_<sup>_<u>nn</u>≤_</sup><sup>_<u>a</u>_</sup> _x_<sup>_NN_, i.e.</sup> 



Luego la serie ∑ _an_ est´a dominada por la serie convergente ∑ _x_<sup>_n_</sup> , lo que implica que ∑ _an_ es convergente. 

2. Si _R >_ 1, existe _N ∈_ N tal que si _n ≥ N_ entonces<sup>_a_</sup> _a_<sup>_<u>n</u>_</sup><sup><u>+</u></sup> _n_<sup><u>1</u></sup><sup>_>_1, i.e.</sup><sup>_an_+1</sup><sup>_> an_. Por lo tanto la sucesi´on</sup> _{an}_ es estrictamente creciente y cada t´ermino es positivo, lo que implica que no converge a 0. Ergo, la serie ∑ _an_ no converge. 



**Ejemplo 2.5.4.** _Consideremos la serie_ ∑ _n_<sup>_<u>nn</u>_</sup><sup><u>!</u></sup><sup>_. Tenemos que_</sup> 



_Como_<sup><u>1</u></sup> _e_<sup>_<_1</sup><sup>_, del Test del cociente surge que la serie_∑</sup> _n_<sup>_<u>nn</u>_</sup><sup><u>!</u></sup><sup>_es convergente._</sup> 

17 

_2.6 Series alternantes_ 

An´alisis Matem´atico III 

### **2.6. Series alternantes** 

**Definici´on 2.6.1.** _Llamamos serie alternante (o alternada) a una serie que alterna t´erminos positivos y negativos, i.e. a una serie de la forma_ 



_donde para todo k ∈_ N _, ak >_ 0 

Algunos ejemplos de series alternantes que ya hemos mencionado son, para _|x| <_ 1, 



y 



Veamos algunos resultados sobre este tipo de series. 

**Teorema 2.6.1.** _[Regla de Leibniz] Sea {an} una sucesi´on mon´otona decreciente con l´ımite_ 0 _. Luego, la_ ∞ _serie_ ∑ ( _−_ 1)<sup>_k−_1</sup> _ak converge. Adem´as, si S es la suma de la serie y sn es la n-´esima suma parcial, se k_ =1 _verifica que_ 



_para todo n ∈_ N _._ 

_Demostraci´on._ Observemos que las sumas parciales _s_ 2 _n_ forman una sucesi´on creciente ya que _s_ 2 _n_ +2 _− s_ 2 _n_ = _a_ 2 _n_ +1 _− a_ 2 _n_ +2 _>_ 0. Similarmente, la sucesi´on _s_ 2 _n−_ 1 es decreciente. Adem´as, ambas sucesiones est´an acotadas inferiormente por _s_ 2 y superiormente por _s_ 1. Luego, ambas sucesiones son mon´otonas y acotadas, por lo que son convergentes. Sean _n_ l´ım _→_ ∞<sup>_s_2</sup><sup>_n_=</sup><sup>_S′_y</sup> _n_<sup>l´ım</sup> _→_ ∞<sup>_s_2</sup><sup>_n−_1 =</sup><sup>_S′′_. Vemos que</sup><sup>_S′_=</sup><sup>_S′′_, ya que,</sup> 



Sea _S_ = _S_<sup>_′_</sup> = _S_<sup>_′′_</sup> . Como _n_ l´ım _→_ ∞<sup>_s_2</sup><sup>_n_=</sup> _n_<sup>l´ım</sup> _→_ ∞<sup>_s_2</sup><sup>_n−_1 =</sup><sup>_S_,entonces</sup> _n_<sup>l´ım</sup> _→_ ∞<sup>_sn_=</sup><sup>_S_(probarlo).Apartirdelcreci-</sup> miento de _s_ 2 _n_ y el decrecimiento de _s_ 2 _n−_ 1 tenemos que _s_ 2 _n < s_ 2 _n_ +2 _≤ S_ y _S ≤ s_ 2 _n_ +1 _< s_ 2 _n−_ 1 para todo _n ∈_ N. En consecuencia, 



y 



Estas dos desigualdades derivan en la desigualdad 



enunciada en el teorema. 

18 

_2.7 Convergencia condicional y absoluta_ 

An´alisis Matem´atico III 

- **Ejemplo 2.6.1.** _1. Observemos que la sucesi´on { n_<sup><u>1</u></sup><sup>_}esdecrecienteyconvergea_0</sup><sup>_.Luego,aplicando_</sup> _la Regla de Leibniz surge que la serie arm´onica alternante_ 1 _−_<sup><u>1</u></sup> 2<sup>+</sup><sup><u>1</u></sup> 3<sup>_−_</sup> 4<sup><u>1</u>+</sup><sup>_...esconvergente._</sup> _Recordemos que la serie arm´onica_ 1 +<sup><u>1</u></sup> 2<sup>+</sup><sup><u>1</u></sup> 3<sup>+</sup><sup><u>1</u></sup> 4<sup>+</sup><sup>_...no es convergente._</sup> 

   - ∞ 

   - _2. Observemos que la serie alternante_ ∑ ( _−_ 1)<sup>_k_ln</sup> _k_<sup><u>(</u></sup><sup>_k_</sup><sup><u>)</u></sup> _es convergente. Vemos que la sucesi´on_<sup>ln</sup> _k_<sup><u>(</u></sup><sup>_k_</sup><sup><u>)</u></sup> _es k_ =1 

   - _decreciente y convergente a_ 0 _(esto puede probarse considerando la funci´on f_ ( _x_ ) =<sup>ln</sup> _x_<sup><u>(</u></sup><sup>_x_</sup><sup><u>)</u></sup> _para x ≥_ 1 _y aplicando propiedades de las sucesiones)._ 

### **2.7. Convergencia condicional y absoluta** 

Hemos visto que la serie arm´onica alternante 1 _−_ 2<sup><u>1</u>+</sup><sup><u>1</u></sup> 3<sup>_−_</sup> 4<sup><u>1</u>+</sup><sup>_..._es convergente, mientras que la serie</sup> obtenida considerando los valores absolutos de cada t´ermino es la serie arm´onica, que no es convergente. Es decir, la convergencia de una serie no implica necesariamente la convergencia de la serie de sus valores absolutos. Veamos ahora qu´e ocurre en la direcci´on contraria. 

**Teorema 2.7.1.** _Si la serie_ ∑ _|ak| converge entonces la serie_ ∑ _ak converge y vale que_ 



_Demostraci´on._ Supongamos primero que _ak ∈_ R para todo _k ∈_ N. Sea _bk_ = _ak_ + _|ak|_ . Si probamos que la serie ∑ _bk_ converge, del Teorema 2.2.1 surge que la serie ∑ _ak_ converge. 

De la definici´on tenemos que _bk_ = 0 o _bk_ = 2 _ak_ , luego 0 _≤ bk ≤_ 2 _|ak|_ . Entonces la serie ∑ _|ak|_ domina a la serie ∑ _bk_ , y del Teorema 2.5.3 surge que ∑ _bk_ es convergente. 

Consideremos ahora que los t´erminos _ak_ son complejos. Sea _ak_ = _uk_ + _ivk_ donde _uk_ y _vk_ son reales. Como 0 _≤|uk| ≤|ak|_ , la convergencia de ∑ _|ak|_ implica la convergencia de ∑ _|uk|_ . Luego, como los t´erminos _uk_ son reales, de lo probado antes tenemos que la serie ∑ _uk_ es convergente. De manera similar se prueba que la serie ∑ _vk_ es convergente. Luego, por linealidad concluimos que la serie ∑ _ak_ = ∑ _uk_ + _ivk_ es convergente. 



**Definici´on 2.7.1.** _Una serie_ ∑ _ak se dice absolutamente convergente si_ ∑ _|ak| es convergente. Si_ ∑ _ak es convergente pero_ ∑ _|ak| no es convergente, la serie_ ∑ _ak se dice condicionalmente convergente._ 

Por ejemplo, la serie arm´onica alternante 1 _−_<sup><u>1</u></sup> 2<sup>+</sup><sup><u>1</u></sup> 3<sup>_−_</sup><sup><u>1</u></sup> 4<sup>+</sup><sup>_..._es condicionalmente convergente.</sup> 

### **2.8. Tests de Dirichlet y Abel** 

**Teorema 2.8.1.** _[Sumas parciales de Abel] Sean {ak} y {bk} dos sucesiones de n´umeros complejos. Conn sideremos An_ = ∑ _ak. Entonces, se verifica la identidad k_ =1 



19 

_2.8 Tests de Dirichlet y Abel_ 

An´alisis Matem´atico III 

_Demostraci´on._ Si consideramos _A_ 0 = 0, resulta _ak_ = _Ak − Ak−_ 1 para todo _k ∈_ N. Ergo, 



**Teorema 2.8.2.** _[Test de Dirichlet] Sea_ ∑ _ak una serie de t´erminos complejos tal que sus sumas parciales forman una sucesi´on acotada. Sea {bn} una secuencia decreciente que converge a_ 0 _. Entonces la serie_ ∑ _akbk es convergente._ 

_Demostraci´on._ Sean _An_ como en el Teorema 2.8.1 anterior. Luego, existe _M >_ 0 tal que _|An| ≤ M_ para todo _n ∈_ N. Entonces la sucesi´on _Akbk_ +1 converge a 0 (“acotada por una que tiende a 0”). Para ver la convergencia de ∑ _akbk_ , en virtud del Teorema 2.8.1 es suficiente probar que la serie ∑ _Ak_ ( _bk − bk_ +1) es convergente. 

Dado que _{bk}_ es decreciente tenemos 



Como la serie ∑ _bk − bk_ +1 es telesc´opica y la sucesi´on _{bk}_ es convergente, del Teorema 2.3.1 surge que la serie ∑ _bk − bk_ +1 es convergente. Adem´as, por la desigualdad anterior, esta serie domina a la serie ∑ _|Ak_ ( _bk − bk_ +1) _|_ . En consecuencia la serie ∑ _Ak_ ( _bk − bk_ +1) es absolutamente convergente y por lo tanto, del Teorema 2.7.1, la serie ∑ _Ak_ ( _bk − bk_ +1) es convergente. 

**Teorema 2.8.3.** _[Test de Abel] Sea_ ∑ _ak una serie de t´erminos complejos y {bn} una sucesi´on mon´otona convergente de t´erminos reales. Entonces la serie_ ∑ _akbk es convergente._ 

_Demostraci´on._ Usamos nuevamente la notaci´on del Teorema 2.8.1. La convergencia de la serie ∑ _ak_ implica la convergencia de la sucesi´on _{Ak}_ , y esto ´ultimo la convergencia de la sucesi´on _{Akbk_ +1 _}_ , ya que por hip´otesis _{bk}_ es convergente. Adem´as, _{Ak}_ es una sucesi´on acotada. Ahora, el resto de la demostraci´on es an´aloga a la que acabamos de ver en el Teorema 2.8.2. 

Para aplicar el Test de Dirichlet necesitamos series con sumas parciales acotadas. Es claro que una serie convergente tiene sus sumas parciales acotadas. Un ejemplo interesante de serie no convergente con sumas parciales acotadas es la serie geom´etrica ∑ _x_<sup>_k_</sup> con _x_ compleja tal que _|x|_ = 1 y _x̸_ = 1. Si _|x|_ = 1 notamos _x_ = _e_<sup>2</sup><sup>_iθ_</sup> con _θ ∈_ R. 

**Teorema 2.8.4.** _Sea θ ∈_ R _distinto de un m´ultiplo entero de π. Entonces, se verifica la igualdad_ 



_Adem´as,_ 



_Demostraci´on._ Si _x̸_ = 0, las sumas parciales de la serie geom´etrica es 



20 

_2.9 Reordenamiento de series_ 

An´alisis Matem´atico III 

Tomando _x_ = _e_<sup>2</sup><sup>_iθ_</sup> ( _θ ∈_ R diferente de un m´ultiplo entero de _π_ ), se tiene 



Finalmente, la desigualdad surge observando que _|_ sen( _nθ_ ) _| ≤_ 1 y _|e_<sup>_i_(</sup><sup>_n_+1)</sup><sup>_θ_</sup> _|_ = 1. 

**Ejemplo 2.8.1.** _Sea {bk} una sucesi´on decreciente de n´umeros reales, con l´ımite_ 0 _. Considerando ak_ = _x_<sup>_k_</sup> _en el Test de Dirichlet, donde x es compleja tal que |x|_ = 1 _y x̸_ = 1 _, resulta que la serie_ 



_es convergente. Notar que la Regla de Leibniz sigue simplemente de considerar x_ = _−_ 1 _._ 

_Tomemos ahora x_ = _e_<sup>_iθ_</sup> _, donde θ ∈_ R _es diferente de un m´ultiplo entero de_ 2 _π y tomemos las partes real e imaginaria en la serie anterior. Deducimos entonces que las series_ 



_son convergentes._ 

_En particular, si bk_ = _k_<sup><u>1</u></sup><sup>_<u>s</u>con s >_0</sup><sup>_, las series_</sup> 



_son convergentes. M´as a´un, si s >_ 1 _las series son absolutamente convergentes ya que est´an dominadas_ ∞ _por_ ∑ _k_ <u>1</u><sup>_<u>s</u>._</sup> _k_ =1 

### **2.9. Reordenamiento de series** 

Sabemos que la suma de un n´umero finito de t´erminos no se altera si modificamos el orden en que los sumamos, ya que la suma es conmutativa. Veamos qu´e ocurre en el caso de series. 

Primero, enunciamos un resultado que nos permite afirmar que si la serie es absolutamente convergente entonces su suma no se modifica si alteramos el orden de los t´erminos de la serie. Para esto, definamos primero qu´e entendemos por reordenamiento de una serie. 

**Definici´on 2.9.1.** _Sea f_ : N _�→_ N _una funci´on biyectiva. A tal funci´on se la denomina permutaci´on (de_ N _). Si_ ∑ _ak y_ ∑ _bk son dos series tales que para todo k ∈_ N 



_para alguna permutaci´on f, entonces la serie_ ∑ _bk es un reordenamiento de la serie_ ∑ _ak._ 

**Teorema 2.9.1.** _Sea_ ∑ _ak una serie absolutamente convergente con suma S. Entonces, todo reordenamiento de_ ∑ _ak es absolutamente convergente y tiene suma S._ 

21 

_2.9 Reordenamiento de series_ An´alisis Matem´atico III 

Ahora bien, surge naturalmente analizar si la condici´on de convergencia absoluta puede relajarse, i.e. ¿qu´e ocurre con una serie condicionalmente convergente? 

Veremos que una serie condicionalmente convergente de t´erminos reales puede reordenarse de forma tal que su suma sea cualquier n´umero real preestablecido. 

Dada una serie ∑ _ak_ definimos dos nuevas series ∑ _a_<sup>+</sup> _k_<sup>y ∑</sup><sup>_a_</sup> _k_<sup>_−_obtenidas tomando solamente los t´ermi-</sup> nos positivos y solamente los t´erminos negativos, respectivamente. De esta forma, ser´an 



Observemos que si _ak_ es positivo, entonces _a_<sup>+</sup> _k_<sup>=</sup><sup>_ak_y</sup><sup>_a_</sup> _k_<sup>_−_= 0, y si</sup><sup>_ak_es negativo, entonces</sup><sup>_a_</sup> _k_<sup>_−_=</sup><sup>_ak_y</sup> _a_<sup>+</sup> _k_<sup>= 0.</sup> 

**Teorema 2.9.2.** _Sean_ ∑ _ak una serie de t´erminos reales y a_<sup>+</sup> _k_<sup>_y a−_</sup> _k_<sup>_como acabamos de definir._</sup> _1. Si_ ∑ _ak es condicionalmente convergente, las series_ ∑ _a_<sup>+</sup> _k_<sup>_y_∑</sup><sup>_a−_</sup> _k_<sup>_no convergen._</sup> 

_2. Si_ ∑ _ak es absolutamente convergente, las series_ ∑ _a_<sup>+</sup> _k_<sup>_y_∑</sup><sup>_a−_</sup> _k_<sup>_convergen y vale_</sup> 



- _Demostraci´on._ 1. Observemos que las serie ∑<sup><u>1</u></sup> 2<sup>_ak_converge y ∑</sup><sup><u>1</u></sup> 2<sup>_|ak|_no converge. En consecuencia,</sup> aplicando el Corolario 2.2.1 obtenemos que las series ∑ _a_<sup>+</sup> _k_<sup>y ∑</sup><sup>_a−_</sup> _k_<sup>no convergen.</sup> 

   2. Las series ∑ 2<sup><u>1</u></sup><sup>_ak_y∑</sup><sup><u>1</u></sup> 2<sup>_|ak|_convergen.Luego,delTeorema2.2.1obtenemosquelasseries∑</sup><sup>_a_</sup> _k_<sup>+y</sup> ∑ _a_<sup>_−_</sup> _k_<sup>convergen y</sup> 



**Teorema 2.9.3.** _Sea_ ∑ _ak una serie de t´erminos reales condicionalmente convergente y sea S un n´umero real cualquiera. Luego, existe un reordenamiento_ ∑ _bk de_ ∑ _ak que converge a S_ 

_Demostraci´on._ Del Teorema anterior sabemos que ∑ _a_<sup>+</sup> _k_<sup>y∑</sup><sup>_a−_</sup> _k_<sup>divergen.Reordenamoslaserie∑</sup><sup>_ak_de</sup> la siguiente forma: Tomamos, en orden, la cantidad m´ınima de t´erminos _a_<sup>+</sup> _k_<sup>de forma tal que su suma sea</sup> mayor a _S_ . Si se requieren _p_ 1 t´erminos positivo, entonces 



Esto es posible ya que ∑ _a_<sup>+</sup> _k_<sup>tiende a +∞.</sup> 

Ahora, a esta suma agregamos la cantidad m´ınima de t´erminos negativos _a_<sup>_−_</sup> _k_<sup>(enorden),digamos</sup><sup>_n_1</sup> tal que la suma resultante sea menor a _S_ . Nuevamente, esto es posible ya que ∑ _a_<sup>_−_</sup> _k_<sup>tiende a</sup><sup>_−_∞. Resulta</sup> entonces 



Repitiendo este procedimiento (agregando la cantidad m´ınima de t´erminos positivos que sea mayor a _S_ y luego la cantidad m´ınima de t´erminos negativos tal que la suma sea menor a _S_ ) obtenemos un reordenamiento ∑ _bk_ . Vemos que cada suma parcial ∑ _bk_ difiere de _S_ en a lo sumo un t´ermino _a_<sup>+</sup> _k_<sup>o</sup><sup>_a−_</sup> _k_<sup>.</sup> Observemos que la sucesi´on _{ak}_ converge a 0 ya que por hip´otesis la serie ∑ _ak_ converge. Luego, el reordenamiento ∑ _bk_ converge y tiene suma _S_ . 

22 

An´alisis Matem´atico III 

## **3. Sucesiones y series de funciones** 

Consideremos ahora una sucesi´on de funciones _{ fn}_ de variable real con mismo dominio y con codominio en R (o C). Luego, para cada _x_ en su dominio, tenemos ahora una sucesi´on num´erica _{ fn_ ( _x_ ) _}_ correspondiente a los valores de cada _fn_ en _x_ . Sea _S_ el conjunto de puntos _x_ del dominio para los cuales esta sucesi´on converge. Es decir, tenemos una funci´on _f_ con dominio en _S_ tal que 



Esta funci´on es llamada _funci´on l´ımite_ de la sucesi´on _{ fn}_ , y se dice que la sucesi´on _{ fn}_ converge puntualmente a _f_ en _S_ . Surge preguntarse, ¿qu´e propiedades de las funciones (continuidad, derivabilidad, integrabilidad) de la sucesi´on hereda la funci´on _f_ ? 

Veamos algunos ejemplos 

**Ejemplo 3.0.1.** _1. Sean fn_ ( _x_ ) = _x_<sup>_n_</sup> _para x ∈_ [0 _,_ 1] _. Esta sucesi´on converge puntualmente a la funci´on f dada por_ 



_Notar que esta funci´on es discontinua en_ 1 _, mientras que todas las funciones fn son continuas en_ [0 _,_ 1] _._ 

_2. Sean fn_ ( _x_ ) = _nx_ (1 _− x_<sup>2</sup> )<sup>_n_</sup> _para x ∈_ [0 _,_ 1] _. Esta sucesi´on converge puntualmente a la funci´on f constante nula en el intervalo_ [0 _,_ 1] _._ 

_Observemos que_ 



Acabamos de ver que algunas de las propiedades mencionadas no pueden “pasar” directamente al l´ımite puntual de las funciones. Veremos un criterio de convergencia m´as fuerte que el puntual, el cual nos permitir´a heredar a la funci´on l´ımite estas propiedades. 

### **3.1. Convergencia uniforme** 

**Definici´on 3.1.1.** _Una sucesi´on de funciones { fn} converge uniformemente a f en un conjunto S si, dado ε >_ 0 _, existe N tal que si n ≥ N entonces_ 



_Notaci´on:_ 

_f → f uniformemente en S._ 

Observemos que el valor de _N_ solo dende de _ε_ y no depende de _x_ . 

23 

_3.1 Convergencia uniforme_ 

An´alisis Matem´atico III 

**Teorema 3.1.1.** _Supongamos que fn → f uniformemente en un intervalo S. Si fn es continua p ∈ S para todo n ∈_ N _, entonces f es continua en p._ 

_Demostraci´on._ Probaremos que dado _ε >_ 0, existe _δ >_ 0 tal que si _|x − p| < δ_ y _x ∈ S_ entonces _| f_ ( _x_ ) _− f_ ( _p_ ) _| < ε_ . 

Sea _ε >_ 0. De la convergencia uniforme sabemos que existe _N_ tal que si _n ≥ N_ entonces 



Por otro lado, como _fN_ es continua en _p_ , existe _δN >_ 0 tal que si _|x − p| < δN_ y _x ∈ S_ , entonces 



Sea _δ_ = _δN_ . Luego, si _|x − p| < δ_ y _x ∈ S_ entonces 



como quer´ıamos probar. 

Consideremos una sucesi´on de funciones _uk_ y sean _fn_ la suma parcial _n_ -´esima de las _uk_ , i.e. 



Si _fn → f_ puntualmente en _x ∈ S_ , tenemos que 



∞ para cada _x ∈ S_ . En este caso decimos que la serie ∑ _uk_ ( _x_ ) converge puntualmente a _f_ en _S_ . _k_ =1 

∞ De la misma forma, si _fn → f_ uniformemente en _S_ , decimos que la serie ∑ _uk_ ( _x_ ) converge uniforme- _k_ =1 

mente a _f_ en _S_ . 

Observemos que si las _uk_ son todas continuas en un punto _p ∈ S_ , entonces cada _fn_ es continua en _p ∈ S_ . Luego, aplicando el teorema anterior a la sucesi´on de sumas parciales _fn_ se tiene el siguiente resultado. 

∞ **Teorema 3.1.2.** _Si una serie de funciones_ ∑ _uk_ ( _x_ ) _converge uniformemente a f en S y cada uk es continua k_ =1 

_en un punto p ∈ S, entonces f es continua en p._ 

Veamos ahora qu´e ocurre con la integraci´on en el caso de la converegncia uniforme. 

**Teorema 3.1.3.** _Supongamos que fn → f uniformemente en un intervalo_ [ _a, b_ ] _y cada fn es continua en_ [ _a, b_ ] _. Sean, para cada n ∈_ N _,_ 



24 

_3.1 Convergencia uniforme_ 

An´alisis Matem´atico III 



_Entonces, gn → g uniformemente en_ [ _a, b_ ] _, i.e._ 



_Demostraci´on._ Dado _ε >_ 0, existe _N ∈_ N tal que si _n ≥ N_ entonces 



Luego, si _x ∈_ [ _a, b_ ] y _n ≥ N_ entonces 



En consecuencia, _gn → g_ uniformemente en [ _a, b_ ]. 

**Corolario 3.1.1.** _Sea_ ∑ _uk una serie de funciones que converge uniformemente a la funci´on suma f en un intervalo_ [ _a.b_ ] _, donde cada uk es continua en_ [ _a, b_ ] _. Para x ∈_ [ _a, b_ ] _, sean_ 



_Entonces, gn → g uniformemente en_ [ _a, b_ ] _, i.e._ 



_Demostraci´on._ El resultado surge inmediatamente de aplicar el teorema anterior a la sucesi´on de sumas _n_ parciales _fn_ ( _t_ ) = ∑ _uk_ ( _t_ ). _k_ =1 

#### **3.1.1. Condici´on suficiente para convergencia uniforme** 

**Teorema 3.1.4** (Test M de Weierstrass) **.** _Sea_ ∑ _uk una serie de funciones que converge puntualmente a la funci´on f en un conjunto S. Si existe una serie num´erica convergente de t´erminos positivos tal que_ 



_entonces la serie_ ∑ _uk converge uniformemente en S._ 

_Demostraci´on._ El test de comparaci´on muestra que la serie ∑ _uk_ converge absolutamentepar cada _x ∈ S_ . Adem´as, para cada _x ∈ S_ , tenemos 



25 

_3.2 Series de potencias. C´ırculo de convergencia._ 

An´alisis Matem´atico III 

Como la serie ∑ _Mk_ converge, para todo _ε >_ 0 existe _N ∈_ N tal que si _n ≥ N_ entonces 



Luego, 



para todo _n ≥ N_ y para todo _x ∈ S_ . Por lo tanto, la serie ∑ _uk_ converge uniformemente a _f_ en _S_ . 

### **3.2. Series de potencias. C´ırculo de convergencia.** 

Una serie de la forma 



donde _z, a, ak ∈_ C para todo _k ∈_ N, es denominada _serie de potencias en z − a_ . 

Veremos que las series de potencias tienen asociado un _c´ırculo de convergencia_ , con un _radio de convergencia r_ , tal que para _z_ en el interior de dicho c´ırculo la serie resulta absolutamente convergente y si _z_ est´a fuera de este c´ırculo la serie diverge. En particular, la serie puede solo converger para _z_ = _a_ , en cuyo caso diremos que _r_ = 0, o puede converger en todo el plano complejo y en tal caso diremos que _r_ = +∞. 



<!-- Start of picture text -->
Región de<br>Región de<br>divergencia<br>convergencia<br>absoluta<br>a r<br><!-- End of picture text -->

Figura 1: C´ırculo de convergencia de radio _r_ . 

#### **Ejemplo 3.2.1.** 

_1. Consideremos la serie_ ∑<sup>_<u>z</u>_</sup> _n_<sup>_n_</sup> !<sup>_. Aplicando el criterio del cociente, para z̸_= 0</sup><sup>_, tenemos_</sup> 



_Como este cociente tiende a_ 0 _cuando n →_ ∞ _, resulta que la serie converge absolutamente para todo z̸_ = 0 _. Como tambi´en es convergente para z_ = 0 _, el radio de convergencia es r_ = +∞ _._ 

_2. Tomemos ahora la serie_ ∑ _n_<sup>2</sup> 3<sup>_n_</sup> _z_<sup>_n_</sup> _. A partir del criterio de la ra´ız, resulta_ 



_Como n_<sup>1</sup><sup>_/n_</sup> _converge a_ 1 _cuando n →_ ∞ _, entonces n_<sup>2</sup><sup>_/n_</sup> = _n_<sup>1</sup><sup>_/n_</sup> _n_<sup>1</sup><sup>_/n_</sup> _converge a_ 1 _. Luego,_ ( _n_<sup>2</sup> 3<sup>_n_</sup> _|z|_<sup>_n_</sup> )<sup>1</sup><sup>_/n_</sup> = _n_<sup>2</sup><sup>_/n_</sup> 3 _|z| converge a_ 3 _|z|, y por lo tanto la serie converge absolutamente si |z| <_<sup><u>1</u></sup> 3<sup>_y diverge si |z| >_</sup> 3<sup><u>1</u></sup><sup>_._</sup> _En consecuencia, el radio de convergencia es r_ =<sup><u>1</u></sup> 3<sup>_._</sup> 

_Observemos que esta serie diverge en todos los puntos de la frontera del c´ırculo de convergencia (z_ : _|z|_ =<sup><u>1</u></sup> 3<sup>_), ya que el t´ermino general n_23</sup><sup>_nzn tiene valor absoluto n_2</sup><sup>_, el cual no tiende a_0</sup><sup>_cuando_</sup> _n →_ ∞ _._ 

26 

_3.3 Series de Potencias reales_ 

An´alisis Matem´atico III 

_3. Consideremos ahora las series_ ∑<sup>_<u>z</u>_</sup> _n_<sup>_ny_∑</sup> _n_<sup>_<u>zn</u>_2</sup><sup>_. Aplicando el criterio del cociente surge que el radio de_</sup> _convergencia es r_ = 1 _. Observemos que la serie_ ∑<sup>_<u>z</u>_</sup> _n_<sup>_ndivergeparaz_= 1</sup><sup>_yconvergeencualquier_</sup> _otro z de la frontera. Sin embargo, la serie_ ∑ _n_<sup>_<u>zn</u>_2</sup><sup>_convergeentodalafrontera|z|_= 1</sup><sup>_,yaquepara_</sup> _estos valores de z est´a dominada por la serie_ ∑ _n_<sup><u>12</u></sup><sup>_._</sup> 

**Teorema 3.2.1.** _Sea_ ∑ _akz_<sup>_k_</sup> _una serie de potencias que converge para alg´un z_ 1 _̸_ = 0 _. Entonces:_ 

_1. La serie converge absolutamente para todo z tal que |z| < |z_ 1 _|._ 

_2. La serie converge uniformemente en todo disco circular cerrado de radio R < |z_ 1 _| con centro en_ 0 _. Demostraci´on._ Como la serie ∑ _akz_<sup>_k_</sup> 1<sup>converge, su t´ermino general</sup><sup>_akzk_</sup> 1<sup>tiende a 0 cuando</sup><sup>_n →_0. Luego,</sup> existe _N ∈_ N tal que si _n ≥ N_ entonces _|akz_<sup>_k_</sup> 1<sup>_| <_1.</sup> 

Sea _S_ un disco cerrado de radio _R < |z_ 1 _|_ . Si _z ∈ S_ y _n ≥ N_ , entonces _|z| ≤ R_ y 



con _t_ = ��� _zR_ 1 ���. 

Como 0 _< t <_ 1, la serie ∑ _akz_<sup>_k_</sup> est´a dominada por la serie ∑ _t_<sup>_k_</sup> , la cual es convergente. Del Test _M_ de Weierstrass surge que la serie ∑ _akz_<sup>_k_</sup> converge uniformemente en _S_ , lo cual demuestra el segundo item. 

De esto ´ultimo, tambi´en se deduce que la serie converge absolutamente para todo _z ∈ S_ . En consecuencia, si _|z| < |z_ 1 _|_ entonces existe _R_ tal que _|z| < R < |z_ 1 _|_ y por lo tanto _z_ est´a en el disco cerrado de radio _R_ . Luego, la serie converge absolutamente en _z_ , lo cual prueba el primer item. 

**Teorema 3.2.2** (Existencia del C´ırculo de convergencia) **.** _Sea_ ∑ _akz_<sup>_k_</sup> _una serie de potencias que converge para alg´un z_ 1 _̸_ = 0 _y diverge para alg´un z_ 2 _̸_ = 0 _. Entonces, existe r >_ 0 _tal que la serie converge absolutamente si |z| < r y diverge si |z| > r._ 

_Demostraci´on._ Sea _A_ el conjunto de todos los n´umeros positivos _|z|_ para los cuales la serie de potencias ∑ _akz_<sup>_k_</sup> converge. El conjunto _A_ es no vac´ıo ( _|z_ 1 _| ∈ A_ ) y por el Teorema 3.2.1 resulta que ning´un elemento de _A_ es mayor a _|z_ 2 _|_ . Luego, _A_ es un conjunto de n´umeros reales no vac´ıo acotado superiormente, lo que, por el Axioma del Supremo, implica que existe _r_ = _sup_ ( _A_ ). 

Evidentemente, como ning´un n´umero en _A_ es mayor a _r_ , la serie ∑ _akz_<sup>_k_</sup> diverge si _|z| > r_ . 

Es claro que _r ≥|z_ 1 _|_ . Adem´as, si _|z| < r_ , existe un n´umero _t ∈ A_ tal que _|z| < t < r_ . Como _t ∈ A_ , del Teorema 3.2.1 obtenemos que la serie ∑ _akz_<sup>_k_</sup> converge absolutamente. 

### **3.3. Series de Potencias reales** 

Estudiaremos ahora _series de potencias reales_ , i.e. series de la forma 



donde _ak, x, a ∈_ R para todo _k ∈_ N0. 

De lo visto antes, surge que existe un intervalo de convergencia, o sea, existe _r_ tal que la serie de potencias reales converge absolutamente para todo _x ∈_ ( _a − r, a_ + _r_ ) y converge uniformemente en [ _a − R, a_ + _R_ ] para todo _R_ con 0 _< R < r_ . De los resultados vistos sobre continuidad e integraci´on surge el siguiente: 

27 

_3.3 Series de Potencias reales_ 

An´alisis Matem´atico III 

**Teorema 3.3.1.** _Sea f una funci´on representada en serie de potencia reales como_ 



_en el intervalo_ ( _a − r, a_ + _r_ ) _. Entonces, f es continua en este intervalo y su integral sobre cualquier subintervalo cerrado puede calcularse integrando la serie t´ermino a t´ermino. En particular, para todo x ∈_ ( _a − r, a_ + _r_ ) _, resulta_ 



Veamos ahora qu´e ocurre en el caso de la derivaci´on t´ermino a t´ermino. 

**Teorema 3.3.2.** _Sea f una funci´on representada en serie de potencia reales como_ 



_en el intervalo de convergencia_ ( _a − r, a_ + _r_ ) _. Entonces:_ 



_2. La derivada f_<sup>_′_</sup> ( _x_ ) _existe para cada x en el intervalo de convergencia y est´a dada por_ 



_Demostraci´on._ Nuevamente, sin p´erdida de generalidad podemos asumir que _a_ = 0. 

Probaremos primero que la serie derivada converge absolutamente en ( _−r, r_ ). Sea _x ∈_ (0 _, r_ ). Consideremos _h_ tal que _x < x_ + _h < r_ (e.g. _h_ =<sup>_<u>r−</u>_</sup> 2<sup>_<u>x</u>_).Luego,lasseriespara</sup><sup>_f_(</sup><sup>_x_)ypara</sup><sup>_f_(</sup><sup>_x_+</sup><sup>_h_)sonambas</sup> absolutamente convergentes, ya que _x_ y _x_ + _h_ pertenecen al intervalo ( _−r, r_ ). En consecuencia, 



La serie de la derecha es absolutamente convergente, ya que es una combinaci´on lineal de series absolutamente convergentes. Aplicando el Teorema del Valor Medio tenemos, 



con _x < ck < x_ + _h_ . Luego, 



la cual converge absolutamente. 

∞ ∞ La serie ∑ _kakck_<sup>_k−_1</sup> no es una serie de potencias, pero domina a la serie ∑ _kakx_<sup>_k−_1</sup> (ya que _x < ck_ ), _k_ =1 _k_ =1 

por lo que esta ´ultima serie es convergente para este _x_ . Esto prueba que el radio de convergencia de la serie 

28 

_3.3 Series de Potencias reales_ 

An´alisis Matem´atico III 

∞ derivada ∑ _kakx_<sup>_k−_1</sup> es al menos _r_ . Pero, por otro lado, el radio de convergencia de la serie derivada no _k_ =1 

∞ puede exceder _r_ ya que la serie derivada domina a la serie original ∑ _akx_<sup>_k_</sup> (notar que _akx_<sup>_k_</sup> _≤ x._ ( _kakx_<sup>_k−_1</sup> )). _k_ =0 Esto prueba la parte ( _a_ ) del teorema. 

Para probar la segunda parte, consideremos _g_ la funci´on suma de la serie derivada, i.e. 



Aplicando el teorema anterior a _g_ , podemos integrar t´emino a t´ermino en el intervalo de convergencia y obtenemos, 



Como _g_ es continua, del Primer Teorema Fundamental del C´alculo surge que _f_<sup>_′_</sup> ( _x_ ) existe y es igual a _g_ ( _x_ ) para cada _x_ en el intervalo de convergencia, lo cual demuestra la parte ( _b_ ). 

29 

