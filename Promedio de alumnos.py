while True:  # todo lo que va dentro del codigo While es para ejecutar un bucle
    Nombre_Alumno = input(
        "Hola! favor de ingresa tu nombre y si no quieres continuar introduce (salir): ")
    if Nombre_Alumno.lower() == "salir":
        break
    print(
        f"Hola {Nombre_Alumno.capitalize()} Por favor captura tus 6 calificaciones de todo el semestre")
    lista_calificaciones = []  # lista vacia para poder llenar con las  calificaciones
    for i in range(6):
        lista_calificaciones.append(
            int(input("Calificacion " + str(i+1) + ":")))
        # la siguiente linea de codigo como se va ingresando poco a poco las calificaciones :)
        print(lista_calificaciones)
    Promedio = sum(lista_calificaciones) / len(lista_calificaciones)
    print(f"Tu promedio es de : {Promedio}")
    if Promedio > 6:
        print("Felicidades aprobaste el curso")
    else:
        print("Reprobaste tendras que recursar la materia")
