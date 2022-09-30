from django.shortcuts import render

from .models import ToMeet

def work (request):
    return render (request,'index1.html')

def works (request):
    todo_list = ToMeet.objects.all()
    return render (request,'meeting.html',{"todo_list" : todo_list})


# Create your views here.
