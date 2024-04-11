#Este programa simula un juego interactivo en el que el usuario debe adivinar un número 
#secreto elegido aleatoriamente por el programa. El número secreto está en el rango de 1 a 100.
#Después de cada intento del usuario, el programa proporciona pistas indicando si el número secreto
#es mayor o menor que la suposición actual. El objetivo es adivinar el número secreto en la menor 
#cantidad de intentos posible.

import random#aleatorio
#variable que crara los numeros aleatorias del 1 al 100

aleatorio_num = random.randint (1, 100)
#mientras sea verdadero se hara 
while True:
   #El usuario ingresara un numero entero del 1 al 100
   
   num = int(input("Por favor ingrese un numero del 1 al 100"))

   if num == aleatorio_num:#si el numero que ingreso es igual al numero aleatorio
      print("FELICIDADES!!! Tuviste mucha suerte")#Dios estaba con el 
      break 
   else:
       #Si no adivino el programa le dara algunas pistas hasta que lo adivine 
      if num < aleatorio_num:
        print("El numero es mayor, vuelvalo a intentar")
      if num > aleatorio_num:
         print("El numero es menor, vuelvalo a intentar")
         
#Desarrolado por Ortiz Zully CC. 1092528097