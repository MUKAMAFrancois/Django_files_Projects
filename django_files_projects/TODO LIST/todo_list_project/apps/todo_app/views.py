from apps.todo_app.models import TodoModel
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class ListingTasks(ListView,LoginRequiredMixin):
    model=TodoModel
    template_name='todo_app/index.html'
    queryset=TodoModel.objects.all().order_by('created')
    context_object_name='tasks'
    paginate_by=4


class DeatiledTask(DetailView):
    model=TodoModel
    template_name='todo_app/detail_task.html'


class UpdateTask(UpdateView,LoginRequiredMixin):
    model=TodoModel
    template_name='todo_app/update_task.html'
    success_url=reverse_lazy('homepage')
    fields='__all__'


class CreateTask(LoginRequiredMixin,CreateView):
    model=TodoModel
    template_name='todo_app/create_task.html'
    success_url=reverse_lazy('homepage')
    fields='__all__'


class DeleteTask(LoginRequiredMixin,DeleteView):
    model=TodoModel
    template_name='todo_app/delete_task.html'
    success_url=reverse_lazy('homepage')
    




