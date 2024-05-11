from Modulos.Administrativo.usuarios import *
from Modulos.Ventas.datos import *
from Modulos.Servicios.servicios import *
from Modulos.Servicios.datos import *

RUTA = "Modulos/Administrativo/CRUD.json"
RUTA_SERVICIOS = "Servicios/serviciosyproductos.json"
RUTA_VENTAS = "Ventas/ventas.json"

datos = cargar_datos_ventas(RUTA)
#datos_servicios = cargar_datos_servicios(RUTA_SERVICIOS)

def ventas_totales(datos:dict):
    for i in datos["usuarios"]:
        if "servicios" in i:
            print(i["servicios"])

 