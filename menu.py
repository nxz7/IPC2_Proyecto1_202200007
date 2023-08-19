import xml.etree.ElementTree as ET
from lista_senales import lista_senales
from lista_datos import lista_datos
from nodo_dato import nodo_dato
from nodo_senal import nodo_senal
from insertar import imprimir
from insertar import insertar_dato
from insertar import insertar_senal
from procesar import procesar_bi
from nodo_procesado import nodo_procesado
from lista_procesados import lista_procesados
from lista_procesados import procesar_and_generate_data_string
from lista_procesados import procesar_bi_and_generar_lista_procesados
from lista_procesados import imprimir_procesados

import graphviz
#-------------------------------------

#-------------------------------
def mostrar_menu():
    
    lista_senalesM = lista_senales()
    lista_datosM = lista_datos()
    global ruta
    lista_final = lista_senales()

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
            ruta = input("ingresar path del xmhhhl: ")
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

                    insertar_dato(nueva_senal, t_dato, A_dato, valor)

            imprimir(lista_senalesM)

        elif opcion == "2":
            print("-------Procesar archivo---------")
            print("-------GENERANDO LA MATRIZ DE PATRONES---------")
            lista_bi = procesar_bi(lista_senalesM, lista_datosM)
            imprimir(lista_bi)

            print("-------GENERANDO LA MATRIZ DE PROCESADOS---------")
            lista_bi_procesados, lista_procesadosM = procesar_bi_and_generar_lista_procesados(lista_bi)
            imprimir_procesados(lista_procesadosM)

        elif opcion == "3":
            print("-------archivo de salida---------")
            #prueba buscar filas
            '''
            nombre_buscar = input("Ingrese el nombre de la señal que desea buscar: ")
            senal_encontrada = lista_senalesM.obtener_senal_por_nombre(nombre_buscar)
            if senal_encontrada:
                lista_senalesM.imprimir_senal_completa(nombre_buscar)
            else:
                print(f"No se encontró la señal '{nombre_buscar}'.")
            '''


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

        
                print("MATRIZ REDUCIDA GENERADA CORRECTAMENTE")
            else:
                print("ERROR - OPCION INVALIDA")

        elif opcion == "6":
            print("-------6---------")

        elif opcion == "7":
            print("Saliendo del sistema")
            break
        else:
            print("ERROR - OPCION INVALIDA")

if __name__ == "__main__":
    mostrar_menu()