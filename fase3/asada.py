from datetime import *


class Estudiante():

    matricula = ''
    nombre = ''
    ap = ''
    am = ''
    fecha_nac = ''   


    def __init__(self, matricula, nombre, ap, am, fecha_nac):
        self.matricula = matricula
        self.nombre = nombre
        self.ap = ap
        self.am = am
        self.fecha_nac = fecha_nac
        pass

def f_nac():
    fecha_nac = input('Ingrese fecha de nacimiento (dd/mm/aaaa): ')
    fecha_nac = datetime.strftime('%d/%m/%Y')

f_nac()
