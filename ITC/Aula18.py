#COntinuação


#R é um conjunto incontável
    #Não há bijeção entre N e R, logo R é incontável. Prova da diagonalização de Cantor.
    #Cria se um mnumero pertencente ao R, o qual possui valores que são diferentes para cada digito N na diagonal
    #Então é um numero com digito 1 diferente do digito 1 do primeiro, do digito 2 diferente do digito 2 do segundo, e assim por diante.
    #Ese numero nunca vai aparecer na tabela, pois ele sempre é diferente de todos os outros, então há uma contradição em quando ele acontecer.
    #logo está provando que R é incontável.




#O conjunto de todas máquinas de turing são contáveis. Mas o conjunto de linguagens é incontável. Logo, existem linguagens que não são reconhecíveis por máquinas de turing. Logo, existem linguagens que não são decidíveis.
    #Isso dado que uma MT só reconhece uma linguagem (O Conjunto de aceite de aceite é uma Linguagem)


#Isso porque o alfabeto é um conjunto contável, isso pode ser codificado (<M>). A maquina codificada pode ser escrito como uma cadeia, e ela irá pertencenter a (sigma)*, que é uma cadeia de algum alfabeto finito. Descartando as cadeias ilegítimas, pode-se listar toas as cadeias que representam todas as MTs. Logo o Conjunto de todas MTs é contável.


#A diagonalização pode provar que o conjunto de todas linguagens não é contável.
    #Para o subconjunto qualquer dela, cria-se uma linha binarinaria indicando se a cadeia pertence ou não a linguagem. 
    #Isso cria uma função bijetora.
    #Diagonaliza-se então essa sequencia binária, que não estará na lista.

    #Isso prova que há linguagens não reconhecíveis por nenhuma MT.
        #Ou seja, se tratamos problemas como linguagens reconheciveis, então há problemas que não podem ser resolvidos por nenhuma matemática.
        #Caso acreditemos que as maquinas de turing são intrinsicamente ligadas a algotimimos.



#------------


#Outra questão, uma MT pode reconhecer o problema de "Recebendo uma cadeia e uma máquina, saber se ela vair aceitar"
    #Isso é a Amt, a maquina de turing universal, que é uma MT que simula qualquer outra MT. Ela é reconhecível, mas não é decidível, pois ele pode entrar em loop durante a execução de simular a entrada.
    #Verificar o funcionamento de um software é insolúvel. Ele pode até aceitar ou negar para alguns, mas não é universal pois ele pode rodar eternamente para alguns.
        #Algumas IAs refinam isso, mas na pratica é impossível.


    #Para provar que é indecidível, existe métodos:
        #Um método é contradição. Crie uma máquina H que recebe uma codificação de uma máquina M e uma cadeia w, e ela aceita se M aceita w, e rejeita se M rejeita w.
        #Cria-se uma máquina D que faz o oposto,ou seja, de H aceita D reijeta, e de H rejeita D aceita. 
        #Então, se D recebe a codificação de D com <M>, ela irá aceitar se D rejeita, e rejeitar se D aceita. Logo, há uma contradição, pois D não pode aceitar nem rejeitar a si mesma.
            #Logo H não existe, Amt não decide.

        #Tem como provar por diagonalização.

    #Demonstrações não são cobradas, só o resultado dos teoremas.


#-----------


#Uma linguagem é co-turing reconhecível se existe uma MT que reconhece a linguagem complementar. Ou seja, se L é co-turing reconhecível, então existe uma MT que reconhece L', o complemento de L.
#?????
#Uma linguagem é indecivel quando ela "não é reconhecivel ou co-reconhecivel". Ou seja, não existe uma MT que reconheça L nem L'.


#O Complemento de Amt portanto não é reconhecível

#---------------------


#Prova terá varias demonstrações por reduções, aulas futuras




