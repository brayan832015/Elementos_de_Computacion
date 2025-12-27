#convertidor dólar, euro, colón
def convertidor(e,f):
    if(f=='dólar'):
        g=round(e / 610.64,2)
        print(g)
    elif(f=='euro'):
         h=round(e / 729.91,2)
         print(h)
    else:
        print(-1)
f=str(input('Ingrese la moneda:'))
e=float(input('Ingrese el monto en colones:'))
convertidor(e,f)