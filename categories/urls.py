from categories.views import  base,add,update,delete
from django.urls import path

app_name = "categories"

urlpatterns = [
    path('categories', base, name="lista"),
    path('categories/add', add, name="add"),
     path('categories/update/<int:catId>',update , name="update"),
    path('categories/delete/<int:catId>', delete, name="delete"),
]