#Matriz triangular (elementos por debajo o por encima de la diagonal son todos ceros), recibe una matriz cuadrada como entrada y retorna True si es triangular y False si no lo es.
def es_triangular(matriz_cuadrada):
    triangular_abajo=0 #Ceros en la esquina inferior de la diagonal.
    triangular_arriba=0 #Ceros en la esquina superior de la diagonal.
    auxiliar=0 #Variable temporal para manejo de la función.
    for fila in range(len(matriz_cuadrada)): #Longitud de la matriz(filas).
        for columna in range(len(matriz_cuadrada[0])): #Longitud de la matriz(columnas).
            if fila==columna: #Para recorrer la diagonal.
                auxiliar=columna #Para mantener el índice de la parte superior de la diagonal.
                while len(matriz_cuadrada[0])>auxiliar: #Mientras esté dentro de la longitud de la matriz.
                    if matriz_cuadrada[fila][auxiliar]==0 and fila!=auxiliar: #Evalúa los ceros que no estén en la diagonal.
                        triangular_arriba+=0 #El valor queda en 0 
                    elif matriz_cuadrada[fila][auxiliar]!=0 and fila!=auxiliar:
                        triangular_arriba+=1 #Si el valor no es 0 se le suma uno a la variable, lo que la hace falsa.
                    auxiliar+=1 #Para evaluar el siguiente valor en la matriz.
    for fila in range(len(matriz_cuadrada)):
        for columna in range(len(matriz_cuadrada[0])):
            auxiliar=columna 
            if fila!=columna: #Evalúa la parte inferior de la diagonal.
                while auxiliar<=fila: #Para evaluar la parte inferior de la diagonal.
                    if matriz_cuadrada[fila][auxiliar]==0 and fila!=auxiliar:
                        triangular_abajo+=0
                    elif matriz_cuadrada[fila][auxiliar]!=0 and fila!=auxiliar:
                        triangular_abajo+=1
                    auxiliar+=1
    if triangular_arriba==0 or triangular_abajo==0: #Si en alguna de las 2 partes es 0, es verdadero.
        return True
    else: #Si ambos son diferentes de 0 va a ser falso.
        return False    
es_triangular( [ [9,0,0,0], [0,9,0,2], [0,0,2,0],[0,5,2,0] ] )