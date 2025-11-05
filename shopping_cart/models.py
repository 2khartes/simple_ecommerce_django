from django.db import models
from django.conf import settings
from products.models import Product

class ShoppingCart(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT, 
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='shopping_carts'
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'product',)
        verbose_name = "Carrito de Compras"
        verbose_name_plural = "Carritos de Compras"