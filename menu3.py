from os import system

carros = {
    "C01":{
        "Id":"C01",
        "marca":"Porsche",
        "modelo":"911GT",
        "cilindraje":2500,
        "estado":"Usado",
        "año":2017,
        "precio":42000,
        "cantidad": 3
    },
    "C02":{
        "Id":"C02",
        "marca":"BMW",
        "modelo":"X1",
        "cilindraje":1400,
        "estado":"Usado",
        "año":2021,
        "precio":28000,
        "cantidad": 3
    },
    "C03":{
        "Id":"C03",
        "marca":"FERRARI",
        "modelo":"365P",
        "cilindraje":4390,
        "estado":"Usado",
        "año":1965,
        "precio":20000000,
        "cantidad": 3
    }
}

articulo = []
carrito = {}
cont = 0
total = 0
total1=0

print("""
--------BIENVENIDO AL CONCESIONARIO TIBUYANO-------
¿Que deseas hacer?
1. Revisa los autos disponibles.
2. Agg los autos a comprar.
3. Revisa el contenido que tienes de compra.
4. ¿Desea terminar el programa?.
---------------------------------------------------
""")

sel=0 # le damos valor a nuestra variable sel-eccion para asi poder ejecutarla en nuestro while
while sel!=3:  # hacemos un while para hacer un bucle a nuestras tres opciones
    system("cls") # colocamos un limpiaar pantalla
    print("""
    -----BIENVENIDO AL CONCESIONARIO TIBUYANO----------
    ¿Que deseas hacer?
    1. Revisa los autos disponibles y añade los que quieras al carrito.
    2. Revisa el contenido que tienes en carrito y tu total de compra.
    4. ¿Desea terminar el programa?.
    ---------------------------------------------------
    """)
    
    sel=int(input("Digita el numero de lo primero que deseas hacer:\n")) # Le pedimos al usuario que por favor ingrese el numero de alguna de nuestras opc.
        
    if sel == 1:

        for i in carros:
            print(carros[i])

        cantidad = int(input("Cuantos productos va a comprar\n"))

        for i in range(0,cantidad):

            articulo = (input("Elija un artículo digitando su código\n"))
            carrito[articulo] = carros[articulo]
            total += carros[articulo]["precio"]
            
 

        input("Para continuar presione enter.")
    
    if sel == 2:
        print(carrito)
        print("El total de compra es: ", total)
       

        input("Para continuar presione enter.")
    
    if sel == 3:

        input("Para continuar presione enter.")