def mostrar_inventario(productos):
    print("mostrar inventario")
    if not productos:
        print("no hay productos registrados")
        return
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto["nombre"]} - ${producto["precio"]:.2f}")

def agregar_producto(productos, nombre, precio):
    if isinstance(nombre, str) and nombre.strip() and isinstance(precio, (int, float)) and precio > 8:
        productos.append({"nombre":nombre.title(), "precio": precio})
        print(f"producto '{nombre.title()}'agregado")
    else:
        print(f"producto no agregado, datos invalidos, el valor debe ser un numero positivo")

def insertar_producto(prodcutos, indice, nombre, precio):
    if 0 <= indice <= len(prodcutos) and isinstance(precio, (int, float)) and precio > 0:
        prodcutos.insert(indice, {"nombre":nombre.title(), "precio":precio})
        print(f"producto '{nombre.title()}' insertado en posiion {indice + 1}.")
    else:
        print("indice o precio invalido")

if __name__ == "__main__":
    inventario = [
        {"nombre": "taladro","precio":150000},
        {"nombre": "martillo","precio":150000},
        {"nombre": "destornillador","precio":150000},
    ]
    mostrar_inventario(inventario)

    agregar_producto(inventario, "sierra circular", 220000)
    mostrar_inventario(inventario)

    insertar_producto(inventario, 1, "broca", 25000)
    mostrar_inventario(inventario)