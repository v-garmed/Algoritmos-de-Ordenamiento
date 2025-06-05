# Clase para representar cada nodo del árbol
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor            # Valor almacenado en el nodo
        self.izquierda = None         # Referencia al hijo izquierdo
        self.derecha = None           # Referencia al hijo derecho

# Función para insertar un valor en el árbol
def insertar_en_arbol(raiz, valor):
    if raiz is None:                  # Si el árbol está vacío, crea un nuevo nodo
        return NodoArbol(valor)
    if valor < raiz.valor:            # Si el valor es menor, inserta en el subárbol izquierdo
        raiz.izquierda = insertar_en_arbol(raiz.izquierda, valor)
    else:                             # Si el valor es mayor o igual, inserta en el subárbol derecho
        raiz.derecha = insertar_en_arbol(raiz.derecha, valor)
    return raiz                       # Devuelve la raíz actualizada

# Recorrido inorden para recuperar los elementos ordenados
def recorrido_inorden(nodo, resultado):
    if nodo is not None:              # Si el nodo existe
        recorrido_inorden(nodo.izquierda, resultado)  # Recorre el subárbol izquierdo
        resultado.append(nodo.valor)                  # Agrega el valor del nodo actual
        recorrido_inorden(nodo.derecha, resultado)    # Recorre el subárbol derecho

def tree_sort(arr):
    """
    Ordena una lista utilizando ordenamiento por árbol binario.
    """
    raiz = None                       # Inicializa la raíz del árbol como vacía
    for valor in arr:                 # Inserta cada elemento del arreglo en el árbol
        raiz = insertar_en_arbol(raiz, valor)
    
    resultado = []                    # Lista para almacenar los elementos ordenados
    recorrido_inorden(raiz, resultado) # Realiza el recorrido inorden para llenar la lista
    return resultado                  # Devuelve la lista ordenada

# Ejemplo de uso
if __name__ == "__main__":
    lista = [5, 3, 8, 1, 4, 7, 6]    # Lista de ejemplo a ordenar
    print("Lista original:", lista)   # Imprime la lista original
    lista_ordenada = tree_sort(lista) # Ordena la lista usando tree_sort
    print("Lista ordenada:", lista_ordenada) # Imprime la lista ordenada
