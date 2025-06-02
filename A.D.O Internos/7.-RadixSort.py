def counting_sort_digito(arr, exp):
    """
    Subrutina de Radix Sort para ordenar por un dígito específico.
    """
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10  # Dígitos del 0 al 9

    # Contamos las ocurrencias de cada dígito
    for i in range(n):
        indice = (arr[i] // exp) % 10
        conteo[indice] += 1

    # Acumulamos los conteos
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construimos la salida
    i = n - 1
    while i >= 0:
        indice = (arr[i] // exp) % 10
        salida[conteo[indice] - 1] = arr[i]
        conteo[indice] -= 1
        i -= 1

    # Copiamos el resultado al arreglo original
    for i in range(n):
        arr[i] = salida[i]

def radix_sort(arr):
    """
    Ordena una lista utilizando Radix Sort (por dígitos).
    """
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_digito(arr, exp)
        exp *= 10
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    lista = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista original:", lista)
    lista_ordenada = radix_sort(lista)
    print("Lista ordenada:", lista_ordenada)
    