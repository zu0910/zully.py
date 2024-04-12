
#1,5,10
#Listado de las monedas que se tendran en cuenta para dar el cambio 
monedas = [10, 5, 1]
booleano=True 
while booleano== True:#Mientras el booleano sea verdadero se hara 
    #Menu principal que se le mostrara al usuario en pantalla 
    print("""
    ================================================================
    ----------------Bienvenidos al cajero---------------------------
    1) Saber el cambio de tu billete
    2) Informacion adicional
    0) Salir del programa 

    ================================================================


""")
    #el ingresara la opcion que desee mirar del menu principal 
    opc=int(input("Ingrese la opcion que deses elegir"))
    #Si opcion es 1 se hara 
    if opc==1:
        #Creamos otro booleano donde se mostrara el cambio del cliente 
        booleano2=True
        while booleano2==True:
            print("Cambio de tu billere")
            money=int(input("Ingrese el numero que le tenemos que dar el cambio: "))
            #Para i en monedas que son las monedas de cambio (10,5,1)
            for i in monedas:
                if money >= i:#si money(cantidad ingresada por el usuario) es mayor o igual a las monedas de la lista 
                    queda = money // i #creamos una variable donde guarde la division la division de numeros enterios con las monedas de la lista
                    print("necesitan " + str (queda) + " monedas de " + str (i) )#Imprimira las cant de monedas 
                    money = money % i #acomoda los residuos de la division 

            #para salir y volver al menu principal el usuario tendra que digitar el numero 1 
            Salir = int(input("Escribe 1 para volver al menu principal: "))
            if Salir==1:
                booleano2=False
    #si el elige la opcion 2 se hara 
    elif opc==2:
       #mostrata la informacion adicional 
       print("""
       Los cambios se daran solo con las monedas 10, 5 y 1 
             si el usuario ingresa una cantidad de 27 se desglosara de esta forma
             2 monedas de 10
             1 modeda de 5
             2 monedas de 1
             el total sera 27 

        Autora: Zully Fernada Ortiz Avendaño 
             Cc.1092528097 

        """)
       #el cliente dara enter para volver al menu principal 
       Enter=input("")
    #Si elige la opcion 3 se saldra del programa
    elif opc ==0:
       break 

    #Elaborado por Zully Fernanda Ortiz Avendaño Cc.1092528097 




       
        



        

    
       




