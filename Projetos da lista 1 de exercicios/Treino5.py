#tentar fazer o programa indicar o produto mais barato
p1 = float(input("Digite o valor do produto"))
p2 = float(input("Digite o valor do produto"))
p3 = float(input("Digite o valor do produto"))

if (p1 < p2 and p1 < p3):
    print("vc deve comprar o produto1")
if (p2 < p1 and p2 < p3):
    print("vc deve comprar o produto2")
if (p3 < p2 and p3 < p1):
    print("vc deve comprar o produto3")

#funcionando.