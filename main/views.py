from django.shortcuts import render

def homepage (request):
    return render (request,'index.html')

def chat (request):
    return render (request,'names.html')

def get (request):
    return HttpResponse('I LOVE YOU')


# Create your views here.
