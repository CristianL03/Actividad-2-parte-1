import math
L1 = float(input("Lado 1 del triángulo:"))
L2 = float(input("Lado 2 del triángulo:"))
L3 = float(input("Lado 3 del triángulo:"))
P = L1+L2+L3
S = P/2
A = math.sqrt(S*(S-L1)*(S-L2)*(S-L3))
print(f"perímetro:{P}",f"semiperímetro:{S}",f"área:{A}", sep="\n")