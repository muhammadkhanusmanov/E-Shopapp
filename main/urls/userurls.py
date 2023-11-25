from django.urls import path

from ..views import (
    UserView,
    RegisterView,
    LogoutView
)


urlpatterns = [
    path('signup/',RegisterView.as_view()),
    path('login/',UserView.as_view()),
    path('logout/',LogoutView.as_view())
]