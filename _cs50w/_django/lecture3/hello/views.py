from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    return HttpResponse(f"Hello {name.capitalize()}!")