# La compania de seguros funerarios "El Hogar de Cristo" ofrece a sus clientes 3 tipos de seguro
# Tipo  Pago mensual
# Ancianos = $45.000
# Adultos = $30.000
# Jovenes = $22.000
# segun la estacion del ano, tiene un descuento especial, siendo en invierno el 10%, primavera del 15%, verano del 20% y otono del 25%
# Ademas de dichos descuentos las mujeres tienen un descuento adicional de otro 5%, siempre y cuando vayan vestidas de rojo
if __name__ == '__main__':
    tipop = str()
    estacion = str()
    sexo = str()
    colorvesti = str()
    joven = float()
    adulto = float()
    anciano = float()
    print("Tipo de sexo: ", end="")
    sexo = input()
    print("Introduce el tipo de persona: ", end="")
    tipop = input()
    print("De que color va vestida la persona: ", end="")
    colorvesti = input()
    print("En que estacion del a�o estamos: ", end="")
    estacion = input()
    print("")
    anciano = 45000
    adulto = 30000
    joven = 22000
    if estacion=="invierno":
        if (tipop)=="anciano":
            if (sexo=="mujer" and colorvesti=="rojo"):
                print("El valor de su seguro es de: $",anciano-anciano*0.1-anciano*0.05)
            else:
                print("El valor de su seguro es de: $",anciano-anciano*0.1)
        elif (tipop)=="adulto":
            if (sexo=="mujer" and colorvesti=="rojo"):
                print("El valor de su seguro es de: $",adulto-adulto*0.1-adulto*0.05)
            else:
                print("El valor de su seguro es de: $",adulto-adulto*0.1)
        elif (tipop)=="joven":
            if (sexo=="mujer" and colorvesti=="rojo"):
                print("El valor de su seguro es de: $",joven-joven*0.1-joven*0.05)
            else:
                print("El valor de su seguro es de: $",joven-joven*0.1)
    elif estacion=="primavera":
        if (tipop)=="anciano":
            if (sexo=="mujer" and colorvesti=="rojo"):
                print("El valor de su seguro es de: $",anciano-anciano*0.15-anciano*0.05)
            else:
                print("El valor de su seguro es de: $",anciano-anciano*0.15)
        elif (tipop)=="adulto":
            if (sexo=="mujer" and colorvesti=="rojo"):
                print("El valor de su seguro es de: $",adulto-adulto*0.15-adulto*0.05)
            else:
                print("El valor de su seguro es de: $",adulto-adulto*0.15)
        elif (tipop)=="joven":
            if (sexo=="mujer" and colorvesti=="rojo"):
                print("El valor de su seguro es de: $",joven-joven*0.15-joven*0.05)
            else:
                print("El valor de su seguro es de: $",joven-joven*0.15)
    elif estacion=="verano":
        if (tipop)=="anciano":
            if (sexo=="mujer" and colorvesti=="rojo"):
                print("El valor de su seguro es de: $",anciano-anciano*0.2-anciano*0.05)
            else:
                print("El valor de su seguro es de: $",anciano-anciano*0.2)
        elif (tipop)=="adulto":
            if (sexo=="mujer" and colorvesti=="rojo"):
                print("El valor de su seguro es de: $",adulto-adulto*0.2-adulto*0.05)
            else:
                print("El valor de su seguro es de: $",adulto-adulto*0.2)
        elif (tipop)=="joven":
            if (sexo=="mujer" and colorvesti=="rojo"):
                print("El valor de su seguro es de: $",joven-joven*0.2-joven*0.05)
            else:
                print("El valor de su seguro es de: $",joven-joven*0.2)
    elif estacion=="oto�o":
        if (tipop)=="anciano":
            if (sexo=="mujer" and colorvesti=="rojo"):
                print("El valor de su seguro es de: $",anciano-anciano*0.25-anciano*0.05)
            else:
                print("El valor de su seguro es de: $",anciano-anciano*0.25)
        elif (tipop)=="adulto":
            if (sexo=="mujer" and colorvesti=="rojo"):
                print("El valor de su seguro es de: $",adulto-adulto*0.25-adulto*0.05)
            else:
                print("El valor de su seguro es de: $",adulto-adulto*0.25)
        elif (tipop)=="joven":
            if (sexo=="mujer" and colorvesti=="rojo"):
                print("El valor de su seguro es de: $",joven-joven*0.25-joven*0.05)
            else:
                print("El valor de su seguro es de: $",joven-joven*0.25)

    

