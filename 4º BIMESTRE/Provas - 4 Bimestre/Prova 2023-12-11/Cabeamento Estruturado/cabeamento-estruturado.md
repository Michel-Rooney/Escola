# Slide 06 - Testes e Verificação de Desempenho
Objetivo  de  assegurar  que  uma  rede  esteja funcionando de maneira confiável, eficiente e de acordo  com  os  padrões  desejados.

## Testes de Conectividade
São  utilizados  para verificar se os dispositivos em uma rede podem se comunicar  uns  com  os  outros

### Tipos de Conectividade
- Física (Por meio de cabos e conexões de hardware)
- Lógica (Garantindo que os dispositivos estejam configurados corretamente para se comunicarem na rede)

### Exemplos de testes de conectividade
- **Ping (Lógico):** O comando "ping" é usado para verificar a conectividade entre dois dispositivos. Ele envia pacotes de dados de um dispositivo para outro e verifica se eles são recebidos e retornados com sucesso.

- **Verificação de endereços IP (Lógico):** Garantir que os dispositivos estejam configurados com os endereços IP corretos e que pertençam à mesma sub-rede

- **Testes de portas (Lógico):** Verificar se as portas de rede necessárias estão abertas e funcionando

- **Teste de cabo (Físico):** Verificação física dos cabos de rede para garantir que não haja danos ou interrupções


#### IPERF
- Linha de comando
- Ferramenta de código aberto
- Testes de desempenhos em redes de computadores
- Originalmente desenvolvido para medir a largura de banda e a taxa de transferência em redes TCP/IP e UDP
- Opera em modelo de cliente e servidor, onde um computador atua como servidor e outro como cliente. O servidor gera tráfego de teste e o cliente mede o desempenho

##### Principais funcionalidades
- **Teste de Largura de Banda:** Útil para determinar quanto tráfego a rede pode acomodar. (Atenda as necessidades de transferências de dados)

- **Teste de Taxa de Transferência:** Mede a taxa de transferência real de dados entre dois pontos na rede. Determina o desempenho efetivo da rede

- **Teste de Latência:** Atraso na transmissão de dados de um ponto a outro na rede. Baixa latência é essencial para aplicações em tempo real, como videoconferência e jogos online

- **Testes de UDP e TCP:** Faz teste de garantia e velocidade
  - **TCP:** Confiabilidade na entrega de dados, porém lentindão
  - **UDP:** Transmissão rápida, porem sem garantias de entrega confiável

## Verificação de Desempenho
"Afinal  nossa  rede  pode  está  disponível  mas  não 
necessariamente  ela  estará  funcionando  com  toda  a 
capacidade possível ou disponível."

### Exemplos de Testes
- **Largura de Banda:** Quantidade máxima de dados que podem ser transmitidos pela rede em um determinado período de tempo. (Mede a capacidade da rede de transferir dados)
- **Taxa de Transmissão:** Velocidade real com que os dados são transmitidos na rede. (Mede a eficiência da taxa de transmissão)
- **Latência:** Atraso na trasnmissão de dados através da rede. (Mede o tempo que leva para os dados percorrem a rede de um ponto ao outro)
- **Perda de Pacotes:** Avaliam a porcentagem de pacotes de dados perdidos durante a transmisão, o que pode indicar problemas na rede


# Slide 07 - Manutenção do Cabeamento Estruturado
"Toda a eficiência dessa estrutura depende diretamente da correta manutenção do cabeamento estruturado"

## Problemas que a manutenção pode evitar
- Perda de qualidade
- Interferências
- Interrupções na transmissão de dados
- Paralisação de serviços administrativos que dependem do processamento de informações, dados voz ou imagem
- Indisponibilização da conexão à internet
- Interrupção de circuitos internos de TV e voz que afetam o monitoriamento, a comunicação interna e a segurança das empresas
- Perda de acesso a dados ou mesmos a sistemas administrativos digitais utilizados em rotinas diárias de trabalho
- Queda de eficiência em função de perdas na velocidade ou qualidade da transmissão de dados

## Como surgem esses problemas no cabeamento estruturado?
- Infiltrações
- Descargas elétricas
- Golteiras
- Interferências elétricas e magnéticas
- Redes mal projetadas ou ampliadas sem planejamento (Pode causar incopatibildiade)
- Rachaduras na estrutura física da edificação
- Reforma civil -> Cabos podem ser rompidos
- Poeira

## Pertubações
- **Eco:** Ouvimos nossa própria voz. Causado pela reflexão de sinal transmitido ao logo dos cabos

- **Ruídos:** Distúrbios elétricos que ocorrem em uma transmissão por agitação de elétrons ou surtos de corrente elétrica

- **Atenuação:** Deformação  com perda de potência do sinal. Gerada por cabos ou filtros

- **Retardo:** Atrasos na frequência d eum sinal de comunicação. Também pode deformar o sinal transmitido

- **Harmônica:** Deformação do sinal é causada por amplicaficação de sinais de espectro múltiplo do sinal princiapl

- **Difonia:** (Crosstalk ou  Linha cruzada). Par de fios do cabeamento estruturado provaca interferência em outro par. Um exemplo é quando ouvidos conversas de outras pessoas ao fazemos uma ligação telefônica

- **Agitação de Fase (Phase Jitter):** Instabilidade na frequência do sinal de comunicação

- **DROPT-OUT:** Perda do sinal por um tempo muito curto. Causado, normalmente por ruídos ou outras deformações na transmissão


## O plano de manutenção do cabeamento estruturado
- Vistorias rotineiras para corrigir e monitorar toda a infraestrutura da rede
- Executar o diagnóstico apontando soluções eficazes para os problemas encontrados
- Atender aos pedidos de alterações ou remanejamento de pontos
- Executar a instalção de novos pontos de utilização dos serviços de dados
- Fazer todas as conectorizações encessárias ao funcinamento eficaz da rede
- Apresentar relório de certificação dos pontos. Isso é importante para o controle da rede estruturada quando são feitas alterações
- Realizar laudos técnicos de avaliação da instalação elétrica e do cabeamento estrutruado

## Testador, qualificador e certificador de cabos
- **Testador de cabos (Pequenos reparos):** Testa a continuidade dos condutores, apontando erros ou coneções cruzadas que possam interferir no bom funcionamento do sistema
- **Qualificador de cabos:** Identificar se o cabeamento está transmitindo os dados com eficiência e com segurança
- **Certificador:** Ferramento que realiza a medição e testa todas as funcionalidades dos cabos comparando com as normas vigentes