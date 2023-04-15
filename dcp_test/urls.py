from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select_animal_center/', views.select_animal_center, name="select_animal_center"),
    path('abc/', views.abc, name="abc")
]