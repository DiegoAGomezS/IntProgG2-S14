from models.classes import DatosEstudiante

class TramiteBeca:
    def __init__(self, average):
        self.average = average
    
    def calcular_promedio(self):
        if not self.average:
            return 0.0
        return sum(self.average)/len(self.average)
    
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