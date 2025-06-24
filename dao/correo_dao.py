from models.classes import DatosEstudiante

class CorreoEstudiante:
    def __init__(self, name, surname):
        iniciales_surname = surname.replace(" ", "").lower()[:3]
        iniciales_name = name.replace(" ", "").lower()[:2]
        
        return f"{iniciales_surname}_{iniciales_name}@uamv.edu.ni"