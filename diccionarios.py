#estructuras de datos 3 
print("***************Diccionarios*************************")
diccionario ={} #dict vacio

## Diccionarios


"""diccionario = {} #dict vacío

diccionario = {
    "clave":valor, #clave string
    1 : valor #clave numerica,
    (1,2) : valor #clave en tupla
}"""

print("*****************Elementos del diccionario********************")
#creemos un diccionario que simule una libreta de contactos
libreta = {
    "Emanuel" : 5486710,
    "Yessica"   : 2483675,
    "Marilyn"   : 4215876,
    "Yeison"   : 3658741
}
#accedamos al número de paco
print(libreta["Marilyn"])


dic_anidado = {
    "tupla" : (1,2,3,4,5),
    "lista" : [55.2,41.7,658.3],
    "dict"  : {
        1 : "hola",
        2 : "mundo"
    },
    "set": set([3,3.14,4])
}
print("tupla",dic_anidado["tupla"], dic_anidado["tupla"][1])
print("lista",dic_anidado["lista"], dic_anidado["lista"][0])
print("dict",dic_anidado["dict"], dic_anidado["dict"][1])

libreta = {
    "Emanuel" : 5486710,
    "Yessica"   : 2483675,
    "Marilyn"   : 4215876,
    "Yeison"   : 3658741
}


print(libreta.get("Yessica"))

print(libreta.get("rodolfo"))


print("************ adicion de elementos aun diccionario*************")


#creemos un diccionario que simule una libreta de contactos
libreta = {
    "Emmanuel" : 5486710,
    "Yessica"   : 2483675,
    "Marilyn"   : 4215876,
    "Yeison"   : 3658741
}

libreta['rodolfo'] = 8452165
libreta["carlos"]  = 6542138

print("*****************eliminacion de elementos de diccionario**************************")

# diccionario de cuadrados de números
cuadrados = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("antes",cuadrados)
del cuadrados[3]
print("después",cuadrados)


# diccionario con cuadrados y cubos de números
numeros = {
    "cuadrados" : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25},
    "cubos"     : {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
}
print('antes', numeros)
del numeros["cubos"][1]
print('después', numeros)

print("*************usando la funcion POP**************")

print('antes',libreta)
eliminado = libreta.pop('Yeison')
print('después',libreta)
print('elemento eliminado:',eliminado)

print("*************iterar  a traves de un diccionario*********")

"""for i in diccionario:
print(diccionario[i]) #accso al valor a traves de la i_esima clave 
"""

for tel in libreta:
    print(f"{tel}, tel: {libreta[tel]}")


print(libreta)






