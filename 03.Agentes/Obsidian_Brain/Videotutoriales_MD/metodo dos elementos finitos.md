---
tags:
  - pdf_extraido
  - videotutoriales_f
original_path: "F:\VIDEOTUTORIALES\Rotura_Presa_HEC_RAS_e_IBER_y_Model_Flujo_No_Permantente_\06. Rotura Presa HEC-RAS e IBER y Model. Flujo No Permantente\DATA\Flujo No Permanente\02 Bibliografia\metodo dos elementos finitos.pdf"
---

**Índice Principal:** [[MOC_Videotutoriales_Ingenieria]]

## **MÉTODO DOS ELEMENTOS FINITOS** 

Álvaro F. M. Azevedo 

http://www.fe.up.pt/~alvaro 



Faculdade de Engenharia da Universidade do Porto 

1ª Edição Abril  2003 

Portugal 

# **Método dos Elementos Finitos** 

Álvaro F. M. Azevedo 

http://www.fe.up.pt/~alvaro 

Faculdade de Engenharia da Universidade do Porto Portugal 

1ª Edição - Abril 2003 

### PREFÁCIO 

O Método dos Elementos Finitos (MEF) apresenta actualmente um nível de desenvolvimento que permite a sua utilização pela generalidade dos projectistas de estruturas. Enquanto que no passado muitos dos utilizadores do MEF estavam também envolvidos na respectiva programação em computador, verifica-se hoje em dia que a quase totalidade dos projectistas de estruturas apenas se preocupa com a utilização do correspondente software e com a interpretação dos resultados obtidos. Devido à grande complexidade associada ao desenvolvimento de modernos programas de computador dispondo de uma interface gráfica intuitiva, o desenvolvimento de software tem sido cada vez mais restringido às empresas especializadas. Por este motivo, o utilizador programador quase desapareceu, dando lugar ao mero utilizador. Perante um problema de análise de estruturas e dispondo de um software intuitivo, é perfeitamente acessível a um projectista a obtenção de resultados credíveis, mesmo quando não tem acesso à fonte do código computacional ou quando desconhece as características do modelo que está a utilizar. Será então necessário exigir que um estudante de Engenharia atribua parte do seu tempo à aprendizagem de formulações e metodologias que na vida profissional vai certamente ignorar? Antecedendo a resposta a esta questão, apresentam-se algumas considerações. 

Para que possa dar resposta em tempo útil à necessidade de justificação da segurança de uma estrutura, um projectista que não conheça as técnicas correspondentes à formulação do MEF será tentado pela simples utilização de um qualquer software de cálculo. Uma vez que não tem acesso aos modelos que estão programados, nem tem bases para a sua compreensão, procederá à utilização do software de acordo com o treino que recebeu ou com base em sucessivas improvisações. A tentação para aceitar os resultados provenientes do programa é grande, quaisquer que sejam esses resultados, uma vez que considera que o software escolhido tem elevada qualidade. Os potenciais perigos de uma utilização nestas condições são a não percepção de eventuais erros na introdução dos dados, a ausência de correspondência entre o modelo seleccionado e a estrutura que está a ser analisada, o facto de serem desprezadas importantes condicionantes, etc. Na ausência de uma comparação dos resultados provenientes do MEF com os oriundos de outros modelos, existe o sério risco de a segurança de uma estrutura ser justificada com 

iii 

_Método dos Elementos Finitos - Prefácio_ 

base em cálculos completamente inadequados. Este facto tem sido confirmado pelo elevado número de acidentes em estruturas acabadas de construir, bem como pela grande quantidade de reparações que tem sido necessário efectuar em construções recentes. A transmissão aos alunos dos fundamentos do MEF, e também de uma introdução à correspondente programação em computador, constituem certamente factores que conduzirão os futuros projectistas a uma utilização mais segura dos softwares de análise de estruturas. 

Existe uma outra motivação para continuar a ser necessário ensinar as bases teóricas do MEF, que consiste no facto de ser fundamental preparar hoje os inovadores de amanhã. Uma vez que as ferramentas relativas à aplicação do MEF se encontram intimamente ligadas ao mundo da informática e uma vez que este apresenta uma constante e rápida evolução, é garantido que dentro de alguns anos será necessário adaptar as técnicas de análise de estruturas às plataformas de computação que nessa altura existirem. Se a actual base de conhecimentos ficar limitada a um reduzido número de pessoas, certamente que será difícil encontrar no futuro investigadores que garantam o progresso da ciência. 

Por todos estes motivos se conclui ser fundamental prosseguir com o ensino das técnicas em que se baseia a generalidade dos programas de elementos finitos. 

A principal motivação para a escrita desta publicação foi a de organizar de um modo coerente algumas das formulações em que se baseou o desenvolvimento do programa FEMIX 4.0. Apesar de já existirem versões anteriores, a actual versão do programa foi totalmente rescrita, de modo a ser possível explorar uma muito mais versátil estruturação do código computacional. Espera-se, com este empreendimento, produzir um software em que seja simples desenvolver e testar novas formulações. Por último, desejo agradecer às pessoas que se têm empenhado no desenvolvimento do projecto FEMIX e que muito contribuíram para que todos os conceitos aqui expostos apresentem uma indispensável clareza e coerência. Em particular um agradecimento àquele que esteve presente desde o início, Joaquim Barros, bem como aos entusiastas mais recentes, José Sena Cruz e António Ventura Gouveia. Agradeço também ao Luís Brás o trabalho que teve na preparação do modelo da ponte que figura na capa. 

Álvaro F. M. Azevedo - Abril 2003 

iv 

### ÍNDICE 

|1 - INTRODUÇÃO...........................................................................................................1|
|---|
|1.1 - Tipo de análise..........................................................................................................2|
|1.2 - Fundamentos do MEF...............................................................................................4|
|1.3 – Breve história do MEF.............................................................................................5|
|1.4 - Exemplo de aplicação do MEF.................................................................................6|
|2 - TRANSFORMAÇÃO LINEAR DE COORDENADAS ..........................................13|
|2.1 - Simbologia..............................................................................................................13|
|2.2 - Caso geral................................................................................................................14|
|2.3 - Caso particular com_S_e_S'_coincidentes..................................................................18|
|2.4 - Matriz de transformação de uma barra rectilínea no espaço...................................19|
|2.5 - Considerações finais ...............................................................................................27|
|3 - MÉTODO DOS DESLOCAMENTOS EM TRELIÇAS E PÓRTICOS...................29|
|3.1 - Simbologia..............................................................................................................29|
|3.2 - Referenciais.............................................................................................................31|
|3.3 - Graus de liberdade ..................................................................................................32|
|3.4 - Matriz de transformação .........................................................................................34|
|3.5 - Matriz de rigidez e vector solicitação .....................................................................35|
|3.6 - Assemblagem da matriz de rigidez global e do vector solicitação.........................37|
|3.7 - Introdução das condições de apoio .........................................................................41|
|3.8 - Faseamento da análise de um pórtico 3D ...............................................................44|
|3.9 - Matriz de rigidez de uma barra de treliça 3D no referencial local..........................45|
|3.10 - Matriz de rigidez de uma barra de pórtico 3D no referencial local ......................46|
|3.11 - Considerações finais .............................................................................................47|
|4 - ELEMENTOS FINITOS UNIDIMENSIONAIS ......................................................49|
|4.1 - Simbologia..............................................................................................................49|
|4.2 - Funções interpoladoras ou funções de forma..........................................................50|
|4.3 - Campo de deformações...........................................................................................54|



v 

_Método dos Elementos Finitos - Índice_ 

|4.4 - Princípio dos trabalhos virtuais...............................................................................56|
|---|
|4.5 - Matriz de rigidez e vector solicitação .....................................................................57|
|4.6 - Elemento finito unidimensional com três nós.........................................................60|
|4.7 - Elemento finito unidimensional com substituição de variável ...............................64|
|4.8 - Considerações finais ...............................................................................................70|
|5 - QUADRATURA DE GAUSS...................................................................................73|
|5.1 - Simbologia..............................................................................................................73|
|5.2 - Integração de uma função polinomial.....................................................................73|
|5.3 - Integrais múltiplos ..................................................................................................79|
|5.4 - Considerações finais ...............................................................................................81|
|6 - ESTADO PLANO DE TENSÃO ..............................................................................83|
|6.1 - Simbologia..............................................................................................................83|
|6.2 - Funções interpoladoras ou funções de forma..........................................................85|
|6.3 - Campo de deformações...........................................................................................90|
|6.4 - Princípio dos trabalhos virtuais...............................................................................92|
|6.5 - Matriz de rigidez e vector solicitação .....................................................................92|
|6.5.1 - Cálculo de um elemento da matriz de rigidez......................................................95|
|6.5.2 - Cálculo do vector solicitação correspondente a uma carga distribuída ...............97|
|6.6 - Caso geral com substituição de variáveis ...............................................................99|
|6.7 - Algoritmo de cálculo da matriz de rigidez de um elemento isoparamétrico ........108|
|6.8 - Cálculo das tensões e deformações finais.............................................................112|
|6.9 - Considerações finais .............................................................................................113|
|7 - FUNÇÕES INTERPOLADORAS ..........................................................................115|
|7.1 - Simbologia............................................................................................................115|
|7.2 - Caso unidimensional.............................................................................................116|
|7.3 - Caso bidimensional...............................................................................................118|
|7.4 - Procedimento genérico para determinar as funções de forma ..............................121|
|7.5 - Elementos bidimensionais: famílias Lagrangeana e_serendipity_..........................126|
|7.6 - Propriedades das funções interpoladoras..............................................................130|
|7.7 - Interpolação Hermitiana........................................................................................132|



vi 

_Método dos Elementos Finitos - Índice_ 

|7.8 - Considerações finais .............................................................................................142|
|---|
|8 - ASSEMBLAGEM DE ELEMENTOS FINITOS....................................................145|
|8.1 - Simbologia............................................................................................................145|
|8.2 - Assemblagem da matriz de rigidez global e do vector solicitação.......................146|
|8.3 - Considerações finais .............................................................................................152|
|9 - FORÇAS NODAIS EQUIVALENTES...................................................................153|
|9.1 - Simbologia............................................................................................................153|
|9.2 - Expressões genéricas das forças nodais equivalentes...........................................155|
|9.3 - Força concentrada num ponto interior..................................................................160|
|9.4 - Carga distribuída por unidade de comprimento....................................................163|
|9.5 - Carga distribuída por unidade de superfície .........................................................170|
|9.6 - Carga distribuída por unidade de volume.............................................................170|
|9.7 - Considerações finais .............................................................................................172|
|10 - SÓLIDOS, ESTADO PLANO DE DEFORMAÇÃO E AXISSIMETRIA ..........175|
|10.1 - Simbologia..........................................................................................................175|
|10.2 - Elementos sólidos tridimensionais (_bricks_) ........................................................176|
|10.3 - Estado plano de deformação ...............................................................................184|
|10.4 - Estado axissimétrico ...........................................................................................187|
|10.5 - Considerações finais ...........................................................................................192|
|11 - FLEXÃO DE VIGAS ............................................................................................193|
|11.1 - Simbologia..........................................................................................................193|
|11.2 - Flexão composta plana........................................................................................194|
|11.3 - Considerações finais ...........................................................................................200|
|12 - VIGA DE EULER-BERNOULLI .........................................................................203|
|12.1 - Simbologia..........................................................................................................203|
|12.2 - Viga de dois nós sem substituição de variável....................................................204|
|12.3 - Viga de três nós sem substituição de variável ....................................................212|
|12.4 - Viga de dois nós com substituição de variável...................................................212|



vii 

_Método dos Elementos Finitos - Índice_ 

|12.5 - Considerações finais ...........................................................................................220|
|---|
|13 - VIGA DE TIMOSHENKO....................................................................................223|
|13.1 - Simbologia..........................................................................................................223|
|13.2 - Viga de dois nós com substituição de variável...................................................224|
|13.3 - Considerações finais ...........................................................................................237|
|ANEXO A - UTILIZAÇÃO DO PROGRAMA FEMIX 3.1 .......................................239|
|A.1 - Instalação .............................................................................................................239|
|A.2 - Preparação dos dados...........................................................................................240|
|A.3 - Execução do programa.........................................................................................245|
|A.4 - Visualização gráfica.............................................................................................246|
|A.5 - Considerações finais ............................................................................................248|



viii 

### CAPÍTULO 1 

### INTRODUÇÃO 

No âmbito da Engenharia de Estruturas, o Método dos Elementos Finitos (MEF) tem como objectivo a determinação do estado de tensão e de deformação de um sólido de geometria arbitrária sujeito a acções exteriores. Este tipo de cálculo tem a designação genérica de análise de estruturas e surge, por exemplo, no estudo de edifícios, pontes, barragens, etc. Quando existe a necessidade de projectar uma estrutura, é habitual proceder-se a uma sucessão de análises e modificações das suas características, com o objectivo de se alcançar uma solução satisfatória, quer em termos económicos, quer na verificação dos pré-requisitos funcionais e regulamentares. As técnicas descritas nesta publicação apenas correspondem à fase de análise do comportamento de uma estrutura cuja geometria, materiais e acções são a priori conhecidos. 

Nos cursos de Engenharia Civil e de Engenharia Mecânica é tradicional começar-se por ensinar a análise de estruturas limitada às vigas, pórticos, treliças e grelhas. As estruturas deste tipo recebem a designação de reticuladas, por serem constituídas por barras prismáticas cuja secção transversal apresenta dimensões muito inferiores ao comprimento do seu eixo. As estruturas não reticuladas são, em geral, estudadas como meios contínuos (e.g., paredes, lajes, cascas, sólidos). Nas estruturas reticuladas surgem já muitos conceitos que são comuns à generalidade das estruturas, tais como o de equilíbrio, compatibilidade, tensão, deformação, relação entre tensão e deformação, etc. No âmbito das estruturas reticuladas torna-se particularmente simples explicar o método das forças e o método dos deslocamentos, bem como outras técnicas que, em geral, são difíceis de estender aos meios contínuos. 

Antes do aparecimento do MEF, a análise dos meios contínuos era efectuada por resolução directa dos sistemas de equações de derivadas parciais que regem o fenómeno, tendo em consideração as necessárias condições fronteira. Para facilitar a aplicação desta técnica a problemas não elementares, era comum recorrer a séries de Fourier [1.1]. Devido à sua complexidade, estes procedimentos só eram aplicáveis a meios contínuos homogéneos e de geometria simples. Para tentar ultrapassar algumas destas limitações, era frequente a substituição de derivadas exactas por derivadas 

1 

_Introdução - Álvaro F. M. Azevedo_ 

aproximadas, calculadas com base em grelhas de pontos. Da aplicação desta técnica resulta o método das diferenças finitas, que, antes do aparecimento dos computadores, apresentava o inconveniente de requerer a resolução de grandes sistemas de equações lineares. Para evitar este inconveniente foram propostos diversos métodos de relaxação baseados na sucessiva diminuição de um conjunto de resíduos [1.1]. Devido à morosidade associada à aplicação de qualquer um destes métodos, tornava-se muito atractiva a substituição do problema real por outro semelhante, de modo a se poder recorrer a resultados publicados em tabelas ou ábacos. Com o grande desenvolvimento que o MEF teve na década de 60 [1.2] e com a banalização do recurso ao computador, passou a ser prática corrente a análise de estruturas de geometria arbitrária, constituídas por múltiplos materiais e sujeitas a qualquer tipo de carregamento. Este avanço é tão significativo que os outros métodos, atrás referidos, deixaram praticamente de ser utilizados. Actualmente, o seu interesse restringe-se ao de fornecer soluções teóricas de problemas simples para validar métodos aproximados. 

A formulação do MEF pode ser baseada no método dos deslocamentos, em modelos de equilíbrio, ou em métodos híbridos e mistos [1.3]. De todos estes métodos, aquele que apresenta uma maior simplicidade e, consequentemente, uma maior versatilidade é o método dos deslocamentos, sendo este o único que é abordado nesta publicação. Associado ao método dos deslocamentos surgem muitos conceitos que se supõe que o leitor já domina no âmbito das estruturas reticuladas, como por exemplo as noções de grau de liberdade, deslocamento generalizado, força generalizada, equilíbrio, matriz de rigidez, vector solicitação, assemblagem, introdução de condições de apoio, etc. Nesta publicação, alguns destes conceitos são de novo abordados, sendo dada particular ênfase à sua generalização aos meios contínuos bidimensionais e tridimensionais. 

### **1.1 - Tipo de análise** 

Quando surge a necessidade de resolver um problema de análise de uma estrutura, a primeira questão que se coloca é a sua classificação quanto à geometria, modelo do material constituinte e acções aplicadas. O modo como o MEF é formulado e aplicado depende, em parte, das simplificações inerentes a cada tipo de problema. Referem-se em seguida alguns aspectos que é necessário ter em consideração na fase que antecede a análise de uma estrutura. 

2 

_Introdução - Álvaro F. M. Azevedo_ 

### <u>Análise dinâmica ou estática</u> 

As acções sobre as estruturas são em geral dinâmicas, devendo ser consideradas as forças de inércia associadas às acelerações a que cada um dos seus componentes fica sujeito. Por este motivo, seria de esperar que a análise de uma estrutura teria obrigatoriamente de ter em consideração os efeitos dinâmicos. Contudo, em muitas situações é razoável considerar que as acções são aplicadas de um modo suficientemente lento, tornando desprezáveis as forças de inércia. Nestes casos a análise designa-se estática. Nesta publicação apenas são considerados problemas em que se supõem válidas as simplificações inerentes a uma análise estática. 

### <u>Análise não linear ou linear</u> 

Na análise de uma estrutura sólida, é habitual considerar que os deslocamentos provocados pelas acções exteriores são muito pequenos quando comparados com as dimensões dos componentes da estrutura. Nestas circunstâncias, admite-se que não existe influência da modificação da geometria da estrutura na distribuição dos esforços e das tensões, i.e., todo o estudo é feito com base na geometria inicial indeformada. Se esta hipótese não for considerada, a análise é designada não linear geométrica. 

É também frequente considerar que, ao nível do material que constitui a estrutura, a relação entre tensões e deformações é linear. Nos casos em que esta simplificação não é considerada, é necessário recorrer a algoritmos específicos de análise não linear material. 

Nesta publicação apenas se aborda o caso da análise linear, quer geométrica, quer material. 

### <u>Tipo de estrutura</u> 

As estruturas podem ser classificadas quanto à sua geometria como reticuladas, laminares ou sólidas. Estas últimas são as mais genéricas, sendo classificadas como sólidas as que não apresentarem características que as permitam enquadrar no grupo das laminares ou das reticuladas. 

As estruturas laminares são as que se desenvolvem para ambos os lados de uma superfície média, mantendo-se na sua vizinhança. É o caso de uma lâmina cuja 

3 

_Introdução - Álvaro F. M. Azevedo_ 

espessura é muito inferior às restantes dimensões. Quando a superfície média é plana, a estrutura laminar pode ser classificada como parede, laje ou casca plana. Uma parede apenas se encontra sujeita a acções paralelas ao seu plano médio. Uma laje pode ter aplicadas forças perpendiculares ao plano médio e momentos cujo vector está contido no plano médio. Uma estrutura laminar plana sujeita a outros tipos de acções é designada casca plana. Quando a superfície média não é plana, tem-se uma casca tridimensional. 

As estruturas reticuladas são as constituídas por barras prismáticas, cujas dimensões transversais são muito menores do que o comprimento do respectivo eixo. Neste tipo de estruturas é habitual distinguir os pórticos das treliças, conforme é ou não considerada a compatibilidade de rotações nas extremidades de barras adjacentes. 

É possível tratar com grande eficiência uma classe de problemas de análise de estruturas designados axissimétricos. Estes ocorrem quando a estrutura é um sólido de revolução e as acções são todas axissimétricas em relação ao mesmo eixo. Neste tipo de problemas é ainda possível distinguir o caso do sólido de revolução do caso da lâmina de revolução. 

Será também tratado como um caso particular a análise de uma estrutura que consiste num sólido cuja geometria a acções se repetem indefinidamente ao longo de um eixo rectilíneo. Trata-se do estado plano de deformação, que pode ser estudado com base numa geometria bidimensional. 

### **1.2 - Fundamentos do MEF** 

A formulação do MEF requer a existência de uma equação integral, de modo que seja possível substituir o integral sobre um domínio complexo (de volume _V_ ) por um somatório de integrais estendidos a sub domínios de geometria simples (de volume _Vi_ ). Esta técnica é ilustrada com o seguinte exemplo, que corresponde ao integral de volume de uma função _f_ 



4 

_Introdução - Álvaro F. M. Azevedo_ 

Em (1) pressupõe-se que 



Se for possível calcular todos os integrais estendidos aos sub domínios _Vi_ , basta efectuar o somatório correspondente ao segundo membro de (1) para se obter o integral estendido a todo o domínio. Cada sub domínio _Vi_ corresponde a um elemento finito de geometria simples (e.g., segmento de recta, triângulo, quadrilátero, tetraedro, paralelepípedo). O somatório indicado em (1) vai dar origem à operação designada assemblagem, que apresenta muitas semelhanças com a que é efectuada nas estruturas reticuladas. 

A equação integral referida no início desta secção é proveniente da aplicação do método dos resíduos pesados ou de um princípio variacional [1.3]. No caso da aplicação do MEF à análise de estruturas a formulação mais intuitiva é a que se baseia no Princípio dos Trabalhos Virtuais (PTV), sendo a única que é abordada nesta publicação. 

### **1.3 – Breve história do MEF** 

Em [1.2] encontra-se uma descrição detalhada da evolução do método dos elementos finitos ao longo do tempo. Em [1.3] é efectuado o seu enquadramento com outros métodos da mesma família. Apresenta-se em seguida apenas uma breve referência às principais fases do desenvolvimento do MEF. 

Na generalidade dos casos, é muito difícil definir a data em que determinado avanço do conhecimento foi efectuado. No caso particular do MEF, é referido por vários autores que a publicação mais antiga em que é utilizada a designação “elemento finito” é o artigo [1.4], que data de 1960 e tem como autor Ray Clough. Anteriormente eram já conhecidas algumas técnicas que vieram a ser incorporadas no MEF, sem este aparecer ainda com as principais características que hoje em dia possui. Os grandes passos do desenvolvimento do MEF, que o conduziram ao formato que actualmente apresenta maior aceitação, foram dados na década de 60 e início da de 70. Inicialmente os elementos finitos mais comuns eram os triangulares e os tetraédricos, passando-se mais tarde a dar preferência aos quadriláteros e aos hexaedros. 

5 

_Introdução - Álvaro F. M. Azevedo_ 

Ao contrário de outros métodos que eram utilizados no passado, o MEF só tem utilidade prática se se dispuser de um computador digital. Este requisito é devido à grande quantidade de cálculos que é necessário realizar, nomeadamente na resolução de grandes sistemas de equações lineares. Assim se compreende que o rápido desenvolvimento do MEF tenha praticamente coincidido com a generalização da utilização de computadores nos centros de investigação. Com a proliferação de micro-computadores ocorrida no final da década de 80 e na década de 90, o MEF chega finalmente às mãos da generalidade dos projectistas de estruturas. 

### **1.4 - Exemplo de aplicação do MEF** 

Apresenta-se em seguida um exemplo de aplicação do MEF, que consiste na análise de uma estrutura do tipo consola curta de pequena espessura, sujeita às acções indicadas na Figura 1.1. Nestas condições pode-se admitir que se trata de um meio contínuo, sujeito a um [[Analisis_Cualitativo_Evaluacion_cualitativa_del_uso_de_cuyinaza_y_eucalipto_en_comunidades_aledanas_a_Atacocha|estado plano de tensão]] [1.5]. Na Figura 1.1 está representada a malha utilizada, que é constituída por 92 elementos finitos quadriláteros, sendo cada um destes elementos definido por 8 nós. Encontram-se também assinalados os 10 nós que estão ligados ao meio exterior. 

Depois de completada a análise da estrutura pelo MEF, fica-se a conhecer os valores aproximados dos deslocamentos e das tensões instaladas. Na Figura 1.2 está representada a malha deformada pela acção das forças aplicadas à estrutura. Para permitir uma melhor visualização dos deslocamentos, estes são multiplicados por um factor de ampliação. Como referência, é também representada a malha original indeformada. 

Com o tipo de visualização utilizado na Figura 1.3 é possível ter uma percepção imediata dos locais em que as tensões principais apresentam maiores valores, bem como da trajectória das tensões dentro da estrutura. Neste tipo de representação cada segmento de recta está orientado segundo uma direcção principal de tensão e a sua grandeza é proporcional ao valor da correspondente tensão normal. A cor verde indica que se trata de uma tracção e à cor vermelha está associada uma compressão. 

Na Figura 1.4, o valor da componente vertical do vector deslocamento é representado, em cada ponto, por intermédio de uma codificação por cores. Consultando a escala 

6 

_Introdução - Álvaro F. M. Azevedo_ 

lateral, fica-se a conhecer a ordem de grandeza do deslocamento vertical em qualquer ponto da estrutura. 

Na Figura 1.5, o tipo de visualização gráfica coincide com o da Figura 1.4, tratando-se também da representação de um campo escalar por intermédio de uma codificação por cores. O campo representado na Figura 1.5 é o das tensões normais σ _y_ , sendo _y_ o eixo vertical. Esta componente do tensor das tensões é sempre perpendicular a facetas horizontais. 



Fig. 1.1 - Consola curta: malha de elementos finitos e acção exterior. 

7 

_Introdução - Álvaro F. M. Azevedo_ 



Fig. 1.2 - Consola curta: malha deformada representada sobre a estrutura indeformada. 



Fig. 1.3 - Consola curta: tensões principais e respectivas direcções. 

8 

_Introdução - Álvaro F. M. Azevedo_ 



Fig. 1.4 - Consola curta: campo de deslocamentos verticais. 

9 

_Introdução - Álvaro F. M. Azevedo_ 



Fig. 1.5 - Consola curta: campo de tensões normais segundo um eixo vertical. 

10 

_Introdução - Álvaro F. M. Azevedo_ 

### **BIBLIOGRAFIA** 

[1.1] – Timoshenko, S. P.; Goodier, J. N. - Theory of Elasticity, Third Edition, McGraw-Hill, 1988. 

[1.2] - Cook, R. D.; Malkus, D. S.; Plesha, M. E.; Witt, R. J. - Concepts and Applications of Finite Element Analysis, Fourth Edition, John Wiley & Sons, Inc., 2002. 

[1.3] - Zienkiewicz, O. C.; Taylor, R. L. - The Finite Element Method, Fourth Edition, McGraw-Hill, 1988. 

[1.4] – Clough, R. W. - The Finite Element in Plane Stress Analysis, Proc. 2nd ASCE Conf. on Electronic Computation, Pittsburgh, Pa., September 1960. 

[1.5] - Azevedo, A. F. M. - Mecânica dos Sólidos, Faculdade de Engenharia da Universidade do Porto, 1996. 

11 

_Introdução - Álvaro F. M. Azevedo_ 

12 

### CAPÍTULO 2 

### TRANSFORMAÇÃO LINEAR DE COORDENADAS 

Neste capítulo é apresentada a dedução da expressão que permite transformar as coordenadas de um ponto no espaço de um referencial ( _S_ ′ ) para outro ( _S_ ′′ ). Quer os eixos de _S_ ′ quer os de _S_ ′′ são definidos por versores cujas componentes se encontram no referencial geral _S_ . Estes três referenciais apresentam origem comum (ponto _O_ ). Sendo _P_ um ponto genérico no espaço, a transformação das componentes do vector _OP_ coincide com a transformação das coordenadas do ponto _P_ . 

### **2.1 - Simbologia** 

Apresenta-se em primeiro lugar um resumo da simbologia adoptada neste capítulo. 

Tabela 2.1 - Simbologia relativa à transformação linear de coordenadas. 

|_S_|Sistema de coordenadas (referencial)|
|---|---|
|_O_|Origem do sistema de coordenadas|
|_P_|Ponto genérico|
|_p_|Vector posição do ponto_P_|
|_x_|Eixo do sistema de coordenadas|
|_e_|Versor de um eixo do sistema de coordenadas|
|_A_|Matriz de transformação de _S_′ em _S_′′|
|_B_|Matriz de transformação de _S_′′ em _S_′|
|_g_|Referencial geral|
|_a_|Referencial auxiliar|
|_l_|Referencial local|



13 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 

|α|Ângulo entre eixos dos referenciais auxiliar e local|
|---|---|
|Τ|Matriz de transformação|
|_i_|Primeiro nó de uma barra|
|_j_|Segundo nó de uma barra|
|_L_|Comprimento de uma barra|



### **2.2 - Caso geral** 

′ ′′ Na Figura 2.1 encontram-se representados os três referenciais ( _S_ , _S e S_ ), um ponto genérico _P_ e o vector _<u>p</u>_ = _OP_ . 



<!-- Start of picture text -->
x 3 x 3 ′<br>x 3 ′′<br>P<br>e ˆ 3 ′<br>e ˆ 3 p<br>e ˆ 3 ′′<br>e ˆ 1 ′′ O e ˆ 2 x 2<br>e ˆ 2 ′<br>x 1  ′′<br>x 2 ′<br>e ˆ 1 ′ e ˆ 2 ′′<br>e ˆ 1<br>x 1 ′<br>x 2 ′′<br>x 1<br><!-- End of picture text -->

Fig. 2.1 - Referenciais e ponto genérico _P_ . 

Os três referenciais (que se supõem directos e ortonormados) são definidos do seguinte modo 

14 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 



Versores de cada referencial: 



Ponto genérico: 



Vector posição do ponto _P_ : 



Nota: todos os versores e vectores apresentam as suas componentes no referencial _S_ . 

Versores do referencial _S_ : 



Vector _<u>p</u>_ : 





′′ ′′ ′′ ′′ As coordenadas do ponto _P_ no referencial _S_ ( _x_ 1, _x_ 2, _x_ 3 ) obtêm-se projectando o vector _<u>p</u>_ sobre os versores do referencial _S_ ′′ : 

15 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 



Matricialmente tem-se: 





Nesta expressão, _<u>x</u>_ ′ são as coordenadas de _P_ no referencial _S_ ′ , _<u>x</u>_ ′′ são as coordenadas de _P_ no referencial _S_ ′′ e _<u>A</u>_ é a matriz de transformação de _S_ ′ em _S_ ′′ . 

De um modo semelhante tem-se: 



16 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 





Comparando (12) com (17) verifica-se que 



A expressão (16) pode escrever-se da seguinte forma 



Substituindo (11) em (19) tem-se 



Concluindo-se que 



sendo _<u>I</u>_ a matriz identidade. 

Multiplicando ambos os membros de (21) por _<u>A</u>_ − 1 (à direita) obtém-se 



Quando a inversa de uma matriz coincide com a sua transposta diz-se que a matriz é **<u>ortogonal</u>** . Assim se conclui que a matriz de transformação _<u>A</u>_ é uma matriz ortogonal. 

Vai-se agora proceder à análise do significado de cada um dos elementos de _<u>A</u>_ . 

A expressão (11) pode escrever-se do seguinte modo 



17 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 

. sendo _aij_ o elemento genérico da matriz _<u>A</u>_ 

Em (12) verifica-se que 



Recorrendo à definição de produto escalar tem-se 



Uma vez que os versores dos referenciais possuem norma unitária 



e a matriz de transformação _<u>A</u>_ pode ser obtida a partir dos cosenos dos ângulos entre versores dos referenciais _S_ ′ e _S_ ′′ . 



### **2.3 - Caso particular com** **_S_ e** **_S'_ coincidentes** 

Reproduzem-se em seguida as expressões (5), (11) e (12) 





No caso de os referenciais _S_ e _S_ ′ serem coincidentes, verifica-se que 

18 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 





Substituindo (31) em (30) obtém-se 



Atendendo a (28), verifica-se em (33) que a primeira linha da matriz _<u>A</u>_ contém as componentes do versor<sup>_e_ˆ</sup> 1<sup>′′noreferencial</sup><sup>_S_.Asegundaeterceiralinhascontêmas</sup> componentes em _S_ dos versores<sup>_e_ˆ</sup> 2<sup>′′e</sup><sup>_e_ˆ</sup> 3<sup>′′.</sup> 



### **2.4 - Matriz de transformação de uma barra rectilínea no espaço** 

Nesta secção são utilizadas as expressões deduzidas nas secções anteriores com o objectivo de chegar à matriz de transformação de uma barra de treliça 3D e de pórtico 3D. No âmbito da análise de estruturas pelo método dos deslocamentos, admitem-se as seguintes hipóteses: 

- é conhecida a geometria da estrutura, que é constituída por barras prismáticas de eixo rectilíneo e de secção constante; 

- para cada barra, são conhecidas as coordenadas dos dois nós extremos, ficando assim definida a localização do seu eixo baricêntrico; 

- é conhecida a posição dos eixos principais centrais de inércia da secção transversal da barra [2.1]. 

19 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 

Considere-se um ângulo ( α ), que será definido adiante e que posiciona o referencial local (principal central de inércia - PCI) em relação a um referencial auxiliar. 

Assim, vão ser considerados os seguintes referenciais: 



O referencial geral ( _g_ ) é aquele em relação ao qual todos os pontos e todos os vectores estão definidos, sendo os seus versores definidos por (28). 

O referencial auxiliar ( _a_ ), ao qual corresponde um ângulo α nulo, tem o primeiro eixo coincidente com o eixo da barra e o segundo eixo perpendicular ao plano vertical que contem a barra. O terceiro eixo é aquele que faz com que o referencial seja directo e ortonormado. Este referencial será adiante definido com mais rigor. 

O referencial local ( _l_ ) tem como primeiro eixo o eixo da barra, sendo os restantes eixos os eixos principais centrais de inércia da secção transversal da barra. 

O ângulo α define a posição do referencial local ( _l_ ) em relação ao referencial auxiliar ( _a_ ). 

Vão ser em seguida definidas duas transformações: 

- transformação de _g_ para _a_ ; 

- transformação de _a_ para _l_ . 

A primeira transformação é realizada com a seguinte expressão que é semelhante a (32) 



sendo _<u>T</u> ag_ a matriz que transforma as coordenadas de um ponto do referencial _g_ para o referencial _a_ . 

A segunda transformação permite obter as coordenadas de um ponto no referencial _l_ a partir das suas coordenadas no referencial _a_ , sendo semelhante à definida por (11) 

20 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 



Substituindo (36) em (37) chega-se a 



Uma vez que se pretende uma matriz de transformação de _g_ para _l_ 



comparando (38) com (39) conclui-se que 



Na Figura 2.2 é definida a posição do referencial auxiliar _a_ em relação ao referencial geral _g_ e à barra. 



<!-- Start of picture text -->
g  3<br>a  3<br>a 2<br>a 1<br>j<br>i<br>g 2<br>g<br>1<br>i  < j<br><!-- End of picture text -->

Fig. 2.2 - Posição do referencial _a_ em relação ao referencial _g_ . 

Em relação à Figura 2.2 considera-se ainda o seguinte: 

- o eixo _g_ 3 é vertical e orientado para cima; 

- o eixo baricêntrico da barra é definido pelos nós _i_ e _j_ ; 

21 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 

- é em geral vantajoso considerar a convenção de ser sempre _i_ < _j_ . Assim, o primeiro nó da barra é o nó _i_ e o segundo é o nó _j_ . Esta convenção clarifica todo o processo de estudo da barra sem lhe introduzir qualquer limitação; 

- o eixo _a_ 1 coincide com o eixo baricêntrico da barra, i.e., o eixo que é definido pelos centros de gravidade de todas as secções transversais da barra; 

- o eixo _a_ 1 encontra-se orientado do nó _i_ para o nó _j_ ; 

- o eixo _a_ 2 é perpendicular ao plano ( _g_ 3, _a_ 1) e está orientado de acordo com o sentido do produto vectorial entre os versores de _g_ 3 e _a_ 1; 

- o eixo _a_ 3 está contido no plano ( _g_ 3, _a_ 1) e resulta do produto vectorial entre os versores de _a_ 1 e _a_ 2; 

- desta forma o referencial ( _a_ 1, _a_ 2, _a_ 3) é sempre directo e ortonormado. 

Para se calcular a matriz de transformação de _g_ para _a_ (36) vai-se recorrer à expressão (34). Assim, a primeira linha de _<u>T</u> ag_ é constituída pelas componentes do versor _a_ 1 no referencial _g_ , e assim sucessivamente. 

O cálculo das componentes do versor _a_ 1 é feito com base nas coordenadas dos nós _i_ e _j_ . 





O comprimento da barra é calculado com a seguinte expressão 



O vector<sup>_<u>a</u>_</sup> 1<sup>,queemgeralnãotemnormaunitária,obtém-seporsubtracçãodas</sup> coordenadas dos nós _i_ e _j_ . 



O versor<sup>_a_ˆ</sup> 1<sup>obtém-se dividindo o vector</sup><sup>_<u>a</u>_</sup> 1<sup>pela respectiva norma</sup> 

22 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 



Para posterior referência, designam-se as componentes do versor<sup>_a_ˆ</sup> 1<sup>por</sup><sup>_A_1,</sup><sup>_A_2 e</sup><sup>_A_3</sup> 



Tal como foi atrás referido, o eixo _a_ 2 é definido pelo produto vectorial entre os versores dos eixos _g_ 3 e _a_ 1, sendo _g_ ˆ3 = ( 1,0,0 ) 



Uma vez que deste produto vectorial não resulta um versor, é necessário dividir o vector _<u>a</u>_ 2 pela respectiva norma 



Para posterior referência, designam-se as componentes do versor<sup>_a_ˆ</sup> 2<sup>por</sup><sup>_B_1,</sup><sup>_B_2 e</sup><sup>_B_3</sup> 



Para que o referencial _a_ seja directo e ortonormado, calcula-se o versor<sup>_a_ˆ</sup> 3<sup>como sendo</sup> o resultado do produto vectorial entre<sup>_a_ˆ</sup> 1 e<sup>_a_ˆ</sup> 2<sup>.Doprodutovectorialentreversores</sup> perpendiculares entre si resulta sempre um versor. 



Para posterior referência, designam-se as componentes do versor<sup>_a_ˆ</sup> 3<sup>por</sup><sup>_C_1,</sup><sup>_C_2 e</sup><sup>_C_3</sup> 



De acordo com o que foi deduzido, os elementos da matriz de transformação do referencial _g_ para o referencial _a_ (36) são os seguintes 



23 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 

O resultado do produto vectorial expresso em (45) é um vector nulo sempre que o versor<sup>_a_ˆ</sup> 1<sup>seja paralelo ao versor</sup><sup>_g_ˆ</sup> 3<sup>. Supondo que o eixo</sup><sup>_g_ˆ</sup> 3<sup>é sempre vertical (hipótese</sup> considerada atrás), esta situação singular ocorre sempre que a barra é vertical. Para estes casos é então necessário definir a matriz de transformação _<u>T</u> ag_ com outro critério. Na Figura 2.3 e na Figura 2.4 encontra-se a posição do referencial _a_ em relação ao referencial _g_ para os casos da barra vertical orientada para cima e orientada para baixo. 



Fig. 2.3 - Posição do referencial _a_ em relação ao referencial _g_ para o caso da barra vertical orientada para cima. 



Fig. 2.4 - Posição do referencial _a_ em relação ao referencial _g_ para o caso da barra vertical orientada para baixo. 

Considerando as seguintes expressões para os versores do referencial _a_ , ficam cobertas as duas situações esquematizadas nas Figuras 2.3 e 2.4. 



24 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 





Tal como em (48), a matriz de transformação _<u>T</u> ag_ é constituída por 



_la_ Procede-se em seguida à definição da matriz _<u>T</u>_ que foi referida em (37). Esta matriz de transformação relaciona as coordenadas de um ponto no referencial auxiliar ( _a_ ) com as suas coordenadas no referencial local ( _l_ ). As considerações que se seguem baseiam-se na Figura 2.5, em que estão representados os referenciais _a_ e _l_ . O referencial _l_ é constituído pelo eixo da barra e pelos eixos principais centrais de inércia da secção transversal. 



<!-- Start of picture text -->
a 3<br>l  2 l 3<br>α<br>l<br>a 1 1<br>a 2 α<br>j<br>i<br>i  < j<br><!-- End of picture text -->

Fig. 2.5 - Posição do referencial _l_ em relação ao referencial _a_ . 

De acordo com a Figura 2.5, pode-se constatar o seguinte: 

- os eixos _a_ 1 e _l_ 1 coincidem; 

- os eixos _l_ 2 e _l_ 3 estão rodados de um ângulo α em relação aos eixos _a_ 2 e _a_ 3. 

25 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 

A transformação entre os referenciais _a_ e _l_ é um caso de transformação entre dois referenciais distintos do geral. Nesta situação pode-se recorrer à matriz definida em (27), que corresponde a uma transformação entre os referenciais _S_ ′ e _S_ ′′ . Neste caso, o referencial _S_ ′ é o referencial _a_ e o referencial _S_ ′′ é o referencial _l_ . A matriz de transformação é neste caso calculada com base nos cosenos dos ângulos formados pelos eixos dos dois referenciais. 



De acordo com a Figura 2.5 tem-se 





As matrizes de transformação _<u>T</u> ag_ e _<u>T</u> la_ encontram-se já definidas. De acordo com (40), a matriz de transformação _<u>T</u>_ , do referencial geral para o local é definida do seguinte modo 



Tal como foi indicado em (39), a correspondente transformação é efectuada com a seguinte expressão 



As expressões aqui deduzidas e que permitem calcular a matriz _<u>T</u>_ foram baseadas na informação de que é habitual dispor numa análise de um pórtico 3D pelo método dos deslocamentos, i.e., das coordenadas dos nós e do ângulo α . 

26 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 

Uma vez que a matriz _<u>T</u>_ é ortogonal, a transformação do referencial local para o geral é efectuada com a seguinte relação 



### **2.5 - Considerações finais** 

As expressões da matriz de transformação deduzidas neste capítulo podem ser directamente utilizadas na formulação da matriz de rigidez de elementos de treliça ou de pórtico 3D, bem como na formulação dos respectivos vectores de forças nodais equivalentes. 

### **BIBLIOGRAFIA** 

[2.1] - Brazão Farinha, J. S.; Correia dos Reis, A. - Tabelas Técnicas, Edições Técnicas E. T. L., 1998. 

27 

_Transformação Linear de Coordenadas - Álvaro F. M. Azevedo_ 

28 

### CAPÍTULO 3 

MÉTODO DOS DESLOCAMENTOS EM TRELIÇAS E PÓRTICOS 

Com o objectivo de apresentar alguns conceitos como o de assemblagem e introdução de condições de apoio, faz-se aqui uma sucinta descrição do método dos deslocamentos aplicado à análise de treliças e pórticos tridimensionais. 

### **3.1 - Simbologia** 

Apresenta-se em primeiro lugar um resumo da simbologia adoptada na formulação do método dos deslocamentos em treliças e pórticos. 

Tabela 3.1 - Simbologia relativa ao método dos deslocamentos em estruturas reticuladas. 

|_g_|Referencial geral|
|---|---|
|_a_|Referencial auxiliar|
|_l_|Referencial local|
|_i_|Primeiro nó de uma barra|
|_j_|Segundo nó de uma barra|
|α|Ângulo entre eixos dos referenciais auxiliar e local|
|_xg_|Coordenadas de um ponto no referencial geral|
|_xl_|Coordenadas de um ponto no referencial local|
|_T_|Matriz de transformação|
|_a_|Deslocamento ou deslocamento generalizado|
|θ|Rotação|
|_F_|Força ou força generalizada|
|_M_|Momento|



29 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 

|_a_|Deslocamentos nodais, nos graus de liberdade da estrutura, no referencial geral|
|---|---|
|_ag_|Deslocamentos nodais, nos graus de liberdade da barra, no referencial geral|
|_al_|Deslocamentos nodais, nos graus de liberdade da barra, no referencial local|
|_K_|Matriz de rigidez da estrutura no referencial geral|
|_Kg_|Matriz de rigidez da barra no referencial geral|
|_Kl_|Matriz de rigidez da barra no referencial local|
|_F_|Forças nodais equivalentes à acção exterior, nos graus de liberdade da estrutura,<br>no referencial geral|
|_Fg_|Forças nodais equivalentes à acção exterior, nos graus de liberdade da barra, no<br>referencial geral|
|_Fl_|Forças nodais equivalentes à acção exterior, nos graus de liberdade da barra, no<br>referencial local|
|_L_|Índice correspondente a um grau de liberdade não prescrito (livre)|
|_P_|Índice correspondente a um grau de liberdade prescrito|
|_R_|Reacção num apoio da estrutura|
|_n_|Número de graus de liberdade não prescritos (livres)|
|_p_|Número de graus de liberdade prescritos|
|_E_|Módulo de Young de um material|
|_A_|Área da secção transversal de uma barra|
|_L_|Comprimento de uma barra|
|_G_|Módulo de distorção de um material|
|_I_|Momento de inércia da secção transversal de uma barra|
|_It_|Momento de inércia de torção da secção transversal de uma barra|



30 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 

### **3.2 - Referenciais** 

De acordo com o que foi descrito no Capítulo 2, na formulação da matriz de rigidez de uma barra de eixo rectilíneo e de secção constante são considerados dois referenciais directos e ortonormados: o geral ( _g_ 1, _g_ 2, _g_ 3) e o local ( _l_ 1, _l_ 2, _l_ 3). O referencial geral é aquele em que se encontram expressas as coordenadas de todos os nós que depois são utilizados para definir a posição das barras. O referencial local é definido pelos seguintes eixos: _l_ 1 é o eixo da barra e _l_ 2 e _l_ 3 são os eixos principais centrais de inércia da secção transversal da barra (ver a Figura 3.1). 



<!-- Start of picture text -->
g 3<br>l  3 l 2<br>l  1<br>j<br>i<br>g<br>2<br>g<br>1 i  < j<br><!-- End of picture text -->

Fig. 3.1 - Barra _i j_ , referencial geral _g_ e referencial local _l_ . 

Considera-se habitualmente, sem perda de generalidade, que a barra definida pelos nós _i_ e _j_ tem o nó _i_ coincidente com a origem dos dois referenciais e o nó _j_ sobre o semi-eixo positivo _l_ 1. É também habitual considerar que o número do nó _i_ é inferior ao número do nó _j_ ( _i_ < _j_ ). 

Os eixos _l_ 2 e _l_ 3 podem ser trocados entre si, tendo em atenção que o referencial local deve ser sempre directo. A troca de _l_ 2 com _l_ 3 obriga a trocar entre si os valores dos momentos de inércia em relação a _l_ 2 e _l_ 3. Em qualquer dos casos é necessário definir criteriosamente o ângulo α (ver o Capítulo 2). 

31 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 

A transformação de coordenadas entre os referenciais _g_ e _l_ é efectuada com a seguinte expressão em que _<u>T</u>_ é a matriz de transformação (3 x 3) definida também no Capítulo 2. 



Nesta expressão, _<u>x</u> g_ são as coordenadas de um ponto no referencial _g_ e<sup>_<u>x</u>_</sup> _l_ são as coordenadas desse mesmo ponto no referencial _l_ . A equação (1) também pode ser utilizada para transformar as componentes de um vector do referencial _g_ para o referencial _l_ . 

### **3.3 - Graus de liberdade** 

Num ponto do espaço pertencente a um corpo sujeito a deslocamentos e deformações podem ser considerados seis graus de liberdade (três de deslocamento e três de rotação). 



Designa-se por deslocamentos generalizados o agrupamento dos três deslocamentos e das três rotações num só vector com seis componentes (ver a Figura 3.2). 



<!-- Start of picture text -->
a 3<br>θ  3 =  a  6<br>θ  2 =  a  5<br>a<br>2<br>θ  1 =  a  4<br>a<br>1<br><!-- End of picture text -->

Fig. 3.2 - Deslocamentos generalizados. 

32 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 

No estudo de um pórtico 3D são considerados os seis deslocamentos generalizados em cada ponto nodal (da barra ou da estrutura). O caso da treliça 3D, em que apenas são considerados três deslocamentos em cada ponto nodal ( _a_ 1, _a_ 2 e _a_ 3), pode ser adaptado do pórtico 3D, bastando eliminar tudo o que diz respeito a rotações e momentos. Para se passar da treliça 3D para a treliça 2D basta suprimir tudo o que diz respeito a um dos três graus de liberdade. Os pórticos 2D, grelhas e vigas contínuas são também simplificações do caso do pórtico 3D. 

Por ser o caso mais genérico, de aqui em diante apenas se desenvolve a formulação da barra de pórtico 3D. 

Em correspondência com os seis deslocamentos generalizados, são consideradas seis forças generalizadas (3 forças e 3 momentos), que se representam na Figura 3.3. 



<!-- Start of picture text -->
F 3<br>Μ 3 =  F 6<br>Μ 2 =  F 5<br>F<br>2<br>Μ  1 =  F 4<br>F<br>1<br><!-- End of picture text -->

Fig. 3.3 - Forças generalizadas. 

Na Figura 3.4 encontra-se representada uma barra de dois nós ( _i_ e _j_ ). Em cada nó são considerados seis graus de liberdade em correspondência com os seis deslocamentos generalizados (2). Assim, o número de graus de liberdade da barra é doze. 

33 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
l 3<br>3<br>6<br>i 5<br>2<br>1 4<br>9 l  2<br>12<br>j 11<br>i  < j<br>7 8<br>10<br>l  1<br><!-- End of picture text -->

Fig. 3.4 - Graus de liberdade da barra _i j_ no referencial local. 

Em correspondência com os doze graus liberdade representados na Figura 3.4, têm-se também as forças e os momentos que actuam nas extremidades da barra. 

### **3.4 - Matriz de transformação** 

A matriz de transformação _<u>T</u>_ referida em (1) é uma matriz 3 x 3 cujos componentes são 



A transformação dos doze deslocamentos generalizados representados na Figura 3.4 pode ser efectuada com a seguinte relação, desde que a matriz de transformação _<u>T</u>_ passe a ser uma matriz 12 x 12 constituída pela repetição de (3) quatro vezes. 



34 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 

|<br><br><br><br>_l_<br>_a_<br>1|<br>_T_<br>11|_T_<br>12|_T_<br>13|0|0|0|0|0|0|0|0|<br>0|<br><br><br><br>_g_<br>_a_<br>1||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|<br><br><br><br><br>_l_<br>_a_<br>2|<br><br>_T_<br>21|_T_<br>22|_T_<br>23|0|0|0|0|0|0|0|0|<br><br>0|<br><br><br><br><br>_g_<br>_a_<br>2||
|<br><br><br><br>_l_<br>_a_<br>3|<br><br><br>_T_<br>31|_T_<br>32|_T_<br>33|0|0|0|0|0|0|0|0|<br><br><br>0|<br><br><br><br>_g_<br>_a_<br>3||
|<br><br><br><br><br>_l_<br>_a_<br>4|<br><br>0|0|0|_T_<br>11|_T_<br>12|_T_<br>13|0|0|0|0|0|<br><br>0|<br><br><br><br><br>_g_<br>_a_<br>4||
|<br><br><br><br>_l_<br>_a_<br>5|<br><br>0|0|0|_T_<br>21|_T_<br>22|_T_<br>23|0|0|0|0|0|<br><br>0|<br><br><br><br>_g_<br>_a_<br>5||
|<br><br><br><br><br>_l_<br>_a_<br>6|<br><br>=<br>0|0|0|_T_<br>31|_T_<br>32|_T_<br>33|0|0|0|0|0|<br><br>0|<br><br><br><br><br>_g_<br>_a_<br>6||
|<br><br><br><br>_l_<br>_a_<br>7|<br><br><br>0|0|0|0|0|0|_T_<br>11|_T_<br>12|_T_<br>13|0|0|<br><br>0|<br><br><br><br>_g_<br>_a_<br>7|(5)|
|<br><br><br><br><br>_l_<br>_a_<br>8|<br><br>0|0|0|0|0|0|_T_<br>21|_T_<br>22|_T_<br>23|0|0|<br><br>0|<br><br><br><br><br>_g_<br>_a_<br>8||
|<br><br><br><br>_l_<br>_a_<br>9|<br><br>0|0|0|0|0|0|_T_<br>31|_T_<br>32|_T_<br>33|0|0|<br><br>0|<br><br><br><br>_g_<br>_a_<br>9||
|<br><br><br><br><br>_l_<br>_a_<br>10|<br><br>0|0|0|0|0|0|0|0|0|_T_<br>11|_T_<br>12|<br><br>_T_<br>13|<br><br><br><br><br>_g_<br>_a_<br>10||
|<br><br><br><br>_l_<br>_a_<br>11|<br><br>0|0|0|0|0|0|0|0|0|_T_<br>21|_T_<br>22|<br><br>_T_<br>23|<br><br><br><br>_g_<br>_a_<br>11||
|<br><br><br><br><br><br>_l_<br>_a_<br>12|<br><br><br>0|0|0|0|0|0|0|0|0|_T_<br>31|_T_<br>32|<br><br><br>_T_<br>33|<br><br><br><br><br><br>_g_<br>_a_<br>12||



### **3.5 - Matriz de rigidez e vector solicitação** 

Supondo o caso de uma barra de eixo rectilíneo e secção constante, a respectiva matriz de rigidez no referencial local <u>(</u> _<u>K</u> l_ ) , bem como o vector de forças nodais equivalentes a diversos tipos de acções <u>(</u> _<u>F</u> l_ ) podem ser directamente obtidos com base num formulário de estruturas [3.1] (ver também as Secções 3.9 e 3.10). Assim, parte-se do princípio que se dispõe da matriz _<u>K</u> l_ e do vector _<u>F</u> l_ , que se relacionam com a habitual equação 



sendo<sup>_<u>a</u>_</sup> _l_<sup>o vector dos deslocamentos generalizados da barra no referencial local.</sup> 

As equações (4) e (5) são válidas, quer para os deslocamentos generalizados, quer para as forças generalizadas, tendo-se também 



Uma vez que a matriz de transformação é ortogonal, i.e. 



35 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 

multiplicam-se ambos os membros de (7) por _<u>T</u> T_ e obtém-se 



Substituindo em (9) a equação (6) 



resulta 



Substituindo (4) em (11) chega-se a 



Uma vez que a relação de rigidez da barra no referencial geral é 



Da comparação de (12) com (13) conclui-se que a matriz de rigidez da barra de pórtico 3D no referencial geral é dada por 



O vector solicitação _<u>F</u> g_ pode ser calculado com a expressão (9). 

Depois de serem conhecidos os deslocamentos _<u>a</u> g_ , é possível calcular as acções nas extremidades das barras no referencial local, recorrendo à seguinte expressão, que resulta da substituição de (4) em (10) 



36 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 

### **3.6 - Assemblagem da matriz de rigidez global e do vector solicitação** 

Depois de calculadas todas as matrizes de rigidez das barras no referencial geral com recurso à expressão (14), é necessário proceder ao cálculo da matriz de rigidez global da estrutura. Uma operação semelhante tem de ser efectuada com os vectores solicitação das diversas barras. 

A assemblagem na matriz de rigidez global das matrizes de rigidez das diversas barras é em seguida apresentada com base no exemplo da Figura 3.5. 



<!-- Start of picture text -->
a  1 a  2 a  3 a  4<br>F 1 F 2 F 3<br>F 4<br>1 2 3 4<br>B C<br>A D<br><!-- End of picture text -->

Fig. 3.5 - Assemblagem num exemplo unidimensional. 

A estrutura representada na Figura 3.5 é unidimensional, tem quatro nós (1 a 4) e quatro barras ( _A_ a _D_ ). Cada barra tem as suas características, nomeadamente, o módulo de Young ( _E_ ), a área da secção transversal ( _A_ ) e o comprimento ( _L_ ). Em cada nó existe um único grau de liberdade. Em correspondência com os quatro graus de liberdade existem quatro deslocamentos nodais ( _a_ ) e quatro forças nodais equivalentes à acção exterior ( _F_ ). Cada barra tem dois graus de liberdade (um em cada extremidade). 

Para cada barra é conhecida a matriz de rigidez (2 x 2) no referencial geral, cuja designação se simplifica de acordo com 





37 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 





Atendendo à numeração global dos graus de liberdade (1 a 4), as matrizes de rigidez das barras passam a ser 









O vector dos deslocamentos em todos os graus de liberdade da estrutura é 



38 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
a  1 a  2 a  3 a  4<br>B B C C<br>F A F A F 1 F 2 F 1 F 2<br>1 2 B C<br>A<br>D D D<br>F 1 F 2<br><!-- End of picture text -->

Fig. 3.6 - Vectores das forças nodais equivalentes a acções exteriores. 

Atendendo à numeração global dos graus de liberdade, os vectores das forças nodais equivalentes às acções nas diversas barras são (ver a Figura 3.6) 









Os vectores e matrizes indicados em (20)-(28) relacionam-se entre si de acordo com as seguintes equações 

39 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 









A soma dos primeiros membros das equações (29)-(32) é igual à soma dos seus segundos membros, resultando 



Uma vez que a relação de rigidez envolvendo todos os graus de liberdade da estrutura é 



conclui-se que 



e 



Adicionando as matrizes (20)-(23) de acordo com (36) chega-se a 



Adicionando os vectores solicitação (25)-(28) de acordo com (37) chega-se a 

40 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 



O procedimento de assemblagem aqui exposto é generalizável ao caso em que existem seis graus de liberdade em cada nó. Para esse fim, é suficiente considerar que, por exemplo, _C_ 12 em vez de ser um escalar é uma matriz 6 x 6 contendo os elementos da matriz _<u>K</u> C_ que relacionam os graus de liberdade do nó 1 com os graus de liberdade do nó 2. 

### **3.7 - Introdução das condições de apoio** 

O sistema de equações (35) ainda não pode ser resolvido, porque falta entrar em linha de conta com as condições de apoio da estrutura. Estas condições fronteira correspondem a apoios fixos ou assentamentos de apoio. Os apoios fixos podem sempre ser tratados como assentamentos de apoio de valor nulo. Por este motivo, no desenvolvimento que se segue apenas são referidos os assentamentos de apoio. 

O sistema de equações (35) relaciona forças e deslocamentos que se encontram no referencial geral, englobando todos os graus de liberdade da estrutura. Tendo em vista a consideração das condições de apoio, os graus de liberdade da estrutura são divididos em dois grupos: 

- L - graus de liberdade não prescritos (livres) 

- P - graus de liberdade prescritos 

Assim, o sistema de equações (35) passa a ter a seguinte organização por blocos 



Em (40), _<u>a</u> L_ é o vector que engloba os deslocamentos segundo os graus de liberdade não prescritos e _<u>a</u> P_ engloba os prescritos. O mesmo tipo de subdivisão é efectuado com o vector das forças nodais equivalentes à acção exterior ( _<u>F</u>_ ). O vector adicional em que 

41 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 

figura _<u>R</u> P_ contém as reacções de apoio, que consistem nas forças (ainda desconhecidas) que fazem com que os deslocamentos em apoios assumam os valores prescritos. 

Designando por _n_ o número de graus de liberdade não prescritos e por _p_ o número de graus de liberdade prescritos, são especificadas na Tabela 3.2 as dimensões das sub-matrizes que figuram em (40). 

Tabela 3.2 - Dimensões das sub-matrizes presentes em (40). 

|_LL_<br>_K_|→|(_n_x_n_)|
|---|---|---|
|_LP_<br>_K_|→|(_n_x_p_)|
|_PL_<br>_K_|→|(_p_x_n_)|
|_PP_<br>_K_|→|(_p_x_p_)|
|_L_<br>_L_ <sup>_F_</sup><br>_a_ ,|→|(_n_x1 )|
|_P_<br>_P_<br>_P_<br>_R_<br>_F_<br>_a_<br>,<br>,|→|(_p_x1 )|



Esta divisão em sub-matrizes obriga a fazer uma reorganização das linhas e das colunas da matriz _<u>K</u>_ que figura em (35), bem como das componentes dos vectores _<u>a</u>_ e _<u>F</u>_ . 

Na Tabela 3.3 é apresentado o significado dos elementos das quatro sub-matrizes de _<u>K</u>_ indicadas em (40). 

Tabela 3.3 - Significado dos elementos das sub-matrizes de _<u>K</u>_ indicadas em (40). 

||Deslocamento unitário<br>imposto segundo um<br>grau de liberdade:|Forças de fixação<br>num grau de<br>liberdade:|
|---|---|---|
|_LL_<br>_K_|Livre|Livre|
|_LP_<br>_K_|Livre|Prescrito|
|_PL_<br>_K_|Prescrito|Livre|
|_PP_<br>_K_|Prescrito|Prescrito|



No novo sistema de equações indicado em (40), as incógnitas são _<u>a</u> L_ e _<u>R</u> P_ . Os elementos de _<u>K</u>_ , _<u>a</u> P_ , _<u>F</u> L_ e _<u>F</u> P_ têm valores conhecidos. 

42 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 

O sistema de equações (40) pode ser escrito do seguinte modo 





A equação (41) pode ser rescrita do seguinte modo 



Em (43), _<u>K</u> LL_ é uma matriz quadrada, que em geral é não singular, _<u>a</u> L_ é o vector das incógnitas e os valores dos vectores e matrizes que estão no segundo membro são conhecidos. Por este motivo, (43) constitui um sistema de equações lineares, que depois de resolvido fornece os valores dos deslocamentos _<u>a</u> L_ . 

A equação (42) pode ser rescrita do seguinte modo 



Uma vez que os deslocamentos _<u>a</u> L_ já são conhecidos, esta expressão fornece os valores das reacções em graus de liberdade prescritos ( _<u>R</u> P_ ). 

O modo de introdução das condições de apoio aqui descrito tem as seguintes vantagens: 

- na fase do processo que requer um maior volume de cálculos e uma grande quantidade de memória de armazenamento, i.e., na fase de resolução do sistema de equações (43), o número de equações e incógnitas é _n_ em vez de ser _n_ + _p_ ; 

- em comparação com o método em que é adicionado à diagonal principal de _<u>K</u>_ um número elevado, o método aqui proposto apresenta menos problemas numéricos, principalmente quando se utilizam métodos iterativos para resolver o sistema de equações. 

A principal desvantagem do método aqui proposto é a necessidade de agrupar os elementos de _<u>K</u>_ em diversas sub-matrizes. Esta nova arrumação causa algumas dificuldades, principalmente quando se utilizam técnicas de armazenamento esparso, em banda ou em perfil. 

43 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 

### **3.8 - Faseamento da análise de um pórtico 3D** 

Tendo em vista a análise de uma estrutura do tipo pórtico 3D pelo método dos deslocamentos, sugere-se o seguinte algoritmo 

### - Para cada barra: 

   - Calcular a matriz de transformação _<u>T</u>_ (3) e em seguida calcular (5) 

   - Calcular a matriz de rigidez da barra, no referencial local ( _<u>K</u> l_ ) 

   - Calcular a matriz de rigidez da barra, no referencial geral ( _<u>K</u> g_ ) com (14) 

   - Assemblar ( _<u>K</u> g_ ) em ( _<u>K</u>_ ) (ver a Secção 3.6) 

   - Calcular o vector das forças nodais equivalentes à acção exterior na barra, no referencial local ( _<u>F</u> l_ ) 

   - Calcular ( _<u>F</u> g_ ) com (9) 

   - Assemblar ( _<u>F</u> g_ ) em ( _<u>F</u>_ ) (ver a Secção 3.6) 

- Introduzir as condições de apoio (ver a Secção 3.7) 

- Resolver o sistema de equações lineares (43), determinando assim os deslocamentos 

- Calcular as reacções nos apoios com (44) 

- Para cada barra: 

   - Passar os deslocamentos relativos à barra corrente do vector _<u>a</u>_ para o vector _<u>a</u> g_ 

   - Calcular ( _<u>F</u> l_ ) com (15) 

### - Fim 

Embora seja possível utilizar o procedimento sugerido sem recursos informáticos, é hoje em dia preferível implementá-lo por intermédio de um programa de computador. Neste domínio surgem muitas alternativas, tais como a selecção da linguagem de 

44 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 

programação, o modo de criar os dados do problema, o modo de armazenamento da informação, as técnicas numéricas utilizadas, o recurso ou não a bibliotecas de operações matriciais, etc. 

### **3.9 - Matriz de rigidez de uma barra de treliça 3D no referencial local** 

Na Figura 3.7 encontra-se representada uma barra de treliça espacial, de eixo rectilíneo e secção constante. A sua matriz de rigidez (45), expressa no referencial local _l_ , depende das seguintes grandezas: 

- _E_ - módulo de Young, constante em todos os pontos da barra; 

- _A_ - área da secção transversal da barra, considerada constante; 

- _L_ - comprimento da barra. 



<!-- Start of picture text -->
l 3<br>3<br>i<br>2<br>1<br>6 l  2<br>j<br>i  < j<br>5<br>4<br>l  1<br><!-- End of picture text -->

Fig. 3.7 - Treliça 3D: graus de liberdade da barra _i j_ no referencial local. 



45 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 

### **3.10 - Matriz de rigidez de uma barra de pórtico 3D no referencial local** 

Na Figura 3.8 encontra-se representada uma barra de pórtico espacial, de eixo rectilíneo e secção constante. A sua matriz de rigidez (46)-(50), expressa no referencial local _l_ , depende das seguintes grandezas: 

- _E_ - módulo de Young, constante em todos os pontos da barra; 

- _A_ - área da secção transversal da barra, considerada constante; 

- _L_ - comprimento da barra; 

- _G_ - módulo de distorção [3.2]; 

- _I_ 2 - momento de inércia da secção transversal da barra em relação ao eixo _l_ 2; 

- _I_ 3 - momento de inércia da secção transversal da barra em relação ao eixo _l_ 3; 

- _It_ - momento de inércia de torção da secção transversal da barra [3.3] [3.4]. 

Nota: _l_ 2 e _l_ 3 são eixos principais centrais de inércia da secção transversal da barra. 



<!-- Start of picture text -->
l  3<br>3<br>6<br>i 5<br>2<br>1 4<br>9 l 2<br>12<br>j 11<br>i  < j<br>7 8<br>10<br>l 1<br><!-- End of picture text -->

Fig. 3.8 - Pórtico 3D: graus de liberdade da barra _i j_ no referencial local. 



(46) 

46 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 







### **3.11 - Considerações finais** 

Neste capítulo não foi considerada a possibilidade da a barra apresentar eixo não rectilíneo, nem o facto de a secção transversal ser variável ao longo do eixo da barra. Não foi também considerada a contribuição das tensões tangenciais para a deformação, habitualmente designada deformação por esforço transverso. A inclusão destas características faz com que a formulação apresentada neste capítulo perca a simplicidade atrás evidenciada. Mais adiante serão apresentadas formulações da matriz de rigidez de uma barra recorrendo a técnicas específicas do Método dos Elementos Finitos, em particular a formulação de viga de Timoshenko. Com este tipo de elementos de barra é possível ter em consideração a deformação por esforço transverso, o eixo curvilíneo e a secção variável. 

47 

_Método dos Deslocamentos em Treliças e Pórticos - Álvaro F. M. Azevedo_ 

### **BIBLIOGRAFIA** 

[3.1] - Brazão Farinha, J. S.; Correia dos Reis, A. - Tabelas Técnicas, Edições Técnicas E. T. L., 1998. 

[3.2] - Azevedo, A. F. M. - Mecânica dos Sólidos, Faculdade de Engenharia da Universidade do Porto, 1996. 

[3.3] - Segadães Tavares, A. - Análise Matricial de Estruturas, Laboratório Nacional de Engenharia Civil, Curso 129, Lisboa, 1973. 

[3.4] - Massonnet, C. - Résistance des Matériaux, Dunod, Paris, 1968. 

48 

### CAPÍTULO 4 

### ELEMENTOS FINITOS UNIDIMENSIONAIS 

Antes de expor o método dos elementos finitos (MEF) de um modo aplicável a meios contínuos bidimensionais e tridimensionais, apresenta-se com algum detalhe o caso unidimensional. Quando apenas se considera uma dimensão, o método resultante não tem grande interesse prático, mas serve como introdução às técnicas que mais adiante serão expostas para os casos mais genéricos. 

O método dos elementos finitos, que adiante será exposto, baseia-se no método dos deslocamentos e na discretização de uma estrutura em sub-estruturas. Cada uma dessas sub-estruturas designa-se por elemento finito e tem comportamento conhecido, sendo o comportamento do todo considerado como a soma das partes. Cada elemento finito tem _n_ nós, sendo apenas considerados explicitamente os deslocamentos generalizados nesses nós. Os deslocamentos nos restantes pontos do elemento finito obtêm-se por interpolação dos deslocamentos dos nós. 

### **4.1 - Simbologia** 

Apresenta-se em primeiro lugar um resumo da simbologia adoptada na formulação do método dos elementos finitos. 

Tabela 4.1 - Simbologia relativa ao método dos elementos finitos. 

|_n_|Número de nós do elemento finito|
|---|---|
|_L_|Comprimento da barra prismática|
|_x_|Coordenada cartesiana|
|_u_|Campo de deslocamentos|
|_a_|Deslocamento nodal|
|_N_|Função interpoladora ou função de forma|



49 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 

|ε|Deformação|
|---|---|
|_B_|Matriz de deformação|
|_L_ <sup>1</sup>|Operador diferencial (_L_ <sup>1 </sup>=_d_/_d x_)|
|_V_|Volume da barra prismática|
|σ|Tensão normal|
|_p_|Acção exterior distribuída por unidade de comprimento|
|_F_|Forças nodais equivalentes à acção exterior, nos graus de liberdade do<br>elemento finito, no referencial local|
|_A_|Área da secção transversal da barra prismática|
|_E_|Módulo de elasticidade ou módulo de Young|
|_D_|Matriz de elasticidade (<br>ε<br>σ<br>_D_<br>=<br>)|
|_K_|Matriz de rigidez do elemento finito no referencial local|
|_c_|Coeficiente de um termo de um polinómio|
|_~~x~~_|Coordenada cartesiana de um nó de um elemento finito|
|_s_|Coordenada local|
|_E_|Módulo de elasticidade num nó do elemento finito|
|_A_|Área da secção transversal num nó do elemento finito|
|_J_|Jacobiano da transformação (_J_=_d x_/_d s_)|



### **4.2 - Funções interpoladoras ou funções de forma** 

Na Figura 4.1 encontra-se representado um elemento finito unidimensional com dois nós e com comprimento _L_ = 2. 

50 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
u  ( x )<br>a 1 a 2 x<br>1 2<br>L  = 2<br>( x  = - 1) ( x  = 1)<br><!-- End of picture text -->

Fig. 4.1 - Elemento finito unidimensional de dois nós. 

O único eixo coordenado que é considerado é o eixo _x_ , ocorrendo todos os deslocamentos paralelamente a _x_ . A função _u_ ( _x_ ) corresponde ao campo de deslocamentos, verificando-se o seguinte 



sendo portanto _a_ 1 e _a_ 2 os deslocamentos dos nós. 

Considere-se agora, como aproximação, que a lei de variação do deslocamento entre os nós 1 e 2 é linear. Nestas circunstâncias, a seguinte função _u_ ( _x_ ) representa o campo de deslocamentos porque é linear em _x_ e respeita (1) 



Os valores numéricos dos parâmetros _a_ 1 e _a_ 2 passarão a ser conhecidos depois de analisada a estrutura. 

Colocando _a_ 1 e _a_ 2 em evidência em (2), chega-se à seguinte expressão 



Em (3) tem-se uma soma de produtos de funções lineares de _x_ pelos deslocamentos nodais _a_ 1 e _a_ 2. 

51 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 

A equação (3) pode ser escrita em forma matricial 



ou 



sendo 



e 



com 



e 



O gráfico das funções lineares _N_ 1 e _N_ 2 indicadas em (6) encontra-se representado na Figura 4.2. 

52 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
N 1( x ) N 2( x )<br>1 1<br>x x<br>- 1 1 - 1 1<br><!-- End of picture text -->

Fig. 4.2 - Gráfico das funções _N_ 1( _x_ ) e _N_ 2( _x_ ). 

A principal característica dos gráficos das funções _N_ 1( _x_ ) e _N_ 2( _x_ ) é salientada na Tabela 4.2 e consiste no facto de a função _N_ 1( _x_ ) assumir o valor unitário no nó 1 e nulo nos restantes nós. A função _N_ 2( _x_ ) assume o valor unitário no nó 2 e nulo nos restantes nós. Esta característica será clarificada adiante quando se apresentarem exemplos de elementos finitos com mais do que dois nós. 

Tabela 4.2 - Características das funções _N_ 1( _x_ ) e _N_ 2( _x_ ). 

|_x_|-1|1|
|---|---|---|
|_N_1(_x_)|1|0|
|_N_2(_x_)|0|1|



Apresentam-se em seguida as funções de forma _N_ 1( _x_ ) e _N_ 2( _x_ ) para o caso da barra de dois nós de comprimento _L_ (ver a Figura 4.3). 



<!-- Start of picture text -->
u  ( x )<br>a 1 a 2 x<br>1 2<br>L<br>( x  = -  L  / 2) ( x  =  L  / 2)<br><!-- End of picture text -->

Fig. 4.3 - Elemento finito unidimensional de dois nós com comprimento _L_ . 

53 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 

De um modo semelhante ao que foi descrito para o elemento de comprimento _L_ = 2, tem-se sucessivamente 









### **4.3 - Campo de deformações** 

O campo de deformações na barra é definido do seguinte modo 



Atendendo a (5) tem-se 



Uma vez que os deslocamentos nodais _a_ 1 e _a_ 2 não dependem de _x_ , da derivação resulta 



que em notação matricial fica 



54 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 

Designando por _<u>B</u>_ a matriz 



e atendendo a (9), tem-se 



Designando por _L_<sup>1</sup> o seguinte operador diferencial 



a equação (14) escreve-se 



Atendendo a (7) tem-se 



Comparando (22) com (19), conclui-se que 



De acordo com (18) e com (6), para o caso da barra de comprimento _L_ = 2, os elementos da matriz _<u>B</u>_ são os seguintes 



No caso da barra de comprimento _L_ , de (18) e (13) chega-se a 

55 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 



De (9), (19) e (27) conclui-se que, no caso da barra de comprimento _L_ , se tem 



Neste exemplo simples, a expressão do campo de deformações corresponde ao que se considera habitualmente para uma barra sujeita a um esforço axial. Uma vez que ε não depende da coordenada _x_ , este elemento finito apresenta deformação constante. 

### **4.4 - Princípio dos trabalhos virtuais** 

Considere-se um corpo sujeito a um conjunto de forças de volume e de superfície que lhe provocam uma deformação. Com base no seu estado de equilíbrio estático, a configuração do corpo é modificada por um conjunto de deslocamentos muito pequenos e compatíveis com as condições fronteira, que se designam deslocamentos virtuais. O princípio dos trabalhos virtuais ou princípio dos deslocamentos virtuais estabelece que o trabalho realizado pelas tensões internas na deformação virtual do corpo é igual ao trabalho realizado pelas forças exteriores nos deslocamentos virtuais dos seus pontos de aplicação [4.1] [4.2]. De um modo mais simplista é comum afirmar que o trabalho interno de deformação é igual ao trabalho externo das forças aplicadas. 

_Trabalho Interno = Trabalho Externo_ (29) 

Apresenta-se em seguida uma versão simplificada do princípio dos trabalhos virtuais (PTV) adaptada ao caso das barras sujeitas a deslocamentos e forças apenas axiais. Nas expressões que se seguem, o prefixo δ indica que os deslocamentos ou deformações são virtuais. 

56 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 



Nesta expressão o vector <u>δε</u> apenas tem a componente correspondente à extensão segundo o eixo da barra, o vector <u>σ</u> apenas contem a tensão normal na secção transversal da barra, o campo de deslocamentos ( δ _<u>u</u>_ ) e a acção exterior distribuída ( _<u>p</u>_ ) apenas referem a componente segundo o eixo da barra (ver a Figura 4.4). 



<!-- Start of picture text -->
u  ( x )<br>p<br>F 1 F 2<br>x<br>1 2<br>L<br>( x  = -  L  / 2) ( x  =  L  / 2)<br><!-- End of picture text -->

Fig. 4.4 - Elemento finito unidimensional sujeito a uma acção axial uniformemente distribuída. 

Neste caso a expressão do PTV (30) passa a ser a seguinte 



### **4.5 - Matriz de rigidez e vector solicitação** 

Com base no princípio dos trabalhos virtuais apresentado na secção anterior, vai-se em seguida proceder à dedução das expressões da matriz de rigidez e do vector solicitação que são utilizados no método dos deslocamentos. 

Designando por _A_ a área da secção transversal da barra, tem-se 



Uma vez que o eixo da barra coincide com o eixo _x_ , tem-se 



57 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 

A equação (19) referida à deformação virtual é a seguinte 



que é equivalente a 



A relação constitutiva ou relação tensão-deformação é neste caso 



apresentando a matriz de elasticidade _D_ apenas um elemento que consiste no módulo de Young ( _E_ ). 

Substituindo (19) em (36) tem-se 



A equação (7) referida à deformação virtual é a seguinte 



que é equivalente a 



Substituindo todas estas equações em (31) passa a ter-se o PTV expresso por 



Uma vez que os deslocamentos nodais não dependem de _x_ podem passar para fora do integral 



58 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 

De acordo com o PTV, a equação (41) é verdadeira para qualquer conjunto de deslocamentos virtuais, concluindo-se assim que 



Comparando esta equação com a relação de rigidez que é utilizada no método dos deslocamentos 



tem-se no caso da barra unidimensional 



As expressões (42)-(45) são aplicáveis quando as seguintes grandezas são variáveis ao longo da barra: módulo de Young ( _E_ ), área da secção transversal ( _A_ ) e carga distribuída ( _p_ ). 

Apresenta-se em seguida o desenvolvimento das expressões (44) e (45) para o caso de _E_ , _A_ e _p_ serem constantes. 



Atendendo a (27) 



59 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 

Neste caso simples os elementos da matriz de rigidez coincidem com os que se obtêm directamente pelo método dos deslocamentos. 

Partindo de (45), tem-se neste caso em que _p_ é constante 



Atendendo a (8) e a (13) tem-se 





Esta expressão também coincide com a que se obtém por processos mais simples. 

### **4.6 - Elemento finito unidimensional com três nós** 

Considere-se o elemento finito unidimensional com três nós representado na Figura 4.5, cujo comprimento é _L_ = 2. 



<!-- Start of picture text -->
u  ( x )<br>a 1 a 2 a 3<br>x<br>1 2 3<br>( x  = - 1) ( x  = 0) ( x  = 1)<br>L  = 2<br><!-- End of picture text -->

Fig. 4.5 - Elemento finito unidimensional de três nós. 

60 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 

De um modo semelhante ao que foi apresentado na Secção 4.2, considera-se que a função _u_ ( _x_ ) é aproximada pelo seguinte polinómio de segundo grau 



Pretende-se que a função (52) respeite nos nós os valores dos respectivos deslocamentos, sendo 



Atendendo a (52) tem-se 



que é equivalente a 



Explicitando _c_ 0, _c_ 1 e _c_ 2 tem-se 



Substituindo as expressões de _c_ 0, _c_ 1 e _c_ 2 em (52), chega-se a 



que é equivalente a 



61 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 

Em notação matricial tem-se 



Considerando 



tem-se 



Neste caso 





Na Figura 4.6 estão representados os gráficos das funções _N_ 1( _x_ ), _N_ 2( _x_ ) e _N_ 3( _x_ ) indicadas em (61) 

62 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
N 1( x )<br>1<br>x<br>-1 1<br>N 2( x )<br>1<br>x<br>-1 1<br>N 3( x )<br>1<br>x<br>-1 1<br><!-- End of picture text -->

Fig. 4.6 - Gráfico das funções _N_ 1( _x_ ), _N_ 2( _x_ ) e _N_ 3( _x_ ). 

Na Tabela 4.3 encontram-se algumas características das funções de forma representadas na Figura 4.6 (comparar com a Tabela 4.2). 

Tabela 4.3 - Características das funções _N_ 1( _x_ ), _N_ 2( _x_ ) e _N_ 3( _x_ ). 

|_x_|-1|0|+1|
|---|---|---|---|
|_N_1(_x_)|1|0|0|
|_N_2(_x_)|0|1|0|
|_N_3(_x_)|0|0|1|



63 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 

Generalizando a expressão (18) para o caso do elemento de três nós, resulta 



Atendendo a (61), os elementos da matriz _<u>B</u>_ são neste caso os seguintes 



O cálculo da matriz de rigidez _<u>K</u>_ e do vector solicitação _<u>F</u>_ pode ser efectuado por um processo semelhante ao indicado na Secção 4.5, não sendo aqui desenvolvido. 

### **4.7 - Elemento finito unidimensional com substituição de variável** 

Na Figura 4.7 encontra-se representado um elemento finito unidimensional com três nós e geometria qualquer. 



<!-- Start of picture text -->
u  ( x )<br>a 1 a 2 a 3<br>x<br>1 2 3<br>( x = x 1 ) ( x = x 2 ) ( x = x 3 )<br><!-- End of picture text -->

Fig. 4.7 - Elemento finito unidimensional de três nós com geometria arbitrária. 

As coordenadas dos nós são<sup>_~~x~~_</sup> 1<sup>,</sup><sup>_~~x~~_</sup> 2<sup>e</sup><sup>_~~x~~_</sup> 3<sup>. Tal como nos casos descritos anteriormente,</sup><sup>_E_</sup> representa o módulo de Young, _A_ é a área da secção transversal e _p_ é a acção axial distribuída. Todas estas grandezas podem eventualmente depender de _x_ . 

É possível calcular a matriz de rigidez _<u>K</u>_ e o vector solicitação _<u>F</u>_ com (44) e (45), utilizando como variável a coordenada _x_ . Contudo, e tendo em vista a generalização deste estudo aos casos bidimensionais e tridimensionais, vai ser efectuada uma substituição de variável do tipo 

64 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 



A função _x_ ( _s_ ) , neste caso seleccionada, corresponde a uma interpolação coincidente com a que foi efectuada na Secção 4.6 para a função deslocamento _u_ ( _x_ ) , em que foi utilizada a interpolação (60), conjuntamente com as funções de forma (61). 



_x_ ( _s_ ) = _N_ 1 ( _s_ ) _~~x~~_ 1 + _N_ 2 ( _s_ ) _~~x~~_ 2 + _N_ 3 ( _s_ ) _~~x~~_ 3 (69) 



De um modo semelhante ao que se verificou em (53), tem-se 



A substituição de variável (67) encontra-se esquematizada na Figura 4.8. 

65 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 



Fig. 4.8 - Substituição da variável _x_ . 

Após a substituição da variável _x_ , o integral (44) passa a ser 



com _D_ , _<u>B</u>_ , _A_ e _dx_ / _ds_ dependentes da nova variável _s_ . 

Se não forem constantes, _D_ (que coincide com _E_ ) e _A_ são interpolados com as mesmas funções de forma que foram utilizadas para interpolar as coordenadas dos nós, i.e., a interpolação é efectuada tal como em (69). 





Nestas funções,<sup>_E_</sup> _i_<sup>e</sup><sup>_A_</sup> _i_<sup>são os valores no nó</sup><sup>_i_do módulo de Young e da área da secção</sup> transversal. 

A expressão de _dx_ / _ds_ , que se passa a designar por _J_ , obtém-se por derivação de (69), resultando 

Por derivação de (70) em ordem a _s_ , obtém-se 

66 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 



ficando 



Para avaliar o integral (72) é ainda necessário definir a matriz _<u>B</u>_ em função de _s_ . Atendendo à adaptação de (18) ao elemento de três nós, que foi também utilizada em (65), existe a necessidade de calcular as derivadas das funções de forma em ordem a _x_ , mas expressas em função de _s_ . Com este objectivo, e uma vez que as funções de forma _Ni_ (61) dependem de _x_ , que por sua vez depende de _s_ (69), tem-se, recorrendo à regra da cadeia 



Multiplicando ambos os membros de (79) pela inversa de _dx_ / _ds_ resulta 



Uma vez que _dx_ / _ds_ é um escalar, pode escrever-se 



67 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 

sendo, de acordo com (76) e (77) 



A matriz _<u>B</u>_ apresenta os seguintes componentes 



Depois de definidos todos os componentes da função integranda de (72), é possível efectuar as seguintes simplificações 



sendo 



68 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 



Atendendo a (81) e ao facto de ser _J_ = _dx_ / _ds_ , tem-se 



A expressão genérica do elemento _Kij_ da matriz _<u>K</u>_ é 



Como exemplo, apresenta-se em seguida a expressão do elemento _K_ 13 da matriz de rigidez do elemento finito, de acordo com (90) e (76) 



Considere-se agora um caso particular de uma barra de comprimento total _L_ e nó 2 centrado (ver a Figura 4.7), com 



Neste caso particular, a expressão de _J_ calculada com (77) não depende de _s_ , sendo 

69 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 



Se além de _J_ ser constante, _E_ e _A_ também forem constantes, é simples calcular o integral (91), resultando 



Apresenta-se em seguida um exemplo numérico em que o nó 2 não se encontra centrado no elemento finito de três nós (ver a Figura 4.7) 



Neste caso concreto, a expressão de _J_ calculada com (77) é 



Supondo _E_ e _A_ constantes, tem-se, de acordo com (91) 



Na prática é conveniente resolver os integrais (90) e (97) recorrendo a uma técnica de integração numérica, que será descrita no Capítulo 5. 

### **4.8 - Considerações finais** 

A formulação pelo MEF aqui efectuada no âmbito de um problema muito simples serve como introdução às técnicas que se aplicam em meios contínuos com duas ou três dimensões, de que são exemplo os estados planos de tensão, as cascas e os sólidos. Muitas das expressões matriciais que aqui foram apresentadas coincidem com as que 

70 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 

surgem nos casos mais genéricos, sendo apenas necessário redefinir as dimensões e os elementos dos vectores e das matrizes. 

### **BIBLIOGRAFIA** 

[4.1] - Cook, R. D.; Malkus, D. S.; Plesha, M. E.; Witt, R. J. - Concepts and Applications of Finite Element Analysis, Fourth Edition, John Wiley & Sons, Inc., 2002. 

[4.2] - Zienkiewicz, O. C.; Taylor, R. L. - The Finite Element Method, Fourth Edition, McGraw-Hill, 1988. 

71 

_Elementos Finitos Unidimensionais - Álvaro F. M. Azevedo_ 

72 

### CAPÍTULO 5 

### QUADRATURA DE GAUSS 

Muitos dos integrais que é necessário calcular no âmbito da aplicação do Método dos Elementos Finitos (MEF) não são triviais, i.e., ou a primitiva da função integranda não existe explicitamente, ou é demasiado complicada para viabilizar a sua utilização prática. Por este motivo é essencial recorrer a técnicas de integração numérica, que também recebem a designação de quadratura. Neste capítulo é descrita e justificada a quadratura de Gauss, por ser a mais utilizada no âmbito do MEF [5.1]. 

### **5.1 - Simbologia** 

Apresenta-se em primeiro lugar um resumo da simbologia adoptada no estudo da quadratura de Gauss. 

Tabela 5.1 - Simbologia relativa à quadratura de Gauss. 

|_c_|Coeficiente de um termo de um polinómio|
|---|---|
|_I_|Valor exacto do integral|
|_J_|Valor do integral calculado de acordo com a quadratura de Gauss|
|_P_|Posição de um ponto de Gauss ou ponto de amostragem|
|_W_|Peso (_weight_) associado a um ponto de Gauss ou ponto de amostragem|
|_n_|Número de pontos de Gauss utilizados numa direcção|
|_p_|Grau de um polinómio|



### **5.2 - Integração de uma função polinomial** 

Na Figura 5.1 encontra-se representada uma função polinomial de grau 5, cuja expressão genérica é a seguinte 

73 

_<u>Quadratura de Gauss</u> - Álvaro F. M. Azevedo_ 





<!-- Start of picture text -->
f  ( x )<br>x<br>-1 P 1 P 2 P 3 +1<br><!-- End of picture text -->

Fig. 5.1 - Função polinomial de grau 5. 

O integral (exacto) do polinómio (1) no intervalo [-1,1] é 







Para facilitar a sua comparação com uma expressão que vai ser em seguida apresentada, o segundo membro de (4) é rescrito da seguinte forma 



Suponha-se agora que se pretende avaliar o integral de _f_ ( _x_ ) por intermédio do somatório de avaliações da função _f_ ( _x_ ) em determinados locais, multiplicadas por adequados pesos. No caso do polinómio de grau 5 indicado em (1), será adiante mostrado que, para se obter um resultado exacto, se deve avaliar a função _f_ ( _x_ ) em três pontos de amostragem _Pi_ e multiplicar cada um desses valores por pesos _Wi_ (ver a Figura 5.1). O integral avaliado desta forma é designado por _J_ , sendo 

74 

_<u>Quadratura de Gauss</u> - Álvaro F. M. Azevedo_ 



Mais adiante será deduzido o valor adequado para os seguintes parâmetros: 

- posição dos pontos de amostragem _P1_ , _P2_ e _P3_ em que a função _f_ ( _x_ ) deve ser avaliada (ver a Figura 5.1); 

- valores dos pesos _W1_ , _W2_ e _W3_ . 

Uma vez que _f_ ( _x_ ) é um polinómio do tipo (1), a expressão (6) passa a ser 



No segundo membro de (7) podem-se colocar em evidência os coeficientes _ci_ , resultando 



Neste exemplo, relativo ao polinómio de grau 5 indicado em (1), pretende-se que a expressão de _J_ (8) seja exactamente igual à de _I_ (5) 



Igualando os segundos membros de (5) e de (8) resulta 

75 

_<u>Quadratura de Gauss</u> - Álvaro F. M. Azevedo_ 



Uma vez que os coeficientes _ci_ são arbitrários, para que a igualdade (10) se verifique sempre, é suficiente que 



Para obter os valores de _P1_ , _P2_ , _P3_ , _W1_ , _W2_ e _W3_ , resolve-se o sistema de seis equações não lineares a seis incógnitas (11). A respectiva solução é 



O valor exacto do integral de um polinómio de grau 5, no intervalo [-1,1], pode ser obtido com 



No caso de a função _f_ ( _x_ ) ser genérica, i.e., não polinomial ou polinomial de grau superior a 5, a expressão (13) fornece um valor aproximado do integral _I_ (2). 

76 

_<u>Quadratura de Gauss</u> - Álvaro F. M. Azevedo_ 



O valor do integral calculado com o segundo membro de (14) é tanto mais correcto, quanto mais a função _f_ ( _x_ ) se aproximar de um polinómio do tipo (1). Se se desejar um valor mais correcto para o integral, existe a possibilidade de se utilizar mais pontos de amostragem ( _Pi_ ) e correspondentes pesos ( _Wi_ ). Os pontos de amostragem também são designados por pontos de Gauss. 

O estudo que foi aqui realizado com um polinómio de grau 5 pode ser feito, de um modo semelhante, com polinómios de qualquer grau. Na Tabela 5.2 apresenta-se os resultados que se obtêm quando se faz o estudo com polinómios de grau 1, grau 3, grau 5 e grau 7. 

Em [5.2] encontra-se uma tabela que fornece os valores das posições dos pontos de amostragem e dos pesos para um número de pontos de Gauss no intervalo [1,10]. 

Com base na Tabela 5.2 podem-se extrair as seguintes conclusões: 

- com _n_ pontos de Gauss, obtém-se o valor exacto do integral de um polinómio de grau _p_ = 2 _n_ - 1, ou inferior; 

- quando se pretende a solução exacta do integral de um polinómio de grau _p_ , o número de pontos de Gauss que se tem de utilizar é _n_ = ( _p_ + 1) / 2, ou superior. Nota: quando _p_ é par, deve-se substituir o seu valor pelo número ímpar imediatamente superior. 

Nota: o intervalo de integração de todos os integrais referidos no âmbito da quadratura de Gauss é o intervalo [-1,1]. 

77 

_<u>Quadratura de Gauss</u> - Álvaro F. M. Azevedo_ 

Tabela 5.2 - Posições dos pontos de amostragem e respectivos pesos. 

|Número de|Grau do polinómio que é possível|Posiçõ|es d|os pontos de Gauss|
|---|---|---|---|---|
|pontos de Gauss|integrar de um modo exacto|e respe|ctiv|os pesos|
|_n_|_p_= 2_n_-1|_P_|_i_,_W_|_i_|
|1|1|1<br>1<br>_W_<br>_P_|=<br>=|2<br>0|
|||1<br>_P_|=|3<br>1<br>−|
|2|3|1<br>2<br>_W_<br>_P_|=<br>=|1<br>3<br>1|
|||2<br>_W_|=|1|
|||1<br>_P_|=|5<br>3<br>−|
|||2<br>_P_|=|0|
|3|5|1<br>3<br>_W_<br>_P_|=<br>=|9<br>5<br>5<br>3|
|||2<br>_W_|=|9<br>8|
|||3<br>_W_|=|9<br>5|
|||1<br>_P_|=|63116<br>0.86113<br>−|
|||2<br>_P_|=|10436<br>33998<br>.0<br>−|
|||3<br>_P_|=|10436<br>33998<br>.0|
|||4<br>_P_|=|63116<br>0.86113|
|4|7|1<br>_W_|=|48451<br>0.34785|
|||2<br>_W_|=|51549<br>0.65214|
|||3<br>_W_|=|51549<br>0.65214|
|||4<br>_W_|=|48451<br>0.34785|



Para justificar a expressão _p_ = 2 _n_ - 1 (ver a Tabela 5.2) é suficiente considerar o seguinte (sugere-se que se acompanhem as seguintes considerações com o exemplo do polinómio de grau _p_ = 5, atrás descrito): 

- suponha-se que se pretende integrar de um modo exacto um polinómio de grau _p_ (sendo _p_ um número ímpar); 

78 

_<u>Quadratura de Gauss</u> - Álvaro F. M. Azevedo_ 

- o número de coeficientes _ci_ no polinómio de grau _p_ é igual a _p_ + 1; 

- uma vez que existem _p_ + 1 coeficientes _ci_ , o sistema de equações não lineares (11) vai ter _p_ + 1 equações; 

- para que o sistema de equações (11) possa ser resolvido, o número de incógnitas deve ser também _p_ + 1; 

- uma vez que as incógnitas são as posições dos pontos de Gauss e respectivos pesos ( _P_ 1, _P_ 2, _P_ 3,..., _W_ 1, _W_ 2, _W_ 3,...), o número de pontos de Gauss ( _n_ ) tem de ser metade do número de incógnitas ( _p_ + 1), i.e., _n_ = ( _p_ + 1) / 2; 

- nesta expressão pode-se explicitar _p_ , resultando _p_ = 2 _n_ - 1, que é o resultado que se pretendia demonstrar. Qualquer que seja o valor de _n_ , o valor de _p_ que se obtém é sempre um número ímpar. É por este motivo que, conforme foi atrás referido, se deve passar _p_ para o valor ímpar imediatamente superior, quando se utiliza a expressão _n_ = ( _p_ + 1) / 2 e o valor de _p_ é par. 

A expressão genérica da quadratura de Gauss com _n_ pontos é 



### **5.3 - Integrais múltiplos** 

Apresenta-se em seguida a adaptação da integração numérica descrita na secção anterior ao caso do integral duplo 



Considerando em primeiro lugar o integral em ordem a _x_ , tem-se, de acordo com (15) 

sendo _nx_ o número de pontos de Gauss utilizados na direcção _x_ . 

79 

_<u>Quadratura de Gauss</u> - Álvaro F. M. Azevedo_ 

Considerando que a função integranda de (17) é uma função _g_ ( _y_ ), tem-se 



com 



Substituindo agora o integral em ordem a _y_ em (18) por um somatório do tipo (15), resulta 



sendo _ny_ o número de pontos de Gauss utilizados na direcção _y_ . 

Atendendo a (19), a expressão (20) passa a ser 



que é equivalente a 



O número de pontos de Gauss associados à direcção _x_ ( _nx_ ) pode ser diferente do número de pontos de Gauss associados à direcção _y_ ( _ny_ ). A selecção destes números deve atender ao modo como a função _f_ ( _x_ , _y_ ) varia com _x_ e com _y_ . Assim, se na direcção _x_ a função _f_ ( _x_ , _y_ ) se assemelhar a um polinómio de grau 5 e na direcção _y_ a um de grau 7, deve ser _nx_ = 3 e _ny_ = 4 (ver a Tabela 5.2). 

No caso do integral triplo, pode-se generalizar (22), resultando 



80 

_<u>Quadratura de Gauss</u> - Álvaro F. M. Azevedo_ 

No caso do integral do produto das funções _f_ e _g_ , tem-se 



o que permite uma avaliação sequencial de _f_ e _g_ no ponto de Gauss ( _Pi_ , _Pj_ , _Pk_ ). Esta consideração é extensiva a qualquer combinação de funções, e.g., adição, divisão, etc. Quando se tem, por exemplo, o integral de um produto de matrizes, pode-se avaliar cada uma das matrizes em cada ponto de Gauss e só em seguida fazer o produto matricial. Assim se evita ter de explicitar a função que resulta do produto matricial de diversas funções. 

### **5.4 - Considerações finais** 

O procedimento de integração numérica genericamente designado quadratura de Gauss tem como principal vantagem o facto de poder ser facilmente incluído num programa de computador destinado à análise de estruturas pelo MEF. A principal dificuldade associada à sua utilização reside na necessidade de escolher um número de pontos de Gauss adequado à precisão pretendida. 

### **BIBLIOGRAFIA** 

[5.1] - Cook, R. D.; Malkus, D. S.; Plesha, M. E.; Witt, R. J. - Concepts and Applications of Finite Element Analysis, Fourth Edition, John Wiley & Sons, Inc., 2002. 

[5.2] - Zienkiewicz, O. C.; Taylor, R. L. - The Finite Element Method, Fourth Edition, McGraw-Hill, 1988. 

81 

_<u>Quadratura de Gauss</u> - Álvaro F. M. Azevedo_ 

82 

### CAPÍTULO 6 

### ESTADO PLANO DE TENSÃO 

Neste capítulo é descrita com pormenor a formulação de elementos finitos destinados à discretização de problemas de análise de estruturas que se enquadram no caso particular designado "Estado Plano de Tensão" [6.1]. Apresenta-se em primeiro lugar o caso do elemento finito quadrado de dimensões fixas, seguindo-se o elemento finito rectangular _L_ 1 x _L_ 2 e, por último, o caso mais geral de geometria arbitrária. 

A formulação aqui descrita baseia-se no método dos deslocamentos e na discretização do domínio em elementos finitos de _n_ nós, apresentando algumas semelhanças com o que foi descrito no Capítulo 4. 

### **6.1 - Simbologia** 

Apresenta-se em primeiro lugar um resumo da simbologia adoptada na formulação do método dos elementos finitos. 

Tabela 6.1 - Simbologia relativa ao método dos elementos finitos. 

|_L_|Dimensão do elemento finito|
|---|---|
|_n_|Número de nós do elemento finito|
|_x_|Coordenada cartesiana|
|_u_|Campo de deslocamentos|
|_a_|Deslocamento nodal|
|_h_|Espessura do elemento finito laminar|
|_~~x~~_|Coordenada cartesiana de um nó de um elemento finito|
|_m_|Número de direcções consideradas (no estado plano de tensão:_m_= 2)|
|_N_|Função interpoladora ou função de forma|



83 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

|_c_|Coeficiente de um termo de um polinómio|
|---|---|
|_p_|Número de graus de liberdade do elemento finito (_p_=_n_x_m_)|
|ε|Extensão|
|γ|Distorção|
|_L_|Operador diferencial|
|_q_|Número de componentes do vector ε<br>e do vector σ|
|_B_|Matriz de deformação|
|_V_|Volume do elemento finito laminar|
|σ|Tensão normal|
|τ|Tensão tangencial|
|_p_|Acção exterior distribuída por unidade de comprimento|
|_S_|Superfície do elemento finito laminar|
|_E_|Módulo de elasticidade ou módulo de Young|
|ν|Coeficiente de Poisson|
|_D_|Matriz de elasticidade (<br>ε<br>σ<br>_D_<br>=<br>)|
|_K_|Matriz de rigidez do elemento finito no referencial geral|
|_F_|Forças nodais equivalentes à acção exterior, nos graus de liberdade do<br>elemento finito, no referencial geral|
|_s_|Coordenada local (curvilínea)|
|_~~s~~_|Coordenada local de um nó de um elemento finito|
|_NV_|Vector das funções interpoladoras ou funções de forma|
|_J_|Jacobiano da transformação|
|_E_|Módulo de elasticidade num nó do elemento finito|
|~~ν~~|Coeficiente de Poisson num nó do elemento finito|
|_h_|Espessura do elemento finito num nó|



84 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

|_P_|Posição de um ponto de Gauss ou ponto de amostragem|
|---|---|
|_W_|Peso (_weight_) associado a um ponto de Gauss ou ponto de amostragem|
|_nGPi_|Número de pontos de Gauss associado à direcção_si_|
|_J_|Valor do integral calculado de acordo com a quadratura de Gauss|



### **6.2 - Funções interpoladoras ou funções de forma** 

Na Figura 6.1 encontra-se representado um elemento finito quadrado com quatro nós e com dimensões _L_ 1 x _L_ 2 = 2 x 2. 



<!-- Start of picture text -->
a 42 x 2 a 32 u 2 ( x 1 ,  x 2)<br>a 41 a 31<br>4<br>u 1 ( x 1 ,  x 2)<br>3<br>x 1<br>L 2 = 2<br>a 12 a 22<br>a 11 a 21<br>1 L 1 = 2 2 h  ( x 1 ,  x 2)<br><!-- End of picture text -->

Fig. 6.1 - Elemento finito quadrado de quatro nós. 

As coordenadas dos nós são armazenadas na matriz _~~<u>x</u>~~_ , cujo elemento genérico<sup>_~~x~~_</sup> _ij_ corresponde à coordenada cartesiana do nó _i_ segundo a direcção _xj_ . 



De acordo com a simbologia atrás apresentada, a matriz _~~<u>x</u>~~_ tem dimensões _n_ x _m_ . 

A espessura do elemento finito laminar representado na Figura 6.1 é designada por _h_ , que pode também ser uma função de _x_ 1 e de _x_ 2. 

85 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

A função _<u>u</u>_ <u>(</u> _<u>x</u>_ ) corresponde ao campo de deslocamentos, verificando-se o seguinte 



Cada uma das componentes de _<u>u</u>_ <u>(</u> _<u>x</u>_ ) é interpolada separadamente com base em funções de forma _Ni_ ( _x_ 1, _x_ 2) e nos deslocamentos dos nós (ver a Figura 6.1) 



Em (3) e (4), bem como na Figura 6.1, _aij_ corresponde ao deslocamento do nó _i_ segundo a direcção _xj_ . Note-se que o número de funções de forma _Ni_ coincide com o número de nós do elemento finito ( _n_ ). 

As considerações que se seguem serão apenas efectuadas com a componente _u_ 1 do campo de deslocamentos. A sua extensão à componente _u_ 2 seria trivial. 

A função _u_ 1( _x_ 1, _x_ 2) deve assumir nos nós os valores nodais do campo de deslocamentos. Atendendo às coordenadas dos nós indicadas em (1), pretende-se que 



Para que as condições expressas em (5) sejam respeitadas, as funções de forma a utilizar em (3) devem possuir as características indicadas na Tabela 6.2. 

86 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

Tabela 6.2 - Características das funções _Ni_ ( _x_ 1, _x_ 2). 

|Nó|1|2|3|4|
|---|---|---|---|---|
|(_x_1,_x_2)|(-1, -1)|(+1, -1)|(+1, +1)|(-1, +1)|
|_N_1(_x_1,_x_2)|1|0|0|0|
|_N_2(_x_1,_x_2)|0|1|0|0|
|_N_3(_x_1,_x_2)|0|0|1|0|
|_N_4(_x_1,_x_2)|0|0|0|1|



As seguintes funções polinomiais respeitam as condições indicadas na Tabela 6.2, que consistem no facto da a função _Ni_ ter de assumir um valor unitário no nó _i_ e um valor nulo nos restantes nós. 



A função _N_ 1 ( _x_ 1, _x_ 2) pode tomar a seguinte forma 



Um polinómio de segundo grau completo tem a seguinte expressão genérica 



Comparando (7) com (8), verifica-se que a função de forma _N_ 1 ( _x_ 1, _x_ 2) é um polinómio de segundo grau incompleto, porque lhe faltam os termos que em (8) se encontram sublinhados. Considerações idênticas poderiam ser feitas em relação às restantes funções de forma. 

87 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

Armazenando os deslocamentos nodais da seguinte forma 



tem-se, atendendo a (3) e a (4) 



que em notação matricial se reduz a 



sendo _p_ = _n_ x _m_ (no caso da Figura 6.1, _p_ = 4 x 2 = 8). 

A matriz _<u>N</u>_ é 



Os gráficos das funções _Ni_ ( _x_ 1, _x_ 2), definidas em (6), encontram-se representados na Figura 6.2 (ver também a Figura 6.1). 

No caso do elemento finito rectangular de dimensões _L_ 1 x _L_ 2, representado na Figura 6.3, as funções de forma seriam 

88 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 





<!-- Start of picture text -->
N 1 N 4<br>1<br>4<br>x 2 x 2<br>x 1 x 1<br>N 2 N 3<br>2<br>x 2 x 2<br>x 1 x 1 3<br><!-- End of picture text -->

Fig. 6.2 - Gráficos das funções _Ni_ ( _x_ 1, _x_ 2) para um elemento de dimensões _L_ 1 x _L_ 2 = 2 x 2. 

89 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
a 42 x 2 a 32 u 2 ( x 1 ,  x 2)<br>a 41 a 31<br>4<br>u 1 ( x 1 ,  x 2)<br>3<br>x 1<br>L 2<br>a 12 a 22<br>a 11 a 21<br>1 L 1 2 h  ( x 1 ,  x 2)<br><!-- End of picture text -->

Fig. 6.3 - Elemento finito rectangular de quatro nós. 

### **6.3 - Campo de deformações** 

O campo de deformações num estado plano de tensão é definido do seguinte modo [6.1] 



ou de um modo mais compacto 



Em (15), _q_ é o número de componentes do vector <u>ε ,</u> que são neste caso três, e _<u>L</u>_ é o seguinte operador diferencial 



90 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

Substituindo (11) em (15), tem-se 



Designando por _<u>B</u>_ o produto _<u>L N</u>_ 



a expressão (17) passa a 



sendo, de acordo com (18), (16) e (12) 





No caso do elemento com dimensões _L_ 1 x _L_ 2 = 2 x 2, a matriz _<u>B</u>_ é constituída pelas derivadas de (6), de acordo com (21) 



No caso do elemento de dimensões _L_ 1 x _L_ 2, a matriz _<u>B</u>_ é constituída pelas derivadas de (13), de acordo com (21) 

91 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 



### **6.4 - Princípio dos trabalhos virtuais** 

Considere-se um estado plano de tensão constituído por um elemento finito formulado de acordo com o que foi exposto nas secções anteriores. Supondo que apenas existem acções distribuídas por unidade de comprimento na periferia do elemento finito, do Princípio dos Trabalhos Virtuais (PTV), que foi exposto no Capítulo 4, resulta a seguinte equação 



Nesta expressão o vector <u>δε</u> apresenta componentes em correspondência com o vector <u>ε , definido em (14) e (15). O vector σ</u> é o seguinte 



### **6.5 - Matriz de rigidez e vector solicitação** 

Com base no princípio dos trabalhos virtuais referido na secção anterior, vai-se em seguida proceder à dedução das expressões da matriz de rigidez e do vector solicitação que são utilizados no método dos deslocamentos, aplicado à análise de um estado plano de tensão. 

Designando por _h_ a espessura do elemento finito, tem-se em (24) 



92 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

em que _dS_ representa o elemento de superfície. 

A equação (19) referida à deformação virtual é a seguinte 



que é equivalente a 



A relação entre tensões e deformações é, para um estado plano de tensão e no caso dos materiais isotrópicos [6.1] 



ou de um modo mais compacto 



sendo a matriz de elasticidade _<u>D</u>_ a seguinte 



A matriz de elasticidade _<u>D</u>_ depende do módulo de Young ( _E_ ) e do coeficiente de Poisson ( ν ). 

Substituindo (19) em (30) tem-se 



A equação (11) referida à deformação virtual é a seguinte 

93 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

δ _<u>u</u>_ = _<u>N</u>_ δ _<u>a</u>_ (33) 

que é equivalente a 



Substituindo todas estas equações em (24) passa a ter-se o PTV expresso por 



Uma vez que _dS_ = _dx_ 1 _dx_ 2 e os deslocamentos nodais não dependem das variáveis _x_ 1 _T_ e _x_ 2, os vectores δ _<u>a</u>_ e _<u>a</u>_ podem passar para fora do integral 



De acordo com o PTV, a equação (36) é verdadeira para qualquer conjunto de deslocamentos virtuais, concluindo-se assim que 



Comparando esta equação com a relação de rigidez que é utilizada no método dos deslocamentos 



tem-se, no caso do estado plano de tensão 





O vector _<u>a</u>_ encontra-se definido em (9). 

Nas expressões (37)-(40) admite-se que as seguintes grandezas podem não ser constantes no domínio de integração: módulo de Young ( _E_ ), coeficiente de Poisson ( ν ), espessura ( _h_ ) e carga distribuída ( _<u>p</u>_ ). 

94 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

No caso do elemento finito rectangular representado na Figura 6.3, a expressão da matriz de rigidez (39) passa a ser 



A matriz _<u>B</u>_ corresponde à expressão (23) e, no caso dos materiais isotrópicos, a matriz _<u>D</u>_ é dada por (31). 

Uma vez que _h_ é um escalar, as dimensões da matriz _<u>K</u>_ coincidem com as do produto _<u>BT D B</u>_ 



No caso do elemento finito de quatro nós, tem-se 



Atendendo a (40), as dimensões do vector solicitação _<u>F</u>_ coincidem com as do produto _<u>N</u> T_ _<u>p</u>_ 



No caso do elemento finito de quatro nós, tem-se 



### **6.5.1 - Cálculo de um elemento da matriz de rigidez** 

Apresenta-se em seguida o cálculo do elemento _K_ 58 da matriz de rigidez do elemento finito representado na Figura 6.1, com _E_ = 200 000 MPa, ν = 0 e _h_ = 0.3 m. De acordo com (41), tem-se 

95 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 



O cálculo de _<u>BT D B</u>_ pode ser efectuado com base nos somatórios correspondentes aos produtos matriciais 



sendo _q_ = 3. 

Para calcular _K_ 58 é suficiente desenvolver os somatórios para o caso: _i_ = 5; _j_ = 8 







Consultando as matrizes _<u>B</u>_ (22) e _<u>D</u>_ (31) com ν = 0, verifica-se facilmente que, neste exemplo, só o último monómio de (50) é não nulo. Assim, tem-se 



Atendendo a (22) e (31) e ao facto de ser _E_ = 200 000, chega-se a 



Atendendo a (46) e ao facto de ser _h_ = 0.3 m, tem-se 

96 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 



### **6.5.2 - Cálculo do vector solicitação correspondente a uma carga distribuída** 

Na Figura 6.4 encontra-se representado o elemento finito da Figura 6.1, sujeito a uma carga distribuída no bordo 2-3. 



<!-- Start of picture text -->
p 1 p 2<br>4 3 4 MN/m 9 MN/m<br>x 2 dL<br>L 2 = 2 x 1<br>1 L 1 = 2 2 2 MN/m 3 MN/m<br><!-- End of picture text -->

Fig. 6.4 - Elemento finito sujeito a uma carga distribuída. 

As forças nodais equivalentes à acção distribuída no bordo calculam-se com a expressão (40), que aqui se reproduz 



sendo _<u>N</u>_ a matriz (12) e _<u>p</u>_ o seguinte vector 



97 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

Neste exemplo, _dL_ coincide com _dx_ 2 e todos os pontos do domínio de integração apresentam coordenada _x_ 1 = 1. Assim, o integral de linha (57) passa a ser 



e nos elementos da matriz _<u>N</u>_ , que são as funções de forma (6), deve-se substituir _x_ 1 por 1, obtendo-se 



Atendendo a (12) e a (58), o produto _<u>N</u> T_ _<u>p</u>_ que figura em (59) é o seguinte 



Para os valores das acções indicados na Figura 6.4, são as seguintes as expressões das funções _p_ 1 e _p_ 2 



Com base em (61), (60) e (62), tem-se 

98 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 



resultando de (59) 



Em (64), _Fij_ representa a componente de _<u>F</u>_ que está associada ao nó _i_ e que actua na direcção _xj_ . 

Nos nós 1 e 4, são nulas as componentes da força nodal equivalente à carga distribuída no bordo 2-3. 

Neste exemplo simples, os valores indicados em (64) coincidem com as reacções que se obteriam numa viga simplesmente apoiada carregada com as cargas trapezoidais da Figura 6.4. 

### **6.6 - Caso geral com substituição de variáveis** 

O estudo apresentado nas secções anteriores e que se encontra limitado a um elemento quadrado de dimensões 2 x 2 pode ser facilmente estendido a elementos rectangulares de dimensões _L_ 1 x _L_ 2. Toda a sua formulação seria uma extensão trivial do que foi atrás 

99 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

apresentado. Nesta secção é desenvolvido um elemento finito quadrilátero de geometria arbitrária, destinado à discretização de estados planos de tensão (ver a Figura 6.5). 



<!-- Start of picture text -->
x 2 a 32 u 2 ( x 1 ,  x 2)<br>a 31<br>a 42 u 1 ( x 1 ,  x 2)<br>3<br>a 41<br>4<br>a 22<br>a 12<br>a 21<br>a 11 h  ( x 1 ,  x 2)<br>2<br>1<br>x 1<br><!-- End of picture text -->

Fig. 6.5 - Elemento finito quadrilátero de quatro nós com geometria arbitrária. 

As coordenadas dos nós são armazenadas na matriz _~~<u>x</u>~~_ , cujo elemento genérico<sup>_~~x~~_</sup> _ij_ corresponde à coordenada cartesiana do nó _i_ segundo a direcção _xj_ . 



De acordo com a simbologia apresentada na Secção 6.1, a matriz _~~<u>x</u>~~_ tem dimensões _n_ x _m_ . 

A espessura do elemento finito laminar representado na Figura 6.5 é designada por _h_ , que pode também ser uma função de _x_ 1 e de _x_ 2. 

A determinação da matriz de rigidez do elemento finito com a expressão (39), requer neste caso o cálculo de um integral duplo com um domínio de integração _S_ , que corresponde a um quadrilátero irregular de geometria definida pelos quatro nós do elemento. Tendo em vista a sistematização deste processo, de modo a facilitar a sua programação em computador, revela-se muito vantajoso efectuar a seguinte substituição das variáveis _x_ 1 e _x_ 2. 

100 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 



Na Figura 6.6 encontra-se representado o novo domínio de integração, que corresponde ao intervalo [-1, 1], quer para a variável _s_ 1, quer para _s_ 2. 



<!-- Start of picture text -->
x 2 s 2<br>3<br>4 3<br>1<br>4<br>s 1<br>1<br>2<br>2<br>1 1<br>1 1<br>x 1<br><!-- End of picture text -->

Fig. 6.6 - Substituição das variáveis _x_ 1 e _x_ 2. 

Os valores nodais das coordenadas _s_ 1 e _s_ 2 são os seguintes 



De acordo com (66), a cada ponto ( _s_ 1, _s_ 2) corresponde um ponto ( _x_ 1, _x_ 2). A passagem do sistema de coordenadas _s_ para o sistema de coordenadas _x_ é efectuada com uma interpolação semelhante à que foi efectuada na Secção 6.2 para o campo de deslocamentos. De acordo com (3) e (4), tem-se 



No sistema de coordenadas _s_ , as funções de forma coincidem com as que foram descritas na Secção 6.2, bastando substituir em (6) _x_ 1 por _s_ 1 e _x_ 2 por _s_ 2, resultando 

101 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 



Tal como no caso do campo de deslocamentos, ao atribuir a ( _s_ 1, _s_ 2) os valores nodais indicados em (67), obtêm-se em (68) e (69) as coordenadas dos nós (65). 

Por exemplo, para ( _s_ 1, _s_ 2) = (1, 1), a função _N_ 3 vale um e as restantes são nulas, obtendo-se em (68) _x_ 1 ( 1,1 ) = _~~x~~_ 31 e em (69) _x_ 2 ( 1,1 ) = _~~x~~_ 32 . 

As equações (68) e (69) podem ser colocadas em forma matricial do seguinte modo 



ou 



sendo 





Em (72), _~~<u>x</u>~~_ é a matriz _n_ x _m_ definida em (65). 

Após a substituição de variáveis indicada em (66), o integral (39) passa a ser 

102 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 



Nesta expressão _J_ é o determinante Jacobiano, que corresponde ao determinante da matriz Jacobiana _<u>J</u>_ <u>.</u> A matriz Jacobiana correspondente à transformação (66) é definida da seguinte forma [6.2] 





Para permitir o cálculo do integral (75), todos os componentes da função integranda têm de depender de _s_ 1 e _s_ 2. 

Se a matriz _<u>D</u>_ (31) não for constante, é possível utilizar o mesmo tipo de interpolação para definir _E_ e ν em função de _s_ 1 e _s_ 2. 



Nesta expressão,<sup>_E_</sup> _i_<sup>e</sup><sup>~~ν~~</sup> _i_ são os valores no nó _i_ do módulo de Young e do coeficiente de Poisson. Na generalidade dos casos práticos _E_ e ν são considerados constantes ao nível de cada elemento finito. Quando uma estrutura apresenta mais do que um tipo de material, a fronteira entre as zonas correspondentes a cada material deve coincidir com a transição entre elementos finitos. 

Se a espessura do elemento não for constante pode ser interpolada de um modo semelhante 



103 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

Nesta expressão,<sup>_h_</sup> _i_<sup>é o valor da espessura no nó</sup><sup>_i_.</sup> 

Os elementos da matriz Jacobiana (76) obtêm-se por derivação de (68) e (69), resultando 



As equações (81)-(84) são equivalentes à seguinte equação matricial 



De um modo mais compacto, tem-se 



sendo 

104 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 



As expressões dos elementos da matriz (87) obtêm-se por derivação de (70) em ordem a _s_ 1 e _s_ 2. resultando 



Substituindo as expressões (88) em (85), obtêm-se os elementos da matriz Jacobiana em função de _s_ 1 e _s_ 2. Nota: os elementos da matriz _~~<u>x</u>~~_ são as coordenadas cartesianas dos nós, sendo portanto constantes de valor conhecido. 

Tendo em vista o cálculo do integral (75) encontram-se já definidos em função de _s_ 1 e _s_ 2 todos os componentes da função integranda, com excepção da matriz _<u>B</u>_ . Apresenta-se em seguida o procedimento para a sua obtenção. 

No caso do elemento finito quadrilátero de quatro nós e de geometria arbitrária, as equações (9)-(12) permanecem válidas (ver as Secções 6.2 e 6.3). As equações (10) e (11) são em seguida reproduzidas. 



105 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 



No caso do elemento de geometria arbitrária, as funções de forma _<u>N</u>_ dependem das variáveis _s_ 1 e _s_ 2. Neste caso, a interpolação dos deslocamentos (89) é efectuada de um modo coincidente com o que foi utilizado para interpolar as coordenadas cartesianas dos nós (68) e (69). Quando o método de interpolação dos deslocamentos nodais e das coordenadas cartesianas dos nós coincidem, diz-se que a formulação do elemento finito 

### é **<u>isoparamétrica</u>** <u>.</u> 

O campo de deformações obtém-se de um modo semelhante ao que foi descrito na Secção 6.3, reproduzindo-se em seguida as equações mais significativas. 



Por substituição de (90) em (91) chega-se a 











106 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

A matriz _<u>B</u>_ depende das derivadas das funções de forma em ordem a _xj_ (∂ _Ni_ ∂ _x j_ ) . De modo a ser possível calcular o integral (75), é necessário obter as expressões de ∂ _Ni_ ∂ _x j_ em função de _s_ 1 e _s_ 2. 

Considere-se uma das funções de forma ( _Ni_ ) dependendo de _x_ 1 e _x_ 2, que por sua vez dependem de _s_ 1 e _s_ 2. 



Pela regra da cadeia tem-se 



que se pode escrever da seguinte forma em notação matricial 



Atribuindo ao índice _i_ os valores 1 a 4 e agrupando os quatro casos nas seguintes matrizes, chega-se a 



que de um modo mais compacto se pode escrever 



107 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

sendo _<u>J</u>_ a matriz Jacobiana definida em (76) e em (86). 

Multiplicando ambos os membros de (101), à direita, por _<u>J</u>_ − 1 obtém-se 



A matriz ∂ _<u>N</u>_ ∂ _<u>s</u>_ foi definida em (87) e (88), sendo os seus elementos funções de _s_ 1 e _s_ 2. Em (86) pode verificar-se que os elementos da matriz _<u>J</u>_ são também funções de _s_ 1 e _s_ 2. Os elementos da seguinte matriz, que dependem de _s_ 1 e _s_ 2, 



são depois espalhados na matriz _<u>B</u>_ de acordo com (96). 

Deste modo se alcançou o objectivo de calcular os elementos da matriz _<u>B</u>_ como sendo funções de _s_ 1 e _s_ 2. 

Uma vez que todos os componentes da função integranda de (75) se encontram definidos em função de _s_ 1 e _s_ 2, é agora possível proceder ao cálculo da matriz de rigidez do elemento finito. O facto de se tratar de um integral de difícil resolução e de os limites de integração serem -1 e +1, sugere o recurso à técnica de integração numérica que se encontra descrita no Capítulo 5. 

### **6.7 - Algoritmo de cálculo da matriz de rigidez de um elemento isoparamétrico** 

Um integral duplo, cujos limites de integração sejam -1 e +1 para ambas as variáveis, pode ser calculado pela quadratura de Gauss, sendo o resultado obtido, em geral, um valor aproximado. De acordo com o que foi exposto no Capítulo 5, a correspondente expressão é a seguinte 

108 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 



Nesta expressão, _nGP_ 1 é o número de pontos de Gauss associado à direcção _s_ 1 e _nGP_ 2 é o número correspondente à direcção _s_ 2. Os parâmetros _Wi_ e _Wj_ são os pesos associados às direcções _s_ 1 e _s_ 2. A função _f_ deve ser avaliada nos pontos de Gauss, cujas coordenadas são 



De aqui em diante, o segundo membro de (104) passa a ser designado por _J_ . Assim, no caso de ser _nGP_ 1 = 2 e _nGP_ 2 = 2, da expansão dos somatórios em (104) resulta a seguinte expressão para _J_ 





De acordo com o que foi exposto no Capítulo 5, os valores dos pesos _Wi_ e das posições _Pi_ é neste caso 



passando _J_ a ser avaliado do seguinte modo 



O valor aproximado do integral duplo (104), depende do resultado da avaliação da função _f_ ( _s_ 1, _s_ 2) em quatro pontos de Gauss, cuja localização se encontra na Figura 6.7. 

109 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
s 2<br>4 3<br>1<br>3 4 s 1<br>1 2<br>1<br>→ Ponto de Gauss<br>2<br>1<br>1 1<br><!-- End of picture text -->

Fig. 6.7 - Localização dos quatro pontos de Gauss no sistema de coordenadas ( _s_ 1, _s_ 2). 

De acordo com (107), para calcular o valor aproximado do integral (75), recorrendo à quadratura de Gauss com 2 x 2 pontos, procede-se do seguinte modo: 

- avalia-se a sua função integranda nos quatro pontos de Gauss; 

- multiplica-se o resultado correspondente a cada ponto de Gauss pelos respectivos pesos (que neste caso são unitários); 

- e somam-se as quatro parcelas. 

Como se pode verificar em (75), a função integranda é um produto de matrizes de funções, que é em seguida multiplicado por funções escalares. Atendendo às características da quadratura de Gauss, é possível avaliar todos os elementos de cada matriz em cada ponto de Gauss e só em seguida fazer o produto matricial, bem como o produto pelas funções escalares avaliadas também nesse ponto de Gauss. Deste modo os produtos matriciais são efectuados com valores numéricos em vez de funções, facilitando assim a programação deste algoritmo em computador. 

Apresenta-se em seguida a sequência de operações que têm de ser efectuadas para calcular a matriz de rigidez de um elemento finito quadrilátero, recorrendo à quadratura de Gauss com 2 x 2 pontos. 

Dados: 

- coordenadas cartesianas dos nós (<sup>_~~x~~_</sup> _ij_<sup>);</sup> 

- espessura do elemento finito em cada nó (<sup>_h_</sup> _i_<sup>);</sup> 

110 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

- módulo de Young ( _E_ - constante em todo o elemento finito); 

- coeficiente de Poisson ( ν - constante em todo o elemento finito). 

### Algoritmo: 

- Inicializar a matriz _~~<u>x</u>~~_ com as coordenadas cartesianas dos nós do elemento finito (65) 

- Inicializar o vector _<u>h</u>_ com as espessuras do elemento finito nos nós 

- Inicializar uma tabela com os pesos associados a cada ponto de Gauss 

|P. de Gauss|_Wi_|_Wj_|
|---|---|---|
|1|1.0|1.0|
|2|1.0|1.0|
|3|1.0|1.0|
|4|1.0|1.0|



- Inicializar uma tabela com as coordenadas de cada ponto de Gauss (ver a Figura 6.7) 

|P. de Gauss|_Pi_|_Pj_|
|---|---|---|
|1|-0.57735...|-0.57735...|
|2|+0.57735...|-0.57735...|
|3|-0.57735...|+0.57735...|
|4|+0.57735...|+0.57735...|



- Calcular os elementos da matriz _<u>D</u>_ , recorrendo a (31) 

- Inicializar com valor nulo todos os elementos da matriz de rigidez _<u>K</u>_ , cuja dimensão é 8 x 8 

- Para cada ponto de Gauss ( _s_ 1, _s_ 2) = ( _Pi_ , _Pj_ ): 

   - Avaliar as funções de forma _Ni_ no ponto ( _Pi_ , _Pj_ ), recorrendo a (70) 

   - Calcular a espessura _h_ no ponto ( _Pi_ , _Pj_ ), recorrendo a (80) 

   - Calcular os elementos da matriz ∂ _<u>N</u>_ ∂ _<u>s</u>_ no ponto ( _Pi_ , _Pj_ ), recorrendo a (88) 

   - Calcular os elementos da matriz Jacobiana ( _<u>J</u>_ ) no ponto ( _Pi_ , _Pj_ ), recorrendo a (85) 

   - Calcular o determinante da matriz Jacobiana ( _J_ ) 

   - Calcular a inversa da matriz Jacobiana _<u>J</u>_ − 1 ( ) 

   - Calcular a matriz ∂ _<u>N</u>_ ∂ _<u>x</u>_ no ponto ( _Pi_ , _Pj_ ), recorrendo a (102) 

111 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

   - Espalhar os elementos da matriz ∂ _<u>N</u>_ ∂ _<u>x</u>_ (103) na matriz _<u>B</u>_ de acordo com (96) 

   - Calcular _<u>B</u> T_ _<u>D B</u> h J_ , que consiste num produto de matrizes e escalares avaliados no ponto ( _Pi_ , _Pj_ ) (75), do qual resulta uma matriz com as dimensões da matriz de rigidez _<u>K</u>_ <u>, que se designa por</u> _<u>K</u>_ ′ 

   - Multiplicar todos os elementos de _<u>K</u>_ ′ pelos pesos _Wi Wj_ correspondentes ao ponto de Gauss corrente 

   - Adicionar _Wi W j_ _<u>K</u>_ ′ à matriz de rigidez do elemento finito ( _<u>K</u>_ ). 

- Fim do ciclo estendido aos pontos de Gauss. 

### **6.8 - Cálculo das tensões e deformações finais** 

Depois de resolvido o sistema de equações _<u>K a</u>_ = _<u>F</u>_ , com _<u>K</u>_ , _<u>a</u>_ e _<u>F</u>_ referentes à totalidade dos graus de liberdade da estrutura, é possível calcular o estado de tensão e deformação em qualquer ponto de qualquer elemento. Apesar de a formulação permitir o cálculo de tensões e extensões em qualquer ponto, verifica-se que existe uma muito maior precisão se os pontos seleccionados coincidirem com os pontos de Gauss correspondentes à quadratura de Gauss com 2 x 2 pontos [6.3]. Este facto é independente do número de pontos de Gauss que foi utilizado no cálculo dos componentes de _<u>K</u>_ e _<u>F</u>_ . Assim, deve-se proceder do seguinte modo para calcular as deformações e tensões num ponto de um elemento finito: 

- seleccionar o elemento finito que vai ser alvo do estudo; 

- nesse elemento, seleccionar o ponto de Gauss em que se pretende conhecer o estado de tensão; 

- calcular a matriz _<u>B</u>_ no ponto seleccionado, cujas coordenadas são 



- com base no vector que contém todos os deslocamentos, extrair para um vector de oito componentes os deslocamentos dos nós do elemento que está a ser estudado ( _<u>a</u>_ ); 

- calcular o vector deformação ( <u>ε</u> ) com a expressão (94); 

112 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

- calcular a matriz de elasticidade ( _<u>D</u>_ ) com a expressão (31); 

- calcular o vector tensão ( <u>σ</u> ) com a expressão (30); 

Depois de obtidos os valores de <u>σ</u> e <u>ε</u> nos pontos de Gauss (2 x 2), é possível fazer a sua interpolação ou extrapolação para outros pontos do elemento, nomeadamente para os seus nós [6.4]. Desta forma se obtêm resultados mais precisos do que aqueles que se obteriam com a avaliação directa das tensões no ponto pretendido. 

### **6.9 - Considerações finais** 

Neste capítulo foi apresentado o modo de obter a matriz de rigidez de um elemento finito quadrilátero de geometria arbitrária, destinado à discretização de estados planos de tensão. Foi apresentado com detalhe o caso do elemento de quatro nós e da quadratura de Gauss com 2 x 2 pontos. Alguns aspectos importantes são deixados para outros capítulos, tais como a assemblagem da matriz de rigidez global, o desenvolvimento de elementos com mais do que quatro nós, a influência do número de pontos de Gauss na qualidade dos resultados, o cálculo de acções nodais equivalentes a acções concentradas, distribuidas e de volume, etc. 

### **BIBLIOGRAFIA** 

[6.1] - Azevedo, A. F. M. - Mecânica dos Sólidos, Faculdade de Engenharia da Universidade do Porto, 1996. 

[6.2] - Kreyszig, E. - Advanced Engineering Mathematics, Sixth Edition, John Wiley & Sons, Inc., 1988. 

[6.3] - Zienkiewicz, O. C.; Taylor, R. L. - The Finite Element Method, Fourth Edition, McGraw-Hill, 1988. 

[6.4] - Cook, R. D.; Malkus, D. S.; Plesha, M. E.; Witt, R. J. - Concepts and Applications of Finite Element Analysis, Fourth Edition, John Wiley & Sons, Inc., 2002. 

113 

_Estado Plano de Tensão - Álvaro F. M. Azevedo_ 

114 

### CAPÍTULO 7 

### FUNÇÕES INTERPOLADORAS 

Neste capítulo são descritos diversos modos de obtenção de funções interpoladoras, também designadas funções de forma. São apresentados exemplos relativos a meios unidimensionais, bidimensionais e tridimensionais. As funções de forma obtidas por procedimentos genéricos podem depois ser utilizadas em distintas formulações do método dos elementos finitos. 

### **7.1 - Simbologia** 

Apresenta-se em primeiro lugar um resumo da simbologia adoptada no âmbito da determinação de funções interpoladoras. 

Tabela 7.1 - Simbologia relativa à determinação de funções interpoladoras. 

|_x_|Coordenada cartesiana|
|---|---|
|_~~x~~_|Coordenada cartesiana de um nó de um elemento finito|
|_u_|Campo de deslocamentos|
|_a_|Deslocamento nodal|
|_N_|Função interpoladora ou função de forma|
|_n_|Número de nós do elemento finito|
|_L_|Dimensão do elemento finito|
|_s_|Coordenada local (curvilínea)|
|_h_|Espessura do elemento finito laminar|
|_h_|Espessura do elemento finito num nó|
|_~~s~~_|Coordenada local de um nó de um elemento finito|
|_NV_|Vector das funções interpoladoras ou funções de forma|



115 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

|_V_|Vector contendo os factores não constantes de um polinómio|
|---|---|
|_c_|Coeficiente de um termo de um polinómio|
|_Q_|Matriz cujas colunas contêm o vector _V_<br>avaliado em nós do elemento finito|
|_p_|Número de nós de um bordo de um elemento finito|
|∆|Deslocamento de um nó de um elemento finito|
|θ|Rotação de um nó de um elemento finito|



### **7.2 - Caso unidimensional** 

Na Figura 7.1 encontra-se representado um elemento finito unidimensional com quatro nós colocados sobre o eixo _x_ . A posição de cada nó é definida pela respectiva coordenada cartesiana<sup>_~~x~~_</sup> _i_<sup>, sendo</sup><sup>_i_o número do nó.</sup> 



<!-- Start of picture text -->
u  ( x )<br>a 1 a 2 a 3 a 4<br>x<br>1 2 3 4<br>( x = x 1 ) ( x = x 2 ) ( x = x 3 ) ( x = x 4 )<br><!-- End of picture text -->

Fig. 7.1 - Elemento finito unidimensional de geometria arbitrária. 

As características essenciais de uma função de forma _Ni_ são as seguintes: 

- deve assumir o valor unitário para _x_ =<sup>_~~x~~_</sup> _i_ ; 

- deve anular-se nos restantes nós. 

É também desejável, no caso das funções polinomiais, manter o grau do polinómio tão baixo quanto possível. 

Na Tabela 7.2 encontram-se os valores que cada função de forma deve assumir nos nós do elemento finito. 

116 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

Tabela 7.2 - Características das funções _N_ 1( _x_ ) , _N_ 2( _x_ ) , _N_ 3( _x_ ) e _N_ 4( _x_ ). 

|_x_|1<sup>_~~x~~_</sup>|2<sup>_~~x~~_</sup>|3<sup>_~~x~~_</sup>|4<sup>_~~x~~_</sup>|
|---|---|---|---|---|
|_N_1(_x_)|1|0|0|0|
|_N_2(_x_)|0|1|0|0|
|_N_3(_x_)|0|0|1|0|
|_N_4(_x_)|0|0|0|1|



É fácil verificar que as seguintes funções de forma são polinómios que respeitam as condições definidas na Tabela 7.2. 



A expressão genérica para o caso de um elemento finito unidimensional com _n_ nós é 



A expressão (5) é designada fórmula de interpolação de Lagrange [7.1], sendo as expressões (1)-(4) o caso particular de (5), quando _n_ = 4. 

Se em (5) se considerar _n_ = 2, _~~x~~_ 1 = − 1 e _~~x~~_ 2<sup>=</sup> 1, obtêm-se as funções de forma que foram determinadas no Capítulo 4 para o caso da barra de dois nós e comprimento _L_ = 2. De um modo semelhante seria possível verificar a coincidência 

117 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

entre as restantes funções de forma determinadas no Capítulo 4 e as que se obtêm com (5). 

### **7.3 - Caso bidimensional** 

Considere-se agora o elemento finito bidimensional com 16 nós representado na Figura 7.2. 



<!-- Start of picture text -->
s 2<br>13 14 15 16<br>2/3<br>s 1<br>9 10 11 12<br>2/3<br>2/3 5 6 7 8<br>1 2 3 4<br>2/3 2/3 2/3<br><!-- End of picture text -->

Fig. 7.2 - Elemento finito bidimensional com 16 nós. 

Relativamente ao elemento finito de 16 nós, pretende-se obter a função de forma _N_ 7 ( _s_ 1, _s_ 2). Esta função deve ser unitária no nó 7 e deve anular-se nos restantes nós. As coordenadas do nó 7 são ( _s_ 1, _s_ 2) = (1/3, -1/3). 

Na direcção _s_ 1, o nó 7 é o terceiro nó. Por isso deve-se utilizar a função _N_ 3 indicada em (3) e considerar _x_ =<sup>_s_</sup> 1 , _~~x~~_ 1 = − 1 , _~~x~~_ 2 = − 1 3 , _~~x~~_ 3<sup>=</sup> 1 3 e _~~x~~_ 4<sup>=</sup> 1. Esta função é designada _N_ 31 e tem a seguinte expressão 

118 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 



Os índices em _N_ 31 têm o significado de função de forma unidimensional correspondente ao nó 3 e com _x_ substituido por _s_ 1. 

Na direcção _s_ 2, o nó 7 é o segundo nó. Por isso deve-se utilizar a função _N_ 2 indicada em (2), considerar _x_ =<sup>_s_</sup> 2 e, de igual forma, _~~x~~_ 1 = − 1 , _~~x~~_ 2 = − 1 3 , _~~x~~_ 3<sup>=</sup> 1 3 e _~~x~~_ 4<sup>=</sup> 1. Esta função é designada _N_ 22 e tem a seguinte expressão 



A função _N_ 7 ( _s_ 1, _s_ 2) é o produto de (7) por (9) 



Como se pode facilmente verificar, esta função de forma assume o valor unitário no nó 7 e anula-se nos restantes nós. As funções de forma correspondentes aos restantes 15 nós poderiam ser obtidas de um modo idêntico ao que foi aqui apresentado. Na Figura 7.3 encontra-se, em perspectiva, o gráfico da função _N_ 7 ( _s_ 1, _s_ 2). 

119 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
N 7 ( s 1,  s 2)<br>s 2<br>s 1<br><!-- End of picture text -->

Fig. 7.3 - Gráfico da função de forma _N_ 7 ( _s_ 1, _s_ 2). 

A expressão (11) é equivalente à seguinte 



120 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

O triângulo de Pascal correspondente a uma função de duas variáveis é o seguinte 



<!-- Start of picture text -->
1<br>s 1 s 2<br>2 2<br>s 1 s 1 s 2 s 2<br>3 2 2 3<br>s 1 s 1 s 2 s 1 s 2 s 2 (13)<br>4 3 2 2 3 4<br>s 1 s 1 s 2 s 1 s 2 s 1 s 2 s 2<br>5 4 3 2 2 3 4 5<br>s 1 s 1 s 2 s 1 s 2 s 1 s 2 s 1 s 2 s 2<br>6 5 4 2 3 3 2 4 5 6<br>s 1 s 1 s 2 s 1 s 2 s 1 s 2 s 1 s 2 s 1 s 2 s 2<br><!-- End of picture text -->

Comparando (12) com o triângulo de Pascal representado em (13), pode observar-se que a função de forma _N_ 7 ( _s_ 1, _s_ 2) é um polinómio de sexto grau incompleto, em que foram utilizados apenas os 16 termos que figuram em (12). 

### **7.4 - Procedimento genérico para determinar as funções de forma** 

Apresenta-se em seguida um procedimento que permite determinar as funções de forma de um elemento finito com _n_ nós arbitrariamente distribuídos [7.2]. A exposição que se segue baseia-se num exemplo, que consiste num elemento finito de cinco nós posicionados de acordo com a Figura 7.4. 



<!-- Start of picture text -->
s 2<br>5 4 3<br>1 h 5 h 4 h 3<br>s 1<br>1<br>h 1 h 2<br>1 2 h  ( s 1 ,  s 2)<br>1 1<br><!-- End of picture text -->

Fig. 7.4 - Elemento finito com cinco nós. 

As coordenadas dos cinco nós do elemento finito são, no sistema de eixos ( _s_ 1, _s_ 2) 

121 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 



Pretende-se fazer a interpolação do campo de espessuras _h_ ( _s_ 1, _s_ 2), sendo utilizada a seguinte expressão, em que<sup>_h_</sup> _i_<sup>representa a espessura do elemento finito no nó</sup><sup>_i_.</sup> 



Recorrendo à notação matricial, a equação (15) passa a 



ou 



sendo 





122 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

Tendo em vista a determinação das cinco funções de forma polinomiais _Ni_ , é necessário seleccionar no triângulo de Pascal um número de termos igual ao número de nós do elemento finito. Por este motivo, o exemplo da Figura 7.4 requer a escolha de cinco termos, que devem ser de grau tão baixo quanto possível. No triângulo de Pascal atrás apresentado (13), são assim seleccionados os seguintes termos, que se agrupam num vector designado por _<u>V</u>_ 



Na selecção efectuada, foi dada preferência a termos de grau mais elevado em _s_ 1 do que em _s_ 2, devido ao facto de o elemento finito apresentar mais nós segundo a direcção _s_ 1. De acordo com a selecção de termos efectuada, a função _h_ ( _s_ 1, _s_ 2) vai ser aproximada com o seguinte polinómio 



que em notação matricial se escreve 



ou 



sendo 

123 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 



Ao efectuar em (22) a substituição das variáveis _s_ 1 e _s_ 2 pelas coordenadas do nó 1, pretende-se obter o valor da espessura _h_ no nó 1 ( _h_ 1 ) 



Procedendo de igual forma com os restantes nós e agrupando as cinco expressões do tipo (25) numa única expressão matricial, tem-se 



ou 



sendo 



124 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

No caso do exemplo da Figura 7.4 e de acordo com (14), os elementos de _<u>Q</u>_ são 



Uma vez que a matriz _<u>Q</u>_ é quadrada e se supõe não singular, pode-se multiplicar, à direita, ambos os membros de (27) por _<u>Q</u>_ − 1 , resultando 



Substituindo o segundo membro de (30) em (23) resulta 



Uma vez que são iguais os segundos membros de (17) e (31), e uma vez que o vector de espessuras ( _<u>h</u>_ ) é arbitrário, conclui-se que 



No caso do exemplo da Figura 7.4, a inversa da matriz _<u>Q</u>_ (29) é 



resultando 

125 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 



As funções de forma são 



Existem alguns casos em que, devido à localização dos nós ou devido à incorrecta selecção de termos no triângulo de Pascal, a matriz _<u>Q</u>_ resulta singular. Nestes casos o procedimento aqui descrito não pode ser utilizado. 

### **7.5 - Elementos bidimensionais: famílias Lagrangeana e** **_serendipity_** 

O procedimento descrito na Secção 7.4 encontra-se bem definido, com excepção do facto de ser necessário seleccionar, em cada caso, um adequado conjunto de termos no triângulo de Pascal. Nos casos em que não existe um critério óbvio, é conveniente ensaiar várias alternativas. De cada conjunto de termos do triângulo de Pascal vai resultar uma distinta formulação do elemento finito, sendo conveniente averiguar qual é a que conduz a resultados mais precisos. Para as situações mais comuns existem já formulações que conduzem a bons resultados, sendo em seguida apresentados dois desses casos, que são designados de elementos da família Lagrangeana e elementos da família _serendipity_ [7.2]. 

126 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

Os elementos bidimensionais da família Lagrangeana são quadriláteros com _p_<sup>2</sup> nós, sendo _p_ o número de nós de um bordo (ver a Figura 7.5). 



<!-- Start of picture text -->
s 2 s 2 s 2<br>s 1 s 1 s 1<br>L 2 = 2<br>L 1 = 2 L 1 = 2 L 1 = 2<br>p  = 2 p  = 3 p  = 4<br><!-- End of picture text -->

Fig. 7.5 - Elementos finitos bidimensionais da família Lagrangeana. 

As funções de forma do elemento Lagrangeano com _p_ = 4 foram já apresentadas na Secção 7.3. Quando se determinam as funções de forma com o procedimento genérico descrito na Secção 7.4, deve-se seleccionar os termos do triângulo de Pascal com o critério definido na Figura 7.6. 



<!-- Start of picture text -->
1 p  = 2<br>s 1 s 2 p  = 3<br>2 2<br>s 1 s 1 s 2 s 2 p  = 4<br>3 2 2 3<br>s 1 s 1 s 2 s 1 s 2 s 2<br>4 3 2 2 3 4<br>s 1 s 1 s 2 s 1 s 2 s 1 s 2 s 2<br>5 4 3 2 2 3 4 5<br>s 1 s 1 s 2 s 1 s 2 s 1 s 2 s 1 s 2 s 2<br>6 5 4 2 3 3 2 4 5 6<br>s 1 s 1 s 2 s 1 s 2 s 1 s 2 s 1 s 2 s 1 s 2 s 2<br><!-- End of picture text -->

Fig. 7.6 - Selecção de termos no triângulo de Pascal para elementos finitos bidimensionais da família Lagrangeana. 

Como se pode observar na Figura 7.6, o critério de selecção de termos no triângulo de Pascal é facilmente extensível a valores superiores de _p_ . 

127 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

Apresentam-se na Figura 7.7 alguns exemplos de elementos finitos da família _serendipity_ . 



<!-- Start of picture text -->
s 2 s 2 s 2<br>s 1 s 1 s 1<br>L 2 = 2<br>L 1 = 2 L 1 = 2 L 1 = 2<br>p  = 2 p  = 3 p  = 4<br>Fig. 7.7 - Elementos finitos bidimensionais da família  serendipity .<br>O número de nós de cada elemento da família  serendipity  é 4 (  p  - 1 ), sendo  p  o número<br>de nós de um bordo.<br>Na Figura 7.8 encontra-se o critério de selecção de termos no triângulo de Pascal para o<br>caso de elementos da família  serendipity .<br>p  = 2 1 p  = 2<br>p  = 3 s 1 s 2 p  = 3<br>2 2<br>p  = 4 s 1 s 1 s 2 s 2 p  = 4<br>3 2 2 3<br>p  = 5 s 1 s 1 s 2 s 1 s 2 s 2 p  = 5<br>4 3 2 2 3 4<br>p  = 6 s 1 s 1 s 2 s 1 s 2 s 1 s 2 s 2 p  = 6<br>5 4 3 2 2 3 4 5<br>s 1 s 1 s 2 s 1 s 2 s 1 s 2 s 1 s 2 s 2<br>6 5 4 2 3 3 2 4 5 6<br>s 1 s 1 s 2 s 1 s 2 s 1 s 2 s 1 s 2 s 1 s 2 s 2<br><!-- End of picture text -->

O número de nós de cada elemento da família _serendipity_ é 4 ( _p_ - 1 ), sendo _p_ o número de nós de um bordo. 

Na Figura 7.8 encontra-se o critério de selecção de termos no triângulo de Pascal para o caso de elementos da família _serendipity_ . 

Fig. 7.8 - Selecção de termos no triângulo de Pascal para elementos finitos bidimensionais da família _serendipity_ . 

128 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

De cada vez que _p_ é incrementado uma unidade, são acrescentados quatro nós ao elemento finito (um em cada bordo) e são seleccionados mais quatro termos no triângulo de Pascal. Este critério é extensível a qualquer valor de _p_ . 

Na prática, os elementos finitos que apresentam um bom compromisso entre o número de nós e a qualidade dos resultados obtidos são os da família _serendipity_ , com oito nós ( _p_ = 3). Apresenta-se na Figura 7.9 um exemplo de um destes elementos finitos no referencial ( _x_ 1, _x_ 2). 



<!-- Start of picture text -->
x 2<br>p  = 3<br>x 1<br><!-- End of picture text -->

Fig. 7.9 - Elemento finito de 8 nós da família _serendipity_ . 

Quando comparado com o quadrilátero de quatro nós, o elemento finito representado na Figura 7.9 tem a vantagem de ser mais preciso e de se adaptar bem a fronteiras curvilíneas. 

Apresenta-se em seguida um exemplo de um elemento finito que apresenta mais nós na direcção _s_ 2 do que na direcção _s_ 1 (ver a Figura 7.10). 

129 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
s 2<br>s 1<br>L 2 = 2<br>L 1 = 2<br><!-- End of picture text -->

Fig. 7.10 - Elemento finito bidimensional com oito nós. 

Tendo em vista a determinação das funções de forma do elemento finito representado na Figura 7.10, devem ser seleccionados os termos do triângulo de Pascal que se encontram assinalados na Figura 7.11. 



<!-- Start of picture text -->
1<br>s 1 s 2<br>2 2<br>s 1 s 1 s 2 s 2<br>3 2 2 3<br>s 1 s 1 s 2 s 1 s 2 s 2<br>4 3 2 2 3 4<br>s 1 s 1 s 2 s 1 s 2 s 1 s 2 s 2<br><!-- End of picture text -->

Fig. 7.11 - Selecção de termos no triângulo de Pascal para o elemento finito bidimensional representado na Figura 7.10. 

São preferidos termos de grau mais elevado em _s_ 2, porque o elemento possui mais nós na direcção _s_ 2 do que na direcção _s_ 1. 

### **7.6 - Propriedades das funções interpoladoras** 

Considere-se o elemento finito de três nós representado na Figura 7.12. 

130 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
u  ( x )<br>a 1 a 2 a 3<br>x<br>1 2 3<br>( x = x 1 ) ( x = x 2 ) ( x = x 3 )<br><!-- End of picture text -->

Fig. 7.12 - Elemento finito unidimensional de geometria arbitrária. 

Supondo que não é efectuada qualquer substituição de variável, a interpolação do campo de deslocamentos é efectuada da seguinte forma 



Admita-se agora que em todos os nós é imposto o mesmo deslocamento ∆ . 



Neste caso pretende-se que a função interpolada _u_ ( _x_ ) seja uma função constante 



em todos os pontos do elemento finito. 

Substituindo (41) e (42) em (40), resulta 





sendo _n_ o número de nós do elemento finito. 

A equação (45) constitui uma propriedade que as funções de forma devem possuir. Só assim se garante que uma translação do elemento finito é correctamente interpolada com a equação (40). 

131 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

É fácil constatar que todos os conjuntos de funções de forma apresentados nos Capítulos 4 e 6 possuem a propriedade (45). 

Outra questão que se coloca é a de definir um procedimento que garanta que as funções interpoladoras que se pretende determinar possuam a propriedade (45). Com este objectivo considere-se a expressão que define as funções interpoladoras (32) 



Multiplicando ambos os membros de (46) por _<u>Q</u>_ obtém-se 



que no exemplo da Figura 7.4 corresponde a (ver a Secção 7.4) 



Como se pode verificar em (48), se no triângulo de Pascal o elemento unitário do seu vértice for o primeiro dos termos seleccionados, então o primeiro elemento do vector _<u>V</u>_ é sempre unitário e a primeira linha da matriz _<u>Q</u>_ tem todos os elementos também unitários. A primeira das cinco equações a que (48) corresponde é 



As funções de forma determinadas com (46) respeitam as condições (48) e (49). Assim fica provado que sempre que o termo unitário do triângulo de Pascal é seleccionado, então as funções de forma obtidas possuem a propriedade (45). 

### **7.7 - Interpolação Hermitiana** 

Em todas as interpolações que foram efectuadas nas secções anteriores apenas se atendeu aos valores nodais das funções. Na interpolação Hermitiana, que é descrita 

132 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

nesta secção, são também consideradas as derivadas das funções nos nós. Este tipo de interpolação tem interesse para a formulação de elementos finitos em que são consideradas as rotações (e.g., vigas, lajes). 

Na Figura 7.13 encontra-se um elemento finito com dois nós e comprimento _L_ . A função _u_ ( _x_ ) corresponde ao deslocamento vertical, cujos valores nodais são ∆ 1 e ∆ 2. Nos nós 1 e 2 a rotação é θ 1 e θ 2, respectivamente. 



<!-- Start of picture text -->
a 4 =  θ 2<br>a 2 =  θ 1 u  ( x )<br>a 3 =  ∆ 2<br>a 1 =  ∆ 1<br>x<br>1 2<br>( x = x 1 = − L 2 ) L  / 2 L  / 2 ( x = x 2 = L 2 )<br><!-- End of picture text -->

Fig. 7.13 - Interpolação Hermitiana num elemento unidimensional com dois nós. 

Os deslocamentos generalizados dos nós do elemento finito representado na Figura 7.13 são os seguintes 



De acordo com a Figura 7.13 e designando _du_ / _dx_ por _u_ ′( _x_ ) , tem-se 



Uma vez que as rotações são muito pequenas, supõe-se 

133 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 



Pretende-se determinar a função _u_ ( _x_ ) que respeita as condições (51). Com esse objectivo, admite-se que a função _u_ ( _x_ ) é o seguinte polinómio de grau 3 



que em notação matricial corresponde a 



ou 



sendo 



e 



Derivando ambos os membros de (53) obtém-se 



que em notação matricial corresponde a 

134 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 



ou 



sendo 



Para que (51) se verifique quando as funções _u_ e _u'_ são (54) e (59), é necessário que 







135 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

Agrupando (62)-(65) numa única expressão matricial, resulta 



ou 



sendo _<u>a</u>_ definido por (50), _<u>c</u>_ definido por (56) e _<u>Q</u>_ definido por 



Verifica-se assim que as colunas da matriz _<u>Q</u>_ são constituídas pelos vectores _<u>V</u>_ (57) e _<u>V</u>_ ' (61) avaliados nos pontos nodais<sup>_~~x~~_</sup> 1<sup>e</sup><sup>_~~x~~_</sup> 2<sup>.</sup> 

No caso da Figura 7.13 tem-se 



Multiplicando, à direita, ambos os membros de (67) por _<u>Q</u>_ − 1 resulta 



136 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

A matriz inversa de (69) é 



Substituindo (70) em (55) obtém-se 



A interpolação que se pretende definir deve ter as seguintes características 



que em notação matricial corresponde a 



ou 



sendo _<u>a</u>_ definido por (50) e 



Uma vez que são iguais os segundos membros de (72) e (75), e uma vez que o vector dos deslocamentos nodais ( _<u>a</u>_ ) é arbitrário, conclui-se que 



137 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

No caso do exemplo da Figura 7.13, as funções de forma obtêm-se fazendo o produto de (71) por (57), resultando 







No caso particular de ser _L_ = 2, as funções de forma são as seguintes 





Os gráficos das funções (82)-(85) encontram-se representados na Figura 7.14 

138 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
N 1 ( x ) N 2 ( x )<br>1 1<br>x x<br>-1 1 -1 1<br>N 3 ( x ) N 4 ( x )<br>1 1<br>x x<br>-1 1 -1 1<br><!-- End of picture text -->

Fig. 7.14 - Gráficos das funções _Ni_ ( _x_ ) correspondentes ao elemento de dois nós com comprimento _L_ = 2. 

Apresenta-se em seguida o caso da interpolação Hermitiana de um elemento de três nós. O elemento considerado tem comprimento _L_ = 2 e o nó intermédio centrado (ver a Figura 7.15). 



<!-- Start of picture text -->
u  ( x )<br>a 6 =  θ 3<br>a 2 =  θ 1 a 4 =  θ 2<br>a 3 =  ∆ 2 a 5 =  ∆ 3<br>a 1 =  ∆ 1<br>x<br>1 2 3<br>( x = x 1 = − 1 ) ( x = x 2 = 0 ) ( x = x 3 = 1 )<br>L  = 2<br><!-- End of picture text -->

Fig. 7.15 - Interpolação Hermitiana num elemento unidimensional com três nós. 

139 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

O vector dos deslocamentos generalizados é 



A função _u_ ( _x_ ) que respeita as condições indicadas na Figura 7.15 é 







A derivada da função _u_ ( _x_ ) é 





140 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

A matriz _<u>Q</u>_ é neste caso a seguinte 



De acordo com as coordenadas indicadas na Figura 7.15, tem-se 





Atendendo a (77), tem-se 





141 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 







Os gráficos das funções (98)-(103) encontram-se representados na Figura 7.16. 

### **7.8 - Considerações finais** 

Neste capítulo foram apresentados alguns procedimentos destinados à determinação de funções de forma. Sempre que os procedimentos mais simples não sejam aplicáveis, deve-se utilizar um dos métodos genéricos descritos nas Secções 7.4 e 7.7. A metodologia descrita na Secção 7.4 pode ser facilmente adaptada aos casos tridimensionais. Neste caso, no lugar do triângulo de Pascal tem-se uma pirâmide em cujo vértice figura o elemento unitário, seguido de um segundo nível em que figuram as variáveis _s_ 1, _s_ 2 e _s_ 3, etc. 

142 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
N 1 ( x ) N 2 ( x )<br>1 1<br>x x<br>-1 1 -1 1<br>N 3 ( x ) N 4 ( x )<br>1<br>1<br>x x<br>-1 1 -1 1<br>N 5 ( x ) N 6 ( x )<br>1 1<br>x x<br>-1 1 -1 1<br><!-- End of picture text -->

Fig. 7.16 - Gráficos das funções _Ni_ ( _x_ ) correspondentes ao elemento de três nós com comprimento _L_ = 2. 

### **BIBLIOGRAFIA** 

[7.1] - Cook, R. D.; Malkus, D. S.; Plesha, M. E.; Witt, R. J. - Concepts and Applications of Finite Element Analysis, Fourth Edition, John Wiley & Sons, Inc., 2002. 

[7.2] - Zienkiewicz, O. C.; Taylor, R. L. - The Finite Element Method, Fourth Edition, McGraw-Hill, 1988. 

143 

_Funções Interpoladoras - Álvaro F. M. Azevedo_ 

144 

### CAPÍTULO 8 

### ASSEMBLAGEM DE ELEMENTOS FINITOS 

No Capítulo 3, foi apresentado com detalhe o caso da assemblagem de barras em problemas unidimensionais. Neste capítulo apresenta-se de um modo sucinto a adaptação da técnica já descrita ao caso dos elementos finitos com mais do que dois nós e mais do que um grau de liberdade por nó [8.1]. 

### **8.1 - Simbologia** 

Apresenta-se em primeiro lugar a simbologia adoptada na descrição da assemblagem de elementos finitos. 

Tabela 8.1 - Simbologia relativa à assemblagem de elementos finitos. 

|_x_|Coordenada cartesiana|
|---|---|
|_a_|Deslocamentos nodais, nos graus de liberdade da estrutura, no referencial geral|
|_ag_|Deslocamentos nodais, nos graus de liberdade do elemento finito, no<br>referencial geral|
|_K_|Matriz de rigidez da estrutura no referencial geral|
|_Kg_|Matriz de rigidez do elemento finito no referencial geral|
|_F_|Forças nodais equivalentes à acção exterior, nos graus de liberdade da estrutura,<br>no referencial geral|
|_Fg_|Forças nodais equivalentes à acção exterior, nos graus de liberdade do elemento<br>finito, no referencial geral|



145 

_Assemblagem de Elementos Finitos - Álvaro F. M. Azevedo_ 

### **8.2 - Assemblagem da matriz de rigidez global e do vector solicitação** 

Depois de calculadas as matrizes de rigidez de todos os elementos finitos no referencial geral ( _<u>Kg</u>_<sup>),énecessárioprocederaocálculodamatrizderigidezglobalda</sup> estrutura ( _<u>K</u>_ ). Uma operação semelhante tem de ser efectuada com os vectores solicitação dos diversos elementos finitos. 

A assemblagem das matrizes de rigidez dos diversos elementos finitos na matriz de rigidez global é em seguida apresentada com base no exemplo da Figura 8.1. 



<!-- Start of picture text -->
a 2 a 4 a 6<br>a 1 a 3 a 5<br>1 2 B 3<br>A<br>a 8 a 10 C a 12<br>x 2<br>a 7 a 9 a 11<br>4 5 6<br>x 1<br><!-- End of picture text -->

Fig. 8.1 - Estrutura constituída por um elemento de 4 nós ( _A_ ), um elemento de 2 nós ( _B_ ) e um elemento de 3 nós ( _C_ ). 

A estrutura representada na Figura 8.1 tem seis nós (1 a 6) e três elementos finitos ( _A_ , _B_ e _C_ ). O elemento _A_ tem quatro nós, o elemento _B_ tem dois nós e o elemento _C_ tem três nós. Em cada nó existem dois graus de liberdade. Em correspondência com os doze graus de liberdade da estrutura existem doze deslocamentos nodais ( _<u>a</u>_ ) e doze forças nodais equivalentes à acção exterior ( _<u>F</u>_ ). 

146 

_Assemblagem de Elementos Finitos - Álvaro F. M. Azevedo_ 



De acordo com (1), nas considerações que se seguem é adoptada a numeração dos graus de liberdade de 1 a 12. 

Na relação de rigidez correspondente à estrutura 



a matriz de rigidez global ( _<u>K</u>_ ) é uma matriz 12 x 12. 

Nas Figuras 8.2, 8.3 e 8.4 encontram-se representados os elementos finitos que vão ser assemblados e a respectiva numeração local (nós e graus de liberdade). 



<!-- Start of picture text -->
a 8 a 6<br>a 7 a 5<br>4 3<br>A<br>a 2 a 4<br>a 1 a 3<br>1 2<br><!-- End of picture text -->

Fig. 8.2 - Numerações locais do elemento finito de 4 nós ( _A_ ). 

147 

_Assemblagem de Elementos Finitos - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
a 2 a 4<br>a 1 a 3<br>1 2<br>B<br><!-- End of picture text -->

Fig. 8.3 - Numerações locais do elemento finito de 2 nós ( _B_ ). 



<!-- Start of picture text -->
a 6<br>a 5<br>3<br>a 2 C a 4<br>a 1 a 3<br>1 2<br><!-- End of picture text -->

Fig. 8.4 - Numerações locais do elemento finito de 3 nós ( _C_ ). 

São as seguintes as matrizes de rigidez dos três elementos finitos no referencial geral 





148 

_Assemblagem de Elementos Finitos - Álvaro F. M. Azevedo_ 



Atendendo à numeração global dos graus de liberdade indicada na Figura 8.1 (1 a 12), as matrizes de rigidez dos elementos finitos passam a ser 



149 

_Assemblagem de Elementos Finitos - Álvaro F. M. Azevedo_ 



De acordo com o que foi exposto no Capítulo 3, a matriz de rigidez global é a soma de (6), (7) e (8), resultando 

_A B C_ _<u>K</u>_ = _<u>K</u>_ + _<u>K</u>_ + _<u>K</u>_ = 



Em correspondência com os graus de liberdade indicados nas Figuras 8.1 a 8.4, têm-se as forças nodais equivalentes às acções exteriores sobre a estrutura. Assim, e de acordo com o que foi exposto no Capítulo 3, são os seguintes os vectores solicitação correspondentes a cada elemento finito, atendendo à numeração global da estrutura 

150 

_Assemblagem de Elementos Finitos - Álvaro F. M. Azevedo_ 



O vector _<u>F</u>_ é a soma destes três vectores 



A relação de rigidez correspondente à totalidade dos graus de liberdade, no referencial geral, é a seguinte (ver o Capítulo 3) 



151 

_Assemblagem de Elementos Finitos - Álvaro F. M. Azevedo_ 

Depois de acrescentar a (13) as condições de apoio (ver o Capítulo 3), é possível resolver o sistema de equações lineares que daí resulta e obter os deslocamentos segundo todos os graus de liberdade da estrutura. 

### **8.3 - Considerações finais** 

Neste capítulo foi apresentada a assemblagem da matriz de rigidez global com base no armazenamento de todos os seus termos. A matriz de rigidez global apresenta uma distribuição de termos particular, que, quando devidamente explorada, conduz a significativas economias de recursos informáticos, nomeadamente a redução do número de operações de cálculo e a diminuição da quantidade de memória consumida. A característica mais simples de explorar é o facto de a matriz de rigidez global ser simétrica, evitando-se assim o cálculo e o armazenamento dos termos do seu triângulo inferior, bem como todas as operações de cálculo que sobre eles teriam de ser efectuadas. Considerando apenas os termos do triângulo superior, é ainda vantajoso atender ao facto de muitos desses termos serem nulos. O critério de selecção da técnica de armazenamento dos termos da matriz depende do método que vai ser usado para resolver o sistema de equações. As técnicas de armazenamento mais comuns são as seguintes: armazenamento em semibanda de largura constante, armazenamento em semibanda de largura variável, armazenamento em _skyline_ e armazenamento esparso [8.2]. 

### **BIBLIOGRAFIA** 

[8.1] - Zienkiewicz, O. C.; Taylor, R. L. - The Finite Element Method, Fourth Edition, McGraw-Hill, 1988. 

[8.2] - Cook, R. D.; Malkus, D. S.; Plesha, M. E.; Witt, R. J. - Concepts and Applications of Finite Element Analysis, Fourth Edition, John Wiley & Sons, Inc., 2002. 

152 

### CAPÍTULO 9 

### FORÇAS NODAIS EQUIVALENTES 

Quando um elemento finito se encontra sujeito a acções exteriores genéricas é necessário proceder ao cálculo das forças nodais equivalentes à solicitação exterior. Exemplos destas solicitações são as cargas concentradas num ponto do interior do elemento, as cargas distribuídas em bordos, as cargas distribuídas em faces e as forças de volume. Começa-se por apresentar a formulação genérica do cálculo das forças nodais equivalentes, seguindo-se um conjunto de exemplos ilustrativos dos procedimentos que, em cada caso, se devem adoptar. 

### **9.1 - Simbologia** 

Apresenta-se em primeiro lugar um resumo da simbologia adoptada no estudo das forças nodais equivalentes a acções exteriores. 

Tabela 9.1 - Simbologia relativa às forças nodais equivalentes a acções exteriores. 

|_x_|Coordenada cartesiana|
|---|---|
|_P_|Ponto onde actua uma carga concentrada|
|_L_|Arco onde actua uma carga distribuída por unidade de comprimento|
|_S_|Superfície onde actua uma carga distribuída por unidade de superfície|
|_V_|Volume onde actua uma carga distribuída por unidade de volume|
|_Q_|Carga concentrada|
|_p_|Carga distribuída por unidade de comprimento|
|_q_|Carga distribuída por unidade de superfície|
|_b_|Carga distribuída por unidade de volume|
|ε|Extensão|



153 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

|γ|Distorção|
|---|---|
|σ|Tensão normal|
|τ|Tensão tangencial|
|_u_|Campo de deslocamentos|
|_a_|Deslocamento nodal|
|_B_|Matriz de deformação|
|_D_|Matriz de elasticidade (<br>ε<br>σ<br>_D_<br>=<br>)|
|_C_|Elemento da matriz de elasticidade(_D_<br>)|
|_E_|Módulo de elasticidade ou módulo de Young|
|ν|Coeficiente de Poisson|
|_N_|Função interpoladora ou função de forma|
|_K_|Matriz de rigidez do elemento finito no referencial geral|
|_F_|Forças nodais equivalentes à acção exterior, nos graus de liberdade do<br>elemento finito, no referencial geral|
|_s_|Coordenada local (curvilínea)|
|_~~x~~_|Coordenada cartesiana de um nó de um elemento finito|
|_~~s~~_|Coordenada local de um nó de um elemento finito|
|_~~p~~_|Valor nodal da carga distribuída por unidade de comprimento|
|_NV_|Vector das funções interpoladoras ou funções de forma|
|_T_|Matriz de transformação|
|_n_ˆ|Versor|
|_J_|Jacobiano da transformação|
|ρ|Massa específica do material|
|_g_|Aceleração da gravidade|



154 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

|_h_|Espessura do elemento finito laminar|
|---|---|
|_h_|Espessura do elemento finito num nó|



### **9.2 - Expressões genéricas das forças nodais equivalentes** 

Na Figura 9.1 encontra-se representado um corpo tridimensional sujeito a diversos tipos de acções exteriores. 



<!-- Start of picture text -->
Q ( x ) b ( x )<br>p d L q d S<br>d S b d V<br>P<br>p ( x ) q ( x )<br>x 3 d L<br>L S<br>d V<br>x 1 x 2 V<br><!-- End of picture text -->

Fig. 9.1 - Corpo sujeito a diversos tipos de acções exteriores. 

Os tipos de acções indicados na Figura 9.1 são os seguintes: 

- Força generalizada _<u>Q</u>_ <u>(</u> _<u>x</u>_ ) concentrada no ponto _P_ . As componentes de _<u>Q</u>_ <u>(</u> _<u>x</u>_ ) são três forças e três momentos. 

- Acção distribuída por unidade de comprimento _<u>p</u>_ <u>(</u> _<u>x</u>_ ) . Esta carga actua ao longo da linha _L_ , que se encontra definida no espaço e três dimensões. As componentes de _<u>p</u>_ <u>(</u> _<u>x</u>_ ) são três forças por unidade de comprimento e três momentos por unidade de comprimento. 

- Acção distribuída por unidade de superfície _<u>q</u>_ <u>(</u> _<u>x</u>_ ) . Esta carga actua na superfície _S_ , que se encontra definida no espaço e três dimensões. As componentes de _<u>q</u>_ <u>(</u> _<u>x</u>_ ) são três forças por unidade de superfície e três momentos por unidade de superfície. 

155 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

- Força de volume _<u>b</u>_ <u>(</u> _<u>x</u>_ ) . Esta carga actua num volume _V_ , que pode ser apenas uma parte do volume total do corpo. As componentes de _<u>b</u>_ <u>(</u> _<u>x</u>_ ) são três forças por unidade de volume. Em problemas estáticos não são consideradas as componentes de momento por unidade de volume. 

Todos os tipos de acções atrás referidos são definidos como funções das coordenadas cartesianas 



Na Figura 9.1 apenas foi indicado um exemplo de cada tipo de carga. Nas aplicações do MEF é habitual existirem diversos exemplares de cada tipo de carga, e.g., várias cargas concentradas em diferentes pontos do corpo, várias cargas distribuídas em distintas zonas, etc. 

De acordo com o que foi exposto no Capítulo 4, o princípio dos trabalhos virtuais (PTV) estabelece que 

### _Trabalho Interno = Trabalho Externo_ (2) 

Considerando todos os tipos de acções indicados na Figura 9.1 tem-se 



Na exposição que se segue, não são consideradas as rotações nem os momentos. Assim, as componentes das diversas grandezas vectoriais que figuram em (3) são 



156 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 



Na formulação do MEF (ver o Capítulo 6), o campo de deformações é interpolado a partir dos deslocamentos nodais com a seguinte expressão 



Quando esta equação se refere aos deslocamentos virtuais e correspondentes deformações, também virtuais, tem-se 



que é equivalente a 



No caso geral tridimensional e em materiais isotrópicos, a relação entre tensões e deformações é a seguinte [9.1] 



sendo 



157 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

ou de um modo mais compacto 



A matriz de elasticidade _<u>D</u>_ depende do módulo de Young ( _E_ ) e do coeficiente de Poisson ( ν ). 

Substituindo (6) em (11) resulta 



Na formulação do MEF (ver o Capítulo 6), considera-se que a interpolação do campo de deslocamentos a partir dos deslocamentos nodais é efectuada com a seguinte expressão 



A equação (13) referida à deformação virtual é a seguinte 



que é equivalente a 



Substituindo todas estas equações em (3) passa a ter-se o PTV expresso por 



Uma vez que _dV_ = _dx_ 1 _dx_ 2 _dx_ 3 e os deslocamentos nodais não dependem das _T_ variáveis _x_ 1, _x_ 2 e _x_ 3, os vectores δ _<u>a</u>_ e _<u>a</u>_ podem passar para fora dos integrais 

158 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 



De acordo com o PTV, a equação (17) é verdadeira para qualquer conjunto de deslocamentos virtuais, concluindo-se assim que 



Comparando esta equação com a relação de rigidez que é utilizada no método dos deslocamentos 



tem-se, para o caso geral indicado na Figura 9.1 





sendo as forças nodais equivalentes a cada carga as seguintes 



159 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

Exceptuando casos particulares, não se consegue uma precisão aceitável quando se discretiza um corpo com um único elemento finito. Por este motivo, deve-se considerar que as expressões (18)-(25) se referem a um elemento finito e que depois se procede à habitual assemblagem da matriz de rigidez global e do vector solicitação global (ver o Capítulo 8). 

### **9.3 - Força concentrada num ponto interior** 

O cálculo das forças nodais equivalentes a uma acção concentrada num ponto interior ao elemento finito é exemplificado com um elemento de quatro nós para estados planos de tensão (ver a Figura 9.2). 



<!-- Start of picture text -->
x 2<br>a 32 u 2 ( x 1 ,  x 2)<br>s 2<br>a 31<br>a 42 u 1 ( x 1 ,  x 2)<br>3<br>a 41<br>Q 2 s 1<br>4<br>P Q 1<br>a 22<br>a 12<br>a 21 Ponto P = ( x P 1 , x P 2 )<br>a 11<br>2 Ponto P = ( s P 1 , s P 2 )<br>1<br>x 1<br><!-- End of picture text -->

Fig. 9.2 - Elemento finito de quatro nós com uma força concentrado num ponto interior. 

De acordo com os graus de liberdade indicados na Figura 9.2, são os seguintes os vectores dos deslocamentos nodais e das correspondentes forças nodais. 

160 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 



No ponto _P_ encontra-se aplicada uma força exterior com as seguintes componentes 



As coordenadas locais do ponto _P_ são 



As funções de forma do elemento finito são as seguintes (ver o Capítulo 6) 



As forças nodais equivalentes à carga concentrada _<u>Q</u>_ são calculadas com a expressão (22), sendo a matriz _<u>N</u>_ constituída pelas funções de forma (29) avaliadas no ponto (28). 



De todas estas considerações resulta a seguinte expressão para o cálculo das forças nodais equivalentes à força _<u>Q</u>_ 

161 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 



A expressão (31) é facilmente avaliada desde que se conheçam as coordenadas locais ( _s_ 1, _s_ 2) do ponto _P_ . Contudo, na generalidade dos casos práticos o ponto _P_ é definido pelas suas coordenadas cartesianas ( _x_ 1, _x_ 2). Esta questão requer uma operação preliminar, que consiste em calcular as coordenadas locais do ponto _P_ a partir das suas coordenadas cartesianas. Este cálculo é efectuado com base na interpolação das coordenadas cartesianas, que foi apresentada no Capítulo 6, e que em seguida se reproduz 



Em (32),<sup>_~~x~~_</sup> _ij_ representa a coordenada cartesiana do nó _i_ segundo a direcção _xj_ . Substituindo em (32) _x_ 1 e _x_ 2 pelas coordenadas cartesianas do ponto _P_ e _Ni_ pelas funções de forma (29), resulta um sistema de duas equações não lineares com duas incógnitas ( _s_ 1 e _s_ 2). 



que, de um modo mais compacto, se pode escrever da seguinte forma 



162 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

Este sistema de equações não lineares deve, em geral, ser resolvido por um método iterativo (e.g., método de Newton). A sua solução corresponde às coordenadas locais do ponto _P_ ( _~~s~~ P_ 1<sup>,</sup><sup>_~~s~~_</sup> _P_ 2 ) . 

### **9.4 - Carga distribuída por unidade de comprimento** 

Na Figura 9.3 encontra-se representado o elemento finito de oito nós da família _serendipity_ , que, neste caso, se destina à discretização de estados planos de tensão. Num dos bordos existe uma carga distribuída por unidade de comprimento _<u>p</u>_ <u>(</u> _<u>x</u>_ ) . 



<!-- Start of picture text -->
x 2 s 2<br>5<br>6<br>4<br>s 1<br>7<br>8 2<br>3<br>1<br>p ( x )<br>x 1<br><!-- End of picture text -->

Fig. 9.3 - Elemento finito de oito nós com uma carga distribuída por unidade de comprimento. 

As funções de forma do elemento de oito nós são as seguintes 



163 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

As interpolações das grandezas correspondentes ao bordo carregado são efectuadas com as seguintes funções de forma, que se obtêm substituindo _s_ 2 por -1 em (35). Note-se ainda que em todos os pontos do domínio de integração do integral (23) a variável _s_ 2 assume o valor -1. 



Estas funções de forma coincidem com as que foram obtidas no Capítulo 4 para o elemento unidimensional de três nós. 

Na Figura 9.4 está representado o eixo tangente ao bordo (<sup>_x_′</sup> 1 )<sup>, bem como o eixo normal</sup> ao bordo ( _x_ ′ 2 ) . O eixo tangente ao bordo segue a numeração local dos nós. O eixo _x_ ′ 2 forma com<sup>_x_′</sup> 1<sup>um referencial directo.</sup> 



<!-- Start of picture text -->
( s 1 = 0)<br>x 2<br>( s 1 = 1)<br>d L<br>x ′ 2 x ′ 1 2 3<br>L s 1<br>p 2 ′<br>1<br>( s 1 = -1) p 1 ′<br>x 1<br><!-- End of picture text -->

Fig. 9.4 - Bordo de três nós com uma carga distribuída por unidade de comprimento. 

164 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

A carga distribuída _<u>p</u>_ ( _x_ 1<sup>,</sup><sup>_x_</sup> 2 ) é decomposta nas suas componentes tangencial ( _p_ ′ 1 ) e normal ( _p_ ′ 2 ) . Numa análise por elementos finitos são habitualmente conhecidos os valores nodais das componentes tangencial e normal da carga distribuída, que se designam por _~~p~~ ij_ ′ , i.e., valor da carga distribuída no nó _i_ , segundo a direcção<sup>_x_′</sup> _j_<sup>. Todas</sup> as grandezas relativas às cargas distribuídas são forças por unidade de comprimento de arco. 

A interpolação das componentes tangencial e normal da carga distribuída a partir dos correspondentes valores nodais é efectuada da forma habitual, recorrendo às funções de forma (36) 



ou 





Designando por _<u>T</u>_ a matriz de transformação do referencial ( _x_ 1<sup>,</sup><sup>_x_</sup> 2 ) para o referencial ′ ′ ( _x_ 1<sup>,</sup><sup>_x_</sup> 2 ) , tem-se 



e a relação inversa 



Substituindo (39) em (41) chega-se a 



165 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

A primeira linha da matriz de transformação _<u>T</u>_ utilizada em (40) é constituída pelo versor<sup>_n_ˆ</sup> 1<sup>e a segunda pelo versor</sup><sup>_n_ˆ</sup> 2 (ver a Figura 9.5). 



<!-- Start of picture text -->
x 2<br>x ′ 2<br>x ′ 1<br>n ˆ 1<br>n ˆ 2<br>s 1<br>d L<br>d L<br>d x 2<br>d x 1<br>x 1<br><!-- End of picture text -->

Fig. 9.5 - Referencial tangente ao bordo. 

O versor<sup>_n_ˆ</sup> 1<sup>obtém-se com a seguinte expressão</sup> 



sendo _J_ a norma do vector 





O versor<sup>_n_ˆ</sup> 2<sup>é ortogonal a</sup><sup>_n_ˆ</sup> 1<sup>e forma com</sup><sup>_n_ˆ</sup> 1<sup>um referencial directo, sendo a seguinte a</sup> sua expressão 



Os elementos da matriz de transformação _<u>T</u>_ são os seguintes 

166 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 



Os elementos da matriz _<u>T</u>_ são calculados com base na seguinte interpolação das coordenadas de um ponto genérico do arco _L_ . 



Nesta expressão _Ni_ são as funções de forma associadas aos nós do arco (36) e<sup>_~~x~~_</sup> _ij_ representa a coordenada cartesiana do nó _i_ segundo a direcção _xj_ . Derivando ambos os membros em ordem a _s_ 1 chega-se a 



As derivadas em ordem a _s_ 1 das funções de forma (36) são 



Para calcular as forças nodais equivalentes à carga distribuída no bordo deve-se utilizar a expressão (23), que em seguida se reproduz 



167 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

Para facilitar o recurso à quadratura de Gauss (ver o Capítulo 5), deve ser efectuada a seguinte mudança de variável 



De acordo com a Figura 9.5, verifica-se que 



Atendendo a (47), tem-se 



Substituindo (53) em (52), chega-se a 



Comparando (54) com (44), conclui-se que 



e a expressão (51) passa a ser 



Substituindo (42) em (56), obtém-se 



Uma vez que em todo o domínio de integração se verifica ser _s_ 2 = -1, na matriz _<u>N</u>_ devem ser utilizadas as funções de forma (36). 

168 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

Considerando todas as expressões já deduzidas, o vector das forças nodais equivalentes à carga distribuída indicada nas Figuras 9.3 e 9.4 é o seguinte 



que se simplifica para 



No vector _<u>F</u> p_ apenas as seis primeiras componentes são não nulas, i.e., nos nós 1, 2 e 3 (ver a Figura 9.3) existem forças nodais equivalentes, enquanto que nos restantes cinco nós a contribuição da carga distribuída é nula. 

O integral (59) pode ser calculado recorrendo à quadratura de Gauss (ver o Capítulo 5). 

Todos os componentes da função integranda de (59) são funções de _s_ 1 ou são constantes de valor conhecido, como é o caso da matriz _~~<u>p'</u>~~_ . 

169 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

### **9.5 - Carga distribuída por unidade de superfície** 

O cálculo das forças nodais equivalentes a uma carga distribuída por unidade de superfície é efectuado com a expressão (24). Este tipo de cargas só tem interesse prático em elementos de laje, elementos de casca e faces de elementos sólidos ( _bricks_ ). O processo de cálculo de _<u>F</u> q_ é semelhante ao apresentado na Secção 9.4, sendo necessário adaptá-lo às características dos referidos elementos. O domínio de integração passa a ser uma superfície. 

### **9.6 - Carga distribuída por unidade de volume** 

Este tipo de acção é devido à presença de forças de volume _<u>b</u>_ ( _<u>x</u>_ ). Estas forças estão presentes sempre que o corpo se encontra sujeito a uma aceleração. O caso mais comum é o da aceleração da gravidade que se define do seguinte modo 



Nesta expressão, ρ é a massa específica do material e _<u>g</u>_ é a aceleração da gravidade. No caso mais comum, i.e., supondo que o eixo _x_ 3 é vertical e orientado para cima, que a aceleração da gravidade actua segundo _x_ 3 e é negativa e que se utilizam as unidades do Sistema Internacional ( _SI_ ), tem-se 



Em (61), a aceleração da gravidade foi considerada igual a − .981 _m s_ 2 . 

As unidades de _b_ e de ρ devem ser as seguintes: 

- _bi_ em _N / m_<sup>3</sup> e ρ em _kg / m_<sup>3</sup> , ou 

- _bi_ em _kN / m_<sup>3</sup> e ρ em _t / m_<sup>3</sup> , ou 

- _bi_ em _MN / m_<sup>3</sup> e ρ em _kt / m_<sup>3</sup> . 

Ao definir o peso próprio deste modo, é facilitada a sua combinação com outras componentes da aceleração _<u>g</u>_ . 

170 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

Se a única força de volume for a devida ao peso próprio, então pode-se atribuir a ρ o valor do peso específico do material e considerar _<u>g</u>_ = ( 0,0, − 1 ) . Deste modo fica facilitada a preparação dos dados de uma análise por elementos finitos em que é utilizado um sistema de unidades distinto do _SI_ . 

As forças nodais equivalentes às forças de volume são calculadas com a expressão (25), que em seguida se reproduz 



Na Figura 9.6 encontra-se representado um elemento finito de quatro nós destinado à discretização de estados planos de tensão. 



<!-- Start of picture text -->
x 2<br>a 32 u 2 ( x 1 ,  x 2)<br>s 2 b d V<br>a 31<br>a 42 u 1 ( x 1 ,  x 2)<br>3<br>a 41<br>s 1<br>4 d S d V<br>a 22<br>a 12<br>a 21 h ( s 1 , s 2 )<br>a 11<br>2<br>1<br>x 1<br><!-- End of picture text -->

Fig. 9.6 - Elemento finito de quatro nós sujeito a forças de volume. 

No elemento representado na Figura 9.6 actuam forças de volume _<u>b</u>_ ( _<u>x</u>_ ), cujas componentes são 



No caso do estado plano de tensão, o integral (62) passa a 



171 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

Nesta expresão, _h_ corresponde à espessura do elemento finito, que pode eventualmente ser não constante. A sua interpolação a partir das espessuras nos nós (<sup>_h_</sup> _i_ ) é efectuada com a seguinte expressão (ver o Capítulo 6) 



De um modo semelhante ao que foi efectuado no Capítulo 6 para a matriz de rigidez, deve ser efectuada em (64) a seguinte mudança de variável 



Nesta expressão, _J_ é o determinante Jacobiano definido no Capítulo 6. 

Uma vez que _<u>N</u>_ é a matriz que relaciona os deslocamentos nodais com o campo de deslocamentos ( _<u>u</u>_ = _<u>N a</u>_ ) (ver o Capítulo 6), chega-se à seguinte expressão final 



Nesta expressão, os componentes da função integranda são funções de _s_ 1 e _s_ 2, ou são constantes. 

O integral (67) pode ser calculado recorrendo à quadratura de Gauss (ver o Capítulo 5). 

### **9.7 - Considerações finais** 

As deduções relativas a casos particulares, que foram apresentadas neste capítulo, podem ser facilmente adaptadas a outros casos, tais como elementos finitos com mais nós, outros tipos de elementos finitos, meios com rotações e momentos, etc. 

172 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

### **BIBLIOGRAFIA** 

[9.1] - Azevedo, A. F. M. - Mecânica dos Sólidos, Faculdade de Engenharia da Universidade do Porto, 1996. 

[9.2] - Hinton, E.; Owen, D. R. - Finite Element Programming, Academic Press, 1980. 

[9.3] - Kreyszig, E. - Advanced Engineering Mathematics, Sixth Edition, John Wiley & Sons, Inc., 1988. 

[9.4] - Cook, R. D.; Malkus, D. S.; Plesha, M. E.; Witt, R. J. - Concepts and Applications of Finite Element Analysis, Fourth Edition, John Wiley & Sons, Inc., 2002. 

173 

_Forças Nodais Equivalentes - Álvaro F. M. Azevedo_ 

174 

### CAPÍTULO 10 

SÓLIDOS, ESTADO PLANO DE DEFORMAÇÃO E AXISSIMETRIA 

Neste capítulo são descritas algumas particularidades dos elementos sólidos tridimensionais, do estado plano de deformação e do estado axissimétrico. Pressupõe-se que já é conhecida com detalhe a formulação descrita no Capítulo 6. 

### **10.1 - Simbologia** 

Apresenta-se em primeiro lugar um resumo da simbologia adoptada neste capítulo. 

Tabela 10.1 - Simbologia relativa ao método dos elementos finitos. 

|_m_|Número de direcções consideradas (no caso tridimensional:_m_= 3)|
|---|---|
|_n_|Número de nós do elemento finito|
|_p_|Número de graus de liberdade do elemento finito (_p_=_n_x_m_)|
|_x_|Coordenada cartesiana|
|_u_|Campo de deslocamentos|
|_a_|Deslocamento nodal|
|_F_|Forças nodais equivalentes à acção exterior, nos graus de liberdade do<br>elemento finito, no referencial geral|
|_K_|Matriz de rigidez do elemento finito no referencial geral|
|_~~x~~_|Coordenada cartesiana de um nó de um elemento finito|
|_s_|Coordenada local (curvilínea)|
|_~~s~~_|Coordenada local de um nó de um elemento finito|
|_N_|Função interpoladora ou função de forma|
|_V_|Vector contendo os factores não constantes de um polinómio|



175 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 

|_NV_|Vector das funções interpoladoras ou funções de forma|
|---|---|
|_B_|Matriz de deformação|
|_D_|Matriz de elasticidade (<br>ε<br>σ<br>_D_<br>=<br>)|
|_V_|Volume|
|_J_|Jacobiano da transformação|
|ε|Extensão|
|γ|Distorção|
|σ|Tensão normal|
|τ|Tensão tangencial|
|_C_|Elemento da matriz de elasticidade(_D_<br>)|
|_E_|Módulo de elasticidade ou módulo de Young|
|ν|Coeficiente de Poisson|
|_q_|Número de componentes do vector ε<br>e do vector σ|
|_L_|Operador diferencial|
|_h_|Espessura do elemento finito laminar|
|_Q_|Carga concentrada|
|_p_|Carga distribuída por unidade de comprimento|
|θ|Ângulo; direcção circunferencial|
|_P_|Perímetro|
|_S_|Superfície|



### **10.2 - Elementos sólidos tridimensionais (** **_bricks_ )** 

No desenvolvimento de elementos sólidos do tipo _brick_ é considerada uma formulação genérica com três graus de liberdade do tipo deslocamento. A exposição aqui apresentada baseia-se num elemento finito sólido com oito nós (ver a Figura 10.1). O número de graus de liberdade deste elemento é _p_ = 8 x 3 = 24. 

176 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
a 53<br>u 3 ( x 1 ,  x 2 ,  x 3)<br>a 51 a 52<br>8<br>5 u 2 ( x 1 ,  x 2 ,  x 3)<br>6<br>7 u 1 ( x 1 ,  x 2 ,  x 3)<br>1<br>x 3 4<br>2<br>x 1 x 2 3<br><!-- End of picture text -->

Fig. 10.1 - Elemento finito sólido de oito nós com geometria arbitrária. 

Os vectores dos deslocamentos nodais e das forças nodais equivalentes às acções exteriores são os seguintes. 



A matriz de rigidez do elemento ( _<u>K</u>_ ) é uma matriz _p_ x _p_ = 24 x 24. 

No referencial geral, a matriz das coordenadas cartesianas dos nós do elemento é a seguinte 



177 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 

Pelos motivos referidos no Capítulo 6, é conveniente fazer a seguinte substituição de variáveis 



Na Figura 10.2 encontra-se indicado o sistema de coordenadas locais, bem como o novo domínio de integração. 



<!-- Start of picture text -->
s 3<br>5 s 1 ∈ [ − 1 , + 1 ]<br>8 s 2 ∈ [ − 1 , + 1 ]<br>6 s 3 ∈ [ − 1 , + 1 ]<br>7<br>1<br>s 2<br>4<br>2<br>s 1 3<br><!-- End of picture text -->

Fig. 10.2 - Sistema de coordenadas locais. 

Os valores nodais das coordenadas _s_ 1, _s_ 2 e _s_ 3 são os seguintes 



Uma vez que o elemento é da família Lagrangeana, as funções de forma são 

178 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 



No caso da determinação das funções de forma com o procedimento genérico descrito no Capítulo 7, é necessário seleccionar oito termos na pirâmide de Pascal que se encontra representada na Figura 10.3. 



<!-- Start of picture text -->
1<br>s 3<br>s 1<br>s 2<br>2<br>s 3<br>s 1  s 3<br>2<br>s 1<br>s 2  s 3<br>s 1  s 2<br>2<br>s 2<br><!-- End of picture text -->

Fig. 10.3 - Pirâmide de Pascal. 

Os termos seleccionados são agrupados no vector _<u>V</u>_ , que é, neste caso, o seguinte 



Nota: o termo de terceiro grau não se encontra representado na Figura 10.3. 

O procedimento para a determinação das funções de forma é semelhante ao que foi descrito no Capítulo 7. 

A interpolação das coordenadas cartesianas é efectuada com a seguinte expressão 

179 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 



que corresponde a 



De acordo com o que foi apresentado no Capítulo 9, a matriz de rigidez do elemento finito é calculada com a expressão genérica 



Após a substituição de variáveis (3) passa a ter-se 



No caso tridimensional a matriz Jacobiana _<u>J</u>_ é a seguinte 



e o determinante Jacobiano é 



No caso dos materiais isotrópicos, é a seguinte a relação entre tensões e deformações [10.1] 

180 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 



sendo 



Em (13) o número de componentes de <u>σ</u> e <u>ε</u> ( _q_ ) é 6, podendo escrever-se de um modo mais compacto 



A matriz de elasticidade _<u>D</u>_ depende do módulo de Young ( _E_ ) e do coeficiente de Poisson ( ν ). 

A matriz Jacobiana obtém-se com a seguinte expressão, que resulta da derivação de (7) em ordem a _s_ 1, _s_ 2 e _s_ 3 



De um modo mais compacto, tem-se 

181 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 



Os elementos da matriz ∂ _<u>N</u>_ ∂ _<u>s</u>_ são as derivadas de (5) em ordem a _s_ 1, _s_ 2 e _s_ 3. 

No caso geral tridimensional, a relação entre o campo dos deslocamentos e o campo das deformações é [10.1] 



ou, de modo mais compacto 



A interpolação do campo de deslocamentos é efectuada com 



ou 

182 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 



Substituindo (21) em (19), chega-se a 



sendo 





Os elementos da matriz _<u>B</u>_ obtêm-se com a seguinte expressão, que é uma generalização do que foi exposto no Capítulo 6 

183 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 



Em notação matricial tem-se 



Uma vez que todos os componentes da função integranda de (10) se encontram definidos em função de _s_ 1, _s_ 2 e _s_ 3, já é possível calcular o integral triplo recorrendo à quadratura de Gauss descrita no Capítulo 5. 

O algoritmo de cálculo da matriz de rigidez do elemento sólido tridimensional é semelhante ao que foi apresentado no Capítulo 6, sendo apenas necessário remover todas as operações relativas à espessura do elemento e adaptar as dimensões das matrizes envolvidas no cálculo. 

O cálculo das tensões e deformações no elemento finito são também efectuadas de acordo com o que foi exposto no Capítulo 6, desde que se efectuem as necessárias adaptações ao caso tridimensional. 

### **10.3 - Estado plano de deformação** 

As características de um estado plano de deformação encontram-se descritas em [10.1]. Na Figura 10.4 está representado um corpo prismático, de secção constante e eixo segundo _x_ 3. 

184 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
x 2<br>h  = 1<br>1/2<br>1/2<br>O<br>x 1<br>Plano médio<br>x 3<br><!-- End of picture text -->

Fig. 10.4 - Estado plano de deformação. 

De acordo com as hipóteses consideradas para o estado plano de deformação, são efectuadas as seguintes simplificações 



Atendendo a (13) tem-se 



Os parâmetros _C_ 1, _C_ 2 e _C_ 3 encontram-se definidos em (14). 

185 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 

A equação (29) simplifica-se da seguinte forma 



sendo a tensão normal σ 3 dada por 



As tensões tangenciais τ 23 e τ 31 são nulas. 

Em [10.1] encontra-se a relação inversa de (13), cuja terceira equação é 



Como no estado plano de deformação ε 3 = 0, resulta 



Uma vez que se supõe que os campos de tensões e deformações não variam com _x_ 3, é suficiente estudar o comportamento de um troço de comprimento unitário, cujo plano médio passa pela origem e é perpendicular a _x_ 3 (ver a Figura 10.4). 

Nestas circunstâncias, apenas é necessário discretizar com elementos finitos a secção transversal que é perpendicular a _x_ 3 e que passa pela origem (ver a Figura 10.5). 

186 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
x 2 a 32 u 2 ( x 1 ,  x 2)<br>Q<br>a 31<br>a 42 u 1 ( x 1 ,  x 2)<br>3<br>a 41<br>4<br>a 22<br>a 12<br>a 11 a 21 h  = 1<br>p 2<br>1<br>x 1<br><!-- End of picture text -->

Fig. 10.5 - Elemento finito para estados planos de deformação. 

A formulação de um elemento finito para estados planos de deformação coincide com a que foi apresentada no Capítulo 6, com excepção do seguinte: 

- em todas as expressões deve ser considerado _h_ = 1; 

- a relação constitutiva <u>σ</u> = _<u>D</u>_ <u>ε</u> passa a ser a equação (30), sendo os elementos da matriz _<u>D</u>_ definidos em (14); 

- a força _<u>Q</u>_ que actua no corpo (ver a Figura 10.5) passa a ser uma força por unidade de comprimento segundo _x_ 3; 

- a força por unidade de comprimento _<u>p</u>_ que actua no corpo (ver a Figura 10.5) passa a ser uma força por unidade de superfície. 

### **10.4 - Estado axissimétrico** 

Na Figura 10.6 encontra-se representada uma secção transversal que, ao ser rodada em torno de _x_ 2, gera um sólido de revolução que corresponde a um reservatório axissimétrico. A secção transversal está discretizada em elementos finitos quadriláteros contidos no plano ( _x_ 1, _x_ 2). 

187 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
x 2  → Eixo de axissimetria<br>u 2<br>u θ<br>u 1<br>A<br>θ x 1<br><!-- End of picture text -->

Fig. 10.6 - Reservatório axissimétrico. 

Se, além da geometria, for também axissimétrica a distribuição do material que constitui o reservatório, bem como as características das acções exteriores, verifica-se que o comportamento é também axissimétrico. Devido ao facto de as acções axissimétricas serem, na generalidade dos casos, de natureza gravítica, admite-se que o eixo de axissimetria ( _x_ 2) é sempre vertical. O eixo _x_ 1, bem como os componentes segundo _x_ 1 de todas as grandezas, recebem a designação de radiais. O componente _u_ θ do campo de deslocamentos designa-se deslocamento circunferencial. A deformação circunferencial εθ corresponde ao quociente entre a variação do perímetro de uma fibra e o perímetro original (ver a Figura 10.7). 



<!-- Start of picture text -->
x 2<br>A A'<br>x 1<br>uA  1<br>xA  1<br><!-- End of picture text -->

Fig. 10.7 - Definição da deformação circunferencial. 

188 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 

O perímetro inicial da circunferência que passa pelo ponto _A_ é 



O perímetro da circunferência após a deformação é 



A deformação circunferencial é 



Substituindo (34) e (35) em (36) resulta 



No caso de um ponto genérico tem-se 



Por não corresponderem a uma deformação axissimétrica, são nulas as distorções γ 1 θ e γ 2 θ (ver a Figura 10.6). Nestas circunstâncias o vector <u>ε</u> é o seguinte 



189 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 

De um modo análogo ao que foi exposto no Capítulo 6, tem-se 



que, de um modo mais compacto, corresponde a 



Nestas circunstâncias, a relação constitutiva é 



Os parâmetros _C_ 1, _C_ 2 e _C_ 3 encontram-se definidos em (14). 

Na Figura 10.8 estão representados os componentes não nulos do tensor das tensões em problemas axissimétricos. 

No cálculo da matriz de rigidez _<u>K</u>_ deve ser considerado o seguinte (ver o Capítulo 9) 





Nesta expressão, 2 π _x_ 1 é o perímetro da fibra correspondente aos pontos de abcissa _x_ 1. 

190 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
x 2<br>σ  2<br>τ  12<br>τ  12<br>σ  1<br>σ θ<br>γ  1 θ = γ  2 θ = 0 ⇒ τ  1 θ = τ  2 θ = 0<br>x 1<br><!-- End of picture text -->

Fig. 10.8 - Componentes não nulos do tensor das tensões em problemas axissimétricos. 

Após a mudança de variável, tem-se 



Uma vez que se pretende que todos os componentes da função integranda de (45) sejam funções de _s_ 1 e _s_ 2, deve-se calcular _x_ 1 com a seguinte expressão 

em que _n_ é o número de nós do elemento finito. 

A matriz _<u>B</u>_ e o determinante Jacobiano _J_ são calculados tal como foi exposto no Capítulo 6, supondo que os elementos finitos do problema axissimétrico se situam no plano ( _x_ 1, _x_ 2) (ver a Figura 10.6). 

O integral duplo (45) pode ser calculado recorrendo à quadratura de Gauss (ver o Capítulo 5). 

Os integrais correspondentes ao cálculo das forças nodais equivalentes às acções exteriores têm de ser adaptados ao caso axissimétrico de um modo semelhante ao que foi apresentado para a matriz de rigidez _<u>K</u>_ . 

191 

_Sólidos, Estado Plano de Deformação e Axissimetria - Álvaro F. M. Azevedo_ 

Em problemas axissimétricos, os apoios, assentamentos de apoio e as cargas concentradas em nós estão presentes numa linha que se obtém por rotação do correspondente ponto em torno de _x_ 2 (ver a Figura 10.6). 

### **10.5 - Considerações finais** 

Neste capítulo, a descrição das formulações foi efectuada de um modo mais sucinto, uma vez que se supunha um bom conhecimento da formulação do estado plano de tensão exposta no Capítulo 6. Os elementos sólidos tridimensionais ( _bricks_ ) são os que, aparentemente, permitem modelar qualquer geometria. No entanto, apresentam os inconvenientes de necessitarem de uma preparação dos dados mais trabalhosa, requererem um maior esforço computacional e apresentarem maior dificuldade na interpretação dos resultados. Os estados planos de deformação surgem tipicamente em problemas geotécnicos (e.g., muros de suporte, barragens gravidade, túneis). Os estados axissimétricos apresentam o inconveniente de necessitarem de uma acção axissimétrica, que, na prática, nem sempre ocorre. Para ultrapassar esta limitação, em [10.2] é desenvolvida uma formulação correspondente a sólidos de revolução com acções não axissimétricas. Contudo, o seu elevado grau de dificuldade constitui um entrave a uma aplicação generalizada. 

### **BIBLIOGRAFIA** 

[10.1] - Azevedo, A. F. M. - Mecânica dos Sólidos, Faculdade de Engenharia da Universidade do Porto, 1996. 

[10.2] - Cook, R. D.; Malkus, D. S.; Plesha, M. E.; Witt, R. J. - Concepts and Applications of Finite Element Analysis, Fourth Edition, John Wiley & Sons, Inc., 2002. 

[10.3] - Zienkiewicz, O. C.; Taylor, R. L. - The Finite Element Method, Fourth Edition, McGraw-Hill, 1988. 

192 

### CAPÍTULO 11 

FLEXÃO DE VIGAS 

Antecedendo a apresentação da formulação de diversos tipos de elementos de viga, efectua-se em seguida uma revisão dos fundamentos da flexão de vigas. Apenas são consideradas as deformações devidas às tensões normais. 

### **11.1 - Simbologia** 

Apresenta-se em primeiro lugar um resumo da simbologia adoptada na formulação da flexão de vigas. 

Tabela 11.1 - Simbologia relativa à flexão de vigas. 

|_g_|Referencial geral|
|---|---|
|_l_|Referencial local|
|_i_|Primeiro nó de uma barra|
|_j_|Segundo nó de uma barra|
|_x_|Coordenada cartesiana|
|_u_|Campo de deslocamentos|
|θ|Ângulo|
|_G_|Centro de gravidade|
|ε|Extensão|
|σ|Tensão normal|
|_E_|Módulo de elasticidade ou módulo de Young|
|_S_|Superfície|
|_N_|Esforço axial|



193 

_Flexão de Vigas - Álvaro F. M. Azevedo_ 

|_M_|Momento flector|
|---|---|
|_k_|Curvatura|
|_A_|Área da secção transversal da barra prismática|
|_I_|Momento de inércia da secção transversal da barra prismática|



### **11.2 - Flexão composta plana** 

Considere-se uma barra prismática de eixo rectilíneo e secção variável, representada na Figura 11.1 conjuntamente com os referenciais geral ( _g_ ) e local ( _l_ ). 



<!-- Start of picture text -->
g  3<br>l<br>l 3 2<br>l 1<br>j<br>i<br>g<br>2<br>g<br>1 i  < j<br><!-- End of picture text -->

Fig. 11.1 - Barra _i j_ , referencial geral _g_ e referencial local _l_ . 

O eixo _l_ 1 do referencial local coincide com o eixo da barra e está orientado do nó _i_ para o nó _j_ , correspondendo _i_ e _j_ à numeração global dos nós da malha. Os eixos _l_ 2 e _l_ 3 são os eixos principais centrais de inércia da secção transversal. Apesar de a secção ser variável, considera-se que a localização destes eixos é constante ao longo da barra. A transformação dos deslocamentos generalizados e das forças generalizadas entre os referenciais _l_ e _g_ encontra-se descrita nos Capítulos 2 e 3. 

No estudo que se segue, apenas é considerado o referencial _l_ , que passa a ser designado por _x_ . Supõe-se também que todas as acções estão contidas no plano ( _x_ 1, _x_ 3), sendo os 

194 

_Flexão de Vigas - Álvaro F. M. Azevedo_ 

deslocamentos segundo _x_ 2 considerados nulos. Na Figura 11.2 está representado o eixo da barra indeformado e deformado, para o caso da flexão plana. Encontra-se também representada a secção transversal da barra, cujos eixos principais centrais de inércia são _x_ 2 e _x_ 3. 



<!-- Start of picture text -->
x 3<br>u 3<br>G x 2<br>x 3 θ<br>u 3 (  x 1 )<br>x 1 u 1<br><!-- End of picture text -->

Fig. 11.2 - Barra deformada e secção transversal. 

Uma vez que os deslocamentos são muito pequenos, considera-se 



sendo θ o ângulo de rotação do eixo da barra. A função _u_ 3 (ver a Figura 11.2) corresponde ao deslocamento do eixo da barra, que apenas depende de _x_ 1. De acordo com (1) e com a equação da deformada, que se encontra representada na Figura 11.2, tem-se 



Na Figura 11.3 encontram-se representados os deslocamentos de três pontos de uma secção transversal ( _A_ , _O_ e _B_ ). 

195 

_Flexão de Vigas - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
u 3 θ<br>B B'<br>x 3 θ<br>B'<br>x 3 O' O O' uO 1 (  x 1 )<br>u 1 (  x 1 ,  x 3 )<br>A'<br>A A'<br>u 3 (  x 1 )<br>B<br>O<br>A x 1 u 1<br><!-- End of picture text -->

Fig. 11.3 - Barra deformada e deslocamentos da secção transversal. 

Admite-se que uma secção plana se mantém plana após a deformação. Admite-se também que uma secção perpendicular ao eixo da barra mantém esta característica após a deformação. O ponto _O_ apresenta coordenada nula segundo _x_ 3. O deslocamento do ponto _O_ segundo _x_ 1 é designado _uO_ 1 e depende apenas de _x_ 1. O deslocamento de um ponto genérico da secção transversal segundo _x_ 1 depende de _x_ 1 e de _x_ 3 e é definido pela seguinte expressão 



ou 



A extensão segundo _x_ 1 é dada por 



A extensão ε 1 é positiva quando existe um alongamento. 

Substituindo (2) em (5) obtém-se 



196 

_Flexão de Vigas - Álvaro F. M. Azevedo_ 

Uma vez que se consideram muito pequenas as dimensões da secção transversal em comparação com o comprimento da barra, pode-se desprezar o efeito das tensões normais σ 2 e σ 3, ficando a lei de Hooke reduzida a ε 1 = σ 1 / _E_ , ou 



sendo _E_ o módulo de Young, que é sempre positivo [11.1]. A um valor positivo da tensão σ 1 corresponde uma tracção. 

Substituindo (2) em (7) resulta 



A resultante das tensões normais na secção transversal é (ver a Figura 11.4) 



sendo _S_ a área da secção transversal (ver a Figura 11.2). 

De um modo semelhante se define o momento flector como sendo 



Considera-se que um momento flector é positivo quando provoca tracções nas fibras que têm coordenada _x_ 3 positiva (ver a Figura 11.4). 

197 

_Flexão de Vigas - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
x 3 Curvatura ( k ) positiva<br>Momento flector<br>positivo<br>Esforço axial<br>positivo<br>M<br>N<br>x 1<br><!-- End of picture text -->

Fig. 11.4 - Definição do esforço axial e do momento flector. 

Supondo que o módulo de Young ( _E_ ) é constante em todos os pontos da barra e passando para fora do integral tudo o que não depende de _x_ 2 nem de _x_ 3, resulta de (9) e (10) 



e 



Uma vez que os eixos _x_ 2 e _x_ 3 são principais centrais de inércia, o seguinte momento estático é nulo 



A área e o momento de inércia em relação a _x_ 2 são definidos com as seguintes expressões (ver a Figura 11.2) 





198 

_Flexão de Vigas - Álvaro F. M. Azevedo_ 

É assim possível simplificar (11) e (12) para 





Designando a extensão correspondente ao eixo da barra por ε _o_ , tem-se 





que corresponde à expressão clássica relativa à tracção de barras [11.2]. 

Substituindo (2) em (17) tem-se 



Designando por _k_ a curvatura da barra 



resulta 



ou 



que corresponde a uma das expressões clássicas da flexão de vigas [11.2]. 

Na Figura 11.2, todos os pontos da linha que representa o eixo da barra deformada apresentam ordenada positiva ( _u_ 3 > 0), primeira derivada positiva ( _d u_ 3 _d x_ 1 > 0 ) e 

199 

_Flexão de Vigas - Álvaro F. M. Azevedo_ 

2 2 segunda derivada também positiva ( _d u_ 3 _d x_ 1 > 0 ). Atendendo à definição do sentido positivo do momento flector (ver a Figura 11.4), verifica-se que um momento flector positivo provoca uma curvatura negativa. Esta questão encontra-se expressa na equação (23), em que _E_ e _I_ são sempre positivos. 

A expressões (16) e (17) são equivalentes às seguintes 



Substituindo (24) e (25) em (7), tem-se 



resultando 



que corresponde à expressão clássica da flexão composta [11.2]. 

### **11.3 - Considerações finais** 

A formulação apresentada neste capítulo apresenta a vantagem de ser facilmente estendida a problemas em que os eixos _x_ 2 e _x_ 3 não são principais centrais de inércia. Apresenta também a vantagem de recorrer a um conjunto de convenções coerente com o que é habitual considerar no método dos elementos finitos. Fica assim facilitada a formulação de elementos finitos de viga, bem como a sua combinação com outros tipos de elementos. 

200 

_Flexão de Vigas - Álvaro F. M. Azevedo_ 

### **BIBLIOGRAFIA** 

[11.1] - Azevedo, A. F. M. - Mecânica dos Sólidos, Faculdade de Engenharia da Universidade do Porto, 1996. 

[11.2] - Massonnet, C. - Résistance des Matériaux, Dunod, Paris, 1968. 

201 

_Flexão de Vigas - Álvaro F. M. Azevedo_ 

202 

### CAPÍTULO 12 

VIGA DE EULER-BERNOULLI 

Designa-se por Euler-Bernoulli a formulação do elemento finito de viga em que se considera que as secções se mantêm planas e normais ao eixo da barra após a deformação. Deste modo não é considerada a deformação devida ao corte. 

### **12.1 - Simbologia** 

Apresenta-se em primeiro lugar um resumo da simbologia adoptada na formulação do elemento de viga de Euler-Bernoulli. 

Tabela 12.1 - Simbologia relativa ao elemento de viga de Euler-Bernoulli. 

|_L_|Comprimento da barra prismática|
|---|---|
|_x_|Coordenada cartesiana|
|_u_|Campo de deslocamentos|
|_a_|Deslocamento generalizado nodal|
|∆|Deslocamento nodal|
|θ|Rotação nodal|
|_~~x~~_|Coordenada cartesiana de um nó de um elemento finito|
|_N_|Função interpoladora ou função de forma|
|ε|Deformação|
|_B_|Matriz de deformação|
|σ|Tensão normal|
|_E_|Módulo de elasticidade ou módulo de Young|
|_p_|Acção exterior distribuída por unidade de comprimento|



203 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 

|_F_|Forças nodais equivalentes à acção exterior, nos graus de liberdade do<br>elemento finito, no referencial local|
|---|---|
|_V_|Volume|
|_S_|Superfície|
|_I_|Momento de inércia da secção transversal da barra prismática|
|_K_|Matriz de rigidez do elemento finito no referencial local|
|_M_|Momento flector|
|_s_|Coordenada local|
|_~~s~~_|Coordenada local de um nó de um elemento finito|
|_J_|Jacobiano da transformação (_J_=_d x_1/_d s_)|



### **12.2 - Viga de dois nós sem substituição de variável** 

Na Figura 12.1 encontra-se representado um elemento de viga com dois nós e com comprimento _L_ (ver os Capítulos 7 e 11). 



<!-- Start of picture text -->
u 3 ( x 1)<br>x 3 a 4 =  θ 2<br>a 2 =  θ 1<br>a 3 =  ∆ 2<br>a 1 =  ∆ 1<br>x 1<br>1 2<br>( x 1 = x 11 = − L 2 ) L  / 2 L  / 2 ( x 1 = x 21 = L 2 )<br><!-- End of picture text -->

Fig. 12.1 - Elemento de viga com dois nós. 

Os deslocamentos generalizados dos nós do elemento finito representado na Figura 12.1 são os seguintes 

204 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 



De acordo com o que foi exposto no Capítulo 11, o deslocamento lateral é _u_ 3( _x_ 1). A coordenada cartesiana<sup>_~~x~~_</sup> _ij_<sup>corresponde ao nó</sup><sup>_i_e refere-se ao eixo</sup><sup>_xj_.</sup> 

A interpolação do campo de deslocamentos é efectuada com a seguinte expressão (ver o Capítulo 7) 



que em notação matricial se escreve 



ou 



sendo 



As funções de forma _N_ 1 a _N_ 4 são as correspondentes à interpolação Hermitiana e têm as seguintes expressões (ver o Capítulo 7) 





205 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 





Considerando apenas os deslocamentos laterais _u_ 3( _x_ 1), i.e., considerando constante a componente _uO_ 1 do campo de deslocamentos, tem-se, de acordo com o que foi exposto no Capítulo 11 



Designando por<sup>~~ε~~</sup> 1<sup>a seguinte componente da expressão (10)</sup> 



passa a ter-se 



Substituindo (2) em (11) chega-se a 



Definindo a matriz _<u>B</u>_ da seguinte forma 



passa a escrever-se 



206 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 

Substituindo (15) em (12) obtém-se 



Atendendo às funções de forma (6) a (9), são os seguintes os componentes da matriz _<u>B</u>_ 



Também de acordo com o que foi exposto no Capítulo 11, tem-se 



e, atendendo a (16), 



Considere-se que na viga da Figura 12.1 actua a carga uniformemente distribuída representada na Figura 12.2 



Fig. 12.2 - Carga uniformemente distribuída e respectivas forças nodais equivalentes. 

As forças nodais equivalentes à acção exterior encontram-se também representadas na Figura 12.2 e apresentam os mesmos sentidos positivos que foram considerados para os deslocamentos generalizados _ai_ . 

O princípio dos trabalhos virtuais (PTV), que foi apresentado no Capítulo 4, corresponde ao seguinte 

207 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 



No caso da viga representada nas Figuras 12.1 e 12.2 a equação (20) passa a 



Nesta equação, _S_ é a superfície correspondente à secção transversal da barra (ver o Capítulo 11) e 



A equação (16) referida à deformação virtual é a seguinte 



que é equivalente a 



A equação (4) referida à deformação virtual é a seguinte 



que é equivalente a 



Substituindo todas estas equações em (21) passa a ter-se o PTV expresso por 



Passando para fora de cada integral tudo o que não depende da respectiva variável chega-se a 

208 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 



Nesta expressão considera-se que o módulo de Young _E_ é constante dentro da secção transversal e variável ao longo do eixo da barra. 

O momento de inércia em relação ao eixo _x_ 2 é definido da seguinte forma, sendo designado por _I_ 2 



De acordo com o PTV, a equação (28) é verdadeira para qualquer conjunto de deslocamentos virtuais, concluindo-se assim que 



A matriz de rigidez do elemento de viga é 



e o vector de solicitação é 



Supondo o módulo de Young e o momento de inércia constantes em toda a barra, a expressão da matriz de rigidez passa a 



Substituindo em (33) a expressão (17), tem-se 

209 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 



Depois de efectuar o cálculo dos integrais presentes em (34) chega-se a 



Esta matriz coincide com a que se obtém pelos métodos clássicos da teoria das estruturas reticuladas [12.1]. 

Substituindo (5) em (32) e considerando as funções de forma (6)-(9), obtém-se 



Depois de efectuar o cálculo dos integrais presentes em (36) chega-se a 



que também corresponde ao que se obtém por métodos clássicos [12.1]. 

210 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 

No Capítulo 11 encontra-se deduzida a seguinte expressão para o cálculo do momento flector na viga, quando o módulo de Young é constante 



Atendendo a (11), (15) e (38), conclui-se que o momento flector pode ser obtido com 



A matriz _<u>B</u>_ é avaliada no ponto em que se pretende calcular o momento flector. Deve-se notar que, em geral, esta expressão não fornece valores para os momentos flectores coincidentes com os da teoria clássica, porque quando os deslocamentos _<u>a</u>_ são nulos o momento flector calculado com (39) é nulo em toda a barra, sendo assim ignorada a contribuição das cargas que actuam no seu interior (e.g., carga distribuída _p_ ). Esta questão obriga a que seja efectuada uma discretização de cada barra de um pórtico em vários elementos finitos (ver a Figura 12.3). 



Fig. 12.3 - Exemplo: discretização das barras de um pórtico em 22 elementos finitos. 

O procedimento aqui apresentado para o cálculo da matriz de rigidez e do vector solicitação apresenta a vantagem de ser mais facilmente estendido a outras situações mais elaboradas (e.g., elementos finitos com mais do que dois nós, barras de secção variável, barras não rectilíneas). 

211 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 

### **12.3 - Viga de três nós sem substituição de variável** 

A formulação da matriz de rigidez e vector solicitação da viga de três nós é efectuada de um modo semelhante ao que foi exposto na Secção 12.2. As únicas diferenças são o aumento da dimensão de todos os vectores e matrizes envolvidos e o recurso às expressões da interpolação Hermitiana com três nós (ver o Capítulo 7). 

### **12.4 - Viga de dois nós com substituição de variável** 

Quando é utilizada a interpolação Hermitiana e se faz uma substituição de variável, surgem algumas questões que são apresentadas com base no exemplo da Figura 12.4. 



<!-- Start of picture text -->
u 3 ( x 1)<br>x 3 a 4 =  θ 2<br>a 2 =  θ 1<br>a 3 =  ∆ 2<br>a 1 =  ∆ 1<br>x 1<br>1 2<br>( x 1 = x 11 = − L 2 ) L  / 2 L  / 2 ( x 1 = x 21 = L 2 )<br>u 3 ( s ) a 4 = θ 2<br>a 2 = θ 1<br>a 3 = ∆ 2<br>a 1 = ∆ 1<br>s<br>1 2<br>( s = s 1 = − 1 ) 1 1 ( s = s 2 = 1 )<br><!-- End of picture text -->

Fig. 12.4 - Substituição de variável num elemento de viga com dois nós. 

A transformação entre a coordenada _x_ 1 e a coordenada _s_ é, neste caso simples, efectuada com a seguinte expressão 

212 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 



O vector dos deslocamentos generalizados na viga real é 



sendo 



Após a substituição de variável e atendendo à coordenada local _s_ , tem-se 



sendo 



A derivada em ordem a _s_ da função _u_ 3( _x_ 1( _s_ )) é, pela regra da cadeia 



De acordo com (40), tem-se neste caso 



Designando por _J_ a seguinte derivada 

213 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 



tem-se 



e, atendendo a (42) e (44) 



Nos nós, tem-se 





Substituindo (50) em (43), obtém-se 



Atendendo a (41), chega-se a 



A interpolação do campo de deslocamentos pode ser efectuada com base na coordenada _s_ , sendo utilizada a seguinte expressão (ver a Figura 12.4) 



214 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 

As funções de forma _Ni_ são definidas com as seguintes expressões, que correspondem à interpolação Hermitiana numa viga com comprimento _L_ = 2 (ver o Capítulo 7) 









Substituindo (52) em (53) chega-se a 



Uma vez que se pretende que a interpolação de _u_ 3 seja efectuada da seguinte forma 



ou 



conclui-se que 



sendo 



215 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 





Atendendo às equações (10)-(14), existe a necessidade de calcular a seguinte matriz 



Para calcular as derivadas de _Ni_ em ordem a _x_ 1, quando apenas se conhecem as funções _Ni_ ( _s_ ) (62)-(65), deve-se recorrer à regra da cadeia 



Atendendo a (47), fica 



Derivando outra vez em ordem a _s_ e considerando de novo a regra da cadeia tem-se 



Considerando (47) e (68) chega-se a 



Uma vez que _J_ é constante, tem-se 

216 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 



que é equivalente a 



Derivando duas vezes as funções de forma (62)-(65) em ordem a _s_ , tem-se 



Estas expressões são substituídas em (72), obtendo-se assim as segundas derivadas de _Ni_ em ordem a _x_ 1 



Atendendo a (47), tem-se 

217 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 







De acordo com (66), são os seguintes os elementos da matriz _<u>B</u>_ em função da variável _s_ 



De acordo com (33), i.e., supondo o módulo de Young e a secção constantes, tem-se a seguinte expressão para a matriz de rigidez do elemento finito de viga no referencial local 



Após a substituição da variável _x_ 1 pela variável _s_ , (86) passa a 



Atendendo a (47) e a (85) tem-se 



218 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 

Note-se que todos os elementos da matriz que constitui a função integranda são funções de _s_ . O comprimento da barra ( _L_ ) é um parâmetro fixo. 

Após o cálculo dos integrais obtém-se a seguinte matriz 



Considerando a carga uniformemente distribuída representada na Figura 12.2, tem-se o seguinte vector solicitação, que é calculado com a expressão (32). 



Após a substituição da variável _x_ 1 pela variável _s_ , (90) passa a 



Atendendo a (47) e às funções de forma (62)-(65), tem-se 



Do cálculo destes integrais resulta 

219 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 



As expressões (89) e (93) coincidem com as que se obtêm recorrendo à teoria clássica da flexão de vigas [12.1]. A formulação aqui apresentada possui contudo a vantagem de ser extensível a casos mais genéricos, tais como vigas curvas e vigas de secção variável, em que pode ser vantajosa a utilização de funções de interpolação de grau mais elevado e, consequentemente, o recurso a elementos finitos com mais do que dois nós. 

O cálculo do momento flector num ponto definido pela coordenada _s_ é efectuado com a expressão (39), sendo a matriz _<u>B</u>_ calculada com (85). 

Nas condições do elemento atrás descrito, é possível demonstrar que os valores mais correctos do campo de momentos flectores se encontram nos pontos cuja coordenada _s_ é 



Se se pretender conhecer os valores do campo de momentos noutros pontos, é em geral mais vantajoso efectuar uma extrapolação ou interpolação simples a partir dos pontos (94). 

O campo de esforços transversos pode ser obtido por derivação do campo de momentos em ordem a _x_ . 

### **12.5 - Considerações finais** 

A formulação da viga de Euler-Bernoulli, aqui apresentada, não é mais desenvolvida porque, na prática, é preferível utilizar uma formulação que entre em linha de conta com a deformação por esforço transverso. Esta formulação é apresentada no Capítulo 13. 

220 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 

### **BIBLIOGRAFIA** 

[12.1] - Correia de Araújo, F. - Cálculo Matricial das Estruturas Contínuas pelo Método dos Deslocamentos, Revista "Engenharia", Publicação dos Alunos da FEUP, Ano XIX, Número 43, Novembro/Dezembro, 1965/66. 

[12.2] - Hinton, E.; Owen, D. R. J. - An Introduction to Finite Element Computations, Pineridge Press, Swansea, U.K., 1979. 

[12.3] - Hughes, T. J. R. - The Finite Element Method - Linear Static and Dynamic Finite Element Analysis, Prentice-Hall, Inc., 1987. 

221 

_Viga de Euler-Bernoulli - Álvaro F. M. Azevedo_ 

222 

### CAPÍTULO 13 

### VIGA DE TIMOSHENKO 

Na formulação do elemento de viga de Timoshenko [13.1] é considerado que as secções planas se mantêm planas. Contudo, supõe-se que uma secção normal ao eixo da viga não mantém essa característica após a deformação. Deste modo é possível considerar a deformação devida ao corte. 

### **13.1 - Simbologia** 

Apresenta-se em primeiro lugar um resumo da simbologia adoptada na formulação do elemento de viga de Timoshenko. 

Tabela 13.1 - Simbologia relativa ao elemento de viga de Timoshenko. 

|_L_|Comprimento da barra prismática|
|---|---|
|_x_|Coordenada cartesiana|
|_u_|Campo de deslocamentos|
|_a_|Deslocamento generalizado nodal|
|∆|Deslocamento nodal|
|θ|Rotação nodal|
|_~~x~~_|Coordenada cartesiana de um nó de um elemento finito|
|_s_|Coordenada local|
|_~~s~~_|Coordenada local de um nó de um elemento finito|
|_J_|Jacobiano da transformação (_J_=_d x_1/_d s_)|
|_N_|Função interpoladora ou função de forma|
|_G_|Centro de gravidade|



223 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 

|φ|Rotação correspondente à deformação por esforço transverso|
|---|---|
|ε|Extensão|
|_Bb_|Matriz de deformação relativa ao termo de flexão (_bending_)|
|σ|Tensão normal|
|_E_|Módulo de elasticidade ou módulo de Young|
|γ|Distorção|
|_Bs_|Matriz de deformação relativa ao termo de corte (_shear_)|
|τ|Tensão tangencial|
|_G_|Módulo de distorção|
|_W_|Trabalho|
|_V_|Volume|
|_S_|Superfície|
|_I_|Momento de inércia da secção transversal da barra prismática|
|_A_|Área da secção transversal da barra prismática|
|_A_<sup>_*_</sup>|Área efectiva de corte relativa à secção transversal da barra prismática|
|α|Coeficiente de redução da área da secção transversal para atender ao corte|
|_F_|Forças nodais equivalentes à acção exterior, nos graus de liberdade do<br>elemento finito, no referencial local|
|_K_|Matriz de rigidez do elemento finito no referencial local|
|_M_|Momento flector|
|_V_|Esforço transverso|



### **13.2 - Viga de dois nós com substituição de variável** 

Na Figura 13.1 encontra-se representado um elemento de viga com dois nós e com comprimento _L_ (ver o Capítulo 11). Supõe-se que nos nós não há deslocamentos segundo _x_ 1. Deste modo apenas se considera o comportamento à flexão da viga. 

224 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
u 3 ( x 1)<br>x 3 a 4 =  θ 2<br>a 2 =  θ 1<br>a 3 =  ∆ 2<br>a 1 =  ∆ 1<br>x 1<br>1 2<br>( x 1 = x 11 = − L 2 ) L  / 2 L  / 2 ( x 1 = x 21 = L 2 )<br>u 3 ( s ) θ  ( s )<br>s<br>1 2<br>( s = s 1 = − 1 ) 1 1 ( s = s 2 = 1 )<br><!-- End of picture text -->

Fig. 13.1 - Substituição de variável num elemento de viga com dois nós. 

Os deslocamentos generalizados dos nós do elemento finito representado na Figura 13.1 são os seguintes 



A transformação entre a coordenada _x_ 1 e a coordenada _s_ é, neste caso simples, efectuada com a seguinte expressão 



sendo a derivada em ordem a _s_ a seguinte 



225 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 

A interpolação do deslocamento lateral _u_ 3 e da rotação θ é efectuado separadamente para cada uma destas variáveis. Assim, e uma vez que _u_ 3 e θ apresentam dois valores nodais cada, é utilizada a seguinte interpolação unidimensional com dois nós 





Neste exemplo com dois nós as funções de forma são as seguintes (ver o Capítulo 4) 





Na Figura 13.2 está representado o eixo da viga na sua posição inicial (sobre _x_ 1) e a correspondente deformada (ver o Capítulo 11). Está também representada a secção transversal cujos eixos são _x_ 2 e _x_ 3. Uma vez que se consideram pequenas deformações, supõe-se que o declive da recta tangente ao eixo coincide com o ângulo de rotação do eixo da barra. 



<!-- Start of picture text -->
x 3<br>u 3<br>G x 2<br>d u 3<br>x 3<br>d x 1<br>u 3 (  x 1 )<br>x 1 u 1<br><!-- End of picture text -->

Fig. 13.2 - Barra deformada e secção transversal. 

Na Figura 13.3 estão indicados os seguintes ângulos: rotação do eixo da barra ( _d u_ 3 _d x_ 1 ) , rotação da secção transversal ( θ ) e rotação correspondente à deformação por esforço transverso ( φ ). Encontra-se também representado o campo de deslocamentos _u_ 1 na secção transversal. 

226 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
B' B<br>θ<br>d u 3 θ<br>x 3<br>φ  d x 1 O  ≡ O'<br>u 3<br>u 1 (  x 1 ,  x 3 )<br>x 3 B' O'<br>A' A A'<br>u 3 (  x 1 )<br>B<br>O<br>A x 1 u 1<br><!-- End of picture text -->

Fig. 13.3 - Barra deformada e deslocamentos da secção transversal. 

Na formulação da viga de Euler-Bernoulli considera-se que o ângulo φ é nulo, sendo os ângulos _d u_ 3 _d x_ 1 e θ coincidentes. Na formulação da viga de Timoshenko, o ângulo φ é considerado não nulo, sendo 



Estes três ângulos dependem de _x_ 1. 

De acordo com a Figura 13.3, tem-se 



A extensão ε 1 é definida por [13.2] 



sendo 

227 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 



Designando por<sup>~~ε~~</sup> 1<sup>a seguinte componente da expressão (11)</sup> 



passa a ter-se 



Derivando (5) em ordem a _x_ 1 chega-se a 



Substituindo (14) em (12) obtém-se 



Considere-se agora uma matriz de deformação, que é designada _<u>B</u> b_<sup>pelofactodeestar</sup> associada à flexão ( _bending_ ). A sua definição é a seguinte 



Atendendo a (1), (15) passa a escrever-se 



Substituindo (17) em (13) obtém-se 



228 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 

Tal como no Capítulo 12, considera-se a lei de Hooke referida apenas à tensão normal σ 1 e à extensão ε 1 



Substituindo (18) em (19), tem-se 



A distorção γ 13 é definida por [13.2] 



Atendendo a (9), tem-se a seguinte distorção média [13.3] 





Substituindo (8) em (23) obtém-se 



Derivando (4) em ordem a _x_ 1 chega-se a 



Substituindo (5) e (25) em (23) obtém-se 



Em notação matricial tem-se 

229 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 



Considere-se agora uma matriz de deformação, que é designada _<u>B</u> s_<sup>pelofactodeestar</sup> associada ao corte ( _shear_ ). A sua definição é a seguinte 



Atendendo a (1), (27) passa a escrever-se 



Uma vez que, de acordo com a lei de Hooke para materiais isotrópicos [13.2] 



tem-se, depois de substituir (29) em (30) 



De acordo com o Princípio dos Trabalhos Virtuais (PTV) (ver o Capítulo 4), admite-se que 



Considerando 







De acordo com (32), tem-se 

230 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 



Considerando que a contribuição da flexão para o trabalho apenas depende da tensão normal σ 1, tem-se (ver o Capítulo 4) 



A equação (18) referida à deformação virtual é a seguinte 



sendo equivalente a 



Substituindo (39) e (20) em (37) obtém-se 



Nesta equação, _S_ é a superfície correspondente à secção transversal da barra (ver o Capítulo 11). De acordo com a Figura 13.2, tem-se 



Supondo o módulo de Young _E_ constante em todos os pontos do elemento de viga e passando para fora dos integrais tudo o que não depende da respectiva variável de integração, resulta 



O momento de inércia em relação ao eixo _x_ 2 é definido da seguinte forma, sendo designado por _I_ 2 (ver a Figura 13.2) 



231 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 

Substituindo (43) em (42) e supondo que a barra é de secção constante, passa a ter-se 



Considerando que a contribuição do corte para o trabalho apenas depende da tensão tangencial τ 13, tem-se 



A equação (29) referida à deformação virtual é a seguinte 



sendo equivalente a 



Substituindo (47) e (31) em (45) obtém-se 



Supondo o módulo de distorção _G_ constante em todos os pontos do elemento de viga e passando para fora dos integrais tudo o que não depende da respectiva variável de integração, resulta 



A área da secção transversal da barra é 



Na expressão (49) é necessário introduzir o factor correctivo de corte α , sendo a área reduzida de corte definida por [13.3] 

232 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 



Substituindo (50) em (49) e considerando a área reduzida de corte, passa a ter-se, no caso de uma barra de secção constante 



Por uma questão de simplificação desta exposição, considera-se que o trabalho externo associado às forças exteriores ( δ _W_<sup>_e_</sup> ) inclui apenas a contribuição das forças generalizadas concentradas nos nós da barra. Nestas condições tem-se 



As componentes do vector _<u>F</u>_ são forças generalizadas (forças e momentos) em correspondência com os quatro graus de liberdade dos nós da barra (ver a Figura 13.1). 

Substituindo (44), (52) e (53) em (36), obtém-se 



Uma vez que (54) tem de se verificar para qualquer deformação virtual <u>δ</u> _<u>a</u>_ <u>,</u> chega-se à habitual equação 



sendo a matriz de rigidez _<u>K</u>_ calculada com a seguinte expressão 



Depois de efectuar em (56) a substituição de variável definida em (2), tem-se 



233 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 

Substituindo (3) em (57), chega-se a 



Para se obter os elementos das matrizes _<u>B</u> b_<sup>(16)e</sup><sup>_<u>B</u>_</sup> _s_<sup>(28)emfunçãodavariável</sup><sup>_s_,é</sup> necessário calcular a derivada das funções de forma em ordem a _x_ 1. Para isso é suficiente recorrer à regra da cadeia, ficando 



Atendendo a (3), passa a ter-se 



que é equivalente a 



Da derivação de (6) e (7) em ordem a _s_ resulta 





Atendendo a (61), tem-se 





Substituindo (64) e (65) em (16), obtém-se 

234 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 



Substituindo (6), (7), (64) e (65) em (28), obtém-se 



Os elementos das matrizes _<u>Bb</u>_<sup>e</sup><sup>_<u>B</u>_</sup> _s_<sup>apenasdependemde</sup><sup>_L_,queseconsideraum</sup> parâmetro fixo, e da variável _s_ . Depois de substituir estas expressões em (58) e de calcular os integrais em ordem a _s_ , resulta a seguinte expressão para a matriz de rigidez do elemento finito 



O facto de a expressão (68) ser aproximada, obriga a que na análise de um pórtico cada uma das suas barras tenha de ser discretizada em vários elementos finitos. Esta questão foi já referida no Capítulo 12. 

No Capítulo 11 encontra-se deduzida a seguinte expressão para o cálculo do momento flector na viga, quando o módulo de Young é constante 



Atendendo a (12), (17) e (69), conclui-se que o momento flector pode ser obtido com 



A matriz _<u>Bb</u>_<sup>é avaliada no ponto em que se pretende calcular o momento flector.</sup> 

As expressões (29) e (31) referem-se à distorção média e à tensão tangencial média. 

O esforço transverso _V_ é calculado com a seguinte expressão 

235 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 



Nesta expressão, τ 13( _x_ 3) representa a tensão tangencial real, que depende da coordenada _x_ 3 (ver a Figura 13.2). Uma vez que na presente formulação apenas se dispõe da tensão tangencial média τ 13, é necessário calcular o esforço transverso _V_ com base na área efectiva de corte _A_<sup>*</sup> . A sua expressão é a seguinte [13.4] 



Atendendo a (23), tem-se 



Substituindo (24) em (73), obtém-se 



O ângulo φ está representado na Figura 13.3. 

Substituindo (29) em (73), chega-se a 



A matriz _<u>Bs</u>_<sup>é avaliada no ponto em que se pretende calcular o esforço transverso.</sup> 

A expressão que fornece a área efectiva de corte _A_<sup>*</sup> depende da forma de secção transversal [13.3]. 

Deve-se ter em consideração que, quer o momento flector, quer o esforço transverso, apenas apresentam valores com precisão aceitável em determinados pontos do elemento finito [13.5]. Se se pretender conhecer os valores dos esforços noutros pontos, é em geral preferível efectuar uma extrapolação ou interpolação simples a partir dos pontos em que os resultados são mais correctos. 

236 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 

### **13.3 - Considerações finais** 

A formulação da viga de Timoshenko aqui apresentada pode ser estendida aos seguintes casos: barras com mais do que dois nós, barras curvilíneas, barras de secção variável, barras tridimensionais sujeitas a flexão desviada, inclusão da torção, consideração do centro de corte distinto do centro de gravidade, barras em que as propriedades do material variam ao longo do eixo da barra ou dentro da secção transversal, etc. [13.4]. 

### **BIBLIOGRAFIA** 

[13.1] - Oñate, E. - Cálculo de Estructuras por el Método de los Elementos Finitos - Análisis Estático Lineal, Segunda Edición, CIMNE, Barcelona, 1995. 

[13.2] - Azevedo, A. F. M. - Mecânica dos Sólidos, Faculdade de Engenharia da Universidade do Porto, 1996. 

[13.3] - Massonnet, C. - Résistance des Matériaux, Dunod, Paris, 1968. 

[13.4] - Barros, J. A. O. - Método dos Elementos Finitos Aplicado a Estruturas Reticuladas, Relatório 01-DEC/E-99, Universidade do Minho, 2001. 

[13.5] - Cook, R. D.; Malkus, D. S.; Plesha, M. E.; Witt, R. J. - Concepts and Applications of Finite Element Analysis, Fourth Edition, John Wiley & Sons, Inc., 2002. 

237 

_Viga de Timoshenko - Álvaro F. M. Azevedo_ 

238 

### ANEXO A 

UTILIZAÇÃO DO PROGRAMA FEMIX 3.1 

Neste capítulo é efectuada uma breve descrição das tarefas que é necessário empreender para analisar uma estrutura com o programa FEMIX - Versão 3.1. 

A documentação completa, bem como as instruções para o _download_ do programa FEMIX 3.1, encontram-se no seguinte URL: 

http://civil.fe.up.pt/Software/Femix_3.1/Femix_3.1_Manual.htm 

Refere-se em primeiro lugar o modo de instalação, seguindo-se um exemplo de aplicação. Nesta publicação não se pretende repetir o conteúdo do manual do programa [A.1], devendo o leitor recorrer à documentação completa sempre que surgirem dúvidas. 

### **A.1 - Instalação** 

Descarregar do URL acima referido o seguinte ficheiro: 

femix_V3.1_0031.zip 

Fazer a extracção de todo o conteúdo deste ficheiro para um directório qualquer. Sugere-se a instalação em C:\ sendo automaticamente criado neste local um directório chamado C:\femix . Dentro deste directório surgem outros subdirectórios. É aconselhável acrescentar ao "PATH" o directório C:\femix\bin . Em Windows 2000 ou XP , esta operação pode ser efectuada clicando em "My Computer" com o botão da direita e seleccionando "Properties / Advanced / Environment Variables" . Seleccionar em seguida o "PATH" do utilizador corrente a carregar no botão "Edit" . Em seguida deve-se acrescentar no fim da lista de directórios o seguinte texto: 

#### ; C:\femix\bin 

Aconselha-se também a criação no "Desktop" de "Shortcuts" para os seguintes programas: 

239 

_Utilização do Programa Femix 3.1 - Álvaro F. M. Azevedo_ 

C:\femix\bin\s3dcad.exe 

C:\femix\bin\drawmesh.exe 

Habitualmente, a invocação dos diversos módulos é feita a partir da linha de comandos. Para obter uma janela que suporta a invocação de comandos deve-se seleccionar: "Start / Run" e em seguida escrever na janela de texto: 

cmd 

Para aumentar o número de linhas de texto deve-se clicar no canto superior esquerdo da janela de comandos e seleccionar: "Properties / Layout" . Em seguida aumentar o parâmetro "Window Size / Height" . 

Para testar a instalação, deve-se fazer o seguinte: 

Abrir uma janela de comandos (cmd) cd \temp md femix cd femix s3dcad 

Se a instalação tiver sido feita correctamente, deve ser possível arrancar o programa s3dcad a partir do directório corrente. 

Tendo em vista uma familiarização com os diversos ficheiros que fazem parte da instalação, aconselha-se uma inspecção ao conteúdo de todos os directórios que se encontram dentro de C:\femix . 

### **A.2 - Preparação dos dados** 

Apresenta-se em seguida uma descrição dos principais passos a dar para se chegar aos resultados de uma análise com o programa FEMIX 3.1. Todas as fases são exemplificadas com base na estrutura representada na Figura A.1. 

240 

_Utilização do Programa Femix 3.1 - Álvaro F. M. Azevedo_ 



<!-- Start of picture text -->
x 2 E = 20 GPa<br>50 kN / m<br>ν = 0.15<br>h = 0.3 m<br>1.0 m<br>x 1<br>10.0 m<br><!-- End of picture text -->

Fig. A.1 - Viga que se pretende analisar pelo MEF usando o programa FEMIX. 

Para criar um ficheiro de dados contendo a quase totalidade da informação que descreve o problema, deve-se escrever o seguinte a partir da linha de comandos [A.2]: 

Nota: o caracter '#' e todos os que se encontram à sua direita são comentários, não sendo necessário digitá-los. 

s3dcad 

- csm # Create a simple mesh 2 # Rectangle 10 # Size in x [1] 

   - 1 # Size in x [2] 

- gen # Generate a refined mesh 

   - 2 # Surfaces 

   - 4 # N. of nodes of the generated elements 

   - 4 # N. of divisions for all the elements in s1 

   - 1 # N. of divisions for all the elements in s2 

- ren # Renumber elements, nodes and special nodes 

   - 1 # Default answer 

   - 2 # Default answer 

   - 3 # Default answer 

   - y # Default answer 

   - y # Default answer 

   - y # Default answer 1.0e-5 # Default answer 

- wri # Write a .s3d file 

viga44 # Job name (elementos de 4 nós; malha com 4 elementos) 

- gld # Write a _gl.dat file (femix) 

   - viga44 # Job name 

241 

_Utilização do Programa Femix 3.1 - Álvaro F. M. Azevedo_ 

- 1 # Plane stress 

1 # From the coordinates (x1,x2) 

end # End s3dcad 

Da execução destes comandos resultam os seguintes ficheiros: 

viga44.s3d # Ficheiro com a geometria, tendo em vista a sua visualização gráfica viga44_gl.dat # Ficheiro com os dados para a análise com o FEMIX 

Uma vez que se tratam de ficheiros do tipo "texto", o seu conteúdo pode ser inspeccionado, por exemplo, com os programas Notepad ou Word . 

O ficheiro viga44.s3d destina-se ao programa drawmesh (ver a Figura A.2). Os principais comandos deste programa são os seguintes: 

File / Import # Importar o ficheiro de extensão .s3d View / Set View Angles / XY # Visualizar o plano XY Options / Markers # Colocar tudo "Visible" Options / Numbers # Colocar tudo "Visible" Options / Lines # Alterar o "Shrink factor" para 90% View / Shading # Fazer a coloração dos elementos 

Nota: para muitos dos comandos existem botões nas barras de ferramentas, bem como 

teclas de atalho (fazer Help / Keyboard Commands ). 



Fig. A.2 - Visualização da malha com o programa drawmesh . 

O ficheiro viga44_gl.dat , que foi gerado com o programa s3dcad , ainda não se encontra completo. Referem-se em seguida as alterações que devem ser efectuadas. 

242 

_Utilização do Programa Femix 3.1 - Álvaro F. M. Azevedo_ 

Substituir o título "Rectangular mesh" por: 

Viga discretizada com 4 elementos de 4 no's (kN,m) 

Substituir o bloco de parâmetros pelo seguinte: 

4 # nelem (n. of elements in the mesh) 10 # npoin (n. of points in the mesh) 2 # nvfix (n. of points with fixed degrees of freedom) 1 # ncase (n. of load cases) 1 # nmats (n. of sets of material properties) 1 # nspen (n. of sets of element nodal properties) 1 # ntype (problem type) 4 # nnode (n. of nodes per element) 2 # ngaus (n. of Gauss points in the integration rule) (element stiffness) 2 # ngstr (n. of Gauss points in the integration rule) (stresses) 2 # ndime (n. of geometric dimensions) 2 # ndofn (n. of degrees of freedom per node) 0 # nnscs (n. of points with specified coordinate system) 0 # nsscs (n. of specified coordinate systems) 0 # npspr (n. of springs) 0 # nsspv (n. of spring vectors) 4 # nprop (n. of material properties used in the formulation) 1 # npren (n. of element nodal properties used in the formulation) 0 # nwink (n. of element faces with Winkler coefficients) 

Acrescentar as definições das características dos apoios ao seguinte bloco de dados: 

### Points with fixed degrees of freedom and fixity codes (1-fixed;0-free) # ivfix nofix ifpre ... 1 1 1 1 2 9 0 1 

Remover os seguintes blocos de dados: 

### Points with specified coordinate system ### Specified coordinate system index ### Spring index, point number, type of spring vector, spring constant value and... ### Spring vector index 

Modificar as propriedades do material para o seguinte: 

243 

_Utilização do Programa Femix 3.1 - Álvaro F. M. Azevedo_ 

### Sets of material properties ### (Young modulus, Poisson ratio, mass per unit volume and thermic coeff.) # imats young poiss dense alpha 1 20.0e+6 0.15 0.0 0.0 # kPa 

Modificar o bloco das espessuras nodais para o seguinte: 

### Sets of element nodal properties # ispen 1 # inode thickness 1 0.3 2 0.3 3 0.3 4 0.3 

Substituir os casos de carga que surgem por defeito pelas seguintes linhas: 

### Title of the first load case Carga distribuida de 50 kN/m 

### Load parameters 0 # nplod (n. of point loads in nodal points) 0 # ngrav (gravity load flag: 1-yes;0-no) 4 # nedge (n. of edge loads) (F.E.M. only) 0 # nface (n. of face loads) (F.E.M. only) 0 # nteme (n. of elements with temperature variation) (F.E.M. only) 0 # nudis (n. of uniformly distributed loads) (3d frames and trusses only) 0 # ntral (n. of trapezoidal distributed loads (3d frames and trusses only) 0 # nepoi (n. of bar point loads) (3d frames and trusses only) 0 # ntemb (n. of bars with temper. variation) (3d frames and trusses only) 0 # nprva (n. of prescribed and non zero degrees of freedom) 

### Edge load (loaded element, loaded points and load value) ### (local coordinate system) 

# iedge loele 

1 1 # lopoe fe1 fe2 2 0.0 -50.0 

244 

_Utilização do Programa Femix 3.1 - Álvaro F. M. Azevedo_ 

4 0.0 -50.0 

# iedge loele 2 2 # lopoe fe1 fe2 4 0.0 -50.0 6 0.0 -50.0 

# iedge loele 3 3 # lopoe fe1 fe2 6 0.0 -50.0 8 0.0 -50.0 # iedge loele 4 4 # lopoe fe1 fe2 8 0.0 -50.0 10 0.0 -50.0 

END_OF_FILE 

### **A.3 - Execução do programa** 

Depois de ter o ficheiro viga44_gl.dat completamente definido, escrever na linha de comandos o seguinte: 

prefemix viga44 # Verificar a coerência dos dados femix viga44 d # Calcular a matriz de rigidez global, calcular o vector solicitação global e resolver o sistema de equações lineares 

posfemix viga44 # Gravar diversos tipos de ficheiros de resultados 

Depois de executar as diversas opções do programa posfemix pode-se inspeccionar os ficheiros que foram criados, dos quais se destacam os seguintes: 

viga44_gl.lpt - dados formatados viga44_rs.lpt - resultados formatados viga44_me.s3d - malha indeformada 

245 

_Utilização do Programa Femix 3.1 - Álvaro F. M. Azevedo_ 

viga44_dm.s3d - malha deformada viga44_ps.s3d - tensões principais viga44_di.pva - campo de deslocamentos viga44_d.s3d - malha indeformada desconectada viga44_d_st.pva - campo de tensões relativo à malha desconectada 

### **A.4 - Visualização gráfica** 

Para visualizar os ficheiros de extensão .s3d deve-se fazer, no drawmesh , "File / Import" . 

Para visualizar os campos escalares contidos em ficheiros de extensão .pva deve-se fazer, no drawmesh , "PVA / Import" . Este opção deve ser seleccionada depois de se ter lido a correspondente malha num ficheiro de extensão .s3d . 

Para capturar o conteúdo de uma janela do drawmesh pode-se fazer "File / Export View Image" . Desta forma é criado um ficheiro com extensão .bmp , que pode em seguida ser inserido num documento Word , ou em qualquer outra aplicação Windows . 

Para combinar a malha indeformada com a malha deformada deve-se escrever na linha de comandos: 

s3djoin -o viga44_medm viga44_me viga44_dm 

Em seguida importar o ficheiro viga44_medm.s3d com o drawmesh (ver a Figura A.3). 



Fig. A.3 - Visualização da malha deformada com o programa drawmesh . 

246 

_Utilização do Programa Femix 3.1 - Álvaro F. M. Azevedo_ 

Para combinar as tensões principais com a malha indeformada deve-se escrever na linha de comandos: 

s3djoin -o viga44_meps viga44_me viga44_ps 

Em seguida importar o ficheiro viga44_meps.s3d com o drawmesh (ver a Figura A.4). 



Fig. A.4 - Visualização das tensões principais com o programa drawmesh . 

Na Figura A.5 encontra-se representado o campo escalar correspondente aos deslocamentos segundo _x_ 1. 



Fig. A.5 - Visualização do campo de deslocamentos horizontais com o programa drawmesh . 

247 

_Utilização do Programa Femix 3.1 - Álvaro F. M. Azevedo_ 

Na Figura A.6 encontra-se representado o campo escalar correspondente às tensões normais segundo _x_ 1. 



Fig. A.6 - Visualização do campo de tensões normais σ _x_ 1 com o programa drawmesh . 

### **A.5 - Considerações finais** 

Neste capítulo foi apresentado um exemplo muito simples de aplicação do programa FEMIX à análise de uma estrutura pelo MEF. Para fazer aplicações a outros tipos de estruturas aconselha-se a leitura da correspondente documentação [A.1] [A.2]. 

### **BIBLIOGRAFIA** 

- [A.1] - Azevedo, A. F. M.; Barros, J. A. O. - Manual de Utilização do Programa FEMIX 

- Versão 3.1, Porto, 2000. 

http://civil.fe.up.pt/Software/Femix_3.1/Femix_3.1_Manual.htm 

[A.2] - Azevedo, A. F. M.; Barros, J. A. O. - Manual de Utilização do Programa S3DCAD - Versão 3.0, Porto, 1998. 

http://civil.fe.up.pt/Software/Femix_3.1/pdf/S3dcad.pdf 

248 

