from django.contrib import admin
from .models import Categories, Products

admin.site.register([
    Categories,Products
])
