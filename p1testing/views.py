from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def IndexView(request):
    #Página principal
    #return HttpResponse("Hola mundo")
    return render(request, "index.html")

def LoginView(request):
    #Página principal
    #return HttpResponse("Hola mundo")
    return render(request, "login.html")

def NuevaCompraView(request):
    #Página principal
    #return HttpResponse("Hola mundo")
    return render(request, "nuevacompra.html")

def PrincipalView(request):
    #Página principal
    #return HttpResponse("Hola mundo")
    return render(request, "principal.html")

def ProductosView(request):
    #Página principal
    #return HttpResponse("Hola mundo")
    return render(request, "productos.html")

def RegistroView(request):
    #Página principal
    #return HttpResponse("Hola mundo")
    return render(request, "registro.html")

def PerfilView(request):
    #Página principal
    #return HttpResponse("Hola mundo")
    return render(request, "perfil.html")

def CompraView(request):
    #Página principal
    #return HttpResponse("Hola mundo")
    return render(request, "compra.html")

# def loginView(request):
#     #Página principal
#     #return HttpResponse("Hola mundo")
#     return render(request, "login.html")
    

# def loginView(request):
#     #Página principal
#     #return HttpResponse("Hola mundo")
#     return render(request, "login.html")
