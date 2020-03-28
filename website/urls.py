from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    path('', views.index, name='index'),
    path('home', HomeView, name='home'),
]