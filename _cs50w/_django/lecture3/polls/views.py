from django.http import HttpResponse
from django.shortcuts import render

def greet(request, name):
    return render(request, "polls/greet.html", {
        "name": name.capitalize()
    })