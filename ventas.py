from Modulos.Administrativo.usuarios import *
from Modulos.Ventas.datos import *
from Modulos.Servicios.servicios import *
from Modulos.Servicios.datos import *

RUTA = "Modulos/Administrativo/CRUD.json"
RUTA_SERVICIOS = "Servicios/serviciosyproductos.json"
RUTA_VENTAS = "Modulos/Ventas/ventas.json"

datos = cargar_datos_ventas(RUTA)
datos_ventas = cargar_datos_ventas(RUTA_VENTAS)


def ventas_totales(datos:dict):
    for i in datos["usuarios"]:
        if "servicios" in i:
            print(i["servicios"])
    
    

def interacciones_servicios(datos_ventas:dict):
    
    try:
        opc = int(input("Ingrese 1 para comprar un servicio: "))
    except Exception:
        opc = 0
    finally:
        if opc == 1:
            for i in range(len(datos_ventas["ventas"])):
                servicio={}
                servicio["servicio adquirido"]=input("Ingrese el servicio: ")
                        
    datos_ventas["ventas"].append(servicio)
    return datos_ventas

def interacciones_productos(datos_ventas:dict):
    
    try:
        opc = int(input("Ingrese 1 para comprar un servicio: "))
    except Exception:
        opc = 0
    finally:
        if opc == 1:
            for i in range(len(datos_ventas["ventas"])):
                producto={}
                producto["producto adquirido"]=input("Ingrese el producto: ")
                        
    datos_ventas["ventas"].append(producto)
    return datos_ventas
            

datos = guardar_datos_servicios(datos, RUTA_VENTAS)
guardar_datos_ventas(datos_ventas, RUTA_VENTAS)

 