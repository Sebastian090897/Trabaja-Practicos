def ingresar_numeros():
    numeros = []
    for i in range(10):
        num = float(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)
    return numeros

def calcular_maximo(numeros):
    maximo = max(numeros)
    return maximo

def mostrar_resultado(maximo):
    print("El valor máximo es:", maximo)

# Parte principal del ejercicio

numeros = ingresar_numeros()  # Carga de los 10 números

maximo = calcular_maximo(numeros)  # Determinar el máximo

mostrar_resultado(maximo)  # Mostrar el valor máximo
