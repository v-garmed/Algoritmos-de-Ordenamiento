def bubble_sort(arr):
    """
    Ordena una lista utilizando el algoritmo de burbuja (intercambio).
    """
    n = len(arr)  # Obtiene la longitud de la lista
    for i in range(n):  # Recorre la lista n veces
        intercambiado = False  # Bandera para detectar si hubo intercambio en esta pasada
        for j in range(0, n - i - 1):  # Recorre la lista hasta el elemento no ordenado
            if arr[j] > arr[j + 1]:  # Compara el elemento actual con el siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambia si están en el orden incorrecto
                intercambiado = True  # Marca que hubo un intercambio
        print(f"Lista ordenada en el paso {i + 1}: {arr}")  # Muestra el estado de la lista después de cada pasada

        if not intercambiado:  # Si no hubo intercambios, la lista ya está ordenada
            break  # Sale del ciclo principal

    return arr  # Devuelve la lista ordenada

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]  # Lista de ejemplo a ordenar
    print("Lista original:", lista)  # Muestra la lista original
    lista_ordenada = bubble_sort(lista)  # Llama a la función de ordenamiento
    print("Lista ordenada:", lista_ordenada)  # Muestra la lista ordenada
