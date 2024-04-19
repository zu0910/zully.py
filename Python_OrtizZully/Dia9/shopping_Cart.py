# -----------------------------------------------------------
# -----------------SHOPPING CART-----------------------------
#------------------------------------------------------------
#Lista donde se guardara los nombres de los productos 
nameP= []
#Lista donde se guardara los precios de los productos 
priceP=[]
#Lista donde se guardara la cantidad de cada producto 
quantityP=[]
#booleanito va ser verdadero 
booleanito = True
#Mientras booleanito sea verdadero se hara:
while booleanito == True:
   #Se mostrara un mini menu con las siguiente opciones
    print("""
    ------------------------------- SHOPPIGN CART --------------------------------
        HERE YOU CAN ENTER THE NAME, PRICE AND THE QUANTITY OF THE SHOOPING CART 

        1). Add products at shooping cart.
        2). Show the shooping cart
        3). Close shopping cart
          
    -------------------------------------------------------------------------------
    """)
    #depende de la opcion que el usuario ingrese se hara:
    opc = int(input("Select one of the options from the menu above: "))
    #Si elige la opcion uno se hara:
    if opc == 1:
        #Primero le preguntara cuantos productos quiere agregarle al carrito de compra
        print("")
        cant_products= int(input("How many products you wants to add to the cart: "))
        print("")
        #para i(shop) que va a contar la cantidad de producto que el usuario ingreso, hasta que no llegue al tope no va a dejar de mostrarle las siguientes preguntas
        for shop in range(cant_products):
            print("")
            #El usuario va ingresar el nombre del producto 
            name= str(input("Please add the name of the product: "))
            #El nombre ingresado se guardara a la lista nameP(nombre de producto)
            nameP.append(name)
            print("")
            #El usuario ingresara el precio del producto 
            price= int(input("Please add the price of the product: "))
            #El precio ingresado se guardara en la lista pricep(Precio de producto)
            priceP.append(price)
            print("")
            #por ultimo le preguntara la cantidad del producto 
            quantity= int(input("Please add the quantity of the product: "))
            #y esa cantidad se guardara a la lista de quantityP( cantidad de producto )
            quantityP.append(quantity)
            
    #si elige la opcion dos se hara 
    elif opc == 2: 
        #Para i en rago contara de cero hasta nameP(coloquye un nombre de la lista ya que como fin todos los productos se guardaron con una funcion y se mostrara los otros )
        for i in range(0,len(nameP)):
            print("List of all products added of shopping cart : " 
                  " Name: ", nameP[i] , " Price: ", priceP[i], " Quantity: ", quantityP[i]) #imprimira todos los nombres, precios y cantidades de productos agregado por el usuario 
    #si la opcion elegida es tres se hara
    elif opc == 3:
        #finalizara el programa 
        print("THANKS FOR COMING")#se le agradecera por venir 
        print("HAVE A GOOD DAY, SEE YOU :))) ")# y le deseara un buen dia 
        booleanito = False#mientras booleanito es igual a falso terminara el programa 

#Elaborapo por Zully Fernanda Ortiz Avendaño Cc. 1092528097
