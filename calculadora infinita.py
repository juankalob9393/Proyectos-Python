while True:

    operacion = input(
        "Introduce la operacion (+),(-),(*),(/) tambien introduce (salir) para terminar: ")
    if operacion.lower() == "salir":
        break

    x = int(input("introduce el primer numero: "))
    y = int(input("Introduce el segundo numero: "))

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
