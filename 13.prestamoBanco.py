#Hacer un algoritmo donde una persona recibe un prestamo de $1000000 de un banco y desea saber cuanto pagara de interes,
#si el banco le cobra una tasa del 2% mensual. Ingresar el numero de meses por teclado.

print("usted recibio un prestamo de 1.000.000")
print("la taza de interes mensual es de 2 %")

meses=int(input("ingreser la cantidad de meses: "))

inter=(meses*(1000000*2/100))

print(f"el valor de sus intereses es :{inter}")




