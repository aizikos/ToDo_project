from django.shortcuts import render,HttpResponse,redirect

from .models import TODO

def homepage (request):
    todo_list=TODO.objects.all()
    return render (request,'index.html',{"todo_list": todo_list})

def test (request):   
    return render (request,'test.html')

def add_todo(request):
    f = request.POST
    text = f["texts"]
    todo = TODO(
        text= text
    )
    todo.save()
    return  redirect(homepage)


def delete_todo (request,id):
    todo = TODO.objects.get(id=id)
    todo.delete()
    return redirect(homepage)


def mark_todo(request,id):
    todo = TODO.objects.get(id = id)
    todo.is_favorite = True
    todo.save()
    return redirect(homepage)

# Create your views here.
