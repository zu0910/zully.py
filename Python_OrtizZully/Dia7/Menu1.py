skincare = {
    "123": {"nombre" : "Jabon liquido",
           "precio": 25000,
           "cantidad": 15

           },
    "231": {"nombre": "Crema hidratante",
           "precio": 33000,
           "cantidad": 15
           },
    "312": {"nombre": "Serum",
           "precio": 27000,
           "cantidad": 15
          },
}



carrito = {"product": 0}

menu = True
while menu == True:

    print ("""
    --------------Bienvenido a SKINCARE_STORE-----------------
        Por favor seleccion una opción del menu 
        1). Agrega skincare al carrito
        2). Ver contenido del carrito
        3). Total de la compra
        4). Finalizar compra
    """)
    
    opc = int(input("digite una opcion del menu: "))
    print(skincare)
    if opc ==1:
        comprita=int(input("Cuantos productos de skincare deseas agregar al carro: "))
        if comprita<skincare["123"]["cantidad"]:
            ref=int(input("Ingrese el numero de referencia del producto: "))
            if ref ==123:
                skincare["123"]["cantidad"]-=comprita 
                carrito["product"]+=comprita
        
                print(skincare["123"]["cantidad"])
                print("carrito: ", carrito["product"])
               

        elif comprita<skincare["231"]["cantidad"]:
                ref=int(input("Ingrese el numero de referencia del producto: "))
                if ref ==231:
                    skincare["231"]["cantidad"]-=comprita 
                    carrito["product"]+=comprita

                    print(skincare["231"]["cantidad"])
                    print("carrito: ", carrito["product"])
                    
                    
        elif comprita<skincare["312"]["cantidad"]:
                ref=int(input("Ingrese el numero de referencia del producto: "))
                if ref ==312:
                    skincare["312"]["cantidad"]-=comprita 
                    carrito["product"]+=comprita

                    print(skincare["312"]["cantidad"])
                    print("carrito: ", carrito["product"])
                    

        

        
            

    
        
       