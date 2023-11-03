import json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Diccionario para almacenar usuarios y contraseñas
usuarios = {}

# Función para registrar un usuario
def registrar_usuario():
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    usuarios[nombre_usuario] = contrasena
    print("Usuario registrado exitosamente.")

# Función para mostrar la información de usuarios
def mostrar_informacion():
    print("Lista de usuarios registrados:")
    for usuario, contrasena in usuarios.items():
        print(f"Usuario: {usuario}, Contraseña: {contrasena}")

# Función para realizar el inicio de sesión
def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena:
        print("Inicio de sesión exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

# Función para guardar la información en un archivo local
def guardar_en_archivo():
    with open("usuarios.txt", "w") as archivo:
        json.dump(usuarios, archivo)
    print("Información guardada en archivo local (usuarios.txt).")

# Función para cargar la información desde un archivo local
def cargar_desde_archivo():
    try:
        with open("usuarios.txt", "r") as archivo:
            usuarios.clear()  # Limpiamos el diccionario antes de cargar
            usuarios.update(json.load(archivo))
        print("Información cargada desde archivo local (usuarios.txt).")
    except FileNotFoundError:
        print("El archivo no existe. No se pudo cargar la información.")

# Main
if __name__ == "__main__":
    cargar_desde_archivo()

    while True:
        print("\nOpciones:")
        print("1. Registrar usuario")
        print("2. Mostrar información de usuarios")
        print("3. Iniciar sesión")
        print("4. Guardar información en archivo")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1/2/3/4/5): ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_informacion()
        elif opcion == "3":
            iniciar_sesion()
        elif opcion == "4":
            guardar_en_archivo()
        elif opcion == "5":
            guardar_en_archivo()
            break
        else:
            print("Opción no válida. Intente de nuevo.")

