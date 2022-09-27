# Hacer un algoritmo que permita al usuario ingresar 10 numeros enteros y muestre la cantidad de numeros pares e impares ingresados 
if __name__ == '__main__':
    cont = int()
    num = int()
    pares = int()
    impares = int()
    for cont in range(1,11):
        print("Introduce el Numero ",cont," : ", end="")
        num = int(input())
        if (num%2)==0:
            pares = pares+1
            print(num," Es par")
        else:
            impares = impares+1
            print(num," Es impar")
    print("La cantidad de pares ingresados son: ",pares)
    print("La cantidad de impares ingresados son: ",impares)

