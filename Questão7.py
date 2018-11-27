valores1 = []
valores2 = []
valores3 = []
print("Primeiro vetor...")
for c in range(0,10):
    num1 = int(input("Digite um número: "))
    valores1.append(num1)
print("Segundo vetor...")
for c in range(0,10):
    num2 = int(input("Digite um número: "))
    valores2.append(num2)
valores3.append(valores1)
valores3.append(valores2)
print(valores3)
