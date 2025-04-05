estudiantes = []

from clase import *

def get_int(s):
    while True:
        num = input(f'{s}: ')
        try:
            return int(num)
        except ValueError:
            print('Ingrese un número válido')
        

def menu():
    while True:
        print('[1] Crear estudiante')
        print('[2] Buscar estudiante')
        print('[3] Eliminar estudiante')
        print('[X] Salir')
        opc = get_int('Ingrese opción')
        
        if opc not in [1,2,3,'X']:
            print('Ingrese una opción válida')
        else:
            if opc == 1:
                crear()
            elif opc == 2:
                buscar()
            elif opc == 3:
                eliminar()
            else:
                print('Gracias...')
                break

def crear():
    nombre = input('Ingrese nombre: ')
    matricula = get_int('Ingrese matrícula')

    estudiante() = {'nombre': nombre, 'matricula': matricula}
    estudiantes.append(estudiante)

def buscar():
    pass

def eliminar():
    pass

