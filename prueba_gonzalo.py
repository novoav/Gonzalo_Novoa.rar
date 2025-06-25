
   usuarios = {}


def mostrar_menu():
    print("\nMENÚ DE OPCIONES:")
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")


def tiene_numero(texto):
    for caracter in texto:
        if caracter.isdigit():
            return True
    return False


def tiene_letra(texto):
    for caracter in texto:
        if caracter.isalpha():
            return True
    return False


def validar_contraseña(contra):
    if len(contra) < 8:
        return False
    if " " in contra:
        return False
    if not tiene_numero(contra):
        return False
    if not tiene_letra(contra):
        return False
    return True


def ingresar_usuario():
    nombre = input("Ingrese nombre de usuario: ")
    if nombre in usuarios:
        print("Usuario ya existe.Intente otro.")
        return

    sexo = input("Ingrese sexo (F o M): ")
    if sexo != "F" and sexo != "M":
        print("Debe ingresar F o M solamente.Intente de nuevo.")
        return

    contra = input("Ingrese contraseña: ")
    if not validar_contraseña(contra):
        print("Contraseña no válida.")
        return

    usuarios[nombre] = {"sexo": sexo, "contraseña": contra}
    print("Usuario ingresado con exito.")


def buscar_usuario():
    nombre = input("Ingrese nombre de usuario a buscar: ")
    if nombre in usuarios:
        print("Sexo:", usuarios[nombre]["sexo"])
        print("Contraseña:", usuarios[nombre]["contraseña"])
    else:
        print("El usuario no se encuentra.")


def eliminar_usuario():
    nombre = input("Ingrese nombre de usuario a eliminar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado con exito!")
    else:
        print("No se pudo eliminar usuario!")


opcion = ""
while opcion != "4":
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        ingresar_usuario()
    elif opcion == "2":
        buscar_usuario()
    elif opcion == "3":
        eliminar_usuario()
    elif opcion == "4":
        print("Programa terminado...")
    else:
        print("!Debe ingresar una opcion válida!.")
