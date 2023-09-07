import math
L = float(input("Lado del triángulo equilatero:"))
P = 3*L
H = ((math.sqrt(3))*L)/2
A = ((L**2)*math.sqrt(3))/4
print(f"perímetro:{P}",f"altura:{H}",f"área:{A}", sep="\n")