from django.urls import path
from .views import TaskListCreateView, TaskDetailView, TaskCompleteView, TaskIncompleteView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:task_id>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:task_id>/complete/', TaskCompleteView.as_view(), name='task-complete'),
    path('tasks/<int:task_id>/incomplete/', TaskIncompleteView.as_view(), name='task-incomplete'),
]