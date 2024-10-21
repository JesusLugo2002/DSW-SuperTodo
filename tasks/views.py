from django.shortcuts import render, redirect
from django.utils.text import slugify

from .models import Task
from .forms import AddTaskForm, EditTaskForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task-list.html', dict(tasks=tasks))

def add_task(request):
    if request.method == 'POST':
        if (form := AddTaskForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.title)
            task.save()
            message = f'Task {task.title} added!'
            return render(request, 'tasks/feedback.html', dict(message=message))
    else:
        form = AddTaskForm()
    return render(request, 'tasks/add-task.html', dict(form=form))

def done_tasks(request):
    tasks = Task.objects.filter(done=True)
    return render(request, 'tasks/task-list.html', dict(tasks=tasks))

def pending_tasks(request):
    tasks = Task.objects.filter(done=False)
    return render(request, 'tasks/task-list.html', dict(tasks=tasks))

def task_detail(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    return render(request, 'tasks/task/task-detail.html', dict(task=task))

def remove_task(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    message = f'Task {task.title} removed!'
    task.delete()
    return render(request, "tasks/feedback.html", dict(message=message))

def edit_task(request, task_slug: str):
    task = Task.objects.get(slug=task_slug)
    if request.method == 'POST':
        if (form := EditTaskForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.title)
            task.save()
            message = f'Task {task.title} edited!'
            return render(request, 'tasks/feedback.html', dict(message=message))
    else:
        form = EditTaskForm(instance=task)
    return render(request, 'tasks/task/edit-task.html', dict(task=task, form=form))

def toggle_task(request, task_slug: str):
    task = Task.objects.get(slug=task_slug)
    task.done = not task.done
    task.save()
    return redirect("tasks:task-list")