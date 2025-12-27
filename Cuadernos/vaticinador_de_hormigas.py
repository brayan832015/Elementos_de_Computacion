#función hormigas(n) que predice cuantas hormigas van a existir después de n periodos, en un periodo dado existen la mayor cantidad de parejas posibles.
def hormigas(n):
    contador=0
    hormigas_totales=10 #iniciamos con 10 hormigas
    muertes=0
    periodo=0
    while periodo<n:
        hormigas=hormigas_totales #comenzamos con 10 y a medida que vayan aumentado y muriendo se ve reflejado en el valor de hormigas_totales
        parejas=hormigas//2 #parejas es la división entera del total de hormigas entre 2 para sacar la mayor cantidad posible de parejas
        nacimientos=parejas*3 #por cada pareja nacen 3 hormigas
        if n>1: #a partir del periodo 1 las hormigas nacidas dos periodos anteriores comienzan a morir en cada periodo
            hormigas_totales=hormigas+nacimientos-muertes #las hormigas totales son las que habían más las que nacieron menos las que murieron
        elif n==1: #si el periodo es 1 ninguna hormiga va a morir, ya que, mueren en el segundo periodo de sus vidas, entonces las hormigas totales son las que habían más las que nacieron
            hormigas_totales=hormigas+nacimientos
        contador+=1 #sumamos uno a contador para que ingrese al if y cuente las muertes que van a haber en el siguiente periodo
        if contador==1:
            muertes=hormigas_totales-nacimientos #muertes van a ser las hormigas que había en el periodo que acaba de pasar, que van a morir en el siguiente periodo
            contador=0 #igualamos a 0 para que vuelva a pasar lo mismo en todas las generaciones
        periodo+=1 #sumamos a periodo para cuando se llegue al n salir del While
    return hormigas_totales
    if n==0: #si n es 0 van a estar solo las hormigas iniciales
        return hormigas_totales
hormigas(5)     