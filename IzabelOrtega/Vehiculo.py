class Vehiculo:
    def mover(self):
        print("El vehiculo se esta moviendo")

class Moto (Vehiculo):
    def mover(self):
        print("La moto rueda  por la carretera")
    pass

class Carro (Vehiculo):
    def mover(self):
        print("El carro esta barado")
    pass

class Avion (Vehiculo):
    def mover(self):
        print("El avion vuela")
    pass

class Submarino (Vehiculo):
    def mover(self):
        print("El submarino bucea en el mar")
    pass


def main():

    moto1 = Moto()
    moto1.mover()

    carro1 = Carro()
    carro1.mover()

    avion1 = Avion()
    avion1.mover()

    submarino1 = Submarino()
    submarino1.mover()

if __name__ == "__main__":
    main()