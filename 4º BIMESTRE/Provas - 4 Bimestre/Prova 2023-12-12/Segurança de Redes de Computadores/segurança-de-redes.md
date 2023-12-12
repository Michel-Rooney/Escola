# Proxy
Servidores que comuniquem-se com sites em seu nome

```
User <-> Pagina da Google <-> Proxy <-> Internet ~~ Servidores
```

A aplicação faz uma requisição ao proxy que solicita a web a mesma requisição identificando por meio de autenticação o user. O Proxy também recebe a resposta do site e envia de volta até você.

## Funcionalidades
Como intermédio na web, servidores Proxy's podem atuar de diferentes formas.
- **Firewall's:** Sistema de segurança de rede de computadores que restringe o tráfego da internet para, de ou em uma rede privada.
- **Filtro de conteúdo:** Método para permitir, negar acesso a informação em redes através do conteúdo de sua informação.
- **Contorno de filtro:** Permite o acesso a sites bloqueados ou sistemas, rota com intermediário entre o usuário e a servidor desejado.
- **Caching:** Armazenamento intermediário de dados de aplicação atráves de hardware e software.
- **Segurança:** Proteção contra perigo ou ameaças compartilhamento de informação.
- **Compartilhamento de Conexões:** Pemrmite compartilhar uma única conexão de internet entre vários dispositivos em uma rede. Ao intermediar as solicitações de conexão, ele pode otimizar o uso de largura de banda, melhorando a eficiência e a velocidade de conexão para usuários de rede

## Tipos de Proxy's
1. **Proxies transparentes:** Não oferecem segurança externa ou privacidade. Recebe um Ip Real e consegue identificar o user via proxy
2. **Proxie Anônimos (Proxies de distribuição):** Prometem não passar seu IP aos sites e serviços, eles recebem IP Falso
3. **Proxies altamente Anônimo:** Utilizar as mesmas funcionalidades do Proxie Anônimo, porem eles disfarçam o seu uso do próprio proxy, assim o site não detecta que você usa proxy.


# Firewall
Garante a seguranã em redes de computadores. Funciona como uma barreira que controla o tráfego de dados.

## Tipos de Firewall
### 1. Firewall de pacotes: (Ver se é pacote - É pacote?)
- Verifica os pacotes de dados que entram e saem da rede, com base em regras predefinidas.
- Eficiente e rápido, mas não analísa o conteúdo do pacote.

### 2. Firewall de circuito (É pacote? Quem é a pessoa? (Destino Correto))
- Estabelece uma conexão virtual entre o remetente e o destinatário, conhecido como circuito.
- É verificada antes da troca de dados.
- O firewall de circuito é mais seguro, porém mais lento.

### 3. Firewall de Aplicação (É pacote? Quem é a pessoa? A informação interna é segura?)
- Analisa as camadas de aplicação do tráfego permitindo mais controle e segurança. Verifica a conexão e os dados do pacote bloquando atividade suspeitas como ataques DDoS, injections e malwares.

## Exemplos
1. Windows  Firewall
2. pfSense
3. Cisco Asa

# VPN - Virtual Private Network
Conexão Ponto a Ponto em redes privadas ou públicas. Um cliente VPN utiliza protocolos especiais baseados no TCP/IP, chamados de protocolos de túnel

## Benefícios
1. Amplia a conectividade
2. Aumenta a segurança
3. Reduz custos operacionais
4. Aumenta de produtividade
5. Simplifica a topologia de rede
6. Compatibildiade

## Elementos de uma VPN
1. Tuneamento
2. Autenticação das extremidades
3. Transporte subjacentes

```
----------------- ----------------- -------------------- -------
| Novo Cabeçalho | Cabelaçho IPSEC | Cabeçalho IpAntigo | Dados 
----------------- ----------------- -------------------- -------
                 | -----------------> Dados <-----------------|
```

## Segunraça VPN
- Firewalls
- Criptografia
- IPSEC (Cria um cabeçalho novo a partir da entrega (encapsulamento))
- Servidor AAA
  - Autenticidade
  - Autorização
  - Contabilização

## Tipos de VPN
- VPN acesso remoto
- VPN site a site
- VPN ponto a ponto

## Outros
### Camadas
1. Aplicação
2. Transporte
3. Rede / Enlace
4. Física

### Tipos net
- Extranet - VPN
- Intranet - Local
- Internet - Global


# Wireshark (Analisador de Pacotes)
Intercepta o tráfego da rede indentificando e registrando dados das informações trafegadas

- Interface de rede: Conecta o Hardware a enlace
- Ethernet: Internet Cabeada
- NAT: Vai fazer o switch comunicar com a sub-rede

## Outros
- 21 - FTP
- 80 - HTTP
- 443 - HTTPS