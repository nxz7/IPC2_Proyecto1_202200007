import xml.etree.ElementTree as ET
from lista_senales import lista_senales
from lista_datos import lista_datos
from nodo_dato import nodo_dato
from nodo_senal import nodo_senal
from insertar import imprimir
from insertar import insertar_dato
from insertar import insertar_senal
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import fromstring
from ListaComparacion import ListaComparacion
from NodoRepetidos import NodoRepetidos
from NodoT import NodoT
#from nodo_procesado import nodo_procesado
#from lista_procesados import lista_procesados

def procesar_bi(lista_senalesM, lista_datosM):
    nueva_lista = lista_senales()
    
    actual_senal = lista_senalesM.primero
    while actual_senal:
        n_senal = nueva_lista.insertar_senal(actual_senal.nombre, actual_senal.t, actual_senal.A)
        
        actual_dato = actual_senal.primero_dato
        while actual_dato:
            n_valor = 1 if actual_dato.valor != 0 else 0
            insertar_dato(n_senal , actual_dato.t, actual_dato.A, n_valor)
            
            actual_dato = actual_dato.siguiente_dato
        
        actual_senal= actual_senal.siguiente_senal
    
    return nueva_lista

def procesar_lista_comparacion(lista_comp, lista_rep):
    actual_nodo_comp = lista_comp.primero
    while actual_nodo_comp:
        nombre_actual = actual_nodo_comp.nombre
        string_actual = actual_nodo_comp.string_datos
        t_actual = actual_nodo_comp.t

        print(f"Comparando: Nombre={nombre_actual}, String={string_actual}, t={t_actual}")

        # ver la comparacion
        repetido_existente = False
        actual_nodo_repetidos = lista_rep.primero
        while actual_nodo_repetidos:
            if actual_nodo_repetidos.nombre == nombre_actual and actual_nodo_repetidos.string_datos == string_actual:
                print("Match found in lista_repetidos")
                actual_nodo_repetidos.t_values.insertar(t_actual)
                repetido_existente = True
                break
            actual_nodo_repetidos = actual_nodo_repetidos.siguiente
        
        # si no existe la combinacion agregar solo la t 
        if not repetido_existente:
            nuevo_nodo_rep = NodoRepetidos(nombre_actual, t_actual)
            nuevo_nodo_rep.string_datos = string_actual
            nuevo_nodo_rep.t_values.insertar(t_actual)
            if lista_rep.primero is None:
                lista_rep.primero = nuevo_nodo_rep
            else:
                actual_rep = lista_rep.primero
                while actual_rep.siguiente:
                    actual_rep = actual_rep.siguiente
                actual_rep.siguiente = nuevo_nodo_rep
        
        actual_nodo_comp = actual_nodo_comp.siguiente

        actual_nodo_repetidos = lista_rep.primero
        while actual_nodo_repetidos:
            if actual_nodo_repetidos.nombre == nombre_actual and actual_nodo_repetidos.string_datos == string_actual:
                break
            actual_nodo_repetidos = actual_nodo_repetidos.siguiente

