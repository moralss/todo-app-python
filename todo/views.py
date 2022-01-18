from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

todos_array = []


class todo():
    def __init__(self, topic, description):
        self.topic = topic
        self.description = description


todos_array.append(todo('work',  'clean room'))
todos_array.append(todo('play', 'play fifa'))


def show_todo(request):
    print(todos_array[0].topic)
    return render(request, 'todos.html', {'todos_array': todos_array})


def post_todo(request):
    form = forms.Todoform()
    return render(request, 'addTodo.html', {'form': form})
