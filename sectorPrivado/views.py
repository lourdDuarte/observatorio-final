from django.shortcuts import render
from sectorPrivado.models import *
from Año.models import Año
from Mes.models import Mes

# Create your views here.
def privado_panel(request):
    listado = AsalariadosRegistrados.objects.all()
   
    años = Año.objects.all()
    context = {
        'años':años, 
        'listado':listado,
       
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