#forma tradicional de encapsulamiento y validaciones seguras a los atributos de la clase libro.
class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio
#GETTER = CONSULTAR, VER, MOSTRAR; Nos permite acceder al valor almacenado en el atributo de forma segura

    def get_titulo(self):
        #vamos a devolverel valor almacenado en titulo
        return self.__titulo
    def get_precio(self):
        return self.__precio
#SETTER: Modificar valores, controla y valida los valores antes de ser modificados    

    def set_titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str):
            self.__titulo = nuevo_titulo
        else:
            print("debe ingresar un titulo valido")

    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int,float)) and nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("debe ingresar un precio valido")

    def mostrar_info(self):
        print(f"titulo: {self.__titulo}")
        print(f"precio: ${self.__precio:,.2f}")


def main():
    print("\n=== SISTEMA DE LIBROS ADSO ===")

    libro1 = Libro("El Quijote",80000)

    print("inforacion principal del libro\n")
    libro1.mostrar_info()


    print(f"precio actual:", libro1.get_precio())


    libro1.set_precio(20000)
    print(f"El nuevo precio actualizado es:", libro1.get_precio())

    print("informacion principal del libro\n")
    libro1.mostrar_info()

    print("====================PROGRAMA FINALIZADO=======================")
if __name__ == "__main__":
    main()
