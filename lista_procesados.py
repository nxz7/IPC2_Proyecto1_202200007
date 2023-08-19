from nodo_procesado import nodo_procesado
from lista_senales import lista_senales


class lista_procesados:
    def __init__(self):
        self.primero = None

    def insertar_procesado(self, t, data_str):
        nuevo_procesado = nodo_procesado(t, data_str)
        if not self.primero:
            self.primero = nuevo_procesado
        else:
            actual = self.primero
            while actual.siguiente_procesado:
                actual = actual.siguiente_procesado
            actual.siguiente_procesado = nuevo_procesado
    
def procesar_and_generate_data_string(senal):
    data_str = ""
    actual_dato = senal.primero_dato
    t_current = None
    while actual_dato:
        if t_current is None or t_current != actual_dato.t:
            if data_str:
                data_str += "--"  
            t_current = actual_dato.t
            data_str += f"t={t_current}, "
        data_str += str(actual_dato.valor)
        actual_dato = actual_dato.siguiente_dato
    return data_str


def procesar_bi_and_generar_lista_procesados(lista_senalesM):
    nueva_lista = lista_senales()
    lista_procesadosM = lista_procesados()

    actual_senal = lista_senalesM.primero
    while actual_senal:
        n_senal = nueva_lista.insertar_senal(actual_senal.nombre, actual_senal.t, actual_senal.A)

        data_str = procesar_and_generate_data_string(actual_senal)
        lista_procesadosM.insertar_procesado(actual_senal.nombre, data_str)

        actual_senal = actual_senal.siguiente_senal

    return nueva_lista, lista_procesadosM

def imprimir_procesados(lista_procesadosM):
    actual_procesado = lista_procesadosM.primero
    while actual_procesado:
        print(f"Signal '{actual_procesado.t}': {actual_procesado.data_str} ")
        actual_procesado = actual_procesado.siguiente_procesado