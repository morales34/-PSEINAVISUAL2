#realizar un algoritmo que dados 4 números enteros, visualice en pantalla si son par o impar.
#en el caso de ser 0, debe visualizar "el número no es par ni impar" (para que un número sea par, se debe dividir entre
#dos y que su resto sea 0), si ambos son pares, escribir "ambos son pares", de lo contrario "ambos son impares"


num1=int(input("introduce el primer número: "))

num2=int(input("introduce el segundo número: "))

num3=int(input("introduce el tercer número: "))

num4=int(input("introduce el cuarto número: "))

cociente1=round (num1/2)
residuo1=(cociente1*2)
resultado1=(num1-residuo1)

cociente2=round (num2/2)
residuo2=(cociente2*2)
resultado2=(num2-residuo2)

cociente3=round (num3/2)
residuo3=(cociente3*2)
resultado3=(num3-residuo3)

cociente4=round (num4/2)
residuo4=(cociente4*2)
resultado4=(num4-residuo4)

#si todos los numero son 0

if num1==0 and num2==0 and num3==0 and num4==0:
    print(num1, " , ", num2, " , ", num3, " y ",num4," no son pares ni impares")

#cuando uno de los numeros es diferente de 0 y es impar, y los otros numeros son 0

elif resultado1!=0 and num2==0 and num3==0 and num4==0:
    print(num1, " es impar ", "y ",num2," , ",num3," , ",num4, " no son pares ni impares")
elif num1==0 and resultado1 !=0 and num3==0 and num4==0:
    print(num2, " es impar ", "y ",num1," , ",num3," , ",num4, " no son pares ni impares")

elif num1==0 and num2==0 and resultado3!=0 and num4==0:
    print(num3, " es impar ", "y ",num1," , ",num2," , ",num4, " no son pares ni impares")
elif num1==0 and num2==0 and num3==0 and resultado4!=0:
    print(num4, " es impar ", "y ",num1," , ",num2," , ",num3, " no son pares ni impares")
#cuando uno de los numeros es diferente de 0 y es par, y los otros numeros son 0

elif resultado1==0 and num2==0 and num3==0 and num4==0:
    print(num1, " es par ", "y ",num2," , ",num3," , ",num4, " no son pares ni impares")
elif num1==0 and resultado2==0 and num3==0 and num4==0:
    print(num2, " es par ", "y ",num1," , ",num3," , ",num4, " no son pares ni impares")
elif num1==0 and num2==0 and resultado3==0 and num4==0:
    print(num3, " es par ", "y ",num1," , ",num2," , ",num4, " no son pares ni impares")
elif num1==0 and num2==0 and num3==0 and resultado4==0:
    print(num4, " es par ", "y ",num1," , ",num2," , ",num3, " no son pares ni impares")

#cuando todos son impares
if resultado1!=0 and resultado2!=0 and resultado3!=0 and resultado4!=0 :
    print(num1, " , ", num2, " , ", num3, " y ",num4," son impares")



elif resultado1==0 and resultado2==0 and num3==0 and num4==0:
    print (num3," , ",num4," no son pares ni impares ","y ",num1," , ",num2," son pares")


elif resultado1!=0 and resultado2!=0 and num3==0 and num4==0:
    print(num3," , ",num4," no son pares ni impares ","y ",num1," , ",num2," son impares")

elif num1==0 and num2==0 and resultado3==0 and resultado4==0:
    print(num1," , ",num2," no son pares ni impares ","y ",num3," , ",num4," son pares")

elif num1==0 and num2==0 and resultado3!=0 and resultado4!=0:
    print(num1," , ",num2," no son pares ni impares ","y ",num3," , ",num4," son impares")

#cuando uno de los numeros es 0 y los otos son diferentes de 0 y son pares


elif num1==0 and resultado2==0 and resultado3==0 and resultado4==0:
    print(num1, " no par ni impar ", "y ",num2," , ",num3," y ",num4, " son pares")

elif resultado1==0 and num2==0 and resultado3==0 and resultado4==0:
    print(num2, " no par ni impar ", "y ",num1," , ",num3," y ",num4, " son pares")

elif resultado1==0 and resultado2==0 and num3==0 and resultado4==0:
    print(num3, " no par ni impar ", "y ",num1," , ",num2," y ",num4, " son pares")

elif resultado1==0 and resultado2==0 and resultado3==0 and num4==0:
    print(num4, " no par ni impar ", "y ",num1," , ",num2," y ",num3, " son pares")

#cuando uno de los numero es 0 y los otros son diferentes de 0 y son impares
elif num1==0 and resultado2!=0 and resultado3!=0 and resultado4!=0:
    print(num1, " no es par ni impar ", "y ",num2," , ",num3," , ",num4, " son impares")

elif resultado1!=0 and num2==0 and resultado3!=0 and resultado4!=0:
    print(num2, " no es par ni impar ", "y ",num1," , ",num3," , ",num4, " son impares")

elif resultado1!=0 and resultado2!=0 and num3==0 and resultado4!=0:
    print(num3, " no es par ni impar ", "y ",num1," , ",num2," , ",num4, " son impares")

elif resultado1!=0 and resultado2!=0 and resultado3!=0 and num4==0:
    print(num4, " no es par ni impar ", "y ",num1," , ",num2," , ",num3, " son impares")

#cuando 2 numeros medios o extremos son 0 y los otros son pares o impares
elif num1==0 and resultado2==0 and resultado3!=0 and  num4==0:
    print(num1," , ",num4," no son pares ni impares ",", ",num2," es par"," y ",num3," es impar")

elif num1==0 and resultado2!=0 and resultado3==0 and  num4==0:
    print(num1," , ",num4," no son pares ni impares ",", ",num3," es par"," y ",num2," es impar")

elif resultado1!=0 and num2==0 and num3==0 and  resultado4==0:
    print(num2," , ",num3," no son pares ni impares ",", ",num4," es par"," y ",num1," es impar")

elif resultado1==0 and num2==0 and num3==0 and  resultado4!=0:
    print(num2," , ",num3," no son pares ni impares ",", ",num1," es par"," y ",num4," es impar")

#cuando un numero es 0, uno es par y los otros son impares
elif num1==0 and resultado2!=0 and resultado3!=0 and resultado4==0:
    print(num1," no es par ni impar ",num4," es par ", "y ",num2," , ",num3," son impares")
elif num1==0 and resultado2==0 and resultado3!=0 and resultado4!=0:
    print ( num1," no es par ni impar ",num2," es par ", "y ",num3," , ",num4," son impares")
#si hay dos numeros iguales a 0 y dos numeros pares o impares
elif num1==0 and resultado2!=0 and num3==0 and resultado4!=0:
    print(num1," , ",num3," no son pares ni impares ","y ",num2," , ",num4," son impares")
elif num1==0 and resultado2==0 and num3==0 and resultado4==0:
    print(num1," , ",num3," no son pares ni impares ","y ",num2," , ",num4," son pares")
elif resultado1!=0 and num2==0 and resultado3!=0 and num4==0:
    print(num2," , ",num4," no son pares ni impares ","y ",num1," , ",num3," son impares")
#cuando hay 2 numeros iguales a 0 y los otros uno es par y el otro impar
elif num1==0 and resultado2==0 and num3==0 and resultado4!=0:
    print(num1," , ",num3," no son pares ni impares",", ",num2," es par"," y ",num4," es impar")

elif num1==0 and resultado2!=0 and num3==0 and resultado4==0:
    print(num1," , ",num3," no son pares ni impares ",", ",num4," es par"," y ",num2," es impar")

elif resultado1!=0 and num2==0 and resultado3==0 and num4==0:
    print(num2," , ",num4," no son pares ni impares ",", ",num3," es par"," y ",num1," es impar")

elif resultado1==0 and num2==0 and resultado3!=0 and num4==0:
    print(num2," , ",num4," no son pares ni impares ",", ",num1," es par"," y ",num3," es impar")

#cuando los 2 primeros numeros uno es par y el otro es impar y los dos ultimos son iguales a 0
elif resultado1!=0 and resultado2==0 and num3==0 and num4==0:
    print(num3," , ",num4," no son pares ni impares ",", ",num2," es par"," y ",num1," es impar")

elif resultado1==0 and resultado2!=0 and num3==0 and num4==0:
    print(num3," , ",num4," no son pares ni impares ",", ",num1," es par"," y ",num2," es impar")

#cuando los 2 ultimos numeros uno es par and el otro es impar y los dos primeros son iguales a 0
elif num1==0 and num2==0 and resultado3!=0 and resultado4==0:
    print(num1," , ",num2," no son pares ni impares ",", ",num4," es par"," y ",num3," es impar")

elif num1==0 and num2==0 and resultado3==0 and resultado4!=0:
    print(num1," , ",num2," no son pares ni impares ",", ",num3," es par"," y ",num4," es impar")

#si un numero es impar y los otros son pares
elif resultado1!=0 and resultado2==0 and resultado3==0 and resultado4==0:
    print(num1, " es impar ", "y ",num2," , ",num3," y ",num4, " son pares")

elif resultado1==0 and resultado2!=0 and resultado3==0 and resultado4==0:
    print(num2, " es impar ", "y ",num1," , ",num3," y ",num4, " son pares")

elif resultado1==0 and resultado2==0 and resultado3!=0 and resultado4==0:
    print(num3, " es impar ", "y ",num1," , ",num2," y ",num4, " son pares")

elif resultado1==0 and resultado2==0 and resultado3==0 and resultado4!=0:
    print(num4, " es impar ", "y ",num1," , ",num2," y ",num3, " son pares")

#si uno de los numero es par y los otros son impares
elif resultado1==0 and resultado2!=0 and resultado3!=0 and resultado4!=0:
    print(num1, " es par ", "y ",num2," , ",num3," y ",num4, " son impares")

elif resultado1!= 0 and resultado2==0 and resultado3!=0 and resultado4!=0:
    print(num2, " es par ", "y ",num1," , ",num3," y ",num4, " son impares")

elif resultado1!=0 and resultado2!=0 and resultado3==0 and resultado4!=0:
    print(num3, " es par ", "y ",num1," , ",num2," y ",num4, " son impares")

elif resultado1!=0 and resultado2!=0 and resultado3!=0 and resultado4==0:
    print(num4, " es par ", "y ",num1," , ",num2," y ",num3, " son impares")

#si el numero1, numero3 son impares y numero2, numero4 son pares y viceversa
elif resultado1!=0 and resultado2==0 and resultado3!=0 and resultado4==0:
    print(num1," , ", num3," son impares ","y ",num2," , ",num4," son pares")

elif resultado1==0 and resultado2!=0 and resultado3==0 and resultado4!=0:
    print(num2," , ", num4," son impares ","y ",num1," , ",num3," son pares")

#si el numero1, numero2 son impares y numero3, numero4 son pares y veceversa
elif  resultado1!=0 and resultado2!=0 and resultado3==0 and resultado4==0:
    print(num1," , ", num2," son impares ","y ",num3," , ",num4," son pares")

elif resultado1==0 and resultado2==0 and resultado3!=0 and resultado4!=0:
    print(num1," , ", num2," son pares ","y ",num3," , ",num4," son impares")

#cuando el numero1, numero2 son 0 y numero3, numero4 son pares y viceversa
elif num1==0 and num2==0 and resultado3==0 and resultado4==0:
    print(num1," , ", num2," no son pares ni impares ","y ",num3," , ",num4," son pares")

elif resultado1==0 and resultado2==0 and num3==0 and num4==0:
    print(num3," , ", num4," no son pares ni impares ","y ",num1," , ",num2," son pares")

#cuando el numero1, numero2 son impares y numero3, numero4 valen 0 y viceversa
elif resultado1!=0 and resultado2!=0 and num3==0 and num4==0:
    print(num3," , ", num4," no son pares ni impares ","y ",num1," , ",num2," son impares")

elif num1==0 and num2==0 and resultado3==0 and resultado4==0:
    print(num1," , ", num2," no son pares ni impares ","y ",num3," , ",num4," son impares")

#cuando el numero1, numero4 son pares y numero2, numero3 son impares y viceversa
elif resultado1==0 and resultado2!=0 and resultado3!=0 and resultado4==0:
    print(num1, " , ", num4, " son pares ", "y ",num2," , ",num3," son impares")
 
elif resultado1!=0 and resultado2==0 and resultado3==0 and resultado4!=0:
    print(num1, " , ", num4, " son impares ", "y ",num2," , ",num3," son pares")

#cuando todos los números son pares
elif resultado1==0 and resultado2==0 and resultado3==0 and resultado4==0:
    print(num1, " , ", num2, " , ", num3, " y ",num4," son pares")
