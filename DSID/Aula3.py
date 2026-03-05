#Aula 3

#Processos
    #Programa em execução
    #Instruções, E/S e Memória (Contexto), visto em SO

#Virtualização de Recursos (Memória Simulada por exemplo)
    #Troca de contexto, feito pelo escalonador
    

#Thread
    #Unidade escalonável do processo (Uma parte dele que pode rodar independnete)
    #Obiviamente um processos vão ter ao menos uma thread principal
    #+Desempenho com paralelismo
    #Organização do código (QUando roda o que) (E/S)

    #Caracteristicas
        #Organização de hardware mais complexa
        #Memoria compartilhada entre threads do mesmo processo (Mais fácil organizar endereçamento)
            #Diferentes maneiras de comunicação entre procesos (Pipes etc...)

#============

#Virtualização de Interfaces
    #Em máquinas sem virtualização de interfaces o funcionamento é
    #CPU dá um conjunto de instruções privilegiadas (Do modo Kernel) e um conjunto geral.
    #SO faz uso de instruções privilegiadas e algumas gerais.
    #Bibliotecas usam instruções gerais, e essas bibliotecas farão também chamadas ao sistema (Para o SO), que ele não pode fazer diretamente
    #Acima das biblitoecas tem as aplicações, que fazem chamadas às bibliotecas através de APIs. E também usam funções gerais da CPU.
    
#Virtualização é você fazer com que o software tenha a impressão de que tem acesso direto a uma dessas interfaces que na verdade não existe.

#Virtualização de processos
    #Invés de bibliotecas providas pelo SO, terá um ambiente de execução "RUNTIME", onde será independete do sistema operacional.
    #Isso é util para a aplicação ter a mesma interface sempre, o que facilita seu uso em qualquer lugar
    #Máquina virtual java (JVM) é assim
    #Python usa para inpretar (Isto é, enviar o código em tempo de execução)
    #Wine usa isso também para sua virtuzalização de interfaces, para rodar programas do Windows em Linux, ele virtualiza a interface do Windows, e traduz as chamadas para o Linux.


#Virtualização de bibliotecas (Conainers)
    #Mesmo nível de virtualização, mas uso diferente
    #Um aplicativo irá executar acima de um container, e não biblioteca, que abaixo dele terá o SO
    #A ideia é que não tenha dependência de versões, ou seja, o container terá toda coleção de requisitos para que seu programa funcione, uma fatia de sistema de arquivo disponível para a aplicação
    #Docker é um exemplo de container, onde você pode criar uma imagem com todas as dependências necessárias para sua aplicação, e depois rodar essa imagem em qualquer lugar, sem se preocupar com o ambiente de execução. Suas propriedades de isolamento são muito fortes
        #Namespaces, cada container tem seu próprio namespace, ou seja, seu próprio sistema de arquivos
        #Sistema de arquivo isolado
        #Gerenciamento de recursos



#Máquinas Virtuais
#Vários Modelos diferentes
#Note que no boot, o VMM é considerado o SO hospedeiro pela bios, e o SO é escalonado como um processo posteriormente

    #1
    #Virtual Machine monitor, uma camada de software que fica antes do hardware, que o virtualiza, ou seja, o sistema operacional tem a impressão de que tem acesso direto ao hardware, mas na verdade ele está acessando uma máquina virtual que é gerenciada pelo monitor. 
    #O monitor é responsável por gerenciar os recursos do hardware e alocar esses recursos para as máquinas virtuais.
    #Absolutamente todas requisições passam por ela nesse caso

    #2 
    #Tem um outro modelo o qual a VMM é uma camada só entre o SO e o Hardware, e virtualiza só algumas instruções, mas certos aplicativos conseguem enviar informações diretamente para o Hardware

    #3
    #E ainda tem outros, que funcionam como uma camada entre um SO hospedeiro e um SO colocado posteiromente (Host e Guest), e realiza a tradução da comunicação.


#Entre Conteiner e VM tem algumas diferenças
    #Container no geral é mais fácil de usar, e mais scriptável (Atuomatizável)
    #Outro ponto é desempenho, seja de memória, disco ou CPU, que também o container tende a ser melhor
    #VM é um pouco mais flexível entretanto, mais fácil fazer migração e também tem mais isolamento





#Virtualização e Cloud Computing
    #Saas - Software as a Service, Google drive da vida, serviço pronto, virtual na nuvem
    #Paas - Platform as a Service, Análogo a um container, sem muita config de ambiente, ele já está pronto.
    #Tem o funcion as a service também, onde se paga só pelo uso da função
    #Iaas - Infrastructure as a Service, Analógo a VM, uma máquina inteira remota, com acesso e customização livre

    #Tem algumas vantagens, como elasticidade e alocação de recursos



#Migração de Código
    #Migrar dados é o mais comum, transfere-se informação de uma máquina para outra
    #Nesse caso é mover uma unidade de execução, um processo/thread, uma VM inteira, ou até um container
    #Essa movimentação é útil por questões de:
        #Desempenho (Velocidade/Vazão), 
        #Realizar balancemento de máquinas sobrecarregadas, 
        #Economizar energia (Que nesse caso é juntar vários). 
        #Uso de banda também é um fato
        #Privacidade, ou seja, migrar para uma máquina com especificações seguras específicas e depois voltar com resultado.
        #Flebilidade de onde rodar o código (Meio que o javascript)


#Migração Forte vs Fraca
    #Fraca é quando não transporta contexto de execução (Ele roda do zero)
    #Forte é quando até o contexto da execução também é transportaddo, dificíl implemtnar na pratica porque preceisa ter compatibildiade do ambiente. Por isso migrar a máquina virtual é mais comum
    #Diferente de replicação, muito comum, onde duas VM clones rodam e podem assumir o controle dos programas caso uma caia



