#Diseñar un algoritmo que nos calcule la suma de los N primeros numeros pares, es decir, si insertamos un 7, 
#nos haga la suma de 2+4+6+8+10+12+14. 



contador=0
suma=0
n=int(input("Ingrese la cantidad de numeros a sumar: "))
	
while (contador<n) :
    if n % 2==0:
        suma=n+suma
        contador=contador+1
    else:
            if n  % 2==0:
                suma=n+suma
                contador=contador+1
suma=suma+1    
	
print("La suma de los numeros es: ",suma,)




