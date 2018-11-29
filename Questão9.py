InfoCarros = []
dado = []
c = 1
while (c <= 5):    
    print(f"Veículo {c}")
    dado.append(str(input("Nome: ")))
    dado.append(float(input("Km por litro: ")))
    InfoCarros.append(dado[:])
    dado.clear()
    c += 1
print("Relatorio Final...")
cont = 1
Distancia = 0
for Carros in InfoCarros:
    Distancia = 1000 / Carros[1]
    print(f"{cont} - {Carros[0]}   - {Carros[1]} - {Distancia:.1f} Litros  - {Distancia * 3.50:.2f} ")
    cont += 1
carro = Eco = 0
for km in InfoCarros:
    L = km[1]
    if (km[1] > Eco):
        Eco = L
        carro = km[0]
print(f"O menor consumo é do {carro}")
