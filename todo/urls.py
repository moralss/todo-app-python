from django.urls import path
from . import views


urlpatterns = [
    path('showTodo/', views.show_todo, name='show_todo'),
    path('addTodo/', views.post_todo),
    # path(r'^delete/(?P<pk>[0-9]+)/$', views.todo_delete, name='todo_delete')
    path('todoDelete/<int:id>/', views.todo_delete,  name='todo_delete')
]
