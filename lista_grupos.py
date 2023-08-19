from nodo_grupo import nodo_grupo
class lista_grupos:
    def __init__(self):
        self.primero = None

    def insertar_grupo(self, t, data_str):
        nuevo_nodo = nodo_grupo(t, data_str)
        nuevo_nodo.next_grupo = self.primero
        self.primero = nuevo_nodo