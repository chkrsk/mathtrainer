from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('calculate', views.calculate, name='calculate'),
    path('summary', views.summary, name='summary')
]