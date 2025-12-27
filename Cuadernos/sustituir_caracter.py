#Esta es una función que recibe un texto, un caracter para sustituir y un caracter sustituto, en ese orden. Cambia todas las apariciones del carácter a sustituir con el carácter sustituto y retorna el texto resultante.
def sustituir_caracter(texto, sustituir, sustituto):
    longitud=len(texto) #para poder evaluar las letras individualmente
    resultado=''
    pos=0
    while pos<longitud: #mientras la posición sea menor que la longitud sigue corriendo el código(hasta que se evalúe todo se termina el while)
        letra=texto[pos] #evalúa el texto en esa posición
        if (letra!=sustituir):   #si el caracter es diferente al caracter a sustituir se agrega al resultado
            resultado+=letra   
        elif (letra==sustituir):  #si el caracter es igual al caracter a sustituir se agrega el sustituto al resultado
            resultado+=sustituto
        pos+=1 
    return resultado
sustituir_caracter('Hola a todos', 'a', 'w')