from django.shortcuts import render
from django.http import HttpResponse



def base(request):
    return HttpResponse("Hello, World!")

def greeting(request):
    return HttpResponse("Hello, Django!")