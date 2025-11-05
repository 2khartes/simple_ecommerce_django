from products.views import  base,add,delete,update
from django.urls import path

app_name = "products"

urlpatterns = [
    path('products', base, name="lista"),
    path('products/add', add, name="add"),
    path('products/update/<int:productId>',update , name="update"),
    path('products/delete/<int:productId>', delete, name="delete"),
]