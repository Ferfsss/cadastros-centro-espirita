from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('main.urls')),
    path ('pessoas', include('pessoa.urls')),
    path ('', include('doacoes.urls')),
]
