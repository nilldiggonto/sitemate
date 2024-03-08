from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tasks


class TaskCrudAPIView(APIView):
    def get(self, request):
        tasks = Tasks.objects.all()
        return Response({"tasks": tasks})

    def post(self, request):
        task = Tasks.objects.create(**request.data)
        return Response({"task": task})

    def put(self, request):
        task = Tasks.objects.get(id=request.data["id"])
        task.title = request.data["title"]
        task.description = request.data["description"]
        task.save()
        return Response({"task": task})

    def delete(self, request):
        task = Tasks.objects.get(id=request.data["id"])
        task.delete()
        return Response({"task": task})
