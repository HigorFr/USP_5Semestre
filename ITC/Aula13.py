


#Aula 13, Lema do bombeamento para GLC


#Funciona muito semelhante, estárá na prova, mas a demonstração não será cobrada.

#Demonstração consiste basicamente em observar a árvore de derivação.
    #Duas variaveis devem se repetir desde a raíz até as folhas.
    #COmo elas se repetem, é possível repetir a derivação até chegar nela novamente.
    #Dessa forma, é possivel dividir a saída em 5 partes, UVXYZ, já que VY repetem
    #Posso bombear o VY então para cima/baixo que deve ser possível.


#Invés de provar uma linguagem xyîz, prova-se que uma YViXYiZ com VY maior que zero não pertence a linguagem.
    #Cadeia suficientemente grande P, e que satisfaça isso. Normalmente é muito grande, nesse caso, mas só mantemos a variável
    #Um deles pode ser vazio, mas não ambos, pois se ambos forem vazios, não há bombeamento.
    #Também tem um S que é qualquer cadeia da linguagem
    #VY <= P
    #Note que o bombeamento para VY é simultaneamente, mesmo íncice.

    #Tem como definir o P como sendo b^(|v|+1), logo a altura minima é |v|+1, numero de variaveis. 
    #Escolhe o R, que  de modo que ambas as ocorrências fiquem dentre as |v|+1 variáveis inferiores no caminho, e escolh-se o caminhos mais longo da arvoré sintática.
    #Logo eu garanto que uma variável vai se repetir pois a altura é maior que o número de variáveis, e isso permite o bombeabmento.

    #Provavaelmente vai cair.



#





