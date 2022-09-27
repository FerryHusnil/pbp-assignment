from django.shortcuts import render, redirect
from todolist.forms import TaskForm
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, models as auth_models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/todolist/login")
def show_todolist(request):
    tasks = Task.objects.filter(user=request.user)
    username = request.user.username
    created = True if len(tasks) else False
    context = {"tasks": tasks, "created": created, "username": username}
    return render(request, "todolist.html", context)

@login_required(login_url="/todolist/login")
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = auth_models.User.objects.get(pk=request.user.id)
            task.save()
            print("sudah bikin task")
            print(Task.objects.all())
            messages.success(request, "Task Created Successfully")
            return redirect("todolist:show_todolist")
    else:
        form = TaskForm()
    context = {"form": form}
    return render(request, "create_task.html", context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            return redirect("todolist:login")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "register.html", context)

def login_user(request):
    if request.method == "POST":
        form  = UserCreationForm(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("todolist:show_todolist")
        else:
            messages.info(request, "Username or Password is incorrect")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("todolist:login")