
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member



def base(request):
    return HttpResponse("Hello, World!")

# def greeting(request):
#     return HttpResponse("Hello, Django!")

def greeting(request):
    template = loader.get_template('hello.html')
    return HttpResponse(template.render())


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }    
    return HttpResponse(template.render(context, request))