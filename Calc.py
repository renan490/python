#Calculadora para contas matemáticas envolvendo dois números. É possível com o "#" utilizar os resultados anteriores.
#Exemplos de entrada:
#79/3
#26.33
##+#
#52.67
#-0.66
#52.01

Total=0
while 1:Exp=input();Total=eval(Exp.replace("#","%s"%Total))if Exp else exit();print("%.2f"%Total)
