import os
import sys
from datetime import datetime

# Diccionario de empleados: clave = ID del empleado
empleados = {
    "E001": {
        "nombre": "Jose alberto",
        "edad": 32,
        "cargo": "Vendedor",
        "departamento": "Ventas",
        "salario": 1800000,
        "fecha_ingreso": "2023-01-15",
        "telefono": "3001234567",
        "email": "juan.perez@empresa.com",
        "activo": True
    },
    "E002": {
        "nombre": "Yadira mejia",
        "edad": 28,
        "cargo": "Contadora",
        "departamento": "Finanzas",
        "salario": 2500000,
        "fecha_ingreso": "2022-06-01",
        "telefono": "3109876543",
        "email": "maria.lopez@empresa.com",
        "activo": True
    },
    "E003": {
        "nombre": "Carlos Cardenas",
        "edad": 45,
        "cargo": "Gerente General",
        "departamento": "Dirección",
        "salario": 4500000,
        "fecha_ingreso": "2020-03-10",
        "telefono": "3205557788",
        "email": "carlos.ramirez@empresa.com",
        "activo": True
    }
}

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_encabezado_tabla():
    print(f"{'ID':<6} {'NOMBRE':<25} {'CARGO':<18} {'DEPARTAMENTO':<15} {'SALARIO':<12} {'EDAD':<5} {'ACTIVO':<6}")
    print("-" * 95)

def mostrar_empleados():
    print("**************** LISTA DE EMPLEADOS ****************")
    if not empleados:
        print("No hay empleados registrados.")
    else:
        mostrar_encabezado_tabla()
        for id_emp, datos in empleados.items():
            estado = "Sí" if datos['activo'] else "No"
            print(f"{id_emp:<6} {datos['nombre']:<25} {datos['cargo']:<18} "
                  f"{datos['departamento']:<15} ${datos['salario']:>10,.0f} "
                  f"{datos['edad']:<5} {estado:<6}")
    print("-" * 95)

def buscar_empleado_nombre():
    print("**************** BUSCAR EMPLEADO POR NOMBRE ****************")
    termino = input("Ingrese el nombre o parte del nombre a buscar: ").strip().lower()
    encontrados = False
    print("\nResultados de búsqueda:")
    mostrar_encabezado_tabla()
    for id_emp, datos in empleados.items():
        if termino in datos['nombre'].lower():
            estado = "Sí" if datos['activo'] else "No"
            print(f"{id_emp:<6} {datos['nombre']:<25} {datos['cargo']:<18} "
                  f"{datos['departamento']:<15} ${datos['salario']:>10,.0f} "
                  f"{datos['edad']:<5} {estado:<6}")
            encontrados = True
    if not encontrados:
        print("No se encontraron empleados con ese nombre.")
    print("-" * 95)

def agregar_nuevo_empleado():
    print("**************** AGREGAR NUEVO EMPLEADO ****************")
    id_emp = input("Ingrese un ID único (ej: E004): ").strip().upper()
    if id_emp in empleados:
        print("¡ERROR! Ya existe un empleado con ese ID.")
        return

    nombre = input("Nombre completo: ").strip()
    try:
        edad = int(input("Edad: "))
        cargo = input("Cargo: ").strip()
        departamento = input("Departamento: ").strip()
        salario = float(input("Salario mensual: "))
        telefono = input("Teléfono: ").strip()
        email = input("Email: ").strip()
        fecha_ingreso = input("Fecha de ingreso (YYYY-MM-DD) o presione Enter para hoy: ").strip()

        if not fecha_ingreso:
            fecha_ingreso = datetime.now().strftime("%Y-%m-%d")

        empleados[id_emp] = {
            "nombre": nombre,
            "edad": edad,
            "cargo": cargo,
            "departamento": departamento,
            "salario": salario,
            "fecha_ingreso": fecha_ingreso,
            "telefono": telefono,
            "email": email,
            "activo": True
        }
        print(f" Empleado '{nombre}' agregado exitosamente con ID {id_emp}")
    except ValueError:
        print("Error: La edad y el salario deben ser números válidos.")

def modificar_empleado():
    print("**************** MODIFICAR EMPLEADO ****************")
    mostrar_empleados()
    id_emp = input("Ingrese el ID del empleado a modificar: ").strip().upper()

    if id_emp in empleados:
        emp = empleados[id_emp]
        print(f"\nEmpleado seleccionado: {emp['nombre']} - {emp['cargo']}")
        print("\n¿Qué desea modificar?")
        print("1. Nombre")
        print("2. Edad")
        print("3. Cargo")
        print("4. Departamento")
        print("5. Salario")
        print("6. Teléfono")
        print("7. Email")
        print("8. Estado (Activo/Inactivo)")
        print("9. Cancelar")

        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == "1":
                emp['nombre'] = input("Nuevo nombre: ").strip()
            elif opcion == "2":
                emp['edad'] = int(input("Nueva edad: "))
            elif opcion == "3":
                emp['cargo'] = input("Nuevo cargo: ").strip()
            elif opcion == "4":
                emp['departamento'] = input("Nuevo departamento: ").strip()
            elif opcion == "5":
                emp['salario'] = float(input("Nuevo salario: "))
            elif opcion == "6":
                emp['telefono'] = input("Nuevo teléfono: ").strip()
            elif opcion == "7":
                emp['email'] = input("Nuevo email: ").strip()
            elif opcion == "8":
                estado = input("¿Está activo? (s/n): ").lower()
                emp['activo'] = estado == "s"
            elif opcion == "9":
                print("Operación cancelada.")
                return
            else:
                print("Opción inválida.")
                return

            print(" Empleado modificado correctamente.")
        except ValueError:
            print("Error: Ingrese datos numéricos válidos.")
    else:
        print("Empleado no encontrado.")

def eliminar_empleado():
    print("**************** ELIMINAR EMPLEADO ****************")
    mostrar_empleados()
    id_emp = input("Ingrese el ID del empleado a eliminar: ").strip().upper()

    if id_emp in empleados:
        emp = empleados[id_emp]
        print(f"Va a eliminar: {emp['nombre']} - {emp['cargo']}")
        confirmacion = input("¿Está seguro? Esta acción no se puede deshacer (s/n): ").lower()
        if confirmacion == "s":
            eliminado = empleados.pop(id_emp)
            print(f" Empleado '{eliminado['nombre']}' eliminado correctamente.")
        else:
            print("Operación cancelada.")
    else:
        print("ID de empleado no encontrado.")

def main():
    while True:
        print("\n" + "="*80)
        print("          SISTEMA DE GESTIÓN DE EMPLEADOS")
        print("="*80)
        print("1. Mostrar todos los empleados")
        print("2. Buscar empleado por nombre")
        print("3. Agregar nuevo empleado")
        print("4. Modificar empleado")
        print("5. Eliminar empleado")
        print("6. Salir")
        print("-" * 50)

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                mostrar_empleados()
            case "2":
                buscar_empleado_nombre()
            case "3":
                agregar_nuevo_empleado()
            case "4":
                modificar_empleado()
            case "5":
                eliminar_empleado()
            case "6":
                print("Saliendo del sistema... ¡Hasta pronto!")
                break
            case _:
                print("Opción no válida.")

        input("\nPresione ENTER para continuar...")
        limpiar_pantalla()


if __name__ == "__main__":
    if sys.version_info < (3, 10):
        print("Error de python")
    else:
        main()