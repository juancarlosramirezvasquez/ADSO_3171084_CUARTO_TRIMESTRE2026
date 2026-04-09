class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio

    @property
    def titulo(self):
        return self.__titulo
    @property
    def precio(self):
        return self.__precio

    @titulo.setter
    def titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str):
            self.__titulo = nuevo_titulo
        else:
            print("debe ingresar un texto")

    @precio.setter
    def precio(self, nuevo_precio,):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >=0:
            self.__precio = nuevo_precio
        else:
            print("debe ingresar un numero entero o flotante")

    def mostrar_info(self):
        print(f"El titulo del libro es: {self.__titulo}, El precio es: ${self.__precio:,.2f}\n")

def main():
    print("PROGRAMA PARA VERIFICAR LOS DECORADORES EN POO @property para GETTER y @atrbutos.setter para SETTER\n")
    libro1 = Libro("100 años de soledad",75000)

    libro1.mostrar_info()
    libro1.titulo = "El coronel no tiene quien le escriba"
    print(libro1.titulo)

    #actualizar precio del libro
    libro1.precio = float(input("igrese el nuevo valor del libro: $.."))
    print(libro1.precio)

    libro1.mostrar_info()

if __name__ == "__main__":
    main()