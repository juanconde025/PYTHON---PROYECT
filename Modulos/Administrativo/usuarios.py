def crear_usuario(datos:dict):
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre: ")
    usuario["documento"]=input("Ingrese el documento: ")
    usuario["direccion"]=input("Ingrese la direccion: ")
    try:
        usuario["edad"] = int(input("Ingrese la edad: "))
    except Exception:
        usuario["edad"] = 0
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
    

        

def actualizar_usuario(datos):
    print("")

def eliminar_usuario(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
                datos["usuarios"].pop(i)
                print("Eliminado")
    return datos
        
def categoria_usuario(datos):
    print("")

def servicios_utilizados(datos):
    print("")

def interacciones(datos):
    print("")

def servicios_especiales(datos):
    print("")

def productos_adquiridos(datos):
    print("")    

def servicios_y_productos(datos):
    print("")

def volver(datos):
    print("")