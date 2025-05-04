from datetime import *


class estudiante():
    def __init__(self, matricula, nombre, ap, am, fecha_nac):
        self.matricula = matricula
        self.nombre = nombre
        self.ap = ap
        self.am = am
        self.fecha_nac = fecha_nac

def get_date():
    while True:
        try:
            fecha = input('Ingrese fecha de nacimiento (dd/mm/aaaa):')
            fecha = datetime.strptime(fecha, '%d/%m/%Y')
            return fecha
        except ValueError:
            print('Ingrese la fecha en el formato correcto')

estudiantes = []