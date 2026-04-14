import os
import sys
from datetime import datetime

estudiantes = {
    "101": {"nombre": "Emily Muñoz", "edad": 4, "grupo": "Párvulos", "presente": False, "acudiente": "Yazmin.G"},
    "102": {"nombre": "Iber Ortega", "edad": 5, "grupo": "Pre-jardín", "presente": False, "acudiente": "Surania.O"},
    "103": {"nombre": "Evan Lee", "edad": 3, "grupo": "Caminadores", "presente": False, "acudiente": "Ana M.L"},
}

bitacora_asistencia = [] 

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_encabezado():
    print(f"{'ID':<6}{'ESTUDIANTE':<20}{'GRUPO':<15}{'ESTADO':<10}")
    print("-" * 55)

def mostrar_lista_completa():
    print("\n****** LISTADO GENERAL DE ESTUDIANTES ******")
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        mostrar_encabezado()
        for id_est, d in estudiantes.items():
            estado = "PRESENTE" if d['presente'] else " AUSENTE"
            print(f"{id_est:<6} {d['nombre']:<20} {d['grupo']:<15} {estado:<10}")
    print("-" * 55)

def registrar_entrada():
    print("\n****** REGISTRAR ENTRADA  ******")
    id_est = input("Ingrese el ID del estudiante: ").strip()
    if id_est in estudiantes:
        est = estudiantes[id_est]
        if est['presente']:
            print(f"¡Atención! {est['nombre']} ya marcó entrada.")
        else:
            hora = datetime.now().strftime("%H:%M:%S")
            est['presente'] = True
            bitacora_asistencia.append({"id": id_est, "nombre": est['nombre'], "evento": "Entrada", "hora": hora})
            print(f"Entrada registrada para {est['nombre']} a las {hora}.")
    else:
        print("Estudiante no encontrado.")


def registrar_salida():
    print("\n****** REGISTRAR SALIDA  ******")
    id_est = input("Ingrese ID del estudiante que se retira: ").strip()
    if id_est in estudiantes:
        est = estudiantes[id_est]
        if not est['presente']:
            print(f"Error: {est['nombre']} no ha ingresado hoy.")
        else:
            autorizado = input(f"¿Quién retira al niño? (Autorizado: {est['acudiente']}): ").strip()
            hora = datetime.now().strftime("%H:%M:%S")
            est['presente'] = False
            bitacora_asistencia.append({"id": id_est, "nombre": est['nombre'], "evento": f"Salida (Retira: {autorizado})", "hora": hora})
            print(f"Salida confirmada para {est['nombre']}. Retirado por: {autorizado} a las {hora}.")
    else:
        print("ID no válido.")


def reporte_inasistencia():
    print("\n****** REPORTE DE NIÑOS AUSENTES ******")
    ausentes = [d['nombre'] for d in estudiantes.values() if not d['presente']]
    if not ausentes:
        print("¡Excelente! Asistencia completa hoy.")
    else:
        print("Los siguientes estudiantes no han llegado:")
        for nombre in ausentes:
            print(f"- {nombre}")
    print("-" * 35)

def agregar_estudiante():
    print("\n****** MATRICULAR NUEVO ESTUDIANTE ******")
    id_est = input("Asigne un ID: ").strip()
    if id_est in estudiantes:
        print("El ID ya pertenece a otro estudiante.")
    else:
        try:
            nombre = input("Nombre completo: ").strip()
            edad = int(input("Edad: "))
            grupo = input("Grupo (Párvulos/Jardín/etc): ").strip()
            acudiente = input("Nombre del acudiente principal: ").strip()
            
            estudiantes[id_est] = {
                "nombre": nombre, "edad": edad, "grupo": grupo, 
                "presente": False, "acudiente": acudiente
            }
            print(f"Estudiante {nombre} registrado exitosamente.")
        except ValueError:
            print("Error: La edad debe ser un número.")

def ver_bitacora():
    print("\n****** BITÁCORA DE MOVIMIENTOS DEL DÍA ******")
    if not bitacora_asistencia:
        print("No hay movimientos registrados hoy.")
    else:
        print(f"{'HORA':<10}{'ESTUDIANTE':<20}{'EVENTO'}")
        for reg in bitacora_asistencia:
            print(f"{reg['hora']:<10}{reg['nombre']:<20}{reg['evento']}")

def main():
    while True:
        print("\n--- SISTEMA DE ASISTENCIA JARDÍN INFANTIL 'PEQUEÑOS GENIOS' ---")
        print("1. Ver lista de estudiantes y estado")
        print("2. Registrar Entrada (Check-in)")
        print("3. Registrar Salida (Retiro de niño)")
        print("4. Ver reporte de inasistencias")
        print("-" * 30)
        print("5. Matricular nuevo estudiante")
        print("6. Ver bitácora de movimientos (Log)")
        print("7. Salir")

        opcion = input("\nSeleccione una opción: ")
        
        match opcion:
            case "1": mostrar_lista_completa()
            case "2": registrar_entrada()
            case "3": registrar_salida()
            case "4": reporte_inasistencia()
            case "5": agregar_estudiante()
            case "6": ver_bitacora()
            case "7":
                print("Cerrando sistema escolar...")

                break
            case _:
                print("Opción no válida.")

        input("\n[Presione ENTER para continuar...]")
        limpiar_pantalla()

if __name__ == "__main__":
    if sys.version_info < (3, 10):
        print("ERROR DE PYTHON.")
    else:
        main()