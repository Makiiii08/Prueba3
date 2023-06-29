from Cliente import *

import random as rn

lista_cita=0

lista_cita: list[any]=[]


def grabarCita(lista_cita):
    cita = Cliente()

    c = False
    while c == False:
        c = cita.setCodigo_cliente(input("Ingrese Codigo Cliente"))

    c = False
    while c == False:
        c = cita.setNombre_cliente(input("Ingrese Nombre Cliente"))

    c = False
    while c == False:
        try:
           c = cita.setCosto(int(input("Ingrese Costo")))

        except BaseException as error:
            print(f"Error: {error}")

    cita.fecha_cliente = input("Ingrese Fecha Cliente")
    cita.descripcion = input("Ingrese Descripcion Cliente")
    cita.atencion = input("Ingrese Atencion del cliente")


    lista_cita.append(cita)
    if cita.costo > 45000:
        print("Cliente Registrado con masaje GRATIS ....")
    else:
        print("Cliente Registrado")


def buscarCita(lista_cita):
    codigo_cliente = input("Ingrese codigo cliente a buscar")
    flag = False
    for cita in lista_cita:
        if cita.codigo_cliente == codigo_cliente:
            flag = True
            print(f"Codigo cliente      {cita.codigo_cliente}")
            print(f"Nombre Cliente      {cita.nombre_cliente}")
            print(f"Fecha Cita          {cita.fecha_cliente} ")
            print(f"Descripcion Cliente {cita.descripcion}")
            print(f"Atencion Cliente    {cita.atencion} ")
            print(f"Costo Cita          {cita.costo} ")

        if cita.costo > 45000:
            print("Tiene Masaje Gratis")



def imprimirAtencion(lista_cita):
    print("1) Boleta Cita")
    print("2) Cita Gratis")
    try:
        at=int(input("Seleccione 1-2"))

        match at:
            case 1:
                print("Boleta")

            case 2:
                print("Cita Gratis")
            case _:
                print("Opcion Incorrecta")


    except BaseException as error:
        print(f"Error:{error}")




def salirPrograma():
    print("Nicolas Miranda 002_D FORMA D")





ciclo = True





while ciclo:
    print("Peluqueria Mechas Locas")
    print("1) Grabar Cita")
    print("2) Buscar Cita ")
    print("3) Imprimir Atencion")
    print("4) Salir")
    try:
        op=int(input("Seleccione (1-4): "))
        match op:
            case 1:
                print("Grabar Cita")
                grabarCita(lista_cita)
            case 2:
                print("Buscar Cita")
                buscarCita(lista_cita)
            case 3:
                print("Imprimir Atencion")
                imprimirAtencion(lista_cita)
            case 4:
                print("Salir")
                salirPrograma()
                ciclo = False
            case _:
                print("Opcion Incorrecta ")



    except BaseException as error:
        print(f"Error :{error}")
