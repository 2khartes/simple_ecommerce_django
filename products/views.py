from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from . import forms
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth import logout
from django.contrib.messages import get_messages
from django.db.models import ProtectedError

@login_required(login_url="login")
def base(req:HttpRequest):
    if(not req.user.is_superuser):
        current_messages = get_messages(req)
        for _ in current_messages:
            pass
        logout(req)
        messages.success(req,"Usuario no autorizado")
        return redirect("/login")
    products= []
    termino_busqueda = req.GET.get('q')
    if termino_busqueda:
        products = Product.objects.filter(name__icontains=termino_busqueda)
    else:
        products = Product.objects.all()
    return render(req,"products/lista.html",{"products":products})

@login_required(login_url="login")
def add(req):
    if(not req.user.is_superuser):
        current_messages = get_messages(req)
        for _ in current_messages:
            pass
        logout(req)
        messages.success(req,"Usuario no autorizado")
        return redirect("/login")
    if req.method == "POST":
        newProduct = forms.CrearProduct(req.POST,req.FILES)
        if newProduct.is_valid():
            messages.success(req,"Producto añadido")
            newProduct.save()
            return redirect("/products")
    return render(req,"products/crear.html")


@login_required(login_url="login")
def delete(req,productId):
    try:
        if(not req.user.is_superuser):
            current_messages = get_messages(req)
            for _ in current_messages:
                pass
            logout(req)
            messages.success(req,"Usuario no autorizado")
            return redirect("/login")
        product = get_object_or_404(Product,id = productId)
        product.delete()
        messages.success(req, "Producto eliminado ")
        return redirect("/products")
    except ProtectedError:   
        messages.success(req, "Este producto esta siendo usado por un usuario y no se puede eliminar ")
        return redirect("/products") 
    

@login_required(login_url="login")
def update(req, productId):
    if(not req.user.is_superuser):
        current_messages = get_messages(req)
        for _ in current_messages:
            pass
        logout(req)
        messages.success(req,"Usuario no autorizado")
        return redirect("/login")
    product = get_object_or_404(Product, id=productId)
    if req.method == "POST":
        form = forms.CrearProduct(req.POST, req.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(req, "Producto actualizado correctamente.")
            return redirect("/products")
        else:
            messages.error(req, "Datos inválidos, revisa el formulario.")
    return render(req, "products/crear.html", {"product": product})

