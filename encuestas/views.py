from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Team 5, Codo a Codo")
