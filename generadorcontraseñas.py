import random

print("Bienvenido al generador de contraseñas, por favor selecciona la cantidad de digitos que deseas en tu contraseña")
numero_digitos = int(input("Ingresa el numero de longitud: "))

lst_contraseña = []
for digito in range(0, numero_digitos):
    digito = random.randint(0, 9)
    lst_contraseña.append(digito)

print(digito)
print(lst_contraseña)
