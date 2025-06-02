def straight_merging(arr):
    """
    Ordenamiento por mezcla directa. Divide, ordena, y mezcla pares de bloques.
    """
    print("Inicio de Straight Merging:")
    # Paso 1: dividir en sublistas de tamaño 1
    runs = [[x] for x in arr]
    print(f"Sublistas iniciales: {runs}")

    # Paso 2: mezclar de dos en dos hasta tener una sola lista
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
    return runs[0] if runs else []

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
lista = [8, 3, 7, 4, 9, 2]
resultado = straight_merging(lista.copy())
print("Resultado final:", resultado)
