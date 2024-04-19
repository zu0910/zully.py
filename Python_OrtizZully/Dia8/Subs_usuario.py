#se guardara todos nombre de usuario que el cliente ingrese al programa 
usuario =[]
#Se guardara todas las contraseña que cree el usuario 
contraseña = []
#La cantidad de dinero que ingresara el cliente se guardara en esa variable 
dineroTotal=0
#Costo de la suscipcion 
costo_Suscripcion= 20000
#todos los nombre de los amigos se guardaran en esa lista
amix=[]
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
        5) Regalar una suscripcion a un amigo
        0) Finalizar 
          
    """)
    opc= int(input("Ingrese una opcion del menu anterior: "))#El usuario podra ingresar unas de las opciones que se le mostro del menu principal

    if opc ==1: # Si la opcion elegida es uno se hara 
        print("_INICIAR SESION_")
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
    #Si la opcion elegida es tres se hara 
    elif opc ==3:

        dinero= int(input("¿Cuanto dinero deseas añadir a la cuenta?: "))#en la variable dinero se guardara la cantidad de dinero que el cliente desea guardar en su cuenta 
        dineroTotal += dinero #el dinero que ingreso el cliente se guardara en la variable dinero total 
        print(dineroTotal)#imprimire la cantidad guardada
    #Si la opcion elegida es cuatro se hara 
    elif opc == 4:
        print("_COMPRAR DE SUSCRIPCION_")#Se le mostrata al usuario que se va hacer
        print("Recuerde que solo tienes recargado a la cuenta: ", dineroTotal )#Se le cordara el monto que tiene guardado en su cuenta
        print("Cada suscripcion tiene costo de: ", costo_Suscripcion)#Tambien se le recordara el precio que tiene la suscripcion
        sn =str(input("¿Deseas realizar la compra de suscripcion? (yes/not):  "))#Se le preguntara al usuario si desea comprar una suscripcion 
        if sn == "yes":#si la respuesta es yes(si) se hara
            cant_años=int(input("¿Cuantos años deseas tener la suscripcion?: "))#se le preguntara al usuario cuando años deseas mantener la suscripcion y lo que ingresara se guarda en la variable cant_años(cantidad de años)
            costo_Suscripcion*cant_años<=dineroTotal#se multiplicara el costo de suscripcion por la cantidad de años que ingreso el usuario, tiene que ser menor o igual del dinero acumulado del usuario para poder comprarla 
            years=int(input("¿Desde que año deseas activar la suscripcion?"))#se le preguntara desde que año desea tener la suscripcion para activarla y se guardara en la variable year(año)
            if years > 1990:#si años va ser mayor a 1990, los años que el ponga debe ser mayor a ese, si no es no dejara continuar con la compra 
                final=cant_años+years# se sumara la cantidad de años con los años que desea la compra y se guardara en la variable final
                dineroTotal-=cant_años*costo_Suscripcion#se le restara el dinero que ingreso con el total de la cantidad de año con el costo de la suscripcion
                print("Tu suscripcion caduca en el año ",final)#se le mostrara al usuario el año que finalizara la suscipcion
                print("Ahora tienes", dineroTotal, "en tu cuenta.")#Imprime el dinero que le queda al usuario
                
            else:
                if years < 1990:
                    print("Lo siento el año que ingresaste no es valido")
                    
                
        else:#si la opcion va ser no se le mostrara al usuario lo siguiente 
            
            print("Okey, have a good day XD")
    #Si la opcion elegida es cinco se hara     
    elif opc == 5:
        print("______REGALAR UNA SUSCRIPCION_____")#Imprimira al usuario lo que se va hacer 
        print("Recuerde que solo tienes recargado a la cuenta: ", dineroTotal)#se le recordara al usuario el monto que tiene guardado en su cuenta
        print("Cada suscripcion tiene un costo de: ", costo_Suscripcion)#y tambien se le recordara el costo de cada suscripcion
        sn= str(input("¿Deseas regalarle una suscripcion a algunos de tus amigos? (yes/not) :"))#se le preguntara al usuario si desea regalar una suscripcion 
        if sn == "yes":#si la rspuesta es yes(si) se hara 
            cant_años = int(input("¿Por cuantos años deseas regarlar la suscripciona unos de tus amigos?: "))#se le preguntara al usuario por cuantos años desea regalar la suscripcion se guardara en la variable cant_años(cantidad de años)
            if costo_Suscripcion*cant_años <= dineroTotal:# se multiplara el costo de suscripcion por la cantidad de años ingresada y se verificara si el usuario cuenta con la cantidad suficiente
                friends = input("Ingrese el nombre del amigo que desees regalarle la suscripcion: ")#se ingresara el nombre del amigo y se guardara en la variable friends
                amix.append (friends)#el nombre ignresado se guardara en la lisra de amix
                dineroTotal -= costo_Suscripcion*cant_años#aqui se le va a restar al usuario la compra por el dinero total q tiene en la cuenta
                print("Has regalado una suscripcion de ", cant_años, "años a ", friends)#se le mostrara los años y  el nombre del amigo que le regalo la suscripcion 
                print("Ahora tienes", dineroTotal, "en tu cuenta.")#Imprime el dinero que le queda al usuario
            else:
                print("Lo lamento, no cuentas con el dinero suficiente para regalar una suscripcion")#si el usuario no cuenta con el dinero sufiente se le hara saber 
        
    #si la opcion elegida es 0 se hara 
    elif opc == 0:
        print("GRACIAS POR ELEGIRNOS, VUELVA PRONTO")#finalizara el programa
        booleanito=False#al ser booleanito falso se cerrara el programa 
        
    #Elaborado por Zully Fernanda Ortiz Avendaño Cc. 1092528097