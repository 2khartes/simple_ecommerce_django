from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from django.http import HttpRequest
import random
def base(req):
    products =  Product.objects.all()
    opciones_aos = [
        'fade-up', 
        'fade-down', 
        'zoom-in', 
        'flip-left'
    ]
    for i, product in enumerate(products):
        product.aos_animacion = random.choice(opciones_aos)
        product.aos_retraso = 0
    return render(req,"main/inicio.html",{"products":products})



def auth_login(req:HttpRequest):
    if req.user.is_authenticated:
        if req.user.is_superuser :
            return redirect("/products")
        else:
            return redirect("/")
        
    if req.method == "POST":
        form =  AuthenticationForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req,user)
            messages.success(req,"Inicio de sesion correcto")
            if user.is_superuser:
                return redirect("/products")
            else:
                return redirect("/")
        else:
            messages.success(req,"Credenciales incorrectas")
    return render(req,"main/login.html")


def auth_register(req:HttpRequest):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():   
            user =  form.save()
            login(req,user)
            messages.success(req,"Usuario registrado exitosamente")     
            return redirect("/")
        else:
            print(form.errors) 
            messages.success(req,"Datos ingresados invalidos")
    return render(req,"main/register.html")

@login_required(login_url="/login")
def auth_logout(req):
    logout(req)
    messages.success(req, "Sesion cerrada")
    return redirect("/login")

def custom_404(req,_):
    return render(req,"main/404.html", status=404)