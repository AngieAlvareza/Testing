from django.shortcuts import render

# Create your views here.
def Boleta_funcion(request):
    return render(request, 'boleta.html')