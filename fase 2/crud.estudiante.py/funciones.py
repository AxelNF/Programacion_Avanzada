def get_int(s):
    num = input(f'{s}: ')
    try:
        return int(num)
    except ValueError:
        print('Ingresa un número válido')

def menu():
    while True:
        print('[1] Crear estudiante')
        print('[2] Buscar estudiante')
        print('[3] Eliminar estudiante')
        print('[X] Salir')
        opc = get_int('Ingrese opción: ')
        if opc is not [1,2,3,'X']:
            print('Ingrese una opción válida')

def crear():
    pass

def buscar():
    pass

def eliminar():
    pass

