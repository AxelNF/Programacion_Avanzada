class estudiante:
    def __init__(self, matricula, nombre):
        self.matricula = matricula
        self.nombre = nombre

    def __str__(self):
        return f'{self.matricula:<10} {self.nombre:<10}'