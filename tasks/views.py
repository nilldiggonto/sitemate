from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tasks
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"


class TaskCrudAPIView(APIView):
    def get(self, request):
        tasks = Tasks.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({"tasks": serializer.data})
    def post(self, request):
        #create new task
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"task": serializer.data})
        else:
            return Response(serializer.errors)

    def put(self, request):
        task = Tasks.objects.get(id=request.data["id"])
        
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"task": serializer.data})
        else:
            return Response(serializer.errors)

    def delete(self, request):
        task = Tasks.objects.get(id=request.data["id"])
        task.delete()
        return Response({"status": "success"})
