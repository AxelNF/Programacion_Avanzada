from datetime import *
import json


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

estudiantes.append(estudiante('1', 'Luis', 'Martinez', 'Montemayor', '10/10/2010'))
estudiantes.append(estudiante('2', 'Julieta', 'Gonzalez', 'Sanchez', '15/07/2008'))
estudiantes.append(estudiante('3', 'Martin', 'Gutierrez', 'Chapa', '23/12/2011'))
estudiantes.append(estudiante('4', 'Ana', 'Gonzalez', 'Martinez', '01/01/2000'))
estudiantes.append(estudiante('5', 'Pedro', 'Jimenez', 'Lopez', '05/05/2005'))
estudiantes.append(estudiante('6', 'Maria', 'Hernandez', 'Garcia', '20/02/2002'))
estudiantes.append(estudiante('7', 'Jose', 'Ramirez', 'Torres', '30/03/2003'))
estudiantes.append(estudiante('8', 'Laura', 'Vasquez', 'Reyes', '25/12/2004'))
estudiantes.append(estudiante('9', 'Carlos', 'Morales', 'Cruz', '15/08/2006'))
estudiantes.append(estudiante('10', 'Sofia', 'Reyes', 'Gonzalez', '18/11/2007'))

'''
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
'''

json_data = json.dumps(estudiantes, default=lambda o: o.__dict__, indent=4)
print(json_data)