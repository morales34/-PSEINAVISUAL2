#manejo de archivo 3 

#Archivos CSV
"""nombre,edad,sexo
'Hugo',35,'M'
'Luisa',,'F'
'Paco',24,'M'"""

#Lectura de archivos

import csv

cabecera = []
registros = []
with open('starwars_characters.csv', 'r') as csvfile:
    lector = csv.reader(csvfile)

    #para sacar la cabecera usamos la función next
    cabecera = next(lector)

    # extraemos cada registro con un ciclo for
    for fila in lector:
        registros.append(fila)
    
    print('total de registros encontrados', lector.line_num) 

print('cabecera: ', cabecera)
print('primeros 5 registros')
for i in range(5):
    print(registros[i])

#Escritura a un archivo CSV

cabecera = ['Nombre', 'Apellido', 'Carrera', 'Semestre','Promedio']

datos = [['Paco','Peralta','Psicología',8,4.0],
         ['Gustavo','Lopez','Física',5,3.8],
         ['Rosario','Márquez','Medicina',9,4.7],
         ['Roberto','Florez','Ing. Sistemas',7,3.5]]

with open('notas_universidad.csv','w') as csvfile:
    escritor = csv.writer(csvfile)

    #escritura de la cabecera
    escritor.writerow(cabecera)
    
    #escritura de registros
    escritor.writerows(datos)


#Verifiquemos el archivo:

with open('notas_universidad.csv','r') as salida:
    print(salida.read())


