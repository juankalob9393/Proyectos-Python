saldoInicial = 10000
Nip = 1234
Cuenta = 1234

while True:
    print("""          Bienvenido al cajero automatico
          Te comparto el menu de inicio donde tienes que ingresar tu cuenta
          y continuacion tu NIP, si quieres salir del ATM introduce solo **salir** """)
    
    Cuentaing =input("Ingresa tu cuenta------> ")

    if Cuentaing.lower() == "salir":
        break
    elif Cuentaing.lower() != "salir":
        Cuentaing = int(Cuentaing)

    if Cuenta != Cuentaing:
        print ("Cuenta No Existe, Intenta de nuevo")
        continue

    Niping = int(input("Ingresa tu Nip------> "))
    if Nip != Niping:
        print ("Nip Incorrecto, Intenta de nuevo")
        continue

    while True:
        print(f"""¿Que movimiento deseas hacer para la cuenta: {Cuenta}?
            -Consultar Saldo (1)
            -Retirar dinero (2)
            -Depositar dinero (3)
            -Cambiar NIP (4)
            -Salir (5)
            """)
        
        menu1 = (float(input("Que movimiento haras?------> ")))
        if menu1 == 0:
            print("Operacion incorrecta, introduce otra del 1 al 5")
            continue
        elif menu1 > 5:
            print("Operacion incorrecta, introduce otra del 1 al 5")
            continue            

        if menu1 == 1:
            print(f"Tu saldo es de: ${saldoInicial} Pesos")
            continue
        elif menu1 == 2:
            retiro1 = float(input("¿cuanto dinero quieres retirar?---> "))
            if saldoInicial > 0:
                saldoInicial = saldoInicial - retiro1
                print (f"Tu saldo final es de ${saldoInicial} Pesos")
            else:
                print("No tienes suficientes fondos!!")
            continue
        elif menu1 == 3:
            deposito1 = float(input("¿cuanto dinero quieres depositar?---> "))
            saldoInicial = saldoInicial + deposito1   
            print (f"Tu saldo final es de ${saldoInicial} Pesos")
            continue
        elif menu1 == 4:
            NipNuevo = float(input("Cual es tu nuevo NIP?--->"))
            Nip = NipNuevo  
            print (f"Tu nuevo NIP es {Nip}")
            continue
        elif menu1 == 5:
            break      
