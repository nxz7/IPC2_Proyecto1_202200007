from NodoT import NodoT
class ListaT:
    def __init__(self):
        self.primero = None

    def insertar(self, t):
        nuevo_nodo = NodoT(t)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo