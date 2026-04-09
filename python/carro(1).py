class Carro:
    def __init__(self, marca, modelo, año, placas):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__placas = placas
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_año(self):
        return self.__año
    def get_placas(self):
        return self.__placas
    def set_marca(self, nueva_marca):
         if isinstance(nueva_marca, (int, float)) and nueva_marca > 0:
            self.__centro = nueva_marca
         else:
            print("inserte la marca del vehiculo")
    def set_modelo(self, nuevo_modelo):  
        if isinstance(nuevo_modelo, int) and nuevo_modelo > 0:
            self.__ficha = nuevo_modelo
        else:
            print("inserte el modelo")
    def set_año(self, nuevo_año):  
        if isinstance(nuevo_año, int) and nuevo_año > 0:
            self.__programa = nuevo_año
        else:
            print("inserte el año del modelo")
    def set_placas(self, nueva_placas):  
        if isinstance(nueva_placas, int) and nueva_placas > 0:
            self.__trimestre= nueva_placas
        else:
            print("inserte las placas ")
    def mostrar_info(self):
        print(f"\nmarca:{self.__marca}")
        print(f"\nmodelo:{self.__modelo}")
        print(f"\naño:{self.__año}")
        print(f"\nplacas:{self.__placas}")
def main():
    cliente1 = Carro ("chevrolet ","twingo",2009,"tre435",)
    print("el carro antiguo tenia estos atributos"(cliente1.set_marca))
    cliente1.set_marca = input("ingrese la marca")
    cliente1.set_modelo= (input("ingrese el modelo :$ .."))
    cliente1.set_año= int(input("ingrese el año :$ .."))
    cliente1.set_placas= (input("ingrese las placas :$ ..")) 
    print(cliente1.set_marca)
    print(cliente1.set_modelo)
    print(cliente1.set_año)
    print(cliente1.set_placas)

if __name__ == "__main__":
    main()