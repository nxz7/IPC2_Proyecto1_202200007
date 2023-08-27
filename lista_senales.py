from nodo_senal import nodo_senal
import graphviz

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
    def obtener_senal_por_nombre(self, nombre):
        actual = self.primero
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente_senal
        return None

    def imprimir_fila_de_senal(self, nombre, t_fila):
        senal = self.obtener_senal_por_nombre(nombre)
        if senal:
            print(f"Fila {t_fila} de la señal '{nombre}':")
            actual_dato = senal.primero_dato
            while actual_dato:
                if actual_dato.t == t_fila:
                    print(actual_dato.valor, end=' ')
                actual_dato = actual_dato.siguiente_dato
            print()
        else:
            print(f"No se encontró la señal '{nombre}'.")
    
    def imprimir_senal_completa(self, nombre):
        senal = self.obtener_senal_por_nombre(nombre)
        if senal:
            print(f"Señal '{nombre}':")
            actual_dato = senal.primero_dato
            fila_actual = None
            while actual_dato:
                if fila_actual is None or fila_actual != actual_dato.t:
                    print('-' * 20)
                    fila_actual = actual_dato.t
                print(actual_dato.valor, end=' ')
                actual_dato = actual_dato.siguiente_dato
            print()
        else:
            print(f"No se encontró la señal '{nombre}'.")


    #SOLO DATOS, MATRIZ HACIA ABAJO 
    def generar_grafico_senal(self, nombre):
        senal = self.obtener_senal_por_nombre(nombre)
        if senal:
            dot = graphviz.Digraph(format='png')
            dot.node('S', nombre)
            actual_dato = senal.primero_dato
            fila_cuenta = 0 #fila  cuenta - para que se agrupen los datos con la misma 1 =fila
            while actual_dato:
                if fila_cuenta == 0 or actual_dato.t != fila_cuenta:
                    fila_cuenta = actual_dato.t
                    dot.node(f'dato{fila_cuenta}_1', f'Fila {fila_cuenta}')
                    dot.edge('S', f'dato{fila_cuenta}_1')
                dot.node(f'dato{fila_cuenta}_{actual_dato.A}', str(actual_dato.valor))
                if actual_dato.A > 1:
                    dot.edge(f'dato{fila_cuenta}_{actual_dato.A-1}', f'dato{fila_cuenta}_{actual_dato.A}')
                actual_dato = actual_dato.siguiente_dato
            dot.render(nombre, view=False)
        else:
            print(f"No se encontró la señal '{nombre}'.")

    def existe_senal(self, nombre, t, A):
        senal = self.obtener_senal_por_nombre(nombre)
        if senal:
            actual_dato = senal.primero_dato
            while actual_dato:
                if actual_dato.t == t and actual_dato.A == A:
                    return True
                actual_dato = actual_dato.siguiente_dato
        return False

    def obtener_valor(self, nombre, t, A):
        senal = self.obtener_senal_por_nombre(nombre)
        if senal:
            actual_dato = senal.primero_dato
            while actual_dato:
                if actual_dato.t == t and actual_dato.A == A:
                    return actual_dato.valor
                actual_dato = actual_dato.siguiente_dato
        return 0
    
    def clear_lista(self):
        self.primero = None




