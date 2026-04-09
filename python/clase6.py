""" import random
nombre = ["Kelly","Cristian","Nelson","Sra. Peka", "Ñaño","Sebastian"]
nombre_secreto =  random.choise(nombre)

print("=========Adivina al chato=========")
print("Tiene 3 intentos de vida")
vidas = 3
while vidas > 0:
    for nombre in nombre:
        print (nombre)
    intento = input("Ingrese el nombre del CHATO")
    if intento.lower() == nombre_secreto.lower():
        print("CHATO ganaste, Adivinaste el nombre.....")
        break
    else:
        vidas -= 1
        print("ERROR CRITICO, El nombre del CHATO no es. Intentos restantes: ", vidas)
if vidas == 0:
    print("PAILAS, PERDISTE") """
#EJERCICIO DE GESTION DE CLIENTES 
#AGREGAR NUEVOS CLIENTES 
#RECORRER LA LISTA Y MOSTRAR TODOS LOS DATOS
#MODIFICAR  UN NOMBRE EN CASO DE ERROR
#ELIMINAR CLIENTE

#FUNCIONES QUE UTILIZAREMOS
#len() -> que cuente cuantas instancias dentro de la lista
#append() -> añade datos a la lista
#title() -> coloca la primar letra en mayuscula
#pop() -> elimina datos de la lista

#agregar Nuevos clientes
def agregar_cliente(lista_clientes, nombre):
    if isinstance(nombre, str)  and 2 <= len(nombre) <= 50:
        lista_clientes.append(nombre.title())
        print(f"cliente agregado: {nombre.title()}")
    else:
        print("Nombre del cliente invitado debe tener entre 2 a 50 caracteres")
def mostrar_clientes(lista_clientes):
    for cliente in lista_clientes:
        print(f" - {cliente}")
def modificar_cliente(lista_clientes, indice, nuevo_nombre):
    if not isinstance(nuevo_nombre, str) and 2 <= len(nuevo_nombre) <= 50:
        print("Nombre de cliente no valido debe de tener entre 2 a 50 carecteres")
        return
    if 0 <= indice <= len(lista_clientes):
        original = lista_clientes[indice]
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"El cliente {original} fue modificado por : {nuevo_nombre.title()}")
    else:
        print("No existe ese cliente en la lista")

def eliminar_cliente(lista_clientes, indice):
    if 0 <= indice <= len(lista_clientes):
        eliminado = lista_clientes.pop(indice)
        print(f"Cliente eliminado {eliminado}")
    else:
        print("Ese cliente no existe en nuestro sistema")

def main():
    clientes = ["Kelly","Cristian","Nelson","Sra. Peka", "Ñaño","Sebastian"]
    print("Clientes activos")
    mostrar_clientes(clientes)
    agregar_cliente(clientes, "alejandro")
    print("clientes activos mas el nuevo")
    mostrar_clientes(clientes)
    modificar_cliente(clientes,4,"Gabriela")
    mostrar_clientes(clientes)
    eliminar_cliente(clientes, 3)
    mostrar_clientes(clientes)
if __name__ == "__main__":
    main()
