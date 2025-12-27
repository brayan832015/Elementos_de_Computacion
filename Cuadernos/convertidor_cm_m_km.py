#convertidor m, cm o km
med_inicial=str(input('Ingrese la medida inicial (cm, m o km):'))
med_final=str(input('Ingrese la medida a la que quiere convertir su dato (cm, m o km):'))
medida=int(input('Ingrese la medida a convertir:'))
if(med_inicial=='cm' and med_final=='m'):
    print(medida/100, 'metros')
if(med_inicial=='cm' and med_final=='km'):
    print(medida/100000, 'kilómetros')
if(med_inicial=='m' and med_final=='cm'):
    print(medida*100, 'centímetros')
if(med_inicial=='m' and med_final=='km'):
    print(medida/1000, 'kilómetros')
if(med_inicial=='km' and med_final=='m'):
    print(medida*1000, 'metros')
if(med_inicial=='km' and med_final=='cm'):
    print(medida*100000, 'centímetros')