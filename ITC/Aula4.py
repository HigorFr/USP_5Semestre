#Aula4
    #Revisão raṕida da ultima aula
    
    #Definiçao muda pouco, principalmente que a saída da função de transição é um conjunto de estados possíveis
    #Abre-se uma árvore, alguns aceitam e alguns rejeitam, mas se algum aceitar já é suficente para aceita-lo
    #Diagrama -> #Cada andar da árvore é um simbolo lido de uma cadeia especifica.


#Programa Jflat cosnsegue simular todos os caminhos


#É possível existir laços infinitos em AFN válidos, isso pode acontecer com uma recursão de valores Epslon (Nulos)
#Não detemrinisticos são uteis para certas situações especiificar tipo "Idenficiar sequencias que o antepenultimo numero é 1"
    #Lembrando que se somente um caminho aceitar, a cadeia é aceita
    

#Diferença de não deterministico para deterministico
    #É possível converter, não anotei como, mas sempre tem uma maneira equivalente de se converter um AFN para um AFD
    #No geral eles são equivalentes na linguagem, AFD são mais eficientes em checaegem e simulação
    #AFN são mais fáceis de construir, AFD são mais fáceis de simular, util em versões probabilisticas
    #Provar isso é bem complexo, é construtivo e abstranto, mas será provado.



#Equivalencia sem epsilon
    #Cada caminho  possivel de um nó X vira um {x1,x2}, e o proximo {y1,y2}
    #Isso já é deterministico


#Equivalencia com epsilon
    #Junta a origem e o caminho a qual ele pode ir instantanemente, então se X1 pode recbeer 0 ou Epsilon para X2 ele vira {X1, X2}
    #Prova matemática não cai na prova
    #






