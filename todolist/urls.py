# TODO: Implement Routings Here
from django.urls import path
from todolist.views import (
    show_todolist,
    create_task,
    update_task,
    delete_task,
    register,
    login_user,
    logout_user,
    show_todolist_json,
    create_task_ajax,
)

app_name = "todolist"

urlpatterns = [
    path("", show_todolist, name="show_todolist"),
    path("register", register, name="register"),
    path("login", login_user, name="login"),
    path("logout", logout_user, name="logout"),
    path("create-task", create_task, name="create_task"),
    path("update-task/<int:pk>", update_task, name="update_task"),
    path("delete-task/<int:pk>", delete_task, name="delete_task"),
    path("json", show_todolist_json, name="show_todolist_json"),
    path("add", create_task_ajax, name="create_task_json"),
]
