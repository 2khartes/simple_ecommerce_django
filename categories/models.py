from django.db import models

class Categorie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)