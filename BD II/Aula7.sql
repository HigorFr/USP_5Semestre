#Discussão de paralelos, estar sempre no limiar
    #todo modelo é útil para desenolver determinado racicínio


#Dado serve para usar, ou seja, exige, consultar, editar remover etc...
    #Tudo isso exige eficiência



    #Algumas práticas
        #Evitar junções, pois tem alto custo computacional
        #Ter pouco numero de chaves
        #Evitar campos adicionais. Campos podem assumir NULL. Fazer verificação
        #Nome para campos chaves precisam ser bem definidos. Noraml,mente coloca-se o nome da tabela Junto
            #Ex CodEmp invés de só Cod para Empregado.
        #Utilizar atributos na relação para evitar redundancia e maneira como as interações acontecem
            #Normalmente sempre tem um atriuto de relação no contexto de "Muitos -> Um"
            
        #A chave sempre vai de um lado por outro, ou uma nova tabela é criada.
            #1:1 só se pode Fundir tabela ou Migrar a Chave
            #1:N só se Migra a chave
            #N:N só se cria uma nova tabela. (Acho que da relação)


        #Relações com maiores que 2
            #É comum fazer essa tabela a qual se relaciona virar uma entidade propria para se relacionar com as outras
            #Isso torna mais chavaes compostas e melhora tempo de indexação
        

        