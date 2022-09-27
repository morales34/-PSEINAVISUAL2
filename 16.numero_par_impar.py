#Ingresar un numero y mostrar si es numero par o impar

#ANALISIS:
#¿comodeterminar si un numero es par?
#todo numero que pueda dividirse entre 2 y si su residuo es igual a 0 es un numero par, de lo contrario es un numero impar.


Numero=int(input("Intrtroduce el numero: "))

if Numero % 2==0:
    print(f'{Numero} es un número par:')
else:
    print(f'{Numero} es un número impar:')

