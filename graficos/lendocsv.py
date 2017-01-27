import pandas as pd
import numpy as np

lendo = pd.read_csv("alimentos.csv")
print("Lendo a tabela\n",lendo.head(),"\n")
print("Lendo a coluna Valor: \n",lendo['Valor'],"\n")
print("Somando a coluna valor: \n",lendo['Valor'].sum(),"\n")
print("Valor-linha 3\n",lendo['Valor'].ix[2],"\n")
print("lendo as primeiras duas linhas: \n",lendo.head(2),"\n")
print("Usando o describe nos Valores: \n",lendo['Valor'].describe(),"\n")
print("Filtrando os dados: \n",lendo[lendo.Valor < 30],"\n")
