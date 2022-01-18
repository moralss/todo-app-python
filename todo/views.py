from django.shortcuts import render
from django.http import HttpResponse
from .forms import TodoForm
from django.shortcuts import render, redirect, get_object_or_404
import random
# Create your views here.

todos_array = []
selected_id = 0


class Todo():
    def __init__(self, id,  topic, description):
        self.id = id
        self.topic = topic
        self.description = description


todos_array.append(Todo(1, 'work',  'clean room'))
todos_array.append(Todo(2, 'play', 'play fifa'))


def show_todo(request):
    return render(request, 'todos.html', {'todos_array': todos_array})


def post_todo(request):

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():

            topic = form.cleaned_data['topic']
            descrption = form.cleaned_data['descrption']
            todos_array.append(
                Todo(random.randint(0, 100000), topic, descrption))
            return redirect('/todo/showTodo/')

    form = TodoForm()
    return render(request, 'addTodo.html', {'form': form})


def todo_delete(request, id):
    if request.method == 'POST':
        for item in todos_array:
            print(request)
            if item.id == id:
                print("I found what I was looking for")
                todos_array.remove(item)
                return redirect('/todo/showTodo/')
    return render(request, 'delete.html', {})
