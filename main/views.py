from django.shortcuts import render,HttpResponse

#from .models import ToDo

def homepage (request):
        return render (request,'index.html')

def test (request):   
    return render (request,'test.html',)

#def add_todo(request):
    #f = request.POST
   # text=f["todo_text"]
    #todo = ToDo(
    #    text=text
    
    #todo.save()

    #return HttpResponse("FORMA")




# Create your views here.
