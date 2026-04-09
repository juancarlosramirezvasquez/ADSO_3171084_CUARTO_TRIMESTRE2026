class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio= precio 
    #decoradores
    #para el getter, sea mostrar los valores
    #de las variables 
    @property
    def titulo(self):
        return self.__titulo 
    @property #decorador para el getter 
    def precio(self):
        return self.__precio
    #setter, modificar los valores de los atributos

    @titulo.setter
    def titulo(self,nuevo_titulo):
        if isinstance(nuevo_titulo, str):
            self.__titulo = nuevo_titulo
        else:
            print("debe ingresar un texto")
    @precio.setter
    def precio(self,nuevo_precio):
        if isinstance(nuevo_precio,(int, float)) and nuevo_precio >=0:
            self.__precio = nuevo_precio
        else:
            print("debe ingresar un numero entero o flotante ")
    def mostrar_info(self):
        print(f"El titulo del libro es: {self.__titulo},el precio del libro es: ${self.__precio:,.2f}")
def main():
    print("programa para verificar los decoradores en poo @property para getter y @atributo.setter para setter")
    Libro1 = Libro("100 años de soledad", 75000)
    Libro1.mostrar_info()
    Libro1.titulo = "el coronel no tiene quien le escriba"
    Libro1.precio = float(input("ingrese el nuevo valor :$ .."))
    print(Libro1.precio)
if __name__ == "__main__":
    main()