#Aula2

#Arquitetura
    #Organização de componentes, componentes sendo aquilo que compõe um sistema
    #Organzizar  com interfaces, topologias, conexões, dados etc..., 
        #Exemplo: "Arq em Camadas, onde requisição flui em sentido único"
            #-Rede, MVC etc...
        #Exemplo: "Arquitetura orientada a serviços, onde cada serviço é independente, e se comunicam via mensagens"
            #-SOA, Microserviços etc...
    
    #Remote Procedure Call (RPC)
        #Permite que um processo chame um procedimento em outro processo, como se fosse local
        #Meio que o objeto mesmo em outro computador, e as funções publicas são chamadas em outras máquinas
        #Em um computador fica só a assinatura, e a implementação fica em outro computador. Um stub fica no cliente, e outro no servidor, e eles se comunicam via mensagens. O cliente chama o stub, que envia a mensagem para o servidor, que chama o stub do servidor, que chama a função real, e depois retorna a resposta para o cliente.
        #Isso permite sincronizar objetos, que facilita bastante



#Integrando  componentes

#Interfaces
    #Interface é o contrato, o que é feito
    #Pode ser complexas, ou simples, que definem o conjunto de operações possíveis
    #Simples
        #Ex Restful - PUT, DELETE, GET, PUSH. Ou seja, operações complexas precisam executar ela várias vezes, mas é mais moldável
        #Nomeação clara



#Arquitetura e Publish Subscribe
    #Vários componentes e um componente central que gerencia os eventos.
    #Todos componentes chamam esse gerenciador invés de ficar interagindo entre sí
    #Funções Publish e Subscribe, onde o componente publica um evento, e os outros componentes se inscrevem para receber esse evento.
        #Ex "COmponente 2 precisa do time SP, então ele manda Subscrinbe(Time= SP) "
    #Desacomplamento referência

#Desacoplamento referência
    #Comunicação não é feita de acordo com uma referẽncia, mas com um tópico, não tem destino

#Desacoplamento temporal
    #Seria a comunicação não precisar acontecer ao mesmo tempo, ou seja, o componente pode publicar um evento, e o outro componente pode receber esse evento em outro momento via algum buffer.


#=====

#Middleware
    #Basicamente um software que fica entre o sistema operacional e as aplicações, e fornece serviços para as aplicações, como comunicação, segurança, etc...
    #Exemplo , o SO fornece o socket, mas o middleware fornece uma API mais fácil de usar, como o gRPC, que é um framework de RPC, ou o Kafka, que é um sistema de mensagens.
    #Meio que sendo uma camada em comum para todas as máquiaas, independente do SO e do APP


#Arquitetura P2P
    #Invés de cada componente ter uma função diferente, aqui todos os componentes são homogêneos na funcionalidade, todos são clientes-servidor entre sí, gerenciando várias conexões de tipos diferentes ao mesmo tempo.
    #Precisa de uma lista de pares conhecidos
    
    #Estruturado
        #Toplogia é bem determinada, seguindo uma regra específica, facilita operações de busca
            #Ex Hipercubo, cada bit vai diferenciado os pares de cada dimensão e identificando o nó de cada peer
                #Requer manutenção, toda vez que peer saí ou entra, a regra precisa se atualizar
                #Útil para fazer DHT (Distributed Hash Table), onde cada peer é responsável por um intervalo de chaves, e a busca é feita seguindo a topologia, até encontrar o peer responsável pela chave desejada.
            #Ex Chord, onde existe um anel de peers, e certos peers atravessam esse anel, que transforma a busca em logarítmica.

    #Não estruturado
        #Topologia é aleatória, não segue uma regra específica, mais fácil de manter, mas dificulta operações de busca
        #Requer flooding, ou seja, enviar a mensagem para todos os peers conhecidos, e eles enviam para os seus peers conhecidos, e assim por diante, até encontrar o peer desejado ou atingir um limite de hops, resposta rápida, mas cara.
        #Tem o método random walk, onde a mensagem é enviada para um peer aleatório, e ele envia para outro peer aleatório, e assim por diante, até encontrar o peer desejado ou atingir um limite de hops, mas lento, mas menos caro.
    
    #Super peer
        #Alguns peers são mais poderosos, e ficam responsáveis por gerenciar os outros peers, facilitando operações de busca, mas criando um ponto de falha.


    #Block chain
        #Cadeia de blocos, com informações dele, do bloco anterior e um hash formado com elas
        #Informações do tipo, novo usuario, transferencia etc...
        #Varios peers tem uma cópia da cadeia, e varios peers competem para ver quem vai adicionar o próximo bloco, chamado validador, com as informações novas e transações novas.
            #O validador então adiciona o bloco na cadeia, e os outros peers validam esse bloco, e se for válido, eles adicionam na cadeia deles também, e assim por diante. (O validador recebem um pouco de bitcoin)
            #Validar é resolver um problma computacional difícil, chamado proof of work.

        #Proof of work é resolver um problema computacional difícil
        #Proof of Stake é outro método, onde cada peer é escolhido aleatoriamente, mas com uma probabilidade proporcional à quantidade de moedas que o peer tem, ou seja, quanto mais moedas, mais chances de ser escolhido como validador, e assim por diante.

    


#Wrapper (Adaptador)
    #