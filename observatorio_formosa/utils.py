def consulta_personalizada(modelo,valor,año):
    data = modelo.objects.filter(anio_id = año).values()
    return data 