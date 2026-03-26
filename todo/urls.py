from django.urls import path
from todo.views import todo_list, create_todo, update_todo, delete_todo

urlpatterns = [
    path('', todo_list, name="todo_list"),
    path('create/', create_todo, name="crate_todo"),
    path('update/<str:id>/', update_todo, name="update_todo"),
    path('delete/<str:id>/', delete_todo, name="delete_todo"),
]
