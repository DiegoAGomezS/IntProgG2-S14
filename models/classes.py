class DatosEstudiante:
    def __init__(self, cif, nombres, apellidos, carrera):
        self.cif = cif
        self.nombres = nombres
        self.apellidos = apellidos
        self.carrera = carrera
        self.notas: list[float]

    def calcular_promedio(self):
        if not self.notas:
            return 0.0
        return sum(self.notas)/len(self.notas)
    
    def calcular_beca(self):
        promedio = self.calcular_promedio
        if 85 < promedio <= 90:
            return 'Beca del 25%'
        elif 90 < promedio <= 95:
            return 'Beca del 50%'
        elif 95 < promedio <= 98:
            return 'Beca del 75%'
        elif 98 < promedio:
            return 'Beca del 100%'
        else:
            return 'Lo siento, no tiene permitido tramitar beca'

    def generar_correro(self):
        iniciales_apellidos = self.apellidos.replace(" ", "").lower()[:3]
        iniciales_nombres = self.nombres.replace(" ", "").lower()[:2]
        
        return f"{iniciales_apellidos}_{iniciales_nombres}@uamv.edu.ni"

    def __str__(self):
        return f"CIF: {self.cif}\n Nombres: {self.nombres}\n Apellidos: {self.apellidos}\n Carrera: {self.carrera}\n Promedio: {self.calcular_promedio:.2f}"