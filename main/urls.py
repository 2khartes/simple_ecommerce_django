from main.views import base,auth_login,auth_logout,custom_404,auth_register
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name="inicio"),
    path('login', auth_login, name="login"),
    path('register', auth_register, name="register"),
    path('logout', auth_logout, name="logout"),
    path('', include('products.urls'))   ,
    path('', include('shopping_cart.urls')), 
    path('', include('categories.urls')), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = custom_404