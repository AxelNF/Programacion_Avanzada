from clase import *
from main import estudiantes

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
        opc = input('Ingrese opción')
        
        if opc not in ['1','2','3','X','x']:
            print('Ingrese una opción válida')
        else:
            if opc == '1':
                crear()
            elif opc == '2':
                buscar()
            elif opc == '3':
                eliminar()
            else:
                print('Gracias...')
                break

def crear():
    matricula = get_int('Ingrese matrícula')
    nombre = input('Ingrese nombre: ')

    estudiante(nombre, matricula)
    estudiantes.append(estudiante)
    print('Estudiante creado')

def buscar():
    pass

def eliminar():
    pass

