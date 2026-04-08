class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("inicializando operacion...")
    def calcular(self):
        print("operacion generica")

class Suma(Operacion):
    def __init__(self, a, b):
        super().__init__(a, b)
        print("preparando operacion suma ")
    def calcular(self):
        super().calcular()
        resultado = self.a + self.b
        print(f"la suma es {resultado}")

class Resta(Operacion):
    def __init__(self, a, b):
        super().__init__(a, b)
        print("preparando operacion suma ")
    def calcular(self):
        super().calcular()
        resultado = self.a - self.b
        print(f"la suma es {resultado}")

class Multiplicacion(Operacion):
    def __init__(self, a, b):
        super().__init__(a, b)
        print("preparando operacion suma ")
    def calcular(self):
        super().calcular()
        resultado = self.a * self.b
        print(f"la suma es {resultado}")

class Division(Operacion):
    def __init__(self, a, b):
        super().__init__(a, b)
        print("preparando operacion suma ")
    def calcular(self):
        super().calcular()
        resultado = self.a / self.b
        print(f"la suma es {resultado}")

class Potencia(Operacion):
    def __init__(self, a, b):
        super().__init__(a, b)
        print("preparando operacion suma ")
    def calcular(self):
        super().calcular()
        resultado = self.a ** self.b
        print(f"la suma es {resultado}")

def main():
    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    operacion1=Suma(num1,num2)
    operacion1.calcular()
    print("-------------------------------------------------")

    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    operacion1=Resta(num1,num2)
    operacion1.calcular()
    print("-------------------------------------------------")

    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    operacion1=Multiplicacion(num1,num2)
    operacion1.calcular()
    print("-------------------------------------------------")

    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    operacion1=Division(num1,num2)
    operacion1.calcular()
    print("-------------------------------------------------")

    num1 = float(input("ingrese el primer numero: "))
    num2 = float(input("ingrese el segundo numero: "))
    operacion1=Potencia(num1,num2)
    operacion1.calcular()
    print("-------------------------------------------------")

if __name__ == "__main__":
    main()
