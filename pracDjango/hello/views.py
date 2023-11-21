from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def anu(request):
    return HttpResponse("Hello anubhav!")

def greet(request, name):
    return render(request, "hello/greets.html", {"name": name.capitalize()})
