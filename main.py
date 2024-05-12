from Menu.datos import *
from Menu.menu import *
from Modulos.Administrativo.usuarios import *

from Modulos.Servicios.datos import *
from Modulos.Servicios.servicios import *

from ventas import *

from registros import *


RUTA = "Modulos/Administrativo/CRUD.json"
RUTA_SERVICIOS = "Modulos/Servicios/serviciosyproductos.json"
RUTA_REGISTROS = "registros.txt"

datos_servicios = cargar_datos(RUTA_SERVICIOS)
datos_servicios = cargar_datos(RUTA_SERVICIOS)
datos = cargar_datos(RUTA)



while True:
    menu_principal()
    opc = pedir_opcion()
    
    if opc == 1:
        print(menu_usuarios())
        opc = pedir_opcion()
        if opc == 1:
            datos = crear_usuario(datos)
        elif opc == 2:
            datos = leer_usuario(datos)
        elif opc == 3:
            datos = actualizar_usuario(datos)
        elif opc == 4:
            datos = eliminar_usuario(datos)
        elif opc == 5:
            datos= categoria_usuario(datos)
        elif opc == 6:
            datos = interacciones_productos(datos)
        elif opc == 7:
            datos = interacciones_servicios(datos)
           

    elif opc == 2:
        
        print(menu_servicios())
        opc = pedir_opcion()
        if opc == 1:
           datos_servicios = crear_servicio(datos_servicios)
           datos_servicios = crear_producto(datos_servicios)
        elif opc == 2:
           catalogo_servicios(datos_servicios)
        elif opc == 3:
           datos_servicios = actualizar_servicio(datos_servicios)
           datos_servicios = actualizar_producto(datos_servicios)
        elif opc == 4:
           datos_servicios = eliminar_servicio(datos_servicios)
           datos_servicios = eliminar_producto(datos_servicios)
            
    elif opc == 3:
        print(menu_reportes())
        opc = pedir_opcion()
        if opc == 1: 
         cant_serv(datos_servicios)
         cant_product(datos_servicios)

    elif opc == 4:
        print(menu_ventas())
        opc = pedir_opcion()
        if opc == 1:
            ventas_totales(datos)

    elif opc == 5:
        print("Salió!!")
        break

    registrar_excepcion(Exception)
    
    guardar_datos(datos, RUTA)
    guardar_datos_servicios(datos_servicios, RUTA_SERVICIOS)