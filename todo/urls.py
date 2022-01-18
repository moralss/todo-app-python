from django.urls import path
from . import views


urlpatterns = [
    path('todo_show/', views.todo_show, name='todo_show'),
    path('todo_update/<int:id>/', views.todo_update, name="todo_update"),
    path('todo_post/', views.todo_post, name='todo_post'),
    path('todo_delete/<int:id>/', views.todo_delete,  name='todo_delete')
]
