# MENU DO PROJETO CINEMA
# tem q adicionar os caracteres de login em string ou da erro na hr do imput

ADM = {"c": ["caze1", "1"], "guilherme1@gmail.com":["guilherme1","12345"]}

dicionario_login_normais = {}

tentar = ""
#nessa parte aqui a gente podeira fazer algo tipo um cartão de credito para poder add a "grana" dos usuarios para comprar os ingressos
creditos = []
#aqui to vendo pra usar dessa maneira, o filme é a chave
#o indice 0 é a sala, o 1 o horario, 2 o valor é so um teste, se quiser implementar
dicionario_filmes = [{"Aquaman":[1,"16:30","15"]}]

lista_de_filmes = ["Aquaman"]
while True:
    print('Escolha uma das opções abaixo:\n')
    print('1: Fazer Login')
    print('2: Se Registrar')
    print('3: Entrar como visitante')
    print('4: Sair')
    op = input('\nDigite a opção desejada: ')

    if op != "1" and op != "2" and op != "3" and op != "4":
        print("\n""Caracteres invalidos, tente novamente""\n")

    if (op == "1"):
        while op == "1":
            email = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")
            # parte dos login de ADM funcionando perfeitamente
            if email in ADM and ADM[email][1] == senha:
                print(f"\nseja bem-vindo ADM {ADM[email][0]}""\n")
                while op == "1":
                    print('1: Listar filmes')
                    print('2: Remover filme')
                    print('3: Adicionar filme')
                    print('4: Atualizar filme')
                    print('5: Registar ADM')
                    print('6: Gerenciar ingressos')
                    print('7: Fazer logout')
                    op1 = (input('O que deseja fazer?'))
                    if op1 == "1":


                        #listar filmes
                        while op1 == "1":
                            for i in range(len(lista_de_filmes)):
                                print(lista_de_filmes[i])
                            print("1:voltar para o menu")
                            print("2:rever a lista")
                            quer_continuar = input("escolha uma das opções")
                            if quer_continuar == "1":
                                    op1 = ""
                            #aqui tava tentando fazer um menu mais arrumado pra nn ficar repetindo sempre
                            #todas as 7 opções, da pra fazer nos outros tbm pra deixar mais arrumado e com criatividade



                    #remoção de filmes com dicinonario, no momento estamos usando 2 listas, uma com dicionario e outra so lista msm
                    elif op1 == "2":
                        for x in range(len(lista_de_filmes)):
                            print(lista_de_filmes[x])
                        filme_para_remover = input('Digite o filme q queira remover: ')
                        lista_de_filmes.remove(filme_para_remover)
                        dicionario_filmes.remove(filme_para_remover)
                        print("filme removido com sucesso")
                        print("Nova lista:")
                        for a in range(len(lista_de_filmes)):
                            print(f"{lista_de_filmes[a]}")
                            print(dicionario_filmes)




                    #adicionar filmes no dicionario, a msm coisa do exemplo acima, temos q ver como fazer
                    #pq com dicionario é mais facil, mais temos q saber como usar lista
                    elif op1 == "3":
                        filme_para_adicionar = input('Digite um filme para adicionar: ')
                        sala_redirecionar = input('para qual sala esse filme vai?')
                        horario = input('a que horas esse filme passara?')
                        ingresso = input("qual sera o valor do ingresso?")
                        lista_de_filmes.append(filme_para_adicionar)
                        dicionario_filmes[filme_para_adicionar] = [sala_redirecionar,horario,ingresso]
                        print("filme adicionado com sucesso")
                        print("Nova lista:")
                        for g in range(len(lista_de_filmes)):
                            print(f"{lista_de_filmes[g]}")
                            print(dicionario_filmes)




                    #atualizar filmes tbm com dicionario, creio q estão funcionando, é so remover os [] da dicionario filmes
                    elif op1 == "4":
                        for z in range(len(lista_de_filmes)):
                            print(f"{lista_de_filmes[z]}")
                        chaveantiga = input("qual filme gostaria de atulizar?")
                        novo = input("Digite o novo filme")
                        dicionario_filmes[novo] = dicionario_filmes.pop(chaveantiga)
                        print("filme atualizado com sucesso")
                        for c in lista_de_filmes:
                            print(c)




                    #registrar um ADM essa parte esta certa e funcionando
                    elif op1 == "5":
                        registrar_adm = input("digite seu nome para registrar")
                        email = input("digite seu email")
                        senha = input("senha para sua conta")
                        if email in ADM:
                            print("email ja existe, tente novamente")
                        else:
                            ADM[email] = [registrar_adm, senha]
                            print("cadastro concluido com sucesso")
                            print(ADM)
                    # aqui ainda nn foi programado
                    elif op1 == "6":
                        print("a")


                    elif op1 == "7":
                        op = ""

                # login de usuarios normais funcionando normal, so tem q fazer dps o submenu deles
            elif email in dicionario_login_normais and dicionario_login_normais[email][1] == senha:
                while op == "1":
                    print("Login bem-sucedido!")
                    print(f"bem vindo usuario {dicionario_login_normais[email][0]}")
                    print('1: Fazer Login')
                    print('2: Se Registrar')
                    print('3: Entrar como visitante')
                    print('4: Sair')
                    print('Escolha uma das opções abaixo: ')


            else:
                print("login ou senha errada")
                denovo = input("gostaria de tentar novamente?")
                if denovo == 'não':
                    op = ""

                # EU DEIXEI O CODIGO ESPAÇOSO SO PARA MELHOR TRABALHO



    elif (op == "2"):
        #registro de usuarios esta funcionando perfeitamente
        while op == "2":
            registrar = input("Digite seu nome para registrar: ")
            email = input("Digite seu email: ")
            senha = input("Crie uma senha para sua conta: ")
            if registrar in dicionario_login_normais:
                print("Nome já registrado, tente novamente.")
            else:
                dicionario_login_normais[email] = [registrar, senha]
                print("Cadastro concluido com sucesso.")
                print(dicionario_login_normais)
                op = ""


    #parte dos visitantes esta basicamente pronta, so dar um acabamento dps
    elif (op == "3"):
        print("\nVc esta em modo visitante, não poderá comprar nada, so olhar\n")
        while op == "3":
            print("1: Listar filmes")
            print("2: Ver as sessões")
            print("3: Ajuda")
            print("4: Sair")
            op3 = (input("Escolha uma das opções acima: "))
            if op3 != "1" and op != "2" and op != "3" and op != "4":
                print("caracteres invalidos, tente novamente")
            if op3 == "1":
                print('Aqui estão os filmes em cartaz:\n')
                for i in range(len(lista_de_filmes)):
                    print(f'{lista_de_filmes[i]}\n')
            if op3 == "2":
                print('\nAqui estão as sessões disponiveis:\n')
                for sessao in sessoes:
                    print(f'{sessao}\n')
            if op3 == "3":
                print('Para assistir os filmes e comprar ingressos, você precisará se registrar no nosso cinema.')
            if op3 == "4":
                op = ""
    elif(op == "4"):
        break