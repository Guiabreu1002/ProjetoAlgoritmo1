
while True:
    nota = int(input("digite uma nota entre 0 e 10"))
    if 0 <= nota <= 10:
        print(f"nota valida {nota}")
        break
    else:
        print("valor invalido, digite novamente")