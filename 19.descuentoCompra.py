#Dado un monto de compra calcular su descuento considerando que por encima de $35000,
#el descuento es del 35% y por debajo de 35000es de 10%.


	
moco=int(input("Introduce el monto de la compra: "))
	
if moco>=35000:
    print( "El valor del descuento del 35% es de: ","$",(moco*0.35))
    print( "Total a pagar es de: ","$",(moco-(moco*0.35)))
else:
		print( "El valor del descuento del 10% es de: ","$",(moco*0.1))
		print( "Total a pagar es de: ","$",(moco-(moco*0.1)))
print( "Gracias por su compra, esperamos que vuelva pronto")
print( "Con gusto la Panadería San José °c°")


	
