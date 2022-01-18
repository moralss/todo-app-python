from django.urls import path
from . import views


urlpatterns = [
    path('showTodo/', views.show_todo, name='show_todo'),
    path('updateTodo/<int:id>/', views.todo_update, name="todo_update"),
    path('addTodo/', views.post_todo),
    path('todoDelete/<int:id>/', views.todo_delete,  name='todo_delete')
]
