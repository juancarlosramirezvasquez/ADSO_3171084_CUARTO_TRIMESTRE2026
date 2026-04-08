from abc import ABC, abstractmethod

class figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class circulo(figura):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return (self.radio **2)*3.1416
    
class ccuadrado(figura):
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado * self.lado
    
        
def mostrar_area(figura: figura):
    print(f"area es. {figura.calcular_area():.2f}")

def main():
    radio = float(input("ingrese el radio del siculo:  "))