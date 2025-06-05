def quick_sort(arr):
    """
    Ordena una lista utilizando QuickSort.
    """
    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(arr) <= 1:
        return arr
    else:
        # Elegimos el último elemento como pivote
        pivote = arr[-1]
        # Creamos una lista con los elementos menores o iguales al pivote
        menores = [x for x in arr[:-1] if x <= pivote]
        # Creamos una lista con los elementos mayores al pivote
        mayores = [x for x in arr[:-1] if x > pivote]
        # Mostrar el estado de la lista en cada paso (para seguimiento)
        print(f"Lista en el paso: {arr}, Pivote: {pivote}, Menores: {menores}, Mayores: {mayores}")
        # Llamada recursiva para ordenar las sublistas y combinar el resultado
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos una lista de ejemplo
    lista = [64, 34, 25, 12, 22, 11, 90]
    # Mostramos la lista original
    print("Lista original:", lista)
    # Ordenamos la lista usando quick_sort
    lista_ordenada = quick_sort(lista)
    # Mostramos la lista ordenada
    print("Lista ordenada:", lista_ordenada)