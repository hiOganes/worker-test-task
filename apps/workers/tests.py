from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Worker

class TestWorker(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser('admin', 'admin@test.com', 'pass')
        self.user = User.objects.create_user('user', 'user@test.com', 'pass')
        self.client.force_authenticate(self.admin)
        self.worker = Worker.objects.create(
            first_name='Test', last_name='User', email='test@test.com', position='Tester')

    def test_list_workers(self):
        response = self.client.get('/api/workers/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_worker(self):
        data = {'first_name': 'New', 'last_name': 'Worker', 'email': 'new@test.com', 'position': 'Dev'}
        response = self.client.post('/api/workers/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Worker.objects.count(), 2)

    def test_filter_is_active(self):
        response = self.client.get('/api/workers/?is_active=true')
        self.assertEqual(len(response.data['results']), 1)