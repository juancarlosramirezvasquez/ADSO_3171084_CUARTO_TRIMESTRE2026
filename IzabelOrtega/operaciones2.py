class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Inicializando opereacion...")
    def calcular(self):
        print("Operacion generica")


class Suma(Operacion):
    def __init___(self,a,b):
        super().__init__(a,b)
        print("Preparando operacion suma ")
    def calcular(self):
        super().calcular() #Aqui llamamos el metodo del padre
        resultado = self.a + self.b
        print(f"La suma es: {resultado}")


class Resta(Operacion):
    def __init__(self, a, b):
        super().__init__(a,b)
        print("Preparando operacion resta")
    def calcular(self):
        super().calcular()
        resultado = self.a - self.b
        print(f"La resta es: {resultado}")

class Multiplicacion(Operacion):
    def __init__(self, a, b):
        super().__init__(a,b)
        print("Preparando operacion multiplicacion")
    def calcular(self):
        super().calcular()
        resultado = self.a * self.b
        print(f"La multiplicacion es: {resultado}")

class Division(Operacion):
    def __init__(self, a, b):
        super().__init__(a,b)
        print("Preparando operacion division")
    def calcular(self):
        super().calcular()
        resultado = self.a / self.b
        print(f"La division: {resultado}")

class Potencia(Operacion):
    def __init__(self, a, b):
        super().__init__(a,b)
        print("Preparando operacion Potencia")
    def calcular(self):
        super().calcular()
        resultado = self.a ** self.b
        print(f"La Potencia es: {resultado}")


def main():

    num1 = float (input("Ingrese el primer numero: "))
    num2 = float (input ("Ingrese el segundo numero: "))

    operacion1 = Suma (num1, num2)
    operacion1.calcular()
    print("----------------------------------------------")

    operacion2 = Resta (num1, num2)
    operacion2.calcular()
    print("----------------------------------------------")

    operacion3 = Multiplicacion (num1, num2)
    operacion3.calcular()
    print("----------------------------------------------") 

    operacion4 = Division(num1, num2)
    operacion4.calcular()

    print("----------------------------------------------") 

    operacion5 = Potencia(num1, num2)
    operacion5.calcular()



if __name__ == "__main__":
    main()