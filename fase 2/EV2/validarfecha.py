from datetime import *


class estudiante():
    def __init__(self, matricula, nombre, ap, am, fecha_nac):
        self.matricula = matricula
        self.nombre = nombre
        self.ap = ap
        self.am = am
        self.fecha_nac = fecha_nac

    def __str__(self):
        return f'''
Estudiante:
Matricula: {self.matricula}
Nombre: {self.nombre}
Apellido Paterno: {self.ap}
Apellido Materno: {self.am}
Fecha de Nacimiento: {self.fecha_nac}'''

def get_date():
    while True:
        try:
            fecha = input('Ingrese fecha de nacimiento (dd/mm/aaaa): ')
            fecha = datetime.strptime(fecha, '%d/%m/%Y')
            return date.strftime(fecha, '%d/%m/%Y')
        except ValueError:
            print('Ingrese la fecha en el formato correcto')

estudiantes = []

while True:
    matricula = input('Ingrese matricula: ')
    nombre = input('Ingrese nombre: ')
    ap = input('Ingrese apellido paterno: ')
    am = input('Ingrese apellido materno: ')
    fecha_nac = get_date()
    estudiantes.append(estudiante(matricula, nombre, ap, am, fecha_nac))
    
    while True:
        opc = input('¿Desea agregar otro estudiante? (s/n): ')
        if opc.lower() not in ['s', 'n']:
            print('Opción no válida')
        else:
            break
    
    if opc.lower() == 'n':
        break

for e in estudiantes:
    print(e)