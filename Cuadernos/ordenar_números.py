#ordenar números
def ordenar(b,c,d):
    if(b>c and b>d and c>d):
            tupla_1=(d,c,b)
            print (tupla_1)
    elif(b>c and b>d and d>c):
            tupla_2=(c,d,b)
            print (tupla_2)
    elif(c>b and c>d and d>b):
            tupla_3=(b,d,c)
            print (tupla_3)
    elif(c>b and c>d and b>d):
            tupla_4=(d,b,c)
            print (tupla_4)
    elif(d>b and d>c and c>b):
            tupla_5=(b,c,d)
            print (tupla_5)
    elif(d>b and d>c and b>c):
            tupla_6=(c,b,d)
            print (tupla_6)
b=int(input('Ingrese el primer numero:'))
c=int(input('Ingrese el segundo numero:'))
d=int(input('Ingrese el tercer numero:'))
ordenar(b,d,c)