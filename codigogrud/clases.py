class estudiante:
    def __init__(self, matricula, nombre, ap, am):
        self.matricula = matricula
        self.nombre = nombre
        self.ap = ap
        self.am = am

    def __str__(self):
        return f'{self.matricula:<10} {self.nombre:<15} {self.ap:<15} {self.am:<15}'