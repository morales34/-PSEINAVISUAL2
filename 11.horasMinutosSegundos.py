#Hacer un programa que ingrese por teclado un numero total de segundos y que luego pueda mostrar la
#cantidad de horas, minutos y segundos que existen en el valor ingresado

#ANALISIS:
#Lo que necesitamos saber es cuantos segundos tiene en una hora (3600) y cuantos segundos tiene un minuto (60)
#para de esa manera dividir la cantidad de segundos y obtener las horas y minutos existentes.


S=float(input( "Ingresa la cantidad de segundos:"))
	
print("En minutos equivale a: ",S*1/60)
print( "En horas equivale a: ",S*1/3600)
	


