def menu_principal():
    print("*************")
    print("Bienvenido a nuestro menu interactivo de Claro\n en él te presentamos las siguientes opciones")
    print("*************")
    print("Ingrese la opción que requiera")
    print("1. para ir al modulo administrativo de usuarios")
    print("2. para ir al modulo administrativo de servicios")
    print("3. para ir al modulo de reportes")
    print("4. para ir al modulo de ventas")
    print("5. para salir")
    print("*************")

def menu_usuarios():
    print("*************")
    print("Ingrese la opción que requiera")
    print("1. para crear un usuario")
    print("2. para ver la informacion de un usuario")
    print("3. para actualizar a un usuario")
    print("4. para eliminar un usuario")
    print("5. para ver la categoria del usuario")
    print("*************")

def menu_servicios():
    print("*************")
    print("Ingrese la opción que requiera")
    print("1. para crear un servicio")
    print("2. para ver el catalogo de servicios")
    print("3. para actualizar un servicio")
    print("4. para eliminar un servicio")
    print("*************")

def menu_reportes():
    print("*************")
    print("Ingrese la opción que requiera")
    print("1. para ver la cantidad de productos y servicios que hay en la empresa")
    print("*************")

def menu_ventas():
    print("*************")
    print("Ingrese la opción que requiera")
    print("1. para ver el registro de ventas totales")
    print("2. para comprar un servicio")
    print("3. para comprar un producto")
    print("*************")
    
def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("*************")
        return opc
    except Exception:
        print("Valor inválido")
        print("*************")
        return -1