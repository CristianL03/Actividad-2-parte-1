Num = int(input("Número de inscripción:"))
Nom = str(input("Nombre completo del estudiante:"))
P = float(input("Patrimonio:"))
E = int(input("Estrato:"))
M = 50000
if P>2000000 and E>3:
  M = M+(P*(3/100))
  print(f"Número de inscripción:{Num}",f"Nombre:{Nom}",f"pago de matrícula:{M}", sep="\n")
else:
  print(f"pago de matrícula:{M}")