def insertion_sort(arr):
    """
    Ordena una lista utilizando el algoritmo de inserción.
    """
    # Recorre la lista desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        # Guarda el valor actual que se va a insertar en la posición correcta
        valor_actual = arr[i]
        # Inicializa j para comparar con los elementos anteriores
        j = i - 1

        # Desplaza los elementos mayores que valor_actual una posición a la derecha
        while j >= 0 and arr[j] > valor_actual:
            arr[j + 1] = arr[j]  # Mueve el elemento hacia la derecha
            j -= 1  # Decrementa j para seguir comparando hacia la izquierda
        
        # Inserta valor_actual en la posición correcta
        arr[j + 1] = valor_actual

    # Devuelve la lista ordenada
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [5, 2, 9, 1, 5, 6]  # Lista original desordenada
    print("Lista original:", lista)
    lista_ordenada = insertion_sort(lista)  # Ordena la lista
    print("Lista ordenada:", lista_ordenada)
