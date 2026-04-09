"""
1. Ingresar nuevos productos
2. Insertar productos
3. Eliminar productos agorados
4. Ordena precios por nombre y precio
5.. Invertir orden de presentacion de los prodcutos
Requisitos del sistema
    -lista debe de tener nombre y precio
    -Validacion de entradas
"""
def mostrar_inventario(productos):
    print ("Inventario de sistema")
    if not productos:
        print("No hoy productos registrados")
        return
    for i, productos in enumerate(productos, start = 1):
        print(f"{i}. {productos['nombre']} - $ {productos['precio']:.2f}")
        print(f"{i}. $ {productos['precio']:.2f} - {productos['nombre']} ")

def main():
    invetario =  [
        {"nombre" : "taladro", "precio": 150000},
        {"nombre" : "martillo", "precio":14000},
        {"nombre" : "destornillador", "precio": 15000}

    ]
    mostrar_inventario(invetario)
if __name__ == "__main__":
    main()