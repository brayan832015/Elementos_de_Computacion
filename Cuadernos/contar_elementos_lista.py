#Cuente todos, función que recibe una lista de números enteros y cuenta todos los elementos en la lista, sin importar las sublistas
def cuente_todos(lista):
    resultado=0 #variable para contar la cantidad de números.
    lista_1=str(lista) #pasar la lista a string para calcular su longitud.
    sustituir='[' #sustituir son los caracteres que no suman al resultado.
    sustituir_2=']'
    sustituir_3=','
    sustituir_4=' '
    for fila in range(len(lista_1)):    
        if lista_1[fila]!=sustituir and lista_1[fila]!=sustituir_2 and lista_1[fila]!=sustituir_3 and lista_1[fila]!=sustituir_4: #si el dígito evaluado es diferente a todos los de sustituir se suma uno a resultado.
           resultado+=1
    return resultado
    
cuente_todos([4,  [[[3,8,   4], 5], [3]], 4, 8])