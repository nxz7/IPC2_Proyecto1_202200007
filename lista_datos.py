from nodo_dato import nodo_dato

class lista_datos:
    def __init__(self):
        self.primero = None

    def insertar_dato(self, t, A, valor):
        nuevo_dato = nodo_dato(t, A, valor)
        if not self.primero:
            self.primero = nuevo_dato
        else:
            actual = self.primero
            while actual.siguiente_dato:
                actual = actual.siguiente_dato
            actual.siguiente_dato = nuevo_dato

    def obtener_dato(self, t, A):
        actual = self.primero
        while actual:
            if actual.t == t and actual.A == A:
                return actual.valor
            actual = actual.siguiente_dato
        return None
    
    def clear_listad(self):
        self.primero = None