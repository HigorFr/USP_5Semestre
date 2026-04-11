#Aula 5


#Cordenação

#Construção em cima da troca de mensagem da aula anterior

#Primitivas úteis em diversos contextos.

#Ordenação de eventos
#Exclusão Mútua
#Eleição de líder




#Ordenação de Eventos
#Estabelecer ordem
#Dois processos que não interagem, não possuem dessincronia observável. Ou seja, a ordem é indistinguível

#Pratica mais comum: Timestamp
    #Tempo atual fica relacionado a mensagem, ao evento criado. Necessíta de algum tipo de relógio global.
        #Cada máquina entretanto terá o seu relógio, e eles podem estar dessincronizados.
        #O cristal de quartzo (Presente em todo computador), possui um desvio, que dessincroniza ao passar to tempo.
        #Para utilizar o relogio portanto é melhor usar o UTC, que é um padrão de tempo global. Isso é sincronizado via rede.
            #Baseado no decaimento do césio, uma média entre vários relógios atômicos.


    #Protocolo NTP (Network Time Protocol) é utilizado para sincronizar os relógios das máquinas, e é baseado em um modelo cliente-servidor, onde o cliente envia uma requisição para o servidor, e o servidor responde com a hora atual. O cliente então calcula o desvio entre a hora do servidor e a hora local, e ajusta o relógio local de acordo.
        #Dado que  T1 é a hora que o cliente envia, T2 a hora que chega ao servidor, T3 a hora que o servidor responde, e T4 a hora que o cliente recebe a resposta, o cliente pode calcular o desvio
        #T2 será T1 + Desvio, E T2 - T1 será igual a T4 - T3
        #Logo Desvio
        #  = (T2 - T1 + T3 - T4) / 2, e dá para ajustar o relógio local de acordo.


#Relógios Lógicos
    #Com base na premissa que processos que não se comunicam não possuem dessincronia observável, é possível estabelecer uma lógica.

    #Relógio de Lamport
        #Relação entre A e B será "Ocorreu antes", 
        #Se A e B ocorrem no mesmo processo, A -> B
        #Se A é o envio da mensagem Tx(m), e B é o recebimento da mensagem Rx(m), em qualquer processo, A -> B
        #Se A-> B e B -> C, então A -> C, transitividade.

        #Na prática, cada processo P possui um relógio Lp, como um contador, o evento local incrementará Lp em 1, e ao receber mensagem Lp assumirá o max(Lp, lm) + 1, onde lm é o relógio da mensagem recebida.


        #Multicast totalmente ordenado
            #Cada nó recebe a requisição assim como o timestamp igual do nó que quer fazer a mudança.
            #Cada nó terá um fila de mensagens, e o middleware só ira passar para a aplicação quando receber um ACK dos outros nós, para garantir que todos os nós receberam a mensagem e que consequentemente não ficou nenhuma nova requisição defasada pendente.
            

        #Relógio Vetoriais
            #Noção de causalidade entre os eventos.
            #Sistema de cordenada, onde é somado em cada i do vetor é referente ao tempo de um dos processos que interagem entre só.
            #Todos começam com (0,0,0), e cada processo incrementa o seu tempo local, ou seja, o i do vetor referente a ele, e ao enviar uma mensagem ele anexa o vetor, e ao receber uma mensagem ele faz o max entre o vetor da mensagem e o seu vetor local, e depois incrementa o i do vetor referente a ele.
            #É possível identificar atualização concorrente se der divergẽncia.






#Exclusão Mútua
    #Recurso compartilhado que apenas um processo pode acessar o recurso por vez.
        

    #Centralizada
        #Possui um nó como cordenador. Os processos mandam requisições para usar o recurso e o cordenador coloca eles em uma fila garantindo o acesso individual em ordem.

    #Baseado em Lamport
        #Não é tão robusto, porque se um processo falhar, o recurso pode ficar bloqueado, e não tem como recuperar.
        #Basciamente 3 mensagens, Request, Reply e Release aos elementos na rede, para gerenciar o acesso a área crítica.
        #Requisição: O processo envia uma mensagem de requisição para todos os outros processos, e espera receber uma resposta de todos eles.
        #Resposta: O processo responde a mensagem de requisição, e só pode responder a uma.
        #Liberação: O processo envia uma mensagem de liberação para todos os outros processos, indicando que ele terminou de usar o recurso compartilhado.
            
        
    #Token Ring
        #Parecido com o visto em Sitemas Operacionais, cada nó tem um token que permite usar a região cricia, quando ele termina ele passa para próximo.

    #Tem o por votação
        #Para entrar na região critica, precisa da aprovação De base(N/2) +1 votos dos outros processos.
        #Mesmo se uma parte da rede falhar ainda da pra ter votos suficientes
        #Garante exclusão mútua.
        #Da pra disperdiçar mensagem se tiver por exemplo 3 processos concorrendo, e cada um ficar com 33%. Isso exige novas eleiçoes




#Eleição de Líder
    #Mecanismo para escolher um processo para ser o líder, ou seja, o responsável por coordenar certas atividades. Esse algoritimo é para evitar que um seja "Hard Coded". 
    
    #Útil para funções diferenciadas

    #Eleição por Bullying
        #O mais forte é o lider, através de um identificador único númerico.
        #Quando um processo identifica que o líder morreu, ele manda pedido para os indentificadores mais maiores. Esses processos negam e tentam eles mesmos serem os líderes recursivamente. Até algum grande suficiente não ser negado pelos seus maiores (Porque cairam).
        
    #Eleição por Anel
        #Organiza os nós em um círculo, quando o líder cai, o que aponta para ele irá identificar e iniciará uma eleição começando pelo qual o líder apontava. Cada nó irá por seu nome numa lista e quando todos colocarem, e ter dado uma volta completa, é escolhido alguem da lista para ser o líder (Através de qualquer heurística, como o pŕoprio bullying)

    #Votação
        #Cada nó está em um dos 3 estados, seguidor, candidato ou líder
        #Quando o líder cai, algum nó irá identificar que caiu, os nós que por padrão são seguidores podem se tornar candidato então.
        #Ai se pede votos enviando mensagems a todos os nós se candidatando, onde precisa de maioria.
        #Se o líder do periodo N voltar a vida, ele pode cancelar a eleição do periodo N+1

    #Blockchain
        #POW e POS
        #Pode ser considerado eleição de líder.
        


