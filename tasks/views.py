from django.shortcuts import render, redirect
from django.utils.text import slugify
from django.db.models import F

from .models import Task
from .forms import TaskForm

# Create your views here.
def task_list(request):
    title = 'All tasks'
    tasks = Task.objects.all().order_by('done', F('complete_before').asc(nulls_last=True))
    return render(request, 'tasks/task-list.html', dict(tasks=tasks, title=title))

def add_task(request):
    if request.method == 'POST':
        if (form := TaskForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task/add.html', dict(form=form))

def done_tasks(request):
    title = 'Completed tasks'
    tasks = Task.objects.filter(done=True).order_by(F('complete_before').asc(nulls_last=True))
    return render(request, 'tasks/task-list.html', dict(tasks=tasks, title=title))

def pending_tasks(request):
    title = 'Pending tasks'
    tasks = Task.objects.filter(done=False).order_by(F('complete_before').asc(nulls_last=True))
    return render(request, 'tasks/task-list.html', dict(tasks=tasks, title=title))

def task_detail(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/task/detail.html', dict(task=task))

def remove_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    message = f'Task "{task.name}" removed!'
    task.delete()
    return render(request, "tasks/feedback.html", dict(message=message))

def edit_task(request, task_slug: str):
    task = Task.objects.get(slug=task_slug)
    if request.method == 'POST':
        if (form := TaskForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            message = f'Task "{task.name}" edited!'
            return render(request, 'tasks/feedback.html', dict(message=message))
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task/edit.html', dict(task=task, form=form))

def toggle_task(request, task_slug: str):
    task = Task.objects.get(slug=task_slug)
    task.done = not task.done
    task.save()
    return redirect("tasks:task-list")