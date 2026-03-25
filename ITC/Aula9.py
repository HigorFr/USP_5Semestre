#Gramaticas Livre de Contexto hoje, e gramaticas circulares na sexta (Que não está no livro)
    #Material estará no slide

#Relembrando

#Gramatica livre de contexto é definido por 4 elemtnos
    #V é um conjunto finito denominado variaveis
    #Sigma é um conjunto, disjunto de V, denominado os terminais
    #R é o conjunto de regras, onde cada regra é uma produção do tipo A -> alpha, onde A é uma variavel e alpha é uma string de simbolos
    #Elemento Inicial


#Basicamente uma sequencia de substiuições que podem ser recursivas ou não. Tem varios possíveis resultados
    #Terminais normalmente são 01, ab ou #


# O simbolo | é "OU", ou seja, pode assumir ambos valores indeterminadamente

#Linguagens livre de contexto são gerada por essas regras. Essas linguagens utilizam expressões regulares
#Há mais de um cojunto de regras existente para realizar o mesmo conjunto.
    #Para fazer a linguagem L = {a}, a regra ś somente S -> a.
    #Para L = {a}* é S -> aS | epsilon   ou S -> Sa | epsilon
    #Para L = {a}*{b}* é S -> aS | bS | epsilon

#Da para encadear regras
    #L = {Cadeias que começam e terminam com A}
    #S -> aTa e S-> a   (Que vira S-> aTa | a)
    #T -> aTa | bTb | epsilon

#E dá para gerar expressões não regulares
    #L = {a^n b^n | n >= 0}
    # é descrito por S -> aSb | epsilon


#Dá para concatenar, quando se quebra a a expressão em duas partes
    #L = {a^n b^n c^m d^m | n >= 0, m >= 0}
    #Issé o mesmo que L1 concatena L2
    #L1 = {a^n b^n | n >= 0} e L2 = {c^m d^m | m >= 0}
    #L1 é descrito por S -> aSb | epsilon e L2 é descrito por S -> cSd | epsilon
    #Logo L é S -> S1 S2, S1 -> aS1b | epsilon e S2 -> cS2d | epsilon



#Para estrela, tem truques, 
    #Para L*    
    #S' -> SS' | epsilon  ,  para um S que descreve L.
    #S' é só uma variavel nova.

#Elas são um conjunto maior que as regulares, que são particulares dela.

#Com isso, a classes de linguagens geradas por gramaticas livres de contexto é fechada para união, concatenação e estrela de Kleene
    #L1 e L2 são livres de contexto, logo L1 U L2, L1 L2 e L1* são livres de contexto
    #Intersecção e complemento não são fechados, ou seja, L1 e L2 são livres de contexto, mas L1 interseção L2 e complemento de L1 podem não ser


#=================


#Ambiguidade

#É possível que a mesma gramatica gere a mesma cadeia de diferentes maneiras, ou seja, tenha mais de uma derivação para a mesma cadeia.
#Como vários caminhos, fica claro em uma arvore. (No slide)

#Derivação a esquerda é aquela onde a substituição é feita sempre na variavel mais a esquerda, e a derivação à direita é aquela onde a substituição é feita sempre na variavel mais a direita.
    #A gramatica S -> S + S | S * S | a é ambígua, pois a cadeia a + a * a tem mais de uma derivação à esquerda e mais de uma derivação à direita, ou seja, tem mais de uma arvore de derivação

#"Uma gramatica livre de contexto G é ambiguoa se existe cadeias w em L(G) que tem mais de uma derivação à esquerda ou mais de uma arvore de derivação. Caso contrário, G é não ambígua." ?


#Uma linguagem pode ser inerentemente ambígua, ou seja, toda gramatica que gera essa linguagem é ambígua. Exemplo: L = {a^n b^n c^m d^m | n >= 0, m >= 0} é inerentemente ambígua, pois tem mais de uma derivação para a cadeia a^n b^n c^m d^m.


#Exemplo de ambiguidade em linguagens de progrmação "If Else". If condition then statement1 if condition then statement2 else statement3. A cadeia "if condition then statement1 if condition then statement2 else statement3" tem mais de uma derivação, ou seja, tem mais de uma arvore de derivação, ou seja, é ambígua.
    #Para resolver, pode se associar o else ao ultimo if, colocar identação ou colocar endif


#Um problema de ocmputação é dizer se uma linguagen é ambígua ou não, e é um problema indecidível, ou seja, não existe um algoritmo que possa dizer se uma linguagem é ambígua ou não para todas as linguagens.


#============


#Forma normal de Chomsky, topico  importante.
    #Chomsky é um linguista, e ele criou uma forma normal para gramaticas livres de contexto, onde as regras são do tipo A -> BC ou A -> a, onde A, B e C são variaveis e a é um terminal. Essa forma normal é importante para algoritmos de análise sintática, como o algoritmo de CYK.

    #É uma maneira mais simples de se trabalhar com formas livres de contexto. Um "Padrão". Mas que no fim gera a mesma linguagem. Usado por matematicos para simplificar demosntrações
        #Por isso tem como transformar de GLC fora do FNC para dentro FNC, com as seguintes regras:


    #Regras
        #Toda regra é da fomra V-> W...X ou V-> a  
        #Variavel inicial S não pode aparecer no lado direito de nenhuma regra.
        #Somente variavel inicial pode ter regra S-> epsilon

    

    #Isso torna tudo mais previsível, mas as regras ficam maiores.

    #Teorema: Qualquer linguagem livre de contexto é gerada por uma gramatica de de contexto na forma normal de Chomsky. Ou seja, para toda gramatica livre de contexto G, existe uma gramatica G' na forma normal de Chomsky tal que L(G) = L(G').



    #Tem um passo a passo para demonstrar a aplicação. A prova do teorema é bascamente isso.

        #Quando se tem variavel terminal, precisa criar variavel para cada uma, e cada uma leva para a terminal unicamente.



#Propriedades
    #A gramatica G só é vazia se possui a regra S0 -> epislon (S0 é sempre a inicial)
    #A gramatica G gera uma cadeia unitária a se e somente se possui a regra S0 -> a
    #A derivaçao de w precisa exatamente 2n-1 etapas, onde n é o numero de terminais em w
