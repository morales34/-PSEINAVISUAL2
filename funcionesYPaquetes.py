#funciones 

"""def funcion(parámetros)
documentación
instrucciones
return resultado"""

"""creacion de una funcion """
from pyrsistent import b


def saludar():
    print('hola mundo')

saludar()


"""argumentos y parametros de una funcion """

#función para definir si un número es par o impar

def paridad(x): #recibimos el número del usuario en x
    if x%2 == 0: #evaluamos la paridad de x con el módulo
        print(f'{x} es par')
    else:
        print(f'{x} es impar')



paridad(2) #aquí x=2
paridad(5) #aquí x=5
paridad(84) #aquí x=84
paridad(33) #aquí x=33

""" tipos de parametros """

#función para multiplicar números

def multiplicar(x,y=2):
    print(f'x = {x}, y = {y}')
    print('x*y=',x*y)


multiplicar(5)
multiplicar(5,5)


""" parametros con palabras clave ("keyword")"""

#Programa para demostrar el paso par palabra clave.

def estudiantes (nombre,apellido):
    print(nombre,apellido)

#argumentos por palabra clave

estudiantes(nombre='Pepe',apellido='Mujica')
estudiantes(apellido='Tapias',nombre='Armando')

#docstring

#print(nombre_funcion.__doc__)

#función para definir si un número es par o impar

def paridad(x): #recibimos el número del usuario en x
    """Función para comprobar si el número es par o impar.
    Entrada:
        x -> int: número a verificar
    Salida
        None. En la función se imprime el resultado
    """
    if x%2 == 0: #evaluamos la paridad de x con el módulo
        print(f'{x} es par')
    else:
        print(f'{x} es impar')

#print(paridad.__doc__)


#la sentencia RETURN

# return salida1,salida2,salida3

#creemos una funcion que calcule potencias o el cuadrado de un numero por defento y lo retorne 

def potencias(a,b=2):
    """
    Función para calcular la potencia de un número (a^b)
    Entradas:
        a -> int o float: base de la potencia
        b -> int o float: exponente, valor por defecto: 2
    Salidas:
        p -> int o float: a**b
    """
    return a**b

print(potencias(2))
print(potencias(3,5))
x = potencias(2,8) # podemos almacenar los resultados en variables
print('x:',x)


# función para separar nombre y apellido a partir de un solo string separado por espacios

def separador(texto):
    """
    Función para separar nombre y apellido a partir de un solo string separado por espacios
    Entrada:
        texto -> string: cadena con nombre y apellido
    Salida:
        nombre,apellido -> string: nombre y apellido separados
    """
    aux = texto.split(" ") #la función split permite separar en una lista strings
                           #según el argumento que se le pase.
    nombre = aux[0]        #esperamos solo un nombre y apellido, el nombre estará
    apellido = aux[1]      #en la primera posición de aux, el apellido en la segunda

    return nombre,apellido



print(separador("Fulanito DeTal"))

print(type(separador("Fulanito DeTal")))

nombre,apellido = separador("Fulanito DeTal") #podemos guardar las salidas en distintas variables
                                              #separando cada una con comas

print(nombre)
print(apellido)


#alcance y vida util de las variables

def func():
	x = 10
	print("Valor dentro de la función:",x)

x = 20
func()
print("Valor fuera de la función",x)



def func():
	x = 10
	print("Valor dentro de la función:",x)

x = 20
func()
print("Valor fuera de la función",x)






