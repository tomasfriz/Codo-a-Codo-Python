# ------------------------------------------------------------
# Getters y Setters
# ------------------------------------------------------------

class ListadoBebidas:

    def __init__(self):
        self._bebida = 'Naranja'
        self.bebidas_validas = ['Naranja', 'Manzana']

    # Encapsulamiento: atributos privados
    # decorador @property
    # https://codigofacilito.com/articulos/decoradores-python
    @property
    def bebida(self):
        return f"La bebida oficial es: {self._bebida}"

    @bebida.setter
    def bebida(self, bebida):
        self._bebida = bebida

# ------------------------------------------------------------
# Bloque principal
# ------------------------------------------------------------
print("\033[H\033[J")          # Limpiamos la pantalla        

bebidas = ListadoBebidas()
print(bebidas.bebida)
bebidas.bebida = 'Limonada'
print(bebidas.bebida)

bebidas.bebidas_validas[0] = 'Limon'
print(bebidas.bebidas_validas)