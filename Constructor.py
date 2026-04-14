class Vehiculo:
    def accion(self):
        print("El animal hace sonidos")

class Moto(Vehiculo):
    def accion(self):
        print("La moto rueda")
    pass
class Carro(Vehiculo):
    def accion(self):
        print("El carro rueda")
    pass
class Avion(Vehiculo):
    def accion(self):
        print("El avion vuela")
    pass
class Submarino(Vehiculo):
    def accion(self):
        print("Submarino vucea")
    pass

def main():
    moto1=Moto
    carro1=Carro
    avion1=Avion
    submarino1=Submarino
    moto1.accion
    carro1.accion
    avion1.accion
    submarino1.accion

if __name__ == "__main__":
    main()