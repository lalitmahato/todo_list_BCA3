from django.urls import path
from todo.views import todo_list, create_todo

urlpatterns = [
    path('', todo_list, name="todo_list"),
    path('create/', create_todo, name="crate_todo"),
]
