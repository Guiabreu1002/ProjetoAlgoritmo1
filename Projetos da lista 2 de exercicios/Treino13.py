#O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de
#quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado
#o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na
#tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os
#preços de 1 até 50 produtos, conforme o exemplo abaixo:

p = int(input("quantos produtos vc vai querer comprar?"))

pedido = 0

for i in range(p):
    pedido += 1

valor_final = pedido * 1.99

print("o valor que vc tera que pagar é de {}".format(valor_final))