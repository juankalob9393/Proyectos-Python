while True:
    Dic_ARa = {"Nombre": "Dragon Alado Del Ra", "Ataque": "????",
               "Defensa": "???", "Tipo": "Bestia Divina"}
    Dic_Obe = {"Nombre": "Obelisco El Atormentador", "Ataque": "4000",
               "Defensa": "4000", "Tipo": "Bestia Divina"}
    Dic_Sli = {"Nombre": "Slifer El Dragon Celestial", "Ataque": "XXXX",
               "Defensa": "XXXX", "Tipo": "Bestia Divina"}

    print("**Bienvenido al identificador de cartas de YuGiOh, a continuacion te muestro los nombres de las cartas en la base datos: ")
    print("Dragon Alado Del Ra (1)")
    print("Obelisco El Atormentador (2)")
    print("Slifer El Dragon Celestial (3)")
    Num_Analizar = input(
        "**Ingresa el numero de la carta a analizar (1,2,3) o ingresa |salir| para terminar: ")

    if Num_Analizar.lower() == "salir":
        break
    Num_Analizar = int(Num_Analizar)

    if Num_Analizar == 1:
        print("La tarjeta", Dic_ARa.get("Nombre"), "tiene un ataque de", Dic_ARa.get(
            "Ataque"), "con una defensa de", Dic_ARa.get("Defensa"), "y esta carta es de tipo", Dic_ARa.get("Tipo"))
    elif Num_Analizar == 2:
        print("La tarjeta", Dic_Obe.get("Nombre"), "tiene un ataque de", Dic_Obe.get(
            "Ataque"), "con una defensa de", Dic_Obe.get("Defensa"), "y esta carta es de tipo", Dic_Obe.get("Tipo"))
    elif Num_Analizar == 3:
        print("La tarjeta", Dic_Sli.get("Nombre"), "tiene un ataque de", Dic_Sli.get(
            "Ataque"), "con una defensa de", Dic_Sli.get("Defensa"), "y esta carta es de tipo", Dic_Sli.get("Tipo"))
