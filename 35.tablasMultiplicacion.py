# Desarrollar un algoritmo que me pida al usuario un numero entero del 1 - 13 y muestre la tabla de multiplicar de dicho numero 
if __name__ == '__main__':
    num = int()
    cont = int()
    print("Ingrese un numero del 1 al 13: ", end="")
    num = int(input())
    for cont in range(1,14):
        print(num," x ",cont," = ",(num*cont))

    

