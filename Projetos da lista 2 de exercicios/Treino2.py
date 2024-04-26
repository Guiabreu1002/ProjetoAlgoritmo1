
while True:
    nome = input("digite seu nome")
    senha = input("digite sua senha")
    if nome != senha:
        print(f"informações corretas {nome} e {senha}")
        break
    else:
        print("nome e senha são iguais, digite novamente")