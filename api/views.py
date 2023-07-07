from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome</h1>')

def logged_in(request):
    return render(request, 'logged_in.html')