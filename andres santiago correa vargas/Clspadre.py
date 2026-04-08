class  Vehiculo:

    def mover(self):

        print("El Vehiculo se esta moviendo")

class Moto(Vehiculo):

    pass

def main():
    vehiculo1 = Vehiculo()
    moto1 = Moto()
    print("Metodo desde la clase vehiculo")
    vehiculo1.mover
    moto1.mover
  
if __name__ == "__main__":
    main()