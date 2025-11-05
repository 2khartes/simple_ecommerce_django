from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.http import JsonResponse
from shopping_cart.models import ShoppingCart
from products.models import Product
from django.db import IntegrityError

@login_required(login_url="/login")
def base(req:HttpRequest):
    data = ShoppingCart.objects.select_related().filter(user= req.user)
    return render(req,"shopping_cart/base.html",{"carts":data})


@login_required(login_url="/login")
def add(req:HttpRequest,productId):
    if req.method != "POST":
        return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)
    
    try:
        productMatch = Product.objects.get(id=productId)
        
        ShoppingCart.objects.create(
            user =  req.user,
            product =  productMatch
        )
        return JsonResponse({'status': 'error', 'message': 'Producto añadido'}, status=202)
    except Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El producto Seleccionado no existe'}, status=404)
    except IntegrityError:
        return JsonResponse({'status': 'error', 'message': 'El producto seleccionado ya esta en el carrito'}, status=409)


def delete(req:HttpRequest,cartId):
    if req.method != "DELETE":
        return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)
    try:
        productMatch = ShoppingCart.objects.get(id=cartId)
        productMatch.delete()
        return JsonResponse({'status': 'error', 'message': 'Item eliminado'}, status=202)
    except cartId.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'El producto seleccionado no existe'}, status=404)

def deleteAll(req:HttpRequest):
    if req.method != "DELETE":
        return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)
    try:
        ShoppingCart.objects.filter(user= req.user).delete()
        return JsonResponse({'status': 'error', 'message': 'Carrito comprado'}, status=202)
    except:
        return JsonResponse({'status': 'error', 'message': 'Error al comparar'}, status=404)