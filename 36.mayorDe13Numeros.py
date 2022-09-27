# Hacer un algoritmo que muestre al usuario el mayor de 13 numeros ingresados 
if __name__ == '__main__':
    cont = int()
    may = int()
    num = int()
    may = 0
    for cont in range(1,14):
        print("Ingrese el numero: ",cont," : ", end="")
        num = int(input())
        if may<num:
            may = num
    print("El numero mayor es el: ",may)

