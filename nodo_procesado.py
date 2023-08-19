class nodo_procesado:
    def __init__(self, t=None, data_str=None):
        self.t = t
        self.data_str = data_str
        self.siguiente_procesado = None