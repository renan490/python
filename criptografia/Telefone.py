#Telefone
#Desafio do Code Golf #003 28/11 a 02/12
#Que tal decorar numeros de telefone associando seus digitos com letras?
#Exemplo:
#Entrada:
#1-HOME-SWEET-HOME
#MY-MISERABLE-JOB
#Saída
#1-4663-79338-4663
#69-647372253-562

t="";n="22233344455566677778889999"
for c in input():
 for i in range(26):
  if c==chr(65+i):t+=n[i];break
 else:t+=c
print(t)
