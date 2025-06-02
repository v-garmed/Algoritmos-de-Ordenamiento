# Clase para representar cada nodo del árbol
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para insertar un valor en el árbol
def insertar_en_arbol(raiz, valor):
    if raiz is None:
        return NodoArbol(valor)
    if valor < raiz.valor:
        raiz.izquierda = insertar_en_arbol(raiz.izquierda, valor)
    else:
        raiz.derecha = insertar_en_arbol(raiz.derecha, valor)
    return raiz

# Recorrido inorden para recuperar los elementos ordenados
def recorrido_inorden(nodo, resultado):
    if nodo is not None:
        recorrido_inorden(nodo.izquierda, resultado)
        resultado.append(nodo.valor)
        recorrido_inorden(nodo.derecha, resultado)

def tree_sort(arr):
    """
    Ordena una lista utilizando ordenamiento por árbol binario.
    """
    raiz = None
    for valor in arr:
        raiz = insertar_en_arbol(raiz, valor)
    
    resultado = []
    recorrido_inorden(raiz, resultado)
    return resultado

# Clase para representar cada nodo del árbol
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para insertar un valor en el árbol
def insertar_en_arbol(raiz, valor):
    if raiz is None:
        return NodoArbol(valor)
    if valor < raiz.valor:
        raiz.izquierda = insertar_en_arbol(raiz.izquierda, valor)
    else:
        raiz.derecha = insertar_en_arbol(raiz.derecha, valor)
    return raiz

# Recorrido inorden para recuperar los elementos ordenados
def recorrido_inorden(nodo, resultado):
    if nodo is not None:
        recorrido_inorden(nodo.izquierda, resultado)
        resultado.append(nodo.valor)
        recorrido_inorden(nodo.derecha, resultado)

def tree_sort(arr):
    """
    Ordena una lista utilizando ordenamiento por árbol binario.
    """
    raiz = None
    for valor in arr:
        raiz = insertar_en_arbol(raiz, valor)
    
    resultado = []
    recorrido_inorden(raiz, resultado)
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    lista = [5, 3, 8, 1, 4, 7, 6]
    print("Lista original:", lista)
    lista_ordenada = tree_sort(lista)
    print("Lista ordenada:", lista_ordenada)