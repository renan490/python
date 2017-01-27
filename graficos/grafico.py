import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Lendo o CSV
lendo = pd.read_csv("alimentos.csv")
#Lista dos valores
ListaValor = lendo['Valor']
#Lista dos legumes
ListaLegumes = lendo['Legumes']
#Tamanho da lista
x_pos = np.arange(len(ListaLegumes))
legumes = [x[:3] for x in ListaLegumes]
#Definindo o gráfico pelos valores
first_bar = plt.bar(x_pos, ListaValor, 0.5, color='b')
# Definir posição e labels no eixo X
#Os legumes ficarão na base
plt.xticks(x_pos+0.25,ListaLegumes)
#apresentar o gráfico
plt.show()
