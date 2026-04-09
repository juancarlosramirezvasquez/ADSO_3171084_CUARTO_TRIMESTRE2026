from abc import ABC, abstractmethod
class PersonalMedico(ABC):
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
class Doctor(PersonalMedico):
    def trabajar(self) -> None:
        print(f"{self.nombre} El doctor esta atendiendo pacientes en la consulta.")
class Enfermero(PersonalMedico):
    def trabajar(self) -> None:
        print(f"{self.nombre} El enfermo esta asistiendo a los pacientes.")
class Cirujano(PersonalMedico):
    def trabajar(self) -> None:
        print(f"{self.nombre} El cirujano esta haciendo una cirujia.")
def ejecutar_tarea(Personal: PersonalMedico) -> None:
    Personal.trabajar()
def main():
    doctor1 = Doctor("alejandro benitez")
    enfermero1 = Enfermero ("kevin Barreto")
    cirujano1 = Cirujano("Samuel diaz")
    ejecutar_tarea(doctor1)
    ejecutar_tarea(enfermero1)
    ejecutar_tarea(cirujano1)
    print("actualizando el nombre del doctor")
    doctor1._nombre = "Samuel Diaz "
    print(f"el nuevo docotr es {doctor1.nombre}")
    print("n/************* FIN DEL PROGRAMA PersonalMedico  /*******")

if __name__ == "__main__":
    main()