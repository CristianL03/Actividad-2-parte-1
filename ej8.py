V = float(input("Valor de la compra:"))
C = str(input("Color de la bola:"))
if C=="blanco":
  print(f"El valor a pagar es:{V}")
elif C=="verde":
  V = V-(V*0.1)
  print(f"El valor a pagar es:{V}")
elif C=="amarillo":
  V = V-(V*0.25)
  print(f"El valor a pagar es:{V}")
elif C=="azul":
  V = V-(V*0.5)
  print(f"El valor a pagar es:{V}")
else:
  V = 0
  print(f"El valor a pagar es:{V}")