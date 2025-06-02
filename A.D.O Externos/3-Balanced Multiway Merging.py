import heapq

def multiway_merge(runs):
    """
    Mezcla balanceada multivía usando una cola de prioridad (heapq).
    """
    print("Inicio de Balanced Multiway Merging:")
    heap = []
    result = []

    for i, run in enumerate(runs):
        if run:
            heapq.heappush(heap, (run[0], i, 0))

    while heap:
        value, i, j = heapq.heappop(heap)
        result.append(value)
        if j + 1 < len(runs[i]):
            heapq.heappush(heap, (runs[i][j + 1], i, j + 1))
    return result

# Ejemplo de uso
runs = [[1, 5], [2, 6], [0, 3]]
resultado = multiway_merge(runs)
print("Resultado final:", resultado)
