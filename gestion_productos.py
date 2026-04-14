#Gestion clientes
def agregar_clientes(lista_cliente, nombre):
    #Validar la longitud del cliente
    #verifica que el nombre sea una cadena con longitud entre 2 a 50 carecteres
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        #si valida colocaremos indicando que el cliente fue agregado
        lista_cliente.append(nombre.title())
        print(f"Cliente agregado{nombre.title()}")
    else:
        print("Debe agregar un nombre valido entre 2 a 50 carecteres.")

#Imprimimos todos los clientes registrados en la lista_clientes
def mostrar_cliente(lista_clientes):
    for cliente in lista_clientes:
        print(f"- {cliente}")

def modificar_cliente(lista_clientes, indice, nuevo_nombre):
    if not isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50:
        print("Nombre de cliente invalido debe tener entre 2 y 50 caracteres")
        return
    if 0 <= indice < len(lista_clientes):
    #guardaremos el nombre original de la lista antes de modificarlo en (original)
        original = lista_clientes[indice] 
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"Cliente modificado {original} por -> {nuevo_nombre.title()}")
    else: 
        print(f"No existe ese dato en la lista o indice incorrecto")

def eliminar_cliente(lista_clientes, indice):
    if 0 <= indice < len(lista_clientes):
        eliminado = lista_clientes.pop(indice)
        print(f"Cliente eliminado: {eliminado}")
    else: 
        print("No se puede eliminar un cliente con ese indice fuera de rango")
        
def contar_clientes(lista_clientes):
    print(f"El total de clientes registrados es: {len(lista_clientes)}")
def ordenar_clientes(lista_clientes):
    for cliente in sorted(lista_clientes):
        print(cliente)

def main():
    clientes = ["ana","calos","beatrix"]
    print("Clientes actuales")
    mostrar_cliente(clientes)
    #agregamos un nuevo cliente
    print("Agregamos a cliente: Marcos")
    agregar_clientes(clientes, "Marcos")
    mostrar_cliente(clientes)
    #modificamos un cliente
    modificar_cliente(clientes, 1, "Jhon")
    mostrar_cliente(clientes)
    #eliminar cliente
    print("Eliminar cliente")
    eliminar_cliente(clientes,2)
    mostrar_cliente(clientes)

if __name__ == "__main__":
    main()