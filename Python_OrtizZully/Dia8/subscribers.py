#se guardara todos nombre de usuario que el cliente ingrese al programa 
usuario =[]
#Se guardara todas las contraseña que cree el usuario 
contraseña = []
#La cantidad de dinero que ingresara el cliente se guardara en esa variable 
dineroTotal=0
#Costo de la suscipcion 
costo_Suscripcion= 20000
#Iniciacion del programa
booleanito= True #Booleanito es verdadero
#Mientras booleanito sea verdadero se hara: 
while booleanito == True:
#Se le mostrara al usuario el menu principal 
    print("""
    ----------------MENU PRINCIPAL--------------------
          
        1) Iniciar sesion 
        2) Crear cuenta
        3) Añadir dinero a la cuenta
        4) Comprar suscripcion
        0) Finalizar 
          
    """)
    opc= int(input("Ingrese una opcion del menu anterior: "))#El usuario podra ingresar unas de las opciones que se le mostro del menu principal

    if opc ==1: # Si la opcion elegida es uno se hara 
        print("____________INICIAR SESION________________")
        sesionU = input("Ingrese un usuario: ")#la variable sesionUsuario se guardara el nombre de usuario que el cliente ingreso en la opcion dos
        if sesionU in usuario: #Si el nombre que ingreso en sesionUsuario esta dentro de la lista de usuarios 
            print("Usuario correcto")#Imprimira que el usuario es correcto 
            sesionC = input("Ingrese la contraseña del usuario: ")#la variable sesionContgraseña se guardara la contraseña que el usuario creo en la opcion dos 
            if sesionC in contraseña:# Si la contraseña que creo en sesionContraseña esta dentro de la lista contraseñas
                print("Contraseña correcta")#Imprimira que la condicion es correcta
            else:
                print("Lo siento este no fue la contraseña que creaste")#Si la contraseña no concuerda con la contraseña creada se le hara saber al usuario 
        else: 
            print("Lo siento este no fue el usuario que creaste")#Pero si el usuario que ingreso no esta en la lista guardada se le hara saber al cliente 
    #Si la opcion elegida es dos se hara
    elif opc ==2:

        nombre = input("Por favor ingrese su usuario: ")#El cliente creara su nombre de usuario y ese se guardara en la variable nombre 
        usuario.append(nombre)#usuario es el nombre de la lista donde se guarda el nombre creado por el usuario 
        password = input("Por favor ingrese su contraseña de su usuario: ")#El cliente creara su contraseña y se guardara en la variable password
        contraseña.append(password)#contraseña es la lista donde se guardara la contraseña que el usuario creo
  
    elif opc ==3:

        dinero= int(input("¿Cuanto dinero deseas añadir a la cuenta?: "))
        dineroTotal += dinero 
        print(dineroTotal)

    elif opc == 4:
        print("__________________COMPRAR DE SUSCRIPCION______________________")
        print("Recuerde que solo tienes recargado a la cuenta: ", dineroTotal )
        print("Cada suscripcion tiene costo de: ", costo_Suscripcion)
        
        sn = str(input("¿Deseas comprar una suscripcion?: (yes/not)"))
        if sn =="yes":
            cant_años= int(print("¿Cuales años deseas comprar?"))
            if cant_años*cant_Sus>dineroTotal:
                

                cant_Sus= int(input("¿Cuantas suscripciones deseas comprar?: "))
                Costo_Compra=costo_Suscripcion*cant_Sus

                if dineroTotal >= costo_Suscripcion:
                    dineroTotal -= costo_Suscripcion
                    print("La compra se hizo con exito")
                else:
                    print("Lo siento no se pudo completar la comprar por falta de plata")

            
            









        




