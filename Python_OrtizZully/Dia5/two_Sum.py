def dossumas(numbers, target): #funcion
    a = {}#numeros almacenados 

    for i, number in enumerate(numbers):
        c = target - number#c es una variable donde se guardara lo siguiente
        if c in a:
            return [a[c], i]
        a[number] = i
    return print("No hay números en la lista ")

print("SUM")
print("")

nums = [2,7,11,15,3,4]#numeros almacenados en una lista

target=int(input("Ingrese un número: "))#el ususario ingresa el numero que desee sumar 

print("")
print(nums)
print("")
print(dossumas(nums, target)) #la posicion que esta el numero que ingreso el usuario 

#Elaborado por Zully Fernanda Ortiz Avendaño Cc. 1092528097