#Ingrese la cantidad de aprtendices aprobados y desaprobados de una formacion,
#luego mostrar el porcentaje de aprendices aprobados y el porcentaje de aprendices desaprobados


print("Aprendices aprobados y desaprobados con sus respectivos porcentajes: ")

	
aprobados=int(input("Introduce el numero de aprendices aprobados:"))
desaprobados=int(input("Introduce el nuemro de aprendices desaprobados: "))
print( "El porcentaje de estudiantes aprobados es de: ",(aprobados*100)/(aprobados+desaprobados))
print( "El porcentaje de estudiantes desaprobados es de: ",(desaprobados*100)/(aprobados+desaprobados))



