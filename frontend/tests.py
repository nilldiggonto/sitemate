from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from tasks.models import Tasks
from tasks.views import TaskSerializer

class TaskCrudAPIViewTest(APITestCase):

    def setUp(self):
        self.task_data = {"title": "Test Task", "description": "This is a test task."}
        self.task = Tasks.objects.create(title="Existing Task", description="This is an existing task.")

    def test_get_tasks(self):
        url = "/api/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["tasks"]), Tasks.objects.count())
        
    def test_create_task(self):
        url = "/api/"
        response = self.client.post(url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tasks.objects.count(), 2)
        self.assertEqual(Tasks.objects.last().title, self.task_data['title'])

    def test_update_task(self):
        url =  "/api/"
        updated_data = {"id": self.task.id, "title": "Updated Task", "description": "This task has been updated."}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Tasks.objects.get(id=self.task.id).title, updated_data['title'])

