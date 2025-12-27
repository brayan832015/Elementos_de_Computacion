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