#Aula 7
#Consistencia e Replicação 

    #Replicação, algo benéfico
        #Seja para desempenho ou robustez
        #Desempenho pode ser no ponto de vista geográfico, ou seja, ter um recurso mais próximo do cliente, para reduzir a latência.
            #Também pode ser para escabilidade horizontal, literalmente aumentar a capacidade de hardware.
        
        #Robustez é mais ligado a tolerar falhas.

    #Consistencia, algo necessário
        #Se há mais de uma cópia de um recurso, é necessário garantir que elas sejam consistentes.
        #Há certos tipos de conflitos, como WW (Duas escritas) e WR (Ler dado desatualizado)


    #Consitência "Forte"
        #Operações atomicas e instantaneas, ou seja, quando uma operação é realizada, ela é imediatamente visível para todos os outros clientes.
        #Tem boas garantidas de como os dados serão tratados
            #Custosa
        
    #Consitência mais "Fraca"
        #Sem tanta consistência crtica, pode ser usado em lugares não críticos, ou seja, onde não há risco de falhas catastróficas. COmo comentarios de redes sociais.


    
#Modelos de Consistência
    #Duas Escolas basicamente, Contrato em Dados (Sendo Causal ou Sequencial) e o Modelo Centrado no Cliente
    #Elas vão especificar protocolos de funcionamento para suas operações



#Modelos de COnsitência Centrado em Dados
    #Datastore: Recurso com dado, seja um banco de dados, um sistema em arquivos ou memŕoai compartilhadada (Basciamente uma abstraao que engloba tudo, já que não faz diferença)
    #Certos processos farão processo de leitura ou escrita nesse datastore
    #Datastore pode ser composto por vários blocos de armazenamento conectados pela rede.


#Consistência Sequencial
    #Relativamente simples de implementar
    #É possível estabelece ruma ordme global de operações, ou seja, todos os nós do datasotre verão a mesma ordem de operações.
    #Da mesma forma ele tem que continuar respeitando a ordem local.
    #Notação:
        #Oi(X)v -> Operação O, realizada por um processo i (PID), no recurso X (nome do dado, variável), com valor v, que será lido ou escrito.
    #Não garante forte porque existe um delay de propagação (não especificado no modelo) entre os processos.
    #Ou seja, ele garante CONSISTENCIA SEQUENCIAL entre os processo, se ninguem escreveu mais nada, todos os leitores lerão sempre a mesma coisa independente quando rodaram. Mesmo que não seja o que ocorreu temporalmente.
    #Não há exclusão mútua, e da para ter condições de corrida se nada for implementado além disso.
    #Parto da premissa que o processo irá funcionar devidamente com o conteúdo recebido. Isto é, não é temporalemnte dependente.


    #Protocolos de Consistencia Sequencial
    #Baseado em Primário
        #Um pouco centalizado
        #Funciona escolhendo um servidor responsável por ordenar as operações de escrita
        #Quando um processo deseja realizar uma escrita, ele envia para o servidor original normalmente, que repassa para o primario. O primário repassa para todos os servidores a informação da escrita, e quando eles confirmam que receberam a informação, o primário responde para o original que e operação pode ocorrer.
        #Todas as bases ficam sicronizadas
        #Tem uma versão sem ser bloqueante, ou seja, o primario responde assim que recebe o dado do original. E ele que resolve os possíveis conflitos.
        #A operação fica lenta

    

    #Baseado em quorum
        #Quórum de Leiutra (Ne) e um Quórum de Escrita (Nw) e Versionamento de dados
        #Uma replica pode ser Nw e Ne ao mesmo tempo (Na verdade pelo menos uma)
        #A quantidade Ne + Nw > N (Numero total de réplicas) e Nw > N/2 (Quórum de escrita é maior que a metade das réplicas)
        #Quando um processo deseja realizar uma escrita, ele envia os Nw servidores.
        #Quando um processo deseja realizar uma leitura, ele envia para os Ne servidores, e espera receber a resposta de pelo menos Nw servidores, para garantir que ele leu a versão mais atualizada do dado.




#Consistência Causal
    #Operações casualmente dependentes devem acontecer na mesma ordem para todos os processos.
    #Ou seja, se um processo realiza uma operação O1, e depois realiza uma operação O2, e O2 depende de O1, então todos os processos devem ver O1 antes de ver O2.
    #Operações concorrentes podem aparecer fora de ordem.
    #Ou seja, se B e C dependem de A, ambos B e C podem aparecer em ordens diferentes para cada processo, mas ele garante que A será antes de ambos.
    #COnsidera-se que uma leitura desconsidera as anteriores


#Consitência Eventual
    #Na Ausência de operações de escrita, os dados em todas as réplicas eventualmente se tornarão consistentes. (Ficarão com mesmo valor)
    #Ela pode meio que ser combinada com os outros modelos
    #Casos com baixa de conflitos tipo WW, normalmente usada em sistemas onde se tem uma fonte de dados escritos, e que vão se propagando, ou seja, poucos W e muitos R
    #"Problema Monotônico"

#Modelos de Consistência Centrado no Cliente
    #Mobilidade, cliente acessa o sistema a partir de réplicas diferentes ao longo do tempo 
    #Ilusão do sistema consistente, independente da infraestrutura
    #Tem 4 modelos de leituras
    
    #Leituras Monotônicas: Se um cliente leu um valor, ele nunca lerá um valor mais antigo. (Não pode ler um valor mais antigo do que o que ele já leu)

    #Escritas Monotônicas: Se um cliente realizou uma escrita, ele nunca verá um valor mais antigo do que o que ele escreveu. (Não pode ler um valor mais antigo do que o que ele já escreveu)

    #Lera-suas-escritas: Se um cliente realizou uma escrita, ele sempre verá o valor que ele escreveu ou um valor mais recente. (Não pode ler um valor mais antigo do que o que ele já escreveu) (Ou seja, nesse caso que ELE escreveu obrigatoriamente)

    #Escritas-seguem-leituras: Se um cliente realizou uma leitura, e depois realizou uma escrita, a escrita deve ser visível para todos os clientes que leram o valor lido. (Se um cliente leu um valor, e depois escreveu um valor, esse valor escrito deve ser visível para todos os clientes que leram o valor lido)



#Connsistência Contínua
    #Pode ser em termos de Valor, Obsolecência ou ordem
    #Teŕa uma métrica de nível de consistência, que será aplicado a cada um desses aspectos
    
    #Valor - Valor não consistente    
    #Obsolecência - Tempo que leva para um valor se tornar consistente
    #Ordem - Numero maximo fora de ordem





    






