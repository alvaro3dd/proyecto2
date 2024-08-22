from django.urls import path
from . import views

app_name = "productos"


urlpatterns = [
    path("", views.index, name="index"),
    path("productocategorias/list", views.productocategoria_list, name="productocategoria_list"),
    #path("cliente/list", views.cliente_list, name="cliente_list"),
]
