from django.contrib import admin
from .models import Categories, Products, UsersProduct, MarketProduct, RecomntsProduct

admin.site.register([
    Categories,Products, UsersProduct, MarketProduct,RecomntsProduct
])
