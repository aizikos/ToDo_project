from django.shortcuts import render,HttpResponse

from .models import TODO

def homepage (request):
    todo_list=TODO.objects.all()
    return render (request,'index.html',{"todo_list": todo_list})

def test (request):   
    return render (request,'test.html')

#def add_todo(request):
    #f = request.POST
   # text=f["todo_text"]
    #todo = ToDo(
    #    text=text
    
    #todo.save()

    #return HttpResponse("FORMA")




# Create your views here.
