def calcular_potencia(x, k):
    return x ** k

def contar_digitos(x):
    return len(str(abs(x)))

def es_capicua(x):
    return str(x) == str(x)[::-1]

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Calcular la potencia K de un número X")
    print("2. Obtener la cantidad de dígitos de un número X")
    print("3. Determinar si un número es capicúa")
    print("4. Salir")

# Parte principal del programa

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        x = int(input("Ingrese el número X: "))
        k = int(input("Ingrese el exponente K: "))
        print(f"{x} elevado a la {k} es {calcular_potencia(x, k)}")
    
    elif opcion == "2":
        x = int(input("Ingrese el número X: "))
        print(f"El número {x} tiene {contar_digitos(x)} dígitos.")
    
    elif opcion == "3":
        x = int(input("Ingrese el número X: "))
        if es_capicua(x):
            print(f"El número {x} es capicúa.")
        else:
            print(f"El número {x} no es capicúa.")
    
    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
