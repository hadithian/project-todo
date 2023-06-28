from django.urls import path
from .views import task_list, task_create, task_delete, task_update, logout_user, register_user

app_name = "todo_app"

urlpatterns = [
    # re_path(r'^delete/(?P<delete_id>[0-9]+)$', task_delete, name='task-delete'),
    path('delete/<delete_id>', task_delete, name='task-delete'),
    path('update/<update_id>', task_update, name='task-update'),
    path('register/', register_user, name="register"),
    path('create/', task_create, name='task-create'),
    path('logout/', logout_user, name="logout"),
    path('', task_list, name='task-list'),
]