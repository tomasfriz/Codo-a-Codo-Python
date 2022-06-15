class Fraccion():

    def __init__(self, numerador, denominador):
        self.nume = numerador
        self.deno = denominador
    
    def __str__(self):
        return f"{self.nume} / {self.deno}"

    def sumar(self, otro):
        numerador = self.nume * otro.deno + self.deno * otro.nume
        denominador = self.deno * otro.deno
        return Fraccion(numerador, denominador)

    def multiplicar(self, otro):
        numerador = self.nume * otro.nume
        denominador = self.deno * otro.deno
        return Fraccion(numerador, denominador)

    def dividir(self, otro):
        numerador = self.nume * otro.deno
        denominador = self.deno * otro.nume
        return Fraccion(numerador, denominador)

    def restar(self, otro):  
        numerador = self.nume * otro.deno - self.deno * otro.nume
        denominador = self.deno * otro.deno
        return Fraccion(numerador, denominador)              


fraccion1 = Fraccion(3, 2)
fraccion2 = Fraccion(1, 2)
fraccion3 = fraccion1.sumar(fraccion2)
print(fraccion3)
print(fraccion1.sumar(fraccion3))
print(fraccion1.restar(fraccion2))
