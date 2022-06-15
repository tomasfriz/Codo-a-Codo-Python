# ------------------------------------------------------------
# Problema 4:
# Desarrollar una clase que represente un punto en el plano y 
# tenga los siguientes métodos:
# inicializar los valores de x e y que llegan como parámetros, 
# imprimir en que cuadrante se encuentra dicho punto (concepto
# matemático, primer cuadrante si x e y son positivas, si x<0 
# e y>0 segundo cuadrante, etc.)
# ------------------------------------------------------------

class Punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __del__(self):
        print('Método delete llamado')

    def imprimir(self):
        print(f"Coordenada del punto: ({self.x}:{self.y})")

    def imprimir_cuadrante(self):
        if self.x > 0 and self.y>0: 
            print("Primer cuadrante")
        elif self.x < 0 and self.y>0: 
            print("Segundo cuadrante")
        elif self.x < 0 and self.y<0: 
            print("Tercer cuadrante")
        else: 
            print("Cuarto cuadrante")

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")          # Limpiamos la pantalla

punto1 = Punto(10,-30)         # Instanciamos el objeto
punto1.imprimir()
punto1.imprimir_cuadrante()


