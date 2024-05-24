
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('', home, name='home'),  # Home URL
     path('productos/', lista_productos, name='lista_productos'),
    path('hacer_pedido/', hacer_pedido, name='hacer_pedido'),
    path('factura/<int:factura_id>/', factura_detalle, name='factura_detalle'),

    # Add other URLs here
]