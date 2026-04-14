import  os
import sys
inventario = {
    "001": {"nombre": "Martillo", "precio":15000,"stock":10},
    "002": {"nombre": "Destornillador", "precio":48000, "stock":7},
    "003": {"nombre": "Taladro", "precio":500000, "stock":4},
    "004": {"nombre": "Llave inglesa", "precio":150000, "stock":5},
}
factura_actual = []

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
def mostrar_encabezado_tabla():
    print(f"{'ID':<6}{'NOMBRE':<20}{'PRECIO':<10}{'STOCK':<8}")
    print("-" * 48)
def mostrar_inventario():
    print("\n****** INVENTARIO COMPLETO ******")
    if not inventario:
        print("El inventario esta vacio")
    else:
        for id_prod, datos in inventario.items():
            print(f"{id_prod:<6} {datos['nombre']:<20} ${datos['precio']:9.2f}{datos['stock']:<8}")
    print("-" * 48)
def buscar_producto_nombre():
    print("\n****** BUSCAR POR NOMBRE ******")
    termino = input("Ingrese el nombre del producto a buscar: ").strip().lower()
    encontrados = False
    print("Resultados de busqueda")
    mostrar_encabezado_tabla()
    for id_prod, datos in inventario.items():
        if termino in datos['nombre'].lower():
            print(f"{id_prod:<6} {datos['nombre']:<20} ${datos['precio']:9.2f}{datos['stock']:<8}")
            encontrados = True
    if not encontrados:
        print("No se encontraron productos con ese nombre")
    print("-" * 48)
def agregar_nuevo_producto():
    print("\n****** AGREGAR NUEVO PRODUCTO ******")
    id_prod = input("Ingrese un ID unico: ").strip()
    if id_prod in inventario:
        print("Error: Ya existe ese ID.")
    else:
        nombre = input("Nombre del producto: ").strip()
        try:
            precio = float(input("precio unitario:"))
            stock = int(input("Stock inicial: "))
            inventario[id_prod] = {
                "nombre": nombre,
                "precio": precio,
                "stock": stock
            }
            print(f" Producto '{nombre}' creado con exito")
        except ValueError:
            print("Error: El precio y stock deben ser numeros")
def modificar_producto():
    print("\n****** MODIFICAR PRODUCTO ******")
    mostrar_inventario()
    id_prod = input("Ingrese el ID del producto a modificar: ").strip()
    if id_prod in inventario:
        prod = inventario[id_prod]
        print(f"\nProducto seleccionado: {prod['nombre']} (stock: {prod['stock']}) | Precio: ${prod['precio']}")
        print("1. Agregar unidades (Aumentar Stock)")
        print("2. Cambiar Precio")
        print("3. Cancelar")
        op_mod = input("Seleccione una opción")
        try:
            match op_mod:
                case "1":
                    cantidad = int(input("Cuantas unidades desea agregar?: "))
                    if cantidad > 0:
                        prod["stock"] += cantidad
                        print(f"stock actualizado. Nuevo total: {prod['stock']} unidades.")
                    else:
                        print("La cantidad debe ser positiva.")
                case "2":
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    if nuevo_precio >= 0:
                        prod['precio'] = nuevo_precio
                        print(f"Precio actualizado a: ${prod['precio']:.2f}")
                    else:
                        print(f"El precio no puede ser negativo.")
                case "3":
                    print("Operacion Cancelada")
                case _:
                    print("Operacion no valida")
        except ValueError:
            print("Error: Ingrese datos numericos validos")
    else:
        print("Producto no encontrado")
def eliminar_producto():
    print("\n****** ELIMINAR PRODUCTO ******")
    mostrar_inventario()
    id_prod = input("Ingrese el id del producto que quiere eliminar").strip()
    if id_prod in inventario:
        print(f"Va a eliminar: {inventario[id_prod]['nombre']}")
        confirmacion = input("¿Esta seguro? esta accion no se puede deshacer (s/n)").lower()
        if confirmacion == "s":
            eliminado = inventario.pop(id_prod)
            print(f"Producto '{eliminado['nombre']}' eliminado correctamente del inventario")
        else:
            print("Operacion cancelada")
    else:
        print("ID no encontrado")

def vender_producto():
    print("\n****** VENTA DE PRODUCTOS ******")
    mostrar_inventario
    buscar = input("Desea buscar el ID por nombre)? (s/n)").lower()
    if buscar == "s":
        buscar_producto_nombre()
    id_prod =  input("Ingrese el ID del producto a vender:" ).strip()
    if id_prod in inventario:
        prod= inventario[id_prod]
        try:
            print(f"Producto: {prod['nombre']} | Disponible: {prod['stock']}")
            cantidad = int(input("Cantidad a vender"))
            if 0 < cantidad <= prod['stock']:
                subtotal = cantidad * prod['precio']
                prod ['stock'] -= cantidad
                factura_actual.append({
                    "nombre":prod['nombre'],
                    "cantidad": cantidad,
                    "precio": prod['precio'],
                    "subtotal": subtotal
                })
                print(f"Agregado al carrito: ${subtotal:.2f}")
            else:
                print("Cantidad invalida o stock insuficiente.")
        except ValueError:
            print("Error: Ingrese un numero valido")
    else:
        print("Producto no encontrado")
def generar_factura():
    print("\n" + "="*40)
    print("FERRETERIA 'LE FALTA UN TORNILLO'")
    print("     FACTURA DE VENTA      ")
    print("="*40)
    if not factura_actual:
        print("No hay items en la factura actual")
    else:
        total = 0
        print(f"{'CANT':<5}{'ARTICULO':<20}{'UNIDAD':<8}{'SUBTOTAL':<10}")
        print("_"*45)
        for item in factura_actual:
            print(f"{item['cantidad']:<5} {item['nombre']:<20} ${item['precio']:<7.2f} ${item['subtotal']:<9.2f}")
            total += item['subtotal'] 
        print("_"*45)
        print(f"Total a pagar: ${total:.2f}")
        print("_"*40)
        if input("\n Confirmar el pago y cerrar venta? s/n").lower() == "s":
            factura_actual.clear()
            print("Venta finalizada. Gracias por su compra...")
def main():
    while True:
        print("\n **** SISTEMA DE GESTION DE FERRETERIA ****")
        print("1. Mostrar inventario completo")
        print("2. Buscar inventario por nombre")
        print("3. Vender (agregar a factura)")
        print("4. Generar factura / cerrar venta")
        print("-" * 30)
        print("5. Agregar nuevo producto")
        print("6. Modificar producto (stock/precio)")
        print("7. Eliminar producto")
        print("8. Salir")


        opcion = input("\n Seleccione una opcion: ")
        match opcion:
            case "1":
                mostrar_inventario()
            case "2":
                buscar_producto_nombre()
            case "3":
                vender_producto()
            case "4":
                generar_factura()
            case "5":
                agregar_nuevo_producto()
            case "6":
                modificar_producto()
            case "7":
                eliminar_producto()
            case "8":
                print("Saliendo del sistema")
                break
            case _:
                print("Opcion no valida")

        input("\n[Presione ENTER para continuar....]")
        limpiar_pantalla()


if __name__ == "__main__":
    if sys.version_info < (3, 10):
        print("Error de python")
    else:
        main()



