def cargar_matriz(nombre, filas, columnas):
    matriz = []
    print(f"\nIngrese los valores para la matriz {nombre}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"{nombre}[{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_matrices(matriz_a, matriz_b):
    filas = len(matriz_a)
    columnas = len(matriz_a[0])
    matriz_c = [[matriz_a[i][j] + matriz_b[i][j] for j in range(columnas)] for i in range(filas)]
    return matriz_c

def multiplicar_matrices(matriz_a, matriz_b):
    filas_a, columnas_a = len(matriz_a), len(matriz_a[0])
    filas_b, columnas_b = len(matriz_b), len(matriz_b[0])

    if columnas_a != filas_b:
        print("No se puede multiplicar: las columnas de A deben ser iguales a las filas de B.")
        return None

    matriz_c = [[sum(matriz_a[i][k] * matriz_b[k][j] for k in range(columnas_a)) for j in range(columnas_b)] for i in range(filas_a)]
    return matriz_c

def mostrar_matriz(nombre, matriz):
    print(f"\nMatriz {nombre}:")
    for fila in matriz:
        print(" ".join(map(str, fila)))

# Parte principal del programa

M = int(input("Ingrese la cantidad de filas de las matrices: "))
N = int(input("Ingrese la cantidad de columnas de las matrices: "))

matriz_a = cargar_matriz("A", M, N)
matriz_b = cargar_matriz("B", M, N)

print("\nElija una operación:")
print("1. Sumar las matrices")
print("2. Multiplicar las matrices")
opcion = input("Seleccione una opción (1-2): ")

if opcion == "1":
    matriz_c = sumar_matrices(matriz_a, matriz_b)
    mostrar_matriz("C (Suma)", matriz_c)

elif opcion == "2":
    matriz_c = multiplicar_matrices(matriz_a, matriz_b)
    if matriz_c:
        mostrar_matriz("C (Producto)", matriz_c)

else:
    print("Opción inválida.")
