#Cuadrado mágico, es una matriz cuadrada en la cual todas las filas, columnas y diagonales suman lo mismo, retorna true si es mágico y false si no lo es.
def es_magico(matriz):
    lista_suma=[] #lista donde se añaden todos los resultados de las diferentes sumas.
    #realiza la suma de forma horizontal sumando una columna con la otra en determinadas filas.
    for fila in range(len(matriz)): 
        suma_1=0 #las variables suma se utilizan para almacenar temporalmente el valor de las sumas y cuando se realicen las sumas pertinentes el valor se añade a lista_suma
        for columna in range(len(matriz[0])):
            suma_1=suma_1+matriz[fila][columna] #el valor de suma más el valor en esa fila y en esa columna.
        lista_suma.insert(0,suma_1) #insertar el valor de suma a lista_suma     
    #realiza la suma de forma vertical sumando una fila con la otra en determinadas columnas.
    for columna in range(len(matriz[0])): 
        suma_2=0
        for fila in range(len(matriz)):
            suma_2=suma_2+matriz[fila][columna]
        lista_suma.insert(0,suma_2)      
    suma_3=0
    #realiza la suma de forma diagonal sumando de la esquina superior izquierda hasta la esquina inferior derecha.
    for columna in range(len(matriz[0])):
        for fila in range(len(matriz)):
            if columna==fila:#cuando la columna es igual a la fila se encuentra en la diagonal
                suma_3=suma_3+matriz[fila][columna]
    lista_suma.insert(0,suma_3)      
    #realiza la suma de forma diagonal sumando desde la esquina inferior izquierda hasta la esquina superior derecha.
    longitud=len(matriz)-1 #longitud es el valor de la longitud de la matriz menos uno, ya que las filas y columnas comienzan en 0 y la longitud comienza en 1.
    suma_4=0
    fila=0 #variable para contar las filas
    columna=0 #variable para contar las columnas
    fila=longitud #fila toma el valor de la longitud, entonces es igual a la última fila
    if fila==longitud-columna: #si la fila es igual a longitud menos columna
        while fila>=0:
            suma_4=suma_4+matriz[fila][columna]
            columna+=1 #sumar 1 a columna
            fila-=1 #restar 1 a fila, osea, que estamos avanzando en forma diagonal hacia arriba y a la derecha
        lista_suma.insert(0, suma_4)
    #verifica si la suma de diagonales, filas y columnas tienen el mismo resultado.
    cuenta_ok=0
    for elemento in lista_suma:
        if lista_suma[0]==lista_suma[cuenta_ok]:#si el primer elemento de lista suma es igual a todo el resto de elementos de lista suma, entonces es verdadero si no es igual es falso.
            cuenta_ok+=1 #sumar 1 a cuenta ok para que tome el siguiente valor en la lista y para que luego se pueda comparar con la longitud total de lista_suma
    if cuenta_ok==len(lista_suma): #si el valor de cuenta_ok es igual a la longitud de la lista quiere decir que todos los elementos en la lista tienen el mismo valor
        return True
    else:
        return False
es_magico( [[11,4,17,10,23],[20,8,21,14,2],[24,12,5,18,6],[3,16,9,22,15],[7,25,13,1,19]] )