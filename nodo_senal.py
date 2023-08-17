class nodo_senal:
    def __init__(self, nombre=None, t=None, A=None):
        self.nombre = nombre
        self.t = t
        self.A = A
        self.primero_dato = None
        self.siguiente_senal = None
