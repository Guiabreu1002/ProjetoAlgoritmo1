aluguel = int(input("quandos dias vc alugou o carro?"))
kmr = float(input("quantos km vc rodou?"))
dia = 60 * aluguel
tax = 0.15 * kmr
soma = dia + tax
print("o total a pagar pelo carro alugado é de R${}".format(soma))