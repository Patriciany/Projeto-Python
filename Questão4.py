tipo = str(input("Qual tipo de carne vc vai levar?"))
quantidade = int(input("Qual vai ser a Quantidade?"))
if (tipo == "File Duplo"):
	if (quantidade <= 5 ):
		total = 4.90
	elif (quantidade > 5):
		total = 5.80
elif (tipo == "Alcatra"):
	if (quantidade <= 5):
		total = 5.90
	elif (quantidade > 5):
		total = 6.80
elif (tipo == "Picanha"):
	if (quantidade <= 5):
		total = 6.90
	elif (quantidade > 5):
		total = 7.80
total1 = total * quantidade
FormaP = str(input("Qual a Forma de Pagamento?"))
if (FormaP == "Cartão Tabajara"):
	desconto = (total1 * 5 / 100)
	total2 = total1 - (total1 * 5 / 100)
else:
	desconto = 0 
	total2 = 0
print("Sua Nota Fiscal...")
print("Produto:{}".format(tipo))
print("{}Kg De {}".format(quantidade, tipo))
print("Valor total a Pagar R${:.2f}".format(total1))
print("Forma de Pagamento: {} ".format(FormaP))
print("Valor do Desconto: R${:.2f}".format(desconto))
print("Valor Total a Pagar caso haja Desconto: R${:.2f}".format(total2))Detalhes
