def distribuir_corridas(arr, tam_bloque):
    """
    Distribuye corridas iniciales de tamaño fijo simulando memoria limitada.
    """
    # Imprime mensaje de inicio con el tamaño de bloque usado
    print(f"Inicio de Distribución de Corridas (bloques de tamaño {tam_bloque}):")
    runs = []  # Lista para almacenar las corridas (bloques ordenados)
    # Recorre el arreglo en pasos del tamaño de bloque
    for i in range(0, len(arr), tam_bloque):
        bloque = arr[i:i + tam_bloque]  # Extrae un bloque del arreglo
        bloque_ordenado = sorted(bloque)  # Ordena el bloque extraído
        runs.append(bloque_ordenado)  # Agrega el bloque ordenado a la lista de corridas
        print(f"  Bloque ordenado: {bloque_ordenado}")  # Muestra el bloque ordenado
    return runs  # Devuelve la lista de corridas generadas

# Ejemplo de uso
lista = [8, 6, 3, 1, 7, 2, 5, 4]  # Lista de entrada
runs = distribuir_corridas(lista.copy(), 3)  # Genera corridas de tamaño 3
print("Corridas iniciales generadas:", runs)  # Muestra las corridas generadas
