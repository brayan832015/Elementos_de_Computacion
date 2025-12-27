#Cálculo del área y el perímetro de un rectángulo
print ('Bienvenido a su programa para calcular el área y el perímetro de un rectángulo')
altura=int(input('Ingrese la medida de la altura en metros : '))
base=int(input('Ingrese la medida de la base en metros: '))
f='El área correponde a:'
g='El perímetro corresponde a:'
area= base*altura
perimetro= 2*base+2*altura
print (f, area,"m2")
print(g, perimetro,"m")