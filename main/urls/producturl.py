from django.urls import path

from ..views import (
    ProductView, SearchProduct,Reklama
)


urlpatterns = [
    path('allproducts/',ProductView.as_view()),
    path('productbyid/<str:id>',ProductView.as_view()),
    path('search/product/<str:name>',SearchProduct.as_view()),
    path('special/',Reklama.as_view()),
]