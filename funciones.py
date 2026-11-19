import json

# Lista global que almacenará los diccionarios de las canciones, iniciada con 3 canciones fijas
lista_canciones = [{"nombre": "Go to sleep", "artista": "G5"}, {"nombre": "Ruthlessness", "artista": "Jorge Rivera-Herrand"}, {"nombre": "Culpable o No", "artista": "Luis Miguel"}]

# Función para agregar una canción a la lista
def agregar_cancion(nombre, artista):
    # Se crea un diccionario con los datos de la canción
    nueva_cancion = {"nombre": nombre, "artista": artista}
    # Se agrega a la lista global
    lista_canciones.append(nueva_cancion)
    print("¡Canción agregada con éxito!")

# Función para mostrar todas las canciones registradas
def ver_canciones():
    print("\n--- LISTA DE CANCIONES ---")
    # Condicional para verificar si la lista está vacía
    if len(lista_canciones) == 0:
        print("No hay canciones registradas en la lista.")
    else:
        # Ciclo para recorrer la lista e imprimir cada canción
        for i in range(len(lista_canciones)):
            print(f"{i + 1}. {lista_canciones[i]['nombre']} - {lista_canciones[i]['artista']}")

# Función para eliminar una canción por su número
def eliminar_cancion(indice):
    # Condicional para verificar si el índice está dentro del rango de la lista
    if indice >= 0 and indice < len(lista_canciones):
        # Se elimina el elemento de la lista usando pop()
        lista_canciones.pop(indice)
        print("¡Canción eliminada con éxito!")
    else:
        print("Número de canción inválido.")

# Función para buscar una canción por su nombre
def buscar_cancion(nombre_buscar):
    print("\n--- RESULTADO DE BÚSQUEDA ---")
    encontrado = 0
    # Ciclo para recorrer la lista y comparar el nombre
    for cancion in lista_canciones:
        # Condicional para ver si el nombre coincide (ignorando mayúsculas/minúsculas)
        if cancion["nombre"].lower() == nombre_buscar.lower():
            print(f"Encontrada: {cancion['nombre']} - {cancion['artista']}")
            encontrado = 1
            
    # Condicional final si no se encontró ninguna coincidencia
    if encontrado == 0:
        print("Canción no encontrada.")

# Función para guardar la lista de canciones en un archivo json
def guardar_canciones_json():
    # Se crea un diccionario vacío para guardar los datos en formato artista: cancion
    datos_guardar = {}
    
    # Se recorre la lista de canciones
    for cancion in lista_canciones:
        # Se asigna el artista como clave y el nombre de la canción como valor
        datos_guardar[cancion["artista"]] = cancion["nombre"]
        
    # Se abre el archivo canciones.json en modo escritura
    with open("canciones.json", "w") as f:
        # Se escribe el diccionario en el archivo
        json.dump(datos_guardar, f)
        
    print("Lista de canciones guardada en 'canciones.json'.")
