# Elaborar un algoritmo que permita al usuario almacenar los nombres y promedios de 7 aprendices de ADSI, las notas deben estar entre 0 y 20.
# mostrar los 3 aprendices con las mejores notas 
if __name__ == '__main__':
	notas = int()
	contnotas = int()
	cont = int()
	mnota = int()
	promedio = int()
	nombres = str()
	for cont in range(7):
		print("Introduce el nombre del aprendiz ",cont+1, end="")
		nombres = input()
		contnotas = 0
		promedio = 0
		while contnotas<3:
			print("Introduce la nota ",contnotas+1," de ",nombres, end="")
			notas = int(input())
			while notas<0 or notas>20:
				print("Error, la nota es incorrecta ingrese nuevamente")
				notas = int(input())
			promedio = promedio+notas
			contnotas = contnotas+1
		promedio = round(promedio/3)
		print("Su promedio es de: ",promedio)
	mnota = 0
	if promedio>mnota:
		mnota = promedio
		print("El mejor promedio es de: ",nombres," con promedio de: ",mnota)
