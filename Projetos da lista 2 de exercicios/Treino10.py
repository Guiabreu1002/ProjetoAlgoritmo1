n = int(input("quantas pessoas?"))
soma = 0

for i in range(n):
    pessoa = int(input("digite a idade"))
    soma = pessoa + soma

media = soma / n

if media <= 25:
    print("a media da sala é de jovens")
elif media <= 26 and media < 60:
    print("a media da sala é de adultos")
else:
    print("A media é de idosos")
print(media)
