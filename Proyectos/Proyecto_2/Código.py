import pygame
from pygame import mixer
import random
import sys
pygame.font.init()
pygame.init()
reloj=pygame.time.Clock()
fps=60 #Para la fluidez del juego
puntaje=0 #puntaje para los highscores

#parametros de la ventana
pygame.display.set_caption('Space Invaders (Brayan Barquero)') #título ventana
ancho_ventana=970
alto_ventana=600
ventana=pygame.display.set_mode((ancho_ventana,alto_ventana)) #crear ventana
fondo=pygame.image.load("Imagenes/FONDO.jpg") #cargar fondo


def Highscore():
    f=open("Imagenes/highscores.txt",'a') #abre el archivo que se encuentra en la carpeta imagenes (al inicio el top 5 son ceros)
    f.write(str(puntaje)) #escribe el puntaje obtenido en el archivo de texto
    f.write(", ")
    f.close() #cierra el archivo


def mostrar_texto(texto,font,color_texto,x,y):#para mostrar texto en la ventana
    imagen=font.render(texto,True,color_texto)
    ventana.blit(imagen,(x,y)) #mostrar en la ventana
    

def cerrar_ventana():#cerrar ventana
    for accion in pygame.event.get():
        if accion.type==pygame.QUIT:#si la acción es cerrar se cierra la ventana
            pygame.quit()
            sys.exit()
            
            
#letras
letra_2=pygame.font.SysFont('Aharoni', 60) 
letra_1=pygame.font.SysFont('Aharoni', 20)
letra=pygame.font.SysFont('Aharoni', 40)
blanco=(255,255,255) #color para la letra
               
#juego para un jugador recibe filas de aliens, tiempo de recarga de los aliens, velocidad de movimiento de la nave y la velocidad de la recarga de la nave
def juego(filas,columnas,tiempo_disp_alien,velocidad_movimiento_nave,vel_recarga_nave):
    global puntaje #usar la variable puntaje como global
    puntaje=0 #para resetear a 0 el puntaje cada vez que se inicia un nuevo juego
    
    #sonidos
    pygame.mixer.pre_init(22050,-16,2,4096) # para establecer los valores predeterminados apropiados antes de usar init de nivel superior (frequency, size, channels, buffersize) 
    mixer.init() #se llama al init
    explosion_fx=pygame.mixer.Sound('Imagenes/invaderkilled.wav') #cargar el sonido de explosion
    explosion_fx.set_volume(0.25) #configurar volumen sonido
    explosion2_fx=pygame.mixer.Sound('Imagenes/explosion.wav')
    explosion2_fx.set_volume(0.25)
    laser_fx=pygame.mixer.Sound('Imagenes/shoot.wav')
    laser_fx.set_volume(0.25)
    disparo_alien_fx=pygame.mixer.Sound('Imagenes/fastinvader1.wav')
    disparo_alien_fx.set_volume(0.25)
    victoria_fx=pygame.mixer.Sound('Imagenes/ganador.mp3')
    victoria_fx.set_volume(0.25)
    derrota_fx=pygame.mixer.Sound('Imagenes/perdedor.mp3')
    derrota_fx.set_volume(0.20)
    obstaculo_fx=pygame.mixer.Sound('Imagenes/obst.wav')
    obstaculo_fx.set_volume(0.25)
    
    
    #parametros generales
    ult_disp_alien= pygame.time.get_ticks() #el ultimo disparo de los aliens
    game_over=0 #game over es 0 cuando aún no se ha perdido ni ganado
    vidas=3 #en el modo un jugador vidas es igual a 3
    estado=3 #estado de los obstaculos
    contador=0 #se usa al finalizar el juego para no entrar en bucles
    
    
    #Funciones ventana
    def mostrar_fondo(): #muestra el fondo, las vidas y la puntuación
        ventana.blit(fondo,(0,0)) #mostrar la imagen de fondo en el punto de inicio 0,0
        puntaje_pantalla=letra.render(f'Puntaje: {puntaje}',1,blanco) #mostrar la variable puntaje mientras se juega
        ventana.blit(puntaje_pantalla,(10,10)) #muestra el puntaje en el inicio 10,10
        mostrar_texto('VIDAS:',letra_1,blanco,int(ancho_ventana/2-470),int(alto_ventana/2+240)) #muestra el texto vidas justo arriba de las imagenes de las naves que indican la cantidad de vidas
        if nave.vidas==3:#muestra 3 naves para indicar que hay 3 vidas
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(105,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(60,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(15,560))
        if nave.vidas==2:#muestra 2 naves para indicar que hay 2 vidas
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(60,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(15,560))
        if nave.vidas==1:#muestra 1 nave para indicar que hay 1 vida
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(15,560))
            
    
    def crear_aliens(): #crea aliens
        for fila in range(filas): #filas aliens
            for columna in range(columnas): #columnas aliens
                alien = Aliens(125+columna*80,100+fila*70) #generar alien en esa posicion
                grupo_alien.add(alien) #agregar al alien creado al grupo de aliens
                
          
    #Clase nave           
    class Nave(pygame.sprite.Sprite): #sprite para crear el objeto de la nave independiente al resto de objetos
        def __init__(self,x,y):   
            pygame.sprite.Sprite.__init__(self) #constructor de la nave
            self.image=pygame.image.load("Imagenes/nave.png") #carga la imagen de la nave
            self.rect=self.image.get_rect() #dibujar un rectangulo
            self.rect.center=[x,y] 
            self.vidas=vidas 
            self.ultimo_disparo=pygame.time.get_ticks() #ultimo disparo de la nave para que pueda disparar cada cierto tiempo
            self.contacto=pygame.mask.from_surface(self.image) #solo se contacta con la nave solo si le pega en sí a la nave, no al rectangulo generado anteriormente
        def update(self): #actualizar
            game_over=0
            tecla=pygame.key.get_pressed()
            tiempo=pygame.time.get_ticks()
            if tecla[pygame.K_LEFT] and self.rect.left>0: #mover a la izquierda sin que pase los bordes (límites)
                self.rect.x-=velocidad_movimiento_nave #se mueve conforme la velocidad establecida
            if tecla[pygame.K_RIGHT] and self.rect.right<ancho_ventana: #mover a la derecha sin que pase los bordes (límites)
                self.rect.x+=velocidad_movimiento_nave #se mueve conforme la velocidad establecida
            if tecla[pygame.K_SPACE] and tiempo-self.ultimo_disparo>vel_recarga_nave: #disparar cada cierto tiempo
                laser_fx.play() #reproduce el sonido de laser
                bala=Balas(self.rect.centerx,self.rect.top) #para que la bala salga del centro de la nave
                grupo_bala.add(bala) #agrega bala al grupo de balas
                self.ultimo_disparo=tiempo
            if self.vidas<=0: #si las vidas llegan a 0 elimine a la nave y game over es -1
                self.kill()
                game_over=-1
            return game_over
        
        
    #Clase balas de la nave
    class Balas(pygame.sprite.Sprite): 
        def __init__(self,x,y):   
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load("Imagenes/disparo.png") #cargar imagen de bala
            self.rect=self.image.get_rect()
            self.rect.center=[x,y]
        def update(self):
            self.rect.y-=7 #velocidad de movimiento de la bala
            if self.rect.bottom<100: #para que no llegue hasta arriba de la ventana sino que apenas salga del cuadro de juego se elimine
                self.kill()
            if pygame.sprite.spritecollide(self, grupo_alien, True):#si la bala toca al grupo alien suma a puntaje, pone el sonido de explosion y elimina al alien
                global puntaje
                self.kill()          
                explosion_fx.play()
                puntaje+=1
                
                
    #Clase aliens
    class Aliens(pygame.sprite.Sprite): 
        def __init__(self,x,y):   
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load("Imagenes/enemigo" + str(random.randint(1,3)) + ".png") #cargar las imagenes de los aliens de forma aleatoria, alternando entre los 3 aliens
            self.rect=self.image.get_rect()
            self.rect.center=[x,y]
            self.mover_disparo=0 #para que el dispario sea movido de un alien a otro aleatoriamente
            self.mover_direccion=1 #para que se muevan los aliens de izquierda a derecha
        def update(self):
            self.rect.x+=self.mover_direccion #mover aliens
            self.mover_disparo+=1 #mover disparo
            if abs(self.mover_disparo)>100: #cuando se llega al borde se cambia la dirección del movimiento
                self.mover_direccion *=-1
                self.mover_disparo*=self.mover_direccion
                
                
    #Clase balas de los aliens
    class Alien_Balas(pygame.sprite.Sprite): 
        def __init__(self,x,y):   
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load("Imagenes/disparoalien.png")
            self.rect=self.image.get_rect()
            self.rect.center=[x,y]
            disparo_alien_fx.play() #reproduce el sonido de disparo alien
        def update(self):
            self.rect.y+=4 #velocidad de movimiento de las balas de los aliens
            if self.rect.top>alto_ventana: #elimina la bala al llegar al fondo
                self.kill()
            if pygame.sprite.spritecollide(self, grupo_nave, False, pygame.sprite.collide_mask): #si toca una bala con la nave, le quita una vida, le resta a puntaje y se reproduce una explosion, se llama a mostrar fondo para actualizar el fondo y las vidas de la nave
                global puntaje
                self.kill()
                explosion2_fx.play()
                nave.vidas-=1
                puntaje-=1
                mostrar_fondo()
    
    
    class Obstaculos(pygame.sprite.Sprite): 
        def __init__(self,x,y):   
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load("Imagenes/obstaculo1.png")
            self.rect=self.image.get_rect()
            self.rect.center=[x,y]
            self.estado=estado
            self.contacto=pygame.mask.from_surface(self.image)
        def update(self):
            if pygame.sprite.spritecollide(self, grupo_bala_alien, True) or pygame.sprite.spritecollide(self, grupo_bala, True): #si el obstaculo es impactado por una bala (alien o de la nave) 
                self.estado-=1 #se resta al estado
                obstaculo_fx.play() #y se reproduce un sonido
            if self.estado==2:
                self.image=pygame.image.load('Imagenes/obstaculo2.png') #carga la imagen con 1 impacto
            if self.estado==1:
                self.image=pygame.image.load('Imagenes/obstaculo3.png') #carga la imagen con 2 impactos
            if self.estado<=0: #si estado es 0 elimina el obstaculo
                self.kill()
            
                
    #Grupos de clases
    grupo_nave=pygame.sprite.Group()
    grupo_bala=pygame.sprite.Group()
    grupo_alien=pygame.sprite.Group()
    grupo_bala_alien=pygame.sprite.Group()
    grupo_obstaculos=pygame.sprite.Group()
    
    
    #Ejecución de funciones
    crear_aliens()
    obstaculo_1=Obstaculos(int(ancho_ventana-836),alto_ventana-170)
    obstaculo_2=Obstaculos(int(ancho_ventana-660),alto_ventana-170)
    obstaculo_3=Obstaculos(int(ancho_ventana-484),alto_ventana-170)
    obstaculo_4=Obstaculos(int(ancho_ventana-308),alto_ventana-170)
    obstaculo_5=Obstaculos(int(ancho_ventana-132),alto_ventana-170)
    grupo_obstaculos.add(obstaculo_5, obstaculo_4, obstaculo_3,obstaculo_2,obstaculo_1) #agregar los obstaculos al grupo
    nave=Nave(int(ancho_ventana/2),alto_ventana-100)
    grupo_nave.add(nave) #agregar nave al grupo
    
    
    #Verificar si se está ejecutando el juego
    ejecutando=True #el juego no se ha cerrado
    while ejecutando:
        reloj.tick(fps) #fluidez o refresco del juego
        mostrar_fondo()
        tiempo=pygame.time.get_ticks()
        if tiempo - ult_disp_alien>tiempo_disp_alien and len(grupo_bala_alien)<5 and len(grupo_alien) > 0:#los aliens no pueden tener mas de 5 balas al mismo tiempo, no pueden atacar si no ha pasado el tiempo para recargar y si no hay aliens no hay cual dispare
            alien_atacando= random.choice(grupo_alien.sprites()) #uno dispara aleatoriamente
            bala_alien = Alien_Balas(alien_atacando.rect.centerx,alien_atacando.rect.bottom) #la bala sale del centro del alien que atacó
            grupo_bala_alien.add(bala_alien) #se agregala bala del alien al grupo
            ult_disp_alien=tiempo #se actualiza el tiempo de recarga
            
            
        if len(grupo_alien)==0:#si ya no quedan aliens ganó
            game_over=1
            
            
        if game_over==0: #si aún quedan aliens no se ha terminado el juego
            game_over= nave.update()
            for accion in pygame.event.get():
                if accion.type==pygame.QUIT: #si se elije cerrar el juego termina
                    ejecutando=False #sale del while porque se hace false
                    pygame.quit()
                    
            
            #actualizar grupos
            grupo_bala.update()
            nave.update()
            grupo_alien.update()
            grupo_bala_alien.update()
            grupo_obstaculos.update()
            
        
        if game_over==-1: #derrota (sin vidas)
            mostrar_texto('USTED PERDIÓ',letra,blanco,int(ancho_ventana/2-110),int(alto_ventana/2+50)) #muestra texto en pantalla
            mostrar_texto('Presione M para volver al menú',letra,blanco,int(ancho_ventana/2-400),int(alto_ventana/2+150))
            while contador==0:
                Highscore() #se llama a highscore para que guarde el puntaje obtenido en el documento de texto
                derrota_fx.play()
                contador+=1 #con este se rompe un posible bucle al finalizar
            tecla=pygame.key.get_pressed()
            if tecla[pygame.K_m]:#si se presiona m se vuelve al menú principal
                menu()

            
        if game_over==1: #victoria (no quedan aliens)
            mostrar_texto('USTED GANÓ!',letra,blanco,int(ancho_ventana/2-110),int(alto_ventana/2+50))
            mostrar_texto('Presione M para volver al menú',letra,blanco,int(ancho_ventana/2-400),int(alto_ventana/2+150))
            while contador==0:
                Highscore()
                victoria_fx.play()
                contador+=1
            tecla=pygame.key.get_pressed()
            if tecla[pygame.K_m]:    
                menu()
                
                
        #mostrar en la ventana los grupos 
        grupo_nave.draw(ventana)
        grupo_bala.draw(ventana)
        grupo_alien.draw(ventana)
        grupo_bala_alien.draw(ventana)
        grupo_obstaculos.draw(ventana)
        pygame.display.update() #actualizar ventana
        cerrar_ventana()
            
#juego para el modo 2 jugadores, el funcionamiento es igual al de 1 jugador solo que se agrega una nave y balas para esa nave
def juego_2(filas,columnas,tiempo_disp_alien,velocidad_movimiento_nave,vel_recarga_nave):
    global puntaje
    puntaje=0
    
    #sonidos
    pygame.mixer.pre_init(44100,-16,2,512)
    mixer.init()
    explosion_fx=pygame.mixer.Sound('Imagenes/invaderkilled.wav')
    explosion_fx.set_volume(0.25)
    explosion2_fx=pygame.mixer.Sound('Imagenes/explosion.wav')
    explosion2_fx.set_volume(0.25)
    laser_fx=pygame.mixer.Sound('Imagenes/shoot.wav')
    laser_fx.set_volume(0.25)
    disparo_alien_fx=pygame.mixer.Sound('Imagenes/fastinvader1.wav')
    disparo_alien_fx.set_volume(0.25)
    victoria_fx=pygame.mixer.Sound('Imagenes/ganador.mp3')
    victoria_fx.set_volume(0.25)
    derrota_fx=pygame.mixer.Sound('Imagenes/perdedor.mp3')
    derrota_fx.set_volume(0.20)
    obstaculo_fx=pygame.mixer.Sound('Imagenes/obst.wav')
    obstaculo_fx.set_volume(0.25)
    
    
    #parametros generales
    ult_disp_alien= pygame.time.get_ticks()
    game_over=0
    vidas=6  #en este las vidas son 6
    estado=3
    contador=0
    
    
    #Funciones ventana
    def mostrar_fondo():
        ventana.blit(fondo,(0,0))
        puntaje_pantalla=letra.render(f'Puntaje: {puntaje}',1,blanco)
        ventana.blit(puntaje_pantalla,(10,10))
        mostrar_texto('VIDAS:',letra_1,blanco,int(ancho_ventana/2-470),int(alto_ventana/2+240))
        if nave.vidas==6: #se tienen que mostrar más naves que en la anterior ya que son 6 vidas
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(240,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(195,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(150,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(105,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(60,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(15,560))
        if nave.vidas==5:
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(195,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(150,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(105,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(60,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(15,560))
        if nave.vidas==4:
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(150,560)) 
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(105,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(60,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(15,560))
        if nave.vidas==3:
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(105,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(60,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(15,560))
        if nave.vidas==2:
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(60,560))
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(15,560))
        if nave.vidas==1:
            ventana.blit(pygame.transform.scale(nave.image, (25,25)),(15,560))
            
    
    def crear_aliens():
        for fila in range(filas):
            for columna in range(columnas):
                alien = Aliens(125+columna*80,100+fila*70)
                grupo_alien.add(alien)
                
          
    #Clase nave           
    class Nave(pygame.sprite.Sprite): 
        def __init__(self,x,y):   
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load("Imagenes/nave.png")
            self.rect=self.image.get_rect()
            self.rect.center=[x,y]
            self.vidas=vidas
            self.ultimo_disparo=pygame.time.get_ticks()
            self.contacto=pygame.mask.from_surface(self.image)
        def update(self):
            game_over=0
            tecla=pygame.key.get_pressed()
            if tecla[pygame.K_LEFT] and self.rect.left>0:
                self.rect.x-=velocidad_movimiento_nave
            if tecla[pygame.K_RIGHT] and self.rect.right<ancho_ventana:
                self.rect.x+=velocidad_movimiento_nave  
            tiempo=pygame.time.get_ticks()
            if tecla[pygame.K_SPACE] and tiempo-self.ultimo_disparo>vel_recarga_nave:
                laser_fx.play()
                bala=Balas(self.rect.centerx,self.rect.top)
                grupo_bala.add(bala)
                self.ultimo_disparo=tiempo
            if self.vidas<=0:
                self.kill()
                game_over=-1
            return game_over
        
        
    #Clase balas de la nave
    class Balas(pygame.sprite.Sprite): 
        def __init__(self,x,y):   
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load("Imagenes/disparo.png")
            self.rect=self.image.get_rect()
            self.rect.center=[x,y]
        def update(self):
            self.rect.y-=7
            if self.rect.bottom<100:
                self.kill()
            if pygame.sprite.spritecollide(self, grupo_alien, True):
                global puntaje
                self.kill()          
                explosion_fx.play()
                puntaje+=1
                
                
    #Clase aliens
    class Aliens(pygame.sprite.Sprite): 
        def __init__(self,x,y):   
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load("Imagenes/enemigo" + str(random.randint(1,3)) + ".png")
            self.rect=self.image.get_rect()
            self.rect.center=[x,y]
            self.mover_disparo=0
            self.mover_direccion=1
        def update(self):
            self.rect.x+=self.mover_direccion
            self.mover_disparo+=1
            if abs(self.mover_disparo)>100:
                self.mover_direccion *=-1
                self.mover_disparo*=self.mover_direccion
                
                
    #Clase balas de los aliens
    class Alien_Balas(pygame.sprite.Sprite): 
        def __init__(self,x,y):   
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load("Imagenes/disparoalien.png")
            self.rect=self.image.get_rect()
            self.rect.center=[x,y]
            disparo_alien_fx.play()
        def update(self):
            self.rect.y+=4
            if self.rect.top>alto_ventana:
                self.kill()
            if pygame.sprite.spritecollide(self, grupo_nave, False, pygame.sprite.collide_mask):
                global puntaje
                puntaje-=1
                self.kill()
                explosion2_fx.play()
                nave.vidas-=1
                mostrar_fondo()
    
    
    class Obstaculos(pygame.sprite.Sprite): 
        def __init__(self,x,y):   
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load("Imagenes/obstaculo1.png")
            self.rect=self.image.get_rect()
            self.rect.center=[x,y]
            self.estado=estado
            self.contacto=pygame.mask.from_surface(self.image)
        def update(self):
            if pygame.sprite.spritecollide(self, grupo_bala_alien, True) or pygame.sprite.spritecollide(self, grupo_bala, True):
                self.estado-=1
                obstaculo_fx.play()
            if self.estado==2:
                self.image=pygame.image.load('Imagenes/obstaculo2.png')
            if self.estado==1:
                self.image=pygame.image.load('Imagenes/obstaculo3.png')
            if self.estado<=0:
                self.kill()
     
            
    class Nave_2(pygame.sprite.Sprite): #clase para definir la nave del segundo jugador, es exactamente igual que la del primer jugador, la única diferencia es que se mueve con A y D y dispara con S
        def __init__(self,x,y):   
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load("Imagenes/nave.png")
            self.rect=self.image.get_rect()
            self.rect.center=[x,y]
            self.vidas=vidas
            self.ultimo_disparo=pygame.time.get_ticks()
            self.contacto=pygame.mask.from_surface(self.image)
        def update(self):
            game_over=0
            tecla=pygame.key.get_pressed()
            if tecla[pygame.K_a] and self.rect.left>0:
                self.rect.x-=velocidad_movimiento_nave
            if tecla[pygame.K_d] and self.rect.right<ancho_ventana:
                self.rect.x+=velocidad_movimiento_nave  
            tiempo=pygame.time.get_ticks()
            if tecla[pygame.K_s] and tiempo-self.ultimo_disparo>vel_recarga_nave:
                laser_fx.play()
                bala=Balas(self.rect.centerx,self.rect.top)
                grupo_bala.add(bala)
                self.ultimo_disparo=tiempo
            if self.vidas<=0:
                self.kill()
                game_over=-1
            return game_over
        
        
    #Clase balas de la segunda nave
    class Balas_2(pygame.sprite.Sprite): 
        def __init__(self,x,y):   
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load("Imagenes/disparo.png")
            self.rect=self.image.get_rect()
            self.rect.center=[x,y]
        def update(self):
            self.rect.y-=7
            if self.rect.bottom<100:
                self.kill()
            if pygame.sprite.spritecollide(self, grupo_alien, True):
                self.kill()          
                explosion_fx.play()     
        
           
    #Grupos de clases
    grupo_nave=pygame.sprite.Group()
    grupo_bala=pygame.sprite.Group()
    grupo_alien=pygame.sprite.Group()
    grupo_bala_alien=pygame.sprite.Group()
    grupo_obstaculos=pygame.sprite.Group()
    
    
    #Ejecución de funciones
    crear_aliens()
    obstaculo_1=Obstaculos(int(ancho_ventana-836),alto_ventana-170)
    obstaculo_2=Obstaculos(int(ancho_ventana-660),alto_ventana-170)
    obstaculo_3=Obstaculos(int(ancho_ventana-484),alto_ventana-170)
    obstaculo_4=Obstaculos(int(ancho_ventana-308),alto_ventana-170)
    obstaculo_5=Obstaculos(int(ancho_ventana-132),alto_ventana-170)
    grupo_obstaculos.add(obstaculo_5, obstaculo_4, obstaculo_3,obstaculo_2,obstaculo_1)
    nave=Nave(int(ancho_ventana/2),alto_ventana-100)
    nave_2=Nave_2(int(ancho_ventana/2),alto_ventana-100) 
    grupo_nave.add(nave, nave_2) #nave 2 igual forma parte del grupo nave, por lo tanto, al ser impactada también resta a la cantidad de vidas
    
    
    #Verificar si se está ejecutando el juego
    ejecutando=True
    while ejecutando:
        reloj.tick(fps)
        mostrar_fondo()
        tiempo=pygame.time.get_ticks()
        if tiempo - ult_disp_alien>tiempo_disp_alien and len(grupo_bala_alien)<5 and len(grupo_alien) > 0:
            alien_atacando= random.choice(grupo_alien.sprites())
            bala_alien = Alien_Balas(alien_atacando.rect.centerx,alien_atacando.rect.bottom)
            grupo_bala_alien.add(bala_alien)
            ult_disp_alien=tiempo
            
            
        if len(grupo_alien)==0:#si ya no quedan aliens ganó
            game_over=1
            
            
        if game_over==0: #si aún quedan aliens no se ha terminado el juego
            game_over= nave.update()
            for accion in pygame.event.get():
                if accion.type==pygame.QUIT: #si se elije cerrar el juego termina
                    ejecutando=False
                    pygame.quit()
                    
            
            #actualizar grupos
            grupo_bala.update()
            nave.update()
            nave_2.update()
            grupo_alien.update()
            grupo_bala_alien.update()
            grupo_obstaculos.update()
            
        
        if game_over==-1: #derrota (sin vidas)
            mostrar_texto('USTED PERDIÓ',letra,blanco,int(ancho_ventana/2-110),int(alto_ventana/2+50))
            mostrar_texto('Presione M para volver al menú',letra,blanco,int(ancho_ventana/2-400),int(alto_ventana/2+150))
            while contador==0:
                Highscore()
                derrota_fx.play()
                contador+=1
            tecla=pygame.key.get_pressed()
            if tecla[pygame.K_m]:    
                menu()

            
        if game_over==1: #victoria (no quedan aliens)
            mostrar_texto('USTED GANÓ!',letra,blanco,int(ancho_ventana/2-110),int(alto_ventana/2+50))
            mostrar_texto('Presione M para volver al menú',letra,blanco,int(ancho_ventana/2-400),int(alto_ventana/2+150))
            while contador==0:
                Highscore()
                victoria_fx.play()
                contador+=1
            tecla=pygame.key.get_pressed()
            if tecla[pygame.K_m]:    
                menu()
        
        
        #mostrar en la ventana los grupos 
        grupo_nave.draw(ventana)
        grupo_bala.draw(ventana)
        grupo_alien.draw(ventana)
        grupo_bala_alien.draw(ventana)
        grupo_obstaculos.draw(ventana)
        pygame.display.update()
        cerrar_ventana()


   
def menu(): #menú al inicio del juego
    ejecutando=True #mientras no se cierre la ventana
    while ejecutando:
        ventana.blit(fondo,(0,0))
        #mostrar texto de las opciones del menú
        mostrar_texto('MENÚ PRINCIPAL', letra_2, blanco, ancho_ventana-950, alto_ventana-400)
        mostrar_texto('Mantenga presionado 1 para jugar en el modo un jugador', letra, blanco, ancho_ventana-950, alto_ventana/2)
        mostrar_texto('Mantenga presionado 2 para jugar en el modo 2 jugadores', letra, blanco, ancho_ventana-950, alto_ventana/2+50)
        mostrar_texto('Mantenga presionado 3 para ayuda', letra, blanco, ancho_ventana-950, alto_ventana/2+100)
        mostrar_texto('Mantenga presionado 4 para ver los highscores', letra, blanco, ancho_ventana-950,alto_ventana/2+150)
        
        tecla=pygame.key.get_pressed()
        if tecla[pygame.K_1]: #si la tecla es 1
            ventana.blit(fondo,(0,0))
            #mostrar texto de dificultades a elegir
            mostrar_texto('ESCOJA LA DIFICULTAD', letra_2, blanco, ancho_ventana-950, alto_ventana-400)
            mostrar_texto('Digite F para fácil', letra, blanco, ancho_ventana-950, alto_ventana/2)
            mostrar_texto('Digite I para intermedio', letra, blanco, ancho_ventana-950, alto_ventana/2+50)
            mostrar_texto('Digite D para difícil', letra, blanco, ancho_ventana-950, alto_ventana/2+100)
            if tecla[pygame.K_f]:#si se eligió fácil
                juego(2,10,750,5,750) #la nave recarga rápido, los aliens recargan lento,la velocidad de la nave es alta y hay 2 filas de aliens
            if tecla[pygame.K_i]:#si se eligió intermedio
                juego(3,10,500,3,1000)#la nave recarga medio, los aliens recargan medio,la velocidad de la nave es media y hay 3 filas de aliens
            if tecla[pygame.K_d]:#si se eligió difícil
                juego(3,10,300,2,1500)#la nave recarga lento, los aliens recargan rápido,la velocidad de la nave es baja y hay 3 filas de aliens
            pygame.display.update()  
            
            
        if tecla[pygame.K_2]:#en multijugador es la misma configuración
            ventana.blit(fondo,(0,0))
            mostrar_texto('ESCOJA LA DIFICULTAD', letra_2, blanco, ancho_ventana-950, alto_ventana-400)
            mostrar_texto('Digite F para fácil', letra, blanco, ancho_ventana-950, alto_ventana/2)
            mostrar_texto('Digite I para intermedio', letra, blanco, ancho_ventana-950, alto_ventana/2+50)
            mostrar_texto('Digite D para difícil', letra, blanco, ancho_ventana-950, alto_ventana/2+100)
            if tecla[pygame.K_f]:
                juego_2(2,10,750,5,750)
            if tecla[pygame.K_i]:
                juego_2(3,10,500,3,1000)
            if tecla[pygame.K_d]:
                juego_2(3,10,300,2,1500)
            pygame.display.update() 
            
            
        if tecla[pygame.K_3]:#si se eligió 3 (ayuda), se muestra un texto con especificaciones básicas del juego
            ventana.blit(fondo,(0,0))
            mostrar_texto('AYUDA', letra_2, blanco, ancho_ventana-950, alto_ventana-580)
            mostrar_texto('Este juego consta de acabar con los aliens en su totalidad antes de perder las vidas de nuestra nave, se cuenta con dos modos de juego: un jugador y', letra_1, blanco, ancho_ventana-950, alto_ventana-525)
            mostrar_texto('dos jugadores, en el modo de un jugador, una única nave se enfrenta con todos los aliens, contando con 3 vidas, en este modo podemos disparar ', letra_1, blanco, ancho_ventana-950, alto_ventana-500)
            mostrar_texto('pulsando la tecla ESPACIO y movernos con las flechas del teclado (izquierda y derecha), si logramos acabar con todos los aliens ganamos, por el ', letra_1, blanco, ancho_ventana-950, alto_ventana-475)
            mostrar_texto('contrario si los aliens acaban con nosotros perdemos, también tenemos el modo de dos jugadores donde, en modo cooperativo se enfrentan contra los ', letra_1, blanco, ancho_ventana-950, alto_ventana-450)
            mostrar_texto('aliens, cuentan con 6 vidas compartidas entre ambos y su objetivo es el mismo, acabar con todos los aliens, en este modo utilizamos los ', letra_1, blanco, ancho_ventana-950, alto_ventana-425)
            mostrar_texto('controles del primer modo y la segunda nave se controla con las teclas A y D para moverse a izquierda y derecha y la tecla S para disparar, ', letra_1, blanco, ancho_ventana-950, alto_ventana-400)
            mostrar_texto('ambos modos cuentan con 3 niveles de dificultad elegibles según el gusto del jugador, variando en cosas como la velocidad de movimiento de la(s) ', letra_1, blanco, ancho_ventana-950, alto_ventana-375)
            mostrar_texto('nave(s), el tiempo de recarga de aliens (más rápido) y el de la(s) nave(s) (más lento) y la cantidad de enemigos. La puntuación aumenta y disminuye ', letra_1, blanco, ancho_ventana-950, alto_ventana-350)
            mostrar_texto('aumenta en 1 cada vez que muere un alien y disminuye en 1 cada vez que se pierde una vida de la nave, en la opción 4 del menú se puede acceder a los', letra_1, blanco, ancho_ventana-950, alto_ventana-325)
            mostrar_texto('historiales de puntuación', letra_1, blanco, ancho_ventana-950, alto_ventana-300)
            pygame.display.update()
            
            
        if tecla[pygame.K_4]:#4 es para ver los records
            ventana.blit(fondo,(0,0))
            mostrar_texto('HIGHSCORES', letra_2, blanco, ancho_ventana-950, alto_ventana-580) #mostrar texto
            r=open('Imagenes/highscores.txt',encoding='utf-8') #se abre el archivo almacenado en la carpeta, este cuenta con el top 5 de puntuaciones y con la última puntuación generada (si ya se jugó una partida, sino solo contiene los 5 primeros)
            texto=r.read() #se lee el archivo
            lista=[] #se crea una lista vacía
            numero=str() #cada número en el texto lo vamos a sacar como un string
            for caracter in texto: #por cada caracter en el texto
                if caracter!=',': #si es diferente a una coma
                    numero+=(caracter) #agreguelo a número
                if caracter==',': #si es una coma
                    lista.append(numero) #agregue el número almacenado a la lista vacía
                    numero=str() #resetear número
            lista_2=[] #lista vacía 2
            pos=0 #para caminar el while
            while pos<len(lista): #mientras pos sea menor que la longitud de la lista
                lista_2.append(int(lista[pos])) #agregue a lista 2 el número presente en esa posición, entonces lista 2 va a contener todos los numeros que existen en el documento de texto pero en forma de entero para poder ordenarlos y sacar solo los 5 primeros
                pos+=1 #sumar 1 a pos
            r.close() #cerramos el archivo de texto
            lista_2.sort(reverse=True) #ordenamos de mayor a menor
            archivo_2=open('Imagenes/highscores.txt','w') #abrimos como write
            aux=0 #para caminar el while
            while aux<len(lista_2) and aux<5: #mientras aux sea menor que la longitud que lista 2 y sea menor que 5 (para que tome solo los 5 primeros)
                archivo_2.write(str(lista_2[aux])) #escriba lo que hay en esa posición en el archivo de texto
                archivo_2.write(',') #escriba ,
                aux+=1 #sumar a auxiliar
            archivo_2.close() #cerrar archivo
            p=open('Imagenes/highscores.txt',encoding='utf-8') #abrir como utf-8 para poder mostrarlo en la pantalla
            archivo_3=p.read() #leer el archivo
            records=letra.render(f'Top 5 highscores:{archivo_3}',1,blanco) #mostrar lo que contiene el archivo en la pantalla
            ventana.blit(records,(10,80)) 
            pygame.display.update()
            
            
        pygame.display.update()
        for accion in pygame.event.get():
            if accion.type==pygame.QUIT: #si se elije cerrar el juego termina
                ejecutando=False
                pygame.quit()
        
menu()  
