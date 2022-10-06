from django.shortcuts import render,HttpResponse,redirect

from .models import ToMeet, Habits

def work (request):
    return render (request,'index1.html')

def works (request):
    todo_list = ToMeet.objects.all()
    return render (request,'meeting.html',{"todo_list" : todo_list})

def meet (request):
    todo_list = ToMeet.objects.all()
    return render (request,'Toomet1.html',{"todo_list": todo_list})

def add_todos(request):
    f = request.POST
    text = f["todo_text"]
    num = f ["todo_number"]
    com = f ["todo_com"]
    todo = ToMeet(
        persone = text,

        phone_number=num,

        comment = com
    )
    todo.save()
    return redirect(meet)
    
def habits(request):
    todo_list = Habits.objects.all()
    return render (request,"habits.html",{"todo_list": todo_list})

def add_habits(request):
    f = request.POST
    name = f["habits_text"]
    num = f ["habits_day"]
    hot=f ["habits_hot"]
    com = f ["habits_com"]
    hab = Habits(
        name = name,

        done_for_today=num,

        important= hot,

        comment = com
    )
    hab.save()
    return redirect(habits)

def delete_to_meet (request,id):
    todo = ToMeet.objects.get(id=id)
    todo.delete()
    return redirect(meet)

def  mark_to_meet(request,id):
    todo = ToMeet.objects.get(id = id)
    todo.is_favorite = not todo.is_favorite
    todo.save()
    return redirect(meet)

def closed_todo(request,id):
     todo = ToMeet.objects.get(id=id)
     todo.is_closed= not todo.is_closed
     todo.save()
     return redirect (meet)





# Create your views here.
