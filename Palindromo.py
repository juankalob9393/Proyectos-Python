print("FUNCION DE PALINDROMO")

Palindro1 = input("Ingresa tu Oracion o palabra a verificar: ")


def espaciosblancos(Frase1):
    frasenueva = ""
    for char in Frase1:
        if char == " ":
            char = ""
        else:
            frasenueva += char
    return frasenueva


print("STOP1")
l1 = ((espaciosblancos(Palindro1)).lower())
print(l1, "Elimine los espacios")


def voltear(Frase2):  # ! VOLTEA ORACION O PALABRA
    return Frase2[::-1]


print("STOP2")  # ! Muestra la frase volteada
l2 = voltear(l1)
print(l2, "Pude Voltear la frase o palabra")


def comprobacionFinal(Frase3, Frase4):  # ! COMPRUEBA SI LA PALABRA ES PALINDROMO O NO
    if Frase3 == Frase4:
        a1 = "Si es un palindromo"
    else:
        a1 = "No es un palindromo"
    return a1


print("STOP3")
l3 = comprobacionFinal(l1, l2)
print(l3)
