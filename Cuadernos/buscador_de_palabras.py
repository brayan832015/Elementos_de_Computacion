#programa que recibe una entrada de texto .txt, lo lee y el usuario es capaz de escoger varias opciones según lo que desee hacer

abecedario="abcdefghijklmnñopqrstuvwxyzáéíóú0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ"
print('Aclaración:')
print('El texto ingresado debe estar gramaticalmente bien escrito (incluyendo que no tenga espacios dobles ni signos de puntuación dobles), cualquier símbolo que no sea una letra o un número será contado como un signo de puntuación.')
ruta=input('Ingrese la ruta completa del archivo .txt que desea utilizar: ') #ruta del archivo
texto=open(ruta, encoding='utf-8') #abrir el texto deseado
archivo=texto.read() #leer el texto
texto.close #cerrarlo una vez leído y almacenado en archivo
opcion='' #opcion elegida por el usuario
while opcion!=7:
    print("Menú") #Menú
    print('¿Que desea hacer?')
    print("1...........................Buscar palabra") #busca en el texto si se encuentra la palabra que ingresa el usuario
    print("2...........................Total palabras") #indica la cantidad total de palabras
    print("3..........................Total oraciones") #indica la cantidad de oraciones
    print("4.......................... Total párrafos") #indica la cantidad de párrafos
    print("5...........................Total espacios") #indica la cantidad de espacios
    print("6...............Total signos de puntuación") #indica la cantidad de signos de puntuación
    print("7....................................Salir") #sale del programa
    opcion=int(input('Ingrese la opción deseada: ')) #aquí el usuario ingresa la opción
    if opcion==1:
        print('***El programa no distingue entre mayúsculas y minúsculas***')
        palabra=input('Ingrese la pablabra que desea buscar: ') #palabra para buscar en el texto
        letra=0
        repite=0
        resultado=0
        while letra<len(archivo): #evalúa todos los caracteres del texto uno por uno    
            caracter=archivo[letra] #toma el caracter del texto en la posición que le indique letra
            caracter_palabra=palabra[resultado] #toma el caracter de la palabra que se quiere encontrar en la posición que le indique resultado
            if caracter_palabra==caracter: #si el caracter del archivo es igual al de la palabra que se busca sume uno a resultado, entonces se pasa a evaluar la siguiente letra
                resultado+=1
            elif caracter!=caracter_palabra:#si el primer caracter si era igual pero alguno de los que seguía no era igual al caracter de la palabra buscada, vuelva a resultado 0
                resultado=0
            letra+=1 #para avanzar el índice de archivo
            if resultado==len(palabra): #si el resultado es igual a la longitud de la palabra que estamos buscando quiere decir que encontramos una vez la palabra, si se encuentra más veces se continuan contando
                repite+=1
                resultado=0 #para que resultado sea cero y la palabra buscada vuelva a iniciar en su primer caracter
        print('La palabra',palabra,'se encuentra',repite,'veces en el texto')
    if opcion==2:
        espacios=0
        for caracter in archivo: #por cada caracter en el archivo
            if caracter==' ': #si el caracter es un espacio sume 1 a espacios
                espacios+=1
        print ('El texto ingresado tiene',espacios+1, 'palabras.') #al sumarle uno a la cantidad de espacios se obtienen la cantidad de palabras
    if opcion==3:
        espacios=0
        letras=0
        for caracter in archivo:
            if caracter==' ':
                espacios+=1
        for letra in abecedario: #evalúa cada valor que se encuentre en el abecedario (letras y números)
            for caracter in archivo:
                if caracter==letra:
                    letras+=1
            resultado=(len(archivo)-letras-espacios) #al restar las letras, números y espacios a la longitud del texto se obtienen la cantidad de oraciones, ya que, cada oración está separada por un signo de puntuación
        print ('El texto ingresado tiene',resultado, 'oraciones.')
    if opcion==4:
        parrafos=0
        for caracter in archivo:
            if caracter=='\n':#si el caracter es igual a \n que significa 'enter', entonces sume uno a párrafos
                parrafos+=1
        print ('El texto ingresado tiene',parrafos, 'párrafos.')
    if opcion==5:
        espacios=0
        for caracter in archivo:
            if caracter==' ':
                espacios+=1
        print ('El texto ingresado tiene',espacios, 'espacios.')
    if opcion==6: 
        espacios=0
        letras=0
        for caracter in archivo:
            if caracter==' ':
                espacios+=1
        for letra in abecedario:
            for caracter in archivo:
                if caracter==letra:
                    letras+=1
            resultado=(len(archivo)-letras-espacios) #al restar las letras, números y espacios a la longitud del texto se obtienen los signos de puntuación
        print ('El texto ingresado tiene',resultado, 'signos de puntuación.')
    if opcion==7:
        print('--------El programa finalizó--------')