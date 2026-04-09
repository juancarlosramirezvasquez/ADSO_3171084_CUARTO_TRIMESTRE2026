class Padre:
    def __init__(self, mensaje):
        self.mensaje = mensaje

class Hijo(Padre):
    def __init__(self, mensaje, nombre):
        super().__init__(mensaje)
        self.nombre = nombre
def main():
    objepadre = Padre("Este es el mensaje desde el padre")
    print(objepadre.mensaje)
    objehijo = Hijo("Este es el mensaje desde hijo","puto")
    print(objehijo.mensaje)
    print(objehijo.nombre)

if __name__ == "__main__":
    main()