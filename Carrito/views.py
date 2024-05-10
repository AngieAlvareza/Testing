from django.shortcuts import render

# Create your views here.
def Carrito_funcion(request):
    return render(request, 'carritoDeCompras.html')