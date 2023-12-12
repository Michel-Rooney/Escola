# Configuração Básica do Servidor
## Outros
- O servidor precisa de 2 interfaces
  - Modo Bridge
  - Modo NAT (Não funcona sozinho) (Rede interna - Não permite saida de pacotes)
- Nunca minha interface ligada a WEB, não pode estar em mode BRIDGE por causa da segurança, já que teroa acessp ap server

## Comandos
- **sudo apt get update:** Esse comando permit eao servidor atualizar sua lista de pacotes/serviços em relação ao banco de dados da linux na nuvem
- **lspci:** Permite ao adm verificas todas as interfaces e dispositivos instalado no servidor. (pc interface)
- **clear:** limpa a tela
- **ip address | ip addr | ip ad**


## Passos
1. Atualizar o sistema
   - **sudo apt get update:** Esse comando permit eao servidor atualizar sua lista de pacotes/serviços em relação ao banco de dados da linux na nuvem
2. Verificar os dispositovs conectados ao servidor
   - **lspci:** Permite ao adm verificas todas as interfaces e dispositivos instalado no servidor.
3. Verificar as informações sobre os dispositivos e endereços da rede.
    - **ip address | ip addr | ip ad**
    - **LO:** Interface de Loopback: Permite que um cliente e um servidor em um mesmo host se comunique entre si, usando o protocolo TCP (**endereço reservado:** inet 127.0.0.1/8)
    - **enp0s3:** Nome da interface está atribuida a bios, slot, marcaddress. O que garante que não ocorra a troca das interfaces em caso de atuaçozação
4. Instalar o net-tools e usar o ifconfig
    - **sudo apt install net-tools:** Baixa pacotes basicos para ver a rede (ifconfig)
5. Alterar a interface para o modo Bridge
    - Só consegue fazer a alteração com a máquina deslgiada
    - Precisa fazer essa alteração pois o modo NAT não deixa nossa rede "visível na rede" e não permite o compartilhamento de dados
    - Depois de configurado é como se tivesse ligado o servidor ao switch da rede
6. Reniciar as configurações de interface
    - ifdown enp0s3
    - Pegar um novo ip: ifup enp0s3
    - Apartir daqui o pc já é visível e pode ser pingado (ping ip-do-server)

## Pratica
1. Alteração do IP fixo atráves das configurações internas do sistema
2. Entrar na pasta que faz referência as configurações de internet (network) do nosso servidor
    - cd /etc/netplan
    - Editar o arquivo: 00-installer-config.yam1
3. Inserir as seguintes configurações:
    ```
    renderer: networkd
    ethernets: 
        enp0s3:
            addresses:
                - 192.168.1.5/24
            gateway4: 192.168.1.1
            nameservers:
                addresses: [1.1.1.1, 8.8.8.8]
    ```

        renderer: networkd: Especifica que o Netplan deve usar o networkd como o backend para renderização de configurações de rede. O networkd é um componente do systemd responsável pela configuração de rede.

    **ethernets:** Indica que as configurações a seguir se aplicam a interfaces Ethernet.

    **enp0s3:** É o nome da interface Ethernet. Este pode variar dependendo do sistema, mas é comumente encontrado em instalações padrão do Ubuntu.

    **addresses:** - 192.168.1.5/24: Define o endereço IP da interface enp0s3 como 192.168.1.5 com uma máscara de sub-rede /24. Isso significa que a máscara de sub-rede é 255.255.255.0, indicando que os primeiros 24 bits do endereço IP são destinados à rede.

    **gateway4:** 192.168.1.1: Define o gateway padrão para 192.168.1.1. O gateway é o roteador que permite a comunicação com outras redes ou a Internet.

    **nameservers:** addresses: [1.1.1.1, 8.8.8.8]: Configura os servidores DNS para a interface enp0s3. Neste caso, são fornecidos dois servidores DNS: 1.1.1.1 (da Cloudflare) e 8.8.8.8 (da Google).

    - Por fim basta executar o arquivo para aplicar
      - sudo netplan apply


# DHCP
## Passos
1. Ip estatico ja definido
2. Baixar o serviço de dhcp do linux:
    - sudo apt-get install isc-dhcp-server
3. Configurar os valores de temp lease
    - temp lease: tempo medido em segundos, que determina quanto tempo aquele endereço ficará alocado para um determinado host. Ou seja a cada fim do ciclo temp release esse endereço caso não esteja mais sendo utilizado volatará para o escopo DHCP.
    - tempo médio de 8 horas -> 28.800s
4. Editar o arquivo tempo realease:
    - sudo nano /etc/dhcp/dhcpd.conf
5. Alte as configurações do default-lease-time
6. Aplicar o lease time
   1. subnet 192.168.1.0 netmask 255.255.255.0 { 
        - Range 192.168.1.11 192.168.1.30;     
        - Option routers 192.168.1.10;     
        - Option domain-name-servers 192.168.1.10;     
        - Option domain-name "example.com";   
      - }


    a subnet representa o endereço da rede, podemos receber que o final e 0 portanto é necessariamente a rede.   
    
    a máscara por ser classe C é 255.255.255.0 ou seja /24.  
    
    
    o range é o espaço de alocação do DHCP, os endereços que serão distribuídos, nesse  caso os endereços serão do 11º endereço até o 30º Endereço, um range de 20 Endereços 
    válidos para distribuição.   
    
    option routers faz referência a saída do router ou seja o gateway, no caso o endereço  onde vai está nosso DNS, nosso próprio servidor 192.168.1.10;  
    
    Na opção de DNS - domain name server utilizaremos também nosso próprio servidor é nele que estará nosso servidor, pode ser adicionado mais de 1 servidor caso queira. e no domain name é apenas um exemplo de pesquisa de domínio como vimos do Windows Server;
7. Reserva dos IP
   1. No mesmo documnento:
   2. host Server1 { 
      - hardware ethernet 08:00:07:26:c0:a5;
      - fixed-address 192.168.1.10;   
    }

    a aba hardware ethernet faz referência ao endereço MAC da placa de Rede para verificar basta inserir o comando ifconfig como já foi mostrado:
8. Ativar o Servidor
    - sudo service isc-dhcp-server restart


# Outros
O Apache é um servidor de código aberto e nome oficial é Apache HTTP Server, mantido pela Apache Software Foundation, e alimenta cerca de 46% de todos os sites hospedados na internet.

O Apache permite que donos de sites mostrem e mantenham seus conteúdos na internet – daí o nome de “servidor de internet”. Ele é um dos mais antigos e confiáveis servidores de internet. A sua primeira versão, por exemplo, foi lançada em 1995, há mais de 20 anos.

Quando alguém visita um site, esse visitante entra em um domínio na barra de endereço por um navegador. Em seguida, o servidor entrega os arquivos solicitados atuando como se fosse um como um entregador de encomendas, só que virtual.