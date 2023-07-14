from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello Ada!</h1>")
    return render(request, "home.html", {})

def artist_view(*args, **kwargs):
    return HttpResponse("<h1>Artist page</h1>")
