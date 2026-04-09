class Operacion:
    def __init__(self, dato1, dato2):
        self.dato1 = dato1
        self.dato2 = dato2
    def calcular(self):
        print("operaiones genericas matematicas")

class Suma(Operacion):
    def calcular(self):
        resultado = self.dato1 + self.dato2
        print(f"la suma es: {resultado}")
class Resta(Operacion):
    def calcular(self):
        resultado = self.dato1 - self.dato2
        print(f"la resta es: {resultado}")
class Multiplicacion(Operacion):
    def calcular(self):
        resultado = self.dato1 * self.dato2
        print(f"la multiplicacion es: {resultado}")
class Division(Operacion):
    def calcular(self):
        if self.dato2 !=0:
            resultado = self.dato1 / self.dato2
            print(f"la division es: {resultado}")
        else:
            print("No se puede dividir entre CERO")
def main():
    dato1 = float(input("ingrese el primer numero: "))
    dato2 = float(input("ingrese el segundo numero: "))
    operacion1=Suma(dato1,dato2)
    operacion1.calcular()

    dato1 = float(input("ingrese el primer numero: "))
    dato2 = float(input("ingrese el segundo numero: "))
    operacion1=Resta(dato1,dato2)
    operacion1.calcular()

    dato1 = float(input("ingrese el primer numero: "))
    dato2 = float(input("ingrese el segundo numero: "))
    operacion1= Multiplicacion(dato1,dato2)
    operacion1.calcular()

    dato1 = float(input("ingrese el primer numero: "))
    dato2 = float(input("ingrese el segundo numero: "))
    operacion1=Division(dato1,dato2)
    operacion1.calcular()



if __name__ == "__main__":
    main()
