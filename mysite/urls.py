from django.contrib import admin
from django.urls import path, include
from portfolio import views

urlpatterns = [
    path('', include('portfolio.urls')),
    path('admin/', admin.site.urls),
]
