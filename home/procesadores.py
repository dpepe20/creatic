from .models import Producto

def mi_ctx(request):
	x = 'Tienda Cluster Creatic 2018'
	context = {'empresa': x}
	return context 

	