from NodoRepetidos import NodoRepetidos
class ListaRepetidos:
    def __init__(self):
        self.primero = None

    def insertar(self, nombre, t):
        nuevo_nodo = NodoRepetidos(nombre, t)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
