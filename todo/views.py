from django.shortcuts import render
from django.http import HttpResponse
from .forms import TodoForm
from django.shortcuts import render, redirect, get_object_or_404

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

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():

            topic = form.cleaned_data['topic']
            descrption = form.cleaned_data['descrption']
            todos_array.append(todo(topic, descrption))
            return redirect('/todo/show_todo/')

    form = TodoForm()
    return render(request, 'addTodo.html', {'form': form})
