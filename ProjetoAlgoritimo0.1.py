#MENU DO PROJETO CINEMA
#tem q adicionar os caracteres de login em string ou da erro na hr do imput

dicionario_login = {"guilherme":"12345" , "caze":"12345"}
lista_de_login = []
lista_de_filmes = []
op_1_break = 0
while True:
    #vms fazer um login normal e um login pra nos como ADM com as opções de poder sobre o programa
    print('escolha uma das opções abaixo')
    print('1:Fazer Login')
    print('2:Se Registrar')
    print('3:Entrar como visitante')
    print('4:Sair')
    op = int(input('digite a opção desejada'))
    if(op == 1):
        while op_1_break == 0:
            login = input("Digite seu nome de usuário: ")
            senha = input("Digite sua senha: ")
            if login in dicionario_login and dicionario_login[login] == senha:
                print("Login bem-sucedido!")
            else:
                print("login ou senha errada tente novamente")
    elif(op == 2):
        #essa parte eu tava pensando em coisas pra fazer para quando a pessoa for registrar sabe
        #soq tem q fazer com dicionario e lista junto
        #da tbm pra tentar ler e dizer se o nome ja esta registrado ou nn
        regist = input("digite seu nome para registrar")
        email = input("digite seu email")
        cpf = int(input("digite seu cpf"))
        lista_de_login.append([regist,email,cpf])
        break
print(lista_de_login)