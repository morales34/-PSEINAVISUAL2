#Realizar un algoritmo que dados 2 numeros enteros, visualice en pantalla si son par o impar.
#En el caso de ser 0, debe visualizar "el numero no es par ni impar" (para que un numero sea par, se debe dividir entre
#dos y que su resto sea 0), si ambos son pares, escribir "Ambos son Pares", de lo contrario "Ambos son impares"



num1=int(input("Introduce el primer numero: "))
	
num2=int(input( "Introduce el segundo numero: "))
	
cociente1=round(num1/2)
residuo1=(cociente1*2)
resultado1=(num1-residuo1)
	
cociente2=round(num2/2)
residuo2=(cociente2*2)
resultado2=(num2-residuo2)

if num1==0 and num2==0:
		print( num1, " and ", num2, " no son pares ni impares")
elif resultado1!=0 and num2==0:
	print( num1, " es impar ", "y ",num2, " no es par ni impar")
elif num1==0 and resultado2!=0:
	print( num1, " no es par ni impar ","y ",num2, " es impar")
elif num1==0 and resultado2==0:
	print( num1, " no es par ni impar ","y ",num2, " es par")
elif resultado1==0 and num2==0:
	print (num1," es par ","y ",num2," no es par ni impar")
elif resultado1==0 and resultado2==0:
	print( num1, " y ", num2, " ambos son pares")
elif resultado1==0 and resultado2!=0:
	print( num1, " es par ", "y ", num2, " es impar")
elif resultado1!=0 and resultado2==0:
	print( num1, " es impar ", "y ", num2, " es par")
elif resultado1!=0 and resultado2!=0:
    print( num1," y ", num2, " ambos son impares")
					

									