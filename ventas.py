from Modulos.Administrativo.usuarios import *
from Modulos.Ventas.datos import *
from Modulos.Servicios.servicios import *
from Modulos.Servicios.datos import *

RUTA = "Modulos/Administrativo/CRUD.json"
RUTA_SERVICIOS = "Servicios/serviciosyproductos.json"
RUTA_VENTAS = "Modulos/Ventas/ventas.json"
RUTA_TENDENCIAS="Modulos/Ventas/tendencias.json"

datos = cargar_datos_ventas(RUTA)
datos_ventas = cargar_datos_ventas(RUTA_VENTAS)


def ventas_totales(datos:dict):
    for i in datos["usuarios"]:
        if "servicios" in i:
            print(i["servicios"])
    
    

def interacciones_servicios(datos:dict,datos_ventas:dict):
    
    nombre= input("Ingrese el nombre del usuario que va a hacer esa compra: ")
    for i in range(len(datos["usuarios"])):
        if nombre == datos["usuarios"][i]["nombre"]:
            servicio={}
            servicio["adquirido"]=input("Ingrese el servicio: ")
            servicio["nombre quien adquirio"]=nombre
            try:
                servicio["cantidad que quiere adquirir"]=int(input("Ingrese la cantidad que va a adquirir de dicho servicio: "))
            except Exception:
                servicio["cantidad que quiere adquirir"]=1
            datos_ventas["ventas"].append(servicio)
        else:
            print("No es un cliente")
    return datos_ventas

def interacciones_productos(datos:dict,datos_ventas:dict):
    
    nombre= input("Ingrese el nombre del usuario que va a hacer esa compra: ")
    for i in range(len(datos["usuarios"])):
        if nombre == datos["usuarios"][i]["nombre"]:
            producto={}
            producto["adquirido"]=input("Ingrese el producto: ")
            producto["nombre quien adquirio"]=nombre
            try:
                producto["cantidad que quiere adquirir"]=int(input("Ingrese la cantidad que va a adquirir de dicho producto: "))
            except Exception:
                producto["cantidad que quiere adquirir"]=1
            datos_ventas["ventas"].append(producto)
        else:
            print("No es un cliente")
    
    return datos_ventas

def producto_tendencia(datos_ventas:dict):
    print("Productos y servicios tendencia:")
    for i in range(len(datos_ventas["ventas"])):
        if datos_ventas["ventas"][i]["cantidad que quiere adquirir"] > 5:
            print (datos_ventas["ventas"][i]["adquirido"])
        


            

datos = guardar_datos_servicios(datos, RUTA_VENTAS)
guardar_datos_ventas(datos_ventas, RUTA_VENTAS)

 