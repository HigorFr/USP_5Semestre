
#Consistência, é basciamente a ideia de validar toda informação consolidada. Isso é uma escolha, adicionada em camadas, e requer mais processamento, custo.
#Há informações que não necessitam de consistência, e quanto mais confêrencias, dado em níveis, melhor o dado, mas mais lenta sua implementação.
#IA por exemplo, não tem consistência



#Durabilidade , nem todo dado precisa ser durável, alguns devem ser apagados.


#Arquivo de log 
    #Registra valor anteriores e novos, antes de mudar de fato "Irei mudar"
    #Registra o commit da ação de fato, tudo interligado por ID


#Usuário
    #Deve ser encapsulado, as coisas devem ser acessadas através dos aplicativos
    #Fronts Ends, chamadas para se consumir dados
    #Consultas Adhoc usando DML (AS mais sofisticadas)

    #Programadores desenham e implementam a aplicação que acessa o BD. Mundos distantes, que não devem ser preucupar

    #DBA é o administrador do banco de dados, responsável por manter o banco, otimizar, etc. 
    #Define e gerencia o esquema, define visões, monitora, Carrega e controla a base de dados



#SGBD são bons para
    #Dados estrutureados
    #Muito dados
    #Controle de concorrência
    #Backup, Segurança

#Não usar SGBD
    #Não é necessário muito usuário
    #Os dados são simples
    #Segurança, controle de concorrência e recuperação


#Terá trabalho provas e exercicios
    #Trabalho: Qualquer SGBD relacional e pode qualquer outro complementar
    #AVA: Ambiente virtual de aprendizagem. Local de trabalho será só na prox aula
    #Exercicios na aula