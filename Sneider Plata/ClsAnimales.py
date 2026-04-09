class Animal:
    def sonido(self):
        print("El animal hace sonidos")

class Perro(Animal):
    def sonido(self):
        print("Perro: GUAU!!!!!")
    pass
class Gato(Animal):
    def sonido(self):
        print("Gato: MIAU...")
    pass
class Leon(Animal):
    def sonido(self):
        print("Leon: ROAAHR!!!!!!!!!!!")
    pass
class Aguila(Animal):
    def sonido(self):
        print("Aguila: COH COOAAAH!!!")
    pass

def main():
    perro1=Perro()
    gato1=Gato()
    leon1=Leon()
    aguila1=Aguila()
    perro1.sonido()
    gato1.sonido()
    leon1.sonido()
    aguila1.sonido()

if __name__ == "__main__":
    main()