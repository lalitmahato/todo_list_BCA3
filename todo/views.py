from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from todo.models import Todo
from todo.forms import TodoForm

# Create your views here.
def hello_world(request):
    return HttpResponse("<h1 style='color:red;'>Hello World I am starting Django.</h1>")

def json_response(request):
    my_response = {
        "Name": "Lalit Mahato",
        "Student ID": 1,
        "Message": "Hello Word",
        "Status": True 
    }
    return JsonResponse(my_response)

def template_hello_world(request):
    context = {
        "Name": "Lalit Mahato",
        "Student_ID": 10000000000001,
        "Message": "Hello Word",
        "Status": True 
    }
    return render(request, "index.html", context)


def todo_list(request):
    todo_query = Todo.objects.filter(completion_status=False)
    context = {
        "todo_query": todo_query
    }
    return render(request, "todo/todo_list.html", context)

def create_todo(request):
    form = TodoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid:
            form.save()
            return redirect("todo_list")
    context = {
        "form": form
    }
    return render(request, "todo/create_todo.html", context)