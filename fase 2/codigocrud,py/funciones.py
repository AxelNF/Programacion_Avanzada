from clases import *

def menu():
    while True:
        print('[1] Crear estudiante')
        print('[2] Buscar estudiante')
        print('[3] Eliminar estudiante')
        print('[X] Salir')
        
        opc = input('Seleccione opción: ')
        if opc not in ['1','2','3','X','x']:
            print('Seleccione una opción válida.')
        elif opc == '1':
            crear()
        elif opc == '2':
            pass
        elif opc == '3':
            pass
        else:
            print('Saliendo...')
            break

def crear(estudiantes):
    nombre = input('Ingrese nombre: ')
    matricula = int(input('Ingrese matricula: '))
    estudiante() = (nombre, matricula)
    estudiantes.append(estudiante)
    print(estudiantes)

def buscar():
    m = int(input('Ingrese matícula: '))
    for e in estudiantes:
        if e.matricula == m:
            print(e)
            break


        

        


def eliminar():
    pass