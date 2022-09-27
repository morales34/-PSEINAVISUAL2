#Diseñar un algoritmo que nos calcule la suma de los N primeros numeros pares, es decir, si insertamos un 7, 
#nos haga la suma de 2+4+6+8+10+12+14. 


num=int(input( "Ingrese la cantidad de numeros a sumar: "))
contador=0
suma=0
	
while  contador <= num:
    suma=suma+contador
    contador=contador+1
	
	
print( "La suma de los numeros es: ",suma,)

