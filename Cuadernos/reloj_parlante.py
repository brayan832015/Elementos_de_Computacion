#reloj parlante
def reloj_parlante(reloj):
    hora=reloj[0:2]
    minutos=reloj[3:5]
    tipo=reloj[6:]
    if (tipo =='am' ):
        tipo='mañana.'
    elif (tipo =='pm'):
        hora_int=int(hora)
        if (hora_int<6 and hora_int>11):
            tipo='tarde.'
        elif(hora_int>11):
            tipo='tarde.'
        else:
            tipo= 'noche'
    hora_p = int(hora)
    if (hora_p<10):
        hora=reloj[1:2]
    else:
        hora=reloj[0:2]
    return ("Son las "+(hora)+" y "+(minutos)+" de la "+(tipo))
a=str(input( 'Ingrese la hora:'))
texto = reloj_parlante(a)
print(texto)