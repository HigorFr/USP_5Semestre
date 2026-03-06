#Aula 4 - COmunicação


#Primeiro os fundamentos de redes
#Camadas
    #App
    #Transporte
    #Redes
    #Enlace
    #Fisica


#Transporte fornece o socket, ip e porta. Reealiza a comunicação
    #CLiente-Servidor
    #Sincrona
    #Transiente (Ambos online)


#É possível haver middleswares que abstraem de maneira mais genérica a comunicação entre o app e a camada de transporte




#RPC (Remo Procedure Call)
    #Execução de procedicmentos remotamente
    #Cliente Chama função -> Stub faz um send ("RCP func, param") -> SO Recebe e manda para a network. -> Chega na placa de rede do servidor -> SO do servidor recebe e manda para o stub do servidor (Pela função recieve) -> Stub do servidor descobre da mensagem a função e a chama localmente e retorna o resultado.
    #Na hora de voltar o caminho é o mesmo, só que ao contrário, o stub do servidor manda a resposta para o cliente, e o stub do cliente recebe e retorna para a função local.

    #STUB é o manipulador de sockets da programa, na verdade normalmente le fica incluso no próprio programa
        #SO em sí só vai te falar a API de "SEND" e "RECEIVE", o básico.

    #Ponteiro e memória tem que ser adequados, já que o endereço da memoria não será igual. É possível delarar o valor da variável no servidor usando um *p = .... para só então usar &p... em seguida (Isso pode gerar problemas dependendo do tamanho). Também tem a possibilidade de desabilitar 



#Comunicação orientada a mensagens
    #ZeroMQ
    #Biblioteca transiente, adiciona novos tipos de socket.
        #REQ-REP (Request-Reply), que funciona como o RPC, o cliente faz uma requisição e espera a resposta do servidor
            #1- Send, 2- Receive, 3- Send, 4- Receive. É 1 pra 1
        
        #PUB-SUB (Publish-Subscribe), onde o cliente se inscreve em um tópico, e o servidor publica mensagens nesse tópico, e o cliente recebe essas mensagens é 1:N
            #1- Subscribe, 2- Publish, 3- Receive
        
        #PUSH-PULL, um push é exatamente igual a um REQ, e um PULL é exatamente igual a um REP, mas a diferença é que o PUSH pode enviar mensagens para vários PULLS, e os PULLS podem receber mensagens de vários PUSHES, ou seja, é meio que um N:N em um pipeline
            #Tem sockets tipo pull e tipo push, e conforme a mensagem vai ficando disponível os pull vão pegando


#Mensage Passing Interface (MPI)
    #Não é implementação, é uma interface, (OpenMPI, por exemplo implementa)
    #POssui clusters
    #Grupo de processos com idenficador Gid e Pid
    
    #Tipos de Send: Send, Ssend (Synchronous Send), Bsend (Buffered Send), Rsend (Ready Send), Isend,  Send recv etc...
    #Ou seja, é bem completa, muitas variações, só que mais complexa.




#Comunicação Persistente
    #Abstração de fila de mensagnes
    #Haverá um processo transmissor, que colocará mensagens em uma fila e um processo receptor, que irá tirar mensagens e lendo dessa fila.
    #Tem basciamente 4 operações
        #Put, colocar coisas na fila
        #Get Bloqueante, que pega a mensagem da fila, mas se não tiver nada ele espera
        #Get Não Bloqueante, chamada de POLL, que tenta pegar a mensagem da fila, mas se não tiver nada ele retorna um erro
        #Notify, que assincronizadamente avisa quando recebe uma mensagem nova
    #Nome de alto nível, 
    #A fila pode ser ou não persistente, ou seja, mesmo que um dos lados esteja offline, a mensagem persiste para eventualmente ser usado, inclusive se ninguém tiver online.




#ADvanced Message Queuing Protocol (AMQP)
    #Também só uma interface especificada, tem várias implementações, como RabbitMQ
    #ELe tem uma hierarquia de comunicação
        #Conexões tem canais e canais possuem filas
        #Existe um servidor de filas, que resolve os nomes e tudo mas
    #Garantia de entrega


#Multicast
    #Multicast, um nó direto para vários, difícil implementar devida a estrutura.
    #Precisa de overlay para fazer o multicast
    #Cria se um grupo de nós alvo por um overlay, e então realiza um broadcast para eles.
    #Maneira mais eficiente de realizar isso é através de uma árvore, o overlay pode ser meio ineficiente pois isso não leva em consideração a infraestrutura física, e isso faz com que o delay não seja ótimo.
        #Isso pode ser medido por link stress, o numero de vez que um link é usado.
        #Delay strech é basciamente uma a fração delay obtido / delay ótimo, ou seja o quão bem ela está performando



#Visão broadcast com P2P
    #Em uma rede mesh (Rede conectado parcialment, aleatoriamente)
    #Algumas opções de broadcast:
    #Flooding (Força bruta), envia para todos e todos enviam para todos
    #Controle pflood, que faz um sorteio
    #Pode ser estruturado, que só utiliza a estrutura mesmo



#Tem também os protocolos epidemicos
    #Espalham "como doença"
    #Anti-Entropia - Pull e Push, 
        #Push - onde em um grupo, cada nó "contaminado" escolhe outro aleatorio (Pode ser igual) para contaminar. Isso é probabilistico, exponencialmente.
        #Pull - Invés de contaminar, cada nó ele pede informação nova de algum aleatorio. 
        #E tem o ambos, que faz os dois, ou seja, cada nó "contaminado" escolhe um aleatorio para pedir informação nova, e também escolhe um aleatorio para contaminar. Isso é o mais eficiente dos três, pois tem a vantagem de ser mais rápido que o pull, e mais eficiente que o push.
    
    #Rumor Spreading
        #Cada nó tem um contador de quantas vezes ele já falou a mesma informação (pra quem já ouviu), e quando esse contador chega a um certo valor, ele tem uma chance de parar de falar essa informação, ou seja, ele se "cura" da doença. 
        #Isso é útil para evitar que a informação fique circulando eternamente, e também para evitar que a informação fique circulando por muito tempo, o que pode ser ruim em alguns casos, como em uma rede de sensores, onde a informação pode ficar circulando por muito tempo e consumir muita energia.
        #Existe uma chance do rumor parar e acabar, sem ninguém ter ouvido o rumor.






