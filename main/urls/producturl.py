from django.urls import path

from ..views import (
    ProductView
)


urlpatterns = [
    path('allproducts/',ProductView.as_view()),
    path('productbyid/<str:id>',ProductView.as_view())
]