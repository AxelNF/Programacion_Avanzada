class estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula

    def __str__(self):
        return {f'Nombre: {self.nombre}\nMatrícula: {self.matricula}\n'}