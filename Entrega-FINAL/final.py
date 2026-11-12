import modulos

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
menu_ppal =["1. Agregar producto.", "\n2. Mostrar producto.", "\n3. Buscar producto.", "\n4. Eliminar producto.", "\n5. Salir."]

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
lista_productos = modulos.cargar_productos()


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
            modulos.agregar_producto(lista_productos)
            modulos.guardar_productos(lista_productos)

        case "2":
            print("------------------------------------------------")
            print("--*Productos Ingresados*--: ")
            print("------------------------------------------------")
            modulos.mostrar_producto(lista_productos)
        case "3":
            print("------------------------------------------------")
            print("--* Buscar productos *--")
            print("------------------------------------------------")
            modulos.buscar_producto(lista_productos)
        case "4":
            print("------------------------------------------------")
            print("--* Eliminar productos *--")
            print("------------------------------------------------")
            modulos.eliminar_producto(lista_productos)
            modulos.guardar_productos(lista_productos)

        case "5":
            print("------------------------------------------------")
            print("Saliste de nuestro sistema. ")
            print("--* QUINTOTEK | Conectividad y Productivdad*--")
            print("------------------------------------------------")
            break
        case _:
            print("Opcion no valida")

        
           


        
    

  
