#Calcular el cambio de monedas en dolares y euros al igresar cierta cantidad de dinero.(tipo de cambio del Dolar: 3789.36 pesos - Euro: 4401.46 pesos - peso argentino:38,37 - Yen:33,55  )

#ANALISIS:
# #Para poder realizar el cambio a Dolar, Euro, Peso Argentino y Yen, hay que conocer el tipo de cambio, de esa manera el monto dado se divide entre el  tipo de cambio.
#Ejemplo: $1 peso colombiano equivale a 0.0026 dolar, $1 peso coloombiano equivale a 0,00022 euro, $1 peso colombiano equivale a 0,026 peso argentino, $1 peso colombiano equivale a 0,030 yen

	
	
pc=int(input("introduce el monto en pesos colombianos:"))

print("el valor en dolares es de :",pc/3789.36,)
print("el valor en euros es de :",pc//44401.46,)
print("el valor enpesos argentinos es de:",pc/38.37)

print("el valor en yen es de :",pc/33,55,)


d=int(input("introduce el monto en dolares:"))

print("el valor en pesos colombianos es de:",d*3789.36, )
print("el valor en euros es de :",d*0.86,)
print("el valor en pesos argentino es de: ",d*99.88,)
print("el valor en yen es de :",d*114.24,)


eu=int(input("introduce el monto en euro:"))

print("el valor en pesoscolombianos es de : ",eu*4401.46,)
print("el valor en dolares es de : ",eu*1.16,)
print("el valor en pesos argentinos es de : ",eu*115.87,)
print("el valor en yen es de :",eu*132.54,)

pa=int(input("introduce el monto en pesos argentinos:"))

print("el valor en pesos colombianos es de :",pa*38.37,)
print("el valor en dolares es de :",pa*0.010,)
print("el valor en euro es de :",pa*0.0086,)
print("el valor enyen es de : ",pa*1.14,)


yen=int(input("introduce el monto de yen:"))

print("el valor en pesos colombianos es de:",yen*33.56,)
print("el valor en dolores es de :",yen*0.0088,)
print("el valor en euro es de :" ,yen*0.0075,)
print("el valor en pesos argentinos es de:",yen*0.87,)

