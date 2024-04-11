#-----------------------------------------------
#----------DIA 1 CHEAT SHEET PYTHON-------------
#-----------------------------------------------

#Imprimir hola mundo
print("Hola mundooo!!!")

#numero
numerito=1 #nombreVariable = Valor 
print(numerito)#imprimir (variable)
print(type(numerito))#imprimir(tipo(variable))

#Decimal
NumeritoDecimal=1.2 #nombreVariable = Valor
print(NumeritoDecimal)#imprimir (variable)
print(type(NumeritoDecimal))#imprimir(tipo(variable))

#Booleano 
MiBooleanito=True #nombreVariable = booleano
print(MiBooleanito)#imprimir (bool)
print(type(MiBooleanito))#imprimir(tipo(booleano))

#Cadena texto
Texto="Mi Tibu" #nombreVariable = texto
print(Texto)#imprimir (texto)
print(type(Texto))#imprimir(tipo(texto))


#Ingresa por teclado la infomarcion

nombre= str(input("Por favor, Ingrese su nombre"))#nombreVariable = tipo texto (el nombre que ingresara el usuario)
print(nombre)#Imprimir el nombre que ingreso

edad= int(input("Por favor, ingrese su edad"))#Realizamos lo mismo del anterior la diferencia que no va a ser nombre si no edad(numero en entero)
print(edad)#Imprimir la edad que ingreso

#Conversion de tipos de variable
print(int(23.4))#le indique al progroma que me imprimira un numero en entero por ende el numero q ingrese se va a convertir en entero 
print(float(54))#Pasa lo mismo q el anterior, como el tipo q estar en decimal al imprimirlo va  a mostrarun numero en decimal
print(bool(True))#Booleano True(Verdadero)
print(bool(False))#Booleano False(Falso)
print(str("textos"))#Imprimir textos

#Bucles for y while 

a=int(input("por favor ingrese hasta que numeros desees contar"))#El usuario ingresara hasta que numero quiere contar
for i in range (1,(1+a)):#El bucle imprimira del 1 hasta el numero que ingreso el usuario, range crea una secuencia desde uno  hasta a 
    print(i)#imprimira todos los numeros ingresados 

while True: #Mientras el booleano sea verdadero se hara 
    print("""
        1). seguir con el programa
        2). salir del programa 
""")# se le mostrara este pequeño menu al usuario en la pantalla 
    
    opcion=int(input("Por favor ingrese un nuemero del menu"))#depende de la opcion que escoja se hara 
    if opcion==1:#si elige la primera opcion seguira con el programa y se mostrara lo siguiente
        print("funciones")
        
   
        #Funciones 4 tipos
        
        #1
        #definir y llamar funciones con parametro
        
        #Saludar a mi amiga valen 
        def SaludarAmigo(nombre, Apellido):
            print("Hola mi amiga ", nombre , Apellido)
            
        Nombref = "Valen"#cree una varible que guarde el nombre y el apellido de mi amiga
        Apellidof = 'Molina'
        SaludarAmigo(Nombref , Apellidof)#imprimira el nombre y apellido
        
        #2 lo mismo del anterio solo que con mi nombre completo cree una variable que guarde cada nombre y apellido
        
        def MyFullName(fName, sName , fLastname , sLastname):
            print("Mi nombre completo es ", fName, sName , fLastname , sLastname)
            
        NombreF = "Zully"
        NombreS =  "Fernada"
        ApellidoF = "Ortiz"
        ApellidoS = "Avendaño"
        MyFullName(NombreF , NombreS , ApellidoF , ApellidoS)
        
        #3 funcion basica de suma
        
        def suma (a, b, c ):
            return a + b + c
            #defini lo que iba a hacer y le asigne un valor a (a=1, b=2 y c=3)
        resultado = suma ( 1, 2, 3)
        
        print("El resultado de la suma es:", resultado)#imprimira la suma de los numeros
        #resultado 6
        
        #4 funcion media 
        def puntuacion(alum1, alum2, alum3):#a los tres alumnos se le asignara un valor
            suma = alum1 + alum2 + alum3# los valores asignados se dividira en tres 
            return suma / 3
            
        media= puntuacion(7,8,1)
        
        print("La puntuacion de esta clase es:", media)#imprimir media
        
        
        
    if opcion==2:#si el usuario elige la opcion dos terminara con el programa
        print("Gracias por usar este programaXD")
        
        



#Desarrollado por Ortiz Zully - C.C 1092528097