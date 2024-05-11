from ..Administrativo.usuarios import *
from ...Menu.datos import *
from ..Servicios.servicios import *
from ..Servicios.datos import *

RUTA = "../Administrativo/CRUD.json"
RUTA_SERVICIOS = "../Servicios/serviciosyproductos.json"

datos = cargar_datos(RUTA)
datos_servicios = cargar_datos_servicios(RUTA_SERVICIOS)

def ventas_totales(datos:dict):
    
