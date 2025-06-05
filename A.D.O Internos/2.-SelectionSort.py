def selection_sort(arr):
    """
    Ordena una lista utilizando el algoritmo de selección.
    """
    n = len(arr)  # Obtiene la longitud de la lista
    for i in range(n):  # Recorre cada elemento de la lista
        min_idx = i  # Supone que el elemento actual es el mínimo
        for j in range(i + 1, n):  # Busca el elemento más pequeño en el resto de la lista
            if arr[j] < arr[min_idx]:  # Si encuentra un elemento menor
                min_idx = j  # Actualiza el índice del mínimo encontrado
        
        # Intercambia el elemento mínimo encontrado con el primer elemento sin ordenar
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr  # Devuelve la lista ordenada

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 25, 12, 22, 11]  # Lista de ejemplo a ordenar
    print("Lista original:", lista)  # Muestra la lista original
    lista_ordenada = selection_sort(lista)  # Ordena la lista usando selection_sort
    print("Lista ordenada:", lista_ordenada)  # Muestra la lista ordenada
