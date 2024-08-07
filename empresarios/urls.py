from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_empresa/', views.cadastrar_empresa, name="cadastrar_empresa"),
    path('listar_empresa/', views.listar_empresa, name="listar_empresa"),
]
