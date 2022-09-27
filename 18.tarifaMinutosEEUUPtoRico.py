# Dada la duracion (en minutos) de una llamda telefonica, calcular su costo, de la siguiente manera:
#Si la llamada es a puerto rico, Hasta 5 min el costo es de 90 pesos. por encima de 5 min el costo es de 90+20 por cada minuto adicional a los 5 primeros min.
#Si la llamada es a EE.UU, Hasta 5 min el costo es de 130 pesos. por encima de 5 min el costo es de 130+40 por cada minuto adicional a los 5 primeros min.


	
mipr=float(input( "Introduce la cantidad de minutos usados a Puerto Rico: "))

if mipr<=5 :
    print("Su costo es de: ","$",mipr*90)
else:
    print( "Su costo es de: ","$",(5*90)+((mipr-5)*110),)

	
mieeuu=float(input( "Introduce la cantidad de minutos usados a EE.UU: "))

	
if mieeuu<=5:
    print( "Su costo es de: ","$",mieeuu*130)
else:
    print ("Su costo es de: ","$",(5*130)+((mieeuu-5)*170),)

