from abc import ABC, abstractmethod
class Empleado:
    def __init__(self, nombre: str) -> None:
        self._nombre = None         #Queda el atributo nombre como privado
        self.nombre =nombre  #aqui llamamamos al SETTER automoticamente
    #creamos los GETTER
    @property
    def nombre(self) -> str:
        return self._nombre
    # Tendra acceso seguro del empleado

    @nombre.setter
    def nombre (self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip()
        else:
            raise ValueError("El nombre debe ser de tipo texto")
    def trabajar (self) -> None:
        pass
class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} Esta administrando toda la empresa")

class Desarrollador(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta escribiendo el codigo en PYTHON")

def ejecutar_tarea(empleado: Empleado):
    empleado.trabajar()

def main():
    gerente1 = Gerente("Sebastian Herreria")
    desarrollador1 =Desarrollador("Cristian Valero")
    print("******** === Polimorfismo con Getters === *******")

    ejecutar_tarea(gerente1)
    ejecutar_tarea(desarrollador1)

    print("******** === Poliformismo con SETTERS === ********")

    desarrollador1.nombre = "ñiaño Riñones"
    gerente1.nombre = "chis"
if __name__ == "__main__":
    main()




