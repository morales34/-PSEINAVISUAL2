def saludar():
    print("Hola, estimados aprendices!!")
    

def   CalcularDoble (num) :
      calc = num*2
      return calc 
print("Llamada a la función saludar")

x=int(input("Ingrese el valor que le pasamos por parámetro"))
print("Llamada a la función CalcularDoble")
print("El doble de ",x, "es"  ,CalcularDoble(x))
