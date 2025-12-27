# Carpeta de Soluciones de Python - Curso Elementos de Computación

Esta carpeta contiene soluciones a los ejercicios prácticos del curso **Elementos de Computación**. Los códigos presentados corresponden a distintas actividades y cuadernos del curso, abarcando conceptos de programación en Python.

---

## Archivos de la carpeta

### 1. **reloj_parlante.py**

**Descripción**: Función que convierte una hora en formato de 12 horas (hh:mm am/pm) a una descripción textual clara indicando la hora actual.

**Funcionalidad específica**:
- Recibe un string con formato "hh:mm am" o "hh:mm pm"
- Distingue entre tres períodos del día: mañana (am), tarde (pm entre 12:00-11:59) y noche (pm después de cierta hora)

**Ejemplo de uso**:
```
reloj_parlante("05:25 am") -> "Son las 5 y 25 de la mañana."
reloj_parlante("07:55 pm") -> "Son las 7 y 55 de la noche"
```


---

### 2. **ordenar_numeros.py**

**Descripción**: Función que recibe tres números enteros y retorna una tupla con los números ordenados de menor a mayor.

**Funcionalidad específica**:
- Solicita tres números enteros del usuario mediante input
- Retorna una tupla con los tres números organizados en orden ascendente

**Ejemplo de uso**:
```
ordenar(5, 8, 1) -> (1, 5, 8)
ordenar(9, 3, 6) -> (3, 6, 9)
```

---

### 3. **convertidor_colon_dolar_euro.py**

**Descripción**: Función que convierte un monto en colones costarricenses a dólares estadounidenses o euros, redondeando al segundo decimal.

**Funcionalidad específica**:
- Solicita al usuario un monto en colones y la moneda destino
- Utiliza tasas de cambio predeterminadas (1 USD = ₡610.64, 1 EUR = ₡729.91)
- Emplea la función `round()` para redondear el resultado a dos decimales
- Retorna -1 si la moneda especificada es inválida

**Ejemplo de uso**:
```
convertidor(1500, "dólar") -> 2.46
convertidor(1500, "euro") -> 2.08
convertidor(1500, "yen") -> -1
```

---

### 4. **desglose_menor_cantidad_billetes.py**

**Descripción**: Programa que solicita un monto en dólares y calcula el desglose en la menor cantidad posible de billetes.

**Funcionalidad específica**:
- Solicita al usuario un monto en dólares (números enteros)
- Calcula la cantidad de billetes de cada denominación: $100, $50, $20, $10, $5 y $1
- Garantiza que el desglose representa la menor cantidad de billetes posibles
- Imprime el resultado

**Ejemplo de uso**:
```
Entrada: 1427
Salida:
14 Billetes de 100
0 Billetes de 50
1 Billetes de 20
0 Billetes de 10
1 Billetes de 5
2 Billetes de 1
```

---

### 5. **convertidor_cm_m_km.py**

**Descripción**: Programa que realiza conversiones entre centímetros, metros y kilómetros en cualquier combinación.

**Funcionalidad específica**:
- Solicita al usuario la unidad de medida inicial y la unidad de destino
- Solicita el valor a convertir
- Realiza la conversión utilizando factores de conversión predeterminados:
  - 1 metro = 100 centímetros
  - 1 kilómetro = 1000 metros
  - 1 kilómetro = 100,000 centímetros
- Maneja todas las combinaciones posibles de conversión entre las tres unidades
- Imprime el resultado

**Ejemplo de uso**:
```
Entrada: 
Ingrese la medida inicial (cm, m o km):km
Ingrese la medida a la que quiere convertir su dato (cm, m o km):cm
Ingrese la medida a convertir:20
Salida: 
2000000 centímetros

Entrada: km a cm, 2
Salida: 200000 centímetros
```

---

### 6. **celsius_a_fahrenheit.py**

**Descripción**: Programa que solicita una temperatura en grados Celsius y retorna el equivalente en grados Fahrenheit.

**Funcionalidad específica**:
- Solicita al usuario una temperatura en grados Celsius
- Aplica la fórmula de conversión: F = C × (9/5) + 32
- Imprime el resultado

**Ejemplo de uso**:
```
Entrada: 
Ingrese la temperatura en grados celsius: 56
Salida: 
La temperatura en grados Fahrenheit es: 132.8

```

---

### 7. **cantidad_mayusculas.py**

**Descripción**: Función que recibe un texto como parámetro y retorna la cantidad de letras mayúsculas presentes en él.

**Funcionalidad específica**:
- Recibe un string como entrada
- Utiliza la función `isupper()` para identificar letras mayúsculas
- Retorna el contador total de mayúsculas encontradas
- Ignora números, espacios y caracteres especiales

**Ejemplo de uso**:
```
cuenta_mayusculas("Al infinito y más allá") -> 1
cuenta_mayusculas("PERDON POR LAS MAYUSCULAS") -> 22
cuenta_mayusculas("Python es muy Bueno") -> 2
```

---

### 8. **eliminar_numero.py**

**Descripción**: Función que recibe un número entero y un dígito, retornando el número con el dígito especificado eliminado en todas sus apariciones.

**Funcionalidad específica**:
- Recibe un número entero y el dígito a eliminar
- Convierte el número a string para evaluar cada dígito individualmente
- Itera sobre la representación de string del número
- Elimina todas las apariciones del dígito especificado
- Retorna el resultado como un número entero

**Ejemplo de uso**:
```
eliminar_repetidos(10, 0) -> 1
eliminar_repetidos(1231410, 1) -> 2340
eliminar_repetidos(1590, 7) -> 1590
```

---

### 9. **verificar_numero_primo.py**

**Descripción**: Función que determina si un número entero positivo es primo o no.

**Funcionalidad específica**:
- Recibe un número entero positivo como entrada
- Maneja casos especiales: el número 1 (no primo) y números 2 y 3 (primos)
- Retorna `True` si el número es primo, `False` en caso contrario
- Un número primo es aquel que solo es divisible entre 1 y sí mismo

**Ejemplo de uso**:
```
numero_primo(7) -> True
numero_primo(4) -> False
numero_primo(15) -> False
numero_primo(211) -> True
```

---

### 10. **verificar_palindromo.py**

**Descripción**: Función que verifica si un texto es un palíndromo (se lee igual en ambos sentidos).

**Funcionalidad específica**:
- Recibe un string como parámetro
- Convierte el texto a minúsculas para hacer la verificación case-insensitive
- Elimina espacios en blanco del texto
- Invierte el string eliminados los espacios
- Compara el texto original (sin espacios) con su versión invertida
- Retorna `True` si es un palíndromo, `False` en caso contrario

**Ejemplo de uso**:
```
es_palindromo("Yo soy") -> True
es_palindromo("Amor a Roma") -> True
es_palindromo("Reconocer") -> True
es_palindromo("Hola") -> False
```

---

### 11. **sustituir_caracter.py**

**Descripción**: Función que sustituye todas las apariciones de un carácter específico por otro en un texto.

**Funcionalidad específica**:
- Recibe tres parámetros: el texto, el carácter a sustituir y el carácter sustituto (es sensible a mayúsculas)
- Itera sobre cada carácter del texto original
- Verifica si el carácter coincide con el carácter a sustituir
- Construye un nuevo string reemplazando todas las coincidencias
- Retorna el texto resultante con todas las sustituciones aplicadas

**Ejemplo de uso**:
```
sustituir_caracter("Elefante", "e", "u") -> "Elufantu"
sustituir_caracter("esto_es_un_texto", "_", " ") -> "esto es un texto"
sustituir_caracter("123,456,789", ",", ".") -> "123.456.789"
```

---

### 12. **verificar_matriz_triangular.py**

**Descripción**: Función que verifica si una matriz cuadrada es una matriz triangular.

**Funcionalidad específica**:
- Una matriz triangular es aquella donde todos los elementos por debajo o por encima de la diagonal son ceros
- Recibe una matriz cuadrada como parámetro
- Analiza la diagonal principal de la matriz
- Verifica los elementos en la región superior-derecha e inferior-izquierda de la diagonal
- Retorna `True` si la matriz es triangular, `False` en caso contrario

**Ejemplo de uso**:
```
es_triangular([[8, 9, 5], [0, 7, 1], [0, 0, 2]]) -> True
es_triangular([[1, 0, 0], [8, 5, 0], [5, 6, 3]]) -> True
es_triangular([[1, 0, 5], [4, 1, 0], [8, 0, 2]]) -> False
```

---

### 13. **contar_elementos_lista.py**

**Descripción**: Función recursiva que cuenta todos los elementos en una lista, incluyendo elementos en sublistas de cualquier nivel de profundidad.

**Funcionalidad específica**:
- Recibe una lista que puede contener números enteros y sublistas anidadas
- Convierte la lista a string para facilitar el conteo
- Itera sobre cada carácter del string resultante
- Excluye caracteres especiales de formato ([, ], ,, espacios)
- Cuenta cada dígito como un elemento individual
- Retorna el total de elementos encontrados

**Ejemplo de uso**:
```
cuente_todos([4, 5, [[[3, 4], 5], [3]], 4, 8]) -> 8
cuente_todos([1, [2, [3, 4]], 5]) -> 5
```

---

### 14. **inventario_de_pulperia.py**

**Descripción**: Aplicación para administrar un inventario de productos de una pulpería.

**Funcionalidad específica**:
- Implementa un sistema de gestión de inventario utilizando un diccionario
- Contiene un inventario inicial de 10 productos variados (arroz, frijoles, refrescos, galletas, etc.)
- Presenta un menú interactivo con cuatro opciones principales:
  1. **Ver inventario actual**: Muestra todos los productos y sus cantidades
  2. **Ver un producto**: Busca un producto específico y muestra su cantidad disponible
  3. **Agregar al inventario**: Permite agregar cantidad a un producto existente o crear un nuevo producto
  4. **Salir**: Termina la ejecución del programa
- Maneja búsquedas no sensibles a las mayúsculas

**Ejemplo de uso**:
```
1 Ver el inventario actual
2 Ver un producto
3 Agregar al inventario
4 Salir
¿Que desea hacer? Escoja una opción:1
Los productos existentes son:
arroz 10
frijoles 15
refresco 5
galletas 8
harina 3
gelatina 2
yogurt 4
helados 15
jalea 1
pan 12
1 Ver el inventario actual
2 Ver un producto
3 Agregar al inventario
4 Salir
¿Que desea hacer? Escoja una opción:
```

---

### 15. **vaticinador_de_hormigas.py**

**Descripción**: Función que predice la población de hormigas después de n períodos, considerando nacimientos y muertes.

**Funcionalidad específica**:
- Modela un sistema demográfico de hormigas con características específicas:
  - Población inicial: 5 parejas (10 hormigas individuales)
  - Reproducción: una pareja produce 3 hormigas por período
  - Longevidad: una hormiga vive exactamente 2 períodos
- Calcula la máxima cantidad de parejas posibles en cada período
- Maneja dos casos especiales:
  - Período 0: retorna solo la población inicial (10 hormigas)
  - Período 1: no hay muertes, solo nacimientos
- A partir del período 2: aplica la fórmula completa con nacimientos y muertes
- Retorna la población total después de n períodos

**Ejemplo de uso**:
```
hormigas(0) -> 10
hormigas(1) -> 25
hormigas(2) -> 51
```

---

### 16. **buscador_de_palabras.py**

**Descripción**: Aplicación para analizar archivos de texto plano (.txt) con múltiples funcionalidades de búsqueda y análisis.

**Funcionalidad específica**:
- Solicita al usuario la ruta completa de un archivo de texto (.txt)
- Lee y procesa el archivo completo con soporte para caracteres especiales (ñ, acentos)
- Presenta un menú con 7 opciones:
  1. **Buscar palabra**: Busca una palabra específica en el texto (case-insensitive) y cuenta sus apariciones
  2. **Total palabras**: Calcula y muestra el número total de palabras en el documento
  3. **Total oraciones**: Cuenta las oraciones basándose en signos de puntuación (., !, ?)
  4. **Total párrafos**: Cuenta los párrafos separados por saltos de línea
  5. **Total espacios**: Cuenta todos los espacios en blanco del documento
  6. **Total signos de puntuación**: Cuenta todos los caracteres de puntuación
  7. **Salir**: Cierra la aplicación

**Ejemplo de uso**:
```
Ingrese la ruta completa del archivo .txt que desea utilizar: /documentos/texto.txt
Menú
¿Que desea hacer?
1...........................Buscar palabra
2...........................Total palabras
3..........................Total oraciones
4.......................... Total párrafos
5...........................Total espacios
6...............Total signos de puntuación
7....................................Salir
Ingrese la opción deseada: 1
***El programa no distingue entre mayúsculas y minúsculas***
Ingrese la palabra que desea buscar: python
La palabra "python" se encuentra 5 veces en el texto.
```


Perfecto, aquí está el texto listo para copiar y pegar en GitHub con la descripción de los 4 archivos faltantes:

text

### 17. **area_y_perimetro_rectangulo.py**

**Descripción**: Programa que solicita las dimensiones de un rectángulo y calcula su área y perímetro.

**Funcionalidad específica**:
- Solicita al usuario la altura del rectángulo en metros
- Solicita al usuario la base del rectángulo en metros
- Calcula el área utilizando la fórmula: área = base × altura
- Calcula el perímetro utilizando la fórmula: perímetro = 2 × base + 2 × altura
- Imprime ambos resultados con sus unidades correspondientes (m² para área, m para perímetro)
- Utiliza variables descriptivas para almacenar los mensajes de salida

**Ejemplo de uso**:
Bienvenido a su programa para calcular el área y el perímetro de un rectángulo
Ingrese la medida de la altura en metros: 5
Ingrese la medida de la base en metros: 8
El área correponde a: 40 m2
El perímetro corresponde a: 26 m

---

### 18. **area_y_perimetro_circulo.py**

**Descripción**: Programa que solicita el radio de un círculo y calcula su área y perímetro (circunferencia).

**Funcionalidad específica**:
- Solicita al usuario la medida del radio del círculo
- Importa la constante `pi` de la biblioteca estándar `math`
- Calcula el área utilizando la fórmula: área = π × r²
- Calcula el perímetro (circunferencia) utilizando la fórmula: perímetro = 2 × π × r
- Convierte el radio a float para permitir decimales
- Imprime ambos resultados

**Ejemplo de uso**:
Bienvenido a su programa para calcular el área y perímetro de un círculo
Ingrese la medida del radio del círculo: 5
El área del círculo es: 78.53981633974483
El perímetro del círculo es: 31.41592653589793

---

### 19. **verificar_cuadrado_magico.py**

**Descripción**: Función que verifica si una matriz cuadrada es un cuadrado mágico.

**Funcionalidad específica**:
- Un cuadrado mágico es una matriz cuadrada donde todas las filas, columnas y diagonales suman exactamente lo mismo
- Recibe una matriz cuadrada de cualquier dimensión como parámetro
- Calcula la suma de todos los elementos en cada fila horizontalmente
- Calcula la suma de todos los elementos en cada columna verticalmente
- Calcula la suma de la diagonal principal (esquina superior izquierda a inferior derecha)
- Calcula la suma de la diagonal secundaria (esquina inferior izquierda a superior derecha)
- Almacena todas las sumas en una lista denominada `lista_suma`
- Verifica que todos los valores en `lista_suma` sean idénticos
- Retorna `True` si todas las sumas coinciden (es un cuadrado mágico), `False` en caso contrario

**Ejemplo de uso**:
es_magico( [[11,4,17,10,23],[20,8,21,14,2],[24,12,5,18,6],[3,16,9,22,15],[7,25,13,1,19]] ) -> True
​
es_magico( [[11,4,15,10,23],[20,8,21,14,2],[24,4,5,18,6],[3,16,9,22,15],[7,25,13,1,19]] )  -> False

---

### 20. **triangulo_de_Pascal.py**

**Descripción**: Función que retorna la enésima fila del triángulo de Pascal iniciando en cero.

**Funcionalidad específica**:
- El triángulo de Pascal es una estructura numérica donde cada número es la suma de los dos números directamente encima de él
- Recibe un número entero `n` que indica qué fila del triángulo se desea obtener
- Inicializa una lista con las dos primeras filas del triángulo: [1] y [1, 1]
- Itera desde la fila 1 hasta la fila n (exclusiva)
- Para cada nueva fila, crea una lista temporal que comienza con 1
- Calcula los valores intermedios sumando elementos adyacentes de la fila anterior
- Añade un 1 al final de cada fila (característica del triángulo de Pascal)
- Utiliza el método `extend()` para añadir valores sumados y `append()` para agregar filas completas a la matriz
- Retorna la fila n solicitada en formato de lista

**Ejemplo de uso**:
Pascal(0) -> [1]
​
Pascal(1) -> [1, 1]
​
Pascal(3) -> [1, 3, 3, 1]
​
Pascal(5) -> [1, 5, 10, 10, 5, 1]
​
Pascal(6) -> [1, 6, 15, 20, 15, 6, 1]
---
