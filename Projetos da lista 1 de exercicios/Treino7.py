#fazer o programa somar os salarios adicionando um percentual
Sal = float(input("Digite seu salario"))

if (Sal < 280):
    perc = Sal * 0.20
    print("seu percentual de aumento foi de 20%")
if (Sal >= 280 and Sal < 700):
    perc = Sal * 0.15
    print("seu percentual de aumento foi de 15%")
if (Sal >= 700 and Sal <1500):
    perc = Sal * 0.10
    print("seu percentual de aumento foi de 10%")
if (Sal >= 1500):
    perc = Sal * 0.05
    print("seu percentual de aumento foi de 5%")

Sal_final = Sal + perc
aumento = Sal_final - Sal

print(f"Seu salario era de {Sal}")
print(f"Vc teve um aumento de {aumento}")
print(f"seu novo salario é {Sal_final}")

#funcionando.