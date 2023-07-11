
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def base(request):
    return HttpResponse("Hello, World!")

# def greeting(request):
#     return HttpResponse("Hello, Django!")

def greeting(request):
    template = loader.get_template('hello.html')
    return HttpResponse(template.render())