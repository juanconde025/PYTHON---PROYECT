from Menu.datos import *
from Menu.menu import *
from Modulos.Administrativo.usuarios import *



RUTA = "Modulos/Administrativo/CRUD.json"
RUTA_SERVICIOS = "Modulos/Servicios/serviciosyproductos.json"




while True:
    menu_principal()
    opc = pedir_opcion()
    datos = cargar_datos(RUTA)
    if opc == 1:
        print(menu_usuarios())
        opc = pedir_opcion()
        if opc == 1:
            datos = crear_usuario(datos)
        elif opc == 2:
            leer_usuario(datos)
        elif opc == 4:
            datos = eliminar_usuario(datos)
    elif opc == 2:
        datos = cargar_datos(RUTA_SERVICIOS)
        print(menu_servicios())
        opc = pedir_opcion()


    elif opc == 3:
        print(menu_reportes())
        opc = pedir_opcion()

    elif opc == 4:
        print(menu_ventas())
        opc = pedir_opcion()

    elif opc == 5:
        print("Salió!!")
        break

    guardar_datos(datos, RUTA)