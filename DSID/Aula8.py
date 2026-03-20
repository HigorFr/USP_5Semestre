#Toelrância a Falhas



#Defeiito
    #Problema que é observavel

#Erro
    #É o proprio bug na implementção, ou seja, o código errado

#Falha
    #É a causa do erro, por exemplo um programador desatento

#Tempo de erro
    #Previnir (Antes)
    #Tolerar (Durante)
    #Remover (Depois)


#Duração da Falha
    #Transientes (Só tentar novamente que ela se resolve (Tipo erro em entrega TCP))
    #Intermitentes (Repetem-se, mas não são permanentes, duram um certo tempo)
    #Prenes (Não se resolve sozinha)


#Tipos de Falha
    #Crash˙Serivdor para abrupdamente, mas sem problemas até parar
    #Omissão: sem reposta
    #Temporal: informação chegou tarde
    #Resposta: Resposta chegou, mas com valor errado ou em um estado errado (Para maquinas de estado), ela é constante para todos
    #Arbitrária ou Byzantina: Respostas diferentes, inconsitência (Usado muitas vezes para manipular comportamento do sistema)



#Modelos para detectar falha
    #Failstop: Crash detectável de forma confiável
    #Fail-noisy: Falhas de crash eventualmente detectáveis, com delay e possibilidade de erro
    #Fail-silent: Falhas de crash e omissão não são diferensiáveis. (Ou seja, não tem como saber se o servidor parou ou se ele está demorando para responder)
        #Mais realsita, pois na internet é quase impossível diferenciar
    #Failsafe: Falhas de crash e omissão são diferensiáveis, mas não são detectáveis de forma confiável. (Ou seja, tem como saber se o servidor parou ou se ele está demorando para responder, mas não tem como ter certeza disso)
    #Fail-arbitrary: Falhas de crash, omissão, resposta e temporais não são diferensiáveis. (Ou seja, não tem como saber se o servidor parou, se ele está demorando para responder, ou se ele está respondendo com um valor errado)


#Tipos de redundância
    #Informação: Redundancia do dado, colocar codigo para recuperação usando info extra
    #Tempo: Tentar novamente depois de um tempo
    #Fisica: Aqui  é de fato criar a Replicação, comentada na ultima aula, pode ser hardware ou processo (Que será abordada).


#Redundância de Processos
    #Grupo de Processos
        #Um Cliente interagem com um grupo de processos, que em sua visão é só um. Esses porcessos podem se organizar hierarquicaemnte ou de forma plana.


    #Consenso
        #Todos os processos (Sem falhas) executam os memesmos comandos na mesma ordem, ou seja, há um consenso na escolha dos comandos
    
        #Protocolos de consenso

            #Flooding (Assim como tudo que é distribuido, tem jeito por flooding). Fail-Stop e Plana.
                #Cada Processo P envia uma lsita de comandos pendentes, Pi recebe a lista {Pj | j difere i}
                    #Concatena, escolhe o proximo cmd e anuncia a sua escolha
                    #Se ele não receber alguma resposta, ele aguarda a proxima roddada. Se anúncio, exec.


            #Raft: Fail-Noisy (Pode ter atraso), e Primário, eleição de líder por mandatos
                #Todas requisições de clientes são diretas para o lider
                #Todas requisições passam pelo líder, que mantem um lóg de comandos
                    #Entradas podem ser operações, mandato ou indice e mantem #Op, feitas e "C", que é o numero de operações feitas.
                #Manda periodicamente Heartbeats e um C, para todos processos saberem numero de operações feitas
                #Lider ao R requisição, poe no log <o,p,i> e envia o log para os seguidpores
                #Seguidores ao receber o log, atualizam a copia local, executam até C operações e depois respondem com ACK
                #O lider, ao receber a maioria de ACK, atualiza o C. (por ser maioria, ele tolera falhas, 2k+1 = n)
                
    
            #Paxos
                #Fail-silent
                #Suporta mensagem fora de ordem
                #Funciona em 2 Fases - Primeiro detecta-se o líder (para desambiguizar caso tenha dois lideres) e a segunda é a execução
                #Execução é muito semelhante ao raft
                




    #Falhas Arbritárias
        #Se chamam bisantinas por conta do "Acordo Bisantino"
            #Só por curiosidade, o acordo bisantino é um problema de comunicação entre generais, onde eles precisam se comunicar para atacar um castelo, mas tem um traidor no meio que pode enviar mensagens falsas. O objetivo é encontrar um protocolo de comunicação que permita aos generais chegarem a um consenso mesmo com a presença do traidor. O número mínimo de generais necessários para resolver o problema é 3f + 1, onde f é o número de traidores.

        #Considera-se que todos os processos "Honestos" (Sem falhas arbritárias) chegam na mesma decisão
        #Também que se o líder for honesto, os outros processos honestos vão concordar com ele

        #Ou seja, pode dar falso-positivo, o importante é todo mundo decidir a mesma coisa junto


        #Pritical Bizantine Fault tolerance
            #Falhas Arbritárias
            #Primario
            #Suporta mensagens peridas e fora de ordem
            #Necessitam assinatura, alguma criptografia assimétrica (Tipo curva eliptica)
            #3 Fases, ou seja é mais complexo


        #Teorema CAP
            #Tolerancia a parcionamento
            #Avalability
            #Consistencia

            #Das 3 apenas duas propriedades são aintgíveis






