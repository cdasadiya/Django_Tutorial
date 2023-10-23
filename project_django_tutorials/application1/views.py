from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h5> Wecome to my first page from the Application -1 </h5>')

def second(request):
    return HttpResponse('<h5> Wecome to my second page from the Application-1 </h5>')