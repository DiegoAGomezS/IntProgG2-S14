from models.classes import DatosEstudiante  # Importación de la clase

class EstudianteDAO:
    def __init__(self, estudiante: DatosEstudiante):
        self.estudiante = estudiante

    def calcular_beca(self):
        promedio = self.estudiante.calcular_promedio()
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

    def generar_correo(self):
        iniciales_apellidos = self.estudiante.apellidos.replace(" ", "").lower()[:3]
        iniciales_nombres = self.estudiante.nombres.replace(" ", "").lower()[:2]
        return f"{iniciales_apellidos}_{iniciales_nombres}@uamv.edu.ni"

    def guardar_informacion(self, nombre_archivo):
        with open(nombre_archivo, "a") as archivo:
            promedio = self.estudiante.calcular_promedio()
            correo = self.generar_correo()
            archivo.write(f"CIF: {self.estudiante.cif}\n")
            archivo.write(f"Nombre: {self.estudiante.nombres} {self.estudiante.apellidos}\n")
            archivo.write(f"Carrera: {self.estudiante.carrera}\n")
            archivo.write(f"Notas: {self.estudiante.notas}\n")
            archivo.write(f"Promedio: {promedio:.2f}\n")
            archivo.write(f"Correo: {correo}\n")
            archivo.write(f"Beca: {self.calcular_beca()}\n")
            archivo.write("--------------------------------------------------\n")