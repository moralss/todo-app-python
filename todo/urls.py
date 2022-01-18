from django.urls import path
from . import views


urlpatterns = [
    path('showTodo/', views.show_todo),
    path('addTodo/', views.post_todo)
]
