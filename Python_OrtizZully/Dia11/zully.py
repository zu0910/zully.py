import json

# Ruta al archivo JSON
archivo_json = "largefile.json"

# Abre y lee el archivo JSON
with open(archivo_json, encoding="utf-8") as archivo:
    datos_json = json.load(archivo)

print(datos_json)

booleanito= True
while booleanito == True:

    print("""
    -----------------------WELCOME TO MENU--------------------------
        1). Crear.
        2). Actualizar.
        3). Revisar 
        4). Eliminar
        5). Finalizar
    -----------------------------------------------------------------
    """)
    opc= int(input("Elige unas de las opciones anteriores: "))



                                                                                                                                             