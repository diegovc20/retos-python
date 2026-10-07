
# EJERCICIO 1


def procesar_solicitudes(solicitudes):
solicitudes = [("S001", "ventas", "alta"), ("S002", "clientes", "media"), ("S003", "inventario", "alta"), ("S004", "ventas", "baja"), ("S005", "clientes", "alta"), ("S006", "inventario", "media"), ("S007", "ventas", "alta")]

solicitud_por_area = {}
prioridad_alta = 0
orden_procesamiento = []

for id_solicitud, area, prioridad in solicitudes:
    orden_procesamiento.append(id_solicitud)
    if area in solicitud_por_area:
        solicitud_por_area[area] = solicitud_por_area[area]+1
    else:
        solicitud_por_area[area]= 1
    if prioridad == "alta": prioridad_alta = prioridad_alta+1

resultado = {"por_area": solicitud_por_area,"prioridad_alta": prioridad_alta,"orden_procesamiento": orden_procesamiento}


print(solicitud_por_area)
print(prioridad_alta)
print(orden_procesamiento)
print(resultado)


if __name__=="__main__":
