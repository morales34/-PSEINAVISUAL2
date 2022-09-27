#manejo de archivo en Python

#Control genérico de archivos

#Apertura de archivos con open
#f = open("nombre_archivo", "modo")
file = open('Frankenstein.txt','r+')
print(file, type(file))

#Lectura de archivos
print(file.read())

#la función read extrae toda la información del archivo
#por este motivo debemos volverlo a abrir, de lo contrario
#file.readlines() nos entregará una lista vacía
file = open('Frankenstein.txt','r+') 
lineas = file.readlines()
print(type(lineas),lineas)

stop = 0 #usaremos una variable para contar las líneas e interrumpir el ciclo
for l in lineas:
    print(l.split(" ")) #creamos una lista por cada línea cortando por los espacios: " "
    stop += 1
    if stop==5: # Romperemos la ejecución luego de 5 iteraciones
        break   # para hacer más simple la visualización de la salida
                # ¿Qué pasaría si eliminas este condicional?

#Cierre de archivos

file.close() #liberamos la memoria

#Creación de un archivo utilizando el modo escritura

archivo = open('numeros.txt','w')
archivo.write("cuadrados y cubos de los números del 1 al 15\n")
for i in range(1,16): #es importante añadir el salto de línea al final de cada write
    archivo.write(f'{i}^2 = {i**2}, {i}^3 = {i**3}\n') 
archivo.close()

#Leamos el archivo que creamos

resultado = open('numeros.txt','r')
print(resultado.read())
resultado.close()

#También, si queremos, podemos visualizarlo línea por línea usando el ciclo for

texto = open('numeros.txt','r')
for l in texto.readlines():
    print(l) 
texto.close()

#Uso de la sentencia with

"""with operación as variable:
    instrucciones"""

with open('numeros.txt','r') as texto:
    for l in texto.readlines():
        print(l) 



