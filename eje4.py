def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in palabra if letra in vocales)

def contar_consonantes(palabra):
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for letra in palabra if letra in consonantes)

# Parte principal del ejercicio

texto = input("Ingrese una o más oraciones: ")

palabras = texto.split() # Dividir el texto en palabras


total_vocales = sum(contar_vocales(palabra) for palabra in palabras)

total_consonantes = sum(contar_consonantes(palabra) for palabra in palabras)

print("Cantidad total de vocales:", total_vocales)

print("Cantidad total de consonantes:", total_consonantes)
