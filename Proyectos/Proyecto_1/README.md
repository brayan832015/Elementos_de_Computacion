# Proyecto 1: Filtro Digital FIR para Procesamiento de Audio

## Descripción General del Proyecto

Este proyecto implementa un **filtro digital FIR (Finite Impulse Response)** mediante una aplicación en Python que permite procesar archivos de audio en formato WAV. El filtro FIR es un algoritmo que recibe una secuencia de datos de audio como entrada y los procesa mediante una ecuación matemática para obtener una nueva secuencia de datos "filtrada", modificando el contenido de frecuencias del audio.

---

## ¿Qué es un Filtro Digital FIR?

Un filtro de respuesta finita al impulso (FIR) es un algoritmo que modifica una señal de entrada aplicando la siguiente ecuación:

**y[n] = Σ(bₖ × x[n-k])** para k = 0 hasta 14

Donde:
- **y[n]**: Valor filtrado en la posición n
- **bₖ**: Coeficiente del filtro en la posición k (tabla de 15 coeficientes)
- **x[n-k]**: Valores pasados de la señal de entrada
- **n**: Posición actual en la secuencia

---

## Descripción del Código

**Opciones disponibles en el primer menú**:
1. **Filtrar, graficar o escuchar un audio determinado**
2. **Salir del programa**

**Opciones disponibles en el segundo menú**:
1. **Escuchar audio sin filtrar**
2. **Escuchar audio filtrado**
3. **Graficar los audios**
4. **Regresar al menú principal**


---

**Coeficientes del Filtro FIR**
- Lista de 15 coeficientes utilizados

k = [1.6687317037448562e-16, -0.03551153864045256, -1.7257607380175936e-16, 0.10653199877675365, 1.9371078815074347e-16, -0.18642779737756615, -6.256569336689685e-17, 0.2219393360180186, -6.245004513516506e-17, -0.18642779737756615,  1.9371078815074347e-16,  0.10653199877675364,  -1.7257607380175936e-16,  -0.03551153864045256,  1.6687317037448562e-16]

