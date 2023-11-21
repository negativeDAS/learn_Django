from django.shortcuts import render

tasks=["anu", "pan", "shin"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })