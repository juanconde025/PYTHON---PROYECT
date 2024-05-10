def crear_servicio(datos_servicios):
    servicio={}
    servicio["nombre"]=input("Ingrese el nombre: ")
    servicio["caracteristicas"]=input("Ingrese las caracteristicas: ")
    try:
        servicio["precio"] = int(input("Ingrese el precio: "))
    except Exception:
        servicio["precio"] = 0
    
    datos_servicios["servicios"].append(servicio)
    print("servicio registrado")
    print(datos_servicios)
    return datos_servicios
    
def catalogo_servicios(datos_servicios):
    for i in datos_servicios["usuarios"]:
        for llave,valor in i.items():
            print(llave,"=", valor)

def actualizar_servicio():
    