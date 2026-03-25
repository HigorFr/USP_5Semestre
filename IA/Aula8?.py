#Esqueci o caderno. Essa aula é a pós K-mean



#Continuação do K-Means
    #Problema de minimização, você quer o menor valor de uma função.
    #Função de perda nesse caso, é Somatorio (para cada K) de um Somatorio(Para cada N amostra), de Uij * d(Ci, xj) ao quadrado
    #uij é a variável de decisão/indicadora (Meio que liga/desliga), que é 1 se a amostra xj pertence ao cluster i, e 0 caso contrário. Ela é uma matriz binária.
    #d(Ci, xj) é a distância entre o centroide Ci e a amostra xj
    #Ou seja, esse é o erro, ele movimenta o prototipo para agrupar os dados, e me diz a distancia geral.


#Medida de erro dependende de comparações, perda boa pode ser 1 ou 1000, depende do dominio.
    #Esse erro aprensentado é o mais puro, é chamado de erro de quantização, mas tem vários nomes

#No caso do K-means, existe um modelo perfeito sempre, mas nem sempre ele é alcançado e nós não sabemos qual é.


#=====


#Restrições
    #A soma de cada coluna i deve ser igual a 1, ou seja, cada amostra pertence a um cluster
        #É o mais proximo, naturalmente atendiad

    #A soma de cada coluna deve ser pelo menos 1, ou seja, cada cluster deve ter pelo menos uma amostra
        #Isso evita ele de ficar sem amostra e ficar preso, mas não garante
        #Tem maneiras mais sofisticadas, tipo escolhendo "Regiçoes de muitos dados"


#Antes de se inspecionar o modelo, é impossível definir de antemão o numero de clusters para qualquer problema.
    #Tem algumas heuristicas e estatisticas que são aplicadas para facilitar.
    #Não existe almoço grátis, não há solução definitiva que funcione para todas situações de análise.
        #Existe mecanismos de inspeção para chegar em uma boa solução



#Normalização de C. É simplesmente colocar I na posição calculada pela soma de cada distancia sua dividida pela soma de uij.





#+=================================================



#Rede neural

    #Uma rede neural é compsota por unidade menores.
    #Essas partes individualmente mimetizam o comportamento de um neurõnio biologio com operações básicas.

    #Biologicamente
        #Cada neurônio tem dendritos, que ficam responsável por uma sinal, e estimulada por algum impulso elétrico.
        #Esses sinais nos dendritos se tornam só um por um espaço químico, e se ele tiver potẼncia suficiência ele coloca para fora pelo axonio
            #isso é comportamento básico do cérebro humano, e é o que a rede neural tenta mimetizar.


    #A versão que será estudada é melhor que a básica, o Perception



