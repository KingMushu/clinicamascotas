import os
import random
import msvcrt
import time
def randrange():
    for i in range(1):
        print(random.randrange(1,10,1))
sw=1
Mascotas=[]
flag=True 
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





while sw==1:
    try:
        menu()
        opcion=int(input("Seleccione opcion:"))
        print("                       ")
        if opcion==1:
            print("     ****Registrar Mascota****")
            print("                      ")
            i=0
            while flag==True:
                while flag==True:
                    print("                              ")
                    id_mascota=int(input("Ingrese ID mascota:"))
                    if id_mascota != id_mascota.isdigit():
                        print("Ingrese solo valores numericos")
                    if len(id_mascota)== 5 and id_mascota.isdigit():
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
                    elif len(id_mascota) > 5 or len(id_mascota) < 5:
                        print("Codigo Invalido, intente nuevamente")
                    
                print("                 ")
                nombreM=input("Ingrese nombre de mascota:")
                print("                      ")
                nombreD=input("Ingrese nombre del dueño:")
                print("                           ")
                print("   Tipo de mascota ")
                print("  Perro        Gato ")
                print("                             ")
                while flag==True:
                    tipoM=input("Escriba tipo de mascota:")
                    tipoM=tipoM.capitalize()
                    if tipoM =='Perro':
                        break
                    elif tipoM=='Gato':
                        break
                    else:
                        print("Ingrese Mascota valida")
                        flag==True
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
                    break
        if opcion==2:
            print("     ****Listado de Mascotas****")
            print("                       ")
            for Mascota in Mascotas:
                print(f"ID: {Mascota['ID']} Nombre Mascota: {Mascota['Nombre Mascota']} Nombre Dueño: {Mascota['Nombre Dueño']} Tipo: {Mascota['Tipo']} ")
        if opcion==3:
            print("     ****Buscar Mascota****")
            print("                          ")
            id_mascota=input("Ingrese ID de mascota:")
            print("                     ")
            for Mascota in Mascotas:
                if Mascota['ID']== id_mascota:
                    print(f"ID: {Mascota['ID']} Nombre Mascota: {Mascota['Nombre Mascota']} Nombre Dueño: {Mascota['Nombre Dueño']} Tipo: {Mascota['Tipo']} ")
                else:
                    print("Mascota no registrada")
        if opcion==4:
            print("     ****Imprimir Reportes****")
            print("     Tipo de mascota ")
            print(" 1- Perro         2 - Gato")
            print("                    ")
            tipoM=int(input("Escriba tipo de mascota:"))
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
        if opcion==5:
            print("                                                  ")
            for i in range(5,0,-1):
                print(f"Saliendo en...{i}")
                time.sleep(1)
                os.system("cls")
            sw=0
    except:
        print("Error, Intente nuevamente")