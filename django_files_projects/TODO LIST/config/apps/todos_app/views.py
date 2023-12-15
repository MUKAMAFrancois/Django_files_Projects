from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from apps.todos_app.models import TodoModel
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin


class ListingTasks(LoginRequiredMixin,ListView):
    model=TodoModel
    context_object_name='tasks'
    template_name='todo/index.html'
    queryset=TodoModel.objects.all().order_by('due_date')
    paginate_by=2


class DetailedTask(LoginRequiredMixin,DetailView):
    model=TodoModel
    template_name='todo/details.html'

class UpdateTask(LoginRequiredMixin,UpdateView):
    model=TodoModel
    template_name='todo/update.html'
    success_url=reverse_lazy('homepage')
    fields='__all__'

class CreateTask(LoginRequiredMixin,CreateView):
    model=TodoModel
    template_name='todo/createtask.html'
    success_url=reverse_lazy('homepage')
    fields='__all__'

    # whenever we create the task, it should be related to login user   


    
class DeleteTask(LoginRequiredMixin,DeleteView):
    model=TodoModel
    template_name='todo/deletetask.html'
    success_url=reverse_lazy('homepage')
    




