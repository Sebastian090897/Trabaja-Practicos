import math

def ingresar_matriz(m):
    matriz = []
    for i in range(m):
        fila = []
        for j in range(m):
            num = int(input(f"Ingrese el elemento en la posición ({i + 1}, {j + 1}): "))
            fila.append(num)
        matriz.append(fila)
    return matriz

def suma_diagonal_principal(matriz, m):
    suma = 0
    for i in range(m):
        suma += matriz[i][i]
    return suma

def factorial(num):
    return math.factorial(num)

def elementos_vector(matriz, m, suma_diagonal):
    vector = []
    for i in range(m):
        for j in range(m):
            num = matriz[i][j]
            if factorial(num) >= suma_diagonal:
                vector.append(num)
    return vector

def eliminar_repetidos(vector):
    return list(set(vector))

def ordenar_vector(vector):
    return sorted(vector)

def mostrar_resultado(vector):
    print("Vector ordenado sin elementos repetidos:", vector)

# Parte principal del ejercicio

m = int(input("Ingrese el tamaño de la matriz cuadrada (M x M): "))  # Ingresamos el tamaño de la matriz

matriz = ingresar_matriz(m)  # Ingresamos la matriz de tamaño M x M

suma_diagonal = suma_diagonal_principal(matriz, m)  # Calculamos la suma de la diagonal principal
print(f"Suma diagonal principal = {suma_diagonal}")

vector = elementos_vector(matriz, m, suma_diagonal)  # Obtenemos el vector con números cuyo factorial sea >= suma diagonal
print(f"Vector = {vector}")

vector_sin_repetidos = eliminar_repetidos(vector)  # Eliminamos los repetidos del vector
vector_ordenado = ordenar_vector(vector_sin_repetidos)  # Ordenamos el vector de menor a mayor

mostrar_resultado(vector_ordenado)  # Mostramos el resultado final
