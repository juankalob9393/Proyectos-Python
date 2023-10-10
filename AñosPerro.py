Nombreperro = input("Ingresa el nombre de tu perro: ").capitalize()
edadPerro = int(input("Ingresa la edad en años de tu perro: "))

if edadPerro == 1:
    Mensaje = "Su edad en humano es de 20 años"
elif edadPerro == 2:
    Mensaje = "Su edad en humano es de 28 años"
elif edadPerro == 3:
    Mensaje = "Su edad en humano es de 32 años"
elif edadPerro == 4:
    Mensaje = "Su edad en humano es de 36 años"
elif edadPerro == 5:
    Mensaje = "Su edad en humano es de 40 años"
elif edadPerro == 6:
    Mensaje = "Su edad en humano es de 44 años"
elif edadPerro == 7:
    Mensaje = "Su edad en humano es de 48 años"
elif edadPerro == 8:
    Mensaje = "Su edad en humano es de 52 años"
elif edadPerro == 9:
    Mensaje = "Su edad en humano es de 56 años"
else:
    Mensaje = "Supera los 56 años ya esta pagando horas extras"

print(f" {Nombreperro} tiene una edad perruna de {edadPerro} años entonces {Mensaje}")
