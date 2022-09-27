
#Ingrsar un numero del 1-12 y mostrar el mes del año que corresponde, si el numero ingrsado no es correcto, "mostrar un mensaje de error"
#ANALISIS: guardar el numero ingresado en una variable y luego comparar cada variable con un valor del 1-12; si corresponde
#a un numero dentro de ese rango mostrar en pantalla el mes que corresponde, EJEMPLO: 1 = Enero, 2 = Febrero, etc.

#solicitar el numero del mes
num=int(input("Ingrese el numero del mes (1-12): "))

#usar la funcion para encontrar el mes correspondiente

if num==1:
    print("enere")
elif num==2:
    print("febrero")
elif num==3:
    print("marzo")
elif num==4:
    print("abril")
elif num==5:
    print("mayo")
elif num==6:
    print("junio")
elif num==7:
    print("julio")
elif num==8:
    print("agosto")
elif num==9:
    print("setirmbre")
elif num==10:
    print("octubre")
elif num==11:
    print("noviembre")
elif num==12:
    print("diciembre")
else:
    print("numero del mes incorrecto")
    
        




    
