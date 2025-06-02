def polyphase_sort_simulado(arr):
    """
    Simulación simplificada del ordenamiento por polifase.
    """
    print("Inicio de Polyphase Sort (simulación):")
    # Paso 1: dividir en runs
    runs = [[x] for x in sorted(arr)]
    print(f"Runs simulados distribuidos: {runs}")

    # Paso 2: fase de mezcla (en teoría usa menos archivos temporales)
    while len(runs) > 1:
        run1 = runs.pop(0)
        run2 = runs.pop(0)
        merged = merge(run1, run2)
        print(f"Mezclando {run1} + {run2} → {merged}")
        runs.append(merged)
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
lista = [7, 4, 5, 2]
resultado = polyphase_sort_simulado(lista.copy())
print("Resultado final:", resultado)
