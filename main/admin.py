from django.contrib import admin
from .models import Categories, Products, UserProduct, MarketProduct, RecomntsProduct

admin.site.register([
    Categories,Products, UserProduct, MarketProduct,RecomntsProduct
])
