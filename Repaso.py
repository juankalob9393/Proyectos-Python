# --------------------------------------------------------------------------------------TEST DE EDAD------------------------------------------------------------

# edad_usuario = int(input("Cual es tu edad?: "))

# if edad_usuario >= 18:
#     print("Tu eres mayor de edad")
# else:
#     print("Tu eres menor de edad")


# ---------------------------------------------------------------------------------TEST DE CONTRASEÑA------------------------------------------------------------

# contraseña_first = "jaime"

# while True:
#     contraseña_new = (input("Ingresa la contraseña: "))
#     contraseña_new = contraseña_new.lower()

#     if contraseña_new == contraseña_first:
#         print("Contraseña correcta")
#         break
#     elif contraseña_new == "Salir":
#         break
#     else:
#         print("Introduce de nuevo la contraseña")

# ---------------------------------------------------------------------------------TEST DE PAR O IMPAR------------------------------------------------------------


# numero_prueba = int(input("Introduce un numero: "))
# Divinum = numero_prueba % 2

# if Divinum == 0:
#     print("Numero Par")
# else:
#     print("Numero Inpar")

# ---------------------------------------------------------------------------------TEST DE IMPUESTOS------------------------------------------------------------

# nombre = input("Ingresa tu Nombre: ")
# Ingresos = int(input("Cual es tu ingreso sin decimales?: "))
# edad = int(input("Cual es tu edad?: "))

# print(
#     f"Tu nombre es {nombre} y tienes una edad de {edad} años con un ingreso mensual de ${Ingresos} pesos")

# if edad > 18 and Ingresos > 3000:
#     print(f"Tu {nombre} tienes que declarar impuestos")
# else:
#     print(
#         f"No es necesario que declares impuestos {nombre} ya que tus ingresos son menores a $3000.00 y no eres mayor de edad.")

# ---------------------------------------------------------------------------------TEST REPETICION EN FOR ------------------------------------------------------------

# nombreUsuario = input("Ingresa tu nombre:")
# for i in range(9):
#     print(nombreUsuario)
# ----------------------------------------------------------------------------------------------------
# nombreUsuario = input("Ingresa tu nombre:")
# Lst = ["Perro", "Agua", "Chanchito"]
# for i in Lst:
#     print(nombreUsuario)
# ----------------------------------------------------------------------------------------------------
# lst = ["Perro", "gato", "Oso"]
# ----------------------------------------------------------------------------------------------------
# for i in lst:
#     print(i*2)
# ----------------------------------------------------------------------------------------------------
# edad = int(input("Cual es tu edad?: "))
# for i in range(edad):
#     print("Tu edad es de " + str(i+1) + " años")
# ----------------------------------------------------------------------------------------------------
# numero = int(input("Introduce un numero: "))
# ----------------------------------------------------------------------------------------------------
# for i in range(0, numero):
#     if i % 3 == 0:
#         print(i)
# ----------------------------------------------------------------------------------------------------
# numero = int(input("Introduce un numero: "))
# for i in range(0, numero):
#     print(i+1, end=",")
# ----------------------------------------------------------------------------------------------------
# numero = int(input("Ingresa numero entero: "))
# for i in range(numero, -1, -5):
#     print(i, end=(","))
