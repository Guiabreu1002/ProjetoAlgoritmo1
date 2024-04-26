#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
vogais = ['a','e','i','o','u']
carat = []
for i in range(10):
    caractere = input("digite um caractere, exemplo 'a'")
    carat.append(caractere)
qtde = 0
for x in carat:
    if (x in vogais):
        qtde += 1
print(qtde)


