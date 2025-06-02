# Algoritmos De Ordenamiento

## ¿Qué son los algoritmos de ordenamiento?
Los algoritmos de ordenamiento son procedimientos utilizados para organizar los elementos de una lista o arreglo (como números, letras o palabras) en un orden específico, ya sea ascendente o descendente.
El ordenamiento es una operación fundamental en la informática porque:

- **Mejora la eficiencia de otras operaciones:** como búsquedas o uniones de datos.

- **Facilita la visualización y comprensión de los datos.**

- **Es una etapa previa común en análisis de datos, procesamiento de archivos y estructuras de datos.**
## 📌 Insertion Sort (Ordenamiento por Inserción)
El algoritmo construye la lista ordenada uno a uno, tomando cada elemento y colocándolo en la posición correcta respecto a los ya ordenados.

- **Complejidad promedio:** O(n²)  
- **Ventajas:** Simple, eficiente para listas pequeñas o parcialmente ordenadas.  
- **Desventajas:** Ineficiente para listas grandes.  

---

## 📌 Selection Sort (Ordenamiento por Selección)
Este método busca el elemento más pequeño (o más grande) y lo intercambia con el primer elemento, luego repite el proceso con los elementos restantes.

- **Complejidad promedio:** O(n²)  
- **Ventajas:** Fácil de implementar, no requiere memoria adicional.  
- **Desventajas:** Siempre realiza el mismo número de comparaciones, aunque la lista esté ordenada.  

---

## 📌 Exchange Sort (Ordenamiento por Intercambio)
Consiste en comparar todos los pares posibles y realizar intercambios si están en el orden incorrecto. Una variante conocida es el Bubble Sort.

- **Complejidad promedio:** O(n²)  
- **Ventajas:** Fácil de entender.  
- **Desventajas:** Muy ineficiente en la práctica.  

---

## 📌 Tree Sort (Ordenamiento de Árbol)
Utiliza un árbol binario de búsqueda (BST) para insertar todos los elementos, y luego realiza un recorrido in-order para obtener los elementos ordenados.

- **Complejidad promedio:** O(n log n)  
- **Ventajas:** Estable si se usa un árbol balanceado.  
- **Desventajas:** Puede degradarse a O(n²) si el árbol no está balanceado.  

---

## 📌 QuickSort
Algoritmo que utiliza la estrategia de divide y vencerás. Elige un pivote, divide el arreglo en dos subarreglos y los ordena recursivamente.

- **Complejidad promedio:** O(n log n)  
- **Ventajas:** Muy eficiente en la práctica.  
- **Desventajas:** En el peor caso puede ser O(n²), aunque rara vez ocurre.  

---

## 📌 MergeSort
Divide la lista en mitades, las ordena recursivamente y luego las combina (merge) en una sola lista ordenada.

- **Complejidad promedio:** O(n log n)  
- **Ventajas:** Estable, eficiente y predecible.  
- **Desventajas:** Requiere memoria adicional proporcional al tamaño de la lista.  

---

## 📌 RadixSort
Ordena los elementos por dígitos individuales, desde el menos significativo al más significativo. Ideal para enteros o cadenas de longitud fija.

- **Complejidad promedio:** O(nk), donde *k* es el número de dígitos.  
- **Ventajas:** Muy eficiente para datos enteros y cadenas.  
- **Desventajas:** No es comparativo, limitado a ciertos tipos de datos.  

---

## 📌 Straight Merging (Mezcla Directa)
Variante de MergeSort que divide la lista en bloques de tamaño fijo, los ordena y luego los mezcla. Utiliza almacenamiento adicional.

- **Complejidad promedio:** O(n log n)  
- **Ventajas:** Ideal para archivos grandes.  
- **Desventajas:** Requiere espacio extra y múltiples pasadas.  

---

## 📌 Natural Merging (Mezcla Natural)
Mejora del straight merging. Detecta y utiliza las subsecuencias ya ordenadas (runs) dentro de la lista original antes de mezclarlas.

- **Complejidad promedio:** O(n log n)  
- **Ventajas:** Aprovecha el orden parcial de los datos.  
- **Desventajas:** Puede requerir múltiples pasadas sobre los datos.  

---

## 📌 Balanced Multiway Merging
Extiende MergeSort utilizando múltiples archivos o bloques (más de dos) para realizar la mezcla de manera equilibrada.

- **Complejidad promedio:** O(n logₖ n), donde *k* es el número de vías.  
- **Ventajas:** Reduce el número de pasadas necesarias.  
- **Desventajas:** Mayor complejidad en la implementación.  

---

## 📌 Polyphase Sort
Optimización del balanced multiway merging que usa desbalance intencional en la distribución de datos para minimizar el número de archivos utilizados simultáneamente.

- **Complejidad promedio:** O(n log n)  
- **Ventajas:** Menor uso de archivos temporales.  
- **Desventajas:** Difícil de implementar correctamente.  

---

## 📌 Distribution of Initial Runs (Distribución de Secuencias Iniciales)
Fase inicial en algoritmos de mezcla externa donde se identifican y distribuyen secuencias ordenadas (runs) en varios archivos para su posterior mezcla eficiente.

- **Objetivo:** Preparar los datos para la mezcla.  
- **Ventajas:** Mejora el rendimiento de la mezcla.  
- **Desventajas:** Requiere una buena estrategia de distribución.  

