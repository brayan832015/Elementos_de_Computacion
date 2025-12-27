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