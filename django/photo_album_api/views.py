from .models import Task
from .serializers import TaskSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

from rest_framework import generics
# from rest_framework_jwt.utils import jwt_decode_handler
from .utils import get_auth0_user_id_from_request
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCreator


# Lists and Creates entries of Task.
class TaskList(generics.ListCreateAPIView):
    """
    Lists and creates tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        auth0_user_id = get_auth0_user_id_from_request(self.request)
        # Set the user to the one in the token.
        serializer.save(created_by=auth0_user_id)

    def get_queryset(self):
        """
        This view should return a list of all Tasks
        for the currently authenticated user.
        """
        auth0_user_id = get_auth0_user_id_from_request(self.request)
        return Task.objects.filter(created_by=auth0_user_id)


# class TaskDetail(APIView):
#     """
#     Returns a single Task and allows updates and deletion of a Task.
#     """
#     def get_object(self, task_id):
#         try:
#             return Task.objects.get(pk=task_id)
#         except Task.DoesNotExist:
#             raise Http404
#
#     def get(self, request, task_id, format=None):
#         task = self.get_object(task_id)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#
#     def put(self, request, task_id, format=None):
#         task = self.get_object(task_id)
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, task_id, format=None):
#         task = self.get_object(task_id)
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single Task and allows updates and deletion of a Task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,IsCreator]
    lookup_url_kwarg = 'task_id'
