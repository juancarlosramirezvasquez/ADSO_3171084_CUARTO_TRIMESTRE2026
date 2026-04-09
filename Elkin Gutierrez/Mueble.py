class Mueble:
    def __init__(self, id, nombre, dimenciones, color, propietario, material, ubicacion):
        self.__id = id
        self.__nombre = nombre
        self.__dimenciones = dimenciones
        self.__color = color
        self.__propietario = propietario
        self.__material = material
        self.__ubicacion = ubicacion

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre
    
    def get_dimenciones(self):
        return self.__dimenciones

    def get_color(self):
        return self.__color
    
    def get_propietario(self):
        return self.__propietario

    def get_material(self):
        return self.__material
    
    def get_ubicacion(self):
        return self.__ubicacion
    
#====================================================================================================

    def set_color(self, nuevo_color):
        if isinstance(nuevo_color, (str)):
            self.__color = nuevo_color
        else:
            print("El color debe ser valido")

    def set_propietario(self, nuevo_propietario):
        if isinstance(nuevo_propietario, (str)):
            self.__propietario = nuevo_propietario
        else:
            print("El propietario debe ser valido")
    
    def set_ubicacion(self, nuevo_ubicacion):
        if isinstance(nuevo_ubicacion, (str)):
            self.__ubicacion = nuevo_ubicacion
        else:
            print("El ubicacion debe ser valida")

#=====================================================================================================

    def mostrar_info(self):
        print(f"\nId: {self.__id}", f"\nNombre: {self.__nombre}", f"\nDimenciones: {self.__dimenciones}", f"\nColor: {self.__color}", f"\nPropietario: {self.__propietario}", f"\nMaterial: {self.__material}", f"\nUbicacion: {self.__ubicacion}",)
        print("=======================================")

def main():

    print("--------------------------------------")
    print("Informacion del pedido")

    mueble1 = Mueble(111,"Sillon", 300, "Rojo", "Jose", "Tela transpirable", "Bosa")
    mueble2 = Mueble(222,"Mesa", 600, "Verde", "Carla", "Madera de pino", "Soacha")
    mueble3 = Mueble(333,"Cajon", 1000, "Cafe", "Mario", "Roble oscuro", "Kennedy")

    mueble1.mostrar_info()
    mueble2.mostrar_info()
    mueble3.mostrar_info()

    print("Actualizacion de color...:", mueble1.set_color("Azul"),mueble2.set_color("Negro"),mueble3.set_color("Beige"))
    print("Actualizacion de propietario...:",  mueble1.set_propietario("Joseph"), mueble2.set_propietario("Carlos"), mueble3.set_propietario("Maria"))
    print("Actualizacion de ubicacion...:", mueble1.set_ubicacion("Barrios unidos"),mueble2.set_ubicacion("Ciudad montes"),mueble3.set_ubicacion("Suba"))

    print("============================================")
    print("Datos actualizados...:")

    mueble1.mostrar_info()
    mueble2.mostrar_info()
    mueble3.mostrar_info()

    print("============================================")

if __name__ == "__main__":
    main()
