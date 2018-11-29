perg = ["Telefonou para a vítima?","Esteve no local do crime?"
,"Mora perto da vítima?", "Devia para a vítima?",
"Já trabalhou com a vítima?"]
respostas = 0 
si = 0
for c in perg:
  respostas = str(input(f"{c} [Sim/Não]: ")).lower()
  if (respostas in "sim"):
    si += 1
if (si == 2):
  print("Suspeito")
elif( 3 <= si <= 4):
  print("Cúmplice")
elif( si == 5):
  print("Assasino")
else:
  print("Inocente")
