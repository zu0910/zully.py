# El programa selecciona aleatoriamente un número secreto entre 1 y 100., donde 
#el usuario tiene un total de 10 intentos para adivinar el número secreto. Después 
#de cada intento, el programa dará pistas indicando si el número secreto es mayor o menor
#que la suposición actual del usuario. Si el usuario adivina correctamente, el programa felicitará 
#al jugador y mostrará en cuántos intentos lo logró.
#El programa debe ser amigable y explicar claramente las instrucciones al usuario.

import random#Aleatorio

numero_Secreto = random.randint(1, 100)
#Explicacion del juego
print("""
-------------------ADIVINA ADIVINADOR--------------------------
      OBJETIVO: adivinar un numero del 1 al 100
              -Tendras solo 10 intentos 
      Si te equivocas no te preocupes te dare pequeñas pistas;)
                  
""")
#Para i en rango va contar hasta 10 (donde eso son los numeros de intentos)
for i in range(1, 11):
    #El usuario ingresara un numero 
    num=int(input("Por favor ingrese un numero del 1 al 100"))
    #Si lo adivina a la primera lo felicitara y mostrara los numeros de intentos
    if num == numero_Secreto:
        print("FELICITACIONES DIOS ESTUVO CONTIGO OTRA VEZ", i)
    #Si no le va a mostrar las pequeñas pistas
    else:
        if num < numero_Secreto:
            print("El numero es mayor, Vuelva a intentar!")

        if num > numero_Secreto:
            print("El numero es menor, Vuelvalo a intentar!!!")
            
#Elaborado por Ortiz Zully CC.1092528097