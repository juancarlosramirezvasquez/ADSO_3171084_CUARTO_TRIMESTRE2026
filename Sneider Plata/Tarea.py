class Aprendiz:
    def __init__(self, id, nombre, apellido, edad, programa, trimestre, ambiente):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__programa = programa
        self.__trimestre = trimestre
        self.__ambiente = ambiente

    #Metodos

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_edad(self):
        return self.__edad

    def get_progrma(self):
        return self.__programa

    def get_trimestre(self):
        return self.__trimestre

    def get_ambiente(self):
        return self.__ambiente

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

    #datos iniciales

    def mostrar_info(self):
        print(f"\nId: {self.__id}", f"\nNombre: {self.__nombre}", f"\nApellido {self.__apellido}",f"\nEdad {self.__edad}", f"\nPrograma {self.__programa}", f"\nTrimestre {self.__trimestre}", f"\nAmbiente {self.__ambiente}")
        print("---------------------------------")

def main():
    aprendiz1 = Aprendiz(1,"kevin","barreto",21,"ADSO",4,218)

    aprendiz1.mostrar_info()


    #Information
    print("(Informacion Inicial del aprendiz:)")
    aprendiz1.mostrar_info()
            
    #Actualizacion edad

    aprendiz1.set_edad(22)
    print("Actualizacion de dato del aprendiz:")

    #Actualizacion ambiente
    aprendiz1.set_ambiente(220)
    print("Actualizacion de ambiente del aprendiz:")

    #Actualizacion trimestre
    aprendiz1.set_trimestre(5)
    print("Actualizacion de trimestre del aprendiz:")

    print("Informacion actualizada del aprendiz")
    aprendiz1.mostrar_info() 

if __name__ == "__main__":
    main()