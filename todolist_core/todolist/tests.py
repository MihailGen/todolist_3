from django.test import TestCase
from django.urls import reverse
from .models import Task


class TaskTestCase(TestCase):
    def test_create_task(self):
        response = self.client.get(reverse('task/add/', kwargs={'name': "Test Task", 'description': "Test Description"}))
        self.assertEqual(response.status_code, 200)
        task = Task.objects.all().first()
        self.assertEqual(task.name, "Test Task")
        self.assertEqual(task.description, "Test Description")
