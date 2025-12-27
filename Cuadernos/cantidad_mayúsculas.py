#Esta es una función que recibe un texto como parámetro de entrada y retorna la cantidad de letras mayúsculas que posee el texto.
def cuenta_mayusculas(texto):
    long=len(texto)  #conocer la longitud del texto
    letra=0          
    mayus=0          #para contar la cantidad de mayúsculas
    while letra<long:     
        caracter=texto[letra]     #evalúa el texto en una determinada letra
        if caracter.isupper():    #si el caracter es mayuscula corre el if, sino no vuelve a correr el código con la siguiente letra
            mayus+=1   #sumar 1 al resultado de las mayusculas
        letra+=1       #pasar a la siguiente letra
    return mayus    
cuenta_mayusculas("HLAAokaeUY")