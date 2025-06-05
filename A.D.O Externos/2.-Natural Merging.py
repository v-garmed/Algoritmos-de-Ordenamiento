def natural_merging(arr):
    """
    Ordenamiento por mezcla natural. Usa las secuencias ya ordenadas como bloques.
    """
    print("Inicio de Natural Merging:")

    def find_runs(arr):
        # Encuentra secuencias ordenadas (runs) en el arreglo
        runs = []
        run = [arr[0]]  # Comienza con el primer elemento
        for i in range(1, len(arr)):
            if arr[i] >= arr[i - 1]:
                run.append(arr[i])  # Continúa la secuencia si está ordenada
            else:
                runs.append(run)    # Termina la secuencia y comienza una nueva
                run = [arr[i]]
        runs.append(run)            # Agrega la última secuencia
        return runs

    runs = find_runs(arr)           # Obtiene las secuencias iniciales
    print(f"Runs iniciales: {runs}")

    # Mientras haya más de una secuencia, sigue fusionando
    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                merged = merge(runs[i], runs[i + 1])  # Fusiona dos secuencias
                print(f"Mezclando {runs[i]} + {runs[i + 1]} → {merged}")
                new_runs.append(merged)
            else:
                new_runs.append(runs[i])  # Si queda una secuencia sola, la agrega sin fusionar
        runs = new_runs                  # Actualiza la lista de secuencias
    return runs[0]                       # Devuelve la secuencia final ordenada

def merge(left, right):
    """Fusiona dos listas ordenadas."""
    result = []
    i = j = 0
    # Fusiona los elementos de ambas listas en orden
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])   # Agrega los elementos restantes de left
    result.extend(right[j:])  # Agrega los elementos restantes de right
    return result

# Ejemplo de uso
lista = [1, 2, 5, 3, 4, 6]           # Lista de ejemplo
resultado = natural_merging(lista.copy())  # Ordena la lista usando mezcla natural
print("Resultado final:", resultado)       # Imprime el resultado final

