from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy #goes back to the same page after submission

class TaskList(ListView):   # Class-based view for listing tasks
    model = Task
    context_object_name = 'tasks'  # Define the context variable used in the template

class TaskDetail(DetailView):  # Class-based view for showing task details
    model = Task
    context_object_name = 'task'  # Define the context variable used in the template
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks') #redirects users to task
    
class TaskUpdate(UpdateView):
    model= Task
    fields = '__all__'
    success_url = reverse_lazy('tasks') #redirects users to task
    
class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')