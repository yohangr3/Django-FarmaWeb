from django import forms
from django.db import models

categoria_productos = [
    1,'Analgesicos',
    2,'Belleza',
    3,'Dermatologicos'
    
]

# Create your models here.
class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(max_length=6)
    description = models.CharField(max_length=200)
    # ? categoria = models.CharField(max_length=50) // Preguntar
    stock = models.IntegerField(default=0, verbose_name='stock')

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    number = models.IntegerField()
    phone = models.IntegerField()