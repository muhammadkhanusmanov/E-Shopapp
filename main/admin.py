from django.contrib import admin
from .models import Categories, Products, UserProduct

admin.site.register([
    Categories,Products, UserProduct
])
