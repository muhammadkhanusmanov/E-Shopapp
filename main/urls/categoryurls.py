from django.urls import path

from ..views import (
    CategoryView
)


urlpatterns = [
    path('allcategories/',CategoryView.as_view())
]