numero = []
par = []
impar = []

for i in range(20):
    num = int(input('digite um numero'))
    numero.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print("o total de numero foram:")
for x in range(len(numero)):
    print(numero[x])
print("o total de numeros pares foram:")
for z in range(len(par)):
    print(par[z])
print("o total de numero impares foram:")
for o in range(len(impar)):
    print(impar[o])