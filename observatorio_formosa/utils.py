from django.shortcuts import render, redirect
from Año.models import Año
from Ipc.models import Ipc
from sectorPrivado.models import *
from django.db.models import F

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
                intermensual_uno = Ipc.objects.filter(año = request.POST['año']).annotate(intermensual=F('mes_anterior')).values('mes', 'intermensual')
                intermensual_dos = Remuneracion.objects.filter(año = request.POST['año']).annotate(intermensual=F('var_intermensual')).values('mes', 'intermensual')
                
                context.update ({
                    'intermensual_uno':intermensual_uno,
                    'intermensual_dos':intermensual_dos,

                    
                })
        

    return render(request,'panel.html', context)