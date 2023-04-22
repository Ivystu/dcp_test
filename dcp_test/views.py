from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def select_animal_center(request):
    return render(request, 'select_animal_center.html')

def story_dog(request):
    return render(request, 'story_dog.html')

def aboutus_dog(request):
    return render(request, 'aboutus_dog.html')

def kn_dog(request):
    return render(request, 'kn_dog.html')

def list_dog(request):
    return render(request, 'list_dog.html')

def quiz_dog_3(request):
    return render(request, 'quiz_dog_3.html')