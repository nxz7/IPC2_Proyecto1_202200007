from nodo_senal import nodo_senal

class lista_senales:
    def __init__(self):
        self.primero = None

    def insertar_senal(self, nombre, t, A):
        nueva_senal = nodo_senal(nombre, t, A)
        if not self.primero:
            self.primero = nueva_senal
        else:
            actual = self.primero
            while actual.siguiente_senal:
                actual = actual.siguiente_senal
            actual.siguiente_senal = nueva_senal

        return nueva_senal

    def obtener_senal(self, indice):
        actual = self.primero
        contador = 0
        while actual:
            if contador == indice:
                return actual
            contador += 1
            actual = actual.siguiente_senal
        return None
