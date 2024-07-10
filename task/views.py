from django.shortcuts import redirect, render
from .forms import TaskForm
from .models import Task


def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    tasks = Task.objects.filter(is_done=False)
    context = {
        'form': form,
        'tasks': tasks
    }
    return render(request, 'task/index.html', context)


def mark_as_done(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.is_done = True
    task.save()
    return redirect('index')


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('index')
