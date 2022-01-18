from pydoc_data import topics
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

    def change_todo(self, topic, description):
        self.topic = topic
        self.description = description


todos_array.append(Todo(1, 'work',  'learn python Django'))
todos_array.append(Todo(2, 'play', 'play fifa 22'))


def todo_show(request):
    return render(request, 'pages/todo_show.html', {'todos_array': todos_array})


def todo_post(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            descrption = form.cleaned_data['descrption']
            todos_array.append(
                Todo(random.randint(0, 100000), topic, descrption))
            return redirect('/todo/todo_show/')

    form = TodoForm()
    return render(request, 'pages/todo_post.html', {'form': form})


def todo_delete(request, id):
    if request.method == 'POST':
        for item in todos_array:
            print(request)
            if item.id == id:
                todos_array.remove(item)
                return redirect('/todo/todo_show/')
    return render(request, 'pages/delete_confirm.html', {})


def todo_update(request, id):
    if request.method == 'POST':
        for index, item in enumerate(todos_array):
            if item.id == id:
                form = TodoForm(request.POST)
                if form.is_valid():
                    topic = form.cleaned_data['topic']
                    descrption = form.cleaned_data['descrption']
                    todos_array[index] = Todo(item.id, topic, descrption)
                    return redirect('/todo/todo_show/')

    filtered = list(filter(lambda a: a.id == id, todos_array))
    selected_topic = filtered[0].topic
    selected_description = filtered[0].description
    form = TodoForm(
        {'topic': selected_topic, 'descrption': selected_description})
    return render(request, 'pages/todo_update.html', {'form': form})
