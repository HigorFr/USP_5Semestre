#Aula 14 e 15 perdidas, dado no sábado.
#Aula 16 em algum lugar.


#Em teoria é para essa terceira ser menos corrido que a segunda prova.
#Proxima aula tem uma demonstração principal.



#Revisão
    #Descriçãos menos formais de linguagens.
        #Invés de implementar diretamente, mais fácil descrever a implementação, que é o mais alto nível
        #Também a descrição de linguagens em alto nível, com expressões e mais específicos
        #E a implementação formal, que é o diagrama em sí.

    #Abre e fecha aspas, para descrição com passo a passo. Ex M2 = "1- Faça X, 2 - Faça Y etc..."

    #Linguagem reconhecível é se existe alguma máquina de turing que reconheça a linguagem.
        #Subconjunto de turing decisíveis, que é a qual rejeita ou aceita sempre. (Entrada finita)
        #Não há como saber se uma máquina entrará em loop para uma linguagem, ou se ela está em loop.

#Motivar quis problemas podem ser resolvdos.    
#Certos problemas não podem ser resolvidos por computadores, sem alguma aproximação ou abordagem diferente.
    
#Irá se considerar que uma llinguagem é decidível se o problema da parada é decidível por alguma codificação.
#Esse tipo de demonstração irá cair na prova, seja problemas que usam o teorema ou o teroema em sí.

#Provas e demonstrações
    #Para certezas provas utiliza-se máquinas anteriores para auxiliar na prova, tipo no teorema 4.2 que utiliza de 4.1.
        #Nesse teorema, utiliza-se o resultado anterior para facilitar, mas poderia ser simulado diretamente o não deterministico, sem usar o 4.1
        #Também concluise que o 4.2 é decisivo.
    #O Mesmo vale para o teorema *.*, que faça sobre Agr (gramaticas regulares)

    #Cerca de 80% da prova vai ser algo relacionado a isso, fazer demonstraçõs utilizando a demonstração anterior para ir construindo o teorema

#Simbolo <A> é a "Codificação", de A, ou seja, A inserido na máquina de turning de maneira que ele entenda.

#Teorema 4.4, só aceita a cadeia se a codificação a qual ele fala for de uma linguagem AFD que não aceita nada.
    #Basicamente faz uma busca em largura com vertice direcionado até achar um estado de aceitarção, se achar rejeita, se não, aceita.


#4.5
    #Utiiliza operações fechadads para lingaugens regulares para fazer manipulação de conjunto.
    #Faz o XOR e confere se dá um valor vazio ou não.



#4.7
    #Faz chomsky, confere se 2n-1 da certo.


#4.8
    #Marque terminais G, repita o seguinte:  toda regra A -> U, marque A, sendo U algum G ou variavel marcada. Repita até não marcar mais nada. Se S estiver marcado, então L(G) != vazio.
    #Logo se a variável inicial não aparecer marcada aceite, se aparecer rejeite.

#4.9
    #Basta usar a gramática
    

#Esses teoremas provam que tudo abaixo de livre de contexto são decidíveis.


#Tem uma que não é decidível que é a máquina que confere se duas GLC são equivalentes ou não. Isso exigiria complemento e intersecção, que não são fechadas para GLC. Logo não é decidível. Nem por outros métodos tem como provar que é.


#===========

#Essa parte será aprofundada posteriormente.
#Uso de mátemática discreta para provar que certos problemas não são decidíveis.

#Cantor
    #Uso da bijeção para provar que certos conjuntos são infiitos diferentes de outros.
    #Numerável = Contável = Mesma cardinalidade que N. Racionais são assim.


    #Diagonalização prova que reais e irracionais não possuem uma bijeção, logo são infinitos diferentes
    

    #23 Problemas de Hilbert. ICM vai rolar inclusive daqui 2 semanas de quando estou estudando isso. (Hj é 08/07/2026)






#Prox aula continua





























