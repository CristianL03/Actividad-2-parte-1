A = float(input("Número A:"))
B = float(input("Número B:"))
C = float(input("Número C:"))
if A>B and A>C:
  print("A es el mayor")
elif B>A and B>C:
  print("B es el mayor")
elif C>A and C>B:
  print("C es el mayor")
else:
  print("Hay dos o más números iguales que son mayores")