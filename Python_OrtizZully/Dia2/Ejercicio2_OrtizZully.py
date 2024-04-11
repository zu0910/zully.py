#1. Al inicio, el programa dará la bienvenida y explicará la naturaleza de la Secuencia de Fibonacci, donde solicitará al usuario ingresar un valor entero "n",
# representando hasta qué término de la secuencia se generará. Aquí mostrará la secuencia de Fibonacci hasta el enésimo término ingresado por el usuario. Luego, 
#preguntará si el usuario desea continuar o salir, donde si se decide salir, el programa se detendrá; de lo contrario, se repetirá el proceso.

#Secuencia de Fibonacci
#mientras el booleano sea verdadero hara 
bool = True
while bool:
#le dara la bienvenida al usuaruo y le explicara como se lleva a cabo la secuencia e fibonacci
    print("----------BIENVENIDO A LA SECUENCIA DE FIBONACCI--------------")
    print("""
    EXPLICACION DE LA SECUENCIA DE FIBONACCI:
        Fibonacci se trata de una secuencia infinita de números naturales; a partir del 0 y el 1, se van sumando a pares, 
        de manera que cada número es igual a la suma de sus dos anteriores
        0,1,1,2,3,5...
        0+1=1
        1+2=3
        3+2=5....
    """)
    cant=int(input("Por favor ingrese cuantos numeros desees generar"))#El usuario ingresara un numero entero, depemde de ese numero se hara lo siguiente
    #tres variables
    a = 1
    inicioFi = 0 #primer termino de la secuencia 
    FinalFi = 1 #segundo termino de la secuencia
    #se ejecutara las siguientes funciones
    while a <= cant:
        if a%2 == 1:
            print(inicioFi)

            inicioFi = inicioFi + FinalFi

        else: 
            print(FinalFi)

            FinalFi = FinalFi + inicioFi

        a = a + 1
        #Indicaciones de volver a repetir el programa o finalizarla 
    num=int(input("""
    1). Repetir el programa 
    2). Salir del programa
    """))
    
    if num==1:
        print("-----SEA BIENVENIDO OTRA VEZ AL PROGRAMA-----")

    elif num==2:
     break
    
    




    # Desarrollado por Zully Ortiz CC 1092528097