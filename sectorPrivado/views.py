from django.shortcuts import render
from sectorPrivado.models import *
from Año.models import Año
from Mes.models import Mes

# Create your views here.

def asalariados_listado(request):
    listado = AsalariadosRegistrados.objects.all()
    context = {
        
        'listado':listado,
        
    }
    return render(request, 'SectorPrivado/asalariado/listado.html', context)

def privado_panel(request):
    listado = AsalariadosRegistrados.objects.all()
    data_actual = AsalariadosRegistrados.objects.filter(año=6).all()
    
    años = Año.objects.all()
    context = {
        'años':años, 
        'data_actual':data_actual       
    }


    if request.method == "POST":
        año = request.POST.get('año')
        if año and año.isdigit():
            data_filtro = AsalariadosRegistrados.objects.filter(año=año).all()
            
            context.update({
                'data_filtro': data_filtro,
                
            })

        else:
            context['error'] = "Debe elegir siempre un año para realizar una comparativa (las tablas son opcionales)"

    return render(request, 'SectorPrivado/asalariado/panel.html', context)


def rama_panel(request):
    
    ramas = RamaActividad.objects.all()
   
    años = Año.objects.all()
    context = {
        'años':años, 
        'ramas':ramas,
        
       
    }

    if request.method == "POST":
        año = request.POST.get('año')
        rama = request.POST.get('tipo_rama')
        if año and año.isdigit() and rama:
            data_filtro = AsalariadosRama.objects.filter(año=año, tipo_rama=rama).all()
            listado = AsalariadosRama.objects.filter(año=año, tipo_rama=rama).all()
            context.update({
                'data_filtro': data_filtro,
                'listado':listado
            })

        else:
            context['error'] = "Debe elegir siempre un año y tipo de rama para obtener datos"

    return render(request, 'SectorPrivado/asalariado/panel-rama.html', context)