nota = 0
nota2 = 0
nota_mais_baixa = 0
nota_mais_alta = 0
total_de_pessoas = 0
erros = 0
erros_teste = 10
continuar = "sim"
while continuar == "sim":
    nome = input("digite seu nome")
    for i in range(1,11):
        resposta = input("digite a resposta da prova:")
        if i == 1 and resposta == "A":
            nota += 1
            erros_teste -= 1
        elif i == 2 and resposta == "B":
            nota += 1
            erros_teste -= 1
        elif i == 3 and resposta == "C":
            nota += 1
            erros_teste -= 1
        elif i == 4 and resposta == "D":
            nota += 1
            erros_teste -= 1
        elif i == 5 and resposta == "E":
            nota += 1
            erros_teste -= 1
        elif i == 6 and resposta == "E":
            nota += 1
            erros_teste -= 1
        elif i == 7 and resposta == "D":
            nota += 1
            erros_teste -= 1
        elif i == 8 and resposta == "C":
            nota += 1
            erros_teste -= 1
        elif i == 9 and resposta == "B":
            nota += 1
            erros_teste -= 1
        elif i == 10 and resposta == "A":
            nota += 1
            erros_teste -= 1
        else:
            erros += 1
    total_de_pessoas += 1
    nota2 += nota
    continuar = input("Outro aluna vai ultilizar o programa?")
    if nota > nota_mais_alta:
        nota_mais_alta = nota
    if nota < erros_teste:
        nota_mais_baixa = nota
    if continuar == "sim":
        nota = 0
        erros_teste = 10
media = ""
if total_de_pessoas > 0:
    media = nota2 / total_de_pessoas
else:
    print("não teve pessoas")
print(f"a nota mais alta foi {nota_mais_alta}")
print(f"a nota mais baixa foi {nota_mais_baixa}")
print(f"o total de aluno que usou o programa foi {total_de_pessoas}")
print("a media de notas dos alunos foi de {:.2}".format(media))
print(f"o total de erros foi de {erros}")