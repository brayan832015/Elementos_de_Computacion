# Proyecto 2: Space Invaders

## Descripción General del Proyecto

Este proyecto implementa una **versión del clásico juego Space Invaders**, desarrollada completamente en Python utilizando la biblioteca PyGame. Es un juego arcade de disparos en 2D donde el jugador (o dos jugadores en modo cooperativo) debe destruir oleadas de enemigos alienígenas mientras se defiende de sus ataques.

---

## Características Principales del Juego

### Modos de Juego

1. **Modo Individual**: Un jugador controla una nave y enfrenta olas de enemigos
   - 3 vidas disponibles
   - Sistema de puntuación donde se suma 1 por enemigo destruido y se resta 1 por daño recibido

2. **Modo Multijugador Cooperativo**: Dos jugadores en el mismo equipo
   - 6 vidas compartidas entre ambos jugadores
   - Colaboración para destruir todos los enemigos
   - Cada jugador tiene controles independientes

### Niveles de Dificultad

| Nivel | Velocidad Nave | Recarga Nave | Recarga Aliens | Filas Aliens | Descripción |
|-------|---|---|---|---|---|
| **Fácil** | 5 | 750ms | 750ms | 2 | Velocidad alta, recarga rápida, pocos enemigos |
| **Intermedio** | 3 | 1000ms | 500ms | 3 | Velocidad media, recarga balanceada |
| **Difícil** | 2 | 1500ms | 300ms | 3 | Velocidad baja, recarga lenta, muchos enemigos |

### Sistema de Obstáculos

Existen **5 obstáculos defensivos** distribuidos en el mapa que pueden absorber daño:
- Cada obstáculo tiene **3 estados de resistencia**
- Cambia visualmente con cada impacto recibido
- Proporciona cobertura temporal contra ataques enemigos

---

## Arquitectura del Código

### Estructura Basada en Programación Orientada a Objetos

El código implementa las siguientes clases principales:

#### **Clase Nave**
Representa la nave del jugador en modo individual.

**Atributos**:
- `image`: Imagen del sprite de la nave
- `rect`: Rectángulo de colisión
- `vidas`: Cantidad de vidas restantes
- `ultimo_disparo`: Timestamp del último disparo
- `contacto`: Máscara de colisión precisa

**Métodos**:
- `__init__(x, y)`: Constructor de la nave
- `update()`: Actualiza posición, disparo y estado de vida

**Controles**:
- Tecla **Izquierda/Derecha**: Movimiento horizontal
- Tecla **Espacio**: Disparo

#### **Clase Nave_2**
Representa la segunda nave en modo multijugador.

**Características**:
- Idéntica a la clase Nave
- Controles alternativos (A, D, S)

**Controles**:
- Tecla **A**: Movimiento izquierda
- Tecla **D**: Movimiento derecha
- Tecla **S**: Disparo

#### **Clase Balas**
Representa los proyectiles disparados por el jugador.

**Funcionalidad**:
- Se mueve hacia arriba
- Se destruye al salir de la pantalla o al impactar un enemigo

#### **Clase Aliens**
Representa los enemigos alienígenas.

**Características**:
- Patrón de movimiento oscilante (lado a lado)
- Sprite aleatorio entre 3 tipos
- Dispara hacia la nave del jugador

**Atributos**:
- `mover_disparo`: Control del movimiento
- `mover_direccion`: Dirección actual (1 o -1)

#### **Clase Alien_Balas**
Representa los proyectiles enemigos.

**Funcionalidad**:
- Se mueve hacia abajo
- Detecta colisión con nave usando máscara de colisión
- Reduce vida de la nave al impactar

#### **Clase Obstaculos**
Representa las defensas destructibles.

**Características**:
- 3 estados de resistencia
- Cambia imagen visualmente con cada impacto
- Se destruye al alcanzar estado 0
- Reproduce sonido al ser impactado

**Atributos**:
- `estado`: Resistencia actual (3, 2, 1, 0)
- `contacto`: Máscara de colisión precisa

---

## Sistema de Puntuación y Highscores

### Mecánica de Puntos

- **+1 punto**: Por cada enemigo destruido
- **-1 punto**: Por cada daño recibido en la nave
- **Persistencia**: Los puntajes se guardan en `Imagenes/highscores.txt`

### Archivo de Highscores

El archivo `highscores.txt` almacena:
- Los 5 mejores puntajes históricos
- El puntaje de la última partida jugada
- Formato: números separados por comas

---

## Sistema de Sonidos

El juego incorpora efectos de sonido para mejorar la experiencia:

| Sonido | Archivo | Evento | Volumen |
|--------|---------|--------|---------|
| Explosión Enemigo | `invaderkilled.wav` | Al eliminar un enemy | 0.25 |
| Explosión Nave | `explosion.wav` | Al recibir daño | 0.25 |
| Disparo Nave | `shoot.wav` | Al disparar | 0.25 |
| Disparo Alien | `fastinvader1.wav` | Al alien disparar | 0.25 |
| Victoria | `ganador.mp3` | Al ganar partida | 0.25 |
| Derrota | `perdedor.mp3` | Al perder partida | 0.20 |
| Impacto Obstáculo | `obst.wav` | Al golpear obstáculo | 0.25 |

---

## Menús del Juego

### Menú Principal
Presenta 4 opciones al iniciarse:

**Opción 1**: Juego Individual
- Presionar y mantener **tecla 1**
- Lleva a pantalla de selección de dificultad

**Opción 2**: Juego Multijugador  
- Presionar y mantener **tecla 2**
- Lleva a pantalla de selección de dificultad

**Opción 3**: Ayuda
- Presionar y mantener **tecla 3**
- Muestra explicación completa del juego y controles

**Opción 4**: Highscores
- Presionar y mantener **tecla 4**
- Muestra tabla ordenada de mejores puntuaciones

### Pantalla de Selección de Dificultad

**Opción F**: Modo Fácil
**Opción I**: Modo Intermedio
**Opción D**: Modo Difícil

---

## Pantallas de Fin de Juego

### Pantalla de Victoria
Muestra cuando se eliminan todos los enemigos:
- Mensaje: "USTED GANÓ!"
- Reproduce sonido de victoria
- Opción: **Presionar M** para volver al menú principal
- Guarda el puntaje en archivo highscores

### Pantalla de Derrota
Muestra cuando se agotan todas las vidas:
- Mensaje: "USTED PERDIÓ"
- Reproduce sonido de derrota
- Opción: **Presionar M** para volver al menú principal
- Guarda el puntaje en archivo highscores

---

## Bucle Principal del Juego

INICIO
↓
Mostrar Menú Principal
↓
Usuario elige Modo (1 o 2)
↓
Usuario elige Dificultad (F, I, D)
↓
Inicializar Juego
├─ Crear aliens
├─ Crear obstáculos
├─ Crear nave(s)
├─ Inicializar sonidos
└─ Configurar parámetros de dificultad
↓
BUCLE DE JUEGO (mientras ejecutando = True):
├─ Mostrar fondo y puntuación
├─ Procesar entrada del usuario
├─ Actualizar posiciones (naves, balas, aliens)
├─ Detectar colisiones
├─ Aliens disparan aleatoriamente (máximo 5 balas)
├─ Reproducir sonidos según eventos
├─ Verificar condiciones de victoria/derrota
└─ Actualizar pantalla (60 FPS)
↓
FIN DE PARTIDA
├─ Mostrar pantalla de victoria o derrota
├─ Reproducir sonido final
├─ Guardar puntuación en archivo
└─ Esperar entrada para volver al menú

---


## Pantallas del Juego

![Menú Principal](Imágenes_funcionamiento/menu_principal.jpg)
*Pantalla principal con opciones de juego*

![Selección de Dificultad](Imágenes_funcionamiento/menu_dificultad.jpg)
*Menú para elegir nivel de dificultad*

![Juego Individual](Imágenes_funcionamiento/juego_individual.jpg)
*Juego en modo de un jugador durante la partida*

![Juego Multijugador](Imágenes_funcionamiento/juego_dos_jugadores.jpg)
*Modo cooperativo con dos jugadores simultáneamente*

![Pantalla de Victoria](Imágenes_funcionamiento/pantalla_ganada.jpg)
*Pantalla mostrada al ganar la partida*

![Pantalla de Derrota](Imágenes_funcionamiento/pantalla_perdida.jpg)
*Pantalla mostrada al perder todas las vidas*
