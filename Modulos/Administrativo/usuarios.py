def crear_usuario(datos:dict):
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre: ")
    usuario["documento"]=input("Ingrese el documento: ")
    usuario["estado"]= ("activo")
    usuario["servicios"]= input("Ingrese el servicio que desee adquirir:  ")
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
            usuario["estado"]= input("Ingrese estado del usuario: ")
            usuario["servicios"]= input("Ingrese el servicio que desee adquirir:  ")
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
    
    codigo =input("Ingrese el codigo: ")
    
    
    if codigo == "1" or "2" or "3" or "4" or "5":
                print("Usuario leal")
    elif codigo == "6" or "7" or "8" or "9" or "10":
                print("Usuario nuevo")
    


def interacciones_servicios(datos:dict):
    
    try:
        opc = int(input("Ingrese 1 para comprar un servicio: "))
    except Exception:
        opc = 0
    finally:
        if opc == 1:
            documento =input("Ingrese el documento: ")
            for i in range(len(datos["usuarios"])):
                if datos["usuarios"][i]["documento"] == documento:
                    for i in range(len(datos["usuarios"])):
                        servicio={}
                        servicio["servicio adquirido"]=input("Ingrese el servicio: ")
                        
    datos["usuarios"].append(servicio)
    return datos

def interacciones_productos(datos:dict):
    
    try:
        opc = int(input("Ingrese 1 para comprar un producto: "))
    except Exception:
        opc = 0
    finally:
        if opc == 1:
            documento =input("Ingrese el documento: ")
            for i in range(len(datos["usuarios"])):
                if datos["usuarios"][i]["documento"] == documento:
                    for i in range(len(datos["usuarios"])):
                        producto={}
                        producto["producto adquirido"]=input("Ingrese el producto: ")
                        
    datos["usuarios"].append(producto)
    return datos
            


