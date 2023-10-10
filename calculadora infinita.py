while True:
    while True:

        x = (input("introduce el primer numero ó (salir) para terminar: "))
        x = x.lower()
        if x == "salir":
            break
        else:
            x = int(x)

        operacion = input(
            "Introduce la operacion (+),(-),(*),(/) ó (salir) para terminar: ")
        if operacion.lower() == "salir":
            break

        y = (input("introduce el segundo numero ó (salir) para terminar: "))
        y = y.lower()
        if y == "salir":
            break
        else:
            y = int(y)

        if operacion == "+":
            resultado = x + y
            print(f"La suma de {x} {operacion} {y} = {resultado}")
        elif operacion == "-":
            resultado = x - y
            print(f"La resta de {x} {operacion} {y} = {resultado}")
        elif operacion == "/":
            resultado = x / y
            print(f"La division de {x} {operacion} {y} = {resultado}")
        elif operacion == "*":
            resultado = x * y
            print(f"La multiplicacion de {x} {operacion} {y} = {resultado}")
        else:
            print("Operacion invalida ingresa uno correcto")

        salirCalc = input("Deseas hacer otro calculo rapido? (S/N): ")
        salircalc = salirCalc.lower()
        if salirCalc == "s":
            continue
        else:
            break

    break
