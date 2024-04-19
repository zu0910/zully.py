#crear tres frutas con su precio y cantidad
fruits = [("strawberry", 2.34, 10), ("watermelon",0.25,25), ("pineapple", 0.51 , 4)]
result = []
#Convertir los nombres de las frutas en mayusculas se utiliza .upper
capitalized_Name = [fruit.upper() for fruit, price, cant in fruits]
print(capitalized_Name)
#Como lo explico pedro en la lista
for i in fruits:

    result.append(i[0].upper())
    if len(result)>2:

        print(result)

#mostrar la fruta que tenga el precio menor a 0.50 

cheaper = [fruit for fruit, price, cant in fruits if price < 0.50]
print(cheaper)

#mostrar el numero mayor de las frutas disponibles 
largest_num = max(fruits, key=lambda x: x[2]);
print(largest_num)

#orden decreciente, el valor de la fruta en stock se calculara multiplicando el número de frutas
fruits.sort(key=lambda fruit: fruit[1]*fruit[2], reverse = True)
for fruit in fruits:
    name, price, cant = fruit
    print(f"Name: {name}, Price: {price}, Cant: {cant}, total_Stock: {price*cant}")