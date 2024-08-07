"""observatorio_formosa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Ipc import views as ipc
from sectorPrivado import views as privado
from observatorio_formosa import utils

urlpatterns = [
    path('admin/', admin.site.urls),
    path('panel',utils.panel, name='panel'),
    path('ipc-division', ipc.ipc_divisiones, name='ipc-division'),
    path('ipc-listado',ipc.listado, name='ipc-listado'),
    path('ipc-panel',ipc.ipc_panel, name='ipc-panel'),
    path('asalariado-panel',privado.privado_panel, name='asalariado-panel'),
    path('asalariado-listado',privado.asalariados_listado, name='asalariado-listado'),
    path('rama-panel',privado.rama_panel, name='rama-panel'),

]
