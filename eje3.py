def ingresar_vector(nombre, tamaño):
    vector = []
    print(f"Ingrese {tamaño} números enteros para el vector {nombre}:")
    for i in range(tamaño):
        num = int(input(f"{nombre}[{i}]: "))
        vector.append(num)
    return vector

def sumar_vector(vector):
    return sum(vector)

def sumar_vectores(vector_a, vector_b):
    if len(vector_a) == len(vector_b):
        return [vector_a[i] + vector_b[i] for i in range(len(vector_a))]
    else:
        return None  # No se puede sumar si los tamaños son diferentes

def mostrar_resultado(suma_a, suma_b, vector_resultante):
    print("Suma de los elementos del vector A:", suma_a)
    print("Suma de los elementos del vector B:", suma_b)
    if vector_resultante is not None:
        print("Vector resultante de la suma de A y B:", vector_resultante)
    else:
        print("No se puede sumar los vectores porque tienen tamaños diferentes.")

# Parte principal del ejercicio

N = int(input("Ingrese la cantidad de elementos del vector A: "))
M = int(input("Ingrese la cantidad de elementos del vector B: "))

vector_a = ingresar_vector("A", N)  # Carga del vector A
vector_b = ingresar_vector("B", M)  # Carga del vector B

suma_a = sumar_vector(vector_a)  # Suma de A
suma_b = sumar_vector(vector_b)  # Suma de B

vector_resultante = sumar_vectores(vector_a, vector_b)  # Intentar sumar los vectores

mostrar_resultado(suma_a, suma_b, vector_resultante)  # Mostrar los resultados
