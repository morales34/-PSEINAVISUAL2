# Hacer un algoritmo que lea 10 consumos de una cafeteria, si el consumo total excede los $50.000, el descuento sera del 7%
# mostrar el pago total acumulado y su respectivo descuento (si lo hay).
if __name__ == '__main__':
    cont = int()
    consumo = float()
    ptotal = float()
    descuento = float()
    ptotal = 0
    consumo = 0
    descuento = 0
    for cont in range(1,11):
        print("Ingrese el consumo: ",cont," : ", end="")
        consumo = float(input())
        ptotal = ptotal+consumo
    if ptotal>50000:
        descuento = ptotal*0.07
    else:
        descuento = 0
    print("El consumo total es de: ",ptotal)
    print("El decuento es de: ",descuento)
    print("El pago total es de: ",(ptotal-descuento))

