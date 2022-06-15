# Creamos la clase "Alumno":
class Alumno:   
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota   = nota
    
    def __str__(self):
        return f"{self.nombre} tiene una nota de {self.nota}"
	

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")          # Limpiamos la pantalla

alumno1 = Alumno("Juan", 7)    # Instanciamos el objeto
print(alumno1)

alumno1.nota = 10
print(alumno1)

