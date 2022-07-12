from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='weather'),
    path('api/', views.weather, name='api'),
]