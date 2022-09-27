#Diseñar un algoritmo que pida por teclado tres numeros, si el primero es negativo,
# debe imprimir la multiplicacion de los tres y si no lo es, imprimir la suma.


	
num1=int(input( "Introduce el primer numero: "))
	
num2=int(input( "Introduce el segundo numero: "))
	
num3=int(input("Introduce el tercer numero: "))
	
	
if num1<0:
    print("El resultado es: ",num1*num2*num3)
else:
	print("El resultado es: ",num1+num2+num3)


