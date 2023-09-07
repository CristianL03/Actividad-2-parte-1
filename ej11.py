Nom = str(input("Nombre del empleado:"))
Sh = float(input("Salario por hora:"))
H = float(input("Horas trabajadas al mes:"))
Sm = Sh * H
if Sm > 450000:
    print(f"Nombre:{Nom}", f"Salario mensual:{Sm}", sep="\n")
else:
    print(f"Nombre:{Nom}")
