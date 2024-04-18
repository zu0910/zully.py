usuario =[]
contraseña = []
dineroTotal=0
booleanito= True
while booleanito == True:

    print("""
    -----------------------------------------
        1) Iniciar sesion 
        2) Comprar cuenta
        3) Añadir dinero a la cuenta
        4) Finalizar 
    """)
    n= int(input("Ingrese una opcion del menu anterior: "))

    if n ==1: 

        print("INICIAR SESION")
        sesionU = input("Ingrese un usuario: ")
        if sesionU in usuario: 
            print("Usuario correcto")

            sesionC = input("Ingrese la contraseña del usuario: ")
            if sesionC in contraseña:
                print("Contraseña correcta")

            else:
                print("Lo siento este no fue la contraseña que creaste")
        else: 
            print("Lo siento este no fue el usuario que creaste")

    elif n ==2:

        nombre = input("Por favor ingrese su usuario: ")
        usuario.append(nombre)
        password = input("Por favor ingrese su contraseña de su usuario: ")
        contraseña.append(password)

    elif n ==3:
        dinero= int(input("¿Cuanto dinero deseas añadir a la cuenta?: "))
        dineroTotal += dinero 
        print(dineroTotal)



        




