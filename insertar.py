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

def datos_ordenados(nueva_senal, t_dato, A_dato, valor):
    nuevo_dato = nodo_dato(t_dato, A_dato, valor)

    # empezar ingresando el 1
    if not nueva_senal.primero_dato:
        nueva_senal.primero_dato = nuevo_dato
        return

    prev_dato = None
    current_dato = nueva_senal.primero_dato
    while current_dato:
        if t_dato < current_dato.t or (t_dato == current_dato.t and A_dato <= current_dato.A):
            if prev_dato:
                prev_dato.siguiente_dato = nuevo_dato
                nuevo_dato.siguiente_dato = current_dato
            else:
                nueva_senal.primero_dato = nuevo_dato
                nuevo_dato.siguiente_dato = current_dato
            return
        prev_dato = current_dato
        current_dato = current_dato.siguiente_dato

    prev_dato.siguiente_dato = nuevo_dato

def obtener_dato(lista, nombre, t, A):
    senal = lista.obtener_senal_por_nombre(nombre)
    if senal:
        actual_dato = senal.primero_dato
        while actual_dato:
            if actual_dato.t == t and actual_dato.A == A:
                return actual_dato.valor
            actual_dato = actual_dato.siguiente_dato
    return None