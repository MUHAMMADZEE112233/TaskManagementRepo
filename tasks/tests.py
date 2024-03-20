from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Task


class TaskAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        data = {
            'title': 'Test Task',
            'description': 'This is a test task.',
            'due_date': '2024-03-20T12:00:00Z',
            'priority': 'high',
        }
        response = self.client.post(reverse('task-list'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_get_task_list(self):
        Task.objects.create(title='Task 1', description='Description 1', due_date='2024-03-20T12:00:00Z',
                            priority='medium', creator=self.user)
        Task.objects.create(title='Task 2', description='Description 2', due_date='2024-03-21T12:00:00Z',
                            priority='high', creator=self.user)

        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    # Add more test cases for other CRUD operations


class CeleryTestCase(TestCase):
    def test_celery_task(self):
        # You can add tests for Celery tasks here
        pass
