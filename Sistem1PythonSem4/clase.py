class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones=[]
    
    def agregar_calificacion(self, nota:float):
        self.calificaciones.append(nota)
    
    def promedio(self):
        if len(self.calificaciones) == 0:  # Verificar si la lista está vacía
            return 0.0  # Retornar 0.0 si no hay calificaciones
        return sum(self.calificaciones) / len(self.calificaciones)
    def mostrar_info(self):
        #Mostramos toda la informacion personal del estudiante
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.promedio():.2f}")
        
    
        
