from django.urls import path
from .views import ListadoItem, RegistrarItem,EditarItem,EliminarItem, ConfigurarReposicionItem, ListarCategorias, Pedido,ListarPedidos, CompletarPedido,prueba, VerPedido
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('listado_items/', login_required(ListadoItem.as_view()) ,name='listar_items'),
    path('registrar_item/', login_required(RegistrarItem.as_view()),name = 'registrar_item'),
    path('actualizar_item/<int:pk>/', login_required(EditarItem.as_view()), name = 'actualizar_item'),
    path('eliminar_item/<int:pk>/',login_required(EliminarItem.as_view()), name='eliminar_item'),
    path('reposicion_item/<int:pk>/', login_required(ConfigurarReposicionItem.as_view()), name='reposicion_item'),
    path('listar_categorias/', login_required(ListarCategorias.as_view()), name = 'listar_categorias'),
    path('visualizar_pedidos/', login_required(ListarPedidos.as_view()) ,name='visualizar_pedidos'),
    path('visualizar_pedidos/<int:id>/', login_required(CompletarPedido) ,name='completar_pedido'),
    path('pedido_proveedor/<int:sucursal>/<int:proveedor>', VerPedido, name= 'pedido_proveedor'),
    path('prueba/', prueba, name='prueba'),
]