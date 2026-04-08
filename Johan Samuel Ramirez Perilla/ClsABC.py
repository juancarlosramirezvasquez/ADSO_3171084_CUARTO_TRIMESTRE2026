from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio=radio
    
    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)

#===============================================================
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    
    def calcular_area(self, ):
        return (self.base * self.altura) / 2 
#===============================================================
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def calcular_area(self):
        return (self.base * self.altura)
#===============================================================
class Cubo(Figura):
    def __init__(self, lado):
        self.lado=lado

    def calcular_area(self):
        return 6 * (self.lado ** 2 )
    
#===============================================================
class Cuadrado(Figura):
    def __init__(self, areal, areab):
        self.areal=areal
        self.areab=areab
    def calcular_area(self):
        return
#===============================================================
def mostrar_area(figura: Figura):
    print(f"Area: {figura.calcular_area():,.2f}")


def main():
    circulo1 = Circulo(5)
    mostrar_area(circulo1)

    triangulo1 = Triangulo(7,5)
    mostrar_area(triangulo1)
    
    rectangulo1 = Rectangulo(5,9)
    mostrar_area(rectangulo1)
    
    cubo1 = Cubo(8)
    mostrar_area(cubo1)

    cuadrado1 = Cuadrado(5)
    mostrar_area(cuadrado1)
if __name__ == "__main__":
    main()