def quick_sort(arr):
    """
    Ordena una lista utilizando QuickSort.
    """
    if len(arr) <= 1:
        return arr
    else:
        # Elegimos el último elemento como pivote
        pivote = arr[-1]
        menores = [x for x in arr[:-1] if x <= pivote]
        mayores = [x for x in arr[:-1] if x > pivote]
        # Mostrar el estado de la lista en cada paso
        print(f"Lista en el paso: {arr}, Pivote: {pivote}, Menores: {menores}, Mayores: {mayores}")
      

        return quick_sort(menores) + [pivote] + quick_sort(mayores)
        
        
    

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    lista_ordenada = quick_sort(lista)
    print("Lista ordenada:", lista_ordenada)