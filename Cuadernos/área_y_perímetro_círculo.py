#Cálculo del área y del perímetro de un círculo
print('Bienvenido a su programa para calcular el área y perímetro de un círculo')
radio=float(input('Ingrese la medida del radio del círculo: '))
from math import pi 
area=float(pi*radio*radio)
perimetro=2*pi*radio
h="El área del círculo es:"
i="El perímetro del círculo es:"
print(h,area)
print(i,perimetro)