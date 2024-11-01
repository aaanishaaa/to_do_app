from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy #goes back to the same page after submission
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin #retricts a userr to only see stufff that is important to it

from django.contrib.auth.forms import UserCreationForm #creates a user for us

from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name ='base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks') #redirects users to tasks
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super()(RegisterPage,self).form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)
            
    
class TaskList(LoginRequiredMixin,ListView):   # Class-based view for listing tasks
    model = Task
    context_object_name = 'tasks'  # Define the context variable used in the template
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete = False).count()
        
        search_input= self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks']=context['tasks'].filter(
                title__icontains=search_input)
            #title__startswith=search_input) for only the words starting with the search input
        
        context['search_input']= search_input
        return context

class TaskDetail(LoginRequiredMixin, DetailView):  # Class-based view for showing task details
    model = Task
    context_object_name = 'task'  # Define the context variable used in the template
    template_name = 'base/task_detail.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks') #redirects users to tasks
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model= Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks') #redirects users to task
    
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')