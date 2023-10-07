# ---------------------------------------------------------------------------------TEST DE ACOMODO DE GRUPO POR SEXO MODIFICADO------------------------------------------------------------
while True:

    Mujeres_grpA = []
    Hombres_grpB = []

    while True:
        sexo = input(
            "Ingresa el sexo de la persona, (M/H) o (Salir) para no continuar: ")
        sexo = str(sexo.capitalize())

        if sexo.capitalize() == "Salir":
            break
        elif sexo.capitalize() != "H" and sexo.capitalize() != "M":
            print("No es correcto ingresa un sexo ya sea Hombre (H) o mujer (M)")
            continue

        nombre = input(
            "Ingresa un nombre del alumno o (Salir) para no continuar: ")
        nombre = str(nombre.capitalize())

        if nombre == "Salir":
            break

        if sexo == "M":
            Mujeres_grpA.append(nombre)
        elif sexo == "H":
            Hombres_grpB.append(nombre)

        mensaje_continuo = input(
            f"""Deseas continuar agregando personas?, (Si) para continuar y (No) para terminar
            Te comparto las listas de alumnos segun su sexo ingresado con anterioridad:
            Lista de hombres = {Hombres_grpB}
            Lista de Mujeres = {Mujeres_grpA} """)

        if mensaje_continuo.capitalize() == "Si":
            continue
        else:
            break

    seguir = input(
        "¿Quieres ingresar más nombres en una nueva lista? (Si/No): ")
    if seguir.capitalize() != "Si":
        break
