# ------------------------------------------------------------
# Encapsulacion:
# encapsular consiste en hacer que los atributos o métodos 
# internos a una clase no se puedan acceder ni modificar desde
# fuera, sino que tan solo el propio objeto pueda acceder a ellos.
# ------------------------------------------------------------

# Creamos la clase "Coche":

class Coche():
	# Metodo constructor (Estado inicial)
    def __init__(self):
        self.__ruedas      = 4     
        self.__largoChasis = 280
        self.__anchoChasis = 145
        self.__en_marcha   = False

    # Metodos --------------------------------
    def arrancar(self, arrancamos):
        self.__en_marcha = arrancamos
        if self.__en_marcha:
            if self.__chequeo_interno() == False:
                return "El coche no puede arrancar"
            else:
                return "El coche está OK y ha arrancado"
        else:
            return "El coche se ha detenido"

    # Método que comprueba el "estado interno" del coche
    def __chequeo_interno(self):
        print("Comprobando el coche:")
        self.combustible = "Ok"
        self.puertas     = "Cerradas"
        if self.combustible == "Ok" and self.puertas == "Cerradas":
            return True
        else:
            return False


# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")             # Limpiamos la pantalla

coche1 = Coche()   
print(coche1.arrancar(True))
print(coche1.arrancar(False))
print(coche1.arrancar(True))

#print(coche1.ruedas)              # Esto no se permite mas porque es un atributo privado
#coche1.ruedas = 6                 # Esto no se permite mas porque es un atributo privado
#print(coche1.ruedas)              # Esto no se permite mas porque es un atributo privado

#print(coche1.chequeo_interno())   # Esto no se permite mas porque es un atributo privado



