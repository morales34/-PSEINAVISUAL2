
# Dada la duracion (en minutos) de una llamda telefonica, calcular su costo, de la siguiente manera:
#Hasta 5 min el costo es de 90 pesos. por encima de 5 min el costo es de 90+20 por cada minuto adicional a los 5 primeros min.

Minutos=float(input("Introduce la cantidad de minutos usados: "))

if (Minutos<=5) : 
    print("Su costo es de: ",Minutos*90,)
else:
    print("Su costo es de: ",(5*90)+((Minutos-5)*110),)
