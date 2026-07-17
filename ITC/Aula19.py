#Provas por redução



#A é redutível em B, se A pode ser resolvido com um algoritimo que resolve B.
    #Serve para provar por contradição certos teoremas. Se A cria um B decisor que seria impossível, então A ser decidível está errado.




#Problema da parada -> Uma maquina "Para" que recebe uma MT e uma entrada codificada e ela me diz se a MT para ou não para com aquela entrada.
    #Se ela for decidível (Se de fato existir uma MT que decide ela), podemos criar uma MT que resolve o problema Amt, que sabemos que é indecídível, logo a hipotesé está errada por ter gerado uma contradição.
    #Logo por redução "Para", é indecídivel.

    #Prova:
        #Usando essa máquina, criamos outra que usa ela:
        #Rodamos o Para <M,W>, se ela reijar, reijeita
        #Se aceita, simula M sobre w até que pare (pois ela para)
        #Se essa maquina no final aceitou, aceite, se não rejeite

        #Isso é uma Amt, mas ela não é pra existir, contradição.

#Na p3, os teoremas são fatos, a demonstração precisa ser feita, passo a passo.


#Para ver se é vazio, Vmt é mais complexo
    #criamos uma máquina de apoio, que recebe um X instrinseco nele e o M e W da maquina global
    #se for igual X = W ele vai simplesmente rodar W em M e aceitar se aceitar e negar se nega.
    #se for diferente, ele rejeita.
    #logo ele só aceita a Linguagem de M, mas com a entrada W, que é o que queremos.

    #Se eu jogar isso no Vmt ele vai me dizer se a maquina aceita só nulo ou não. Mas isso é exatamente me dizer se a linaugem de M aceita W ou não. O que decide Amt



#para checar se duas são iguais EQ, basta travar uma linguagem como nulo, isso vai decidir Vmt, que é indecídivel.


#para chechar se é regular, REGULAR é a mesma técnica do Vmt.
    #crio a máquina auxiliar que recebe uma cadeia X, um M e um W, ela tem duas opções
        #Se x for da forma 0^n1^n, ou seja, se ele não for regular, ele sempre aceita.
        #Caso contrario, eu rodo a maquina M3 com a entrada W, se ela aceitar, eu aceito.



    #Eu posso rodar essa máquina no REGULAR, e ela vai me me decidir Amt, pois dependendo de X:
    #  1 - Se ele não for regular (0^n1^n), ele aceita tudo, logo a linguagem é Tudo
    #  2-  Se for regular, ele coloca o W na M e aceita se aceitar e nega se negar., logo a linguagem é só M

    #Ou seja, se REGULAR falar que é regular, significa que a máquina M aceita W, e se REGULAR falar que não é regular, significa que a máquina M não aceita W. Logo, REGULAR decide Amt, o que é impossível, logo REGULAR é indecível.

    


#----------------------

#Lema 5,8
    #ALL é uma MT que tem uma fita limitada, e bate na parede caso tente escrever mais do que a fita permite
    #Ele tem no máximo qng^n configurações, logo ele é finito, Estados * Comprimento N * e G^n cadeias possíveis, com G sendo o alfabeto.
    #


#5.9
#ALL limitado passa a ser decisível, pois sabemos quando ele começa a repetir, caso ele repita a configuração passando do numero máximo G^n*N, logo detectamos loop.



#---------------------


#Formalização de redução usando mapeamento
    #Se a é redutivel por mapemento a B (A <=m B)
        #O elemento w que paetecece a A é mapeado para um elemento f(w) que pertence a B
        #Ou seja, existe um f que pega a entrada de A e transforma em uma entrada de B, tal que ambas são aceites.
        #f fica denomianada redução A para B


#SE A <=m B, e B é decidível, então A é decidível.
#Da mesma forma se A <=m B, e A é indecível, então B é indecível.

#Ou seja, fizemos anteriormente vários M que deciadm um A que já sabemos ser indecídivel, e com isso provamos que B é indecível também por contradição.
    #Esse processo era basicamente uma função de mapeamneto?



#IMCOMPLETO BATERIA ACABANDO