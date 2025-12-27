#desglose de billetes
centenas=int(input('Ingrese el monto en dólares:'))
de_100=centenas//100
decenas= centenas%100
de_50= decenas//50
de_20= (decenas-(de_50*50))//20
de_10= (decenas-(de_50*50)-(de_20*20))//10
de_5= (decenas-(de_50*50)-(de_20*20)-(de_10*10))//5
de_1= (decenas-(de_50*50)-(de_20*20)-(de_10*10)-(de_5*5))
print(de_100,'Billetes de 100 ')
print(de_50,'Billetes de 50 ')
print(de_20,'Billetes de 20 ')
print(de_10,'Billetes de 10 ')
print(de_5,'Billetes de 5 ')
print(de_1,'Billetes de 1 ')