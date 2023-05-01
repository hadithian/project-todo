from django.shortcuts import render, redirect


# Create your views here.

from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    
    context = {
        "page_title":"Todo-list",
        "tasks":tasks,
    }
    
    return render(request, 'todo_app/task_list.html', context)

def task_create(request):
    account_form = TaskForm(request.POST or None)
    
    if request.method == 'POST':
        if account_form.is_valid():
            account_form.save()
        
        return redirect('todo_app:task-list')
    
    context = {
        "page_title":"Create Items",
        "account_form":account_form,
    }
    
    return render(request, 'todo_app/task_create.html', context)

def task_update(request, update_id):
    account_update = Task.objects.get(id=update_id)
    
    account_form = TaskForm(request.POST or None, initial={"title":account_update.title}, instance=account_update)
    
    if request.method == 'POST':
        if account_form.is_valid():
            account_form.save()
        
        return redirect('todo_app:task-list')
    
    context = {
        "page_title":"Create Items",
        "account_form":account_form,
    }
    
    return render(request, 'todo_app/task_create.html', context)


def task_delete(request, delete_id):
    Task.objects.filter(id=delete_id).delete()
    return redirect("todo_app:task-list")