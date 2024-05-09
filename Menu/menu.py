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
    print("6. para ver los servicios utilizados por el usuario")
    print("7. para ver interacciones usuario con la empresa")
    print("8. para ver servicios especiales para ti")
    print("9. para ver tu historial de productos adquiridos")
    print("10. para ver servicios y productos que adquieren demas usuarios")
    print("11. para volver al menu principal")
    print("*************")

def menu_servicios():
    print("*************")
    print("Ingrese la opción que requiera")
    print("1. para crear un servicio")
    print("2. para ver el catalogo de servicios")
    print("3. para actualizar un servicio")
    print("4. para eliminar un servicio")
    print("5. para volver al menu principal")
    print("*************")

def menu_reportes():
    print("*************")
    print("Ingrese la opción que requiera")
    print("1. para ver la cantidad de productos y servicios que hay en la empresa")
    print("2. para ver los servicios mas solicitados")
    print("3. para ver informes de servicios y productos adquiridos y quienes lo adquieren")
    print("4. para volver al menu principal")
    print("*************")

def menu_ventas():
    print("*************")
    print("Ingrese la opción que requiera")
    print("1. para ver las caracteristicas de los productos y servicios")
    print("2. para ver el registro de ventas totales")
    print("3. para volver al menu principal")
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