---
tags:
  - master_ia
  - teoria
source: MIA_A3_Mod7_IA en la Era del Cloud Computing.pdf
---

**Módulo IA en la Era del Cloud Computing** 



# **Módulo IA en la Era del Cloud Computing** 

|**1. INTRODUCCIÓN AL MUNDO CLOUD. TIPOS DE ENTORNO ..............................03**<br>|
|---|
|1.1. INTRODUCCIÓN AL MUNDO CLOUD ..............................................................03|
|1.2. TIPOS DE ENTORNOS CLOUD .........................................................................10<br>|
|1.2.1 CLOUD PÚBLICO. .....................................................................................10|
|1.2.2 CLOUD PRIVADO .....................................................................................13<br>|
|1.2.3 CLOUD HÍBRIDO ......................................................................................16|
|1.2.4 COMPARATIVA ENTRE ENTORNOS ...........................................................20|
|1.2.5. CASOS DE USO POR ENTORNO ...............................................................21|
|1.3. CONCEPTO DE ENTORNO MULTICLOUD .........................................................32|
|1.3.1. ¿QUÉ ES UN ENTORNO MULTICLOUD? ...................................................32|
|1.3.2. ¿POR QUÉ ADOPTAR UNA ESTRATEGIA MULTICLOUD? ...........................39|
|1.3.3. RETOS EN LA IMPLEMENTACIÓN DE ENTORNOS MULTICLOUD. ..............43<br>|
|1.3.4. SOLUCIONES TECNOLÓGICAS A NIVEL IT - IA Y OTRAS ..........................46|
|1.3.5.DISEÑOS ..................................................................................................51|
|1.3.6. ESCENARIO COMÚN EN LA ADOPCIÓN DE UNA ESTRATEGIA<br>MULTICLOUD. CASO DE USO............................................................................54<br>|
|1.3.7. APLICACIÓN Y GESTIÓN DE UNA INFRAESTRUCTURA MULTICLOUD .......55|
|1.3.8. OPTIMIZACIÓN USANDO ENTORNOS MULTICLOUD ................................56<br>|
|1.4. PROVEEDORES DE SERVICIOS CLOUD. VISIÓN GENERAL ................................58<br>|
|1.5. BEST PRÁCTICES DEL CONSUMO CLOUD. GENERAL ......................................63|
|1.6. RESUMEN DEL APARTADO Y ACTIVIDADES DE FORTALECIMIENTO DEL<br>|
|CAPÍTULO .............................................................................................................66<br>|
|**2. APIS DE VISIÓN ARTIFICIAL Y NPL ......................................................................70**|
|2.1. HERRAMIENTAS DE PYTHON ..........................................................................74|
|2.2. HERRAMIENTAS NODE ...................................................................................76|
|2.3. HERRAMIENTAS JAVA .....................................................................................77|
|**3. PROVEEDORES SERVICIOS CLOUD Y APLICACIONES DEDICADAS A LA IA .....81**|
|3.1. AMAZON  ......................................................................................................82<br>|
|3.1.1. ANÁLISIS DE DATOS CON AWS ...............................................................83|
|3.1.2. SERVICIOS DE IA CON AWS ....................................................................92|
|3.2. GOOGLE CLOUD ............................................................................................93|
|3.2.1. DESARROLLO CON IA .............................................................................95|
|3.2.2. IA CONVERSACIONAL .............................................................................98|
|3.2.3. IA PARA DOCUMENTOS ........................................................................100|
|3.2.4. IA PARA SECTORES EMPRESARIALES .....................................................101|
|3.3. IBM ..............................................................................................................103<br>|
|3.3.1. ¿QUÉ ES IBM WATSON? ........................................................................108|
|3.3.2. APLICACIONES DE IA / MACHINE LEARNING DE IBM ............................109|
|3.4. MICROSOFT .................................................................................................130|
|3.4.1. SERVICIOS DE IA APLICADA DE AZURE  ................................................136|
|3.4.2. AZURE COGNITIVE SERVICES  ...............................................................142|
|3.4.3. AZURE MACHINE LEARNING  ................................................................144|
|3.4.4. INFRAESTRUCTURA PARA INTELIGENCIA ARTIFICIAL COMO SERVICIO  .146|
|3.5. ALIBABA  .....................................................................................................148|



|**4. CONTENEDORES Y MICROSERVICIOS ORIENTADOS A LA IA .........................150**<br>|
|---|
|4.1. VISIÓN GENERAL DE LOS MICROSERVICIOS: BENEFICIOS E|
|INCONVENIENTES ................................................................................................151<br>|
|4.2. MIGRACIÓN DE ARQUITECTURAS NATIVAS MONOLÍTICAS A|
|MICROSERVICIOS ................................................................................................154|
|4.3. IMPLEMENTACIÓN DE MICROSERVICIOS ......................................................155|
|4.4. MICROSERVICIOS SIN ESTADO VS MICROSERVICIOS CON ESTADO ..............156|
|4.5. SERVERLESS: BENEFICIOS E INCONVENIENTES ..............................................156|
|4.6. ENFOQUE HÍBRIDO CON SERVERLESS ...........................................................159|
|4.7. INTRODUCCIÓN FUNCTION AS A SERVICE (FAAS) ........................................160|
|4.8. INTRODUCCIÓN A SERVICE MESH Y TIPOS ...................................................161|
|4.9. INTRODUCCIÓN A ISTIO ...............................................................................162|
|4.10. EL CAMINO A LAS APLICACIONES ALOJADAS EN LA NUBE. RED HAT<br>OPENSHIFT. .........................................................................................................165|
|4.11. RED HAT OPENSHIFT DATA SCIENCE ...........................................................167|
|4.12. ACTIVIDAD COMPLEMENTARIA. CONTENEDORES Y NPL ............................169|
|**CONCLUSIONES .....................................................................................................173**|
|**ANEXO. SOLUCIONES ACTIVIDADES FORTALECIMIENTO ...................................175**<br>|
|**BIBLIOGRAFÍA ........................................................................................................178**|



**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

## **1. Introducción al mundo Cloud. Tipos de entorno** 

_“El Cloud Computing o computación en la nube es una tecnología que permite el acceso remoto a servidores propios o de terceros con capacidad de cómputo, a servicios, softwares, almacenamiento de archivos y procesamiento de datos por medio de Internet. ”_ 

Los servicios de Inteligencia Artificial se ven potenciados en los entornos cloud por la flexibilidad y adaptabilidad que les brindan. Una de las limitaciones de la IA es la gestión de grandes volúmenes de información tanto en periodos de entrenamiento como en escenarios productivos, por lo cual requiere amplios servicios; desde infraestructura a capa aplicativa. 

Este módulo tiene como objetivo hacer una introducción a los fundamentos del Cloud Computing a la par que ligarlo a las aplicaciones, servicios y herramientas existentes en los principales proveedores de cloud pública para resolver problemas empresariales mediante la aplicación de Inteligencia Artificial. 

A lo largo de las próximas páginas, mediante casos de uso , ejercicios prácticos guiados y actividades complementarias se plantea temario útil para adquirir un conocimiento estratégico de negocio amplio a la hora de gestionar recursos IT , desde la capa de infraestructura IT a las decisiones relacionadas con las herramientas con las que ejecutar IA. 

### **1.1. Introducción al mundo Cloud** 

#### **¿Por qué surge la infraestructura cloud?** 

A efectos prácticos la infraestructura en la nube lleva existiendo tanto tiempo como el propio internet. Cuando en 1963 La Agencia de Investigación de Proyectos de Defensa Avanzados (DARPA) mostró al mundo una computadora siendo usada por más de una persona desde distintas localizaciones, el uso en remoto de una máquina comenzó a ser una realidad. En las décadas siguientes, las empresas comenzaron a emplear sistemas de cómputo descentralizados pero la limitación del ancho de red puso freno a la expansión de esta tecnología. 

04 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

A raíz de un incremento sustancial del ancho de banda en internet en la década de los 90, esta tecnología comienza su despegue. Los servicios de nube llegarían al gran público a finales del siglo pasado por medio de los servicios de correo y el alojamiento de páginas web. Aunque distan de los despliegues en cloud actuales, estos servicios suponen el empleo de infraestructura deslocalizada y por múltiples usuarios, encajando por tanto en la definición de Cloud Computing. Otros servicios que surgieron desde este momento basados en la computación en la nube fueron los servicios de almacenamiento de fotos (Flickr) o las redes sociales (MySpace). 

En la primera década del siglo XXI, ciertas empresas tecnológicas como Amazon, Google o Microsoft descubren que no están empleando toda su infraestructura disponible y deciden ponerla a disposición de terceros. Con servicios como [[Buscador_Papers_Biofiltros_de_eucalipto_y_cuyinaza_para_remocion_de_metales_pesados|Amazon Web Services]] o [[MOC_UDH_Academico|Microsoft Azure]] comienza la era de la computación en la nube, en la que empresas de cualquier tamaño o particulares pueden acceder a una gran variedad de infraestructuras y servicios que son propiedad de terceros y no se encuentran en sus instalaciones. 

En los últimos años las empresas han empezado a desplegar modelos de nube privada, que serán explicados más adelante. Estos modelos se basan en la utilización exclusiva de los recursos hardware necesarios para disponer de una infraestructura cloud, pero con la misma filosofía de ubicuidad, acceso remoto y deslocalización. 

#### **¿Qué es el cloud?** 

El Cloud Computing o computación en la nube es una tecnología que permite el acceso remoto a servidores propios o de terceros con capacidad de cómputo, a servicios, softwares, almacenamiento de archivos y procesamiento de datos por medio de Internet. Es por tanto una alternativa a la ejecución en una computadora personal o servidor local. En el modelo de nube, no hay necesidad de instalar aplicaciones localmente en computadoras, ni siquiera de tener la propiedad del hardware sobre el que se ejecutan las mismas. 

La computación en la nube ofrece a los individuos y a las empresas la capacidad de acceder a un conjunto de recursos de computación con un mantenimiento garantizado, de forma segura, con fácil acceso, fácilmente escalable y bajo demanda. 

#### **¿Qué nos ofrecen los entornos cloud?** 

Un entorno cloud no deja de ser un conjunto de recursos de hardware y una capa de software gestionados por un tercero. El cliente contrata un servicio con el proveedor de cloud que puede pasar por el acceso directo a una máquina o servidor determinado, o una serie de servicios que se mencionarán más adelante. 

Generalmente, los proveedores de cloud tendrán toda su infraestructura centralizada en los denominados CPD (Centros de Procesamiento de Datos). Son grandes instalaciones en las que se encuentra alojada la capa de infraestructura de cada proveedor cloud. 

05 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

El cliente tiene acceso a esta infraestructura o a los servicios que se ofrecen sobre la misma en función de un contrato con su proveedor cloud. Así obtiene una serie de ventajas respecto a adquirir y gestionar por sí mismo toda la infraestructura y servicios necesarios para el funcionamiento de su negocio. 

Por otra parte, aquella empresa que opte por tener la propiedad de la infraestructura física por medio de un despliegue privado podrá acoger la infraestructura en sus propias instalaciones o usar de forma exclusiva la infraestructura de un proveedor de cloud en sus centros de datos. 

Las principales ventajas de emplear modelos cloud son tanto económicas como organizativas. Por una parte, los modelos cloud eliminan la necesidad de una inversión inicial en infraestructura física que permita ejecutar la carga que el cliente desee. Con servicios como la Infraestructura como Servicio (IaaS), en cuestión de minutos se puede disponer de una máquina con las características requeridas (CPU, GPU, RAM, Almacenamiento, …) por la que solo se paga cuando se usa. Así se pueden acelerar plazos de despliegue y flexibilizar enormemente la inversión y facturación. 

Por otro lado, se elimina la necesidad de realizar un mantenimiento de dicha infraestructura o servicio. Los proveedores cloud ofrecen modelos de soporte completos y mantenimiento constante para que el cliente solo necesite centrarse en su negocio, sin la necesidad de gestionar de forma autónoma los recursos de bajo o alto nivel. 

Los servicios ofrecidos por un proveedor cloud pueden ser agrupados en tres categorías. Se listan a continuación en función de las capas de la infraestructura hardware y software que sean gestionadas por cada parte, cliente y proveedor. 

Además de las ventajas y beneficios que puede aportar el despliegue de una infraestructura cloud a las empresas actuales, contamos con un punto de innovación acelerado por la adopción y consumo de los servicios en la nube. Basándose y apoyando la transformación digital de las empresas, la nube puede impulsar el desarrollo de tecnologías como el IoT y la AI de forma más rápida. En definitiva, todo avance tecnológico (como lo es el uso de servicios cloud de todo tipo que más adelante veremos), trae consigo un mayor desarrollo de la inteligencia artificial, del Big Data, y del IoT. La nube comienza a tener más presencia en las empresas y poco a poco están apareciendo nuevos modelos como el Edge Computing para dotar de competitividad a las empresas desde el IT. Llegamos a la conclusión de que innovación es inherente a la nube por dos razones principales: 

> • El uso de computación cognitiva es uno de los usos más extendidos y consumidos en cloud para, por ejemplo, crear experiencias personalizadas a clientes de todos los sectores o la creación de tratamientos médicos de forma más rápida y concreta (entre otros casos de uso). Todo ello para explotar la gran volumetría de información accesible para las empresas. 

06 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- Las escasas barreras de entrada a recursos físicos (servidores y almacenamiento) puede agilizar el desarrollo de software, y por ende la proliferación y ejecución de ideas. Esto supone fomentar nuevas formas de negocio de grandes empresas y startups; arrancar nuevos proyectos, ahorrar costes y descentralizar recursos de gestión para centrarse en la innovación. 

#### **Infraestructura como Servicio (IaaS): Servidores autogestionados** 

La Infraestructura como Servicio o IaaS es un modelo por el cual un proveedor de cloud ofrece a sus clientes todas las ventajas que ofrecen los modelos tradicionales de despliegue on-premises (es decir, tener la propiedad y gestión de la capa de infraestructura) sin que esto implique una alta inversión inicial ni costes recurrentes de mantenimiento. En este modelo, el proveedor es el propietario de la infraestructura física y los clientes manejan las aplicaciones, los datos, los sistemas operativos, el middleware y los tiempos de ejecución. 

Por tanto, el proveedor ofrece las capas de virtualización, almacenamiento, red y servidores físicos. En este modelo de servicio el cliente se libera de la necesidad de tener un centro de datos on-premises, ni tiene la responsabilidad de actualizar o mantener físicamente estos elementos, con el ahorro de costes consecuente. 



07 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

En la mayoría de los casos, el cliente efectúa el control sobre la infraestructura a través de una interfaz de programación de aplicaciones (API) o de un panel de control proporcionado por el proveedor (Dashboard). Este modelo de nube como servicio es el más flexible, ya que facilita enormemente el escalamiento, la actualización y la incorporación de recursos permitiendo afrontar los costes del crecimiento de sus necesidades siempre por adelantado. 

En definitiva, en un modelo de Infraestructura como servicio, el proveedor gestiona la conexión a la red, el almacenamiento físico, el servidor y su virtualización. El cliente, por su parte, gestiona el Sistema Operativo, el middleware, las cargas de ejecución, la gestión de los datos y las aplicaciones e interfaces. 

#### **Plataforma como Servicio (PaaS)** 

En un modelo de cloud computing de Plataforma como Servicio o PaaS, el proveedor de cloud ofrece a su cliente un sistema de hardware y una plataforma de software en el que desarrollar, ejecutar y distribuir aplicaciones. La gran ventaja de este modelo frente al IaaS es que el cliente no solo se ve liberado de adquirir, alojar y mantener el hardware, sino que también evita gestionar todos los aspectos relacionados con el Sistema Operativo, el middleware y la configuración de la plataforma. De esta forma, se abstrae de los aspectos de más bajo nivel de la infraestructura que contrata. De esta manera, las empresas pueden acceder a pilas de soluciones a través de internet en las que sencillamente ejecutarán las aplicaciones que desarrollen y gestionarán los datos que estas requieran o generen. Otra ventaja del modelo PaaS es que permite un despliegue rápido y deslocalizado de cualquier aplicación, así como una escalabilidad y migración fáciles y rápidas. 

El proveedor de la plataforma será el encargado de gestionar la seguridad de la infraestructura y sus datos, así como de realizar copias de seguridad periódicas, facilitando aún más al cliente poner el foco en el desarrollo de su producto. Este modelo acelera enormemente el _time to market_ de una aplicación a la vez que reduce el riesgo por la inversión en una gran variedad de recursos. 

#### **Software como Servicio (SaaS): Aplicaciones** 

El software como servicio es un modelo de cloud computing que proporciona al cliente una aplicación que se ejecuta en la nube incluyendo toda la infraestructura necesaria y las plataformas subyacentes requeridas. 

08 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



En general, el término como servicio hace referencia a una solución que gestiona otra persona, para que el cliente pueda concentrarse en el núcleo de su negocio. 

Estos servicios no solo están orientado a empresas (SaaS empresarial) sino que cada vez hay más opciones de SaaS para consumidores finales particulares. 

##### **SaaS empresarial** 

##### **SaaS para consumidores** 

- Suites empresariales de correo y ofi• Servicios de correo electrónico mática (Microsoft 365, Google Suite) (Gmail, Outlook) 

- Software empresarial de SAP 

- Solución de SaaS de mensajería de Atos 

- Software de gestión de contenido de WordPress 

- Software de gestión de la relación con el cliente de Salesforce. 

- Servicios de mensajería (Slack, Discord) 

- Servicios de streaming de video (Netflix, Youtube, Twitch) 

- Servicios de almacenamiento de archivos (Drive, Dropbox) 

- Servicios de mapas (GMaps, OpenMaps). 

09 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **Otros X as a Services: Almacenamiento as a Service (ex.BaaS).** 

Además de los anteriormente mencionados existen otra serie de servicios que los múltiples Cloud Service Providers ofertan. 

El almacenamiento en la nube es un método de almacenamiento de datos en el que la información es alojada o guardada en espacios virtuales vía internet (normalmente son ofrecidos como un servicio por parte de proveedores cloud). 

Es decir, hablamos de un almacenamiento online en el que la información - archivos y programas - se encuentran en un espacio físico externo y contratado como un servicio. El cliente de almacenamiento como servicio, cuenta con las mismas tecnologías de discos duros, librerías de cintas, bucket de objetos que en un almacenamiento on premises. Siendo su ubicación un lugar intangible y accesible vía red. 

La capacidad del almacenamiento en la nube varía en función de cada proveedor, de los planes de sus servicios y de las necesidades de cada empresa al contratarlos. Esta capacidad de almacenamiento cloud contratada puede ser ilimitada, y alojada en muchos proveedores. Las tarifas varían también en función de cada proveedor garantizando todos ellos el acceso 24x7 a la información. 

Un caso de uso concreto del almacenamiento como servicio es el realizar copias de seguridad como servicio, o el uso de Backup As A Service (BaaS). Es un enfoque que implica el consumo de servicios de copia de seguridad y recuperación de información a través de la infraestructura de un proveedor cloud. Todo medido mediante el acceso (tanto de lectura como de escritura en línea). 

En lugar de realizar copias de seguridad directamente por el departamento de TI local centralizado – y consumiendo infraestructura propietaria – el servicio de BaaS permite utilizar y conectar diferentes sistemas a una nube privada, pública o híbrida administrada por un proveedor externo. Uno de los principales beneficios de consumir este tipo de servicio es su facilidad de administración (tanto si lo comparamos con la administración en los centros de procesos de datos propios, como la administración a nivel XaaS). 

La utilización del BaaS se suele encontrar cuando una organización ha consumido la totalidad de sus recursos IT derivados este entorno y requiere de una ampliación o actualización costosa de los sistemas para realizar un respaldo puramente local. Esta subcontratación de la copia de seguridad y la recuperación de información desde las instalaciones de un proveedor mantiene también los datos accesibles y/o restaurables desde cualquier ubicación remota en caso de una interrupción o fallo de los entornos productivos de la empresa contratante del servicio. 

10 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

¿Qué se debe considerar al contratar la copia de seguridad como servicio? 

- Deduplicación de la información que se realizará. Tipología del dato. 

- Compartición de archivos. Acceso recurrente /o no a la información. 

- Backups garantizados por parte del proveedor para una protección de datos continua. 

Algunos de los puntos en la planificación previos al uso de este servicio serían: 

- Problemas de cumplimiento que regulan la capacidad de una organización para almacenar datos en la nube. 

- Problemas de seguridad, como cifrado, listas de control de acceso y autenticación basada en roles. 

- Requisitos adicionales de ancho de banda. 

- Precios. Los costes pueden cambiar a medida que aumenta la cantidad de datos, por lo que es posible que los ahorros no estén garantizados. 

Dada la facilidad de gestión de este tipo de servicio y a medida que aumentan los volúmenes de datos a manejar por muchas organizaciones, son muchos los CSPs y MSPs que deciden desplegar en sus instalaciones sistemas de almacenamiento de objetos para mayor compatibilidad con las nuevas aplicaciones (la conexión a este tipo de almacenamiento se puede realizar mediante APIRest). 

### **1.2. Tipos de entornos cloud** 

### **1.2.1 Cloud Público.** 

#### **Propiedad** 

En un entorno cloud público el sistema de hardware no es propiedad del cliente, sino que pertenece a una empresa externa que es también la encargada de gestionarlo. Los recursos hardware y software de la empresa proveedora de cloud se ponen a disposición de múltiples clientes, que pueden compartir o no los recursos virtuales en función del tipo de contratación de cada uno de ellos.  Por lo general estos recursos son compartidos entre varios clientes, los cuales ven un entorno propio virtualizado, permitiéndoles trabajar de forma transparente en la nube pública sin interferir con el resto de los clientes. 

11 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

El usuario final sencillamente establece un acuerdo con el proveedor por el cual utiliza sus recursos pagando solo por lo que usan, bien sea ciclos de CPU, cantidad de almacenamiento o ancho de banda, entre otros. Por lo general la nube pública se articula por medio de acuerdos de suscripción, permitiendo así una gran flexibilidad. 

#### **Localización.** 

En general los proveedores de cloud permiten conocer las regiones del mundo en las que se encuentran los recursos y servicios contratados. El cliente no tiene capacidad de decisión sobre estos lugares, más allá de seleccionar el más adecuado para su caso de uso por motivos legales o de reducción de latencia. Las regiones suelen ser nombradas por partes de continentes, como Europa del Este, o Asia Central. Es por ello por lo que en ocasiones los clientes encuentran limitaciones en cuanto al proveedor cloud disponible para una cierta aplicación por motivos de normativas específicas y en materia de protección de datos. 

#### **Gestión** 

El proveedor siempre gestiona el hardware sobre el que se ejecuta la nube. Es decir, la capa de sistema siempre estará gestionada por el propietario de la infraestructura. En cuanto a la plataforma y las aplicaciones, existen diversos modelos en función de las necesidades del cliente. 

#### **Costes** 

Dado que el proveedor es el propietario de los centros de datos y del equipamiento físico, los clientes de la nube pública no requieren de grandes inversiones iniciales ya que el pago en este tipo de implementación tiende a ser un pago por uso, como ya se ha mencionado. 

Los proveedores de cloud suelen ofrecer distintos precios en función de la intensidad del uso, por lo que, a mayores requerimientos, menor será el precio unitario. Este coste es predecible si se conocen las necesidades de antemano, lo que facilita los aprovisionamientos necesarios por parte del cliente para la contratación de los servicios en nube. 

No obstante, es un requisito indispensable realizar una planificación de costes exhaustiva para poder explotar el ahorro en recursos IT que busca este tipo de cloud.  A partir de un cierto nivel de necesidades puede llegar a resultar más eficiente el uso de cloud privado o híbrido. 

12 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **Escalabilidad** 

La nube pública es el modelo más rápidamente escalable de todos, pudiendo afirmarse que su escalabilidad es prácticamente ilimitada.  Debido a que los recursos son ajenos, para obtener una mayor capacidad sencillamente hay que contratar más servidores, almacenamiento o licencias. De igual manera, al basarse en un modelo de pago por uso, el cliente puede desistir del uso de la cloud sin previo aviso, reduciendo sus costes a cero ante cualquier imprevisto. 

#### **Beneficios para el negocio** 

La nube pública puede llegar a ser sumamente sencilla en función del tipo de despliegue que se desee emplear, pero también puede requerir conocimientos específicos en función del tipo de uso que se vaya a realizar. En sus modalidades de SaaS principalmente, y en ocasiones de PaaS, su configuración, gestión e implementación brillan por su facilidad y rapidez, pudiendo desplegar aplicaciones o servicios en función de días sin necesidad de un conocimiento especializado. 

No obstante, la nube pública también ofrece numerosos servicios y opciones enormemente potentes como son el auto escalado. Esto permite aumentar o disminuir la capacidad disponible en base a reglas para ajustarse a la demanda. Siendo así capaz de asimilar grandes picos de carga; o la reserva de recursos, comprometiéndose a la contratación de estos durante un periodo determinado de tiempo (generalmente 1 o 3 años). Que, si bien resultan necesarias para determinados clientes que desean gestionar la mayor parte del stack de componentes y aumentar al máximo la eficiencia de costes, precisan de personal formado y especializado en infraestructura cloud para así poder obtener todos los beneficios que este tipo de servicios ofrecen. 

Debido a la sencillez de su contratación y facturación, las empresas clientes solo deben provisionar los recursos necesarios en el proveedor. De esta forma y dado que el pago tiende a ser por uso, bien sea temporal o por capacidad, la escalabilidad es inmediata. Si el cliente requiere de más capacidad de cómputo o de almacenamiento, sencillamente deberá incrementar su pedido al proveedor de nube, aumentando así notablemente la rapidez de reacción ante aumentos imprevistos de demanda, pudiendo hacer cambios con un margen de maniobra realmente ajustado. 

Respecto a la continuidad del servicio, la nube pública está sustentada por grandes proveedores que gestionan varios centros de datos dispersos en distintas ubicaciones geográficas en los que la información se guarda de forma redundante. De esta forma si hubiera algún problema con la infraestructura en la que un cliente basa su negocio, toda su información y sus configuraciones seguirían a salvo y estarían listas de nuevo en cuestión de segundos. 

13 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

La nube pública se basa en el empleo de un mismo recurso físico por numerosos clientes. Es por ello por lo que los usuarios de la nube pública pueden llegar a ver su disponibilidad, rendimiento y ancho de banda afectados por el comportamiento de otros clientes que empleen la misma infraestructura. 

Por otro lado, las empresas se benefician de una gestión especializada por parte del proveedor que les permite no necesitar una especialización del personal interno de la empresa para gestionar recursos complejos. 

Además, al no tener la propiedad de los sistemas, se produce un ahorro no solo en inversión inicial y mantenimiento, sino también en costes de espacio, consumos, mantenimiento del espacio físico de los servicios contratados y personal dedicado. 

### **1.2.2 Cloud Privado** 

#### **Propiedad** 

Originalmente un despliegue de nube privado también llamado nube interna o corporativa, era ejecutado en servidores propiedad del cliente, también llamado _on-premises_ . Sin embargo, actualmente se realizan despliegues de nube privada en centros de datos propiedad de un tercero, fuera de las propias instalaciones del cliente, por lo que esta premisa no siempre es cierta en la actualidad. 

Por ello, la definición actual de cloud privado se acepta como un despliegue en nube en el que al menos la infraestructura subyacente de servidores, red y almacenamiento están destinados a un solo cliente con un acceso completamente aislado para este. 

En el caso del software empleado para la gestión de la infraestructura y plataforma de esta nube privada suele ser un software licenciado que se ejecuta sobre la capa de hardware de esta nube. 

En el caso de las aplicaciones sobre la nube privada, los usuarios dentro del cliente acceden a las aplicaciones mediante dos procedimientos. El procedimiento más directo es el acceso a las aplicaciones en nube privada por medio de la intranet de la empresa, mediante un usuario corporativo. De esta manera, se consigue el acceso limitado a los recursos de dicha nube. En caso de no tener acceso directo a la intranet de la empresa, los usuarios pueden emplear una VPN (red privada virtual) tras obtener la autorización para ello. El firewall o cortafuegos se asegura de que solo se produzcan accesos internos legítimos a la cloud privada. 

14 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **Localización** 

En este caso es la empresa contratante la que decide la ubicación exacta de la infraestructura subyacente. A diferencia de la nube pública, el cliente puede decidir si la infraestructura es alojada en sus propias instalaciones en el caso de tenerlas, o bien el centro de datos concreto en el que desea alojarlas. 

#### **Gestión** 

Hay diversas formas de gestionar una cloud privada, entre las que destacan las siguientes cuatro: 

- a. Nube privada interna. La empresa aloja y administra la infraestructura subyacente de la nube privada, manteniendo y gestionando sus componentes, red y almacenamiento 

- b. Nube privada gestionada. En este caso los recursos físicos están alojados en la propia empresa, pero son gestionados por un tercero subcontratado. En este modelo la empresa obtiene los beneficios de personalización y protección de una cloud privada, pero evita la especialización de sus empleados. 

- c. Nube privada alojada. El alojamiento de la infraestructura física que sostiene la nube privada se encuentra en un centro de datos de un proveedor externo en este caso. Tanto la gestión como el soporte y el mantenimiento son proporcionados por el proveedor de servicios propietario del centro de datos. 

- d. Nube comunitaria. En este caso los recursos físicos son compartidos entre un conjunto de empresas. Suelen ser empresas con alguna relación mutua. 

#### **Costes** 

La nube privada varía en su coste en función del tipo de gestión seleccionado, pero generalmente no se ahorran costes debido a la necesidad de mantener los recursos hardware bien con empleados internos o mediante una subcontratación. La inversión inicial es alta, ya que se deben adquirir estos componentes, y los costes de personal, gestión y mantenimiento tienden a ser asimilables a un centro de datos convencional, aunque se cuente con los numerosos beneficios de la nube frente a este modelo. 

El coste de los equipos es amortizable, por lo que puede ser beneficio en función de las necesidades de la empresa, pero los costes fijos asociados se mantendrán a lo largo del tiempo. 

15 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **Escalabilidad** 

Dado que los recursos hardware son propiedad del cliente o, al menos, de uso dedicado, todo aumento de capacidad requerido por el usuario implica la adquisición de nuevos recursos implicando una alta inversión inicial para el despliegue de nuevos recursos, reduciendo no solo la escalabilidad, sino la capacidad de reacción, la disponibilidad y por tanto la flexibilidad. 

#### **Beneficios** 

La nube privada ofrece la gran mayoría de beneficios de la nube pública, aportando el valor añadido del control y personalización de todo el stack de componentes, desde la infraestructura física hasta las aplicaciones que se ejecutan en ella. Sin embargo, dado que este modelo de cloud requiere por definición una inversión en recursos previa a su despliegue, la escalabilidad y flexibilidad ofrecidas por este formato de cloud se ven disminuidas respecto a un modelo público, en el que los recursos están siempre disponibles para ser levantados al instante a petición del cliente. Es por ello por lo que el usuario de una cloud privada deberá realizar mayores esfuerzos en términos de planificación y anticipación para poder responder a posibles aumentos de demanda de forma adecuada, mientras que un usuario de cloud pública tendrá a su disposición los recursos de su proveedor sin necesidad de una provisión por adelantado. 

En muchas ocasiones este modelo de nube es seleccionado por motivos de conformidad con la normativa actual de protección de datos como sucede habitualmente en los sectores de la salud y en las finanzas y sector bancario. 

Este tipo de normativas suelen basarse en aspectos como que el firewall del sistema y el alojamiento físico son dedicados para el cliente, de tal forma que ni las operaciones ni los datos con carácter confidencial son accesibles para un proveedor externo. Sin embargo, esto no quiere decir que un despliegue de cloud privada tenga necesariamente un mejor nivel de seguridad frente a amenazas que un despliegue de cloud público. Los grandes proveedores de cloud público ofrecen numerosas certificaciones de seguridad como son la normativa internacional ISO (9001, 22301, 27001, 27017, 27018), las directrices de la CSA (Cloud Security Alliance) o la publicación de informes de auditoría de SOC (Systems and Organizations Control) así como las diversas normativas y certificaciones locales. Estas certificaciones aseguran a sus clientes los más altos estándares de seguridad y confianza para cualquier aplicación o servicio que se ejecute en su infraestructura. La desventaja de la cloud privada en términos de seguridad es que el cumplimiento de la normativa y estándares de seguridad recaen sobre el cliente. De esta manera, el usuario deberá definir todas las políticas de seguridad que desea aplicar en su stack de componentes, aunque no contará con el soporte de un gran proveedor detrás. 

16 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Dado que el cliente es el responsable de administrar y gestionar su nube privada, tanto en el nivel de sistemas como en la capa de software, aumenta notablemente el coste y la especialización de sus empleados, ya que deberán ser capaces de gestionar todos y cada uno de los componentes del stack. En definitiva, la nube privada supone una inversión prácticamente equiparable a la que se requiere para administrar y mantener un centro de datos tradicional propiedad de la empresa. 

### **1.2.3 Cloud Híbrido** 

Las nubes públicas tradicionalmente se ejecutaban fuera de las instalaciones de cualquier compañía. Con una nube pública, los datos y las aplicaciones de cada empresa o cliente ejecutados en esa nube permanecen ocultos para otros usuarios de esa misma infraestructura en la nube. Son muy amplios los servicios a elegir y utilizar en una nube pública. 

Todos los recursos de computación, almacenamiento y redes basados en hardware son propiedad y están administrados por un proveedor de nube pública externo como Amazon Web Services (AWS), Microsoft Azure o [[02_Metodologias|Google Cloud]] Platform (GCP) 

Para la mayoría de las empresas, encontrar la mejor solución en la nube es una combinación de nube pública y privada. La elección de una nube híbrida significa que su organización combina una o más nubes públicas con una nube privada o con una infraestructura local (estando aisladas entre ellas las nubes públicas). Es una o N relaciones entre infraestructura de nube privada o local y una única nube pública. 

Esto significa que su organización utiliza una combinación de entornos informáticos, de almacenamiento y de servicios (infraestructura local, servicios de nube privada y nube pública). Con la nube híbrida, existe una clara orquestación entre las distintas plataformas. 

El resultado de un entorno híbrido (y que lo diferencia de uno multicloud) viene dado del uso conjunto y combinado de diferentes tipologías de infraestructura. ¿Cuál es la diferencia entre la infraestructura tradicional y la nube privada?, ¿qué hay de la diferencia entre un entorno híbrido y una nube privada? 

Esta descripción hace que los entornos de nube híbrida compartan una serie de características: 

- Una infraestructura de identidad centralizada en múltiples entornos. 

- Una conectividad segura de alta velocidad entre la empresa y el entorno de la nube. 

- Una red integrada que crea una infraestructura de red general segmentada pero única. 

17 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- Un seguimiento y gestión de recursos. 

- Su centro de datos local, los recursos de la nube pública y privada y las cargas de trabajo están vinculados bajo una administración de gobierno. 

En conclusión, aunque la adopción de una solución de nube híbrida y multicloud puede tener puntos comunes, como el uso combinatorio de nubes para crear la estructura ideal de cada empresa, una gran flexibilidad, la adaptación a los requisitos de económicos y de negocio (de gasto _upfront_ y generalmente perpetuo a gasto operativo) y el aumento de la redundancia de la información. 

#### **Beneficios** 

En los actuales entornos cloud, la variedad de diseños a implementar y la definición de los requisitos, se convierten en clave para adaptarse a las necesidades de las organizaciones en cuanto a infraestructura, cargas de trabajo y seguridad. 

El mayor beneficio de este tipo de diseños/implementaciones es que la empresa pueda operar de forma flexible e interoperable y empleando la mejor combinación entre elementos y sistemas TI a su disposición de la forma más efectiva. Y por consecuente menos complejo. Cada una de estas arquitecturas aporta una dificultad y unos beneficios allí donde son desplegadas. A continuación, se detallan los principales beneficios de la adopción de un entorno conjugado de nubes (lo que implica el uso combinado de infraestructuras y servicios). 

1. Seguridad en los sistemas 

La seguridad de la información es un factor crítico de todas las organizaciones que se convierte en una de las mayores prioridades de las organizaciones. El modelo de implementación de una cloud híbrida brinda la posibilidad de una toma de decisiones estratégica, informada, selectiva y precisa sobre la ubicación de la información en cada instante. Esta visión, por ejemplo, asegura que datos o aspectos confidenciales y críticos por su alto valor para la empresa puedan estar sometidos a una configuración dinámica y prioritaria en cuanto a su localización en una infraestructura cloud on premises que a su vez convive con otras cargas de menor criticidad situadas en un cloud privado. 

Esta integración de nubes privadas y públicas es clave en el refuerzo de la seguridad de los sistemas híbridos. 

18 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

2. Escalabilidad del entorno y recursos IT. 

Una estrategia de nube híbrida ayuda a las organizaciones a coordinar cargas de trabajo dispares y administrar flujos de trabajo híbridos. Gracias a la automatización, se beneficia de una disposición eficiente de datos, aplicaciones e infraestructura en diferentes entornos de nube. Dentro de esta automatización, tanto desarrolladores como usuarios de la tecnología/recursos contratados deben tener un control en la planificación del uso del servicio. Cabe destacar en este punto la importancia de la velocidad y de la previsión ligadas a la reducción de costes IT de las empresas. La automatización implica y genera una flexibilidad en el uso y adquisición de servicios. Los entornos de cloud híbrida se caracterizan, en parte, por la posibilidad de hacer una previsión del gasto IT que se consumirá en modo pago por uso en función de los servicios utilizados (que no contratados únicamente). Con esto, el impacto económico de las empresas se reduce a la hora de contar con infraestructura, plataformas e incluso backup como servicios. 

Conocer los actores que intervienen en un entorno híbrido permiten por panto implementar reglas de la automatización IT de la infraestructura; escalar recursos hacia donde lo requiera la organización aprovechando recursos ilimitados en función del uso basado en la demanda. 

3. Control y gestión de riesgos 

A la par de los cambios que sufre la tecnología, así se generan nuevos riesgos para tener en cuenta a la hora de gestionar los entornos IT empresariales. Mediante la implementación de una nube híbrida es factible gestionar los riesgos de una forma eficiente mediante la correcta planificación de recursos, elección de proveedores (y arquitecturas) así como de las políticas de rendimiento y soporte óptimas para cada carga de trabajo integrada en el entorno. 

4. Dinamismo en las cargas de trabajo 

El sistema de nube híbrida aporta valor para todas las empresas que gestionan cargas de trabajo dinámicas (no homogéneas).  Un entorno de nube híbrida ayuda a estar alineado a la operativa óptima en el mercado en el tratamiento de esas cargas, por lo que te ayudará a estar a la par con tus competidores. Esto se traduce, por ejemplo, en que toda aplicación podrá ser ejecutada en una nube privada mientras puede acceder a recursos adicionales desde la nube pública. 

19 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

5. Innovación 

Un diferencial competitivo de las empresas es la innovación, que impacta directamente al negocio. En el contexto IT esto se traduce en mejorar desde el punto de vista de infraestructura los procesos productivos sin incurrir en gastos adicionales, incorporando nuevas plataformas y tecnologías y siempre midiendo el éxito y efectividad de los sistemas propios o contratados (Aquí se incluyen los servicios cloud). 

Para finalizar este punto, es importante destacar que uno de los puntos importantes para beneficiarse de estos beneficios es cómo realizar/planificar la conexión entre entornos de una infraestructura híbrida. Para este propósito existen tres alternativas a estudiar: 

- Vía Internet: resulta la opción más obvia para poder transferir datos y por ende también implica riesgos más evidentes, como la posibilidad de sufrir una velocidad de conexión inestable y menos garantizada. 

- Vía Internet + VPN: esta alternativa que incluye encriptación supone mayor seguridad y resistencia a ciberataques. Pueden existir eso sí, problemas de latencia y velocidad. 

- Vía Conexión directa: esta última alternativa implica una conexión directa con el proveedor cloud para eliminar problemas de latencia, rendimiento y seguridad. Por ejemplo, implementando una extensión de la red de cualquier cliente desde su centro de proceso de datos hasta sus recursos en la cloud pública. 

#### **Diferencias con entornos multicloud** 

La implementación de una estrategia multicloud va un paso más allá a los entornos híbridos. La primera diferencia clave es que una nube híbrida siempre incluye una nube pública en combinación con nubes privadas o/y entornos locales. Este no es el caso de un entorno multicloud, que incluye varias nubes públicas según la necesidad de servicio. En segundo lugar, una infraestructura híbrida supone una conectividad directa entre nube pública y privada. Una relación 1-1. En un entorno multicloud, la integración entre diferentes proveedores de servicios y productos cloud debe sobreentenderse. Por ello, la relación e integración entre nube privada/infraestructura _on premises_ – nube pública 1 - nube pública 2 (por ejemplo) debe fluir en toda dirección. 

20 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



### **1.2.4 Comparativa entre entornos** 

Tras el monográfico de estos tres conceptos, es interesante conocer algunas diferencias entre cloud público, privado e híbrido ya que cobrarán importancia a la hora de cómo implementar un entorno multicloud. Para ello nos apoyaremos en 3 puntos a alto nivel. 

||**Propiedad**|**Localización**|**Gestión**|
|---|---|---|---|
|**Cloud**<br>**Público**|Proveedor externo<br>propietario del HW<br>compartido y del SW<br>para gestionar el<br>entorno.|Instalaciones<br>del proveedor<br>externo. Ubicuidad<br>de los recursos<br>predefinida.|Propia o del<br>proveedor|
|**Cloud**<br>**Privado**|Proveedor externo<br>del propietario de<br>HW exclusivo /<br>empresa propietaria.<br>SW de gestión<br>licenciado /<br>propietario.|Instalaciones del<br>proveedor externo.<br>Ubicuidad de los<br>recursos predefinida<br>/ Centro de Procesos<br>de Datos propio.|Propia o del<br>proveedor.<br>Común gestión<br>subcontratada.|
|**Cloud**<br>**Híbrido**|Combinación de uso de l<br>co). Y posibilidad de incl|os anteriores (un único prove<br>uir un entorno on premises.|edor de cloud públi-|



21 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **1.2.5. Casos de uso por entorno** 

No sólo la arquitectura sobre la que se va a orquestar una estrategia de cloud híbrida es importante para la ejecución y adopción óptima de este tipo de infraestructuras. Existen tres capas por encima que se han de tener en cuenta en esta decisión de diseño según los requerimientos de las aplicaciones a desarrollar por la empresa, las plataformas en uso e incluso la tipología de _software middleware_ con el que cuenta la empresa. O al que recurrirá también como servicio. 



La definición e implementación del entorno implica el conocimiento de las organizaciones sobre el punto de digitalización en el que se encuentran, y sobre los requisitos en relación con la criticidad de las aplicaciones gestionadas. La combinación de estos dos factores junto a las aplicaciones y plataformas usadas por cualquier compañía generan el siguiente _stack_ de elementos. 

Independientemente de la implementación elegida en el desarrollo de una estrategia híbrida, toda infraestructura local, de cloud pública y de cloud privada que intervienen requieren de recursos físicos para su funcionamiento (y capacidad de servicio). En este punto de infraestructura existen componentes de software como sistemas de gestión de contenido (CMS), sistemas de software de planificación de recursos empresariales (ERP), sistemas operativos y servidores web que se contemplan para una correcta gestión de estos recursos físicos. 

22 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

En cuanto a los principales componentes físicos de todo centro de proceso de datos, es imprescindible: 

- Recursos de computación: hace referencia a la memoria y la potencia de proceso necesarios para ejecutar las aplicaciones que proporcionan los servidores, generalmente de propósito empresarial (Intel , HPE, Dell, IBM, SuperMicro , Lenovo). 

- Recursos de almacenamiento: los centros de datos incluyen dispositivos de almacenamiento primario y de copia de seguridad. Granjas de dispositivos _all-flash_ , cintas, despliegue de servidores con disco interno y múltiples tecnologías pueden ser utilizados. (PureStorage, NetApp, DEL EMC, IBM, Huawei, HDS) 

- Redes y comunicación: conmutadores, cortafuegos, controladores, etc. 

Es decir, junto al software de gestión, cualquier centro de proceso de datos se compone de hardware, redes, instalaciones y herramientas necesarias para monitorizar y gestionar toda esa infraestructura. 

A continuación, se detallan casos de uso en los que las empresas se benefician de los recursos físicos a su disposición en el mercado. 

#### **Caso de uso cloud público.** 

La nube pública es el gran aliado, entre muchas otras, para empresas con foco en la inversión en innovación de productos, aplicaciones y procesos. Para este tipo de compañías el cloud público es un gran aliado por el gran número de servicios que ofrecen. Es en gran medida un trampolín para por, llevar a cabo iniciativas de análisis de datos. El tratamiento de la información comercial se convierte en crucial para ayudar a personalizar los precios de clientes franquiciados, etc. Los datos son un activo muy diferenciador para muchos negocios. Pongamos como caso de uso una empresa emergente que desea comenzar su actividad de cursos de formación online explotando los servicios de Google Cloud. Decide beneficiarse de: 

- Herramientas de análisis y colaboración para la cadena de valor del comercio 

- Herramientas de computación, gestión de datos y analíticas para servicios financieros. 

- Soluciones para operaciones de producción y distribución de contenido. 

- Soluciones basadas en inteligencia artificial para crear y escalar juegos más rápidamente. 

- Herramientas de migración e inteligencia artificial para optimizar la cadena de valor de búsqueda de empresas registradas en Facebook a las que ofrecer sus cursos. 

23 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- Soluciones de almacenamiento de datos tipo archivo digitar (contratan un bucket inicial de 20TB). 

- Herramientas de enseñanza para fomentar el interés durante el aprendizaje. 

- La solución de alojamiento web y desarrollo de aplicaciones complementarias a la formación online. 

Otro buen ejemplo para el uso de cloud pública, puede ser un periódico digital con cobertura internacional. La cloud pública le permite aprovechar las distintas Availability Zones de las que disponga la cloud para dar a sus clientes contenido en múltiples idiomas. En función del país desde el cual se haga la petición a la web, se puede dirigir el tráfico a una Availability Zone u otra, proporcionando así un servicio más rápido, y en el idioma del país desde el cual se accedió. El uso de cloud pública también le permite escalar en almacenamiento y servidores web si lo requiriese, programando la reserva de instancias basado en análisis de accesos a la web por temporada y Availability Zone para una mayor eficiencia en el uso de los recursos contratados. 

Para esta casuística de consumo de cloud y de migración de servicios online a la cloud pública de AWS, estudiaremos el caso de BBC Online. El periódico digital de British Broadcasting Corporation ligado a una serie de buenas prácticas genéricas a la hora de adoptar una estrategia IT ligada al consumo de servicios en cloud. Como muchas otras entidades del sector, y de otros, el equipo de diseño e ingeniería de la BBC se aventuró a comenzar un proceso completo de reestructuración de su cara visible, su website. El principal movimiento 



a alto nivel se basó en el movimiento del hosting de la plataforma, de unas instalaciones físicas/su propio centro de proceso de datos a la nube. Así como se planteó la migración de la página web, también se hizo con la mayoría de las herramientas y sistemas que nutrían de recursos a su web corporativa. Se planteó un enforque de uso de tecnologías serverless orientadas a que tanto el diseño, el enfoque y el flujo de trabajo editorial de la BBC se modernizaran con el fin de poder ejecutar cambios tecnológicos de calidad de una forma efectiva y rápida. 

Previamente a esta decisión de modernización IT, la web de la BBC estaba escrita en PHP y alojado en dos centros de procesos de datos cerca de la capital británica. Esto, llegó a ser limitante a la hora de alojar servicios (como iPlayer, Sounds, News y Sport) que cada vez eran demandantes de recursos IT escalables y rápidamente accesibles. La implementación de técnicas y herramientas modernas, como el frame React y el uso de Devops se convirtieron en los perfectos aliados para abordar esta transformación. 

24 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Los principales puntos para tener en cuenta en este proyecto de la BBC en cuanto al consumo de cloud pública, se convierten, por tanto, en un claro ejemplo de buenas prácticas para la adopción cloud: 

#### **1. Correcta selección de los servicios a implementar en cloud.** 

Considerar construir desde cero todos los servicios que la BBC Online gestionada y alojaba desde sus instalaciones físicas podría dotar de mayor control de la plataforma, sin embargo, el coste de ejecución incrementaba considerablemente. De forma genérica migrar servicios a cloud / consumirlos, debe solucionar la casuística de negocio a la que una empresa se enfrenta, pero es preferible no realizar un movimiento a cloud completo si esto implica incurrir en gastos adicionales de proyecto, al modernizar cargas que de forma tradicional cubren una necesidad completa de negocio. 

Un gran ejemplo tecnológico de esto es el uso de serverless. Cerca de la mitad de la web de la BBC se procesa hoy sin servidores en propiedad con AWS Lambda. Esto es causado por el alto coste de administración de máquinas virtuales (o contenedores) y la necesidad de mantener este tipo de seguros y escalarlos, supone un alto consumo en tiempo. Serverless en su mayoría resuelve ese problema, pero sin embargo la BBC optó por mantener en sus centros de procesos de datos otras cargas que, ya sea por automatización en la gestión, o por su inmutabilidad no requieren de unos servicios externalizados y no implican un limitante IT al negocio. 

#### **2. Eliminar duplicados sin una simplificación excesiva.** 

Al coexistir equipos en la gestión de plataformas IT, la duplicación es inevitable. Dos equipos pueden coincidir con un mismo problema y crear soluciones diferentes. 

A medida que se fue reconstruyendo la BBC Online se fueron eliminando muchas duplicaciones y diferencias que se habían creado con el tiempo. Por ejemplo, sistemas y servicios que se habían personalizado por país fueron reemplazados por un sistema genérico alojado en cloud y gestionado de forma uniforme para los consumidores de la BBC Online. Además de ser más eficientes y económicos esto ha implicado que la web de la BBC ahora tiene un mejor rendimiento y accesibilidad. 

Sin embargo, de forma genérica en la adopción de una estrategia cloud se debe tener cuidado con la simplificación excesiva. Reemplazar múltiples sistemas con uno externo, puede aumentar la complejidad del software intermedio para la armonización de plataformas que crece exponencialmente. Llega un punto en el que dos sistemas simples, se alojen donde se alojen, son mejores que un sistema demasiado sofisticado. 

25 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



En este caso en concreto, se decidió mantener la web del Servicio Mundial de la BBC separada de la web principal de la BBC en inglés. Las necesidades del Servicio Mundial, como por ejemplo trabajar con un mal ancho de banda, era lo suficientemente justificable como para tener una solución separada. 

#### **3. Consolidar silos tecnológicos a través de la comunicación y la cultura.** 

La creación de un nuevo sitio web de la BBC implicó involucrar a muchos equipos. Para tener éxito en este proyecto (al igual que en otros de rediseño IT), fue necesario que estos equipos se alinearan y colaboraran. La comunicación trae comprensión, y eso permite que la cultura cambie empresarial e IT cambie. En organismos multi país como es la BBC, es además importante contar con el factor cultural para la gestión exitosa de la toma de decisiones. 

#### **4. Organizarse en torno a los problemas para una correcta toma de decisiones.** 

En numerosos proyectos como pudo ser este, el “diagrama de cebolla” ayuda a explicar cómo las preocupaciones y capacidades comunes (en el centro del círculo) pueden ser abordadas. Esto libera a los equipos para que trabajen en las capacidades más especializadas de los anillos exteriores. 



26 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Históricamente, la BBC ha tenido sitios web separados: para noticias, para deportes, etc. Cada uno tenía un equipo separado. Para cambiar eso y construir un sitio web se necesitó una reorganización. Se crearon equipos para cada ‘tipo’ de página: una página de inicio, una página de artículo, una página de video, etc. También se crearon equipos para manejar inquietudes comunes, como la forma en que se desarrolla y aloja el sitio. En conjunto esta pauta de actuación minimizó la superposición y la duplicación, y a su vez permitió que cada equipo se apropiara y se volviera experto en su área. 

#### **5. Planificación para el futuro.** 

Al diseñar grandes sistemas basados en software, incluso basándonos en soluciones alojadas en cloud públicas, existe un equilibrio difícil de encontrar; Debemos planificar para el futuro, de modo que satisfagamos las necesidades de mañana, así como las de hoy. Pero sin llegar a sobre diseñar. Los requisitos de las plataformas y servicios pueden cambiar, los proveedores de la nube ofrecerán nuevas tecnologías, incluso la tasa de cambio y rotación en el mundo de la tecnología es más alta que nunca. 

Es importante tener en cuenta que no hay sustituto para un buen análisis, planificación y diseño de software. Investigar las oportunidades y opciones disponibles es clave para garantizar que un proyecto se ponga en marcha en la dirección correcta. 

Lo que brinda el desarrollo Agile de software y su aplicación a la hora de abordar este tipo de proyectos es la adaptación. Adaptación continua a los desafíos que a medida que avanzamos en la implantación y adopción de recursos como puede ser el cloud público se encuentran desde el área IT de las empresas. 

#### **6. Cree primero, optimizar después.** 

Ampliando lo anterior, debemos tener cuidado de no optimizar demasiado pronto. Los grandes proyectos de software inevitablemente tendrán problemas de rendimiento en algún momento. Es muy difícil predecir cuándo y cómo aparecerán estos problemas. Otros de los beneficios actuales que el cloud brinda con herramientas de gestión de proyectos mediante metodologías Agile es, el desarrollo ágil para responder a los problemas de rendimiento solo cuando se vuelvan reales. 

Como se mencionó anteriormente, gran parte del sitio web de la BBC ahora se procesa sin servidor utilizando AWS Lambda. Al comienzo del proyecto se pudo intuir mediante pruebas de concepto de la rapidez con la que Lambda podía llegar a presentar páginas web. Sin embargo, desde los equipos organizados del área IT existía un enfoque alternativo (que no se llegó a ejecutar) en caso de que el rendimiento con serverless no hubiera sido óptimo. Al no optimizar demasiado pronto, la BBC evitó una gran cantidad de esfuerzo de personal y de consumo de recursos. 

27 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **7. Si el problema es complejo, vuelve a empezar** 

Se acuña en el mundo de la transformación digital en torno al uso de cloud este principio, la Ley de Gall. Eliminar la complejidad de un sistema existente y en producción es difícil, y en el caso de la BBC en concreto, ya que disponían de varios sitios web complejos que se deseaban combinar. Los requisitos colectivos de estos sitios potencialmente podrían suponer una sobrecarga para cualquier sistema que los alojara. Entonces, tuvieron que comenzar de nuevo, volviendo a los conceptos básicos de las habilidades comunes que se necesitaban. 

#### **8. Ejecución rápida y segura.** 

Finalmente, un principio muy práctico en la adopción de cloud es poder mover rápidamente las aplicaciones cuando parte del servicio/plataforma está preparada para ser ejecutada. Como se comentó anteriormente, predecir el futuro es notoriamente difícil. 

El contraargumento a esto es que el cambio trae riesgo. Y con un servicio popular como BBC Online, la seguridad y la confiabilidad de un sitio web es crítica. La BBC siempre ha tenido un sólido proceso operativo que incluye servicios de administración de equipos las 24 horas del día, los 7 días de la semana, y un enfoque DevOps para garantizar que quienes desarrollan los sistemas también sean responsables de mantenerlos. Es por ello por lo que se sigue invirtiendo en esta área, con nuevos equipos que se enfocan en la infraestructura y en la experiencia del desarrollador (DevX). 

Poniendo en práctica los principios anteriores, aquí hay una descripción general de cómo funciona el sitio web de la BBC: 

28 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



<u>Capa de gestión de tráfico:</u> 

Todo el tráfico de la BBC Online el tráfico llega al Global Traffic Manager (GTM). Esta es una solución de gestión de tráfico interna y propia de la compañía basada en Nginx. Maneja miles de solicitudes por segundo. Debido a su escala y a la necesidad de ofrecer una latencia extremadamente baja, reside en parte en sus propios centros de datos y en parte en AWS. Es decir contamos con una solución híbrida que implica una solución on site y una solución de cloud pública. Para parte de este tráfico se utiliza una segunda capa de gestión de tráfico. Estos servicios, alojados en AWS EC2, manejan alrededor más de diez mil solicitudes por segundo. Los servicios de AWS proporcionan almacenamiento en caché, enrutamiento y balanceo de carga. También juegan un papel clave en mantener la web con una resiliencia óptima, al detectar errores y permitir que los sistemas subyacentes se recuperen de caso de fallo. 

29 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### <u>Capa de representación del sitio web</u> 

La gran mayoría de las páginas web de la BBC se procesan en AWS, utilizando React. La naturaleza de React permite mejorar el rendimiento desde el punto de vista del servidor que aloja la página/parte de los servicios de la página web rendimiento. 

La representación se realiza en AWS Lambda. Alrededor de 2000 llamadas se ejecutan cada segundo para crear el sitio web de la BBC. Como se comentó anteriormente, el uso de servicios serverless para el cliente elimina el coste de operación y mantenimiento. Y es mucho más rápido a la hora de escalar. Cuando hay un evento de última hora, los niveles de tráfico de la BBC pueden dispararse en un instante; Lambda puede manejar esto de una manera que el escalado automático de EC2 no puede. 

Como se mencionó anteriormente, la web del Servicio Mundial de la BBC se mantuvo alojada en los centros de procesos de datos de la BBC como una implementación separada, para que, por ejemplo, poder focalizar en el desafío conocer a una audiencia mundial diversa. (Este proyecto, llamado Simorgh, es de código abierto y está disponible en GitHub). Páginas de la BBC como iPlayer y Sounds también se mantienen separados, aunque todavía hay una cantidad considerable de uso compartido. 

#### <u>Capa empresarial</u> 

Esta capa se enfoca solo en la presentación. La lógica para obtener y comprender el contenido está mejor ubicada en una capa comercial/externalizada. Esta capa proporciona una API (RESTful) a la capa de representación de la web, precisamente con el contenido correcto necesario para crear la página. Las aplicaciones de la BBC usan esta API para obtener los mismos beneficios. 

La BBC tiene una amplia variedad de tipos de contenido, desde programas, guías de revisión de Bitesize, a pronósticos del tiempo. Cada uno tiene datos diferentes y requiere su propia lógica de negocio por lo que crear docenas de sistemas separados para cada tipo de contenido, es costoso. No solo necesitan la lógica correcta, sino que también deben ejecutarse de manera confiable, a escalable y segura. 

Por eso, una parte clave de la estrategia tanto en la BBC como en proyectos similares es simplificar el proceso de creación de capas comerciales. Los problemas como el control de acceso, la supervisión, el escalado y el almacenamiento en caché, se manejan de una manera única y estándar. 

30 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### <u>Capas de plataforma y fujo de trabajol</u> 

Las dos capas finales proporcionan una amplia gama de servicios y herramientas que permiten crear, controlar, almacenar y procesar contenido. Está más allá del alcance de esta publicación hablar sobre esta área. Pero los principios son los mismos: estos servicios se han trasladado de los centros de datos a la nube, abordando las diferencias y duplicaciones mientras lo hacen, y asegurándose de que estén en la mejor posición para evolucionar a medida que crece BBC Online. 

Como conclusión, la BBC Online opera prácticamente en la nube. Y, como resultado, es más rápida, más moderna y confiable. Las claves de la adopción de AWS en este caso de uso real son: 

- Los servicios digitales de la BBC se ejecutaban en una pila LAMP (Linux, Apache, MySQL, PHP/Perl/Python) de forma convencional en un par de centros de proceso de datos en Londres, ambos funcionando como entornos productivos sincronizados para garantizar la resiliencia de la plataforma web. 

- La BBC comenzó su migración a la nube pública manteniendo algunos recursos como la transcodificación de video. La migración no supuso solo un cambio tecnológico, sino que también cambió las prácticas de trabajo para adoptar más DevOps y CI/CD. 

- La compañía creó su propia plataforma similar a Cloud Function, a la que se refirieron como nano servicios, sobre AWS, antes de cambiar a AWS Lambda. 

- El rendimiento es muy importante para la BBC y empresas que gestionan alto contenido multimedia como esta. Si una página se ralentiza un par de segundos esto impacta en la audiencia. Es por ello por lo que contar con una capa de administración de tráfico basada en NGINX que se ejecuta en máquinas virtuales en lugar de Lambda, fue clave para la BBC. 

#### **Caso de uso privado.** 

Un ejemplo de un caso de uso de Cloud Privada se puede ver en empresas del sector de las Telecomunicaciones. Con el rápido crecimiento de las tecnologías de comunicaciones, las empresas del sector Telco están apostando fuertemente por la virtualización de funciones de red (NFV – Network Function Virtualization) sobre infraestructuras cloud. 

31 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Las cloud se pueden desplegar en múltiples localizaciones en función del servicio que ofrecen. Se pueden desplegar clouds en el límite de la red (EdgeCloud) para virtualizar servicios de acceso a la red (un ejemplo puede ser el proyecto openRAN - https://www.o- <u>ran.org), o virtualización de sus centros de datos para otros servicios como puede ser una</u> CDN (Content Distributed Network). Por lo general se desaconseja alojar este tipo de servicios en clouds publicas ya que los requerimientos de este tipo de servicios (latencias, acceso radio, etc.) son más difícilmente alcanzables en este tipo de infraestructura (y más accesibles desplegando un cloud privado con infraestructura dedicada). 



El uso de clouds privada les permite escalar horizontalmente los servicios en función de la demanda, y también les permite un rápido despliegue y corto Time-to-market de nuevos servicios o cambios de tecnología. Otra gran ventaja es el uso de estrategias de despliegue evitando perdidas de servicio, crítico para las empresas de este sector. 

#### **Caso de uso híbrido.** 

Encontramos una empresa en cuyas oficinas/Data Centers se dispone de infraestructura especifica que les permita dar un servicio, y que se apoyen en la cloud pública para poder ofrecer otra serie de servicios adicionales. Por ejemplo, una empresa cuyo negocio gire en torno a los videojuegos online. En este caso, podrían desplegar una cloud pública onpremises para la virtualización de servicios de múltiples videojuegos, que les permita escalar en función de la demanda de cada juego para un mejor uso de su infraestructura. Sobre la cloud pública, pueden hacer uso de servicios Web y bases de datos para publicar noticias sobre actualizaciones y parches, foros para la interacción entre usuarios, servicios de gestión de suscripciones, etc. 

32 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Otro ejemplo de empresa que usa el modelo de cloud hibrida es Netflix. El motor de recomendaciones, gestión de usuarios, como se organiza el catálogo, y otros muchos servicios funcionan sobre AWS. Este uso de cloud pública le permite soportar picos de demanda sin afectar al servicio. Sin embargo, para el servicio de Streaming, Netflix opera su propia CDN, para poder esta lo más cerca posible del usuario, y esta no se aloja sobre cloud pública. 

### **1.3. Concepto de entorno MultiCloud** 

### **1.3.1. ¿Qué es un entorno multicloud?** 

#### **Breve introducción de la evolución IT. Estado del arte** 

El origen del concepto Multicloud implica tener conciencia de una breve historia del cloud computing. En los años 50, el gran tamaño de la infraestructura propietaria de muchas empresas impedía el objetivo de tener disponible la información desde varios puntos de acceso. Fue entonces el momento de la aparición de la computación compartida, pensando en ofrecer como servicio/vender, el uso de espacios de memoria, el espacio de los recursos y los propios servidores y sistemas de almacenamiento. Transcurrieron unas décadas hasta que este concepto cobra importancia con la aparición de Internet. Los años 90 se caracterizan por la aparición de los primeros centros de datos centralizados que daban los servicios anteriormente mencionados, entre otros. El Cloud Computing había llegado para quedarse. Es en los 2000 cuando nacen conceptos como la virtualización. Desde 2010 aparece un modelo que permite gestionar la infraestructura como un servicio de forma remota e incluso desde 2014 aproximadamente, encontramos plataformas como servicio. ¿Qué lleva al desarrollo de infraestructuras multicloud? Principalmente el extendido acceso a este modelo de externalización de cualquier servicio ligado a las tendencias tecnológicas actuales a continuación detalladas. 

Las tendencias tecnológicas continúan evolucionando y cada día van apareciendo nuevos conceptos que conocer. Hoy en día caso no se puede tener una discusión respecto a Cloud Computing sin llegar al concepto de “Contenedores” (Containers). Organizaciones de diferentes industrias y todos los segmentos de negocio hoy quieren entender qué son los contenedores, qué signifivan para las aplicaciones en la nube y cómo pueden beneficiarse de su uso. 

Antes de ahondar en el concepto de contenedores, volvamos unos años atrás para recordar el nacimiento de la virtualización. A medida que le hardware se hacía más poderoso y físicamente inabarcable, nos encontrábamos con que el software no ocupaba todas las capacidades de la máquina física donde se ejecutaba (en muchos casos ni siquiera una fracción de estos recursos). Dado lo anterior se crearon recursos “virtuales” para simular el hardware base sobre el cual se ejecuta el software, permitiendo que múltiples aplicaciones puedan ser ejecutadas al mismo tiempo, cada una usando una fracción de los recursos del hardware físico disponible. A esta “simulación” que permite compartir recursos la denominamos comúnmente virtualización. 

33 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

El concepto general de virtualización es el de habilitar un sistema operativo que tenga la ilusión de poseer recursos dedicados para operar. Entendiendo lo anterior podemos ahora definir los Contenedores como otra alternativa de virtualización. 

En términos generales los contenedores crean la percepción de un ambiente aislado exclusivo para la aplicación, mientras que en la virtualización “tradicional” de máquinas virtuales, la aplicación se ejecuta en un sistema operativo virtualizado donde convive con otros aplicativos. 

La tecnología de contenedores ayuda a obtener mayor flexibilidad y portabilidad de las aplicaciones y hacen que estas se puedan ejecutar en instalaciones físicas, una nube pública, o en una nube privada. 

Este nivel de paquetización conseguido en una aplicación permite que esta pueda ser trasladada de un ambiente a otro con mínimo o nulo impacto. Permitiendo así que, en escenarios de alta carga, el sistema pueda escalar clonando nuevas instancias de la aplicación muy rápido. 



34 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Evolución: 



Si pensamos en los entornos IT tradicionales, en los cuales la infraestructuras cloud no era una opción, encontrar escenarios _full on premises_ era muy común. Producción - Réplica y Backup suponían una inversión en infraestructura física recurrente. 

Esta visión eminentemente _legacy_ desde hace años deriva en la convivencia con una estrategia cluod por parte de muchas compañías. Desde una infraestructura cloud, que libera recursos físicos propietarios, estando estos alojados por lo general en una localización externa y ajena a las compañías. Este primer salto en la adopción de una estrategia cloud supone 5 aspectos generalizados: 

- Los usuarios de diferentes proveedores cloud utilizan mayoritariamente un único proveedor Cloud para adquirir servicios de IaaS, SaaS o PaaS. 

- Integración de aplicaciones y reducción de costes son la clave para la toma de decisión de esta estrategia. 

- Por lo general no se dispone de herramientas de control y gestión para distribuir cargas de trabajo. 

- La tendencia a la búsqueda de flexibilidad (soluciones no _vendor lockin_ ) y continua mejora de los servicios de IT que deriven en avances para la producción de los negocios. 

- Reconocimiento de la incapacidad de explotar el valor del gran volumen de datos generados y gestionados. 

35 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

La combinación de ambas opciones supone la instauración de entornos híbridos como receta de despliegue para muchas empresas. 

Volviendo a la mencionada flexibilidad y portabilidad de las aplicaciones al ser desplegadas en contenedores, estos entornos híbridos, en ocasiones no son considerados como la forma óptima de utilizar este nuevo tipo de plataformas. 

A lo largo de los siguientes puntos conoceremos el siguiente paso de los requisitos y características de un entorno multicloud que supone el salto adelante de la hibridación para cubrir las necesidades tecnológicas y alojar plataformas como Openshift, Jelastic, A2Holding e incluso Google Cloud Run. Entre otras. 

#### **Definición de Entorno Multicloud** 

Antes de entrar a hablar en profundidad del concepto Multicloud, es interesante recopilar algunas diferencias entre cloud público, privado e híbrido del apartado anterior (1.2.4) ya que cobrarán importancia a la hora de cómo implementar un entorno multicloud. Para ello nos apoyaremos en 3 puntos a alto nivel, e incorporaremos una cuarta línea de la arquitectura a comentar. 

||**Propiedad**||**Localización**|**Gestión**|
|---|---|---|---|---|
|**Cloud**<br>**Público**|Proveedor externo<br>propietario del HW<br>compartido y del SW<br>para gestionar el<br>entorno.||Instalaciones<br>del proveedor<br>externo. Ubicuidad<br>de los recursos<br>predefinida.|Propia o del<br>proveedor|
|**Cloud**<br>**Privado**|Proveedor externo<br>del propietario de<br>HW exclusivo /<br>empresa propietaria.<br>SW de gestión<br>licenciado /<br>propietario.||Instalaciones del<br>proveedor externo.<br>Ubicuidad de los<br>recursos predefinida<br>/ Centro de Procesos<br>de Datos propio.|Propia o del<br>proveedor.<br>Común gestión<br>subcontratada.|
|**Cloud**<br>**Híbrido**|Combinación de uso de<br>co). Y posibilidad de inc|los<br>luir|anteriores (un único prove<br>un entorno on premises.|edor de cloud públi-|
|**Multi-**<br>**cloud**|Combinación de uso de<br>co). Y posibilidad de inc|los<br>luir|anteriores (más de un pro<br>un entorno on premises.|veedor de cloud públi-|



36 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

El modelo Multicloud se refiere a la implementación que aprovecha múltiples tipos de servicios ya se desplieguen en una nube pública, privada o en una infraestructura _on premises_ tradicional. Llevándolo a un ejemplo práctico, una empresa puede usar una nube pública como repositorio _data lake_ , y utilizar una nube privada para hacer explotación de esos datos no estructurados o tipo fichero para realizar su computación empleando sobre ellos IA. En este punto, y se verá en puntos posteriores, algunos proveedores son mejores para determinadas tareas que otros, por lo que la definición del uso de cada tipo de entorno es crucial para el éxito en el despliegue de este tipo de infraestructura. La búsqueda del máximo beneficio de cada uno de los servicios, de los diferentes proveedores es el punto clave a definir. Las implementaciones multicloud suelen ser parte de una estrategia para evitar bloqueos de proveedores, ya que este riesgo aumenta cuando se tiene un único proveedor de servicios en la nube. Además, este tipo de entornos buscan flexibilizar el despliegue de aplicaciones y el movimiento de la información de forma automática. Por ello, y como se ha mencionado en el Módulo I, son entornos óptimos para el despliegue de cualquier plataforma de contenedores. 

Algunas ya han sido mencionadas, pero las principales características de un entorno multicloud pueden agruparse en tres categorías principales: 

1. Flexible. 

   - a. Portabilidad de datos entre nubes públicas y privadas. 

   - b. Nubes seguras y compatibles. 

   - c. Casos de uso de alto ROI. 

2. Moderno. 

   - a. Impulsado por el nivel de servicio (SLAs). 

   - b. Definido por software y optimizado. 

   - c. Copia de seguridad y replicación modernas. 

3. Ágil. 

   - a. Automatización de las API. 

   - b. Capacidad de DevOps nativa. 

   - c. Autoservicio/autogestión. 

37 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



#### **Diferenciación con otras infraestructuras.** 

Las nubes públicas tradicionalmente se ejecutaban fuera de las instalaciones de cualquier compañía. Con una nube pública, los datos y las aplicaciones de cada empresa o cliente ejecutados en esa nube permanecen ocultos para otros usuarios de esa misma infraestructura en la nube. Son muy amplios los servicios a elegir y utilizar en una nube pública. 

Todos los recursos de computación, almacenamiento y redes basados en hardware son propiedad y están administrados por un proveedor de nube pública externo como Amazon Web Services (AWS), Microsoft Azure o Google Cloud Platform (GCP). 

Para la mayoría de las empresas, encontrar la mejor solución en la nube es una combinación de nube pública y privada. La elección de una nube híbrida significa que su organización combina una o más nubes públicas con una nube privada o con una infraestructura local (estando aisladas entre ellas las nubes públicas). Es una o N, relaciones entre infraestructura de nube privada o local y una única nube pública. 

Esto significa que su organización utiliza una combinación de entornos informáticos, de almacenamiento y de servicios (infraestructura local, servicios de nube privada y nube pública). Con la nube híbrida, existe una clara orquestación entre las distintas plataformas. 

38 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

El resultado de un entorno híbrido (y que lo diferencia de uno multicloud) viene dado del uso conjunto y combinado de diferentes tipologías de infraestructura. ¿Cuál es la diferencia entre la infraestructura tradicional y la nube privada?, ¿qué hay de la diferencia entre un entorno híbrido y una nube privada? 

La infraestructura tradicional es un sistema dedicado y personalizado, ideal para organizaciones que necesitan ejecutar muchos tipos diferentes de aplicaciones. Las empresas con esta infraestructura deben comprar hardware adicional y actualizaciones para ampliar su almacenamiento de datos y sus servicios para admitir a más usuarios. 

Esta descripción hace que los entornos de nube híbrida compartan una serie de características: 

- Una infraestructura de identidad centralizada en múltiples entornos. 

- Una conectividad segura de alta velocidad entre la empresa y el entorno de la nube. 

- Una red integrada que crea una infraestructura de red general segmentada pero única. 

- Un seguimiento y gestión de recursos 

- Su centro de datos local, los recursos de la nube pública y privada y las cargas de trabajo están vinculados bajo una administración de gobierno. 

En conclusión, aunque la adopción de una solución de nube híbrida y multicloud puede tener puntos comunes, como el uso combinatorio de nubes para crear la estructura ideal de cada empresa, una gran flexibilidad, la adaptación a los requisitos económicos y de negocio (de gasto _upfront_ y generalmente perpetuo a gasto operativo) y el aumento de la redundancia de la información. La implementación de una estrategia multicloud va un paso más allá. La primera diferencia clave es que una nube híbrida siempre incluye nubes públicas y privadas. Este no es el caso de un entorno multicloud, que incluye varias nubes públicas según la necesidad de servicio. En segundo lugar, una infraestructura híbrida supone una conectividad directa entre nube pública y privada. Una relación 1-1. En un entorno multicloud, la integración entre diferentes proveedores de servicios y productos cloud debe sobreentenderse. Por ello, la relación e integración entre nube privada/ infraestructura _on premises_ – nube pública 1 - nube pública 2 (por ejemplo) debe fluir en toda dirección. 

39 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



#### **Objetivos y beneficios de un entorno multicloud.** 

En los actuales ecosistemas cloud, la variedad de diseños y la definición de los requisitos, se convierte en clave para adaptarse a las necesidades de las organizaciones en cuanto a infraestructura, cargas de trabajo y seguridad. Cada una de estas arquitecturas aporta una dificultad y unos beneficios allí donde son desplegadas. A lo largo del siguiente apartado se abordará la temática de los beneficios de la adopción de una estrategia multicloud, claves para la toma de un proceso de hibridación u otro. 

### **1.3.2. ¿Por qué adoptar una estrategia multicloud?** 

Desde el punto de vista tecnológico, algunos de los beneficios específicos de los entornos multicloud se pueden reducir en cuatro categorías. 

#### **1. Reducción de riesgos:** 

Si uno de sus proveedores de nube tiene un problema o fallo temporal, su rendimiento total disminuirá en ese momento específico. Pero con una estrategia de múltiples nubes, puede cambiar a otro proveedor. 

#### **2. Capacidad para encontrar mejores proveedores de múltiples nubes de su clase a precios competitivos:** 

El número de proveedores de servicios en la nube ha aumentado significativamente en los últimos años. Cuando algunas de las políticas de un solo proveedor no coinciden con su organización, simplemente pueden comparar diferentes proveedores y seleccionar la mejor oferta que se adapte a sus necesidades. De esta forma se logra un alto nivel de agilidad. 

40 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

En este punto cabe destacar el concepto mencionado de _vendor lockin_ de una manera más extensa. La potestad de poder desligarte de recursos – ya sean a nivel físico o de servicios - sin impacto tecnológico (ni económico) en el negocio es una máxima en la implementación de este tipo de arquitecturas. Este término otorga una flexibilizad adicional a este tipo de entornos que implica contar con tecnologías de diferentes proveedores bajo demanda de las necesidades de negocio sin tener penalización alguna a la hora de dejar de usar ninguna de ellas. Pongamos un ejemplo de este concepto ( _vendor lockin_ ) ligado a la capacidad que el almacenamiento definido por software (SDS) en un entorno de BBDD Oracle desplegado sobre un dispositivo VMAX (DellEMC) propietario ubicado y gestionado en un CPD externo del proveedor. Algunos productos de esta naturaleza están certificados para poder desplegar el driver CSI y dotar de almacenamiento externo a entornos de contenedores desde un almacenamiento tradicional. En un cierto momento la empresa asume la estrategia de utilizar esta BBDD para mejorar su CRM. Este desarrollo lo quiere hacer en un entorno de contenedores de AWS. La posibilidad de mover los datos vía controlador CSI a AWS desde el CPD de servicio, es un éxito gracias a la inteligencia del SDS. Por cambios el crecimiento anual de la BBDD, el cliente decide desligarse además de la infraestructura propietaria VMAX, contratando al proveedor sus servicios de cloud pública para este almacenamiento. También utiliza la virtualización del almacenamiento para migrar la BBDD sin disrupción alguna. 

Esta toma de decisiones en función de las necesidades del negocio garantizando la portabilidad de aplicaciones, servicios, cambio de fabricantes/proveedores. Y todo ello con la viabilidad técnica que implica la NO disrupción en el negocio, es lo que se considera evitar el _vendor lock in_ . 

Es en este punto también, en el que hay que ligar el concepto hasta ahora mencionado de vendor lock in a la capacidad de elección de recursos, servicios y proveedores bajo demanda de las necesidades de la empresa en cada momento sin coste adicional. Es el ejemplo de abandonar una plataforma para utilizar otra; Pese a que GCP y AWS agrupan sus productos bajo los mismos tipos de categoría, pueden existir ciertos tipos de desarrollo que en un proveedor de servicio se desplieguen de forma más óptima que otro. Es aquí cuando el concepto de la portabilidad en un entorno multicloud reluce, en la selección y movimiento de cargas según la demanda de las empresas en cada momento. Por ejemplo, Cloud Computing de Google consta con un tipo de disco local SSD que aporta más persistencia a algunas aplicaciones que EC2 de AWS (con disco efímero). Este punto pude ser crítico para la toma de decisión de muchas empresas que, en un entorno multicloud, deberían de carecer de problema en mover cargar de una plataforma a otra en cualquier momento. 

41 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **3. Automatización y escalabilidad:** 

Independientemente de la cantidad de datos con los que se trabaje, con una estrategia de múltiples nubes se podrán almacenar todos. Por otro lado, una estrategia de múltiples nubes ayuda a las organizaciones a coordinar cargas de trabajo dispares y administrar flujos de trabajo híbridos. Gracias a la automatización, se beneficia de una disposición eficiente de datos, aplicaciones e infraestructura en múltiples entornos de nube. Dentro de esta automatización, tanto desarrolladores como usuarios de la tecnología/recursos contratados deben tener un control en la planificación del uso del servicio. Más adelante se comentará el papel del Cloud Broker y de su actuación como intermediario en la optimización de este uso de infraestructuras, pero cabe destacar la importancia de la velocidad y de la previsibilidad ligadas a la reducción de costes IT de las empresas. La automatización implica y genera una flexibilidad en el uso y adquisición de servicios. Los entornos multicloud se caracterizan, en parte, por la posibilidad de hacer una previsión del gasto IT que se consumirá en modo pago por uso en función de los servicios utilizados (que no contratados únicamente). Con esto, el impacto económico de las empresas se reduce a la hora de contar con infraestructura, plataformas e incluso backup como servicios. 

#### **4. Seguridad robusta: los proveedores de cloud son responsables de la propia seguridad de sus infraestructuras, por lo que pueden garantizar que tienen todas las capacidades para proteger sus datos:** 

Por la propia seguridad de la infraestructura (ya sea en sabor tradicional o en cloud), debe contar con redundancia y un sistema de backup de datos. En el momento en el que los proveedores de servicio de infraestructura cloud entran en escena, las empresas se ven liberadas de tramitar la definición de este tipo de estrategias ante desastres. Una de las máximas por las que apostar por un entorno multicloud es por la garantía de acceso a datos y servicios que los proveedores cloud ponen a disposición de sus clientes en convivencia incluso con entornos on premises. Servidores, elementos de las redes de comunicación, almacenamiento… se encuentra por defecto redundado para poder prever fallos y paradas en los servicios que una infraestructura cloud ofrece. Es por ello, que externalizar y desligar recursos (total o parcialmente) de una estrategia tradicional, añade un compromiso por parte de los proveedores cloud a la hora de garantizar la disponibilidad de los recursos y servicios contratados. Por ejemplo, en cuestión de almacenamiento de datos, existen mecanismos como la configuración DRAID de los discos de los sistemas, que permiten balancear la carga contratada entre los recursos disponibles en caso de un fallo de hardware. Si este sistema de almacenamiento fallara, existen otros mecanismos como el Hyperswap entre cabinas para garantizar la continuidad del negocio. Incluso la propia geodispersión del dato almacenado en un sistema de objetos para garantizar la no pérdida de información en muchos servicios cloud actuales. 

42 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Todos los elementos de una infraestructura multicloud, y en definitiva de una plataforma cloud, resultan redundados en diferentes ubicaciones para garantizar HA en todo momento de los recursos y servicios contratados o externalizados. 

Además, la adopción de este tipo de infraestructura está justificada por tres razones principales: 

- Ya utiliza un proveedor de nube pública, pero otro proveedor ofrece un servicio que su proveedor actual no ofrece. 

- No desea migrar todos sus servicios, por lo que opta por una estrategia de múltiples nubes. 

- Una infraestructura diversa puede ser más eficiente y rentable, si no se quieren tener todos los recursos IT de la empresa en una misma cesta. 

Además, a nivel de negocio, adoptar un entorno multicloud puede generar un fuerte impacto en todos los departamentos de una compañía. 

- Permitirá a Recursos Humanos identificar y evaluar candidatos de manera más eficaz. 

- Los desarrolladores de productos/aplicaciones podrán acelerar el desarrollo y de las PoC. 

- Los diseñadores de productos podrán crear nuevos productos, con nuevas características y servicios. 

- Monitorización de los datos para nuevas fuentes de ingresos / nuevos usos a la información. 

- Permitirá la optimización de las cadenas de logística. 

- Los especialistas en marketing podrán atraer a usuarios/clientes de manera más eficaz y eficiente. 

- Permitirá la optimización en la gestión de usuarios/clientes potenciales., 

- Creará mejoras en las consultas del servicio técnico de clientes. 

- Aumentará el alcance de las herramientas de colaboración. 

43 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **1.3.3. Retos en la implementación de entornos multicloud.** 

Entre las primeras consideraciones que muchas empresas se plantean a la hora de desarrollar una estrategia multicloud, surgen una serie de asunciones iniciales que han de estar muy bien planificadas en un inicio, para finalizar con éxito la implantación de un entorno multicloud y su posterior gestión. 

#### **Control y planificación de recursos (incluyendo la conectividad entre entornos)** 

El desconocimiento de la ubicación del centro de proceso de datos de las diferentes empresas de cloud proveedoras de un servicio gestionado, puede causar problemas en cuanto a las comunicaciones entre éste y otros proveedores. E incluso entre el centro de proceso privado (cloud privada/ infraestructura on premises) propiedad de la empresa y el proveedor externo. Además, en este punto la red no solo se convierte en un punto crítico, externalizar servicios – que implica externalizar información empresarial – pone en jaque de forma más exhaustiva las medidas de seguridad para ejecutar esta evolución a una infraestructura multicloud. Es decir, los costes en seguridad, red y conocimiento sobre estas áreas son una inversión adicional al propio servicio cloud. 

Como ejemplo: En muchas ocasiones, detectar el origen de un problema de rendimiento en este tipo de entornos (que por ende afecta al rendimiento de despliegues y aplicaciones en uso) puede suponer un reto añadido. Por ello incluir en el esquema de arquitectura multicloud Controladores de Distribución de Aplicaciones (ADCs) supone una alianza en el control del rendimiento tanto desde el acceso a la aplicación como de la aplicación en sí. 

Hasta aquí, se puede encontrar cierta evolución entre los ADCs y los balanceadores de carga de servidor (SLBS). Sin embargo, es importante saber qué tipo de ADC se está utilizando para la óptima integración con el automatismo propio de todo entorno multicloud. Principalmente si nos encontramos utilizando un entorno con alta virtualización de los recursos IT, o en un entorno de computación en la nube. Un requisito favorable para la automatización de la red que conecta diferentes clouds es que estos ADCs sean capaces de hablar protocolo _SDN OpenFlow_ . Una buena segmentación de la red implica además un complemento a los controles y herramientas de seguridad necesarias en este tipo de entornos para garantizar modelos “Trust-Zero”, como por ejemplo el uso de la autenticación multifactor. 

En este control y planificación es crítico por tanto conocer la red, comunicaciones (e incluso distancia entre centros de proceso de datos) que vamos a utilizar. La agilidad implícita y que se asume a la hora de desarrollar una estrategia multicloud puede truncarse por la existencia de retardos entre los entornos que conforman dicha infraestructura. Generalmente por una alta latencia en la red, otras veces por una potencia de cómputo baja por parte del servidor cliente/ o del destino contra el cual se establece la comunicación. 

44 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Por tanto, conocer por ejemplo la caché de los servidores origen y destino a contratar como servicio /adquirir como infraestructura propia, facilita que se cumpla con los requisitos de rendimiento que posteriormente se van a pedir en la solución global. Igualmente pasa con la RAM, también la distancia entre ubicaciones de los recursos físicos o los juegos de línea disponibles. Se debe por tanto contar con una comunicación que evite que el rendimiento de la red sea pobre; En este punto cobran importancia los enrutadores como se ha mencionado y se debe hacer una correcta planificación del ancho de banda contratado/disponible. 

En conclusión, a esto, contar (que no ser propietario) de recursos IT óptimos en clave para una correcta adopción de una infraestructura multicloud. 

#### **Exclusión de recursos innecesarios** 

Un punto decisivo para el correcto funcionamiento de una infraestructura multicloud en la que se combinen servicios, licencias y recursos de diferentes proveedores cloud es el _Business Case_ . Realizar un control sobre el ahorro de costes que supone a la propiedad de diferentes licencias y ligarlo al consumo real de las mismas, es fundamental para el éxito en este camino multicloud. 

#### **Recursos humanos** 

La gestión operativa y las condiciones en el uso de recursos de terceros (hablando en términos tanto de software como de hardware) sufren cambios de manera constante en este tipo de entornos. La formación del equipo IT pasa a considerarse un requerimiento constante. Esto implica que en ocasiones el talento y el conocimiento interno se complementa, de nuevo, con expertos externos a las organizaciones que asumen funciones diarias de este personal técnico en la gestión global de la infraestructura. 

En este punto, es importante realizar una planificación que tenga en cuenta los recursos adicionales necesarios para el soporte de la infraestructura. Nos referimos, a unas garantías de soporte con SLAs 24x7 para contar con personal cualificado que pueda actuar en cualquier momento en caso de fallo de la infraestructura. Este servicio suele externalizarse a la empresa proveedora de la infraestructura (en caso de un cloud privado), al fabricante (en caso de infraestructura tradicional) o al equipo técnico del proveedor del servicio. 

La máxima de la automatización no se ve comprometida a la hora de contar con este tipo de mantenimiento en la adopción, lo que supone principalmente la continuidad de negocio y ningún tipo de fallo disruptivo en el servicio o en la información. 

Tanto la capacitación de los trabajadores propios de la compañía como el apoyo de equipos de expertos externos se convierte, si cabe, en el punto más crítico del proceso de transformación digital de la mayoría de las compañías. 

45 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Se suman a estos tres pilares otros retos a definir o afrontar al acelerar la transformación de cualquier infraestructura / despliegue de un entorno multicloud.  Otros retos de las compañías cubren aspectos y decisiones ligados principalmente a la integración, seguridad y flexibilidad que aporta el potencial entorno: 

1. Transferencia de cargas de trabajo entre diferentes plataformas y proveedores. 

2. Sincronización y movimiento de datos de forma segura entre diferentes plataformas. 

3. Resiliencia. Cómo adoptarla de forma transversal en todas las infraestructuras utilizadas. 

4. Interoperabilidad segura y compatible entre múltiples plataformas. 

5. Aspectos económicos, comerciales y de gobernanza de las infraestructuras. 

6. Administración según requisitos / necesidades dependiendo de las diferentes cargas de la organización. 

7. ¿Estoy modernizando los procesos de desarrollo de mis aplicaciones? Si es así, dónde las alojo. 

Ya sea desde la propia empresa, o desde el servicio de gestión externalizado existen herramientas de apoyo a la implementación que permiten el control, uso combinado y gestión de infraestructura de forma eficiente y segura. 

Antes de continuar con el tema de la administración es necesario abordar el concepto de “infraestructura como código” (IaC). Esto permite gestionar recursos virtuales vía código/programando. Esto supone una gestión automatizada (desde el punto de vista de aprovisionamiento, desarrollo, despliegue y envío de aplicaciones a la nube), de todas las piezas hardware disponibles de forma individualizada, sin necesidad de hacer una configuración manual de las mismas. La infraestructura se convierte, por tanto, en un componente cuya gestión es completamente extensible y reutilizable. Por ello, la inclusión de este tipo de piezas en la gestión de un entorno multicloud puede suponer mayor velocidad en la ejecución, por ejemplo, de una actualización. También un mayor ahorro de costes por el desarrollo de códigos conjuntos extrapolables a la gestión de diferentes recursos. Terraform es una de estas herramientas declarativas que ayuda a la gestión de entornos multicloud. 

46 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Volviendo a la administración que aporta Terraform, que supone una herramienta de gestión de infraestructura en todos sus formatos (desde SaaS -administración de openstack - a servidores físicos y plataforma de contenedores). Uno de los casos de uso más extendido de este tipo de aplicaciones es ayudar a crear y gestionar componentes básicos para la correcta ejecución de aplicaciones y servicios en la infraestructura óptima para ello. Por ello, dentro de la complejidad que requiere la gestión de un entorno multicloud Terraform (y otras herramientas software similares como Puppet, Helm o Ansible entre otras) facilitan la implementación, administración y la concepción única de los diferentes entornos que componen dicho esquema de arquitectura en multitud de empresas; gestión y unificación global de instancias trabajadas en diferentes proveedores cloud como un único recurso para las compañías, orquestación y simplicidad de uso son accesibles con conocimiento de una única herramienta.  La base de su funcionamiento es la definición de cualquier infraestructura como código y provee al administrador de las herramientas necesarias para actualizar la infraestructura bajo demanda y de forma automatizada. 

Por lo tanto, el uso de Terraform y otras herramientas de gestión como IaC proporciona una ejecución más rápida al configurar la infraestructura y aumentan la visibilidad para ayudar a otros departamentos de la empresa a trabajar de forma eficiente garantizando una serie de beneficios: 

- Menor riesgo asociado a errores humanos: mala configuración manual o menor tiempo de inactividad. 

- Testing: los equipos de DevOps tienen la posibilidad de probar las aplicaciones en entornos de producción en el inicio del ciclo de desarrollo. 

- Escalabilidad de los entornos: al evitar la configuración manual de los entornos, las implementaciones de infraestructura con IaC se reiteran en su uso y reducen el tiempo de ejecución. 

- Consistencia en la ejecución: disminuyendo así también la incompatibilidad de diferentes componentes de la infraestructura. También de la generación de una documentación sobre la gestión consolidada. 

### **1.3.4. Soluciones tecnológicas a nivel IT - IA y otras** 

No sólo la arquitectura sobre la que se va a orquestar una estrategia multicloud es importante para la ejecución y adopción óptima de este tipo de infraestructuras. Existen 3 capas por encima que se han de tener en cuenta en esta decisión de diseño según los requerimientos de las aplicaciones a desarrollar por la empresa, las plataformas en uso e incluso la tipología de _software middleware_ con el que cuenta la empresa. O al que recurrirá también como servicio. 

47 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

La definición e implementación de una estrategia multicloud implica el conocimiento de las organizaciones sobre el punto de digitalización en el que se encuentran, y sobre los requisitos en relación con la criticidad de las aplicaciones gestionadas. 

La combinación de estos dos factores junto a las aplicaciones y plataformas usadas por cualquier compañía generan el siguiente _stack_ de elementos. 



Independientemente de la infraestructura en la que se aloje una única aplicación/cada aplicación de una empresa, el objetivo genérico en cualquier infraestructura multicloud es que las cargas gestionadas en dicha aplicación sean nominables a ser movidas. Que sean capaces de transferirse entre una y otra infraestructura, a través de cualquier _middleware_ y plataforma, de forma totalmente transparente a desarrolladores y usuarios según la necesidad de la compañía. 

En el siguiente apartado se expondrán diferentes ejemplos de diseños y arquitecturas multicloud. Para dicho objetivo, es importante identificar los posibles componentes que pueden aparecer en cada una de las capas anteriormente comentadas. 

#### **1. ¿Qué aplicaciones y requerimientos genéricos tienen las empresas?** 

- Aplicaciones críticas de negocio. 

- Desarrollos explotando recursos de Big Data y analítica de datos. 

- Aplicaciones contenerizadas. 

48 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



#### **2. ¿Sobre qué plataformas se despliegan las aplicaciones?** 

A la hora de seleccionar proveedores de cloud la principal estrategia que adoptan todas estas empresas de servicio es el uso de contenedores. Los contenedores como se adelantó en el módulo primero empaquetan y aíslan las aplicaciones y sus entornos en tiempo de ejecución. Por ello, los usuarios son capaces de trasladar una aplicación encapsulada entre diferentes nubes y, al mismo tiempo, conservar toda la funcionalidad de lo empaquetado. Esta es la clave de la elección totalmente flexible de un proveedor cloud u otro por parte de las empresas. Los microservicios son los que orquestan y facilitan esta portabilidad y este esquema de arquitectura. 



#### **3. Se necesita software de gestión de la infraestructura que orqueste la portabilidad de la información entre plataformas.** 

Es importante considerar la virtualización a nivel servidor de cómputo como del almacenamiento (este segundo punto se consigue a través del almacenamiento definido por software como herramienta). Estas tecnologías que permiten crear múltiples entornos simulados o recursos dedicados desde un solo sistema de hardware físico. El software llamado hipervisor se conecta directamente con el hardware alojado en cualquier tipo de infraestructura, y genera la separación de dichos recursos en entornos separados e independientes, las máquinas virtuales (VMs).  Encontramos hipervisores bare metal ejecutados directamente en el hardware del host (como VMWare ESX Server, Wind River, Microsoft Hyper-V , Citrix XenServer) e hipervisores alojados, se ejecutan como una capa de software sobre un sistema operativo (como Oracle VM VirtualBox ,VMware Workstation Pro / VMware Fusion ,Windows Virtual PC). 

49 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Por otro lado, la virtualización del almacenamiento se realiza mediante el almacenamiento definido por software. Este recurso _middleware de software_ genera una capa de abstracción, de nuevo, sobre los recursos físicos (o en cloud) con los que cuenta cualquier compañía. Además de generar una capa agnóstica al fabricante de infraestructura, este componente es clave para acceder a los datos alojados por debajo. Es un punto importante a la hora de plantear una estrategia alejada del famoso _vendor lock in_ . Toda plataforma consta de unos requerimientos en los protocolos de acceso al dato. En una infraestructura multicloud esta capa de software debería, al menos, proponer una interfaz de programación estándar (API) con el fin de gestionar y mantener cualquier sistema de almacenamiento, y garantizar el acceso a cualquier tipo de dato (objeto, bloque o fichero) según los requerimientos de cada aplicación. (IBM Spectrum Storage, Red Hat Data Services, MetroCluster SDS entre muchos otros). 



**4. ¿Dónde se encuentran los recursos físicos de cómputo y almacenamiento sobre los que se apoya todo el IT de la empresa?** 

Por un lado, el cloud público supone la implementación IT más extendida en la que todos los recursos de infraestructura son propiedad de un proveedor externo, y son explotados a través de la red por la empresa consumidora de los mismos. Siendo este proveedor quien administra y ofrece servicios a través de la red. De esta manera ofrecen sus servicios grandes empresas como Alibaba Cloud, Amazon Web Services (AWS), Google Cloud, [[Base_Datos_Costos_Historicos|IBM Cloud]] o Microsoft Azure. Es común en este punto la explotación de este tipo de implementación utilizándola como IaaS, DaaS, BaaS, SaaS… 

El modelo de cloud computing que funciona en una única organización se denomina cloud privado, y puede ser gestionado por personal interno de la empresa o por un tercero. Además, su alojamiento también puede disponerse tras el cortafuegos de la empresa o en centro de proceso de datos externo. El cloud privado supone las mismas ventajas de un cloud público; rápido despliegue, facilidad de uso, escalabilidad y flexibilidad. Pero además el cloud privado garantiza un control del rendimiento, previsión de costes y seguridad mayor.  Es decir, un cloud privado permite personalizar un entorno de acuerdo las necesidades y requisitos de seguridad y utilizada exclusiva de diferentes recursos IT. 

50 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Acompañando al modelo de cloud computing y las modalidades que brevemente se han descrito, existe un tercer tipo de infraestructura que puede iterar y convivir en un entorno multicloud. La infraestructura tradicional u on premises sigue siendo una opción válida y óptima para algunas cargas y formas de trabajar en muchas compañías. 

Independientemente de la implementación elegida, toda infraestructura local, de cloud pública y de cloud privada requiere de recursos físicos para su funcionamiento (y capacidad de servicio). En este punto de infraestructura existen componentes de software como sistemas de gestión de contenido (CMS), sistemas de software de planificación de recursos empresariales (ERP), sistemas operativos y servidores web que se contemplan para una correcta gestión de estos recursos físicos. 

En cuanto a los principales componentes físicos de todo centro de proceso de datos, es imprescindible: 

- Recursos de computación: hace referencia a la memoria y la potencia de proceso necesarios para ejecutar las aplicaciones que proporcionan los servidores, generalmente de propósito empresarial (Intel, HPE, Dell, IBM, SuperMicro, Lenovo). 

- Recursos de almacenamiento: los centros de datos incluyen dispositivos de almacenamiento primario y de copia de seguridad. Granjas de dispositivos _all-flash_ , cintas, despliegue de servidores con disco interno y múltiples tecnologías pueden ser utilizados. (PureStorage, NetApp, DEL EMC, IBM, Huawei, HDS) 

- Redes y comunicación: conmutadores, cortafuegos, controladores, etc. 

Es decir, junto al software de gestión, cualquier centro de proceso de datos se compone de hardware, redes, instalaciones y herramientas necesarias para monitorizar y gestionar toda esa infraestructura. 



51 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **1.3.5.Diseños** 

A lo largo de los módulos y apartados anteriores se han enumerado los requisitos a nivel de servicio, seguridad e infraestructura - entre otros - para la implementación de una correcta estrategia de digitalización en torno al término multicloud. 

Es importante conocer los principales diseños que pueden implementarse y de forma paralela ser válidos en todos los criterios que se han mencionado a lo largo del curso. No hay una única combinación de infraestructuras válida para cumplir con la definición de entorno multicloud. A continuación, se presentan algunas soluciones multicloud fáciles de implementar en numerosas compañías de muy diversas industrias. 

#### **Diseño 1.** 

Existen empresas como OVHCloud que ofrecen numerosos servicios relacionados con el _cloud computing_ . Uno de ellos es el servicio de alojamiento y gestión de infraestructura en sus instalaciones. Es decir, ofrece la posibilidad de crear y contratar también servicios de mantenimiento y gestión de un cloud privado denominado Hosted Private Cloud. Imaginemos que este cloud privado está compuesto por infraestructura dedicada a la larga retención de información de una empresa, una tercera dedicada a la copia de los datos para recuperación ante desastres. A este cloud privado hosteado en una localización externa, se envían datos desde un centro de procesos de datos privado y local, gestionado y mantenido por la empresa contratante de los servicios. Tanto la infraestructura _on premises_ como en Hosted Private Cloud de OVHcloud basan su funcionamiento en plataformas vSphere, vCenter, NSX y vROps. A su vez, OVHcloud ofrece servicios de cómputo con servidores con GPUs dentro de su porfolio de servicios de cloud pública. 

Este es un ejemplo de infraestructura multicloud en el que intervienen: 

- Infraestructura propietaria on premises de la compañía ALPHA. 

- Infraestructura de cloud privada hosteada en un proveedor externo BETA. 

- Infraestructura de cloud pública del mismo proveedor externo BETA. 

52 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

De forma esquemática: 



Para dar vida a este tipo de diseño de una infraestructura multicloud, podemos encontrar numerosos proveedores que ofrecen tantos servicios de _hosting_ de cloud privadas y a la vez servicios de cloud pública. 

Es importante detallar, que, si una empresa únicamente acude a los servicios de cloud privada y de cloud pública señalados en este diseño, cambiaremos de modelo de infraestructura y estaremos describiendo una infraestructura híbrida. 

#### **Diseño 2.** 

Una empresa decide adquirir un almacenamiento de objetos (accesible vía protocolo S3) en sus propias instalaciones. Este almacenamiento típico de implementaciones de almacenamiento cloud garantiza mayor durabilidad del dato, se considera, en muchas ocasiones un almacenamiento _backup less_ y genera un acceso directo vía APIRest a la información. Nos encontramos ante un almacenamiento cloud privado local y alojado en servidores x86 _standard_ . Sobre él una capa de almacenamiento definido por software. Esta empresa consta de dos nuevos equipos de desarrollo con el objetivo de empezar a trabajar con contenedores.  Para ello apuestan por RedHat Openshift sobre Azure, es decir una plataforma para creación y despliegue de contenedores sobre una infraestructura de cloud pública. 

Se apoya en vRealize, producto de gestión integral de entornos multicloud. 

53 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Como la intención de esta empresa es que su repositorio de almacenamiento de objetos se convierta en el recurso de almacenamiento externo de cualquier clúster levantado en Azure, cree necesaria una pieza de gestión cloud. Para ello apuesta por VMWare Cloud Manage Platform. 

Este es un ejemplo de infraestructura multicloud en el que intervienen: 

- Infraestructura de cloud privada on premises de la compañía ALPHA. 

- Infraestructura de cloud pública de proveedor externo BETA. 

- Paquete de gestión de infraestructura multicloud del proveedor GAMMA. 

#### **Diseño 3.** 

Una empresa comienza reutilizando sus recursos de infraestructura _on premises_ para desarrollar un entorno no productivo para test y desarrollo con contenedores. Optan por utilizar Kubernetes. Adquieren licencias de Anthos Onprem para la administración de las aplicaciones y operaciones de la plataforma Google Kubernetes Engine (GKE) sobre VMware. Tras este periodo de pruebas, optan por una estrategia multicloud para contar con dos equipos independientes en el rediseño de las actuales aplicaciones de la empresa; su automatización en la medición del uso energético de sus clientes, y su aplicativo postventa. Toman la decisión de extender la tecnología utilizada en su entorno on premises al cloud de Google Cloud y en modo consumo de licencias de clústeres GKE de Amazon Web Services (AWS). El piloto de cada aplicación comenzará en la infraestructura propietaria. Tras la planificación de recursos deciden finalizar el desarrollo de sus aplicaciones en Google Cloud, portando el piloto, para su posterior despliegue y gestión del CRM posventa en AWS.  La automatización del estado de las instancias de las aplicaciones desplegadas en diferentes clústeres en todo momento se realiza por Anthos.  La visión, administración, control y gestión de todo el proceso de rediseño de la aplicación, desarrollo del piloto y ejecución como servicio se manejan de forma conjunta desde el panel de Google Anthos. Esta empresa se plantea un modelo multicloud basado en microservicios. 

Este es un ejemplo de infraestructura multicloud en el que intervienen: 

- Infraestructura on premises de la compañía ALPHA, con gestor de contenedores de la empresa PI. 

- Infraestructura de cloud pública de proveedor externo BETA con gestor de contenedores de la empresa PI. 

- Infraestructura de cloud pública de proveedor externo PI con gestor de contenedores de la empresa PI. 

54 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

De forma esquemática: 



### **1.3.6. Escenario común en la adopción de una estrategia multicloud. Caso de uso.** 

A continuación, se describe el proceso de transformación del mundo local puro, a explotar recursos de diferentes proveedores. 

Una empresa basa su actividad en el uso de infraestructura local en una granja de servidores virtualizados, para dotar de recursos a las aplicaciones tradicionales de su empresa y de almacenamiento local en dispositivos NAS. Esta empresa comienza a almacenar imágenes captadas por una serie de satélites y a procesarlas con esta infraestructura. El crecimiento de datos no estructurados es mayor del esperado, y deciden valorar opciones de infraestructura en la nube para la creación de un nueva _data lake_ de la empresa. Para ello, estudian la convivencia de su infraestructura local con una infraestructura en cloud económica y escalable. Además, y con una parte de los datos incluidos en su _data lake_ , la empresa decide ejecutar una estrategia de analítica de datos cada 3 meses. Con ello pretenden generar un modelo predictivo que les permita mejorar la productividad y los resultados de la empresa semestralmente (ciclo de tratamiento de los datos e implantación de las mejoras de sus aplicativos de negocio). Tras el estudio de diferentes proveedores cloud, las SLAs de cada uno de ellos, y estudiar los diferentes protocolos de seguridad ofrecidos. La empresa llega a la conclusión que, la mejor fórmula es mantener la infraestructura local para el funcionamiento diario de sus aplicaciones históricas, mientras que Google Cloud es la opción que mejor encaja para empezar a crear su _data lake_ . 

55 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Pese a que Google consta de herramientas para el propósito de proceder a aplicar analítica sobre sobre estos datos, la explotación puntual de esta información decide realizarla en AWS. AWS le ofrece Amazon EMR y la posibilidad de utilizar Spark y Hadoop de forma muy optimizada. El resultado de este proceso tiene como fin mejorar la aplicación CRM de la compañía y supondrá una mejora de la principal aplicación core de la compañía. Esta empresa ha desarrollado y adoptado una estrategia multicloud basada en la conexión entre infraestructuras vía VPN. 

Gráficamente: 



### **1.3.7. Aplicación y gestión de una infraestructura multicloud** 

La elección de un XaaS (X as a Service), pudiendo ser aplicado a toda carga de Inteligencia Artificail, así como localización de los sistemas empresariales, permite centrar los esfuerzos de desarrolladores y equipos IT en las aplicaciones que creen un diferencial en la actividad empresarial de sus empresas. Sin embargo, esa elección de Infraestructura como servicio (IaaS), backuo como servicio (BaaS) etc., existe un cambio en el rol de gestor IT interno en las compañías. 

56 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **1.3.8. Optimización usando entornos multicloud** 

Como se ha podido observar, existen numerosas combinaciones a la hora de contar con recursos IT provistos por diferentes proveedores además de los propios. Para una óptima explotación de una determinada infraestructura multicloud existen técnicas, mecanismo e incluso algoritmos a utilizar. En este punto, resulta necesaria la introducción del término cloud _brokerin_ que engloba todas estas técnicas para una mayor automatización y uso beneficioso de la actual oferta de servicios cloud. 

Actualmente existen algoritmos estáticos y customizables para la optimización de parámetros a la hora de considerar ciertas restricciones en el uso de una u otra infraestructura y servicio. Al final, todo ello se orienta al ahorro en el uso de dichos recursos y de la selección del camino óptimo para cada empresa. Desde la creación de algoritmos específicos para cada organización orientados a la predicción de costes, la estimación futura de recursos de la empresa, hasta la predicción del uso de almacenamiento de datos en base a roadmap de proyectos... Este tipo de algoritmos aritméticos ayudan a las empresas, por ejemplo, a tomar decisiones como la localización óptima en cuestión de rendimiento de las aplicaciones en cada momento. Pudiendo indicar en cada momento un viraje necesario para tomar una ruta óptima. O, dicho de otra manera, pudiendo recomendar una reubicación del total o parte de la infraestructura en otro proveedor de cloud para optimizar el conjunto de todos los recursos de una empresa (a nivel coste y rendimiento). De nuevo es importante para esta automatización positiva lo ya comentado respecto a evitar el _vendor lockin_ . 

### **1.3.9. Capacitación para afrontar la gestión de un entorno multicloud** 

Actualmente se puede afirmar que el máximo común denominador es la aplicación de diferentes técnicas de Big Data en las empresas, así como el refuerzo de todo lo relacionado con la Ciberseguridad. También la adopción de Blockchain, DevOps y el reto del tratamiento de grandes volúmenes de datos. Parcialmente o en su totalidad, esto queda enmarcado en la transformación digital de las empresas y en la cada vez más frecuente tendencia de implantación de infraestructuras multicloud. 

Pensando en el personal interno de las empresas que de forma histórica gestionaban el IT de las compañías de formar generalista, cada vez se exige una mayor especialización en áreas como las anteriormente mencionadas. Desde el punto de vista de desarrolladores de aplicaciones, gestores tradicionales de _software y middleware_ , la tendencia de implantar técnicas Agile requiere una reeducación corporativa en los modelos internos de las empresas respecto a la gestión y capacitación de equipos IT. Pensando en el área de infraestructura y sistemas la cercanía al área de negocio es cada vez más común debido a este modelo diferente de consumo de recursos IT. 

57 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

En este punto es importante, la división entre decisiones como mantener un modelo especializado de gestión propia de recursos críticos para la empresa, y la externalización de la gestión de recursos que, dadas las tendencias en el mercado, muchas empresas ponen en manos de diferentes proveedores cloud y de servicios. Sin embargo, esta necesidad operativa se diluye en tareas externalizadas que requieren de una formación a nivel más funcional dentro de las compañías. 

En esta transformación, toda empresa cuenta con especialistas (ya sea como personal interno o como personal de una empresa externa) que lideran el cambio IT en las empresas. Se reconocen y denominan arquitectos cloud. Su capacitación en tecnologías ligadas al concepto Cloud Native les permiten diseñar y configurar la mejor estrategia cloud. Personas con este rol son capaces de diseñar una arquitectura de aplicación sólida y segura y capaces de implementarlas en las tecnologías de la plataforma correspondiente en cada caso (ya sean AWS, Microsoft Azure, Google Cloud Computing o IBM Cloud). También es capaz de definir soluciones mediante el uso de principios de arquitectura basados en los requisitos del cliente y ofrecer directrices de implementación durante el ciclo de vida del proyecto. 

Más allá del rol de arquitecto cloud que orquesta la transformación de las empresas en torno a una infraestructura cloud, ser consciente de los principales servicios que demandan las empresas como servicio, es clave para entender la formación necesaria de especialistas IT en diferentes áreas. Desde un punto de los servicios que más externalizan las empresas encontramos servicios de correo y calendario, bases de datos (DBaaS), servicios de hosting, transferencia de archivos, suites de ofimática, CRMs y ERPs y escritorios virtuales entre otros. Esto hace que el personal externo a una compañía encargado a nivel operativo de estas áreas (entre otras) tenga que adquirir un conocimiento técnico y profundo en cada una de estas herramientas y softwares. Pensando en todo el _stack_ de productos orientados a la gestión de clientes y las ventas, muchos proveedores de cloud ayudan a sus clientes a gestionar herramientas, como por ejemplo SAP ERP para la planificación de recursos empresariales. De esta manera toda empresa que ofrece este tipo de servicios debe tener personas expertas en software y plataformas, desligando esta necesidad en el personal interno de la empresa contratante. Algo parecido pasa con la contratación, por ejemplo, del paquete Office365 como servicio, en el cual se elimina la necesidad de poseer una licencia de ningún producto de la Suite. 

Especialistas en la era multicloud con conocimientos de MySQL, PostgreSQL, Oracle, SQL Server, aplicaciones y plataformas relacionadas con analítica de datos, Data Warehouse, y una larga lista de tecnologías y aplicaciones, tienen cabida en un momento en el que la especialización es clave para el éxito en la implantación de este tipo de infraestructuras. 

58 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Además del valor del conocimiento técnico y estratégico de IT en la actualidad, las empresas cuentan para la correcta implantación de una infraestructura multicloud con el denominado rol de Cloud Broker. Ya comentado brevemente en el apartado anterior, un Cloud Broker es una persona experta en la algoritmia necesaria para la búsqueda de modelos óptimos respecto al consumo de servicios y recursos cloud. Este agente puede ser contratado como intermediador entre la empresa que adquiere un servicio y el proveedor propiamente dicho del servicio de cloud computing seleccionado. Un cloud bróker es capaz de detectar la localidad óptima para el consumo o ubicación de infraestructura/ alojamiento de plataformas /tratamiento de cargas. La gestión de la información tanto del contexto cliente como de abanico de oferta en el mercado cloud, permite que el cloud bróker negocie bajo necesidad el consumo óptimo para la empresa de los recursos más beneficiosos en cada momento. Esta máxima está totalmente alineada al objetivo último de la adopción de una estrategia multicloud; flexibilidad y optimización de los recursos IT. 

### **1.4. Proveedores de servicios cloud. Visión general** 

La computación en la nube permite alojar en la nube datos, aplicaciones y servicios de una empresa, que están accesibles siempre que haya acceso a internet. Entre los proveedores de Cloud Computing existe una tendencia a evolucionar sus servicios (e incluso tarifas) para adaptarse a las necesidades de negocio cambiantes actuales. Sin embargo, apuntadas por Forbes existen empresas que aglutinan una mayor popularidad y extensión por su modelo de Cloud Computing ofrecido. 

#### **Microsoft** 

La gran fuerza de servicios en las tres capas de la nube (IaaS, PaaS y SaaS) conjugado con el gran esfuerzo en desarrollo de aplicaciones y plataformas para que sus clientes puedan implementar AI, ML y Blockchain en entornos de producción hacen que Microsoft sea cada vez uno de los proveedores elegidos por muchas empresas que optan por recurrir a este tipo de servicios. 



59 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **Google** 

Google Cloud Platform consta de más de 100 productos cloud (principalmente en sabor PaaS y SaaS) Entre sus productos destacados ofrece máquinas virtuales, bases de datos SQL, almacenamiento, entornos para ejecutar aplicaciones contenerizadas, red de distribución para publicar contenido web/vídeo, gestión de APIs, IA y aprendizaje automático. También herramientas para gestionar entornos de cloud híbridos y multicloud. 



#### **Amazon** 

Desde un inicio Amazon (AWS) se convirtió en ejemplo del movimiento del Cloud Computing. No resulta el proveedor de cloud más fuerte de software End-to-End, pero Amazon Web Services ofrece una experiencia de usuario sencilla, amigable y asumible económicamente. Estos factores hacen que sea una de las primeras opciones de adopción Cloud para muchas compañías. AWS es la única nube que ofrece una red Ethernet de 100 Gbps para instancias informáticas. 



60 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **IBM** 

En los últimos años IBM ha reforzado su porfolio de servicios y su capa de software que permiten conectar entornos de cualquier naturaleza. Además, esta empresa americana es uno de los proveedores que lidera la opción completa en el uso de servicios de Cloud Computing: IaaS, PaaS y SaaS. Esta oferta en su servicio es una gran ventaja respecto a otros competidores dado que consigue aportar más opciones a los clientes, una integración más fluida y una mejor ciberseguridad. 



#### **Salesforce.com** 

Ofrece una gran innovación y una estrategia de provisión a sus clientes diferencial respecto a su servicio SaaS. La especialización ha hecho que sea referente en este tipo de servicio. 



61 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **SAP** 

Esta empresa es proveedor por excelencia de aplicaciones empresariales en todas las compañías líderes del mundo. SAP tiene alianzas con Amazon, IBM ,Google y Microsoft (entre otras) que le permiten rediseñar sus servicios y aplicativos de forma dinámica para sus clientes. SAP tiene un futuro ligado al modelo de Cloud Computing muy prometedor gracias a su solución HANA. Esta tecnología (procesamiento en memoria alojado en una plataforma de Cloud SAP) permite desarrollar nuevas aplicaciones o módulos de forma más personalizada a todos los clientes de SAP en relación con dichas ampliaciones empresariales. 



#### **Alibaba** 

Pese a que su presencia en Europa aún no está muy extendida, esta empresa asiática cuenta con su propia plataforma de Cloud Computing (Alicloud). Tiene un catálogo de productos, con nubes privadas, base de datos, analítica, seguridad, IA, aplicaciones para empresas, IoT y servicios para desarrolladores. 



62 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **Otras empresas** 

##### **CenturyLink:** 

A través de sus más de 70 centros de procesos de datos provee servicios cloud a empresas, centrados especialmente en soluciones de comunicaciones, servicios de red, seguridad, entornos de nubes públicas, nubes privadas, híbridas y multicloud, entre otros. 



<u>https://www.centurylink.com/</u> 

##### **Virtustream:** 

Esta empresa está vinculada al fabricante EMC (que pertenece al Grupo Dell). Ofrece servicios híbridos en la nube, de software e IaaS, para grandes empresas, gobiernos, MSPs ,y CSPs. Utiliza grandes centros de procesos de datos en propiedad para dar estos servicios en todo el mundo. 



<u>https://www.virtustream.com/</u> 

##### **Rackspace:** 

Ofrece soluciones integrales multicloud. Tiene partnership con las plataformas cloud más conocidas (Azure, AWS y Google Cloud entre otras). Esta empresa norteamericana ofrece soluciones orientadas a la migración a la nube, bases de datos, seguridad en la nube, así como soluciones ERP para empresas. 



##### **Fujitsu:** 

Mediante Enterprise ofrece servicios en la nube, como por ejemplo sistemas integrados; almacenamiento, servidores o infraestructura de gestión. También con multiclouds asociado con AWS, Azure, Oracle y VMWare. 



<u>https://www.fujitsu.com/es/</u> 

<u>https://www.rackspace.com/es</u> 

63 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **1.5. Best práctices del consumo cloud. General** 

Cualquier planteamiento de la incorporación de un servicio cloud en una empresa es necesaria la realización de un ejercicio/cálculo financiero. Existen empresas como ISACA (Information Systems Audit and Control Association) que permiten realizar un estudio previo del ROI del proyecto contemplando tanto el coste total de propiedad (recursos consumidos), el valor neto, y la tasa interna de retorno entre otros parámetros. 

Un ejemplo muy valioso de coste no medible upfront es el coste por problemas con la copia de seguridad y su recuperación. Para muchas empresas este tipo de ejercicios es la realización de estudios en torno a la infraestructura de backup. En ocasiones según el tráfico de lectura de estas copias, hacer una recuperación de los datos de backup (que estaban en el Cloud) puede implicar que los costes de consumo de recursos cloud se disparen. ¿Cuándo necesitaré recuperar una copia de seguridad? En la mayoría de las ocasiones es imprevisible, y toda bajada de información supone por lo general un gasto para la empresa cliente del servicio. Además de los cálculos financieros estándares (que deberían considerarse casi de obligada ejecución para considerar las bondades y ahorros del consumo cloud), existen muchos otros costes ocultos del cloud a considerar a la hora de pensar y poner en práctica una estrategia empresarial de este tipo.  Algunos de ellos son: 

- **Costes de rollback:** 

En ocasiones un cambio regulatorio, o la insatisfacción con un proveedor externo cloud, hacen que se deba volver al centro de proceso de datos/ in-house. 

- **Costes de mantenimiento:** 

Cuando empresas de servicios cloud actualizan sus plataformas es necesario comprobar que lo que tenemos contratado con ellos sigue sirviendo para el propósito con el que adquirimos el servicio, nuestras aplicaciones siguen siendo compatibles y ejecutables… 

- **Pérdida de know-how de IT:** 

El consumo cloud suele traducirse en reducción de personal interno, que en algunos casos hace que el know-how del área IT de la empresa merme también. Si más adelante fuera necesario devolver aplicaciones al centro de proceso de datos/ inhouse esto se convierte en una desventaja y futuro coste adicional. 

- **Costes de auditorías:** 

Las auditorías que antes se realizaban en la propia empresa ahora deben realizarse directamente en el proveedor cloud. Esto implica auditar un entorno altamente complejo y desconocido. 

64 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- **Costes de conformidad:** 

La conformidad con leyes sobre el tratamiento de la información, más en los últimos años, es muy complejo especialmente para grandes empresas. El consumo de servicios en un único proveedor cloud puede implicar el no cumplimiento de alguna normativa al respecto, más en empresas con sedes en múltiples países. 

- **Nubes no detectadas:** 

Por desconocimiento, los trabajadores de cualquier empresa (especialmente a nivel usuario) puede crear «nubes» no detectadas que provoquen riesgos de seguridad.  Simplemente con el uso de servicios de almacenamiento en la nube, como Dropbox, Box, Google Drive puede darse esta situación. 

- **Almacenamiento no apropiado:** 

Carecer de conocimiento sobre si se están aplicando eficiencias como la compresión y la deduplicación en el Backend de la infraestructura contratada puede provocar un desperdicio del espacio de almacenamiento por el cual se está pagando. 

- **Costes de gestión del riesgo:** 

La necesidad de adquirir software para encriptar, realizando backups, auditorías de logs, y planificando y probando estrategias de reducción del riesgo... Es necesario para evitar cualquier riesgo adicional asociado al uso de cloud. 

- **Costes de migración:** 

Migrar ciertas aplicaciones que no estaban planificadas a un entorno cloud, o servidores no virtualizados, tiene un impacto en el coste. Se convierte en necesario sincronizar los datos con el proveedor cloud, gestionar la autenticación/autorización de los usuarios, y desarrollar procesos de gestión globales. 

- **Costes de proveedor:** 

Operar con un único proveedor, o ir a un modelo de servicio propietario puede convertirse en contradictorio en la estrategia de gestión del cambio. 

- **Costes de gestión de los datos en tránsito:** 

Al consumir servicios y recursos cloud, todos los datos que salen/entran deben estar encriptados mediante certificados SSL. Con esto se consigue una garantía de seguridad. Gestionar dichos certificados puede volverse compleja y derivar en costes ocultos asociados. 

65 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- **Costes de personalización:** 

Desarrollar nuevas aplicaciones o integrarlas al negocio, puede conllevar costes de personalización de estas. 

- **Costes de comunicaciones:** 

Las empresas de comunicaciones que dan acceso a la empresa cliente a internet (y por tanto a los servicios de su proveedor cloud), ofrecen líneas de calidad, duplicadas y seguras que hacen que no solo el proveedor cobre de acuerdo con el ancho de banda (cantidad de datos transmitidos/recibidos). Este coste puede verse repercutido en la factura del cliente que incluso en ciertos casos puede optar también por la adquisición de hardware para optimización del tráfico de red WAN. 

Para optimizar los costes de cada proyecto es imprescindible analizar el diagrama de arquitectura y los usos estimados para tratar de encontrar puntos no óptimos en el despliegue. 

Por ejemplo, en ocasiones una máquina virtual no necesita estar 24h encendida para el correcto funcionamiento de un proyecto. Si el servicio solo va a ser empleado en horas de oficina, será clave emplear un scheduler que nos permita encender y apagar automáticamente la instancia, de tal forma que no tendremos que pagar por todas las horas no hábiles de la máquina como si esta estuviera encendida. 

Este mismo principio aplica a los sistemas de almacenamiento. En ocasiones un proyecto almacena todos los datos históricos que han sido procesados y/o generados por motivos legales o contractuales. Sin embargo, en la mayoría de las ocasiones hay un periodo de tiempo a partir del cual se permite el borrado de estos datos. Si esto no se tiene en cuenta, el almacenamiento crecerá de forma constante y por tanto el coste asociado al mismo. Sin embargo, si se implementa un proceso automático de borrado de backups, podremos mantener la cantidad de almacenamiento empleada bajo control y por tanto la facturación de este. 

De igual manera podemos tratar cualquier recurso en la nube para optimizar su consumo. Si el servicio que desplegamos en la nube tiene grandes transferencias de archivos y nuestro proveedor cloud factura por unidad de transferencia de red, quizá podemos comprimir estos archivos, cambiar su formato, o limitar la información que contienen a la esencial. 

66 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Aplicar esta mentalidad requiere comprender la arquitectura del sistema y el modelo de pago y unidad de pago que nos repercutirá el proveedor cloud, para encontrar el encaje perfecto entre ambas dimensiones. 

De forma muy similar, es importante contar con el periodo estimado de mantenimiento de un despliegue. Como ya hemos comentado, los proveedores cloud ofrecen interesantes descuentos en el caso de reservar recursos para un periodo de tiempo comprometido que suele variar entre el año y los tres años.  Si en un despliegue la arquitectura implica la contratación de una máquina virtual que sabemos con certeza que estará activa durante un año o más, será importante conocer las opciones que ofrece nuestro proveedor cloud como beneficio por la reserva del recurso. 

### **1.6. Resumen del apartado y actividades de fortalecimiento del capítulo** 

Desplegar y delegar ciertas herramientas y servicios de cualquier negocio en un entorno cloud es resultado de la búsqueda en un medio- largo plazo de buscar ventajas competitivas en un mundo cada vez más digital. Los equipos de TI ,alineado con otros departamentos relacionados directamente con el negocio, están decidiendo trasladar cada vez un mayor número de sistemas a infraestructura propiedad de proveedores cloud como AWS, Google Cloud o Microsoft. Apostar por una estrategia cloud permite lograr la agilidad para reaccionar al cambio en el paradigma en la gestión de recursos IT. De esta manera aumentar el valor proporcionado a las empresas. 

Gracias a la flexibilidad que ofrecen las suscripciones de SaaS en la nube, los responsables de TI pueden garantizar una gestión de gastos más efectiva al tiempo que amplían la capacidad de sus recursos internos y productivos. 

Implementar esto en un sabor de cloud público, híbrida y/o privada es decisión de cada empresa, siendo esta decisión totalmente customizables a las necesidades de servicio de cada empresa. SaaS, IaaS , PaaS son los principales servicios delegados en proveedores de servicio cloud. Pero existen otros cuya administración por parte de estas empresas es muy sencilla como puede ser la oferta de BaaS (con el consecuente DRaaS). 

A continuación se presentan una serie de actividades para consolidar el temario comentado. Encontrará las oluiones al final del módulo. 

67 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

**1. Asocia los términos con sus respectivas definiciones aprendidas en de este módulo en relación con los entornos multicloud.** 

|Vendor lockin|Garantizar la portabilidad de aplicaciones sea cual sea<br>su naturaleza|
|---|---|
|Flexibilidad|Modelo de despliegue de cloud computing donde<br>infraestructura, y los recursos de computación son de<br>uso exclusivo del cliente|
|SLA|Posibilidad de migrar de un proveedor de cloud a<br>otro sin coste ni disrupción algunos en la actividad<br>empresarial|
|Nube pública|Modelo de despliegue de cloud computing donde<br>infraestructura, y los recursos de computación son de<br>uso compartido entre clientes|
|Nube privada|Definición de un nivel de servicio/acuerdo/ política<br>para automatizar el movimiento de cargas entre<br>diferentes entornos|



**2. Utilizando los términos indicados, completa las siguientes afirmaciones relacionadas con los retos y beneficios de la implantación de un entorno multicloud.** 

|Capacitación<br>Automatización|Planificación|Competitividad|Monitorización|
|---|---|---|---|



1. El objetivo de implantar una infraestructura multicloud es aumentar la …………… del negocio mejorando, entre otras cosas, el consumo en recursos IT de la empresa 

2. Una correcta ……………de la red es crítico para garantizar un nivel de acceso, seguridad y rendimiento de la infraestructura. 

3. Implementar una estrategia multicloud implica un esfuerzo en la mejora y cambio de la …………. del personal, ya sea externo o interno. 

4. Existen herramientas que permitirán la ……………en el movimiento de cargas entre diferentes infraestructuras según la conveniencia para la empresa. 

5. En un entorno multicloud existe la opción de tener una ………………. centralizada para considerar las diferentes infraestructuras un único recurso a gestionar. 

68 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

**3. Investiga y arrastra/asocia cada plataforma /software de infraestructura/infraestructura en el stack correspondiente según el esquema estudiado en este módulo.** 



**4. Indica si son verdaderas o falsas las siguientes afirmaciones.** 

1. Evitar el vendor lockin no evita una penalización alguna en el uso de servicios y plataformas e infraestructuras bajo necesidad. 

2. La figura del Cloud Broker tiene conocimientos para optimizar la ubicación de aplicaciones y uso de plataformas. 

69 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

3. Por lo general, servicios como las suites de ofimática y aplicaciones críticas para el negocio requieren los mismos requisitos. Por lo que se pueden utilizar exactamente los mismos recursos IT. 

4. Terraform implica una visión global de infraestructura como código. Por ello, la gestión global de toda la infraestructura se simplifica. 

5. El departamento IT de las empresas cada vez está más alineado con las necesidades del negocio, por lo que la externalización de servicios se suma a la externalización de infraestructura. 

70 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

## **2. APIs de Visión Artificial y NPL** 

_“El NLP se define ampliamente como la manipulación automática del lenguaje natural, como el habla y el texto, por parte del software.”_ 

En módulos posteriores se hará hincapié en la temática del Procesamiento del Lenguaje Natural (NLP en inglés en adelante) y la Visión Artificial, sin embargo es importante ligar ambos campos a la temática del cloud computing y a la tendencia tecnológica de empleo de esta modalidad para el uso de IA. 

El NPL se diseñó para ser un puente de lenguaje humano-máquina que transfiere la responsabilidad de comunicarse con los servidores de cómputo de los humanos a esas máquinas cada vez más capaces de imitar los procesos comunicativos. Es decir, el NLP se define ampliamente como la manipulación automática del lenguaje natural, como el habla y el texto, por parte del software. Es interesante saber que el estudio del NPL existe desde hace más de 50 años y surgió del campo de la lingüística con el auge de las computadoras. Es un campo interdisciplinario que se ocupa de las interacciones entre las computadoras y los lenguajes humanos naturales y que garantiza que los softwares que se nutren de esta tecnología nos ayuden en nuestra vida diaria de múltiples formas maneras. Algunos ejemplos conocidos son: 

- Asistentes personales: Siri, Cortana y Google Assistant. 

- Autocompletar: Extendido en motores de búsqueda. 

- Verificación ortográfica: desde en navegadores, su IDE (Visual Studio), aplicaciones de escritorio (Microsoft Word). 

- Traducción automática: Traductor de Google. 



71 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

El NPL juega un papel importante en nuestras interacciones diarias con cualquier clase de dispositivo, también en casos de uso relacionados con el negocio se puede encontrar el NLP como un factor diferencial de las empresas. Desde las cadenas de supermercado que reciben diariamente una gran cantidad de pedidos y quejas, se pueden beneficiar de los avances recientes en la IA conversacional para crear asistentes virtuales que automaticen dichos procesos y reduzcan la intervención humana. También todo tipo de marcas que lancen nuevos productos y los comercializan en plataformas como redes sociales, pueden medir las tasas de éxito de las campañas utilizando métricas como el alcance y la cantidad de interacciones. Esta tarea se puede automatizar mediante el análisis de sentimientos, una tarea de clasificación de texto en la que se entrenan modelos de aprendizaje automático para cuantificar estados afectivos e información subjetiva. 

El NPL se divide principalmente en dos campos: lingüística e informática/tecnología. 

El lado de lingüística se enfoca en comprender la estructura del lenguaje, el NPL abarca todos los subcampos 

- Fonética: El estudio de los sonidos del lenguaje humano. 

- Semántica: El estudio del significado de las oraciones. 

- Pragmática: El estudio de la forma en que las oraciones con sus significados semánticos se usan para objetivos comunicativos particulares. 

- Fonología: El estudio de los sistemas de sonido en los lenguajes humanos. 

- Morfología: El estudio de la formación y estructura interna de las palabras. 

- Sintaxis: El estudio de la formación y estructura interna de las oraciones. 

Desde el punto de vista de la informática, esta se ocupa de traducir el conocimiento lingüístico y la experiencia en el dominio de la lengua, en programas informáticos con la ayuda de subcampos como la inteligencia artificial. Los sistemas basados en NPL se pueden a su vez dividir en sistemas basados en reglas, modelos clásicos de aprendizaje automático (ML) y modelos de aprendizaje profundo (DL). 

Los sistemas basados en reglas se basan en gran medida en la creación de reglas específicas de dominio como por ejemplo, expresiones regulares. Esto permite automatizar tareas simples como extraer datos estructurados de datos no estructurados. Sin embargo, debido a la complejidad de los lenguajes humanos, los sistemas basados en reglas no son extremadamente precisos además de que son difíciles de mantener y no se pueden generalizar en diferentes dominios. 

72 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Los modelos de DL son actualmente los más populares en la investigación y las aplicaciones del NPL. Se emplean de forma más generalizada incluso mejor que los enfoques clásicos de ML. Esto es debido a que no requiere de características hechas a mano o supervisión porque funcionan automáticamente como extractores de características, lo que permite el entrenamiento de modelos de extremo a extremo de una forma más completa y rápida. Las capacidades de aprendizaje de los modelos de DL son más poderosas que las de ML clásico, lo que allá su uso en NLP, por ejemplo, traducción automática. 

El procesamiento del lenguaje natural, a medida que avanza, intenta cada vez más comprender tanto la inflexión como el contexto. Por ejemplo, supongamos que está viendo una película y reconoce a uno de los actores, pero no sabe su nombre. Una futura IA con NLP avanzado sabría qué película estás viendo y podría tener un diálogo contigo que identificaría a quién como consumidor de cine querrías ver. 

El verdadero objetivo de la IA en general, y del NLP en concreto, es tener algo que entienda su necesidad como ser humano y la proporcione una respuesta natural en consonancia. 

Testear este tipo de tecnología desde los servicios de cualquier proveedor de cloud comentado es sencillo. 

1. Acceda a: https://cloud.google.com/natural-language 

2. Introduzca un texto a analizar. Click en ANALYZE. 



3. Estudie los resultados en función de los campos lingüísticos que forman parte del lenguaje natural humano. 

73 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



Como el ejemplo recién ejecutado, a lo largo del módulo en el que se han analizado los principales proveedores de servicios de IA relacionados con NPL en Cloud y se ha tratado con qué herramientas cuentan fabricantes como AWS o Azure. Sin embargo, también existen herramientas de código abierto para el procesamiento del lenguaje natural (NLP) en las que también chatbots, asistentes de voz, texto predictivo y otras aplicaciones de voz/texto pueden basarse. 

Independientemente de que uno de los lenguajes más extendidos en los que se basa en NLP es R, este es un lenguaje orientado (o al menos uno de los más utilizados a día de hoy) en el mundo académico y la investigación. También Scala consta con bibliotecas para el desarrollo de aplicaciones basadas en NPL. Por extensión en uso para NPL por tanto, el apartado se centrará en herramientas de código abierto basadas en Python, Java y Node. 

74 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **2.1. Herramientas de Python** 

**Kit de herramientas de lenguaje natural (NLTK)** 



Sería fácil argumentar que Natural Language Toolkit (NLTK) es una de las herramientas más completas actualmente.  Implementa prácticamente cualquier componente de NLP que se pueda necesitar; desde clasificación, tokenización, derivación, etiquetado, análisis y razonamiento semántico. A menudo hay más de una implementación para cada uno de estos procesos, por lo que se puede elegir el algoritmo o la metodología exactos a usar. También es compatible con muchos idiomas. Representa todos los datos en forma de cadenas, lo que está bien para construcciones simples pero dificulta el uso de algunas funciones avanzadas de tratamiento del lenguaje. La biblioteca de NLTK en general cuenta con un gran conjunto de herramientas para experimentación, exploración y aplicaciones. 

#### **SpaCy** 



SpaCy es probablemente el principal competidor de NLTK. Es más rápido en la mayoría de los casos a la hora de ejecutar código, pero tiene una implementación única para cada componente de NLP. Representa todo como un objeto en lugar de una cadena, lo que simplifica la interfaz para crear aplicaciones. Esto le permite tener una integración amplia con muchos otros frames y herramientas de ciencia de datos que implica que tenga una mejor comprensión de los datos, especialmente de texto. Sin embargo, SpaCy no admite tantos idiomas como NLTK. Tiene una interfaz sencilla con un conjunto simplificado de opciones y excelente documentación pública para su manejo. Cuenta también como múltiples modelos neuronales para diferentes componentes de procesamiento y análisis del lenguaje y en general es una gran herramienta para nuevas aplicaciones que necesiten tener un buen rendimiento en producción y no requieran un algoritmo específico. 

75 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **TextBlob** 



TextBlob es una especie de extensión de NLTK que permite acceder a muchas de las funciones de NLTK de manera simplificada a través de TextBlob, y TextBlob , y también incluye funciones de la biblioteca Pattern. Es una buena herramienta para usar en aplicaciones basadas en NPL productivas sin un requisito excesivo de rendimiento a la vez que se aprende a utilizar. En general, TextBlob se usa de forma generalizada y es excelente para proyectos más pequeños. 

#### **Textacy** 



Textacy usa SpaCy para su funcionalidad principal de NLP, pero maneja gran parte del trabajo antes y después del procesamiento. En un proyecto en el que el planteamiento sea usar SpaCy, también se podría llegar a utilizar Textacy para gestionar fácilmente muchos tipos de datos sin tener que escribir código de ayuda adicional. 

#### **PyTorch-PNL** 



PyTorch-NLP es una herramienta de código abierto relativamente reciente que rápidamente ha ganado una gran comunidad de seguidores. Es una gran herramienta para la creación rápida de prototipos. También se actualiza a menudo nutrida por nuevas investigaciones. En general, PyTorch está dirigido a investigadores, pero también se puede usar para prototipos y cargas de trabajo de producción inicial con los algoritmos más avanzados disponibles. 

76 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **2.2. Herramientas NODE** 

#### **Retext** 



Retext es parte del colectivo Unified. Una interfaz que permite que múltiples herramientas y complementos se integren y trabajen juntos de manera efectiva. Retext es una de las tres sintaxis utilizadas por la Unified. Los otros son Remark para markdown y Rehype para HTML. Retext no expone muchas de sus técnicas subyacentes, sino que utiliza complementos para lograr los resultados que podría estar buscando con NLP. Es fácil hacer cosas como revisar la ortografía, corregir la tipografía, detectar sentimientos o asegurarse de que el texto sea legible con complementos simples. En general, esta es una buena herramienta, para una amplia comunidad si no se desea comprender todo en el proceso subyacente de la obtención de resultados de NPL. 

#### **Compromise** 



Compromise no emplea algoritmos más avanzados o sistemas complejos de análisis. Sin embargo, si busca una herramienta de alto rendimiento que tenga una amplia gama de características Compromise puede ser un buen aliado. Su nombre se debe al compromiso de sus creadores hacia la funcionalidad y la precisión, esto garantiza que es una herramienta que se centra en un paquete pequeño, pero con una funcionalidad mucho más específica que se beneficia de que el usuario comprenda más el contexto que rodea el uso. 

#### **Natural** 

Natural incluye la mayoría de las funciones que se podrían esperar en una biblioteca general de NLP. Se centra en el entendimiento del idioma inglés, pero se han incorporado algunos otros idiomas y la comunidad está abierta a contribuciones adicionales continuas. Admite tokenización, derivación, clasificación, fonética, frecuencia de términos, frecuencia de documento inversa, WordNet, similitud de cadenas y algunas inflexiones. Puede ser más comparable a NLTK, ya que centra en incluir todo en un solo paquete, pero es más fácil de usar y no se centra tanto en la investigación. En general, esta es una biblioteca bastante completa que se encuentra en desarrollo activo y puede requerir un conocimiento adicional de las implementaciones subyacentes para que sea completamente efectiva. 

77 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **Nlp.js** 



Nlp.js se basa en varias otras bibliotecas de NLP, incluidas Franc y Brain.js. Proporciona una buena interfaz en muchos componentes de NLP, como clasificación, análisis de sentimientos, derivación, reconocimiento de entidades nombradas y generación de lenguaje natural. También es compatible con bastantes idiomas, lo que es útil si planea trabajar en algo que no sea inglés. En general, esta es una gran herramienta general, con una interfaz simplificada en varias otras grandes herramientas. 

### **2.3. Herramientas Java** 

#### **OpenNLP** 



OpenNLP está alojado en Apache Foundation, por lo que es fácil integrarlo en otros proyectos de Apache, como Apache Flink, Apache NiFi y Apache Spark. Es una herramienta general de NLP que cubre todos los componentes de procesamiento comunes de NLP y se puede usar desde la línea de comandos o dentro de una aplicación como una biblioteca. También tiene un amplio soporte para múltiples idiomas. En general, OpenNLP es una herramienta con mucho potencial y con muchas funciones, lista para cargas de trabajo de producción desarrolladas en Java. 

#### **StanfordPNL** 



Stanford CoreNLP es un conjunto de herramientas que proporciona NLP estadístico, NLP de aprendizaje profundo y funcionalidades de NLP basada en reglas. Se han creado muchos otros enlaces y traducciones de lenguaje de programación para que esta herramienta se pueda usar fuera de Java. Es una herramienta creada por una institución de investigación por lo que puede que no sea la más apropiada para las cargas de trabajo de producción. En general, esta es una gran herramienta para la investigación y la experimentación, pero puede incurrir en costes adicionales en un sistema de producción. También tiene implementación de Python que podría interesar y ligado a la herramienta existe incluso un curso de DM impartido por docentes de Stanford en Coursera. 

78 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **CogCompNLP** 



CogCompNLP fue desarrollado por la Universidad de Illinois. Tiene una biblioteca de Python con una funcionalidad similar a la de Stanford. Se puede usar para procesar texto, ya sea localmente o en sistemas remotos, lo que puede eliminar una enorme carga de dispositivos locales. Proporciona funciones de procesamiento como tokenización, etiquetado de parte del discurso, fragmentación, etiquetado de entidad nombrada, lematización, análisis de dependencia y circunscripción, y etiquetado de roles semánticos. En general, esta es una gran herramienta para la investigación y tiene muchos componentes a explorar. 

En conclusión, el empleo de PNL como vehículo de ejecución de AI y desarrollo de nuevas aplicaciones crea un vínculo que nos llevará de nuestro presente humano-máquina no integrado por completo a un futuro integrado hombre-máquina mucho mejor y mucho más útil. El acceso a herramientas y servicios de este tipo además es cada vez más sencillo o con un abanico de opciones más extenso (ya sea como servicio consumido en clouds públicas o de ejecución propia a través de herramientas de código abierto) 

Por otro lado la visión artificial es un campo de la inteligencia artificial (IA) que permite que las computadoras y los sistemas obtengan información significativa de imágenes digitales, videos y otras entradas visuales, y tomen medidas o hagan recomendaciones basadas en esa información. Si la IA permite que dispositivos de cómputo piensen, la visión artificial les permite ver, observar y comprender. 

La visión artificial funciona de manera muy similar a la visión humana, excepto que los humanos tienen una ventaja inicial. La vista humana tiene la ventaja de toda una vida de contexto para entrenar cómo diferenciar los objetos, qué tan lejos están, si se están moviendo y si hay algo mal en una imagen. En esta rama de la IA se entrena a las máquinas para realizar estas mismas funciones, pero haciéndolo en mucho menos tiempo con cámaras, datos y algoritmos en lugar de retinas, nervios ópticos y una corteza visual. Debido a que un sistema capacitado para inspeccionar productos u observar un activo de producción puede analizar miles de productos o procesos por minuto y detectar defectos o problemas imperceptibles, puede superar rápidamente las capacidades humanas. 

79 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

La visión artificial necesita muchos datos así como una ejecución y análisis de los mismos, una y otra vez, hasta que discierne distinciones y finalmente reconoce imágenes.  Se utilizan principalmente dos tecnologías esenciales para lograr esto: un tipo de aprendizaje automático llamado aprendizaje profundo (DL) y redes neuronales convolucionales (CNN). El aprendizaje automático (DL) utiliza modelos algorítmicos que permiten que un sistema aprenda de forma autónoma sobre el contexto de los datos visuales. Si se provee a un sistema con suficientes datos a través del modelo, este dispositivo se nutrirá de los datos y aprenderá a diferenciar una imagen de otra. Los algoritmos permiten que la máquina aprenda por sí misma, en lugar de que alguien la programe para reconocer una imagen. 

Una CNN ayuda a un modelo de ML o de DL, ya que divide las imágenes en píxeles a los que se asignan etiquetas. Utiliza las etiquetas para realizar circunvoluciones (una operación matemática en dos funciones para producir una tercera función) y hace predicciones sobre lo que está “viendo”. La red neuronal ejecuta circunvoluciones y verifica la precisión de sus predicciones en una serie de iteraciones hasta que las predicciones comienzan a hacerse realidad. 

Al igual que un ser humano que distingue una imagen a distancia, una CNN primero discierne bordes duros y formas simples, luego completa la información a medida que ejecuta iteraciones de sus predicciones. Se utiliza una CNN para comprender imágenes individuales. Una red neuronal recurrente (RNN) se usa de manera similar para aplicaciones de video. Para ayudar a las computadoras a comprender cómo se relacionan entre sí las imágenes en una serie de frames. Algunos ejemplos de tareas de visión por computadora establecidas: 

- La clasificación de imágenes; una aplicación / recurso de cómputo ingesta una imagen y puede clasificarla. Más precisamente, es capaz de predecir con precisión que una imagen dada pertenece a una clase determinada. Por ejemplo, una empresa de redes sociales podría querer usarlo para identificar y segregar automáticamente las imágenes no publicables cargadas por los usuarios. 

- La detección de objetos . Esta puede usar la clasificación de imágenes para identificar una determinada clase de imagen y luego detectar y percibir su apariencia en una imagen o video. Los ejemplos incluyen la detección de daños en una línea de ensamblaje o la identificación de maquinaria que requiere mantenimiento. 

- El seguimiento de objetos. Seguir /rastrear un objeto una vez que se detecta. Esta tarea a menudo se ejecuta con imágenes capturadas en secuencia o transmisiones de video en tiempo real. Los vehículos autónomos, por ejemplo, no solo necesitan clasificar y detectar objetos como peatones, otros automóviles e infraestructura vial, sino que también deben rastrearlos en movimiento para evitar colisiones y obedecer las leyes de tránsito. 

80 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- La recuperación de imágenes basada en el contenido utiliza también la visión artificial para navegar, buscar y recuperar imágenes de grandes almacenes de datos, en función del contenido de las imágenes en lugar de las etiquetas de metadatos asociadas a ellas. Esta tarea puede incorporar la anotación automática de imágenes que reemplaza el etiquetado manual de imágenes. Estas tareas se pueden utilizar por ejemplo para que sistemas de gestión de activos digitales puedan aumentar la precisión de la búsqueda y recuperación. 

Tanto el NPL como la visión artificial son recursos recurrentes a la hora de aplicar IA. En el siguiente apartado en el que se estudiarán los principales fabricantes y proveedores de cloud pública se mencionarán APIs concretas relacionadas con ambos campos. 

81 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

## **3. Proveedores Servicios Cloud y Aplicaciones dedicadas a la IA** 

_“El cloud impulsará implementaciones de AI a gran escala , más retorno de la inversión (ROI) y un mayor gasto en AI”. Fuente:_ _<u>https://n9.cl/referencia_deloitte</u>_ 

En el apartado anterior se ha hecho referencia genérica a diferentes proveedores de servicios cloud de forma general que ofrecen sus servicios a empresas de numerosas industrias. Sin embargo, los servicios específicos que cada uno de ellos ofrece en el entorno de la inteligencia artificial cuentan ciertos matices que en muchas ocasiones los diferencian. 

Como se ha podido concluir en el apartado anterior el uso de servicios y recursos cloud puede convertirse en un gran aliado de los negocios de las organizaciones aportándoles flexibilidad, agilidad, escalabilidad y la posibilidad de efectuar ahorros importantes. La combinación de estos beneficios con la IA crea el partnership ideal para, no solo rediseñar e impulsar la actividad empresarial. También va a suponer un mayor aprovechamiento de la información, creación de productos personalizados e intuitivos, así como un mayor acceso a ellos. A lo largo del apartado estudiaremos aplicaciones y servicios de IA ofrecidos por diferentes proveedores, con este término se englobarán diferentes tecnologías que conforman subcampos como el DL o el ML. 

El cloud, en sus diferentes formas de consumo, facilita democratizar los beneficios y capacidades que la IA aporta a todo tipo de industria o negocio. Es decir, el cloud pone a disposición de todo tipo de _player_ , servicios embebidos de IA. El cloud fomenta el uso de IA poniendo a disposición recursos que desde los primeros hitos de la IA eran limitados a consumidores capaces de afrontar los costes asociados. Desde el punto de vista del cómputo necesario para un rápido desarrollo o despliegue, los proveedores cloud en los que se centrará el apartado, liberan al usuario de invertir en capacidad de proceso, infraestructura, creación en instalaciones propias de datalakes autogestionados etc. 

En concreto una de las áreas que mayor beneficio obtiene de estos servicios es la gestión de la información. Como bien es sabido, la IA permite realizar una búsqueda, identificación, filtrado, tratamiento y análisis de datos óptimos. Esto junto a la ágil escalabilidad que los entornos cloud proporcionan, implica una combinación perfecta a la hora de generar valor a través de los datos. 

82 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Una de las áreas pioneras en el uso de IA en entornos cloud fue la relacionada con la experiencia de usuario y gestión de estrategias de venta a través de diferentes tipos de SaaS. También chatboots implican el uso de IA, y los conocidos asistentes virtuales como Siri o Alexa permiten personalizar mediante voz desde hace años el consumo de servicios como la realización directa de compras, elección de canciones. 

Los diferentes proveedores cloud que a continuación se han seleccionado cuentas con soluciones, herramientas y una oferta muy extendida para el uso de IA por parte de sus clientes de forma masiva. Esto, conjugado con diferentes tipos de software empresarial con IA integrada hacen que esta tendencia tecnológica cada vez sea utilizada y explotada por un número mayor de usuarios con diferentes usos. 

Siguiendo la referencia de diferentes estudios de Gartner, el mercado cloud está dominado por diferentes proveedores. En este apartado se estudiarán en concreto cinco de ellos, así como su offering de servicios de IA. 



### **3.1. Amazon** 

Amazon Web Services (AWS en adelante) ofrece una amplia selección de servicios de análisis que se adaptan a todas las necesidades de análisis de datos y permite a las organizaciones de todos los tamaños y los sectores reinventar su negocio a través de los datos. Desde el movimiento de datos entre los propios recursos de la empresa (e integración con otros fabricantes y proveedores de servicios similares), el almacenamiento de datos, creación y mantenimiento de data lakes, el análisis de big data, ML entre otros, AWS ofrece servicios especialmente diseñados que proporcionan una óptima relación entre rendimiento, escalabilidad y coste. Existen algunos aspectos a destacar en este proveedor en cuanto a la gestión de la información: 

#### • **Almacenamiento de datos escalar** 

El offering de Amazon está diseñado para albergar grandes volúmenes de datos y escalar de forma fácil y flexible. También permite automatizar numerosas tareas manuales. Los data lakes cuentan con alta disponibilidad respaldada por el almacenamiento de objetos Amazon Simple Storage Service (S3) que permite manejar su propia escalabilidad de forma transparente al usuario. 

83 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- **Acceso a los datos, seguridad y gobernanza unificados** 

AWS proporciona un conjunto integral de herramientas que no se limitan a la funcionalidad de seguridad estándar, como el cifrado y el control del acceso, sino que también ofrecen administración unificada de las políticas de seguridad y monitorización proactivas. Es decir, permite administrar y configurar de forma centralizada políticas de seguridad, gobernanza de datos /aplicaciones y auditorías para cumplir las normativas específicas de todos los sectores en diferentes zonas geográficas. 

- **Integración de machine learning** 

La compañía ofrece una gran integración de ML incorporada como parte de sus propios servicios de análisis. Por ejemplo, AWS cuenta con Amazon SageMaker, un servicio completamente administrado que proporciona las herramientas necesarias para completar cada paso del ciclo de vida del desarrollo de ML en un entorno integrado. Esto se alinea con su apuesta a la hora de ofertar servicios con lo que implementar modelos de ML de forma rápida. 

El ya comentado, y los servicios de IA de Amazon ofertados desde su plataforma AWS son previamente entrenados para dotar a los usuarios de su porfolio de servicios una inteligencia lista para su uso, para sus aplicaciones y flujos de trabajo. Los servicios de inteligencia artificial de AWS se integran con facilidad con todo tipo de aplicaciones para poder ser incorporados en la mejora de casos de uso comunes, como el ya mencionado de crear experiencias personalizadas o la modernización de servicios de atención al cliente recomendaciones personalizadas, modernizar su centro de atención al cliente. AWS utiliza principalmente la tecnología de aprendizaje profundo (DL) y ofrece servicios de ML. Uno de los principales motores del éxito de esta compañía es que el uso de las API que AWS oferta en el mercado no requiere de experiencia en aprendizaje automático previamente. 

### **3.1.1. Análisis de datos con AWS** 

Los servicios de análisis de datos de AWS se agrupan en 3 categorías en función del servicio prestado. 

**1. Almacenamiento de datos, análisis interactivo, procesamiento de big data, análisis operativo, paneles y visualizaciones.** 

   - a. Amazon Athena 

El servicio Amazon Athena es interactivo y facilita el análisis de datos en Amazon S3 mediante consultas SQL estándar. Athena no tiene servidor, de manera que no es necesario administrar infraestructura. Esto implica que solo se incurre en coste a la hora de realizar únicamente las consultas. 

84 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



No requiere trabajos de ETL para preparar los datos antes de analizarlos. Requiere de conocimientos en SQL para generar el esquema de consulta. 

- b. Amazon EMR 

Amazon EMR es una plataforma de _big data_ desplegada en cloud que permite ejecutar trabajos de procesamiento de datos distribuidos a gran escala, consultas SQL y desarrollo de aplicaciones de _machine learning_ (ML) con frames de análisis de código abierto como Apache Spark, Apache Hive y Presto. 



Fuente: <u>https://aws.amazon.com/es/emr/?c=a&sec=srv</u> 

Esta herramienta puede ser utilizada, entre otros casos de uso, para el procesamiento de flujos de datos en tiempo real mediante el análisis del origen de los datos recogidos en streaming en tiempo real. Tras ello, la herramienta es capaz de crear canalizaciones de datos en streaming con larga duración, altamente disponibles y tolerantes a errores. 

85 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### c. Amazon Redshift 

Esta herramienta utiliza SQL para analizar datos estructurados procedentes de diferentes tipos de almacenamientos de datos, bases de datos operativas y data lakes. Cuenta con hardware performante y ofrece servicios de ML diseñados por AWS para ofrecer un alto rendimiento. El gran volumen de datos generados por IoT (al final de este apartado se hará una leve incursión en el concepto de IoT), dispositivos inteligentes, aplicaciones en la nube y redes sociales crece desde los últimos 5 años exponencialmente.  Esto crea la necesidad de un análisis rápido y rentable del análisis de dicha información. El enfoque que AWS mediante Amazon Redshift plantea es el de conectar datos procedentes de diversas fuentes en un data lake; Amazon Simple Storage Service (Amazon S3). Amazon Redshift extiende de manera eficiente sus consultas a este datalake de Amazon S3, haciendo muy sencillo obtener valor de él. Se convierte en una pieza fundamental para muchos desarrollos de ML porque ofrece a tiempo real la transmisión de datos necesaria para obtener información inmediata, lo que facilita la extracción del valor de todos los datos gestionados. Amazon Redshift ML facilita por ende el trabajo de los analistas y científicos de datos. 

Finalmente, el uso de esta herramienta permite dar solución a diferentes casos de uso como experiencias web personalizadas, previsión de la demanda, optimización de la oferta/demanda, decisiones, o combinar datos históricos de series de tiempo con variables tales como producto, características, precios y días festivos. 



Fuente: <u>https://aws.amazon.com/es/redshift/?c=a&sec=srv</u> 

Recomendado este vídeo para mayor comprensión: <u>https://youtu.be/lWwFJV_9PoE</u> 

86 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### d. Amazon Kinesis 

Este servicio ayuda a la recopilación, procesamiento y análisis de datos de streaming en tiempo real para obtener datos de manera oportuna y utilizar e incorporar rápidamente información nueva. Además, permite procesar y analizar datos a medida que se reciben y responder instantáneamente en vez de tener que esperar a que los datos se recopilen antes de que el procesamiento pueda comenzar. Es decir, tiene plena integración con procesos de IA para la mejora continua del producto. 



- e. Amazon OpenSearch Service 

Permite realizar fácilmente análisis interactivo de registros, monitoreo de aplicaciones en tiempo real, búsqueda de sitios web entre otras funcionalidades. 

- f. Amazon QuickSight 

Esta herramienta impulsada por machine learning ofrece a los usuarios de todo tipo de organización paneles interactivos, así como la posibilidad de realizar búsquedas automáticas de patrones y valores atípicos dentro de la organización. AWS QuickSight gestiona millones de visualizaciones semanales del panel para clientes como NFL, Expedia, Volvo, Thomson Reuters, Best Western o Comcast, lo que permite a sus usuarios finales tomar mejores decisiones controladas. Además, su integración de ML permite a estas y muchas otras compañías obtener de forma más rápida información interna de la empresa. Desde la detección de anomalías para analizar de forma continua todos sus datos en busca de ataques/anomalías y variaciones. La previsión de métricas comerciales y realización de análisis hipotéticos interactivos con un click. Y narrativas automáticas que se pueden personalizar y combinar en paneles para crear un contexto más concreto y personalizado para los usuarios. 

87 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



Fuente: <u>https://aws.amazon.com/es/quicksight/</u> 



Visualización recomendada: https://youtu.be/2V1bHRLRG-w 

- g. Amazon AWS Glue DataBrew 

Esta nueva herramienta de AWS es un recurso visual de preparación de datos que facilita a los analistas y científicos de datos limpiar y filtrar los datos para prepararlos para el análisis y el aprendizaje automático. Se pueden seleccionar más de 250 transformaciones preconstruidas para automatizar las tareas de preparación de datos sin necesidad de programar ni conocer ningún código. Permite automatizar el filtrado de anomalías, realizar conversión de datos a formatos estándar y aplicar correcciones de valores no válidos entre otras tareas. Una vez los datos están listos pueden ser usados inmediatamente para proyectos de análisis y aprendizaje automático. Interfaz de usuario del científico de datos: 

88 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



- 1- Estudio del perfil de los datos. 



2- Filtrado y normalización de los datos. 

89 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



#### 3- Mapeado de los datos 



4- Automatización del proceso 

90 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **2. Movimiento de datos en tiempo real.** 

#### **AWS Glue** 

Preparación y carga de datos genéricos. 

#### **Amazon Managed Streaming for Apache Kafka (MSK)** 

Servicio para Apache Kafka completamente administrado, de alta disponibilidad y seguro. 

#### **Amazon Kinesis Data Firehose** 

Permite preparar cargar secuencias de datos en tiempo real en almacenes de datos y herramientas de análisis. 

#### **Amazon Kinesis Data Streams** 

Recopilación de datos de streaming para realizar análisis en tiempo real y escalar de forma ágil. 

#### **Amazon Kinesis Video Streams** 

Garantiza la obtención, proceso y almacenaje de flujos de videos y la realización de su análisis y ML. 

#### **AWS Database Migration Service** 

Esta tool permite realizar la réplica datos desde sistemas SQL y NoSQL a diferentes sistemas de almacenamiento de datos y sistemas de análisis. 

#### **3. Lago de datos: almacenamiento de objetos, copia de seguridad y archivo, catálogo de datos y datos de terceros** 

Aunque existen otros servicios en esta agrupación AWS Backup o AWS DataExchange, centraremos este apartado en AWS S3. Entre sus casos de uso se encuentra la ejecución de aplicaciones nativas en cloud. Esto liga directamente con los requisitos y tendencias que se han ido mencionando a lo largo 



de apartados anteriores en relación con el uso de IA, implementación en contenedores y despliegue en cloud. Amazon S3 permite entre otras cosas crear alojar / almacenar datos de aplicaciones móviles web-based, rápidas y potentes, nativas en cloud que se escalan automáticamente con una configuración de alta disponibilidad. 

91 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **4. Servicios de plataforma, frameworks e interfaces** 

En la oferta de Amazon, encontramos entornos preconfigurados para crear rápidamente aplicaciones de DL. Las AMI de aprendizaje profundo de AWS ofrecen a los investigadores y profesionales del DL la infraestructura y las herramientas necesarias para agilizar las tareas a ejecutar mediante recursos escalares en cloud. Estas herramientas permiten un despliegue rápido de instancias P3 de Amazon EC2 con marcos de aprendizaje profundo conocidos e instalados con anterioridad, como TensorFlow, PyTorch, Apache MXNet, Chainer, Gluon y Keras, para entrenar modelos de inteligencia artificial personalizados y sofisticados, probar algoritmos nuevos o aprender nuevas técnicas y habilidades. 



Fuente: <u>https://aws.amazon.com/es/machine-learning/amis/?c=a&sec=srv</u> 

Por otro lado Amazon SageMaker permite crear e implementar modelos de machine learning (ML) para cualquier caso de uso con infraestructura, herramientas y flujos de trabajo completamente administrados y gestionados por AWS. Esto genera beneficios en relación con la IA en dos sentidos: 

#### **Aceleración de la implementación del ML:** 

Reducción de los tiempos de formación de horas a minutos debido a la infraestructura utilizada. Esto genera un aumento en la productividad de los equipos que utilizan las herramientas. 

#### **Optimización del ciclo de vida del ML:** 

Automatizar, así como estandarizar las prácticas de MLOps en toda organización a la hora de crear, formar, implementar y administrar modelos escalares, deriva en posteriores ventajas para las compañías. 

92 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **3.1.2. Servicios de IA con AWS** 

Por otro lado, AWS permite acceder a una serie de recursos para realizar predicciones precisas, obtener información valiosa y más detallada de los datos provistos por las empresas. AWS ML se conforma de una serie de herramientas específicas para el apoyo y agilización en cada etapa del proceso de adopción de ML. Estos servicios de inteligencia artificial (IA) y ML, infraestructura y recursos de implementación son previamente entrenados y permiten su uso directo en la creación y uso de aplicaciones y su uso en los diferentes flujos de trabajo. Todos estos servicios de IA se engloban en diferentes categorías atendiendo al propósito de negocio o desarrollo; visión artificial, análisis y extracción de datos automatizados, explotación de métricas empresariales, mejora de la experiencia de usuario, desarrollo de código y DevOps, lenguaje e IA, infraestructura y _frames_ y educación. 

Aunque más adelante se dedica un Módulo completo a materializar en casos de uso todo lo estudiado en este y otros módulos del máster, es recomendable ejemplificar algunos de los escenarios más comunes en los que el offering de AWS descrito encaja. 

#### **Análisis preciso de imágenes** 

Esto abarca el diseño y desarrollo de múltiples modelos de visión artificial para una amplia gama de casos de uso. Ejemplos claros y recurrentes son la detección de objetos, el diagnóstico médico y la conducción autónoma. Si pensamos en clientes de sanidad y en el ya mencionado AWS SageMaker, el acceso a recursos de clasificación de imágenes permitirá por ejemplo mejorar el diagnóstico de los pacientes mediante la reducción de la subjetividad de dicho resultado y la reducción de la carga de trabajo de los médicos. 

#### **Automatización en el procesamiento de texto** 

La creación de modelos de ML para procesar y analizar automáticamente los datos de documentos manuscritos y electrónicos está en auge. Transcribirlos permite llevar a cabo un análisis más rápido, preciso y en muchas ocasiones rentable. AWS ofrece algoritmos de ML, como BlazingText y Linear Learner que han sido pensados y diseñados para optimizar la clasificar textos, el procesamiento del lenguaje natural (PLN /NPL en adelante) y el reconocimiento óptico de caracteres (OCR/ OCR en adelante). Es importante además conocer que AWS y sus herramientas objeto para el desarrollo de estas actividades se integran con Hugging Face, una famosa empresa que ofrece tecnologías de PNL/NLP de código abierto. 

93 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **Detección de anomalías en métricas empresariales** 

Realizar un mantenimiento de las aplicaciones predictivo y poder llevar a cabo una temprana detección de fraude es un objetivo transversal en las empresas. AWS facilita la detección de anomalías en transacciones sospechosas antes de que se produzcan y de esta manera poder alertar a sus clientes a tiempo. AWS SageMaker incluye de ML como Random Cut Forest y XGBoost para la rápida creación y ejecución modelos de detección de fraude. 

#### **Recomendaciones personalizadas al usuario** 

La búsqueda de la satisfacción de los clientes es prioridad transversal en todas las empresas e industrias. AWS proporciona algoritmos de ML integrados como por ejemplo máquinas de factorización para de esta manera dar acceso a la creación de motores de recomendación. Otras herramientas como AWS SageMaker Autopilot permite generar automáticamente modelos de personalización e implementarlo con unos pocos pasos para el desarrollador de la aplicación. 

En definitiva, AWS ofrece apoyo en cada etapa del proceso de adopción del ML a través del conjunto más completo de servicios de inteligencia artificial (IA) y ML, infraestructura y recursos de implementación. 



Fuente: <u>https://aws.amazon.com/es/machine-learning/?nc2=h_ql_sol_use_ml</u> 

### **3.2. Google Cloud** 

De forma muy similar a lo que nos encontrábamos en AWS, Google pone a disposición del mercado modelos ya gestionados. Dichos modelos pueden ser invocados vía IP a través de APIs directamente. Esto está principalmente enfocado a los consumidores o usuarios sin conocimientos de ML. La propuesta de servicios de IA de Google también incluye un conjunto de herramientas para entrenar modelos desde el inicio del proceso para usuarios con conocimientos más avanzados. 

94 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Es decir, Google desde su cloud opta por ofertar dos tipos de modelos (o Building Blocks, término que acuña la propia compañía) disponibles para hacer uso del ML:  las APIs predefinidas por Google y la posibilidad de crear modelos más customizados mediante una serie de herramientas que se mencionan a continuación. 

Google Cloud paquetizadas con las que los usuarios acceden a la capacidad, entre otras, de por ejemplo transcribir documentos con datos en múltiples formatos y en distintos lenguajes. El objetivo de este servicio en concreto es inspeccionar elementos que existan en un documento y sirvan de fuente para las aplicaciones a desarrollar. También dentro del portfolio de soluciones paquetizadas existen herramientas para la automatización de las llamadas desde los Contact Centers mediante agentes virtuales que simulan el trabajo de agentes reales. 



Fuente: <u>https://cloud.google.com/solutions/ai</u> 

#### ACTIVIDAD: 

Una de las principales tendencias de la que se benefician muchas empresas hoy en día, es de la recopilación de información de sus clientes y de la posibilidad que esto brinda para crear experiencias transformadoras; Chatbots, Virtual Agents, Agent Assist, Agent Augment son recursos que utilizan IA conversacional para generar de manera eficiente dichas experiencias. La capacidad de comprensión y habla de estos agentes son similares a las humanas permiten su aplicación en todas las industrias y a través de múltiples canales de comunicación.  Desde un ya mencionado Contact Center, a las propias aplicaciones e incluso productos de IoT. En esta actividad podremos profundizar en esta temática además de ligarla a Google con un ejemplo práctico y real de cómo Dialogflow Enterprise Edition y el programa de socios de IA de Cloud Contact Center impulsaron la creación de experiencias de conversación fluídas y de sonido natural. Tras la visualización del contenido se podrá comprender más fácilmente cómo Google integra la IA sin necesidad de expertos en ML. 

95 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



Fuente: <u>https://cloud.google.com/solutions/contact-center</u> 

ACTIVIDAD PRÁCTICA 

1. Acceda al link de la actividad: <u>https://n9.cl/practicagc_mia</u> 

2. Visualice contenido 

3. Analice las herramientas de Google Cloud empleadas y describa los beneficios para el negocio que supuso el uso de la herramienta comentada en el vídeo. 

4. Entrega de documentación en un máximo de 50 líneas de conclusión. 



Tras haber realizado un primer acercamiento a algunas de las herramientas de Google, es importante conocer la agrupación de servicios que este proveedor pone a disposición. 

### **3.2.1. Desarrollo con IA** 

#### **Auto ML & Vertex AI** 

AutoML permite a los desarrolladores con experiencia no avanzada entrenar modelos y obtener resultados de alta calidad adaptados a las necesidades de cada caso de uso. Cuenta con herramientas que abarcan todos los tipos de despliegues más demandados. 

96 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

##### **Visión** 

**Vertex AI Visión** Plataforma unificada para desarrollar, **AutoML Image** desplegar y escalar modelos de inteligencia artificial. Extrae información valiosa de los datos de detección • Preparación y almacenamiento de de objetos y clasificación conjuntos de datos de imágenes, en la nube o en el perímetro • Acceso a las herramientas de aprendizaje automático que usa Google • Uso de las APIs REST y RPC • Posibilidad de probar y desarrollar modelos más rápidamente • Detección de objetos, dónde están y cuántos • Gestión de modelos con total confianza son 

- Gestión de modelos con total confianza 

- Clasificación de imágenes mediante etiquetas personalizadas 

- Despliegue de modelos de aprendizaje automático en el perímetro 

##### **AutoML Video** 

Descubre contenido valioso y ofrece experiencias de vídeo atractivas. 

- Anotación de vídeos mediante etiquetas personalizadas 

- Análisis de vídeos en streaming • Detección de cambios de plano 

- Detección y seguimiento de objetos 

##### **Lenguaje** 

##### **Datos estructurados** 

**AutoML Text AutoML AutoML Tabular Translation** Analiza la estructura Crea y despliega automáticamente modelos de y el significado del Detecta y traduce aprendizaje automático de última generación texto mediante textos de manera sobre datos estructurados. el aprendizaje dinámica automático • Capaz de gestionar una amplia variedad de • APIs REST y tipos primitivos de datos tabulares • API REST integrada gRPC integradas 

   - Modelos fáciles de crear 

- Extracción • Compatible de entidades con más de 50 personalizada idiomas • Análisis de opinión • Traducción personalizado con modelos personalizados 

   - Modelos fáciles de desplegar y escalar 

- Compatibilidad con conjuntos de datos de gran tamaño 

Fuente: <u>https://cloud.google.com/automl</u> 

97 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



En concreto Vertex AI ofrece todas las herramientas necesarias para el desarrollo de ML una sola plataforma de IA. Cuenta con una interfaz y una API unificadas para todo el flujo de trabajo de ML. Vertex AI se nutre de AutoML pero también permite realizar entrenamientos de código personalizados y todos los modelos creados por los usuarios se almacenan en un único repositorio central. Algunas de las funcionalidades destacadas. 

#### **Cuenta con APIs previamente entrenadas para ámbitos de visión, vídeo, lenguaje natural entre otras.** 

Esto ofrece una integración fácil de diferentes modelos de ML de visión, vídeo, traducción y de lenguaje natural en una misma aplicación. 

#### **Integración total de datos e IA** 

Vertex AI Workbench (una de las herramientas incluidas en el producto) se integra de forma nativa con BigQuery, Dataproc y Spark. Esto permite lanzar consultas para crear modelos y ejecutarlos, basándote en datos e información proveniente de estos entornos. Es decir, Google permite de esta manera crear y ejecutar modelos de ML con consultas SQL estándar en herramientas y hojas de cálculo de inteligencia empresarial ya creadas. 

#### **Compatibilidad con todos los frameworks de código abierto** 

Existen frameworks de código abierto muy utilizados como TensorFlow, PyTorch y scikitAprende. El offering de Google admite estos frameworks de ML y así como la integración con otros mediante contenedores. 

Para una mayor comprensión de los recursos con los que Google pone a su disposición con AutoML y Vertex AI existe la posibilidad de crear un proyecto tras la realización de un registro con una cuenta de Google. Para ampliación de conocimiento: https://n9.cl/ <u>practicagcautoml_mia</u> 



Visión inicial para experimentar con Vertex AI 

98 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **3.2.2. IA conversacional** 

##### **Speech to Text** 

Esta herramienta permite convertir voz en texto de forma precisa con una API basada en tecnologías propias de IA de Google. Speech-to-Text aplica los algoritmos de la red neuronal de ML de Google para reconocer la voz automáticamente y convertirla en texto. 

A continuación, se puede comprobar/probar cómo funciona mediante la selección del idioma hablado: <u>https://n9.cl/practicagcs2t_mia</u> 



Esta herramienta ofrece además sugerencias para personalizar las funciones de reconocimiento de voz y transcribir términos de un contexto específico / palabras poco frecuentes. 

##### **Text to Speech** 

Permite convertir texto en voz con apariencia natural a través de una API basada en tecnologías de IA de Google también, como en el caso anterior 





Entre otras funcionalidades, Google T2S permite realizar ajustes de voz, para una personalización del tono de la voz seleccionada/final. También permite modificar la velocidad de elocución mayor o menor velocidad. 

Para testear esta herramienta: <u>https://n9.cl/practicagct2s_mia</u> 





99 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

##### **Contact Center AI** 

Google Contact Center AI permite como ya se ha comentado anteriormente interactuar de forma natural desde Call Centers, por ejemplo. Esto supone una revolución a la hora de utilizar tecnología conversacional basada en IA. 



Gracias a Dialogflow CX, que forma parte de los servicios que incluye Contact Center AI, los usuarios del servicio pueden crear en cuestión de minutos agentes virtuales avanzados que son capaces de cambiar de tema de conversación de manera fluida, abordar preguntas adicionales al tema de la conversación y funcionar de forma ininterrumpida para minimizar las intervenciones de los agentes humanos, especialmente fuera de horario. 

Cuenta con funciones de arrastrar y soltar iconos para crear flujos de forma intuitiva. 

Además, ContactCenter AI cuenta con CCAI Insights que usa el PLN/NPL para identificar el motivo de las llamadas y la opinión que tienen los clientes sobre cómo se ha gestionado la consulta. Eso ayuda a los administradores de los centros de contacto a obtener datos valiosos de las interacciones con los clientes para, así, mejorar los resultados de sus llamadas. 



100 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **3.2.3. IA para documentos** 

##### **Natural Language AI** 

Permite la extracción de información valiosa de textos sin orden aparente / sin estructurar con ML de Google. Esto permite: 

- Obtener análisis con alto valor de textos mediante un sistema de ML no solo extrae información, si no que la analiza y almacena en formato texto también. 

- Permite realizar el entrenamiento de modelos personalizados de ML mediante el ya estudiado AutoML sin tener que escribir o desarrollar líneas de código. 

- Emplea la comprensión del lenguaje natural (CNL/NLC) mediante la API de Natural Language. 



##### **Translation AI** 

Permite que el contenido y las aplicaciones creadas sean multilingües gracias su traducción automática, rápida y dinámica. 

Permite la internacionalización del producto/aplicación resultante y además proporciona una experiencia de usuario fluida gracias a la traducción en tiempo real que ofrece. 

##### **Vision AI** 

Permite la extracción de información de imágenes almacenadas en cloud (S3), en el perímetro con AutoML Vision ya comentado, o usa modelos preentrenados de la API de Vision para detectar emociones, interpretar texto entre otras funciones. Dos productos de visión artificial son los que completan Vision AI; AutoML Vision (anteriormente comentado) y API de Vision. Este segundo ofrece modelos de ML preentrenados y muy potentes a través de las APIs REST y RPC. Además asigna etiquetas a imágenes y permite clasificarlas rápidamente en diferentes categorías predefinidas. Detecta objetos y caras, lee texto tanto manuscrito como impreso. 

Accede al siguiente link para testear Vision AI: <u>https://n9.cl/practicagcvai_mia</u> 



101 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

##### **Document AI** 

Esta herramienta permite automatizar la captura de datos en grandes volúmenes para reducir los costes de procesamiento de documentos lo que deriva en: 

   - Llevar a cabo una decisiones más rápida, precisa y acertada. 

   - La automatización y validación de los datos para que los flujos de trabajo sean más eficientes. 

   - Aprovechamiento y búsqueda de Insight en los datos de los documentos para obtener información nueva y valiosa sobre tus productos y satisfacer las expectativas de los clientes. 

- Pruebe esta funcionalidad para ver la potencia de la tool: <u>https://n9.cl/es/s/practicagcdoc_ mia</u> 



### **3.2.4. IA para sectores empresariales** 

#### **Media Translation** 

La API Media Translation añade traducciones de voz en tiempo real directamente al contenido del cliente así como a sus aplicaciones a partir de datos de audio. Esta API hace uso de las tecnologías de ML de Google para garantía de precisión y simplicidad en la integración, a la vez ofrecer un conjunto variado de funciones para afinar aún más los resultados de traducción. Estas traducciones en streaming de baja latencia son rápidamente escalables. 

102 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



Fuente: <u>https://cloud.google.com/media-translation</u> 

#### **Recommendations AI** 

Recommendations AI aprovecha la experiencia previa sobre anteriores transacciones con cliente y recursos de ML para ofrecer recomendaciones personalizadas según sus gustos y preferencias. Acceda al vídeo que se muestra a continuación para ver un CASO DE ÉXITO real de la herramienta. 



<u>https://youtu.be/PyjC0wRRtBg</u> 

Existen otras herramientas de uso documental y empresarial como Lending de Document AI que permite la automatización en el procesamiento de documentos hipotecarios, para mejorar la experiencia de los usuarios a la hora de solicitar un préstamo para su vivienda. O Procurement de Document AI que permite la conversión de documentos sin estructurar (como facturas y recibos) en datos estructurados para capturar datos de aprovisionamiento de forma automática y rápidamente escalable. 

En definitiva, Google Cloud nos ofrece una amplia gama de servicios para explotar la IA y elementos de cómputo para entrenar el ML de manera eficaz y rentable para el negocio. Es importante enfatizar en la facilidad a la hora de iniciarse en sus herramientas ya que todos los servicios están administrados por Google. 

103 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **3.3. IBM** 

Antes de proceder a estudiar los servicios de IBM Cloud para conocerlos, es interesante conocer historia de la empresa tecnológica con más antigüedad del mundo y cómo la transformación digital década a década la llevaría a proporcionar estos servicios en infraestructura Cloud. 

La actual computación en la nube se remonta a la década de 1950, cuando los sistemas mainframe o más conocidos Z de IBM (https://www.ibm.com/topics/mainframe) se pusieron a disposición de las universidades y grandes corporaciones empresariales para el consumo de recursos deslocalizados de sus instalaciones. La infraestructura de hardware del mainframe se instaló en lo que se llamó una “sala de servidores”. De forma paralela múltiples usuarios podían acceder al mainframe a través de terminales sin ningún tipo de inteligencia computacional, estaciones con la única función de facilitar el acceso a los mainframes y a los recursos que estas máquina daban a sus usuarios. 



Debido al alto coste de comprar y mantener estos grandes ordenadores, este modelo de oferta de consumo se convirtió en una práctica que permitía que varios usuarios compartieran el acceso a la misma capa de almacenamiento de datos y la potencia de la CPU desde cualquier punto remoto. Al permitir el acceso compartido al mainframe, las organizaciones conseguían un mejor retorno de su inversión a la hora de consumir servicios de tecnología de esta manera. 

Veinte años más tarde, en la década de 1970, IBM lanza al mercado un sistema operativo llamado VM que permitía a los administradores de sus sistemas mainframe tener múltiples sistemas virtuales, o máquinas virtuales como actualmente se conocen en un solo nodo físico. El sistema operativo VM llevó la aplicación de acceso compartido de un mainframe de la década de 1950 al siguiente nivel, al permitir que varios entornos informáticos distintos vivieran en el mismo entorno físico. 

104 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



Mainframe virtualization: VM/370 virtual machines 

Es interesante observar cómo ambos hitos están completamente alineados a la historia del Cloud Computing estudiada al inicio del módulo ya que la mayoría de las funciones básicas de cualquier software de virtualización actual se remontan a este antiguo sistema operativo de VM. Cada máquina virtual ejecutaba sistemas operativos personalizados o sistemas operativos invitados que tenían su propia memoria, CPU y discos duros, junto con CD-ROM, teclados y redes, a pesar de que esos recursos se compartían. Desde este momento, la virtualización se convirtió en un motor tecnológico y en un gran catalizador para algunas de las mayores evoluciones en las comunicaciones y la informática. 



105 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Es en la década de 1990 cuando las empresas de telecomunicaciones que históricamente solo ofrecían conexiones de datos punto a punto dedicadas, comenzaron a ofrecer conexiones de red privada virtualizadas. Todo ello con la misma calidad de servicio que los servicios dedicados, pero con un coste reducido. En lugar de construir una infraestructura física para permitir que más usuarios tuvieran sus propias conexiones, las empresas de telecomunicaciones proporcionaron a los usuarios acceso compartido a la misma infraestructura física. Este cambio permitió a las empresas de telecomunicaciones cambiar y balancear el tráfico según fuera necesario, lo que generó un mejor equilibrio de la red y un mayor control sobre el uso del ancho de banda. 

Mientras tanto, la virtualización de sistemas basados en PC comenzó a despuntar. A medida que Internet se volvió más accesible para empresas y usuarios particulares, la virtualización en línea fue aumentando. A medida que el consumo de recursos en línea aumentaba, los costes de consumo de recursos IT disminuían. 



Fuente: <u>https://www.ibm.com/cloud/blog</u> 

Los servidores se virtualizaron en entornos físicos de recursos compartidos, también los servidores privados virtuales y los servidores dedicados virtuales que utilizaban los mismos tipos de funcionalidad proporcionados por VM OS en la década de 1950. ¿Qué impacto tuvo esto en la práctica? Imaginando que una empresa requería de 10 sistemas físicos para ejecutar sus recursos IT y aplicaciones. Con la virtualización de los recursos se abría el abanico de posibilidades de consumir esos 10 sistemas a través de diferentes sistemas operativos utilizando únicamente dos nodos físicos. Obviamente, este tipo de entorno ahorraba costes de infraestructura y minimizaba la cantidad de hardware real que una empresa necesitaba para satisfacer las necesidades IT. 

106 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Al instalar y configurar una pieza de software llamada hipervisor (https://www.redhat. <u>com/es/topics/virtualization/what-is-a-hypervisor), en múltiples nodos físicos, un único</u> sistema sería capaz de presentar todos los recursos del entorno como si esos recursos estuvieran en un solo nodo físico. Para visualizar ese entorno, los tecnólogos usaron términos como utility computing y cloud computing. En estos entornos de computación en la nube, agregar recursos a la nube fue fácil. 



Fuente: <u>https://superuser.com/</u> 

A medida que las tecnologías y los hipervisores mejoraron al compartir y entregar recursos de manera fiable, muchas empresas decidieron unirse y poner los beneficios de la nube a disposición de los usuarios que no tenían una gran cantidad de servidores físicos disponibles para crear su propia infraestructura de computación en la nube. Esos usuarios podían solicitar instancias de computación en la nube (también conocidas como servidores en la nube) solicitando los recursos que necesitaban únicamente. Debido a que los servidores ya estaban en línea, el proceso de encender/ proveer una nueva instancia o servidor era casi instantáneo. Se simplifica por tanto también la gestión de la infraestructura con un único proveedor de este servicio que únicamente ordenaba o cancelaba instancias (ya que es manejada por el software de la nube). 

La mayoría de las empresas hoy en día operan con la definición antes mencionada de la nube, pero IBM Cloud en lugar de instalar software en un grupo de máquinas para permitir que los usuarios tomaran parte de los recursos de la infraestructura compartida, creó una plataforma que automatizaba los aspectos manuales de poner un servidor en línea sin un hipervisor en el servidor. Esta plataforma adquirió el nombre de “IMS”. Lo que los hipervisores y la virtualización hacían por un grupo de servidores, IMS era capaz de hacerlo por un centro de proceso de datos completo. Como resultado, los usuarios de IBM eran capaces de solicitar un servidor bare metal con los recursos necesarios para su propósito de negocio y ese servidor se le entregaría en cuestión de horas. Sin una capa de hipervisor entre su sistema operativo y el hardware completo, los servidores funcionan mejor. 

107 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Debido a esta automatización de casi todos los centros de proceso datos, IBM fue pionero en activar balanceadores de carga, firewalls y dispositivos de almacenamiento bajo demanda, también apagarlos cuando los usuarios terminaban de utilizar los recursos. 



IBM Cloud lideró desde hace años el impulso hacia una adopción más amplia de servicios innovadores en la nube, desde los años 50 con los sistemas mainframe a la actualidad. Ofreciendo desde IBM Cloud una nube pública abierta y segura para empresas. Las arquitecturas abiertas, basadas en Kubernetes y contenedores, hoy en día están impulsando la próxima ola de innovación empresarial basada en la nube y es por eso por lo que IBM cada día incorpora mejoras en su nube pública con una base de software de código abierto, más seguridad e infraestructura de nivel empresarial. 

Tras esta breve introducción de la historia de IBM ligada a la evolución tecnológica principalmente a lo largo del siglo XX, realizaremos el mismo análisis del catálogo que actualmente IBM ofrece desde su plataforma de cloud: <u>https://cloud.ibm.com/catalog</u> 



Antes de proceder a profundizar en el catálogo de aplicaciones de Inteligencia Artificial que encontramos en la plataforma de IBM se analizará el inicio de la IA en esta compañía ligado a IBM Watson, motor de muchas de las aplicaciones que a continuación se estudiarán. 

108 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **3.3.1. ¿Qué es IBM Watson?** 



Watson es una computadora que ejecuta un software llamado Deep QA, desarrollado por IBM Research. En un evento histórico, el ordenador Watson de IBM compitió, y ganó, en Jeopardy! (programa de la televisión americana que consistía en que los participantes a través de una respuesta enunciada por el presentador debían adivinar la pregunta a esa contestación) contra los dos mayores campeones en aquel momento del programa. 

Si bien el desafío inminente del equipo de Research que impulsaba el proyecto era ganar en Jeopardy!, el objetivo más amplio de Watson era crear una nueva generación de tecnología que pudiera encontrar respuestas en datos no estructurados de manera más efectiva que la tecnología de búsqueda estándar. 

David Ferrucci, pasó 15 años trabajando en IBM Research en problemas de lenguaje natural y encontrando respuestas en medio de información no estructurada afirmó que _“El objetivo de Watson era construir una computadora que pueda ser más efectiva para comprender e interactuar en lenguaje natural, pero no necesariamente de la misma manera que lo hacen los humanos”._ 



Fuente: <u>https://www.youtube.com/watch?v=YgYSv2KSyWg</u> 

Actualmente Watson se ejecuta en un clúster de computadoras Power que ejecutan software y almacenamiento DeepQA. Trabaja y mejora con su contenido, el equivalente a aproximadamente un millón de libros de información. Durante un período de años, Watson recibió numerosa información, incluidos textos de fuentes comerciales, como World Book Encyclopedia, y fuentes que le permitieron la copia abierta de su contenido, como Wikipedia y libros del Proyecto Gutenberg. 

Es importante puntualizar que la tecnología de Watson fue un avance sustancial con respecto a IBM Deep Blue y máquinas anteriores porque contó con un software que podía procesar y razonar sobre el lenguaje natural, y luego aprender del suministro masivo de información vertida en él. 

109 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **3.3.2. Aplicaciones de IA / Machine Learning de IBM** 

#### • **Watson Assistant** 

Watson Assistant permite crear interfaces de conversación en cualquier aplicación, dispositivo o canal. 

El objetivo de uso de este servicio es agregar una interfaz de lenguaje natural a todo tipo de aplicación para automatizar las interacciones con los usuarios finales. Las aplicaciones actuales, especialmente aquellas orientadas a fines comerciales incluyen agentes virtuales y chatbots que pueden comunicarse e integrarse a través de cualquier canal o dispositivo. Mediante la configuración del servicio Watson Conversation se pueden crear rápidamente flujos de conversación naturales entre usuarios y aplicaciones para crear soluciones rentables , escalables y de fácil configuración y uso. 





#### **• Watson Studio** 

Watson Studio aglutina funcionalidades de aprendizaje automático y aprendizaje profundo para acelerar la aplicación de IA en cualquier negocio. Watson Studio proporciona un conjunto de herramientas y un entorno colaborativo para científicos de datos, desarrolladores y expertos del análisis de información con fines analíticos. 



110 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Se nutre de código abierto (RStudio, Jupyter Notebooks) y de servicios de Watson, proporcionando así un modelado flexible. Se puede seleccionar desarrollar en Python, R o Scala y permite descargar y configurar entornos de análisis rápidamente. 

Proporciona un servicio bajo demanda de recursos con gran escalabilidad que permite administrar datos, activos analíticos y proyectos en un entorno de nube con una alta seguridad. 

La compartición de archivos y desarrollos es posible, además de que la herramienta facilita el acceso a una comunidad de científicos de datos, desarrolladores y expertos en dominios de todas las industrias, funciones y tipos de organizaciones. 



Fuente: <u>https://cloud.ibm.com</u> 

- **Communication Monitoring** 

Cognitive View realiza la supervisión de diferentes canales de comunicación para automatizar la calidad y la experiencia de cualquier cliente. También proporciona las herramientas necesarias para personalizar en torno al cliente, la comunicación empresarial : 



111 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

   - Análisis de voz y texto 

      - Admite una variedad de fuentes de datos, incluidos texto y voz. 

      - Análisis del centro de llamadas / contact center. 

      - API abierta e integración con cientos de sistemas de terceros, incluido CRM. 

   - Análisis de la experiencia del cliente 

      - Realiza un estudio de conversaciones con clientes para intentar obtener información implícita de los mismos. 

      - Análisis del sentimiento y del tono de la voz. 

      - Permite predecir la preocupación y la rotación del cliente. 

   - Seguro de calidad 

      - Análisis del Contact Center para garantizar que el personal cumple con los requisitos de calidad establecidos. 

      - Automatización del proceso de supervisión para el seguimiento de la fuerza de ventas. 

- **Discovery** 

Este servicio es un motor de búsqueda cognitiva y análisis de contenido a las aplicaciones para identificar patrones, tendencias y conocimientos útiles que puedan derivar en una mejor toma de decisiones. Con Discover se permite consolidar con seguridad datos estructurados y no estructurados, más contenido preenriquecido para posteriormente realizar consultas simplificadas y así eliminar la necesidad de filtrar manualmente resultados de estas. Esto va a permitir al usuario/consumidor del servicio: 



112 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

1. Obtener resultados rápidos 

Reduciendo el tiempo en el tratamiento de los datos mediante una ingesta automatizada y el procesamiento del lenguaje natural integrado. Este servicio está completamente gestionado en la nube por lo que elimina la complejidad de lidiar con el contenido del lenguaje natural. 

2. Aplicar Inteligencia de dominio 

Es posible enseñar a Discovery a aplicar el conocimiento de entidades, relaciones, jerga… únicas en un sector u organización con Watson Knowledge Studio. 

3. Agilizar el uso de Inteligencia artificial en las empresas 

Discovery es capaz de encontrar conexiones en todos los datos de los que se nutre utilizando funciones avanzadas de inteligencia artificial predefinidas, como las consultas de lenguaje natural, la recuperación de fragmentos, el entrenamiento adecuado, los gráficos de relaciones y la detección de anomalías. 

4. Nativo en la nube, a escala empresarial y seguro 

Consta de soporte y seguridad a escala empresarial mediante, por ejemplo, el aislamiento de datos, el cifrado de extremo a extremo, el soporte y el cumplimiento del GDPR en los datos de información de identificación personal no regulados. 

- **IBM Match 360 with Watson** 

IBM Match 360 with Watson permite construir rápidamente todos los procesos para aplicar analítica de datos y generar otros casos de uso mediante datos maestros. Su uso puede comenzar por las entidades de IBM MDM Advanced o Standard Edition, o bien por los activos de datos que contienen información de terceros. Esto se traduce en poder asignar y modelar rápidamente nuevos atributos al modelo de datos trabajado con el fin de obtener una vista más completa de los usuarios o clientes de las compañías. Consta con un motor de correlación basado en IA que acelera la configuración del servicio gracias al uso de métodos estadísticos para mayor precisión. Se puede acceder a los resultados mediante las API RESTful, y estos se pueden exportar a archivos sin formato o visualizar en línea mediante el explorador de entidades. 



113 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



Fuente: <u>https://dataplatform.cloud.ibm.com</u> 

En definitiva IBM Match 360 with Watson ofrece un servicio completo que garantiza: 

1. Amplíe sus conocimientos sobre sus clientes 



2. Búsqueda de texto : Mediante búsquedas de texto y consultas en las entidades de datos maestros 

3. Acceso rápido y fácil: Capacidad de crear integraciones de servicio utilizando las API RESTful o IBM App 

114 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

4. Experiencia guiada por IA: Clasificación automática y correlación de diferentes campos en el proceso de modelado de datos, ajuste del algoritmo de forma constante gracias a los atributos de correlación sugeridos por la IA y la capacidad de priorizar los datos en todo el proceso. 

5. Coincidencia simplificada de casos de uso: Incorpora aprendizaje automático y años de experiencia para agilizar el proceso de configuración y ajuste de los algoritmos de forma constante. 



- **Knowledge Studio** 

Este servicio permite utilizar Watson con el fin de personalizar lenguaje y emplear dominios/tecnicismos concretos con modelos de aprendizaje automático. Esto permite la creación de patrones y relaciones exclusivas de ,por ejemplo, detección de cada sector en textos no estructurados. 

Consta de herramientas para la creación de modelos en un entorno colaborativo y diseñado para desarrolladores sin necesidad de escribir código. Algunos de los modelos al alcance de las personas que utilizan este servicio son de Watson Discovery, Watson Natural Language Understanding y Watson Explorer. 





115 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Mediante estos recursos se explotarán algunos resultados como: 

- Ofrecer a técnicos/expertos en ciertas industrias la posibilidad de enseñar a Watson el lenguaje de su sector u organización sin necesidad de usar código ni de grandes conocimientos técnicos. 

- No existe necesidad de una línea de código única. Al tratarse de un entorno colaborativo de varios usuarios, los expertos pueden generar fácilmente modelos sin ninguna experiencia en codificación. 

- WKS es completo. Es diferencial en el mercado ya que combina las prestaciones de anotación, formación y evaluación en un único servicio centrado en la colaboración. 



- Ejecutable en numerosos entornos: mediante modelos de Watson Knowledge Studio en Watson Discovery, Watson Natural Language Understanding o Watson Explorer, se puede desplegar en número tipo de aplicaciones lo previamente enseñado a Watson. 

#### • **Language Translator** 

Este servicio ofrece una traducción automática neuronal en pares de idiomas. Además al contar con cierto grado de personalización se pueden crear modelos propios de traducción que tengan en cuenta términos regionales específicos, por ejemplo. 

La traducción es instantánea y se permite realizar traducciones del contenido a múltiples idiomas. Se habilita la traducción de documentos, aplicaciones y sitios web. IBM Lenguage Translator incluso ofrece la posibilidad de crear chatbots conversacionales multilingües. 

116 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



- Traducción instantánea entre: 

Árabe, griego, hebreo, búlgaro, catalán, chino (simplificado y tradicional), croata, checo, danés, neerlandés, inglés, esloveno, español, sueco, tailandés, turco ,estonio, finés, francés, alemán ,hindi, húngaro, irlandés (gaélico), italiano, indonesio, japonés, coreano, lituano, malayo, noruego, polaco, portugués (brasileño), rumano, ruso, eslovaco. 



- Traducción automática neuronal 

De forma predeterminada, todos los pares de idiomas usan traducción automática neuronal. Esta nueva tecnología aprovecha el aprendizaje profundo para aportar mayor precisión a mayor velocidad. 

- Identificación de idioma gratuita 

Permite la identificación gratuita de más de 65 idiomas mediante un punto final en la API de identificación de idioma. 

- Personalización de corpus 

La generación de modelos personalizados específicos de un dominio mediante la creación de un corpus paralelo o un glosario específico a través de un archivo .tmx. Esto permitirá crear y obtener traducciones especializadas. 

- Traductor de documentos 

Mediante archivos admitidos que incluyen: MS Office, Open Office, PDF, HTML, JSON, TXT y XML. Se podrán traducir documentos de un idioma a otro manteniendo el formato y el tipo de archivo. 

117 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



- **Machine Learning** 

IBM Watson Machine Learning permite el trabajo en equipo entre desarrolladores y expertos en datos para integrar prestaciones predictivas con sus aplicaciones facilmente. Este servicio ofrece conjunto de API REST a las que puede invocar/ llamar desde cualquier lenguaje de programación con el fin de desarrollar aplicaciones que tomen decisiones más inteligentes, resuelvan problemas difíciles y mejoren los resultados de los usuarios que las utilizan. 



- Características de Machine Learning 

Acceso a la gestión (sistema de aprendizaje continuo) y el despliegue de modelos de aprendizaje automático. Se pone a disposición del usuario del servicio cualquiera de las infraestructuras de aprendizaje automático soportadas: TensorFlow, Keras, Caffe, PyTorch, Spark MLlib, scikit learn, xgboost y SPSS. 

- Amplia gama de interfaces 

Se puede utilizar desde la línea de comandos a un cliente de Python para gestionar el entorno. 

- Integración con Watson Studio 

La creación y entrenamiento de modelos de aprendizaje automático con las mejores herramientas y la experiencia de expertos en datos que colaboran en IBM Watson Estudio es parte del motor que nutre este servicio de IBM Cloud. 

118 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



Fuente: <u>https://cloud.ibm.com</u> 

- **Natural Language Understanding (NLU)** 

El uso de NLP para analizar texto y extraer metadatos de contenido como por ejemplo conceptos, entidades, palabras clave, categorías, sentimiento, emoción, relaciones y roles semánticos está cada vez más extendido. Además este servicio ofrece modelos de anotación personalizados desarrollados con Watson Knowledge Studio. Esto permite identificar relaciones y entidades específicas del sector/dominio/ técnica en un texto sin estructurar con Watson NLU. Es decir, IBM NLU se ofrecen las siguientes capacidades: 



1. Análisis en profundidad 

Análisis de las características semánticas de entrada de texto. Incluyen categorías, conceptos, emoción, entidades, palabras clave, metadatos, relaciones, roles semánticos y sentimientos. 

119 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

2. Personalización de dominios/sectores. 

Mayor comprensión del lenguaje natural con modelos personalizados basados en Watson Knowledge Studio que permiten identificar entidades personalizadas y relaciones únicas con su dominio. 



3. Amplio soporte de idiomas 

Da soporte a una amplia gama de idiomas en función de las características que se vayan a analizar, incluidos inglés, árabe, chino (simplificado), holandés, francés, alemán, italiano, japonés, coreano, portugués, ruso, español, sueco y próximamente más idiomas. 

4. Numerosas aplicaciones 

Se puede aplicar a distintos casos de uso, que incluyen recomendación de contenido, optimización de publicidad, segmentación del público, análisis de voz del cliente, minería de datos, etc. 

Más adelante se propone una actividad para el testeo práctico de este tipo de aplicaciones para NPL. 

#### • **Speech to Text** 

Este servicio convierte la voz humana en palabras escritas. El servicio utiliza inteligencia artificial de DL para aplicar conocimientos de estructura de idioma y gramática, a la vez que composición de señales de audio y voz para transcribir con precisión el habla humana. Se puede utilizar en diferentes aplicaciones desde chatbots automatizados basados en voz, a herramientas de análisis para Call Centers de servicio al cliente y transcripción multimedia. Algunas de las características que definen el servicio son: 

120 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



- Idiomas disponibles. 

Portugués de Brasil, chino (mandarín), holandés, inglés (de Estados Unidos y del Reino Unido), francés, alemán, italiano, japonés, coreano, español (de Argentina, España, Chine, Colombia, México y Perú) y árabe estándar moderno (solo modelo de banda ancha). 

- Interfaces y SDK. 

Se pueden habilitar transcripciones con API REST HTTP síncronas o asíncronas o emplear WebSockets para realizar solicitudes de alto rendimiento y baja latencia mediante una conexión dual completa. Se puede además enviar todo el audio de una vez o secuenciarlo para el reconocimiento de habla en directo. El uso de SDK para el desarrollo rápido y simplificado en Node, Java, Python, Swift y muchos otros lenguajes también están disponibles. 

- Personalización de idioma y acústica. 

Al igual que en el servicio de Speech to Text, la personalización de modelo de idioma para definir palabras específicas del dominio permiten ampliar el vocabulario básico del servicio. Añade la personalización de modelo acústico para mejorar el reconocimiento de características sonoras del audio y las gramáticas empleadas para limitar el reconocimiento a frases y expresiones específicas. 



121 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- Detección de palabras clave y etiquetas por nacionalidad/ habla. 

Se pueden identificar, por ejemplo, distintos hablantes en una conversación entre varios participantes. 

- Explotación de los metadatos de la transcripción. 

Se recibe una respuesta JSON que incluye puntuaciones de confianza, horas de inicio y finalización y varias alternativas posibles para una mayor explotación del servicio. Se puede además dividir una transcripción en múltiples resultados según características semánticas, como por ejemplo frases. 

- Perfeccionamiento constante de la transcripción. 

Se puede activar un formato inteligente para convertir fechas, horas, números, valores de moneda, números de teléfono y mucho más en los formatos escritos convencionales en las transcripciones finales. Además de eliminar información de identificación personal como números de teléfono o tarjeta de crédito de las transcripciones. También permite la censura del lenguaje obsceno en los metadatos y transcripciones. 

- Proceso y métricas de audio 

El servicio acepta la configuración de métricas de proceso para obtener información detallada sobre el análisis del audio, del servicio o métricas de audio para obtener información sobre las características de señal precisas del audio. 



Fuente: <u>https://unalfaruk.com</u> 

122 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### • **Text to Speech** 

El servicio Text to Speech convierte texto escrito en habla natural. El servicio transmite el audio sintetizado con un retardo mínimo. El audio utiliza la cadencia y la entonación adecuadas correspondientes al idioma y dialecto para proporcionar voces que suenan fluidas y naturales. Se puede utilizar el servicio en aplicaciones como por ejemplo chatbots automatizados de voz, así como en distintas aplicaciones sin pantalla y basadas en voz, como por ejemplo herramientas para personas discapacitadas o con problemas de visión, la narración de vídeo y la narración de voz y soluciones educativas y de automatización en el hogar. 

Las características del servicio son similares, prácticamente idénticas a las anteriormente estudiadas en Speech to Text. Añaden: 



- SSML 

Se permite anotar el texto de entrada con SSML (Speech Synthesis Markup Language), una notación basada en XML estándar para aplicaciones de síntesis de habla. Mediante el uso de SSML, se pueden controlar aspectos de la síntesis del habla como por ejemplo el volumen, la pronunciación, el tono, la velocidad entre otros atributos. 

- Personalización de la voz 

Se pueden personalizar y definir diccionarios para términos específicos del dominio, extranjerismos, nombres personales o geográficos y abreviaturas o acrónimos en el léxico de su aplicación. Pronunciaciones definidas basadas en otras palabras, o la creación de pronunciaciones basadas en fonemas del Alfabeto fonético internacional (IPA) y la Representación fonética simbólica (SPR) de IBM son opciones que la herramienta pone a disposición de los usuarios. 



123 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- Voces personalizadas 

Se puede entrenar una nueva voz para cada caso de uso y mercado objetivo. Con el servicio de IBM en apenas una hora de entrenamiento de datos el resultado estará disponible. 

#### • **Statum KPI** 

Amberoon Statum KPI es una solución de gestión del rendimiento de los resultados empresariales, específicamente ayuda a los bancos a medir y gestionar directamente su rendimiento en comparación con otros bancos similares u homólogos. 



La principal diferencia de este servicio con los sistemas de análisis operativos tradicionales, es que Statum proporciona información detallada sobre el futuro mediante un análisis riguroso de los patrones de rendimiento de diferentes instituciones de servicios financieros. 

Statum KPI se nutre de inteligencia artificial, aplica ingeniería de datos y cubre todo con una capa seguridad para crear un sistema de información que es capaz de respaldar las decisiones operativas clave en empresas del sector. 

#### • **Tone Analyzer (TA)** 

Todas las personas muestran distintos tonos de voz dependiendo de su estado anímico. Como por ejemplo alegría, tristeza, ira y simpatía en sus comunicaciones diarias. Dichos tonos pueden repercutir en la eficacia de la comunicación dependiendo de distintos contextos. IBM Tone Analyzer pretende sacar partido del análisis lingüístico cognitivo con el fin de identificar una serie de tonos en ambos niveles, de documento y de frase. Con esta información se busca refinar y mejorar las comunicaciones. El resultado del uso de este servicio detecta tres tipos de tonos, incluidos la emoción (ira, asco, miedo, alegría y tristeza), actitudes sociales (franqueza, diligencia, extroversión, simpatía y rango emocional), y estilos de lenguaje (analítico, seguro y vacilante). 

124 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



Con esto se busca: 

- Evaluación de tono genérico. 

Desde datos web más simples como, por ejemplo, mensajes de correo electrónico o tweets. Hasta documentos más largos como por ejemplo artículos o publicaciones de blog. Además se busca solucionar el estudio de los medios de comunicación y redes sociales para comprender qué están diciendo los clientes /usuarios de una marca, para así determinar a quién dirigirse con una mensajería específica. 



- Tono de fidelización 

La supervisión de las conversaciones de soporte y de servicio al cliente puede ser un caso de uso de esta herramienta. Además el escalar conversaciones con clientes cuando se creen tensiones o se busquen oportunidades para mejorar el servicio al cliente mediante IBM TA puede convertirse en una de las estrategias de diálogo y las experiencias del cliente de muchas empresas. 

125 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- Soporte multi idioma 

Introduciendo texto en inglés o en francés por ejemplo, se puede recibir una respuesta en árabe, alemán, inglés, español, francés, italiano, japonés, coreano, portugués de Brasil, chino simplificado o chino tradicional 

- **Watson Knowledge Catalog** 

El objetivo de este servicio es simplificar la ciencia de datos y la conformidad de los mismos. Esto permite que los datos sean fáciles de encontrar y compartir al tiempo que se controla el acceso a ellos para asegurar que se utilizan adecuadamente. 

Los objetivos principales son encontrar, controlar, catalogar la información. 





Fuente: <u>https://cloud.ibm.com</u> 

- **Watson OpenScale** 

IBM Watson OpenScale es un entorno empresarial y muy escalable para aplicaciones basadas en inteligencia artificial que proporciona principalmente visibilidad en cómo se crea y se utiliza la inteligencia artificial y cómo se genera retorno de la inversión en este tipo de desarrollos a nivel de negocio. 

126 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 





Fuente: <u>https://cloud.ibm.com</u> 

IBM Watson Open Scale se caracteriza por : 

1. Ser una herramienta abierta 

La creación y el desarrollo de inteligencia artificial precisa, se realiza mediante el uso del IDE que se elija, permitiendo así impulsar tanto el desarrollo de negocios como de equipos / soporte con conocimientos de datos. De esta manera la visibilidad de cómo afecta la inteligencia artificial a los resultados empresariales es mucho más comprensible. 

2. Tener un registro de carga útil 

El supervisar el estado continuo de aplicaciones empresariales a través de sus paneles permite ejecutar operaciones, establecer alertas y tener un rápido acceso a un gran repositorio de datos abierto para la creación de informes personalizados. 

127 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

3. Detección de sesgo y mitigación 

Esta herramienta detecta automáticamente cuándo los sistemas de inteligencia artificial entregan resultados equivocados en tiempo de ejecución, basándose en atributos de equidad determinados por la empresa. Además está diseñado para poder mitigar el sesgo a través de recomendaciones inteligentes de nuevos datos para poder entrenar también nuevos modelos. 



4. Confianza y transparencia en la IA 

La creación, ejecución  y gestión de IA proporciona a las compañías confianza para desplegarla en sus cargas de trabajo de producción más críticas, diferenciales y esenciales. 

5. Recomendaciones de IA 

Auditar y rastrear pronósticos de inversión en IA aplicada a entornos y aplicaciones productivas son casos de uso recurrentes del servicio . Es por ello por lo que los pronósticos de modelo y los factores que contribuyen a los resultados finales, o a resultados distintos, se muestran en términos empresariales comprensibles para diferentes tipos de usuarios. 

128 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



6. Supervisión del estado de la IA 

Garantizar una buena praxis de la IA, además de monitorizar los resultados que esta genera en aplicaciones empresariales es necesario para garantizar precisión, equidad y rendimiento en las empresas. Consta de paneles de instrumentos de operaciones, alertas y acceso a despensa de datos abierta para la creación de informes personalizados para este fin. 

- **Apache MXNet (Incubating) packaged by Bitnami** 

Apache MXNet (Incubating) es una biblioteca flexible y eficiente para el DL diseñada para funcionar como una red neuronal. Bitnami incluye OpenBLAS como biblioteca matemática. 



Bitnami empaqueta aplicaciones siguiendo los estándares de la industria y monitoriza continuamente todos los componentes y bibliotecas en busca de vulnerabilidades y actualizaciones de aplicaciones. Cuando se identifica cualquier amenaza de seguridad o actualización, Bitnami vuelve a empaquetar automáticamente las aplicaciones y envía las últimas versiones a los mercados de la nube. 

129 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- **PyTorch packaged by Bitnami** 



PyTorch es una plataforma de DL que acelera la transición de la creación de prototipos de investigación a la implementación de producción. Esta imagen de Bitnami incluye Torchvision para soporte específico de visión por computadora. 

- **TensorFlow ResNet packaged by Bitnami** 



TensorFlow ResNet es una utilidad de cliente para usar con los modelos TensorFlow Serving y ResNet. 



La combinación de IBM Cloud y todos los productos incluidos en Bitnami Application Catalog (no solo los mencionados específicamente para IA) aporta una serie de beneficios en la nueva era del Cloud Computing en la que IA , contenedores , y entornos híbridos deben convivir: 

- Versiones seleccionadas del mejor software de código abierto para desarrollos de IA. 

- Prueba y validación del ciclo de vida de la información para asegurar una correcta ejecución de las aplicaciones. 

- Portabilidad de las aplicaciones creadas, que además de ser consistentes pueden alojarse en el cloud que el usuario decida. 

130 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **3.4. Microsoft** 

Hoy, las organizaciones en búsqueda de un proveedor de nube pública se plantean Microsoft como uno de los principales proveedores del mercado en los que encontrar una amplia gama de servicios disponibles, en particular para crear un entorno de IT híbrido. 

Destaca el offering de Microsoft que principalmente se aglutina en las tres categorías principales de computación en la nube que se han estudiado a lo largo del módulo: software como servicio (SaaS), infraestructura como servicio (IaaS) y plataforma como servicio (PaaS). Comercializando sus ofertas de IaaS y PaaS bajo la marca Microsoft Azure. 

En según qué año de los últimos, Microsoft Azure se suele situar como el segundo servicio de IaaS y PaaS más grande del planeta, detrás de Amazon Web Services (AWS). Es particularmente popular entre las grandes empresas geográficamente dispersas, y en concreto en aquellas que usan software de Microsoft como Windows y Office. 

A día de hoy Microsoft Azure goza de una reputación como proveedor de nube pública maduro, confiable y altamente seguro. 

Antes de hacer hincapié en los servicios relacionados con la computación en la nube de IA , se plantea el escenario a través del cual Microsoft Azure se posiciona tras décadas en el lugar en el que está. 

Azure nace a mediados de la década de los años 2000 como una iniciativa interna de Microsoft cuyo nombre en código era Project Red Dog. En ese momento, Amazon ya había lanzado su servicio de computación en la nube y Microsoft se apresuraba a no quedarse atrás en este nuevo paradigma de provisionamiento de servicios. 



Ilustración. <u>https://www.dynasoftsolutions.es</u> 

Precisamente ocho años más tarde en la Conferencia de desarrolladores profesionales de Microsoft, dos años después de que Amazon Web Services (AWS) lanzara su Servicio de almacenamiento, Ray Ozzie, arquitecto jefe de software de Microsoft anuncia que la compañía planeaba lanzar su propio servicio de computación en la nube llamado Windows Azure. El plan era ambicioso ya que la idea fue que Microsoft ofreciera cinco categorías clave de servicios en la nube: Windows Azure para computación, almacenamiento y redes; Servicios de Microsoft SQL para bases de datos; Servicios de Microsoft .NET para desarrolladores; Servicios en vivo para compartir archivos; y ofertas SaaS de Microsoft SharePoint Services y Microsoft Dynamics CRM Services. 

131 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Citando a Ozzie: _“Es una transformación de nuestro software y una transformación de nuestra estrategia”._ 

En este momento del tiempo Microsoft reconoció el liderazgo de Amazon y señaló que AWS había implantado un patrón de diseño de nivel básico, modelos de arquitectura y modelos comerciales completamente novedoso. La predicción de la compañía en ese momento fue que todo su software empresarial se entregaría en los años posteriores como un servicio en línea principalmente. 

Tras el anuncio, Microsoft comienza a implementar versiones preliminares de sus servicios en la nube y, un par de años más tarde, la plataforma Windows Azure estuvo disponible comercialmente. Las primeras revisiones del servicio fueron mixtas, y muchos analistas IT compararon desfavorablemente a Azure con AWS. Sin embargo, Azure fue mejorado con el tiempo. Agregó entre otras mejoras soporte para proveer de una amplia variedad de lenguajes de programación, frames y sistemas operativos (incluido Linux, algo que alguna vez hubiera sido impensable para un producto de Microsoft). Esto último supuso que la compañía reconociera que su servicio de computación en la nube se había movido mucho más allá de Windows, y cambió el nombre de Windows Azure a Microsoft Azure a mediados del año 2014. 



Ilustración. <u>https://docs.microsoft.com</u> 

132 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

En los años transcurridos desde entonces, Microsoft ha seguido ampliando sus capacidades en la nube, cumpliendo en gran medida con las predicciones de Ozzie en el anuncio inicial en 2008. También ha aumentado su compatibilidad con el software de código abierto. En la actualidad Azure es una opción razonable incluso para las empresas que no basan su cómputo en la ejecución de servidores Windows. Compitiendo con AWS, Google Cloud e IBM, Microsoft Azure es uno de los líderes indiscutibles de a la hora de provisionar servicios cloud en la nube,  con un gran potencial de convertirse en principal proveedor de la nube a largo plazo según analistas de la materia. 

Microsoft Azure ofrece una cartera grande de servicios en la nube, que divide en catorce categorías: 

- Cómputo: incluye máquinas virtuales, conjuntos de escalado de máquinas virtuales, funciones para computación sin servidor, lote para cargas de trabajo por lotes en contenedores, Service Fabric para microservicios y orquestación de contenedores, y servicios en la nube para crear aplicaciones y API basadas en la nube. 

- Redes: incluye una variedad de herramientas de red, como la red virtual, que puede conectarse a centros de datos locales; equilibrador de carga; puerta de enlace de aplicaciones; puerta de enlace VPN; DNS de Azure para alojamiento de dominios, red de entrega de contenido, administrador de tráfico, conexiones de fibra de red privada dedicada ExpressRoute; y monitoreo y diagnóstico de Network Watcher 

- Almacenamiento: incluye Blob, Queue, File y Disk Storage, así como Data Lake Store, Backup y Site Recovery, entre otros. 

- Web + Mobile: incluye varios servicios para crear e implementar aplicaciones, pero el más notable es probablemente App Service, que comprende servicios para Web Apps, Mobile Apps, Logic Apps (un servicio de código bajo, basado en datos) y API Apps. (para crear y usar API). 

- Contenedores: incluye Container Service, que admite Kubernetes, DC/OS o Docker Swarm y Container Registry, así como herramientas para microservicios. 

133 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



Ilustración. <u>https://azure.microsoft.com</u> 

- Bases de datos: incluye varias bases de datos basadas en SQL y herramientas relacionadas, así como Cosmos DB, Table Storage para NoSQL y tecnología en memoria Redis Cache 

- Data + Analytics: incluye herramientas de big data como HDInsight para clústeres de Hadoop Spark, R Server, HBase y Storm; análisis de flujo; análisis de lagos de datos; y Power BI Embedded, entre otros 

- AI + Cognitive Services: incluye múltiples herramientas para desarrollar aplicaciones con capacidades de inteligencia artificial, como Computer Vision API, Face API, Bing Web Search, Video Indexer, Language Understanding Intelligent Service y más 

- Internet de las cosas (IoT): incluye los servicios IoT Hub e IoT Edge que se pueden combinar con una variedad de servicios de comunicaciones, análisis y aprendizaje automático. 

- Integración empresarial: incluye varias herramientas para crear y administrar entornos de computación en la nube híbrida 

- Seguridad + Identidad: incluye Security Center, Azure Active Directory, Key Vault y Multi-Factor Authentication Services 

- Herramientas para desarrolladores: incluye servicios de desarrollo en la nube como Visual Studio Team Services, Azure DevTest Labs, implementación y supervisión de aplicaciones móviles de HockeyApp, desarrollo móvil multiplataforma de Xamarin y más 

134 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- Supervisión y administración: incluye numerosas herramientas para administrar las cargas de trabajo de Azure y los entornos de nube híbrida, como Microsoft Azure Port, Azure Resource Manager, Log Analytics, Automation, Scheduler y más. 

- Microsoft Azure Stack: incluye soluciones para replicar la infraestructura de Azure en centros de datos empresariales con el objetivo de facilitar las implementaciones de nube híbrida 



Ilustración. <u>https://azure.microsoft.com/es-es/</u> 

Una de las mayores ventajas que tiene Microsoft en relación a sus servicios de computación en la nube se puede resumir, en una palabra: Windows. 

Para las organizaciones que ya usan software de Microsoft, como Windows, Office, SQL Server, SharePoint, Dynamics, etc , usar el servicio de computación en la nube de Microsoft implica una evolución del IT natural. Esto permite utilizar las herramientas e interfaces con las que sus trabajadores y gestores de tecnología ya están familiarizados y les ayuda a ponerse en marcha rápidamente. 

Microsoft ha hecho un esfuerzo particular para habilitar la computación híbrida, y su solución Azure Stack que se mostraba anteriormente. Microsoft también ha hecho foco en el entorno gubernamental ya que promociona altas capacidades de seguridad y cumplimiento normativo de múltiples países. 

Un punto para recalcar es que Azure tiene un ecosistema muy amplio y nutrido que implica fuertes alianzas y asociaciones con otros proveedores de tecnología. Por ejemplo, tiene relaciones con Red Hat, Canonical, Citrix, HPE, Adobe, SAP, Cisco y muchos otros, que mejoran los servicios que puede ofrecer a los clientes. 

135 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



Ilustración. <u>https://www.cloudmasters.es</u> 

Microsoft Azure es una excelente opción para las organizaciones que ya usan software de Microsoft en sus centros de datos como se ha comentado, y que además están interesadas en crear entornos de nube híbrida. Las grandes organizaciones parecen particularmente atraídas por Azure según datos extraídos de la lista Fortune 500. 

Los desarrolladores que usan las herramientas de desarrollo de Microsoft, particularmente Visual Studio, encuentran en Azure una performante solución tanto para servidores de desarrollo/prueba como de producción. Microsoft ha incorporado por tanto la integración entre el servicio en la nube y sus herramientas de desarrollo, lo que facilita su uso conjunto. 

Tras esta breve visión generalista del posicionamento de Azure en el mercado y descripción de la oferta de servicios en cloud, daremos paso en el capítulo a estudiar los servicios de AI + Cognitive que Microsoft Azure tiene a disposición de sus clientes. En este punto encontramos una cartera de servicios de inteligencia artificial diseñada para desarrolladores y científicos de datos muy amplia. Tras décadas de investigacióne innovación, Azure incorporó a su cartera de servicios procedimientos de IA responsable, con capacidad de ser consumidos de una forma totalmente flexible, para crear e implementar sus propias soluciones de inteligencia artificial. Azure ofrece desde el acceso directo modelos de inteligencia artificial de visión, voz, lenguaje y toma de decisiones de alta calidad a través de llamadas API sencillas, y la posibilidad de crear modelos  propios de aprendizaje automático con herramientas como Jupyter Notebooks, Visual Studio Code y marcos de código abierto, como TensorFlow y PyTorch. 

136 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



En concreto, existen cuatro bloques desde los que Azure provisiona y aglutina su oferta de servicios en la nube orientados al desarrollo de IA. 

### **3.4.1. Servicios de IA aplicada de Azure** 

Son servicios de inteligencia artificial especializados para escenarios y resolución de problemáticas empresariales específicas. La cartera de productos permite ejecutar una modernización de ciertos procesos empresariales y comerciales. 

Entre algunos procesos a destacar encontramos la automatización en el procesamiento de documentos, mejora del servicio al cliente, comprensión de la causa raíz de las anomalías en los procesos comerciales y la extracción de información de cualquier contenido. Esto se consigue mediante el uso de modelos propios de IA de Azure Machine Learning. 

En definitiva el objetivo es la modernización de los procesos empresariales con inteligencia artificial aplicada en tareas específicas que resuelvan los escenarios más comunes de las empresas. De esta manera acelerar de forma lógica e integrada el negocio ejecutando soluciones de forma responsable en cualquier lugar, con una seguridad que se extienda desde la nube hasta el perímetro de las organizaciones. 



137 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Las herramientas que encontramos son: 

- **Azure Bot Service** 

Permite desarrollar experiencias de usuario mediante inteligencia artificial conversacional con un nivel empresarial a la vez que mantiene el control de los datos utilizados. Permite la creación de bots multilingües y multimodales para cualquier escenario; desde ventas hasta atención al cliente y control de la  productividad de los empleados. 

Las capacidades clave de este servicio son: 

- Fácil de empezar a ser utilizado: mediante una rápida conversión de la documentación y las páginas de encuestas (por ejemplo) existentes en bots simples. 

- Nivel empresarial: mediante la ejecución de los parámetros de seguridad, disponibilidad, cumplimiento legislativo y respaldados  por Azure. 

- Experiencia de conversación natural: Garantiza la creación de diseños de conversación sofisticados y de varios turnos, como manejo de interrupciones, cancelaciones y cambio de contexto. 

- Multilingüe, multimodal: Permite la creación de bots que comprenden y hablan varios idiomas y admite texto y voz. 

- Fuente abierta: Consta de componentes conversacionales reutilizables creados por la comunidad de código abierto. 

- Extensible: El bot creado puede nutrirse con componentes adicionales como cuadros de diálogo y modelos de lenguaje. 

#### • **Azure Form Recognizer** 

Esta herramienta permite rápidamente realizar la extracción del texto y la estructura de los documentos con el fin de acelerar procesos de negocio automatizando la extracción de información. Azure Form Recognizer aplica aprendizaje automático avanzado para extraer con precisión textos, pares clave-valor, tablas y estructuras de los documentos. Con solo unas pocas muestras Azure Form Recognizer se puede adaptar para comprender documentos que se almacenen tanto en las instalaciones propias de la empresa como en la nube. Todo ello con el fin de convertir documentos en datos utilizables en una fracción del tiempo muy reducida. El servicio destaca por una serie de especificidades. 

138 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- Extracción de texto sencilla: Obtención de datos fácil así como de su organización con funciones preconstruidas y personalizadas, sin necesidad de etiquetado manual. 

- Resultados personalizados: Los resultados son adaptados a los diseños propios de cada empresa gracias a la extracción personalizada automática y la constante mejora mediante la incorporación de comentarios humanos. 

- Implementación flexible: Ingesta de datos desde la nube o desde el perímetro de las organizaciones, aplicación a índices de búsqueda y flujos de trabajo de automatización empresarial. 

- Seguridad integrada: Es una herramienta con un alto nivel de seguridad y garantía de privacidad a nivel empresarial, aplicadas tanto a sus datos como a cualquier modelo capacitado. 

La personalización de documentos de forma rápida mediante el reconocimiento del contenido es fácilmente ejecutable. Desde https://azure.microsoft.com/en-us/ <u>services/form-recognizer/#features</u> se ofrece la posibilidad de edición predeterminada de documentos generales. 



139 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### **CASO PRÁCTICO. Ampliación voluntaria.** 

1. Acceda al siguiente recurso <u>https://fott-2-1.azurewebsites.net/</u> 



2. Visite la Guía de Uso <u>https://docs.microsoft.com/en-us/azure/applied-ai-services/ form-recognizer/quickstarts/get-started-sdk-rest-api?pivots=programming-language-csharp#try-it-prebuilt-model</u> 

3. Seleccione la opción de Uso de Modelo predeterminado tras 



4. Seleccione el tipo de documento para testear que desee y siga las instrucciones de la guía recomendada para acceso a la API 

140 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



5. Ejecute análisis y analice resultados. 



#### • **Azure Cognitive Search** 

Azure Cognitive Search es el único servicio de búsqueda en la nube con capacidades de IA integradas que enriquecen todo tipo de información para ayudar a identificar y a explorar el contenido relevante de una forma muy escalable. Integra capacidades cognitivas para la visión, el lenguaje y el habla, incluso el poder usar modelos de aprendizaje automático personalizados para descubrir información en todo tipo de contenido. Azure Cognitive Search también ofrece la capacidad de búsqueda semántica, que utiliza técnicas avanzadas de aprendizaje automático para comprender la intención del usuario y clasificar contextualmente los resultados de búsqueda más relevantes. 

- Es un servicio completamente administrado para reducir la complejidad y escalar fácilmente capacidades de autocompletado, búsqueda geoespacial, filtrado y creación personalizada de contenido para una rica experiencia de usuario. 

- Incorpora capacidades de IA integradas que incluyen OCR, extracción de frases clave y reconocimiento de ciertas palabras malsonantes nombradas para desbloquear dicha información. 

- Consta de una capacidad de búsqueda semántica impulsada por modelos de aprendizaje profundo que comprenden la intención que el usuario quiere mostrar y permite clasificar los resultados de búsqueda más relevantes. 

141 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### • **Azure Metrics Advisor** 

Esta herramienta permite integrar funciones de monitorización impulsadas por IA para dar información a los administradores de IT y ayuadarles a ir un paso por delante en la resolución de posibles incidentes, sin necesidad de experiencia en aprendizaje automático. Esto implica una supervisión del rendimiento de los motores de crecimiento de su organización, incluidos los ingresos por ventas y las operaciones de fabricación. Azure Metrics Advisor integra también Anomaly Detector para identificar y solucionar problemas rápidamente a través de una poderosa combinación de monitorización casi en tiempo real, adaptando modelos a su escenario y ofreciendo análisis granular con diagnósticos y alertas. 

#### • **Azure Video Analyzer** 

La herramienta Azure Video Analyzer permite a los desarrolladores crear rápidamente una solución de análisis de video impulsada por IA para extraer información útil de los videos, ya sea almacenados o transmitidos. Esto permite mejorar la calidad en la edición de videos de una forma segura, mejorar las experiencias relacionadas a la gestión de activos digitales, archivos de media y la comprensión del contenido de audio y video para personas sin experiencia en gestión documental ni ML. 

Azure Video Analyzer al final es un servicio de plataforma de desarrollo para análisis de video, y Azure Video Analyzer for Media aporta las soluciones de inteligencia artificial dirigidas a escenarios de media y entretenimiento. Azure Video Analyzer se basa en modelos de IA, lo que simplifica la captura, la orquestación y la reproducción para la transmisión y los videos almacenados. El análisis del video se ejecuta en tiempo real para crear espacios de trabajo más seguros, experiencias óptimas en la tienda y más. 



142 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Mediante esta herramienta usuarios y compañías dedicadas a la edición de vídeos, por ejemplo, pueden procesar rápidamente sus bibliotecas de videos para mejorar la detección de contenido y aumentar la participación de los usuarios con Azure Video Analyzer for Media. 



Es decir, Azure Video Analyzer for Media puede adaptar los modelos de IA para mejorar la precisión de la información para dar sentido a su contenido, haciendo avanzar la industria en un momento en que la creación de contenido de video está creciendo exponencialmente. Además permite indexar el contenido, puede crear nuevos medios a partir del contenido existente utilizando el editor de video basado en IA. Es decir, permite encontrar el contenido multimedia adecuado en una biblioteca, localizar la información/imágenes que interesen en cada momento y usar un editor para unirlas en un nuevo video. 

### **3.4.2. Azure Cognitive Services** 

Cognitive Services aglutina una serie de servicios de inteligencia artificial tanto para desarrolladores como para científicos de datos. Existen una serie de los modelos iniciales que pueden solventar una gran variedad de casos de uso. Lo único que se necesita es una llamada API para insertar la capacidad de ver, escuchar, hablar, buscar, comprender y acelerar la toma de decisiones avanzada en las aplicaciones que se nutran de estos modelos propios de Microsoft.  Las soluciones de este catálogo se pueden agrupar en cinco categorías en base a la función utilizada para la aplicación de IA y el caso de uso a resolver. 

143 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Una casuística habitual es la mejora de experiencias de los clientes con Cognitive Service para voz. Esto incluye diversas funciones: **Speech to Text:** transcripción de la voz en texto legible en el que se pue- **Voz** dan realizar búsquedas. **Text to Speech:** Conversión de un texto en un lenguaje más natural para obtener interfaces más reales. **Speech Translation:** Fácil integración de la traducción de voz en tiempo real en aplicaciones. **Speaker Recognition:** Identificación de personas que hablan basándose en audio. Entender conversaciones y el contenido de texto no estructurado con Cognitive Service para lenguaje, permite solucionar una serie de casos de uso concretos y transversales en diferentes compañías: **Reconocimiento de entidades:** Identificación de los términos de uso común y específicos del dominio. **Lenguaje Análisis de opiniones:** Detección automática de sentimientos y opiniones a partir de texto. **Respuesta a preguntas:** Integra la capacidad de crear una capa conversacional de preguntas y respuestas sobre los datos. **Language Understanding:** Esta funcionalidad es novedosa y permite incorporar el reconocimiento del lenguaje natural a aplicaciones como bots y dispositivos IoT. **Translator Text:** Garantía de transcribir y traducir más de 100 idiomas y dialectos. 

##### **Visión** 



##### **Decisión** 



**API de reconocimiento facial:** Detección e identificación de personas y emoticonos en las imágenes. **Computer Vision:** Permite el análisis del contenido de imágenes y vídeos. **Custom Vision:** Permite realizar el reconocimiento de imágenes para adaptarlo a las necesidades empresariales de cada compañía. **Anomaly Detector:** Este servicio permite la identificación temprana de los posibles problemas en el entorno empresarial. 

**Content Moderator:** Detecta el contenido potencialmente ofensivo o no deseado. **Personalizer:** Con esta herramienta se pueden crear experiencias personalizadas muy completas para cada usuario. 

144 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

**OpenAI** Microsoft Azure además incorpora una serie de Modelos de lenguaje dinámicos para mejorar las aplicaciones mediante **OpenAI Service** . De esta manera aplicar modelos de lenguaje avanzados a una gran variedad de casos de uso se pone al alcance de numerosas compañías. Esta herramienta no solo permite realizar la personalización de modelos, también conocer los fundamentos de la inteligencia artificial y adquirir experiencia práctica en este campo por parte de los equipos de IA de las compañías. 

### **3.4.3. Azure Machine Learning** 

Azure tiene su propia plataforma para crear, entrenar e implementar modelos de Machine Learning. Dicha plataforma permite tener una visión completa del proceso de generación de algoritmos. 

- Permite desarrollar soluciones con las herramientas como Jupyter Notebook. 

- Creación e implementación de modelos a gran escala usando flujos de trabajo de aprendizaje automático automatizados y reproducibles. 

- Herramientas integradas para reconocer, proteger y controlar los datos, los modelos y los procesos. 

- Gran compatibilidad con plataformas y lenguajes de código abierto, como MLflow, Kubeflow, ONNX, PyTorch, TensorFlow, Python y R. 

- Control total del l ciclo de vida del aprendizaje automático de un extremo a otro (ML) 



145 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

||- Etiquetado de datos.<br>Etiquete los datos de entrenamiento y administre proyectos de<br>etiquetado.|
|---|---|
|**Preparar**<br>**datos**|- Preparación de datos.<br>Integración con motores de análisis para la exploración y preparación<br>de datos.<br>- Conjuntos de datos<br>Acceso a datos , creación y compartición de diferentes conjuntos de<br>datos.|
||- Notebooks : cuadernos de colaboración de Jupyter con procesos<br>asociados.<br>- El ML es automatizado gracias a la posibilidad de diseñar modelos de<br>forma simplificada mediante una interfaz de desarrollo de arrastrar y<br>colocar.|
|**Compilar**<br>**y entrenar**<br>**modelos**|- Permite la ejecución de experimentos así como la creación de paneles<br>personalizados con Visual Studio Code y GitHub<br>- Herramientas ejecutables en entornos híbridos de computación.<br>- Desarrollo en un entorno administrado y seguro servidores con CPUs<br>en la nube, GPU y clústeres de supercomputación.<br>- Bibliotecas y frames de código abierto: soporte integrado para Scikit-<br>learn, PyTorch, TensorFlow, Keras, Ray RLLib y mucho más.|
|**Evaluar e**<br>**implementar**|La plataforma consta de Puntos de conexión administrados que permite<br>automatizar los flujos de trabajo de aprendizaje automático.<br>Además permite acelerar los procesos de entrenamiento e inferencia, y<br>reducir los costes genéricos de la adopción de IA con ONNX Runtime.|
|**Administrar**<br>**y supervisar**|La plataforma permite supervisar, analizar, registrar y analizar datos,<br>modelos y recursos. También detectar el desfase de datos y mantener<br>la precisión del modelo. La plataforma también goza de una supervisión<br>continua con Azure Security Center y cuenta con herramientas de<br>auditoría constante de los procesos ejecutados en ella.|



146 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



Ilustración. MLOps para modelos de Python con Azure Machine Learning 

### **3.4.4. Infraestructura para Inteligencia Artificial como servicio** 

En los últimos años, grandes modelos de lenguaje de aprendizaje profundo (ML) con millones de parámetros han mejorado el estado del arte en casi todas las tareas de procesamiento de lenguaje natural (NLP) posteriores. En Microsoft, los ingenieros de todos los equipos de productos han colaborado ampliamente con Microsoft Research para crear representaciones de lenguaje semántico nuevas y más genéricas. El entrenamiento de modelos masivos de IA requiere herramientas innovadoras e infraestructura avanzada (grupos de hardware de última generación que pueden realizar cálculos de IA conectados por redes de gran ancho de banda), así como herramientas innovadoras para entrenar los modelos en estas computadoras interconectadas. 

Para comprender el impacto de la IaaS para IA que Microsoft ofrece como servicio es importante remontarse a comienzos del año 2020. En esta fecha Microsoft presenta el modelo Turing Natural Language Generation (Turing-NLG) que superó el estado del arte en una variedad de puntos de referencia de modelado de lenguaje gracias sus más de 15.000 millones de parámetros. 

147 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Microsoft Azure pone a disposición del mercado estas capacidades de infraestructura para IA a escala para el entrenamiento de modelos de esta magnitud. Con la plataforma Azure AI el acceso a hiper clústeres que cuentan con miles de GPU de última generación garantiza el uso de redes de gran ancho de banda dentro de cada servidor para poder aprovechar un entorno de computación de alto rendimiento (HPC) como servicio. De esta forma se consigue lograr el entrenamiento de modelos de gran envergadura y de forma masiva. 

Azure ofrece una gran infraestructura para cargas de trabajo de IA de todos los tamaños, compatible con la aceleración de GPU para frames populares como TensorFlow, PyTorch y otro. Es decir, Azure pone a disposición del usuario desde una sola GPU, hasta incluso máquinas virtuales con ocho GPU NVIDIA V100 de 32 GB con NVLink y 100 Gigabit InfiniBand EDR a nivel de clúster, por ejemplo, que permiten poner cerca de 1,000 GPU a funcionar al mismo tiempo. 



En definitiva el servicio de IaaS específico para IA de Azure ofrece una serie de beneficios a sus consumidores: 

- Acceso a una infraestructura a gran escala con hiperclústeres de miles de GPU de última generación, lo que proporciona una aceleración de la inteligencia artificial que está interconectada con las redes de gran ancho de banda más novedosas en cada servidor. 

- Habilita la posibilidad de desplegar implementaciones híbridas y multicloud con Kubernetes habilitado para Azure Arc. 

- Azure da paso a numerosos usuarios y compañías a una amplia gama de hardware de inteligencia artificial con hardware especializado, como FPGA, el conjunto más completo de GPU y una matriz de CPU de uso general. 



148 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **3.5. Alibaba** 

Desde 2009 Alibaba Cloud se convirtió en la columna vertebral de los servicios y tecnología digital de Alibaba Group. La empresa asiática ofrece un conjunto completo de servicios en la nube a clientes de todo el mundo, que incluyen computación flexible, bases de datos, almacenamiento, servicios de virtualización de red, computación a gran escala, servicios de seguridad, administración y aplicaciones, análisis de big data, una plataforma de aprendizaje automático y servicios de IoT.  Según IDC , Alibaba Cloud es el proveedor líder de servicios de nube pública de China en cuestión de ingresos procedentes de servicios PaaS e IaaS. 

La gama de productos en la nube de Alibaba Cloud incluye capacidades de computación a gran escala, recursos de almacenamiento y procesamiento de Big Data para usuarios de todo el mundo. En concreto en torno a los servicios de IA encontramos bloques similares a los ofertados por otros grandes empresas ya comentadas en este módulo. 



A alto nivel , la arquitectura de Machine Learning Platform For AI de Alibaba Cloud se compone de varias capas. De abajo hacia arriba, las capas incluyen el motor de computación, la arquitectura de computación distribuida, el conjunto de algoritmos ofrecidos y la capa de aplicación o servicio. La capa del motor de computación de Machine Learning Platform For AI se basa en el sistema informático distribuido Apsara. Esto permite que Machine Learning Platform for AI calcule simultáneamente datos de nivel EB. 

149 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



##### Ilustración. <u>https://www.alibabacloud.com</u> 

La capa informática de arquitectura distribuida de Machine Learning Platform For AI brinda soporte para múltiples arquitecturas informáticas distribuidas, como MPI, MR y GRAPH. La capa de componentes del algoritmo proporciona soporte para más de cien algoritmos de aprendizaje automático. Mediante el uso de sus propios algoritmos, Machine Learning Platform For AI puede admitir múltiples escenarios de servicio, como la recomendación de productos, la gestión de riesgos financieros y la publicidad en la capa de aplicación del servicio. Uno de ellos, por ejemplo, es el servicio de Intelligent Speech Interaction. Intelligent Speech Interaction se desarrolla sobre tecnologías de última generación, como el reconocimiento de voz, la síntesis de voz y la comprensión del lenguaje natural. Intelligent Speech Interaction está actualmente disponible en chino mandarín, chino cantonés, inglés, japonés, coreano, francés e indonesio, y está atento a otros idiomas. 

150 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

## **4. Contenedores y microservicios orientados a la IA** 

_“El enfoque IT basado en la nube describe una manera de modernizar las aplicaciones monolíticas existentes y crear nuevas aplicaciones internas en función de estándares de la nube, mediante el uso de estrategias y la adopción de métodos optimizados para la implementación y automatización de la computación en la nube.”_ 

El concepto de digitalización refleja el rápido crecimiento de empresas nativas digitales que con su transformación tecnológica evolucionan modelos empresariales tradicionales y hacen desarrollar empresas y sectores industriales ya existentes en torno a tecnologías innovadoras como pueden ser dispositivos móviles, IoT, realidad virtual, chat bots, blockchain, aprendizaje autónomo y otras tecnologías. 

Esta transformación digital implica adoptar una cultura muy dinámica, donde el ritmo acelerado del mercado sólo se puede satisfacer con procesos de desarrollo y producción más rápidos y flexibles. La reconstrucción total de la base tecnologica en muchos casos no es viable, tampoco adoptar nuevas metodologías e ideas de forma inmediata en procesos y tecnología. 

Cobra entonces importancia el uso de diferentes tipologías de software que permiten a las empresas su adaptación a la era de las nuevas tecnologías de forma fexible, rápida y que les permiten mantener y aumentar su competitividad. 

El enfoque IT basado en la nube describe una manera de modernizar las aplicaciones monolíticas existentes y crear nuevas aplicaciones internas en función de estándares de la nube, mediante el uso de estrategias y la adopción de métodos optimizados para la implementación y automatización de la computación en la nube. Parte de esta visión se ha medido en capítulos anteriores. Para terminar de complementarlos a continuación centramos la temática en dos pilares fundamentales: la tecnología de computación sin servidor y cómo se relaciona con los microservicios. 

En su mayoría, la mayor parte de las tecnologías de las que hablaremos hoy las proporcionan IBM, Microsoft, Amazon o Google (como se ha estudiado anteriormente). En este apartado ampliaremos conocimiento sobre qué es computación sin servidor y las piezas clave en esta tecnología para entender cómo aprovecharlos mejor y hablaremos de dónde podría usarse eso en el contexto de una arquitectura de microservicios. 

151 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Este apartado ofrece una visión completa sobre las bases y fundamentos de los microservicios y la computación sin servidor. Esta tendencia tecnológica tiene una relación importante con el consumo y uso de servicios de inteligencia artificial debido a la flexibilidad que aporta este tipo de tecnología. Sin embargo, el uso de contenedores puede presentar una serie de desafíos y retos que también serán analizados. Conceptos como qué es Istio y los diferentes Service Mesh (servicios en malla) cobran importancia a la hora de comprender cómo los contenedores encajan en el mundo de la IA. 

La experiencia de personas de todo el mundo, junto con la aparición de nuevas tecnologías, están teniendo un efecto potente en cómo se utilizan los microservicios, en relación y más allá al uso de Inteligencia Artificial. A continuación, se presentan ejemplos concretos del mundo real, para ayudar a comprender si los microservicios son adecuados para diferentes casos de uso, aplicaciones e implementaciones entorno a la IA. 

### **4.1. Visión general de los microservicios: beneficios e inconvenientes** 

La arquitectura de microservicios crea aplicaciones de software utilizando servicios pequeños, autónomos y con versiones independientes. Estos servicios utilizan interfaces bien definidas y se comunican entre sí a través de protocolos estándar muy ligeros. 

La interacción con un microservicio se lleva a cabo a través de una interfaz definida. Cada microservicio se enfoca en hacer bien una tarea y que pueden trabajar junto con otros microservicios para realizar tareas que son más complejas. 

Una arquitectura de microservicios es muy adecuada para sistemas de software grandes y/o complejos. A diferencia de las arquitecturas monolíticas, las aplicaciones creadas con una arquitectura de microservicios manejan la complejidad al dividir la aplicación en servicios más pequeños que son más fáciles de administrar. El siguiente diagrama ilustra un sistema que tiene una arquitectura de microservicios: 



152 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Las solicitudes entrantes se manejas comúnmente mediante una puerta de enlace API, que sirve como punto de entrada al sistema. Es un servidor HTTP que toma las solicitudes de los clientes y las enruta al microservicio apropiado a través de su configuración de enrutamiento interno. 

En cambio, las arquitecturas de microservicios a menudo son una mala elección para productos nuevos o empresas recién creadas. Está habiendo un cambio en los modelos de desarrollo que, a su vez, darán como resultado que se realicen más cambios en las limitaciones actuales de microservicios. 

Las arquitecturas de microservicios pueden generar mucha complejidad en el diseño y la implementación. Si se desarrolla el software con sus propios medios en la empresa, puede compensar esta nueva complejidad adoptando nuevas tecnologías, formándose en nuevas habilidades y cambiando las prácticas de trabajo. Pero no es algo rápido ni sencillo de aplicar. 

Dicho esto, hay una serie de propiedades básicas relacionadas con la arquitectura de microservicios. En este módulo, examinaremos las siguientes características: 

- Servicios pequeños y enfocados. 

- Interfaces de servicio bien definidas. 

- Servicios de despliegue autónomos e independientes. 

- Almacenamiento de datos independiente. 

- Comunicación con protocolos ligeros. 

- Mejor tolerancia a fallos o errores. 

#### **Servicios pequeños y enfocados** 

La funcionalidad de un microservicio debe tener un alcance reducido. Cada microservicio debe seguir el principio de la filosofía Unix que aboga por hacer una cosa y hacerla bien. Mantener el alcance para cada servicio permite administrar mejor la complejidad del software. 

Las aplicaciones con una arquitectura de microservicios son más fáciles de entender y modificar porque cada servicio tiene una responsabilidad concreta. Esto permite que los servicios se implementen más rápido. Las soluciones más pequeñas son más fáciles de cargar y usar en un ISE (Interfaz de programación), lo que aumenta la productividad. 

153 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Un microservicio puede ser desarrollado por un equipo pequeño. Esto permite a las organizaciones dividir fácilmente el trabajo entre varios equipos de desarrollo. Un solo equipo puede trabajar en cada microservicio, independientemente de otros microservicios. Las tareas para diferentes microservicios pueden trabajar en paralelo. 

Si un sistema de software también utiliza una implementación controlada por áreas, el concepto de implementaciones delimitadas funciona bien con los microservicios, ya que ayuda con la separación de los servicios. En algunos sistemas, cada microservicio se implementa como su propia área delimitada. 

#### **Interfaces de servicio bien definidas** 

Los microservicios se tratan como cajas negras, ocultando su complejidad y los detalles de implementación a los usuarios de servicios. Esto crea una interfaz bien definida, con puntos de entrada y salida claros, lo cual es importante para ayudar a facilitar que los microservicios trabajen juntos. Los servicios interactúan entre sí a través de sus interfaces. 

#### **Servicios de despliegue autónomos e independientes** 

Una aplicación que utiliza una arquitectura de microservicio consta de un sistema de servicios autónomos. 

Los servicios deben estar acoplados de manera flexible, interactuando a través de sus interfaces bien definidas y no deben depender de la implementación del propio servicio. Esto permite que la implementación de servicios cambie y evolucione independientemente de los otros servicios. Siempre que la interfaz del servicio no se modifique, es menos probable que la modificación de un microservicio requiera cambios en otras partes de la aplicación. 

Los servicios autónomos se pueden implementar de forma independiente, lo que facilita su implementación en un sistema productivo. Una arquitectura de microservicio permite la implementación continua porque es más fácil lanzar actualizaciones a los servicios.  Si se realiza un cambio en un microservicio, se puede implementar independientemente de los otros microservicios. La autonomía de los servicios aumenta la agilidad de la empresa. Permite a las empresas adaptarse rápidamente a los requisitos comerciales cambiantes y aprovechar las nuevas oportunidades comerciales. 

#### **Almacenamiento de datos independiente** 

Una de las características que respaldan la independencia del servicio es que cada microservicio puede tener su propio almacén de datos. Esto ayuda a que los servicios sean independientes y estén poco acoplados a otros servicios. 

154 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

El almacén de datos de un servicio se puede modificar sin que esos cambios afecten a otros servicios. El diseño de cada microservicio para que tenga su propio almacén de datos puede venir en forma de un microservicio con su propia base de datos, pero esa no es la única forma de mantener oculto el almacenamiento de datos de un microservicio. 

Si la tecnología de almacenamiento de datos es un sistema de administración de bases de datos relacionales (RDBMS), además de la opción de tener un servidor de base de datos separado, los datos se pueden mantener separados al designar ciertas tablas como propiedad de un servicio en particular. Otra opción es designar un esquema que solo lo utilizará un único microservicio. 

#### **Mejor tolerancia a fallos o errores** 

Un sistema construido sobre una arquitectura de microservicios mejora el aislamiento de fallos o errores. Cuando un microservicio deja de funcionar, otros servicios pueden seguir funcionando normalmente, lo que permite que otras partes del sistema permanezcan operativas. Esto es lo opuesto a una aplicación monolítica, donde un fallo puede provocar una caída completa del sistema. 

### **4.2. Migración de arquitecturas nativas monolíticas a microservicios** 

Las aplicaciones tradicionales pueden tener una arquitectura monolítica. En ese caso, el código puede tener componentes estrechamente acoplados y muy dependientes entre sí. 

Si la aplicación es grande y compleja, puede resultar difícil realizar cambios en una aplicación monolítica. 

Un enfoque para modernizar una aplicación heredada es comenzar a introducir microservicios. Los microservicios son servicios pequeños, enfocados y autónomos que se pueden implementar de forma independiente. 

Al contrario que una aplicación monolítica, el enfoque de microservicios reduce el nivel de complejidad al dividir una aplicación en pequeños servicios que son más fáciles de mantener y administrar. En una aplicación tradicional, podemos tomar componentes y colocarlos en microservicios. 

Los componentes de la aplicación tradicional que necesitan la funcionalidad contenida en un microservicio pueden interactuar con él a través de su interfaz. Las implementaciones de cada servicio se pueden cambiar siempre que la interfaz siga siendo la misma. 

También nos da la capacidad para que un desarrollador modifique un microservicio independientemente de otros servicios. A diferencia de las modificaciones realizadas en una aplicación tradicional, es menos probable que los cambios en microservicios individuales requieran modificaciones en otros lugares de la aplicación. 

155 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Como hemos visto antes, hay una mejor tolerancia a fallos con microservicios. Si una aplicación heredada tiene una arquitectura monolítica, un fallo podría tumbar una gran parte de la aplicación o incluso toda la aplicación. Cuando un solo microservicio falla, no provocará que se caiga toda la aplicación. 

Combinado con una monitorización adecuada, que alertará a los administradores sobre un fallo rápidamente, un microservicio se puede reiniciar rápidamente. 

Si hay un problema con la versión actualmente implementada de un microservicio, se puede implementar una nueva versión que contenga una solución sin tener que modificar toda la aplicación. 

También tenemos la opción de volver a una versión anterior del microservicio si aparece un nuevo problema. 

### **4.3. Implementación de microservicios** 

En primer lugar, una gran parte de lo que hace que la separación en ámbitos para microservicios sea tan útil es que los ámbitos delimitados tratan explícitamente de ocultar información. 

Esto lo que presenta un límite para el sistema más amplio, al tiempo que oculta la complejidad interna que puede cambiar sin afectar a otros componentes del sistema. 

Esto significa que cuando seguimos un enfoque de separación en ámbitos, nos demos cuenta o no, también estamos adoptando la ocultación de información y, como hemos visto, esto es vital para el funcionamiento de los microservicios. 

En segundo lugar, el enfoque en definir una implementación común es de gran ayuda cuando se trata de definir puntos de entrada a los microservicios. Nos ayuda a crear de forma fácil interfaces API para nuestro sistema. 

Dada esta separación de ámbitos, se reduce la cantidad de sitios en nuestro código que necesitamos modificar para realizar un cambio y nos permite implementar ese cambio rápidamente en todo el sistema. 

Esto a su vez, ayuda a generar facilidad y rapidez para los desarrolladores de nuestro software y genera una mayor comunicación entre la entrega final, el desarrollo de productos y los usuarios que la usarán. 

156 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **4.4. Microservicios sin estado vs microservicios con estado** 

Cada microservicio puede ser sin estado o con estado. Un sistema que utiliza microservicios normalmente tiene una aplicación web o móvil sin estado que utiliza servicios sin estado o con estado. 

Los microservicios sin estado no mantienen ningún estado dentro de los servicios a través de las llamadas. Reciben una solicitud, la procesan y envían una respuesta sin conservar o almacenar ninguna información de estado. Un microservicio con estado conserva el estado de alguna forma para que funcione. 

En lugar de almacenar este estado internamente, un microservicio debería almacenar información de estado externamente, en algún tipo de almacén de datos (por ejemplo, una base de datos). 

Los ejemplos de un almacén de datos para mantener el estado incluyen un sistema de administración de bases de datos relacionales (RDBMS), una base de datos NoSQL o algún tipo de almacenamiento en la nube. Mantener el estado externamente proporciona disponibilidad, fiabilidad, escalabilidad e integridad para la información del estado. 

### **4.5. Serverless: beneficios e inconvenientes** 

Las arquitecturas sin servidor permiten el desarrollo rápido de aplicaciones de software que pueden manejar varios niveles de tráfico en entornos productivos. Esta definición encaja de forma natural en el desarrollo de algoritmos de IA, utilizando este tipo de tecnologías podemos agilizar los despliegues relacionados con la analítica de datos etc. 

El término sin servidor se refiere al hecho de que los servicios informáticos se despliegan sin necesidad de gestionar o administrar servidores. Su código se ejecuta a demanda, según sea necesario. Utilizar los servicios informáticos de esta forma es similar a cómo se utiliza el almacenamiento en la nube. Cuando almacenamos en la nube, no necesitamos administrar hardware físico y no necesitamos saber dónde se almacenan los datos. Se utiliza el almacenamiento según se necesite. De manera similar, con la arquitectura sin servidor, no necesitamos contar con servidores físicos y la complejidad de cómo se gestionan o proporcionan los recursos está oculta para el usuario. 

Las aplicaciones de software / las aplicaciones de IA utilizan los recursos informáticos que necesitan. 

La arquitectura sin servidor se puede utilizar para muchos tipos de aplicaciones y procesos de software. Algunos de los tipos comunes de aplicaciones que se adaptan a una arquitectura sin servidor incluyen aplicaciones web, procesamiento de datos impulsado por eventos, tareas programadas (por ejemplo, trabajos CRON), aplicaciones móviles, chat bots y aplicaciones de Internet de las cosas (IoT). 

157 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

También es bueno para tareas de transformación de datos relacionadas con imágenes / video (por ejemplo, con fines de compresión y / u optimización), transmisiones de voz y generación de ficheros PDF. 

El siguiente diagrama muestra un ejemplo de un sistema que tiene una arquitectura sin servidor: 



Las arquitecturas sin servidor utilizan modelos de Función como Servicio (FaaS), Backend como Servicio (BaaS) para proporcionar lógica de backend para aplicaciones de software. Los dos se utilizan juntos para proporcionar la funcionalidad de la aplicación. 

Algunos de los beneficios de las arquitecturas sin servidor son: 

- Ahorro de costes. 

- Escalable y flexible. 

- Identificar y desarrollar sus productos principales. 

- Desarrollo modular. 

#### **Ahorro de costes** 

Con una arquitectura sin servidor, el código solo se ejecuta cuando es necesario. Se cobran cargos de pago por uso, ya que solo se cobra por los recursos reales que se utilizan. 

Las empresas que se trasladan a una arquitectura sin servidor reducen los costes de hardware, ya que no hay servidores ni infraestructura de red que mantener. 

158 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Además, las organizaciones no tienen que contratar personal para mantener toda esa infraestructura. Estos ahorros de costes son similares a los que las empresas podrían ahorrar al usar Infraestructura como servicio (IaaS) o Plataforma como servicio (PaaS), excepto que también hay costes de desarrollo reducidos (aprovechando BaaS) y costes de escalado (aprovechando FaaS). 

#### **Escalable y flexible** 

No se puede aprovisionar de forma insuficiente o excesiva la potencia requerida con una arquitectura sin servidor. Con ella se evita encontrarse en una situación en la que no hay suficientes servidores disponibles durante los períodos alta demanda o que hay demasiados servidores inactivos durante los períodos de poca actividad. 

La escalabilidad y flexibilidad de las arquitecturas sin servidor permite que la capacidad aumente y disminuya a medida que cambia la demanda. Solo se usa la capacidad que se necesita y se cobra por la cantidad que se usa. 

La no utilización de capacidad se mantiene al mínimo y, como resultado, las empresas tienen costes reducidos. 

#### **Identificar y desarrollar sus productos principales** 

Otra de las principales ventajas de utilizar una arquitectura sin servidor es que no hay servidores que administrar. Esto permite a las empresas centrarse en crear soluciones y crear más funcionalidad. 

No tener que administrar una infraestructura aumenta la productividad y reduce el tiempo de desarrollo. 

Incluso un pequeño equipo de desarrolladores puede comenzar a construir una aplicación e implementarla en producción con relativa rapidez porque no necesitarán aprovisionar una infraestructura por adelantado y no tendrán tampoco que administrarla después de la implementación. 

Un equipo de desarrolladores que quiera construir una aplicación rápidamente sin preocuparse menos por cuestiones operativas verá grandes ventajas al usar una arquitectura sin servidor. 

#### **Desarrollo modular** 

Una arquitectura sin servidor permite el desarrollo modular. Los equipos de desarrollo tienen la capacidad de seleccionar los mejores lenguajes y tiempos de ejecución en función de la funcionalidad requerida. 

159 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

También les da a los equipos la oportunidad de probar y testear fácilmente con diferentes tecnologías. Aunque existen limitaciones en cuanto a qué idiomas están disponibles, los proveedores de la nube están ampliando su selección para que se puedan usar diferentes lenguajes para las diferentes funciones que se están desarrollando actualmente en el mercado. 

### **4.6. Enfoque híbrido con serverless** 

El uso de una arquitectura sin servidor para software no tiene por qué ser un enfoque de adopción completo. Además de las nuevas aplicaciones que aprovechan completamente la arquitectura sin servidor, se puede optar por diseñar una parte del sistema con una arquitectura sin servidor y utilizar un diseño de arquitectura diferente para las otras partes de su sistema. 

Por ejemplo, una organización puede optar por adoptar un enfoque híbrido y crear algunas funciones nuevas para una aplicación existente en un entorno sin servidor y otras utilizarlas con otros entornos de arquitectura. 

Podemos encontrar los siguientes casos de uso en los que puede ser una buena idea replantear la estrategia para ver si es viable implementarlos como arquitectura sin servidor. 

Algunos de estos casos podrían ser: 

- Transformaciones muy grandes sobre datos. 

- Aplicaciones web y móviles. 

- Suscripción a colas JMS externas. 

- Suscripción a eventos en otros sistemas externos como Salesforce Platform Events. 

- Ingestas de datos muy grandes. 

- Analítica masiva de datos. 

Estos son solo algunos casos de uso en los que crear una solución sin servidor puede ser más tedioso y complejo que usar una herramienta o conector existente que no sea sin servidor. 

Sin embargo, eso no significa que se deba abandonar la arquitectura sin servidor. Existen alternativas híbridas para una variedad de casos de uso en los que no es posible implementar al 100% arquitecturas sin servidor, pero que nos permiten aprovechar muchos de sus beneficios. 

160 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **4.7. Introducción Function as a Service (FaaS)** 

En una arquitectura sin servidor, una pequeña parte de código, como una función, se puede ejecutar utilizando una parte efímera de recursos para producir un resultado. Esto se conoce como Función como Servicio (FaaS). 

Por efímero nos referimos a que solo durará un tiempo limitado. El código se ejecuta en un contenedor que se activa en la invocación y luego se vuelve a desactivar cuando se completa. 

Las funciones se invocan normalmente debido a eventos o solicitudes HTTP. Cuando una función completa su procesamiento, puede devolver un valor al usuario que la invocó o pasar el resultado a otra función que se invocará como parte de un proceso de trabajo. 

La salida puede estar estructurada, como un objeto de respuesta HTTP, o no estructurada, como una cadena o un entero. 

Cada función debe seguir el principio de responsabilidad única (SRP) y cumplir un propósito único y bien definido. Los desarrolladores pueden programar funciones para realizar la lógica del lado del servidor y luego cargar el código a su proveedor de servicios para su ejecución bajo demanda. 

FaaS facilita enormemente pasar de programar código en un ordenador a ejecutarlo en la nube. 

Las funciones deben diseñarse para que sean inalterables, de modo que varias ejecuciones de la misma solicitud produzcan el mismo resultado, y si la misma solicitud se procesa más de una vez, no debería haber efectos no contemplados. 

Pueden existir copias de mensajes en varios servidores para proporcionar redundancia y alta disponibilidad. Para garantizar la entrega al menos una vez, es posible que una función se invoque más de una vez. 

Por ejemplo, un servidor con una copia de un mensaje puede dejar de estar disponible cuando se recibe o elimina un mensaje, lo que hace que el mismo mensaje se envíe nuevamente a una función. 

Las funciones en FaaS pueden ser síncronas o asíncronas, según las necesidades del programa. Una de las formas en que funcionan las funciones asíncronas en FaaS es que la plataforma devolverá un identificador único que luego se puede usar para monitorizar el estado de la operación asíncrona. 

Una parte importante de una arquitectura sin servidor es su puerta de enlace API. Una puerta de enlace API es el punto de entrada a un sistema. 

161 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Es un servidor HTTP que toma peticiones de clientes y usa su configuración de enrutamiento para redirigirlas al contenedor que aloja dicha funcionalidad relevante. 

Las funciones se ejecutan en contenedores y no deben tener estado. El resultado de la función FaaS se envía de vuelta a la puerta de enlace API y finalmente se devuelve al cliente como una respuesta HTTP. 

Las implementaciones de FaaS están disponibles a través de los diferentes proveedores como Amazon Web Services Lambda, Microsoft Azure Functions, Google Cloud Functions e IBM Cloud Functions. 

### **4.8. Introducción a Service Mesh y tipos** 

Los microservicios pueden ser complejos y difíciles de administrar, pero hay una solución que podemos utilizar para este problema. 

Service Mesh (o mallas de servicio) nos ayudarán a controlar las interacciones entre los servicios de una aplicación. Analizaremos qué es un Service Mesh y cómo funciona con Istio, un Service Mesh de código abierto que sirve para administrar y proteger microservicios. 

El uso masivo de contenedores y de la nube han expandido la naturaleza distribuida de las aplicaciones y han complicado aún más la capacidad de los equipos de desarrollo para comprender y controlar las interacciones entre los servicios dentro de estos entornos. 

Estas complejidades han dado lugar a una nueva solución denominada malla de servicios. Una malla de servicios es una interfaz programable que nos permite analizar, proteger y conectar microservicios. No establece conectividad entre microservicios, sino que tiene políticas y controles que se aplican sobre una red existente para gestionar cómo interactúan los microservicios. 

Por lo general, una malla de servicios es independiente del lenguaje de la aplicación y se puede aplicar a aplicaciones existentes, por lo general con pocos o ningún cambio de código. Una malla de servicios traslada las responsabilidades de implementación fuera de la aplicación y las traslada a la red. Esto se logra modificando el comportamiento y controles dentro de la aplicación que luego se aplican a la red. 

Así es como se implementan funciones como la recopilación de métricas, el análisis de la comunicación y la comunicación segura sin cambiar las aplicaciones en sí. Como hemos indicado anteriormente, una malla de servicios es una interfaz programable. Esto significa que se pueden implementar sus funciones, y la malla se asegurará de que sus funciones declaradas se apliquen a los servicios y la red. Una malla de servicios simplifica el código de la aplicación, lo que facilita la escritura, el soporte y el desarrollo al eliminar la lógica compleja que normalmente se debe incluir en la propia aplicación. Finalmente, una malla de servicios permite innovar más rápido al desarrollar software. 

162 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

### **4.9. Introducción a Istio** 

Istio es una implementación de malla de servicios estable que permite desglosar la complejidad de las implementaciones nativas de la nube distribuidas al eliminar la funcionalidad compleja del código de la aplicación y trasladarla a la red. 

Istio actualmente es considerado el más completo en funcionalidad y también está diseñado para servir a los casos de uso empresarial más parecidos a los que vemos en nuestro día a día. 



Tiene características que permiten administrar una red para servicios implementados con comunicación segura, monitorización, balanceo de carga basado en versiones y mucho más. 

Funciona con aplicaciones nativas de la nube modernas porque requiere pocos o ningún cambio de código con la integración automática de un proxy que intercepta todo el tráfico de red entre servicios. 

La gestión individual de cientos, si no miles, de proxys sería difícil de manejar. El control plane de Istio proporciona una API declarativa para definir las configuraciones y políticas de sus servicios, que luego se propagan a los proxys secundarios con las configuraciones adecuadas por el control plane de Istio. 

Además, Istio permite centrarse en resolver problemas comerciales porque la implementación más propensa a errores se elimina del código de la aplicación. 

La malla de servicios de Istio tiene características que simplifican el problema de tener que resolver estos desafíos, incluidos los siguientes: 

- Métricas automáticas y monitorización de red recopilados entre servicios dentro de la malla, así como comunicación de red entrante y saliente con clientes y servicios externos. 

- Control y enrutamiento de tráfico avanzado basado en reglas con balanceo de carga automático para tráfico HTTP, gRPC, WebSocket y TCP en todas las versiones de servicio. 

- Gestión automática de mTLS para una comunicación segura de servicio a servicio, mediante una potente autenticación y autorización basadas en control de identidades. 

- Comunicación de servicio incorporada con reintentos, activación de caída del sistema y tolerancia a errores. 

163 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Ahora, profundizaremos en las características clave de Istio y analizaremos de forma básica de cómo está diseñado. 

Con esto tendremos un mayor conocimiento básico de la arquitectura de Istio y nos ayudará a comprender como se comunican con el control plane de Istio que afecta el comportamiento dentro de la malla. Algunas de las ventajas genéricas de Istio podrían agruparse en: análisis, gestión del tráfico y seguridad. 

#### **Análisis** 

Simplemente instalando Istio y agregando servicios a la malla, nos ayudará a obtener un seguimiento, monitorización y registro completo para nuestros servicios. 

Este nivel de información nos proporciona rápidamente información sobre los flujos de comunicación entre sus servicios, así como el rendimiento, la seguridad y otros problemas que podrían afectar a esa comunicación. 

Toda esta información importante podremos verla con paneles personalizados de Grafana, así como con otras herramientas útiles que proporciona Istio, como Jaeger para los flujos de seguimiento y Kiali para obtener vistas personalizadas del tráfico de red. 

Istio recopila esta información de manera automática de los diferentes servicios. Esta información nos informa sobre las áreas dentro de la malla en las que es posible que deba aplicar políticas específicas usando las APIs del control plane de Istio. 

El control plane de Istio proporciona detalle sobre la plataforma, lo que permite definir políticas para obtener un control detallado sobre las interacciones de los servicios. También nos permite ver inmediatamente los resultados dentro de los paneles de Grafana y Kiali. 

#### **Gestión del tráfico** 

Al usar reglas fáciles de configurar, Istio proporciona un control detallado sobre cómo fluye el tráfico entre los servicios tanto en la capa de aplicación como en el nivel de la dirección IP de la red. 

Por ejemplo, los Kubernetes tienen un balanceo de carga por turnos en todos los puntos finales de servicio. Con Istio se organizan los puntos finales de servicio por versión y se declaran políticas con el control plane para controlar el balanceo. 

Además, también se pueden tomar decisiones sobre qué servicio usar, en función de una gran cantidad de condiciones, incluida la identificación del cliente de origen, el tipo de entrada del cliente, la geografía, etc. 

164 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Usando estas reglas para controlar el flujo de tráfico, se puede ajustar fácilmente el tráfico a medida que cambian las condiciones dentro de la aplicación. 

El uso de las funciones de gestión del tráfico de Istio permite realizar cambios más rápidamente porque se reducen los riesgos de entrega. Istio permite la implementación controlada de cambios utilizando varios patrones de implementación, como porcentajes, pruebas entre puntos y más cosas. 

La compatibilidad con la gestión del tráfico de Istio también incluye funciones que aumentan la estabilidad de su aplicación sin tener que cambiar el código. 

Por ejemplo, con microservicios distribuidos, es más probable aparezcan fallos de red entre llamadas de servicio o tiempos de espera altos entre llamadas de servicio. 

Esto da como resultado una mala experiencia del usuario. Istio permite establecer condiciones que controlan cómo los servicios se recuperan de fallos en esas peticiones de servicio, como tiempos de espera y reintentos. 

Las funciones de monitorización del tráfico de Istio, junto con las decisiones automatizadas, hacen que sea mucho más sencillo programar una mayor estabilidad y controlar los procesos directamente en la red de su malla de servicio. 

#### **Seguridad** 

Una de las características más difíciles de implementar en una aplicación en la nube es la comunicación segura entre servicios donde existe cifrado de datos y autenticación entre los servicios. 

Esto es un gran motivo por el que implementar dicha lógica en cada servicio es complicado y solo se necesita una configuración incorrecta para crear una amenaza de seguridad. 

Istio proporciona una función que establece automáticamente un canal seguro entre servicios mediante la gestión de identidades de servicio, certificados y protocolo de enlace mTLS. Istio utiliza una identidad de servicio de alto nivel, similar a una cuenta de servicio de Kubernetes, para determinar la identidad del servicio. 

Esto significa que podemos asegurar canales seguros entre los servicios con certificados que se generan y rotan constantemente, lo que reduce drásticamente las posibles amenazas de seguridad entre servicios. 

Al igual que con todas las funciones de Istio, la gestión de la seguridad entre servicios también es implementable utilizando las API disponibles en control plane de Istio. 

Permitir una comunicación segura dentro de la malla no es un escenario que haya que configurar completamente. Istio tiene configuraciones que permiten canales seguros que son más permisivos entre servicios. 

165 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Los canales permisivos hacen que sea conveniente agregar servicios a la malla de manera incremental sin causar fallos en la aplicación. Esta función simplifica la transición hacia la nube. 

### **4.10. El camino a las aplicaciones alojadas en la nube. Red Hat Openshift.** 

Las empresas tienen diferentes prioridades a la hora de realizar la transformación digital. Algunas modernizan la arquitectura y la infraestructura de sus aplicaciones existentes al mismo tiempo que adoptan principios modernos nativos de la nube, mientras que otras innovan con nuevos modelos y aplicaciones empresariales. 

Independientemente de la intención y del caso de uso comercial, todas comparten los mismos objetivos: mayor velocidad, flexibilidad y preparación digital. Los casos prácticos más comunes de las aplicaciones nativas de la nube se pueden clasificar, a grandes rasgos, en las siguientes cuatro categorías comerciales: 



Fuente: <u>https://www.redhat.com/</u> - Cloud native apps 

Algunas empresas pueden centrarse únicamente en un caso práctico nativo de la nube, mientras que otras pueden priorizar varios casos al mismo tiempo. Ya sea que adopte un enfoque evolutivo o revolucionario, su camino es sumamente individual y no necesariamente lineal. Con independencia del rumbo, comercializar aplicaciones con mayor rapidez requiere la tecnología, las prácticas DevOps y la cultura correctas. 

Por ende, el uso de microservicios u otro tipo de herramientas de empresas como Red Hat acelera los flujos de trabajo de IA / ML y la entrega de aplicaciones inteligentes. Red Hat OpenShift permite la autogestión de los servicios en cloud de AI / ML, además de tener un control de proceso de múltiples fases (ML Lifecycle). Esto liga directamente el mundo de los microservicios con la explotación de la información para generación de algoritmos de IA. ML Lifecycle permite obtener beneficios de grandes volúmenes y variedad de datos mediante el uso de herramientas de aprendizaje automático de código abierto para crear aplicaciones inteligentes. 

166 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

En un nivel alto, hay cuatro pasos en el ciclo de vida de los datos que los microservicios respetan e incluso aceleran a la hora del trato de información: 

- Reunir y preparar datos para asegurarse de que los datos de entrada estén completos y de alta calidad. 

- Desarrollar el modelo, incluido el entrenamiento, las pruebas y la selección del modelo con la mayor precisión de predicción. 

- Integrar modelos en el proceso de desarrollo de aplicaciones e inferencias. 

- Supervisión y gestión de modelos para medir el rendimiento empresarial y abordar la posible deriva de datos de producción 



Fuente: <u>https://cloud.redhat.com/learn/topics/ai-ml</u> 

**¿Por qué utilizar entonces contenedores y Kubernetes para sus iniciativas de aprendizaje automático?** 

Los contenedores y Kubernetes son clave para acelerar el ciclo de vida del aprendizaje automático, ya que estas tecnologías brindan a los científicos de datos la agilidad, flexibilidad, portabilidad y escalabilidad que tanto necesitan para entrenar, probar e implementar modelos de aprendizaje automático. 

Red Hat OpenShift es una de las plataformas de nube híbrida de Kubernetes y contenedores más extendidos. Proporciona todos estos beneficios y, a través de las capacidades de DevOps integradas (por ejemplo, OpenShift Pipelines, OpenShift GitOps y Red Hat Quay) y la integración con aceleradores de hardware, permite una mejor colaboración entre los científicos de datos y los desarrolladores de software, y acelera el despliegue de aplicaciones inteligentes en la nube híbrida (centro de datos, borde y nubes públicas). 

Además de lo mencionado hasta aquí, es importante en este punto conocer los desafíos a los que se enfrentan hoy en día todos los científicos de datos en el uso combinado de herramientas para el trabajo con contenedores en el mundo de la IA y el Big Data. Como ya se ha estudiado, los científicos de datos son los principales responsables del modelado de ML. Esto implica que el modelo seleccionado continúe brindando la mayor precisión de predicción. Durante la ejecución de esta tarea existen una serie de toma de decisiones clave: 

167 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- Selección e implementación de forma óptima/correcta de las herramientas de ML adecuadas. Hablamos por ejemplo Apache Spark, Jupyter notebook, TensorFlow o PyTorch entre otras. 

- Aparición de problemas que aumenten el tiempo necesario para entrenar, probar, seleccionar y volver a entrenar el modelo de ML para generar la mayor precisión de predicción posible. 

- Falta de aceleración hardware que deriva en una ejecución lenta de tareas de modelado e inferencia. 

- Falta de independencia de los equipos y recursos de IT para aprovisionar y administrar la infraestructura utilizada. 

- Colaboración con ingenieros de datos y desarrolladores de software con el fin de garantizar un filtrado correcto de los datos de entrada para llevar a cabo una implementación exitosa del modelo ML durante el desarrollo de aplicaciones. 

Con el fin de resolver estos puntos es por lo que el avance en el uso de IA se encuentra estrechamente ligado al uso de Contenedores como plataforma de despliegue de diferentes tipos de herramientas para el desarrollo de aplicaciones de esta naturaleza. 

### **4.11. Red Hat OpenShift Data Science** 

Este servicio en cloud es una herramienta orientada para ser utilizada por científicos de datos y desarrolladores de aplicaciones. Se trata de un espacio aislado totalmente compatible en el desarrollar, entrenar y probar rápidamente modelos de aprendizaje automático (ML) en la nube pública antes de implementarlos en producción. Sus principales garantías: 

- Uso de contenedores para facilitar el tratamiento de los datos. 

- Imágenes /versiones portables y creadas de forma segura de los modelos Los contenedores facilitan la ciencia de datos. 

- Integración con herramientas de aprendizaje automático de diferentes compañías. 

- Probado y comprobado con Operate First. 

168 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



Para mayor comprensión del apartado visitar: 

<u>https://www.youtube.com/watch?time_continue=1&v=joK89xYeuUY&feature=emb_logo</u> 

En definitiva y materializando los beneficios que los contenedores aportan al desarrollo de aplicaciones con ML, vemos como empresas como Red Hat mediante su plataforma OpenShift garantizan una serie de avances en el uso de IA. 

- **Una experiencia de autoservicio de recursos para científicos de datos en la plataformas cloud.  (que liga directamente con lo estudiado en apartados anteriores del capítulo).** 

   - Capacidad de los propios científicos de datos para contar con la flexibilidad y la portabilidad necesarias a la hora de usar las herramientas de aprendizaje automático en contenedores elegidos para crear, escalar, reproducir y compartir modelos de aprendizaje automático rápidamente. 

   - Posibilidad de acceso a las herramientas de ML más relevantes a través de los operadores de Kubernetes certificados por Red Hat para la opción de servicio en la nube autogestionado y de IA. 

   - Se elimina la dependencia de responsables IT para aprovisionar infraestructura durante la ejecución de tareas de modelado de ML iterativas y con uso intensivo de cómputo. 

   - Desaparece cualquier tipo de “bloqueo” con cualquier proveedor de nube en particular y su menú de herramientas ML. 

   - Existencia de una estrecha integración con las herramientas de CI/CD que permite que los modelos de ML se implementen rápidamente de forma iterativa, según sea necesario. 

169 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- **Ejecución acelerada de los trabajos de modelado e inferencia de ML más intensos en cuanto a los recursos con más consumo de cómputo.** 

   - El poder tener una integración directa con aceleradores de HW como pueden ser las GPUs NVIDIA a través de un operadores de GPU certificados implica que se podrán cumplir sin problemas con altos requisitos de recursos informáticos. Esto servirá de ayuda a la hora de seleccionar el mejor modelo de ML, el que proporcione la mayor precisión de predicción, así como para la consecución de trabajos de inferencia de ML a medida que los modelos pueden experimentar con datos en producción. 

- **Agilidad en la creación de aplicaciones inteligentes.** 

   - La combinación con capacidades de automatización y el ciclo de vida de ML permite la colaboración entre científicos de datos, desarrolladores de software y operaciones de TI para que los modelos de ML puedan integrarse rápidamente en el desarrollo de aplicaciones inteligentes. Esto ayuda a aumentar la productividad y simplificar la gestión del ciclo de vida de las aplicaciones inteligentes impulsadas por ML. -En el Módulo VII en relación a la dirección de proyectos de IA se profundizará más en este tipo de herramientas de automatización. 

   - Este tipo de tecnología permite además un desarrollo continuo e iterativo de aplicaciones inteligentes impulsadas por modelos ML. 

   - Uso de repositorios de imágenes para crear versiones de imágenes de contenedores de modelos y microservicios. 

### **4.12. Actividad complementaria. Contenedores y NPL** 

Para la realización de este caso práctico es necesario el registro mediante la cuenta de estudiante proporcionada por CEUPE en la página web de RedHat. Acceso mediante el siguiente link: <u>https://n9.cl/practicaods_mia</u> 

En esta práctica individual se busca la familiarización de los estudiantes con las herramientas mencionadas a lo largo del módulo. Se utilizarán recursos públicos de RH para ello. Este caso práctico no requiere de entrega de material por parte del alumno pero su ejecución es altamente recomendada para superar el cuestionario del Módulo así como para una mayor comprensión del temario. Se trata de una práctica guiada en la que se simulará que cada estudiante es un empleado junior para el departamento de transporte de una ciudad. Se le ha asignado el trabajo de procesar posibles problemas de reparación de autobuses que los conductores han notado durante sus turnos. Para mantener los problemas de reparación organizados y visibles, debe aprender a categorizarlos. 

170 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

Para el desarrollo de la práctica se empleará el mencionado Red Hat OpenShift Data Science, que le proporcionará las herramientas a los alumnos así como los pasos necesarios para hacer posible el objetivo. 

A continuación se exponen los pasos previos a realizar antes de la ejecución de la tarea: 

Debe acceder a la siguiente pantalla: 



1. Completar el Registro 





171 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



2. Tras la verificación de su correo electrónico automáticamente podrá acceder a los recursos proporcionados por RedHat para la ejecución de la práctica guiada. 

La página para realizar dicho acceso sin utilizar el correo de verificación es la siguiente: <u>https://n9.cl/practicaods2_mia</u> 

Clickar en el siguiente botón: 



3. Realizar los pasos guiados del manual. 



172 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

- Paso 1: Iniciar el entorno Jupyter 

- Paso 2: El entorno de Jupyter. Familiarización. 

- Paso 3: Notebooks. 

- Paso 4: Envío de reparaciones de autobuses usando NLP. 

- Paso 6: Empaquetar la aplicación. 

- Paso 7: Prueba de la aplicación. 

Desarrolle una breve memoria de la práctica así como una conclusión de cómo el uso de NLP se ha agilizado gracias al uso de la plataforma RedHat Openshift. 

173 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

## **Conclusiones** 

Las estrategias de cloud híbrida y multicloud ofrecen a las organizaciones la precisión para poder disponer de numerosos servicios (desde la externalización completa de la infraestructura, a la gestión de una infraestructura propietaria, etc.) de manera eficiente y efectiva. En concreto y aterrizando la temática específica del módulo, aquellos servicios, herramientas y catálogos relacionados con la IA. La planificación y adopción de una estrategia cloud implica la existencia de, servicios aprovisionados por proveedores de cloud pública, como AWS, Google, IBM u otros, conviviendo y colaborando para el óptimo funcionamiento IT de una empresa. Automatización, portabilidad y abstracción en la actividad son el fundamento de esta estrategia. 

La adopción de una estrategia de modernización IT está ligada a la rápida evolución de las cargas tradicionales, casuística en concreto de la IA. Nuevas aplicaciones se optimizan con el uso de heterogéneas infraestructuras propiedad de empresas proveedoras de servicio. El nuevo modelo de cloud computing es un aliado que aborda las diferentes casuísticas en que muchas empresas se han visto inmersas durante sus procesos de transformación digital. La elección de dónde se alojan los sistemas de la compañía se ha convertido en una decisión crítica para acelerar el negocio de toda industria. Existe el común denominador a la hora de iniciar esta estrategia: 

#### • **Modernizar workloads** . 

Las infraestructuras tradicionales son igualmente válidas a las cloud privadas y públicas para aportar agilidad, flexibilidad y rentabilidad a la hora de gestionar cargas tradicionales.  Aportar automatización y convivencia de entornos en los cuales gestionar y alojar estas cargas es una motivación en la adopción de una estrategia multicloud. (Entornos VMWARE, cargas Oracle, SQL Server, KVM, HyperV…) 

- **Transformar hacia nueva generación de aplicaciones** 

La infraestructura requerida para soportar análisis de información con un alto rendimiento, junto a la opción de aprovechar los recursos de comunidades Opensource que ponen a disposición de los usuarios, requiere de posibilidad de convivencia de clústeres de un tamaño muy variable con el uso de plataformas de despliegue creadas para este tipo de aplicaciones. Hablamos de cargas relacionadas con basas de datos NoSQL como MongoDB o Cassandra, entornos como Hadoop e interfaces como Kibana. Las capacidades multiprotocolo y flexibilidad en el uso de la infraestructura requeridas cuadran con los requisitos de portabilidad que el cloud computing en su modalidad multicloud implica. Esto aplica de igual norma a la movilidad y desarrollo de aplicaciones Cloud Native que se benefician de tecnologías de automatización en el despliegue como Openstack, Openshift o LXD. 

174 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

#### • **Evitar el vendor lockin** 

Capacitar a las organizaciones de poder migrar de un proveedor de cloud a otro (incluso llegando a iterar con despliegues locales), por ejemplo, servicios de infraestructura, sin coste ni disrupción alguno en su actividad es prioritario para las empresas. Poder recurrir a recursos de forma cíclica y bajo demanda sin ningún tipo de penalización se ha convertido en la base a la hora de seleccionar los recursos y servicios con lo que llevar a cabo esta estrategia multicloud. 

La era del cloud computing está evolucionando la forma en la que las compañías hacen provisión de recursos IT, de cómo diseñan, desarrollan y ejecutan aplicaciones. La virtualización como concepto genérico y el pago por uso se han convertido en una máxima en la adquisición de sistemas y servicios. Es por ello por lo que la oferta en el mercado de los proveedores cloud cada vez es más variado en cuanto a esquemas de arquitectura ofertada, servicios de gestión e incluso precios. Especialmente de los entornos cloud híbridos dinámicos en los que tanto requisitos de usuario como parámetros de despliegue pueden ser variables. Es importante contar con una buena estrategia en torno al cloud brokering, para así , contar con las herramientas necesarias para la optimización y uso óptimo de los recursos que brindan cada uno de los diferentes proveedores de cloud. En combinación a formación técnica especializada en servicios, los gestores globales de la infraestructura cuentan con herramientas como Ansible y Terraform para controlar y automatizar todos los componentes de un entorno multicloud como un único recurso; infraestructura como código. Con todo esto, y sin olvidar a los aún implementados y extendidos entornos legacy (infraestructura on premises), desarrollar la estrategia multicloud más flexible y beneficiosa en cada momento gracias a la amplia oferta de servicios de diferentes proveedores cloud, se ha convertido en la apuesta de multitud de empresas. Tanto la visión de localización como el uso de tecnologías flexibles para el desarrollo de IA mediante herramientas de NPL, por ejemplo, son hoy en día una de las prioridades para muchas empresas a la hora de modernizar sus negocios desde el IT. 

175 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

## **Anexo. Soluciones actividades fortalecimiento** 

#### **Actividad 1** 

Asocia los términos con sus respectivas definiciones aprendidas en de este módulo en relación con los entornos multicloud. 

|Vendor lockin|Garantizar la portabilidad de aplicaciones sea cual sea<br>su naturaleza (B)|
|---|---|
|Flexibilidad|Modelo de despliegue de cloud computing donde<br>infraestructura, y los recursos de computación son de<br>uso exclusivo del cliente (E)|
|SLA|Posibilidad de migrar de un proveedor de cloud a<br>otro sin coste ni disrupción algunos en la actividad<br>empresarial (A)|
|Nube pública|Modelo de despliegue de cloud computing donde<br>infraestructura, y los recursos de computación son de<br>uso compartido entre clientes (D)|
|Nube privada|Definición de un nivel de servicio/acuerdo/ política<br>para automatizar el movimiento de cargas entre<br>diferentes entornos (C)|



#### **Actividad 2** 

Utilizando los términos indicados, completa las siguientes afirmaciones relacionadas con los retos y beneficios de la implantación de un entorno multicloud. 

|Capacitación<br>Automatización|Planificación|Competitividad|Monitorización|
|---|---|---|---|



1. El objetivo de implantar una infraestructura multicloud es aumentar la …………… (D) del negocio mejorando, entre otras cosas, el consumo en resursos IT de la empresa 

176 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

2. Una correcta ……………(C) de la red es crítico para garantizar un nivel de acceso, seguridad y rendimiento de la infraestructura. 

3. Implementar una estrategia multicloud implica un esfuerzo en la mejora y cambio de la …………. (A) del personal, ya sea externo o interno. 

4. Existen herramientas que permitirán la ……………(B) en el movimiento de cargas entre diferentes infraestructuras según la conveniencia para la empresa. 

5. En un entorno multicloud existe la opción de tener una ………………. (D) centralizada para considerar las diferentes infraestructuras un único recurso a gestionar. 

#### **Actividad 3** 

Investiga y arrastra/asocia cada plataforma /software de infraestructura/infraestructura en el stack correspondiente según el esquema estudiado en este módulo. 



177 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 



#### **Actividad 4** 

Indica si son verdaderas o falsas las siguientes afirmaciones. 

1. Evitar el vendor lockin no evita una penalización alguna en el uso de servicios y plataformas e infraestructuras bajo necesidad (F). 

2. La figura del Cloud Broker tiene conocimientos para optimizar la ubicación de aplicaciones y uso de plataformas (V) 

3. Por lo general, servicios como las suites de ofimática y aplicaciones críticas para el negocio requieren los mismos requisitos. Por lo que se pueden utilizar exactamente los mismos recursos IT (F) 

4. Terraform implica una visión global de infraestructura como código. Por ello, la gestión global de toda la infraestructura se simplifica (V) 

5. El departamento IT de las empresas cada vez está más alineado con las necesidades del negocio, por lo que la externalización de servicios se suma a la externalización de infraestructura (V) 

178 

**Módulo. IA en la Era del Cloud Computing** 

**Centro Europeo de Postgrado** 

## **Bibliografía** 

- <u>https://cloud.redhat.com/learn/topics/ai-ml</u> 

- <u>https://aws.amazon.com/es/big-data/datalakes-and-analytics/?nc1=h_ls</u> 

- <u>https://aws.amazon.com/es/machine-learning/?nc2=h_ql_sol_use_ml</u> 

- <u>https://developers.redhat.com/</u> 

- <u>https://opendatahub.io/</u> 

- <u>https://cloud.google.com/solutions/ai</u> 

- <u>https://cloud.google.com/solutions/contact-center</u> 

- <u>https://www.bbc.co.uk/blogs/internet/entries/8673fe2a-e876-45fc-9a5f203c049c9f9c</u> 

- <u>https://www.infoq.com/podcasts/bbc-aws-lambda-react-cicd/</u> 

- <u>https://azure.microsoft.com/es-es/overview/ai-platform/#overview</u> 

179 







**CEUPE** Centro Europeo de Postgrado 

**Web** 

www.ceupe.com 

**E-mail** info@ceupe.com 

