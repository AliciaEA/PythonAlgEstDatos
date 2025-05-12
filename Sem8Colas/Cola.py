#Definienfo la clase nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        

#Definiendo la clase Cola
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        

    def Insetar(self, dato):
        nuevo = Nodo(dato)
        if self.primero is None:
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
    
    def Eliminar(self):
        if self.primero is None:
            return None
        else:
            dato = self.primero.dato
            self.primero = self.primero.siguiente
            if self.primero is None:
                self.ultimo = None
            return dato
            
    def Imprimir(self):
        actual = self.primero
        if actual is None:
            print("Cola vacía.")
            return
        while actual is not None:
            print(actual.dato, end="\n")
            actual = actual.siguiente
        