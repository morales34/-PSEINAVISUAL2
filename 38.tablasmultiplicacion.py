# Desarrollar un algoritmo que me pida al usuario un numero entero del 1 - 13 y muestre la tabla de multiplicar de dicho numero, y que el ciclo se repita 
# Hasta que el usuario decida terminarlo, ingresando el 0 (cero) 
if __name__ == '__main__':
    cont = int()
    num = int()
    terminador = int()
    print("Introduce un numero del 1 al 13")
    num = int(input())
    for cont in range(1,14):
        print(num," x ",cont," = ",(num*cont))
