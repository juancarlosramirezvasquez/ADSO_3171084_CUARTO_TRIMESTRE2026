class Empleado:
    def trabajar(self):
        print("El empleado esta realizando tareas generales")

class Gerente(Empleado):
    def trabajar(self):
        print("El Gerente administra la empresa")
    pass
class Venderdor(Empleado):
    def trabajar(self):
        print("El Vendedor atiende un cliente")
    pass

def main():
    gerente1=Gerente()
    gerente1.trabajar()
    vendedor1=Venderdor()
    vendedor1.trabajar()

if __name__ == "__main__":
    main()