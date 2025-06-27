import pwinput
import os
from main.menu import menu as m

ARCHIVO = "usuarios.txt"
CLAVE = "Admin123"

def inicio1():
    print(" INICIO DE SESIÓN ")
    intento = input("Ingresa la contraseña: ")
    if intento == CLAVE:
        print("Acceso permitído\n")
        return True
    else:
        print("Contraseña incorrecta. Acceso Denegado\n")
        return False

def inicio2():
    print(" INICIO DE SESIÓN ")
    #intento = input("Ingresa la contraseña: ")
    intento = pwinput.pwinput("Ingresa la contraseña: ", "°")
    if intento == CLAVE:
        print("Acceso permitído\n")
        return True
    else:
        print("Contraseña incorrecta. Acceso Denegado\n")
        return False

def agregar_usuarios(usuario, clave):
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario},{clave}\n")

def cargar_usuarios():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                usuario, clave = linea.strip().split(",")
                usuarios[usuario] = clave
            return usuarios

agregar_usuarios("admin", "Admin123")

def inicio3():
    print(" INICIO DE SESIÓN ")
    usuarios = cargar_usuarios()
    usuario = input("Usuario: ")
    clave_ingresada = pwinput.pwinput(prompt ='Contraseña: ', mask = '°')
    if usuario in usuarios and usuarios[usuario] == clave_ingresada:
        print("Acceso permitido")
        return True
    else:
        print("Contraseña incorrecta... Acceso denegado")
        return False

if inicio3():
    m()