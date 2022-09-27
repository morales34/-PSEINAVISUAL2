#Manejo de archivos 2

#¿Qué es JSON?
#Reglas de la sintaxis
#{ "nombre":"Thanos" }

#Los datos están separados por comas

"""{ 
  "nombre":"Thanos",
  "ocupación":"Destruir la mitad del universo"
}"""

#Los corchetes contienen listas

"""{ 
    "nombre":"Thanos",
    "ocupación":"Destruir la mitad del universo",
    "poderes":[
        "Puede destruir cualquier cosa con un chasquido de dedos",
        "Resistencia al daño", 
        "Reflejos sobrehumanos"
    ] 
}"""

#Es posible tener arreglos de objetos JSON.

"""{
    "Avengers": [

        {
          "nombre" : "Tony stark",
          "A.K.A" : "Iron man",
          "habilidades" : [ "Genio", "Billonario",
                        "Playboy", "Filántropo" ]
        },

        {
          "nombre" : "Peter parker",
          "A.K.A" : "Spider man",
          "habilidades" : [ "Telarañas", "Sentido Arácnido" ]
        }
    ]
}"""

#Lectura de archivos JSON

#Carguemos el archivo que descargamos en la primera línea de código

with open("marvel-cinematic-universe.json") as marvel:
    print(marvel.read())

#Trabajar con datos JSON en Python

import json

with open("marvel-cinematic-universe.json") as marvel:
    data = json.load(marvel)
print(type(data),data)


for k in data['Marvel Cinematic Universe']['Iron Man']:
    print(f"{k} : {data['Marvel Cinematic Universe']['Iron Man'][k]} ")
    #recordemos que debemos usar comillas dobles para usar comillas sencillas 
    #dentro de un string

    sub_diccionario = data['Marvel Cinematic Universe']['Doctor Strange']
print(sub_diccionario)
print(sub_diccionario['release_date'])

#Conversión de datos a JSON

print('lista',json.dumps(['hugo', "paco", "luis"]))


print('tupla',json.dumps(('hugo', "paco", "luis")))

print(json.dumps("Hola"))

print(json.dumps(123))

print(json.dumps(23.572))


print(json.dumps(True))
print(json.dumps(False))

print(json.dumps(None))

with open('doctor_strange.json', 'w') as json_file:
  json.dump(sub_diccionario, json_file) #usamos dump para serializar el dict 
                                        #como archivo JSON


with open('doctor_strange.json', 'r') as salida:
    print(salida.read())



