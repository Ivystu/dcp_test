from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select_animal_center/', views.select_animal_center, name="select_animal_center"),
    path('select_animal_common/', views.select_animal_common, name="select_animal_common"),
    path('story_dog/', views.story_dog, name="story_dog"),
    path('aboutus_dog/', views.aboutus_dog, name="aboutus_dog"),
    path('kn_dog/', views.kn_dog, name="kn_dog"),
    path('kn_dog_1/', views.kn_dog_1, name="kn_dog_1"),
    path('kn_dog_2/', views.kn_dog_2, name="kn_dog_2"),
    path('list_dog/', views.list_dog, name="list_dog"),
    path('quiz_dog_3/', views.quiz_dog_3, name="quiz_dog_3"),
    path('instruction_dog/', views.instruction_dog, name="instruction_dog"),
    path('test_result_dog/', views.test_result_dog, name="test_result_dog")
]