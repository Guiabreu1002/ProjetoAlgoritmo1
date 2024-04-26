import pandas as pd

dados = pd.read_html('https://pt.wikipedia.org/wiki/Club_de_Regatas_Vasco_da_Gama')

len(dados)

for tabela in dados:
  if(tabela.columns[0] == 'MUNDIAIS'):
    for titulo in tabela['MUNDIAIS']['Competições']:
      if(titulo == 'Copa Intercontinental'):
        print('ACHEI O MUNDIAL DO VASCO')
else:
  print('nao achei nenhum mundial')