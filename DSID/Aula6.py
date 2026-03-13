#Noemação

    #Em Geral um nome vai se referir a algo de alto nível, como um arquivo, tela, conceito etc..
        #Esse nome irá ser uma tradução de algo local de baixo nível, como endereço, endereço de memória.



#Tradução
    #Nome p/endereço (como ip)
    #Esse endereço terá um ponto de acesso, que pode ser fixo ou único


#Nomeação
    #Plana, Estruturada, ou por atributos
    #Eles vão falar sobre a natureza dos nomes, como eles são formados, para cada um tera um processo de tradução diferente


#Noemação plana
    #Nomes não possuem estrutura
    #Também não possuem signifcado, ou seja ele é dessasociado do que o recurso é ou representa
    #Como por exemplo a saída de uma função de hash, que é basicamente um número aleatório.
    #Para traduzir tem algumas abordagens

    #Broadcast
        #Pergunta onde está o nome X para rede inteira, isso é custoso. Quem receber e tiver irá receber o IP
        #Análogo ao protocolo ARP, que precisa para associar o endereço MAC ao IP

    #Encaminhamento de Ponteiross
        #Mobilidade
        #Invés de refazer o broadcast, atualiza-se o caminho adicionando o novo caminho, permitindo que se olhe e trace as mudanças
        #Tradução vai seguir esses ponteiros

    #Esquema baseado em localização nativa
        #Mobilidade também
        #ponto de acesso fixo, o qual é a casa do recurso.
        #Essa casa terá um pontiero para a localização atual
        #Ou seja, invés de ter uma corrente para pegar um recurso, aqui é sempre 1. 
            #Mobile IP usa esse protoclo.

    #Tabela de Hash distribuida
        #O nome é uma cadeia de BITs aleatorios
        #Sobre essa cadeia, aplica-se uma tabela de hash distribuida, ex: CHORD
        #No cord tem pontos de acessos também são identificados por uma cadeia aleatoria com n BITS, como o proprio endereço IP
            #Cada ponto de acessso tem uma tabela com M entradas
            #E[i] = id + 2^î
            
                #Supondo m =4 bits e ID = 11
                #para o i =0, o prox será o 12, para o i=1 o prox será o 13, para i=2 o prox será 15, para o i = 3 o prox será 19, mas como é só 4 bits, o 19 vira 3

                #Cada requsição envia para o proximo, até chegar no final, perguntando sempre para o mais próximo. (O maior número que é menor ao que eu quero.)

            #Como nem todos nós vão exitir, os nomes deles (que existem) vão parasar para o nó seguinte.


    #Hierarquico
        #Forma hierarquica para traduzir nome plano
        #Tem-se um nó raiz, que conhece todos os nomes da rede. Ele terá ponteiros para os nós de níveis mais baixos, e esses nós terão ponteiros para os próximos níveis, e assim por diante, até chegar no nível mais baixo, que é o recurso.
        #Isso economiza tráfego.

    

#===========

#Noemação Estruturada
    #Nomes possuem uma estrutura, ou seja, eles são formados por partes, e cada parte tem um significado.
    #Exemplo: Nomes de arquivos, onde tem o nome do arquivo (Jutno do caminho) e a extensão
    #

    #DNS
        #FUnciona como hierarquia, mas os nomes tem significado.
        #Tem um servidor raiz que sabe traduzir qualquer tipo de nó, e vai enviando para as partes responsáveis. De frente para trás, já que o .br, .com são os mais altos níveis.
        #E parte do nome é usado para avançar nessa arvore, por isso é nomeação estruturda.
        #TAmbém pode ser separado em zonas para tratamento especifico pelo servidor.


    #Resoluçao de nomes pode ser Iterativa ou Recursvia
        #Iterativa: O cliente pergunta para o servidor raiz, ele responde com o próximo servidor, e o cliente pergunta para esse próximo servidor, e assim por diante, até chegar no servidor que tem a resposta. Isso é mais eficiente, pois o cliente tem controle sobre o processo, e pode parar quando quiser.
        #Recursiva: O cliente pergunta para o servidor raiz, ele responde com a resposta final, ou seja, ele faz todo o processo de tradução para o cliente. Isso é menos eficiente, pois o servidor raiz tem que fazer todo o trabalho, e pode ser sobrecarregado.


#Noemação por Atributos
    #Nomes são formados por atributos, ou seja, eles são formados por um conjunto de atributos, e cada atributo tem um valor. O nome é formado pela combinação desses atributos e seus valores.
    #Não terá "seuencia" de passo lineares, podem estar totalmente desordenados, como um conjunto    
    #Resolução pode ser feito por uma definição parcial dos atributos ou um intervalo

    #Pode haver um pouco de confusão em como os atributos são definidos, e isso pode levar a problemas de tradução, depende do domínio.



    #Resoluções

        #Pode ser hierarquico também, com uma ordem de hierarquia dos atrbutos, ou seja, algum atributo generico fica na raiz e vai se especificando nos nós abaixos por outros atributos.
        #Pode ter problemas, pois dependendo da especificação do atributo pode necessitar de valroes mais abertos, que necessita buscas por várias árvorés.
        #LDAP usa isso. 
        

        #Resolução através de índices
            #Um elemento que vai concentrar uma certa quantidade de nós.

            #Pode ser um servidor por atributo, onde o cliente pega uma lista por serfvidor, e dependnedo da compelxidade da demanda será necessário fazer uma uniao de várias requisições. Fora a assimetria de tamanho de conjuntos.
        
            #Pode se criar um espaço n dimensional onde n é a quandiade de atributos.
                #Cada região tem um nó responsável. Que pode ser diretamente identificado pela posição/valores dos atributos
                #Isso é melhor até para intervalos, mesmo que pode ser necessário pedir para amais de um servidor
            


        #Named Data Network (NDN)   
            #Invés de usar IP, utiliza o proprio nome para realizar roteamento de pacotes
            #Roteamento por Nomes, com cache na camada de redes
            
            #Roteador NDN funciona
                #Content Store, Cache de requisições
                #Pending, Armazena as requsições que estão sendo aguardadas
                #FWD INFO Base, uma tabela de roteamento baseada em nome.

                #A requsição depois de enviada volta, se tiver pending, ela continua para o anterior. 

                #aplicação nichada, dificilmente seria aplicável na internet.


        #Faltou 