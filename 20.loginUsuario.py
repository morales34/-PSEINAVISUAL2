#Elaborar un programa que simule una contraseña de ingreso. si el usuario es: "ADMINISTRADOR" y la clave "ADMIN123456",
#mostrar el mensaje "ACCESO CONCEDIDO" de lo contrario mostrar el mensaje "ACCESO DENEGADO"


usu=str(input( "Introduce tu usuario: "))
	
con=int(input( "Ingresa tu contraseña: "))
	
if usu=="ADMIN" and  con==123456 :
		print( "ACCESO CONCEDIDO")
else:
		print( "ACCESO DENEGADO")
        

