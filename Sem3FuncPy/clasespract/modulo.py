class Alumno:
    #Vamos a definir propiedades
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
       
    
    def saludar(self):
        print(f"Hola programadores y tu que tal? {self.nombre}, {self.edad} años")

class Perro:
    def __init__(self, nombre, raza, altura):
        self.nombre = nombre
        self.raza = raza
        self.altura =altura
    
    def comer(self):
        print(f"{self.nombre} esta comiendo")
    def ladrar(self):
        print(f"{self.nombre} esta ladrando")
    def dormir(self):
        print(f"{self.nombre} esta durmiendo")
    
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def mostrarNota(self):
        aprobado = self.nota>= 70
        print(f"Hola {self.nombre}, tu nota es: {self.nota}")
        if aprobado: print("Estas aprobado")
        else: print("Estas reprobado")
    
    