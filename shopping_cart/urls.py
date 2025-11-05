from shopping_cart.views import base,add,delete,deleteAll
from django.urls import path

app_name ="shopping_cart"

urlpatterns = [
    path('cart/', base, name="lista"),
    path('cart/<int:productId>', add, name='add'),
    path('cart/delete/<int:cartId>', delete, name='delete'),
    path('cart/delete_all', deleteAll, name='delete_all'),
]