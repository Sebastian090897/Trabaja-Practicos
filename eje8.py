def cargar_matriz():
    electrodomesticos = []
    while True:
        nombre = input("Ingrese el nombre del electrodoméstico (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        
        proveedor = input("Ingrese el proveedor: ")
        
        while True:
            try:
                precio = float(input("Ingrese el precio del electrodoméstico: "))
                if precio < 0:
                    print("El precio debe ser un valor positivo. Intente nuevamente.")
                    continue
                break
            except ValueError:
                print("El precio debe ser un número. Intente nuevamente.")
        
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad en stock: "))
                if cantidad < 0:
                    print("La cantidad debe ser un número entero positivo. Intente nuevamente.")
                    continue
                break
            except ValueError:
                print("La cantidad debe ser un número entero. Intente nuevamente.")
        
        electrodomesticos.append([nombre, proveedor, str(precio), str(cantidad)])
    
    return electrodomesticos

def mostrar_por_proveedor(electrodomesticos, proveedor_buscado):
    encontrados = [e[0] for e in electrodomesticos if e[1].lower() == proveedor_buscado.lower()]
    
    if encontrados:
        print(f"Electrodomésticos del proveedor {proveedor_buscado}:")
        for item in encontrados:
            print(f"- {item}")
    else:
        print(f"No se encontraron electrodomésticos del proveedor {proveedor_buscado}.")

def electrodomestico_menor_precio(electrodomesticos):
    menor_precio = float('inf')
    electrodomestico = None
    for e in electrodomesticos:
        precio = float(e[2])
        if precio < menor_precio:
            menor_precio = precio
            electrodomestico = e
    if electrodomestico:
        print(f"El electrodoméstico con el menor precio es {electrodomestico[0]} de {electrodomestico[1]} con un precio de {electrodomestico[2]}.")
    else:
        print("No se encontraron electrodomésticos para determinar el menor precio.")

def mostrar_stock_positivo(electrodomesticos):
    stock_positivo = [e[0] for e in electrodomesticos if int(e[3]) > 0]
    
    if stock_positivo:
        print("Electrodomésticos con stock positivo:")
        for item in stock_positivo:
            print(f"- {item}")
    else:
        print("No hay electrodomésticos con stock positivo.")

def menu():
    electrodomesticos = cargar_matriz()
    
    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar electrodomésticos de un proveedor")
        print("2. Mostrar el electrodoméstico con el menor precio")
        print("3. Mostrar electrodomésticos con stock positivo")
        print("4. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == '1':
            proveedor_buscado = input("Ingrese el nombre del proveedor: ")
            mostrar_por_proveedor(electrodomesticos, proveedor_buscado)
        
        elif opcion == '2':
            electrodomestico_menor_precio(electrodomesticos)
        
        elif opcion == '3':
            mostrar_stock_positivo(electrodomesticos)
        
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu()
