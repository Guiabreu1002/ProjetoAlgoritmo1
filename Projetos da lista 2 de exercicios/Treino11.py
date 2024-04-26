n = int(input("digite um numero inteiro"))
divisão = 0
for i in range(1, n):
    if i %2 != 0:
        divisão += 1
        print(f"{i} é primo")

print(f"o total de divisão é de {divisão}")
