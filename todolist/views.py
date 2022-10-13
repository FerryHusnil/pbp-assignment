from django.shortcuts import render, redirect
from todolist.forms import TaskForm
from todolist.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, models as auth_models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers

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
            messages.success(request, "Task Created Successfully")
    else:
        form = TaskForm()
    context = {"form": form}
    return render(request, "create_task.html", context)

@login_required(login_url="/todolist/login")
def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_finished = not task.is_finished
    task.save()
    messages.success(request, "Status Update Successfully")
    return redirect("todolist:show_todolist")

@login_required(login_url="/todolist/login")
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    messages.success(request, "Task Deleted Successfully")
    return redirect("todolist:show_todolist")

@login_required(login_url="/todolist/login")
def show_todolist_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json");

@login_required(login_url="/todolist/login")
def create_task_ajax(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = auth_models.User.objects.get(pk=request.user.id)
            task.save()
            tasks = Task.objects.filter(user=request.user)
            return HttpResponse(serializers.serialize("json", tasks), content_type="application/json")
    else:
        form = TaskForm()
    context = {"form": form}
    return HttpResponse("only POST method allowed!");

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            return redirect("todolist:login")
        else:
            messages.error(request, form.errors)
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
            messages.error(request, "Username or Password is incorrect")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("todolist:login")