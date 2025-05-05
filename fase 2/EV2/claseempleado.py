from re import *

class empleado():

    def __init__(self, nombre, ap, am, rfc, salario):
        self.nombre = nombre
        self.ap = ap
        self.am = am
        self.rfc = rfc
        self.salario = salario

    def __str__(self):
        return f'''Nombre: {self.nombre}
Apellido Paterno: {self.ap}
Apellido Materno: {self.am}
RFC: {self.rfc}
Salario: ${self.salario}
'''

def get_rfc():
    while True:
        rfc = input('Ingrese RFC: ')
        if search(r'^[A-Za-z]{3,4}[0-9]{6}[A-Za-z0-9]{3}$', rfc):
            return rfc.upper()
        else:
            print('El RFC no es válido')

def get_salario():
    while True:
        salario = input('Ingrese salario (en formato 0.00): ')
        if search(r'^[0-9]+.[0-9]{2}$', salario):
            return salario
        else:
            print('El formato no es correcto')

empleados = []

while True:
    nombre = input('Ingrese nombre: ')
    ap = input('Ingrese apellido paterno: ')
    am = input('Ingrese apellido materno: ')
    rfc = get_rfc()
    salario = get_salario()
    empleados.append(empleado(nombre, ap, am, rfc, salario))

    while True:
        opc = input('¿Desea agregar otro empleado? (s/n): ')
        if opc.lower() not in ['s', 'n']:
            print('Opción no válida')
        else:
            break
    
    if opc.lower() == 'n':
        break
    

print('Empleados registrados:\n')
for emp in empleados:
    print(emp)