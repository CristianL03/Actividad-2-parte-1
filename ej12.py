import math
A = float(input("Valor de A:"))
B = float(input("Valor de B:"))
C = float(input("Valor de C:"))
disc = (B**2)-(4*A*C)
if disc<0:
  print("La ecuación no tiene solución")
else:
  rz = math.sqrt(disc)
  x1 = (-B+rz)/2*A
  x2 = (-B-rz)/2*A
  print(f"Solución 1:{x1}",f"Solución 2:{x2}", sep="\n")