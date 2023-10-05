a = input("Ingresa el nombre de la carta: ")
b = input("Ingresa su ataque: ")
c = input("Ingresa su defensa: ")
d = input("Ingresa su tipo: ")


def Diccionario_carta(a, b, c, d):
    New_dic = {"nombre": a, "Ataque": b, "Defensa": c, "Tipo": d}
    print(New_dic)


Diccionario_carta(a, b, c, d)
