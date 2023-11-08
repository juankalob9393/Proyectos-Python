import random
print("""****Bienvenido al juego del numero adivinador, tienes que adivinar el numero que python escogio por ti****""")
num_azar = random.randint(1,5)

while True:
	num_ing = input("Introduce un numero para intentar adivinar el de python, si quieres terminar introduce salir: ")

	if num_ing.lower() == "salir":
		break
	elif num_ing != "salir":
		num_ing = int(num_ing)

	while True:
		if num_ing > num_azar:
			print("El numero es menor, intenta de nuevo")
			break
		elif num_ing < num_azar:
			print("El numero es mayor, intenta de nuevo")
			break
		else:
			print("-*-*-*-*-*-*- Es el correcto -*-*-*-*-*-*-*-*- El juegos se va a reiniciar")
			break
