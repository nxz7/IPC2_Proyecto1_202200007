import xml.etree.ElementTree as ET
from lista_senales import lista_senales
from lista_datos import lista_datos
from nodo_dato import nodo_dato
from nodo_senal import nodo_senal
from insertar import imprimir
from insertar import insertar_dato
from insertar import insertar_senal


def mostrar_menu():
    
    lista_senalesM = lista_senales()
    lista_datosM = lista_datos()

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
                t = int(senal_elem.get('t'))
                A = int(senal_elem.get('A'))
            # METER LA SEÑAL
                nueva_senal = insertar_senal(lista_senalesM, nombre, t, A)
            # ITERAR EN LO DEL DATO
                for dato_elem in senal_elem.findall('dato'):
                    t_dato = int(dato_elem.get('t'))
                    A_dato = int(dato_elem.get('A'))
                    valor = int(dato_elem.text)
            # METER LOS DATOS EN LA SEÑAL
                    insertar_dato(nueva_senal, t_dato, A_dato, valor)
            imprimir(lista_senalesM)


        elif opcion == "2":
            print("-------Procesar archivo---------")


        elif opcion == "3":
            print("-------archivo de salida---------")
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
                print("GRAFICA DE MATRIZ DE ENTRADA GENERADA CORRECTAMENTE")
            elif opcion5=="2":
                print("GRAFICA DE MATRIZ REDUCIDA GENERADA CORRECTAMENTE")
            else:
                print("ERROR - OPCION INVALIDA")

        elif opcion == "6":
            print("-------6---------")

        elif opcion == "7":
            print("Saliendo del sistema")
            break
        else:
            print("ERROR - OPCION INVALIDA")

mostrar_menu()