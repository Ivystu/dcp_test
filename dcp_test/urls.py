from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select_animal_center/', views.select_animal_center, name="select_animal_center"),
    path('story_dog/', views.story_dog, name="story_dog"),
    path('aboutus_dog/', views.aboutus_dog, name="aboutus_dog"),
    path('kn_dog/', views.kn_dog, name="kn_dog"),
    path('list_dog/', views.list_dog, name="list_dog"),
    path('quiz_dog_3/', views.quiz_dog_3, name="quiz_dog_3")
]