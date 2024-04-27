#MENU DO PROJETO CINEMA
#tem q adicionar os caracteres de login em string ou da erro na hr do imput

ADM = {"caze1@gmail.com":["caze1","12345"]}

dicionario_login_normais = {}

lista_de_login = []

tentar = ""

lista_de_filmes = ["Aquaman", "Transformers"]
while True:


    #vms fazer um login normal e um login pra nos como ADM com as opções de poder sobre o programa
    print('escolha uma das opções abaixo')
    print('1:Fazer Login')
    print('2:Se Registrar')
    print('3:Entrar como visitante')
    print('4:Sair')
    op = input('digite a opção desejada')


    if op != "1" and op != "2" and op != "3" and op != "4":
        print("caracteres invalidos, tente novamente""\n")


    if(op == "1"):
        while op == "1":
            email = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")
            if email in ADM and ADM[email][1] != senha:
                print("email ou senha errada, tente novamente ou aperte S para sair")
            # parte dos login de ADM
            if email in ADM and ADM[email][1] == senha:
                print(f"seja bem-vindo ADM {ADM[email][0]}")
                while op == "1":
                    print('1:Listar filmes')
                    print('2:Remover filme')
                    print('3:Adicionar filme')
                    print('4:Atualizar filme')
                    print('5:Registar ADM')
                    print('6:Gerenciar ingressos')
                    print('7:Fazer logout')

                    op1 = int(input('O que deseja fazer?'))
                    if op1 == 1:
                        for i in range(len(lista_de_filmes)):
                            print(lista_de_filmes[i])
                    elif op1 == 2:
                        for x in range(len(lista_de_filmes)):
                            print(lista_de_filmes[x])
                        filme_para_remover = input('Digite o filme q queira remover: ')
                        lista_de_filmes.remove(filme_para_remover)
                        print("filme removido com sucesso")
                        print("Nova lista:")
                        for a in range(len(lista_de_filmes)):
                            print(f"{lista_de_filmes[a]}")



                    elif op1 == 3:
                        filme_para_adicionar = input('Digite um filme para adicionar: ')
                        lista_de_filmes.append(filme_para_adicionar)
                        print("filme adicionado com sucesso")
                        print("Nova lista:")
                        for g in range(len(lista_de_filmes)):
                            print(f"{lista_de_filmes[g]}")


                    elif op1 == 4:
                        filme_para_atualizar = input('Digite um filme para atualizar: ')
                    elif op1 == 5:
                        registrar_adm = input("digite seu nome para registrar")
                        email = input("digite seu email")
                        senha = input("senha para sua conta")
                        if registrar_adm in ADM:
                            print("nome ja registrado, tente novamente")
                        else:
                            ADM[email] = [registrar_adm, senha]
                            print("cadastro concluido com sucesso")
                            print(ADM)

                    elif op1 == 6:
                        print("a")


                    elif op1 == 7:
                        op = ""

                #login de usuarios normais
            elif email in dicionario_login_normais and dicionario_login_normais[email][1] == senha:
                    while op == 1:
                        print("Login bem-sucedido!")
                        print('escolha uma das opções abaixo')
                        print('1:Fazer Login')
                        print('2:Se Registrar')
                        print('3:Entrar como visitante')
                        print('4:Sair')


            else:
                print("login ou senha errada tente novamente")
                denovo = input("gostaria de tentar novamente?")
                if denovo == 'não':
                    op = ""


                #EU DEIXEI O CODIGO ESPAÇOSO SO PARA MELHOR TRABALHO



    elif(op == "2"):
        #a maneira de login que eu to penssando é usando o email sabe, tipo, digite seu email
        #ai quando loga diz o nome do usuarios, aida to fazendo uns testes
        while op == "2":
            registrar = input("digite seu nome para registrar")
            email = input("digite seu email")
            senha = input("senha para sua conta")
            if registrar in dicionario_login_normais:
                print("nome ja registrado, tente novamente")
            else:
                dicionario_login_normais[email] = [registrar, senha]
                print("cadastro concluido com sucesso")
                print(dicionario_login_normais)
                op = ""


    #parte do modo visitante para poder ver sessões se estão cheia ou vagas, lista de filme e podemos colocar até preço
    elif(op == "3"):
        print("Vc esta em modo visitante, não podera comprar nada, so olhar")
        while op == "3":
            print("1:Listar filmes")
            print("2:Ver as sessões")
            print("3:Help")
            print("4:sair")
            op3 = int(input("escolha uma das opções acima"))
            if op3 == 1:
                for i in range (len(lista_de_filmes)):
                    print(lista_de_filmes[i])
