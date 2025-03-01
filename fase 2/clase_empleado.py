from re import *

class empleado():
    nombre = ''
    apellido = ''
    RFC = ''
    salario = ''

    def __init__(self, nombre, apellido, RFC, salario):
        self.nombre = ''
        self.apellido = ''
        self.RFC = ''
        self.salario = ''

def get_RFC():
    while True:
        rfc = input('Ingrese RFC: ')
        if search(r'^[A-Za-z]{3,4}[0-9]{6}[A-Za-z0-9]{3}$', rfc):
            break
        else:
            print('El RFC no es válido')

def get_salario():
    while True:
        salario = input('Ingrese salario (en formato 0.00): ')
        if search(r'^[0-9]+.[0-9]{2}$', salario):
            break
        else:
            print('El formato no es correcto')


empleado = list()

get_salario()