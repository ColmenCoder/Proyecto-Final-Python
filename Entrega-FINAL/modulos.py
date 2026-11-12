import json

def agregar_producto (lista_productos):
    nombre_prod = input("Ingrese nombre del producto: ")
    print("Escriba el nombre de la categoría al cual pertenece: \n\n-Cables usb -\n-Adaptadores\n-Carga\n-Periféricos\n-Cables de red\n-Almacenamiento\n-Otros.")
    categoria_prod = input("Ingrese la categoria del producto: ")
    precio_prod = int(input("Ingrese precio del producto: "))
    nuevo_producto = [nombre_prod, categoria_prod, precio_prod]
    lista_productos.append(nuevo_producto)

def mostrar_producto(lista_productos):
    for i in range(len(lista_productos)):
        print(f"{i+1}-{lista_productos[i]}")


def buscar_producto(lista_productos):
    encontrado = 0
    buscar_prod = input("Ingrese el producto a buscar: ")
    for producto in (lista_productos):
        if producto [0]== buscar_prod:
            encontrado = encontrado + 1
            print(f"Producto {buscar_prod} ENCONTRADO")
            break
        print("Buscando...")
                
    if encontrado == 0:
        print(f"Producto {buscar_prod} NO ENCONTRADO")
            
    print("Fin de la búsqueda.")
            
def eliminar_producto(lista_productos):
    posicion = int(input("Ingrese la posicion del producto a eliminar: "))
    posicion = posicion - 1
    lista_productos.pop(posicion)
    print("Producto ELIMINADO con éxito")

def guardar_productos(lista_productos):
    with open("productos.json", "w") as archivo:
        json.dump(lista_productos, archivo)

def cargar_productos():
    try:
        with open("productos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
