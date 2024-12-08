from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Task, Comment, Tag


class TaskTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(name="Test Task", description="Test Description")
        self.tag = Tag.objects.create(name="Test Tag")
        User = get_user_model()
        self.user = User.objects.create_superuser(password='testuser', email="user@inbox.ru")
        self.client.login(password='testuser', email="user@inbox.ru")

    def test_view_task(self):  # Тест на просмотр задачи. Работает!
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.name, "Test Task")
        self.assertEqual(task.description, "Test Description")

    def test_edit_task(self):  # Тест на редактирование задачи. Работает!
        self.task.name = "Updated Title"
        self.task.save()
        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.name, "Updated Title")

    def test_delete_task(self):  # Тест на удаление задачи. Работает!
        task_id = self.task.id
        self.task.delete()
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task_id)

    def test_add_comment_to_task(self):  # Тест на добавление комментария к задаче. Работает!
        comment = Comment.objects.create(task=self.task, text="Test Comment")
        self.task.refresh_from_db()
        self.assertIn(comment, self.task.comments.all())

    def test_add_tags_to_task(self):  # Тест на добавление тэга к задаче. Работает!
        self.task.tags.add(self.tag)
        self.task.refresh_from_db()
        self.assertIn(self.tag, self.task.tags.all())

    def test_create_task(self):  # Тест на создание задачи. Работает!
        url = reverse('tasks:tasks-list')  # есть эндпоинт с именем 'tasks-list'
        print(url)
        data = dict(name='New Task', description='New Description', author="Mihail")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
