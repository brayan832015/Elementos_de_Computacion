# Repositorio de prácticas – Elementos de Computación (Python)

Esta carpeta contiene las soluciones en Python a las prácticas del curso **Elementos de Computación**, organizadas según las guías de cuadernos y ejercicios individuales del curso.

Cada archivo `.py` resuelve uno o varios enunciados específicos y está pensado como material de estudio y referencia para conceptos básicos de programación en Python.

---

## Contenido por archivo `.py`

### `celsius_a_fahrenheit.py`

- Implementa un programa que solicita al usuario una temperatura en grados Celsius y muestra su equivalente en grados Fahrenheit usando la fórmula estándar de conversión.
- Corresponde al ejercicio 7 del Cuaderno 01, enfocado en entrada de datos por teclado, uso de tipos numéricos y operaciones aritméticas básicas.

---

### `area_y_perimetro_rectangulo.py`

- Solicita las dimensiones de un rectángulo (base y altura) y calcula tanto el área como el perímetro, mostrando ambos resultados al usuario.
- Resuelve el ejercicio 8 del Cuaderno 01, reforzando el uso de variables, expresiones aritméticas y salida formateada.

---

### `area_y_perimetro_circulo.py`

- Pide el radio de un círculo y calcula su área y perímetro (circunferencia) utilizando la constante `pi` de la librería `math`.
- Desarrolla el ejercicio 9 del Cuaderno 01, integrando importación de módulos y uso de constantes matemáticas.

---

### `reloj_parlante.py`

- Implementa una función que recibe una hora en formato `hh:mm am/pm` y retorna un texto “parlante” indicando la hora en palabras y el periodo del día (mañana, tarde o noche).
- Soluciona la Actividad 1 del Cuaderno 02, practicando manejo de cadenas, cortes de texto y lógica condicional.

---

### `ordenar_numeros.py`

- Define una función que recibe tres números enteros y retorna una tupla con esos números ordenados de menor a mayor.
- Corresponde a la Actividad 2 del Cuaderno 02, enfocada en comparaciones, condicionales y retorno de múltiples valores mediante tuplas.

---

### `convertidor_colon_dolar_euro.py`

- Implementa una función que recibe un monto en colones y una cadena con la moneda objetivo (`"dolar"` o `"euro"`) y retorna el monto convertido, redondeado a dos decimales, o `-1` si la moneda es inválida.
- Resuelve la Actividad 3 del Cuaderno 02, practicando condicionales, cálculo con tasas de cambio y el uso de la función `round`.

---

### `desglose_menor_cantidad_billetes.py`

- Pide al usuario un monto entero en dólares y calcula el desglose en billetes de 100, 50, 20, 10, 5 y 1, usando la menor cantidad de billetes posible.
- Implementa la Actividad 4 del Cuaderno 02, trabajando con divisiones enteras, módulo y estructuras de repetición básicas (o secuencias de operaciones).

---

### `convertidor_cm_m_km.py`

- Permite convertir distancias entre centímetros, metros y kilómetros en cualquier combinación, según la opción elegida por el usuario.
- Da solución a la Actividad 5 del Cuaderno 02, integrando menús simples, condicionales encadenados y conversiones entre unidades.

---

### `cantidad_mayusculas.py`

- Define una función que recibe un texto y retorna la cantidad de letras mayúsculas que contiene, utilizando el método `.isupper()`.
- Corresponde a la Actividad 1 del Cuaderno 03, enfocada en recorrido de cadenas y conteo de caracteres con condiciones.

---

### `eliminar_numero.py`

- Implementa una función que recibe un número entero y un dígito, y devuelve un nuevo entero con todas las apariciones de ese dígito eliminadas.
- Resuelve la Actividad 2 del Cuaderno 03, trabajando con conversión entre cadenas y enteros, y manipulación de texto sin estructuras avanzadas.

---

### `verificar_numero_primo.py`

- Recibe un entero positivo y retorna un valor booleano indicando si el número es primo (`True`) o no (`False`).
- Implementa la Actividad 3 del Cuaderno 03, aplicando divisiones sucesivas y lógica condicional para determinar primalidad.

---

### `sustituir_caracter.py`

- Define una función que recibe un texto, un carácter a sustituir y un carácter sustituto, y retorna el texto con todas las apariciones reemplazadas.
- Resuelve la Actividad 5 del Cuaderno 03, practicando recorrido de cadenas y construcción de nuevos textos carácter por carácter.

---

### `contar_elementos_lista.py`

- Contiene funciones para contar elementos dentro de una lista según algún criterio (por ejemplo, coincidencias con un valor dado o cantidad de elementos totales).
- Se utiliza para reforzar el manejo de listas, ciclos y operaciones de conteo manual, sin usar métodos avanzados no vistos en clase.

---

### `buscador_de_palabras.py`

- Implementa utilidades para buscar palabras dentro de textos, posiblemente contando apariciones, posiciones o coincidencias parciales según los requisitos del ejercicio.
- Sirve como práctica de trabajo intensivo con cadenas, listas y ciclos while, evitando estructuras no permitidas en el enunciado.

---

### `inventario_de_pulperia.py`

- Simula el inventario de una pulpería: manejo de productos, existencias y posibles operaciones básicas como agregar, vender o consultar items.
- Refuerza conceptos de estructuras de datos (listas, diccionarios o tuplas), actualización de valores y modelado de problemas del mundo real.

---

### `herencia-clases.py`

- Contiene un ejemplo de orientación a objetos con definición de clases relacionadas mediante herencia (por ejemplo, una clase base y varias clases hijas especializadas).
- Introduce conceptos como constructores, atributos, métodos, herencia y posible sobreescritura de comportamiento para practicar diseño de jerarquías de clases.

---

### `vaticinador_de_hormigas.py`

- Implementa un programa lúdico que “vaticina” o predice resultados a partir de ciertos datos de entrada, usando lógica condicional y cálculos sencillos.
- Se utiliza como ejercicio integrador de entrada por teclado, condiciones, ciclos y manejo básico de funciones.

---

## Cuadernos en PDF

Además de los scripts en Python, el repositorio incluye las guías originales de trabajo en formato PDF:

- `cuaderno1.pdf`: Enunciados y teoría básica sobre tipos de datos, operaciones y primeros programas (temperatura, área y perímetro).
- `cuaderno2.pdf`: Actividades sobre funciones, manejo de cadenas, conversión de monedas, desglose de billetes y conversión de unidades.
- `cuaderno3.pdf`–`cuaderno8.pdf`: Conjunto de prácticas adicionales que amplían el trabajo con cadenas, números, lógica, ciclos e introducción a conceptos más avanzados.

Estas guías sirven como referencia para entender el contexto de cada archivo `.py` y los objetivos de aprendizaje de cada ejercicio.
