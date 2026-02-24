from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer


class TaskListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        status_filter = request.query_params.get('status', None)
        tasks = Task.objects.filter(user=request.user)
        if status_filter:
            tasks = tasks.filter(status=status_filter)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_task(self, task_id, user):
        try:
            return Task.objects.get(id=task_id, user=user)
        except Task.DoesNotExist:
            return None

    def get(self, request, task_id):
        task = self.get_task(task_id, request.user)
        if task is None:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, task_id):
        task = self.get_task(task_id, request.user)
        if task is None:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        task = self.get_task(task_id, request.user)
        if task is None:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response({'message': 'Task deleted successfully.'}, status=status.HTTP_200_OK)


class TaskCompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id, user=request.user)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
        task.status = Task.STATUS_COMPLETE
        task.save()
        return Response({
            'message': 'Task marked as complete!',
            'task': TaskSerializer(task).data
        })


class TaskIncompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id, user=request.user)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
        task.status = Task.STATUS_PENDING
        task.save()
        return Response({
            'message': 'Task marked as incomplete!',
            'task': TaskSerializer(task).data
        })