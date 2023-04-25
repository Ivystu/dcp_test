from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def select_animal_center(request):
    return render(request, 'select_animal_center.html')

def select_animal_common(request):
    return render(request, 'select_animal_common.html')

def story_dog(request):
    return render(request, 'story_dog.html')

def aboutus_dog(request):
    return render(request, 'aboutus_dog.html')

def aboutus_cat(request):
    return render(request, 'aboutus_cat.html')

def kn_dog(request):
    return render(request, 'kn_dog.html')

def kn_dog_1(request):
    return render(request, 'kn_dog_1.html')

def kn_dog_2(request):
    return render(request, 'kn_dog_2.html')

def kn_cat(request):
    return render(request, 'kn_cat.html')

def list_dog(request):
    return render(request, 'list_dog.html')

def list_cat(request):
    return render(request, 'list_cat.html')

def quiz_dog_3(request):
    return render(request, 'quiz_dog_3.html')

def instruction_dog(request):
    return render(request, 'instruction_dog.html')

def test_result_dog(request):
    return render(request, 'test_result_dog.html')