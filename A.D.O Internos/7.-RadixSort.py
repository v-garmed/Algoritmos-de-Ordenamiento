def counting_sort_digito(arr, exp):
    """
    Subrutina de Radix Sort para ordenar por un dígito específico.
    """
    n = len(arr)  # Longitud del arreglo
    salida = [0] * n  # Arreglo de salida para almacenar el resultado ordenado
    conteo = [0] * 10  # Arreglo para contar ocurrencias de cada dígito (0-9)

    # Contamos las ocurrencias de cada dígito en la posición actual (exp)
    for i in range(n):
        indice = (arr[i] // exp) % 10  # Extrae el dígito relevante
        conteo[indice] += 1  # Incrementa el conteo para ese dígito

    # Acumulamos los conteos para obtener las posiciones finales
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    # Construimos el arreglo de salida ordenado según el dígito actual
    i = n - 1
    while i >= 0:
        indice = (arr[i] // exp) % 10  # Extrae el dígito relevante
        salida[conteo[indice] - 1] = arr[i]  # Coloca el elemento en su posición ordenada
        conteo[indice] -= 1  # Decrementa el conteo para ese dígito
        i -= 1

    # Copiamos el resultado ordenado al arreglo original
    for i in range(n):
        arr[i] = salida[i]

def radix_sort(arr):
    """
    Ordena una lista utilizando Radix Sort (por dígitos).
    """
    max_num = max(arr)  # Encuentra el número máximo para saber el número de dígitos
    exp = 1  # Inicializa el exponente (1, 10, 100, ...)
    while max_num // exp > 0:  # Itera por cada dígito
        counting_sort_digito(arr, exp)  # Ordena por el dígito actual
        exp *= 10  # Pasa al siguiente dígito
    return arr  # Devuelve el arreglo ordenado

# Ejemplo de uso
if __name__ == "__main__":
    lista = [170, 45, 75, 90, 802, 24, 2, 66]  # Lista de ejemplo
    print("Lista original:", lista)  # Muestra la lista original
    lista_ordenada = radix_sort(lista)  # Ordena la lista usando Radix Sort
    print("Lista ordenada:", lista_ordenada)  # Muestra la lista ordenada
