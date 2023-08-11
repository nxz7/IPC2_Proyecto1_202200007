import xml.etree.ElementTree as ET
from lista_senales import lista_senales
from nodo_dato import nodo_dato
from nodo_senal import nodo_senal


def insertar_senal(lista, nombre, t, A):
    nueva_senal = lista.insertar_senal(nombre, t, A)
    return nueva_senal

def insertar_dato(nueva_senal, t_dato, A_dato, valor):
    nuevo_dato = nodo_dato(t_dato, A_dato, valor)
    if not nueva_senal.primero_dato:
        nueva_senal.primero_dato = nuevo_dato
    else:
        actual_dato = nueva_senal.primero_dato
        while actual_dato.siguiente_dato:
            actual_dato = actual_dato.siguiente_dato
        actual_dato.siguiente_dato = nuevo_dato


def imprimir(lista):
    actual_senal = lista.primero
    while actual_senal:
        print(actual_senal.nombre)
        actual_dato = actual_senal.primero_dato
        fila_actual = None
        while actual_dato:
            if fila_actual is None or fila_actual != actual_dato.t:  
                print('-' * 20)
                fila_actual = actual_dato.t
            print(actual_dato.valor, end=' ')
            actual_dato = actual_dato.siguiente_dato
        print()
        actual_senal = actual_senal.siguiente_senal
