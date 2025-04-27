import random

rodillos = [
    ['X', 'O', '7', 'X', 'O', '7', 'X', 'O', '7'],
    ['O', '7', 'X', 'O', '7', 'X', 'O', '7', 'X'],
    ['7', 'X', 'O', '7', 'X', 'O', '7', 'X', 'O']
]

def rotar_rodillo(rodillo, pasos):
    return rodillo[pasos:] + rodillo[:pasos]

def jugar_rodillos():
    rotaciones = [random.randint(0, 8) for _ in range(3)]
    
    rodillos_rotados = [rotar_rodillo(rodillos[i], rotaciones[i]) for i in range(3)]
    
    print(f"\nRod1: {rotaciones[0]}")
    print(f"Rod2: {rotaciones[1]}")
    print(f"Rod3: {rotaciones[2]}")
    print("\nResultado de los rodillos:")
    for i in range(9):
        print(f"{rodillos_rotados[0][i]} {rodillos_rotados[1][i]} {rodillos_rotados[2][i]}")
    
    if rodillos_rotados[0][0] == rodillos_rotados[1][0] == rodillos_rotados[2][0] == 'X':
        print("\nGanó 10 fichas!")
    elif rodillos_rotados[0][0] == rodillos_rotados[1][0] == rodillos_rotados[2][0] == 'O':
        print("\nGanó 100 fichas!")
    elif rodillos_rotados[0][0] == rodillos_rotados[1][0] == rodillos_rotados[2][0] == '7':
        print("\nGanó 1000 fichas!")
    else:
        print("\nNo ganó fichas.")

def continuar_juego():
    while True:
        jugar_rodillos()
        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if respuesta != 's':
            print("Gracias por jugar. ¡Hasta luego!")
            break

# Ejecutamos el juego
continuar_juego()