num = int(input("digite um numero para fatoriar"))
fatorial = 1
expressão = ""
for i in range(num, 0 , -1):
    fatorial *= i
    expressão += str(i)
    if i != 1:
        expressão += " . "
print(f"o fatorial de :{num}!")
print(end="{}! = {} = {} ".format(num, expressão , fatorial))

#(produto * 5 / 100)