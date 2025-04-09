
def menu_opciones():
    
    print("1.\tRegistrar nuevo estudiante")
    print("2.\tAgregar calificación a un estudiante")
    print("3.\tMostrar información de un estudiante")
    print("4.\tMostrar todos los estudiantes")
    print("5.\tSalir del programa")
    opcion = int(input("Seleccione una opción: "))  # Intentar convertir la entrada a entero
    return opcion  

def buscar_estudiante(nombre, lista_estudiantes):   
#Busca un estudiante por nombre en la lista
    for estudiante in lista_estudiantes:
        if estudiante.nombre.upper() == nombre.upper():
            return estudiante
    return None
        


