class Animal:
    def sonido(self):
        print("El animal emite un sonido")

class Perro(Animal):
    def sonido(self):
        print("El perro ladra")
        print("GUAU GUAU!!")
    pass


class Gato(Animal):
    def sonido(self):
        print("El gato maulla")
        print("MIAU MIAU!!")
    pass

class Leon(Animal):
    def sonido(self):
        print("El leon ruge")
        print("RWAA!!")
    pass

class Aguila(Animal):
    def sonido(self):
        print("El aguila da un chillido")
        print("fIUUU!!")
    pass

def main():

    perro1 = Perro()
    perro1.sonido()

    gato1 = Gato()
    gato1.sonido()

    leon1 = Leon()
    leon1.sonido()

    aguila1 = Aguila()
    aguila1.sonido()

if __name__ == "__main__":
    main()


