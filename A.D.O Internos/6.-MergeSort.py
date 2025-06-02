def merge_sort(arr):
    """
    Ordena una lista utilizando MergeSort.
    """
    if len(arr) > 1:
        medio = len(arr) // 2
        izquierda = arr[:medio]
        derecha = arr[medio:]

        # Ordenamos cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)

        # Fusionamos ambas partes
        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        # Agregamos los elementos restantes
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

    return arr
# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    lista_ordenada = merge_sort(lista)
    print("Lista ordenada:", lista_ordenada)