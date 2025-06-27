class DatosEstudiante:
    def __init__(self, cif, nombres, apellidos, carrera):
        self.cif = cif
        self.nombres = nombres
        self.apellidos = apellidos
        self.carrera = carrera
        self.notas: list[float]

    def calcular_promedio(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return 0


    def __str__(self):
        return f"CIF: {self.cif}\n Nombres: {self.nombres}\n Apellidos: {self.apellidos}\n Carrera: {self.carrera}\n Promedio: {self.calcular_promedio:.2f}"