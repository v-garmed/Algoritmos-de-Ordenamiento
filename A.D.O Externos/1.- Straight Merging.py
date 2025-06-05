def straight_merging(arr):
    """
    Ordenamiento por mezcla directa. Divide, ordena, y mezcla pares de bloques.
    """
    print("Inicio de Straight Merging:")
    # Paso 1: dividir en sublistas de tamaño 1
    runs = [[x] for x in arr]  # Crea una lista de sublistas, cada una con un elemento de arr
    print(f"Sublistas iniciales: {runs}")

    # Paso 2: mezclar de dos en dos hasta tener una sola lista
    while len(runs) > 1:  # Mientras haya más de una sublista
        new_runs = []  # Lista para almacenar las nuevas sublistas mezcladas
        for i in range(0, len(runs), 2):  # Recorre las sublistas de dos en dos
            if i + 1 < len(runs):  # Si hay un par de sublistas para mezclar
                merged = merge(runs[i], runs[i + 1])  # Mezcla las dos sublistas
                print(f"Mezclando {runs[i]} + {runs[i + 1]} → {merged}")
                new_runs.append(merged)  # Agrega la sublista mezclada a la nueva lista
            else:
                new_runs.append(runs[i])  # Si queda una sublista sin par, la agrega tal cual
        runs = new_runs  # Actualiza la lista de sublistas
    return runs[0] if runs else []  # Devuelve la lista ordenada final

def merge(left, right):
    """Fusiona dos listas ordenadas."""
    result = []  # Lista para almacenar el resultado de la fusión
    i = j = 0  # Índices para recorrer las listas left y right
    while i < len(left) and j < len(right):  # Mientras no se llegue al final de alguna lista
        if left[i] <= right[j]:  # Compara los elementos actuales de ambas listas
            result.append(left[i])  # Agrega el menor a la lista resultado
            i += 1  # Avanza en la lista left
        else:
            result.append(right[j])  # Agrega el menor a la lista resultado
            j += 1  # Avanza en la lista right
    result.extend(left[i:])  # Agrega los elementos restantes de left (si hay)
    result.extend(right[j:])  # Agrega los elementos restantes de right (si hay)
    return result  # Devuelve la lista fusionada y ordenada

# Ejemplo de uso
lista = [8, 3, 7, 4, 9, 2]  # Lista de ejemplo a ordenar
resultado = straight_merging(lista.copy())  # Llama a la función de ordenamiento
print("Resultado final:", resultado)  # Imprime el resultado final ordenado
