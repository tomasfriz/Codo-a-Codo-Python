# ------------------------------------------------------------
# PYTHON 5 - Objetos
# Ejemplo - Creamos una clase e instanciamos dos objetos
# ------------------------------------------------------------

# Creamos la clase "Persona":
class Alumno:
    def inicializar(self,nombre, nota): # Constructor
        self.nombre = nombre
        self.nota   = nota        

    # Método para mostrar datos
    def imprimir(self):
        print(f"Nombre: {self.nombre}")

    # Método para mostrar la nota 
    def mostrar_estado(self):
        if self.nota <= 4:
            print(f"{self.nombre} tiene regular ({self.nota})")
        else:
            print(f"{self.nombre} ha aprobado ({self.nota})")


# ------------------------------------------------------------
# Programa principal
# ------------------------------------------------------------
alumno1 = Alumno()              # Creamos un objeto
alumno1.inicializar("Juana", 3) # Llamamos al constructor con un nombre y una nota
alumno1.imprimir()              # Mostramos el nombre
alumno1.mostrar_estado()        # Mostramos el valor de los atributos

alumno2=Alumno()                # Creamos otro objeto
alumno2.inicializar("Diego", 7) # Llamamos al constructor con un nombre y una nota
alumno2.imprimir()              # Mostramos el nombre
alumno2.mostrar_estado()        # Mostramos el valor de los atributos


