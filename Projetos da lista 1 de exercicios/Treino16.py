num = int(input("Digite um numero inteiro até 1000"))

centenas = num // 100
resto = num % 100
dezenas = resto // 10
unidade = num % 10

print(f"a quantidade de centenas é {centenas}")
print(f"a quantidade de dezenas é {dezenas}")
print(f"a quantidade de unidades é {unidade} ")
