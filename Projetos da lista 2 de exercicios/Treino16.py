#menu teste
lista = ["guilherme","Gustavo","Rene", "Julia"]
op_1_break = 0
while True:
    print('escolha uma das opções abaixo')
    print('1:adicionar nome')
    print('2:listar pessoas')
    print('3:buscar pessoas')
    print('4:remover pessoas')
    print('5:atualizar pessoas')
    print('0:Sair')
    op = int(input('digite a opção desejada'))
    if(op == 1):
        while op_1_break == 0:
            nome = input("digite o nome para adicionar ou S para sair")
            lista.append(nome)
            if nome == "S":
                op_1_break = 1
                lista.remove("S")
    elif(op == 2):
        for i in range(len(lista)):
            print(lista[i])
    elif(op == 3):
        buscar = input("qual nome gostaria de buscar?")
        for i in lista:
            if i.count(buscar) > 0:
                print(buscar)
    elif(op == 4):
        for i in range(len(lista)):
            print(f'{i} {lista[i]}')
        remover = input("qual nome vc deseja remover?")
        for i in range(len(lista)):
            if(lista[i].count(remover) > 0):
                print(f"{i} - {lista[i]}")
        rem = int(input("Digite o indice para remover"))
        lista.pop(rem)
    elif(op == 5):
        for i in range(len(lista)):
            print(f'{i} {lista[i]}')
        atulizar = input("qual nome vc deseja atualizar?")
        for i in range(len(lista)):
            if(lista[i].count(atulizar) > 0):
                print(f"{i} - {lista[i]}")
        ind_atu = int(input("digite o codigo do uzuario para atualizar"))
        novo = (input("Digite o novo nome"))
        lista[ind_atu] = novo
    elif(op == 0):
        break


