from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

todos_array = []
class todo():
  def __init__(self , name):
    self.name = name

todos_array.append(todo('clean my room '))
todos_array.append(todo('play soccer '))

def say_hello (request):
  print( todos_array[0].name)
  return  render(request , 'todos.html' , {'todos_array' : todos_array})


# def post_list(request, template_name='todos.html'):
#     # posts = blog_posts.objects.all()
#     # data = {}
#     # data['object_list'] = posts
#     return render(request, template_name, data)