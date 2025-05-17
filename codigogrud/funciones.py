from clases import *
from time import sleep
from operator import attrgetter
encabezado = f'{"MATRICULA":<10} {"NOMBRE":<15} {"AP PATERNO":<15} {"AP MATERNO":<15}'

def menu(lista):
    while True:
        sleep(1)
        print('\n')
        print('MENU')
        print('====================')
        print('[1] Crear estudiante')
        print('[2] Buscar estudiante')
        print('[3] Eliminar estudiante')
        print('[4] Mostrar todos los estudiantes')
        print('[5] Modificar estudiante')
        print('[X] Salir')
        
        opc = input('Seleccione opción: ')
        if opc not in ['1','2','3', '4', '5', 'X','x']:
            print('Seleccione una opción válida.')
        elif opc == '1':
            crear(lista)
        elif opc == '2':
            mostrar(lista)
        elif opc == '3':
            eliminar(lista)
        elif opc == '4':
            mostrar_todos(lista)
        elif opc == '5':
            modificar(lista)
        else:
            print('Saliendo...')
            break

def crear(lista):
    matricula = get_matricula(lista)
    #matricula = get_int('Ingrese matrícula: ')
    #if repetido(lista, matricula):
    #    return
    nombre = input('Ingrese nombre: ')
    ap = input('Ingrese apellido paterno: ')
    am = input('Ingrese apellido materno: ')
    lista.append(estudiante(matricula, nombre, ap, am))
    ordenar(lista)
    print('Estudiante creado')

def buscar(lista):
    if lista_vacia(lista):
        return
    matricula = get_int('Ingrese matrícula del estudiante: ')
    for e in lista:
        if e.matricula == matricula:
            return e
    print('Matricula no existente')
    return

def eliminar(lista):
    if lista_vacia(lista):
        return
    estudiante = buscar(lista)
    if estudiante:
        lista.remove(estudiante)
        print('Estudiante eliminado')
        return

def mostrar(lista):    
    estudiante = buscar(lista)
    if estudiante:
        print(encabezado)
        print(estudiante)
        sleep(1)

def mostrar_todos(lista):
    if lista_vacia(lista):
        return
    print(encabezado)
    for e in lista:
        print(e)
    sleep(1)

def modificar(lista):
    estudiante = buscar(lista)
    if estudiante:
        nombre = input('Ingrese nombre: ')
        ap = input('Ingrese apellido paterno: ')
        am = input('Ingrese apellido materno: ')
        estudiante.nombre = nombre
        estudiante.ap = ap
        estudiante.am = am
        print('Estudiante modificado')

'''
def repetido(lista, matricula):
    for e in lista:
        if e.matricula == matricula:
            print('La matrícula ya existe')
            return True

Usar esta funcion en caso de pedir la entrada de una matrícula al crear estudiante
'''

def lista_vacia(lista):
    if not lista:
        print('No hay estudiantes registrados')
        return True
    
def ordenar(lista):
    lista.sort(key=attrgetter('matricula'))

def get_matricula(lista):
    if lista:
        return lista[-1].matricula + 1
    return 1
                
def get_int(s):
    while True:
        try:
            return int(input(s))
        except ValueError:
            print('Ingrese un número entero')