# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Abastecimiento, Factura, DetalleFactura, Proveedor
from .forms import PedidoForm
from django.utils import timezone


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirigir a la página de inicio u otra página deseada
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_productos')  # Redirigir a la página de inicio u otra página deseada
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def home(request):
    return render(request, 'myapp/home.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'myapp/lista_productos.html', {'productos': productos})

@login_required
def hacer_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            proveedor = form.cleaned_data['proveedor']
            productos = form.cleaned_data['productos']
            cantidades = form.cleaned_data['cantidades']
            total = 0
            factura = Factura.objects.create(proveedor=proveedor, fecha_emision=timezone.now(), total=0)
            for producto_id, cantidad in zip(productos, cantidades):
                producto = Producto.objects.get(id=producto_id)
                subtotal = producto.precio * cantidad
                total += subtotal
                DetalleFactura.objects.create(factura=factura, producto=producto, cantidad=cantidad, precio=producto.precio, subtotal=subtotal)
            factura.total = total
            factura.save()
            return redirect('factura_detalle', factura_id=factura.id)
    else:
        form = PedidoForm()
    return render(request, 'myapp/hacer_pedido.html', {'form': form})

@login_required
def factura_detalle(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    detalles = DetalleFactura.objects.filter(factura=factura)
    return render(request, 'myapp/factura_detalle.html', {'factura': factura, 'detalles': detalles})


