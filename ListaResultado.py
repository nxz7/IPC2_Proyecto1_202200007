from insertar import insertar_senal,obtener_dato
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree,tostring
from xml.dom import minidom
import graphviz


class NodoResultado:
    def __init__(self, nombre, t_values, A, dato):
        self.nombre = nombre
        self.t_values = t_values
        self.A = A
        self.dato = dato
        self.siguiente = None

class ListaResultado:
    def __init__(self):
        self.primero = None
    def insertar(self, nombre, t_values, A, dato):  
        nuevo_nodo = NodoResultado(nombre, t_values, A, dato)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.primero
        print("Results:")
        while actual:
            t_values_str = ', '.join(str(t) for t in actual.t_values.iterar())  
            print(f"A: {actual.A} Nombre: {actual.nombre} Dato: {actual.dato} t: {t_values_str}")
            actual = actual.siguiente
    
    def iterar(self):
        actual = self.primero
        while actual:
            yield actual
            actual = actual.siguiente

    def grafica_reducida(self, snombre):
        dot = graphviz.Digraph(format='png')

        found_signal = False
        signal_node_id = None
        t_nodes = None  

        class TNode:
            def __init__(self, t_values, node_id):
                self.t_values = t_values
                self.node_id = node_id
                self.next = None

        for nodo_resultado in self.iterar():
            if nodo_resultado.nombre == snombre:
                found_signal = True

                if signal_node_id is None:
                    signal_node_id = f'senal_{snombre}'
                    dot.node(signal_node_id, snombre)

                t_value = nodo_resultado.t_values
                t_values_str = ', '.join(str(t) for t in t_value.iterar())

                if t_nodes is None:
                    t_node_id = f't_values_{t_values_str}'
                    dot.node(t_node_id, f"t: {t_values_str}")
                    dot.edge(signal_node_id, t_node_id)
                    t_nodes = TNode(t_value, t_node_id)
                else:
                    prev_t_node = None
                    current_t_node = t_nodes
                    while current_t_node:
                        if current_t_node.t_values == t_value:
                            t_node_id = current_t_node.node_id
                            break
                        prev_t_node = current_t_node
                        current_t_node = current_t_node.next
                    else:
                        t_node_id = f't_values_{t_values_str}'
                        dot.node(t_node_id, f"t: {t_values_str}")
                        dot.edge(signal_node_id, t_node_id)
                        new_t_node = TNode(t_value, t_node_id)
                        prev_t_node.next = new_t_node

                actual = self.primero
                while actual:
                    if actual.nombre == snombre and actual.t_values == t_value:
                        data_node_id = f'data_{actual.A}_{id(actual)}'
                        dot.node(data_node_id, f"A: {actual.A}\nDato: {actual.dato}")
                        dot.edge(t_node_id, data_node_id)
                    actual = actual.siguiente

        if not found_signal:
            print(f"SEÑAL'{snombre}' NO EXISTE")
            return

        dot.render(f'{snombre}_REDUCIDA', view=True)


'''
def obtener_dato_from_repetidos_and_senales(lista_repetidos, lista_senalesM):
    resultado = ListaResultado()
    
    actual_repetidos = lista_repetidos.primero
    while actual_repetidos:
        nombre = actual_repetidos.nombre
        t_values = actual_repetidos.t_values
        
        A = 1
        while lista_senalesM.existe_senal(nombre, t_values.primero.t, A):
            dato = 0
            actual_t = t_values.primero
            while actual_t:
                dato += lista_senalesM.obtener_valor(nombre, actual_t.t, A)
                actual_t = actual_t.siguiente
            resultado.insertar(nombre, t_values, A, dato)
            A += 1
        actual_repetidos = actual_repetidos.siguiente
        
    return resultado
'''
def obtener_dato_from_repetidos_and_senales(lista_repetidos, lista_senalesM):
    resultado = ListaResultado()
    
    actual_repetidos = lista_repetidos.primero
    while actual_repetidos:
        nombre = actual_repetidos.nombre
        t_values = actual_repetidos.t_values  
        
        A = 1
        while lista_senalesM.existe_senal(nombre, t_values.primero.t, A):
            dato = 0
            actual_t = t_values.primero
            while actual_t:
                dato += lista_senalesM.obtener_valor(nombre, actual_t.t, A)
                actual_t = actual_t.siguiente
            resultado.insertar(nombre, t_values, A, dato)
            A += 1
        actual_repetidos = actual_repetidos.siguiente
        
    return resultado


def xml_de_resultado(resultado):
    root = Element("senalesReducidas")

    senal_actual = None
    grupo_actual = None

    for nodo_resultado in resultado.iterar():
        nombre = nodo_resultado.nombre  # VER EL NOMBRE
        if senal_actual is None or senal_actual.get('nombre') != nombre:
            senal_actual = SubElement(root, "senal", nombre=nombre, A=str(nodo_resultado.A))
            grupo_actual = None
        
        t_value = nodo_resultado.t_values.primero.t  # OBTENER LAS T
        if grupo_actual is None or grupo_actual.get("g") != str(t_value):
            grupo_actual = SubElement(senal_actual, "grupo", g=str(t_value))
            tiempos_element = SubElement(grupo_actual, "tiempos")
            tiempos_str = ', '.join(str(t) for t in nodo_resultado.t_values.iterar())
            tiempos_element.text = tiempos_str
            datos_grupo_element = SubElement(grupo_actual, "datosGrupo")

        dato_element = SubElement(datos_grupo_element, "dato", A=str(nodo_resultado.A))
        dato_element.text = str(nodo_resultado.dato)

    xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
    return xml_str

def guardar_xml(xml_content, file_path):
    with open(file_path, 'w') as xml_file:
        xml_file.write(xml_content)









