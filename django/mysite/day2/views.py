from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'day2/home.html')

def about(request):
    return render(request, 'day2/about.html')