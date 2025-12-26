#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[155]:


#Esta es una función que recibe un número entero y un dígito, retorna un número entero con el dígito eliminado cada vez que aparece.
def eliminar_repetidos(numeros, digito):
    longitud=len(str(numeros)) #pasar a str para poder evaluar los números individualmente
    resultado=''
    pos=0
    while pos<longitud:
        numero=str(numeros)[pos] 
        if (numero!=str(digito)):   
            resultado+=numero  #agregarle otro número a los números ya contenidos en el resultado 
        pos+=1 #evaluar el siguiente número en la cadena
    return int(resultado)
eliminar_repetidos(343366555712, 3)


# In[176]:


#Esta es una función que recibe un número entero positivo y retorna el valor booleano True si el número es primo y False si no es primo.
def numero_primo(numero):
    if(numero==2 or numero==3):#excepción de 2 y 3 que si son primos
        return True
    elif(numero==1): #excepción de 1 que no es primo
        return False
    elif (numero%2>0 and numero%3>0 and numero%4>0): #no puede ser divisible entre 2, 3 y 4 al mismo tiempo para ser primo
        return True
    else:
        return False

numero_primo(521)


# In[231]:


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


# In[8]:


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

