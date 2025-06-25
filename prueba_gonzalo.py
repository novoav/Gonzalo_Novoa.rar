usuarios = {}


def mostrar_menu():
    print("\nMENU PRINCIPAL:")
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")


def ingresar_usuario():
    print("\nIngrese nombre de  usuario")
    nombre = input("Nombre de usuario: ")

    if nombre in usuarios:
        print("Usuario ya existe. Intente otro.")
        return

    sexo = input("Sexo (F/M): ").upper()
    while sexo not in ['F', 'M']:
        print("Solo se permite F o M solamente")
        sexo = input("Sexo (F/M): ").upper()

    while True:
        contraseña = input("Contraseña: ")
        if len(contraseña) < 8:
            print("Mínimo 8 caracteres")
        elif ' ' in contraseña:
            print("No puede tener espacios")
        elif not any(caracter() for
                     (caracter) in contraseña):
            print("Debe tener al menos un número")
        elif not any(caracter() for (caracter) in contraseña):
            print("Contraseña no valida. Intente otra.")
        else:
            break

    usuarios[nombre] = {'sexo': sexo, 'contraseña': contraseña}
    print("¡Usuario ingresado con exito!")


def buscar_usuario():
    print("\nBuscar usuario")
    nombre = input("Nombre a buscar: ")

    if nombre in usuarios:
        print(f"Sexo: {usuarios[nombre]['sexo']}")
        print(f"Contraseña: {usuarios[nombre]['contraseña']}")
    else:
        print("El usuario no se encuentra")


def eliminar_usuario():
    print("\nEliminar usuario")
    nombre = input("Nombre a eliminar: ")

    if nombre in usuarios:
        del usuarios[nombre]
        print("¡Usuario eliminado con exito!")
    else:
        print("No se encontró el usuario")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        ingresar_usuario()
    elif opcion == "2":
        buscar_usuario()
    elif opcion == "3":
        eliminar_usuario()
    elif opcion == "4":
        print("¡Programa terminado!")
        break
    else:
        print("Debe ingresar una opcion valida!.")
