from abc import ABC, abstractmethod
class Empleado(ABC):
    def __init__(self, nombre: str) -> None:
        self._nombre = None
        self.nombre = nombre 
    @property
    def nombre(self) -> str:
        return self._nombre 
    @nombre.setter
    def nombre(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip()
        else:
            raise ValueError("el nombre debe ser un texto valido")
    @abstractmethod
    def trabajar(self) -> None:
        pass
class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta realizando administracion de empresa.")
class Desarrollador(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} esta programando los diagramas de clase en poo java.")
def ejecutar_tarea(empleado: Empleado) -> None:
    empleado.trabajar()
def main():
    gerente1 = Gerente("laura Perez")
    desarrollador1 = Desarrollador ("kevin Barreto")
    ejecutar_tarea(gerente1)
    ejecutar_tarea(desarrollador1)
    print("actualizando el nombre del desarrollador")
    desarrollador1._nombre = "Samuel Diaz "
    print(f"el nuevo desarrollador es {desarrollador1.nombre}")
    print("n/************* FIN DEL PROGRAMA EMPLEADOS /*******")
if __name__ == "__main__":
    main()