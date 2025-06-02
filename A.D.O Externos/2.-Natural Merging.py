def natural_merging(arr):
    """
    Ordenamiento por mezcla natural. Usa las secuencias ya ordenadas como bloques.
    """
    print("Inicio de Natural Merging:")

    def find_runs(arr):
        runs = []
        run = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] >= arr[i - 1]:
                run.append(arr[i])
            else:
                runs.append(run)
                run = [arr[i]]
        runs.append(run)
        return runs
    
    

    runs = find_runs(arr)
    print(f"Runs iniciales: {runs}")

    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                merged = merge(runs[i], runs[i + 1])
                print(f"Mezclando {runs[i]} + {runs[i + 1]} → {merged}")
                new_runs.append(merged)
            else:
                new_runs.append(runs[i])
        runs = new_runs
    return runs[0]

def merge(left, right):
    """Fusiona dos listas ordenadas."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Ejemplo de uso
lista = [1, 2, 5, 3, 4, 6]
resultado = natural_merging(lista.copy())
print("Resultado final:", resultado)
