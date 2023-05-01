from django.urls import path
from .views import task_list, task_create, task_delete, task_update

urlpatterns = [
    # re_path(r'^delete/(?P<delete_id>[0-9]+)$', task_delete, name='task-delete'),
    path('delete/<delete_id>', task_delete, name='task-delete'),
    path('update/<update_id>', task_update, name='task-update'),
    path('create/', task_create, name='task-create'),
    path('', task_list, name='task-list'),
]

app_name = "todo_app"