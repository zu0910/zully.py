import secrets#numeros aleatorios 
import string#libreria que almacena diferentes tipos de datos como letras, numeros, caracteres especiales entre otras 

Booleanito2=True
while Booleanito2==True: 
    #Mostrar menu principal
    print("""
    ===================================================
          ---------------MENU PRINCIPAL---------------
               1).Numeros primos
               2).informacion adicional de primos
               3).Contraseñas aleatorias
               4).informacion adicional de contraseñas
               0).Salir
    ===================================================
    """)
    #Digitar un numero del menu principal
    opc=int(input("Ingrese un numero para ir a la opcion deseada: "))
    #Si la opcion es 1
    if opc == 1:
        booleanito=True
        while booleanito==True:
            countable=0
            Usuario =int(input("Escribe el numero que deseas saber si es primo: "))
            #para i en rango desde una, hasta la cant que el usuario ingreso, pasos de uno
            for i in range(1,Usuario+1,1):
                if Usuario % i == 0:#si la cant que ingreso el usuario la division modular el residuo es 0
                    countable=countable+1#el contador la a contar uno
            #si el contador solo llega hasta dos el numero va ser primo
            if countable==2:
                print("Este numero es primo")
            else:
                print("Este numero no es primo")
            #para salir y volver al menu principal el usuario debe digitar 1
            Salir = int(input("Escribe 1 para volver al menu principal: "))
            if Salir==1:
                booleanito=False
    elif opc ==2:#si el elige la opcion dos se hara 
        print(""" Un numero primo es aquel que solo es divisible 1 y por si mismo.
              Autora: Zully Fernanda Ortiz Avendaño
              Cc. 1092528097
              """)#mostrara la informacion adicional

        Enter=input("")
    #si el elige la opcion 3 se hara 
    elif opc ==3:
        booleanito3=True
        while booleanito3==True:

            print("Generador de contraseñas")
            #string es la biblioteca donde esta guardada los datos
            LetrasM=string.ascii_uppercase#letras mayusculas
            LetrasMi=string.ascii_lowercase#letras minuscula
            Numeros=string.digits#numeros
            Especiales=string.punctuation#los caracteres especiales
            
            SumaTotal=LetrasM+LetrasMi+Numeros+Especiales#mostrara todas las letras, numeros y caracteres guardados 
            #el usuario ingresara la cantidad que quiere que la contraseña quede 
            CantidadDigitos=int(input("Ingrese la cantidad de digitos que quiere que tenga su contraseña: "))
            
            Vacio=""
            for i in range(1,1+CantidadDigitos,1):#para i en rango desde uno hasta la cantidad de digitos que ingreso el usuario con pasos 1
                Vacio+="".join(secrets.choice(SumaTotal))#se mostrara la contraseña creada 

                if i==CantidadDigitos:
                    print(Vacio)#se mostrara la contraseña final

            Salir = int(input("Ingrese el numero 1 para volver al menu principal: "))#para salir y volver al menu principal va a digitar 1
            if Salir==1:
                booleanito3=False
    
    elif opc ==4:#informacion adicional de contraseña segura
        print("""
    Las contraseñas seguras es una contraseña que otras personas no pueden determinar facilmente adivinandola 
    o utilizando programas automaticos.
              Autora: Zully Fernanda Ortiz Avendaño 
              Cc. 1092528097

    """)

        Enter=input("")
    #si el usuario elige el numero 0 se hara 
    elif opc ==0:
        break#finalizar programa
#Elaborado por OrtizZully Cc. 1092528097