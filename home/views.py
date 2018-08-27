from django.shortcuts import render, redirect 
from .forms import *
from .models import *
# Create your views here.

def quienes_somos_view(request):
	nombre = [12,3,45,67,89,436,51]
	#return render(request, 'quienes_somos.html', {'n':nombre})
	return render(request, 'quienes_somos.html', locals())

def contacto_view(request):
	email=""
	subject=""
	text=""
	info_enviado = False
	if request.method=='POST':
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			email  	= formulario.cleaned_data['correo'] 
			subject = formulario.cleaned_data['asunto']
			text 	= formulario.cleaned_data['texto']
			info_enviado = True
			return render(request, 'contacto.html', locals())
		else:
			msg = 'la informacion no es correcta'	
	else: # si es un metodo GET		
		formulario = contacto_form()
	return render(request, 'contacto.html', locals())


def lista_productos_view (request):
	lista = Producto.objects.filter(status=True)
	return render(request, 'lista_productos.html', locals())

def agregar_producto_view (request):
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST, request.FILES)	
		if formulario.is_valid():
			formulario.save()
			return redirect('/lista_productos/')
		else:
			msj = "hay datos no validos"	 
	else:
		formulario = agregar_producto_form()
	return render(request, 'agregar_producto.html', locals())
	
def ver_producto_view(request, id_prod):
	try:
		obj = Producto.objects.get(id = id_prod)
	except:
		print ("Error en la consulta el Producto no existe")
		msj = "Error en la consulta el Producto no existe"
	return render(request, 'ver_producto.html', locals())

def editar_producto_view(request, id_prod):
	obj = Producto.objects.get(id = id_prod)
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST, request.FILES, instance=obj)
		if formulario.is_valid():
			formulario.save()
			return redirect('/lista_productos/')
	formulario = agregar_producto_form(instance=obj)
	return render(request, 'agregar_producto.html', locals())

def eliminar_producto_view (request, id_prod):
	obj = Producto.objects.get(id = id_prod)
	obj.delete()
	return redirect('/lista_productos/')
def desactivar_producto_view (request,id_prod):
	obj = Producto.objects.get(id = id_prod)
	obj.status = False
	obj.save()
	return redirect('/lista_productos/')
