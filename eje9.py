pacientes = []

def cargar_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    apellido = input("Ingrese el apellido del paciente: ")
    paciente = f"{nombre} {apellido}"
    pacientes.insert(0, paciente)
    print(f"Paciente {paciente} ingresado correctamente.")

def atender_paciente():
    if pacientes:
        atendido = pacientes.pop()
        print(f"Se atendió al paciente: {atendido}")
    else:
        print("No hay pacientes en la lista.")

def urgencia():
    nombre = input("Ingrese el nombre del paciente con urgencia: ")
    apellido = input("Ingrese el apellido del paciente con urgencia: ")
    paciente = f"{nombre} {apellido}"
    if paciente in pacientes:
        pacientes.remove(paciente)
        pacientes.insert(0, paciente)
        print(f"Paciente {paciente} fue movido al inicio de la lista por urgencia.")
    else:
        print("El paciente no está en la lista.")

def pacientes_antes():
    nombre = input("Ingrese el nombre del paciente a consultar: ")
    apellido = input("Ingrese el apellido: ")
    paciente = f"{nombre} {apellido}"
    if paciente in pacientes:
        posicion = pacientes.index(paciente)
        pacientes_delante = len(pacientes) - posicion - 1
        print(f"Faltan {pacientes_delante} paciente(s) antes que {paciente}.")
    else:
        print("El paciente no está en la lista.")

def mostrar_lista():
    if pacientes:
        print("\nLista de pacientes en espera:")
        for i, p in enumerate(reversed(pacientes), start=1):
            print(f"{i}. {p}")
    else:
        print("\nNo hay pacientes en espera.")

def menu():
    while True:
        print("\n--- MENÚ DE PACIENTES ---")
        print("1. Ingresar paciente")
        print("2. Atender paciente")
        print("3. Atender paciente con urgencia")
        print("4. Consultar cuántos pacientes faltan antes de uno")
        print("5. Mostrar lista de espera")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            cargar_paciente()
        elif opcion == '2':
            atender_paciente()
        elif opcion == '3':
            urgencia()
        elif opcion == '4':
            pacientes_antes()
        elif opcion == '5':
            mostrar_lista()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente nuevamente.")

# Ejecutar programa
menu()
