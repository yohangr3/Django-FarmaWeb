from django.contrib import admin
from .models import Productos
from .models import Cliente

# Register your models here.
admin.site.register(Productos)
admin.site.register(Cliente)