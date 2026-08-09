---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\Rotura_Presa_HEC_RAS_e_IBER_y_Model_Flujo_No_Permantente_\06. Rotura Presa HEC-RAS e IBER y Model. Flujo No Permantente\DATA\Rotura de Presas\01 Información\1-Iber_BasesHidraulicas1.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]



## **Modelo de flujo bidimensional en ríos y estuarios BASES CONCEPTUALES HIDRÁULICAS EJEMPLOS** 

El modelo Iber Introducción 



<!-- Start of picture text -->
Turbillon  CARPA<br>GiD<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











El modelo Iber Introducción 



<!-- Start of picture text -->
Módulos de cálculo<br>HIDRODINÁMICA<br>Velocidad<br>Calado<br>TRANSPORTE DE SEDIMENTOS  TURBULENCIA<br>Carga en suspensión  Viscosidad turbulenta<br>Carga de fondo  Energía turbulenta y disipación<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











## El modelo Iber Introducción 

- Modelación numérica en ríos: herramienta para el **e** studio de calados y velocidades para la resolución de problemas de ingeniería y dinámica fluvial (ríos y estuarios): – Delimitación de zonas inundables 

- – Diseño de encauzamientos y obras de protección 

- – Restauración de ríos 

- – Planes de emergencia en roturas de presa 

- – Optimización del funcionamiento de obras hidráulicas 











## El modelo Iber Introducción 

**1D Cuasi-2D 2D 3D** Tramos largos de Ríos con desbordamientos Estuarios Flujo local ríos localizados Canales Tramos cortos de ríos Vertederos Llanuras de inundación Pilas de puentes Flujo fuera de cauces Obras hidráulicas **+ ECONÓMICO + COSTE + SIMLIFICADO + PRECISIÓN (en general)** RS = 28951.6 .028 -40 -20 0 20 40 60 80 Station (m) 



<!-- Start of picture text -->
   RS = 28951.6<br>60 .028<br>58<br>56<br>54<br>52<br>50<br>48<br>46<br>44<br>42-60 -40 -20 0 20 40 60 80<br>Station (m)<br>Elevation (m)<br><!-- End of picture text -->













<!-- Start of picture text -->
El modelo Iber<br>Introducción<br>1D<br>19667.4<br>19628.2*    RS = 28951.6<br>19550.0 .028<br>19509.4* 60<br>19428.2<br>58<br>19364.6<br>19254.1*<br>56<br>19160.8<br>54<br>19062.6<br>18972.3 52<br>18898.5*<br>50<br>18805.7<br>18710.7 48<br>18617.8<br>46<br>18508.7*<br>18431.1* 44<br>18324.4<br>42<br>18229.2* -60 -40 -20 0 20 40 60 80<br>18127.9<br>18001.2 Station (m)<br>17870.6<br>17764.1*<br>17671.8* • Movimiento en la dirección del eje<br>17591.5*<br>17496.8 • Nivel constante en una sección<br>17398 1<br>• Velocidad uniforme<br>hans.sanchez@upc.edu<br>Elevation (m)<br><!-- End of picture text -->

# El modelo Iber Introducción Introducción 



<!-- Start of picture text -->
2D<br>•<br>En cada punto:    calado, Vx, Vy<br>•<br>Salto cualitativo en:  información geométrica<br>     tiempo de cálculo<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











## El modelo Iber Introducción Río Júcar 1982 Terrassa 1971 Llobregat 1982 



<!-- Start of picture text -->
2D<br><!-- End of picture text -->



<!-- Start of picture text -->
Río Júcar 1982<br><!-- End of picture text -->



<!-- Start of picture text -->
Riera de Les Arenes<br>1962<br><!-- End of picture text -->



<!-- Start of picture text -->
Llobregat 1982<br><!-- End of picture text -->











### El modelo Iber 

## Ecuaciones Hidrodinámicas 

## **Ecuaciones del flujo en lámina libre:**  Conservación de la masa  Conservación de la cantidad de movimiento (2ª ley de Newton) (alternativamente: conservación de la energía) 











El modelo Iber 



<!-- Start of picture text -->
Ecuaciones Hidrodinámicas<br>A partir de las ecuaciones de Navier-Stokes (fluido newtoniano e isotropo<br>en 3D):<br>Saint Venant 2D<br>Navier-Stokes  Reynolds<br>Promedio<br>  conservación masa   (aguas someras)<br>temporal<br>           +   Integración en<br> la vertical<br>  2ª ley de Newton  u u  u <br>t<br>2<br>1 1 z 0  h<br>u  udt u u dz<br>t  t   h  z 0<br>2 1 t<br>1<br>u: valor instantaneo u : promedio en la vertical<br>u  :fluctuaciones turbulentas<br>u<br>: promedio temporal<br>Las variables en un modelo 2D son promediadas en la profundidad<br>hans.sanchez@upc.edu<br><!-- End of picture text -->













<!-- Start of picture text -->
El modelo Iber<br>Ecuaciones Hidrodinámicas<br>Ecuaciones de aguas someras 2D<br>h  q x  q y<br>   0<br> t  x <br>y<br>2 2<br> q x    q x  h     qxq y    zb  τb,x    ν h  Ux     ν h  Ux <br> g    gh  t   t <br> t  x  h 2   y  h   x ρ  x   x   y   y <br>2 2<br> q y    q xq y     q y  g h   gh  zb  τb,y    ν ht  U y     ν ht  U y <br> <br> t  x h  h 2   x  x  <br>  y   y ρ   y  y <br> Distribución de  presión hidrostática<br> Velocidad  uniforme en profundidad  h, Ux, Uy<br>hans.sanchez@upc.edu<br><!-- End of picture text -->

El modelo Iber 

## Ecuaciones Hidrodinámicas 

### Forma vectorial: 



<!-- Start of picture text -->
<br><br>U  F H<br> t<br> <br> <br> <br> h   qxx qyy   0 <br>U   qx  ; F   qx 2  g h 2 qxqyxqyqyy  ; H   gh ( Soxox  S fx )    ν htt  Uxx     ν ht  Ux  <br>h 2 h   x  x   <br>  y  y <br>   <br> qy  2 2  <br> qxqyxqyqyy qyy  h       U y     U y  <br> h h g 2   gh ( Soyoy S fy )   x  ν htt  x     ν ht   <br>   y  y  <br>2 2 2 2 2 2<br>u u  v n v u  v n<br>Pendiente  S  ; S <br>fx 4 3 fy 4 3<br>h h<br>motriz:<br>      q : caudal específico<br>hans.sanchez@upc.edu (Ec. en forma conservativa)<br><!-- End of picture text -->











:   **U**  **F H**  _t_    _qxx qyy_   0  _g h_ 2 _qxqyxqyqyy_  ; **H**   _gh_ ( _Soxox_  _S fx_ )    ν htt  Uxx  2 _h_   x   x   2 2  _qxqyxqyqyy qyy_  _h_       U y  _h h g_ 2   _gh_ ( _Soyoy S fy_ )   x  ν htt  x  2 2 2 2 2 2 _u u_  _v n v u_  _v n S_  ; _S_  _fx_ 4 3 _fy_ 4 3 _h h_ : caudal específico 

El modelo Iber 

## Ecuaciones Hidrodinámicas 



<!-- Start of picture text -->
•<br>Sistemas de ecuaciones hiperbólicos: teoría de las características<br>(bicaracterísticas)<br>(cos  , sen  )<br>y<br>(  sen  , cos  )<br>ct <br>( ut,vt )<br>x<br>d ( un  2 c )  ut<br> <br>  g ( S 0 x S fx )cos  g ( S 0 y S fy )sen <br>dt <br>hans.sanchez@upc.edu(Ecuación válida sobre el cono característico)<br><!-- End of picture text -->











## El modelo Iber Ecuaciones Hidrodinámicas 



<!-- Start of picture text -->
Las características Proporcionan información importante del<br>comportamiento de la solución.<br>R. LENTO (Fr<1)<br>t<br>dx dt  v  c Característica<br>dx dt  v  c positiva  C <br>c  celeridad  gh<br>P<br>Dominio de  Característica<br><br>dependencia de P<br>negativa  C<br>hans.sanchez@upc.edu<br><!-- End of picture text -->



<!-- Start of picture text -->
x<br><!-- End of picture text -->











El modelo Iber 

## Ecuaciones Hidrodinámicas 



<!-- Start of picture text -->
R. RÁPIDO Fr>1<br>t<br>dx dt  v  c Característica<br>dx dt  v  c positiva  C <br>P<br>c  celeridad  gh<br>Característica<br>Dominio de<br>dependencia de P  negativa  C <br>x<br>hans.sanchez@upc.edu<br><!-- End of picture text -->













<!-- Start of picture text -->
El modelo Iber<br>Condiciones de contorno<br>• Nº condiciones según teoría de las características<br>Entrada  Salida<br>R. Lento  2  1<br>R. rápido  3  0<br>LENTO<br>RÁPIDO<br>t n+1 t n+1<br>t n t n<br>hans.sanchez@upc.edu<br><!-- End of picture text -->

El modelo Iber 

## Condiciones de contorno 



<!-- Start of picture text -->
Contornos abiertos<br>  Calado constante<br> Salida en ríos, canales  Condición de vertedero<br>  Calado variable en tiempo<br> Marea<br>  Condición de vertedero<br> Sección de control<br> curva de gasto  Hidrograma<br>  Caudal total constante<br> Entrada en ríos, canales<br>  Hidrograma<br> Avenidas en ríos<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











El modelo Iber Hidrodinámica 



<!-- Start of picture text -->
Contornos abiertos<br>Calado variable en tiempo<br>Onda de marea<br>hans.sanchez@upc.edu<br><!-- End of picture text -->













<!-- Start of picture text -->
El modelo Iber<br>Fricción de fondo<br>Fórmula de Manning<br>n2 U U n2 U U<br>x y<br>τ  τ <br>b,x ρ g h  4/3 b,y ρ g h  4/3<br>h h<br>hans.sanchez@upc.edu<br><!-- End of picture text -->



<!-- Start of picture text -->
El modelo Iber<br>Fricción de pared<br>Deslizamiento libre  Rozamiento<br>Ríos, zonas costeras  Canales, estructuras<br>hidráulicas<br>u*  y <br>u  Ln  30 <br>κ K<br> S <br>hans.sanchez@upc.edu<br><!-- End of picture text -->



<!-- Start of picture text -->
El modelo Iber<br>Dominio Público Hidráulico<br>RD 9/2008<br>Zona de flujo preferente<br>Modificación RDPH<br>T=100 años<br>Vía de intenso desagüe  Daños graves para personas y bienes<br> Δ Zs < 0.3 m  (0.1 - 0.5)   h > 1 m<br> V > 1 m/s<br> q > 0.5 m 2 /s<br>Zonas inundables<br>T = 500 años<br>  h > 0 m<br>hans.sanchez@upc.edu<br><!-- End of picture text -->



<!-- Start of picture text -->
El modelo Iber<br>Hidrodinámica<br>Herramientas de soporte para determinación vía<br>intenso desagüe<br>•Línea y distancia<br>•Polígono<br>hans.sanchez@upc.edu<br><!-- End of picture text -->

El modelo Iber Hidrodinámica 



<!-- Start of picture text -->
Zonas de riesgo  Zonas inundables<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











El modelo Iber Frentes Seco-Mojado 

Mojado si h > tolerancia (ewd) **Método estable, conservativo, no difusivo** 



<!-- Start of picture text -->
hans.sanchez@upc.edu<br><!-- End of picture text -->



<!-- Start of picture text -->
t = 0 h<br><!-- End of picture text -->



<!-- Start of picture text -->
t = 4 h<br><!-- End of picture text -->













<!-- Start of picture text -->
El modelo Iber<br>Frentes Seco-Mojado<br>   3 Métodos distintos para el secado cuando Velemento<Dt·SQsalida<br>•<br>Secado normal:  calado negativo<br>    (inestabilidades si h pequeño)<br>h<0<br>ewd<br>•<br>Secado estricto: reducción Dt<br>    (aumento tiempo de cálculo)<br>ewd 0<h<ewd<br>•<br>Secado hidrológico:<br>     reducción caudal de salida<br>     (compromiso)   h=0<br>ewd<br>hans.sanchez@upc.edu<br><!-- End of picture text -->

### El modelo Iber 

## Ejemplo 1: Influencia acondicionamiento carretera 



<!-- Start of picture text -->
3500<br>3000<br>T = 500 anys<br>T = 100 anys<br>2500 T = 10 anysyss<br>2000<br>1500<br>1000<br>500<br>0<br>0 10000 20000 30000 40000 50000 60000 70000 80000<br>Temps (s)<br>hans.sanchez@upc.edu<br>Cabal (m3/s)<br><!-- End of picture text -->



<!-- Start of picture text -->
3500<br>3000<br>T = 500 anys<br>T = 100 anys<br>2500 T = 10 anysyss<br>2000<br>1500<br>1000<br>500<br>0<br>0 10000 20000 30000 40000 50000 60000 70000 80000<br>Temps (s)<br>Cabal (m3/s)<br><!-- End of picture text -->











### El modelo Iber 



<!-- Start of picture text -->
Ejemplo 1: Influencia acondicionamiento carretera<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











El modelo Iber 











Ejemplo 1: Influencia acondicionamiento carretera 

### El modelo Iber 

## Ejemplo 1: Influencia acondicionamiento carretera 



<!-- Start of picture text -->
hans.sanchez@upc.edu<br><!-- End of picture text -->











### El modelo Iber 

## Ejemplo 1: Influencia acondicionamiento carretera 



<!-- Start of picture text -->
hans.sanchez@upc.edu<br><!-- End of picture text -->











### El modelo Iber 

## Ejemplo 1: Influencia acondicionamiento carretera 



<!-- Start of picture text -->
hans.sanchez@upc.edu<br><!-- End of picture text -->











### El modelo Iber 











Ejemplo 1: Influencia acondicionamiento carretera 

### El modelo Iber 

## Ejemplo 2: Actuaciones en el Puerto de Tarragona 

### **Escenario 1** 

- Evaluación del efecto del río en el puerto de Tarragona 

- Evaluación de variables 

- como velocidad, caudal, acción hidrodinámica, etc. 

-Propuesta de dos escenarios de cálculo de acuerdo a las nuevas infraestructuras diseñadas en el puerto 











**Escenario 2**  Evaluación como nuevas 

## El modelo Iber Ejemplo 2: Actuaciones en el Puerto de Tarragona 



<!-- Start of picture text -->
Cota de agua<br>Velocidad<br>Número de Froude<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











### El modelo Iber 



<!-- Start of picture text -->
Ejemplo 2: Actuaciones en el Puerto de Tarragona<br>- Representación vectorial<br>de la velocidad (magnitud)<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











## El modelo Iber Ejemplo 2: Actuaciones en el Puerto de Tarragona 



<!-- Start of picture text -->
Capacidad de erosión<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











### El modelo Iber 

Ejemplo 3: Riesgo inundación en Andorra • Base topográfica obtenida a partir de vuelos LIDAR. (puntos cada 0.5 m) 











### El modelo Iber 



<!-- Start of picture text -->
Ejemplo 3: Riesgo inundación en Andorra<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











### El modelo Iber 











Ejemplo 2: Riesgo inundación en Andorra 

### El modelo Iber 



<!-- Start of picture text -->
Ejemplo 3: Riesgo inundación en Andorra<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











El modelo Iber Ejemplo 3: Riesgo inundación en Andorra 











El modelo Iber Ejemplo 3: Riesgo inundación en Andorra 



<!-- Start of picture text -->
Capacidad de arrastre<br>hans.sanchez@upc.edu<br><!-- End of picture text -->













<!-- Start of picture text -->
El modelo Iber<br>Ejemplo 4: Rotura instantánea balsa<br><!-- End of picture text -->



<!-- Start of picture text -->
V = 278000m 3<br>Calado = 5m<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











### El modelo Iber 

## Ejemplo 4: Rotura instantánea balsa 

Malla de 30104 elementos Condiciones iniciales: y=5m en la balsa 











### El modelo Iber 



<!-- Start of picture text -->
Ejemplo 4: Rotura instantánea balsa<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











### El modelo Iber 



<!-- Start of picture text -->
Ejemplo 4: Rotura instantánea balsa<br>hans.sanchez@upc.edu<br><!-- End of picture text -->











