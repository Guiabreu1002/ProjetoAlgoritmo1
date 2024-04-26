#fazer o computador interrogar sobre o crime

print("Responda com Sim ou Não")
per = input("Telefonou para a vitima?")
per1 = input("Esteve no local do crime?")
per2 = input("Mora perto da vitima?")
per3 = input("Devia para a vitima?")
per4 = input("Ja trabalhou com a vitima?")

soma = 0

if (per == "sim"):
    soma += 1
if (per1 == "sim"):
    soma += 1
if (per2 == "sim"):
    soma += 1
if (per3 == "sim"):
    soma += 1
if (per4 == "sim"):
    soma += 1

print("cheguei a uma conclusão")

if(soma == 2):
    print("Vc é suspeito")
elif(soma == 3 or soma == 4):
    print("Vc é cumplice")
elif(soma == 5):
    print("Vc é o assassino")
else:
    print("Vc é Inocente")

