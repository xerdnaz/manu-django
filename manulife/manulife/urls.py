from django.contrib import admin
from django.urls import path
from manuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('addclient/', views.addclient, name='addclient')
]
