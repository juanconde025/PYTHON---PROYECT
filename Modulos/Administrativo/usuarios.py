def crear_usuario(datos:dict):
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre: ")
    usuario["documento"]=input("Ingrese el documento: ")
    usuario["estado"]= ("activo")
    try:
        usuario["edad"] = int(input("Ingrese la edad: "))
    except Exception:
        usuario["edad"] = 0
    try:
        usuario["codigo"] = int(input("Ingrese el codigo: "))
    except Exception:
        usuario["codigo"] = 0
    try:
        usuario["numero telefonico"] = int(input("Ingrese su numero telefonico: "))
    except Exception:
        usuario["numero telefonico"] = ""
    datos["usuarios"].append(usuario)
    print("usuario registrado")
    print(datos)
    return datos

def leer_usuario(datos):
    documento = input("Ingrese el documento del usuario: ")
    for i in datos["usuarios"]:
        if i["documento"] == documento:
            for llave,valor in i.items():
                print(llave,"=", valor)
    

        

def actualizar_usuario(datos:dict):
    
    documento = input("ingrese el documento del usuario para actualizarlo: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            usuario={}
            usuario["nombre"]=input("Ingrese el nombre: ")
            usuario["documento"]=input("Ingrese el documento: ")
            usuario["estado"]= ("activo")
            try:
                usuario["edad"] = int(input("Ingrese la edad: "))
            except Exception:
                usuario["edad"] = 0
            try:
                usuario["codigo"] = int(input("Ingrese el codigo: "))
            except Exception:
                usuario["codigo"] = 0
            try:
                usuario["numero telefonico"] = int(input("Ingrese su numero telefonico: "))
            except Exception:
                usuario["numero telefonico"] = ""
            datos["usuarios"][i].update(usuario)
        return datos



def eliminar_usuario(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
                datos["usuarios"].pop(i)
                print("Eliminado")
    return datos
        
def categoria_usuario(datos):
    datos = dict(datos)
    codigo =input("Ingrese el codigo: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["codigo"] == codigo and datos["usuarios"][i]["codigo"] == ("activo"):
            if codigo == 1 or 2 or 3 or 4 or 5:
                print("Usuario leal")
            elif codigo == 6 or 7 or 8 or 9 or 10:
                print("Usuario nuevo")
        if datos["usuarios"][i]["codigo"] == codigo and datos["usuarios"][i]["codigo"] == ("inactivo"):
            if codigo == 1 or 2 or 3 or 4 or 5:
                print("Usuario regular")
 
            
                


          
        
                     

def servicios_utilizados(datos):
    print("")

from Modulos.Servicios.datos import *
from Modulos.Servicios.servicios import *
RUTA_SERVICIOSYPRODUCTOS = "Modulos/Servicios/serviciosyproductos.json"

def interacciones(datos_servicios):
    

    opc = int(input("Ingrese 1 para comprar un servicio o 2 para comprar un producto"))
    try:
        opc = int(input("Ingrese la edad: "))
    except Exception:
        opc = 0
    finally:
        if opc == 1:
            print("")

            
def servicios_especiales(datos):
    print("")

def productos_adquiridos(datos):
    print("")    

def servicios_y_productos(datos):
    print("")

