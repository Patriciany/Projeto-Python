list = list()
while (True):
	nota = float(input("Digite suas notas[Quanto quiser parar use(-1)]"))
	if(nota == -1):
		break
	list.append(nota)
taman = len(list)
print("A quantidade de valores lidos foi: {}".format(taman))
print("Os valores informados foram: {}".format(list))
inversa = [ ]
c = taman -1 
while (c >= 0):
	inversa.append(list[c])
	c -= 1
print("O inverso dos valores informados foi: {}".format(inversa))
soma = 0
for num in list:
	soma += num
media = soma / taman
print("A soma total dos valores informados foi: {}".format(soma))
print("O valor da Média final foi: {:.1f}".format(media))
MaiorM = [ ]
Menor7 = [ ]
for n in list:
	if (n > media):
		MaiorM.append(n)
	if (n < 7):
		Menor7.append(n)
print("Os valores maiores que a Média foi: {}".format(MaiorM))
print("Os valores Menores que 7 foi: {}".format(Menor7))
print("Obrigado! Volte Sempre!")
