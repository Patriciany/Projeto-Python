cond = 1
Soma = 0
while(cond <= 4):
	n = float(input("Digite sua nota:"))
	cond += 1
	Soma += n
Media = Soma / 4
print("Sua Média Final foi: {}".format(Media))
