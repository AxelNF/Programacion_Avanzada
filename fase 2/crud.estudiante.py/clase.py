class estudiante:
    
    nombre = ''
    matricula = 0

    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
    
    def __str__(self):
        return f'Estudiante: {self.nombre}, Matrícula: {self.matricula}'