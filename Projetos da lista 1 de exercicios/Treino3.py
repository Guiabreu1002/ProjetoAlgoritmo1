#fazer o programa definir o tipo de triangulo
a=float(input("digite o valor"))
b=float(input("digite o valor"))
c=float(input("digite o valor"))
if(a==b==c):
    print("este é um triangulo equilatero")
if (a==b and a!=c and b!=c):
    print("este é um triangulo isoceles")
if(a!=b and b!=c and a!=c):
    print("este é um triangulo escaleno")

#funcionando.