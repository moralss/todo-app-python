from django.urls import path
from . import views


urlpatterns = [
    path('show_todo/', views.show_todo),
    path('addTodos/', views.post_todo)
]
