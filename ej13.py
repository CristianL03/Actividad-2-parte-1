A = float(input("Peso de la esfera A:"))
B = float(input("Peso de la esfera B:"))
C = float(input("Peso de la esfera C:"))
if A>B and A>C:
  print("La esfera A tiene el mayor peso")
elif B>A and B>C:
  print("La esfera B tiene el mayor peso")
elif C>A and C>B:
  print("La esfera C tiene el mayor peso")
else:
  print("Los pesos de las 3 esferas no son diferentes")