from models.classes import DatosEstudiante
from dao.estudiante_dao import EstudianteDAO

# Lista para almacenar estudiantes registrados en memoria
estudiantes = []

def registrar_estudiante():
    cif = input("Ingrese el CIF del estudiante: ")
    nombres = input("Ingrese los nombres: ")
    apellidos = input("Ingrese los apellidos: ")
    carrera = input("Ingrese la carrera: ")
    estudiante = DatosEstudiante(cif, nombres, apellidos, carrera)
    estudiantes.append(estudiante)
    print("✅ Estudiante registrado exitosamente.\n")

def agregar_notas():
    cif = input("Ingrese el CIF del estudiante: ")
    estudiante = buscar_estudiante(cif)
    if estudiante:
        try:
            cantidad = int(input("¿Cuántas notas desea ingresar?: "))
            for i in range(cantidad):
                nota = float(input(f"Ingrese la nota {i+1}: "))
                estudiante.notas.append(nota)
            print("✅ Notas agregadas correctamente.\n")
        except ValueError:
            print("❌ Error: ingrese valores numéricos válidos.\n")
    else:
        print("❌ Estudiante no encontrado.\n")

def consultar_promedio():
    cif = input("Ingrese el CIF del estudiante: ")
    estudiante = buscar_estudiante(cif)
    if estudiante:
        print(f"📊 Promedio: {estudiante.calcular_promedio():.2f}\n")
    else:
        print("❌ Estudiante no encontrado.\n")

def consultar_beca():
    cif = input("Ingrese el CIF del estudiante: ")
    estudiante = buscar_estudiante(cif)
    if estudiante:
        dao = EstudianteDAO(estudiante)
        print(f"🎓 Beca asignada: {dao.calcular_beca()}\n")
    else:
        print("❌ Estudiante no encontrado.\n")

def generar_correo():
    cif = input("Ingrese el CIF del estudiante: ")
    estudiante = buscar_estudiante(cif)
    if estudiante:
        dao = EstudianteDAO(estudiante)
        print(f"📧 Correo institucional: {dao.generar_correo()}\n")
    else:
        print("❌ Estudiante no encontrado.\n")

def guardar_estudiante_txt():
    cif = input("Ingrese el CIF del estudiante: ")
    estudiante = buscar_estudiante(cif)
    if estudiante:
        dao = EstudianteDAO(estudiante)
        dao.guardar_informacion("registro_estudiantes.txt")
        print("📝 Información guardada en archivo.\n")
    else:
        print("❌ Estudiante no encontrado.\n")

def buscar_estudiante(cif):
    for estudiante in estudiantes:
        if estudiante.cif == cif:
            return estudiante
    return None

def menu():
    while True:
        print("=== Menú Principal ===")
        print("1. Registrar estudiante")
        print("2. Agregar notas a estudiante")
        print("3. Consultar promedio")
        print("4. Consultar beca")
        print("5. Generar correo institucional")
        print("6. Guardar información en archivo")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            agregar_notas()
        elif opcion == "3":
            consultar_promedio()
        elif opcion == "4":
            consultar_beca()
        elif opcion == "5":
            generar_correo()
        elif opcion == "6":
            guardar_estudiante_txt()
        elif opcion == "7":
            print("👋 Gracias por utilizar el sistema.")
            break
        else:
            print("❌ Opción inválida, intente de nuevo.\n")

if __name__ == "__main__":
    menu()