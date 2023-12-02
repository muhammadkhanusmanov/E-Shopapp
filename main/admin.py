from django.contrib import admin
from .models import Categories, Products, UserProduct, MarketProduct

admin.site.register([
    Categories,Products, UserProduct, MarketProduct
])
