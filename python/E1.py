from abc import ABC, abstractmethod
# creamos clase abstracta
class Figura(ABC):
    @abstractmethod
    def calcular(self):
        pass

#creamos una subclase
class Circulo(Figura):
    def __init__(self,radio):
         self.radio = radio
    def calcular(self):
         return 3.1416 * (self.radio ** 2)
    

class Triangulo(Figura):
    def __init__(self,altura,base):
         self.altura = altura
         self.base = base
    def calcular(self):
        return (self.altura * self.base / 2)       
class Rectangulo(Figura):
    def __init__(self,altura,base):
         self.altura = altura
         self.base = base
    def calcular(self):
        return (self.altura * self.base )   
class Cubo(Figura):
    def __init__(self, lado):
        self.lado = lado

    # volumen del cubo
    def calcular(self):
        return self.lado ** 3

# =========================================================================
class Cilindro(Figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    # volumen del cilindro
    def calcular(self):
        return 3.1416 * (self.radio ** 2) * self.altura

# =========================================================================

def mostrar_resultado(figura: Figura, nombre_figura: str):
    print(f"El resultado del {nombre_figura} es: {figura.calcular():,.2f}")

# Ejecucion del programa
def main():
    circulo1 = Circulo(5)
    mostrar_resultado(circulo1, "area del circulo")

    triangulo1 = Triangulo(5, 10)
    mostrar_resultado(triangulo1, "area del triangulo")

    rectangulo1 = Rectangulo(5, 10)
    mostrar_resultado(rectangulo1, "area del rectangulo")

    cubo1 = Cubo(5)
    mostrar_resultado(cubo1, "volumen del cubo")

    cilindro1 = Cilindro(3, 7)
    mostrar_resultado(cilindro1, "volumen del cilindro")


if __name__ == "__main__":
    main()