#Calcular el cambio de monedas en dolares y euros al igresar cierta cantidad de dinero.(tipo de cambio del Dolar: 3789.36 pesos - Euro: 4401.46 pesos)

#ANALISIS
#Para poder realizar el cambio a Dolat o Euro hay que conocer el tipo de cambio, de esa ,anera el monto dado se divide entre el  tipo de cambio.
#Ejemplo: $1 peso equivale a 0.0026 dolar, ya que el valor del dolar es de (3789.36 x cada Dolar), de la misma manera con el Euro
#recordar que el valor del Dolar y Euro siempre cambia con el pasar del tiempo, el mercado y la situacion economica del pais 
#en nuestro caso hemos tomado el valor del cambio como referencia. La misma logica puedes aplicar para convertir de pesos a dolares o de pesos a euros.

	
mp=int(input("Ingrese el monto en pesos: "))
	
print( "El valor en dolares es de: ",mp/3789.36,)
print("El valor en euros es de: ",mp/4401.46,)
	
	
