class Aprendiz:
    def __init__(self, nombre, apellidos, id, centro, ficha, programa, trimestre):
         self.__nombre = nombre
         self.__apellidos = apellidos
         self.__id = id
         self.__centro = centro
         self.__ficha  = ficha
         self.__programa = programa
         self.__trimestre = trimestre
    def get_nombre(self):
        return self.__nombre
    def get_apellidos(self):
        return self.__apellidos
    def get_id(self):
        return self.__id
    def get_centro(self):
        return self.__centro
    def get_ficha(self):
        return self.__ficha
    def get_programa(self):
        return self.__programa
    def get_trimestre(self):
        return self.__trimestre
    def set_centro(self, nuevo_centro):
         if isinstance(nuevo_centro, (int, float)) and nuevo_centro > 0:
            self.__centro = nuevo_centro
         else:
            print("inserte el centro de formacion")
    def set_ficha(self, nueva_ficha):  
        if isinstance(nueva_ficha, int) and nueva_ficha > 0:
            self.__ficha = nueva_ficha
        else:
            print("inserte la nueva ficha")
    def set_programa(self, nuevo_programa):  
        if isinstance(nuevo_programa, int) and nuevo_programa > 0:
            self.__programa = nuevo_programa
        else:
            print("inserte el programa de formacion")
    def set_trimestre(self, nuevo_trimestre):  
        if isinstance(nuevo_trimestre, int) and nuevo_trimestre > 0:
            self.__trimestre= nuevo_trimestre
        else:
            print("inserte el trimestre actual")
    def mostrar_info(self):
        print(f"\nnombre:{self.__nombre}")
        print(f"\napellidos:{self.__apellidos}")
        print(f"\nid:{self.__id}")
        print(f"\ncentro:{self.__centro}")
        print(f"\nficha:{self.__ficha}")
        print(f"\nprograma:{self.__programa}")
        print(f"\ntrimestre:{self.__trimestre}")
def main():
    aprendiz1 = Aprendiz("hugo","mc pato","001","mtc",3274094,"adso",3)

    aprendiz1.set_centro("Centro Industrial y de Desarrollo Empresarial")
    aprendiz1.set_ficha(2987341)
    aprendiz1.set_programa("Técnico en Sistemas")
    aprendiz1.set_trimestre(7) 
    print("nuevo centro:", aprendiz1.get_centro())
    print("nueva ficha:", aprendiz1.get_ficha())
    print("nuevo programa:", aprendiz1.get_programa())
    print("nueva trimestre:", aprendiz1.get_trimestre())

    aprendiz2 = Aprendiz("paco","mc pato","002","mtc",3274094,"adso",3)

    aprendiz2.set_centro("Centro de Servicios Financieros")
    aprendiz2.set_ficha(2897456)
    aprendiz2.set_programa("Gestión Empresarial")
    aprendiz2.set_trimestre(4) 
    print("nuevo centro:", aprendiz2.get_centro())
    print("nueva ficha:", aprendiz2.get_ficha())
    print("nuevo programa:", aprendiz2.get_programa())
    print("nueva trimestre:", aprendiz2.get_trimestre())

    aprendiz3 = Aprendiz("luis","mc pato","002","mtc",3274094,"adso",3) 
    
    aprendiz3.set_centro("Centro Manofactura Textil y Cuero")
    aprendiz3.set_ficha(3171084)
    aprendiz3.set_programa("Análisis y Desarrollo de Software")
    aprendiz3.set_trimestre(5) 
    print("nuevo centro:", aprendiz3.get_centro())
    print("nueva ficha:", aprendiz3.get_ficha())
    print("nuevo programa:", aprendiz3.get_programa())
    print("nueva trimestre:", aprendiz3.get_trimestre())

if __name__=="__main__":
      main() 