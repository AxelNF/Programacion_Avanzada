class participante:
    def __init__(self, correo, nombre, nacimiento, momento=''):
        self.correo = correo
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.momento = momento

    def __str__(self):
        return f'''
Correo: {self.correo}
Nombre: {self.nombre}
Fecha de nacimiento: {self.nacimiento}
Momento de registro: {self.momento}
'''