class Vehiculo:
    def mover(self):
        print("El vehiculo se esta moviendo")


#ahora crear una clase hija 

class Moto(Vehiculo):
    pass

def main():
    vehiculo1 = Vehiculo()
    moto1 = Moto()

    print("Metodo desde clase vehiculo")

    moto1.mover()

if __name__ == "__main__":
    main()


