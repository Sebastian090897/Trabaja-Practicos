def ingresar_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    return num1, num2, num3

def calcular_maximo(num1, num2, num3):
    maximo = max(num1, num2, num3)
    return maximo

def mostrar_resultado(maximo):
    print("El valor máximo es:", maximo)

# Parte principal del ejercicio

num1, num2, num3 = ingresar_numeros()  # Carga de los números

maximo = calcular_maximo(num1, num2, num3)  # Determinar el máximo

mostrar_resultado(maximo)  # Mostrar el valor máximo
