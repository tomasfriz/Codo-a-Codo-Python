# ------------------------------------------------------------
# PYTHON 5 - Objetos
# Ejemplo - Creamos una clase e instanciamos objetos
# ------------------------------------------------------------

# Creamos la clase "Persona":
class Persona:
    piernas = 2 # Atributo (Variable de clase)

    def inicializar(self,nombre): # Constructor
        self.nombre = nombre

    def imprimir(self): # Método para mostrar datos
        print(f"Nombre: {self.nombre}")


# ------------------------------------------------------------
# Programa principal
# ------------------------------------------------------------
persona1 = Persona()          # Creamos un objeto
persona1.inicializar("Pedro") # Llamamos al constructor con un nombre
persona1.imprimir()           # Mostramos el nombre
print(persona1.piernas)       # Mostramos el valor del atributo "piernas"

persona1.piernas = 6

persona2=Persona()            # Creamos otro objeto
persona2.inicializar("Carla") # Llamamos al constructor con un nombre
persona2.imprimir()           # Mostramos el nombre
print(persona2.piernas)       # Mostramos el valor del atributo "piernas"



