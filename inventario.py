class Aprendiz:
    def __init__(self, nombre, documento, edad, programa, promedio):
        self.__nombre = nombre
        self.__documento = documento
        self.__edad = edad
        self.__programa = programa
        self.__promedio = promedio

    #Metodos
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__documento

    def get_edad(self):
        return self.__edad

    def get_progrma(self):
        return self.__programa

    def get_trimestre(self):
        return self.__promedio
    
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, (str)):
            self.__nombre = nuevo_nombre
        else:
            print("El nombre debe ser valido")

    def set_documento(self, nuevo_documento):
        if isinstance(nuevo_documento, (int)) and nuevo_documento >= 1 :
            self.__edad = nuevo_documento
        else:
            print("El documento debe tener numeros validos")

    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, (int)) and nueva_edad >= 4 :
            self.__edad = nueva_edad
        else:
            print("La edad debe ser mayor o igual a 4")

    def set_programa(self, nuevo_programa):
        if isinstance(nuevo_programa, (str)):
            self.__programa = nuevo_programa
        else:
            print("El programa de formacion debe ser valido")

    def set_promedio(self, nuevo_promedio):
        if isinstance(nuevo_promedio, (int)) and nuevo_promedio <= 5:
            self.__promedio = nuevo_promedio
        else:
            print("El promedio debe ser menor a o igual a 5")

    #datos iniciales

    def mostrar_info(self):
        print(f"\nNombre: {self.__nombre}", f"\nDocumento {self.__documento}",f"\nEdad {self.__edad}", f"\nPrograma {self.__programa}", f"\nPromedio {self.__promedio}")
        print("---------------------------------")

def main():

    

     #Information
    print("---------------------------------")
    print("(Informacion Inicial del aprendiz:)")

    aprendiz1 = Aprendiz("Jose",1012345,6,"MTC",4.5)
    aprendiz2 = Aprendiz("Karlos",1054321,4,"ADSO",5)
    aprendiz3 = Aprendiz("Maria",5432101,8,"MMC",3.2)
    
    
    aprendiz1.mostrar_info()
    aprendiz2.mostrar_info()
    aprendiz3.mostrar_info()
    print("---------------------------------")
    
    #Actualizacion Nombre
    
    
    
    print("Actualizacion nombre de los aprendices:", aprendiz1.set_nombre("Josepito"),aprendiz2.set_nombre("Kevincho"), aprendiz3.set_nombre("Johana"))

    #Actualizacion Documento
    aprendiz1.set_documento(1235678)
    aprendiz2.set_documento(8765321)
    aprendiz3.set_documento(1234865)
    print("Actualizacion documento de los aprendices:")

    #Actualizacion Edad
    aprendiz1.set_edad(12)
    aprendiz2.set_edad(11)
    aprendiz3.set_edad(15)
    print("Actualizacion edad de los aprendices:")

    #Actualizacion Programa
    aprendiz1.set_programa("ADSO")
    aprendiz2.set_programa("ADSO")
    aprendiz3.set_programa("MTC")
    print("Actualizacion programa de los aprendices:")

    #Actualizacion Promedio
    aprendiz1.set_promedio(5)
    aprendiz2.set_promedio(5)
    aprendiz3.set_promedio(5)
    print("Actualizacion promedio de los aprendices:")

    print("Informacion actualizada de los aprendices")
    aprendiz1.mostrar_info()
    aprendiz2.mostrar_info()
    aprendiz3.mostrar_info()
    print("---------------------------------") 



if __name__ == "__main__":
    main()