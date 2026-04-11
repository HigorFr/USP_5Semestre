#Aula11

#Revisão básica
    #Linguagens relgulares, como visto, são casos particualres das livres de contexto.
    #Toda linguagem livre de contexto pode ser convertida para forma de chomsky


#=====================


#Certas propriedades da forma normal de chomsky

    #Só gera cadeia vazia se S0 -> ε
    #Se a gramatica gera cadeia unitária, ela é S0 -> a onde a é um terminal
    #derivação de de uma cadeia W sempe necessita de exatamente 2n-1 passos, pois ela fica no formato de árvore
    

#Tem como detemrinar se um GLC G na forma normal gera uma determianda cadeia W. Meio que um passo a passo
    #Ele recebe W e G, e faz varias substituições, e testas todas que possui 2n-1 passos. Se achar W, ele pertence. Caso contrario não

#========

#Como esse algortimo é ineficiente, existe uma maneira mais eficaz.
    #ALgoritimo ZYK (em homenagem a seus criadores, Ziv-Lempel, Cocke e Younger). É bem comum ser independente as pesquisas.
    #Ele é custo polinomial de tempo, que é melhor que NP completo
    #Programação dinamica, ou seja, diminui os problemas em pedaços mais simples


#Se faz uma matriz triangular (Aquela com só a diagonal e acima/baixo preenchida)
    #Cada coluna é o comprimento da subcadeia testada, e se testa as possíveis
    #A linha mais de baixo, só precisam respeita se ele é gerável com alguma regra, ou seja se tem um A -> a
    #Para as linhas de cima, elas devem ser formadas pela subcadeias que estão a esquerda eabaixo.
        #Então se na esquerda tem B, e abaixo tem A, deve-se procurar uma forma de gerar BA. (sempre da esquerda primeira, depois abaixo)
        #Se tiver mais coisas a esquerda ou abaixo, deve-se iterar uma por uma e testar se combina. De maneira a qual os pares de testes são sempre: o mais longe da esquerda com o perto de baixo. E vai aproximando.
        #Se duas regras geram o valor, ele deve ser colocado no memso quadrante, separado por virgula. Nesse caso, será iterado todas as combinações entre elas com sua respectiva outra celula.
    #A sequencia de preenchimento fica  na diagonal, preenchendo subindo a matriz.
    #No final, se S0 estiver na posição (1,n), ou seja, a primeira linha e a última coluna, então W pertence a linguagem gerada por G. Caso contrário, não pertence.
    #Exemplo no sldie.

    #As variaveis que temrinam em (1,n) significam "Se eu começar por essas, eu consigo formar a cadeia" Por isso S0 deve estar lá, porque é a variavel inicial.

#Analisando a compleixdade
    #Codigo no slides
    #No geral, a ideia é pegar a cadeia e fazer blocos subindo, de maneira que vai juntando-as de dois em dois.
    #Pode cair na prova


#Arvore sisntatica
    #Um subproduto de fazer esse algoritmo é uma arvore sintatica.
    #FAzendo uma busca em profundidade em algum ponto da matriz, é possível mapear de onde ela veio, ou seja, qual variaveis geraram ela, (usando um ponteiro mesmo).
    #Depois esses ponteiro quando explicitados, formam um caminho de ponteiros que funciona exatamente com uma árvore sintatica de gramatica
    #Isso deve ser feito durante o preenchimento da matriz, não é algo aplicado depois.
    #Ela pode ser ambigua, ou seja, ter mais de uma possibilidade. Então ele gera uma das árvores. (Que tem caracteristicas especificas, como dividir no máximo em 2).



#Em gramaticas regualres, dá para fazer a mesma coisa.
    #òbivo, pois gramaticas regulares são um caso particular das livres de contexto, então o algoritmo é aplicável.
    #Complexidade sempre O(mn).
    #para cada simbolo, se coloca os caminhos possíveis que ele levou. Quando terminar todos simbolos da cadeia, se tiver algum estdo final na coluna, então ele pertence a linguagem. Caso contrário, não pertence. Inclusive dá para mapear o caminho para chegar nela.
    #linear nesse caso. (inclusive nos sldies tem todas complexidades assintoticas)



