fibo = int(input("digite um numero que queira saber da fibo"))
atual = 1
ant = 0
prox = 0

for i in range(fibo):
    if fibo >= 0:
        prox = atual + ant
        ant = atual
        atual = prox
        print(prox)