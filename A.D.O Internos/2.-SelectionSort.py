def selection_sort(arr):
    """
    Ordena una lista utilizando el algoritmo de selección.
    """
    n = len(arr)
    for i in range(n):
        # Suponemos que el elemento actual es el mínimo
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Intercambiamos el mínimo encontrado con el primer elemento sin ordenar
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 25, 12, 22, 11]
    print("Lista original:", lista)
    lista_ordenada = selection_sort(lista)
    print("Lista ordenada:", lista_ordenada)
    