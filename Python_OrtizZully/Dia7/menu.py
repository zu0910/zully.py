cont = 0 
product = {
    "1234": {
        #inventario con la referencia, nombre del producto y el precio
        "name": "Facial soap",#Jabon facial 
        "Price" : 25000,
        
    },
    "2341": {
        "name": "Avocado mask",#Mascarilla de aguacate
        "Price" : 3000,
        
    },
    "3412": {
        "name": "Moisturising cream",#Crema hidratante 
        "Price" : 30000,
        
    },
    "4123": {
        "name": "Serum Vit c",# serum vitamina c 
        "Price" : 23000,
        
    },

}

Price = {
    "1234": 25000,
    "2341": 3000,
    "3412": 30000,
    "4123": 23000,

}

shopping = {}#carrito de compra
totalPrice = ()#precio total 
totalPrice1 = ()
cant = {
    "1234": 15,
    "2341": 15,
    "3412": 15,
    "4123": 15,
    
}#cantidad
quantity = {}
skincare=[]
#mientras el contador no se igual a 5 se hara 
print(product)
menu = True
while menu == True:

    #Le mostrara el menu inicial al usuario 
    print ("""
    ----------------------WELCOME TO SKINCARE_STORE--------------------------
           choose the opction that do you want to select:

           
           1) Add skincares
           2) list skincares
           3) Total cost
           0) Finalize

    """)
    print(shopping) 

    opc = int(input("Choose the opction from the menu: "))
    #si la opcion elegida es uno se hara
    if opc == 1:
        
        code = input("Enter the product reference number from the catalog ")
        shopping[code]=product[code]

        cantL = int(input("Ingrese la cantidad que desees llevar: "))# cant llevar
    if cantL <= cant[code]:
        cant[code]=cant[code] - cantL
        
    
        
        
 
    
        
    if opc==2:
        print(shopping)


    if opc==0:
        print("Gracias por usar el programa:)")
        menu = False
        
#HECHO POR ZULLY ORTIZ  CC: 1092528097 Y FREILER ORTEGA  CC: 1010075774

        



    



    
    



    