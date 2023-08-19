from ListaT import ListaT
class NodoRepetidos:
    def __init__(self, nombre, t):
        self.nombre = nombre
        self.t_values = ListaT()  # varios t
        self.siguiente = None