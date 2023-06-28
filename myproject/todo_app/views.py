from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

from .models import Task
from .forms import TaskForm, SignUpForm

def task_list(request):
    tasks = Task.objects.all()
    
    context = {
        "page_title":"Todo-list",
        "tasks":tasks,
    }
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('todo_app:task-list')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again!")
            return redirect('todo_app:task-list')
    else:
        return render(request, 'todo_app/task_list.html', context)

def task_create(request):
    account_form = TaskForm(request.POST or None)
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            if account_form.is_valid():
                account_form.save()
            
                messages.success(request, 'Task Added!')
                return redirect('todo_app:task-list')
    
        context = {
            "page_title":"Create Items",
            "account_form":account_form,
        }
        
        return render(request, 'todo_app/task_create.html', context)
    else:
        messages.success(request, 'You Must Be Logged In!')
        return redirect('todo_app:task-list')

def task_update(request, update_id):
    if request.user.is_authenticated:
        account_update = Task.objects.get(id=update_id)
        
        account_form = TaskForm(request.POST or None, initial={"title":account_update.title}, instance=account_update)
        
        if request.method == 'POST':
            if account_form.is_valid():
                account_form.save()
                
            messages.success(request, 'Task has been Updated!')
            return redirect('todo_app:task-list')
        
        context = {
            "page_title":"Create Items",
            "account_form":account_form,
        }
        
        return render(request, 'todo_app/task_create.html', context)
    else:
        messages.success(request, 'You Must Be Logged In!')
        return redirect('todo_app:task-list')


def task_delete(request, delete_id):
    Task.objects.filter(id=delete_id).delete()
    messages.success(request, 'Task Deleted Successfully')
    return redirect("todo_app:task-list")


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been Logged out!')
    return redirect('todo_app:task-list')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)    
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('todo_app:task-list')
    else:
        form = SignUpForm(request.POST)
        return render(request, 'todo_app/register.html', {'form': form})
    
    return render(request, 'todo_app/register.html', {'form': form}) 