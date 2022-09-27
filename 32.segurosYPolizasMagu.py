S=str(input("introduce el sexo del conductor:"))
E=int(input("introduce la edad del conductor:"))

if  S=="H":
    interruptor = 1
else:
    S=="M"
    interruptor = 2

costo=0
if interruptor==1:
    if E < 25:
        costo=1000000
    else:
        costo=700000

if interruptor==2:
    if E<21:
        costo=500000
    else:
        costo=3500000



print("la edad es de:",E,)
print("el sexo es:",S,)
print("el valor a pagar es de:",costo,)



