#Atributos


    #Limite de atributos, tem que analisar cada um se há ou não potencial daquilo ser usado
    #Isso depende do contexto.
        #Atributos multivalorados, aqueles iguais que podem ser mútiplos, como telefone.
        #Atributos compostos, aqueles que podem ser divididos, como endereço.
        #Identificadores, identifica unicamente
            #Alguns acreditam que não se pode usar valores com carga semânica como chave, pois pode sobrecarrega-la
            #Isso porquê se mudar, dá problema, tipo o proprio CPF, que está pra mudar.



    #Dependente
        #Atributos dependentes, aqueles que dependem de outros, como o valor do aluguel, que depende do valor do imóvel.

    #A chave composta também não é melhor das ideias, pois ela, conforme se propaga, ela aumenta de tamanho, tornando o sistema mais lento.
        #Normalmente se concatena as chaves, para virar uma.
        