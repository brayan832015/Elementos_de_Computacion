1#Este código pertenece a un filtro tipo FIR para archivos de audio .wav, recibe un archivo .wav lo lee y conforme a los datos de ese audio y una ecuación se genera otro audio "filtrado", además se pueden reproducir y graficar ambos audios. El audio resultante se guarda donde el usuario indique y también se lee el audio que el usuario desee.
import scipy.io.wavfile as waves #importar para leer y escribir archivos .wav
import numpy as np #importar para manejar los arreglos de datos de una forma más fácil y rápida
import winsound #importar para reproducir los audios que solicite el usuario
import matplotlib.pyplot as plt #importar para graficar ambos archivos de audio
print('Bienvenido al FIR (filtro de respuesta finita al impulso)')
menu={1:'Filtrar, graficar o escuchar un audio determinado',2:'Salir del programa'} #menu para facilidad de uso del usuario
accion=0
while accion!=2: #mientras el usuario no escoja el 2 que es para salir, el programa comienza a correr
    for opcion in menu.keys(): 
        print(opcion,menu[opcion]) #imprime el menu 
    accion=int(input('¿Que desea hacer? ')) #le solicita al usuario que desea hacer siguiendo el menú
    if accion==1: #cuando el usuario escoge 1
        #Comienza el proceso para ejecutar el archivo .wav para luego poder filtrarlo, recibe un archivo .wav y genera otro archivo .wav   
        archivo_a_filtrar=input ('Escriba la ruta completa del archivo formato .wav que desea filtrar: ') #el usuario debe ingresar la ruta de donde se encuentra el archivo que desea ingresar para procesar
        print('Procesando...')
        frecuencia, x= waves.read(archivo_a_filtrar) #lectura del archivo .wav, entrega como resultado la frecuencia del audio y los datos en un array
        if frecuencia!=8000: #cuando la frecuencia del audio ingresado es diferente de 8000 no se obtendrá un resultado satisfactorio
            print('No se obtendrá un resultado satisfactorio debido a que la frecuencia del audio seleccionado es diferente de 8000 Hz')
        k=[1.6687317037448562e-16,-0.03551153864045256,-1.7257607380175936e-16,0.10653199877675365,1.9371078815074347e-16,-0.18642779737756615,-6.256569336689685e-17,0.2219393360180186,-6.245004513516506e-17,-0.18642779737756615,1.9371078815074347e-16,0.10653199877675364,-1.7257607380175936e-16,-0.03551153864045256,1.6687317037448562e-16] #coeficientes dados para la utilización en la ecuación para el filtro
        y=[] 
        for elemento in range(len(x)): #tomar la longitud de los datos del audio ingresado 
            if elemento>=14: #de la posición 14 en adelante entra este if, ya que las x anteriores no se pueden utilizar bien en la ecuación
                c=0 #c como contador
                ecuacion=0 
                for bk in k: #evalúa todos los valores en la lista k
                    ecuacion+=bk*x[elemento-c] #agregarle a ecuación el resultado del valor de bk en ese momento multiplicado por el valor de x evaluado en una posición que se va a restar por c (contador) entonces cada vez que contador sume 1 le va a restar más a la posición de x, así se ejecuta correctamente la ecuación
                    c+=1 #suma 1 a c para que luego reste más a la posición de x
                y.append(ecuacion) #cuando acabe con todos los valores de bk, agreguele a la lista [y] el valor resultante de la ecuación
            else:
                y.append(0) #cuando x está en una posición menor a 14 agrega 0 a esos valores en y, ya que no se pueden calcular       
        audio_filtrado = np.asarray(y,dtype="int16") #se convierte [y] de una lista a un array de tipo int16 para lograr escribir el archivo .wav con este último
        archivo=input('Ingrese el nombre que desea colocarle al archivo filtrado: ') #el usuario ingresa el nombre que guste ponerle al archivo resultante
        ruta=input('Ingrese la ruta donde desea guardar el archivo filtrado: ') #el usuario elige la ruta de donde guardar el archivo
        waves.write(str(ruta)+"\\"+ str(archivo)+'.wav', frecuencia, audio_filtrado) #se escribe el nuevo archivo .wav, se indica la ruta donde se quiere guardar, el nombre, la frecuencia y los datos que provienen del archivo ya filtrado
        print('El archivo se guardó exitosamente en la ruta que indicó')        
        menu_2={1:'Escuchar audio sin filtrar',2:'Escuchar audio filtrado',3:'Graficar los audios', 4:'Regresar al menú principal'} #menu 2 para facilitar el uso del usuario
        accion_2=0
        while accion_2!=4: #mientras la opción elegida por el usuario no sea la 4 de volver al menú principal
            for opcion in menu_2.keys(): 
                print(opcion,menu_2[opcion]) #imprimir las opciones
            accion_2=int(input('¿Que desea hacer? '))    
            if accion_2==1:
                #reproduce el archivo original
                print("Reproduciendo archivo sin filtrar")
                winsound.PlaySound((archivo_a_filtrar), winsound.SND_FILENAME) #se indica que se quiere que se reproduzca un archivo y que se le está indicando el nombre
            if accion_2==2:
                #reproduce el archivo 'filtrado' 
                print("Reproduciendo archivo filtrado")
                filtrado=str(ruta)+"\\"+ str(archivo)+'.wav' #se indica la ruta más el nombre del archivo para que la biblioteca pueda reproducirlo
                winsound.PlaySound(filtrado, winsound.SND_FILENAME) #se indica que se quiere que se reproduzca un archivo y que se le está indicando el nombre
            if accion_2==3:           
                #graficar el audio, el usuario decide la cantidad de muestras que desea graficar, genera gráficas de ambos audios
                muestras=int(input('Escriba el número de muestras que desea graficar (máximo 24000): ')) #el usuario indica el número de muestras que desea graficar
                grafica_original=x[0:(muestras)] #tomar los valores del audio original desde 0 hasta el número de muestras para graficarlo
                grafica_filtrada=audio_filtrado[0:(muestras)] #tomar los valores del audio filtrado desde 0 hasta el número de muestras para graficarlo
                tiempo=np.linspace(start=0, stop=muestras/frecuencia, num=muestras) #para delimitar los datos en el eje x, inicia en 0, termina en la cantidad de muestras dividido por la frecuencia y la cantidad de muestras deseadas
                plt.title('Gráfica de audios') #título gráfica
                plt.xlabel('Tiempo(s)') #nombre valores x
                plt.ylabel('Amplitud') #nombre valores y
                plt.plot(tiempo, grafica_original) #graficar el audio sin filtrar
                plt.plot(tiempo, grafica_filtrada, color='green') #graficar el audio filtrado en color verde
                plt.legend(['Gráfica original', 'Gráfica filtrada']) #agregar un recuadro pequeño a la gráfica para que indique cual línea es de la de cada audio
                plt.show() #mostrar la gráfica
    if accion==2:
        #finaliza el programa
        print('El programa finalizó')