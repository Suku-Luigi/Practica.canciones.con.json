import funciones

print("Bienvenido al gestor de canciones.\n")

# Variable de control para el menú
opcion = ""

# Ciclo principal que se repite hasta que el usuario elija salir (opción 5)
while opcion != "5":
    print("\n--- MENÚ ---")
    print("1. Agregar canción")
    print("2. Ver canciones")
    print("3. Eliminar canción")
    print("4. Buscar canción")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1-5): ")
    
    if opcion == "1":
        nombre = input("Ingresa el nombre de la canción: ")
        artista = input("Ingresa el nombre del artista: ")
        # Se llama a la función del módulo importado
        funciones.agregar_cancion(nombre, artista)
        
    elif opcion == "2":
        # Se llama a la función para ver la lista
        funciones.ver_canciones()
        
    elif opcion == "3":
        funciones.ver_canciones()
        # Se pide el número de la canción y se le resta 1 para que coincida con el índice de la lista
        numero = int(input("Ingresa el número de la canción que deseas eliminar: "))
        funciones.eliminar_cancion(numero - 1)
        
    elif opcion == "4":
        nombre_buscar = input("Ingresa el nombre de la canción a buscar: ")
        # Se llama a la función de búsqueda
        funciones.buscar_cancion(nombre_buscar)
        
    elif opcion == "5":
        print("Saliendo del gestor de canciones...")
        
    else:
        print("Opción inválida. Por favor, elige una opción del menú.")

# Se llama a la función del módulo para guardar las canciones en el archivo json
funciones.guardar_canciones_json()

print("Gracias por usar el programa.")
