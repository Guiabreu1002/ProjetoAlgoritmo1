vetor = []
media = 0
nota = 0
for i in range(4):
    numero = float(input("digite um numero"))
    vetor.append(numero)
    media += 1
    nota += numero
media = nota / media
print("as notas inseridas são:")
for x in reversed(vetor):
    print(x)
print(f"a media é {media}")
