from concurrent.futures.process import _ThreadWakeup
import os
import random
import msvcrt
import time
sw=1
Mascotas=[]
flag=True 
i=0
def menu():
    print("****************************")
    print("    *Veterinaria Patitas*   ")
    print(" 1 - Registrar Mascota      ")
    print(" 2 - Listar Registros       ")
    print(" 3 - Buscar Mascota         ")
    print(" 4 - Imprimir Reportes      ")
    print(" 5 - Salir                  ")
    print("****************************")
    print("       ")

def opcion1():
    flag=True
    flag2=True
    print("     ****Registrar Mascota****")
    print("                      ")
    i=0
    while flag==True:
        print("                              ")
        id_mascota=random.randrange(10000,99999)
        print(f"El Id de su mascota es {id_mascota}")
        for Mascota in Mascotas:
            if Mascota['ID'] ==id_mascota:
                i=1
            else:
                i=0
        if i==0:
            print("Codigo Valido")
            break
        else:
            print("Codigo ya existente")
            
    print("                 ")
    nombreM=input("Ingrese nombre de mascota:")
    print("                      ")
    nombreD=input("Ingrese nombre del dueño:")
    print("                           ")
    print("   Tipo de mascota ")
    print("  Perro        Gato ")
    print("                             ")
    while flag2==True:
        tipoM=input("Escriba tipo de mascota:")
        tipoM=tipoM.capitalize()
        if tipoM =='Perro':
            flag2=False
        elif tipoM=='Gato':
            flag2=False
        else:
            print("Ingrese Mascota valida")
            flag2==True
    print("       ")
    Mascota={"ID": id_mascota, "Nombre Mascota": nombreM, "Nombre Dueño": nombreD, "Tipo": tipoM}
    Mascotas.append(Mascota)
    print("Mascota registrada")
    print("                  ")
    respuesta=input("Desea agregar otra mascota?:")
    respuesta=respuesta.lower()
    if respuesta=='si':
        flag=True
    elif respuesta=='no':
        flag=True

def opcion2():
    print("     ****Listado de Mascotas****")
    print("                       ")
    for Mascota in Mascotas:
        print(f"ID: {Mascota['ID']} Nombre Mascota: {Mascota['Nombre Mascota']} Nombre Dueño: {Mascota['Nombre Dueño']} Tipo: {Mascota['Tipo']} ")

def opcion3():
    print("     ****Buscar Mascota****")
    print("                          ")
    id_mascota=input("Ingrese ID de mascota:")
    print("                     ")
    for Mascota in Mascotas:
        if Mascota['ID']== id_mascota:
            print(f"ID: {Mascota['ID']} Nombre Mascota: {Mascota['Nombre Mascota']} Nombre Dueño: {Mascota['Nombre Dueño']} Tipo: {Mascota['Tipo']} ")
        else:
            print("Mascota no registrada")

def opcion4():
    print("     ****Imprimir Reportes****")
    print("     Tipo de mascota ")
    print(" 1- Perro         2 - Gato")
    print("                    ")
    tipoM=int(input("Escoja tipo de mascota:"))
    if tipoM==1:
        tipoM='Perro'
    elif tipoM==2:
        tipoM='Gato'
    print("                                    ")
    if tipoM == 'Perro':
        for Mascota in Mascotas:
            if Mascota['Tipo']== tipoM:
                ("***********************************")
                print(f"ID Mascota:{Mascota['ID']}")
                print(f"Nombre Mascota:{Mascota['Nombre Mascota']}")
                print(f"Tipo de mascota:{Mascota['Tipo']}")
                print("    ")
                print(f"Dueño de la mascota:{Mascota['Nombre Dueño']}")
                print("   ")
                print(f"Sr/Sra le faltan {random.randrange(1,10)} vacunas a su mascota")
                ("***********************************")
                print("          ")
    elif tipoM== 'Gato':
        for Mascota in Mascotas:
            if Mascota['Tipo']== tipoM:
                print("***********************************")
                print(f"ID Mascota:{Mascota['ID']}")
                print(f"Nombre Mascota:{Mascota['Nombre Mascota']}")
                print(f"Tipo de mascota:{Mascota['Tipo']}")
                print("    ")
                print(f"Dueño de la mascota:{Mascota['Nombre Dueño']}")
                print("   ")
                print(f"Sr/Sra le faltan {random.randrange(1,10)} vacunas a su mascota")
                print("***********************************")
                print("       ")


while sw==1:
    try:
        menu()
        opcion=int(input("Seleccione opcion:"))
        print("                       ")
        if opcion==1:
            opcion1()
        if opcion==2:
            opcion2()
        if opcion==3:
            opcion3()
        if opcion==4:
            opcion4()
        if opcion==5:
            print("                                                  ")
            for i in range(5,0,-1):
                print(f"Saliendo en...{i}")
                time.sleep(1)
                os.system("cls")
            sw=0
    except:
        print("Error, Intente nuevamente")