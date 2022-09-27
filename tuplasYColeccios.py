#estructura de datos 2 
#tuplas 
tupla =(1,2,3,'a','b','c')
tupla=("manzana",1234,"fresa",[1,2,3,4,5],(5,9,7,5,4))
print(tupla)

#longitud de la tupla 
print(len(tupla))
print(type(()))
print(type((1)))
print(type((1,)))

#inmutabilidad
print(tupla[1])


#iteracion en tuplas 

#creemos una tupla
tupla = (1,2,3,4,5,9,6,4,7,11,55,24,85,34)
#recorramos con range
for i in range(len(tupla)):
    print(tupla[i], end=" ")


#creemos una tupla
tupla = (1,2,3,4,5,9,6,4,7,11,55,24,85,34)
#recorramos iterando directamente sobre la tupla
for i in tupla:
    print(i, end=" ")



# sets 

conjunto={}#set vacio
conjunto={1,3,'banana'}

conjunto ={1121,'a',85,(1,2,3),(45.51,85,6)}
print(type(conjunto),conjunto)

#no se permiten duplicados 

c={1,2,3,1}
print(c)

#obtener la longitud de un set 
print(f'{c} tiene{len(c)} elementos')
print(f'{conjunto} tiene{len(conjunto)} elementos')

#añadir elementos a un conjunto
#utilizando el metodo ADD

#creamos un set
set1=set()
print("set en blanco:")
print(set1)

#añadimos elementos y una tupla al set 
set1.add(8)
set1.add(9)
set1.add((6,7))

print("/nSet luego de añadir los numeros del 1 al 5 :")
print(set1)

#uso del metodo UPDATE

#añadimos elementos al set
#usando la funcion update
set1=set([4,5(6,7)])
print('Set inicial/n', set1,sep="")
set1.update([10,11])
print("/nSet luego de añadir elementos con update:")
print(set1)

#Eliminacion de elementos del conjunto

#Utilizando el metodo REMOVE o el metodo DISCARD

#Creamos un seet
set1=set([1,2,3,4,5,6,
          7,8,9,10,11,12])
print("Set inicial:")
print(set1)


#Removemos elementos 
#usando remove()
set1.remove(5)
set1.remove(6)
print("/nSet luego de eliminar 2 elementos:")
print(set1)

#usando discard()
set1.discard(8)
set1.discard(9)
print("\nSet luego de eliminar 2 elementos: ")
print(set1)

# usando un ciclo
for i in range(1, 5):
    set1.remove(i)
print("\nSet luego de eliminar elementos con un ciclo: ")
print(set1)

#Accedeer a un cojunto
# Creating a set
set1 = set() #set vacío
for i in range(0,100,10):
    set1.add(i)
print("set inicial")
print(set1)
  
# acceso mediante ciclo for
print("\nElementos del set: ")
for i in set1:
    print(i, end=" ")
print()  
# Verificar si un elemento pertenece
#usando el operador in
print("10 en set?: ",10 in set1)
print("15 en set?: ",15 in set1)









