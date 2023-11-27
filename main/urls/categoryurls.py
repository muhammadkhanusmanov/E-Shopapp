from django.urls import path

from ..views import (
    CategoryView,ProductView
)


urlpatterns = [
    path('allcategories/',CategoryView.as_view()),
    path('products/bycategory/<str:id>',ProductView.as_view()),
]