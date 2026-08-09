---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\UCCI-especializaciónProy Investigación\MODULO 5-Estadistica 2\Sesion 12\12-Anova-Especialización.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]

**DIPLOMA DE ESPECIALIZACIÓN EN PROYECTOS DE INVESTIGACIÓN ASESORÍA DE TESIS ESTADISTICA APLICADA A LA INVESTIGACIÓN II Tema 12** 



**ANÁLISIS DE VARIANZA ANOVA** 

**Dr. César Fernando Solís Lavado 2022** 





**Comparación de prueba paramétricas y no paramétricas** 

# **¿Qué es el Análisis de varianza (ANOVA)?** 



**El análisis de varianza (ANOVA) de un factor sirve para comparar varios grupos en una variable cuantitativa. Se trata, por tanto, de una generalización de la prueba “t” de Student para dos muestras independientes al caso de diseños con más de dos muestras.** 



**El análisis de la varianza permite contrastar la hipótesis nula de que las medias de K poblaciones (K>2) son iguales, frente a la hipótesis alternativa de que por lo menos una de las poblaciones difiere de las demás en cuanto a su valor esperado.** 



**Formulación de H0 y H1 H0: µ1=µ2=µ3= µ4=…. H1: No todas las medias son iguales** 











**Distribución F** 

#### **El ANOVA requiere el cumplimiento de los siguientes supuestos:** 



- ✓ **Las poblaciones (distribuciones de probabilidad de la variable dependiente correspondiente a cada factor) son normales.** 

✓ **Las K muestras sobre las que se aplican los tratamientos son independientes.** 

✓ **Las poblaciones tienen todas igual varianza (homocedasticidad).** 



###### **Tabla ANOVA** 



<!-- Start of picture text -->
Suma de  Grados de  Cuadrados medios  Razón F<br>Fuente de variación<br>cuadrados libertad (CM) calculada<br>Tratamientos (columnas) SCC k - 1 CMC= SCC/(k-1)<br>Error SCE n - k CME=SCE/(n-k)<br>Total SCT n - 1<br><!-- End of picture text -->

**k: Número de grupos n: Número de datos** 





**SCE: Suma de Cuadrados del Error** 

**SCC: Suma de Cuadrados de Columnas** 

#### **_Ejercicios_** 



**1) Pruebe la hipótesis de que los rendimientos académicos en estadística de los estudiantes del grupo control en el Pre-test, donde trabajaron de manera tradicional con el programa Excel, no difieren según la edad, para un nivel de significación de 5%.** 



**Hipótesis de investigación: No existen diferencias significativas en el rendimiento académico poblacional de los estudiantes que trabajaron con el Excel en el pre-test según edad.** 

**Nota: Los datos se encuentran en la base de datos en el SPSS** 



### **Homocedasticidad** 







**Si el p-valor≥0,05 se concluye H0** Si el p-valor<0,05 se concluye H1 



##### **b) Prueba de hipótesis** 

**Paso 1: Formulación de H0 y H1 H0: No hay diferencias en el rendimiento académico poblacional de los estudiantes del grupo control en el pre-test según edad. H0: µ1=µ2=µ3=µ4=µ5 H1: No todas las medias poblacionales del rendimiento académico de los estudiantes del grupo control en el pre-test según edad son iguales. Paso 2: α=0,005 Paso 3: Prueba ANOVA de un factor Paso 4: Regla de decisión** 



**Si el p-valor≥0,05 se concluye H0 Si el p-valor<0,05 se concluye H1** 

**Paso 5: Conclusión.** 



#### **Comparaciones múltiples de Tukey** 









- **2) Un egresado de Ingeniería tiene ofertas de trabajo de cuatro empresas. Para examinar un poco más las propuestas solicitó a una muestra de personas que tenían menos de 18 meses de labor en dichas empresas, que les informe sobre cuántos meses trabajaron cada uno para su compañía, antes de recibir el primer aumento de sueldo. La información muestral se presenta en la tabla. A un nivel de significación de 5%, ¿Existe alguna diferencia entre las cuatro empresas, en el número medio de meses antes de recibir el primer aumento de sueldo?** 

|**Empresa A **|**Empresa B **|**Empresa C **|**Empresa D**|
|---|---|---|---|
|**11**|**13**|**17**|**11**|
|**9**|**11**|**11**|**13**|
|**13**|**9**|**14**|**15**|
|**11**|**10**|**14**|**13**|



**Nota: Genere una base de datos en el SPSS** 





### **Prueba de normalidad** 





## **Prueba de homogeneidad de varianzas** 



**Conclusión: Para un 95% de confianza se acepta H0, ya que el p-valor (0,933) es mayor a la significancia (0,050), es decir se acepta que: las varianzas poblacionales del número medio de meses antes del primer aumento en las cuatro empresas no difieren (son homogéneas).** 



##### **Prueba de hipótesis** 

**Paso 1: Formulación de H0 y H1 H0: No hay diferencias en el número medio poblacional de los meses antes de recibir el primer aumento en las cuatro empresas. H0: µ1=µ2=µ3=µ4 H1: No todas las medias poblacionales del número de meses antes de recibir el primer aumento son iguales.** 



**Paso 2: α=0,005 Paso 3: Prueba ANOVA de un factor Paso 4: Regla de decisión** 

**Si el p-valor≥0,05 se concluye H0 Si el p-valor<0,05 se concluye H1** 

**Paso 5: Conclusión.** 



**3) Reconsideración: Un egresado de Ingeniería que labora en la empresa B sostiene que hubo un error en su respuesta y señala que en realidad recibió el primer aumento de sueldo en el noveno mes y no así en el mes treceavo. Con esta nueva información ¿Existe alguna diferencia entre las cuatro empresas, en el número medio de meses antes de otorgar el primer aumento de sueldo a los ingenieros, para una significancia α=0,05?** 



|**Empresa A**|**Empresa B**|**Empresa C**|**Empresa D**|
|---|---|---|---|
|**11**|**9**|**17**|**11**|
|**9**|**11**|**11**|**13**|
|**13**|**9**|**14**|**15**|
|**11**|**10**|**14**|**13**|



### **Prueba de normalidad** 



## **Comparación de medias** 





## **Prueba de homogeneidad de varianzas** 





**Conclusión: Para un 95% de confianza se acepta H0, ya que el p-valor es mayor a la significancia (0,050), es decir se acepta que: las varianzas poblacionales del número medio de meses antes del primer aumento en las cuatro empresas no difieren (son homogéneas).** 



**Paso 5: Conclusión: Para un 95% de confianza se rechaza H0, es decir se acepta que: No todas las medias de los meses antes de recibir el primer aumento son iguales, es decir existen diferencias significativas entre las cuatro empresas.** 

#### **Prueba de Tukey de las comparaciones múltiples** 







**Conclusión: Existen diferencias significativas entre la empresa B y la empresa C, mientras que con las demás empresas las diferencias no es significativa, aseveración que se hace para un 95% de nivel de confianza. El egresado debería elegir a la empresa B.** 

#### **_Tarea_** 

**1. El encargado de compras de una compañía tiene que escoger entre tres marcas de máquinas para procesar cierto producto. Luego de operar las tres máquinas, que fueron escogidas al azar, se obtuvieron los tiempos (en segundos) de objetos procesados por cada máquina, los que se presentan en la tabla.** 

**Utilice un nivel de significancia de 0,05 para probar la aseveración de que hay diferencia en los tiempos medios poblacionales de procesamiento de las máquinas. ¿Se puede considerar que los grupos provienen de la misma población?** 



|**Marca A**|**Marca B**|**Marca C**|
|---|---|---|
|**51**|**65**|**58**|
|**52**|**60**|**65**|
|**43**|**61**|**52**|
|**51**|**60**|**52**|
|**41**|**62**|**44**|
|**55**|**59**||
||**58**||





#### **_Tarea_** 



- **2) Pruebe la hipótesis de que los rendimientos académico en estadística de los estudiantes del grupo experimental en el Pos-test, donde trabajaron con el SPSS, difieren significativamente según la procedencia, para un nivel de significación de 5%.** 

##### **Nota: Los datos se encuentran en la base de datos en el SPSS** 





#### **_Tarea_** 



- **3) El instituto Nacional de Salud aplicó encuestas a adultos para determinar cómo pasaban su tiempo libre. Los datos han sido desglosados según la actividad que realizan y se ha seleccionado una muestra aleatoria de tamaño n=16 ¿Parece haber alguna diferencia en el tiempo promedio que se pasa en las diferentes actividades para un 5% de significancia? Realice la correspondiente prueba de hipótesis. Las observaciones estan en horas por semana** 



<!-- Start of picture text -->
Actividad<br>Con la<br>TV Lectura Deportes<br>familia<br>24 12 10 16<br>17 13 12 18<br>20 15 8 15<br>22 20 9 20<br><!-- End of picture text -->







