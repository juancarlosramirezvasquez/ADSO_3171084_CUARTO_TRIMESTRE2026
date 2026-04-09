class Cliente: #clase
    def __init__ (self, nombre, apellido, Id, estatura, edad, saldo):
             
             self.__nombre = nombre
             self.__apellido = apellido
             self.__Id = Id
             self.__estatura = estatura
             self.__edad = edad
             self.__saldo = saldo

    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_Id(self):
        return self.__Id
    def get_estatura(self):
        return self.__estatura
    def get_edad(self):
        return self.__edad
    def get_saldo(self):
        return self.__saldo
    def set_estatura(self, nueva_estatura):
         if isinstance(nueva_estatura, (int, float)) and nueva_estatura > 0:
            self.__estatura= nueva_estatura
         else:
            print("la estatura debe ser positiva")
    def set_edad(self, nueva_edad):  
        if isinstance(nueva_edad, int) and nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("La edad debe ser un número positivo")
    def set_saldo(self, nuevo_saldo):  
        if isinstance(nuevo_saldo, int) and nuevo_saldo > 0:
            self.__saldo = nuevo_saldo
        else:
            print("el saldo debe ser un número positivo")

    def mostrar_info(self):
        print(f"\nnombre:{self.__nombre}")
        print(f"\napellido:{self.__apellido}")
        print(f"\nId:{self.__Id}")
        print(f"\nestatura:{self.__estatura}")
        print(f"\nedad:{self.__edad}")
        print(f"\nsaldo:{self.__saldo}")
def main():
     cliente1 = Cliente("pedro","perez","001", 1.65,19,1000)
    
       
       #mostrar informacion inicial
     print("estatura actual:", cliente1.get_estatura())
     #intento de actualizacion no valida 
     cliente1.set_estatura(-18)
     #actualizacion correcta
     cliente1.set_estatura(1.68)
     cliente1.set_edad(20)
     cliente1.set_saldo(2000)
     print("nueva estatura:", cliente1.get_estatura())
     print("nueva edad:", cliente1.get_edad())
     print("nuevo saldo:", cliente1.get_saldo())
   
     cliente2 = Cliente("pedro","perez","001", 1.65,19,1000)
    
       
       #mostrar informacion inicial
     print("estatura actual:", cliente2.get_estatura())
     #intento de actualizacion no valida 
     cliente2.set_estatura(-18)
     #actualizacion correcta
     cliente2.set_estatura(1.80)
     cliente2.set_edad(22)
     cliente2.set_saldo(300000)
     print("nueva estatura:", cliente2.get_estatura())
     print("nueva edad:", cliente2.get_edad())
     print("nuevo saldo:", cliente2.get_saldo())

if __name__=="__main__":
      main() 