# **Comandos Básicos Prompt de Comando Windows**

## **IPConfig**
Ver as configurações do protocolo TCP/IP. Permite redefinir as definições do DHCP e DNS

- **/all:** Ver todas as configurações do TCP/IP
- **/release:** Remover a configuração de rede que estiver definida (DNS, DHCP)
- **/renew:** Reconfigurar os parâmetros da configuração de rede (DNS, DHCP)
  - informação transmitida pelo servidor DHCP (normalmente o router que controla a rede), para *resolver problemas de ligação*.
- **/flushdns:** Limpa o cache do sistema DNS no seu dispositivo
  - Normalmente, este comando funciona quando não se consegue ligar a outro computador na rede local, ou a um site web, devido à informação que está na cache DNS estar desatualizada.


## **Ping**
Testar a ligação à rede de um dispositivo. *Exemplo: Ping (endreço IP)/Dominio*

- **-a:** Ver o nome atribuído a esse dispositivo para além do endereço IP. *(Informações a mais)*
- **loopback:** Verifica o estado da rede
  - *IP 127.0.0.1* é o endereço IP definido para o loopback da comunicação num computador.
  - A resposta quer dizer que o software de rede do Windows está a funcionar.
- **/?:** Ver comandos do ping
- **-t:** Definir o tempo de execução do comando, o que pode ser útil para *examinar a perda de pacotes de comunicação* quando está a tentar encontrar problemas de ligação.

## **Tracert**
*Traça uma rota de cada pulo do pacote.* Serve para ver o percurso até um dispositivo alvo utilizando uma série de pedidos de eco ICMP. *Exemplo: Tracert (endreço IP)/Dominio*

- Inclui um valor TTL (Time To Live), que aumenta em 1 de cada vez, permitindo ver a lista de dispositivos que estão no percurso, quanto tempo demorou cada pedido e a sua duração.
- **-h:** Ajusta o número de salto até ao destino

## **NSLookup(Name Server Lookup)**
Ajuda a encontrar problemas relacionados com DNS. Mostra informações de ekuprro dentro do servidor DNS. O modo mais usado é o *não interativo* (Escrever o comando completo para obter as informações), o que quer dizer que ira ter de escrever o comando completo para obter a informação de que necessita.

- **nslookup:** Modo interativo. *Exit* para sair do modo intrativo
- **nslookup (Endereço IP):** Dispositivo remoto

## **NetStat (Network Statistics)**
- Mostra estatísticas de todas as ligações de rede. Permite-lhe perceber que portas estão *abertas e ligadas* de forma a encontrar e monitorizar problemas de rede no Windows 10 e respectivas aplicações. (Mostra informações estastiticas da rede)
  
- **-n:** Ligações ativas, mostrando os endereços IP e número da porta, em vez de estar a tentar descobri-los
- **-n (tempo):** Recarregar a informação automaticamente ao fim de algum tempo

## **ARP (Address Resolution Protocol)**
Informações acerca das ligações entre endereços IP e MAC (Media Access Control) que o sistema tenha conseguido resolver. (Mostra a tabela com informações da ligação do MAC e IP, podendo modifica-la e utilizada pra ver o MAC)

- **-a:** Mostrar a tabela arp
- **-a (IP):** Determinar o endereço IP

## **Route**
Mostra a tabela routing (direccionamento) que permite ao Windows perceber a rede e comunicar com outros dispositivos e serviços. (Permite ações de modificar e limpar a tabela se necessário)

- **route print:** Exibe a tabela de roteamento do computador

## **Netsh (Network Shell)**
- Permite aos usuários gerenciar e configurar várias configurações de rede. Através do netsh, você pode interagir com diferentes módulos de configuração e executar várias tarefas relacionadas à rede.


## **Informações Adicionais**

- **cls**: Limpa o terminal 

<br><br><br>

# **Backup e restauração no Windows**
O Windows oferece recursos embutidos para backup e restauração de arquivos e configurações. Aqui estão as principais opções disponíveis:

- **Backup e Restauração do Windows (Windows 7):** Essa é uma ferramenta mais antiga, presente no Windows 7, que permite fazer backup de arquivos pessoais e criar uma imagem do sistema. Você pode acessá-la indo em *"Painel de Controle" > "Sistema e Segurança" > "Backup e Restauração".* Ela permite criar backups agendados ou manuais e restaurar arquivos e pastas específicos ou todo o sistema.

- **Histórico de Arquivos (Windows 8/10):** O Histórico de Arquivos é uma função de backup automático disponível no Windows 8 e posterior. Ele faz backup de arquivos pessoais, como documentos, fotos e músicas, em um disco externo ou em uma pasta de rede. Você pode ativá-lo em *"Configurações" > "Atualização e Segurança" > "Backup" > "Adicionar uma unidade" ou "Mais opções"* para personalizar as configurações.

- **Backup do Sistema (Windows 10):** O Windows 10 introduziu uma nova opção de backup chamada "Backup do Sistema". Ele permite criar uma imagem do sistema que inclui o sistema operacional, configurações e arquivos pessoais. Para acessá-lo, vá em *"Configurações" > "Atualização e Segurança" > "Backup" > "Backup do Sistema"* e siga as instruções para criar um backup ou restaurar a partir de um backup existente.

- **OneDrive:** O OneDrive é um serviço de armazenamento em nuvem da Microsoft, que também pode ser usado para fazer backup e sincronizar arquivos entre dispositivos. Ele está integrado ao Windows 10 e permite armazenar automaticamente arquivos e pastas no OneDrive. Se você ativar essa opção, seus arquivos serão copiados para a nuvem e poderão ser restaurados posteriormente.

Além dessas opções nativas do Windows, também existem ferramentas de terceiros populares para backup e restauração, como o **Acronis True Image, EaseUS Todo Backup, Macrium Reflect, entre outros.** Essas ferramentas oferecem recursos avançados e opções de personalização para atender às suas necessidades específicas de backup e restauração.

<br><br><br>

# **Antivirus e Firewall Windows**
O Windows inclui recursos de segurança embutidos, como antivírus e firewall, para proteger o sistema contra ameaças. Aqui estão os principais recursos de antivírus e firewall disponíveis no Windows:

## Antivírus:

- **Windows Security (Windows Defender):** O Windows 10 inclui o Windows Security, que é um antivírus embutido conhecido anteriormente como Windows Defender. Ele oferece proteção em tempo real contra vírus, malware, spyware e outras ameaças. O Windows Security é ativado por padrão e é atualizado regularmente por meio do Windows Update.

- **Verificação de Segurança do Windows Defender:** Além da proteção em tempo real, o Windows Security também permite que você faça varreduras sob demanda para verificar arquivos e pastas específicos em busca de ameaças. Você pode acessar essa opção indo em *"Configurações" > "Atualização e Segurança" > "Windows Security" > "Proteção contra vírus e ameaças" e clicando em "Verificar opções".*

## Firewall:

- **Firewall do Windows:** O Firewall do Windows é um recurso de segurança integrado que monitora e controla o tráfego de rede. Ele ajuda a bloquear conexões indesejadas e protege seu computador contra ataques externos. O Firewall do Windows está ativado por padrão, mas você pode personalizar suas configurações indo em *"Configurações" > "Atualização e Segurança" > "Windows Security" > "Firewall e Proteção de Rede".*

- **Configurações avançadas do Firewall do Windows:** Além das configurações básicas, você também pode acessar as configurações avançadas do Firewall do Windows, onde é possível criar regras de entrada e saída personalizadas, permitir ou bloquear aplicativos específicos, configurar perfis de rede, entre outras opções. Para acessar as configurações avançadas do firewall, vá em *"Painel de Controle" > "Sistema e Segurança" > "Firewall do Windows".*

Embora o antivírus e o firewall do Windows ofereçam uma camada básica de proteção, algumas pessoas podem preferir utilizar soluções de segurança de terceiros mais abrangentes e com recursos adicionais. Existem muitos antivírus e firewalls disponíveis no mercado, como o **Avast, Bitdefender, Norton, Kaspersky, entre outros**, que oferecem recursos avançados de proteção contra ameaças.

## Ativar ou desativar o Microsoft Defender Firewall:
Para ativar ou desativar o Firewall do Windows Defender (anteriormente conhecido como Firewall do Windows), você pode seguir estas etapas:

1. Pressione as teclas "Win + S" para abrir a pesquisa do Windows.
2. Digite "Firewall do Windows Defender" e selecione o resultado correspondente.
3. Na janela do Firewall do Windows Defender, clique na opção "Ativar ou desativar o Firewall do Windows Defender" no painel esquerdo.
4. Agora você tem duas opções:
   - Para desativar o Firewall do Windows Defender, selecione a opção "Desativar o Firewall do Windows Defender" tanto para a rede privada quanto para a rede pública. Clique em "OK" para confirmar.

   - Para ativar o Firewall do Windows Defender, selecione a opção "Ativar o Firewall do Windows Defender" tanto para a rede privada quanto para a rede pública. Clique em "OK" para confirmar.