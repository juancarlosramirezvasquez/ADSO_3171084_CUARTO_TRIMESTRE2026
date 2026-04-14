class Operaciones:
    def __init__(self, dato1,dato2): 
        self.dato1 = dato1
        self.dato2 = dato2


    def calcular(self):
        print("Operaciones genericas en matematicas")

class Suma(Operaciones):
    def calcular(self):
        resultado = self.dato1 + self.dato2

        print(f"La suma es: {resultado}")


class Resta(Operaciones):
    def calcular(self):
        resultado = self.dato1 - self.dato2

        print(f"La Resta es: {resultado}")


class Multiplicacion(Operaciones):
    def calcular(self):
        resultado = self.dato1 * self.dato2

        print(f"La multiplicacion es: {resultado}")


class Division(Operaciones):
    def calcular(self):
        if self.dato2 != 0:
           resultado = self.dato1 / self.dato2
           print(f"La division es: {resultado}")
        else:
            print("NO se puede dividir emtre CERO")

def main():
    dato1 = float(input("Ingrese el primer numero: "))
    dato2 = float(input("Ingrese el segundo numero: "))

    operacion1 = Suma(dato1,dato2)
    operacion1.calcular()

    operacion2 = Resta(dato1, dato2)
    operacion2.calcular()

    operacion3 = Multiplicacion(dato1, dato2)
    operacion3.calcular()

    operacion4 = Division(dato1, dato2)
    operacion4.calcular()

    


if __name__ == "__main__":
    main()