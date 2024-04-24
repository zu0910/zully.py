import json

with open('large-file.json',encoding="utf-8") as openfile:
    miJSON= json.load(openfile)
#print(type(miJSON))
'''
for i in range (5):
  print(miJSON[i])
'''
crearEventos=[]
for i in range (len(miJSON)):
    if(miJSON[i]['type']=='CreateEvent'):
        crearEventos.append(miJSON[i])

#print(crearEventos[5]['actor']['id'])

for q in range (5):
    print("#######################")
    print("#### Evento # ",q+1 ,"##")
    print("#######################")
    print("ID: ",crearEventos[q]['id'])
    print("Tipo:",crearEventos[q]['type'])
    print("Actor:")
    print("------- ID:",crearEventos[q]['actor']['id'])
    print("------- login:",crearEventos[q]['actor']['login'])
    print("------- gravatar_id:",crearEventos[q]['actor']['gravatar_id'])
    print("------- url:",crearEventos[q]['actor']['url'])
    print("------- avatar_url:",crearEventos[q]['actor']['avatar_url'])

crearEventos[0]['id']=256
crearEventos[0]['login']=256
crearEventos[0]['gravatar_id']=256
crearEventos[0]['url']=256
crearEventos[0]['avatar_url']=256
with open("eventos.json","w") as outfile:
    json.dump(crearEventos,outfile)