def merge_sort(arr):
    """
    Ordena una lista utilizando MergeSort.
    """
    # Si la lista tiene más de un elemento
    if len(arr) > 1:
        medio = len(arr) // 2  # Calcula el punto medio de la lista
        izquierda = arr[:medio]  # Divide la lista en la mitad izquierda
        derecha = arr[medio:]    # Divide la lista en la mitad derecha

        # Ordena recursivamente la mitad izquierda
        merge_sort(izquierda)
        # Ordena recursivamente la mitad derecha
        merge_sort(derecha)

        # Fusiona ambas mitades ordenadas
        i = j = k = 0  # Inicializa los índices para izquierda, derecha y arr
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]  # Coloca el menor elemento en arr
                i += 1
            else:
                arr[k] = derecha[j]    # Coloca el menor elemento en arr
                j += 1
            k += 1

        # Copia los elementos restantes de izquierda (si hay)
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        # Copia los elementos restantes de derecha (si hay)
        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

    return arr  # Devuelve la lista ordenada

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]  # Lista original
    print("Lista original:", lista)
    lista_ordenada = merge_sort(lista)     # Ordena la lista
    print("Lista ordenada:", lista_ordenada)  # Imprime la lista ordenada