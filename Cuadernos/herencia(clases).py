pi=3.141592653589793 #para utilizar en operaciones
class Figura: #clase principal
    def __init__(self,area,perimetro): #constructor de figura
        self.area=area   
        self.perimetro=perimetro  
    def __add__(self,f2): #sobrecargar add para sumar las áreas de 2 objetos
        return Figura(self.area + f2.area,self.perimetro+f2.perimetro)
    def __str__(self): #sobrecargar str para que el resultado se muestre númericamente indicando un formato
        texto="Suma de áreas={suma}"    
        return  texto.format(suma=self.area) #darle formato
class Círculo(Figura): #subclase
    def __init__(self,radio): #constructor círculo
        self.radio=radio #atributo
    def CalcularPerimetro(self):
        print('Perímetro círculo=',int(self.radio*2*pi)) #método para calcular perímetro del círculo
    def CalcularArea(self):
        print('Área círculo=',int(self.radio*self.radio*pi)) #método para calcular el área del círculo
class Cuadrado(Figura): #subclase
    def __init__(self,lado):
        self.lado=lado #atributo
    def CalcularPerimetro(self):
        print('Perímetro cuadrado=',int(self.lado*4)) #método
    def CalcularArea(self):
        print('Área cuadrado=',int(self.lado*self.lado)) #método
class Triángulo(Figura): #subclase
    def __init__(self,base,altura):
        self.base=base #atributo
        self.altura=altura #atributo
    def CalcularPerimetro(self):
        print('Perímetro triángulo=',int(self.base*3)) #método
    def CalcularArea(self):
        print('Área triángulo=',int(self.base*self.altura/2)) #método