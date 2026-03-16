from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

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