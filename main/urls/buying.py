from django.urls import path

from ..views import (
    BuyingView
)


urlpatterns = [
    path('buying/',BuyingView.as_view()),
    path('user/goods/',BuyingView.as_view()),
]