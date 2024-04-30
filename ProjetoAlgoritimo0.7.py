# MENU DO PROJETO CINEMA
# tem q adicionar os caracteres de login em string ou da erro na hr do imput
ADM = {"c": ["caze1", "1"], "guilherme1@gmail.com":["guilherme1","12345"]}
dicionario_login_normais = {"normal":["usuario","1"]}
tentar = ""
#nessa parte aqui a gente podeira fazer algo tipo um cartão de credito para poder add a "grana" dos usuarios para comprar os ingressos
dicionario_creditos = {}
#aqui to vendo pra usar dessa maneira, o filme é a chave
#o indice 0 é a sala, o 1 o horario, 2 o valor é so um teste, se quiser implementar
dicionario_sessao = {"A": ["Aquaman", "transformers"],"B":["Kung Fu Panda", "HarryPotter"]}
dicionario_filmes = {"Aquaman":["5","16:30","15",50]}
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
                    print('5: gerenciar sessões')
                    print('6: Registar ADM')
                    print('7: Gerenciar ingressos')
                    print('8: Fazer logout')
                    op1 = (input('O que deseja fazer?'))
                    if op1 == "1":
                        #listar filmes
                        while op1 == "1":
                            for i in dicionario_filmes:
                                print(i)
                            print("1:voltar para o menu")
                            print("2:rever a lista")
                            quer_continuar = input("escolha uma das opções")
                            if quer_continuar == "1":
                                    op1 = ""
                            #aqui tava tentando fazer um menu mais arrumado pra nn ficar repetindo sempre
                            #todas as 7 opções, da pra fazer nos outros tbm pra deixar mais arrumado e com criatividade
                    #remoção de filmes com dicinonario, no momento estamos usando 2 listas, uma com dicionario e outra so lista msm
                    elif op1 == "2":
                        for x in dicionario_filmes:
                            print(f"{x}")
                        filme_para_remover = input('Digite o filme q queira remover: ')
                        dicionario_filmes.pop(filme_para_remover)
                        print("filme removido com sucesso")
                        print("Nova lista:")
                        for a in dicionario_filmes:
                            print(f"{a}")
                    #adicionar filmes no dicionario, a msm coisa do exemplo acima, temos q ver como fazer
                    #pq com dicionario é mais facil, mais temos q saber como usar lista
                    elif op1 == "3":
                        filme_para_adicionar = input('Digite um filme para adicionar: ')
                        sala_redirecionar = input('para qual sala esse filme vai?')
                        horario = input('a que horas esse filme passara?')
                        ingresso = input("qual sera o valor do ingresso?")
                        qtde_ingresso = int(input("qual a quantidade de ingressos que ira vender?"))
                        dicionario_filmes[filme_para_adicionar] = [sala_redirecionar,horario,ingresso,qtde_ingresso]
                        print("filme adicionado com sucesso")
                        print("Nova lista:")
                        for g in dicionario_filmes:
                            print(f"{g}")
                    #atualizar filmes tbm com dicionario, creio q estão funcionando, é so remover os [] da dicionario filmes
                    elif op1 == "4":
                        for z in dicionario_filmes:
                            print(f"{z}")
                        chaveantiga = input("qual filme gostaria de atulizar?")
                        novo = input("Digite o novo filme")
                        dicionario_filmes[novo] = dicionario_filmes.pop(chaveantiga)
                        print("filme atualizado com sucesso")
                        for c in dicionario_filmes:
                            print(c)
                    #parte de gerenciar sessão ainda imcompleta
                    elif op1 == "5":
                        print("as sessõe no momentos são:")
                        for h in dicionario_filmes:
                            print(f"{h} as {dicionario_filmes[h][1]}")
                        print("mudar horario")
                        print("")
                        print()
                        sessao = input("oque gostaria de fazer?")

                    #registrar um ADM essa parte esta certa e funcionando
                    elif op1 == "6":
                        registrar_adm = input("digite seu nome para registrar")
                        email = input("digite seu email")
                        senha = input("senha para sua conta")
                        if email in ADM:
                            print("email ja existe, tente novamente")
                        else:
                            ADM[email] = [registrar_adm, senha]
                            print("cadastro concluido com sucesso")
                    # aqui ainda nn foi programado
                    elif op1 == "7":
                        for i in dicionario_filmes:
                            print(f"o filme {i} o ingresso esta constando {dicionario_filmes[i][2]}$")
                        alterar_ingresso = input("gostaria de alterar algum ingresso?")
                        if alterar_ingresso == "sim":
                            for p in dicionario_filmes:
                                print(p)
                            valor = input("de qual filme vc quer alterar?")
                            novo_ingresso = input("qual o novo valor do ingresso?")
                            dicionario_filmes[valor][2] = novo_ingresso
                            print(dicionario_filmes)
                        else:
                            print("nenhum ingresso foi alterado")
                    elif op1 == "8":
                        op = ""
                # login de usuarios normais funcionando normal, so tem q fazer dps o submenu deles
            elif email in dicionario_login_normais and dicionario_login_normais[email][1] == senha:
                print("Login bem-sucedido!")
                print(f"bem vindo usuario {dicionario_login_normais[email][0]}")
                while op == "1":
                    #descontos para incentivar a compra de creditos
                    print('1:comprar ingresso')
                    print('2:ver sessões')
                    print('3:cadastrar cartão')
                    print('4:comprar credito')
                    print('5:loggout')
                    op1 = input("Oque deseja fazer?")
                    if op1 == "1":
                        print("a")
                    elif op1 == "3":
                        while op1 == "3":
                            tem_cartao = input("gostaria de registrar seu cartão?:")
                            if tem_cartao != "sim" and tem_cartao != "não":
                                print("caracteres invalidos")
                                tentar_dnv = input("quer tentar novamente?")
                                if tentar_dnv == "não":
                                    op1 = ""
                            elif tem_cartao == "não":
                                op1 = ""
                            elif tem_cartao == "sim":
                                if email in dicionario_creditos and dicionario_creditos[email][0] == card:
                                    print(f"vc ja tem seu cartão registrado: {dicionario_creditos[email][0]}")
                                else:
                                        while op1 == "3":
                                            email = input("digite seu email")
                                            senha = input("digite sua senha")
                                            if email in dicionario_login_normais and dicionario_login_normais[email][1] == senha:
                                                card = input("digite os numeros do seu cartão de credito")
                                                dicionario_creditos[email] = [card, "10"]
                                                print("cartão de credito registrado")
                                                print("vc ganhou 10 de creditos de graça!")
                                                print(dicionario_creditos)
                                                op1 = ""
                                            else:
                                                print("login ou senha errada")
                                                denovo = input("gostaria de tentar novamente?")
                                                if denovo == 'não':

                                                    op1 = ""
                    elif op1 == "5":
                        op = ""
            else:
                print("login ou senha errada")
                denovo = input("gostaria de tentar novamente?")
                if denovo == 'não':
                    op = ""
    elif (op == "2"):
        #registro de usuarios esta funcionando perfeitamente
        while op == "2":
            registrar = input("Digite seu nome para registrar: ")
            email = input("Digite seu email: ")
            senha = input("Crie uma senha para sua conta: ")
            if email in dicionario_login_normais:
                print("Email já registrado, tente novamente.")
            else:
                dicionario_login_normais[email] = [registrar, senha]
                dicionario_creditos[email] = []
                print("Cadastro concluido com sucesso.")
                print(dicionario_creditos)
                op = ""
    #parte dos visitantes esta basicamente pronta, so dar um acabamento dps
    elif (op == "3"):
        print("\nVc esta em modo visitante, não poderá comprar nada, so olhar\n")
        while op == "3":
            print("1: ver filmes e sessões")
            print("2: ")
            print("3: Ajuda")
            print("4: Sair")
            op3 = (input("Escolha uma das opções acima: "))
            if op3 != "1" and op != "2" and op != "3" and op != "4":
                print("caracteres invalidos, tente novamente")
            if op3 == "1":
                for sessao in dicionario_filmes:
                    print(f'esta passando {sessao} as {dicionario_filmes[sessao][1]}\n')
            if op3 == "2":
                print('\nAqui estão as sessões disponiveis:\n')
                for sessao in dicionario_filmes:
                    print(f'esta passando {sessao} as {dicionario_filmes[sessao][1]}\n')
            if op3 == "3":
                print('Para assistir os filmes e comprar ingressos, você precisará se registrar no nosso cinema.')
            if op3 == "4":
                op = ""
    elif(op == "4"):
        break