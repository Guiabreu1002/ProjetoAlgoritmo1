# MENU DO PROJETO CINEMA
# tem q adicionar os caracteres de login em string ou da erro na hr do imput

dicionario_login = {"guilherme": "12345", "caze": "12345"}
lista_de_login = []
lista_de_filmes = []
op_1_break = 0
while True:
    # vms fazer um login normal e um login pra nos como ADM com as opções de poder sobre o programa
    print('Escolha uma das opções abaixo: ')
    print('1:Fazer Login')
    print('2:Se Registrar')
    print('3:Entrar como visitante')
    print('4:Sair')
    op = int(input('Digite a opção desejada: '))
    if (op == 1):
        while op_1_break == 0:
            login = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")
            if login in dicionario_login and dicionario_login[login] == senha:
                print("Login bem-sucedido!")
            else:
                print("login ou senha errada tente novamente")
            break
    elif (op == 2):
        # essa parte eu tava pensando em coisas pra fazer para quando a pessoa for registrar sabe
        # soq tem q fazer com dicionario e lista junto
        # da tbm pra tentar ler e dizer se o nome ja esta registrado ou nn
        register = input("Digite seu nome para registrar-se: ")
        email = input("Digite seu email: ")
        cpf = int(input("Digite seu cpf: "))
        # Aqui a gente podia fazer com que fosse contado os caracteres do CPF, pq o cpf tem um limite, por exemplo,
        #de acordo com a net o CPF tem um maximo de 11 caracteres, deviamos implementar isso dai
        lista_de_login.append([regist, email, cpf])
        break
print(lista_de_login)
