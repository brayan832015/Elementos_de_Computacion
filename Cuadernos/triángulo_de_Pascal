#Triangulo de Pascal, función que retorna la fila que se le indique del triangulo de Pascal, inicia en cero.
def Pascal(n):
    lista = [[1],[1,1]] #es la variable para definir a la lista que va almacenando las sumas de las diferentes n
    for fila in range(1,n):
        longitud=len(lista[fila])-1 #longitud va a ser la longitud de la lista evaluada en una fila determinada y restandole 1, ya que, se utiliza en el trayecto que van a realizar las columnas, que comienzan en 0, al contrario la longitud comienza a contar en 1 por lo tanto hay que restar uno para que llegue hasta la columna límite.
        linea = [1] #variable donde se almacenan temporalmente las sumas de las filas y las columnas 
        for columna in range(0,longitud): #columnas van en el rango desde 0 hasta la longitud que tenga la fila determinada.
            linea.extend([lista[fila][columna] + lista[fila][columna+1]]) #para añadirle a linea el valor de esa fila en esa columa sumado al valor que está en esa misma fila pero la siguiente columna.
        linea += [1] #para añadir los unos que van al final del triángulo, después de que se hayan acabado las columnas. 
        lista.append(linea) #añade los valores que se obtienen de linea a la lista que los acomoda en una matriz, cada una con su determinado n.
    return lista[n]
Pascal(6)