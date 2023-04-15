from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def select_animal_center(request):
    return render(request, 'select_animal_center.html')

def abc(request):
    return render(request, 'abc.html')