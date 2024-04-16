numeros = []#el usuario ingresa la lista de numeros

zully = int(input("Cantidad de valores "))
assert 0< zully <300 ,"ERROR la cantidad supera el rango"
for i in range(0,zully):
    numeros.append(input("Ingrese los numeros de la lista "))
    
    numerito= list(set(numeros))
    numerito.sort()#sort ordenara los numeros que agrego a la lista 

print(numerito)#imprimir todos los numeros egresados sin repeticiones y ordenados 

#Elaborado por Zully Fernanda Ortiz Avendaño Cc. 1092528097
               


