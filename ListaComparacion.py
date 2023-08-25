from NodoComparacion import NodoComparacion

class ListaComparacion:
    def __init__(self):
        self.primero = None

    def insertar(self, nombre, t, string_datos):
        nuevo_nodo = NodoComparacion(nombre, t, string_datos)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def clear_listaC(self):
        self.primero = None