#estructura de datos 
num1 = 10
num2 = 20
num3 = 30
num4 = 40
num5 = 50
print(num1,num2,num3,num4,num5)

"""lista=[] #lista vacia
lista[2] =5 #asignación de un valor a una posición
"""
lista =[1,2,3,4]
print(lista)
print(lista[2])

lista[2]=5 #asignación de un valor a una posición 

print('lista original', lista)
lista[2]= 5 #asignación de un valor a una posición 
print('lista modificada', lista)


lista2 = ['a',0,5.14,[1,2,3]]
print(lista2)

print(len(lista2))

print(lista2[0])
print(lista2[1])
print(lista2[2])
print(lista2[3])

print(lista2[3][2])

s='soy un string indexado'
print(s[5],s[8])

#insercion de elementos 

#lista.append(dato)
print('lista antes de insercion:',lista)
lista.append(5)
print('lista luego de insercion:',lista)

#lista+=[dato]

print('lista antes de insercion:',lista)
lista+=[6]
print('lista luego de insercion:',lista)

print('lista antes de insercion:', lista)
lista+=[7,8,9,10]
print('lista luego de inserción:',lista)

#eliminar elementos de una lista

print('lista antes de eliminar un dato:', lista)
del lista[3]
print('lista luego de eliminar un dato:',lista)


lista3=[5,1,2,8,6,4,3,9,10,56,10,9,5,1]

#remove
#lista.remove(dato)

print('lista antes de eliminar un dato:', lista3)
lista3.remove(8)
print('lista luego de eliminar un dato:',lista3)

#pop

lista.pop() #elimina el ultimo dato
lista. pop(5) #elimina el dato en el indice 5
x=lista.pop(4) #elimina el dato en el indice 4 y lo almacena en la variable x
n=lista.pop()#elimina el ultimo dato y lo almacena el la variable n

print('lista antes de eliminar un dato:',lista3)
lista3.pop ()
print('lista luego de eliminar un dato:',lista3)


print('lista antes de eliminar un dato:', lista3)
lista3.pop(0) #eliminemos el primer dato
print('lista luego de eliminar un dato:', lista3)

print('lista antes de eliminar un dato:', lista3)
x=lista3.pop()
print('lista luego de eliminar un dato:',lista3)
print('datoeliminado:',x)

#iteración en una lista

"""for i in range(0,len(lista)):
    lista[i] #acceso a la i_ésima posición de la lista
""" 

#creemos una lista con los numeros del 1 al 15
l =[]#lista vacia
for i in range(1,16):
    l.append(i)
    print(i)


#cremos una lista con los numeros del 1 al 15
l=[] # lista vacia 
for i in range(1,16):
    l.append(i)
    print(1)
    #eliminemos los valores entre 5 y 10
    for i in range(5,11):
        l.remove(i)
    print(l)

"""for i in lista:
    instrucciones  
"""

lista3 =[5,1,2,8,6,4,3,9,10,56,10,9,5,1]
media=0
for i in lista3:
    print(i)#veamos que hay internamente en i
    media+=i #sumamos el dato al acumulado
media/=len(lista3) #dividimos por el total de datos
print("la media de lso datos es :",media)


#indexado negativo

print(lista3)
print('ultimo dato:',lista3[-1])
lista3.pop()
print(lista3)
print('ultimo dato:',lista3[-1])
lista3.pop()
print(lista3)
print('ultimodato:',lista3[-1])

#slicing

#lista[indice_inicial:indice_final:variacion]

texto=['M','O','N','T','Y','','P','Y','T','H','O','N']
print(texto[:])


print(texto[6:10])

print(texto[-12:-7])

print(texto[::-1])

texto[2:8:2]

#similitudes entre string y listas
"""for s in string
intruccion
"""

cadena = 'parangaricutirimícuaro'
for s in cadena:
    print(s)



cadena = 'parangaricutirimícuaro'
for i in range(len(cadena)):
    print(cadena[i])


    


















   
























