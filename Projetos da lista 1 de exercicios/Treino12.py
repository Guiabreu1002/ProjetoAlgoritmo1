#fazer um programa de caixa eletronico para sacar o valor:
caixa = int(input("Digite o valor que deseja sacar (entre: 10 e 600)"))

if (10<= caixa and caixa <=600):
    print(f"para sacar o valor {caixa} notas serão emitidas")
    notas_100 = caixa // 100
    caixa %= 100

    notas_50 = caixa // 50
    caixa %= 50

    notas_10 = caixa // 10
    caixa %= 10

    notas_1 = caixa

    print(f"{notas_100} notas de 100")
    print(f"{notas_50} notas de 50")
    print(f"{notas_10} notas de 10")
    print(f"{notas_1} notas de 1")
else:
    print("valor invalido")