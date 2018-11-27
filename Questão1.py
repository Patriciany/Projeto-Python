cond = 1
Soma = 0
while(cond <= 3):
	n = float(input("Digite sua nota:"))
	cond += 1
	Soma += n
Media = Soma / 3
if (Media == 10.0):
	print("Aprovado com Distinção!")
elif (Media >= 7):
	print("Aprovado!")
else:
	print("Reprovado!")
