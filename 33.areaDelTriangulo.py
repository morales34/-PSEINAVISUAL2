#Desarrollar un algoritmo que me de un menu de opciones.
# A. El valor del area de un trialgulo, dada la base y la altura
# B. El valor de la base de un triangulo, dada la altura y el area
# C. El valor de la altura, dada la base y el area
#Dependiendo de la opcion selecionada, A, B, C se ejecutara la opcion correspondiente

print("Observa las siguientes opciones que te ofrece el programa: ")
print("a.El valor del area de un trialgulo, dada la base y la altura")
print("b.El valor de la base de un triangulo, dada la altura y el area")
print("c.El valor de la altura, dada la base y el area")

nes=str(input("Introduce la opcion que necesitas: "))

if nes== "a":
	base=int(input("Introduce el valor de la base del triangulo: "))
	altura=int(input("Introduce el valor de la altura del triangulo: "))
	area=base*altura/2
	print("El area del triangulo es: ",area)

elif nes=="b":
	altura=int(input("Introduce el valor de la altura del triangulo: "))
	area=int(input("Introduce el valor del area del triangulo: "))
	base=area*2/altura
	print("La base del triangulo es: ",base)

elif nes=="c":
	base=int(input("Introduce el valor de la base del triangulo: "))
	area=int(input("Introduce el valor del area del triangulo: "))
	altura=area*2/base
	print( "La altura del triangulo es: ",altura)
else:
	print("Opcion Incorrecta escoga entre A,B,C")


