from abc import ABC, abstractmethod
class Figura(ABC):
    @abstractmethod
    def calcular_area(self): #Este metodo es obligatorio en todas las clases
        pass
    # Ahora vamos a crear las subclases de figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return ((self.radio ** 2) * 3.1416) 
class Cuadrado(Figura):
    def __init__(self,lado1):
        self.lado1 = lado1
    def calcular_area(self):
        return (self.lado1 ** 2) 
class Piradime(Figura):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    def calcular_area(self):
        return ((self.radio ** 2) * 3.1416) 
class Rectangulo(Figura):
    def __init__(self,lado1):
        self.lado1 = lado1
    def calcular_area(self):
        return (self.lado1 ** 2) 
class Cilindro(Figura):
    def __init__(self,lado1):
        self.lado1 = lado1
    def calcular_area(self):
        return (self.lado1 ** 2) 
 #Vamos a ejecutar
def mostrar_area(figura :Figura):
    print(f"Area {figura.calcular_area():.2f}")
def main():
    radio1 = float(input("Ingrese el radio del circulo: ")) 
    circulo1 = Circulo(radio1)
    mostrar_area(circulo1)
def main():
    lado1 = float(input("Ingrese un lado: ")) 
    cuadrado1 = Cuadrado(lado1)
    mostrar_area(cuadrado1)
     
if __name__ == "__main__":
    main()
