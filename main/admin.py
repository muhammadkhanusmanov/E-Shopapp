from django.contrib import admin
from .models import Categories, Products, UserProduct, ReklamaProduct

admin.site.register([
    Categories,Products, UserProduct,ReklamaProduct
])
