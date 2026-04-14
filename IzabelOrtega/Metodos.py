class Padre:
    def __init__ (self, mensaje):
        self.mensaje = mensaje


class Hijo(Padre):
    def __init__(self, mensaje,nombre):
        super().__init__(mensaje) #aqui invoco el atributo ue esta en Padre
        self.nombre = nombre 

def main():

    objepadre = Padre("Este es el mensaje de Padre")
    print (objepadre.mensaje)

    objetohijo = Hijo("Este es el mensaje del Hijo", "Iber Ortega")
    print(objetohijo.mensaje)
    print(objetohijo.nombre)

if __name__ == "__main__":
    main()