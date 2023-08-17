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

