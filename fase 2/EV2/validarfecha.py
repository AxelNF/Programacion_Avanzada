from datetime import *
import os


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
estudiantes.append(estudiante('3', 'Martín', 'Gutierrez', 'Chapa', '23/12/2011'))


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


ruta = os.path.abspath(os.getcwd())
archivo_trabajo=ruta+"\\estudiantes.csv"
archivo_respaldo=ruta+"\\contactos.bak"

if os.path.exists(archivo_trabajo):
    if os.path.exists(archivo_respaldo):
        os.remove(archivo_respaldo)

        os.rename(archivo_trabajo,archivo_respaldo)

f = open(archivo_trabajo,"w+")
f.write("Matricula|Nombre|APP|APM|Fecha de nacimiento\n")

for e in estudiantes:
    f.write(f'{e.matricula}|{e.nombre}|{e.ap}|{e.am}|{e.fecha_nac}\n')

f.close()

#for e in estudiantes:
#    print(e)