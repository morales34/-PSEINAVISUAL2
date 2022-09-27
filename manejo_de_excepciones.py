
#Manejo de Excepciones

#Diferencia entre errores de sintaxis y excepciones

#Try Except en Python

"""try:
    instrucciones
except:
    instrucciones
    #se ejecuta si hubo error en try"""

#¿Cómo funciona try()?

#Resolvamos la excepción del ejercicio anterior

particiones = 1

for i in range(10):
    try:
        particiones /= i
    except:
        print('división por cero, el ciclo ignorará la operación')

print(particiones) 


a = input('digite un número: ')
try:
    print(a + 15)
except TypeError as e:
    print('La variable no se almacenó como número')
    print('error: ',e, sep='\n') 

#Palabra clave finally en Python

"""try:
    instrucciones
except:
    instrucciones
    #se ejecuta si hubo error en try
finally:
    instrucción
    #siempre se ejecuta"""

particiones = 1

for i in range(10):
    try:
        particiones /= i
    except:
        print('división por cero, el ciclo ignorará la operación')
    finally:
        print('\ndivisión parcial: ',particiones)

print('\nresultado final',particiones) 


