media_dos_alunos = []
n = int(input("quantos alunos vai suar o programa?:"))
notas_soma = 0
for i in range(n):
    print("proximo")
    for notas in range(1,4+1):
        nota = float(input("digite sua nota"))
        notas_soma += nota
        if notas == 4:
            media = notas_soma / 4
            media_dos_alunos.append(media)
            notas_soma = 0
print(f"as media dos {n} alunos foram:")
for x in range(len(media_dos_alunos)):
    print(media_dos_alunos[x])
print("e as medias acimas de 7 foram:")
for z in range(len(media_dos_alunos)):
    if (media_dos_alunos[z] >= 7):
        print(media_dos_alunos[z])
