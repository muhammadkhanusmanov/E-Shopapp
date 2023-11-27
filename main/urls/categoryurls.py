from django.urls import path

from ..views import (
    CategoryView,CategoryImg
)


urlpatterns = [
    path('allcategories/',CategoryView.as_view()),
    path('save/<str:id>',CategoryImg.as_view())
]