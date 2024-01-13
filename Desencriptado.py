import random

password = 5962
lst_password = []
for numeros in str(password):
    (lst_password.append(numeros))
# * aqui uso el metodo de map para poder aplicar la funcion de int a cada uno de los elementos de la lista creada
lst2_password = list(map(int, lst_password))
# * aqui uso el metodo de map para poder aplicar la funcion de int a cada uno de los elementos de la lista creada
# print(lst2_password)

while True:
    puerta1 = False
    numero_aleatorio1 = random.randint(0, 9)
    if numero_aleatorio1 == lst2_password[0]:
        puerta1 = True
        print(f"Numero encontrado: {numero_aleatorio1}")
        break
    else:
        print(f"Numero erroneo: {numero_aleatorio1}")
        continue

print(puerta1)

while True:
    puerta2 = False
    numero_aleatorio2 = random.randint(0, 9)
    if numero_aleatorio2 == lst2_password[1]:
        puerta2 = True
        print(f"Numero encontrado: {numero_aleatorio2}")
        break
    else:
        print(f"Numero erroneo: {numero_aleatorio2}")
        continue

print(puerta2)

while True:
    puerta3 = False
    numero_aleatorio3 = random.randint(0, 9)
    if numero_aleatorio3 == lst2_password[2]:
        puerta3 = True
        print(f"Numero encontrado: {numero_aleatorio3}")
        break
    else:
        print(f"Numero erroneo: {numero_aleatorio3}")
        continue

print(puerta3)

while True:
    puerta4 = False
    numero_aleatorio4 = random.randint(0, 9)
    if numero_aleatorio4 == lst2_password[3]:
        puerta4 = True
        print(f"Numero encontrado: {numero_aleatorio4}")
        break
    else:
        print(f"Numero erroneo: {numero_aleatorio4}")
        continue

print(puerta4)

nip = [numero_aleatorio1, numero_aleatorio2,
       numero_aleatorio3, numero_aleatorio4]

print(f"El nip final encontrado es: {nip}")
