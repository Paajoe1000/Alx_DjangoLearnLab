from django.shortcuts import render, HttpResponse

# Create your views here.

def lounge(request):
    return HttpResponse("Hello, welcome to my Library Project")
