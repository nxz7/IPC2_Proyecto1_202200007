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
            row_count = 0
            while actual_dato:
                if row_count == 0 or actual_dato.t != row_count:
                    row_count = actual_dato.t
                    dot.node(f'dato{row_count}_1', f'Fila {row_count}')
                    dot.edge('S', f'dato{row_count}_1')
                dot.node(f'dato{row_count}_{actual_dato.A}', str(actual_dato.valor))
                if actual_dato.A > 1:
                    dot.edge(f'dato{row_count}_{actual_dato.A-1}', f'dato{row_count}_{actual_dato.A}')
                actual_dato = actual_dato.siguiente_dato
            dot.render(nombre, view=False)
        else:
            print(f"No se encontró la señal '{nombre}'.")

#FILAS - HORIZONTAS
'''
    def generar_grafico_senal(self, nombre):
        senal = self.obtener_senal_por_nombre(nombre)
        if senal:
            dot = graphviz.Digraph(format='png')
            dot.node('S', nombre)
            actual_dato = senal.primero_dato
            fila_actual = None
            while actual_dato:
                if fila_actual is None or fila_actual != actual_dato.t:
                    fila_actual = actual_dato.t
                    with dot.subgraph() as s:
                        s.attr(rank='same')
                        s.node(f'fila{fila_actual}', f'Fila {fila_actual}')
                    dot.edge('S', f'fila{fila_actual}', rank='same')
                dot.node(f'dato{actual_dato.t}_{actual_dato.A}', str(actual_dato.valor))
                dot.edge(f'fila{fila_actual}', f'dato{actual_dato.t}_{actual_dato.A}')
                actual_dato = actual_dato.siguiente_dato
            dot.render('grafica', view=False)
        else:
            print(f"No se encontró la señal '{nombre}'.")
'''
#OTRO ESTILO DE GRAFICO - DATOS Y MATRIX PARA ABAJO
#'''
'''
    def generar_grafico_senal(self, nombre):
        senal = self.obtener_senal_por_nombre(nombre)
        if senal:
            dot = graphviz.Digraph(format='png')
            dot.node('S', nombre)
            actual_dato = senal.primero_dato
            row_node = None
            current_row = 0
            current_column = 0
            while actual_dato:
                if current_row != actual_dato.t:
                    current_row = actual_dato.t
                    row_node = f'fila{current_row}'
                    dot.node(row_node, f'Fila {current_row}')
                    dot.edge('S', row_node)
                    current_column = 1
                else:
                    current_column += 1
                data_node = f'dato{current_row}_{current_column}'
                dot.node(data_node, str(actual_dato.valor))
                if current_column > 1:
                    prev_data_node = f'dato{current_row}_{current_column - 1}'
                    dot.edge(prev_data_node, data_node)
                actual_dato = actual_dato.siguiente_dato
            dot.render('grafica', view=False)
        else:
            print(f"No se encontró la señal '{nombre}'.")
'''



