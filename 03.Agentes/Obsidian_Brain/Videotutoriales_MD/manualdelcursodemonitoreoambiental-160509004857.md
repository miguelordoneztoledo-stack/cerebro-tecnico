---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\EIA\5-8 EVALUACION DE IMPACTO AMBIENTAL CON QGIS\MODULO 8\Modulo 8-20200418T032708Z-001\Modulo 8\MATERIAL-MODULO8\MATERIAL-MODULO8\manualdelcursodemonitoreoambiental-160509004857.pdf"
---











**Programa para la Protección Ambiental Acuerdo de Cooperación No. 517-A-00-09-00106-00 MANUAL DEL CURSO DE MONITOREO AMBIENTAL** 

##### **INTEC 2012** 

Este manual fue posible gracias al apoyo generoso provisto por el pueblo estadounidense mediante la Agencia de los Estados Unidos para el Desarrollo Internacional (USAID) y su receptor principal The Nature Conservancy(TNC) y socio el Instituto Tecnológico de Santo Domingo, INTEC, según los términos de Acuerdo de Cooperación No. 517-A-00-09-00106-00 (Programa de Protección Ambiental). El contenido y las opiniones aquí expresadas son responsabilidad del INTEC y no USAID Environmental Protection Program Quarterly Report April-June 2010 reflejan necesariamente la posición o la política de USAID o de TNC, y no se deberá inferir ninguna adopción oficial de las 1 mismas. 



Programa de la USAID Para la Protección Ambiental Instituto Tecnológico de Santo Domingo | Servicios Editoriales Printcorp Servicios Gráficos Corporativos, S.R.L. | Primera Edición, 2012 D.R. INTEC | Impreso en República Dominicana | Distribución Gratuita | Prohibida su venta. 

Este manual fue posible gracias al apoyo generoso provisto por el pueblo estadounidense mediante la Agencia de los Estados Unidos para el Desarrollo Internacional (USAID) y su receptor principal The Nature Conservancy(TNC) y socio el  Instituto Tecnológico de Santo Domingo, INTEC, según los términos de Acuerdo de Cooperación No. 517-A-00-09-00106-00 (Programa de Protección Ambiental). El contenido y las opiniones aquí expresadas son responsabilidad del INTEC y no reflejan necesariamente la posición o la política de USAID o de TNC, y no se deberá inferir ninguna adopción oficial de las mismas. 



2 

<mark>Í n d i c e d e c o n t e n i d o</mark> 

Introducción 

4 

1 Agua 5 1.1 Introducción 5 1.2  Clasificación de las aguas 6 1.3 Contaminación  del Agua 7 2 Aire 12 2.1- Introducción 12 2.2  Contaminación  del aire 12 3 Ruido 14 3.1 Contaminación por ruido 14 4  Muestreo y análisis ambiental 15 5 Manejo estadístico de datos ambientales 17 6  Referencias bibliográficas 19 7 Anexos 20 



3 

**Introducción** 

### **[[16 Anexo 3 - Manual de Monitoreo|Monitoreo Ambiental]]** . **Componentes de un Sistema Ambiental** 

En un sistema ambiental pueden distinguirse los siguientes elementos componentes que requieren ser monitoreados: 

Fisicoquímicos (dentro y fuera de la tierra): atmósfera, clima, suelos, recursos hídricos. 

- Biológicos (flora y fauna): animales, plantas y microorganismos. 

- Humanos: infraestructura, tecnología, desarrollo social y económico. 

Cada uno de estos componentes interacciona con los demás y son dependientes entre sí. Uno de los efectos más graves de la interacción del componente humano con los componentes físico-químicos y biológicos es la contaminación. Para garantizar que cada componente cumpla adecuadamente sus funciones dentro del sistema, es necesario que el componente humano asuma ciertos requerimientos de control en sus actividades. Esos requerimientos están establecidos por las normas ambientales y su cumplimiento es evaluado por un sistema de monitoreo ambiental. 

Un sistema de monitoreo ambiental  verifica el cumplimiento de las normas ambientales vigentes para cada uno de los componentes. En cuanto a los componentes fisicoquímicos del sistema ambiental, la atmosfera  requiere una composición estable para impedir el sobrecalentamiento de la corteza terrestre y el cambio climático; los suelos necesitan condiciones adecuadas para las necesidades de las plantas y para el emplazamiento de edificaciones seguras; los recursos hídricos requieren condiciones para el desarrollo de la vida. 

Los componentes biológicos requieren una cobertura vegetal amplia y diversa para preservar ecosistemas, contribuir a las condiciones climáticas, proporcionar alimentos. Los animales requieren espacios adecuados que favorezcan su desenvolvimiento natural. Los microorganismos deben ser diferenciados entre los que son beneficiosos y los que son perjudiciales para la salud. 

El componente humano requiere de infraestructuras adecuadas para vivienda, salud y empleo, entre otras necesidades básicas así como el disfrute de un medio ambiente sano. También requiere de participación en la toma de decisiones que lo afectan. 

A continuación exponemos algunas características de los componentes fisicoquímicos y biológicos de un sistema ambiental, sus contaminantes más comunes, la forma de determinarlos y los límites establecidos en las normas ambientales para cada uno de ellos. 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

4 

## **1. Agua** 

#### **1.1 Introducción** 

La extraordinaria importancia del agua radica en el hecho de que la inmensa mayoría de los organismos existentes en la Tierra están constituidos principalmente por agua. Los seres humanos contienen agua en un 65% aproximadamente y en un árbol más o menos el 60% es agua (Tyler 2003). Todos los procesos biológicos y muchas reacciones químicas se llevan a cabo en un medio acuoso por lo cual sin agua no existiría la vida como la conocemos. 

En estado líquido y pura, el agua es incolora, inodora, insípida y transparente. Su alto punto de ebullición (100 C) y el punto de congelación (0 C) permiten que el agua se mantenga en estado líquido 0 o en diferentes climas.Las propiedades únicas del agua se deben a la presencia entre sus moléculas de fuerzas de atracción llamadas _puentes de hidrogeno_ . 

Entre las principales propiedades del agua están los siguientes: 

- Es la única sustancia que se encuentra de forma natural en estado líquido, sólido (nieve, hielo) o gaseoso (vapor de agua) en la superficie terrestre. 

- Capacidad de absorber gran cantidad de calor sin cambiar su temperatura de manera significativa ( _calor especifico_ ), lo que le permite regular la temperatura de los seres vivos, el clima de la tierra, y es un excelente refrigerante en procesos que liberan energía calórica. 

- Puede disolver gran cantidad de compuestos, diluyendo los contaminantes, llevando nutrientes a los tejidos de los seres vivos y sacando de estos tejidos los productos de desecho. Debido a esta propiedad, el agua ha sido llamada _disolvente universal_ , aunque también debido a ella es fácilmente contaminable. 

- Se expande cuando se congela, contrario a la mayoría de los líquidos, por lo cual el hielo flota sobre el agua, y los ríos y lagos se congelan desde la superficie hacia adentro. De ocurrir lo contrario no existiría la vida acuática. 

Alrededor del 97% del agua del planeta tierra se encuentra en los océanos. El 3% restante es agua dulce o potable. De esta, el 2.97% se halla retenido en glaciares o en manantiales subterráneos muy profundos y de difícil extracción. Solo el 0.3%  del total está disponible como vapor de agua, humedad del suelo, aguas subterráneas utilizables, lagos y ríos. 



Figura 1   Distribución del agua (Fuente: Servicio Geológico de los Estados Unidos) 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

5 

El agua se considera un _recurso renovable_ mediante el [[ciclo_hidrologico - sociedad geografica de lima|ciclo hidrológico]]. Pero el uso indiscriminado y la utilización de las fuentes de agua para descargar desechos industriales y domésticos amenazan con convertirla en un _recurso no renovable_ . 

### **1.2 Clasificación de las Aguas según su origen y según su uso** 

El agua se clasifica _según su origen_ en las siguientes categorías: _Agua superficial_ (ríos, lagos y lagunas), _Agua subterránea_ (agua de pozos), _Agua meteorológica_ (agua lluvia), _Agua de mar_ .Cada una de ellas tiene disueltas o suspendidas sales minerales, gases y material particulado en cantidades variables según de donde procedan. 

El agua se clasifica también _según el uso_ que se le vaya a dar: _Aguas de uso domestico_ , _Aguas de uso industrial_ y _Aguas para recreación_ . 

La Norma Ambiental sobre Calidad de Aguas y Control de Descargas del Ministerio de Medio Ambiente y Recursos Naturales de junio 2003, clasifica los cuerpos hídricos como: 

· **Aguas superficiales:** 

**a)** CLASE A: aguas destinadas al abastecimiento público de agua potable sin necesidad de tratamiento previo, excepto simple desinfección; aguas destinadas para el riego de vegetales de consumo crudo, y para usos de recreo con contacto directo (ej. Natación); aguas destinadas a la preservación de la fauna y la flora. 

**b)** CLASE B: aguas destinadas al abastecimiento público de agua potable con tratamiento; aguas aprovechables para regadío de cultivos, deportes acuáticos sin contacto directo, y usos industriales y pecuarios. 

**c)** CLASE C: aguas utilizadas para navegación, enfriamiento, y otros usos que no impliquen contacto directo. 

**d)** CLASE D-1: aguas superficiales a preservar en condiciones naturales, por su excepcional calidad o gran valor ecológico. 

### · **Aguas costeras:** 

**a)** CLASE D-2: aguas costeras y estuarinas que se deben preservar en condiciones naturales, por su excepcional calidad o gran valor ecológico. Su delimitación física y geográfica se  extiende 500 m mar adentro de su ubicación. 

**b)** CLASE E: aguas costeras destinadas a la conservación de recursos naturales como manglares y zonas de reproducción y nutrición de organismos marinos y áreas para acuacultura marina, incluyendo moluscos, camarones, peces y pesca comercial. Además, destinadas a actividades de deportes acuáticos y otras de contacto directo con el agua, como natación, buceo, esquí acuático y otros. 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

6 

**c)** CLASE F: aguas costeras destinadas a deportes acuáticos y otras actividades que no conllevan contacto directo con el agua. 

**d)** CLASE G: aguas costeras destinadas a actividades industriales, portuarias y de transporte naviero En la Norma Calidad de Agua se establecen parámetros de calidad  según la clasificación anterior. Estos parámetros pueden consultarse en Anexos 1 o en la página web del Ministerio de Medio Ambiente y Recursos Naturales. 

Las aguas utilizadas por el hombre para descartar los desechos de sus actividades reciben el nombre de _Aguas Residuales_ . Las aguas residuales también se clasifican según la actividad humana de la cual provienen en: 

- _Aguas residuales urbanas_ son las que provienen de núcleos urbanos. Contienen sustancias procedentes de la actividad humana (alimentos, basuras, productos de limpieza, jabones). 

- _Aguas residuales pluviales_ se originan por arrastre de la suciedad que encuentra a su paso el Agua de lluvia. 

- _Aguas residuales industriales_ contienen desechos de procesos industriales 

- _Aguas residuales agrícolas_ pueden aportar al agua grandes cantidades de estiércol  (materia orgánica, nutrientes y microorganismos). 

### **1.3 Contaminación del agua** 

La contaminación podría definirse de manera general como la introducción en un ambiente natural de cualquier sustancia o forma de energía que altere su calidad. La contaminación del agua altera las propiedades físicas, químicas y biológicas de la misma. Entre las propiedades físicas que resultan alteradas por episodios de contaminación se encuentran: el aspecto, el color, el olor, la turbidez, el sabor, la temperatura y la conductividad. 

Los _contaminantes químicos_ pueden ser **_biodegradables_** , es decir que pueden transformarse por mecanismos biológicos en sustancias inocuas, o **_persistentes,_** que no sufren biodegradación. Los _contaminantes biológicos_ son microorganismos que en ocasiones pueden ser patógenos. 

Los índices más utilizados para medir la contaminación física del agua son el aspecto, el color, la conductividad eléctrica, pH y sólidos totales, disueltos o suspendidos. 

- **Aspecto y Color** : El agua pura es incolora y transparente. Sólo es azul si la fuente tiene gran profundidad (espesor). Ciertos colores en fuentes de  aguas naturales  son indicativos de la presencia de contaminantes como algas y otros compuestos contenidos en aguas residuales descargadas en las fuentes de agua natural. El color que podría tener el agua contaminada se mide en unidades platino-cobalto (Pt-Co). 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

7 

- **Conductividad** : La conductividad eléctrica mide la capacidad del agua para conducir la electricidad y es indicativa de la cantidad de minerales disueltos que tiene el agua, los cuales al disolverse se disocian en partículas con carga eléctrica (iones) que son responsables de la conducción de la electricidad. Una alta conductividad  indica un alto grado de mineralización del agua. La medida de este parámetro se realiza con un equipo llamado conductímetro. Las unidades son Siemens por metro [S/m] en el sistema internacional de medición (SI) y micromhos por centímetro [mmho/cm] en unidades estándar de Estados Unidos. Su símbolo es k o s. 

   - **pH o grado de acidez** : se utiliza como una medida de la  naturaleza ácida o alcalina del agua. Mide la concentración de iones responsables de la acidez (H ) presentes en una + solución. Se expresa como **– log [H ] +** y se interpreta: 

pH= 7 medio neutro       pH <7 medio ácido      pH >7 medio alcalino 

El pH de las aguas naturales se debe a la composición de los terrenos por las cuales atraviesan. El pH alcalino indica que la fuente de agua proviene de terrenos calizos y si el pH es acido los suelos que recorre el agua son silíceos. Los valores de pH más favorables tanto para la vida acuática como para consumo humano se encuentran entre 6-8.  Fuera de este intervalo resultan afectados en mayor o menor grado, el sabor, el olor y el aspecto del agua. Las medidas del pH se realizan con un equipo llamado medidor de pH  (peachímetro) y también de manera aproximada con papel indicador de pH, el cual cambia de color según sea el grado de acidez de la solución que se mide. 

- **Sólidos Totales (ST o TS)** : es la cantidad de sustancias que contiene el agua, tanto disuelta como suspendida. Se define como el residuo seco resultante de evaporar una muestra de agua a una temperatura entre 103 C – 105 C. Los sólidos totales comprenden los 0 0 **sólidos suspendidos (SS)** y los **sólidos disueltos (SD o DS)** : **ST = SS + SD.** 

Los equipos que miden la  conductividad eléctrica también miden sólidos totales porque existe una correlación directa entre la conductividad y la concentración de sólidos totales para aguas dulces y salobres. 

- Los **sólidos suspendidos** son los que quedan retenidos en un filtro después de pasar la muestra de agua. Los **sólidos disueltos** son los que permanecen en la muestra de agua después de pasar por el filtro. Las aguas para el consumo humano, con un alto contenido de sólidos disueltos, tienen mal sabor y pueden inducir una reacción fisiológica adversa en el consumidor. 

Para medir la contaminación química los parámetros más usuales son: 

   - **_-2_** 

- **_Sulfuros S-2_** : son producto de la descomposición de la materia orgánica e indica generalmente contaminación séptica en el agua. 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

8 

Provienen del drenaje de minas, aguas estancadas y aguas residuales de fuentes industriales. La presencia de sulfuros en aguas superficiales y bien oxigenadas es muy escasa, en cambio es frecuente  en aguas subterráneas, especialmente en aguas termales. 

- **_-2_** 

- · **_Sulfatos SO4_** : su presencia es normal en la mayoría de las aguas naturales como consecuencia del arrastre y disolución de los yesos. Pero un valor aumentado de la concentración de sulfatos en una muestra de agua es indicativo de vertidos de aguas residuales. Concentraciones elevadas de sulfatos en agua producen efecto laxante y proporcionan sabor amargo. 

- **_Nitrógeno N_** : El nitrógeno se encuentra en el aire y a través de transformaciones que **_2_** ocurren en el ciclo del nitrógeno, algunas naturales y otras por causas antrópicas, se presenta en diversas formas químicas tanto en el agua natural como en el agua contaminada: 

- **_-Nitrógeno orgánico_** . Es un nutriente indispensable en el desarrollo de organismos fotosintéticos.  Su presencia en exceso causa **_eutrofización_** _(abundancia excesiva de nutrientes)_ de las aguas. Habitualmente se determina el NTK o nitrógeno total Kjeldahl que incluye el nitrógeno procedente de compuestos orgánicos como los fertilizantes y el nitrógeno amoniacal. Proviene de fertilizantes, aguas residuales y algunas algas microscópicas. 

- **_Nitrógeno amoniacal_** . Indica degradación de la materia orgánica. El nitrógeno   orgánico 

- se transforma fácilmente en nitrógeno amoniacal por acción química o bacteriana de sustancias presentes en las aguas residuales.  Se considera no aceptable su presencia en agua potable. 

   - 

   - **_-Nitritos_** (NO2 ). Su presencia en aguas podría indicar contaminación fecal o vertidos industriales. Para determinar esto será necesario tener en cuenta los contenidos de nitratos, de nitrógeno amoniacal, de materias orgánicas y el examen bacteriológico. 

   - 

   - **_-Nitratos_** (NO3 ).  Los nitratos provienen de las transformaciones químicas del nitrógeno orgánico y de los nitritos .Su exceso indica contaminación agrícola. Tanto los nitratos como los nitritos pueden causar varios efectos sobre la salud: disminución en la capacidad de transporte de oxígeno por la sangre (nitrito), disminución del funcionamiento de la glándula tiroidea, bajo almacenamiento de la vitamina A (nitrato), producción de nitrosaminas, las cuales son conocidas como una de las más comunes causas  de cáncer (nitratos y nitritos) 

- **Oxígeno Disuelto (OD)** es la cantidad de oxígeno que está disuelto en el agua de las fuentes naturales, de las cuales depende la vida acuática. La mayor parte del oxígeno 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

9 

- **Demanda Química de Oxígeno (DQO):** se usa para determinar la concentración de materia orgánica en el agua. Se fundamenta en la oxidación de la materia orgánica contenida en el agua mediante un oxidante químico, dicromato de potasio K Cr O . En 2 2 7 este método a diferencia de la DBO (demanda biológica de oxigeno) que solo mide la materia orgánica biodegradable por acción bacteriana, se determina toda la materia orgánica presente en el agua. Por eso los valores de DQO siempre son mayores que los valores de DBO. Esta determinación no es aplicable al agua potable. 

- **_Metales:_** El término genérico “[[Buscador_Papers_Biofiltros_de_eucalipto_y_cuyinaza_para_remocion_de_metales_pesados|metales pesados]]” se refiere a ciertos metales de alta densidad (mayor de 4g/mL) que son tóxicos para los seres humanos. Los metales pesados más conocidos son plomo, cobre, cadmio, níquel, mercurio y talio. En esta clasificación se incluyen también arsénico (metaloide) y el selenio (no metal). 

Los metales pesados son componentes naturales de la corteza de la tierra. Son bioacumulativos y no se degradan. Pueden llegar a los organismos vivos por   el alimento, el agua potable y el aire. Algunos metales pesados en concentraciones de trazas son esenciales para los humanos pero en concentraciones altas son sumamente tóxicos. 

- **-3** 

- · **Fosfatos (PO4 )** : Al igual que los nitratos, son sustancias solubles en agua necesarias para el desarrollo de las plantas pero en exceso producen crecimiento excesivo de algas, las que consumen grandes cantidades de oxígeno disuelto y causan la muerte de otros seres vivos como peces y otras plantas  degradándose así la calidad del agua. 

- **Detergentes** : Producen espumas y añaden fosfatos al agua. El principal problema 

- ambiental de los detergentes son los aditivos que contienen, como blanqueadores, bactericidas, perfumes y sulfatos. Su presencia en aguas naturales altera la transferencia y la disolución del oxígeno entre la superficie del agua y el aire dificultando la autodepuración de la fuente de agua. Provienen de aguas residuales domésticas e industriales. 

- **Fenoles** : Provienen de la industria petroquímica y farmacéutica como materia prima o 

- como subproductos. Su presencia en el agua es señal de contaminación por desechos industriales. Al reaccionar con otras sustancias, como el cloro, forman compuestos que dan al agua mal olor y sabor. 

- **Hidrocarburos:** Provienen de vertidos industriales  y producen cambios en las características organolépticas del agua. Se esparcen rápidamente sobre la superficie del agua ocupando áreas muy extensas e impidiendo la interacción entre  la atmósfera y la vida acuática. 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

10 

**_Contaminación Biológica_** La contaminación biológica ocurre principalmente por excrementos humanos y animales, y por aguas residuales. Algunos de estos contaminantes pueden ser patógenos y otros no, aunque estos últimos en ocasiones pueden afectar la salud de ciertas personas con defensas bajas. Entre los contaminantes biológicos se encuentran: Virus (como el de la hepatitis), bacterias (como la salmonella, escherichia coli, vibrio cólera, la que produce el cólera), hongos y parásitos. 

Uno de los indicadores de contaminación biológica del agua es la cantidad de oxígeno disuelto (OD) mencionada anteriormente, debido a que las bacterias y otros microorganismos utilizan oxígeno para reacciones biológicas. Por lo tanto, el grado de contaminación está relacionado con la cantidad de oxígeno presente en el agua. Otro indicador es la Demanda Biológica de Oxigeno, que se utiliza para determinar el grado de contaminación en cualquier tipo de agua donde se sospeche la presencia de una cantidad significativa de contaminantes biológicos. Como análisis específicos se utilizan las pruebas para coliformes totales, número más probable de coliformes (NMP), número más probable de estreptococos fecales. 

- **Demanda Biológica de Oxígeno (DBO)** mide la cantidad de materia consumida por microorganismos presentes en las aguas. Consiste en medir la cantidad de oxígeno disuelto en una muestra al inicio y al final de cinco días de tratamiento (DBO ). 5 

- **_Coliformes Totales_** El grupo coliforme abarca los géneros Klebsiella, Escherichia, Enterobacter, Citrobacter y Serratia. La determinación de coliformes totales se utiliza para determinar la efectividad de los tratamientos a que se somete el agua destinada al consumo humano. La presencia de bacterias coliformes indica que el agua puede estar contaminada con aguas negras ya que los coliformes fecales, un tipo de bacterias coliformes, se encuentran en los intestinos de humanos  y animales. Su presencia indica contaminación fecal reciente. 

- **_Estreptococos Fecales_** indican contaminación fecal antigua. La relación entre coliformes fecales (CF) y estreptococos fecales (EF) indica si la contaminación fecal proviene de fuentes humanas o de animales. 

- **_Escherichia coli_** La bacteria E. coli reside en los intestinos humanos y de animales. Hay varias clases de E. coli; algunas son dañinas, otras no. Las frutas y los vegetales pueden ser contaminados con E. coli cuando tienen contacto con estiércol contaminado de vacas. Las personas pueden transmitir asimismo la infección de E. coli. 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

11 

## **2. AIRE** 

#### **2.1 Introducción** 

La capa más interna de la atmósfera, la más cercana a la superficie terrestre, recibe el nombre de **_troposfera_** y contiene aproximadamente el 75% del aire de la tierra. Esta capa es la responsable del clima del planeta Tierra. En ella el aire está en movimiento ascendente y descendente. La segunda capa, a continuación de esta, es la **_estratosfera,_** donde el aire está en calma. Estas dos capas son las más importantes para el análisis de la contaminación atmosférica. 

El aire de la troposfera es una mezcla de nitrógeno (78%) y oxígeno (21%);  el 1% restante se compone de gases como el dióxido de carbono, argón, neón, helio, hidrógeno, otros gases y vapor de agua (según la zona del planeta). Estos son los componentes fijos del aire. En la estratosfera, la composición del aire es similar a la de la troposfera excepto que el contenido de vapor de agua  es mucho menor y el de ozono es muchas veces mayor. 

En la zona más baja de la estratosfera, como consecuencia de la transformación de oxigeno (O ) en ozono (O )  y de este de nuevo en oxígeno, a causa de reacciones químicas inducidas 2 3 por la radiación ultravioleta que viene del sol, se forma una capa fina pero muy concentrada de ozono. 

O 2 ↔O 3 

Esta **_capa de ozono_** evita que la radiación ultravioleta dañina que procede del sol alcance la superficie de la tierra. La capa de ozono que envuelve la tierra absorbe aproximadamente el 99% de las radiaciones UV del sol. Es decir, que la presencia de ozono en la estratosfera es beneficiosa para la salud; en cambio si se encuentra en la troposfera, actúa como contaminante con efectos dañinos para la salud. Las sustancias químicas presentes en la atmósfera son determinantes de las temperaturas de la tierra y, por tanto, del clima. 

### **2.2 Contaminación del Aire** 

La contaminación del aire es causada por la emisión hacia la atmósfera de sustancias químicas y otras partículas. La mayor proporción de estos contaminantes la aportan los motores de automóviles y las actividades industriales. Los contaminantes del aire se consideran **_primarios_** si proceden directamente de la fuente de emisión, y **_secundarios_** si provienen de reacciones químicas de los contaminantes primarios con sustancias presentes en la atmósfera. Los contaminantes primarios más comunes son monóxido de carbono (CO), óxidos de nitrógeno (NOx), dióxido de azufre (SO ) 2 , clorofluorocarbonos (CFCs), hidrocarburos y material particulado. Entre los contaminantes * secundarios se encuentran (O ). ozono atmosférico; oxidantes fotoquimicos (Cl ) e hidrocarburos 3 oxidados. 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

12 

Los contaminantes que se encuentran normalmente en todas las zonas urbanas, en concentraciones variables dependiendo de la actividad industrial y del tráfico, se llaman contaminantes de referencia y son seis: monóxido de carbono (CO), óxidos de nitrógeno (NOX), ozono atmosférico (O ), óxidos de 3 azufre (SOX), material particulado (PM-10) e hidrocarburos. 

- **_Monóxido de carbono (CO)_** es un gas incoloro e inodoro, muy tóxico, que se produce por la combustión incompleta de los derivados del petróleo, madera y otras sustancias combustibles. Una exposición moderada a monóxido de carbono puede causar la muerte en corto tiempo porque elimina al oxígeno en la hemoglobina de la sangre. La fuente principal de emisiones de este gas a la atmósfera son los vehículos de motor (70% emisiones), plantas eléctricas, motores industriales, etc. La producción natural de CO es muchas veces mayor que la de origen antropogénico y proviene de la oxidación del metano CH en la troposfera4 . 

- **_Oxidos de nitrógeno (NOX)_** es el nombre con que se conocen varios compuestos formados por la combinación de nitrógeno y oxigeno en diferentes proporciones: monóxido de dinitrógeno (N O), monóxido de nitrógeno (NO), trióxido de di nitrógeno (N O ), dióxido de di 2 2 3 nitrógeno (NO ), penta óxido de di nitrógeno (N O ). Son emitidos a la atmosfera por los 2 2 5 vehículos de motor (principalmente diesel), quema de combustibles fósiles, soldaduras por arco y otras actividades antropicas. De manera natural se producen por oxidación del 

Nitrógeno atmosférico (N ) a elevadas temperaturas. Su presencia en la atmósfera contribuye 2 a la formación del “ **_smog fotoquímico”,_** fenómeno característico de las grandes ciudades con alto tránsito vehicular. 

El smog fotoquímico es una niebla de color pardo rojizo producto de reacciones químicas, inducidas por la luz solar, en las que intervienen óxidos de nitrógeno, ozono troposférico y compuestos orgánicos volátiles (COVs). Este fenómeno se produce en condiciones climáticas y geográficas determinadas, en zonas con alto tráfico vehicular y escaso movimiento de aire. Produce serios problemas respiratorios. 

- **_Dióxido de azufre (SO ) 2_** es un gas incoloro con olor asfixiante que se emite a la atmosfera como consecuencia de la quema de combustibles fósiles y de actividades mineras, también es emitido por las erupciones volcánicas. En la atmósfera, al reaccionar con el agua, este gas es el responsable de la formación de la **_“lluvia_ ácida** **_”_** que causa daño a las construcciones de piedra, a las tierras de cultivo, y a los  bosques y a la vida acuática. 

- Los  cloro fluocarbonos ( **_CFCs)_** son gases formados por átomos de carbono, flúor y cloro, que se utilizan como refrigerantes, aislantes térmicos y aerosoles (spray). Luego de ser liberados permanecen en la atmósfera entre 50 y 100 años, donde por acción de la radiación ultravioleta del sol  liberan radical cloro (Cl*), contribuyendo a la destrucción de la capa de ozono. 

- **_Hidrocarburos:_** _son gases formados por carbono e hidrógeno y que_ se producen por la combustión incompleta de combustibles fósiles, por el uso de derivados del petróleo como gasolina y solventes orgánicos, incendios, descomposición de materia orgánica y reacciones químicas que tienen lugar en la atmósfera. Junto con los óxidos de nitrógeno participan en la formación del smog foto químico. 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

13 

Los **_compuestos orgánicos_** constituyen por mucho, la mayoría de los contaminantes que se encuentran en la atmósfera. Se clasifican según su presión de vapor (a mayor presión de vapor mayor tendencia a evaporarse) a 25 C como:0 

- **_Compuestos Orgánicos Volátiles (COVs):_** están presentes en el aire en fase gaseosa -2 

- (P >10  kPa). 0 

   - -8 

- **_Compuestos Orgánicos No Volátiles (CONVs):_** existen como aerosoles (P < 100 

- kPa). 

- **_Compuestos Orgánicos Semi Volátiles (COSVs)_** : pueden existir tanto en una fase -8 -2 

- como en la otra. ( 10 < P <10 kPa).0 

- **_Material particulado:_** El material particulado atmosférico se define como un conjunto 

- de partículas sólidas y/o líquidas (a excepción del agua pura) presentes en suspensión en la atmósfera (Mészáros,1999). Este es un concepto amplio que engloba las partículas en suspensión y  las partículas sedimentables (diámetro > 20 μm), caracterizadas por un corto tiempo de residencia en la atmósfera (varias horas). El material particulado se clasifica como PM-10 y PM-5 , según que el diámetro de la partícula sea igual o menor que 10 micras o igual o menor que 2.5 micras 

El **_Efecto Invernadero (greenhouse effect)_** , llamado así por su similitud con lo que se observa en un invernadero, es el fenómeno natural mediante el cual algunos gases presentes en la atmósfera retienen una parte de la energía calórica emitida por el suelo, la cual es previamente absorbida por este de la radiación solar. Este fenómeno es el que regula la temperatura de la Tierra manteniéndola en el margen donde es posible la vida. 

Los principales gases responsables de este efecto natural, conocidos como gases invernadero ( **GEI** ) son: el vapor de agua (H O), el dióxido de carbono (CO ),el  metano (CH ), los óxidos de nitrógeno 2 2 4 (NOX), el ozono (O ) y los clorofluorocarbonos (CFC). Aunque el efecto invernadero es esencial para la 3 vida en el planeta, un exceso en la atmosfera terrestre de los gases invernadero, debido a actividades entrópicas está causando un aumento de la temperatura global media. La mayor aportación al aumento del efecto invernadero entrópico corresponde al CO , seguido del CH . El primero tiene un 2 4 tiempo de residencia en la atmósfera de 15 años y el segundo de 8 a 10 años. 

Las Normas Ambientales de Calidad del Aire y Control de Emisiones establecen límites para la concentración de estos gases en la atmosfera.( Anexos 2 o consultar la página web del Ministerio). 

### **3. RUIDO** 

## **3.1 Contaminación por Ruido** 

Ruido es cualquier sonido inadecuado que puede afectar la salud o calidad de vida de las personas. Sus efectos pueden variar desde una molestia moderada hasta la pérdida permanente de la audición. También hay un impacto ecológico negativo del ruido sobre especies sensibles a este. Niveles excesivos de ruido por tiempo prolongado podrían causar daños a la audición y al sistema nervioso. Las fuentes más comunes de contaminación por ruido son el tráfico y la actividad industrial y comercial. 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

14 

El ruido se puede emitir desde un foco puntual (un abanico), un foco espacial (una discoteca o una actividad multitudinaria) o un foco lineal (un avión o un tren en movimiento). 

El nivel de ruido se mide con un medidor de ruido o decibelímetro. El decibel (dB) es la unidad que se utiliza para esto. Para dar una idea, en una habitación insonorizada como un estudio de grabación, el nivel de ruido es inferior a 25 dB. 

Las Normas Ambientales para la Protección contra Ruidos del Ministerio de Medio Ambiente clasifican los niveles de ruido continuo y su efecto en los humanos. También  establecen los niveles máximos permitidos como estándares de contaminación sónica. (Anexos  3 o consultar la  página web del Ministerio) 

### **4. MUESTREO Y ANÁLISIS** 

## **4.2 Introducción** 

Las preguntas más frecuentes en muestreo y análisis ambiental son: qué tipo de muestra y cuántas se necesitan. Una investigación ambiental debe incluir dos tipos básicos de muestras: 1)muestras que se usan para evaluar las clases y niveles de contaminantes presentes en el medio ambiente del área y 2)muestras para control de calidad ( patrones) para evaluar la precisión del sistema de medición utilizado, incluyendo el laboratorio y el muestreo. 

Las muestras deben ser representativas del medio ambiente del lugar que está siendo estudiado. El propósito del muestreo es evaluar una pequeña pero informativa porción de un todo y realizar inferencias con los datos colectados. Por ejemplo, si se encuentra mercurio en muestras de suelo y de agua superficial en un área de estudio, puede inferirse que el resto de suelo y agua contiene mercurio en cantidades similares. Si solo se toman muestras de suelo no puede afirmarse que el agua del río también contiene mercurio. Las muestras de suelo no son representativas por sí solas del agua del río. Por lo tanto, para una adecuada evaluación del medio ambiente en determinado lugar, deben tomarse muestras de diferentes matrices. 

Las matrices primarias en muestreo ambiental incluyen agua, suelo, biota, aire, desechos sólidos y desechos líquidos. Cada una de estas matrices primarias tiene múltiples. Por ejemplo, las muestras de agua pueden ser de río, lagos, lluvia, subterráneas, estuarinas, desechos industriales o del mar. Las muestras de suelo pueden ser arena o arcilla; las de biota, animales o plantas; las de aire, de interior o de exterior; las de desechos sólidos, lodos y cenizas, y las de desechos líquidos pueden ser más densas o menos densas que el agua. También pueden muestrearse combinaciones de estas matrices como sedimentos acuosos del fondo de un lago o corriente de agua, materia particulada en aire, aerosoles en aire, etc. 

Serán seleccionadas aquellas matrices que más interesen de acuerdo al contaminante en cuestión. Por ejemplo, para determinar contaminación por insecticidas, el contaminante de interés sería el insecticida y considerando sus características fisicoquímicas; el suelo, el sedimento y las hojas del follaje (que fijarían el insecticida volatilizado), podrían ser las matrices de mayor interés. Conclusión, las características del contaminante definirán las matrices. 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

15 

Por otra parte, del contaminante o anualito que se desea  determinar, dependerá el equipo que se utilice en el muestreo y el tratamiento para preservar la muestra que será enviada al laboratorio para analizarlo posteriormente. Por ejemplo las muestras para analizar  los metales pesados, los compuestos orgánicos volátiles, semi volátiles y no volátiles requieren  diferentes tipos de contenedores, condiciones de pH y protección del calor, de la luz y del aire como parte de su preservación. 

En resumen, si la muestra no es representativa del área estudiada y /o los métodos de muestreo, preservación y análisis de las muestras no son adecuados, los datos obtenidos del análisis no tienen sentido. Por ejemplo, ¿de qué le sirve a un laboratorio analizar con alta exactitud y precisión  bifenilos policlorinados (PCBs) en muestras de aguas de un lago, si la mayoría de estos se adsorben en los sedimentos acuosos? Los datos no serán representativos del ecosistema. Otro ejemplo seria analizar compuestos orgánicos volátiles,  como benceno y tolueno en suelos sin utilizar un método de muestreo y preservación que impida que estos se volatilicen antes de llegar al análisis. 

Generalmente el método de análisis recomienda el cuidado de las condiciones de muestreo y preservación de las muestras. El anteproyecto de Norma de Calidad de Agua de Cuerpos Hídricos y Superficiales del Ministerio de Medio Ambiente y Recursos Naturales, que actualmente se encuentra en proceso de revisión, y  la Norma Ambiental de Calidad de Aire (junio 2003) establecen los procedimientos y las medidas para la toma de muestras.  (Anexos 4) 

### **4.2 Cadena de Custodia.** 

Son las medidas que deben adoptarse para  preservar la identidad de las muestras de cualquier especie, garantizando la eficacia del proceso de análisis, los resultados y las conclusiones. A través de estas medidas se asegura que la muestra no ha sido alterada o cambiada por otra y se establecen responsabilidades a lo largo del plan de muestreo. 

Las etapas de la cadena de custodia son las siguientes: 

1.  Toma de la muestra (según el  plan elaborado previamente). 

2. Preservación y embalaje de la muestra (según los parámetros que se propone a analizar). 

3. Transporte o traslado de la muestra. 

4. Entrega de las muestras a los laboratorios para su análisis. 

5. Custodia y preservación final de la muestra hasta que se realice el debate. 

(Anexos 5) 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

16 

**5-Manejo Estadístico de Datos Ambientales** 

### **_Contenidos del entrenamiento para el Análisis de Datos Estadísticos manual y automático._** ( **Se utilizará el programa de excel para cálculos estadísticos)** 

1. Conceptos que se deben manejar en estadística. 

2. Calculo manual de la media, varianza, desviación estándar, coeficiente de variación, etc. 

3. Calculo de la media, varianza, desviación estándar, coeficiente de variación usando la calculadora. 

1. Introducción al manejo de la estadística básica con Excel. 

   - 1.1 Estructura y opciones generales del programa. 

   - 1.2 Ventanas de Excel. 

   - 1.3 Menú principal. Barra de herramientas. Barra de estado. 

      - 1.3.1 Menú principal 

      - 1.3.2 Barra de herramientas. 

      - 1.3.3 Barra de estado. 

   - 1.4 Procedimiento básico para un análisis estadístico. 

      - 1.4.1 Seleccionar un archivo de datos. 

      - 1.4.2 Seleccionar un procedimiento estadístico. 

      - 1.4.3 Seleccionar las variables y opciones para el análisis. 

      - 1.4.4 Ventana de salida. 

2. Archivos de datos. 

   - 2.1 Archivos de datos en Excel. 

      - 2.1.1 Crear un archivo. 

      - 2.1.2 Abrir un archivo. 

      - 2.1.3 Tipos de archivos de datos que reconoce Excel 

      - 2.1.4 Guardar un archivo. 

3. Aplicaciones de la función Excel en la elaboración de cuadros o tablas. 

4. Aplicaciones de la función Excel en el cálculo de los principales indicadores de los estadísticos. 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

17 

**6-Referencias bibliográficas** 

1. Bioagrolab www.bioagrolab.com  Marzo 2011. 

2. Depuradoras verdes. Contaminación del agua. www.extec.es .Marzo 2011. 

3. Duke, Catherine; Craig,Williams.Chemistry for Environmental and Earth Sciences. 2008.CRC PRESS, Boca Raton, Fl. 

4. Ecoagua educasitios.educ.ar Julio 2011. 

5. Keith, Lawrence, editor. Principles of Environmental Analysis . 2nd edition 1996. Series American Chemical Society  Washington, DC. 

6. Kiely, Gerad. Ingeniería Ambiental. 1ra edición en español 1999. Mc Graw Hill España. 

7. Lenntech. Water Treatment Solutions. www.lennecht.es/metales-pesados.htm. 

8. Medición de la Calidad del Agua. Comisión Nacional del Agua y el Instituto Mexicano de Tecnología del Agua.  www.bvsde.paho.org  Julio 2011. 

   - ta 

9. Miller, G.Tyler.(2003) Ciencia  Ambiental 5 edición. Thomson Learning.ta 

- 10.Revista Ambientum Febrero 2002  www.ambientum.com. 

11. Ministerio de Medio Ambiente y Recursos Naturales. Junio 2003. Norma ambiental sobre Calidad de Aire y Control de Emisiones. www.ambiente.gov.do. 

- 12.Ministerio de Medio Ambiente y Recursos Naturales. Junio 2003.Anteproyecto Norma Calidad de Agua de Cuerpos Hidricos Superficiales. Reunión Técnica Final de Norma Calidad de Agua. Programa de Proctección Ambiental. Febrero 2011. 

- 13.Ministerio de Medio Ambiente y Recursos Naturales. Junio 2003.Norma ambiental sobre Calidad del Agua y Control de Descargas. www.ambiente.gov.do. 

- 14.Revista Ambientum Febrero 2002  www.ambientum.com. 

- 15.Spiro, Thomas; Stigliani, William. Quimica Medioambiental 2da edición 2004, Pearson Educacion. Madrid, Espana. 

- 16.Stoker, H.; Seager,Spencer. Quimica Ambiental Contaminacion del aire y del agua.Edicion Espanola 1981. Editorial Blume. Barcelona, España. 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

18 

# 7-ANEXOS 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

19 

### **Equipos que se deben utilizar durante las prácticas de este curso-taller:** 

- Medidor de oxígeno disuelto (OD) 

- Conductímetro y medidor de sólidos totales disueltos(TDS) 

- Medidor de pH (peachímetro)para medir el grado de acidez del agua 

- Turbidímetro (para determinar el grado de turbidez del agua) 

- Espectrofotómetro UV-visible y de Absorción Atómica (para determinar sulfatos, nitritos, nitrógeno amoniacal y  metales) 

- Decibelímetro  (para medir intensidad de ruido) 

- Muestreador de alto volumen para determinar material particulado (PM) 

- Analizador de emisiones de  combustión (para gases producidos por combustión) 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

20 



PROGRAMA DE PROTECCIÓN AMBIENTAL 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

21 

Ministerio de Medio Ambiente y Recursos Naturales 



PROGRAMA DE PROTECCIÓN AMBIENTAL 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

22 

Ministerio de Medio Ambiente y Recursos Naturales 



PROGRAMA DE PROTECCIÓN AMBIENTAL 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

23 

Ministerio de Medio Ambiente y Recursos Naturales 



PROGRAMA DE PROTECCIÓN AMBIENTAL 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

24 

PROGRAMA DE PROTECCIÓN AMBIENTAL 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

25 



> MANUAL DEL CURSO DE MONITOREO AMBIENTAL 26 



MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

27 



<!-- Start of picture text -->
Turbidez<br>DBO5<br>DQO<br>Nitrógeno Amoniacal<br>Nitrógeno de Nitrato<br>Nitrógeno de Nitrito<br>FÓsforo Total<br>SST<br>Grasas y Aceites<br>Fenoles<br>Benceno<br>Cianuro<br>Hidrocarburos Totales<br>Arsénico<br>Mercurio<br>Cobre<br>Plomo<br>Cromo<br>Cadmio<br>Zinc<br>Níquel<br>Coliformes  Fecales<br>Coliformes Totales<br>Enterococos<br>Núm.<br>Fecha:<br>Cód.<br>pTomada or:<br>Recibida en Lab por:  Entregada a Lab. por: Desc. gLuar del Muestreo:<br>poTi<br>Fecha: Fecha:<br>Fecha<br>Hora: Hora: Hora<br>Vol.<br>Firma  Firma<br>DEPARTAMENTO DE MONITOREO<br>DIRECCIÓN DE CALIDAD AMBIENTAL<br>VICEMINISTERIO DE GESTIÓN AMBIENTAL<br>Institución Institución<br>QFísico-uímicos<br>Parámetros<br>gMicrobiolóicos<br><!-- End of picture text -->

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

28 

##### **Ministerio de Medio Ambiente y  Recursos Naturales Viceministerio de Gestión Ambiental Dirección de Calidad** 

##### **Formulario de muestreo de para calidad de Agua** 

Localización: ________________________________________ Muestra no.  1: __________________________________ Procedencia: ________________________________________      Muestra no.  2: __________________________________ Fecha: _____________________________________________      Muestra no.  3: __________________________________ Muestra tomada por: __________________________________      Muestra no.  4: __________________________________ 

Muestra no.  5: _________________________________ 

||**1**|**2**|**3**|**4**|**5**|
|---|---|---|---|---|---|
|**Caract. y anal.**|Hora:|Hora:|Hora:|Hora:|Hora:|
|Cond. Climáticas||||||
|Oleaje / corriente||||||
|Vegetación||||||
|Tamaño||||||
|Arena (Text./ Color)||||||
|Topografía||||||
|Coordenadas||||||
|PH||||||
|Temperatura||||||
|Oxígeno disuelto||||||
|Salinidad||||||
|Conductividad||||||
|Sólidos totales<br>disueltos||||||



Observaciones:_______________________________________________________________ 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

29 



<!-- Start of picture text -->
Turbidez<br>DBO5<br>DQO<br>Nitrógeno Amoniacal<br>Nitrógeno de Nitrato<br>Nitrógeno de Nitrito<br>Fosforo Total<br>SST<br>Grasas y Aceites<br>Fenoles<br>Benceno<br>Cianuro<br>Hidrocarburos Totales<br>Arsénico<br>Mercurio<br>Cobre<br>Plomo<br>Cromo<br>Cadmio<br>Zinc<br>Níquel<br>Coliformes  Fecales<br>Coliformes Totales<br>Enterococos<br>Núm.<br>pTomada or:  Fecha:<br>Cód.<br>Recibida en Lab por:  Entregada a Lab. por: gLuar del Muestreo:<br>Desc.<br>poTi<br>Fecha: Fecha:<br>Fecha<br>Hora: Hora: Hora<br>Vol.<br>Firma  Firma<br>DEPARTAMENTO DE MONITOREO<br>DIRECCION DE CALIDAD AMBIENTAL<br>QFísico-uímicos VICEMINISTERIO DE GESTION AMBIENTAL<br>Institución Institución<br>Parámetros<br>gMicrobiolóicos<br><!-- End of picture text -->

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

30 

AUTORES: 

Licda. Carmen Leticia Mendoza Gómez, MSc; Lic. Arismendis Gómez, MSc; Lcda. Carmen Sánchez Pujols, MSc Lic. Fidel Díaz Ferreras, MSc. 

### FICHA TECNICA: 

Dr. José Contreras, Ph.D. Licda. Ligia Ramirez Muñoz, MSc Licda. Jeannette Hache Campos, MSc. 

MANUAL DEL CURSO DE MONITOREO AMBIENTAL 

31 

> MANUAL DEL CURSO DE MONITOREO AMBIENTAL 32 



---
**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]
