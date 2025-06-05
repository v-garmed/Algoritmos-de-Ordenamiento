def polyphase_sort_simulado(arr):
    """
    Simulación simplificada del ordenamiento por polifase.
    """
    print("Inicio de Polyphase Sort (simulación):")
    # Paso 1: dividir en runs (cada elemento se convierte en una lista individual y se ordenan)
    runs = [[x] for x in sorted(arr)]
    print(f"Runs simulados distribuidos: {runs}")

    # Paso 2: fase de mezcla (mezcla los runs de dos en dos hasta que quede uno solo)
    while len(runs) > 1:
        run1 = runs.pop(0)  # Toma el primer run
        run2 = runs.pop(0)  # Toma el segundo run
        merged = merge(run1, run2)  # Fusiona ambos runs
        print(f"Mezclando {run1} + {run2} → {merged}")
        runs.append(merged)  # Agrega el resultado al final de la lista de runs
    return runs[0]  # Devuelve el run final (lista ordenada)

def merge(left, right):
    """Fusiona dos listas ordenadas."""
    result = []  # Lista para almacenar el resultado de la fusión
    i = j = 0  # Índices para recorrer las listas left y right
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])  # Agrega el elemento menor de left
            i += 1
        else:
            result.append(right[j])  # Agrega el elemento menor de right
            j += 1
    result.extend(left[i:])  # Agrega los elementos restantes de left (si hay)
    result.extend(right[j:])  # Agrega los elementos restantes de right (si hay)
    return result  # Devuelve la lista fusionada

# Ejemplo de uso
lista = [7, 4, 5, 2]  # Lista de entrada
resultado = polyphase_sort_simulado(lista.copy())  # Llama a la función de ordenamiento
print("Resultado final:", resultado)  # Imprime el resultado ordenado
