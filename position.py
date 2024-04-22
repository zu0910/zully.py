#nums va a guardar la lista de numeros que va a ingresar el usuario 
nums=input("")
#crear otra variable donde guarda los objetos de la lista 
numeros=list(sorted(set(map(int, nums.split(",")))))
#un contador que empezara desde cero 
cont= 0 
#el numero de target va a estar guardaod con la variable comparate
comparate= int(input(""))
numeros.append(comparate)#agrega el numero a la lista pero como va a quedar de ultimo 
numeros.sort()#utilizamos el sort para que me lo ordene 
#creo otra variable donde eliminara los numeros repetidos de la lista
new_nums= list(set(numeros))
print(new_nums)#le mostrara lo anterior 
#creo un para donde contara desde cero hasta los numeros de la lista 
for i in numeros:
    #el contador va a contar desde 1 
    cont+=1
    #si la lista es igual al numero comparar 
    if i == comparate:
        #resptara un 1 como el contador suma se tiene que igualar para que cuente bien 
        cont-=1
        #Imprimira el numero que ingreso el usuario a comparar 
        print(cont)
        break#finalizar el si 


