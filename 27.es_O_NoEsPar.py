#Teniendo en cuenta el algoritmo anterior  (Numeros pares e impares), hacerlo de nuevo, de forma que si se teclea un cero,
#se vuelva a pedir el numero por teclado, (Así, hasta que se teclee un numero mayor que cero), debe decir "El numero es Par".
#o (El numero no es par)



#Hasta que no se digite un numero mayor a cero, no saldra del bucle.

num=int(input( "Por favor digite un numero mayor que 0: "))

while num <= 0:
	num=int(input( "Por favor digite un numero mayor que 0: "))

if num  % 2==0 :
	print( "El numero ingresado es par")
else:
	print( "El numero ingresado no es par")


