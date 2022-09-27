#Ingresar 2 numeros enteros y un operador (-,+,*,/), segun el operador ingresado, mostrar la operacion matematica que se debe efectuar 
#Ingreso se 2 numeros EJEMPLO: (numero1, numero2) y un operador, dependiendo del operador seleccionado hacer la operacion matematica
#De otro modo mostrar el mensaje "Operacion Incorrecta"


	
num1=int(input("Ingrese el primer numero: "))
	
num2=int(input( "Ingrese el segundo numero: "))
	
print("El numero 1 hace referencia al operador suma")
print("El numero 2 hace referencia al operador resta")
print("El numero 3 hace referencia al operador multiplicacion")
print("El numero 4 hace referencia al operador division")
	

operario=int(input( "Introduce el operador : "))
	
	
if operario==1:
    print("La suma de los numeros es: ",num1+num2)
elif operario==2:
    print("La resta de los numeros es: ",num1-num2)
elif operario==3:
    print( "La multiplicacion de los numeros es: ",num1*num2)
elif operario==4:
    print("La division de los numeros es: ",num1/num2)
else:
    print( "Operacion Incorrecta")

