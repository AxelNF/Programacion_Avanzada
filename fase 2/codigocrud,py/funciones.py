from clases import *

def menu(lista):
    while True:
        print('[1] Crear estudiante')
        print('[2] Buscar estudiante')
        print('[3] Eliminar estudiante')
        print('[4] Mostrar todos los estudiantes')
        print('[X] Salir')
        
        opc = input('Seleccione opción: ')
        if opc not in ['1','2','3', '4', 'X','x']:
            print('Seleccione una opción válida.')
        elif opc == '1':
            crear(lista)
        elif opc == '2':
            mostrar(lista)
        elif opc == '3':
            eliminar(lista)
        elif opc == '4':
            if not lista:
                print('No hay estudiantes registrados')
            else:
                print(f'{"MATRICULA":<10} {"NOMBRE":<10}')
                for e in lista:
                    print(e)
        else:
            print('Saliendo...')
            break

def crear(lista):
    matricula = get_int('Ingrese matrícula: ')
    nombre = input('Ingrese nombre: ')
    lista.append(estudiante(matricula, nombre))
    print('Estudiante creado')

def buscar(lista):
    if not lista:
        print('No hay estudiantes registrados')
        return
    matricula = get_int('Ingrese matrícula del estudiante: ')
    for e in lista:
        if e.matricula == matricula:
            return e
    print('No se encontró el estudiante con esa matrícula')
    return

def eliminar(lista):
    estudiante = buscar(lista)
    if estudiante:
        lista.remove(estudiante)
        print('Estudiante eliminado')

def mostrar(lista):    
    estudiante = buscar(lista)
    if estudiante:
        print(f'{"MATRICULA":<10} {"NOMBRE":<10}')
        print(estudiante)
     
def get_int(s):
    while True:
        try:
            return int(input(s))
        except ValueError:
            print('Ingrese un número entero')