#Crear un programa que devuelva el resultado de un n伹ero elevado a un exponente
def  potencia(base,expo):
    resultado= base^expo
    
    return resultado 

base= int(input("Ingrese la base: "))

expo=int(input("Ingrese el exponente: "))

resultado =potencia(base,expo)

print("La potencia es: ",resultado)
