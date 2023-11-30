from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('main.urls.userurls')),
    path('api/v2/',include('main.urls.categoryurls')),
    path('api/v3/',include('main.urls.producturl')),
    path('api/v4/',include('main.urls.buying')),
]
