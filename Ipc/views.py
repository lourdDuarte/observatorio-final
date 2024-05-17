from django.shortcuts import render, redirect
from Año.models import Año
from Mes.models import Mes
from Ipc.models import Ipc
from TipoValor.models import TipoValor
from IpcTipoDivision.models import TipoDivision
from IpcDivision.models import IpcDivision
from sectorPrivado.models import *
from django.contrib import messages
from observatorio_formosa.utils import *
from django.db.models import F
# Create your views here.
def add(request):

    #obtener datos para las fk
    años = Año.objects.all()
    meses = Mes.objects.all()
    valores = TipoValor.objects.all()
    tipo_division = TipoDivision.objects.all()

    #retornar contexto para la carga de datos fk
    context = {
        'años':años, 
        'meses':meses,
        'valores':valores,
        'tipo_division':tipo_division

    }

    if request.method == 'POST':
        año = Año.objects.get(pk=request.POST['año'])
        mes = Mes.objects.get(pk=request.POST['mes'])
        tipo_valor = TipoValor.objects.get(pk=request.POST['tipo_valor'])
        mes_anterior = request.POST['mes_anterior']
        mes_año_anterior = request.POST['mes_año_anterior']
        dic_mes_anterior = request.POST['dic_mes_anterior']
        var_mensual = request.POST['var_mensual']
        tipo_division = TipoDivision.objects.get(pk=request.POST['tipo_division'])
        valor_mensual = request.POST['valor_mensual']
        valor_interanual = request.POST['valor_interanual']

        #almacenamiento de datos
        ipc = Ipc.objects.create(
            año = año, 
            mes = mes, 
            tipo_valor = tipo_valor,
            mes_anterior = mes_anterior,
            mes_año_anterior = mes_año_anterior,
            dic_mes_anterior = dic_mes_anterior,
            var_mensual = var_mensual
            )
        
        

        ipc_division = IpcDivision.objects.create(
            ipc = ipc,
            tipo_division = tipo_division,
            valor_mensual = valor_mensual,
            valor_interanual = valor_interanual
        )

        messages.success(request, '¡Dato almacenado con exito!')  # Define el mensaje de éxito
        return redirect('ipc-guardar')



    return render(request, 'ipc/add.html', context)


def listado(request):
    ipc = IpcDivision.objects.select_related('ipc').all()
    context = {'ipc':ipc}

    return render(request,'ipc/listado.html',context)


def ipc_panel(request):
    meses = Mes.objects.all()
    años = Año.objects.all()
    interanual = Ipc.objects.filter(año='2').values('mes_anterior', 'mes')
    intermensual = Ipc.objects.filter(año='2').values('mes_año_anterior', 'mes')

    

    context = {
        'meses':meses,
        'años':años,
        'interanual': interanual,
        'intermensual': intermensual
        
    }

    if request.method == "POST":
       
        if request.POST['año']:
            interanual_filtro = Ipc.objects.filter(año=request.POST['año']).values('mes_anterior', 'mes')
            intermensual_filtro = Ipc.objects.filter(año=request.POST['año']).values('mes_año_anterior', 'mes')
            context.update({
                'interanual_filtro': interanual_filtro,
                'intermensual_filtro': intermensual_filtro,
                
            })
            
            if request.POST['tabla']:
                if request.POST['tabla'] == "Remuneracion":
                
                    intermensual_tabla = Remuneracion.objects.filter(año = request.POST['año']).annotate(intermensual=F('var_intermensual')).values('mes', 'intermensual')
                    interanual_tabla = Remuneracion.objects.filter(año = request.POST['año']).annotate(interanual=F('var_interanual')).values('mes', 'interanual')
                    
                    context.update({
                    'intermensual_tabla': intermensual_tabla,
                    'interanual_tabla': interanual_tabla
                    })
                if request.POST['tabla'] == "Asalariados":
                
                    intermensual_tabla = AsalariadosRegistrados.objects.filter(año = request.POST['año']).annotate(intermensual=F('var_intermensual')).values('mes', 'intermensual')
                    interanual_tabla = AsalariadosRegistrados.objects.filter(año = request.POST['año']).annotate(interanual=F('var_interanual')).values('mes', 'interanual')
                    
                    context.update({
                    'intermensual_tabla': intermensual_tabla,
                    'interanual_tabla': interanual_tabla
                    })
        else:
            pass
    return render(request,'ipc/panel.html', context)