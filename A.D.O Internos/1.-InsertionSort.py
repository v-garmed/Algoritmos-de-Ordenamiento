def insertion_sort(arr):
    """
    Ordena una lista utilizando el algoritmo de inserción.
    """
    for i in range(1, len(arr)):
        # Guardamos el valor actual
        valor_actual = arr[i]
        j = i - 1

        # Mover los elementos mayores que valor_actual una posición a la derecha
        while j >= 0 and arr[j] > valor_actual:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insertamos el valor_actual en su posición correcta
        arr[j + 1] = valor_actual

    return arr
# Ejemplo de uso
if __name__ == "__main__":
    lista = [5, 2, 9, 1, 5, 6]
    print("Lista original:", lista)
    lista_ordenada = insertion_sort(lista)
    print("Lista ordenada:", lista_ordenada)
