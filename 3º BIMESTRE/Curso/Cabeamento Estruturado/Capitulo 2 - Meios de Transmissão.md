#Escola #Curso #CabeamentoEstruturado #Livro #Capitulo2

**Reference:** [[Capitulo 2 - Cabeamento Estruturado.pdf]]

#### Objetivo
 Conceito de Sistema de comunicação e sua relação com o meio físico

#### Outros
- Material **dielétrico** (Isolante)

### 2.1 Cabos de pares trançados
- **Meio ou canal de transmissão:** é o caminho utilizado para que um sinal elétrico ou uma informação seja enviada de um transmissor para um receptor.

- Comunicação por **rádio** se utiliza o **ar**
- Em **cabeamento estruturado** se usa o **cabo**

- Cabeamento Estruturado é composto por:
	- Cabos
	- Componentes de Conexão
		- Patch Panels
		- Tomadas
- Tipos:
	- Condutores Paralelos
	- Cabos Coaxiais
	- Cabos Balanceados (Padrão)

#### 2.1.1 Princípios de funcionamento
- Um Circuito simples que consiste de dois condutores trançados entre si:
	- **Transmissão Uniforme:** Quantidade eletrica é igual em toda a extensão do cabo
	
	 - **Transmissão Balanceada:** Possui condutores eletricamente idênticos e simétricos com relação à terra e condutores vizinhos 
		- Ou seja, suas propriedades são iguais em diamentro, comprimento, conectores, etc 
		- A Tensão medida em um condutor do par em qualquer ponto do canal em relação à terra é igual à tensão medida no outro condutor no mesmo ponto.
		- Quanto maior a categoria mais requerem um melhor grau de balanceamento do canal

#### 2.1.2 Tipos de cabos e aplicações
- Podem ser Blindados e Não Blindados
- **Obs:** Cabos sem blindagem devem ser montados em componentes sem blindagem e cabos blindados devem ser montados em componentes blindados

- Tipos:
	- **U/UTP** (Unshielded/ Unshielded Twisted Pair): Par trançado sem blindagem
	- **F/UTP** (Foil/ Unshielded Twisted Pair): Blindagem geral externa feita com uma folha metálica.
	- **S/FTP** (Screened/Foiled Twisted Pair): Blindagem para cada par individual & Blindagem geral externa

#### 2.1.3 Componentes do cabeamento em cobre
- **Esquema Genérico:** É um ponto de distribuição de cabos e um ponto onde os usuários ou outros equipamentos serão conectados para interagir com ele. (Patch Panel com seus patch cords (distribuição de cabos) e tomadas (usuarios / pc))

- **Cordões** denominados **patch cords** (este é outro termo adotado em nosso jargão técnico)

- **Patch Panel:**
	- Comum 24 portas (RJ45)
	- Componente Passivo (Ou seja, não tem qualquer eletrônica nele)
	- Cabos balanceados são montados na parte traseira
	- A montagem dos cabos recebe a denominação de **terminação** (mais adequado) ou, popularmente, **“conectorização”**.

### 2.2 Cabos ópticos
- Baixas perdas entre um transmissor e um receptor e pode ser usado para transmitir sinais analógicos e digitais.
- Em alguns sistemas de comunicação se tem a necessidade de converter sinal elétrico em sinal óptico (E/O) ou virse-versa (O/E). Isso na etapa de *transmissão*

#### 2.2.1 Princípios de funcionamento das fibras ópticas
- Fibras ópticas são filamentos capilares constituídos de vidro e são utilizadas para a transmissão de sinais ópticos.

- A norma **NBR 14565** reconhece as fibras multimodo OM1, OM2, OM3 e OM4 (estas duas últimas conhecidas como fibras otimizadas para transmissão com fonte laser). Bem como as fibras monomodo dos tipos OS1 e OS2,

- Tipos:
	- **Multimodo:** Apresenta vários caminhos (modos)
		- **Índice degrau:** Sinal luminoso é mais atenuado e distorcido que nas fibras **índice gradual.**
		- Operam normalmente em comprimentos de onda de **850 nm e 1300 nm**.
		- Fonte **LED.**
	- **Monomodo:** Permiti que a luz se propague por um único caminho (modo) pelo interior de seu núcleo
		- Operam normalmente em comprimentos de onda de **1310 nm e 1550 nm.**
		- Fonte **Laser.**

#### 2.2.3 Componentes do cabeamento óptico
- Um sistema de cabeamento estruturado óptico também é composto por cabos e componentes de conexão, porém neste caso tanto os cabos quanto os componentes devem ser ópticos.
- **Esquema de backbone genérico:** Queremos dizer que todo cabeamento de backbone terá conexões ópticas entre dois distribuidores.
- Conectores **LC**, que são os mais utilizados na prática para conexões a partir de 1 Gb/s (também são ótimos para 10 Gb/s e 100 Gb/s)