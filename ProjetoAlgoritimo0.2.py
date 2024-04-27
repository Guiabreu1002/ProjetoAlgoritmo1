#MENU DO PROJETO CINEMA
#tem q adicionar os caracteres de login em string ou da erro na hr do imput

ADM = {"guilherme1":"12345", "caze1":"12345"}

dicionario_login_normais = {}

lista_de_login = []

lista_de_filmes = ["aquaman" , "transformers"]
while True:


    #vms fazer um login normal e um login pra nos como ADM com as opções de poder sobre o programa
    print('escolha uma das opções abaixo')
    print('1:Fazer Login')
    print('2:Se Registrar')
    print('3:Entrar como visitante')
    print('4:Sair')
    op = int(input('digite a opção desejada'))
    if(op == 1):


        login = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")


        # parte dos login de ADM
        if login in ADM and ADM[login] == senha:
            print(f"seja bem-vindo ADM {login}")
            while op == 1:
                print('1:Listar filmes')
                print('2:Remover filme')
                print('3:Adicionar filme')
                print('4:Atualizar filme')
                print('5:Registar ADM')
                print('6:Gerenciar ingressos')
                print('7:Fazer loggout')

                op1 = int(input('oque quer fazer?'))
                if op1 == 1:
                    for i in range(len(lista_de_filmes)):
                        print(lista_de_filmes[i])
                elif (op1 == 7):
                    op = ""

            #login de usuarios normais
        elif login in dicionario_login_normais and dicionario_login_normais[login] == senha:
                while op == 2:
                    print("Login bem-sucedido!")
                    print('escolha uma das opções abaixo')
                    print('1:Fazer Login')
                    print('2:Se Registrar')
                    print('3:Entrar como visitante')
                    print('4:Sair')


        else:
            print("login ou senha errada tente novamente")
            tentar = input("gostaria de tentar novamente?")
            if tentar == 'não':
                op_1_break = 1


                #EU DEIXEI O CODIGO ESPAÇOSO SO PARA MELHOR TRABALHO



    elif(op == 2):
        #a maneira de login que eu to penssando é usando o email sabe, tipo, digite seu email
        #ai quando loga diz o nome do usuarios, aida to fazendo uns testes
        registrar = input("digite seu nome para registrar")
        email = input("digite seu email")
        senha = input("senha para sua conta")
        if registrar in dicionario_login_normais:
            print("nome ja registrado, tente novamente")
        else:
            dicionario_login_normais[email]= {registrar: senha}
            print("cadastro concluido com sucesso")


    #parte do modo visitante para poder ver sessões se estão cheia ou vagas, lista de filme e podemos colocar até preço
    elif(op == 3):
        print("Vc esta em modo visitante, não podera comprar nada, so olhar")
        while op == 3:
            print("1:Listar filmes")
            print("2:Ver as sessões")
            print("3:Help")
            print("4:sair")
            op3 = int(input("escolha uma das opções acima"))
            if op3 == 1:
                for i in range (len(lista_de_filmes)):
                    print(lista_de_filmes[i])