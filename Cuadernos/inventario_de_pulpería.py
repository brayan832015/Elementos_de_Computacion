#Programa definido en una función para controlar el inventario de una pulperia. 
def inventario_pulperia(): #Para poder correr todo el programa llamando a esta función.
    inventario={'arroz':10,'frijoles':15,'refresco':5,'galletas':8,'harina':3,'gelatina':2,'yogurt':4,'helados':15,'jalea':1,'pan':12} #Diccionario para definir los productos existentes en el inventario.
    menu={1:'Ver el inventario actual',2:'Ver un producto',3:'Agregar al inventario',4:'Salir'} #Diccionario para definir las opciones a elegir.
    accion=0 #Para que cuando se elija la opción 4 sea posible, cuando se quiera, volver a ejecutar el programa.
    while accion!=4: #Mientras la acción que se ingrese sea diferente de 4 el programa continúa ejecutándose.
        for opcion in menu.keys(): #Para cada opción en el menú.
            print(opcion,menu[opcion]) #Imprima la opción y la acción que realiza.  
        accion=int(input('¿Que desea hacer? Escoja una opción:'))                     
        if accion==1: #Cuando se escoje la opción 1. 
            print('Los productos existentes son:')
            for producto in inventario.keys(): #Para cada producto en el inventario.
                print(producto,inventario[producto]) #Imprima el producto y la cantidad existente.
        if accion==2:
            ver_producto=input('Escriba el producto que desea observar:')#Producto que se desea buscar
            ver_producto_min=ver_producto.lower() #Pasar a minúscula todo el texto para evitar problemas a la hora de buscar el producto.
            verdadero=0 
            for producto in inventario.keys():    
                if ver_producto_min==producto: #Si el producto ingresado es igual a un producto existente.
                    print('El producto que consultó fue',producto,'hay',inventario[producto])
                    verdadero=1 #Verdadero es 1 si el producto ingresado se encuentra en el inventario.
            if verdadero!=1: #Verdadero es diferente de 1 si el producto ingresado no se encuentra en el inventario.
                print('El producto que consultó no se encuentra en el inventario')        
        if accion==3:
            product_agregar=input('Escriba el producto que desea agregar al inventario:')#Producto a agregar
            cant_agregar=int(input('Escriba la cantidad a agregar:'))#Cantidad a agregar
            product_agregar_min=product_agregar.lower()
            verdadero=0
            for producto in inventario.keys():    
                if product_agregar_min==producto:#Si el producto que desea agregarse ya se encuentra en el inventario.
                    verdadero=1 
                    inventario[producto] = inventario[producto]+cant_agregar #Agregar al inventario de ese producto la cantidad deseada.
                    print('Se añadió',cant_agregar,'a',producto,'ahora hay',inventario[producto])
            if verdadero!=1: #Si verdadero es diferente de 1 significa que el producto que se quiere agregar no está en el inventario, por lo tanto hay que añadirlo.
                inventario[product_agregar_min] = cant_agregar #Agregar: inventario [aquí se ingresa el producto a agregar]= aquí se ingresa la cantidad a agregar.
                print('Se añadió',product_agregar_min,'al inventario, ahora hay',cant_agregar)
        if accion==4: #Si la acción seleccionada es 4 el programa finaliza.
            print('El programa finalizó')
inventario_pulperia()