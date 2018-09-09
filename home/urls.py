from django.urls import path 
from .views import *
urlpatterns = [
	path('', inicio_view, name='inicio'),
	path('quienes_somos/', quienes_somos_view, name='quienes_somos'),
	path('contactenos/', contacto_view, name='contacto'),
	path('lista_productos/', lista_productos_view, name = 'lista_productos'),
	path('agregar_producto/', agregar_producto_view, name = 'agregar_producto'),
	path('ver_producto/<int:id_prod>/', ver_producto_view, name = 'ver_producto'),
	path('editar_producto/<int:id_prod>/', editar_producto_view, name = 'editar_producto'),
	path('eliminar_producto/<int:id_prod>/', eliminar_producto_view, name = 'eliminar_producto'),
	path('desactivar_producto/<int:id_prod>/', desactivar_producto_view, name = 'desactivar_producto'),
	path('login/', login_view, name='login'),
	path('logout/', logout_view, name='logout'),
	path('register/', register_view, name='register'),
	path('servicio_web/', servicio_web_view, name='servicio_web'),

	path('nuevo_perfil/', nuevo_perfil_view, name='nuevo_perfil'),
	
	
	path('about/', about_view.as_view(), name='about'),
	path('listar_marca/', listar_marca_view.as_view(), name='listar_marca'),
	path('ver_marca/<int:pk>/', ver_marca_view.as_view(), name='ver_marca'),
	path('agregar_marca/', agregar_marca_view.as_view(), name='agregar_marca'),
	path('editar_marca/<int:pk>/', editar_marca_view.as_view(), name='editar_marca'),
	path('eliminar_marca/<int:pk>/', eliminar_marca_view.as_view(), name='eliminar_marca'),


]  