import json#importamos la biblioteca de json 

# Ruta al archivo JSON
archivo_json = "C:/Users/Usuario/zully.py/Python_OrtizZully/Dia11/largefile.json"

# Abre y lee el archivo JSON
with open(archivo_json, encoding="utf-8") as archivo:
    datos_json = json.load(archivo)
#todos los eventos encontrados se guardara en esa lista 
eventos=[]
#crear 14 contadores para guardar la cantidad de los eventos 
cantidades=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#para i que contara los datos de json
for i in datos_json:
    #se agregaran los types a la lista de eventos
    eventos.append(i["type"]) 
    #el contador lo que va a hacer es que cuendo encuentre un evento va contar uno por uno
    if i["type"] == "IssuesEvent":
        cantidades[0]+=1
    elif i["type"] == "ForkEvent":
        cantidades[1]+=1
    elif i["type"] == "IssueCommentEvent":
        cantidades[2]+=1
    elif i["type"] == "CommitCommentEvent":
        cantidades[3]+=1
    elif i["type"] == "PullRequestReviewCommentEvent":
        cantidades[4]+=1
    elif i["type"] == "PullRequestEvent":
        cantidades[5]+=1
    elif i["type"] == "WatchEvent":
        cantidades[6]+=1
    elif i["type"] == "ReleaseEvent":
        cantidades[7]+=1
    elif i["type"] == "PushEvent":
        cantidades[8]+=1
    elif i["type"] == "MemberEvent":
        cantidades[9]+=1
    elif i["type"] == "PublicEvent":
        cantidades[10]+=1
    elif i["type"] == "GollumEvent":
        cantidades[11]+=1
    elif i["type"] == "CreateEvent":
        cantidades[12]+=1
    elif i["type"] == "DeleteEvent":
        cantidades[13]+=1
#me eliminara todos los eventos repetidos y me los mostrara 
eventicos= list(set(eventos))
print(eventicos)
#booleanito es verdadero 
booleanito= True
#mientras booleanito es igual a verdadero se hara 
while booleanito == True:
    #se mostrara el menu al usuario 
    print("""
    -----------------------WELCOME TO MENU--------------------------
        1). Crear.
        2). Actualizar.
        3). Eliminar
        4). Revisar
        5). Finalizar
    -----------------------------------------------------------------
    """)
    #en opc se guardara la opcion que eliga del menu 
    opc= int(input("Elige unas de las opciones anteriores: "))
    #si la opcion elegida es uno se hara 
    if opc == 1:
        #se mostrara lo que se va a realizar 
        print("___________Crear_______________")
        #creamos una nueva variable donde se guardara el nombre nuevo  
        new_eventico=str(input("Por favor ingrese el nombre del nuevo evento: "))
        #si nuevo eventivo es igual a los eventos almacenados 
        if new_eventico == eventicos:
            #se le mostrara a los usuarios que ya existe
            print("Lo siento este evento ya esta creado:(( ")
        else:#si no 
            eventicos.append(new_eventico)#nuevos eventos se guardara en eventicos 
            #ingresara la cantidad de evento y se guardara en nuevas cantidades 
            new_Cantidades=int(input("Por favor ingrese la cantidad del evento creado: "))
            cantidades.append(new_Cantidades)
            #se le mostrara que se creo con exito 
            print("El evento fue creado con exito!!! ")
    # si la opcion elegida es dos se hara 
    elif opc == 2: 
        #se le mostrara que se va a realizar 
        print("_______________Actualizar________________")
        #se le mostrara todos los eventos y las cantidades existente para recordarle al usuario
        for i in range(len(eventicos)):
            print(i, eventicos [i], cantidades [i])
        #el digitara el numero del  evento a actualizar 
        cantidades_act = int(input("¿Que evento deseas actualizar? "))
        cant_act2 = int(input("Cuantas cantidades quieres agregar al evento o si le quieres quitar coloca el numero en negativo:  "))
        cantidades[cantidades_act] += cant_act2
        #las cantidades a quitar se le restara y se le sumara
    # si la opcion elegida es tres se hara 
    elif opc == 3: 
        #se le mostrara al usuario lo que se va a realizar 
        print("____________________________Eliminar____________________________________")
        #se le volvera a mostrar lo almacenado 
        for i in range(len(eventicos)):
            print(i, "Nombre del evento :" ,eventicos [i],"// Cantidad del evento: " ,cantidades [i])
        #se creara una variable donde el usuario digitara el numero del evento que desea eliminar 
        delete=int(input("¿Cual es el evento que deseas eliminar?: "))
        eventicos.pop(delete)#se borrara el evento y de una la cantidad
        cantidades.pop(delete)
    #si la opcion ejegida es cuatro se hara 
    elif opc == 4: 
        #se le mostrara que se va a realizar 
        print("_______________Revisar______________")
        #se le mostrara todas las modificaciones que ha realizado el usuario 
        for i in range(len(eventicos)):
            print(i, "Nombre del evento :" ,eventicos [i],"// Cantidad del evento: " ,cantidades [i])
    #si el usuario elegida es cinco se va a realizar 
    elif opc == 5:
        #se le agradecera al usuario por usar este programa 
        print("----Gracias por usar este programa:))---- ")
        #booleanito va a ser falso y se finalizara 
        booleanito=False

#Elaborado por Zully Fernanda Ortiz Avendaño Cc. 1092528097 








                                                                                                                                             