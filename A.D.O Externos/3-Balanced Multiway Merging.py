import heapq  # Importa el módulo heapq para usar una cola de prioridad (min-heap)

def multiway_merge(runs):
    """
    Mezcla balanceada multivía usando una cola de prioridad (heapq).
    """
    print("Inicio de Balanced Multiway Merging:")
    heap = []    # Inicializa la cola de prioridad (min-heap)
    result = []  # Lista para almacenar el resultado final ordenado

    # Inserta el primer elemento de cada run en el heap
    for i, run in enumerate(runs):
        if run:  # Verifica que el run no esté vacío
            # (valor, índice del run, índice dentro del run)
            heapq.heappush(heap, (run[0], i, 0))

    # Mientras el heap no esté vacío, extrae el menor elemento y agrega el siguiente del mismo run
    while heap:
        value, i, j = heapq.heappop(heap)  # Extrae el menor elemento del heap
        result.append(value)               # Agrega el valor al resultado final
        if j + 1 < len(runs[i]):          # Si hay más elementos en el mismo run
            # Inserta el siguiente elemento del mismo run en el heap
            heapq.heappush(heap, (runs[i][j + 1], i, j + 1))
    return result  # Devuelve la lista ordenada

# Ejemplo de uso
runs = [[1, 5], [2, 6], [0, 3]]  # Runs de entrada (listas ya ordenadas)
resultado = multiway_merge(runs)  # Llama a la función de mezcla multivía
print("Resultado final:", resultado)  # Imprime el resultado final ordenado
