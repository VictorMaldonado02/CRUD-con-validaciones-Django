from django.shortcuts import redirect, render
from AppDemo.models import Producto, Usuario
from AppDemo.forms import FormProducto, FormProduct, FormUsu,FormUsua,CustomUserCreationForm
from . import forms 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login

 
# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required 
def listado1(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'productos.html', data)

def agregarProducto(request):
    form = FormProducto()
    if request.method == 'POST':
        form = FormProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productos')
    data={'form':form}
    return render(request, 'agregarProducto.html', data)

def eliminarProducto(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect('/productos')
 
def actualizarProducto(request, id):
    product = Producto.objects.get(id = id)
    form = FormProduct( instance = product)
    if request.method == "POST" :
        form = FormProduct(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('/productos')
    data={'form' : form}
    return render(request, 'agregarProducto.html', data)

def listado2(request):
    usuarios = Usuario.objects.all()
    data = {'usuarios': usuarios}
    return render(request, 'usuarios.html', data)

def agregarCliente(request):
    form = FormUsu()
    if request.method == 'POST':
        form = FormUsu(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/usuarios')
    data={'form':form}
    return render(request, 'agregarUsuario.html', data)

def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(id = id)
    usuario.delete()
    return redirect('/usuarios')

def actualizarUsuario(request, id):
    usuario = Usuario.objects.get(id = id)
    form = FormUsua( instance = usuario)
    if request.method == "POST" :
        form = FormUsua(request.POST, instance =usuario)
        if form.is_valid():
            form.save()
            return redirect('/usuarios')
    data={'form' : form}
    return render(request, 'agregarUsuario.html', data)

def register(request):
    data = {'form': CustomUserCreationForm()}
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('/productos')
        else:
            data['form'] = user_creation_form
    return render(request, 'registration/registro.html', data)

def exit(request):
    logout(request)
    return redirect('../')


