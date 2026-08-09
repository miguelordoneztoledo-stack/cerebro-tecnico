---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\UCCI-especializaciónProy Investigación\MODULO 5-Estadistica 2\Sesion 10\10-Chi-cuadrada-Especialización.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]

**DIPLOMA DE ESPECIALIZACIÓN EN PROYECTOS DE INVESTIGACIÓN ASESORÍA DE TESIS ESTADISTICA APLICADA A LA INVESTIGACIÓN II Tema 10** 



# **PRUEBA CHI CUADRADA** 



**Dr. César Fernando Solís Lavado 2022** 





**Comparación de prueba paramétricas y no paramétricas** 

## **Distribución Ji cuadrada;     Chi cuadrada o X**<sup>**2**</sup> 



**Definición: La distribución Chi cuadrado (X**<sup>**2**</sup> **) es la distribución de una variable aleatoria que siempre es positiva, con una posición oblicua hacia la derecha y unimodal. La forma de la distribución depende de un parámetro llamado grados de libertad.** 



- **El valor mínimo es 0. Todas las curvas son asimétricas.** 

- **Cuando aumentan los grados de libertad las curvas son menos elevadas y más extendidas a la derecha.** 





<!-- Start of picture text -->
Estadística no paramétrica<br>Prueba Chi cuadrado<br>Una variable Dos variables<br>Prueba de bondad de  Prueba de  Prueba de<br>ajuste independencia homogeneidad<br>Grados de libertad de X 2<br>Prueba Descripción de los grados de libertad (g.l.) Su fórmula es:<br>Bondad de ajuste. Está en función del número de categorías (k):<br>(una variable) g.l. = k – 1<br>Homogeneidad e  Se obtiene multiplicando el número de filas<br>independencia. menos uno (r-1) por el número de columnas<br>(dos variables) menos uno (c-1), es decir: g.l. = (r - 1)(c - 1)<br><!-- End of picture text -->







**PRUEBA DE BONDAD DE AJUSTE** 



### **PRUEBA PARA CATEGORÍAS IGUALMENTE PROBABLES** 



**1) El gerente de una empresa constructora está preocupado por el ausentismo de sus trabajadores. Ha decidido muestrear las listas de asistencia para determinar si el ausentismo está distribuido uniformemente entre los seis días de la semana laboral. La hipótesis nula a ser probada es:** **_el ausentismo está distribuido equitativamente durante toda la semana_ , para un nivel de significación 0,05. Aplique los cinco pasos de la prueba de hipótesis. Grafique.** 







**Paso 1: Formulación de H0 y H1 H0: El ausentismo esta distribuido equitativamente durante la semana. H0: p1=p2=p3= ….=p6** 

**H1: El ausentismo no esta distribuido equitativamente durante la semana. H1: Al menos una de las proporciones es diferente de las otras. Paso 2: α = 0,05** 

**Paso 3: Prueba Chi cuadrada de bondad de ajuste para categorías iguales . Paso 4: Regla de decisión Si el p-valor≥0,05 se concluye H0 Si el p-valor<0,05 se concluye H1** 

**Paso 5: Conclusión** 

**PRUEBA PARA CATEGORÍAS CON PROPORCIONES DIFERENTES 2) Calidad de atención: Los siguientes datos son las frecuencias observadas para cuatro categorías: Malo; Regular; Bueno y Excelente. Para un nivel de significancia del 0,05 pruebe mediante la prueba de bondad de ajuste, la aseveración de que las cuatro categorías tienen proporciones de 20%; 25%; 25% y 30% respectivamente.** 







**Paso 1: Formulación de H0 y H1 H0: p1=0,20; p2=0,25; p3=0,25; p4=0,30 H1: Al menos una de las proporciones es diferente del valor aseverado. Paso 2: α = 0,05 Paso 3: Prueba Chi cuadrada de bondad de ajuste para categorías diferentes Paso 4: regla de decisión Si el p-valor≥0,05 se concluye H0 Si el p-valor<0,05 se concluye H1 Paso 5: Conclusión** 









**PRUEBA DE INDEPENDENCIA** 



**3) La Ford Motor Company opera una planta de ensamble en Dearborn, Michigan. La planta opera tres turnos. El gerente de control de calidad quiere comparar el nivel de calidad en los tres turnos. Los vehículos se clasifican por su nivel de calidad (aceptable, inaceptable) y por turno (mañanas, tardes y noches). ¿Está relacionada la calidad del producto con el turno donde se fabricó?** 



###### **Tabla de contingencia** 





##### **Paso 1:** 

**H0: La calidad del producto y el turno de trabajo no están relacionados (Son independientes) H1: La calidad del producto y el turno de trabajo están relacionados (Son dependientes) Paso 2: α = 0,05 Paso 3: Prueba Chi cuadrada de independencia. Paso 4: Regla de decisión Si el p-valor≥0,05 se concluye H0 Si el p-valor<0,05 se concluye H1** 

**Paso 5: Conclusión** 







**4) La base de datos presenta los resultados de una encuesta a personas sobre su afinidad política y se desea probar la hipótesis de que el género y la afinidad política son independientes para α=0,05** 

**Paso 1: H0: El género y la afinidad política son independientes (No están relacionados) H1: El género y la afinidad política son dependientes (Están relacionados) Paso 2: α = 0,05 Paso 3: Prueba Chi cuadrada de independencia. Paso 4: Regla de decisión** 



**Paso 5: Conclusión** 

### **PRUEBA DE HOMOGENEIDAD** 





**Permite probar si varias muestras de un mismo carácter provienen de la misma población.** 

**Ejemplo: Se desea comprobar la fiabilidad de un software de acuerdo al distribuidor que lo suministra. Para esto se tomaron muestras de 20 software de cada uno de los 3 distribuidores, probando el número de defectuosos en cada lote para cada distribuidor.** 

||**Defectuosos**|**Correctos**|**Total**|
|---|---|---|---|
|**Distribuidor 1**|**3**|**17**|**20**|
|**Distribuidor 2**|**2**|**18**|**20**|
|**Distribuidor 3**|**1**|**19**|**20**|
|**Total**|**6**|**54**|**60**|





**5) Para determinar la conciencia pública y preocupación por la contaminación ambiental, se entrevistó a una muestra de ciudadanos de dos distritos de Lima. La pregunta fue: ¿Es la contaminación ambiental una preocupación en su distrito? Determine mediante una prueba de hipótesis si la preocupación por la** 

**contaminación ambiental es homogénea o no.** 







##### **Paso 1:** 

**H0: La preocupación por la contaminación ambiental no difieren según el distrito (son homogéneos) H1: La preocupación por la contaminación ambiental difieren según el distrito (Son heterogéneos)** 

**Paso 2: α=0,050 Paso 3: Prueba ji cuadrada de homogeneidad. Paso 4: Regla de decisión** 



**Paso 5: Conclusión** 

#### **Tarea** 



**1. Para conocer la opinión de los ciudadanos sobre la gestión del alcalde de una Municipalidad distrital de Lima, se realizó una encuesta a una muestra aleatoria de ciudadanos del distrito. Los resultados se presentan en la tabla. Genere una base de datos en el SPSS y contraste la hipótesis, con un nivel de significación del 5% que no existen diferencias de opinión entre varones y mujeres ante a la gestión del alcalde.** 

||**En desacuerdo**|**De acuerdo**|**No contestan**|
|---|---|---|---|
|**Varones**|**11**|**10**|**5**|
|**Mujeres**|**15**|**8**|**3**|



**2. Un investigador quiere estudiar si hay asociación entre la práctica deportiva y la sensación de bienestar de las personas** 

**mayores de 40 años. Extrae una muestra aleatoria de personas. Los datos se muestran en la tabla. Genere la base de datos en el SPSS** 







