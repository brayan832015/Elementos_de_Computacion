#Esta es una función que recibe un texto y retorna un True si el texto es un palíndromo y un False si no lo es, ignora si las letras son mayúsculas o minúsculas y ignora los espacios en blanco.
def es_palindromo(letras):
    palabra=letras.lower() #pasar a minúsculas
    longitud=len(palabra) #longitud de palabra
    desorden=''
    i=0
    while(i<longitud):
        desorden+= palabra[((longitud-i)-1):(longitud-i)] #si la longitud=9, al restar 1 toma el digito de 9 a 8 cuando i es 0, y asi sucesivamente según vaya aumentando el valor de i
        i+=1
    if(palabra==desorden): #se retorna True si la palabra es igual a desorden 
        return True
    else:                  #si no es igual retorna False
        return False
es_palindromo('mor a rom')