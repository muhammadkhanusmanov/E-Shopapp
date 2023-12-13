from django.urls import path

from ..views import (
    UserView,
    RegisterView,
    LogoutView,
    GetData
)


urlpatterns = [
    path('signup/',RegisterView.as_view()),
    path('login/',UserView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('user/data/',LogoutView.as_view()),
    path('get/data/',GetData.as_view()),
]