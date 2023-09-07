A = float(input("Peso de la esfera A:"))
B = float(input("Peso de la esfera B:"))
C = float(input("Peso de la esfera C:"))
D = float(input("Peso de la esfera D:"))
if A == B and B == C and D != A:
    if D > A:
        print("El peso de la esfera D es mayor que las demás")
    else:
        print("El peso de la esfera D es menor que las demás")
elif A == B and B == D and C != A:
    if C > A:
        print("El peso de la esfera C es mayor que las demás")
    else:
        print("El peso de la esfera C es menor que las demás")
elif A == C and C == D and B != A:
    if B > A:
        print("El peso de la esfera B es mayor que las demás")
    else:
        print("El peso de la esfera B es menor que las demás")
elif B == C and C == D and A != B:
    if A > B:
        print("El peso de la esfera A es mayor que las demás")
    else:
        print("El peso de la esfera A es menor que las demás")
else:
    print("El peso de las esferas no se ingresó correctamente")
