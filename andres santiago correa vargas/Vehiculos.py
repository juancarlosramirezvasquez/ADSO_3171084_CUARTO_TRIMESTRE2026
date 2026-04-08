class Vehiculo:
    def __init__(self, tipo, marca, dueño, precio):
        self.__tipo = tipo
        self.__marca = marca
        self.__dueño = dueño
        self.__precio = precio

    def get_tipo(self):
        return self.__tipo

    def get_marca(self):
        return self.__marca

    def get_dueño(self):
        return self.__dueño

    def get_precio(self):
        return self.__precio
    
    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, (int)) and nueva_edad >= 14 :
            self.__edad = nueva_edad
        else:
            print("La edad debe ser mayoor o igual a 14")

    def set_trimestre(self, nuevo_trimestre):
        if isinstance(nuevo_trimestre, (int)) and nuevo_trimestre > 1:
            self.__trimestre = nuevo_trimestre
        else:
            print("El trimestre debe ser mayor a 1")

    def set_ambiente(self, nuevo_ambiente):
        if isinstance(nuevo_ambiente, (int)) and nuevo_ambiente :
            self.__ambiente = nuevo_ambiente
        else:
            print("El ambiente no se")