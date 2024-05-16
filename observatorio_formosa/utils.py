from django.shortcuts import render, redirect
from Año.models import Año
from Ipc.models import Ipc
from sectorPrivado.models import *

def consulta_personalizada_valores(modelo,valor,mes,año):
    data = modelo.objects.filter(año = año).values(valor,mes)
    return data 

def consulta_personalizada_tabla(modelo):
    data = modelo.objects.all()
    return data 


def panel(request):
    años = Año.objects.all()
    meses = Mes.objects.all()
    context = {
        'años':años,
        'meses': meses
    }

    if request.method == 'POST':
        if request.POST['valor'] == 'intermensual':
            if request.POST['tabla1'] == 'Remuneracion - IPC':
                intermensual_uno = consulta_personalizada_valores(Ipc,'mes_anterior','mes', request.POST['año'])
                lista_modelo_uno= consulta_personalizada_tabla(Ipc)
                intermensual_dos = consulta_personalizada_valores(Remuneracion,'var_intermensual','mes', request.POST['año'])
                lista_modelo_dos= consulta_personalizada_tabla(Remuneracion)
                context.update ({
                    'intermensual_uno':intermensual_uno,
                    'intermensual_dos':intermensual_dos,
                    'lista_uno': lista_modelo_uno,
                    'lista_dos': lista_modelo_dos

                })
        

    return render(request,'panel.html', context)