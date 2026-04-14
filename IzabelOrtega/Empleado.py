class Empleado:
    def trabajar(self):
        print("El empleado esta realizando tareas generales")

class Gerente(Empleado):
    def trabajar(self):
        print("El gerente administra la empresa")

class Vendedor(Empleado):
    def trabajar(self):
        print("El vendedor atiende al cliente")

def main():
    gerente1 = Gerente()
    gerente1.trabajar()

    vendedor1 = Vendedor()
    vendedor1.trabajar()

if __name__ == "__main__":
    main()

