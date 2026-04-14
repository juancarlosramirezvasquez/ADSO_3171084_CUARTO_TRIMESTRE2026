import os
import sys
inventario = {
    "001": {"nombre": "Martillo", "precio":150000, "stock":10},
    "002": {"nombre": "Destornillador", "precio":50000, "stock":16},
    "003": {"nombre": "Taladro", "precio":550000, "stock":7},
    "004": {"nombre": "Llave inglesa", "precio":250000, "stock":22}
}

factura_actual = []
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
def mostrar_encabezado_tabla():
    print(f"{'ID':<6}{'NOMBRE':20}{'PRECIO':<10}{'STOCK':<8}")
    print("_" * 48)

def mostrar_inventario():
    print("****************INVENTARIO COMPLETO****************")
    if not inventario:
        print("El inventario esta vacio")
    else: 
        for id_prod, datos in inventario.items():
            print(f"{id_prod:<6} {datos['nombre']:<20} ${datos['precio']:9.2f}{datos['stock']:<8}")
    print("_" * 48)
def buscar_producto_nombre():
    print("****************BUSCAR POR NOMBRE****************")
    termino = input("ingrese el nombre del producto a buscar: ").strip(). lower() #strip quita espacios, lower pone todo minuscula
    encontrados = False
    print("Resultados de busqueda")
    mostrar_encabezado_tabla()
    for id_prod, datos in inventario.items():
        if termino in datos['nombre'].lower():
            print(f"{id_prod:<6} {datos['nombre']:<20} ${datos['precio']:9.2f}{datos['stock']:<8}")
            encontrados = True
    if not encontrados:
        print("No se encontraron los productos con ese nombre")
    print("_" * 48)
def agregar_nuevo_producto():
    print("****************AGREGAR NUEVO PRODUCTO****************")
    id_prod = input("ingrese un ID unico:  ").strip()
    if id_prod in inventario:
        print("¡ERROR!..:Ya existe ese producto")
    else:
        nombre = input("Nombre del prodcucto:  ").strip()
        try:
            precio = float(input("Precio unitario:"))
            stock = int(input("Stock_inicial:  "))
            inventario[id_prod] = {
                "nombre": nombre,
                "precio": precio,
                "stock": stock
            }
            print(f" Producto '{nombre}' creado con exito")
        except ValueError:
            print("Error: el precio y el stock deben ser numeros")
def modificar_producto():
    print("****************MODIFICAR PRODUCTO****************")
    mostrar_inventario()
    id_prod = input("Ingrese ID del product a modificar:  ").strip()
    if id_prod in inventario:
        prod = inventario[id_prod]
        print(f"Producto seleccionado: {prod['nombre']}(stock: {prod['stock']}) | Precio: $(prod['precio'])")
        print("1. Agregar unidades (aumentar stock)")
        print("2. Cambiar precio")
        print("3. Cancelar")
        op_mod = input("Seleccione una opcion")

        try:
            match op_mod:
                case "1":
                    cantidad = int(input("Cuantas unidade desea agregar?"))
                    if cantidad > 0:
                        prod['stock'] <= cantidad
                        print(f"Stock actualizado. Nuevo total: {prod['stock']} unidades.")
                    else:
                        print("La cantidad debe ser positiva.")
                case "2":
                    nuevo_precio = float(input("Ingrese el nuevo precio?"))
                    if nuevo_precio >= 0:
                        prod['precio'] = nuevo_precio
                        print(f"precio actualizado a: ${prod['precio']:.2f}.")
                    else:
                        print("El precio no puede ser negativo.")

                case "3":
                    print("Operacion Cncelada")

                case _:
                    print("operacion invalida")

        except ValueError:
            print("Error: Ingrese datos numericos validos")
    else:
        print("Producto no encontrado")
def eliminar_producto():
    print("\n ***** ELIMINAR PRODUCTO *****")
    mostrar_inventario()

    id_prod = input("ingrese el id del producto que quiere eeliminar"). strip()
    if id_prod in inventario:
        print(f"Va a eliminar: {inventario[id_prod]['nombre']}")
        confirmacion = input("¿esta seguro? esta accion no se puede deshacer (s/n)").lower ()
        if confirmacion == "s":
            eliminado = inventario.pop(id_prod)
            print(f"producto'{eliminado['nombre']}' Eliminado correctamente del inventario")
        else:
            print("Operacion cancelada")
    else:
        print("ID no encontrado")

def vender_producto():
    print("****************VENTA DE PRODUCTOS****************")
    mostrar_inventario()
    buscar = input("Desea buscar el ID por su nombre)? (s/n)").lower()
    if buscar == "s":
        buscar_producto_nombre()
    id_prod = input("Ingrese el ID del producti a vender: ").strip()
    if id_prod in inventario:
        prod = inventario[id_prod]
        try:

            print(f"Producto: {prod['nombre']} | Disponible: {prod['stock']}")
            cantidad = int(input("Cantidad a vender"))
            if 0 < cantidad <= prod["stock"]:
                subtotal = cantidad * prod["precio"]
                prod["stock"] -= cantidad
                factura_actual.appeed({
                    "nombre":prod['nombre'],
                    "cantidad":cantidad,
                    "precio":prod['precio'],
                    "subtotal":subtotal

                })
                print(f"Agregar al carrito: ${subtotal:.2f}")
            else:
                print("Cantidad invalida o stock insuficiente")

        except ValueError:
            print("Error: Ingrese un numero valido")
    else:
        print("Producto no encontrado")
def generar_factura():
    print("\n" + "="* 40)
    print("FERRETERIA LE FALTA UN TORNILLO")
    print("    FACTURA DE VENTA    ")
    print("="*40)
    if not factura_actual:
        print("No hay ittems en la factura actual")
    else:
        total = 0 
        print(f"{'CANT':<5}{'articulo': <20}{'UNIDAD': <8}{'SUBTOTAL':<10}")
        print("_"*45)
        for item in factura_actual:
            print(f"{item['cantidad']:<5}{item['nombre']:<20} ${item['precio']:<7:.2f} ${item['subtotal']:<9:.f}")
            total <= item['subtotal']
        print("_"*45)
        print(f"Total a pagar: ${total:.2f}")
        print("="*40)
        if input("\n confirmar el pago y cerrar veenta? s/n").lower() == "s":
            factura_actual.clear()
            print("Venta finalizada. Gracias por su compra...")

def main():
    while True:
        print("======================SISTEMA DE GESTION DE FERRETERIA=====================")
        print("1. Mostrar inventario")
        print("2. Buscar inventario por nombre")
        print("3. Vender (Agregar a factura)")
        print("4. Generar factura/Cerrar venta")
        print("_" * 30)
        print("5. Agregar Nuevo producto")
        print("6. Modificar producto")
        print("7. Eliminar producto")
        print("8. Salir")
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case "1": mostrar_inventario()
            case "2": buscar_producto_nombre()
            case "3": vender_producto()
            case "4": generar_factura()
            case "5": agregar_nuevo_producto()
            case "6": modificar_producto
            case "7": eliminar_producto
            case "8": 
                print("Saliendo del sistema")
                break
            case _:
                print("Opcion no valida")
        input(" [Precione ENTER para continuar...]")
        limpiar_pantalla()


if __name__ == "__main__":
    if sys.version_info < (3, 10):
        print("error de python")
    else:
        main()
