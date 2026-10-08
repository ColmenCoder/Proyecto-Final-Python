print("------------------------------------------------")
print("--* QUINTOTEK| Conectividad y Productividad *--")
print("------------------------------------------------")
print("Sistema de control de productos")
#Autenticacion de usuario
#Usuarios validos
nombre_usuario1 = "may"
contraseña_usuario1 = "admin1"

nombre_usuario2 = "isle"
contraseña_usuario2 = "admin2"
#Menu principal
menu_ppal =["1. Agregar producto.", "\n2. Mostrar productos.", "\n3. Buscar producto.", "\n4. Eliminar producto.", "\n5. Salir."]

#Autenticacion

while True:
    usuario = input("Ingrese su nombre de usuario: ").strip()
    contraseña = input("Ingrese su contraseña: ").strip()
    if usuario == "" or contraseña == "":
        print("Los campos no pueden estar vacios. Intentá de nuevo.")
    elif usuario.lower() == nombre_usuario1 and contraseña.lower() == contraseña_usuario1:
        print("------------------------------------------------")
        print(f"Bienvenid/a {usuario.capitalize()}")
        break
        
    elif usuario.lower() == nombre_usuario2 and contraseña.lower() == contraseña_usuario2:
        print("------------------------------------------------")
        print(f"Bienvenid/a {usuario.capitalize()}")
        break
        
    else:
        print("------------------------------------------------")
        print("Error de autenticación")


#Menú Principal
lista_productos = []
nuevo_producto = []

while True:
    print("------------------------------------------------")
    print("¿Como deseas continuar?")
    print("------------------------------------------------")
    for i in range(len(menu_ppal)):
        print(f"{menu_ppal[i]}")
    opcion = input("\n\nIngresá el numero de la opcion y presiona enter: ").strip()
    print("------------------------------------------------")
   
    match opcion:
        case "":
            print("------------------------------------------------")
            print("Ingresá una opción valida")
        case "1":
            print("------------------------------------------------")
            print("--* Ingreso de productos nuevos *--")
            print("------------------------------------------------")
            nombre_prod = input("Ingrese nombre del producto: ")
            print("Escriba el nombre de la categoría al cual pertenece: \n\n-Cables usb -\n-Adaptadores\n-Carga\n-Periféricos\n-Cables de red\n-Almacenamiento\n-Otros.")
            categoria_prod = input("Ingrese la categoria del producto: ")
            precio_prod = int(input("Ingrese precio del producto: "))
            nuevo_producto = [nombre_prod, categoria_prod, precio_prod]
            lista_productos.append(nuevo_producto)

            print("------------------------------------------------")
            print("Producto ingresado con exito")
            

        case "2":
            print("------------------------------------------------")
            print("--*Productos Ingresados*--: ")
            print("------------------------------------------------")
            for i in range(len(lista_productos)):
                print(f"{i+1}-{lista_productos[i]}")

        case "3":
            encontrado = 0
            print("------------------------------------------------")
            print("--* Buscar productos *--")
            print("------------------------------------------------")
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
        
        case "4":
            print("------------------------------------------------")
            print("--* Eliminar productos *--")
            print("------------------------------------------------")
            posicion = int(input("Ingrese la posicion del producto a eliminar: "))
            posicion = posicion - 1
            lista_productos.pop(posicion)
            print("Producto ELIMINADO con éxito")


        case "5":
            print("------------------------------------------------")
            print("Saliste de nuestro sistema. ")
            print("--* QUINTOTEK | Conectividad y Productivdad*--")
            print("------------------------------------------------")
            break

        case _:
            print("Opcion no valida")

        
           


        
    

  
