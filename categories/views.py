from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from categories.models import Categorie
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth import logout
from django.contrib.messages import get_messages
from django.db.models import ProtectedError
from .forms import CrearCategorie

@login_required(login_url="login")
def base(req:HttpRequest):
    if(not req.user.is_superuser):
        current_messages = get_messages(req)
        for _ in current_messages:
            pass
        logout(req)
        messages.error(req,"Usuario no autorizado")
        return redirect("/login")
    
    categories = []
    
    termino_busqueda = req.GET.get('q')
    if termino_busqueda:
        categories = Categorie.objects.filter(name__icontains=termino_busqueda)
    else:
        categories = Categorie.objects.all()
    return render(req,"categories/lista.html",{"categories":categories})


@login_required(login_url="login")
def add(req):
    if(not req.user.is_superuser):
        current_messages = get_messages(req)
        for _ in current_messages:
            pass
        logout(req)
        messages.error(req,"Usuario no autorizado")
        return redirect("/login")
    
    if req.method == "POST":
        newCategorie = CrearCategorie(req.POST,req.FILES)
        if newCategorie.is_valid():
            messages.success(req,"Categoria Creada")
            newCategorie.save()
            return redirect("/categories")
    return render(req,"categories/create.html")


@login_required(login_url="login")
def delete(req,catId):
    try:
        if(not req.user.is_superuser):
            current_messages = get_messages(req)
            for _ in current_messages:
                pass
            logout(req)
            messages.error(req,"Usuario no autorizado")
            return redirect("/login")
        categorie = get_object_or_404(Categorie,id = catId)
        categorie.delete()
        messages.success(req, "Categoria eliminada ")
        return redirect("/categories")
    except ProtectedError:   
        messages.error(req, "Esta categoria esta siendo usado, no se puede eliminar ")
        return redirect("/categories") 
    

@login_required(login_url="login")
def update(req, catId):
    if(not req.user.is_superuser):
        current_messages = get_messages(req)
        for _ in current_messages:
            pass
        logout(req)
        messages.error(req,"Usuario no autorizado")
        return redirect("/login")
    categorie = get_object_or_404(Categorie, id=catId)
    if req.method == "POST":
        form = CrearCategorie(req.POST, req.FILES, instance=categorie)
        if form.is_valid():
            form.save()
            messages.success(req, "Categoria actualizada")
            return redirect("/categories")
        else:
            messages.error(req, "Datos inválidos, revisa el formulario.")
    return render(req, "categories/create.html", {"categorie": categorie})

