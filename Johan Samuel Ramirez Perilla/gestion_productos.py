# Gestión de productos
def agregar_producto(lista_productos, nombre):

    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        lista_productos.append(nombre.title())
        print(f"Producto agregado: {nombre.title()}")
    else:
        print("Debe ingresar un nombre de producto válido (2 a 50 caracteres).")


def mostrar_productos(lista_productos):

    if not lista_productos:
        print("No hay productos registrados aún.")
        return
    
    print("Lista de productos:")
    for producto in lista_productos:
        print(f"- {producto}")


def modificar_producto(lista_productos, indice, nuevo_nombre):

    if not isinstance(nuevo_nombre, str) or not (2 <= len(nuevo_nombre) <= 50):
        print("Nombre de producto inválido. Debe tener entre 2 y 50 caracteres.")
        return
    
    if 0 <= indice < len(lista_productos):
        original = lista_productos[indice]
        lista_productos[indice] = nuevo_nombre.title()
        print(f"Producto modificado: {original} → {nuevo_nombre.title()}")
    else:
        print(f"Índice inválido. No existe producto en la posición {indice}")


def eliminar_producto(lista_productos, indice):

    if 0 <= indice < len(lista_productos):
        eliminado = lista_productos.pop(indice)
        print(f"Producto eliminado: {eliminado}")
    else:
        print(f"No se puede eliminar. Índice {indice} fuera de rango.")


def contar_productos(lista_productos):
 
    total = len(lista_productos)
    print(f"Total de productos registrados: {total}")


def ordenar_productos(lista_productos):

    if not lista_productos:
        print("No hay productos para ordenar.")
        return
    
    print("Productos ordenados alfabéticamente:")
    for producto in sorted(lista_productos):
        print(f"- {producto}")


def main():

    productos = ["arroz", "leche", "aceite"]
    
    print("=== SISTEMA DE GESTIÓN DE PRODUCTOS ===")
    print("Productos actuales:")
    mostrar_productos(productos)
    print()
    

    print("Agregamos un nuevo producto: 'Azúcar'")
    agregar_producto(productos, "Azúcar")
    mostrar_productos(productos)
    print()
    
  
    print("Modificamos el producto en posición 1")
    modificar_producto(productos, 1, "Leche entera")
    mostrar_productos(productos)
    print()
    
    
    print("Eliminamos un producto")
    eliminar_producto(productos, 2)
    mostrar_productos(productos)
    print()
  
    contar_productos(productos)
    print()
    
    ordenar_productos(productos)


if __name__ == "__main__":
    main()