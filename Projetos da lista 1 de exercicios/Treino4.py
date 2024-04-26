#fazer o programa calcular as 4 medias
N1 = float(input('digite sua nota'))
N2 = float(input('digite sua nota'))
N3 = float(input('digite sua nota'))
N4 = float(input('digite sua nota'))

media = (N1+N2+N3+N4) / 4

if (media >= 0 and media < 4):
    print('Vc tirou E, vc ficou')
if (media >= 4 and media <6):
    print('Vc tirou D, vc ficou')
if (media >= 6 and media <7.5):
    print('vc tirou C, vc passou')
if (media >= 7.5 and media < 9):
    print('vc tirou B, vc passou')
if (media >= 9 and media <10):
    print('vc tirou A, vc passou')

print(f'Sua media é de {media}')

#funcionando.