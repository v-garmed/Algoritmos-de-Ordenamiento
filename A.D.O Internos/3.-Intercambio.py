def bubble_sort(arr):
    """
    Ordena una lista utilizando el algoritmo de burbuja (intercambio).
    """
    n = len(arr)
    for i in range(n):
        # Bandera para detectar si hubo intercambio
        intercambiado = False
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambiado = True
        # Mostrar el estado de la lista en cada paso
        print(f"Lista ordenada en el paso {i + 1}: {arr}")


        # Si no se hizo ningún intercambio, la lista ya está ordenada
        if not intercambiado:
            break
    
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    lista_ordenada = bubble_sort(lista)
    print("Lista ordenada:", lista_ordenada)