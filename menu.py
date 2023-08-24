import xml.etree.ElementTree as ET
from lista_senales import lista_senales
from lista_datos import lista_datos
from nodo_dato import nodo_dato
from nodo_senal import nodo_senal
from insertar import imprimir
from insertar import insertar_dato, datos_ordenados
from insertar import insertar_senal,obtener_dato
from procesar import procesar_bi, procesar_lista_comparacion
from ListaComparacion import ListaComparacion
from NodoRepetidos import NodoRepetidos
from NodoT import NodoT
from ListaRepetidos import ListaRepetidos
from ListaT import ListaT
from ListaResultado import NodoResultado,ListaResultado,obtener_dato_from_repetidos_and_senales,xml_de_resultado,guardar_xml
#from ListaGrupos import ListaGrupos
import os
import graphviz
#-menu

#-------------------------------
def mostrar_menu():
    
    lista_senalesM = lista_senales()
    lista_datosM = lista_datos()
    global ruta


    

    while True:
        print("\n-----------------------------------")
        print("Proyecto 1 - IPC 2")
        print("-----------------------------------")
        print("MENU PRINCIPAL")
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo de salida")
        print("4. Datos del estudiante")
        print("5.Generar grafica")
        print("6. Inicializar sistema")
        print("7. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            print("-------CARGAR ARCHIVO---------")
            ruta = input("ingresar path del xml: ")
            ar = ET.parse(ruta)
            rt = ar.getroot()
            # ITERAR SOBRE SENAL -  SENAL> DATOS
            for senal_elem in rt.findall('senal'):
                nombre = senal_elem.get('nombre')
                t = int(senal_elem.get('t', '0'))  # CONDICION DE QUE CERO SI FALTA
                A = int(senal_elem.get('A', '0'))  

                nueva_senal = insertar_senal(lista_senalesM, nombre, t, A)

                for dato_elem in senal_elem.findall('dato'):
                    t_dato = int(dato_elem.get('t', '0'))  
                    A_dato = int(dato_elem.get('A', '0'))  # CONDICION DE QUE CERO SI FALTA
                    valor = int(dato_elem.text)

                    datos_ordenados(nueva_senal, t_dato, A_dato, valor)

            imprimir(lista_senalesM)

        elif opcion == "2":
            print("-------Procesar archivo---------")
            print("-------GENERANDO LA MATRIZ DE PATRONES---------")
            lista_bi = procesar_bi(lista_senalesM, lista_datosM)
            imprimir(lista_bi)

            print("-------GENERANDO Lista de comparacion---------")

            lista_comparacion = ListaComparacion()

# iterar en la señal
            actual_senal = lista_bi.primero
            while actual_senal:
                nombre_senal = actual_senal.nombre
                t_comun = None
                string_datos_comun = ""

    #iterar en los nodos de cada señak
                actual_dato = actual_senal.primero_dato
                while actual_dato:
                    if t_comun is None:
                        t_comun = actual_dato.t
                    if actual_dato.t == t_comun:
                        string_datos_comun += str(actual_dato.valor) + " "
                    else:
            # insertar cuando t cambie
                        lista_comparacion.insertar(nombre_senal, t_comun, string_datos_comun)
                        t_comun = actual_dato.t
                        string_datos_comun = str(actual_dato.valor) + " "
                    actual_dato = actual_dato.siguiente_dato

    #INSERTAR el valor de t
                lista_comparacion.insertar(nombre_senal, t_comun, string_datos_comun)
                actual_senal = actual_senal.siguiente_senal

#IMPRIMIR lista_comparacion
            actual_nodo_comparacion = lista_comparacion.primero
            while actual_nodo_comparacion:
                print("Nombre:", actual_nodo_comparacion.nombre)
                print("t:", actual_nodo_comparacion.t)
                print("Datos:", actual_nodo_comparacion.string_datos)
                print("-" * 20)
                actual_nodo_comparacion = actual_nodo_comparacion.siguiente
                #-----------------------------------------------------------------------
            print("-------ver repetidos---------")
            lista_repetidos = ListaRepetidos()
# AGREGAR A LA LISTA DE REPETIDOS Y LUEGO SE IMPRIME EN BASE A LA LISTA DE COMPARACION ANTERIOR
            procesar_lista_comparacion(lista_comparacion, lista_repetidos)
            print("-------proceso de imprimir---------")

            actual_nodo_repetidos = lista_repetidos.primero
            while actual_nodo_repetidos:
                print("Nombre:", actual_nodo_repetidos.nombre)
                print("t values:", end=" ")
    
                actual_t_node = actual_nodo_repetidos.t_values.primero
                while actual_t_node:
                    print(actual_t_node.t, end=" ")
                    actual_t_node = actual_t_node.siguiente
    
                print("\n" + "-" * 20)
                actual_nodo_repetidos = actual_nodo_repetidos.siguiente
#----------------------- YA FINAL
            print("-------SENALES REDUCIDAS---------")
            resultado = obtener_dato_from_repetidos_and_senales(lista_repetidos, lista_senalesM)
            resultado.imprimir()

        elif opcion == "3":
            print("-------archivo de salida---------")
            user_file_path = input("ingrese la ruta donde desea guardar el archivo: ")

            xml_data = xml_de_resultado(resultado)
            guardar_xml(xml_data, user_file_path)
            print("ARCHIVO DE SALIDA DE MATRIZ REDUCIDA GENERADO CORRECTAMENTE")

        elif opcion == "4":
            print("NATALIA MARIEL CALDERON ECHEVERRIA")
            print("202200007")
            print("INTRODUCCION A LA PROGRAMACION Y COMPUTACION 2 - ")
            print("4to SEMESTRE")
        elif opcion == "5":
            print("-------GENERAR GRAFICA---------")

            print("1.matriz de archivo de entrada")
            print("2.matriz reducida")
            opcion5 = input("Ingrese una opción: ")
            #---
            if opcion5=="1":
                nombre_buscar = input("Ingrese el nombre de la señal que desea graficar: ")
                senal_encontrada = lista_senalesM.obtener_senal_por_nombre(nombre_buscar)
                if senal_encontrada:
                    lista_senalesM.generar_grafico_senal(nombre_buscar)
                    print("GRAFICA DE MATRIZ DE ENTRADA GENERADA CORRECTAMENTE")
                else:
                    print(f"No se encontró la señal '{nombre_buscar}'.")
                
            elif opcion5=="2":
                snombre = input("Ingrese el nombre de la señal que desea graficar: ")
                resultado.grafica_reducida(snombre)

        
                print("GRAFICA DE MATRIZ REDUCIDA GENERADA CORRECTAMENTE")
            else:
                print("ERROR - OPCION INVALIDA")

        elif opcion == "6":
            print("-------Inicializar sistema--------")
            

        elif opcion == "7":
            print("Saliendo del sistema")
            break
        else:
            print("ERROR - OPCION INVALIDA")


if __name__ == "__main__":
    mostrar_menu()