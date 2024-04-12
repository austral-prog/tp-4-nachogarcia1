import math

def line():
    cof_a =float(input("Ingrese el coeficiente A: "))
    cof_b =float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 =float(input("Ingrese el coeficiente X2: "))
    Y1 = cof_a * X1 + cof_b
    Y2 = cof_a * X2 + cof_b

    p = [X1, Y1]
    q = [X2, Y2]

    print(f"El coeficiente A de su ecuación de la recta es: {cof_a}")
    print(f"El coeficiente B de su ecuación de la recta es: {cof_b}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")

    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {cof_a}X + {cof_b}")

    print("")
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({X1}, {Y1})")
    print(f"\tP2 ({X2}, {Y2})")

    print("")

    print(f"La distancia entre ellos es: {math.dist(p, q)}")



