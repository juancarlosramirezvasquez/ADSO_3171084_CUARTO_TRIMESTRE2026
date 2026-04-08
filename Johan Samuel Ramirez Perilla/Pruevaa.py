class Vehiculo: #Clae padre
    

    def mover (seft): #Metodo
        print("El vehiculo se esta moviendo")


class Carro(Vehiculo): #Clase hija
    pass #Ni atributos ni metodos (vacia)

#=============================================================

def main():
    print("CLASE PADRE Y SU METODO")

    Vehiculo1 = Vehiculo()
    Vehiculo1.mover() #Invoca al metodo mover() de la clase padre

    print("Utilizaremos el metodo mover() de la clase padre en la clase HIJO")
    carro1 = Carro()
    carro1.mover()
    
if __name__ == "__main__":
    main()

    v=Vehiculo()
    c=Carro()

    print("vehiculo")
    v.mover()

    print("/ncarro (herda de vehiculo)")
    c.mover()
