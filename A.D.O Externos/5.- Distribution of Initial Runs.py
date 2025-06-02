def distribuir_corridas(arr, tam_bloque):
    """
    Distribuye corridas iniciales de tamaño fijo simulando memoria limitada.
    """
    print(f"Inicio de Distribución de Corridas (bloques de tamaño {tam_bloque}):")
    runs = []
    for i in range(0, len(arr), tam_bloque):
        bloque = arr[i:i + tam_bloque]
        bloque_ordenado = sorted(bloque)
        runs.append(bloque_ordenado)
        print(f"  Bloque ordenado: {bloque_ordenado}")
    return runs

# Ejemplo de uso
lista = [8, 6, 3, 1, 7, 2, 5, 4]
runs = distribuir_corridas(lista.copy(), 3)
print("Corridas iniciales generadas:", runs)
