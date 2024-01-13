import random

password = 5962
lst_password = []
for numeros in str(password):
    (lst_password.append(numeros))
# * aqui uso el metodo de map para poder aplicar la funcion de int a cada uno de los elementos de la lista creada
lst2_password = list(map(int, lst_password))
# * aqui uso el metodo de map para poder aplicar la funcion de int a cada uno de los elementos de la lista creada
# print(lst2_password)


def desencriptado(digito):
    while True:
        numero_aleatorio = random.randint(0, 9)
        if numero_aleatorio == lst2_password[digito]:
            print(f"Numero encontrado: {numero_aleatorio}")
            return numero_aleatorio
        else:
            print(f"Numero erroneo: {numero_aleatorio}")
        continue


nip1 = desencriptado(0)
nip2 = desencriptado(1)
nip3 = desencriptado(2)
nip4 = desencriptado(3)

NIP_Completo = [nip1, nip2,
                nip3, nip4]

print(f"El NIP encontrado es:  {NIP_Completo}")
